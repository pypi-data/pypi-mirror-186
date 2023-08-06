"""Object Based Storage (OBS) backend."""

from .client import Client
from .credential import Credential
from .bucket import Bucket

__all__ = ["Client", "Credential", "Bucket"]