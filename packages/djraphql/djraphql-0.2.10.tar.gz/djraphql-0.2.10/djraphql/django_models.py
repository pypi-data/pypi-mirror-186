def get_pk_fields_for_model(model_class, available_model_classes):
    """Get all fields comprising a model class's primary key.
    """
    return tuple(
        [
            f
            for f in model_class._meta.get_fields()
            if getattr(f, "primary_key", False)
            and (not f.is_relation or f.related_model in available_model_classes)
        ]
    )


def get_field_by_name(model_class, field_name):
    """Given a Django model class and a field name, return the field.
    """
    if hasattr(model_class._meta, "get_field"):
        return model_class._meta.get_field(field_name)

    raise Exception("Cannot fetch {} field {}.".format(model_class, field_name))


def get_target_field(relational_field):
    """Given a relational Field, e.g. <ManyToOneRel: sample_music_app.artist>,
    gets the corresponding field on the referenced model.
    """

    # Django 2+
    if hasattr(relational_field, "target_field"):
        return relational_field.target_field

    # Django 1.8+
    if hasattr(relational_field, "related_field"):
        return relational_field.related_field

    raise Exception("Cannot get target field on field {}.".format(relational_field))
