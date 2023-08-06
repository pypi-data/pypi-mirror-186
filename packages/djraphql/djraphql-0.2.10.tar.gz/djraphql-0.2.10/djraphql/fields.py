from graphene import Int, String
from djraphql.django_models import get_field_by_name


class ModelField:
    def __init__(self, name, read_only=False, graphene_type=None):
        self.name = name
        self.read_only = read_only
        self.graphene_type = graphene_type

    def get_resolver(self, entity_class):
        return lambda context, instance: getattr(instance, self.name, None)

    def get_django_model_field(self):
        return get_field_by_name(self.model_class, self.name)

    def with_model_class(self, model_class):
        """This method is used to hydrate this ModelField instance
        with the associated model class (which comes from Entity.meta.model).

        Maybe a bit hacky, but if we didn't have it, we'd have to provide the
        model class to each instance in the Entity.Meta.fields tuple,
        which is a poor DX.
        """

        self.model_class = model_class
        return self


class ComputedField:
    def __init__(self, name, graphene_type, depends_on=()):
        self.name = name
        self.graphene_type = graphene_type
        self.depends_on = depends_on

    def get_graphene_type(self):
        return self.graphene_type

    def get_resolver(self, entity_class):
        def method_property_resolver(context, instance):
            resolver = getattr(entity_class, "get_{}".format(self.name))
            return resolver(context, instance)

        return method_property_resolver


class AllModelFields:
    def __init__(self, excluding=()):
        self.exclude_fields = excluding

    def field_is_excluded(self, field):
        return field.name in self.exclude_fields

    def generate_model_fields(self, model_class):
        return {
            field.name: ModelField(field.name).with_model_class(model_class)
            for field in model_class._meta.get_fields()
            if field.name not in self.exclude_fields
        }
