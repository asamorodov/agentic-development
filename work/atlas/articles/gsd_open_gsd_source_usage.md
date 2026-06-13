# GSD / Open GSD — source usage

Статус: Final verification / source companion complete for current package. Внешние факты в статье ссылаются на первичные или публично читаемые источники, указанные в досье. Внутреннее досье использовано как quarry-материал и не является citation target в статье.

| Источник | Роль в статье | Где использован | Статус |
|---|---|---|---|
| https://www.opengsd.net/ | Общая позиция Open GSD, текущая формула `Git. Ship. Done.` | Вступление, ориентация | Использован |
| https://opengsd.net/origin | Origin Credit, lineage старого GSD | Вступление, open questions | Использован ограниченно |
| https://opengsd.net/promise | Рамка доверия и прозрачности | Вступление, риски доверия | Использован ограниченно |
| https://opengsd.net/products/gsd-core | Продуктовая поверхность `gsd-core`, поддерживаемые среды выполнения | Ориентация | Использован |
| https://github.com/open-gsd/gsd-core | README / общий контекст `gsd-core` | Инициализация существующего репозитория, релизные оговорки | Использован ограниченно |
| https://github.com/open-gsd/gsd-core/releases | Релизные оговорки и необходимость проверки версий | Failure modes | Использован как caution |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md | `context rot`, быстрые пути, субагенты со свежим контекстом | Проблема, quick/fast, размер процесса | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | Центральная петля `Discuss -> Plan -> Execute -> Verify -> Ship`, перенос состояния | Фазовый процесс, Discuss, Plan, Execute, Verify | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md | Конкретные файлы первого проекта, UAT-пример | Старт `gsd-core`, Verify | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md | Команды, ship, slopcheck, checkpoints | `gsd-core` команды, execute, ship | Использован |
| https://www.opengsd.net/docs/v1/commands | Актуальная web-справка команд, ingest/graphify/surface, heartbeat | Маршрутизация и боковые поверхности | Использован |
| https://opengsd.net/docs/v1/configuration | `.planning/config.json`, модели, безопасность, аудит, tools policy | Политика инструментов, моделей и безопасности | Использован |
| https://www.opengsd.net/docs/v1/user-guide | Namespaces, Nyquist, Plan Drift Guard, code review, backlog/seeds/threads/workstreams | Плановая проверка, маршрутизация, side channels | Использован |
| https://www.opengsd.net/docs/v1/architecture | Слои `gsd-core`, `.planning/`, waves, drift gate | Механизм, артефакты, архитектурная трактовка | Использован через фактуру досье и ссылки в тексте ограниченно |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md | Контракт планировщика | Планирование, размер задач | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md | Контракт plan-checker, verdicts | Revision gate | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md | Контракт executor, checkpoints, autonomy boundary, stuck signal | Execute и ограничения автономии | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md | Контекстный бюджет, уровни деградации, MCP-schema cost | Политика контекста | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md | Профили моделей, `inherit`, `omit` | Маршрутизация моделей | Использован |
| https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md | Жизненный цикл и потребители артефактов | Артефакты и consumption figure | Использован с оговоркой lineage |
| https://github.com/open-gsd/gsd-pi | README / базовая поверхность `gsd-pi` | Ориентация, базовые команды | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/getting-started.md | Установка и требования `gsd-pi` | `gsd-pi` section | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md | Auto mode, SQLite, ToolsPolicy, Context Mode, git isolation, recovery, verification, supervision | Основной раздел `gsd-pi` | Использован |
| https://www.opengsd.net/docs/v2/auto-mode | Актуальная v2 граница требований и state authority | Deep planning / database authority | Использован |
| https://www.opengsd.net/docs/v2/commands | Commands, headless, MCP server, rebuild, reports | `gsd-pi` commands, troubleshooting, DB/projection risk | Использован |
| https://www.opengsd.net/docs/v2/configuration | Preferences, MCP config, workspace, hooks, skills, `.gsd/RUNTIME.md` | Политика `gsd-pi` | Использован |
| https://www.opengsd.net/docs/v2/troubleshooting | Diagnostics and recovery surfaces | Failure modes | Использован ограниченно |
| https://www.opengsd.net/docs/v2/migration | Migration/recovery boundary | DB vs markdown risk | Использован |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md | `none` / `worktree` / `branch`, squash merge, trailers | Git isolation | Использован |
| https://opengsd.net/roadmap | Поверхности Open GSD и статус `gsd-browser` | Ориентация, boundaries | Использован |
| https://opengsd.net/products/gsd-browser | Сопутствующий продукт browser proof | Ориентация / verification | Использован |
| https://opengsd.net/docs/v5/commands | Browser screenshots, assertions, traces, HAR, takeover | Verify / evidence | Использован |
| work/theory-writing/fragments/C5_theory_to_technical_atlas.md | Контракт самостоятельной статьи атласа и controlled repetition | Структура статьи и theory return | Внутренний источник, не публичная citation target |
| work/theory-writing/fragments/C5_concept_atlas_article_map.md | Место GSD в concept-first atlas | Theory links / boundaries | Внутренний источник, не публичная citation target |
| work/theory-writing/fragments/A10_mode_selection_map.md | Граница process profile vs PWG, режим выбора внешней структуры | Раздел “Почему GSD ещё не PWG” | Внутренний источник, не публичная citation target |

