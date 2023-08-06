import abc
from pathlib import Path
from typing import Union, Optional

from .services import ContextableService
from .serialization import load

__all__ = ('BaseFixtureService',)


class BaseFixtureService(ContextableService, abc.ABC):
    """Service base for fixture initialization."""

    service_name = 'fixtures'
    BASE_DIR = './fixtures'

    def __init__(self, app=None, base_dir: Union[str, Path] = BASE_DIR, logger=None):
        super().__init__(app=app, logger=logger)
        self._base_dir = Path(base_dir)
        self._base_dir.mkdir(parents=True, exist_ok=True)

    def load_file(self, filename: Union[Path, str]) -> Optional:
        """
        Loads a fixture from a file. Returns None if file doesn't exist.
        """

        if isinstance(filename, str):
            filename = self._base_dir / filename

        if not filename.exists() or filename.is_dir():
            return None
        else:
            with open(str(filename), 'r', encoding="utf8") as f:
                return load(f)
