from graphene import (
    List,
    NonNull,
)
from djraphql.access_permissions import READ
from ....abstract_type_builder import QueryRootTypeBuilder, CacheableTypeBuilder
from ...resolvers.list import build_list_resolver
from ...mappings import Types
from ...util.arguments import create_query_arguments


class ManyQuery(CacheableTypeBuilder, QueryRootTypeBuilder):
    @classmethod
    def make(cls, registry, **kwargs):
        model_class = kwargs["model_class"]
        where_type = registry.get_or_create_type(
            Types.WHERE_CLAUSE_TYPE, model_class=model_class
        )
        order_by_type = registry.get_or_create_type(
            Types.ORDER_CLAUSE_TYPE, model_class=model_class
        )

        field = List(
            NonNull(registry.lambda_from_registry(model_class, Types.BASIC_TYPE)),
            args=create_query_arguments(where_type, order_by_type),
            description=cls.get_docs(model_class),
        )

        resolver = build_list_resolver(model_class, registry)

        return (field, resolver)

    @staticmethod
    def get_field_name(model_class):
        model_name = model_class.__name__
        return "{}{}Many".format(model_name, "" if model_name[-1] == "s" else "s")

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
