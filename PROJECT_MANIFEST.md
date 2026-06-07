# Project manifest

Архив собран как чистая основа `main` для репозитория сайта агентской разработки.

## Версия

`v14-main` от 2026-06-06.

## Главное отличие

В этом архиве нет `/work`. Это чистое принятое состояние, от которого можно создать рабочую ветку. Рабочий дискурс и task-local документы должны появляться в `/work` только в рабочей ветке.

## Основные решения

- `main` — чистое состояние без `/work`.
- Мелкие низкорисковые правки можно коммитить напрямую в `main` по явному разрешению пользователя.
- Крупные задачи и текущий дискурс ведутся в рабочих ветках.
- Контракт задачи и порядок выполнения объединены в `protocols/rules/codex-task-work-protocol.md`.
- Один skill — один Markdown-файл в `protocols/skills/`.

## Лицензия

- Добавлен `LICENSE.md` с простой лицензией CC BY 4.0 для репозитория.
- Раздельное лицензирование кода и контента намеренно не вводилось, чтобы не усложнять публичный scaffold.


## v14 update

Added chat-github commit-anchored revision rules: read `work/discourse.md` before work, read relevant `/work` documents or all if unclear, create new working files in repository `/work`, update existing documents through anchored commits instead of chat-local copies, and update discourse at the end of non-trivial work.


## v14 update

- Added `protocols/rules/discourse-maintenance-rules.md` as the shared discourse invariant.
- Re-separated `chat-github-repo-work-protocol.md` and `codex-task-work-protocol.md`: ChatGPT/GitHub writes vs Codex task execution.
- Updated related skills and `AGENTS.md` to route each mode explicitly.
