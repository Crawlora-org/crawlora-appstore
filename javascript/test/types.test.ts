import { AppStoreClient } from "../src/index.js";

const client = new AppStoreClient({ apiKey: "test-key" });
void client.collection({"platform": "iphone", "collection_id": "sample"});
void client.request("appstore-collection", {"platform": "iphone", "collection_id": "sample"});
const streamResponse: Promise<Response> = client.request("appstore-collection", {"platform": "iphone", "collection_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("appstore-collection", {"platform": "iphone", "collection_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.collection({"platform": "iphone", "collection_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("appstore-collection", {"platform": "iphone", "collection_id": "sample", "country": "sample", "lang": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("appstore-collection", {"platform": "iphone", "collection_id": "sample"}, { responseType: "text" });
void rawText;


void client.app();
void client.request("appstore-app");
// @ts-expect-error The selected operation requires its documented params.
void client.collection();
