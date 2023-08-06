from .type_registry import TypeRegistry
from .schemas.default import DefaultSchema


class SchemaBuilder(object):
    """Entry point into the library. It is responsible for passing Entity classes
    to the TypeRegistry instance (via register_entity_classes) and building the
    root Query and Mutation types.

    Exposes QueryRoot and MutationRoot, which should then be passed to a
    graphene.Schema instance.
    """

    def __init__(self, schema=None):
        self.schema = schema or DefaultSchema()
        self.registry = TypeRegistry(self.schema)

    def register_entity_classes(self, *entity_classes):
        self.registry.register_entity_classes(*entity_classes)

    @property
    def QueryRoot(self):
        return self.schema.build_query_root_type(self.registry)

    @property
    def MutationRoot(self):
        return self.schema.build_mutation_root_type(self.registry)
