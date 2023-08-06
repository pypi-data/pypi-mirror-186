from ....abstract_type_builder import AbstractTypeBuilder, CacheableTypeBuilder
from graphene import List, InputObjectType, Boolean, Field
from ...mappings import Types
from graphql import Undefined


class WhereClause(CacheableTypeBuilder, AbstractTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)

        # Build where predicate InputObjects to allow filtering in queries.
        where_input_type_attrs = {}
        for model_field in registry.get_model_fields(model_class).values():
            field = model_field.get_django_model_field()

            if field.many_to_one or field.one_to_many:
                where_input_type_attrs[field.name] = Field(
                    registry.lambda_from_registry(
                        field.related_model, Types.WHERE_CLAUSE_TYPE
                    ),
                    default_value=Undefined,
                )

            if not field.concrete:
                continue

            # TODO: Remove when support for many to many is implemented
            if field.many_to_many:
                continue

            # Convert names of ForeignKey/OneToOneFields from 'foo' to 'foo_id'
            field_name = field.name
            if field.many_to_one or field.one_to_one and field_name != "id":
                field_name = "{}_id".format(field_name)

            # The predicate input types for e.g. IntegerFields need different type
            # definitions than CharFields.
            # e.g., where: {id: _eq: 1} vs. where: {name: _eq: "hello"}
            # Examine the type of a model's field and build the appropriately typed
            # predicate input objects.
            type_name = field.get_internal_type()
            if field.choices:
                enum_type = registry.get_or_create_type(
                    Types.ENUM_TYPE,
                    model_class=model_class,
                    field=field,
                    choices=field.choices,
                )
                where_input_type_attrs[field_name] = type(
                    "WherePredicate{}".format(enum_type.__name__),
                    (InputObjectType,),
                    {
                        "_eq": enum_type(name="_eq", default_value=Undefined),
                        "_neq": enum_type(name="_neq", default_value=Undefined),
                        "_in": List(enum_type, name="_in", default_value=Undefined),
                        "_nin": List(enum_type, name="_nin", default_value=Undefined),
                        "_is_null": Boolean(name="_is_null", default_value=Undefined),
                    },
                )()
            else:
                graphene_type = registry.get_graphene_type_or_default(model_field)
                where_input_type_attrs[field_name] = registry.get_or_create_type(
                    Types.WHERE_PREDICATE_INPUT_TYPE,
                    graphene_type=graphene_type,
                )(default_value=Undefined)

        # These fields are always the same, they just recursively reference the
        # input type we're building.
        where_input_lambda = registry.lambda_from_registry(
            model_class, Types.WHERE_CLAUSE_TYPE
        )
        where_input_type_attrs["_and"] = List(
            where_input_lambda, name="_and", default_value=Undefined
        )
        where_input_type_attrs["_or"] = List(
            where_input_lambda, name="_or", default_value=Undefined
        )
        where_input_type_attrs["_not"] = Field(
            where_input_lambda, name="_not", default_value=Undefined
        )

        return type(
            "Where{}".format(model_class.__name__),
            (InputObjectType,),
            where_input_type_attrs,
        )
