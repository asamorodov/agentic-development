import { readFile, mkdir, readdir } from "node:fs/promises";
import path from "node:path";
import { exists, passArtifactPaths, safeDocName } from "./path-utils.js";

export interface PassValidationResult {
  afterPass: string;
  delta: string;
  shouldStop: string;
  shouldStopValue: "yes" | "no";
}

export async function validatePassArtifacts(repoRoot: string, docPath: string, passNumber: number): Promise<PassValidationResult> {
  const paths = passArtifactPaths(repoRoot, docPath, passNumber);
  const missing: string[] = [];
  for (const filePath of [paths.afterPass, paths.delta, paths.shouldStop]) {
    if (!(await exists(filePath))) missing.push(path.relative(repoRoot, filePath));
  }
  if (missing.length > 0) throw new Error(`Pass ${paths.pass} did not produce required artifacts: ${missing.join(", ")}`);
  const rawShouldStop = (await readFile(paths.shouldStop, "utf8")).trim().toLowerCase();
  if (rawShouldStop !== "yes" && rawShouldStop !== "no") {
    throw new Error(`Invalid should_stop value in ${path.relative(repoRoot, paths.shouldStop)}: ${JSON.stringify(rawShouldStop)}`);
  }
  return { afterPass: paths.afterPass, delta: paths.delta, shouldStop: paths.shouldStop, shouldStopValue: rawShouldStop };
}

export async function ensurePassDir(repoRoot: string, docPath: string): Promise<void> {
  await mkdir(path.join(repoRoot, "passes", safeDocName(docPath)), { recursive: true });
}

export async function detectLastPass(repoRoot: string, docPath: string): Promise<number> {
  const safeName = safeDocName(docPath);
  const passDir = path.join(repoRoot, "passes", safeName);
  if (!(await exists(passDir))) return 0;
  const entries = await readdir(passDir);
  let max = 0;
  const pattern = new RegExp(`^${escapeRegExp(safeName)}_after_pass_(\\d+)\\.md$`);
  for (const entry of entries) {
    const match = entry.match(pattern);
    if (match) max = Math.max(max, Number(match[1]));
  }
  return max;
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
