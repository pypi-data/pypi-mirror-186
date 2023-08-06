from django.db.models.query import Prefetch
from .arguments import update_queryset_based_on_arguments


class QuerysetOptimizer:
    def __init__(self, root_info, selection_prefetch_info):
        """One of the artifacts produced by the visit_query method in the
        visitors/__init__.py file is an instance of this class.

        Args:
            root_info: NodeInfo instance. The NodeInfo class is defined in the
                visitors/query_optimization_visitor.py file.
            selection_prefecth_info: dict where the keys are Django model
                paths to be used as arguments into Prefetch instances, and the
                values are lists of NodeInfo instances.
        """
        self.root_info = root_info
        self.selection_prefetch_info = selection_prefetch_info

    def optimize(self, queryset):
        """Given the info passed to our constructor, take the given queryset
        and apply the select_related and prefetch_related calls so that we can
        minimize the number of SQL queries we need to fulfill the request.

        Additionally, call .only() for each one to ensure we only fetch the
        columns necessary to fulfill the request.
        """

        # Why do we sort the keys? Because we ran into an issue where
        # if we process e.g. ['artists__albums', 'artists'], Django complains:
        # ValueError("'artists' lookup was already seen with a different queryset.
        # You may need to adjust the ordering of your lookups.",)
        # Oddly, the error does not happen when processed in order
        # like ['artists', 'artists__albums']. So we sort the keys. This will
        # probably blow up in unexpected ways but theoretically the order shouldn't
        # matter at all, so if ordering them to appease Django works, it feels OK.
        to_many_sorted_keys = sorted(self.selection_prefetch_info.keys())
        for key in to_many_sorted_keys:
            prefetches = []
            use_to_attr = len(self.selection_prefetch_info[key]) > 1
            for prefetch_info in self.selection_prefetch_info[key]:

                # Only select the columns necessary to fulfill the request
                prefetch_queryset = prefetch_info.model_class.objects.only(
                    *prefetch_info.field_names
                )

                # Prefetches (which generally map to *-to-many relations of the root
                # object) can have nested *-to-one relations which we need to fetch
                # via select_related. This minimizes the # of queries Django ORM executes.
                if prefetch_info.select_related_keys:
                    prefetch_queryset = prefetch_queryset.select_related(
                        *prefetch_info.select_related_keys
                    )

                prefetches.append(
                    Prefetch(
                        prefetch_info.alias_path if use_to_attr else key,
                        queryset=update_queryset_based_on_arguments(
                            prefetch_queryset,
                            prefetch_info.arguments,
                            take_slice=False,
                        ),
                        to_attr=prefetch_info.alias if use_to_attr else None,
                    )
                )

            # Call prefetch_related, passing in the Prefetch object that contains
            # our optimizations plus filtering for any arguments from the query.
            queryset = queryset.prefetch_related(*prefetches)

        # The prefetch_stack should now have a single item, which maps
        # to the root object in the query. Select only necessary columns and filter
        # via any arguments passed in.
        queryset = update_queryset_based_on_arguments(
            queryset.only(*self.root_info.field_names),
            self.root_info.arguments,
        )

        # Finally, add any necessary select_related calls.
        if self.root_info.select_related_keys:
            queryset = queryset.select_related(*self.root_info.select_related_keys)

        return queryset
