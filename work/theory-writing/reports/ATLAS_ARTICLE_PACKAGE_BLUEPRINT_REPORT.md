# Atlas article package blueprint report

Дата: 2026-06-12.

## Что сделано

Создан отдельный документ:

```text
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
```

Он фиксирует будущий шаблон планов для больших concept-first статей атласа.

## Основные решения

- Atlas article package использует отдельную сильную очередь: 25 рабочих проходов + финальная проверка.
- Внутренние ограничения на объём запрещены: объём определяется полнотой раскрытия концепции и источниковой фактуры.
- Добавлены два свободных прохода добора материала после направленных source-depth проходов.
- Внешние источники разрешены, особенно для поиска реальных изображений, screenshots, diagrams, UI and source-specific details; предпочтение у первоисточников.
- Локальные релевантные ассеты должны вставляться в статью как `<figure><img ...></figure>`, даже если тяжёлые файлы не переданы в конкретный package context.
- Внешние реальные изображения не скачиваются в writing package, но ставятся inline как `external-real-candidate` placeholders и выносятся в нижний раздел `Внешние изображения для asset-pass` / external image queue.
- Синтетические схемы остаются редкими и допустимы только при явной нетривиальной пользе.
- C5 полезен для конкретизации планов, но не является жёсткой зависимостью для разработки общего blueprint или первых конкретных article plans; если C5 отсутствует, фиксируется `C5 sync pending`.

## Связанные документы

Обновлены `START.md`, `work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md`, `work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md`, `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md`, `protocols/rules/visual-assets-and-figures.md`, `work/theory-writing/CORE_NODES_WRITING_PLAN.md`, `work/theory-writing/WORKING_DOCUMENTS_MAP.md`, `work/discourse.md` and service files.
