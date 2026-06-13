# spdd_method_source_transfer_ledger

Статус: P23 sync. Это исторический журнал переноса фактов, а не coverage-матрица. Текущие блокеры вынесены в `spdd_method_open_questions.md`; текущая роль источников — в `spdd_method_source_usage.md`.

## Перенесено в основной текст

| Тема | Перенесённая фактура | Куда перенесено | Источник |
| --- | --- | --- | --- |
| Prompt как артефакт поставки | Промпт хранится рядом с кодом, ревьюится и синхронизируется, а не исчезает после генерации. | Введение. | Fowler/Thoughtworks SPDD. |
| Capability/control | Сильная модель не должна выбирать несущие проектные компромиссы; SPDD ограничивает пространство допустимых вариантов. | «Почему сильной модели всё равно нужны границы намерения». | OpenSPDD design philosophy. |
| Статус между свободным prompt и формальной спецификацией | SPDD как низко-/среднеформальный слой, без независимого оракула правильности Canvas. | «Место SPDD…». | Lahiri + Fowler SDD comparison. |
| REASONS Canvas | Семь частей Canvas и их рабочие функции. | «REASONS Canvas как рабочий контракт». | Fowler/Thoughtworks SPDD; OpenSPDD templates. |
| Работа Canvas с контекстом | Полное чтение `@`-ссылок, целевое исследование проекта, отсутствие заполнителей. | «Как Canvas собирает и ограничивает контекст». | `/spdd-analysis`, `/spdd-reasons-canvas`. |
| Рабочий процесс OpenSPDD | `story → analysis → reasons-canvas → generate → api-test → code-review → prompt-update/sync`. | «Рабочий процесс OpenSPDD». | OpenSPDD README + templates. |
| Свидетельства поведения | `scripts/test-api.sh`, `curl`, таблицы expected/actual, нормальные и ошибочные сценарии. | «Свидетельства поведения и ревью по намерению». | `/spdd-api-test`, Fowler/Thoughtworks. |
| Drift review | Положительный, отрицательный и направленный дрейф; неявные решения; scope creep. | «Свидетельства поведения и ревью по намерению». | `/spdd-code-review`. |
| Пример с биллингом | `modelId`, планы Standard/Premium, prompt/completion rates, квоты, отрицательные значения. | «Свидетельства поведения…». | Fowler/Thoughtworks SPDD. |
| Prompt-update / sync | Два направления: изменение намерения → prompt → code; рефакторинг/структура → code → prompt. | «`prompt-update` и `sync`». | OpenSPDD templates; WebReactiva as secondary practical wording. |
| Команды, навыки и границы доверия | Copilot prompts, Codex skills, `.agents/skills/<id>/SKILL.md`, `allow_implicit_invocation: false`, trust boundary. | «Команды, навыки и границы доверия». | OpenSPDD README. |
| Плановое сопровождение спецификаций | Плановое сопровождение specification corpus через workflow и issue. | «Плановое сопровождение спецификаций». | `github/gh-aw` workflow and issue. |
| Fit / ROI / failures | Где SPDD оправдан и где может стать лишней церемонией; неверный Canvas, устаревший Canvas, ложная уверенность. | «Где SPDD оправдан» и «Сценарии сбоев». | Fowler/Thoughtworks, OpenSPDD design philosophy, dossier synthesis. |
| Граница с persistent work graph | SPDD синхронизирует Canvas/code, но не хранит очередь, blockers, ownership and recovery. | «Где SPDD заканчивается». | B1 fragment; Beads contrast from B1 used conceptually without adding Beads detail. |

## Сознательно не развёрнуто в P01 — исторический снимок

Эти пункты объясняют, почему первичный черновик не пытался охватить всё досье. После P23 они не являются автоматическими долгами статьи; актуальные blockers перечислены ниже и в `spdd_method_open_questions.md`.

- Подробная установка OpenSPDD проверялась точечно в дальнейших проходах, но статья сознательно не стала install manual.
- `/spdd-reverse` не раскрывался как самостоятельная механика; текущий долг возникает только при расширении его роли.
- Визуальные кандидаты обработаны в P11–P13: локальные source-backed изображения и одна синтетическая схема остались в статье, внешние реальные кандидаты вынесены в очередь.
- Сравнение со Spec Kit, Kiro, BMAD, GSD и Constitutional SDD сохранено на уровне границ, чтобы статья не превратилась в обзор всех методологий.
- `daily-spdd-spec-planner` оставлен как короткий внешний сигнал планового сопровождения, без превращения в отдельный режим SPDD.
- Токенная стоимость полного чтения `@`-ссылок названа как риск без численных оценок, потому что разрешённые источники не дают устойчивых чисел.

