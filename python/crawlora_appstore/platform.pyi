from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelAppstoreVersionHistoryResponseDoc = TypedDict('ModelAppstoreVersionHistoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreVersionHistoryItem]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreVersionHistoryItem = TypedDict('ModelAppstoreVersionHistoryItem', {
    'release_date': NotRequired[str],
    'release_notes': NotRequired[str],
    'release_timestamp': NotRequired[str],
    'version_display': NotRequired[str],
}, total=False)

ModelAppstoreSuggestResponseDoc = TypedDict('ModelAppstoreSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreSuggestion]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreSuggestion = TypedDict('ModelAppstoreSuggestion', {
    'term': NotRequired[str],
}, total=False)

ModelAppstoreSimilarResponseDoc = TypedDict('ModelAppstoreSimilarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreApp]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreApp = TypedDict('ModelAppstoreApp', {
    'app_id': NotRequired[str],
    'appletv_screenshots': NotRequired[list[str]],
    'content_rating': NotRequired[str],
    'currency': NotRequired[str],
    'current_version_reviews': NotRequired[int],
    'current_version_score': NotRequired[float],
    'description': NotRequired[str],
    'developer': NotRequired[str],
    'developer_id': NotRequired[int],
    'developer_url': NotRequired[str],
    'developer_website': NotRequired[str],
    'free': NotRequired[bool],
    'genre_ids': NotRequired[list[str]],
    'genres': NotRequired[list[str]],
    'histogram': NotRequired[dict[str, int]],
    'icon': NotRequired[str],
    'id': NotRequired[int],
    'ipad_screenshots': NotRequired[list[str]],
    'languages': NotRequired[list[str]],
    'platforms': NotRequired[list[str]],
    'price': NotRequired[float],
    'primary_genre': NotRequired[str],
    'primary_genre_id': NotRequired[int],
    'ratings': NotRequired[int],
    'release_notes': NotRequired[str],
    'released': NotRequired[str],
    'required_os_version': NotRequired[str],
    'reviews': NotRequired[int],
    'score': NotRequired[float],
    'screenshots': NotRequired[list[str]],
    'size': NotRequired[str],
    'supported_devices': NotRequired[list[str]],
    'title': NotRequired[str],
    'updated': NotRequired[str],
    'url': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelAppstoreSearchResultsResponseDoc = TypedDict('ModelAppstoreSearchResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreReviewsResponseDoc = TypedDict('ModelAppstoreReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreReview]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreReview = TypedDict('ModelAppstoreReview', {
    'id': NotRequired[str],
    'score': NotRequired[int],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'updated': NotRequired[str],
    'url': NotRequired[str],
    'user_name': NotRequired[str],
    'user_url': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelAppstoreRatingsResponseDoc = TypedDict('ModelAppstoreRatingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreRatingsResult],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreRatingsResult = TypedDict('ModelAppstoreRatingsResult', {
    'histogram': NotRequired[dict[str, int]],
    'ratings': NotRequired[int],
}, total=False)

ModelAppstorePrivacyResponseDoc = TypedDict('ModelAppstorePrivacyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstorePrivacyDetails],
    'msg': NotRequired[str],
}, total=False)

ModelAppstorePrivacyDetails = TypedDict('ModelAppstorePrivacyDetails', {
    'manage_privacy_choices_url': NotRequired[str],
    'privacy_policy_url': NotRequired[str],
    'privacy_types': NotRequired[list[ModelAppstorePrivacyType]],
}, total=False)

ModelAppstorePrivacyType = TypedDict('ModelAppstorePrivacyType', {
    'data_categories': NotRequired[list[ModelAppstorePrivacyCategory]],
    'description': NotRequired[str],
    'identifier': NotRequired[str],
    'privacy_type': NotRequired[str],
    'purposes': NotRequired[list[ModelAppstorePrivacyPurpose]],
}, total=False)

ModelAppstorePrivacyPurpose = TypedDict('ModelAppstorePrivacyPurpose', {
    'data_categories': NotRequired[list[ModelAppstorePrivacyCategory]],
    'identifier': NotRequired[str],
    'purpose': NotRequired[str],
}, total=False)

ModelAppstorePrivacyCategory = TypedDict('ModelAppstorePrivacyCategory', {
    'data_category': NotRequired[str],
    'data_types': NotRequired[list[str]],
    'identifier': NotRequired[str],
}, total=False)

ModelAppstoreListResultsResponseDoc = TypedDict('ModelAppstoreListResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreEditorialResponseDoc = TypedDict('ModelAppstoreEditorialResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreEditorialPage],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreEditorialPage = TypedDict('ModelAppstoreEditorialPage', {
    'device': NotRequired[str],
    'page_id': NotRequired[str],
    'section': NotRequired[str],
    'seo_title': NotRequired[str],
    'shelves': NotRequired[list[ModelAppstoreEditorialShelf]],
    'title': NotRequired[str],
}, total=False)

ModelAppstoreEditorialShelf = TypedDict('ModelAppstoreEditorialShelf', {
    'content_type': NotRequired[str],
    'id': NotRequired[str],
    'items': NotRequired[list[ModelAppstoreEditorialItem]],
    'title': NotRequired[str],
}, total=False)

ModelAppstoreEditorialItem = TypedDict('ModelAppstoreEditorialItem', {
    'age_rating': NotRequired[str],
    'bundle_id': NotRequired[str],
    'destination_id': NotRequired[str],
    'developer_name': NotRequired[str],
    'icon_url': NotRequired[str],
    'id': NotRequired[int],
    'kind': NotRequired[str],
    'rating': NotRequired[float],
    'rating_count': NotRequired[int],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAppstoreDeveloperResponseDoc = TypedDict('ModelAppstoreDeveloperResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreApp]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreCollectionsResponseDoc = TypedDict('ModelAppstoreCollectionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelAppstoreAppStoreCollection]],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreAppStoreCollection = TypedDict('ModelAppstoreAppStoreCollection', {
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'platform': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelAppstoreCollectionResponseDoc = TypedDict('ModelAppstoreCollectionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreAppStoreCollectionPage],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreAppStoreCollectionPage = TypedDict('ModelAppstoreAppStoreCollectionPage', {
    'apps': NotRequired[list[ModelAppstoreEditorialItem]],
    'id': NotRequired[str],
    'kind': NotRequired[str],
    'platform': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelAppstoreCategoriesResponseDoc = TypedDict('ModelAppstoreCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreCategoriesResult],
    'msg': NotRequired[str],
}, total=False)

ModelAppstoreCategoriesResult = TypedDict('ModelAppstoreCategoriesResult', {
    'categories': NotRequired[list[ModelAppstoreCategoryInfo]],
    'collections': NotRequired[list[ModelAppstoreCollectionInfo]],
}, total=False)

ModelAppstoreCollectionInfo = TypedDict('ModelAppstoreCollectionInfo', {
    'active': NotRequired[bool],
    'chart_type': NotRequired[str],
    'id': NotRequired[str],
    'platform': NotRequired[str],
}, total=False)

ModelAppstoreCategoryInfo = TypedDict('ModelAppstoreCategoryInfo', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'parent_id': NotRequired[int],
}, total=False)

ModelAppstoreAppDetailsResponseDoc = TypedDict('ModelAppstoreAppDetailsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelAppstoreApp],
    'msg': NotRequired[str],
}, total=False)

AppstoreAppResponse = ModelAppstoreAppDetailsResponseDoc
AppstoreAppParams = TypedDict('AppstoreAppParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ratings': NotRequired[bool],
    'platforms': NotRequired[bool],
}, total=False)

AppstoreCategoriesResponse = ModelAppstoreCategoriesResponseDoc
AppstoreCategoriesParams = TypedDict('AppstoreCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

AppstoreCollectionResponse = ModelAppstoreCollectionResponseDoc
AppstoreCollectionParams = TypedDict('AppstoreCollectionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'collection_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionsResponse = ModelAppstoreCollectionsResponseDoc
AppstoreCollectionsParams = TypedDict('AppstoreCollectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreDeveloperResponse = ModelAppstoreDeveloperResponseDoc
AppstoreDeveloperParams = TypedDict('AppstoreDeveloperParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialResponse = ModelAppstoreEditorialResponseDoc
AppstoreEditorialParams = TypedDict('AppstoreEditorialParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'section': NotRequired[Literal['main', 'arcade']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialCategoryResponse = ModelAppstoreEditorialResponseDoc
AppstoreEditorialCategoryParams = TypedDict('AppstoreEditorialCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'category_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreListResponse = ModelAppstoreListResultsResponseDoc
AppstoreListParams = TypedDict('AppstoreListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'num': NotRequired[int],
    'full_detail': NotRequired[bool],
}, total=False)

AppstorePrivacyResponse = ModelAppstorePrivacyResponseDoc
AppstorePrivacyParams = TypedDict('AppstorePrivacyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreRatingsResponse = ModelAppstoreRatingsResponseDoc
AppstoreRatingsParams = TypedDict('AppstoreRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreReviewsResponse = ModelAppstoreReviewsResponseDoc
AppstoreReviewsParams = TypedDict('AppstoreReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['mostRecent', 'mostHelpful']],
    'lang': NotRequired[str],
}, total=False)

AppstoreSearchResponse = ModelAppstoreSearchResultsResponseDoc
AppstoreSearchParams = TypedDict('AppstoreSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'num': NotRequired[int],
    'page': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ids_only': NotRequired[bool],
    'platform': NotRequired[Literal['phone', 'pad', 'mac']],
}, total=False)

AppstoreSimilarResponse = ModelAppstoreSimilarResponseDoc
AppstoreSimilarParams = TypedDict('AppstoreSimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreSuggestResponse = ModelAppstoreSuggestResponseDoc
AppstoreSuggestParams = TypedDict('AppstoreSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppstoreVersionHistoryResponse = ModelAppstoreVersionHistoryResponseDoc
AppstoreVersionHistoryParams = TypedDict('AppstoreVersionHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

class AppstoreGroup:
    @overload
    def app(self, **params: Unpack[AppstoreAppStreamParams]) -> BinaryIO: ...
    @overload
    def app(self, **params: Unpack[AppstoreAppTextResponseParams]) -> str: ...
    @overload
    def app(self, **params: Unpack[AppstoreAppDefaultParams]) -> AppstoreAppResponse: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesDefaultParams]) -> AppstoreCategoriesResponse: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionStreamParams]) -> BinaryIO: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionTextResponseParams]) -> str: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionDefaultParams]) -> AppstoreCollectionResponse: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsTextResponseParams]) -> str: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsDefaultParams]) -> AppstoreCollectionsResponse: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperTextResponseParams]) -> str: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperDefaultParams]) -> AppstoreDeveloperResponse: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialStreamParams]) -> BinaryIO: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialTextResponseParams]) -> str: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialDefaultParams]) -> AppstoreEditorialResponse: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryTextResponseParams]) -> str: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryDefaultParams]) -> AppstoreEditorialCategoryResponse: ...
    @overload
    def list(self, **params: Unpack[AppstoreListStreamParams]) -> BinaryIO: ...
    @overload
    def list(self, **params: Unpack[AppstoreListTextResponseParams]) -> str: ...
    @overload
    def list(self, **params: Unpack[AppstoreListDefaultParams]) -> AppstoreListResponse: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyStreamParams]) -> BinaryIO: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyTextResponseParams]) -> str: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyDefaultParams]) -> AppstorePrivacyResponse: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsTextResponseParams]) -> str: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsDefaultParams]) -> AppstoreRatingsResponse: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsDefaultParams]) -> AppstoreReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchDefaultParams]) -> AppstoreSearchResponse: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarStreamParams]) -> BinaryIO: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarTextResponseParams]) -> str: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarDefaultParams]) -> AppstoreSimilarResponse: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestDefaultParams]) -> AppstoreSuggestResponse: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryTextResponseParams]) -> str: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryDefaultParams]) -> AppstoreVersionHistoryResponse: ...

