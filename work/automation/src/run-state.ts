import { mkdir, rm, cp, writeFile } from "node:fs/promises";
import path from "node:path";
import { exists, safeDocName } from "./path-utils.js";
import type { LoopOptions } from "./args.js";

export interface RunPaths {
  runRoot: string;
  workerRoot: string;
  promptsDir: string;
  logsDir: string;
  backupDir: string;
  workerId: string;
  safeName: string;
}

export async function prepareRunPaths(repoRoot: string, runId: string, docPath: string, workerId?: string): Promise<RunPaths> {
  const safeName = safeDocName(docPath);
  const finalWorkerId = workerId ?? safeName;
  const runRoot = path.join(repoRoot, "work", "automation", "runs", runId);
  const workerRoot = path.join(runRoot, finalWorkerId);
  const promptsDir = path.join(workerRoot, "prompts");
  const logsDir = path.join(workerRoot, "logs");
  const backupDir = path.join(workerRoot, "backup");
  await mkdir(promptsDir, { recursive: true });
  await mkdir(logsDir, { recursive: true });
  await mkdir(backupDir, { recursive: true });
  return { runRoot, workerRoot, promptsDir, logsDir, backupDir, workerId: finalWorkerId, safeName };
}

export async function writeRunConfig(paths: RunPaths, options: LoopOptions, resolved: Record<string, unknown>): Promise<void> {
  await writeFile(path.join(paths.workerRoot, "run.config.json"), JSON.stringify({ options, resolved, createdAt: new Date().toISOString() }, null, 2), "utf8");
}

export async function backupAndResetDocument(repoRoot: string, docPath: string, topic: string, paths: RunPaths, freshAction: "stub" | "delete"): Promise<void> {
  const absoluteDocPath = path.resolve(repoRoot, docPath);
  const passDir = path.join(repoRoot, "passes", paths.safeName);
  if (await exists(absoluteDocPath)) await cp(absoluteDocPath, path.join(paths.backupDir, "document-before-fresh.md"), { force: true });
  if (await exists(passDir)) {
    await cp(passDir, path.join(paths.backupDir, "passes-before-fresh"), { recursive: true, force: true });
    await rm(passDir, { recursive: true, force: true });
  }
  if (freshAction === "delete") {
    if (await exists(absoluteDocPath)) await rm(absoluteDocPath, { force: true });
    return;
  }
  await mkdir(path.dirname(absoluteDocPath), { recursive: true });
  await writeFile(absoluteDocPath, `# ${topic}\n\n## Черновое назначение\n\nДокумент создан режимом fresh для накопления материала из первоисточников.\n\n## Источники\n\n## Поисковые формулировки\n\n## Кандидаты на иллюстрации\n\n## Открытые вопросы\n`, "utf8");
}
