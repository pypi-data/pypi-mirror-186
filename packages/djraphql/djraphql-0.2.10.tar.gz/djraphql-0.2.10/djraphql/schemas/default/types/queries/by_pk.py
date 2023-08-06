from graphene import (
    Field,
    Argument,
)
from ....abstract_type_builder import QueryRootTypeBuilder, CacheableTypeBuilder
from ...resolvers.by_pk import build_by_pk_resolver
from ...mappings import Types
from djraphql.access_permissions import READ


class ByPkQuery(CacheableTypeBuilder, QueryRootTypeBuilder):
    @classmethod
    def make(cls, registry, **kwargs):
        model_class = kwargs["model_class"]
        basic_type = registry.get_or_create_type(
            Types.BASIC_TYPE, model_class=model_class
        )
        pk_input_type = registry.get_or_create_type(
            Types.PK_INPUT_TYPE, model_class=model_class
        )
        field = Field(
            basic_type,
            args={"pk": Argument(pk_input_type, required=True)},
            description=cls.get_docs(model_class),
        )

        resolver = build_by_pk_resolver(model_class, registry)

        return (
            field,
            resolver,
        )

    @staticmethod
    def get_field_name(model_class):
        model_name = model_class.__name__
        return "{}ByPk".format(model_name)

    @staticmethod
    def get_docs(model_class):
        model_name = model_class.__name__
        return "Given its primary-key, returns a single {} object.".format(model_name)

    @staticmethod
    def get_required_access_permissions():
        return READ
