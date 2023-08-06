import logging
from functools import lru_cache
from pathlib import Path
from urllib.parse import urljoin
from typing import *

from aiohttp import BasicAuth
from aiohttp.client import ClientSession, TCPConnector, ClientResponseError
from aiohttp.cookiejar import CookieJar

from kaiju_tools.rpc.abc import AbstractRPCTransportInterface
from kaiju_tools.services import ContextableService
from kaiju_tools.serialization import dumps, loads
from kaiju_tools.mapping import get_field, set_field

__all__ = ['HTTPService']


class HTTPService(ContextableService, AbstractRPCTransportInterface):
    """Абстрактный класс для HTTP REST клиента."""

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json'
    }  #: заголовки для коннекта к еластику по HTTP

    UPLOAD_CHUNK_SIZE = 4096 * 1024

    def __init__(
            self, host: str = 'http://localhost:80', app=None, session: ClientSession = None,
            conn_settings: dict = None, auth: Union[dict, str] = None,
            cookie_settings: dict = None, logger: logging.Logger = None):
        """
        :param app: optional web application instance
        :param host: полное имя хоста
        :param session: готовая HTTP сессия
        :param conn_settings: настройки для HTTP сессии (игнорируются, если передана сессия)
        :param auth: basic auth settings — "login", "password" and
            (optional) "encoding" (ignored if a session has been passed)
            or pass a single string which goes directly into the authorization header.
        :param logger: a logger for a super class
        """

        super().__init__(app=app, logger=logger)
        self.headers = {**self.headers}
        self.host = host
        self.conn_settings = conn_settings if conn_settings else {}
        self.cookie_settings = cookie_settings if cookie_settings else {}
        self.basic_auth = None
        if isinstance(auth, str):
            self.headers['Authorization'] = auth
        elif isinstance(auth, dict):
            self.basic_auth = auth
        self.session = session

    async def init(self):
        if self.closed:
            self._init()

    def _init(self):
        auth = BasicAuth(**self.basic_auth) if self.basic_auth else None
        connector = TCPConnector(verify_ssl=False, limit=256, ttl_dns_cache=60)
        self.session = ClientSession(
            connector=connector,
            cookie_jar=CookieJar(**self.cookie_settings),
            headers=self.headers,
            json_serialize=dumps,
            raise_for_status=False,
            auth=auth,
            **self.conn_settings)

    @property
    def closed(self) -> bool:
        return self.session is None or self.session.closed

    async def close(self):
        if not self.closed:
            self.logger.debug('Closing session to "%s".', self.host)
            await self.session.close()
            self.session = None
            self.logger.debug('Closed session to "%s".', self.host)

    async def iter_request(
            self, method: str, uri: str, json: dict = None, params: dict = None,
            *args, offset: int = 0, limit: int = 10,
            count_key='count', offset_key='offset', limit_key='limit',
            in_params=True, **kws) -> AsyncGenerator:
        """Iterate request by parts."""

        count = offset + 1

        if in_params:
            if params is None:
                params = {}
            pagination = params
        else:
            if json is None:
                json = {}
            pagination = params

        while count < offset:
            set_field(pagination, offset_key, offset)
            set_field(pagination, limit_key, limit)
            data = await self.request(
                method=method, uri=uri, params=params, json=json, *args, **kws)
            count = get_field(data, count_key)
            offset += limit
            yield data

    async def iter_pages(
            self, *args, page_key='page', pages_key='pages',
            params=None, data_key='data', **kws):
        """Iterates over paginated HTTP request."""

        page, pages = 0, 1
        if params is None:
            params = {}
        while page < pages:
            params[page_key] = page + 1
            data = await self.request(*args, params=params, **kws)
            page = get_field(data, page_key, default=0)
            pages = get_field(data, pages_key, default=0)
            result = get_field(data, data_key, default=None)
            yield result

    async def upload_file(
            self, uri: str, file: Union[Path, str],
            method: str = 'post', chunk_size=UPLOAD_CHUNK_SIZE):
        """A simple method for asynchronous file uploading."""

        def _read_file(path):
            with open(path, 'rb') as f:
                chunk = f.read(chunk_size)
                while chunk:
                    yield chunk
                    chunk = f.read(chunk_size)

        if type(file) is str:
            file = Path(file)
        result = await self.request(method=method, uri=uri, data=_read_file(file))
        return result

    async def rpc_request(self, uri, request, headers: Optional[dict]) -> Union[dict, list]:
        """This method depends on a specific transport."""

        return await self.request(method='post', uri=uri, json=request, headers=headers)

    async def request(
            self, method: str, uri: str, *args, data=None, json=None,
            params=None, headers=None, return_invalid_json_as_str=False, **kws) -> dict:

        """Выполняет HTTP REST запрос (аргументы аналогичны стандартным,
        но вместо URL передается URI)."""

        if self.closed:
            self._init()

        # if isinstance(params, dict):
        #     params = to_multidict(params)

        url = self.resolve(uri)
        if json:
            log_data = str(json)[:512]
        else:
            log_data = str(data)[:512]
        self.logger.debug('[%s] "%s" <- %s.', method.upper(), url, log_data)

        if headers:
            headers = {k: str(v) for k, v in headers.items()}

        async with self.session.request(
                method, url, params=params, headers=headers,
                data=data, cookies=self.session.cookie_jar._cookies,  # noqa ? pycharm
                json=json, **kws) as response:

            response.encoding = 'utf-8'
            text = await response.text()

            if response.status >= 400:
                try:
                    data = loads(text)
                except ValueError:
                    data = None
                exc = ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message=text)
                exc.data = data
                raise exc

        self.logger.debug('[%s] "%s" -> [%d] %s.', method.upper(), uri, response.status, str(text)[:512])

        if text is not None:
            try:
                text = loads(text)
            except Exception:
                if not return_invalid_json_as_str:
                    raise

        return text

    @lru_cache(maxsize=128)
    def resolve(self, uri: str) -> str:
        """Дополняет URI до полноценного URL."""

        return urljoin(self.host, uri)
