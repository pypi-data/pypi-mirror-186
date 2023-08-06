from ....abstract_type_builder import AbstractTypeBuilder
from graphene import Boolean, InputObjectType, List
from graphql import Undefined


class WherePredicate(AbstractTypeBuilder):
    @classmethod
    def cache_key(cls, type_key, **kwargs):
        graphene_type = kwargs["graphene_type"]
        return graphene_type.__name__

    @staticmethod
    def make(registry, **kwargs):
        graphene_type = kwargs["graphene_type"]
        return type(
            "WherePredicate{}".format(graphene_type.__name__),
            (InputObjectType,),
            {
                "_eq": graphene_type(name="_eq", default_value=Undefined),
                "_neq": graphene_type(name="_neq", default_value=Undefined),
                "_gt": graphene_type(name="_gt", default_value=Undefined),
                "_gte": graphene_type(name="_gte", default_value=Undefined),
                "_lt": graphene_type(name="_lt", default_value=Undefined),
                "_lte": graphene_type(name="_lte", default_value=Undefined),
                "_in": List(graphene_type, name="_in", default_value=Undefined),
                "_nin": List(graphene_type, name="_nin", default_value=Undefined),
                "_is_null": Boolean(name="_is_null", default_value=Undefined),
                "_like": graphene_type(name="_like", default_value=Undefined),
                "_ilike": graphene_type(name="_ilike", default_value=Undefined),
            },
        )
