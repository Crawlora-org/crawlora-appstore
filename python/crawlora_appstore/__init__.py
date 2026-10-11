"""Typed App Store client for the Crawlora hosted API."""

from .platform import AppStoreClient, AsyncAppStoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AppStoreClient
AsyncClient = AsyncAppStoreClient
__version__ = '0.1.0'
DISPLAY_NAME = 'App Store'
PLATFORM = 'appstore'
CONTRACT_REVISION = 'sha256:d75b3ce6c6708361cbf9dc8413d9ab462e6d66aa3b363abf15289cb39c0cc986'

__all__ = [
    "AppStoreClient", "AsyncAppStoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
