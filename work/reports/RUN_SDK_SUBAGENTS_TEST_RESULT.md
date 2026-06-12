# SDK subagents test result

Дата: 2026-06-09

Status: FAIL

Run id:

```text
debug-source-accumulation-2026-06-08-2359
```

## Что было запущено

Прочитан и выполнен тестовый prompt:

```text
work/prompts/RUN_SDK_SUBAGENTS_TEST_PROMPT.md
```

Тест проверял связку:

```text
Codex controller
-> native worker-subagent per debug document
-> TS loop
-> --backend sdk
-> child SDK-thread per pass
-> debug prompt
-> pass artifacts
-> should_stop
```

Реальные методологические досье, главы теории, истории and source maps не пополнялись.

## Dry-run

Dry-run для `DEBUG_ALPHA` прошёл.

Команда запускалась из `work/automation` через локальный npm script, с явным `--repo-root ..\..`:

```text
npm.cmd run run-source-loop -- --repo-root ..\.. --backend sdk --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md --doc work/automation/debug/DEBUG_ALPHA.md --topic "Debug Alpha DEBUG_STOP_NOW" --min-pass 2 --max-pass 4 --mode fresh --fresh-action stub --run-id debug-source-accumulation-2026-06-08-2359 --worker-id DEBUG_ALPHA --dry-run
```

Dry-run создал prompt-файлы:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_01.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_02.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_03.prompt.md
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/prompts/DEBUG_ALPHA_pass_04.prompt.md
```

Важно: `work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/status.json` относится к dry-run, а не к настоящему worker-run.

## SDK preflight

SDK preflight прошёл с network/escalated доступом:

```text
npm.cmd run sdk-probe -- --run-id debug-source-accumulation-2026-06-08-2359-preflight
```

Status file:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359-preflight/sdk-probe/status.json
```

Зафиксировано:

```text
status: PASS
sdkImported: true
threadStarted: true
childRunCompleted: true
debugFileExists: true
```

## Subagents

Native subagents были доступны and запущены параллельно:

```text
DEBUG_ALPHA
DEBUG_BETA
```

`DEBUG_ALPHA` завершился `failed` до выполнения команды: escalation внутри subagent был отклонён auto-review, потому что SDK-backed npm run может отправлять prompt/workspace data во внешний network service. Fallback не запускался.

`DEBUG_BETA` дошёл до SDK-backed TS-loop and pass 01 был attempted. `work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_BETA/logs/DEBUG_BETA_pass_01.sdk-status.json` показывает:

```text
sdkImported: true
threadStarted: true
childRunCompleted: true
```

Но parent loop упал на validation:

```text
Pass 01 did not produce required artifacts:
passes\DEBUG_BETA\DEBUG_BETA_after_pass_01.md
passes\DEBUG_BETA\DEBUG_BETA_delta_01.md
passes\DEBUG_BETA\DEBUG_BETA_should_stop_01.txt
```

Причина уточнена по `sdk-result.txt`: child SDK-thread работал относительно `work/automation`, поэтому создал debug-файлы в неправильной зоне:

```text
work/automation/passes/DEBUG_BETA/DEBUG_BETA_after_pass_01.md
work/automation/passes/DEBUG_BETA/DEBUG_BETA_delta_01.md
work/automation/passes/DEBUG_BETA/DEBUG_BETA_should_stop_01.txt
work/automation/work/automation/debug/DEBUG_BETA.md
```

Ожидаемые root-level artifacts under `passes/DEBUG_BETA/` не созданы.

## Проверка обязательных artifacts

Ожидаемые artifacts отсутствуют:

```text
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_01.txt
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_02.txt

passes/DEBUG_BETA/DEBUG_BETA_after_pass_01.md
passes/DEBUG_BETA/DEBUG_BETA_delta_01.md
passes/DEBUG_BETA/DEBUG_BETA_should_stop_01.txt
passes/DEBUG_BETA/DEBUG_BETA_after_pass_02.md
passes/DEBUG_BETA/DEBUG_BETA_delta_02.md
passes/DEBUG_BETA/DEBUG_BETA_should_stop_02.txt
```

Pass 03 root-level artifacts also отсутствуют, but this is not a success condition because pass 01/pass 02 artifacts were not produced.

## Логи

Основной run:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359/
```

Trace:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359/resolved-targets.csv
```

`DEBUG_ALPHA`:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_ALPHA/
```

`DEBUG_BETA`:

```text
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_BETA/logs/DEBUG_BETA_pass_01.sdk-status.json
work/automation/runs/debug-source-accumulation-2026-06-08-2359/DEBUG_BETA/logs/DEBUG_BETA_pass_01.sdk-result.txt
```

## Вывод

Тест не прошёл.

Новая фактическая картина:

```text
SDK preflight works with escalation.
Native subagents are available.
Subagent-level escalation is not reliably available: DEBUG_ALPHA was blocked before command execution.
SDK child thread can run, but current SDK backend does not preserve repo-root cwd for relative paths: DEBUG_BETA wrote artifacts under work/automation instead of repo root.
```

Следующий технический repair должен исправить SDK backend path/cwd contract: либо запускать child SDK-thread with repo-root cwd if SDK supports it, либо передавать absolute paths and explicitly verify that child writes under repository root. После этого нужен повторный test run.
