# Agentic Dev Site

Репозиторий содержит рабочий сайт и корпус документов по агентской разработке.

Основные папки:

- `content/` — содержательные Markdown-документы, из которых строится сайт.
- `site/` — текущий построенный сайт, который можно открыть локально через `site/index.html`.
- `site-spec/` — спецификация структуры и поведения сайта.
- `protocols/` — правила работы и готовые запросы для Codex.
- `project/` — документация о самом репозитории, решениях и планах.
- `work/` — рабочая зона текущей активной задачи рабочей ветки. В чистом `main` этой папки обычно нет. Главный файл в рабочей ветке — `work/discourse.md`.

Перед работой с Codex сначала дайте ему запрос из `protocols/prompts/first-codex-task.md`, чтобы проверить, как он понимает структуру репозитория.

## Как открыть текущий сайт

Откройте `site/index.html` в браузере. Текущий сайт является рабочим артефактом, а не одноразовой папкой `dist`.

## Первый шаг в Codex

Скопируйте запрос из `protocols/prompts/first-codex-task.md` и попросите Codex осмотреть репозиторий без правок. После ответа проверьте, что он правильно различает `/content`, `/site`, `/site-spec`, `/protocols`, `/project` и `/work`, а также понимает роль `work/discourse.md` как главного носителя дискурса активной задачи. Отдельно проверьте, что Codex понял: значимые файлы и артефакты должны называться прямо в дискурсе, иначе связь между разговором и рабочими документами теряется.


## Skills

Повторяемые режимы работы лежат в `protocols/skills/`. Один skill — один Markdown-файл. Prompt-файлы в `protocols/prompts/` могут вызывать эти skills с параметрами конкретной задачи.

Ключевая модель работы: Git branch = активная задача или подзадача; `work/discourse.md` = живая память рабочей ветки; `main` = принятое чистое состояние без `/work`; мелкие низкорисковые правки можно коммитить прямо в `main` по явному разрешению пользователя.


## О main и рабочей ветке

Этот архив содержит чистую основу `main`: папки `/work` здесь нет. Для текущей задачи создайте рабочую ветку и добавьте в неё `/work` из workbranch-архива или через Codex/ChatGPT.

## License

This repository is licensed under CC BY 4.0. See `LICENSE.md`.


## ChatGPT/GitHub integration

When ChatGPT writes to this repository through the GitHub integration, it should follow `protocols/rules/chat-github-repo-work-protocol.md`: read `work/discourse.md` before non-trivial work, create new working files in repository `/work`, update existing documents through anchored commits, and update the discourse after non-trivial work.


## Protocol note

ChatGPT/GitHub and Codex protocols are intentionally separate. Codex task execution uses `protocols/rules/codex-task-work-protocol.md`; ChatGPT write-through-GitHub uses `protocols/rules/chat-github-repo-work-protocol.md`; both share `protocols/rules/discourse-maintenance-rules.md` for `work/discourse.md`.
