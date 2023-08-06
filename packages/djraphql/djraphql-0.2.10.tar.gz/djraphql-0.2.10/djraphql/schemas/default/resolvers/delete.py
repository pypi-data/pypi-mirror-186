from djraphql.django_models import get_pk_fields_for_model
from ..mappings import Types
from ...abstract_type_builder import CacheableTypeBuilder


class DeleteMutationResolverType(CacheableTypeBuilder):
    @staticmethod
    def make(registry, **kwargs):
        return build_delete_mutation_resolver(kwargs["model_class"], registry)


def build_delete_mutation_resolver(model_class, registry):
    entity_class = registry.get_entity_class(model_class)

    def delete_mutation_resolver(root, info, **args):

        if not entity_class.is_deletable_by_context(info.context):
            raise Exception("Invalid permissions.")

        # Search for the deleted item by queryset/PK to make sure it exists.
        assert "pk" in args, "Must pass pk for deletes."
        pk_fields = registry.get_pk_fields_for_model(model_class)

        if len(pk_fields) == 1:
            pk_search_kwargs = {pk_fields[0].name: args["pk"]}
        else:
            pk_search_kwargs = {field.name: args[field.name] for field in pk_fields}

        queryset = entity_class.get_queryset(info.context)
        instance = queryset.get(**pk_search_kwargs)

        success = False
        try:
            instance.delete()
            success = True
        except Exception as e:
            print("Something bad happened!", e)

        mutation_class = registry.get_or_create_type(
            Types.DELETE_MUTATION_TYPE, model_class=model_class
        )
        return mutation_class(success=success)

    return delete_mutation_resolver
