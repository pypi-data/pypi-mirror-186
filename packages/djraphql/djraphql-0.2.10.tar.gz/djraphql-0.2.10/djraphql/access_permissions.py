from abc import ABCMeta, abstractmethod
from six.moves import reduce

CREATE = 1
READ = 2
UPDATE = 4
DELETE = 8


class PermissionFlag:
    """Representation of a permission, such as Create. Can be passed a list of
    permission checks, which the context must satisfy in order to be able to perform
    the operation associated with this permission.
    """

    def __init__(self, *permission_checks):
        self.permission_checks = permission_checks

    def __and__(self, value):
        return self.TYPE & value

    def __rand__(self, value):
        return self.TYPE & value

    def __or__(self, value):
        return self.TYPE | value

    def __ror__(self, value):
        return self.TYPE | value

    def has_permission(self, context):
        for permission_check in self.permission_checks:
            if not permission_check.is_authorized(context):
                return False

        return True

    def matches(self, permission_type):
        return bool(self.TYPE & permission_type)


class AccessPermissionsBitmap:
    """This class is used to wrap a list of PermissionFlags, and allow bit-wise
    operations on the permissions passed in, which will be one of the 4 PermissionFlag
    objects defined below: Create, Read, Update, Delete.
    """

    def __init__(self, *permissions):
        self.permissions = permissions
        self._bitmap = reduce(lambda a, b: a | b, permissions)

    def __iter__(self):
        return iter(self.permissions)

    def __and__(self, value):
        return self._bitmap & value

    def __or__(self, value):
        return self._bitmap | value


class Create(PermissionFlag):
    TYPE = CREATE


class Read(PermissionFlag):
    TYPE = READ


class Update(PermissionFlag):
    TYPE = UPDATE


class Delete(PermissionFlag):
    TYPE = DELETE


"""Expose convenient constants that contain no checks. I.e., Permissions(C, R, U, D)
means the Entity will be C/R/U/D-able without restriction.
"""
C = Create()
R = Read()
U = Update()
D = Delete()


class RequestAuthorizationCheck:
    """Base class used to perform a context-level (i.e. the request object) check
    against a permission type, e.g. Create or Read.

    E.g. if Foos are readable by everyone, but only staff users can create them,
    then you'd need a class to check whether a user is staff:

    class IsStaffUser(RequestAuthorizationCheck)
        def is_authorized(self, context):
            return context.user.is_staff

    And define the permissions like:

    class FooEntity(Entity):
        access_permissions = Permissions(Create(IsStaffUser()), R)
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def is_authorized(self, context):
        pass
