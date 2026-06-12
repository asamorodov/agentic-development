# Claude Code product migration dossier — anti-degradation report

Проверка проведена против последнего текста досье перед раскрытием кейсов и против расширенной версии перед консолидацией.

## Использованные версии

- Baseline before case expansion: `/mnt/data/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.before.md`.
- Expanded before consolidation: `/mnt/data/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.expanded_before_consolidation.md`.
- Consolidated dossier: `work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md`.

## Количественная сверка

- Baseline: 108 927 знаков, 412 строк.
- Expanded before consolidation: 112 607 знаков, 490 строк.
- Consolidated dossier: 106 898 знаков, 462 строк.
- Source URLs from baseline preserved: 40/40.
- Missing baseline URLs: none.
- New URLs relative to baseline: none.

## Что считалось деградацией

- Потеря источников, ссылок или source-backed facts из baseline.
- Замена конкретных кейсов общими тезисами.
- Внутренний “самоотчёт” в основном тексте досье: “в текущем проходе”, “сверка”, “предыдущий текст”, “после переработки”.
- Несистемные служебные секции внутри досье, которые должны жить в отчёте, а не в источниковом документе.
- Регрессия исправлений: Karthik attribution, Rakuten source status, `/claude-api migrate` vs old `migrate-installer`.

## Найденная деградация и исправления

- Фактической деградации по источникам не найдено: все URLs из baseline сохранены.
- Редакционная деградация найдена: после раскрытия кейсов в основной файл попали служебные фрагменты `## Сверка с предыдущим текстом досье` и `## Детали, восстановленные после сверки с последней загруженной версией`. Они удалены из main dossier; их функция перенесена в этот внешний report.
- Убраны self-referential phrases: “раздел переписан”, “в текущем проходе”, “досье раньше”, “предыдущий текст”.
- Source sections нормализованы: вместо pass/progress headings используются тематические headings по типу источников.
- Illustration candidates consolidated: DEV article images moved into `### Кандидаты из DEV article`; duplicate loose bullet removed.
- Corrective facts preserved: DEV article author is Karthik Subramanian; Rakuten `devin-clone` wording remains unconfirmed; confirmed API migration entry point is `/claude-api migrate`.

## Anchor-fact coverage check

| Anchor | baseline | expanded | consolidated |
|---|---:|---:|---:|
| `Reddit SaaS` | 0 | 4 | 4 |
| `Next.js 16` | 2 | 2 | 2 |
| `React 19` | 2 | 2 | 2 |
| `Drizzle/Postgres` | 2 | 2 | 2 |
| `Better Auth` | 2 | 2 | 2 |
| `Hono` | 7 | 9 | 8 |
| `cron` | 6 | 11 | 10 |
| `claude.md` | 42 | 36 | 33 |
| `status.md` | 10 | 10 | 10 |
| `handoff.md` | 10 | 10 | 10 |
| `do not touch` | 2 | 2 | 2 |
| `Karthik Subramanian` | 0 | 6 | 5 |
| `181` | 1 | 2 | 2 |
| `25+` | 1 | 2 | 2 |
| `18-service` | 1 | 2 | 1 |
| `17 memory` | 4 | 7 | 6 |
| `context funnel` | 5 | 7 | 6 |
| `brainstorming` | 3 | 5 | 4 |
| `agent teams` | 3 | 5 | 3 |
| `37KB` | 1 | 2 | 2 |
| `46KB` | 2 | 3 | 3 |
| `updateConfluencePage` | 3 | 3 | 3 |
| `19 Jira` | 3 | 3 | 3 |
| `customfield_10058` | 3 | 4 | 4 |
| `worktree` | 62 | 47 | 46 |
| `/execute-plan` | 4 | 7 | 6 |
| `manage-mr` | 4 | 6 | 5 |
| `/loop` | 6 | 8 | 7 |
| `SonarQube` | 6 | 11 | 10 |
| `Chrome DevTools` | 2 | 2 | 2 |
| `Figma` | 3 | 4 | 3 |
| `Postman` | 3 | 4 | 3 |
| `move-to-qa` | 2 | 1 | 1 |
| `30–40` | 1 | 1 | 1 |
| `15 рабочих` | 0 | 0 | 1 |
| `15 work` | 1 | 2 | 1 |
| `5,000` | 0 | 2 | 2 |
| `50 tickets` | 1 | 2 | 2 |
| `580 tests` | 1 | 2 | 2 |
| `95%` | 2 | 4 | 4 |
| `91%` | 1 | 2 | 2 |
| `Winder` | 38 | 41 | 37 |
| `Kodit` | 28 | 18 | 15 |
| `migration-project` | 8 | 7 | 6 |
| `MIGRATION.md` | 21 | 20 | 19 |
| `claude --print` | 8 | 5 | 5 |
| `VectorChord` | 1 | 4 | 3 |
| `reciprocal` | 1 | 4 | 3 |
| `snippets` | 2 | 5 | 4 |
| `L2` | 0 | 2 | 2 |
| `cosine` | 0 | 2 | 2 |
| `Augmented Code` | 24 | 25 | 23 |
| `9,835` | 3 | 3 | 3 |
| `six-gate` | 0 | 1 | 1 |
| `6-gate` | 3 | 3 | 3 |
| `FactoryBot` | 0 | 2 | 2 |
| `AASM` | 0 | 3 | 3 |
| `Stripe` | 26 | 23 | 19 |
| `10,000` | 7 | 7 | 7 |
| `signed enterprise binary` | 0 | 2 | 2 |
| `Wiz` | 23 | 22 | 18 |
| `pypdf` | 4 | 4 | 4 |
| `50,000` | 6 | 6 | 6 |
| `18,413` | 0 | 1 | 1 |
| `99% match` | 0 | 2 | 2 |
| `Rakuten` | 20 | 21 | 17 |
| `vLLM` | 0 | 7 | 6 |
| `99.9` | 0 | 5 | 4 |
| `79%` | 0 | 5 | 4 |
| `/claude-api migrate` | 4 | 9 | 7 |
| `migrate-installer` | 4 | 4 | 3 |
| `April 23` | 2 | 3 | 3 |
| `v2.1.116` | 1 | 2 | 2 |
| `pg-migration-reviewer` | 7 | 7 | 6 |
| `persist-memory.sh` | 3 | 2 | 2 |
| `/qcheck` | 1 | 4 | 3 |
| `HOSPR210` | 6 | 7 | 7 |
| `OPPSCAL` | 5 | 6 | 6 |
| `BILL-UNITS2` | 1 | 3 | 3 |
| `Comment and Control` | 8 | 8 | 8 |
| `ANTHROPIC_API_KEY` | 4 | 3 | 3 |
| `GITHUB_TOKEN` | 4 | 3 | 3 |

## Смысловой вывод

Основной текст после консолидации короче expanded version because process/comparison material was removed from the dossier and externalized here. This is not factual compression of cases. The concrete case material remains in the main sections: Reddit SaaS threshold, Karthik SDLC loop, Winder/Kodit semantic failure, Augmented Code gated pipeline, official customer stories, API migration guide, Claude Code quality postmortem, headless automation, mechanism layer, Vinny Carpenter, community cloud-thread reports, TechChannel/Swimm and Comment-and-Control.

Remaining editorial caveat: the dossier still deliberately keeps many English technical terms and source names (`worktree`, `MCP`, `review`, `gates`, `customer story`, `field report`) because they are part of the source vocabulary. The anti-degradation pass focused on removing self-talk and preserving factual/detail density, not on full Russian language normalization.
