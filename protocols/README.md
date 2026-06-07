# Протоколы работы

Эта папка содержит три разных слоя рабочих документов: устойчивые правила, повторяемые рабочие режимы и готовые запросы.

```text
protocols/
  rules/
  skills/
  prompts/
```

`rules/` содержит устойчивые инварианты: язык, стиль, источники, сохранение текста, работу с текущей задачей, работу ChatGPT с GitHub, ветки, merge and discourse maintenance. Эти файлы отвечают на вопрос: какие правила нельзя нарушать.

`skills/` содержит повторяемые рабочие режимы. Один skill — один Markdown-файл. Skill отвечает на вопрос: как выполнить типовую работу в конкретной ситуации. Отдельная папка под skill создаётся только если skill перерастёт один файл и потребует собственных шаблонов, скриптов или больших вспомогательных материалов.

`prompts/` содержит активные запросы, которые можно копировать в Codex, ChatGPT или новый чат. Prompt обычно вызывает skill и добавляет параметры задачи: ветку, файлы, ограничение, human gate, ожидаемый отчёт.

## Разделение Codex и ChatGPT

В репозитории существуют два похожих, но разных операционных протокола.

Codex-задачи выполняются по:

```text
protocols/rules/codex-task-work-protocol.md
protocols/skills/codex-task-work.md
```

Это режим `task/thread/session`: Codex работает в repo/local/worktree/cloud, меняет файлы, запускает проверки, готовит diff/commit/PR and updates discourse.

Работа ChatGPT с репозиторием через GitHub-интеграцию выполняется по:

```text
protocols/rules/chat-github-repo-work-protocol.md
protocols/skills/chat-github-repo-work.md
```

Это режим `chat answer + GitHub write`: ChatGPT перед ответом читает repo, обновляет файлы через GitHub API, коммитит точечные изменения and reports commit anchors.

Общий инвариант для обоих режимов:

```text
protocols/rules/discourse-maintenance-rules.md
protocols/skills/maintain-work-discourse.md
```

И Codex, и ChatGPT должны обновлять `work/discourse.md` по одним правилам, но операционные шаги у них разные.

## Главные маршруты

Для работы Codex с активной задачей начинайте с `skills/codex-task-work.md`, `rules/codex-task-work-protocol.md` and `work/discourse.md`.

Для работы ChatGPT с репозиторием через GitHub-интеграцию начинайте с `skills/chat-github-repo-work.md` and `rules/chat-github-repo-work-protocol.md`.

Для обновления дискурса используйте `skills/maintain-work-discourse.md` and `rules/discourse-maintenance-rules.md`.

Для переноса результата обсуждения между ChatGPT и Codex без прямой записи в repo используйте `rules/chat-codex-transfer-protocol.md`. Если ChatGPT имеет write access, предпочтительнее прямой commit по `chat-github-repo-work-protocol.md`.

Для финализации ветки в `main` используйте `skills/finalize-working-branch-for-main.md` and `rules/git-branching-and-merge-protocol.md`.

Для отката отдельной правки используйте `skills/rollback-working-change.md`.

Для правки пользовательского текста начинайте с `rules/language-style-rules.md`.

Перед созданием или изменением файлов в `prompts/` читайте `rules/prompt-construction-rules.md`.

## Task protocol

Форма постановки задачи и порядок выполнения Codex объединены в `rules/codex-task-work-protocol.md`. Отдельный `codex-task-contract.md` не используется.

Мелкие низкорисковые правки могут коммититься прямо в `main` по явному разрешению пользователя; крупные изменения выполняются через рабочую ветку.
