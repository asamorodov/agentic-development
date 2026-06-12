# Codex SDK probe result

Дата: 2026-06-08

Status: PASS with escalation required

## Что проверялось

Проверялся backend:

```text
Codex controller -> TS probe -> @openai/codex-sdk -> new Codex thread -> debug file
```

`codex exec` в этом тесте не запускался вручную. Реальные досье, главы, истории и рабочие документы не пополнялись.

## Preflight

Из `work/automation`:

```text
node --version -> v22.14.0
npm.cmd --version -> 10.9.2
npm.cmd view @openai/codex-sdk version -> 0.137.0
```

`npm view` в обычном sandbox завис и был повторён с escalation. Registry ответил версией `0.137.0`.

## Установка

`@openai/codex-sdk` не был установлен локально.

Выполнено:

```text
npm.cmd install @openai/codex-sdk
```

Команда выполнена с escalation, потому что сетевые npm-команды в обычном sandbox зависали.

Изменения:

```text
work/automation/package.json
work/automation/package-lock.json
work/automation/node_modules/
```

`node_modules` не предназначен для добавления в git.

## Запуски

Первый запуск без escalation:

```text
npm.cmd run sdk-probe -- --run-id sdk-probe-2026-06-08-2315
```

Результат: `FAIL`.

Причина:

```text
stream disconnected before completion: error sending request for url (https://api.openai.com/v1/responses)
```

Артефакты:

```text
work/automation/runs/sdk-probe-2026-06-08-2315/sdk-probe/prompt.md
work/automation/runs/sdk-probe-2026-06-08-2315/sdk-probe/result.txt
work/automation/runs/sdk-probe-2026-06-08-2315/sdk-probe/status.json
```

`work/automation/debug/SDK_PROBE.md` не был создан.

Повторный запуск с escalation:

```text
npm.cmd run sdk-probe -- --run-id sdk-probe-2026-06-08-2315-escalated
```

Результат: `PASS`.

Артефакты:

```text
work/automation/runs/sdk-probe-2026-06-08-2315-escalated/sdk-probe/prompt.md
work/automation/runs/sdk-probe-2026-06-08-2315-escalated/sdk-probe/result.txt
work/automation/runs/sdk-probe-2026-06-08-2315-escalated/sdk-probe/status.json
work/automation/debug/SDK_PROBE.md
```

`status.json` подтвердил:

```text
sdkImported: true
threadStarted: true
childRunCompleted: true
debugFileExists: true
```

`SDK_PROBE.md` содержит строку:

```text
SDK_PROBE_CHILD_THREAD_OK
```

## Вывод

`@openai/codex-sdk` может запускать дочерний Codex thread из TS probe и писать в workspace, но в текущей среде это требует escalated shell/network access. В обычном sandbox SDK импортируется и thread создаётся, но запрос к OpenAI API обрывается.

Важная техническая деталь: установленный SDK сам оборачивает Codex CLI из пакета `@openai/codex`; это не полностью бесклиентный backend. Тем не менее он обходит проблему `Access is denied` у WindowsApps `codex.exe`, потому что использует npm-поставляемый Codex binary.

`result.txt` успешного запуска сейчас содержит только `[object Object]`, потому что `sdk-probe.ts` сериализует результат через `String(childResult)`. Это не ломает PASS, но probe-скрипт стоит улучшить перед использованием в реальном оркестраторе: писать `finalResponse`, `items` and `usage` как JSON.
