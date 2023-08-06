from .query_fields_visitor import QueryFieldsVisitor
from ..queryset_optimizer import QuerysetOptimizer


class NodeInfo(object):
    def __init__(self, key, model_class, field_names, arguments=None, alias=None):
        self.key = key
        self.model_class = model_class
        self.field_names = field_names
        self.select_related_keys = []
        self.arguments = arguments
        self.alias = alias
        self.alias_path = None


class QuerysetOptimizationVisitor(QueryFieldsVisitor):
    """Problem: We allow a caller to specify e.g. a 'where' filter in a
    GraphQL query at any level of the query: root, child, grandchild, ...
    When there is a 'where' at a non-root level, we will fall victim
    to the N+1 problem and issue as many queries as there are children.
    Solution: To avoid N+1 queries, we traverse the GraphQL query's AST
    to find opportunities to use Django's Prefetch objects.
    Example: consider the following query
    query {
      albums(where: {author: _eq: "bob"}}) {
        name
        releaseDate
        songs(where: {starCount: {_eq: 5}}) {
          id
          name
          starredBy {
            name
          }
        }
      }
    }
    If bob has released 5 albums, and on each of those albums, 3 songs
    have 5 stars, then:
    1x query for albums where bob is the author... returns 5 albums
    5x (5 albums) query for 5-star songs on each album... each query returns 3 songs
    15x (3 songs x 5 albums) query for the names of the people that
    starred the song.
    For a grand total of 75 queries to the database in a single request!
    Using Prefetch can bring that down the number of level deep
    the query goes, which in this case is 3.

    This class does two things to optimize the SQL executed for this query;
    (a) Update the queryset to only fetch the columns necessary to fulfill the request
    (b) Update the queryset to prefetch/select relate fields to avoid N+1
    """

    def __init__(self, registry, info):
        self.prefetch_stack = []
        self.prefetch_info_by_key = {}
        super(QuerysetOptimizationVisitor, self).__init__(registry, info)

    def hello_field(self, field, arguments, graphql_node=None):

        if field.is_relation:
            # Subtle thing here to account for how ORM optimizes query prefetching.
            # If the field is concrete, we need to add the field's name to the
            # field names for the node we're leaving.
            # If not concrete we need to add the reverse related name to the
            # field names for the node we're entering.
            field_names = []
            if field.concrete:
                self.prefetch_stack[-1].field_names.append(field.name)
            else:
                field_names = [field.field.name]

            # Push a NodeInfo onto the stack.
            alias = graphql_node.alias.value if graphql_node.alias else None
            self.prefetch_stack.append(
                NodeInfo(field.name, field.related_model, field_names, arguments, alias)
            )

        else:
            # This is just a scalar, which we add to the top of the stack's
            # list of field names to be passed to .only() later.
            self.prefetch_stack[-1].field_names.append(field.name)

    def goodbye_field(self, field):

        # If we aren't leaving a relational field, there's nothing to do
        if not field.is_relation:
            return

        if field.one_to_many or field.many_to_many:
            # *-to-many relations are handled via a later prefetch_related,
            # so we need to perform some bookkeeping by updating prefetch_info_by_key.

            # Fun edge case for handling aliased queries on the same field, e.g.
            # LabelByPk(pk: $labelId) {
            #   artists(where: {id: {_eq: $artistId}}) {
            #     name
            #     albums(where: {id: {_eq: $albumId}}) { title }
            #     allAlbums: albums(orderBy: {title: desc}) { title }
            #   }
            #   allArtists: artists(orderBy: {name: desc}) {
            #     name
            #     albums(where: {id: {_eq: 2}}) { title }
            #     allAlbums: albums(orderBy: {title: desc}) { title }
            #   }
            # }
            # Django handles this use case via the "to_attr" kwarg to Prefetch.
            # The following code constructs the path that works w/ aliases / to_attr.

            # We construct a path where aliases are _not_ used, because it allows
            # us to later determine if we _really_ need to use to_attr, which loads
            # its list into memory. We want to avoid doing this if e.g. a single
            # query happened to use an alias, and only use to_attr when two or more
            # queries of the same field exist within the same node.
            key_path = "__".join([pi.key for pi in self.prefetch_stack if pi.key])
            if key_path not in self.prefetch_info_by_key:
                self.prefetch_info_by_key[key_path] = []

            # Add to the list of prefetches on this key path. If the list on
            # this key path has more than 1 item, then we know we must use to_attr.
            prefetch_info = self.prefetch_stack.pop()
            self.prefetch_info_by_key[key_path].append(prefetch_info)

            # Set the correct path to be passed to Prefetch: all nonterminal
            # parts of the path use its alias if one exists, else its normal key.
            # The terminal/last part always uses its normal key.
            path_parts = [pi.alias or pi.key for pi in self.prefetch_stack if pi.key]
            path_parts.append(prefetch_info.key)
            prefetch_info.alias_path = "__".join(path_parts)
        elif field.one_to_one or field.many_to_one:
            # *-to-one relations are handled via a later select_related,
            # we've got bookkeeping here as well, but it's a bit more complex.
            # We must collapse/coalesce the top 2 items in the prefetch_stack.
            to_one = self.prefetch_stack.pop()

            # Add the popped item's key to the new top item's select_related_keys list.
            self.prefetch_stack[-1].select_related_keys.append(to_one.key)

            # Add the popped item's select_related_keys to the new top item's
            # select_related_keys, each prefixed with the popped item's key.
            for select_related_key in to_one.select_related_keys:
                self.prefetch_stack[-1].select_related_keys.append(
                    "{}__{}".format(to_one.key, select_related_key)
                )

            # Add the popped item's field_names to the new top item's field_names,
            # but prefixed with the popped item's key.
            for field_name in to_one.field_names:
                self.prefetch_stack[-1].field_names.append(
                    "{}__{}".format(to_one.key, field_name)
                )

    def hello_optimizable_tree(self, model_class, arguments):
        self.prefetch_stack.append(NodeInfo(None, model_class, [], arguments))

    def goodbye_optimizable_tree(self, model_class):
        self.artifacts = {
            "queryset_optimizer": QuerysetOptimizer(
                self.prefetch_stack.pop(), self.prefetch_info_by_key
            )
        }
