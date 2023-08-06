from djraphql.django_models import get_pk_fields_for_model


class TypeRegistry:
    """The TypeRegistry is the control-center of DjraphQL. It takes a schema object
    which is created by the library user and exposes methods that are called during
    GraphQL-schema build-time and query resolution time.

    It takes a list of Entity classes (via register_entity_classes) and makes them
    accessible to the classes that build the Graphene types that eventually become
    GraphQL classes.

    Each builder type (e.g. basic.py) exposes a make method that takes a TypeRegistry
    instance as its first argument. Through this instance, type builders reference any
    related types associated with the model being processed.
    """

    _ENTITY_CLASS_KEY = "__entity_class__"
    _MODEL_FIELDS_KEY = "__model_fields_by_name__"

    def __init__(self, schema):
        """
        Args:
            schema: Instance of a class that implements
                    djraphql.schemas.abstract_type_builder.AbstractSchema.
        """
        self.schema = schema
        self._node_graphql_type_name_to_model_class = {}
        self._cache = {
            "models": {},
            "types": {},
        }

    def get_available_model_classes(self):
        """A convenience method that returns a list of all Model classes that
        should be exposed in the GraphQL API. Which is all the models that have
        an associated Entity class that was passed to register_entity_classes.
        """
        if not hasattr(self, "_available_model_classes"):
            self._get_available_model_classes = self._model_cache.keys()

        return self._get_available_model_classes

    @property
    def _model_cache(self):
        """A dictionary that stores any models whose Entity class we're aware of."""
        return self._cache["models"]

    @property
    def _type_cache(self):
        """A dictionary that stores any Graphene types we've created."""
        return self._cache["types"]

    def get_entity_class(self, model_class):
        return self._model_cache.get(model_class, {}).get(self._ENTITY_CLASS_KEY)

    def lambda_from_registry(self, model_class, key):
        """A heavily used method that returns a lambda that returns a Graphene type.
        This is necessary because circular relationships exist. If we're building a
        schema that contains a Foo model that is one-to-many with a Bar model, we'll
        start creating the Foo, notice that it has a field "bars" and then attempt
        to create the Bar type. But then we'll run into the Bar.foo field, and attempt
        to create the Foo type, creating an infinite loop.

        Graphene solves this by allowing the "type" argument on the Field be a lambda
        that returns a type, which allows us to avoid the infinite loop by providing
        a lambda (that returns the type) instead of the type itself.

        Args:
            model_class: class of the Django modele for the Graphene type we want
            key: string from the djraphql.schemas.default.mappings.Types class.
        Returns:
            A lambda that returns the Graphene type corresponding to the inputs.
        """

        def _get_type_from_registry():
            cache_key = "{}/{}".format(model_class.__name__, key)
            if cache_key not in self._type_cache:
                raise RuntimeError(
                    "{} does not exist in DjraphQL type cache.".format(cache_key)
                )

            return self._type_cache[cache_key]

        return _get_type_from_registry

    def register_entity_classes(self, *entity_classes):
        """Takes the given list of Entity classes, caches each one plus its
        associated model and also builds a mapping where the keys are GraphQL
        type names and the values are dicts containing the Entity and Model classes.

        Args:
            entity_classes: list of Entity classes for which we want to build
                Graphene types.
        """
        # Entity classes for API settings
        for entity_class in entity_classes:
            model_class = entity_class.Meta.model

            self._model_cache[model_class] = {
                self._ENTITY_CLASS_KEY: entity_class,
            }

            # Update our mapping of names (of GraphQL schema objects) to
            # model class and entity class. During query optimization,
            # as we traverse the tree of selected fields in the GraphQL query,
            # we only have access to the GraphQL type names. This mapping
            # will enable us to map those names to the associated model.
            node_name = self.schema.get_node_name_for_model(model_class)
            self._node_graphql_type_name_to_model_class[node_name] = {
                "model_class": model_class,
                "entity_class": entity_class,
            }

    def get_or_create_type(self, type_key, **kwargs):
        """Given a type_key (from the Types class) and one or more kwargs,
        get or build the type corresponding to the type_key.

        The kwargs are passed through to the builder in the case we haven't yet
        built this type which is indicated by the type not being in the cache.

        Args:
            type_key: string from the djraphql.schemas.default.mappings.Types class.
        Kwargs:
            Arbitrary, but most of the time it will be "model_class". The kwargs
                are defined by the builder's make method. E.g. in basic.py, the
                model_class is required.
        Returns:
            Graphene type associated with the type_key
        """
        if type_key not in self.schema.BUILDER_MAP:
            raise Exception(
                "get_or_create_type called with unknown key: {}".format(type_key)
            )

        # Check to see if we've already built this type and if so, return it.
        builder = self.schema.BUILDER_MAP[type_key]
        cache_key = builder.cache_key(type_key, **kwargs)
        if cache_key in self._type_cache:
            return self._type_cache[cache_key]

        # The type was not in the cache, so use the builder class
        # for this type key to create it, then cache the result and return it.
        result = builder.make(self, type_key=type_key, **kwargs)
        self._type_cache[cache_key] = result
        return result

    def get_model_fields(self, model_class):
        """When building a type, a type builder class (e.g. basic.py) needs to
        know what fields the library user wants to expose on the model being
        processed. This method basically proxies to the Model class's associated
        Entity class which is the source of truth for what fields to expose.

        Since this operation may require iterating through each field on a Model
        class, we cache the result as this method is called many times per model.

        Args:
            model_class: class of the Django Model being processed
        Returns:
            dict where the keys are strings whose value is the field, and the
                values are djraphql.fields.ModelField instances.
        """

        if self._model_cache[model_class].get(self._MODEL_FIELDS_KEY):
            return self._model_cache[model_class].get(self._MODEL_FIELDS_KEY)

        result = {}
        entity_class = self.get_entity_class(model_class)
        available_model_classes = self.get_available_model_classes()
        for model_field in entity_class.get_all_model_fields():
            django_model_field = model_field.get_django_model_field()
            if (
                not django_model_field.is_relation
                or django_model_field.related_model in available_model_classes
            ):
                result[model_field.name] = model_field

        self._model_cache[model_class][self._MODEL_FIELDS_KEY] = result
        return result

    def get_pk_fields_for_model(self, model_class):
        """Convenience method that wraps a utility method that gets the primary-key
        fields on a model.
        """
        return get_pk_fields_for_model(model_class, self.get_available_model_classes())

    def get_graphene_type_or_default(self, model_field):
        """Convenience method that returns the appropriate Graphene type for a
        ModelField.

        Args:
            model_field: ModelField instance that _may_ have a graphene_type specified.
        Returns:
            A graphene type e.g. Int, String. If the passed-in ModelField specifies
                a graphene_type (set by the user), use that. Otherwise the schema's
                type mapping is used .
        """
        # If the ModelField specifies its desired graphene_type, use it
        if model_field.graphene_type:
            return model_field.graphene_type

        # Otherwise, fall back to the type map used by the generation schema
        field = model_field.get_django_model_field()
        return self.schema.FIELD_TYPE_MAP[field.get_internal_type()]
