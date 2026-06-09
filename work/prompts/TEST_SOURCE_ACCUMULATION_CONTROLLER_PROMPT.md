# Prompt: тест запуска source accumulation automation через SDK backend

Этот prompt проверяет связку:

```text
управляющий Codex prompt
→ worker-subagent
→ TS-loop
→ Codex SDK backend
→ debug prompt
→ pass-артефакты
→ should_stop
```

Он не должен трогать реальные методологические досье.

## Важное условие

Настоящий тест должен запускаться с network/escalated доступом. Не выполнять `npm install` inside `work/automation`; использовать только `.cmd` wrappers из `work/automation`.

Без такого доступа SDK probe уже падал на запросе к API. Не надо сначала запускать обычный sandbox-вариант: если network/escalated доступ недоступен, остановись и верни `FAIL`.

## Что нужно сделать

Создать тестовый run_id вида:

```text
debug-source-accumulation-{дата-время}
```

Подготовить две тестовые темы:

```text
Debug Alpha DEBUG_STOP_NOW
Debug Beta DEBUG_STOP_NOW
```

и два тестовых документа:

```text
work/automation/debug/DEBUG_ALPHA.md
work/automation/debug/DEBUG_BETA.md
```

Использовать prompt:

```text
work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md
```

Параметры проходов:

```text
min_pass = 2
max_pass = 4
mode = fresh
fresh_action = stub
backend = sdk
```

Так как тема содержит `DEBUG_STOP_NOW`, debug prompt будет писать `should_stop=yes` на каждом проходе. Оркестратор должен выполнить обязательные 2 прохода и остановиться после второго прохода.

## Сначала dry-run

Перед настоящим запуском выполнить dry-run для одного документа:

```bash
work\automation\run-source-loop.cmd \
  --backend sdk \
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md \
  --doc work/automation/debug/DEBUG_ALPHA.md \
  --topic "Debug Alpha DEBUG_STOP_NOW" \
  --min-pass 2 \
  --max-pass 4 \
  --mode fresh \
  --fresh-action stub \
  --run-id <run_id> \
  --worker-id DEBUG_ALPHA \
  --dry-run
```

Проверить, что prompt-файлы для проходов собраны.

Dry-run не требует SDK API call.

## Потом SDK preflight

С network/escalated доступом выполнить:

```bash
work\automation\sdk-probe.cmd --run-id <run_id>-preflight
```

Если preflight не проходит, не запускать worker-subagents.

## Потом настоящая проверка

Запустить два worker-subagents параллельно, по одному на документ.

Каждый worker должен выполнить:

```bash
work\automation\run-source-loop.cmd \
  --backend sdk \
  --prompt work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md \
  --doc <debug_doc> \
  --topic "<debug_topic>" \
  --min-pass 2 \
  --max-pass 4 \
  --mode fresh \
  --fresh-action stub \
  --run-id <run_id> \
  --worker-id <worker_id>
```

## Что проверить после запуска

Для каждого документа должны существовать:

```text
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_01.txt
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_02.txt
```

и аналогично для `DEBUG_BETA`.

Не должно быть pass 03, потому что после pass 02 уже разрешено уважать `should_stop=yes`.

Также должны существовать:

```text
work/automation/runs/<run_id>/DEBUG_ALPHA/status.json
work/automation/runs/<run_id>/DEBUG_BETA/status.json
work/automation/runs/<run_id>/DEBUG_ALPHA/logs/
work/automation/runs/<run_id>/DEBUG_BETA/logs/
```

## Финальный ответ

Верни короткий статус:

```text
dry-run: ok / failed
sdk preflight: ok / failed
sdk backend: ok / failed
subagents: ok / failed
should_stop after min_pass: ok / failed
debug docs:
logs:
```

Если SDK backend не запускается с network/escalated доступом, не чинить реальные досье. Честно зафиксировать ограничение.
