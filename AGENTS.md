# Инструкции для Codex и других агентов

Этот репозиторий содержит рабочий сайт и корпус Markdown-документов по агентской разработке.

## Карта репозитория

- `content/` — источник содержательного текста для сайта.
- `site/` — текущий построенный сайт. Его можно править в малых технических задачах.
- `site-spec/` — спецификация сайта: структура, навигация, ссылки, якоря, последовательное чтение и проверки.
- `protocols/` — правила работы, повторяемые skills и готовые запросы.
- `project/` — документация о репозитории, решениях, планах, ветках и source precedence.
- `work/` — рабочая зона текущей активной задачи рабочей ветки. В чистом `main` этой папки обычно нет. Главный файл задачи в рабочей ветке — `work/discourse.md`.

## Базовое чтение перед задачами

Перед любой нетривиальной задачей сначала прочитайте:

- `project/repository-structure.md`
- `project/source-precedence.md`

Если задача относится к текущей активной работе в `/work`, также прочитайте:

- `work/discourse.md`
- `protocols/rules/discourse-maintenance-rules.md`

После этого оцените остальные файлы в корне `/work` и прочитайте те, которые относятся к текущей операции.

## Разделение режимов работы

Для Codex task/thread/session используйте:

- `protocols/skills/codex-task-work.md`
- `protocols/rules/codex-task-work-protocol.md`

Для ChatGPT, который пишет в репозиторий через GitHub-интеграцию, используйте:

- `protocols/skills/chat-github-repo-work.md`
- `protocols/rules/chat-github-repo-work-protocol.md`

Для обновления дискурса оба режима используют:

- `protocols/skills/maintain-work-discourse.md`
- `protocols/rules/discourse-maintenance-rules.md`

Не смешивайте эти режимы: Codex работает как task executor в repo/worktree/cloud; ChatGPT работает как смысловой чат с точечными GitHub commit-операциями.

## Skills

Повторяемые рабочие режимы лежат в:

```text
protocols/skills/
```

Один skill — один Markdown-файл. Перед применением skill прочитайте соответствующий файл. Не ищите общий `skills.md` как замену skill-файлам.

Основные skills:

- `protocols/skills/maintain-work-discourse.md`
- `protocols/skills/codex-task-work.md`
- `protocols/skills/chat-github-repo-work.md`
- `protocols/skills/finalize-working-branch-for-main.md`
- `protocols/skills/stage-0-5-coverage-audit.md`
- `protocols/skills/restore-anchor-case-from-baseline.md`
- `protocols/skills/rollback-working-change.md`

## Что читать перед конкретными задачами

Перед правкой сайта прочитайте:

- `project/repository-structure.md`
- `site-spec/README.md`
- релевантные файлы из `site-spec/`
- `protocols/rules/site-update-rules.md`
- `protocols/rules/content-preservation.md`

Перед правкой содержательного текста прочитайте:

- `project/source-precedence.md`
- `protocols/rules/language-style-rules.md`
- связанные файлы, перечисленные внутри `language-style-rules.md`
- `protocols/rules/english-source-handling.md`
- `protocols/rules/source-and-provenance.md`
- `protocols/rules/content-preservation.md`

Перед работой над теорией прочитайте:

- `project/repository-structure.md`
- `project/source-precedence.md`
- `protocols/skills/codex-task-work.md`
- `protocols/rules/theory-rebuild-rules.md`
- `work/discourse.md`
- релевантные сопутствующие документы в корне `/work`, включая approved plan, source map, baseline restore rule and seed-файлы SPDD/Gas Town, если они нужны для операции

Перед работой ChatGPT с репозиторием через GitHub-интеграцию прочитайте:

- `protocols/skills/chat-github-repo-work.md`
- `protocols/rules/chat-github-repo-work-protocol.md`
- `work/discourse.md`, если задача относится к текущей рабочей ветке или `/work`
- релевантные документы из корня `/work`; если неясно, какие нужны, прочитайте все релевантные текстовые документы в корне `/work`
- `project/branching-and-task-model.md`, если задача связана с ветками

Перед финализацией рабочей ветки в `main` прочитайте:

- `protocols/skills/finalize-working-branch-for-main.md`
- `protocols/rules/git-branching-and-merge-protocol.md`
- `project/branching-and-task-model.md`

Перед откатом отдельной правки прочитайте:

- `protocols/skills/rollback-working-change.md`
- `protocols/rules/git-branching-and-merge-protocol.md`
- `project/branching-and-task-model.md`

Перед созданием или правкой рабочих запросов прочитайте:

- `protocols/rules/prompt-construction-rules.md`
- `protocols/README.md`

Перед изменением структуры репозитория или переносом файлов прочитайте:

- `project/repository-structure.md`
- `project/decisions.md`
- `project/open-questions.md`

## Жёсткие правила

- Мелкие низкорисковые правки можно коммитить прямо в `main`, если пользователь явно разрешил запись. Крупные изменения и работа с `/work` идут через рабочую ветку.
- Пишите пользовательский текст на русском языке, кроме допустимых технических имён и коротких точных фрагментов.
- Не переписывайте и не сокращайте `/content`, если задача касается только сайта, навигации или структуры репозитория.
- Если правка в `/site` меняет устойчивое поведение сайта, обновите `/site-spec`.
- Не добавляйте служебные отчёты, README, pass-файлы, build-файлы или рабочие документы в пользовательскую навигацию сайта.
- Не создавайте вложенные `AGENTS.md` без явного решения человека. В этом репозитории используется один корневой `AGENTS.md`.
- После нетривиальной сессии по текущей задаче обновите `work/discourse.md` по `protocols/rules/discourse-maintenance-rules.md`.
- Если работа создала, изменила или переоценила файлы, впишите их точные имена прямо в дискурс рядом с соответствующим смысловым ходом.
- При работе ChatGPT с репозиторием через GitHub-интеграцию новые рабочие файлы создавайте в `/work` репозитория, а существующие файлы обновляйте через commit новой версии с понятным commit anchor. Не создавайте “копии внутри чата” как рабочий артефакт.
- Не заявляйте завершение, если нет проверяемых артефактов: изменённых файлов, отчёта, списка проверок or созданных рабочих документов.

## Финальный отчёт

В конце задачи укажите:

1. Какие файлы изменены.
2. Какие источники и правила были прочитаны.
3. Какие проверки выполнены.
4. Какие проверки не выполнялись.
5. Как обновлён `work/discourse.md`, если задача была нетривиальной.
6. Какие вопросы остались открытыми.