## P02 boundary sources

| Источник | Роль в P02 | Где использован | Статус |
|---|---|---|---|
| work/dossiers/BMAD_METHOD_DOSSIER.md | Внутренний quarry-материал для границы GSD/BMAD | Контракт статьи, boundary section | Внутренний источник; public citation targets взяты из BMAD primary links |
| https://github.com/bmad-code-org/BMAD-METHOD | Primary source BMAD | Boundary GSD/BMAD | Использован |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md | BMAD workflow map / document accumulation | Boundary GSD/BMAD | Использован |
| work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md | Внутренний quarry-материал для границы GSD/PWG | Контракт и раздел “Почему GSD ещё не PWG” | Внутренний источник; не public citation target |
| work/dossiers/GAS_TOWN_METHOD_DOSSIER.md | Внутренний quarry-материал для границы GSD/Gas Town | Контракт статьи, boundary section | Внутренний источник; public citation targets взяты из Gas Town/Beads links |
| https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | Gas Town framing as multi-agent operating environment | Boundary GSD/Gas Town | Использован |
| https://github.com/gastownhall/gastown | Gas Town README / workflows | Boundary GSD/Gas Town | Использован |
| https://gastownhall.github.io/beads/ | Beads docs as PWG/data plane anchor | Boundary GSD/Gas Town | Использован |
| work/dossiers/SPEC_KIT_METHOD_DOSSIER.md | Внутренний quarry-материал для границы GSD/Spec Kit | Boundary GSD/Spec Kit | Внутренний источник; public citation target — GitHub Spec Kit |
| https://github.com/github/spec-kit | Primary source Spec Kit | Boundary GSD/Spec Kit | Использован |
| work/dossiers/KIRO_SPECS_DOSSIER.md | Внутренний quarry-материал для границы GSD/Kiro | Boundary GSD/Kiro | Внутренний источник; public citation target — Kiro Specs docs |
| https://kiro.dev/docs/specs/ | Primary source Kiro Specs | Boundary GSD/Kiro | Использован |
| work/dossiers/SPDD_METHOD_DOSSIER.md | Внутренний quarry-материал для границы GSD/SPDD | Boundary GSD/SPDD | Внутренний источник; public citation target — Fowler SPDD |
| https://martinfowler.com/articles/structured-prompt-driven/ | Primary source SPDD | Boundary GSD/SPDD | Использован |

## P03 dossier inventory source status

| Источник / группа источников | Решение inventory | Нужен позже? |
|---|---|---|
| `GSD_METHOD_DOSSIER.md` — верхнеуровневый синтез | Уже достаточно перенесён в article structure | Продолжать использовать как quarry, не как public citation target |
| `gsd-core`: фазовая петля, инженерия контекста, команды, руководство пользователя, конфигурация | Основные anchors статьи уже использованы | Да, source-depth pass может уточнить детали |
| `gsd-core`: исходные reference-файлы checkpoints/gates/verification/artifact/model profiles | Частично использованы через досье; остаётся неопределённость текущих путей | Да, если P04–P08 расширят gate/verification sections |
| `gsd-core` releases | В статье не фиксируются версии | Да, перед публикацией нужна свежая проверка |
| `gsd-pi` Auto Mode / Commands / Configuration / Migration / Troubleshooting | Основные runtime-опоры уже использованы | Да, для проверки согласованности и решения, нужны ли MCP/headless детали |
| `gsd-browser` product/docs | Использован только как evidence backend | Да, P12 visual/evidence pass |
| Origin / Promise | Использован кратко как provenance/trust note | Возможно; не расширять без отдельной причины |


