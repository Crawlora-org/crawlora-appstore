"""Typed App Store client for the Crawlora hosted API."""

from .platform import AppStoreClient, AsyncAppStoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = AppStoreClient
AsyncClient = AsyncAppStoreClient
__version__ = '0.1.2'
DISPLAY_NAME = 'App Store'
PLATFORM = 'appstore'
CONTRACT_REVISION = 'sha256:6211ab803d8da5196a95427c7021c31c333f10c8338fa9bd6ee32fb3a18eef21'

__all__ = [
    "AppStoreClient", "AsyncAppStoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
