# Source accumulation automation

Цель: запускать один и тот же prompt над документом несколько раз как реальные отдельные проходы.

TS-loop не знает очередь документов. Он выполняет только один документ.

Параллельность по документам делает управляющий Codex prompt через subagents. Каждый worker-subagent запускает этот TS-loop только для своего документа.

## Не ставить node_modules в репозиторий

Не выполнять `npm install` inside `work/automation`.

Для запуска использовать `.cmd` wrappers:

```text
work\automation\run-source-loop.cmd
work\automation\sdk-probe.cmd
```

Wrappers устанавливают `tsx` and `@openai/codex-sdk` во внешний каталог пользователя:

```text
%LOCALAPPDATA%\agentic-development-source-automation\node
```

Если `%LOCALAPPDATA%` недоступен, используется `%TEMP%`.

`work/automation/node_modules/` не нужен and должен быть удалён, если он появился после старых тестов.

## Backend-и

Есть два backend-а:

```text
sdk — основной для запуска изнутри Codex-задачи;
cli — fallback для внешнего терминала / CI.
```

### SDK backend

Использовать внутри Codex:

```text
--backend sdk
```

SDK backend требует network/escalated доступ. Без него SDK может импортироваться and стартовать thread, но упасть на API request.

### CLI backend

CLI backend использует `codex exec`.

Он остаётся полезным для внешнего терминала or CI, но не использовать его как nested backend внутри Codex-задачи: такой путь уже падал с `Access is denied` / `spawn EPERM`.

## Один debug-запуск через SDK

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md ^
  --doc work/automation/debug/DEBUG_ALPHA.md ^
  --topic "Debug Alpha DEBUG_STOP_NOW" ^
  --min-pass 2 ^
  --max-pass 4 ^
  --mode fresh ^
  --fresh-action stub ^
  --run-id debug-local ^
  --worker-id DEBUG_ALPHA
```

Ожидаемый результат: проходы 01 and 02 выполнены, после pass 02 остановка по `should_stop=yes`.

## Dry-run

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md ^
  --doc work/automation/debug/DEBUG_ALPHA.md ^
  --topic "Debug Alpha DEBUG_STOP_NOW" ^
  --min-pass 2 ^
  --max-pass 4 ^
  --mode fresh ^
  --run-id debug-dry-run ^
  --worker-id DEBUG_ALPHA ^
  --dry-run
```

Dry-run собирает prompt-файлы, но не вызывает SDK/API.

## SDK probe

```cmd
work\automation\sdk-probe.cmd --run-id sdk-probe-manual
```

В Codex-задаче этот probe должен запускаться с network/escalated доступом.

## Содержательный запуск одного документа через SDK

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md ^
  --doc work/dossiers/BMAD_METHOD_DOSSIER.md ^
  --topic "BMAD Method" ^
  --min-pass 10 ^
  --max-pass 20 ^
  --mode fresh ^
  --fresh-action stub ^
  --run-id methodology-dossiers-001 ^
  --worker-id BMAD_METHOD_DOSSIER
```

## Fresh mode

`--mode fresh --fresh-action stub` means:

```text
if document exists:
  back it up into the worker run folder
  back up previous passes for this document
  remove previous passes
  replace the document with a fresh stub

if document does not exist:
  create parent directories
  create a fresh stub
```

The controller prompt must not stop only because a target document is absent in fresh mode. Missing document creation is the loop's responsibility.

## Pass artifacts

Для документа:

```text
work/dossiers/BMAD_METHOD_DOSSIER.md
```

ожидаются файлы:

```text
passes/BMAD_METHOD_DOSSIER/BMAD_METHOD_DOSSIER_after_pass_01.md
passes/BMAD_METHOD_DOSSIER/BMAD_METHOD_DOSSIER_delta_01.md
passes/BMAD_METHOD_DOSSIER/BMAD_METHOD_DOSSIER_should_stop_01.txt
```

## Логи

Каждый worker пишет:

```text
work/automation/runs/<run-id>/<worker-id>/prompts/
work/automation/runs/<run-id>/<worker-id>/logs/
work/automation/runs/<run-id>/<worker-id>/backup/
work/automation/runs/<run-id>/<worker-id>/status.json
```

## Важное ограничение

TS-loop проверяет, что дочерний запуск создал обязательные pass-артефакты. Если их нет, запуск падает. Это намеренно: отсутствие pass-артефактов означает, что prompt не выполнил контракт одного прохода.