## P04 source-depth: руководство пользователя как lifecycle control

| Источник | Что уточнено в P04 | Где использовано |
|---|---|---|
| https://www.opengsd.net/docs/v1/user-guide | Руководство пользователя перенесено не как список команд, а как карта переходов: маршрутизация, Nyquist, дрейф плана, code review, backlog/seeds/threads/workstreams | Новый subsection `Фазы как регуляторы движения`; также поддерживает раздел о маршрутизации поверхности команд |
| https://opengsd.net/docs/v1/configuration | Надзор и остановки связаны с режимами workflow, human verify, safety/tool policy and gates | Новый subsection и раздел политики инструментов |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | Центральная фазовая петля использована как основа для “что двигает дальше” | Новый subsection и существующий `gsd-core` section |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md | Revision gate и недостающий ввод оформлены как остановка до исполнения | Новый subsection и Plan section |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md | Checkpoint, package legitimacy и архитектурные отклонения оформлены как точки человеческого решения | Новый subsection и Execute section |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md | UAT и пользовательская проверка использованы как переход Verify -> Ship | Новый subsection и Verify section |

P04 не добавлял новые внешние источники; он переставил уже перенесённую фактуру в lifecycle-control матрицу.


## P05 source-depth: commands/config/architecture as runtime discipline

| Источник | Что уточнено в P05 | Где использовано |
|---|---|---|
| https://www.opengsd.net/docs/v1/architecture | Архитектура `gsd-core` перенесена как слои: commands, workflows, agents, CLI tools, `.planning/` | Новый subsection `Команды и конфигурация как runtime-дисциплина` |
| https://www.opengsd.net/docs/v1/commands | Команды перенесены как маршрутизация и расширение входных каналов, а не как command catalog | Новый subsection; уже существующие разделы о routing/ingest/graphify/surface |
| https://www.opengsd.net/docs/v1/configuration | `config.json` описан как policy surface: workflow toggles, models, skills, gates, audit, safety, tools, git strategy | Новый subsection и раздел политики |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md | `ToolsPolicy`, dispatch, Context Mode, recovery, local runtime supervision | Новый subsection и `gsd-pi` section |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md | Git isolation `none` / `worktree` / `branch`, squash merge and task trailers | Новый subsection и `gsd-pi` git paragraph |
| https://opengsd.net/docs/v5/commands | Browser evidence как сопутствующий слой проверки и privacy-sensitive artifact class | Новый subsection и Verify/evidence paragraphs |

P05 не добавлял новые source URLs сверх уже учтённых; он сгруппировал команды, конфигурацию, architecture, tool policy, git isolation и browser evidence в единую рамку runtime discipline.


## P06 source-depth: state, handoff and recovery

| Источник | Что уточнено в P06 | Где использовано |
|---|---|---|
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | `STATE.md`, фазовые файлы и потребление состояния следующим шагом | Новый subsection `Продолжение и восстановление: что дают файлы состояния` |
| https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md | `HANDOFF.json`, `.continue-here.md`, producer/consumer-грань артефактов | Новый subsection; figure `fig-gsd-artifact-consumption` |
| https://www.opengsd.net/docs/v1/architecture | `.planning/`, codebase maps, workflow files as process surfaces | Новый subsection и существующие sections про `gsd-core` |
| https://www.opengsd.net/docs/v1/user-guide | Backlog, seeds, threads, workstreams as immature/long-lived context surfaces | Новый subsection и lifecycle-control section |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md | SQLite authority, paused sessions, recovery briefing, dispatch state | Новый subsection и `gsd-pi` recovery paragraphs |
| https://www.opengsd.net/docs/v2/commands | `/gsd doctor`, `/gsd inspect`, `/gsd forensics`, headless query, rebuild/report surfaces | Новый subsection and failure/recovery boundary |
| https://www.opengsd.net/docs/v2/migration | DB vs markdown projection boundary and recovery caution | Новый subsection and `.gsd` vs PWG boundary |

P06 не добавлял новые source families; он углубил уже перенесённый материал о persistent state and recovery.


## P07 source-depth: `gsd-pi` runtime/state/verification contour

