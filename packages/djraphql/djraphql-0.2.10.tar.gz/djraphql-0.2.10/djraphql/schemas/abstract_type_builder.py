from abc import ABCMeta, abstractmethod, abstractproperty


class CacheableTypeBuilder:
    @classmethod
    def cache_key(cls, type_key, **kwargs):
        if "model_class" in kwargs:
            return "{}/{}".format(kwargs["model_class"].__name__, type_key)

        return type_key


class AbstractTypeBuilder:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def make(registry, **kwargs):
        raise NotImplementedError()


class AbstractRootTypeBuilder(AbstractTypeBuilder):
    @abstractmethod
    def get_field_name(self, model_class):
        pass

    @abstractmethod
    def get_docs(self, model_class):
        pass

    @abstractmethod
    def get_required_access_permissions():
        pass

    @classmethod
    @abstractmethod
    def get_root_fields(cls, registry, model):
        raise NotImplementedError()


class QueryRootTypeBuilder(AbstractRootTypeBuilder):
    @classmethod
    @abstractmethod
    def get_root_fields(cls, registry, model_class):
        field, resolver = cls.make(registry, model_class=model_class)
        field_name = cls.get_field_name(model_class)
        return {field_name: field, "resolve_{}".format(field_name): resolver}


class MutationRootTypeBuilder(AbstractRootTypeBuilder):
    @classmethod
    @abstractmethod
    def get_root_fields(cls, registry, model_class):
        mutation = cls.make(registry, model_class=model_class)
        mutation_name = cls.get_field_name(model_class)
        return {mutation_name: mutation.Field()}


class AbstractSchema:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_node_name_for_model(self, model_class):
        raise NotImplementedError()

    @abstractmethod
    def build_query_root_type(self, registry):
        raise NotImplementedError()

    @abstractmethod
    def build_mutation_root_type(self, registry):
        raise NotImplementedError()

    @abstractproperty
    def BUILDER_MAP(self):
        raise NotImplementedError()

    @abstractproperty
    def FIELD_TYPE_MAP(self):
        raise NotImplementedError()

    @abstractproperty
    def DEFAULT_QUERIES(self):
        raise NotImplementedError()

    @abstractproperty
    def DEFAULT_MUTATIONS(self):
        raise NotImplementedError()
