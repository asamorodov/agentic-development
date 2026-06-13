# GSD / Open GSD — source transfer ledger

Статус: Final verification / transfer ledger complete for current package. Ledger фиксирует реальные решения переноса фактуры, но не пытается доказать полное покрытие всего досье.

| Перенесённый материал | Источник | Где в статье | Решение P01 |
|---|---|---|---|
| Текущая ориентация `Git. Ship. Done.` и lineage `Get Shit Done` | Open GSD site, Origin Credit, Promise | Вступление | Вставлено коротко; история доверия не развёрнута в отдельный сюжет |
| Различение `gsd-core`, `gsd-pi`, `gsd-browser`, roadmap surfaces | product pages, GitHub, roadmap | Вступление | Вставлено как базовая карта поверхностей |
| `context rot` как деградация длинной сессии | context-engineering.md | “Что ломается без внешнего процесса” | Вставлено как первое давление метода |
| Непроверенная реализация и отделение “код написан” от “фаза завершена” | the-phase-loop.md, Auto Mode | “Что ломается…” | Вставлено как второе давление метода |
| Потеря состояния между сессиями; `STATE.md`; SQLite authority | the-phase-loop.md, Auto Mode, v2 Auto Mode | “Что ломается…” | Вставлено как третье давление метода |
| Центральная петля `Discuss -> (UI design) -> Plan -> Execute -> Verify -> Ship` | the-phase-loop.md | `gsd-core` section, synthetic figure | Вставлено |
| Цепочка `.planning/` и принцип потребителя артефакта | artifact-types.md, учебный пример, architecture | Разделы про process-runtime и артефакты | Вставлено; подчеркнуто, что файл без потребителя инертен |
| Discuss / UI design как перенос решений до планирования | the-phase-loop.md, COMMANDS.md | `gsd-core` section | Вставлено |
| Plan phase, plan waves, `PLAN.md`, plan-checker | the-phase-loop.md, agents files | `gsd-core` section | Вставлено с техническими anchors |
| Nyquist, Plan Drift Guard, statuses `valid/stale/orphaned/dirty/expired` | GSD User Guide | `gsd-core` section | Вставлено как актуальный layer проверки |
| Execute phase, atomic commits, checkpoint, slopsquatting boundary | COMMANDS.md, gsd-executor.md | `gsd-core` section | Вставлено |
| Code review не заменяет verify | User Guide | `gsd-core` section | Вставлено |
| UAT и свидетельства `gsd-browser` | учебный пример, gsd-browser docs | Раздел Verify | Вставлено; `gsd-browser` не смешан с поверхностью GSD core |
| Quick / fast path | context-engineering.md | `gsd-core` section / failures | Вставлено для защиты от over-process |
| Namespace routers, backlog/seeds/threads/workstreams | User Guide | “Поверхность команд выросла…” | Вставлено |
| ingest-docs, graphify, surface | GSD Commands | “Поверхность команд выросла…” | Вставлено |
| `.planning/config.json`, workflow flags, models, security, audit | Configuration | “Политика инструментов…” | Вставлено |
| `agent_skills`, `global_learnings` | Configuration | “Политика инструментов…” | Вставлено как риск переносимого контекста |
| Context budget levels, orchestrator reading discipline | context-budget.md | “Политика инструментов…” | Вставлено |
| `gsd-pi` install and session commands | Getting Started, Commands | `gsd-pi` section | Вставлено |
| Auto mode as SQLite-backed state machine | Auto Mode | `gsd-pi` section | Вставлено |
| Deep planning and requirement authority | Auto Mode, v2 Auto Mode | `gsd-pi` section | Вставлено |
| `ToolsPolicy`, Context Mode, `gsd_exec`, `gsd_resume` | Auto Mode | `gsd-pi` section | Вставлено |
| Git isolation modes and squash merge | Auto Mode, Git Strategy | `gsd-pi` section | Вставлено |
| Single-host SQLite/WAL boundary and reactive execution | Auto Mode | `gsd-pi` section / failure modes | Вставлено |
| Recovery, headless restarts, provider error handling, stuck detection, timeouts | Auto Mode | `gsd-pi` section | Вставлено |
| Verification commands syntax limits | Auto Mode | `gsd-pi` section | Вставлено |
| Headless / Telegram / status panel | Auto Mode, Commands | `gsd-pi` section | Вставлено |
| Boundary: GSD as process-runtime profile, not full PWG | A10/C5 internal theory + GSD facts | “Почему GSD ещё не PWG” | Вставлено как центральная ось статьи |
| Failure modes: ceremony, phase size, autonomy illusion, DB/projection confusion, one host, trust, inert artifacts, surface complexity | Dossier + primary sources | “Типичные сбои…” | Вставлено |

