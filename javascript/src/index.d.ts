import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class AppStoreClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  app(params?: OperationParamsMap["appstore-app"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params?: OperationParamsMap["appstore-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collection(params: OperationParamsMap["appstore-collection"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  collections(params: OperationParamsMap["appstore-collections"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  developer(params: OperationParamsMap["appstore-developer"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  editorial(params: OperationParamsMap["appstore-editorial"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  editorialCategory(params: OperationParamsMap["appstore-editorial-category"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  list(params?: OperationParamsMap["appstore-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  privacy(params: OperationParamsMap["appstore-privacy"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ratings(params?: OperationParamsMap["appstore-ratings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  reviews(params?: OperationParamsMap["appstore-reviews"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["appstore-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  similar(params?: OperationParamsMap["appstore-similar"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  suggest(params: OperationParamsMap["appstore-suggest"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  versionHistory(params: OperationParamsMap["appstore-version-history"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  app(params?: OperationParamsMap["appstore-app"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params?: OperationParamsMap["appstore-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collection(params: OperationParamsMap["appstore-collection"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  collections(params: OperationParamsMap["appstore-collections"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  developer(params: OperationParamsMap["appstore-developer"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  editorial(params: OperationParamsMap["appstore-editorial"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  editorialCategory(params: OperationParamsMap["appstore-editorial-category"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  list(params?: OperationParamsMap["appstore-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  privacy(params: OperationParamsMap["appstore-privacy"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ratings(params?: OperationParamsMap["appstore-ratings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  reviews(params?: OperationParamsMap["appstore-reviews"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["appstore-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  similar(params?: OperationParamsMap["appstore-similar"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  suggest(params: OperationParamsMap["appstore-suggest"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  versionHistory(params: OperationParamsMap["appstore-version-history"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  app(...args: OperationRequestArgs<"appstore-app">): Promise<OperationResponseMap["appstore-app"]>;
  categories(...args: OperationRequestArgs<"appstore-categories">): Promise<OperationResponseMap["appstore-categories"]>;
  collection(...args: OperationRequestArgs<"appstore-collection">): Promise<OperationResponseMap["appstore-collection"]>;
  collections(...args: OperationRequestArgs<"appstore-collections">): Promise<OperationResponseMap["appstore-collections"]>;
  developer(...args: OperationRequestArgs<"appstore-developer">): Promise<OperationResponseMap["appstore-developer"]>;
  editorial(...args: OperationRequestArgs<"appstore-editorial">): Promise<OperationResponseMap["appstore-editorial"]>;
  editorialCategory(...args: OperationRequestArgs<"appstore-editorial-category">): Promise<OperationResponseMap["appstore-editorial-category"]>;
  list(...args: OperationRequestArgs<"appstore-list">): Promise<OperationResponseMap["appstore-list"]>;
  privacy(...args: OperationRequestArgs<"appstore-privacy">): Promise<OperationResponseMap["appstore-privacy"]>;
  ratings(...args: OperationRequestArgs<"appstore-ratings">): Promise<OperationResponseMap["appstore-ratings"]>;
  reviews(...args: OperationRequestArgs<"appstore-reviews">): Promise<OperationResponseMap["appstore-reviews"]>;
  search(...args: OperationRequestArgs<"appstore-search">): Promise<OperationResponseMap["appstore-search"]>;
  similar(...args: OperationRequestArgs<"appstore-similar">): Promise<OperationResponseMap["appstore-similar"]>;
  suggest(...args: OperationRequestArgs<"appstore-suggest">): Promise<OperationResponseMap["appstore-suggest"]>;
  versionHistory(...args: OperationRequestArgs<"appstore-version-history">): Promise<OperationResponseMap["appstore-version-history"]>;
}
export { AppStoreClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default AppStoreClient;
