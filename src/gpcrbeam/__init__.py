from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version as _version

__version__: str
try:
    __version__ = _version("gpcrbeam")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["__version__"]
