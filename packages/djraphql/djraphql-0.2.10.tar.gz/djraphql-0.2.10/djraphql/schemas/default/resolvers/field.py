def build_field_resolver(field, registry):
    entity_class = registry.get_entity_class(field.related_model)

    def resolve_field(parent, info, **kwargs):
        return getattr(parent, field.name, None)

    return resolve_field
