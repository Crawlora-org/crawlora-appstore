package net.crawlora.appstore;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the App Store endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 15;
    public static final List<String> OPERATION_IDS = List.of(
            "appstore-app",
            "appstore-categories",
            "appstore-collection",
            "appstore-collections",
            "appstore-developer",
            "appstore-editorial",
            "appstore-editorial-category",
            "appstore-list",
            "appstore-privacy",
            "appstore-ratings",
            "appstore-reviews",
            "appstore-search",
            "appstore-similar",
            "appstore-suggest",
            "appstore-version-history"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("appstore-app", new Operation("appstore-app", "GET", "/appstore/app", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("app_id", new Param("app_id", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv")), Map.entry("ratings", new Param("ratings", "query", false, "boolean", List.of(), "csv")), Map.entry("platforms", new Param("platforms", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-categories", new Operation("appstore-categories", "GET", "/appstore/categories", Map.of(), List.of("application/json")));
        operations.put("appstore-collection", new Operation("appstore-collection", "GET", "/appstore/collection", Map.ofEntries(Map.entry("platform", new Param("platform", "query", true, "string", List.of("iphone", "ipad", "mac", "vision", "watch", "tv"), "csv")), Map.entry("collection_id", new Param("collection_id", "query", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-collections", new Operation("appstore-collections", "GET", "/appstore/collections", Map.ofEntries(Map.entry("platform", new Param("platform", "query", true, "string", List.of("iphone", "ipad", "mac", "vision", "watch", "tv"), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-developer", new Operation("appstore-developer", "GET", "/appstore/developer/{dev_id}", Map.ofEntries(Map.entry("dev_id", new Param("dev_id", "path", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-editorial", new Operation("appstore-editorial", "GET", "/appstore/editorial", Map.ofEntries(Map.entry("device", new Param("device", "query", true, "string", List.of("iphone", "ipad", "mac", "vision", "watch", "tv"), "csv")), Map.entry("section", new Param("section", "query", false, "string", List.of("main", "arcade"), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-editorial-category", new Operation("appstore-editorial-category", "GET", "/appstore/editorial/category", Map.ofEntries(Map.entry("device", new Param("device", "query", true, "string", List.of("iphone", "ipad", "mac", "vision", "watch", "tv"), "csv")), Map.entry("category_id", new Param("category_id", "query", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-list", new Operation("appstore-list", "GET", "/appstore/list", Map.ofEntries(Map.entry("collection", new Param("collection", "query", false, "string", List.of(), "csv")), Map.entry("category", new Param("category", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv")), Map.entry("num", new Param("num", "query", false, "integer", List.of(), "csv")), Map.entry("full_detail", new Param("full_detail", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-privacy", new Operation("appstore-privacy", "GET", "/appstore/privacy/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-ratings", new Operation("appstore-ratings", "GET", "/appstore/ratings", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("app_id", new Param("app_id", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-reviews", new Operation("appstore-reviews", "GET", "/appstore/reviews", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("app_id", new Param("app_id", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of("mostRecent", "mostHelpful"), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-search", new Operation("appstore-search", "GET", "/appstore/search", Map.ofEntries(Map.entry("term", new Param("term", "query", true, "string", List.of(), "csv")), Map.entry("num", new Param("num", "query", false, "integer", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv")), Map.entry("ids_only", new Param("ids_only", "query", false, "boolean", List.of(), "csv")), Map.entry("platform", new Param("platform", "query", false, "string", List.of("phone", "pad", "mac"), "csv"))), List.of("application/json")));
        operations.put("appstore-similar", new Operation("appstore-similar", "GET", "/appstore/similar", Map.ofEntries(Map.entry("id", new Param("id", "query", false, "string", List.of(), "csv")), Map.entry("app_id", new Param("app_id", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-suggest", new Operation("appstore-suggest", "GET", "/appstore/suggest/{term}", Map.ofEntries(Map.entry("term", new Param("term", "path", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("appstore-version-history", new Operation("appstore-version-history", "GET", "/appstore/version-history/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("lang", new Param("lang", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown App Store operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object app(Map<String, ?> params) { return request("appstore-app", params); }
    public Object categories(Map<String, ?> params) { return request("appstore-categories", params); }
    public Object collection(Map<String, ?> params) { return request("appstore-collection", params); }
    public Object collections(Map<String, ?> params) { return request("appstore-collections", params); }
    public Object developer(Map<String, ?> params) { return request("appstore-developer", params); }
    public Object editorial(Map<String, ?> params) { return request("appstore-editorial", params); }
    public Object editorialCategory(Map<String, ?> params) { return request("appstore-editorial-category", params); }
    public Object list(Map<String, ?> params) { return request("appstore-list", params); }
    public Object privacy(Map<String, ?> params) { return request("appstore-privacy", params); }
    public Object ratings(Map<String, ?> params) { return request("appstore-ratings", params); }
    public Object reviews(Map<String, ?> params) { return request("appstore-reviews", params); }
    public Object search(Map<String, ?> params) { return request("appstore-search", params); }
    public Object similar(Map<String, ?> params) { return request("appstore-similar", params); }
    public Object suggest(Map<String, ?> params) { return request("appstore-suggest", params); }
    public Object versionHistory(Map<String, ?> params) { return request("appstore-version-history", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
