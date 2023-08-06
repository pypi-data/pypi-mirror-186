"""Набор шаблонов классов REST исключений.
Данные исключения перехватываются REST API обработчиком исключений, для них
генерится JSON строка ответа. Остальные исключения будут видимы только в логах
приложения (или на странице, если был включен debug режим).
"""

import traceback
import uuid

from aiohttp.web import middleware, Response, Request
from aiohttp.web_exceptions import *
from aiohttp.client import ClientResponseError

from ..exceptions import APIException, parse_base_exception, ensure_traceback
from ..serialization import dumps, loads, Serializable

__all__ = (
    'create_rest_exception',
    'error_middleware', 'REQUEST_ID_HEADER', 'CONTENT_TYPE_HEADER'
)


CONTENT_TYPE_HEADER = 'Content-Type'
REQUEST_ID_HEADER = 'X-Correlation-ID'


class ErrorCodes:
    INTERNAL_ERROR = 'InternalError'


def create_rest_exception(exc, debug: bool) -> (int, dict):
    """Error to JSON format function."""

    if isinstance(exc, APIException):
        status = exc.status_code
        exc.debug = debug
        error = exc.repr()
    elif isinstance(exc, HTTPClientError):
        status = exc.status
        error = {
            'code': status,
            'message': str(exc),
            'data': {
                'type':  exc.__class__.__name__
            }
        }
    else:
        status = 500
        error = {
            'code': status,
            'message': 'Internal error.',
            'data': {
                'type': exc.__class__.__name__
            }
        }
        if debug:
            error['data'].update(parse_base_exception(exc, debug=True))
    return status, error


@middleware
async def error_middleware(request: Request, handler):
    """Простая мидлваре для ошибок с поддержкой sentry."""

    h = REQUEST_ID_HEADER

    if h in request.headers:
        try:
            request_id = uuid.UUID(request.headers[h])
        except Exception:
            request_id = uuid.uuid4()
    else:
        request_id = uuid.uuid4()

    request['id'] = str(request_id)

    logger = request.app.logger.getChild(f'request.{request["id"]}')
    debug = request.app.debug
    request['logger'] = logger

    try:
        response = await handler(request)
    except Exception as exc:
        status, error = create_rest_exception(exc, debug=debug)
        if request.can_read_body:
            body = await request.json(loads=loads)
        else:
            body = None
        extra = {
            'fingerprint': ['error_middleware', request.method, request.url, status],
            'capturer': 'error_middleware',
            'request': {
                'remote': request.remote,
                'method': request.method,
                'url': request.url,
                'query': request.query_string,
                'headers': dict(request.headers),
                'body': body
            },
            'response': {
                'status': status
            }
        }
        if isinstance(exc, Serializable):
            extra['response']['body'] = exc.repr()
        else:
            extra['response']['body'] = str(exc)
        exc = ensure_traceback(exc)
        if status == 500:
            logger.error(exc, extra=extra, exc_info=(type(exc), exc, exc.__traceback__))
        else:
            logger.info(exc, extra=extra, exc_info=(type(exc), exc, exc.__traceback__))
        error = {
            'id': request_id.int,
            'error': error
        }
        headers = {
            CONTENT_TYPE_HEADER: 'application/json',
            h: request['id']
        }
        error = dumps(error)
        return Response(status=status, text=error, headers=headers)

    response.headers[h] = request['id']
    return response
