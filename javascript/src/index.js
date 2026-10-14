import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class AppStoreClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-appstore-js/0.1.2" });
    this["app"] = (...args) => this.request("appstore-app", ...args);
    this["categories"] = (...args) => this.request("appstore-categories", ...args);
    this["collection"] = (...args) => this.request("appstore-collection", ...args);
    this["collections"] = (...args) => this.request("appstore-collections", ...args);
    this["developer"] = (...args) => this.request("appstore-developer", ...args);
    this["editorial"] = (...args) => this.request("appstore-editorial", ...args);
    this["editorialCategory"] = (...args) => this.request("appstore-editorial-category", ...args);
    this["list"] = (...args) => this.request("appstore-list", ...args);
    this["privacy"] = (...args) => this.request("appstore-privacy", ...args);
    this["ratings"] = (...args) => this.request("appstore-ratings", ...args);
    this["reviews"] = (...args) => this.request("appstore-reviews", ...args);
    this["search"] = (...args) => this.request("appstore-search", ...args);
    this["similar"] = (...args) => this.request("appstore-similar", ...args);
    this["suggest"] = (...args) => this.request("appstore-suggest", ...args);
    this["versionHistory"] = (...args) => this.request("appstore-version-history", ...args);
  }
}

export { AppStoreClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.2";
export default AppStoreClient;