| Источник | Что уточнено в P07 | Где использовано |
|---|---|---|
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md | Lifecycle одной единицы: SQLite state, focused session, UnitContextManifest, ToolsPolicy, `gsd_exec`, verification, pause/recovery | Новый subsection `Единица работы как контур среды выполнения` |
| https://www.opengsd.net/docs/v2/commands | Headless query/dispatch/status and operator visibility as state-reading surfaces | Новый subsection and existing operator-control paragraph |
| https://www.opengsd.net/docs/v2/troubleshooting | `/gsd doctor`, state/worktree health and recovery-first diagnosis | Новый subsection and recovery boundary |
| https://www.opengsd.net/docs/v2/migration | DB/projection boundary and explicit recover risk | Existing P06/P07 state boundary; not expanded into recipe |

P07 intentionally treated `gsd-pi` components as lifecycle functions, not as a feature list.


## P08 source-depth: failure modes and anti-summary limits

| Источник | Что уточнено в P08 | Где использовано |
|---|---|---|
| https://www.opengsd.net/docs/v1/user-guide | Phase workflow without freshness/checks is insufficient; plan status and lifecycle gates matter | `Типичные сбои и чрезмерное применение` intro and stale artifacts risk |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md | Revision gate as actual control rather than tutorial step | Anti-summary paragraph |
| https://www.opengsd.net/docs/v1/configuration | Tool policy, gates, human verification and safety settings as controls | Anti-summary and autonomy/ceremony limits |
| https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md | Artifacts need consumers; stale/inert files are failure mode | Stale artifacts risk |
| https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md | Local SQLite/WAL boundary and supervised autonomy limits | One-host risk and autonomy risk |
| https://www.opengsd.net/docs/v2/commands | `rebuild markdown` / `rebuild database`, diagnostics and state-reading surfaces | DB/projection risk and process diagnostics |
| https://www.opengsd.net/docs/v2/migration | Explicit recovery risk: markdown projection vs DB authority | DB/projection risk |

P08 strengthened limits without adding a new source family.


## P09 free expansion: issue-driven ingress and GitHub sync boundary

| Источник | Что добавлено в P09 | Где использовано |
|---|---|---|
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md | GitHub issue ingress, classification, human review, conversion into phase/roadmap work, close after ship | New paragraphs after ingest/graphify/surface discussion |
| https://www.opengsd.net/docs/v2/configuration | `gsd-pi` GitHub sync: mapping milestones/slices/tasks to Issues/PRs/Milestones, `.gsd/.github-sync.json`, rate-limit skip | New paragraph on external tracker as mirror/channel, not runtime authority |

P09 selected issue-driven ingress as the main underdeveloped fact because previous text mentioned issues inside `graphify` but did not explain how external work enters the lifecycle.


## P10 free expansion: reader path through an issue-to-ship example

| Источник | Что добавлено в P10 | Где использовано |
|---|---|---|
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md | Incoming issue as candidate work, classification, human scope confirmation, issue close after ship | New subsection `Сквозной пример: от входящего issue до поставки` |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | Discuss/Plan/Execute/Verify/Ship progression as reader path | New example subsection |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md | Plan revision when missing requirements, error paths, dependencies or verification | New example subsection |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md | Checkpoint on architecture/package substitution and bounded execution | New example subsection |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md | UAT/ship/state update as final lifecycle movement | New example subsection |
| https://opengsd.net/docs/v5/commands | Browser evidence as possible UI/UAT support | New example subsection |

P10 chose coherence as the main deficit: the article had enough mechanisms but needed an end-to-end reader path.


## P11 local visual asset usage