OperationId = Literal[
    'appstore-app',
    'appstore-categories',
    'appstore-collection',
    'appstore-collections',
    'appstore-developer',
    'appstore-editorial',
    'appstore-editorial-category',
    'appstore-list',
    'appstore-privacy',
    'appstore-ratings',
    'appstore-reviews',
    'appstore-search',
    'appstore-similar',
    'appstore-suggest',
    'appstore-version-history',
]

class CrawloraClient:
    appstore: AppstoreGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-app'],
        params: AppstoreAppParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreAppResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-categories'],
        params: AppstoreCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-collection'],
        params: AppstoreCollectionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCollectionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-collections'],
        params: AppstoreCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCollectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-developer'],
        params: AppstoreDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreDeveloperResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-editorial'],
        params: AppstoreEditorialParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreEditorialResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-editorial-category'],
        params: AppstoreEditorialCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreEditorialCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-list'],
        params: AppstoreListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-privacy'],
        params: AppstorePrivacyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstorePrivacyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-ratings'],
        params: AppstoreRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreRatingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-reviews'],
        params: AppstoreReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-search'],
        params: AppstoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-similar'],
        params: AppstoreSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-suggest'],
        params: AppstoreSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['appstore-version-history'],
        params: AppstoreVersionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreVersionHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-app'],
        params: AppstoreAppParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreAppResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-categories'],
        params: AppstoreCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-collection'],
        params: AppstoreCollectionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCollectionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-collections'],
        params: AppstoreCollectionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreCollectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-developer'],
        params: AppstoreDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreDeveloperResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-editorial'],
        params: AppstoreEditorialParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreEditorialResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-editorial-category'],
        params: AppstoreEditorialCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreEditorialCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-list'],
        params: AppstoreListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-privacy'],
        params: AppstorePrivacyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstorePrivacyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-ratings'],
        params: AppstoreRatingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreRatingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-reviews'],
        params: AppstoreReviewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-search'],
        params: AppstoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-similar'],
        params: AppstoreSimilarParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-suggest'],
        params: AppstoreSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['appstore-version-history'],
        params: AppstoreVersionHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> AppstoreVersionHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class AppStoreClient(CrawloraClient):
    def __enter__(self) -> AppStoreClient: ...
    @overload
    def app(self, **params: Unpack[AppstoreAppStreamParams]) -> BinaryIO: ...
    @overload
    def app(self, **params: Unpack[AppstoreAppTextResponseParams]) -> str: ...
    @overload
    def app(self, **params: Unpack[AppstoreAppDefaultParams]) -> AppstoreAppResponse: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[AppstoreCategoriesDefaultParams]) -> AppstoreCategoriesResponse: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionStreamParams]) -> BinaryIO: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionTextResponseParams]) -> str: ...
    @overload
    def collection(self, **params: Unpack[AppstoreCollectionDefaultParams]) -> AppstoreCollectionResponse: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsTextResponseParams]) -> str: ...
    @overload
    def collections(self, **params: Unpack[AppstoreCollectionsDefaultParams]) -> AppstoreCollectionsResponse: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperTextResponseParams]) -> str: ...
    @overload
    def developer(self, **params: Unpack[AppstoreDeveloperDefaultParams]) -> AppstoreDeveloperResponse: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialStreamParams]) -> BinaryIO: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialTextResponseParams]) -> str: ...
    @overload
    def editorial(self, **params: Unpack[AppstoreEditorialDefaultParams]) -> AppstoreEditorialResponse: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryTextResponseParams]) -> str: ...
    @overload
    def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryDefaultParams]) -> AppstoreEditorialCategoryResponse: ...
    @overload
    def list(self, **params: Unpack[AppstoreListStreamParams]) -> BinaryIO: ...
    @overload
    def list(self, **params: Unpack[AppstoreListTextResponseParams]) -> str: ...
    @overload
    def list(self, **params: Unpack[AppstoreListDefaultParams]) -> AppstoreListResponse: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyStreamParams]) -> BinaryIO: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyTextResponseParams]) -> str: ...
    @overload
    def privacy(self, **params: Unpack[AppstorePrivacyDefaultParams]) -> AppstorePrivacyResponse: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsTextResponseParams]) -> str: ...
    @overload
    def ratings(self, **params: Unpack[AppstoreRatingsDefaultParams]) -> AppstoreRatingsResponse: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[AppstoreReviewsDefaultParams]) -> AppstoreReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[AppstoreSearchDefaultParams]) -> AppstoreSearchResponse: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarStreamParams]) -> BinaryIO: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarTextResponseParams]) -> str: ...
    @overload
    def similar(self, **params: Unpack[AppstoreSimilarDefaultParams]) -> AppstoreSimilarResponse: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[AppstoreSuggestDefaultParams]) -> AppstoreSuggestResponse: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryTextResponseParams]) -> str: ...
    @overload
    def version_history(self, **params: Unpack[AppstoreVersionHistoryDefaultParams]) -> AppstoreVersionHistoryResponse: ...

class AsyncAppStoreClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncAppStoreClient: ...
    appstore: _AsyncAppstoreGroup
    @overload
    async def app(self, **params: Unpack[AppstoreAppStreamParams]) -> BinaryIO: ...
    @overload
    async def app(self, **params: Unpack[AppstoreAppTextResponseParams]) -> str: ...
    @overload
    async def app(self, **params: Unpack[AppstoreAppDefaultParams]) -> AppstoreAppResponse: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesDefaultParams]) -> AppstoreCategoriesResponse: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionStreamParams]) -> BinaryIO: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionTextResponseParams]) -> str: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionDefaultParams]) -> AppstoreCollectionResponse: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsTextResponseParams]) -> str: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsDefaultParams]) -> AppstoreCollectionsResponse: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperTextResponseParams]) -> str: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperDefaultParams]) -> AppstoreDeveloperResponse: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialStreamParams]) -> BinaryIO: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialTextResponseParams]) -> str: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialDefaultParams]) -> AppstoreEditorialResponse: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryTextResponseParams]) -> str: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryDefaultParams]) -> AppstoreEditorialCategoryResponse: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListStreamParams]) -> BinaryIO: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListTextResponseParams]) -> str: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListDefaultParams]) -> AppstoreListResponse: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyStreamParams]) -> BinaryIO: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyTextResponseParams]) -> str: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyDefaultParams]) -> AppstorePrivacyResponse: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsTextResponseParams]) -> str: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsDefaultParams]) -> AppstoreRatingsResponse: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsDefaultParams]) -> AppstoreReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchDefaultParams]) -> AppstoreSearchResponse: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarTextResponseParams]) -> str: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarDefaultParams]) -> AppstoreSimilarResponse: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestDefaultParams]) -> AppstoreSuggestResponse: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryTextResponseParams]) -> str: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryDefaultParams]) -> AppstoreVersionHistoryResponse: ...

