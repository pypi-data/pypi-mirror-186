"""Schema."""
from .. import __version__ as _version

_schema_id = "cbwk"
_name = "hub"
_migration = None
__version__ = _version

from ._core import Account, Instance, Organization, Storage, User
