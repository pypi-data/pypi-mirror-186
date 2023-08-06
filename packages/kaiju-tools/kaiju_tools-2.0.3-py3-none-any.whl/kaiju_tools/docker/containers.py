"""
Docker container management.
"""

import uuid
from time import sleep
from typing import Awaitable, Union

try:
    import docker
    from docker.errors import NotFound
except ModuleNotFoundError:
    pass

from kaiju_tools.services import ContextableService
from kaiju_tools.functions import async_run_in_thread
from .images import DockerImage

__all__ = ['DockerContainer']


class DockerContainer(ContextableService):
    """
    Single docker container management.

    You can use it in your tests or an automatic environment setup for your app.

    See the official Docker documentation for init parameters description.

    Usage:

    .. code-block:: python

        with DockerContainer('postgres', 'latest', 'my_postgres', ports={5444: 5432}) as c:
            ...

    Or with a docker image object:

    .. code-block:: python

        img = DockerImage('my_image')

        with DockerContainer(img, 'latest', 'my_postgres', ports={5444: 5432}) as c:
            ...

    Async versions of commands and the context are supported. All async functions use internal threading wrapped
    in coroutines.

    This class is made compatible with the service context manager class thus you may init it within
    the web app as a service to start the environment before the application itself (however it's not a very fast
    way to do it since it usually takes time to start and health check containers).
    """

    image_class = DockerImage  #: wraps dict or str `image` param in __init__

    def __init__(
        self, image: Union[str, image_class._Dict, image_class], name: str = None, command: str = None,
        ports: dict = None, env: dict = None, healthcheck: dict = None, sleep_interval=0,
        remove_on_exit=False, stop_before_run=True, wait_for_start=True, wait_for_stop=True,
        max_timeout=10, app=None, logger=None, **run_args
    ):
        """
        :param image: image tag string or an image object, in case of a dict or str argument
            it will be automatically wrapped in `DockerImage` class
        :param env: environment variables
        :param command: command to run
        :param name: container name
        :param ports: port mappings
        :param healthcheck: optional docker healthcheck
        :param sleep_interval: optional sleep interval after executing a start command
        :param remove_on_exit: remove the image on context exit
        :param wait_for_start: wait for containers ready when starting
        :param wait_for_stop: wait for containers stopped when stopping
        :param stop_before_run: stop container before running if it's already running
        :param max_timeout: max waiting time for wait_for_start and wait_for_stop commands
            in the first case it will raise an error if container is not up for an exceeded time
            in the latter case it will try to kill the container if it's up
        :param run_args: other docker run command arguments
        :param logger:
        """
        self._docker_cli = docker.from_env()
        self._command = command
        self._env = env
        self._name = name if name else str(uuid.uuid4())[:8]
        self._ports = ports
        self._healthcheck = healthcheck
        self._remove_on_exit = remove_on_exit
        self._wait_for_start = wait_for_start
        self._wait_for_stop = wait_for_stop
        self._stop_before_run = stop_before_run
        self.sleep_interval = float(sleep_interval)
        self.max_timeout = float(max_timeout)
        self._run_args = run_args
        self._container = None
        self._started = False
        super().__init__(app=app, logger=logger)
        self._image = self._init_image_from_args(image)

    def __repr__(self):
        return f'{self.__class__.__name__}.{self._name}'

    def __enter__(self):
        if self._remove_on_exit:
            self.remove()
        self._image.__enter__()
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._image.__exit__(exc_type, exc_val, exc_tb)
        self.stop()
        if self._remove_on_exit:
            self.remove()

    async def init(self):
        if self._remove_on_exit:
            await self.remove_async()
        await self._image.init()
        await self.start_async()

    async def close(self):
        await self.stop_async()
        await self._image.close()
        if self._remove_on_exit:
            await self.remove_async()

    @property
    def closed(self) -> bool:
        return not self._started

    @property
    def metadata(self) -> Union[dict, None]:
        """Returns docker container metadata or None if container doesn't exist."""
        try:
            return self._docker_cli.api.inspect_container(self._name)
        except NotFound:
            return None

    @property
    def exists(self) -> bool:
        return self.metadata is not None

    @property
    def status(self) -> Union[str, None]:
        """Return a container status string."""
        return self._get_status(self.metadata)

    @property
    def running(self) -> bool:
        return self.status == 'running'

    @property
    def healthy(self) -> bool:
        return self.status == 'healthy'

    @property
    def exited(self) -> bool:
        return self.status == 'exited'

    @property
    def ready(self) -> bool:
        metadata = self.metadata
        status = self._get_status(metadata)
        exit_code = metadata['State']['ExitCode']
        return any([
            self._healthcheck and status == 'healthy',
            not self._healthcheck and status == 'running',
            status == 'exited' and exit_code == 0
        ])

    def start_async(self, *args, **kws) -> Awaitable:
        return async_run_in_thread(self.start, *args, **kws)

    def stop_async(self, *args, **kws) -> Awaitable:
        return async_run_in_thread(self.stop, *args, **kws)

    def remove_async(self, *args, **kws) -> Awaitable:
        return async_run_in_thread(self.remove, *args, **kws)

    def start(self, wait=None):
        """
        Run a container.

        If the container is already exists it will be restarted using `docker start` command. You can suppress this
        behaviour by setting `remove_on_exit` to True.

        :param wait: wait until the container is running and healthy
        """
        image = self._image.fullname
        if wait is None:
            wait = self._wait_for_start

        if self.exists:
            self.logger.info('Starting a previously stopped container.')
            self._container = self._docker_cli.api.start(self._name)
        else:
            self.logger.info('Starting a new container.')
            self._container = self._docker_cli.containers.run(
                image, environment=self._env, command=self._command, name=self._name,
                ports=self._ports, auto_remove=False, detach=True, healthcheck=self._healthcheck,
                **self._run_args)

        if wait:
            self._wait_start()

        if self.sleep_interval:
            sleep(self.sleep_interval)

        self._started = True
        self.logger.info('Started.')

    def stop(self, wait=None):
        """
        Stop a running container.

        :param wait: wait for containers stopped when stopping
        """
        if wait is None:
            wait = self._wait_for_stop

        self.logger.info('Stopping the container.')
        if self.running:
            self._docker_cli.api.stop(self._name)

        if wait:
            self._wait_stop()

        self._container = None
        self._started = False
        self.logger.info('Stopped.')

    def pause(self):
        if self.running:
            self._container.pause()

    def unpause(self):
        if self.running:
            self._container.unpause()

    def remove(self):
        """Remove a container (delete its state)."""
        self.logger.info('Removing the container.')
        if self.exists:
            self._docker_cli.api.remove_container(self._name, force=True)
        self.logger.info('Removed the container.')

    def _get_logger_name(self):
        return self.__repr__()

    def _get_status(self, metadata):
        if not metadata:
            return None
        if self._healthcheck:
            status = metadata['State']['Health']['Status'].lower()
        else:
            status = metadata['State']['Status'].lower()
        return status

    def _wait_start(self):
        counter, dt = 0, 0.25
        self.logger.info('Waiting until the container is ready.')
        while not self.ready:
            counter += dt
            sleep(dt)
            if counter > self.max_timeout:
                raise RuntimeError('Container initialization timeout reached.')

    def _wait_stop(self):
        counter, dt = 0, 0.25
        self.logger.info('Waiting until the container is stopped.')
        while self.running:
            counter += dt
            sleep(dt)
            if counter > self.max_timeout:
                self.logger.info('Killing the container.')
                self._docker_cli.api.kill(self._name)
                break

    def _init_image_from_args(self, image) -> DockerImage:
        if isinstance(image, dict):
            if 'dockerfile_str' in image:
                image = self.image_class.from_string(**image)
            else:
                image = self.image_class(**image)
        elif isinstance(image, str):
            image = self.image_class(tag=image, app=self.app, logger=self.logger)
        return image