class _AsyncAppstoreGroup:
    @overload
    async def app(self, **params: Unpack[AppstoreAppStreamParams]) -> BinaryIO: ...
    @overload
    async def app(self, **params: Unpack[AppstoreAppTextResponseParams]) -> str: ...
    @overload
    async def app(self, **params: Unpack[AppstoreAppDefaultParams]) -> AppstoreAppResponse: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[AppstoreCategoriesDefaultParams]) -> AppstoreCategoriesResponse: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionStreamParams]) -> BinaryIO: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionTextResponseParams]) -> str: ...
    @overload
    async def collection(self, **params: Unpack[AppstoreCollectionDefaultParams]) -> AppstoreCollectionResponse: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsTextResponseParams]) -> str: ...
    @overload
    async def collections(self, **params: Unpack[AppstoreCollectionsDefaultParams]) -> AppstoreCollectionsResponse: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperTextResponseParams]) -> str: ...
    @overload
    async def developer(self, **params: Unpack[AppstoreDeveloperDefaultParams]) -> AppstoreDeveloperResponse: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialStreamParams]) -> BinaryIO: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialTextResponseParams]) -> str: ...
    @overload
    async def editorial(self, **params: Unpack[AppstoreEditorialDefaultParams]) -> AppstoreEditorialResponse: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryTextResponseParams]) -> str: ...
    @overload
    async def editorial_category(self, **params: Unpack[AppstoreEditorialCategoryDefaultParams]) -> AppstoreEditorialCategoryResponse: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListStreamParams]) -> BinaryIO: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListTextResponseParams]) -> str: ...
    @overload
    async def list(self, **params: Unpack[AppstoreListDefaultParams]) -> AppstoreListResponse: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyStreamParams]) -> BinaryIO: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyTextResponseParams]) -> str: ...
    @overload
    async def privacy(self, **params: Unpack[AppstorePrivacyDefaultParams]) -> AppstorePrivacyResponse: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsTextResponseParams]) -> str: ...
    @overload
    async def ratings(self, **params: Unpack[AppstoreRatingsDefaultParams]) -> AppstoreRatingsResponse: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[AppstoreReviewsDefaultParams]) -> AppstoreReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[AppstoreSearchDefaultParams]) -> AppstoreSearchResponse: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarTextResponseParams]) -> str: ...
    @overload
    async def similar(self, **params: Unpack[AppstoreSimilarDefaultParams]) -> AppstoreSimilarResponse: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[AppstoreSuggestDefaultParams]) -> AppstoreSuggestResponse: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryTextResponseParams]) -> str: ...
    @overload
    async def version_history(self, **params: Unpack[AppstoreVersionHistoryDefaultParams]) -> AppstoreVersionHistoryResponse: ...

