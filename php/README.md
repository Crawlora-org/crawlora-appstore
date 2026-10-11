# Crawlora App Store API client for PHP (`crawlora/appstore`)

This PHP package calls Crawlora's hosted App Store API at `https://api.crawlora.net/api/v1`. It exposes 15 endpoints covering app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers. It does not call or scrape App Store directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/appstore
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Appstore\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("appstore-search", ['term' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 15 API operations.

## Supported App Store API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-appstore). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md).
