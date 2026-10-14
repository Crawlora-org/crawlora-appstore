# Crawlora App Store API client for Java

The official Java client for Crawlora's hosted App Store API. It exposes 15 endpoints covering app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-appstore</artifactId>
  <version>0.1.2</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-java-console) to get an API key.

```java
import net.crawlora.appstore.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("term", "podcast player")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported App Store API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/appstore/app` | `appstore-app` | Retrieve full App Store app details |
| `GET` | `/appstore/categories` | `appstore-categories` | Retrieve App Store chart categories and collections |
| `GET` | `/appstore/collection` | `appstore-collection` | Retrieve apps in one App Store collection |
| `GET` | `/appstore/collections` | `appstore-collections` | Discover App Store editorial collections |
| `GET` | `/appstore/developer/{dev_id}` | `appstore-developer` | Retrieve apps by developer ID |
| `GET` | `/appstore/editorial` | `appstore-editorial` | Retrieve an App Store device or Arcade editorial landing page |
| `GET` | `/appstore/editorial/category` | `appstore-editorial-category` | Retrieve an App Store category-scoped editorial page |
| `GET` | `/appstore/list` | `appstore-list` | Retrieve App Store collection rankings |
| `GET` | `/appstore/privacy/{id}` | `appstore-privacy` | Retrieve App Store privacy disclosures |
| `GET` | `/appstore/ratings` | `appstore-ratings` | Retrieve App Store ratings histogram |
| `GET` | `/appstore/reviews` | `appstore-reviews` | Retrieve App Store reviews |
| `GET` | `/appstore/search` | `appstore-search` | Search the App Store |
| `GET` | `/appstore/similar` | `appstore-similar` | Retrieve "You Might Also Like" apps |
| `GET` | `/appstore/suggest/{term}` | `appstore-suggest` | Retrieve App Store search suggestions |
| `GET` | `/appstore/version-history/{id}` | `appstore-version-history` | Retrieve App Store version history |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-appstore)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-java-api-docs)
