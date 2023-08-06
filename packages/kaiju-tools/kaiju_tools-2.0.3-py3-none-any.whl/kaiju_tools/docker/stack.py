"""
Docker-compose support.
"""

import subprocess
import tempfile
import textwrap
import uuid
from pathlib import Path
from time import sleep
from typing import Awaitable, List, Union

from kaiju_tools.services import ContextableService
from kaiju_tools.functions import async_run_in_thread

__all__ = ['DockerStack']


class DockerStack(ContextableService):
    """
    Docker stack management class.

    You can use it in your tests or an automatic environment setup for your app.

    For more info about docker-compose see:

    https://docs.docker.com/compose/

    https://docs.docker.com/compose/compose-file/compose-file-v3/

    Usage:

    .. code-block:: python

        with DockerStack(compose_files=['compose-file.yaml', 'compose-file-dev.yaml']) as stack:
            ...

    Async context is also provided (via threaded coroutines). All async functions use internal threading wrapped
    in coroutines.

    This class is made compatible with the service context manager class thus you may init it within
    the web app as a service to start the environment before the application itself (however it's not a very fast
    way to do it since it usually takes time to start and health check containers).

    .. note::

        If you are using Pycharm run configurations you may not be able to run docker because of crippled initialization
        of $PATH in some of docker installations. What you need to do is to echo $PATH from your terminal and copy
        them to the same variable inside your run configuration environment options.

    Recommendations:

    It's recommended to give a proper name to a stack and use profiles to manage services (see docker-compose
    profiles documentation). You should also try to inherit a base compose template in your compose files for different
    environments - this is done by using a list of compose files in arguments, the first file will be sequentially
    updated by other files. This is a standard docker-compose behaviour.

    """

    COMPOSE_FILE = './docker-compose.yaml'

    def __init__(
        self, name: str, compose_files: Union[str, list] = None,
        profiles: List[str] = None, services: List[str] = None, sleep_interval=0,
        stop_before_run=True, remove_containers=True, wait_for_start=True, wait_for_stop=True, build=False,
        max_timeout=10, app=None, logger=None
    ):
        """
        :param app:
        :param compose_files: list of compose files (see official docs about compose file inheritance and format)
            by default `COMPOSE_FILE` is used
        :param name: custom docker stack (project) name
        :param profiles: list of compose profiles (see official docs about that)
        :param services: list of services to run (None means all)
        :param sleep_interval: optional sleep interval after executing a start command
        :param remove_containers: remove containers after stop
        :param wait_for_start: wait for containers ready when starting
        :param wait_for_stop: wait for containers shutdown when stopping
        :param max_timeout: max waiting time for wait_for_start and wait_for_stop commands
            in the first case it will raise an error if container is not up for an exceeded time
            in the latter case it will try to kill the container if it's up
        :param stop_before_run: stop the stack before running if it's already running
        :param build: equivalent of --build flag - build images before the start
        :param logger:
        """
        self.sleep_interval = int(sleep_interval)
        if isinstance(compose_files, str):
            compose_files = [compose_files]
        elif not compose_files:
            compose_files = [self.COMPOSE_FILE]
        self._name = name if name else str(uuid.uuid4())[:8]
        self._compose_files = tuple(Path(compose_file) for compose_file in compose_files)
        self._profiles = profiles if profiles else []
        self._services = services if services else []
        self._remove_containers = remove_containers
        self._wait_for_start = wait_for_start
        self._wait_for_stop = wait_for_stop
        self.max_timeout = max_timeout
        self._stop_before_run = stop_before_run
        self._build = build
        self._started = False
        super().__init__(app=app, logger=logger)

    @classmethod
    def from_string(cls, compose_file_str: str, compose_files: str = None, *args, **kws) -> 'DockerStack':
        """This class method allows to create an image object from a dockerfile string.

        It stores the dockerfile under a temporary name. You still will need to initiate build manually.

        :param compose_file_str: docker compose file yaml formatted string
        :param compose_files: compose file name is not required but you may pass it to store the string in a
            specific location
        :param args: see `DockerStack.__init__`
        :param kws: see `DockerStack.__init__`
        """
        compose_file_str = textwrap.dedent(compose_file_str)
        if isinstance(compose_files, (list, tuple)):
            compose_files = compose_files[0]
        if compose_files:
            with open(compose_files, mode='w') as f:
                f.write(compose_files)
        else:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                f.write(compose_file_str)
        stack = DockerStack(compose_files=f.name, *args, **kws)
        return stack

    def __enter__(self):
        if self._stop_before_run and self.running:
            self.stop()
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._remove_containers:
            self.remove()
        else:
            self.stop()

    def __repr__(self):
        return f'{self.__class__.__name__}.{self._name}'

    async def init(self):
        if self._stop_before_run and self.running:
            await self.stop_async()
        await self.start_async()

    async def close(self):
        if self._remove_containers:
            await self.remove_async()
        else:
            await self.stop_async()

    @property
    def closed(self) -> bool:
        return not self._started

    @property
    def ready(self) -> bool:
        compose_files = self._get_compose_files_cli()
        cmd = f"docker-compose {compose_files} ps | grep -E 'unhealthy|starting'"
        value = self._run_cmd(cmd, check=False)
        return not bool(value)

    @property
    def running(self) -> bool:
        compose_files = self._get_compose_files_cli()
        cmd = f"docker-compose {compose_files} ps | grep -E 'unhealthy|healthy|starting|running'"
        value = self._run_cmd(cmd, check=False)
        return bool(value)

    @property
    def exists(self) -> bool:
        compose_files = self._get_compose_files_cli()
        cmd = f"docker-compose {compose_files} ps -q --all"
        value = self._run_cmd(cmd, check=False)
        return bool(value)

    def start_async(self, *args, **kws) -> Awaitable:
        return async_run_in_thread(self.start, *args, **kws)

    def stop_async(self) -> Awaitable:
        return async_run_in_thread(self.stop)

    def remove_async(self) -> Awaitable:
        return async_run_in_thread(self.remove)

    def start(self, wait=None, build=None):
        """
        Start the container stack.

        :param wait: wait until all containers are healthy (for this option
            you must implement health check functions in all your stack services
        :param build: rebuild containers on start
        """
        if wait is None:
            wait = self._wait_for_start
        if build is None:
            build = self._build
        self.logger.info('Starting a docker stack.')
        self._check_compose_files_exist()
        compose_files = self._get_compose_files_cli()
        profiles = ' '.join(f'--profile {profile}' for profile in self._profiles)
        services = ' '.join(self._services)
        if build:
            build = '--build'
        else:
            build = ''
        cmd = f'docker-compose {compose_files} {profiles} up {build} --force-recreate -d {services}'
        self._run_cmd(cmd)
        if wait:
            self._wait_start()
        if self.sleep_interval:
            sleep(self.sleep_interval)
        self.logger.info('The docker stack should be ready by now.')
        self._started = True

    def stop(self, wait=None):
        """
        Start the container stack.

        :param wait: wait until all containers are healthy (for this option
            you must implement health check functions in all your stack services
        """
        if wait is None:
            wait = self._wait_for_stop
        self.logger.info('Stopping the docker stack.')
        compose_files = self._get_compose_files_cli()
        cmd = f'docker-compose {compose_files} stop'
        self._run_cmd(cmd)
        if wait:
            self._wait_stop()
        self.logger.info('Stopped the docker stack')
        self._started = False

    def remove(self, wait=None):
        """
        Remove the container stack.

        :param wait: wait until all containers are healthy (for this option
            you must implement health check functions in all your stack services
        """
        if wait is None:
            wait = self._wait_for_stop
        self.logger.info('Removing the docker stack.')
        compose_files = self._get_compose_files_cli()
        cmd = f'docker-compose {compose_files} rm -sfv'
        self._run_cmd(cmd)
        if wait:
            self._wait_stop()
        self.logger.info('Removed the stack.')

    def _wait_start(self):
        counter, dt = 0, 0.25
        self.logger.info('Waiting until the stack is ready.')
        while not self.ready:
            counter += dt
            sleep(dt)
            if counter > self.max_timeout:
                raise RuntimeError('Stack initialization timeout reached.')

    def _wait_stop(self):
        counter, dt = 0, 0.25
        self.logger.info('Waiting until the stack is stopped.')
        while self.running:
            counter += dt
            sleep(dt)
            if counter > self.max_timeout:
                raise RuntimeError('Stack termination timeout reached.')

    def _check_compose_files_exist(self):
        for compose_file in self._compose_files:
            if not compose_file.exists() or not compose_file.is_file():
                raise ValueError('Compose file %s does not exist.' % compose_file)

    def _get_logger_name(self):
        return self.__repr__()

    def _get_compose_files_cli(self) -> str:
        project = f'-p {self._name}'
        compose_files = ' '.join(f'-f {file}' for file in self._compose_files)
        return f'{project} {compose_files}'

    def _run_cmd(self, cmd: str, check=True) -> str:
        self.logger.debug(cmd)
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True)
        r = result.stdout.decode()
        self.logger.debug('stdout: %s', r)
        self.logger.debug('stderr: %s', result.stderr.decode())
        return r
