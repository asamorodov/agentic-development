# Prompt: test Codex SDK as nested execution backend

Статус: тестовый prompt.  
Назначение: проверить, можно ли из текущей Codex-задачи запустить новый независимый Codex-thread через Codex SDK, не используя `codex exec`.

Не запускай рабочее пополнение реальных досье.  
Не изменяй реальные методологические документы.

## Зачем этот тест

Предыдущий тест показал:

```text
Codex controller → TS loop → nested codex exec
```

не работает в текущей среде: `codex --version` даёт `Access is denied`, а настоящий запуск падает на `spawn EPERM`.

Теперь нужно проверить другой backend:

```text
Codex controller → TS probe → @openai/codex-sdk → new Codex thread → debug prompt
```

Если SDK работает изнутри Codex-задачи, можно сохранить элегантную схему:

```text
управляющий prompt
→ subagent per document
→ TS loop
→ fresh Codex SDK thread per pass
```

Если SDK тоже не работает, это нужно честно зафиксировать. Не имитируй успех.

## Что прочитать

Сначала прочитай:

```text
work/discourse.md
work/automation/README.md
work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/reports/SOURCE_ACCUMULATION_AUTOMATION_MODULES.md
```

Также проверь текущие файлы:

```text
work/automation/package.json
work/automation/src/sdk-probe.ts
```

Если `work/automation/src/sdk-probe.ts` отсутствует, создай минимальный probe-скрипт сам.

## Что проверить

Выполни проверку в таком порядке.

### 1. Environment preflight

Из `work/automation` проверь:

```text
node --version
npm --version
npm view @openai/codex-sdk version
```

Если `npm view` запрещён сетью or средой, зафиксируй это. Не считай SDK недоступным, пока не проверишь уже установленные packages and package cache.

### 2. Установить SDK только если нужно

Если `@openai/codex-sdk` не установлен, попробуй установить его минимально:

```text
npm.cmd install @openai/codex-sdk
```

На Windows используй `.cmd`, если PowerShell блокирует `.ps1`.

Не добавляй `node_modules` в git. Если `package.json` or `package-lock.json` изменятся, зафиксируй это в отчёте.

### 3. Запустить SDK probe

Запусти:

```text
npm.cmd run sdk-probe -- --run-id sdk-probe-YYYY-MM-DD-HHMM
```

Если npm-script отсутствует, запусти напрямую:

```text
node --loader ts-node/esm src/sdk-probe.ts --run-id sdk-probe-YYYY-MM-DD-HHMM
```

или через уже доступный `tsx.cmd`, если он установлен:

```text
node_modules/.bin/tsx.cmd src/sdk-probe.ts --run-id sdk-probe-YYYY-MM-DD-HHMM
```

Не используй `codex exec` в этом тесте. Проверяется именно SDK, а не CLI.

### 4. Что должен сделать probe

Probe должен создать or обновить только test area:

```text
work/automation/debug/SDK_PROBE.md
work/automation/runs/<run-id>/sdk-probe/
```

Ожидаемый результат успешного SDK-запуска:

```text
work/automation/debug/SDK_PROBE.md
```

содержит запись, созданную дочерним Codex-thread через SDK.

В run-folder должны быть:

```text
prompt.md
result.txt
status.json
```

Если SDK thread запустился, но не смог писать в workspace, зафиксируй это отдельно.

## Правила

- Не трогай реальные досье.
- Не запускай `run-source-loop.ts`.
- Не запускай `codex exec`.
- Не создавай pass artifacts для реальных документов.
- Не обновляй общий рабочий план.
- Можно обновить `work/discourse.md` только короткой записью о результате SDK probe.
- Можно создать отчёт:

```text
work/reports/CODEX_SDK_PROBE_RESULT.md
```

## Итоговый отчёт

В конце верни короткий отчёт:

```text
status: PASS / FAIL / INCONCLUSIVE
что было запущено
установился ли @openai/codex-sdk
создан ли SDK_PROBE.md дочерним SDK-thread
где лежат prompt/result/status
может ли SDK заменить nested codex exec
если нет — точная причина
```

Если получаешь `EPERM`, `Access is denied`, sandbox/approval/authentication error or missing package error, не пытайся скрыть это cleanup-ом. Зафиксируй точный stderr/stdout.
