# 16 — финальная редакция главы

Статус: выполнено. Основной файл главы доведён и сохранён как:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
```

Рабочий черновик в `10_10_full_draft.md` синхронизирован с этим основным файлом.

## Что проверено

### Связь с соседними главами

Глава VIII удерживает своё место между соседними слоями:

- после главы VII: PWG/state показывает, где находится работа, но не выбирает следующий режим;
- перед главой IX: process profile выбирает режим, но ещё не гарантирует реальные права и среду исполнения;
- перед главой X: Gas Town/Beads обозначены как организационная среда для множества линий работы, а не раскрыты в этой главе.

### Сохранение фактуры

Сохранены ключевые источниковые линии:

- GSD: phase loop, `.planning/`, planning artifacts, fresh contexts, specialist agents;
- BMAD: Workflow Map, `bmad-help`, `bmad-spec`, story cycle, `bmad-create-story`, `bmad-correct-course`, established projects, `project-context.md`, `bmad-investigate`;
- small profiles: Jesse Vincent, HumanLayer, Matt Pocock;
- boundary layer: Beads and Gas Town.

P11-добор по BMAD brownfield/investigation не потерян, но после P14 он сжат так, чтобы BMAD не превращался в отдельную статью.

### Плотность источников

В основном файле главы осталось 21 markdown-link. Ссылки стоят рядом с местами, где фактура вводится. Внешние источники не перенесены в общий список без привязки к тексту.

### Язык

После P13 и финальной вычитки убраны наиболее заметные следы английского связующего языка:

- `and/or/as` почти полностью исчезли из русских предложений;
- `stack and versions, critical implementation rules...` переписано по-русски;
- `production code` заменено на `production-код`;
- `role/workflow profile` заменено на «профиль роли или рабочего процесса»;
- `Investigation and implementation reward different instincts` переписано как различие двух режимов работы.

Source-native terms сохранены, где они работают как названия команд, ролей, файлов, статусов или устойчивых понятий источника.

### Внутренние комментарии

В основном тексте не обнаружены служебные пометки P11/P12/P13/P14, рабочие листы, TODO/FIXME или внутренние инструкции пакета.

## Финальные точечные правки

В `10_10_full_draft.md` and `VIII_protected_process_profiles.md` внесены последние языковые правки:

- `project-context.md` теперь описан через «стек и версии, критические правила реализации, организацию кода, паттерны тестирования и ограничения конкретного проекта»;
- BMAD forensic paragraph объясняет `narrative lock-in` and `evidence amnesia` русской фразой, а не оставляет их без расшифровки;
- различие investigation / implementation сформулировано как различие рабочих режимов, а не как английская цитатная формула;
- финальный BMAD-risk paragraph больше не использует `role/workflow profile` как английский псевдотермин.

## Состояние основных файлов после прохода

Создан/обновлён:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
```

Уже созданные companion files остаются актуальными:

```text
work/theory-writing/chapters/VIII_protected_process_profiles_source_register.md
work/theory-writing/chapters/VIII_protected_process_profiles_fragment_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_atlas_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_dossier_gap_notes.md
work/theory-writing/chapters/VIII_protected_process_profiles_external_discovery_log.md
work/theory-writing/chapters/VIII_protected_process_profiles_story_anchors.md
work/theory-writing/chapters/VIII_protected_process_profiles_figure_candidates.md
work/theory-writing/chapters/VIII_protected_process_profiles_open_questions.md
work/theory-writing/chapters/VIII_protected_process_profiles_degradation_and_duplication_audit.md
```

## Остаточные watchpoints

- Если в будущем добавлять визуализацию, сначала использовать `fig-viii-process-profile-interface`, а не method-specific diagrams.
- Не расширять BMAD-раздел без удаления или замены менее важной детали.
- Перед публикацией перепроверить актуальность BMAD/GSD docs, если пройдёт значительное время.
