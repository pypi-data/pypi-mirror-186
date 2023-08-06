from ..util.visitors import visit_query


def build_by_pk_resolver(model_class, registry):
    entity_class = registry.get_entity_class(model_class)

    def by_pk_resolver(parent, info, **kwargs):
        queryset = entity_class.get_queryset(info.context).filter(**kwargs)
        artifacts = visit_query(registry, info)
        optimizer = artifacts.get("queryset_optimizer")
        if not optimizer:
            return queryset
        return optimizer.optimize(queryset).get()

    return by_pk_resolver
