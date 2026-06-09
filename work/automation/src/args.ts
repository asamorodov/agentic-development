import { findRepoRootSync } from "./path-utils.js";

export type Mode = "fresh" | "continue";
export type FreshAction = "stub" | "delete";
export type Backend = "sdk" | "cli";

export interface LoopOptions {
  repoRoot: string;
  promptPath: string;
  docPath: string;
  topic: string;
  minPass: number;
  maxPass: number;
  startPass?: number;
  mode: Mode;
  freshAction: FreshAction;
  runId: string;
  workerId?: string;
  backend: Backend;
  codexBin: string;
  sandbox: "read-only" | "workspace-write" | "danger-full-access";
  askForApproval: "untrusted" | "on-request" | "never";
  model?: string;
  dryRun: boolean;
  skipGitRepoCheck: boolean;
  extraCodexArgs: string[];
}

function readValue(args: string[], index: number, name: string): string {
  const value = args[index + 1];
  if (!value || value.startsWith("--")) throw new Error(`Missing value for ${name}`);
  return value;
}

function numberValue(value: string, name: string): number {
  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed <= 0) throw new Error(`${name} must be a positive integer: ${value}`);
  return parsed;
}

function makeRunId(): string {
  return `run-${new Date().toISOString().replace(/[:.]/g, "-")}`;
}

export function parseArgs(argv: string[]): LoopOptions {
  const opts: Partial<LoopOptions> = {
    repoRoot: findRepoRootSync(process.cwd()),
    backend: "sdk",
    codexBin: "codex",
    sandbox: "workspace-write",
    askForApproval: "never",
    mode: "continue",
    freshAction: "stub",
    dryRun: false,
    skipGitRepoCheck: false,
    extraCodexArgs: []
  };

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    switch (arg) {
      case "--repo-root": opts.repoRoot = readValue(argv, i, arg); i++; break;
      case "--prompt": opts.promptPath = readValue(argv, i, arg); i++; break;
      case "--doc": opts.docPath = readValue(argv, i, arg); i++; break;
      case "--topic": opts.topic = readValue(argv, i, arg); i++; break;
      case "--min-pass":
      case "--min-passes":
      case "--min": opts.minPass = numberValue(readValue(argv, i, arg), arg); i++; break;
      case "--max-pass":
      case "--max-passes":
      case "--max": opts.maxPass = numberValue(readValue(argv, i, arg), arg); i++; break;
      case "--start-pass": opts.startPass = numberValue(readValue(argv, i, arg), arg); i++; break;
      case "--mode": {
        const value = readValue(argv, i, arg) as Mode;
        if (value !== "fresh" && value !== "continue") throw new Error(`--mode must be fresh or continue: ${value}`);
        opts.mode = value; i++; break;
      }
      case "--fresh-action": {
        const value = readValue(argv, i, arg) as FreshAction;
        if (value !== "stub" && value !== "delete") throw new Error(`--fresh-action must be stub or delete: ${value}`);
        opts.freshAction = value; i++; break;
      }
      case "--backend": {
        const value = readValue(argv, i, arg) as Backend;
        if (value !== "sdk" && value !== "cli") throw new Error(`--backend must be sdk or cli: ${value}`);
        opts.backend = value; i++; break;
      }
      case "--run-id": opts.runId = readValue(argv, i, arg); i++; break;
      case "--worker-id": opts.workerId = readValue(argv, i, arg); i++; break;
      case "--codex-bin": opts.codexBin = readValue(argv, i, arg); i++; break;
      case "--sandbox": {
        const value = readValue(argv, i, arg) as LoopOptions["sandbox"];
        if (!["read-only", "workspace-write", "danger-full-access"].includes(value)) throw new Error(`Invalid --sandbox: ${value}`);
        opts.sandbox = value; i++; break;
      }
      case "--ask-for-approval": {
        const value = readValue(argv, i, arg) as LoopOptions["askForApproval"];
        if (!["untrusted", "on-request", "never"].includes(value)) throw new Error(`Invalid --ask-for-approval: ${value}`);
        opts.askForApproval = value; i++; break;
      }
      case "--model": opts.model = readValue(argv, i, arg); i++; break;
      case "--codex-arg": opts.extraCodexArgs!.push(readValue(argv, i, arg)); i++; break;
      case "--dry-run": opts.dryRun = true; break;
      case "--skip-git-repo-check": opts.skipGitRepoCheck = true; break;
      case "--help":
      case "-h": printHelpAndExit(); break;
      default: throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (!opts.promptPath) throw new Error("Missing --prompt");
  if (!opts.docPath) throw new Error("Missing --doc");
  if (!opts.topic) throw new Error("Missing --topic");
  if (!opts.minPass) throw new Error("Missing --min-pass");
  if (!opts.maxPass) throw new Error("Missing --max-pass");
  if (opts.maxPass < opts.minPass) throw new Error("--max-pass must be >= --min-pass");

  return {
    repoRoot: opts.repoRoot!, promptPath: opts.promptPath, docPath: opts.docPath, topic: opts.topic,
    minPass: opts.minPass, maxPass: opts.maxPass, startPass: opts.startPass, mode: opts.mode!, freshAction: opts.freshAction!,
    runId: opts.runId ?? makeRunId(), workerId: opts.workerId, backend: opts.backend!,
    codexBin: opts.codexBin!, sandbox: opts.sandbox!, askForApproval: opts.askForApproval!, model: opts.model,
    dryRun: opts.dryRun!, skipGitRepoCheck: opts.skipGitRepoCheck!, extraCodexArgs: opts.extraCodexArgs ?? []
  };
}

function printHelpAndExit(): never {
  console.log(`Usage:
  work\\automation\\run-source-loop.cmd ^
    --backend sdk ^
    --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md ^
    --doc work/automation/debug/DEBUG_DOC.md ^
    --topic "Debug topic DEBUG_STOP_NOW" ^
    --min-pass 2 ^
    --max-pass 4 ^
    --mode fresh

Inside Codex tasks, use --backend sdk and run with escalated/network access.
Outside Codex, --backend cli remains available as a fallback.
Do not run npm install inside work/automation.
`);
  process.exit(0);
}
