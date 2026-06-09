import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { parseArgs } from "./args.js";
import { renderPassPrompt } from "./prompt-renderer.js";
import { runCodexExec } from "./codex-exec.js";
import { runCodexSdk } from "./codex-sdk-run.js";
import { detectLastPass, ensurePassDir, validatePassArtifacts } from "./pass-artifacts.js";
import { padPass, resolveInsideRepo, toRepoRelative } from "./path-utils.js";
import { backupAndResetDocument, prepareRunPaths, writeRunConfig } from "./run-state.js";

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const repoRoot = path.resolve(options.repoRoot);
  process.chdir(repoRoot);
  const promptAbs = resolveInsideRepo(repoRoot, options.promptPath);
  const docAbs = resolveInsideRepo(repoRoot, options.docPath);
  const promptRel = toRepoRelative(repoRoot, promptAbs);
  const docRel = toRepoRelative(repoRoot, docAbs);

  const paths = await prepareRunPaths(repoRoot, options.runId, docRel, options.workerId);
  await writeRunConfig(paths, options, {
    repoRoot,
    prompt: promptRel,
    doc: docRel,
    topic: options.topic,
    safeName: paths.safeName,
    workerId: paths.workerId,
    backend: options.backend,
    backendNote: options.backend === "sdk"
      ? "SDK backend requires escalated/network access when run from inside Codex."
      : "CLI backend is intended for external terminal/CI use; nested CLI failed in Codex with Access is denied / spawn EPERM."
  });

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

    if (options.dryRun) {
      status.push({ pass, backend: options.backend, dryRun: true, promptPath: toRepoRelative(repoRoot, promptPath) });
      console.log(JSON.stringify({ type: "source-loop.dry-run-pass", backend: options.backend, doc: docRel, topic: options.topic, pass, promptPath: toRepoRelative(repoRoot, promptPath) }));
      continue;
    }

    if (options.backend === "sdk") {
      await runCodexSdk({
        repoRoot,
        prompt,
        resultLogPath: path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.sdk-result.txt`),
        statusLogPath: path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.sdk-status.json`),
        passLabel: pass,
        docPath: docRel,
        topic: options.topic,
        runId: options.runId,
        workerId: paths.workerId
      });
    } else {
      await runCodexExec({
        codexBin: options.codexBin,
        repoRoot,
        prompt,
        stdoutLogPath: path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.stdout.jsonl`),
        stderrLogPath: path.join(paths.logsDir, `${paths.safeName}_pass_${pass}.stderr.log`),
        sandbox: options.sandbox,
        askForApproval: options.askForApproval,
        model: options.model,
        skipGitRepoCheck: options.skipGitRepoCheck,
        extraArgs: options.extraCodexArgs
      });
    }

    const validation = await validatePassArtifacts(repoRoot, docRel, passNumber);
    status.push({
      pass,
      backend: options.backend,
      shouldStop: validation.shouldStopValue,
      afterPass: toRepoRelative(repoRoot, validation.afterPass),
      delta: toRepoRelative(repoRoot, validation.delta),
      shouldStopPath: toRepoRelative(repoRoot, validation.shouldStop)
    });
    console.log(JSON.stringify({ type: "source-loop.pass-completed", backend: options.backend, doc: docRel, topic: options.topic, pass, shouldStop: validation.shouldStopValue }));
    if (passNumber >= options.minPass && validation.shouldStopValue === "yes") {
      console.log(JSON.stringify({ type: "source-loop.stopped", backend: options.backend, doc: docRel, topic: options.topic, pass, reason: "should_stop=yes" }));
      break;
    }
  }
  await mkdir(paths.workerRoot, { recursive: true });
  await writeFile(path.join(paths.workerRoot, "status.json"), JSON.stringify({ doc: docRel, topic: options.topic, runId: options.runId, workerId: paths.workerId, backend: options.backend, status }, null, 2), "utf8");
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(JSON.stringify({ type: "source-loop.failed", error: message }));
  process.exit(1);
});
