import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { findRepoRootSync } from "./path-utils.js";
import { loadCodexSdk } from "./load-codex-sdk.js";

type ProbeStatus = "PASS" | "FAIL" | "INCONCLUSIVE";

interface ProbeResult {
  status: ProbeStatus;
  runId: string;
  startedAt: string;
  finishedAt: string;
  cwdBefore: string;
  repoRoot: string;
  sdkImported: boolean;
  threadStarted: boolean;
  childRunCompleted: boolean;
  debugFileExists: boolean;
  error?: string;
}

function getArg(name: string, fallback?: string): string {
  const index = process.argv.indexOf(`--${name}`);
  if (index >= 0 && process.argv[index + 1]) return process.argv[index + 1];
  if (fallback !== undefined) return fallback;
  throw new Error(`Missing required argument --${name}`);
}

async function pathExists(filePath: string): Promise<boolean> {
  try {
    await readFile(filePath, "utf8");
    return true;
  } catch {
    return false;
  }
}

async function main(): Promise<void> {
  const runId = getArg("run-id", `sdk-probe-${new Date().toISOString().replace(/[:.]/g, "-")}`);
  const repoRoot = path.resolve(getArg("repo-root", findRepoRootSync(process.cwd())));
  const automationRoot = path.join(repoRoot, "work", "automation");
  const runDir = path.join(automationRoot, "runs", runId, "sdk-probe");
  const debugFile = path.join(automationRoot, "debug", "SDK_PROBE.md");

  await mkdir(runDir, { recursive: true });
  await mkdir(path.dirname(debugFile), { recursive: true });

  const prompt = [
    "You are a Codex SDK child thread probe.",
    "",
    `Repository root: ${repoRoot.replaceAll(path.sep, "/")}`,
    "Treat all relative paths as relative to the repository root above.",
    "",
    "Task:",
    `1. Create or update this file exactly: ${debugFile.replaceAll(path.sep, "/")}`,
    "2. Write a short English debug entry containing:",
    "   - the phrase SDK_PROBE_CHILD_THREAD_OK",
    `   - run id: ${runId}`,
    "   - current timestamp",
    "3. Do not edit any other repository files.",
    "",
    "This is only a probe. Do not touch real dossiers or project documents."
  ].join("\n");

  const promptPath = path.join(runDir, "prompt.md");
  const resultPath = path.join(runDir, "result.txt");
  const statusPath = path.join(runDir, "status.json");

  await writeFile(promptPath, prompt, "utf8");

  const previousCwd = process.cwd();
  const result: ProbeResult = {
    status: "FAIL",
    runId,
    startedAt: new Date().toISOString(),
    finishedAt: "",
    cwdBefore: previousCwd,
    repoRoot,
    sdkImported: false,
    threadStarted: false,
    childRunCompleted: false,
    debugFileExists: false
  };

  try {
    process.chdir(repoRoot);
    const sdk = await loadCodexSdk();
    result.sdkImported = true;

    const Codex = (sdk as any).Codex;
    if (!Codex) throw new Error("Imported @openai/codex-sdk, but Codex export was not found.");

    const codex = new Codex();
    const thread = codex.startThread();
    result.threadStarted = true;

    const childResult = await thread.run(prompt);
    result.childRunCompleted = true;

    await writeFile(resultPath, stringifyChildResult(childResult), "utf8");

    const exists = await pathExists(debugFile);
    result.debugFileExists = exists;
    result.status = exists ? "PASS" : "INCONCLUSIVE";
  } catch (error) {
    result.error = error instanceof Error ? `${error.name}: ${error.message}\n${error.stack ?? ""}` : String(error);
    await writeFile(resultPath, result.error, "utf8");
    result.status = "FAIL";
  } finally {
    try { process.chdir(previousCwd); } catch { /* noop */ }
    result.finishedAt = new Date().toISOString();
    await writeFile(statusPath, JSON.stringify(result, null, 2), "utf8");
  }

  console.log(`SDK probe status: ${result.status}`);
  console.log(`Run directory: ${runDir}`);
  console.log(`Status file: ${statusPath}`);

  if (result.status !== "PASS") process.exitCode = 1;
}

function stringifyChildResult(value: unknown): string {
  if (typeof value === "string") return value;
  try { return JSON.stringify(value, null, 2); } catch { return String(value); }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