## Материал, сознательно отложенный или вынесенный из статьи

- Подробная командная шпаргалка `gsd-core` и `gsd-pi` остаётся fieldbook/handbook слоем, не основной atlas article.
- Полные сравнения с Spec Kit, SPDD, BMAD, Kiro, Gas Town и PWG не переносятся в эту статью; здесь нужны только границы, достаточные для чтения GSD.
- История trust/governance Open GSD оставлена как короткая provenance note; социальный сюжет не разворачивается без отдельной задачи.
- Freshness/tagged-release verification остаётся публикационным blocker, потому что статья использует текущие docs/source links и часть raw `main`/lineage paths.
- Реальные внешние screenshots/source diagrams после P12 не вставлены: официального rights-safe standalone visual не выбрано. Очередь сохраняется только в companion-файле.

## P02 transfer decisions

| Перенесённый материал | Источник | Где в статье | Решение P02 |
|---|---|---|---|
| Контракт статьи: не учебник, не справочник и не общий обзор; фокус на lifecycle control | P02 worksheet + C5 model | `Контракт статьи` | Вставлено как явный контракт внутри статьи |
| GSD vs PWG: файлы и runtime-состояние помогают восстановлению, но не гарантируют граф зависимостей, владельцев, gates и готовности | P02 worksheet + PWG dossier + A10 | `Границы с соседними статьями атласа`; существующий PWG section | Усилено; повтор считается controlled repetition |
| GSD vs BMAD: runtime/process supervision vs artifact-first SDLC profile | BMAD dossier + BMAD primary links | `Границы с соседними статьями атласа` | Вставлено коротко, без превращения в BMAD article |
| GSD vs Gas Town: project/local runtime vs multi-agent operating environment | Gas Town dossier + Gas Town/Beads primary links | `Границы с соседними статьями атласа` | Вставлено коротко, без пересказа Gas Town roles |
| GSD vs Spec Kit/Kiro/SPDD: runtime loop vs specification workflow / spec surface / structured prompt artifact | Spec Kit/Kiro/SPDD dossiers + primary links | `Границы с соседними статьями атласа` | Вставлено как grouped boundary for specification family |
| Отрицательная граница: не уходить в инвентарь команд или справочник конфигурации | P02 worksheet | `Контракт статьи` | Вставлено; поддерживает последующий degradation audit |

## P03 dossier inventory

Статус: inventory без тотальной coverage matrix. Проверка смотрит не “всё ли перенесено из досье”, а где статье не хватает опор для читательского вопроса.

### Уже перенесено в статью

| Зона досье | Статус переноса | Комментарий |
|---|---|---|
| Общая ориентация Open GSD и поверхности `gsd-core` / `gsd-pi` / `gsd-browser` | Перенесено | Есть во вступлении и контракте статьи |
| Проблемы `context rot`, непроверенной реализации и потери состояния | Перенесено | Составляют opening problem section |
| Базовая петля `gsd-core` | Перенесено | Discuss, UI, Plan, Execute, Verify, Ship раскрыты как lifecycle control |
| `.planning/` и потребление артефактов | Перенесено | Есть схема и объяснение, что файл без потребителя инертен |
| Agent roles `planner` / `plan-checker` / `executor` | Перенесено | Есть как role contract, но без полной таблицы команд |
| Nyquist, Plan Drift Guard, plan status | Перенесено | Использовано для усиления plan-gate layer |
| Code review vs verify | Перенесено | Разведены как разные проверки |
| `gsd-browser` как evidence backend | Перенесено ограниченно | Поставлен рядом с UAT, не смешан с GSD surface |
| Namespaces, backlog/seeds/threads/workstreams, ingest/graphify/surface | Перенесено как side channels | Есть в разделе о выросшей командной поверхности |
| `.planning/config.json`, model routing, `agent_skills`, `global_learnings`, audit/security | Перенесено | Есть в policy section |
| Context budget | Перенесено | Есть как методологическая дисциплина чтения и делегирования |
| `gsd-pi` Auto Mode / SQLite authority / `.gsd` projections | Перенесено | Есть отдельный section and boundary figure |
| `ToolsPolicy`, Context Mode, git isolation, single-host SQLite/WAL, recovery, verification commands, headless/Telegram | Перенесено | Есть в `gsd-pi` section |
| Failure modes | Перенесено | Церемония, размер фазы, автономность, DB/projection, one host, trust, inert artifacts, surface complexity |
| Boundary with PWG/BMAD/Gas Town/Spec family | Перенесено | Усилено в P02 |

