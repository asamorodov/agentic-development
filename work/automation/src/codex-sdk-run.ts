import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { loadCodexSdk } from "./load-codex-sdk.js";

export interface CodexSdkRunOptions {
  repoRoot: string;
  prompt: string;
  resultLogPath: string;
  statusLogPath: string;
  passLabel: string;
  docPath: string;
  topic: string;
  runId: string;
  workerId: string;
}

export async function runCodexSdk(options: CodexSdkRunOptions): Promise<void> {
  await mkdir(path.dirname(options.resultLogPath), { recursive: true });
  await mkdir(path.dirname(options.statusLogPath), { recursive: true });

  const previousCwd = process.cwd();
  const resolvedRepoRoot = path.resolve(options.repoRoot);

  const status: Record<string, unknown> = {
    backend: "sdk",
    startedAt: new Date().toISOString(),
    finishedAt: null,
    cwdBefore: previousCwd,
    repoRoot: resolvedRepoRoot,
    cwdForChild: resolvedRepoRoot,
    pass: options.passLabel,
    doc: options.docPath,
    topic: options.topic,
    runId: options.runId,
    workerId: options.workerId,
    sdkImported: false,
    threadStarted: false,
    childRunCompleted: false
  };

  try {
    process.chdir(resolvedRepoRoot);

    const sdk = await loadCodexSdk();
    status.sdkImported = true;

    const Codex = (sdk as any).Codex;
    if (!Codex) {
      throw new Error("Imported @openai/codex-sdk, but Codex export was not found.");
    }

    const codex = new Codex();
    const thread = codex.startThread();
    status.threadStarted = true;

    const childResult = await thread.run(options.prompt);
    status.childRunCompleted = true;

    await writeFile(options.resultLogPath, stringifyChildResult(childResult), "utf8");
  } catch (error) {
    const message = error instanceof Error
      ? `${error.name}: ${error.message}\n${error.stack ?? ""}`
      : String(error);

    status.error = message;
    await writeFile(options.resultLogPath, message, "utf8");
    throw new Error(`Codex SDK backend failed for pass ${options.passLabel}. See ${options.resultLogPath}. ${message}`);
  } finally {
    try {
      process.chdir(previousCwd);
    } catch {
      // Ignore cwd restore failures; the process is exiting or continuing with explicit paths.
    }
    status.finishedAt = new Date().toISOString();
    await writeFile(options.statusLogPath, JSON.stringify(status, null, 2), "utf8");
  }
}

function stringifyChildResult(value: unknown): string {
  if (typeof value === "string") return value;
  try {
    return JSON.stringify(value, null, 2);
  } catch {
    return String(value);
  }
}