| Local asset | Source / provenance in catalog | Decision | Where used |
|---|---|---|---|
| `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | OpenAI Codex materials, tracked in local asset catalog | inserted_inline_local_image_asset | `fig-gsd-browser-evidence-analogy`, near Verify/`gsd-browser` evidence paragraph |
| `content/assets/theory-images/openai-codex-dashboard-workflow.webp` | OpenAI Codex materials, tracked in local asset catalog | not_inserted | See image plan: too broad/dashboard-oriented for GSD-specific process argument |
| `content/assets/theory-images/fowler-harness-continuous-feedback.png` | Fowler harness engineering article, tracked in local asset catalog | not_inserted | See image plan: useful for broader harness/feedback theory, but would pull GSD article toward harness engineering |

P11 added one local image and treated it explicitly as an analogy, not as a GSD screenshot.

## P12 external visual source check

| Источник / направление | Visual decision | Где отражено |
|---|---|---|
| `https://opengsd.net/products/gsd-core` | Проверен как внешний visual-candidate source: продуктовая страница полезна как текстовый источник, но не дала отдельного standalone screenshot/diagram для inline `external-real-candidate`. | External image queue / image plan; основной текст не получил новую картинку. |
| `https://www.opengsd.net/docs/v1/user-guide` | Workflow descriptions and text/ASCII-like documentation were treated as source text, not as real image assets. | Image plan P12 disposition. |
| `https://www.opengsd.net/docs/v2/commands` and `https://www.opengsd.net/docs/v2/auto-mode` | Проверены для `gsd-pi` status/report/headless visual; no rights-safe standalone UI image selected. | External image queue. |
| `https://opengsd.net/products/gsd-browser` and `https://opengsd.net/docs/v5/commands` | Browser evidence surface remains text-described; no source screenshot/trace/HAR/live-viewer visual inserted. | Main keeps local Codex browser-evidence analogy from P11. |
| `https://opengsd.net/roadmap` | Roadmap checked as visual/ecosystem candidate; no standalone visual inserted. | External image queue remains deferred. |

P12 added no new source facts to the main argument. It only resolved visual-source status: official/public surfaces checked in this pass were not used as inline images.

## P13 synthetic visual decision

P13 did not insert a new synthetic figure. The existing visual layer already covers the article's nontrivial mechanics: process-runtime profile, browser-evidence analogy, artifact consumption, `gsd-core`/`gsd-pi` state authority and the GSD/PWG boundary. Additional candidates such as issue-to-ship path, runtime-discipline stack, and failure-mode matrix remain deferred because they would mostly duplicate prose or existing figures.

## P14 concept reinforcement source usage

| Source family | How P14 used it | Where reflected |
|---|---|---|
| C5 theory-to-atlas fragments | Editorial framing for standalone article: reader question, local theory minimum, mechanism, surfaces, limits and return to theory. | New subsection `Минимум рамки для самостоятельного чтения`. |
| `GSD_METHOD_DOSSIER.md` | Confirmed that the article already has enough GSD-specific material to avoid generic theory copy-paste. | P14 local distinctions use GSD terms and existing primary-source links. |
| Existing Open GSD primary links | Reused as source support for intent/state/authority/evidence/repair anchors. | New subsection cites phase loop, configuration and auto mode rather than internal fragments. |

P14 added no new external factual source URLs. It strengthened the article's standalone framing while keeping public source citations in the main text.

## P15 concept reinforcement source usage

| Source | What P15 used | Where reflected |
|---|---|---|
| `the-phase-loop.md` | Phase transitions must produce consumable artifacts rather than just tutorial labels. | New subsection `Негативный тест механизма`. |
| `artifact-types.md` | Durable files matter only when another workflow consumes them. | Same subsection and already-existing artifact consumption argument. |
| `Auto Mode` | Autonomy requires explicit pause/recover/takeover and persisted state boundaries. | Same subsection. |
| `verification-patterns.md` | Verification must move beyond existence toward substance/wiring/behavior. | Same subsection. |
| `GSD User Guide` / `GSD Configuration` | Quick/fast paths and policy/gate controls define the ceremony/risk boundary. | Same subsection and existing failure-mode section. |

P15 added one main-text mechanism test and no new image assets.

## P16 theory-source usage

| Theory input | Use in P16 | Main-text effect |
|---|---|---|
| `00_spine_map` | Mapped GSD to the lifecycle of one software change. | No main change required; P14/P15 already expose the local lifecycle frame. |
| `A3` | Checked the boundary between specification inputs and GSD as process runtime. | No main change required; boundary section already protects Spec Kit/Kiro/SPDD distinction. |
| `A5` | Confirmed GSD as process artifact only when state is consumed and gates exist. | No main change required after P15 negative mechanism test. |
| `A7` | Linked browser/UAT/check outputs to evidence rather than mere observation. | No main change required; Verify/browser sections already support it. |
| `A9` | Linked ship to lifecycle repair. | No main change required; P10/P14 and final sections already mention repair. |
| `A10` | Linked mode selection to quick/fast/GSD/PWG boundaries. | No main change required; ceremony limits already present. |
| `C5` | Checked concept-first standalone contract. | No main change required after P14. |