### Осталось неперенесённым или перенесено только как debt

| Зона досье | Почему не перенесено в основной текст P03 | Действие для следующих проходов |
|---|---|---|
| Полная командная шпаргалка `gsd-core` | Увела бы статью в reference | Оставить для Handbook; в статье держать только команды, объясняющие lifecycle control |
| Подробная структура `docs/INVENTORY.md` и все counts команд/агентов | Быстро устаревает и не нужна для reader question | Если понадобится, открыть первоисточник в source-depth pass и использовать только как anchor сложности поверхности |
| Issue-driven orchestration | Может усилить хвост lifecycle, но сейчас не является article-critical | P04–P08: решить, нужен ли короткий абзац про переход issue -> roadmap/phase -> close |
| `manager`, `debug`, `surface`, `graphify` низкоуровневая command detail | Сейчас side-channel уже назван | Не расширять без явной функции в статье |
| `checkpoints.md`, `gates.md`, `verification-patterns.md` как raw references | В P01/P02 не открывались как primary sources в этой рабочей среде; досье отмечает source gap | Source-depth pass: открыть, если нужны точные типы gates/checkpoints/verification ladder |
| `artifact-types.md` из lineage path | Использован как consumer-principle; досье само помечает необходимость сверки текущего `open-gsd/gsd-core` path | Перед final: перепроверить current path/tag или ослабить формулировки |
| Release/version facts `gsd-core` / `gsd-pi` | Досье содержит stale/uncertain notes | Перед публикацией нужен отдельный свежий verification pass; не фиксировать версии как факт статьи |
| Codex-specific command syntax `$gsd-*` | Не article-critical; может зависеть от версии | Только Handbook, если статье не понадобится runtime-specific caveat |
| `gsd-pi` MCP server / Cloud MCP Gateway | Сейчас не нужно для central axis | Добавить только если section about external orchestration becomes too thin |
| Multi-repo workspace in `gsd-pi` | Упомянуто неявно через config; не является центральным | P04–P08: возможно добавить один абзац, если статье нужен нюанс “project/local vs multi-repo, но не fleet” |
| Migration/recovery from v1 `.planning` to `.gsd` | Есть failure note про DB/projection, но нет полного механизма migration | Оставить как open question; подробная migration относится к Handbook |
| Telegram/remote commands detail | Есть коротко; не расширять | No action unless supervision section needs concrete remote-control anchor |
| Full origin/trust history | Упомянуто как provenance/trust note | Не разворачивать в article unless governance pass is requested |

### Где статье могут не хватать технические опоры

1. **Issue-driven orchestration.** Сейчас статья объясняет phases, side channels и ship, но не показывает, как внешние issues входят в lifecycle. Это может быть полезным anchor для “GSD не инвентарь команд, а lifecycle control”.
2. **Gate taxonomy.** Статья называет checkpoints, Nyquist and human verify, но не раскрывает типы gate: pre-flight, revision, escalation, abort. Это лучше делать после открытия `gates.md` / `checkpoints.md`.
3. **Verification ladder.** Сейчас verification раскрыта через UAT, code review и browser evidence. Если будущий source-depth pass подтвердит `existence -> substance -> wiring -> behavior`, это может дать более точную структуру.
4. **Текущий статус релизов и версий.** Статья избегает утверждений о версиях, потому что досье предупреждает о неясности релизов. Перед публикацией нужна свежая проверка источников.
5. **Visual anchors.** В статье стоят synthetic figures; external real screenshots and local assets not checked yet.

### Требует открытия первоисточников перед финальным утверждением

- `gsd-core` releases and current stable/pre-release distinction.
- Текущие raw paths в `open-gsd/gsd-core` для `artifact-types.md`, `verification-patterns.md`, `checkpoints.md`, `gates.md`, `planning-config.md`, `git-integration.md`.
- `gsd-pi` current latest release and v2 docs consistency.
- `gsd-browser` docs/product pages for real image candidates and evidence artifact policy.
- Any command examples intended for Codex-specific syntax.

