from graphene import ObjectType
from ..abstract_type_builder import AbstractSchema
from .types.queries.by_pk import ByPkQuery
from .types.queries.aggregate import AggregateQuery
from .types.queries.many import ManyQuery
from .types.mutations.delete import DeleteMutation
from .types.mutations.insert import InsertMutation
from .types.mutations.update import UpdateMutation
from .types.shared.where_clause import WhereClause
from .types.shared.order_clause import OrderClause
from .types.shared.where_predicate import WherePredicate
from .types.shared.basic import BasicType
from .types.shared.enum import EnumType
from .types.shared.pk_input import PkInputType
from .types.shared.aggregate_result import AggregateResultType
from .types.shared.aggregate_basic import AggregateBasicType
from .types.shared.aggregate_group_by import AggregateGroupByType
from .types.shared.insert_input_type import InsertInputType
from .types.shared.update_input_type import UpdateInputType
from .types.shared.list_update_input_type import ListUpdateInputType
from .types.shared.nested_item_update_input_type import (
    NestedItemUpdateInputType,
)
from .types.shared.nested_item_insert_input_type import (
    NestedItemInsertInputType,
)
from .types.shared.tag_to_pk import TagToPkType
from .resolvers.insert import InsertMutationResolverType
from .resolvers.update import UpdateMutationResolverType
from .resolvers.delete import DeleteMutationResolverType
from .mappings import Types, DJANGO_TYPE_NAMES_TO_GRAPHENE_TYPES


class DefaultSchema(AbstractSchema):

    DEFAULT_QUERIES = (ByPkQuery, ManyQuery, AggregateQuery)
    DEFAULT_MUTATIONS = (InsertMutation, UpdateMutation, DeleteMutation)

    BUILDER_MAP = {
        Types.AGGREGATE_RESULT_TYPE: AggregateResultType,
        Types.AGGREGATE_BASIC_TYPE: AggregateBasicType,
        Types.AGGREGATE_GROUP_BY_TYPE: AggregateGroupByType,
        Types.AGGREGATE_QUERY_TYPE: AggregateQuery,
        Types.BASIC_TYPE: BasicType,
        Types.BY_PK_QUERY_TYPE: ByPkQuery,
        Types.DELETE_MUTATION_RESOLVER: DeleteMutationResolverType,
        Types.DELETE_MUTATION_TYPE: DeleteMutation,
        Types.ENUM_TYPE: EnumType,
        Types.INSERT_INPUT_TYPE: InsertInputType,
        Types.INSERT_MUTATION_RESOLVER: InsertMutationResolverType,
        Types.INSERT_MUTATION_TYPE: InsertMutation,
        Types.LIST_UPDATE_INPUT_TYPE: ListUpdateInputType,
        Types.MANY_QUERY_TYPE: ManyQuery,
        Types.NESTED_ITEM_UPDATE_TYPE: NestedItemUpdateInputType,
        Types.NESTED_ITEM_INSERT_TYPE: NestedItemInsertInputType,
        Types.ORDER_CLAUSE_TYPE: OrderClause,
        Types.PK_INPUT_TYPE: PkInputType,
        Types.TAG_TO_PK_TYPE: TagToPkType,
        Types.UPDATE_INPUT_TYPE: UpdateInputType,
        Types.UPDATE_MUTATION_TYPE: UpdateMutation,
        Types.UPDATE_MUTATION_RESOLVER: UpdateMutationResolverType,
        Types.WHERE_CLAUSE_TYPE: WhereClause,
        Types.WHERE_PREDICATE_INPUT_TYPE: WherePredicate,
    }

    def __init__(self, field_type_map_overrides=None):
        super(DefaultSchema, self).__init__()
        self._field_type_map_overrides = field_type_map_overrides

    @property
    def FIELD_TYPE_MAP(self):
        if not hasattr(self, "_field_type_map"):
            self._field_type_map = DJANGO_TYPE_NAMES_TO_GRAPHENE_TYPES.copy()
            self._field_type_map.update(self._field_type_map_overrides or {})

        return self._field_type_map

    def get_node_name_for_model(self, model_class):
        return model_class.__name__

    def build_query_root_type(self, registry):
        return self._build_root_type(
            registry, "QueryRoot", "query_classes", self.DEFAULT_QUERIES
        )

    def build_mutation_root_type(self, registry):
        return self._build_root_type(
            registry,
            "MutationRoot",
            "mutation_classes",
            self.DEFAULT_MUTATIONS,
        )

    def _build_root_type(
        self, registry, type_name, root_type_classes_key, root_type_classes_default
    ):
        """Used to build a root type, e.g. Query or Mutation. Iterates through
        the Entity class's root-type field as specified by root_type_classes_key
        and checks whether the access_permissions field allows the root type to
        exist (i.e. we don't create an insertFoo mutation for a read-only FooEntity)
        and if so, updates the result with the fields returned by the get_root_fields
        method of the root-type.

        Args:
            type_name: str. One of "MutationRoot" or "QueryRoot"
            root_type_classes_key: str: One of "mutation_classes" or "query_classes"
            root_type_classes_default: A list root type classes, which will come from
                djraphql.schemas.default.types.queries|mutations.
        Returns:
            Graphene type representing the root type for GraphQL queries or mutations.
        """

        attrs = {}
        for model_class in registry.get_available_model_classes():
            entity_class = registry.get_entity_class(model_class)

            # Add the query/mutation fields to the root type being built.
            root_types = getattr(entity_class, root_type_classes_key)

            # If the Entity class does not override query_classes or mutation_classes,
            # then we use the DEFAULT_QUERIES or DEFAULT_MUTATIONS from the schema.
            if root_types is None:
                root_types = root_type_classes_default

            for root_type in root_types:
                # Check permissions before we add the query/mutation type to the root.
                # E.g. insertFoo requires CREATE permission, so we only want to
                # define the insertFoo operation if the FooEntity has a Create in
                # its access_permissions field.
                root_type_permissions = root_type.get_required_access_permissions()
                if not entity_class.allows_permissions(root_type_permissions):
                    continue

                attrs.update(root_type.get_root_fields(registry, model_class))

        return type(type_name, (ObjectType,), attrs)
