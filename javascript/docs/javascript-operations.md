# Crawlora App Store JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `15`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| appstore | `appstore.app` | `appstore-app` | `GET /appstore/app` | `id` (query string)<br>`app_id` (query string)<br>`country` (query string)<br>`lang` (query string)<br>`ratings` (query boolean)<br>`platforms` (query boolean) | `ApiKeyAuth` | `AppstoreAppResponse` |  |
| appstore | `appstore.categories` | `appstore-categories` | `GET /appstore/categories` | none | `ApiKeyAuth` | `AppstoreCategoriesResponse` |  |
| appstore | `appstore.collection` | `appstore-collection` | `GET /appstore/collection` | `platform` (query "iphone" \| "ipad" \| "mac" \| "vision" \| "watch" \| "tv" required)<br>`collection_id` (query string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreCollectionResponse` |  |
| appstore | `appstore.collections` | `appstore-collections` | `GET /appstore/collections` | `platform` (query "iphone" \| "ipad" \| "mac" \| "vision" \| "watch" \| "tv" required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreCollectionsResponse` |  |
| appstore | `appstore.developer` | `appstore-developer` | `GET /appstore/developer/{dev_id}` | `dev_id` (path string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreDeveloperResponse` |  |
| appstore | `appstore.editorial` | `appstore-editorial` | `GET /appstore/editorial` | `device` (query "iphone" \| "ipad" \| "mac" \| "vision" \| "watch" \| "tv" required)<br>`section` (query "main" \| "arcade")<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreEditorialResponse` |  |
| appstore | `appstore.editorialCategory` | `appstore-editorial-category` | `GET /appstore/editorial/category` | `device` (query "iphone" \| "ipad" \| "mac" \| "vision" \| "watch" \| "tv" required)<br>`category_id` (query string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreEditorialCategoryResponse` |  |
| appstore | `appstore.list` | `appstore-list` | `GET /appstore/list` | `collection` (query string)<br>`category` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`num` (query number)<br>`full_detail` (query boolean) | `ApiKeyAuth` | `AppstoreListResponse` |  |
| appstore | `appstore.privacy` | `appstore-privacy` | `GET /appstore/privacy/{id}` | `id` (path string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstorePrivacyResponse` |  |
| appstore | `appstore.ratings` | `appstore-ratings` | `GET /appstore/ratings` | `id` (query string)<br>`app_id` (query string)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreRatingsResponse` |  |
| appstore | `appstore.reviews` | `appstore-reviews` | `GET /appstore/reviews` | `id` (query string)<br>`app_id` (query string)<br>`country` (query string)<br>`page` (query number)<br>`sort` (query "mostRecent" \| "mostHelpful")<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreReviewsResponse` |  |
| appstore | `appstore.search` | `appstore-search` | `GET /appstore/search` | `term` (query string required)<br>`num` (query number)<br>`page` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`ids_only` (query boolean)<br>`platform` (query "phone" \| "pad" \| "mac") | `ApiKeyAuth` | `AppstoreSearchResponse` |  |
| appstore | `appstore.similar` | `appstore-similar` | `GET /appstore/similar` | `id` (query string)<br>`app_id` (query string)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreSimilarResponse` |  |
| appstore | `appstore.suggest` | `appstore-suggest` | `GET /appstore/suggest/{term}` | `term` (path string required)<br>`country` (query string) | `ApiKeyAuth` | `AppstoreSuggestResponse` |  |
| appstore | `appstore.versionHistory` | `appstore-version-history` | `GET /appstore/version-history/{id}` | `id` (path string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `AppstoreVersionHistoryResponse` |  |
