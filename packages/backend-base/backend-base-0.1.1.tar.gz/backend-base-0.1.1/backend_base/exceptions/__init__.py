"""
Global Backend exception and warning classes.
"""


class BaseBackendException(Exception):
    """Base Backend exception"""
    pass


class ImproperlyConfigured(BaseBackendException):
    """Backend is somehow improperly configured"""
    pass


class BackendUnicodeDecodeError(UnicodeDecodeError, BaseBackendException):
    def __init__(self, obj, *args):
        self.obj = obj
        super().__init__(*args)

    def __str__(self):
        return '%s. You passed in %r (%s)' % (
            super().__str__(),
            self.obj, type(self.obj)
        )
