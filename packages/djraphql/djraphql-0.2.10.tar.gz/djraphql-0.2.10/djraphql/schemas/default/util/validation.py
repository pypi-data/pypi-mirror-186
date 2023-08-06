from functools import reduce
from enum import Enum
from graphene.utils.str_converters import to_camel_case


class FatalValidationError(Exception):
    pass


class ValidatableInput:
    def __init__(self, raw_input, root_model_class, is_insert=True):
        self._raw_input = raw_input
        self._root_model_class = root_model_class
        self._is_insert = is_insert

    def to_value(self, camel_case_keys=False, lift_lists=True):
        # Shallow copy so we don't mutate self._raw_input
        # Note that using deepcopy here resulted in a weird
        # "list is not callable" error deep within the deepcopy code...
        value = self._raw_input.copy()

        if lift_lists:
            # The input format for inserts and updates is slightly different:
            # Update input objects go one level deeper -- via an "items" key -- to get
            # the actual item being updated. So to lift the *-to-many fields up,
            # we need to account for that. This extract_list helper performs the
            # correct traversal based on the path variable.
            path = [] if self._is_insert else ["items"]
            extract_list = lambda items: reduce(lambda a, b: a[b], path, items)
            value = self._lift_lists_to_related_key(
                value, self._root_model_class, extract_list
            )

        value = self._convert_enum_values_to_strings(value)

        if camel_case_keys:
            value = self._camel_case_keys(value)

        return value

    @classmethod
    def _convert_enum_values_to_strings(cls, value):
        if isinstance(value, Enum):
            return value.name

        if isinstance(value, dict):
            return {
                key: cls._convert_enum_values_to_strings(value[key]) for key in value
            }

        if isinstance(value, list):
            return [cls._convert_enum_values_to_strings(item) for item in value]

        return value

    @classmethod
    def _camel_case_keys(cls, value):
        if not value or not isinstance(value, dict):
            return value

        result = {}
        for k in value:
            result[to_camel_case(k)] = cls._camel_case_keys(value[k])

        return result

    @classmethod
    def _lift_lists_to_related_key(cls, value, model_class, extract_list):
        """Dealing with the raw input object is cumbersome due to the intermediate
        layers of the object tree that contain things like updateStrategy, etc.

        This method provides a way for the consumer of the library to instead receive
        a structure that mirrors the model structure, which is more convenient for
        validation.

        Args:
            value: object. e.g. for an updateLabel, it may look like:
                {
                    "artists": {
                        "updateStrategy": "replace",
                        "items: [
                            {"pk": 1, "data": {"name": "Jim"}},
                            {"data": {"name": "Bob"}}
                        ]
                    }
                }
            model_class: the model_class being inserted/updated
            extract_list: helper function to get to the list of items
        Returns:
            object: example based on above value argument,
                {
                    "artists": [
                        {"id": 1, "name": "Jim"},
                        {"name": "Bob"}
                    ]
                }
        """

        # Iterate through the model's to-many fields
        for f in model_class._meta.get_fields():
            if (
                not f.name in value
                or not f.is_relation
                or f.one_to_one
                or f.many_to_one
            ):
                continue

            results = []
            for item in extract_list(value[f.name]):
                new_item = cls._lift_lists_to_related_key(
                    item["data"].copy(), f.related_model, extract_list
                )
                if "pk" in item:
                    new_item["pk"] = item["pk"]
                results.append(new_item)

            value[f.name] = results

        return value


def perform_validation(
    entity_class, raw_input_value, model_class, parent, info, is_insert=False
):
    if not entity_class.validator:
        return (True, None)

    validatable_input = ValidatableInput(
        raw_input_value, model_class, is_insert=is_insert
    )

    return entity_class.validator.validate(validatable_input, parent=parent, info=info)
