from ....abstract_type_builder import AbstractTypeBuilder
from graphene import String, ObjectType


class TagToPkType(AbstractTypeBuilder):
    @classmethod
    def cache_key(cls, type_key, **kwargs):
        return type_key

    @staticmethod
    def make(registry, **kwargs):
        return type(
            "TagPrimaryKeyMutationMap",
            (ObjectType,),
            {
                "tag": String(),
                "pk": String(),
                "type": String(),
            },
        )
