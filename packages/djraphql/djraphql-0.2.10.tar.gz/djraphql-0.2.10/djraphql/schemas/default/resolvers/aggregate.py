from six import iteritems
from functools import reduce
from graphene.utils.str_converters import to_snake_case
from ..util.arguments import update_queryset_based_on_arguments

IGNORED_FIELDS = set(["__typename"])


def build_aggregate_resolver(
    model_class, registry, aggregate_field_names_to_django_functions, related_name=None
):
    entity_class = registry.get_entity_class(model_class)

    def aggregate_resolver(parent, info, **kwargs):

        # Leaving this here as the QueryFieldsVisitor class doesn't yet
        # handle keywords like _sum, _max, _avg, etc. and thus the mechanism
        # that blocks unauthorized access *may* not work, so purely as a
        # fail-safe, this will stay for now. The aggregate querying
        # functionality needs a total rewrite/rethink anyhow.
        if not entity_class.is_readable_by_context(info.context):
            raise Exception("Invalid permissions.")

        # If related_name and parent are not None, then we are resolving a
        # subselect, which has already been prefetched via the code below.
        if related_name and parent is not None:
            return getattr(parent, related_name).all()

        # Call any filter_backends that were provided to us.
        queryset = entity_class.get_queryset(info.context)

        # For aggregate queries, all non-aggregate fields are included in the
        # resulting SQL query's group-by clause.
        grouped_fields, aggregated_fields_by_fn = _parse_aggregate_query(
            model_class,
            info,
            aggregate_field_names_to_django_functions.keys(),
        )

        # Filter the root queryset based on the arguments in the query
        queryset = update_queryset_based_on_arguments(
            queryset, kwargs, take_slice=False
        )

        # If there are no group-by fields, we simply need to call .aggregate()
        # with the right column and aggregation-function.
        # This does issue a DB query for every aggregation :(
        if not grouped_fields:
            results = []
            for aggregate_field_type, aggregated_fields in iteritems(
                aggregated_fields_by_fn
            ):
                fn = aggregate_field_names_to_django_functions[aggregate_field_type]
                for aggregated_field in aggregated_fields:
                    aggregate_result = queryset.aggregate(fn(aggregated_field))
                    value = aggregate_result[
                        "{}_{}".format(aggregated_field, aggregate_field_type)
                    ]
                    results.append({aggregate_field_type: {aggregated_field: value}})

            return results

        # We do have a group-by clause, so we have to do a bit more work...
        # Set the values to be in the GROUP BY clause
        queryset = queryset.values(*grouped_fields)

        # Use the mapping to make the annotations on the queryset
        labeled_aggregated_fields_by_aggregate_type = {}
        for aggregate_field_type, aggregated_fields in iteritems(
            aggregated_fields_by_fn
        ):
            labeled_aggregated_fields_by_aggregate_type[aggregate_field_type] = {}

            # fn here will be something like django.models.Sum
            fn = aggregate_field_names_to_django_functions[aggregate_field_type]

            # Group the aggregated fields by their aggregation type
            annotations = {
                "{}__{}".format(aggregate_field_type, aggregated_field): fn(
                    aggregated_field
                )
                for aggregated_field in aggregated_fields
            }

            # Annotate the queryset with each aggregation
            queryset = queryset.annotate(**annotations)

            # Optimization: repurpose our annotations dictionary to aid in
            # our transforming the resultset from the DB into the object shape
            # expected by the GraphQL resolve machinery by creating a list of
            # our nested references and reversing it, e.g.
            # artists__albums__star_count -> ['star_count', 'albums', 'artists']
            # Which is then used in the "reduce" call below to build a result
            # dictionary from the bottom-up.
            for aggregated_field_label, _ in iteritems(annotations):
                labels = aggregated_field_label.split("__")
                labels.reverse()
                labeled_aggregated_fields_by_aggregate_type[
                    aggregate_field_type
                ].update({aggregated_field_label: labels})

        # Do the same optimization we do for grouped fields that we did for
        # aggregated fields (see above).
        grouped_fields_by_resultset_field = {}
        for grouped_field in grouped_fields:
            split_fields = grouped_field.split("__")
            split_fields.reverse()
            grouped_fields_by_resultset_field[grouped_field] = split_fields

        # We must map the SQL result set to the shape of the GraphQL request
        results = []
        for row in queryset:
            # Grouped subqueries
            for resultset_name, split_fields in iteritems(
                grouped_fields_by_resultset_field
            ):
                group_nested = reduce(
                    lambda a, b: {b: a}, [row[resultset_name]] + split_fields
                )
                row.update(group_nested)

            # Aggregate subqueries
            for aggregate_field_name, labeled_aggregated_fields in iteritems(
                labeled_aggregated_fields_by_aggregate_type
            ):
                row[aggregate_field_name] = {}
                for label, split_and_reversed_label in iteritems(
                    labeled_aggregated_fields
                ):
                    nested = reduce(
                        lambda a, b: {b: a}, [row[label]] + split_and_reversed_label
                    )
                    row[aggregate_field_name].update(nested[aggregate_field_name])
            results.append(row)
        return results

    return aggregate_resolver


# TODO: This function should use a visitor, like how query-optimization works.
def _parse_aggregate_query(model_class, info, aggregate_properties):
    def _inner_parse_aggregate_query_aggregate_selection(
        aggregate_fn, selections, parent_key=None
    ):
        result = []
        for selection in selections:
            if selection.name.value in IGNORED_FIELDS:
                continue

            if selection.selection_set and selection.selection_set.selections:
                result += _inner_parse_aggregate_query_aggregate_selection(
                    aggregate_fn,
                    selection.selection_set.selections,
                    parent_key=(
                        "{}__{}".format(parent_key, to_snake_case(selection.name.value))
                        if parent_key
                        else to_snake_case(selection.name.value)
                    ),
                )
            elif parent_key:
                result.append(
                    "{}__{}".format(parent_key, to_snake_case(selection.name.value))
                )
            else:
                result.append(to_snake_case(selection.name.value))

        return result

    def _inner_parse_aggregate_query(
        model_class, parent_type, selections, current_key=None
    ):
        grouped_fields = []
        aggregated_fields_by_fn = {}
        for selection in selections:
            if selection.name.value in IGNORED_FIELDS:
                continue

            if selection.name.value in aggregate_properties:
                if selection.name.value not in aggregated_fields_by_fn:
                    aggregated_fields_by_fn[selection.name.value] = []

                aggregated = _inner_parse_aggregate_query_aggregate_selection(
                    selection.name.value, selection.selection_set.selections
                )
                aggregated_fields_by_fn[selection.name.value] += aggregated
            elif selection.selection_set and selection.selection_set.selections:
                grouped, _ = _inner_parse_aggregate_query(
                    model_class,
                    parent_type,
                    selection.selection_set.selections,
                    current_key=selection.name.value,
                )
                grouped_fields.append(
                    to_snake_case(selection.name.value) + "__" + "__".join(grouped)
                )
            else:
                grouped_fields.append(to_snake_case(selection.name.value))

        return grouped_fields, aggregated_fields_by_fn

    parent_type = info.parent_type.fields.get(info.field_name).type
    selections = info.field_nodes[0].selection_set.selections
    return _inner_parse_aggregate_query(
        model_class,
        getattr(parent_type, "of_type", parent_type),
        selections,
    )
