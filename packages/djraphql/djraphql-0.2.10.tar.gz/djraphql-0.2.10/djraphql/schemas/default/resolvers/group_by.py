def build_group_by_resolver(field):
    def group_by_resolver(parent, info, **kwargs):
        return parent[field.name]

    return group_by_resolver
