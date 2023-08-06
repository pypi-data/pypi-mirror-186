from ..util.visitors import visit_query
from ..util.arguments import (
    DEFAULT_MAXIMUM_RESULTS,
    ABSOLUTE_MAXIMUM_RESULTS,
    update_queryset_based_on_arguments,
)


def build_list_resolver(model_class, registry, related_name=None):
    entity_class = registry.get_entity_class(model_class)

    def list_resolver(parent, info, **kwargs):

        # If related_name and parent are not None, then we are resolving a
        # subselect, which has already been prefetched via the code below.
        if related_name and parent is not None:
            # If we were given offset/limit parameters in the GraphQL query
            # we need to do them manually, because Django's ORM prevents
            # filtering _after_ slicing (rightfully, because it would break the
            # functionality of prefetching), which occurs naturally in
            # the course of query optimization: we'll make the select_related
            # and prefetch_related calls, but those prefetches work by
            # adding another filter predicate of the form "and x.id in (a, b, c)..."
            # which necessarily must occur after our optimization logic has run.
            # Thus, we must defer slicing until we enter this resolver.
            begin, end = get_begin_and_end_from_arguments(**kwargs)

            # Edge-case: if the request contained "twin queries", e.g.
            # LabelByPk(pk: 1) {
            #   oneArtist: artists(where: {id: {_eq: 1}}) { name }
            #   allArtists: artists(orderBy: {name: desc}) { name }
            # }
            # where we're querying the same field ("artists") multiple times,
            # it's handled as a "to_attr" during query optimization.
            # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#prefetch-objects
            # This unfortunately materializes a list in memory _before_ slicing,
            # but it's a valuable use case so we need to handle it somehow.
            maybe_alias = info.path.key
            if maybe_alias != related_name and hasattr(parent, maybe_alias):
                return getattr(parent, maybe_alias)[begin:end]

            # There was a test for queryset.count() < 10000
            # here before. The idea was that if more than 10K rows were
            # about to be loaded into memory, it was better to N+1.
            # It was removed because it was untested and premature,
            # but possibly one day it may make sense to revisit.
            queryset = getattr(parent, related_name).get_queryset()
            return queryset[begin:end]

        # We're resolving a top-level select, so we must filter by org,
        # which is done by running the check lambda provided by the caller
        queryset = entity_class.get_queryset(info.context)
        artifacts = visit_query(registry, info)
        return artifacts["queryset_optimizer"].optimize(queryset)

    return list_resolver


def get_begin_and_end_from_arguments(**kwargs):
    begin = None
    end = None

    if "offset" in kwargs:
        begin = kwargs.get("offset") or 0

    if "limit" in kwargs:
        limit = min(kwargs["limit"], ABSOLUTE_MAXIMUM_RESULTS)
        end = (begin or 0) + limit

    return begin, end
