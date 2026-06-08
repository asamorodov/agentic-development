import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { parseArgs } from "./args.js";
import { renderPassPrompt } from "./prompt-renderer.js";
import { runCodexExec } from "./codex-exec.js";
import { detectLastPass, ensurePassDir, validatePassArtifacts } from "./pass-artifacts.js";
import { padPass, resolveInsideRepo, toRepoRelative } from "./path-utils.js";
import { backupAndResetDocument, prepareRunPaths, writeRunConfig } from "./run-state.js";

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const repoRoot = path.resolve(options.repoRoot);
  const promptAbs = resolveInsideRepo(repoRoot, options.promptPath);
  const docAbs = resolveInsideRepo(repoRoot, options.docPath);
  const promptRel = toRepoRelative(repoRoot, promptAbs);
  const docRel = toRepoRelative(repoRoot, docAbs);

  const paths = await prepareRunPaths(repoRoot, options.runId, docRel, options.workerId);
  await writeRunConfig(paths, options, { repoRoot, prompt: promptRel, doc: docRel, topic: options.topic, safeName: paths.safeName, workerId: paths.workerId });

  if (options.mode === "fresh" && !options.dryRun) await backupAndResetDocument(repoRoot, docRel, options.topic, paths, options.freshAction);
  await ensurePassDir(repoRoot, docRel);

  const lastPass = options.mode === "continue" ? await detectLastPass(repoRoot, docRel) : 0;
  const startPass = options.startPass ?? (options.mode === "continue" ? Math.max(1, lastPass + 1) : 1);
  if (startPass > options.maxPass) {
    console.log(JSON.stringify({ type: "source-loop.skipped", reason: "start-pass-after-max-pass", doc: docRel, topic: options.topic, startPass, maxPass: options.maxPass }));
    return;
  }

  const status: Array<Record<string, unknown>> = [];
  for (let passNumber = startPass; passNumber <= options.maxPass; passNumber++) {
    const pass = padPass(passNumber);
    const prompt = await renderPassPrompt({ repoRoot, promptPath: promptRel, docPath: docRel, topic: options.topic, passNumber, runId: options.runId, workerId: paths.workerId });
    const promptPath = path.join(paths.promptsDir, `${paths.safeName}_pass_${pass}.prompt.md`);
    await writeFile(promptPath, prompt, "utf8");
    const stdoutLog = path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.stdout.jsonl`);
    const stderrLog = path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.stderr.log`);

    if (options.dryRun) {
      status.push({ pass, dryRun: true, promptPath: toRepoRelative(repoRoot, promptPath) });
      console.log(JSON.stringify({ type: "source-loop.dry-run-pass", doc: docRel, topic: options.topic, pass, promptPath: toRepoRelative(repoRoot, promptPath) }));
      continue;
    }

    await runCodexExec({ codexBin: options.codexBin, repoRoot, prompt, stdoutLogPath: stdoutLog, stderrLogPath: stderrLog, sandbox: options.sandbox, askForApproval: options.askForApproval, model: options.model, skipGitRepoCheck: options.skipGitRepoCheck, extraArgs: options.extraCodexArgs });
    const validation = await validatePassArtifacts(repoRoot, docRel, passNumber);
    status.push({ pass, shouldStop: validation.shouldStopValue, afterPass: toRepoRelative(repoRoot, validation.afterPass), delta: toRepoRelative(repoRoot, validation.delta), shouldStopPath: toRepoRelative(repoRoot, validation.shouldStop) });
    console.log(JSON.stringify({ type: "source-loop.pass-completed", doc: docRel, topic: options.topic, pass, shouldStop: validation.shouldStopValue }));
    if (passNumber >= options.minPass && validation.shouldStopValue === "yes") {
      console.log(JSON.stringify({ type: "source-loop.stopped", doc: docRel, topic: options.topic, pass, reason: "should_stop=yes" }));
      break;
    }
  }
  await mkdir(paths.workerRoot, { recursive: true });
  await writeFile(path.join(paths.workerRoot, "status.json"), JSON.stringify({ doc: docRel, topic: options.topic, runId: options.runId, workerId: paths.workerId, status }, null, 2), "utf8");
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(JSON.stringify({ type: "source-loop.failed", error: message }));
  process.exit(1);
});
