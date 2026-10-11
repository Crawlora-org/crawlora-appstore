import os

from crawlora_appstore import AppStoreClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with AppStoreClient(api_key=api_key) as client:
    search = client.search(term='podcast player')
    print('search', search)
    app = client.app(id='324684580')
    print('app', app)
