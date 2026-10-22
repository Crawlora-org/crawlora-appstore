# Crawlora App Store Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `15`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| appstore | `appstore.app` | `appstore-app` | `GET /appstore/app` | `id` (query String)<br>`app_id` (query String)<br>`country` (query String)<br>`lang` (query String)<br>`ratings` (query bool)<br>`platforms` (query bool) | `ApiKeyAuth` | `AppstoreAppResponse` |  |
| appstore | `appstore.categories` | `appstore-categories` | `GET /appstore/categories` | none | `ApiKeyAuth` | `AppstoreCategoriesResponse` |  |
| appstore | `appstore.collection` | `appstore-collection` | `GET /appstore/collection` | `platform` (query String enum{iphone, ipad, mac, vision, watch, tv} required)<br>`collection_id` (query String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreCollectionResponse` |  |
| appstore | `appstore.collections` | `appstore-collections` | `GET /appstore/collections` | `platform` (query String enum{iphone, ipad, mac, vision, watch, tv} required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreCollectionsResponse` |  |
| appstore | `appstore.developer` | `appstore-developer` | `GET /appstore/developer/{dev_id}` | `dev_id` (path String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreDeveloperResponse` |  |
| appstore | `appstore.editorial` | `appstore-editorial` | `GET /appstore/editorial` | `device` (query String enum{iphone, ipad, mac, vision, watch, tv} required)<br>`section` (query String enum{main, arcade})<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreEditorialResponse` |  |
| appstore | `appstore.editorial_category` | `appstore-editorial-category` | `GET /appstore/editorial/category` | `device` (query String enum{iphone, ipad, mac, vision, watch, tv} required)<br>`category_id` (query String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreEditorialCategoryResponse` |  |
| appstore | `appstore.list` | `appstore-list` | `GET /appstore/list` | `collection` (query String)<br>`category` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`num` (query i64)<br>`full_detail` (query bool) | `ApiKeyAuth` | `AppstoreListResponse` |  |
| appstore | `appstore.privacy` | `appstore-privacy` | `GET /appstore/privacy/{id}` | `id` (path String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstorePrivacyResponse` |  |
| appstore | `appstore.ratings` | `appstore-ratings` | `GET /appstore/ratings` | `id` (query String)<br>`app_id` (query String)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreRatingsResponse` |  |
| appstore | `appstore.reviews` | `appstore-reviews` | `GET /appstore/reviews` | `id` (query String)<br>`app_id` (query String)<br>`country` (query String)<br>`page` (query i64)<br>`sort` (query String enum{mostRecent, mostHelpful})<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreReviewsResponse` |  |
| appstore | `appstore.search` | `appstore-search` | `GET /appstore/search` | `term` (query String required)<br>`num` (query i64)<br>`page` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`ids_only` (query bool)<br>`platform` (query String enum{phone, pad, mac}) | `ApiKeyAuth` | `AppstoreSearchResponse` |  |
| appstore | `appstore.similar` | `appstore-similar` | `GET /appstore/similar` | `id` (query String)<br>`app_id` (query String)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreSimilarResponse` |  |
| appstore | `appstore.suggest` | `appstore-suggest` | `GET /appstore/suggest/{term}` | `term` (path String required)<br>`country` (query String) | `ApiKeyAuth` | `AppstoreSuggestResponse` |  |
| appstore | `appstore.version_history` | `appstore-version-history` | `GET /appstore/version-history/{id}` | `id` (path String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `AppstoreVersionHistoryResponse` |  |
