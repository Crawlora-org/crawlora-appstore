# App Store API endpoint reference and client usage

This reference lists all 15 public App Store API endpoints exposed by the `@crawlora-org/appstore` and `crawlora-appstore` packages, covering app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape App Store locally; Crawlora is independent from and not endorsed by App Store or its owners.

The package tracks the public API contract revision `sha256:6211ab803d8da5196a95427c7021c31c333f10c8338fa9bd6ee32fb3a18eef21` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 15 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `appstore` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `app` / `app` | `GET /appstore/app` | `id` (query, optional), `app_id` (query, optional), `country` (query, optional), `lang` (query, optional), `ratings` (query, optional), `platforms` (query, optional) | Retrieve full App Store app details |
| `categories` / `categories` | `GET /appstore/categories` | — | Retrieve App Store chart categories and collections |
| `collection` / `collection` | `GET /appstore/collection` | `platform` (query, required; values: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`), `collection_id` (query, required), `country` (query, optional), `lang` (query, optional) | Retrieve apps in one App Store collection |
| `collections` / `collections` | `GET /appstore/collections` | `platform` (query, required; values: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`), `country` (query, optional), `lang` (query, optional) | Discover App Store editorial collections |
| `developer` / `developer` | `GET /appstore/developer/{dev_id}` | `dev_id` (path, required), `country` (query, optional), `lang` (query, optional) | Retrieve apps by developer ID |
| `editorial` / `editorial` | `GET /appstore/editorial` | `device` (query, required; values: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`), `section` (query, optional; values: `main`, `arcade`), `country` (query, optional), `lang` (query, optional) | Retrieve an App Store device or Arcade editorial landing page |
| `editorialCategory` / `editorial_category` | `GET /appstore/editorial/category` | `device` (query, required; values: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`), `category_id` (query, required), `country` (query, optional), `lang` (query, optional) | Retrieve an App Store category-scoped editorial page |
| `list` / `list` | `GET /appstore/list` | `collection` (query, optional), `category` (query, optional), `country` (query, optional), `lang` (query, optional), `num` (query, optional), `full_detail` (query, optional) | Retrieve App Store collection rankings |
| `privacy` / `privacy` | `GET /appstore/privacy/{id}` | `id` (path, required), `country` (query, optional), `lang` (query, optional) | Retrieve App Store privacy disclosures |
| `ratings` / `ratings` | `GET /appstore/ratings` | `id` (query, optional), `app_id` (query, optional), `country` (query, optional), `lang` (query, optional) | Retrieve App Store ratings histogram |
| `reviews` / `reviews` | `GET /appstore/reviews` | `id` (query, optional), `app_id` (query, optional), `country` (query, optional), `page` (query, optional), `sort` (query, optional; values: `mostRecent`, `mostHelpful`), `lang` (query, optional) | Retrieve App Store reviews |
| `search` / `search` | `GET /appstore/search` | `term` (query, required), `num` (query, optional), `page` (query, optional), `country` (query, optional), `lang` (query, optional), `ids_only` (query, optional), `platform` (query, optional; values: `phone`, `pad`, `mac`) | Search the App Store |
| `similar` / `similar` | `GET /appstore/similar` | `id` (query, optional), `app_id` (query, optional), `country` (query, optional), `lang` (query, optional) | Retrieve "You Might Also Like" apps |
| `suggest` / `suggest` | `GET /appstore/suggest/{term}` | `term` (path, required), `country` (query, optional) | Retrieve App Store search suggestions |
| `versionHistory` / `version_history` | `GET /appstore/version-history/{id}` | `id` (path, required), `country` (query, optional), `lang` (query, optional) | Retrieve App Store version history |

## Client forms

- JavaScript: import `AppStoreClient` (also exported as `Client`) from `@crawlora-org/appstore`; use `new AppStoreClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `AppStoreClient` (also exported as `Client`) from `crawlora_appstore`; use `with AppStoreClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncAppStoreClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
