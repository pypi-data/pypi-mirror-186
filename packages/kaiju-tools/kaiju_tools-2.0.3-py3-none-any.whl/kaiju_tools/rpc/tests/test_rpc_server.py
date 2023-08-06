import asyncio
from time import time
from uuid import uuid4

import pytest

from ..services import JSONRPCServer
from ..etc import JSONRPCHeaders
from ..jsonrpc import *
from .fixtures import *


@pytest.mark.asyncio
async def test_rpc_server_methods(rpc_interface, rpc_compatible_service, logger):
    logger.info('Testing service context initialization.')

    async with rpc_interface as rpc:

        service = rpc_compatible_service(logger=logger)
        rpc.register_service(service.service_name, service)

        app_id = uuid4()
        correlation_id = uuid4()

        headers = {
            JSONRPCHeaders.APP_ID_HEADER: app_id,
            JSONRPCHeaders.CORRELATION_ID_HEADER: correlation_id
        }

        logger.info('Testing basic requests.')

        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        data = {'id': uuid4().int, 'method': 'm.echo', 'params': None}
        _headers, response = await rpc.call(data, headers)
        assert _headers[JSONRPCHeaders.APP_ID_HEADER] == str(app_id)
        assert _headers[JSONRPCHeaders.CORRELATION_ID_HEADER] == str(correlation_id)
        assert response.result == ((), {})

        data = {'id': uuid4().int, 'method': 'm.echo', 'params': {'value': 42}}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert response.result[1]['value'] == 42

        data = {'id': uuid4().int, 'method': 'm.aecho', 'params': {'a': 1, 'b': 2, 'c': 3}}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert response.result[1] == {'a': 1, 'b': 2, 'c': 3}

        data = {'id': uuid4().int, 'method': 'm.echo', 'params': {'x': True}}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert response.result == ((), {'x': True})

        logger.info('Testing data validation.')

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11, 'b': 2}}
        _headers, response = await rpc.call(data, headers)
        assert response.result == 22

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11, 'b': 's'}}
        _headers, response = await rpc.call(data, headers)
        logger.debug(response.repr())
        assert isinstance(response, InvalidParams)

        # testing custom validator
        data = {'id': uuid4().int, 'method': 'm.validated_2', 'params': {'a': 11, 'b': 's'}}
        _headers, response = await rpc.call(data, headers)
        logger.debug(response.repr())
        assert isinstance(response, InvalidParams)

        data = {'id': uuid4().int, 'method': 'm.validated', 'params': {'a': 11}}
        _headers, response = await rpc.call(data, headers)
        logger.debug(response.repr())
        assert isinstance(response, InvalidParams)

        logger.info('Testing multi requests.')

        headers = {
            JSONRPCHeaders.APP_ID_HEADER: app_id,
            JSONRPCHeaders.CORRELATION_ID_HEADER: correlation_id
        }

        data = [
            {'id': uuid4().int, 'method': 'm.echo', 'params': {'x': True}},
            {'id': uuid4().int, 'method': 'm.echo', 'params': {'a': 1, 'b': 2}},
            {'id': uuid4().int, 'method': 'm.aecho', 'params': {'a': 1, 'b': 2}}
        ]
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert _headers[JSONRPCHeaders.APP_ID_HEADER] == str(app_id)
        assert _headers[JSONRPCHeaders.CORRELATION_ID_HEADER] == str(correlation_id)
        assert [r.result for r in response] == [
            ((), {'x': True}),
            ((), {'a': 1, 'b': 2}),
            ((), {'a': 1, 'b': 2})
        ]

        logger.info('Testing request error handling.')

        headers = {
            JSONRPCHeaders.APP_ID_HEADER: app_id,
            JSONRPCHeaders.CORRELATION_ID_HEADER: correlation_id
        }

        data = {'id': uuid4().int, 'method': 'm.unknown', 'params': {'x': True}}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert _headers[JSONRPCHeaders.APP_ID_HEADER] == str(app_id)
        assert _headers[JSONRPCHeaders.CORRELATION_ID_HEADER] == str(correlation_id)
        assert isinstance(response, MethodNotFound)

        data = {'id': uuid4().int}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, InvalidRequest)

        data = {'id': uuid4().int, 'method': 'm.unknown', 'params': {'value': True}, 'shit': 1}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, InvalidRequest)

        data = {'id': uuid4().int, 'method': 'm.sum', 'params': {'x': 1, 'z': '2'}}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, InvalidParams)

        data = {'id': uuid4().int, 'method': 'm.fail', 'params': None}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, InternalError)

        logger.info('Testing timeouts.')

        data = {'id': uuid4().int, 'method': 'm.long_echo', 'params': None}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, RequestTimeout)

        data = {'id': uuid4().int, 'method': 'm.long_echo', 'params': None}
        headers[JSONRPCHeaders.REQUEST_TIMEOUT_HEADER] = 10
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response, RPCResponse)

        logger.info('Testing notifications.')

        data = {'id': None, 'method': 'm.echo', 'params': None}
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        t = time()
        _headers, response = await rpc.call(data, headers)
        t = time() - t
        assert response is None
        assert t < 1

        logger.info('Testing for parallel task execution')

        tasks = []

        for _ in range(4):
            data = {'id': uuid4().int, 'method': 'm.standard_echo', 'params': None}
            headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
            headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = correlation_id
            tasks.append(rpc.call(data, headers))

        t = time()
        await asyncio.gather(*tasks)
        t = time() - t
        assert t <= 1

        logger.info('Testing separate bulk request error handling.')

        data = [
            {'id': None, 'method': 'm.echo', 'params': None},
            {'id': None, 'method': 'm.long_echo', 'params': None},
            {'id': uuid4().int, 'method': 'm.fail', 'params': None},
            {'id': uuid4().int, 'method': 'm.sum', 'params': {'x': 1, 'y': 2}}
        ]
        headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = int(time() + 1)
        _headers, response = await rpc.call(data, headers)
        assert isinstance(response[0], RequestTimeout)
        assert isinstance(response[1], RPCError)
        assert response[2].result == 1 + 2

        logger.info('Testing invalid headers.')

        # headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = 'str'
        # data = {'id': uuid4().int, 'method': 'm.echo', 'params': None},
        # _headers, response = await rpc.call(data, headers)
        # assert isinstance(response, InvalidRequest)
        #
        # headers[JSONRPCHeaders.REQUEST_TIMEOUT_HEADER] = 'str'
        # data = {'id': uuid4().int, 'method': 'm.echo', 'params': None},
        # _headers, response = await rpc.call(data, headers)
        # assert isinstance(response, InvalidRequest)
        #
        # headers[JSONRPCHeaders.APP_ID_HEADER] = 'not_uuid'
        # data = {'id': uuid4().int, 'method': 'm.echo', 'params': None},
        # _headers, response = await rpc.call(data, headers)
        # assert isinstance(response, InvalidRequest)
        #
        # headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = 'not_uuid'
        # data = {'id': uuid4().int, 'method': 'm.echo', 'params': None},
        # _headers, response = await rpc.call(data, headers)
        # assert isinstance(response, InvalidRequest)

        logger.info('All tests finished.')