P03 decision: правка основного текста не требуется. В текущей статье достаточно технических anchors для primary contract; оставшиеся gaps — долги source-depth и visual-pass.


## P04 source-depth transfer: фазы как lifecycle control

### Перенесено в основной текст

- Добавлен subsection `Фазы как регуляторы движения`, который читает `User Guide` как рабочую карту переходов, а не как command catalog.
- Зафиксирована тройка P04: что двигает процесс дальше, что его останавливает, где появляется человеческий надзор.
- В таблицу перенесены ключевые переходы: маршрутизация, Discuss/UI, Plan, Execute, Verify/Ship, backlog/seeds/threads/workstreams.
- Подчёркнуто, что `CONTEXT.md`, валидный `PLAN.md`, `SUMMARY.md`, `UAT.md`, evidence и PR являются переходными артефактами, а `NEEDS_REVISION`, missing input, stale/orphaned/dirty/expired status, `CHECKPOINT-NYQUIST.md`, подозрительные зависимости и архитектурные отклонения являются stop-сигналами.
- Human supervision теперь описан не как общий “человек проверяет”, а как набор точек: выбор степени церемонии, решения Discuss, revision/Nyquist input, архитектура/dependency trust, UAT/acceptance, promotion бокового контекста.

### Не перенесено в P04

- Полная issue-driven orchestration по-прежнему не вынесена в основной текст; P04 ограничился общей строкой о side channels и promotion зрелого контекста.
- Полная taxonomy gates/checkpoints не раскрыта; для этого остаётся долг открытия/проверки primary reference sources.
- Verification ladder не добавлена; Verify/Ship раскрыты через UAT/evidence/fix plans без подробной низкоуровневой проверки implementation patterns.

P04 decision: основной текст изменён, потому что до P04 workflow был технически подробным, но недостаточно явно отвечал на вопросы stop/move/human-supervision.


## P05 source-depth transfer: runtime discipline

### Перенесено в основной текст

- Добавлен subsection `Команды и конфигурация как runtime-дисциплина`.
- Архитектура `gsd-core` сведена к слоистой модели: commands -> workflows -> agents -> CLI tools -> `.planning/`.
- Командная поверхность описана как маршрутизация и расширение входных каналов, а не как справочник команд.
- `.planning/config.json` описан как policy surface: Nyquist, code review, human verify, gates, model profiles, skills, parallelization, audit, dangerous git policy and tool gates.
- `ToolsPolicy`, `UnitContextManifest`, Context Mode, git isolation, headless query/recovery and diagnostics описаны как runtime-ограничения, которые исполняются средой, а не только промптом.
- `gsd-browser` закреплён как evidence backend: screenshots/assertions/recordings/traces/HAR/debug bundles/live takeover могут помогать UAT, но сами становятся privacy-sensitive artifacts.
- Добавлена граница для case study: нельзя оценивать успех/провал GSD без настройки config, модели/профиля, git isolation, tool policy, audit, MCP servers, browser evidence and recovery path.

### Не перенесено в P05

- Полный inventory commands/agents/workflows не добавлен; это осталось Handbook/debugging material.
- MCP server / Cloud MCP Gateway не раскрывались, потому что центральный вопрос P05 закрывается без расширения remote-orchestration surface.
- Worktree-path-safety оставлена в уже существующем `gsd_exec`/worktree paragraph; отдельный warning не нужен до structure pass.

P05 decision: основной текст изменён, потому что прежние sections содержали фактуру, но ещё не собирали commands/config/architecture/tool policy/git/browser evidence в один тезис runtime discipline.


## P06 source-depth transfer: persistent files, handoff and recovery

| Категория | Что перенесено в статью | Что оставлено за пределами статьи |
|---|---|---|
| Продолжение процесса | Добавлено: файлы состояния важны только при наличии следующего потребителя процесса | Не перенесён полный формат каждого файла и шаблонов handoff |
| `.planning/` state | `STATE.md`, phase docs, summaries, verification and UAT описаны как поверхности возобновления | Не перенесены все внутренние workflow filenames and examples |
| Handoff | `HANDOFF.json` and `.continue-here.md` описаны как локальные точки продолжения | Не перенесена точная schema, потому что статья не должна стать справочником artifact formats |
| Side context | Backlog, seeds, threads, workstreams, graphs, codebase maps описаны как разные maturity surfaces | Не перенесён полный user-guide inventory of commands |
| `.gsd` and SQLite | Уточнено: SQLite является authority in `gsd-pi`; markdown projections help review/prompts/git but are not state writes | Не перенесены migration recipes and DB repair commands in detail |
| Recovery | Диагностика и recovery commands включены как operator procedure | Не перенесён troubleshooting checklist; это материал Fieldbook, не Concept Atlas |
| PWG boundary | Уточнено: durable state files can feed a PWG but do not by themselves create PWG semantics | Не перенесена полная PWG theory; сохранена controlled repetition |

