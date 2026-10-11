import { AppStoreClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new AppStoreClient({ apiKey });

  const search = await client.search({ term: "podcast player" });
  console.log("search", search);
  const app = await client.app({ id: "324684580" });
  console.log("app", app);
