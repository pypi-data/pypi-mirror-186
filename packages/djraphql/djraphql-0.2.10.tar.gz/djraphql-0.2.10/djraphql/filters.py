from abc import ABCMeta


class FilterBackend:
    __metaclass__ = ABCMeta

    def filter_backend(self, request, queryset, model_class):
        pass