Решение P06: основной текст изменён, потому что без этого прохода читатель мог бы переоценить `.planning/` and `.gsd` as already being a Persistent Work Graph.


## P07 source-depth transfer: `gsd-pi` runtime contour

| Категория | Что перенесено в статью | Что оставлено за пределами статьи |
|---|---|---|
| SQLite authority | Единица работы начинается из persisted database state, not agent memory | DB schema, table names and migration details not transferred |
| Focused context | Fresh session and focused context framed as context-bloat control | Prompt construction details not expanded |
| Tool policy | `UnitContextManifest` and `ToolsPolicy` linked to lifecycle permissioning | Full policy matrix and glob rules not copied |
| Command execution | `gsd_exec` framed as compressed evidence and stdout/stderr control | Full Context Mode command catalog not copied |
| Verification | `verification_commands`, retries, UAT/verdicts and pause after failure framed as progression control | Full verification syntax and provider-specific behavior not copied |
| Recovery | Provider errors, repeated dispatch patterns, worktree conflicts and doctor/troubleshooting treated as stop/recovery route | Full troubleshooting/recover recipe deferred to Fieldbook |

Решение P07: основной текст изменён, because the article needed one lifecycle-level explanation of `gsd-pi` rather than only separate paragraphs on SQLite, tools, git and verification.


## P08 source-depth transfer: limits and anti-summary

| Limit added or strengthened | Transfer decision | Not transferred |
|---|---|---|
| Phase tutorial without control | Added anti-summary paragraph: phase order without freshness, gates, checkpoints, tool policy and consumption is only an illusion of process | Full tutorial rewrite not added |
| Ceremony heavier than task | Existing ceremony risk retained as first failure mode | No command-by-command quick-mode guide |
| Stale state files | Strengthened stale/inert artifact risk with stale `PLAN.md` and freshness consumption | Full stale-plan repair recipe deferred |
| Supervised autonomy illusion | Existing autonomy paragraph retained; P08 confirms it as core limit | No expanded provider-error matrix |
| No full graph state | Added explicit boundary: graph-like surfaces do not equal full durable work graph | No PWG theory expansion |
| DB/projection confusion | Existing boundary retained and tied to commands/migration | No migration checklist |

Решение P08: основной текст changed to prevent readers from turning GSD into a slogan or product summary.


## P09 free expansion transfer: issue-driven ingress

| Editorial judgment | Added | Left out |
|---|---|---|
| Main underdeveloped fact | External issues were present only as a word in `graphify`; article did not explain how tracker items enter GSD without becoming automatic scope | Full issue workflow recipe, exact file examples and command catalog |
| `gsd-core` issue ingress | Import to `.planning/issues/`, classification as `feature`/`bug`/`enhancement`/`documentation`/`technical-debt`/`research`/`question`/`invalid`, human confirmation before phase inclusion | Full issue schema and GitHub API details |
| Ship boundary | GSD can bind phase work to issue metadata and close issue after ship | PR automation details not expanded |
| `gsd-pi` GitHub sync | Mappings to Issues/PRs/Milestones stored in `.gsd/.github-sync.json`; rate-limit skip framed as integration caution | Multi-repo and auto-PR config deferred |
| Theory boundary | Tracker is mirror/channel, not authority for internal runtime state | No new comparison with project-management tools |

Решение P09: основной текст changed because issue ingress is a source-specific lifecycle mechanism, not just another command surface.


## P10 free expansion transfer: end-to-end reader path

| Editorial judgment | Added | Left out |
|---|---|---|
| Main underdeveloped coherence | Details were technically rich but not yet tied into a single change lifecycle | Full case study with real repository, screenshots or actual issue data |
| Example path | Synthetic but source-supported path: issue candidate -> classification/review -> Discuss -> Plan -> plan-checker -> Execute -> Verify/UAT/browser evidence -> Ship/close -> lifecycle repair | No invented product details, filenames or UI screenshots |
| Boundary reinforced | Ticket/issue, `PLAN.md`, commit and PR are not automatically true/safe/ready/accepted | No general project-management comparison |
| Theory return | Example ends by naming the changing question at each transition | No full A10 matrix added |