## Текущие вопросы источников после P23

- Перед публикацией проверить актуальное состояние OpenSPDD README и шаблонов: статья опирается на v0.4.9 templates и на README/design philosophy как на точечные источники.
- Не расширять `/spdd-reverse` без template-level подтверждения.
- При детализации доверия к Codex skills отдельно проверить текущие формулировки README про `allow_implicit_invocation` и недоверенные проекты.
- Внешние реальные кандидаты возвращать в статью только после проверки скачивания, прав и качества.
- Вторичные источники не раздувать: WebReactiva остаётся короткой практической формулировкой, а `mgks.dev` после P23 не представлен в основном тексте.

## P02 contract/boundary transfer

| Тема | Решение P02 | Где отражено |
| --- | --- | --- |
| Reader question | Статья отвечает на вопрос о lifecycle намерения фичи: до кода, во время реализации, после изменений. | `spdd_method_article_contract.md`; раздел «Как читать эту статью» в основном тексте. |
| Article tier | Самостоятельная concept-first статья атласа, глубокий методологический узел SPDD/OpenSPDD. | `spdd_method_article_contract.md`. |
| Neighbor boundaries | Spec Kit, Kiro, CSDD, TDAD, ADR and PWG зафиксированы как соседние статьи/механизмы, не как материал для развёрнутого сравнения внутри SPDD. | `spdd_method_article_contract.md`; `spdd_method_theory_links.md`. |
| C5/A10 | После P23 нет отдельного долга синхронизации; эти фрагменты доступны только как read-only context для конкретных правок границ и связей. | `spdd_method_theory_links.md`; `spdd_method_open_questions.md`. |
| Main text fix | Добавлен раздел «Как читать эту статью», чтобы первый экран не был просто intro и чтобы читатель видел границы статьи. | `work/atlas/articles/spdd_method.md`. |

## P03 dossier inventory

Статус: inventory after reading `SPDD_METHOD_DOSSIER.md` against current article. Это не тотальная coverage matrix; ниже только материал, влияющий на качество статьи.

### Уже перенесено достаточно для P03

| Досье-тема | Статус в статье | Оценка |
| --- | --- | --- |
| SPDD как feature-level intent artifact, а не «длинный prompt» | Есть во введении и reader-question section. | Достаточно для первичной статьи. |
| Capability/control and negative-space logic | Есть раздел о сильной модели и границах намерения; `Safeguards` раскрыты. | Достаточно, но поздний style pass должен убрать перегруженные формулы. |
| REASONS Canvas, семь зон | Есть отдельный раздел с рабочей функцией каждой зоны. | Достаточно; можно усилить examples in source-depth. |
| Context ingestion | Есть раздел про `/spdd-analysis` and `/spdd-reasons-canvas`, `@file`/`@folder`, no truncation. | Достаточно; нужна проверка первоисточников для exact wording. |
| Рабочий процесс | Есть story/analysis/reasons/generate/api-test/code-review/update/sync. | Достаточно; exact file tree не нужен без нового задания. |
| API-test как поведенческое свидетельство | Есть `scripts/test-api.sh`, `curl`, таблицы, `expected`/`actual`. | Достаточно; локальные source-backed изображения добавлены, внешние кандидаты вынесены в очередь. |
| Code-review как ревью соответствия намерению | Есть drift, implicit decisions, semantic diff. | Достаточно; полный output format остаётся внешним кандидатом ассета. |
| Пример с биллингом | Есть `modelId`, Standard/Premium, prompt/completion rates, quotas и P09-разложение по REASONS. | Достаточно; не добавлять вымышленные тарифы или HTTP-коды. |
| Prompt-update vs sync | Есть отдельный раздел и практическая формулировка WebReactiva. | Достаточно; primary templates уже проверены, остаётся только публикационная актуализация ссылок. |
| Tool adapter surface | Есть Copilot prompts, Codex skills, `allow_implicit_invocation`, trust boundary. | Достаточно; не превращать статью в руководство по установке. |
| Daily planner / spec maintenance | Есть краткий раздел с workflow + issue. | Достаточно; после P23 не расширять без нового задания. |
| Fit / ROI / risks | Есть применимость и сценарии сбоев. | Достаточно для P03. |
| Граница с PWG | Есть раздел «Где SPDD заканчивается». | Достаточно; не расширять Beads внутри SPDD. |

