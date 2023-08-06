from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from graphene import Field, ObjectType
from ...resolvers.field import build_field_resolver
from ...mappings import Types


specialized_field_types_by_aggregate_field_name = {
    "_count": "IntegerField",
    "_avg": "FloatField",
}


class AggregateBasicType(CacheableTypeBuilder, AbstractTypeBuilder):
    @classmethod
    def cache_key(cls, type_key, **kwargs):
        model_class = kwargs["model_class"]
        aggregate_field_name = kwargs["aggregate_field_name"]
        if (
            aggregate_field_name
            in specialized_field_types_by_aggregate_field_name.keys()
        ):
            return "{}/{}{}".format(
                model_class.__name__, type_key, aggregate_field_name
            )

        return "{}/{}".format(model_class.__name__, type_key)

    @staticmethod
    def make(registry, **kwargs):
        model_class = kwargs["model_class"]
        aggregate_field_name = kwargs["aggregate_field_name"]
        type_key = kwargs["type_key"]
        entity_class = registry.get_entity_class(model_class)
        aggregate_basic_type_attrs = {}

        # Edge-case for e.g. _count, where we need to use a different type
        # than the source column. So if we count(name), we want the result
        # to be an Int, not a String.
        registry_key = type_key
        if aggregate_field_name in specialized_field_types_by_aggregate_field_name:
            registry_key = "{}{}".format(registry_key, aggregate_field_name)

        for model_field in registry.get_model_fields(model_class).values():
            field = model_field.get_django_model_field()

            field_name = field.name
            if field.concrete and not field.is_relation:
                type_name = (
                    specialized_field_types_by_aggregate_field_name.get(
                        aggregate_field_name
                    )
                    or field.get_internal_type()
                )
                graphene_type = registry.schema.FIELD_TYPE_MAP[type_name]
                arg = registry.get_or_create_type(
                    Types.WHERE_PREDICATE_INPUT_TYPE,
                    graphene_type=graphene_type,
                )
                aggregate_basic_type_attrs[field_name] = graphene_type(
                    args={"having": arg()}
                )
            elif field.concrete and (field.many_to_one or field.one_to_one):
                aggregate_basic_type_attrs[field_name] = Field(
                    registry.lambda_from_registry(field.related_model, registry_key),
                    required=not field.null,
                )
                aggregate_basic_type_attrs[
                    "resolve_{}".format(field_name)
                ] = build_field_resolver(field, registry)
                type_name = (
                    specialized_field_types_by_aggregate_field_name.get(
                        aggregate_field_name
                    )
                    or field.get_internal_type()
                )
                graphene_type = registry.schema.FIELD_TYPE_MAP[type_name]
                aggregate_basic_type_attrs["{}_id".format(field_name)] = graphene_type(
                    required=not field.null
                )
            elif field.many_to_one or field.one_to_one:
                aggregate_basic_type_attrs[field_name] = Field(
                    registry.lambda_from_registry(field.related_model, registry_key),
                    required=not field.field.null,
                )
                aggregate_basic_type_attrs[
                    "resolve_{}".format(field_name)
                ] = build_field_resolver(field, registry)
                type_name = field.field.get_internal_type()
                graphene_type = registry.schema.FIELD_TYPE_MAP[type_name]
                aggregate_basic_type_attrs["{}_id".format(field_name)] = graphene_type(
                    required=not field.field.null
                )
            elif field.one_to_many or field.many_to_many:
                aggregate_basic_type_attrs[field_name] = Field(
                    registry.lambda_from_registry(field.related_model, registry_key),
                )
                aggregate_basic_type_attrs[
                    "resolve_{}".format(field_name)
                ] = build_field_resolver(field, registry)

        result = type(
            "{}{}{}".format(
                model_class.__name__, "Aggregate", aggregate_field_name or ""
            ),
            (ObjectType,),
            aggregate_basic_type_attrs,
        )

        return result
