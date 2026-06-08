import { spawn } from "node:child_process";
import { createWriteStream } from "node:fs";
import { mkdir } from "node:fs/promises";
import path from "node:path";

export interface CodexExecOptions {
  codexBin: string;
  repoRoot: string;
  prompt: string;
  stdoutLogPath: string;
  stderrLogPath: string;
  sandbox: "read-only" | "workspace-write" | "danger-full-access";
  askForApproval: "untrusted" | "on-request" | "never";
  model?: string;
  skipGitRepoCheck: boolean;
  extraArgs: string[];
}

export async function runCodexExec(options: CodexExecOptions): Promise<void> {
  await mkdir(path.dirname(options.stdoutLogPath), { recursive: true });
  await mkdir(path.dirname(options.stderrLogPath), { recursive: true });

  const args = [
    "exec", "-",
    "--cd", options.repoRoot,
    "--sandbox", options.sandbox,
    "--ask-for-approval", options.askForApproval,
    "--json"
  ];
  if (options.model) args.push("--model", options.model);
  if (options.skipGitRepoCheck) args.push("--skip-git-repo-check");
  args.push(...options.extraArgs);

  const child = spawn(options.codexBin, args, { cwd: options.repoRoot, stdio: ["pipe", "pipe", "pipe"], env: process.env });
  const stdoutLog = createWriteStream(options.stdoutLogPath, { flags: "a" });
  const stderrLog = createWriteStream(options.stderrLogPath, { flags: "a" });
  child.stdout.pipe(stdoutLog);
  child.stderr.pipe(stderrLog);
  child.stdin.write(options.prompt);
  child.stdin.end();

  const exitCode = await new Promise<number | null>((resolve, reject) => {
    child.on("error", reject);
    child.on("close", resolve);
  });
  stdoutLog.end();
  stderrLog.end();
  if (exitCode !== 0) throw new Error(`codex exec failed with exit code ${exitCode}. See logs: ${options.stdoutLogPath}, ${options.stderrLogPath}`);
}
