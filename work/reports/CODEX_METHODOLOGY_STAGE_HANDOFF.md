# Codex methodology stage handoff

Дата: 2026-06-08  
Статус: обновлено после разделения общего протокола и prompt для методологических досье.

## Новая структура

Общий протокол источникового пополнения документов:

```text
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
```

Prompt-спецификация для методологических досье:

```text
work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
```

Старые файлы `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md` and `work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md` помечены как superseded.

## Как использовать

Сначала запустить проверку готовности:

```text
work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md
```

Затем внешний запуск должен передавать Codex явное `{имя документа}`, `{название методологии}` and при необходимости `{номер прохода}` вместе с prompt:

```text
work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
```

## Главное правило

Общий протокол не знает о досье. Он описывает работу с любым документом, который накапливает источникозависимый материал.

Prompt по методологическому досье не дублирует шаги протокола. Он только уточняет, какие детали методологии нужно искать и как понимать качество досье.
