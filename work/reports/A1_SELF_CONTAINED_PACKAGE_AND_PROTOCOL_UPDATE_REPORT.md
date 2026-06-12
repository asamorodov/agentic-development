# A1 self-contained package and protocol update report

Дата: 2026-06-10.
База: `git(8).zip`.

## Что сделано

1. Уточнён `work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md`: режим по умолчанию для пакетов-заданий теперь self-contained. Все существующие target-файлы и read-only источники, перечисленные в планах целевых групп, должны упаковываться внутрь исполнительного архива. `repo-snapshot-bound` режим остаётся допустимым только как явное исключение.
2. Уточнён `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md`: файлы из секций «Обрабатываемые файлы» и «Файлы для чтения» по умолчанию становятся содержимым исполнительного пакета.
3. В `work/theory-writing/target-group-plans/A1_CHANGE_NOT_PROMPT_TARGET_GROUP_PLAN.md` удалено чтение самого build-time плана из prompt-ов. План остаётся документом сборки, но не должен материализоваться в исполнительном слое как источник общей структуры.
4. Собран новый self-contained A1-пакет: `a1_writing_task_package_self_contained_gated_python_record_chain_v4.zip`.

## Свойства нового A1-пакета

- пакет не требует repo snapshot;
- все внутренние источники, указанные в A1 target group plan, находятся в opaque payload;
- видимый Python остаётся generic runner/materializer;
- Python не содержит списка документов, очереди prompt-ов, числа шагов, subject-specific логики, текста заданий или финальной упаковочной логики;
- каждый шаг материализует уникальный рабочий `.md`-файл;
- не финальные рабочие листы сами предписывают снова запустить Python;
- финальный рабочий лист не предписывает запуск Python;
- emergency-команда поддерживается через `python q8v4m.py emergency`.

## Проверки

- `python -m json.tool work/checks.json`;
- `unzip -t a1_writing_task_package_self_contained_gated_python_record_chain_v4.zip`;
- smoke-test: первый запуск создаёт рабочий лист;
- smoke-test: после фиктивных обязательных output-файлов второй запуск создаёт другой рабочий лист;
- grep по видимому Python: нет `docs`, `passes_per_doc`, `total`, `map_task`, `content/stories`, `work/dossiers`, имени A1 target-файла.
