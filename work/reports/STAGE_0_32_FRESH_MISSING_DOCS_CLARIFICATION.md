# Stage 0.32 — fresh mode and missing target documents

Дата: 2026-06-09  
Статус: уточнение перед реальным запуском методологических досье.

## Проблема

В `work/prompts/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION.md` была некорректная формулировка: если целевой файл отсутствует, controller должен остановиться and спросить пользователя.

Это противоречит intended fresh mode.

## Решение

Теперь зафиксировано:

```text
если target document отсутствует and mode=fresh:
  это нормально;
  TS-loop должен создать документ through --mode fresh --fresh-action stub;
  controller не должен останавливать запуск только из-за отсутствия файла.
```

Остановка нужна только если:

```text
discourse/project files явно указывают другой canonical path;
mapping конфликтует с текущей структурой репозитория;
mode=continue and document is missing.
```

## Где отражено

Обновлены:

```text
work/prompts/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION.md
work/prompts/SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/automation/README.md
```

Код `backupAndResetDocument` уже поддерживал это поведение: если документа нет, он создаёт parent directory and пишет fresh stub.