Решение P10: основной текст changed because a concept-first article needs a reader path, not only source density.


## P11 visual transfer: local assets

| Asset | Transfer decision | Rationale |
|---|---|---|
| `openai-codex-chrome-devtools-validation.webp` | Inserted as `fig-gsd-browser-evidence-analogy` | Supports browser/evidence surface: UI action, before/after snapshots, runtime events and repeated validation are close to the `gsd-browser` evidence claim |
| `openai-codex-dashboard-workflow.webp` | Not inserted | It shows a generic Codex task dashboard, not a GSD-specific phase/state/verification surface; inline use would blur method boundary |
| `fowler-harness-continuous-feedback.png` | Not inserted | It belongs to harness engineering/continuous feedback theory; useful background but not a priority real docs/screenshot for GSD |

Решение P11: inserted one relevant local asset and recorded explicit rejection/defer decisions for the other local assets.

## P12 transfer ledger: external real images

| Candidate family | Decision | Reason |
|---|---|---|
| `gsd-core` product/workflow visuals | not_transferred | Official/product/doc surfaces checked during P12 did not expose a distinct external screenshot or source diagram suitable for inline placeholder use. |
| `gsd-pi` status/report/headless visuals | not_transferred | The article already explains the runtime contour with text and synthetic state-boundary figure; no real image asset was found. |
| `gsd-browser` proof visuals | not_transferred_as_external_real_image | The article keeps the P11 local Codex analogy; official GSD-browser pages describe evidence artifacts but no standalone real visual was inserted. |
| Roadmap/ecosystem visuals | not_transferred | Roadmap was kept as source text; no rights-safe standalone graphic was selected. |

No article claim was added from visual search alone. P12 only changed the asset disposition record and preserved the rule that missing screenshots must not be replaced by synthetic diagrams merely to satisfy a visual pass.

## P13 transfer ledger: synthetic figures

| Candidate | Decision | Reason |
|---|---|---|
| `fig-gsd-issue-to-ship-reader-path` | deferred | Useful but overlaps with the prose example and `fig-gsd-artifact-consumption`; not unusually necessary. |
| `fig-gsd-runtime-discipline-stack` | deferred | Runtime discipline is already expressed in a table and in `fig-gsd-process-runtime-profile`. |
| `fig-gsd-failure-modes` | deferred | Would be a risk matrix rather than a mechanism diagram; current failure section is clearer in prose. |
| `fig-gsd-continuation-recovery-boundary` | deferred | Potentially useful for a fieldbook, but the article already has state and artifact-boundary figures. |

P13's transfer decision is conservative: no new synthetic figure was inserted.

## P14 transfer ledger: standalone concept framing

| Added / changed | Transferred into main article | Kept out |
|---|---|---|
| Local theory minimum | Added five reader anchors: intent, working state, authority, evidence and lifecycle repair, each mapped to GSD surfaces. | Full A/B/C theory path, general SDLC synthesis and abstract definitions not specific to GSD. |
| Concept-first article model | Converted into a short local subsection rather than meta-commentary about the atlas. | C5 registry language, article-status rows and broad list of other future articles. |
| GSD dossier orientation | Used to confirm source-specific examples: `.planning/`, `.gsd`, SQLite, roles, checkpoints, UAT and repair. | Dossier prose and internal pass history not cited in public text. |

P14 decision: repeat just enough theory for a standalone GSD article, but ground every repeated term in a GSD surface.

## P15 transfer ledger: mechanism/failure boundary

| Reinforced concern | What moved into article | What stayed out |
|---|---|---|
| Phase workflow becoming tutorial | Added rule: phase transition requires input, consumer and stop condition. | Full command walkthrough. |
| Persistent files not usable work state | Added explicit warning that files without freshness checks and next consumers are an archive. | Detailed artifact lifecycle recipes. |
| Hidden supervision | Added warning that automation without stop/pause/recover/takeover boundaries hides human risk. | Full operator guide for auto mode. |
| Weak verification | Added existence/substance/wiring/behavior boundary. | Stub-pattern checklists and framework-specific examples. |
| GSD imitating PWG | Added graph-state test: nodes/deps/owners/blockers/readiness/evidence must be explicit. | Full PWG theory and Beads-style graph design. |
| Ceremony exceeds task risk | Added rule that small tasks should use quick/fast or no GSD. | Decision matrix / Handbook selection recipe. |

