import asyncio
import logging
from time import time
from uuid import uuid4

import pytest

from ...serialization import dumps, loads
from ...rpc.jsonrpc import *
from ...rpc.tests.fixtures import *
from ...rpc.services import JSONRPCServer
from ...rpc.etc import JSONRPCHeaders
from ..views import JSONRPCView


# @pytest.mark.benchmark
# async def test_rest_rpc_queued_server_performance(
#         aiohttp_client, web_application, system_information, logger):
#
#     async def _test(parallel=1, requests=1000):
#
#         logger.setLevel('ERROR')
#         aiohttp_logger = logging.getLogger('aiohttp')
#         aiohttp_logger.setLevel('ERROR')
#         counter = 0
#
#         async def _do_call(client):
#             nonlocal counter
#             app_id = str(uuid4())
#             data = {"method": "do.sleep", "params": [1, 2, 3]}
#             while 1:
#                 _id = uuid4()
#                 data['id'] = _id.int
#                 headers = {
#                     JSONRPCHeaders.APP_ID_HEADER: str(app_id),
#                     JSONRPCHeaders.CORRELATION_ID_HEADER: str(uuid4()),
#                     'Content-Type': 'application/json'
#                 }
#                 await client.post(
#                     '/rpc', data=dumps(data), headers=headers,
#                     skip_auto_headers=['User-Agent'])
#                 counter += 1
#
#         def _do_sleep(*_, **__):
#             return True
#
#         async with JSONRPCHeaders(max_parallel_tasks=16, logger=logger) as rpc:
#             rpc.register_namespace('do', {'sleep': _do_sleep}, {})
#             web_application.router.add_view('/rpc', JSONRPCView)
#             web_application.rpc = web_application['rpc'] = rpc
#             client = await aiohttp_client(web_application)
#
#             tasks = [
#                 asyncio.ensure_future(_do_call(client))
#                 for _ in range(parallel)
#             ]
#
#             t0 = time()
#             while counter < requests:
#                 await asyncio.sleep(1)
#             t1 = time()
#
#             for task in tasks:
#                 task.cancel()
#             await client.close()
#             return t1 - t0, counter
#
#     requests, parallel, n = 5000, 16, 5
#     print(f'\nJSON RPC Queued Service simple benchmark (best of {n}).')
#     print(f'{parallel} connections\n')
#     print(system_information)
#
#     dt, counter = await _test(parallel, requests)
#
#     print(f'{round(dt, 2)} s')
#     print(f'{counter} requests')
#     print(f'{round(counter / dt, 1)} req/sec')
#

@pytest.mark.asyncio
async def test_rpc_rest_view(
        rpc_interface,
        aiohttp_client, application, rpc_compatible_service, logger):

    logger.info('Testing service context initialization.')
    application = application()

    async with rpc_interface as rpc:
        service = rpc_compatible_service(logger=logger)
        rpc.register_service(service.service_name, service)
        application.router.add_view(JSONRPCView.route, JSONRPCView)
        application.rpc = application['rpc'] = rpc
        client = await aiohttp_client(application)

        logger.info('Testing basic functionality.')

        app_id = uuid4()
        correlation_id = uuid4()

        headers = {
            JSONRPCHeaders.APP_ID_HEADER: str(app_id),
            JSONRPCHeaders.CORRELATION_ID_HEADER: str(correlation_id),
            'Content-Type': 'application/json'
        }
        data = {'id': uuid4().int, 'method': 'm.echo', 'params': {'a': 1, 'b': 2, 'c': 3}}
        data = dumps(data)
        response = await client.post(JSONRPCView.route, data=data, headers=headers)
        assert response.status == 200
        text = await response.text()
        body = loads(text)
        logger.info(body)
        assert body['result'][1] == {'a': 1, 'b': 2, 'c': 3}

        logger.info('Testing batch functionality.')

        headers = {
            JSONRPCHeaders.APP_ID_HEADER: str(app_id),
            JSONRPCHeaders.CORRELATION_ID_HEADER: str(correlation_id),
            'Content-Type': 'application/json'
        }
        data = [
            {'id': uuid4().int, 'method': 'm.echo', 'params': {'a': 1}},
            {'id': uuid4().int, 'method': 'm.echo', 'params': None},
            {'id': uuid4().int, 'method': 'm.echo'}
        ]
        headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = str(uuid4())
        data = dumps(data)
        response = await client.post(JSONRPCView.route, data=data, headers=headers)
        assert response.status == 200
        text = await response.text()
        body = loads(text)
        logger.info(body)
        assert [r['result'] for r in body] == [
            [[], {'a': 1}],
            [[], {}],
            [[], {}]
        ]
        logger.info('All tests finished.')
