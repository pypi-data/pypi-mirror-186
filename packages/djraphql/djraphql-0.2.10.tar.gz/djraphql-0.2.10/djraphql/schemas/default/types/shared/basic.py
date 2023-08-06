from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from ...mappings import Types
from graphene import Field, List, ObjectType
from ...resolvers.field import build_field_resolver
from ...resolvers.list import build_list_resolver
from ...util.arguments import create_query_arguments
from .....django_models import get_field_by_name, get_target_field


class BasicType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        basic_type_attrs = {}
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)

        for model_field in registry.get_model_fields(model_class).values():
            field = model_field.get_django_model_field()

            if (
                field.is_relation
                and not registry.get_entity_class(field.related_model).is_readable()
            ):
                continue

            # Handle concrete, non-relation fields
            if not field.is_relation:
                graphene_type = registry.get_graphene_type_or_default(model_field)

                # Enum/choice fields are handled as special cases
                if field.choices:
                    graphene_type = registry.get_or_create_type(
                        Types.ENUM_TYPE,
                        model_class=model_class,
                        field=field,
                        choices=field.choices,
                    )

                basic_type_attrs[field.name] = Field(
                    graphene_type, required=not field.null
                )
                continue

            # Handle *-to-one relational fields (which may be concrete)
            if field.many_to_one or field.one_to_one:
                basic_type_attrs[field.name] = Field(
                    registry.lambda_from_registry(
                        field.related_model, Types.BASIC_TYPE
                    ),
                    required=not field.null if field.concrete else False,
                )
                basic_type_attrs[
                    "resolve_{}".format(field.name)
                ] = build_field_resolver(field, registry)

                # If this relational field is concrete, also add a *_id property
                # to the GraphQL type. I.e., a foo that has a bar will have both
                # barId and bar { id } available on the type.
                if field.concrete:
                    reverse_model_field = registry.get_model_fields(
                        field.related_model
                    )[get_target_field(field).name]

                    graphene_type = registry.get_graphene_type_or_default(
                        reverse_model_field
                    )
                    basic_type_attrs["{}_id".format(field.name)] = graphene_type(
                        required=not field.null
                    )
                continue

            # Handle *-to-many relational fields (which are never concrete)
            if field.one_to_many or field.many_to_many:
                where_type = registry.get_or_create_type(
                    Types.WHERE_CLAUSE_TYPE, model_class=field.related_model
                )
                order_by_type = registry.get_or_create_type(
                    Types.ORDER_CLAUSE_TYPE, model_class=field.related_model
                )
                basic_type_attrs[field.name] = List(
                    registry.lambda_from_registry(
                        field.related_model, Types.BASIC_TYPE
                    ),
                    args=create_query_arguments(where_type, order_by_type),
                )

                basic_type_attrs["resolve_{}".format(field.name)] = build_list_resolver(
                    field.related_model,
                    registry,
                    related_name=(
                        field.name if field.many_to_many else field.related_name
                    ),
                )
                continue

        # Add computed (property) fields defined on the Entity class
        for computed_field in entity_class._get_computed_fields():
            basic_type_attrs[computed_field.name] = computed_field.graphene_type()
            basic_type_attrs[
                f"resolve_{computed_field.name}"
            ] = build_computed_field_resolver(entity_class, computed_field)

        return type(
            model_class.__name__,
            (ObjectType,),
            basic_type_attrs,
        )


def build_computed_field_resolver(entity_class, computed_field):
    resolver = computed_field.get_resolver(entity_class)

    def resolve(parent, info, **kwargs):
        return resolver(info.context, parent, **kwargs)

    return resolve