P15 kept failure modes inside the concept mechanism rather than adding a separate error catalogue.

## P16 transfer ledger: semantic back-links

| Theory fragment | Transferred into companion semantics | Not transferred into main article |
|---|---|---|
| `00_spine_map` | One-change lifecycle mapping. | Full terminology contract and spine figure. |
| `A3` | Specification/process boundary. | Detailed comparison of SPDD, Spec Kit, Kiro, TDAD and Constitutional SDD. |
| `A5` | Process-as-artifact test. | General theory of process methodologies and all examples. |
| `A7` | Observation/evidence semantic link. | Full evidence taxonomy. |
| `A9` | Post-ship repair semantic link. | General lifecycle-repair chapter. |
| `A10` | Mode-selection semantic link. | Full decision map or stress tests. |
| `C5` | Concept-first atlas back-link rule. | Registry and writing-process discussion. |

P16 deliberately avoided main-text expansion because adding all theory links inline would make the article less standalone and more like a theory index.


## P17 language transfer ledger

| Область | Решение P17 | Причина |
|---|---|---|
| Обычная связка в основном тексте | Переведена на русский: `checkpoint`, `recovery`, `verdict`, `side-channel`, `tool gates`, `debug bundles`, `package legitimacy gates`, `masked keys`, `audit controls` получили русские формы или русские пояснения. | Пользовательский текст не должен выглядеть как смесь русского изложения и английского черновика. |
| Точные имена | Сохранены: команды, пути, файлы, конфигурационные ключи, source labels, статусы и product names. | Эти элементы являются адресуемыми сущностями источников и должны оставаться проверяемыми. |
| Аргумент статьи | Не изменён. | P17 был языковым проходом, а не фактическим или структурным расширением. |
| Риск повреждения ссылок | Проверен вручную после правок. | Предыдущие широкие замены могли повредить `/gsd-workflow`, `workflow.*` или `workflow-map.md`; P17 закрепил точные формы. |

## P18 language transfer ledger

| Область | Решение P18 | Причина |
|---|---|---|
| Заголовки и подписи | Переформулированы без внутреннего pass-жаргона и тяжёлых калькированных оборотов. | Основная статья должна читаться как пользовательский материал, а не как журнал редакционных проходов. |
| Таблицы | Уточнены русские формулировки для `thread`, `workstream`, PWG-границ, браузерных свидетельств и единицы работы. | Таблицы должны объяснять действие, а не выглядеть как глоссарий source labels. |
| Нижний asset-раздел | Убрана ссылка на `P12` из основного текста; статус внешних изображений описан человечески. | Внутренние pass labels уместны в companions, но не в пользовательском тексте статьи. |
| Термины | `process-runtime profile` закреплён как `профиль работы в среде выполнения`; `prompt` в обычном объяснении заменён на `запрос`. | Это сохраняет смысл и уменьшает случайную английскую связку. |

## P19 editorial transfer ledger

| Найденная проблема | Исправление | Почему это важно |
|---|---|---|
| Основная статья заканчивалась служебным разделом про будущий проход по ассетам. | Раздел удалён из `gsd_open_gsd.md`; статус внешних изображений остаётся в `image_plan` и `external_image_queue`. | Standalone concept-first article должна заканчиваться концептуальным выводом, а не редакционным backlog. |
| Финальный акцент мог смещаться с GSD как метода на процесс подготовки статьи. | Финалом снова стал раздел `Как читать GSD в атласе`. | Читатель выходит из текста с границей GSD/PWG/Spec/ADR, а не с внутренней заметкой о картинках. |
| Риск потери визуального решения при удалении раздела. | Companion-файлы синхронизированы: решение по внешним изображениям сохранено вне основного текста. | Фактура asset-pass не потеряна, но больше не мешает чтению статьи. |

## P20 editorial transfer ledger

| Найденная проблема | Исправление | Почему это важно |
|---|---|---|
| Вступительный раздел назывался `Контракт статьи` и звучал как редакционный бриф. | Заголовок заменён на `Что важно удержать`, а первые абзацы переформулированы как рабочая модель чтения GSD. | Сильная standalone article должна сразу помогать читателю понять метод, а не объяснять процесс написания статьи. |
| Раздел слишком явно говорил о `результатах успешного чтения`. | Формулировка заменена на четыре практических вещи, которые должны быть видны после чтения. | Тон стал ближе к инженерному объяснению. |
| Негативная граница была названа слишком абстрактно. | Она раскрыта как практические границы: не справочник команд, не набор `.planning/`-файлов, не универсальная замена соседним режимам. | Граница статьи стала понятнее без потери фактуры. |

