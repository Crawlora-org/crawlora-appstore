<?php

declare(strict_types=1);

namespace Crawlora\Appstore;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'appstore';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 15;
    public const OPERATION_IDS = ["appstore-app", "appstore-categories", "appstore-collection", "appstore-collections", "appstore-developer", "appstore-editorial", "appstore-editorial-category", "appstore-list", "appstore-privacy", "appstore-ratings", "appstore-reviews", "appstore-search", "appstore-similar", "appstore-suggest", "appstore-version-history"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"appstore-app": {"bodyParam": null, "bodyRequired": false, "id": "appstore-app", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"default": false, "description": "Include ratings histogram", "in": "query", "name": "ratings", "type": "boolean"}, {"default": false, "description": "Include the full device-platform compatibility list (adds one extra upstream fetch)", "in": "query", "name": "platforms", "type": "boolean"}], "path": "/appstore/app", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "ratings", "type": "boolean"}, {"in": "query", "name": "platforms", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "appstore-categories": {"bodyParam": null, "bodyRequired": false, "id": "appstore-categories", "method": "GET", "params": [], "path": "/appstore/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "appstore-collection": {"bodyParam": null, "bodyRequired": false, "id": "appstore-collection", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Room ID or EDS UUID collection ID from appstore_collections", "in": "query", "name": "collection_id", "required": true, "type": "string", "x-example": "6757461219"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/collection", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string"}, {"in": "query", "name": "collection_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-collections": {"bodyParam": null, "bodyRequired": false, "id": "appstore-collections", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "platform", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-developer": {"bodyParam": null, "bodyRequired": false, "id": "appstore-developer", "method": "GET", "params": [{"description": "Developer artist ID", "in": "path", "name": "dev_id", "required": true, "type": "string", "x-example": "284882218"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/developer/{dev_id}", "pathParams": ["dev_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-editorial": {"bodyParam": null, "bodyRequired": false, "id": "appstore-editorial", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string", "x-example": "iphone"}, {"default": "main", "description": "Editorial section within the device", "enum": ["main", "arcade"], "in": "query", "name": "section", "type": "string"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/editorial", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string"}, {"enum": ["main", "arcade"], "in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-editorial-category": {"bodyParam": null, "bodyRequired": false, "id": "appstore-editorial-category", "method": "GET", "params": [{"description": "Apple device catalog", "enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Numeric App Store editorial page ID, discovered from appstore_editorial (same device)", "in": "query", "name": "category_id", "required": true, "type": "string", "x-example": "6503709728"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/editorial/category", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["iphone", "ipad", "mac", "vision", "watch", "tv"], "in": "query", "name": "device", "required": true, "type": "string"}, {"in": "query", "name": "category_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-list": {"bodyParam": null, "bodyRequired": false, "id": "appstore-list", "method": "GET", "params": [{"description": "Chart collection slug, see description for the full enum", "in": "query", "name": "collection", "type": "string", "x-example": "topfreeapplications"}, {"description": "Numeric App Store category ID, see description for the full enum; e.g. 6014 = Games, 7012 = Games/Puzzle", "in": "query", "name": "category", "type": "integer", "x-example": 6014}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Number of apps to return", "in": "query", "name": "num", "type": "integer", "x-example": 50}, {"default": false, "description": "Expand each app via lookup API", "in": "query", "name": "full_detail", "type": "boolean"}], "path": "/appstore/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "collection", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "full_detail", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "appstore-privacy": {"bodyParam": null, "bodyRequired": false, "id": "appstore-privacy", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "324684580"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/privacy/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-ratings": {"bodyParam": null, "bodyRequired": false, "id": "appstore-ratings", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/ratings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-reviews": {"bodyParam": null, "bodyRequired": false, "id": "appstore-reviews", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Review page number (1-10)", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"default": "mostRecent", "description": "Sort order", "enum": ["mostRecent", "mostHelpful"], "in": "query", "name": "sort", "type": "string"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["mostRecent", "mostHelpful"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-search": {"bodyParam": null, "bodyRequired": false, "id": "appstore-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "term", "required": true, "type": "string", "x-example": "panda"}, {"description": "Number of apps per page", "in": "query", "name": "num", "type": "integer", "x-example": 50}, {"description": "Search page number (1-based)", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"default": false, "description": "Return only app IDs", "in": "query", "name": "ids_only", "type": "boolean"}, {"default": "phone", "description": "App Store catalog to search: phone, pad, mac", "enum": ["phone", "pad", "mac"], "in": "query", "name": "platform", "type": "string"}], "path": "/appstore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "term", "required": true, "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "ids_only", "type": "boolean"}, {"enum": ["phone", "pad", "mac"], "in": "query", "name": "platform", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-similar": {"bodyParam": null, "bodyRequired": false, "id": "appstore-similar", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "query", "name": "id", "type": "string", "x-example": "553834731"}, {"description": "App Store bundle ID", "in": "query", "name": "app_id", "type": "string", "x-example": "com.midasplayer.apps.candycrushsaga"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/similar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "type": "string"}, {"in": "query", "name": "app_id", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-suggest": {"bodyParam": null, "bodyRequired": false, "id": "appstore-suggest", "method": "GET", "params": [{"description": "Partial search term", "in": "path", "name": "term", "required": true, "type": "string", "x-example": "panda"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}], "path": "/appstore/suggest/{term}", "pathParams": ["term"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}], "security": ["ApiKeyAuth"]}, "appstore-version-history": {"bodyParam": null, "bodyRequired": false, "id": "appstore-version-history", "method": "GET", "params": [{"description": "App Store numeric track ID (digits only)", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "553834731"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Result language tag", "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/appstore/version-history/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-appstore-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function app(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-app", $params, $responseType);
    }
    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-categories", $params, $responseType);
    }
    public function collection(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-collection", $params, $responseType);
    }
    public function collections(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-collections", $params, $responseType);
    }
    public function developer(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-developer", $params, $responseType);
    }
    public function editorial(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-editorial", $params, $responseType);
    }
    public function editorial_category(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-editorial-category", $params, $responseType);
    }
    public function list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-list", $params, $responseType);
    }
    public function privacy(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-privacy", $params, $responseType);
    }
    public function ratings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-ratings", $params, $responseType);
    }
    public function reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-reviews", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-search", $params, $responseType);
    }
    public function similar(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-similar", $params, $responseType);
    }
    public function suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-suggest", $params, $responseType);
    }
    public function version_history(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("appstore-version-history", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
