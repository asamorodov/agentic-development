# spdd_method_source_usage

Статус: P23 sync. Файл фиксирует источники, реально использованные или явно сохранённые как рабочий контекст для текущей версии `work/atlas/articles/spdd_method.md`. Это не coverage-матрица всего досье.

| Источник | Роль в текущей статье | Где использован | Примечание |
| --- | --- | --- | --- |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Главный методологический источник SPDD: промпт как артефакт поставки, REASONS Canvas, рабочий процесс, пример с биллингом, API-свидетельства, `prompt-update`/`sync`, применимость и ограничения. | Введение; `REASONS Canvas как рабочий контракт`; `Как пример с биллингом раскладывается по Canvas`; `Почему Canvas должен сопровождаться`; `Рабочий процесс OpenSPDD`; `Свидетельства поведения и ревью по намерению`; `Где SPDD оправдан`; `Сценарии сбоев`. | Основной публичный источник вместо ссылки на внутреннее досье. |
| [OpenSPDD README](https://github.com/gszhangwei/open-spdd) | Команды, навыки и границы доверия в OpenSPDD: среды, каталоги установки, Codex skills, `allow_implicit_invocation`, модель доверия и переносимость метода. | Введение; `REASONS Canvas как рабочий контракт`; `Команды, навыки и границы доверия`; `Что остаётся открытым`. | Перед публикацией нужна обычная проверка актуальности README. |
| [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) | Различение способности модели и права на решение; граница между repo-level instructions и feature-level Canvas; риск устаревшего Canvas; предупреждение против чрезмерного применения. | `Почему сильной модели всё равно нужны границы намерения`; `Почему Canvas должен сопровождаться`; `Где SPDD оправдан`; `Сценарии сбоев`. | Использовано как источник концептуальных границ, а не как рекламный лозунг. |
| [`/spdd-story` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) | Подготовка бизнес-ввода, `Scope In` / `Scope Out`, ограничение размера будущего Canvas, acceptance criteria. | `Рабочий процесс OpenSPDD`. | Упомянут как необязательная команда. |
| [`/spdd-analysis` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) | Дисциплина целевого чтения проекта: доменные существительные, действия, API-поверхности, ограниченное исследование и сохранение анализа. | `Как Canvas собирает и ограничивает контекст`; `Рабочий процесс OpenSPDD`. | Технический якорь против общей прозы о context engineering. |
| [`/spdd-reasons-canvas` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) | Полное чтение `@file`/`@folder`, отсутствие усечения, готовый к реализации Canvas без заполнителей, сохранение в `spdd/prompt/<file-name>.md`. | `Как Canvas собирает и ограничивает контекст`; `Рабочий процесс OpenSPDD`. | Поддерживает тезис о Canvas как результате дисциплинированного чтения, а не только форме. |
| [`/spdd-generate` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) | Генерация по `Operations`, соблюдение `Norms` и `Safeguards`, отсутствие свободного перепланирования. | `REASONS Canvas как рабочий контракт`; `Рабочий процесс OpenSPDD`. | Поддерживает тезис о реализации фиксированного намерения. |
| [`/spdd-api-test` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) | `scripts/test-api.sh`, `curl`, таблицы `expected`/`actual`, нормальные и ошибочные сценарии, CI-friendly evidence. | `Рабочий процесс OpenSPDD`; `Свидетельства поведения и ревью по намерению`; `Сценарии сбоев`. | Использован как источник технической формы поведенческих свидетельств. |
| [`/spdd-code-review` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md) | Read-only ревью реализации по REASONS, drift, safeguards, scope, implicit decisions. | `Рабочий процесс OpenSPDD`; `Свидетельства поведения и ревью по намерению`; `Сценарии сбоев`. | Поддерживает тезис о semantic diff между Canvas и кодом. |
| [`/spdd-prompt-update` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) | Минимальное обновление Canvas при изменении намерения, без вставки реализации в промпт. | раздел `prompt-update` / `sync`. | Нужен для различения requirement/design → prompt → code. |
| [`/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) | Обратная синхронизация реализации в Canvas: сравнение кода и промпта, update plan, правка `Operations`/`Structure`/`Entities`. | `Рабочий процесс OpenSPDD`; раздел `prompt-update` / `sync`; `Сценарии сбоев`; `Где SPDD заканчивается`. | Нужен для различения code → prompt и для границы сопровождения Canvas. |
| [Intent Formalization](https://ar5iv.labs.arxiv.org/html/2603.17150v1) | Сравнительная рамка: проверка спецификации и отсутствие независимого оракула корректности намерения. | `Место SPDD между свободным промптом и формальной спецификацией`. | Использован осторожно, как фон для статуса SPDD, а не как утверждение о formal methods. |
| [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Отличие `spec-anchored` от `spec-as-source` и соседних SDD-практик. | `Место SPDD между свободным промптом и формальной спецификацией`. | Поддерживает границу SPDD как живого якоря, но не единственного источника всей системы. |
| [WebReactiva SPDD guide](https://www.webreactiva.com/blog/spdd) | Практическое различение `prompt-update`/`sync` и правило поведения/рефакторинга. | раздел `prompt-update` / `sync`. | Вторичный источник; использован только как удобная практическая формулировка. |
| [daily-spdd-spec-planner.md](https://github.com/github/gh-aw/blob/main/.github/workflows/daily-spdd-spec-planner.md) и [github/gh-aw#30864](https://github.com/github/gh-aw/issues/30864) | Пример планового сопровождения спецификаций и результата в виде issue. | `Плановое сопровождение спецификаций`. | Использовано как практический внешний сигнал применения, не как центральная часть метода. |
| `work/theory-writing/fragments/00_spine_map.md` | Внутренний маршрут к общей рамке перехода от намерения к исполнению. | `Связь с общей рамкой SDLC с ИИ-агентами`. | Не является публичным внешним источником. |
| `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md` | Внутренний маршрут к сравнению спецификационных методологий. | `Связь с общей рамкой SDLC с ИИ-агентами`. | Удерживает границу между SPDD и соседними spec-driven подходами. |
| `work/theory-writing/fragments/B1_spdd_contribution_and_limits.md` | Внутренний фрагмент о вкладе SPDD и его границах. | `Связь с общей рамкой SDLC с ИИ-агентами`. | Используется как маршрут к общей теории, не как замена публичным источникам SPDD. |
| `work/theory-writing/fragments/C1_specification_to_pwg.md` | Внутренний маршрут к границе между спецификацией и persistent work graph. | `Связь с общей рамкой SDLC с ИИ-агентами`. | Поддерживает тезис, что Canvas не хранит владельцев, блокировки, handoff и состояние восстановления. |

## P03 source inventory update

P03 did not introduce new external facts beyond sources already listed, but it changed usage emphasis:

- [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) now also supports the distinction between repository-level instruction files and feature-level REASONS Canvas.
- [OpenSPDD README](https://github.com/gszhangwei/open-spdd) now also supports the brief mention of `/spdd-reverse` as an optional path from existing code to Canvas.

Future source-depth passes should open or otherwise verify the primary sources before adding more exact command details, screenshots, template constraints or version-sensitive installation behavior.

## P04 primary source-depth update

Opened primary sources in P04:

| Source | What was verified / transferred | Where used |
| --- | --- | --- |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | REASONS Canvas as seven-part structure; prompt as versioned/reviewable/reusable artifact; workflow rule about fixing prompt when reality diverges; billing walkthrough; API-test and prompt-update/sync details. | Strengthened «REASONS Canvas как рабочий контракт» and «Почему Canvas должен сопровождаться». |
| [OpenSPDD README](https://github.com/gszhangwei/open-spdd) | Plan vs REASONS Canvas contrast; R+E+A / S+O / N+S grouping; supported environments and Codex skills; optional commands including `/spdd-reverse`; current release metadata noted but not used in article. | Strengthened Canvas anatomy and preserved tool-surface section. |
| [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) | Control problem: codebase scanning cannot infer human design trade-offs and negative-space constraints; `CLAUDE.md`/`AGENTS.md` complement Canvas at different granularity; outdated Canvas can become more dangerous than no documentation. | Strengthened Canvas maintainability and warning about misleading Canvas. |

## P05 source-depth update — command mechanics

Opened primary OpenSPDD command templates for the technical mechanics pass:

| Source | What was verified / transferred | Where used |
| --- | --- | --- |
| [`/spdd-story` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) | Full reading of `@` references, no codebase exploration in story phase, INVEST evaluation, Scope In/Out, one–five-day story sizing, business-focused acceptance criteria. | Rewritten «Рабочий процесс OpenSPDD». |
| [`/spdd-analysis` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) | Strategic enrichment: original requirement preserved, concept-driven project exploration, domain nouns/action verbs/API surfaces, one-hop boundary, `spdd/analysis/<file-name>.md`. | Rewritten workflow section and context-ingestion section. |
| [`/spdd-reasons-canvas` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) | Full source consolidation, fully-populated REASONS sections, no placeholders/TODOs, save to `spdd/prompt/<file-name>.md`, ask for confirmation before implementation. | Rewritten workflow section; supports Canvas as maintained file. |
| [`/spdd-generate` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) | Reads entire Canvas, validates Operations sequence, aligns with Structure, follows Norms/Safeguards, does not re-plan or add unspecified features. | Rewritten workflow section; supports Canvas-as-executable-instruction claim. |
| [`/spdd-api-test` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) | `scripts/test-api.sh`, cURL, human-reviewable test overview and expected/actual results, bash+curl only, timeout, exit code for CI. | Rewritten workflow section; supports behavior-evidence explanation. |
| [`/spdd-code-review` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md) | Read-only review against all REASONS zones, Safeguards, scope boundaries, implicit decisions, positive/negative/direction drift, `spdd/review/<file-name>.md`. | Rewritten workflow section and existing review/drift discussion. |
| [`/spdd-prompt-update` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) | Reads the existing prompt, changes only affected sections, preserves filename, validates cross-section consistency, keeps specification/code boundary. | Rewritten workflow section and prompt-update/sync section. |
| [`/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) | Code-to-Canvas sync priorities; Operations highest, Entities/Structure high; compare current implementation and plan prompt updates before applying. | Rewritten workflow section and boundary notes. |
| [OpenSPDD README](https://github.com/gszhangwei/open-spdd) | `/spdd-reverse` listed as beta optional command for reverse-engineering existing code into a Canvas. The v0.4.9 optional-template directory opened in P05 did not expose a `spdd-reverse.md` file, so the article treats this command as README-level evidence only. | Legacy/reverse paragraph in workflow section. |

## P06 source-depth update — limitations and failure modes

| Source | What was verified / transferred | Where used |
| --- | --- | --- |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | SPDD as maintained artifact and closed loop; fix prompt first when reality diverges; prompt-update vs sync for behavior change vs refactor; fitness assessment; functional API testing is auxiliary and core logic needs unit tests. | Rewritten «Где SPDD оправдан» and «Сценарии сбоев». |
| [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) | Capability/control distinction; simple tasks can be lighter; overuse increases cognitive burden; outdated Canvas can become misleading outdated documentation; bidirectional sync remains a hard engineering challenge. | Rewritten fit/cost and failure-mode sections. |
| [`/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) | Sync compares current implementation with Canvas, produces a plan, and updates high-priority detailed sections such as Operations/Structure/Entities. | Failure mode on synchronization cost and degradation audit. |
| `SPDD_METHOD_DOSSIER.md` | Dossier risk map: wrong Canvas, stale Canvas, local patch, cost boundary, hotfix/post-incident signal, human judgment. | Rewritten limitations and created degradation audit. |


## P07 source-depth pass 4 — evidence, review and examples

### Added to main text

| Addition | Source basis | Main-text location |
| --- | --- | --- |
| API-test reframed as behavioral evidence rather than proof: `scripts/test-api.sh`, shell/cURL, test overview, expected/actual/result and exit code. | `/spdd-api-test` template already opened in P05; Fowler/Thoughtworks billing walkthrough already opened in P04/P06. | «Свидетельства поведения и ревью по намерению». |
| Token billing example made more concrete through scenario classes: Standard/Premium, prompt/completion rates, `modelId`, unknown customer, negative tokens, quota and response format. | Fowler/Thoughtworks SPDD; SPDD dossier inventory. | «Свидетельства поведения и ревью по намерению». |
| Evidence distinguished from working observation: artifact + scope + criterion + trace + link to Canvas/promise + reviewer/owner. | `A7_observation_vs_evidence.md`; `C3_pwg_to_evidence.md` as internal theory context. | «Свидетельства поведения и ревью по намерению». |
| Code-review expanded as semantic diff against Canvas: drift types, safeguards, scope, implicit decisions and merge readiness. | `/spdd-code-review` template already opened in P05; SPDD dossier inventory. | «Свидетельства поведения и ревью по намерению». |
| Review triage added: mismatch may require code fix, test expectation fix, prompt-update, sync, scope rejection or Canvas re-analysis. | Fowler/Thoughtworks prompt-update/sync distinction; OpenSPDD command templates; A7/C3 theory context. | «Свидетельства поведения и ревью по намерению». |
| Explicit warning that evidence helps human review but cannot prove the correctness of the original intent. | A7/C3 theory context; prior article argument about absent independent oracle for Canvas. | «Свидетельства поведения и ревью по намерению». |

### Not added / deliberately bounded

- No new external sources were introduced in P07; the pass relied on already-opened primary SPDD/OpenSPDD sources plus the two allowed internal theory fragments.
- The article still does not paste a full generated test table or review report. That is better suited to a later visual/example pass.
- No exact numeric billing rates or HTTP status codes were added because P07 did not require reproducing the full Fowler example and the current article should avoid unsupported invented constants.


## P08 anti-summary check

P08 checked whether the article still contained summary-only claims such as “Canvas is updated”, “review finds drift” or “OpenSPDD supports a workflow” without source-level mechanics.

| Area checked | Result | Main-text change |
| --- | --- | --- |
| Code review detects intent drift | The article had the concept, but the report shape was still thin. | Added concrete `/spdd-code-review` report blocks: `Requirements Alignment`, `Entities Alignment`, `Approach Alignment`, `Structure Alignment`, `Operations Alignment`, `Norms Alignment`, `Safeguards Alignment`, plus drift, implicit decisions and scope boundary. |
| Canvas update via `prompt-update` | The article had the two-lane distinction, but the standalone section could still read like “update the Canvas”. | Added the operational form: prompt path + update instructions, read whole Canvas, identify affected REASONS sections, minimal change, preserve filename, cross-section consistency, no implementation code blocks. |
| Sync from code back to Canvas | The article had the reverse direction, but needed more mechanics in the dedicated section. | Added the sync shape: read current implementation, compare to Canvas, build update plan, update mainly `Operations`, `Structure`, `Entities`, preserve a minimal explainable trace. |
| API-test evidence | Already sufficiently concrete after P07. | No new main-text change; P08 preserved `scripts/test-api.sh`, cURL, overview table, expected/actual/result, timeout and CI exit code. |
| Workflow support | Already sufficiently concrete after P05. | No new main-text change; workflow section retains command sequence, folders and command constraints. |

No new external sources were introduced. P08 relied on `SPDD_METHOD_DOSSIER.md`, the current article, transfer ledger and the two allowed style/provenance rules.


## P09 free material expansion 1 — concrete Canvas example

Main gap selected: the article had a strong description of REASONS sections and a billing example in the evidence section, but it still lacked a compact example of how one feature decomposes across the Canvas before code generation.

| Added material | Source basis | Main-text location |
| --- | --- | --- |
| Новый подраздел «Как пример с биллингом раскладывается по Canvas». | Пример с биллингом из Fowler/Thoughtworks; анатомия REASONS из Fowler/OpenSPDD; уже проверенные детали команд и шаблонов из статьи. | Внутри «REASONS Canvas как рабочий контракт», перед «Почему Canvas должен сопровождаться». |
| Billing mapped across `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards`. | Existing public sources already cited in the article; SPDD dossier used only as navigation/provenance. | Same subsection. |
| Explicit warning that the example is about decision separation, not billing itself. | P09 editorial judgment based on article gap and open question about the billing example. | Closing paragraph of new subsection. |

Boundaries kept: no invented rates, HTTP status codes, package names or exact full Canvas; the section names only scenario classes already present in the Fowler billing example or already used in the article.

## P23 companion sync

- Активная таблица больше не включает источники, которые не представлены в текущем основном тексте. В частности, строка `mgks.dev` снята из активного usage: предупреждения о cargo-cult/окостенении теперь держатся на первичных источниках OpenSPDD и Fowler/Thoughtworks.
- Внешние реальные кандидаты не встроены в статью после P21. Их источники остаются в `spdd_method_external_image_queue.md`, а не в основном тексте.
- В P21–P23 новые факты из внешних источников не добавлялись; правки касались формы статьи и синхронизации companion-файлов.
- Внутренние теоретические фрагменты в текущей статье используются только в разделе «Связь с общей рамкой SDLC с ИИ-агентами» и не превращают статью в coverage-обзор общей теории.

## Final verification update

- Внешние реальные кандидаты снова представлены в package article как inline placeholders и нижний раздел `Внешние изображения для asset-pass`; их authoritative queue находится в `spdd_method_external_image_queue.md`.
- Это не добавило новых внешних фактов: все три candidates опираются на уже учтённые источники OpenSPDD README, `/spdd-code-review`, `/spdd-sync` и design philosophy.
- Перед публикацией placeholders должны быть заменены локальными ассетами после download/rights/quality check или удалены после явного решения по кандидатам.


## Patch: 2026-06-13 local SPDD anchor additions

- Added a focused section on Fowler/Thoughtworks core skills: `Abstraction First`, `Alignment`, and `Iterative Review`.
- Added numeric billing evidence details from the Fowler/Thoughtworks example and `/spdd-api-test` template: `modelId → 400`, `customer → 404`, negative tokens, `100K/90K/30K`, `$0.20`, `10K prompt + 20K completion → $1.50`.
- Expanded `/spdd-reverse` using the current OpenSPDD optional template: scope confirmation, large-scope narrowing, no idealization, no refactoring, codification of existing code as-is.
- Converted three external placeholders into local source-excerpt SVG assets based on OpenSPDD README, `/spdd-code-review`, and `/spdd-sync`.
