# Stage 0.28 — SDK backend for source accumulation loop

Дата: 2026-06-08  
Статус: delta-обновление после SDK probe.

## Исходный результат

Предыдущий nested CLI path не сработал:

```text
Codex controller → TS loop → codex exec
```

Результат: `Access is denied` / `spawn EPERM`.

SDK probe дал другой результат:

```text
Codex controller → TS probe → @openai/codex-sdk → child Codex thread
```

Результат: `PASS with escalation required`.

Без escalation SDK импортировался and thread стартовал, но запрос к API оборвался. С escalation дочерний SDK-thread создал `SDK_PROBE.md`.

## Решение

Внутри Codex использовать SDK backend как основной:

```text
--backend sdk
```

CLI backend оставить только для внешнего терминала/CI:

```text
--backend cli
```

## Что изменено

Добавлено:

```text
work/automation/src/codex-sdk-run.ts
```

Обновлено:

```text
work/automation/src/args.ts
work/automation/src/run-source-loop.ts
work/automation/package.json
work/automation/.gitignore
work/automation/README.md
work/prompts/SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
```

## Новый контракт запуска

Controller-prompt должен:

1. использовать `--backend sdk`;
2. заранее требовать network/escalated доступ;
3. выполнить SDK preflight;
4. запускать worker-subagents только после PASS;
5. не использовать nested `codex exec` внутри Codex-задачи.

## Почему archive is delta-only

С этого шага архив содержит только новые/изменённые файлы. Он не включает полный `work/discourse.md`, чтобы не затереть запись, которую Codex уже добавил после SDK probe.
