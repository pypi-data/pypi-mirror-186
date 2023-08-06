import logging
import traceback
from djraphql.django_models import get_pk_fields_for_model, get_field_by_name
from .by_pk import build_by_pk_resolver
from six import iteritems
from ..mappings import Types
from ...abstract_type_builder import CacheableTypeBuilder
from ..util.validation import perform_validation, FatalValidationError
from ..util import MutationAccumulator


class UpdateMutationResolverType(CacheableTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        return build_update_mutation_resolver(kwargs["model_class"], registry)


def build_update_mutation_resolver(model_class, registry):
    entity_class = registry.get_entity_class(model_class)

    def update_mutation_resolver(root, info, accumulator=None, **args):

        if not entity_class.is_updatable_by_context(info.context):
            raise Exception("Invalid permissions.")

        mutation_class = registry.get_or_create_type(
            Types.UPDATE_MUTATION_TYPE, model_class=model_class
        )

        # Perform validation
        is_valid, validation_errors = perform_validation(
            entity_class, args["data"], model_class, root, info
        )

        if validation_errors:
            accumulator.add_validation_error(validation_errors)

        if not is_valid:
            raise FatalValidationError()

        instance = _get_object_to_update(
            args, model_class, entity_class, info, registry
        )

        pre_rel_inputs, post_rel_inputs = _partition_relation_operations(
            args["data"], model_class, instance, info, registry
        )

        _handle_pre_save_relations(
            pre_rel_inputs, instance, accumulator, info, registry
        )

        # Set the updated values for our instance.
        for key, value in iteritems(args["data"]):
            # In Graphene 3, Enum fields are represented as an instance with
            # name and value properties. We want to save the value property.
            extracted_value = getattr(value, "value", value)
            setattr(instance, key, extracted_value)

        instance.save()

        if root is None:
            accumulator.root_result = instance

        _handle_post_save_relations(
            post_rel_inputs, instance, accumulator, info, registry
        )

        # TODO: this probably should be taken care of in the mutation class.
        resolved_result = instance
        if root is None:
            by_pk_resolver = build_by_pk_resolver(
                model_class,
                registry,
            )
            resolved_result = by_pk_resolver(None, info, pk=instance.pk)

        return mutation_class(
            success=True,
            pks_to_tags=accumulator.pks_to_tags,
            validation_errors=accumulator.validation_errors,
            result=resolved_result,
        )

    return update_mutation_resolver


def _handle_post_save_relations(post_rel_inputs, instance, accumulator, info, registry):
    # Iterate through each relational/nested input we found earlier
    # and call the resolver for each one. If the nested relationship is
    # a list, then call the resolver for each item in the list.
    for field, value in iteritems(post_rel_inputs):
        if field.one_to_many:
            perform_nested_list_update(
                registry,
                info,
                instance,
                value["items"],
                field,
                value["update_strategy"],
                accumulator,
            )
        elif field.one_to_one:
            updated_child = getattr(instance, field.name, None)
            if updated_child and value is None:
                if not registry.get_entity_class(field.related_model).is_deletable():
                    raise Exception(
                        "Setting {} to null is a DELETE operation, and {} is not deletable according to its schema permissions.".format(
                            field.name, field.related_model.__name__
                        )
                    )
                resolver = registry.get_or_create_type(
                    Types.DELETE_MUTATION_RESOLVER,
                    model_class=field.related_model,
                )
                resolver(instance, info, pk=updated_child.pk)
            elif updated_child:
                resolver = registry.get_or_create_type(
                    Types.UPDATE_MUTATION_RESOLVER, model_class=field.related_model
                )
                resolver(
                    instance,
                    info,
                    pk=updated_child.pk,
                    data=value,
                    accumulator=accumulator,
                )
            elif value is None:
                # Here we know updated_child is None, and since value is
                # also None, there's actually nothing to do, so just skip.
                continue
            else:
                value[field.field.name] = instance
                resolver = registry.get_or_create_type(
                    Types.INSERT_MUTATION_RESOLVER, model_class=field.related_model
                )
                resolver(instance, info, data=value, accumulator=accumulator)
        else:
            raise Exception("Not implemented")


def _handle_pre_save_relations(pre_rel_inputs, instance, accumulator, info, registry):
    # If the one-to-one relation object already exists, we call
    # update resolver, else call the insert resolver.
    for field, value in iteritems(pre_rel_inputs):
        relation_instance = getattr(instance, field.name, None)
        if relation_instance:
            resolver = registry.get_or_create_type(
                Types.UPDATE_MUTATION_RESOLVER,
                model_class=field.related_model,
            )
            resolver(
                instance,
                info,
                pk=relation_instance.pk,
                data=value,
                accumulator=accumulator,
            )
        else:
            resolver = registry.get_or_create_type(
                Types.INSERT_MUTATION_RESOLVER,
                model_class=field.related_model,
            )
            result = resolver(
                instance,
                info,
                data=value,
                accumulator=accumulator,
            )

            # Set the field on the instance to the inserted result
            setattr(instance, field.name, result.result)


def _partition_relation_operations(data, model_class, instance, info, registry):
    pre_save_rel_inputs = {}
    post_save_rel_inputs = {}

    data_keys = list(data.keys())
    for name in data_keys:
        field = get_field_by_name(model_class, name)
        if not field.is_relation:
            continue

        if not field.concrete:
            # Remove relational inputs from the dictionary passed to the model,
            # and handle them separately by calling a resolver for each one below.
            post_save_rel_inputs[field] = data.pop(field.name)
        else:
            # If the field is 1-1 and concrete, but is passed in as a dictionary,
            # we must save it before assigning it to the dict passed to the model.
            if isinstance(data[name], dict):
                value = data.pop(name)
                pre_save_rel_inputs[field] = value
            else:
                name_with_id = "{}_id".format(field.name)
                if name_with_id in data and field.name in data:
                    raise Exception(
                        'Pass one of "{}", "{}", not both.'.format(
                            name_with_id, field.name
                        )
                    )
                elif name_with_id in data and data[name_with_id] is not None:
                    # Check that the filter_backend actually includes the referenced object.
                    assert (
                        registry.get_entity_class(field.related_model)
                        .get_queryset(info.context)
                        .filter(pk=data[name_with_id])
                        .exists()
                    ), "{} matching query does not exist.".format(
                        field.related_model.__name__
                    )

    return pre_save_rel_inputs, post_save_rel_inputs


def _get_object_to_update(data, model_class, entity_class, info, registry):
    # Search for the updated item by queryset/PK to make sure it exists.
    assert "pk" in data, "Must pass pk for updates."
    pk_fields = registry.get_pk_fields_for_model(model_class)
    if len(pk_fields) == 1:
        pk_search_kwargs = {pk_fields[0].name: data["pk"]}
    else:
        pk_search_kwargs = {field.name: data[field.name] for field in pk_fields}

    # Fetch the instance by just its PK first, without any filtering from the
    # Entity class's filter_backend, which can result in multiple (duplicate)
    # objects being returned, whereas we always only want just one instance.
    # This was previously causing unnecessary errors during resolution, e.g.
    # ".get() returned more than 1, it returned 2!"
    instance = model_class.objects.get(**pk_search_kwargs)

    # Then, do the check against the Entity class's filter_backend.
    # This ensures we can only update/reference objects our filter_backend
    # has access to. Multiple (duplicate) objects can be returned by this query,
    # we only care that something is returned.
    assert (
        entity_class.get_queryset(info.context).filter(pk=instance.pk).exists()
    ), "{} matching query does not exist.".format(model_class.__name__)

    return instance


def perform_nested_list_update(
    registry,
    info,
    instance,
    items,
    field,
    update_strategy,
    accumulator,
):
    update_resolver = registry.get_or_create_type(
        Types.UPDATE_MUTATION_RESOLVER, model_class=field.related_model
    )

    insert_resolver = registry.get_or_create_type(
        Types.INSERT_MUTATION_RESOLVER, model_class=field.related_model
    )

    updated_or_inserted_pks = []
    accumulator.push_path_part(field.name)
    for i, item in enumerate(items):
        accumulator.push_path_part(i)
        if "pk" in item:
            updated_or_inserted_pks.append(item["pk"])
            update_resolver(instance, info, accumulator=accumulator, **item)
        else:
            item["data"][field.field.name] = instance
            result = insert_resolver(instance, info, accumulator=accumulator, **item)
            updated_or_inserted_pks.append(result.result.pk)
        accumulator.pop_path_part()
    accumulator.pop_path_part()

    # If our update strategy is anything other than 'replace', we're done.
    # Otherwise, we must delete any already-existing objects that do not
    # have a corresponding item in the mutation's nested list.
    if update_strategy != "replace":
        return

    items_to_delete = list(
        getattr(instance, field.name).exclude(pk__in=updated_or_inserted_pks)
    )

    # Check permissions and confirm that these objects are actually deletable
    if (
        items_to_delete
        and not registry.get_entity_class(field.related_model).is_deletable()
    ):
        raise Exception(
            "Nested update with UpdateStrategy 'replace' has resulted in a DELETE operation, but {} is not deletable according to its schema permissions.".format(
                field.name, field.related_model.__name__
            )
        )

    delete_resolver = registry.get_or_create_type(
        Types.DELETE_MUTATION_RESOLVER, model_class=field.related_model
    )

    for item in items_to_delete:
        delete_resolver(instance, info, pk=item.pk)
