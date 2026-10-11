# @crawlora-org/appstore — App Store API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted App Store API.
It exposes 15 API endpoints for app search, details, reviews, ratings, privacy labels, version history, charts, editorial collections, and developers through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-javascript-homepage). It does not run a browser or scrape App Store locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by App Store or its owners.

## Install

```sh
npm install @crawlora-org/appstore
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=appstore-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { AppStoreClient } from "@crawlora-org/appstore";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AppStoreClient({ apiKey });
const result1 = await client.search({ term: "podcast player" });
console.log(result1);
const result2 = await client.app({ id: "324684580" });
console.log(result2);
```

The client also exports `Client` as an alias for `AppStoreClient`. Operation
methods are available directly in camelCase and through the `appstore`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-appstore/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported App Store API endpoints

This package exposes each route below as a direct method and through the `appstore` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-appstore/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
