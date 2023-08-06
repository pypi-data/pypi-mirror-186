from djraphql.django_models import get_target_field
from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from ...mappings import Types
from graphene import Field, InputObjectType
from graphql import Undefined


class UpdateInputType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        """Generates a Graphene InputObjectType for the associated model.
        https://docs.graphene-python.org/en/latest/types/mutations/#inputfields-and-inputobjecttypes
        """
        input_class_attrs = {}
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)
        for model_field in registry.get_model_fields(model_class).values():
            field = model_field.get_django_model_field()

            # Don't allow updating the field is it is (part of) a PK,
            # or it's not included in the Entity.Meta.fields list,
            # or it is read-only.
            if (field.concrete and field.primary_key) or model_field.read_only:
                continue

            if (
                field.is_relation
                and not registry.get_entity_class(field.related_model).is_updatable()
            ):
                # We don't allow the related object to be updated, but we do allow
                # the reference to it to change, i.e., if a Foo has a FK to a Bar,
                # we allow foo.bar_id to be updated (given that a Foo is updatable).
                if field.concrete and not field.many_to_many:
                    # If the related model's entity overrides get_for_insert,
                    # that implies that this field is read-only.
                    related_entity = registry.get_entity_class(field.related_model)
                    if related_entity.can_get_for_insert():
                        continue

                    reverse_model_field = registry.get_model_fields(
                        field.related_model
                    )[get_target_field(field).name]

                    graphene_type = registry.get_graphene_type_or_default(
                        reverse_model_field
                    )
                    input_class_attrs["{}_id".format(field.name)] = graphene_type(
                        default_value=Undefined
                    )
                continue

            if field.one_to_many:
                list_update_input_type = registry.get_or_create_type(
                    Types.LIST_UPDATE_INPUT_TYPE, model_class=field.related_model
                )
                input_class_attrs[field.name] = Field(
                    list_update_input_type, default_value=Undefined
                )
            elif field.many_to_one or field.one_to_one:
                if field.concrete:
                    reverse_model_field = registry.get_model_fields(
                        field.related_model
                    )[get_target_field(field).name]

                    graphene_type = registry.get_graphene_type_or_default(
                        reverse_model_field
                    )
                    input_class_attrs["{}_id".format(field.name)] = graphene_type(
                        default_value=Undefined
                    )
                related_model = field.related_model
                input_class_attrs[field.name] = Field(
                    registry.lambda_from_registry(
                        related_model, Types.UPDATE_INPUT_TYPE
                    ),
                    default_value=Undefined,
                )
            elif field.many_to_many:
                pass
            elif field.choices:
                enum_type = registry.get_or_create_type(
                    Types.ENUM_TYPE,
                    model_class=model_class,
                    field=field,
                    choices=field.choices,
                )
                input_class_attrs[field.name] = Field(
                    enum_type, required=False, default_value=Undefined
                )
            else:
                input_class_attrs[field.name] = registry.get_graphene_type_or_default(
                    model_field
                )(default_value=Undefined)

        return type(
            "{}UpdateInput".format(model_class.__name__),
            (InputObjectType,),
            input_class_attrs,
        )
