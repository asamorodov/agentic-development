# Stage 0.30 — SDK backend path repair and Node tools hygiene

Дата: 2026-06-09  
Статус: delta repair после FAIL проверки SDK backend + native subagents.

## Что сломалось в тесте

`RUN_SDK_SUBAGENTS_TEST_PROMPT.md` дал `FAIL`.

Хорошие новости:

- SDK preflight прошёл с escalation;
- native subagents доступны;
- `DEBUG_BETA` смог запустить SDK child thread.

Проблемы:

1. `DEBUG_ALPHA` остановился до команды: escalation внутри subagent был отклонён auto-review.
2. `DEBUG_BETA` создал pass artifacts в неправильном месте:

```text
work/automation/passes/DEBUG_BETA/...
work/automation/work/automation/debug/DEBUG_BETA.md
```

вместо:

```text
passes/DEBUG_BETA/...
work/automation/debug/DEBUG_BETA.md
```

3. `npm install` inside `work/automation` создал `node_modules/` and `package-lock.json`; это не должно жить в repo work tree.

## Что исправлено

### Repo-root contract

- `findRepoRootSync()` added.
- `run-source-loop.ts` switches `process.cwd()` to repo root before execution.
- `codex-sdk-run.ts` also switches cwd to repo root before creating SDK child thread.
- rendered prompt now includes:
  - absolute repo root;
  - repo-relative document path;
  - absolute document path;
  - repo-relative pass artifact paths;
  - absolute pass artifact paths;
  - explicit warning not to create `work/automation/passes` or duplicated `work/automation/work/automation` paths.

### External Node tools

No more `npm install` inside `work/automation`.

Added wrappers:

```text
work/automation/ensure-node-tools.cmd
work/automation/run-source-loop.cmd
work/automation/sdk-probe.cmd
```

They install `tsx` and `@openai/codex-sdk` outside repository:

```text
%LOCALAPPDATA%gentic-development-source-automation
ode
```

or `%TEMP%` fallback.

### Cleanup

Added:

```text
work/automation/cleanup-stage-0-30.cmd
work/DELETE_PATHS_STAGE_0_30.txt
```

Use them to delete generated junk from failed tests.

## Что ещё остаётся риском

Subagent-level escalation may still be denied by Codex auto-review. This repair cannot force approval. It reduces unnecessary risk by removing local npm install from worker commands, but SDK child threads still require network/escalated access because they call the API.

If subagent escalation remains blocked, the remaining viable paths are:

- run SDK loop from parent controller without native subagents;
- run external terminal orchestration;
- use native subagents without SDK child threads, accepting weaker “fresh prompt per pass” guarantees.
