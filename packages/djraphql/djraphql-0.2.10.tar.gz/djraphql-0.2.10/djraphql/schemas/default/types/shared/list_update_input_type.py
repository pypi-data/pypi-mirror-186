from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from ...mappings import Types
from graphene import Enum, InputObjectType, List


class UpdateStrategy(Enum):
    merge = "merge"
    replace = "replace"


class ListUpdateInputType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        """Generates a Graphene InputObjectType for the associated model.
        https://docs.graphene-python.org/en/latest/types/mutations/#inputfields-and-inputobjecttypes
        """
        input_class_attrs = {}
        model_class = kwargs["model_class"]
        nested_item_update_input_type = registry.get_or_create_type(
            Types.NESTED_ITEM_UPDATE_TYPE, model_class=model_class
        )
        return type(
            "{}ListUpdateInput".format(model_class.__name__),
            (InputObjectType,),
            {
                "update_strategy": UpdateStrategy(required=True, default_value="merge"),
                "items": List(nested_item_update_input_type, required=True),
            },
        )