### Article-critical материал, обнаруженный как недоданный и уже исправленный в P03

| Материал | Почему важен | Правка |
| --- | --- | --- |
| Различение repo-level instructions и feature-level REASONS Canvas | Без него SPDD можно спутать с `AGENTS.md` / `CLAUDE.md` или project constitution files. | Добавлен абзац в раздел про REASONS Canvas. |
| `/spdd-reverse` как путь от legacy-code | Досье считает его важным сигналом, что SPDD может идти от существующего кода к Canvas. | Добавлен короткий абзац в раздел рабочего процесса; путь оставлен необязательным и ограниченным, не центральным. |

### Материал, не перенесённый в основной текст после P23

| Материал из досье | Текущий статус |
| --- | --- |
| Полная установка OpenSPDD: `openspdd init`, `openspdd generate --all`, точные каталоги. | Не переносить без нового задания: статья объясняет метод, а не установку. |
| `Plan vs REASONS Canvas` example from README. | Сохранён как внешний кандидат изображения; в основной текст не возвращать без проверки прав/качества. |
| Полный формат `/spdd-code-review` report. | Основная механика ревью перенесена; полный снимок отчёта остаётся внешним кандидатом ассета. |
| Дополнительные constraints `/spdd-api-test` вроде no `eval`, timeout details, seed data extraction. | Основная форма свидетельств перенесена; мелкие ограничения не нужны текущему читательскому вопросу. |
| OpenSPDD issues around `reasons-context`, Codex/OpenCode, `go install` module path. | Не переносить: это version/tool noise, а не несущая фактура метода. |
| Roadmap: automated artifact checks, decision memory, organization-level exoskeleton. | Не переносить в SPDD-статью; оставить для соседних теоретических материалов. |
| Detailed comparison with Spec Kit/Kiro/TDAD/CSDD/ADR. | Не переносить: границы уже показаны, сравнительный обзор принадлежит соседним статьям. |

### Что требовало открытия первоисточников и текущий статус

- OpenSPDD README, design philosophy и основные шаблоны были проверены в P04–P08; перед публикацией остаётся только проверка актуальности версий.
- `/spdd-reverse` остаётся источниковым пробелом только при расширении роли команды: текущая статья не строит на нём отдельную механику.
- Fowler/Thoughtworks SPDD был использован для REASONS, примера с биллингом, workflow, fit/limitations и локальных source-backed изображений.
- `github/gh-aw` workflow и issue были использованы как короткий пример планового сопровождения; расширять его не требуется без нового задания.
- WebReactiva оставлен как вторичная практическая формулировка про `prompt-update`/`sync`; `mgks.dev` после P23 не представлен в основном тексте.

### Технические gaps после P23

- Перед публикацией проверить актуальные OpenSPDD README/templates и ссылки на v0.4.9.
- Провести отдельный asset-pass для внешних реальных кандидатов, если они будут возвращаться в основной текст.
- Не превращать текущий ledger в coverage-матрицу: дальнейшие факты должны переноситься в статью или в конкретный blocker, а не в новые бюрократические строки.

## P04 source-depth pass 1 — REASONS Canvas anatomy

### Added to main text

| Addition | Source basis | Main-text location |
| --- | --- | --- |
| REASONS grouped as intent/design, implementation path, quality guardrails. | Fowler/Thoughtworks SPDD; OpenSPDD README. | «REASONS Canvas как рабочий контракт». |
| Plan vs REASONS Canvas distinction: ordinary plan names tasks, Canvas specifies responsibility, package/dependencies/methods/error handling/order. | OpenSPDD README, Plan vs REASONS Canvas section. | «REASONS Canvas как рабочий контракт». |
| Canvas as maintained artifact: versioned, reviewed, reused, improved over time. | Fowler/Thoughtworks SPDD. | New subsection «Почему Canvas должен сопровождаться». |
| Why Canvas can mislead: wrong Canvas, outdated Canvas, too-generic Canvas. | Fowler/Thoughtworks SPDD; OpenSPDD design philosophy. | New subsection «Почему Canvas должен сопровождаться». |
| Repo-level instructions vs feature-level Canvas strengthened. | OpenSPDD design philosophy. | Paragraph after Canvas maintainability. |

### Not added yet