## P21 editorial transfer ledger

| Найденная проблема | Исправление | Почему это важно |
|---|---|---|
| `Минимум рамки` и `местные различения` звучали как внутренний теоретический жаргон. | Раздел переименован в `Пять опор для чтения GSD`, таблица теперь говорит о `рабочих опорах`. | Standalone reader получает понятные ориентиры без знания внутренней терминологии атласа. |
| Таблица могла выглядеть как theory-card. | Формулировки оставлены техническими, но заголовки стали ближе к читательскому вопросу. | Concept-first article должна объяснять понятия через рабочую практику. |

## P22 transfer ledger: entry-sequence structure

| Structural issue | What moved into the public sequence | What stayed out |
|---|---|---|
| Entry began too much like taxonomy and atlas boundary | Existing failure section `Что ломается без внешнего процесса` moved directly after the opening/object paragraphs. | No new problem taxonomy, no tutorial preface, no command catalogue. |
| Reader question needed earlier concrete stakes | `context rot`, premature “done”, and lost state now appear before the local reading frame. | Full source inventory and pass history remain outside the main article. |
| Bottom asset-pass backlog risk | Public article still omits the internal external-image backlog section. | External-image queue remains in companion files only until a real asset is selected and localized. |

P22 changed ordering, not source substance: the same primary links support the same paragraphs after relocation.

## P23 transfer ledger sync

| Area | P23 decision |
|---|---|
| Old pass debts | Removed from open questions or consolidated into current publication blockers. |
| Source coverage | Kept as transfer history only where it explains why facts entered or stayed out of the article. |
| Ledger scope | No new coverage bureaucracy added: current remaining issues are freshness, lineage paths and future article links, not missing core article content. |
| Visual backlog | Kept out of the public article and preserved in image companions. |

## P24 transfer ledger: style-only audit

| Style defect | Public-text decision | Source/fact effect |
|---|---|---|
| Pass-facing/public-surface wording in opening | Rewritten as direct public-site / product-surface language. | No source change. |
| Pseudo-terms and calques | Replaced `анти-резюме`, `процессная машина`, `исполняемая дисциплина`, `coverage решений` with ordinary Russian technical phrasing. | No source change. |
| Internal theory term in reader frame | Public text now says `Обновление после поставки` instead of foregrounding `Ремонт жизненного цикла`. | Same lifecycle-repair idea; term bridge noted in theory links. |
| Headings | `Негативный тест механизма`, `Как фазы разрешают следующий шаг`, and command-surface heading rewritten for natural Russian. | No structural/factual change. |

## P25 transfer ledger: selective natural rewrite

| Area | Rewrite decision | Source/fact effect |
|---|---|---|
| Boundary paragraphs | Removed remaining calques such as `шкала операционной среды`, `идут от спецификационной стороны`, and artifact-anchor phrasing. | Same boundary facts and citations retained. |
| Runtime/process language | Replaced abstract `поверхности`, `контуры`, and `дисциплина` where they hid ordinary meaning. | No mechanism change. |
| Command and state sections | Kept concrete command names and file paths; only surrounding Russian prose changed. | No source change. |
| Reader example | Made issue-to-ship phrasing more natural without changing sequence or claims. | Same sources retained. |

## P26 transfer ledger: guarded final style

| Area | Final style decision | Source/fact effect |
|---|---|---|
| Opening product map | Rephrased as products/modes rather than abstract surfaces. | Same `gsd-core` / `gsd-pi` / `gsd-browser` distinction. |
| Runtime profile section | Smoothed transitions and removed remaining awkward English-derived phrasing. | Same five-layer mechanism. |
| `gsd-pi` section | Marked source-specific English labels with code styling where needed and translated ordinary shell/testing wording. | Same command syntax and numeric limits preserved. |
| PWG boundary | Rephrased recovery semantics and dispatch terms without changing the boundary claim. | Same GSD/PWG distinction. |

## Final verification transfer note

Пакет не содержит generic `relevant but untransferred` hard blocker. Оставшиеся долги конкретны: freshness/release verification, lineage/reference paths, external real image policy, image path assembly and future neighbor links. Финальная правка `ремонт жизненного цикла` -> обновление долговечных артефактов после поставки не изменила transfer decisions.
