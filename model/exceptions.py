
class GodebateException(AssertionError):
    pass


class AccessException(GodebateException):
    pass


class AuthenticationFailure(AccessException):

    def __init__(self):
        super().__init__("Wrong username or password")


class AccessDenied(AccessException):
    pass
