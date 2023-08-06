from graphql.language.visitor import visit, ParallelVisitor
from .queryset_optimization_visitor import QuerysetOptimizationVisitor
from .read_permissions_check_visitor import ReadPermissionsCheckVisitor


def visit_query(registry, info):
    query_visitor = QueryVisitor(
        [
            QuerysetOptimizationVisitor(registry, info),
            ReadPermissionsCheckVisitor(registry, info),
        ]
    )
    visit(info.field_nodes[0], query_visitor)
    return query_visitor.artifacts


class QueryVisitor(ParallelVisitor):
    @property
    def artifacts(self):
        result = {}
        for visitor in self.visitors:
            result.update(getattr(visitor, "artifacts", {}))
        return result