P16 modified `theory_links` as the primary output and left the article text unchanged because it already carried the necessary theory connection without rewriting the general theory.


## P17 language-pass source usage

P17 не добавлял новые факты и не вводил новые внешние источники. Проход использовал уже разрешённые правила русского режима и применил их к основному тексту: обычные объяснительные слова были переведены на русский, а точные имена команд, файлов, путей, конфигурационных ключей, продуктовых поверхностей и исходных source labels оставлены в исходной форме.

Проверены особенно чувствительные места: URL `workflow-map.md`, команда `/gsd-workflow`, ключи `workflow.*`, `checkpoint:human-verify`, `debug bundles`, `package legitimacy gates`, `GitHub sync`, `issue-driven orchestration`, `frontmatter`, `tool gates` и другие исходные labels. Они не использовались как английская связка; рядом, где нужно, добавлено русское пояснение.

## P18 language-pass source usage

P18 не добавлял источники и не менял фактическую опору статьи. Правки касались читаемости: заголовки, подписи фигур, таблицы, нижний раздел про ассеты и отдельные объяснительные фразы приведены к более естественному русскому техническому стилю. Source-specific имена, команды, файлы, пути, статусы и конфигурационные ключи сохранены.

## P19 editorial source usage

P19 не добавлял новые источники. Редакторская проблема была не в нехватке фактуры, а в том, что основной текст после P18 всё ещё содержал служебный раздел про будущий asset-pass. Этот материал удалён из пользовательской статьи и оставлен в companion-файлах, где ему место. Источниковая опора статьи не изменилась.

## P20 editorial source usage

P20 не добавлял источники и не менял фактологию. Основная правка касается входного редакционного раздела: `Контракт статьи` был заменён на более читательский `Что важно удержать`, а формулировки вокруг цели чтения стали меньше похожи на внутренний бриф. Все source-specific ссылки и технические детали сохранены.

## P21 editorial source usage

P21 не добавлял источники. Правка касается standalone-читаемости: внутреннее выражение `минимум рамки / местное различение` заменено на более естественную опору чтения GSD. Первичные ссылки в этом блоке сохранены.

## P22 structure-pass source usage

P22 не добавлял источники и не менял фактическую опору статьи. Правка переставила уже существующий раздел `Что ломается без внешнего процесса` ближе к началу, чтобы первый экран был problem-first: сначала длинная агентная сессия, преждевременная готовность и потеря состояния, затем рабочая рамка чтения GSD. Ссылки внутри перенесённого раздела сохранены без изменения.

## P23 companion-sync source usage

P23 не добавлял источники и не менял основной текст. Source usage сведен с фактической статьёй: текущие public citations поддерживают вводную provenance/product карту, `context rot`, фазовую петлю, `.planning/`/artifact consumption, config/runtime policy, `gsd-pi` state/auto-mode, browser evidence, issue ingress, failure modes and mode boundaries. Оставшийся source risk — не отсутствие переноса, а freshness: перед датированной публикацией нужно перепроверить release channels, tagged releases и lineage/reference paths.

## P24 style audit source usage

P24 не добавлял и не удалял источники. Правки касались только русской формы: убраны несколько калькированных или pass-facing оборотов (`публичная поверхность`, `анти-резюме`, `процессная машина`, `исполняемая дисциплина`, `coverage решений`) и сохранены source-specific labels, команды, paths, config keys and product names. Фактология и цитируемые primary links не изменились.

## P25 selective rewrite source usage

P25 не добавлял источники. Правки выборочно улучшили русский технический текст в уже поддержанных источниками местах: boundary paragraphs, command routing, issue-to-ship example, runtime policy, `gsd-pi` lifecycle and failure-mode section. Source-specific names, commands, config keys and URLs preserved.

## P26 guarded final style source usage

P26 не добавлял и не удалял источники. Финальный стилевой проход сохранил source factuality: команды, числа, ограничения, raw/doc URLs, config keys, product names and evidence boundaries остались прежними. Изменились только формулировки вокруг уже перенесённых фактов.

## Final verification source-usage note

Финальная проверка не добавляла новых источников и не меняла фактические claims. Единственная правка основного текста была стилевой: читательская формула `ремонт жизненного цикла` заменена на прямое объяснение обновления долговечных артефактов после поставки. Источниковая опора этого места осталась прежней: phase loop, executor contract, first-project tutorial and browser evidence commands.