AppstoreAppDefaultParams = TypedDict('AppstoreAppDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ratings': NotRequired[bool],
    'platforms': NotRequired[bool],
}, total=False)

AppstoreAppTextResponseParams = TypedDict('AppstoreAppTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ratings': NotRequired[bool],
    'platforms': NotRequired[bool],
}, total=False)

AppstoreAppStreamParams = TypedDict('AppstoreAppStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ratings': NotRequired[bool],
    'platforms': NotRequired[bool],
}, total=False)

AppstoreCategoriesDefaultParams = TypedDict('AppstoreCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

AppstoreCategoriesTextResponseParams = TypedDict('AppstoreCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

AppstoreCategoriesStreamParams = TypedDict('AppstoreCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

AppstoreCollectionDefaultParams = TypedDict('AppstoreCollectionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'collection_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionTextResponseParams = TypedDict('AppstoreCollectionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'collection_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionStreamParams = TypedDict('AppstoreCollectionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'collection_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionsDefaultParams = TypedDict('AppstoreCollectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionsTextResponseParams = TypedDict('AppstoreCollectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreCollectionsStreamParams = TypedDict('AppstoreCollectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'platform': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreDeveloperDefaultParams = TypedDict('AppstoreDeveloperDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreDeveloperTextResponseParams = TypedDict('AppstoreDeveloperTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreDeveloperStreamParams = TypedDict('AppstoreDeveloperStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'dev_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialDefaultParams = TypedDict('AppstoreEditorialDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'section': NotRequired[Literal['main', 'arcade']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialTextResponseParams = TypedDict('AppstoreEditorialTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'section': NotRequired[Literal['main', 'arcade']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialStreamParams = TypedDict('AppstoreEditorialStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'section': NotRequired[Literal['main', 'arcade']],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialCategoryDefaultParams = TypedDict('AppstoreEditorialCategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'category_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialCategoryTextResponseParams = TypedDict('AppstoreEditorialCategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'category_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreEditorialCategoryStreamParams = TypedDict('AppstoreEditorialCategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'device': Required[Literal['iphone', 'ipad', 'mac', 'vision', 'watch', 'tv']],
    'category_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreListDefaultParams = TypedDict('AppstoreListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'num': NotRequired[int],
    'full_detail': NotRequired[bool],
}, total=False)

AppstoreListTextResponseParams = TypedDict('AppstoreListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'num': NotRequired[int],
    'full_detail': NotRequired[bool],
}, total=False)

AppstoreListStreamParams = TypedDict('AppstoreListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection': NotRequired[str],
    'category': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'num': NotRequired[int],
    'full_detail': NotRequired[bool],
}, total=False)

AppstorePrivacyDefaultParams = TypedDict('AppstorePrivacyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstorePrivacyTextResponseParams = TypedDict('AppstorePrivacyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstorePrivacyStreamParams = TypedDict('AppstorePrivacyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreRatingsDefaultParams = TypedDict('AppstoreRatingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreRatingsTextResponseParams = TypedDict('AppstoreRatingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreRatingsStreamParams = TypedDict('AppstoreRatingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreReviewsDefaultParams = TypedDict('AppstoreReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['mostRecent', 'mostHelpful']],
    'lang': NotRequired[str],
}, total=False)

AppstoreReviewsTextResponseParams = TypedDict('AppstoreReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['mostRecent', 'mostHelpful']],
    'lang': NotRequired[str],
}, total=False)

AppstoreReviewsStreamParams = TypedDict('AppstoreReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['mostRecent', 'mostHelpful']],
    'lang': NotRequired[str],
}, total=False)

AppstoreSearchDefaultParams = TypedDict('AppstoreSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'term': Required[str],
    'num': NotRequired[int],
    'page': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ids_only': NotRequired[bool],
    'platform': NotRequired[Literal['phone', 'pad', 'mac']],
}, total=False)

AppstoreSearchTextResponseParams = TypedDict('AppstoreSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'term': Required[str],
    'num': NotRequired[int],
    'page': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ids_only': NotRequired[bool],
    'platform': NotRequired[Literal['phone', 'pad', 'mac']],
}, total=False)

AppstoreSearchStreamParams = TypedDict('AppstoreSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'term': Required[str],
    'num': NotRequired[int],
    'page': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'ids_only': NotRequired[bool],
    'platform': NotRequired[Literal['phone', 'pad', 'mac']],
}, total=False)

AppstoreSimilarDefaultParams = TypedDict('AppstoreSimilarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreSimilarTextResponseParams = TypedDict('AppstoreSimilarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreSimilarStreamParams = TypedDict('AppstoreSimilarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': NotRequired[str],
    'app_id': NotRequired[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreSuggestDefaultParams = TypedDict('AppstoreSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppstoreSuggestTextResponseParams = TypedDict('AppstoreSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppstoreSuggestStreamParams = TypedDict('AppstoreSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'term': Required[str],
    'country': NotRequired[str],
}, total=False)

AppstoreVersionHistoryDefaultParams = TypedDict('AppstoreVersionHistoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreVersionHistoryTextResponseParams = TypedDict('AppstoreVersionHistoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

AppstoreVersionHistoryStreamParams = TypedDict('AppstoreVersionHistoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)