- Full Plan vs REASONS Canvas code block from README: better as visual/source example in later pass, not pasted into main prose now.
- Full Q&A from Fowler article about human-led framework and “why” capture: relevant but would duplicate current maintainability explanation.
- Current OpenSPDD release/version metadata: version-sensitive and not necessary for Canvas anatomy.

## P05 source-depth pass 2 — technical mechanics

### Added to main text

| Addition | Source basis | Main-text location |
| --- | --- | --- |
| OpenSPDD описан как порядок поддержания Canvas, а не как справочник команд. | Combined command-template reading. | Opening of «Рабочий процесс OpenSPDD». |
| `/spdd-story` as boundary-sizing step, not code-analysis step. | `/spdd-story` template. | Workflow section. |
| `/spdd-analysis` as strategic, concept-driven enrichment saved under `spdd/analysis/`. | `/spdd-analysis` template. | Workflow section. |
| `/spdd-reasons-canvas` as creation of fully populated `spdd/prompt/` artifact with no placeholders and no implementation before confirmation. | `/spdd-reasons-canvas` template. | Workflow section. |
| `/spdd-generate` as execution of existing Operations/Norms/Safeguards, not re-planning. | `/spdd-generate` template. | Workflow section. |
| `/spdd-api-test` as behavior evidence with `scripts/test-api.sh`, overview table, expected/actual, bash+curl, timeout, exit code. | `/spdd-api-test` template. | Workflow section. |
| `/spdd-code-review` as read-only intent-alignment review with drift, implicit decisions and scope boundary. | `/spdd-code-review` template. | Workflow section. |
| `/spdd-prompt-update` and `/spdd-sync` distinguished as intent→Canvas and code→Canvas maintenance flows, with section-specific/minimal updates. | `/spdd-prompt-update` and `/spdd-sync` templates. | Workflow section; existing prompt-update/sync section retained. |
| `/spdd-reverse` treated cautiously as legacy onboarding path. | OpenSPDD README; attempted template open did not find a v0.4.9 optional file. | Workflow section. |

### Not added / deliberately bounded

- The article still does not include a complete command reference or every guardrail line from templates; P05’s instruction explicitly asked to explain method function rather than list all commands.
- Exact installation paths for every supported tool remain in the instrument-surface section only at high level. A full installation manual would break the article contract.
- `/spdd-reverse` lacks primary template verification in P05 because the v0.4.9 optional directory exposed `spdd-story`, `spdd-code-review` and `spdd-api-test`, but not `spdd-reverse`; README-level mention is retained and marked as bounded.
- Full generated report/table examples are still not pasted into the main article; they are better candidates for проход визуальных кандидатов и примеровes.

## P06 source-depth pass 3 — limitations and failure modes

### Added to main text

| Addition | Source basis | Main-text location |
| --- | --- | --- |
| Fit/cost rewritten around SPDD as engineering investment rather than universal best practice. | Fowler/Thoughtworks fitness assessment; OpenSPDD design philosophy limitations. | «Где SPDD оправдан». |
| Strong failure mode: convincing but wrong Canvas can make generation, API-test and review align around a wrong business decision. | SPDD dossier; Lahiri/specification-oracle point already present; Fowler Canvas-first workflow. | «Сценарии сбоев». |
| Stale Canvas can be more dangerous than absent documentation. | OpenSPDD design philosophy. | «Сценарии сбоев». |
| Local patch vs updated intent; behavior changes go through prompt-update, refactors through sync. | Fowler/Thoughtworks prompt-update/sync section. | «Сценарии сбоев». |
| Prompt-first inversion: sometimes the Canvas needs re-analysis, not a small patch. | SPDD dossier synthesis. | «Сценарии сбоев». |
| Evidence is auxiliary; API-test/review report do not replace human judgment. | Fowler/Thoughtworks unit-test note; command templates. | «Сценарии сбоев». |
| Sync cost and degradation risk made explicit. | `/spdd-sync` template; OpenSPDD design philosophy. | «Сценарии сбоев». |
| Created degradation audit companion file. | P06 task. | `spdd_method_degradation_audit.md`. |

### Degradation audit status

The new audit file is intentionally not a source-coverage matrix. It tracks failure modes that later style, shortening or visual passes must not erase: wrong Canvas, stale Canvas, local code patch, mechanical prompt-first update, false evidence confidence, sync cost, ceremony, adapter/tool drift and human judgment.


## P07 evidence/review transfer

