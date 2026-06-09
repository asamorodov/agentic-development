import path from "node:path";
import { pathToFileURL } from "node:url";

export async function loadCodexSdk(): Promise<any> {
  const externalNodeModules = process.env.SOURCE_AUTOMATION_NODE_MODULES;

  if (externalNodeModules) {
    const resolved = path.join(externalNodeModules, "@openai", "codex-sdk", "dist", "index.js");
    return await import(pathToFileURL(resolved).href);
  }

  return await import("@openai/codex-sdk");
}
