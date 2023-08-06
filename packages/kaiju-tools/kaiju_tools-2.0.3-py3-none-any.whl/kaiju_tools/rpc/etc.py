
__all__ = ('JSONRPCHeaders',)


class JSONRPCHeaders:
    """List of JSONRPC request / response headers"""

    APP_ID_HEADER = 'X-App-ID'
    CORRELATION_ID_HEADER = 'X-Correlation-ID'
    SERVER_ID_HEADER = 'X-Server-ID'
    REQUEST_DEADLINE_HEADER = 'X-Request-Deadline'
    REQUEST_TIMEOUT_HEADER = 'X-Request-Timeout'
    CONTENT_TYPE_HEADER = 'Content-Type'
    SESSION_ID_HEADER = 'X-Session-ID'
    CALLBACK_ID = 'X-Callback-ID'
    AUTHORIZATION = 'Authorization'
