from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from ...mappings import Types
from graphene import Field, ObjectType
from ...resolvers.group_by import build_group_by_resolver


class AggregateGroupByType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        attrs = {}
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)

        for model_field in registry.get_model_fields(model_class).values():
            field = model_field.get_django_model_field()

            if field.concrete and not field.is_relation:
                attrs[field.name] = registry.get_graphene_type_or_default(model_field)()
            elif field.concrete and field.is_relation:
                # Example: model_class is Album, and field is Album.artist
                attrs[field.name] = Field(
                    registry.lambda_from_registry(
                        field.related_model, Types.AGGREGATE_GROUP_BY_TYPE
                    )
                )
                attrs["resolve_{}".format(field.name)] = build_group_by_resolver(field)
            elif field.one_to_many:
                attrs[field.name] = Field(
                    registry.lambda_from_registry(
                        field.related_model, Types.AGGREGATE_GROUP_BY_TYPE
                    )
                )
                attrs["resolve_{}".format(field.name)] = build_group_by_resolver(field)

        return type(
            "{}GroupBy".format(model_class.__name__),
            (ObjectType,),
            attrs,
        )
