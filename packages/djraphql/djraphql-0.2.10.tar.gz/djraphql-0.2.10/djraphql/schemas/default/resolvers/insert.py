import logging
import traceback
from djraphql.django_models import get_field_by_name
from six import iteritems
from ..mappings import Types
from ...abstract_type_builder import CacheableTypeBuilder
from .update import perform_nested_list_update
from ..util import MutationAccumulator
from ..util.validation import perform_validation, FatalValidationError


class InsertMutationResolverType(CacheableTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        return build_insert_mutation_resolver(kwargs["model_class"], registry)


def build_insert_mutation_resolver(model_class, registry):
    entity_class = registry.get_entity_class(model_class)

    def insert_mutation_resolver(root, info, accumulator=None, **args):

        if not entity_class.is_creatable_by_context(info.context):
            raise Exception("Invalid permissions.")

        mutation_class = registry.get_or_create_type(
            Types.INSERT_MUTATION_TYPE, model_class=model_class
        )

        # Perform validation
        is_valid, validation_errors = perform_validation(
            entity_class, args["data"], model_class, root, info, is_insert=True
        )
        if validation_errors:
            accumulator.add_validation_error(validation_errors)

        if not is_valid:
            raise FatalValidationError()

        pre_save_rel_inputs, post_save_rel_inputs = _partition_relation_operations(
            args["data"], info.context, model_class, registry
        )

        args["data"].update(
            _call_any_get_for_inserts(model_class, info.context, registry)
        )

        entity_class.before_insert(args["data"], info.context)

        # In Graphene 3, Enum fields are represented as an instance with
        # name and value properties. We want to save the value property.
        instance = model_class(
            **{k: getattr(v, "value", v) for k, v in iteritems(args["data"])}
        )

        _handle_pre_save_relations(
            instance,
            pre_save_rel_inputs,
            registry,
            info,
            accumulator,
        )

        instance.save()

        # If the query passed a tag attribute, map it to the inserted object's PK.
        # But only on the root object; the nested list inserts are handled
        # via perform_nested_list_update below.
        if args.get("tag"):
            accumulator.add_pk_to_tag(
                instance.pk, args["tag"], instance.__class__.__name__
            )

        if root is None:
            accumulator.root_result = instance

        _handle_post_save_relations(
            instance,
            post_save_rel_inputs,
            registry,
            info,
            accumulator,
        )

        entity_class.after_insert(instance, info.context)

        return mutation_class(
            success=True,
            pks_to_tags=accumulator.pks_to_tags,
            validation_errors=accumulator.validation_errors,
            result=instance,
        )

    return insert_mutation_resolver


def _partition_relation_operations(data, context, model_class, registry):
    pre_save_rel_inputs = {}
    post_save_rel_inputs = {}
    data_keys = list(data.keys())
    for name in data_keys:
        field = get_field_by_name(model_class, name)
        if not field.is_relation:
            continue

        if field.concrete:
            name_with_id = "{}_id".format(field.name)
            if name_with_id in data and field.name in data:
                raise Exception(
                    'Pass one of "{}", "{}", not both.'.format(name_with_id, field.name)
                )
            elif name_with_id in data:
                # If the *_id is None, skip the following check, since None doesn't exist
                if data[name_with_id] is None:
                    continue

                # Otherwise, check that the filter_backend actually includes the referenced object
                related_entity_class = registry.get_entity_class(field.related_model)
                assert (
                    related_entity_class.get_queryset(context)
                    .filter(pk=data[name_with_id])
                    .exists()
                ), "{} matching query does not exist.".format(
                    field.related_model.__name__
                )
            else:
                pre_save_rel_inputs[field] = data.pop(field.name)
        else:
            post_save_rel_inputs[field] = data.pop(field.name)

    return pre_save_rel_inputs, post_save_rel_inputs


def _call_any_get_for_inserts(model_class, context, registry):
    result = {}
    # Update the data dict based on any caller-provided relation values
    for field in model_class._meta.get_fields():
        if not field.concrete or not field.is_relation:
            continue

        related_entity_class = registry.get_entity_class(field.related_model)
        if (
            related_entity_class is None
            or not related_entity_class.can_get_for_insert()
        ):
            continue

        result[field.name] = related_entity_class.get_for_insert(context)

    return result


def _handle_pre_save_relations(
    instance, pre_save_rel_inputs, registry, info, accumulator
):
    # Save the relations whose PK instance needs to be valid
    for field, value in iteritems(pre_save_rel_inputs):
        resolver = registry.get_or_create_type(
            Types.INSERT_MUTATION_RESOLVER, model_class=field.related_model
        )

        # It is possible that field is e.g. a concrete OneToOneField,
        # which means we must save the model before calling setattr,
        # because value will be a dict instead of a model.
        if isinstance(value, dict):
            accumulator.push_path_part(field.name)
            result = resolver(
                None,
                info,
                data=value,
                accumulator=accumulator,
            )
            accumulator.pop_path_part()
            setattr(instance, field.name, result.result)
        else:
            setattr(instance, field.name, value)


def _handle_post_save_relations(
    instance, post_save_rel_inputs, registry, info, accumulator
):
    # Save relations that need the instance's PK to be valid
    for field, value in iteritems(post_save_rel_inputs):
        resolver = registry.get_or_create_type(
            Types.INSERT_MUTATION_RESOLVER, model_class=field.related_model
        )
        if field.one_to_many:
            # value is a list when this is an insert* mutation,
            # and a dict when it's an update* mutation.
            # This is because for update* mutations, we allow the user
            # to specify an update stategy (merge or replace) which drives
            # whether each item in the list is created/updated/deleted.
            # But for an insert, all we need is the list, because we know
            # there are no nested items to update/delete.
            items = value
            update_strategy = "merge"
            if isinstance(value, dict):
                items = value["items"]
                update_strategy = value["update_strategy"]
            perform_nested_list_update(
                registry,
                info,
                instance,
                items,
                field,
                update_strategy,
                accumulator,
            )
        else:
            # It is possible that field is e.g. a concrete OneToOneField,
            # which means we must save the model before calling setattr,
            # because value will be a dict instead of a model.
            if isinstance(value, dict):
                value[field.field.name] = instance
                accumulator.push_path_part(field.name)
                result = resolver(
                    None,
                    info,
                    data=value,
                    accumulator=accumulator,
                )
                accumulator.pop_path_part()
                setattr(instance, field.name, result.result)
            else:
                setattr(instance, field.name, value)
