
class StatusCodes:
    """Status and error codes for locks."""
    LOCK_EXISTS = 'LOCK_EXISTS'         #: the lock already present in the db
    NOT_LOCK_OWNER = 'NOT_OWNER'        #: service trying to release a lock is not a lock owner
    RUNTIME_ERROR = 'RUNTIME_ERROR'     #: any other error
    LOCK_ACQUIRE_TIMEOUT = 'LOCK_ACQUIRE_TIMEOUT'
    OK = 'OK'                           #: OK
