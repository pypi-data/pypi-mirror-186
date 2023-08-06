from six import iteritems
from graphql.language.visitor import Visitor
from graphene.utils.str_converters import to_snake_case
from djraphql.django_models import get_field_by_name
from graphql.execution.values import get_argument_values

IGNORED_FIELDS = set(["__typename"])


class QueryFieldsVisitor(Visitor):
    def __init__(self, registry, info):
        super().__init__()
        self.registry = registry
        self.type_lookup = registry._node_graphql_type_name_to_model_class
        self.info = info
        self.graphql_type_stack = [info.parent_type]
        self.model_class_stack = []

    def _get_terminal_gql_type(self, gql_type):
        while hasattr(gql_type, "of_type"):
            gql_type = gql_type.of_type
        return gql_type

    def enter_field(
        self,
        node,
        key,
        parent,
        path,
        ancestors,
    ):
        # Get the parent type of this field
        parent_gql_type = self.graphql_type_stack[-1]

        # Get a dictionary of the arguments associated with this field
        field_def = parent_gql_type.fields.get(node.name.value)

        # If the query contains GraphQL-spec-level fields like __typename,
        # field_def will be None here. We can ignore when this happens.
        if field_def is None and node.name.value in IGNORED_FIELDS:
            return

        arguments = get_argument_values(
            field_def,
            node,
            self.info.variable_values,
        )

        # Do we call hello_field?
        if parent_gql_type.name in self.type_lookup:
            model_class = self.type_lookup[parent_gql_type.name]["model_class"]
            field = try_get_related_field(model_class, node.name.value)
            if field:
                self.hello_field(field, arguments, graphql_node=node)
            else:
                # The associated model doesn't have a field with the same name.
                # The only possibility is that this field corresponds to a ComputedField.
                # If this ComputedField defined a depends_on list, we process it here.
                entity_class = self.type_lookup[parent_gql_type.name]["entity_class"]
                for computed_field in entity_class._get_computed_fields():
                    for dependency in computed_field.depends_on:
                        field = try_get_related_field(model_class, dependency)
                        if field:
                            self.hello_field(field, arguments, graphql_node=node)
                            self.goodbye_field(field)

        # If we're traversing a relationship (e.g., we're entering the
        # "artists" node within the "LabelsMany" query), we need to push the new
        # GraphQLTypeObject class and model class onto their respective stacks.
        if node.selection_set:
            maybe_nonterminal_gql_type = parent_gql_type.fields.get(
                node.name.value
            ).type
            next_gql_type = self._get_terminal_gql_type(maybe_nonterminal_gql_type)
            self.graphql_type_stack.append(next_gql_type)

            if next_gql_type.name in self.type_lookup:
                model_class = self.type_lookup[next_gql_type.name]["model_class"]
                if not self.model_class_stack:
                    self.hello_optimizable_tree(model_class, arguments)
                self.model_class_stack.append(model_class)

    def hello_optimizable_tree(self, model_class, arguments):
        pass

    def goodbye_optimizable_tree(self, model_class):
        pass

    def hello_field(self, field, arguments, graphql_node=None):
        pass

    def goodbye_field(self, field):
        pass

    def leave_field(
        self,
        node,
        key,
        parent,
        path,
        ancestors,
    ):
        # If we're traversing a relationship, e.g. we're leaving the "artists" node
        # within the "LabelsMany" query, we need to pop our GraphQLType stack
        # and _possibly_ our model stack.
        if node.selection_set:
            self.graphql_type_stack.pop()
            if len(self.model_class_stack) == 1:
                # We're about to pop the last item from our model stack,
                # that means we're exiting the optimizable tree, so call that handler.
                self.goodbye_optimizable_tree(self.model_class_stack.pop())
            elif self.model_class_stack:
                # There will still be items left in our model stack, we're still
                # within the optimizable tree. In this case, call goodbye_field.
                self.model_class_stack.pop()
                field = try_get_related_field(
                    self.model_class_stack[-1], node.name.value
                )
                if field:
                    self.goodbye_field(field)
            return

        # We are not traversing a relationship. If we have a non-empty
        # model stack, we need to call the goodbye_field handler.
        if self.model_class_stack:
            field = try_get_related_field(self.model_class_stack[-1], node.name.value)
            if field:
                self.goodbye_field(field)


def try_get_related_field(model_class, selection_name):
    names_to_try = [
        # First try just getting the field from the model via the selection's name
        # in the GraphQL query. This is usually a camelCased name. We do this in
        # case the user has defined their model's related_name(s)
        # in camelCase instead of snake_case
        selection_name,
        # Next, attempt to get the field by snake_casing the name of the selection.
        to_snake_case(selection_name),
    ]

    for name in names_to_try:
        try:
            return get_field_by_name(model_class, name)
        except:  # FieldDoesNotExist
            pass
