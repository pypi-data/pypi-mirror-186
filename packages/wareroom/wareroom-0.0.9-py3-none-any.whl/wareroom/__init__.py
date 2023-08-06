"""Cloud storage backends."""

from .storage import Client, Credential, Bucket

__all__ = ["Client", "Credential", "Bucket"]

from . import _version

__version__ = _version.get_versions()['version']
