from six import iteritems
from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from graphene import Field
from ...mappings import AGGREGATE_FIELD_NAMES_TO_DJANGO_FUNCTIONS, Types


class AggregateResultType(CacheableTypeBuilder, AbstractTypeBuilder):
    # @classmethod
    # def cache_key(cls, type_key, **kwargs):
    #     return type_key

    @staticmethod
    def make(registry, **kwargs):
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)
        attrs = {}
        for aggregate_field_name in AGGREGATE_FIELD_NAMES_TO_DJANGO_FUNCTIONS.keys():

            aggregate_basic_type = registry.get_or_create_type(
                Types.AGGREGATE_BASIC_TYPE,
                model_class=model_class,
                aggregate_field_name=aggregate_field_name,
            )

            attrs[aggregate_field_name] = Field(
                aggregate_basic_type, name=aggregate_field_name
            )
            attrs[
                "resolve_{}".format(aggregate_field_name)
            ] = resolver_for_aggregate_field(aggregate_field_name)

        group_by_type = registry.get_or_create_type(
            Types.AGGREGATE_GROUP_BY_TYPE, model_class=model_class
        )
        return type(
            "{}AggregateResult".format(model_class.__name__),
            (group_by_type,),
            attrs,
        )


class AggregateResultStruct:
    """Class is used for converting a dictionary to the equivalent object,
    which Graphene resolver expects. In aggregate (e.g. sum, max, etc.) queries,
    the results are dictionaries rather than model instances, so we must use this.
    """

    def __init__(self, **entries):
        for key, value in iteritems(entries):
            if isinstance(value, dict):
                self.__dict__[key] = AggregateResultStruct(**value)
            else:
                self.__dict__[key] = value


def resolver_for_aggregate_field(field_name):
    return lambda parent, info, **kwargs: AggregateResultStruct(**parent[field_name])
