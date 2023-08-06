from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from graphene import Field, InputObjectType
from djraphql.django_models import get_pk_fields_for_model
from graphql import Undefined


class PkInputType(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)
        pk_fields = registry.get_pk_fields_for_model(model_class)

        if len(pk_fields) == 1:
            model_field = registry.get_model_fields(model_class)[pk_fields[0].name]
            return registry.get_graphene_type_or_default(model_field)

        return type(
            "{}PKInputType".format(model_class.__name__),
            (InputObjectType,),
            {
                field.name: Field(
                    registry.schema.type_map[field.get_internal_type()],
                    required=True,
                    default_value=Undefined,
                )
                for field in pk_fields
            },
        )
