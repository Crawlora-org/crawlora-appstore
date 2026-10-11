# App Store clients for Crawlora

Official Crawlora client packages for the hosted App Store API. Access 15 API endpoints covering app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape App Store locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by App Store or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/appstore`](javascript/README.md)
- Python: [`crawlora-appstore`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-appstore`](go.mod)
- Ruby: [`crawlora-appstore`](ruby/README.md)
- Java: [`net.crawlora:crawlora-appstore:0.1.1`](java/README.md)
- PHP: [`crawlora/appstore`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 15 selected public App Store API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
