# SDK subagents test result: Stage 0.30 rerun

Дата: 2026-06-09

Status: PASS

Final run id:

```text
debug-source-accumulation-2026-06-09-0033
```

Этот запуск проверял только debug-связку. Реальные методологические досье, истории, главы теории and source maps не пополнялись.

## Предстартовый cleanup

Выполнен cleanup старых generated artifacts из предыдущего FAIL:

```text
work/automation/cleanup-stage-0-30.cmd
```

После cleanup отсутствуют:

```text
work/automation/node_modules/
work/automation/package-lock.json
work/automation/passes/
work/automation/work/
```

Node tools используются через external cache:

```text
C:\Users\andre\AppData\Local\agentic-development-source-automation\node
```

`npm install` inside `work/automation` не выполнялся.

## Малые repair во время запуска

Повторный dry-run сначала выявил ошибку wrapper-а: `ensure-node-tools.cmd` возвращал `SOURCE_AUTOMATION_NODE_MODULES` with trailing space, и `run-source-loop.cmd` не находил `tsx.cmd`. Это исправлено в:

```text
work/automation/ensure-node-tools.cmd
```

Затем preflight run `debug-source-accumulation-2026-06-09-0030-preflight` выявил ошибку external SDK loader:

```text
No "exports" main defined in ...\node_modules\@openai\codex-sdk\package.json
```

Причина: `loadCodexSdk()` использовал `require.resolve("@openai/codex-sdk")` from external node_modules, а пакет экспортирует ESM entry. Исправлено в:

```text
work/automation/src/load-codex-sdk.ts
```

Loader теперь импортирует:

```text
@openai/codex-sdk/dist/index.js
```

из external node_modules.

## Dry-run

Dry-run для `DEBUG_ALPHA` прошёл через wrapper:

```text
work\automation\run-source-loop.cmd --backend sdk --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md --doc work/automation/debug/DEBUG_ALPHA.md --topic "Debug Alpha DEBUG_STOP_NOW" --min-pass 2 --max-pass 4 --mode fresh --fresh-action stub --run-id debug-source-accumulation-2026-06-09-0033 --worker-id DEBUG_ALPHA --dry-run
```

Prompt files созданы:

```text
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_01.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_02.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_03.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_04.prompt.md
```

Trace controller-а:

```text
work/automation/runs/debug-source-accumulation-2026-06-09-0033/resolved-targets.csv
```

## SDK preflight

Preflight прошёл:

```text
work\automation\sdk-probe.cmd --run-id debug-source-accumulation-2026-06-09-0033-preflight
```

Status file:

```text
work/automation/runs/debug-source-accumulation-2026-06-09-0033-preflight/sdk-probe/status.json
```

Зафиксировано:

```text
status: PASS
sdkImported: true
threadStarted: true
childRunCompleted: true
debugFileExists: true
```

## Native subagents

Запущены два native worker-subagents параллельно:

```text
DEBUG_ALPHA
DEBUG_BETA
```

Оба worker запускали только:

```text
work\automation\run-source-loop.cmd ... --backend sdk
```

`--backend cli` and nested `codex exec` не использовались.

## DEBUG_ALPHA

Status:

```text
completed
last_pass: 02
should_stop after pass 02: yes
```

Artifacts:

```text
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_01.txt
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_02.txt
```

`DEBUG_ALPHA_after_pass_03.md` отсутствует.

Status and logs:

```text
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/status.json
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/logs/DEBUG_ALPHA_pass_01.sdk-status.json
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_ALPHA/logs/DEBUG_ALPHA_pass_02.sdk-status.json
```

## DEBUG_BETA

Status:

```text
completed
last_pass: 02
should_stop after pass 02: yes
```

Artifacts:

```text
passes/DEBUG_BETA/DEBUG_BETA_after_pass_01.md
passes/DEBUG_BETA/DEBUG_BETA_delta_01.md
passes/DEBUG_BETA/DEBUG_BETA_should_stop_01.txt
passes/DEBUG_BETA/DEBUG_BETA_after_pass_02.md
passes/DEBUG_BETA/DEBUG_BETA_delta_02.md
passes/DEBUG_BETA/DEBUG_BETA_should_stop_02.txt
```

`DEBUG_BETA_after_pass_03.md` отсутствует.

Status and logs:

```text
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_BETA/status.json
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_BETA/logs/DEBUG_BETA_pass_01.sdk-status.json
work/automation/runs/debug-source-accumulation-2026-06-09-0033/DEBUG_BETA/logs/DEBUG_BETA_pass_02.sdk-status.json
```

## Path/cwd repair verification

Каждый SDK pass status содержит:

```text
cwdForChild: C:\work\noveia\dev_process\agentic-development\git
repoRoot: C:\work\noveia\dev_process\agentic-development\git
sdkImported: true
threadStarted: true
childRunCompleted: true
```

Wrong-location artifacts не появились:

```text
work/automation/passes/
work/automation/work/
```

Root-level pass artifacts появились в ожидаемых namespaces:

```text
passes/DEBUG_ALPHA/
passes/DEBUG_BETA/
```

## Вывод

Stage 0.30 rerun прошёл: controller dry-run, SDK preflight, native worker-subagents, SDK-backed child threads, root-level pass artifacts and `should_stop` after mandatory `min_pass=2` all worked on debug documents.

Это не означает, что реальные методологические dossier можно запускать без отдельного human gate. Тест подтверждает только техническую связку debug automation.
