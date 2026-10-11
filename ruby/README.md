# Crawlora App Store API client for Ruby (`crawlora-appstore`)

This Ruby gem calls Crawlora's hosted App Store API at `https://api.crawlora.net/api/v1`. It exposes 15 endpoints covering app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers; it does not call or scrape App Store directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-appstore"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/appstore"

client = Crawlora::Appstore::Client.new
result = client.request("appstore-search", JSON.parse("{\"term\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 15 API operations.

```ruby
client = Crawlora::Appstore::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported App Store API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-appstore) for account setup, the API operation reference, and release history.
