import re
from six import string_types
from ....abstract_type_builder import AbstractTypeBuilder
from graphene import Enum


class EnumType(AbstractTypeBuilder):
    @classmethod
    def cache_key(cls, type_key, **kwargs):
        model_class = kwargs["model_class"]
        field = kwargs["field"]
        return "enum/{model_class}/{field}".format(
            model_class=model_class.__name__, field=field.name
        )

    @staticmethod
    def make(registry, **kwargs):
        model_class = kwargs["model_class"]
        field = kwargs["field"]
        choices = kwargs["choices"]
        entity_class = registry.get_entity_class(model_class)
        # Values can be strings or integers. We basically always want the attribute
        # keys to be a descriptive string. So we don't like to use integers
        enum_attrs = {}
        for value, pretty in choices:
            name = value if isinstance(value, string_types) else pretty
            enum_name = format_graphql_enum_name(name)
            enum_attrs[enum_name] = value

        camel_case = "".join([part.capitalize() for part in field.name.split("_")])
        return type(
            "{}{}Enum".format(model_class.__name__, camel_case),
            (Enum,),
            enum_attrs,
        )


def format_graphql_enum_name(enum_name):
    """GraphQL has rules for Enum names, e.g., cannot begin
    with double underscores or contain special characters.
    """
    formatted_name = enum_name.replace(" ", "_").replace("-", "_")
    formatted_name = re.sub(r"^_+", "_", formatted_name)
    formatted_name = re.sub(r"\W+", "", formatted_name)
    if not re.match(r"^[_a-zA-Z]", formatted_name):
        formatted_name = f"_{formatted_name}"
    return formatted_name
