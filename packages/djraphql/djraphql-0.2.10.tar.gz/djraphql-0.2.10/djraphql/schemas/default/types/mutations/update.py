import logging
import traceback
from graphene import (
    String,
    List,
    Boolean,
    Field,
    Argument,
    Mutation,
)
from graphene.types.generic import GenericScalar
from graphene.utils.str_converters import to_snake_case
from djraphql.access_permissions import UPDATE
from ...util import MutationAccumulator
from ...util.validation import FatalValidationError
from ....abstract_type_builder import MutationRootTypeBuilder, CacheableTypeBuilder
from ...mappings import Types


class UpdateMutation(CacheableTypeBuilder, MutationRootTypeBuilder):
    @classmethod
    def make(cls, registry, **kwargs):
        model_class = kwargs["model_class"]
        entity_class = registry.get_entity_class(model_class)
        update_input_type = registry.get_or_create_type(
            Types.UPDATE_INPUT_TYPE, model_class=model_class
        )
        pk_input_type = registry.get_or_create_type(
            Types.PK_INPUT_TYPE, model_class=model_class
        )
        model_name = model_class.__name__
        mutation_arguments_type = type(
            "{}UpdateArguments".format(model_name),
            (object,),
            {
                "pk": Argument(pk_input_type, required=True),
                "tag": Argument(String),
                "data": Argument(update_input_type, required=True),
            },
        )

        return type(
            "Update{}".format(model_name),
            (Mutation,),
            {
                "Arguments": mutation_arguments_type,
                "success": Boolean(),
                "pks_to_tags": List(registry.get_or_create_type(Types.TAG_TO_PK_TYPE)),
                "validation_errors": GenericScalar(),
                "result": Field(
                    registry.lambda_from_registry(model_class, Types.BASIC_TYPE)
                ),
                "mutate": cls._catch_all_exceptions(registry, model_class),
                "__doc__": cls.get_docs(model_class),
            },
        )

    @staticmethod
    def _catch_all_exceptions(registry, model_class):
        resolver = registry.get_or_create_type(
            Types.UPDATE_MUTATION_RESOLVER, model_class=model_class
        )

        def _catch_all(*args, **kwargs):
            accumulator = MutationAccumulator()
            try:
                return resolver(*args, accumulator=accumulator, **kwargs)
            except FatalValidationError as ve:
                mutation_type = registry.get_or_create_type(
                    Types.UPDATE_MUTATION_TYPE, model_class=model_class
                )
                return mutation_type(
                    success=False,
                    pks_to_tags=accumulator.pks_to_tags,
                    validation_errors=accumulator.validation_errors,
                    result=accumulator.root_result,
                )
            except:
                logging.error(
                    "Error resolving object at path {}".format(accumulator.current_path)
                )
                traceback.print_exc()
                raise

        return _catch_all

    @staticmethod
    def get_field_name(model_class):
        return "update_{}".format(to_snake_case(model_class.__name__))

    @staticmethod
    def get_docs(model_class):
        return """Given a {} identifier (pk) and an object representing the
            changed values (data), updates an existing object in the database.
        """.format(
            model_class.__name__
        )

    @staticmethod
    def get_required_access_permissions():
        return UPDATE
