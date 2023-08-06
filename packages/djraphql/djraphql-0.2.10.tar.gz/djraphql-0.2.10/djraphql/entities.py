from djraphql.access_permissions import (
    CREATE,
    READ,
    UPDATE,
    DELETE,
    R,
    AccessPermissionsBitmap,
)
from djraphql.fields import AllModelFields, ComputedField, ModelField


class Entity:
    properties = ()
    filter_backends = ()
    access_permissions = (R,)
    query_classes = None
    mutation_classes = None
    validator = None

    @classmethod
    def get_queryset(cls, context):
        queryset = cls.Meta.model.objects.all()

        try:
            for backend_filter in cls.filter_backends:
                queryset = backend_filter.filter_backend(context, queryset)
        except Exception as e:
            raise Exception(
                "An error occurred when applying filter backend {}: {}".format(
                    backend_filter.__class__.__name__, str(e)
                )
            )

        return queryset

    @classmethod
    def can_get_for_insert(cls):
        return cls.get_for_insert != Entity.get_for_insert

    @staticmethod
    def get_for_insert(context):
        raise NotImplementedError()

    @classmethod
    def allows_permissions(cls, access_permissions):
        """Check that the access_permissions field defined on this Entity class
        matches the passed in access_permissions bitmap, which will come from
        AbstractRootTypeBuilder.get_required_access_permissions().

        This check is generally used to ensure we want to expose a Root query
        or mutation for an Entity, e.g. fooByPk should only exist if FooEntity's
        READ flag is 1.
        """
        return access_permissions == (
            cls._get_access_permissions_bitmap() & access_permissions
        )

    @classmethod
    def is_creatable(cls):
        return bool(cls._get_access_permissions_bitmap() & CREATE)

    @classmethod
    def is_readable(cls):
        return bool(cls._get_access_permissions_bitmap() & READ)

    @classmethod
    def is_updatable(cls):
        return bool(cls._get_access_permissions_bitmap() & UPDATE)

    @classmethod
    def is_deletable(cls):
        return bool(cls._get_access_permissions_bitmap() & DELETE)

    @classmethod
    def is_creatable_by_context(cls, context):
        return cls._is_context_authorized_for_permission_type(context, CREATE)

    @classmethod
    def is_readable_by_context(cls, context):
        return cls._is_context_authorized_for_permission_type(context, READ)

    @classmethod
    def is_updatable_by_context(cls, context):
        return cls._is_context_authorized_for_permission_type(context, UPDATE)

    @classmethod
    def is_deletable_by_context(cls, context):
        return cls._is_context_authorized_for_permission_type(context, DELETE)

    @classmethod
    def _is_context_authorized_for_permission_type(cls, context, permission_type):
        for access_permission in cls.access_permissions:
            if access_permission.matches(permission_type):
                return access_permission.has_permission(context)

        return False

    @classmethod
    def _get_access_permissions_bitmap(cls):
        # Cache the AccessPermissionsBitmap and reuse it across calls
        if not hasattr(cls, "_access_permissions_bitmap"):
            cls._access_permissions_bitmap = AccessPermissionsBitmap(
                *cls.access_permissions
            )
        return cls._access_permissions_bitmap

    @staticmethod
    def before_insert(data, context):
        pass

    @staticmethod
    def after_insert(instance, context):
        pass

    @classmethod
    def _get_meta_fields(cls):
        return getattr(cls.Meta, "fields", ())

    @classmethod
    def _get_computed_fields(cls):
        return [f for f in cls._get_meta_fields() if isinstance(f, ComputedField)]

    @classmethod
    def get_all_model_fields(cls):
        result = {}
        model_fields, _, special_fields = cls._partition_basic_and_special_fields()

        # Get ModelFields that are implicit via AllModelFields
        if special_fields:
            implicit_fields = special_fields[0].generate_model_fields(cls.Meta.model)
            result.update(implicit_fields)

        # Get the raw ModelFields define by the user, which override implicit ones
        for explicit_field in model_fields:
            if special_fields and explicit_field.name not in result:
                raise Exception(
                    "{}.{} (a) does not exist, or (b) both excluded via AllModelFields's excluding keyword argument and included as a ModelField, or (c) references a model that is not specified by an Entity.".format(
                        cls.Meta.model.__name__, explicit_field.name
                    )
                )
            result[explicit_field.name] = explicit_field.with_model_class(
                cls.Meta.model
            )

        return result.values()

    @classmethod
    def _partition_basic_and_special_fields(cls):
        fields_list = cls._get_meta_fields()
        special_fields = []
        computed_fields = []
        basic_fields = []

        for field in fields_list:
            if isinstance(field, AllModelFields):
                special_fields.append(field)
            elif isinstance(field, ComputedField):
                computed_fields.append(field)
            else:
                basic_fields.append(field)

        assert len(special_fields) <= 1, "Provide zero or one AllModelFields instances."
        return basic_fields, computed_fields, special_fields
