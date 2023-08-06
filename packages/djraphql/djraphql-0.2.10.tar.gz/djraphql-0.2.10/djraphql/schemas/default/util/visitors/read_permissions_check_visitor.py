from .query_fields_visitor import QueryFieldsVisitor


class ReadPermissionsCheckVisitor(QueryFieldsVisitor):
    def hello_field(self, field, arguments, graphql_node=None):
        # If this is the "fooId" field (vs. the "foo" field), then
        # it's perfectly fine to read, because it's a scalar field
        # on a type that's already passed permissions-check successfully.
        # Thus, only check permissions if the GraphQL node has subselections.
        if graphql_node.selection_set:
            self._check_permissions(field.related_model)

    def hello_optimizable_tree(self, model_class, arguments):
        # Check permissions for reading the _root-level_ object.
        self._check_permissions(model_class)

    def _check_permissions(self, model_class):
        entity_class = self.registry.get_entity_class(model_class)
        if not entity_class.is_readable_by_context(self.info.context):
            raise Exception("Invalid permissions.")
