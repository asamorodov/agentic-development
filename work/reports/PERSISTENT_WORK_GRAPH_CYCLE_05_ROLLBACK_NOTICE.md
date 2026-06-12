# Persistent Work Graph — rollback notice for cycle 05

Дата: 2026-06-09.

Статус: `cycle_05` отозван. Каноничным состоянием PWG-досье считаются `cycles_01_04`.

Причина: `cycle_05` слишком сильно сместил досье из режима source-backed mechanism dossier в режим проектирования будущей реализации. Раздел про файловую схему перед SQLite/Dolt может быть полезен как отдельная предварительная техническая заметка, но он не должен входить в основное досье `Persistent Work Graph` и не должен становиться основанием для будущей теоретической главы.

## Каноническая граница

Канонично для PWG-линии:

```text
cycle_01: Beads / issue graphs / Taskmaster / durable execution contrasts
cycle_02: multi-pass document workflow primitives
cycle_03: parallel-agent coordination / shared-state research
cycle_04: safe parallel source-work protocol
```

Неканонично и не применять:

```text
cycle_05: file-layout implementation sketch before SQLite/Dolt
```

## Если cycle 05 уже применён

Zip-overlay не удаляет файлы. Если `persistent_work_graph_dossier_cycles_01_05_delta_from_git5.zip` уже был наложен на рабочую копию, нужно удалить вручную:

```text
work/dossier-passes/persistent-work-graph/cycle_05_prompt_file_layout_implementation_sketch.md
work/dossier-passes/persistent-work-graph/cycle_05_source_discovery.md
work/dossier-passes/persistent-work-graph/cycle_05_source_opening.md
work/dossier-passes/persistent-work-graph/cycle_05_dossier_transfer.md
work/dossier-passes/persistent-work-graph/cycle_05_language_repair.md
work/dossier-passes/persistent-work-graph/cycle_05_delta.md
work/dossier-passes/persistent-work-graph/cycle_05_should_stop.txt
work/dossier-passes/persistent-work-graph/dossier_after_pass_05.md
```

После удаления этих файлов нужно восстановить канонические версии документов из overlay `persistent_work_graph_dossier_cycles_01_04_canonical_delta_from_git5.zip`.

## Терминологическая поправка

В публично читаемых рабочих текстах не используется внутреннее короткое название многопроходного документного процесса. Для общего текста используются нейтральные формулировки:

```text
многопроходный документный процесс
параллельная работа с источниками
пакет свидетельств
проход синтеза
```
