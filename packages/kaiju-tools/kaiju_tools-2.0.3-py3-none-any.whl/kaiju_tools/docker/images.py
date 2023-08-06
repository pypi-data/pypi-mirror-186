"""
Docker images build services.
"""

import tempfile
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Awaitable, Optional

try:
    from typing import TypedDict
except ImportError:
    # python 3.6 compatibility
    from typing_extensions import TypedDict

try:
    import docker
    from docker.errors import NotFound
except ModuleNotFoundError:
    pass

from kaiju_tools.services import ContextableService
from kaiju_tools.functions import async_run_in_thread

__all__ = ['DockerImage']


class DockerImage(ContextableService):
    """
    Docker image builder. Builds docker images from dockerfiles.

    Usage:

    .. code-block:: python

        img = DockerImage('myapp')
        img.build()

    Within a service context (it can remove image automatically on exit):

    .. code-block:: python

        with DockerImage('myapp') as img:
            ...

    Async versions of commands and the context are supported. All async functions use internal threading wrapped
    in coroutines.

    This class is made compatible with the service context manager class thus you may init it within the web app as a
    service to start the environment before the application itself (however it's not a very fast way to do it since
    it usually takes time to start and health check containers).
    """

    DOCKERFILE = './Dockerfile'
    NAMESPACE = 'systems.elemento'
    REPOSITORY = 'docker.io'

    _tempfile_prefix = '_docker_image'

    class _Dict:
        """Used for type hinting in docker container class."""
        tag: str
        version: str
        dockerfile: str
        labels: dict
        namespace: str
        remove_on_exit: bool
        always_build: bool
        pull: bool
        repository: str

    def __init__(
        self, tag: str, version: str = 'latest', dockerfile=DOCKERFILE, labels: dict = None, namespace=NAMESPACE,
        remove_on_exit=False, always_build=False, pull=True, repository=REPOSITORY,
        app=None, logger=None, **build_params
    ):
        """
        :param tag: base image tag, for example "mysite.com/myapp"
        :param version: version tag (latest by default)
        :param dockerfile: dockerfile location, uses `DOCKERFILE` by default
        :param labels: optional dictionary of labels, namespace will be automatically prefixed to the keys
        :param namespace: label namespace, usually it should be reversed domain of your organization
            about namespaces and labels you can use `opencontainers.org` conventions as reference

            https://github.com/opencontainers/image-spec/blob/master/annotations.md

        :param remove_on_exit: remove the image on context exit
        :param pull: will try to pull first before trying to build it locally
        :param repository: docker repository url
        :param always_build: always rebuild the image even if it exists
        :param logger:
        :param build_params: other build parameters for docker `build` command
        """
        self._docker_cli = docker.from_env()
        self._build_params = build_params
        self.tag = tag
        self.version = version
        self.fullname = f'{tag}:{version}'
        self.namespace = namespace
        self.dockerfile = Path(dockerfile)
        self.labels = labels if labels else {}
        self.repo = Path(repository)
        self._image = None
        self._pull = pull
        self._remove_on_exit = remove_on_exit
        self._always_build = always_build
        super().__init__(app=app, logger=logger)

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.tag}'

    def __enter__(self):
        if self._pull and not self.exists:
            try:
                self.pull()
            except NotFound:
                self.logger.info('Image not found in repo.')
            else:
                return self
        if self._always_build or not self.exists:
            self.build()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._remove_on_exit:
            self.remove()

    async def init(self):
        if self._pull and not self.exists:
            try:
                await self.pull_async()
            except NotFound:
                self.logger.info('Image not found in repo.')
            else:
                return
        if self._always_build or not self.exists:
            await self.build_async()

    async def close(self):
        if self._remove_on_exit:
            await self.remove_async()

    @property
    def closed(self) -> bool:
        return not self._image

    @property
    def metadata(self) -> Optional[dict]:
        """Returns docker metadata about the image or None if it doesn't exist."""
        images = self._docker_cli.images.list(name=self.fullname)
        meta = next((i.attrs for i in images if self.fullname in i.tags), None)
        return meta

    @property
    def exists(self) -> bool:
        return self.metadata is not None

    @classmethod
    def from_string(cls, dockerfile_str: str, dockerfile: str = None, *args, **kws) -> 'DockerImage':
        """This class method allows to create an image object from a dockerfile string.

        It stores the dockerfile under a temporary name. You still will need to initiate build manually.

        :param dockerfile_str: dockerfile string in docker format
        :param dockerfile: here dockerfile name is not required but you may pass it to store the image string at a
            specific location
        :param args: see `DockerImage.__init__`
        :param kws: see `DockerImage.__init__`
        """
        dockerfile_str = textwrap.dedent(dockerfile_str)
        if dockerfile:
            with open(dockerfile, mode='w') as f:
                f.write(dockerfile_str)
        else:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                f.write(dockerfile_str)
        image = DockerImage(dockerfile=f.name, *args, **kws)
        return image

    def build_async(self) -> Awaitable:
        return async_run_in_thread(self.build)

    def remove_async(self) -> Awaitable:
        return async_run_in_thread(self.remove)

    def pull_async(self) -> Awaitable:
        return async_run_in_thread(self.pull)

    def build(self):
        """Build a docker image. It may take a lot of time (depending on your dockerfile)."""
        self.logger.info('Building a docker image from %s.', self.dockerfile)
        self._check_dockerfile_exists()
        with open(self.dockerfile, mode='rb') as f:
            self._image = self._docker_cli.images.build(
                fileobj=f, tag=self.fullname, labels=self._get_labels(), **self._build_params)
        self.logger.info('Successfully built a docker image with tag %s.', self.tag)

    def pull(self):
        self.logger.info('Pulling image %s from %s.', self.fullname, self.repo)
        url = str(self.repo / self.tag)
        self._docker_cli.images.pull(repository=url, tag=self.version)
        self.logger.info('Pulled a new image.')

    def remove(self):
        self.logger.info('Removing the docker image.')
        self._docker_cli.images.remove(image=self.fullname, force=True)
        self._image = None
        self.logger.info('Successfully removed the docker image.')

    def _check_dockerfile_exists(self):
        if not self.dockerfile.exists() or not self.dockerfile.is_file():
            raise ValueError('Dockerfile %s does not exist.' % self.dockerfile)

    def _get_labels(self) -> dict:
        labels = {
            'created': datetime.now().isoformat()
        }
        labels.update(self.labels)
        labels = {f'{self.namespace}.{key}': str(value) for key, value in labels.items()}
        return labels

    def _get_logger_name(self):
        return self.__repr__()
