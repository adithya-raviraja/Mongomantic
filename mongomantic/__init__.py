# type: ignore[attr-defined]
"""A MongoDB Python ORM, built on Pydantic and PyMongo."""

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


from db.core.base_repository import BaseRepository
from db.core.database import connect, disconnect
from db.core.index import Index
from db.core.mongo_model import MongoDBModel

__all__ = ["BaseRepository", "MongoDBModel", "connect", "disconnect", "Index"]
