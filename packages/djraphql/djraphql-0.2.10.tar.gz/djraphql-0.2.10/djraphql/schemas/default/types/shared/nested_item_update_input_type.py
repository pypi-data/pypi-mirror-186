from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from ...mappings import Types
from graphene import Field, InputObjectType, String
from graphql import Undefined


class NestedItemUpdateInputType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        input_class_attrs = {}
        model_class = kwargs["model_class"]
        pk_required = not registry.get_entity_class(model_class).is_creatable()

        return type(
            "NestedItemUpdate{}".format(model_class.__name__),
            (InputObjectType,),
            {
                "pk": Field(
                    registry.get_or_create_type(
                        Types.PK_INPUT_TYPE, model_class=model_class
                    ),
                    required=pk_required,
                    default_value=Undefined,
                ),
                "tag": Field(String, default_value=Undefined),
                "data": Field(
                    registry.lambda_from_registry(model_class, Types.UPDATE_INPUT_TYPE),
                    required=True,
                    default_value=Undefined,
                ),
            },
        )
