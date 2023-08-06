from graphene import (
    List,
)
from djraphql.access_permissions import READ
from ....abstract_type_builder import QueryRootTypeBuilder, CacheableTypeBuilder
from ...resolvers.aggregate import build_aggregate_resolver
from ...util.arguments import create_query_arguments
from ...mappings import AGGREGATE_FIELD_NAMES_TO_DJANGO_FUNCTIONS, Types


class AggregateQuery(CacheableTypeBuilder, QueryRootTypeBuilder):
    @classmethod
    def make(cls, registry, **kwargs):
        model_class = kwargs["model_class"]
        registry.get_or_create_type(
            Types.AGGREGATE_GROUP_BY_TYPE, model_class=model_class
        )

        entity_class = registry.get_entity_class(model_class)

        where_type = registry.get_or_create_type(
            Types.WHERE_CLAUSE_TYPE, model_class=model_class
        )
        order_by_type = registry.get_or_create_type(
            Types.ORDER_CLAUSE_TYPE, model_class=model_class
        )
        field = List(
            registry.get_or_create_type(
                Types.AGGREGATE_RESULT_TYPE, model_class=model_class
            ),
            args=create_query_arguments(where_type, order_by_type),
            description=cls.get_docs(model_class),
        )

        resolver = build_aggregate_resolver(
            model_class, registry, AGGREGATE_FIELD_NAMES_TO_DJANGO_FUNCTIONS
        )

        return (
            field,
            resolver,
        )

    @staticmethod
    def get_field_name(model_class):
        model_name = model_class.__name__
        return "{}{}Aggregate".format(model_name, "" if model_name[-1] == "s" else "s")

    @staticmethod
    def get_docs(model_class):
        model_name = model_class.__name__
        return """Given (optional) filtering arguments (where, orderBy,
            limit, offset), returns a list of {} objects.
        """.format(
            model_name
        )

    @staticmethod
    def get_required_access_permissions():
        return READ
