# Source accumulation automation modules

Дата: 2026-06-08  
Статус: добавлены первые связные модули для внешнего запуска source accumulation проходов.

## Что добавлено

### TS-loop

```text
work/automation/src/run-source-loop.ts
work/automation/src/args.ts
work/automation/src/codex-exec.ts
work/automation/src/pass-artifacts.ts
work/automation/src/path-utils.ts
work/automation/src/prompt-renderer.ts
work/automation/src/run-state.ts
```

`run-source-loop.ts` принимает путь к prompt, путь к документу, тему, `min-pass`, `max-pass`, режим `fresh/continue`, `run-id`, `worker-id` and параметры Codex CLI.

Он запускает реальные отдельные `codex exec` проходы. После каждого прохода проверяет pass-артефакты. После `min-pass` начинает уважать `should_stop=yes`.

### Debug prompt

```text
work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md
```

Используется вместо содержательного prompt. Пишет отладочную информацию в документ and pass-артефакты. Если тема содержит `DEBUG_STOP_NOW`, пишет `should_stop=yes`.

### Controller prompt

```text
work/prompts/SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
```

Управляющий prompt для Codex. Он читает discourse/context, сопоставляет темы с файлами, создаёт resolved-targets trace and запускает worker-subagents. TS не хранит очередь документов.

### Test controller prompt

```text
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
```

Проверяет цепочку на debug-документах, не трогая реальные досье.

### README

```text
work/automation/README.md
```

Содержит примеры dry-run, debug-запуска and содержательного запуска одного документа.

## Дополнительное изменение протокола

`work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md` обновлён: pass-артефакты теперь лежат в namespace документа:

```text
passes/{безопасное_имя_документа}/{безопасное_имя_документа}_after_pass_03.md
```

Это нужно для параллельного запуска worker-subagents по разным документам.
