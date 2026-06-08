# Source accumulation automation

Цель: запускать один и тот же prompt над документом несколько раз как реальные отдельные `codex exec`-проходы.

TS-loop не знает очередь документов. Он выполняет только один документ.

Параллельность по документам должна делаться управляющим Codex prompt через subagents. Каждый worker-subagent запускает этот TS-loop только для своего документа.

## Один debug-запуск

```bash
npx tsx work/automation/src/run-source-loop.ts \
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md \
  --doc work/automation/debug/DEBUG_ALPHA.md \
  --topic "Debug Alpha DEBUG_STOP_NOW" \
  --min-pass 2 \
  --max-pass 4 \
  --mode fresh \
  --fresh-action stub \
  --run-id debug-local \
  --worker-id DEBUG_ALPHA \
  --sandbox workspace-write \
  --ask-for-approval never
```

Ожидаемый результат: проходы 01 и 02 выполнены, после pass 02 остановка по `should_stop=yes`.

## Dry-run

```bash
npx tsx work/automation/src/run-source-loop.ts \
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md \
  --doc work/automation/debug/DEBUG_ALPHA.md \
  --topic "Debug Alpha DEBUG_STOP_NOW" \
  --min-pass 2 \
  --max-pass 4 \
  --mode fresh \
  --run-id debug-dry-run \
  --worker-id DEBUG_ALPHA \
  --dry-run
```

Dry-run собирает prompt-файлы, но не вызывает `codex exec`.

## Содержательный запуск одного документа

```bash
npx tsx work/automation/src/run-source-loop.ts \
  --prompt work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md \
  --doc work/dossiers/BMAD_METHOD_DOSSIER.md \
  --topic "BMAD Method" \
  --min-pass 10 \
  --max-pass 20 \
  --mode fresh \
  --fresh-action stub \
  --run-id methodology-dossiers-001 \
  --worker-id BMAD_METHOD_DOSSIER \
  --sandbox workspace-write \
  --ask-for-approval never
```

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

TS-loop проверяет, что Codex создал обязательные pass-артефакты. Если их нет, запуск падает. Это намеренно: отсутствие pass-артефактов означает, что prompt не выполнил контракт одного прохода.