| Тема | Решение P07 | Где отражено | Источник / provenance |
| --- | --- | --- | --- |
| API-test как свидетельство поведения | Добавлено различение между проверкой выбранных сценариев и доказательством корректности всего намерения. | «Свидетельства поведения и ревью по намерению». | `/spdd-api-test` template; Fowler billing example; A7 evidence theory. |
| Expected/actual/result | Таблица результата описана как артефакт с входом, ожидаемым результатом, фактическим результатом и статусом. | «Свидетельства поведения и ревью по намерению». | `/spdd-api-test` template. |
| Пример с биллингом | Сценарии billing раскрыты как классы проверок без добавления неподтверждённых чисел или HTTP-кодов. | «Свидетельства поведения и ревью по намерению». | Fowler/Thoughtworks SPDD; SPDD dossier inventory. |
| Code-review triage | Ревью теперь разделяет баг реализации, неверное тестовое ожидание, drift, implicit decision, prompt-update, sync, scope rejection and Canvas re-analysis. | «Свидетельства поведения и ревью по намерению». | `/spdd-code-review`; `/spdd-prompt-update`; `/spdd-sync`; A7/C3. |
| Human review boundary | Зафиксировано: свидетельства помогают человеку принять/отклонить/вернуть работу, но не заменяют проверку исходного Canvas. | «Свидетельства поведения и ревью по намерению». | A7/C3; prior P06 failure-mode audit. |


## P08 anti-summary transfer

| Claim audited | Added source-level detail | Main-text location |
| --- | --- | --- |
| “Code review finds drift” | Named the alignment blocks and review surfaces from the `/spdd-code-review` report. | «Свидетельства поведения и ревью по намерению». |
| “Canvas is updated” | Added prompt-update input shape, minimal patch rule, preserve filename, cross-section consistency and no code blocks. | «`prompt-update` и `sync`». |
| “Code and Canvas are synchronized” | Added sync mechanics: implementation comparison, update plan, sensitive sections `Operations`, `Structure`, `Entities`, and minimal trace. | «`prompt-update` и `sync`». |
| “API-test provides evidence” | Kept P07 concrete artifact detail unchanged; no further expansion needed in P08. | «Свидетельства поведения и ревью по намерению». |


## P09 free material expansion 1

| Поле | Запись |
| --- | --- |
| Главный недобор | В статье уже была структура REASONS и billing example, но не было короткого места, где видно, как один исходный запрос раскладывается по `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards` до генерации. Из-за этого Canvas мог читаться как абстрактная форма требований. |
| Что добавлено | Новый подраздел «Как пример с биллингом раскладывается по Canvas». Он показывает, как правила Standard/Premium, `modelId`, prompt/completion tokens, unknown customer, negative tokens, quota and response format расходятся по семи зонам Canvas. |
| Откуда взят материал | Fowler/Thoughtworks billing example; ранее проверенная структура REASONS из Fowler/OpenSPDD; `SPDD_METHOD_DOSSIER.md` and current transfer ledger used as navigation/provenance, not as public citation target. |
| Что осталось долгом | Не добавлены точные числовые тарифы, HTTP-коды, реальные фрагменты generated Canvas или скриншоты. Это лучше делать только в проход визуальных кандидатов и примеров после проверки допустимости изображения или прямого фрагмента источника. |

## P23 companion sync

- Ledger не расширялся новой coverage-матрицей. P23 только снял устаревшие формулировки и зафиксировал, где теперь находятся текущие долги.
- Внешние кандидаты после P21 остаются не в основном тексте, а в очереди `spdd_method_external_image_queue.md`.
- Шаблонный C5/A10-долг снят: конкретной проблемы статьи, требующей отдельной синхронизации с C5/A10, не обнаружено.
- Актуальные blockers перед публикацией: проверка OpenSPDD README/templates, источник-пробел по `/spdd-reverse` при расширении, проверка Codex skills/implicit invocation при детализации доверия и проверка прав/качества внешних ассетов.

## Final verification update

- В соответствии с финальным blueprint три внешних real-image candidates возвращены в основной article file как inline placeholders и продублированы в нижнем разделе `Внешние изображения для asset-pass`.
- Переноса новых фактов в прозу не было: placeholders только фиксируют визуальные решения и будущий asset-pass для уже описанных механизмов — Plan vs REASONS Canvas, `/spdd-code-review` report shape и `/spdd-sync` bidirectional flow.
- Историческая запись P21/P23 о временном externalization сохранена как история редакторского решения; текущий package state отражён в `spdd_method_image_plan.md` и `spdd_method_external_image_queue.md`.
