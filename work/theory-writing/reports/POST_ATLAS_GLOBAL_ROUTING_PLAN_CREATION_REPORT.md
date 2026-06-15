# Post-Atlas global routing plan creation report

Дата: 2026-06-13.

Создан repo-level target-group plan:

```text
work/theory-writing/target-group-plans/POST_ATLAS_GLOBAL_CORPUS_ROUTING_TARGET_GROUP_PLAN.md
```

Причина: пользователь уточнил, что общий подготовительный слой должен работать по всему развёрнутому репозиторию, который подключается отдельно, а не по self-contained архиву со всеми входными файлами.

Ключевые решения:

- план помечен как `repo-snapshot-bound`;
- не требуется включать весь корпус файлов в executor package;
- будущий executor, если он будет собран, должен запускаться в корне репозитория;
- план создаёт routing maps, а не главы;
- external discovery classified globally, but executed only by future per-chapter packages when needed;
- language/style cleanup is included for generated maps, but maps must remain working documents, not public essays.

Обновлены:

```text
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/CHECKS.json
```

Статус: ready_for_manual_review.
