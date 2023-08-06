import copy


class MutationAccumulator:
    def __init__(self):
        self.current_path = []
        self.pks_to_tags = []
        self.validation_errors = []  # e.g. [{"path": [], "errors": {"foo": "bar"}}]
        self.fatal_error = None
        self.root_result = None

    def push_path_part(self, path_part):
        self.current_path.append(path_part)

    def pop_path_part(self):
        return self.current_path.pop()

    def add_validation_error(self, error):
        self.validation_errors.append(
            {
                "path": copy.copy(self.current_path),
                "errors": error,
            }
        )

    def add_pk_to_tag(self, pk, tag, _type):
        self.pks_to_tags.append({"pk": pk, "tag": tag, "type": _type})

    def set_fatal_error(self, error):
        self.fatal_error = error

    def should_halt_execution(self):
        return bool(self.fatal_error)
