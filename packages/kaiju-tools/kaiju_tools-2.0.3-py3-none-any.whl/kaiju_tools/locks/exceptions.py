from kaiju_tools.exceptions import APIException


class LockError(APIException):
    """See `.etc.StatusCodes` for possible error messages."""


class LockExistsError(LockError):
    pass


class NotALockOwnerError(LockError):
    pass


class LockAcquireTimeout(LockError):
    pass
