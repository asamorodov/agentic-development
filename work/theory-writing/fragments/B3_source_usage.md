# B3: использование источников

## Источники, использованные при написании основного текста

| Источник | Как использован в `B3_gas_town_beyond_pwg.md` | Статус |
|---|---|---|
| `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` | Взята граница PWG: долговечное рабочее состояние, владелец, зависимости, условия остановки, свидетельства выполнения, передача работы и восстановление после разрыва сессии. В B3 эта граница не переопределяется, а используется как нижний слой. | Внутренний уже созданный фрагмент; не цитируется как внешний источник. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | Использована композиционная функция B3: Gas Town как deep case организационно-операционного жизненного цикла сверх PWG. | Структурный источник, не внешний факт. |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | Использована формула узла: «PWG даёт слой продолжимой работы; Gas Town добавляет организационную среду, роли, Mayor, сервисных агентов, операционную культуру и цену оркестрации». | Плановый источник, не цитируется в основном тексте. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Использованы правила для companion-файлов и фигур: не вставлять декоративные схемы, вести реестр кандидатов, различать synthetic/local/external/editorial. | Методический источник, не цитируется в основном тексте. |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Использован как карта фактов и первичных ссылок по Gas Town, Beads, ролям, Mayor, GUPP, hooks, сервисным агентам, queue/backpressure, ограничениям Dolt/Beads. | В основном тексте не цитируется; все фактические опоры переведены на первичные источники. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Использован для удержания границы: B3 не должен заново доказывать PWG и не должен сводить PWG к Beads. | Внутренний dossier; не цитируется в основном тексте. |
| `work/old-site-theoretical-synthesis-baseline.md` | Использован как anti-degradation anchor: сохранены сильные старые идеи о Gas Town как среде ролей, Mayor, agent-not-session, service agents и цене оркестрации. | Внутренний baseline; не цитируется как источник фактов. |

## Первичные источники, процитированные inline

| Первичный источник | Для каких утверждений использован |
|---|---|
| [Gas Town README](https://github.com/gastownhall/gastown) | Gas Town как система для многих coding agents с persistent work tracking; не просто tmux/чат; `gt feed --problems` как поверхность проблемных состояний для Mayor/человека; базовый workflow You → Mayor → Convoy → Agent → Hook; scheduler как capacity governor и `gt seance` как session discovery/continuation. |
| [Gas Town Architecture](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) | Двухуровневая модель town-level и rig-level Beads, разделение координационной и проектной плоскостей, role/agent beads как часть организационного слоя. |
| [Gas Town polecat lifecycle patrol](https://github.com/gastownhall/gastown/blob/main/docs/design/polecat-lifecycle-patrol.md) | Current source для mail-based per-rig channel, передачи по жизненному циклу и операционных сигналов: `POLECAT_DONE`, `MERGE_READY`, `MERGED`, `MERGE_FAILED`, `GUPP_VIOLATION`, `ORPHANED_WORK`; заменяет старую ссылку на отдельный mail-protocol документ. |
| [Gas Town Escalation Protocol](https://github.com/gastownhall/gastown/blob/main/docs/design/escalation.md) | Escalation as governed work: Agent → Deacon → Mayor → Overseer, severity routing, stale detection, re-escalation and bead comments; поддерживает тезис, что blockers становятся частью организационной петли. |
| [Gas Town Docs](https://docs.gastownhall.ai/) | Роли Crew/Polecat, Convoys как tracking surface, identity/attribution и общая операционная поверхность Gas Town. |
| [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) | Роли, agent-not-session, GUPP/hook culture, высокая цена и хаотичность frontier-системы. Не используется как источник текущей storage-архитектуры Beads. |
| [Mayor role template](https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl) | Правило оформлять кодовую работу через `bd create` и `gt sling`, а не держать её как приватное поручение в чате; правило подотчётности: завершение записывается, передача логируется, а Beads фиксирует сделанное. |
| [Gas Town CHANGELOG](https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md) | Операционные признаки: convoy dashboard, merge queue, heartbeat, event-driven lifecycle, `FIX_NEEDED`, `awaiting_verdict`, pressure checks, typed status; аргумент о сервисных агентах и backpressure. |
| [Gas Town Glossary](https://github.com/gastownhall/gastown/blob/main/docs/glossary.md) | MEOW как термин для Molecular Expression of Work; Hook, Convoy, Wisp, Seance/Patrol as vocabulary supporting work decomposition and lifecycle. |
| [Beads multi-agent coordination](https://gastownhall.github.io/beads/multi-agent/coordination) | `bd pin`, `bd hook`, последовательная передача, `fan-out/fan-in` и резервирование файлов как фактура для владения и передачи работы. |
| [Beads Architecture](https://gastownhall.github.io/beads/architecture) | Dolt как источник истины, JSONL как экспорт, ограничения применимости Beads. |
| [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime) | Compact/AI-oriented rehydration нового агента. |
| [Beads Codex Integration](https://gastownhall.github.io/beads/integrations/codex) | SessionStart/PreCompact/PostCompact/UserPromptSubmit как механизм удержания workflow после compaction. |
| [Beads Workflows](https://gastownhall.github.io/beads/workflows), [Beads Molecules](https://gastownhall.github.io/beads/workflows/molecules), [Beads Wisps](https://gastownhall.github.io/beads/workflows/wisps) | Formula/Molecule/Wisp как формы долговечных и лёгких рабочих цепочек. |
| [DoltHub: Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/) | Dolt-backed Beads workflows, shared remote, multi-clone visibility и поверхность конфликтов. |

## Источники, сознательно не использованные в основном черновике

| Источник | Причина |
|---|---|
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | HumanLayer полезен как соседний опора нижнего слоя про harness, но B3 должен быть о Gas Town сверх PWG. В основном тексте оставлена только короткая теоретическая линия «harness → PWG → Gas Town» без пересказа истории. |
| Hacker News discussion from dossier | Слабый социальный сигнал о восприятии/скепсисе. Не нужен для основного аргумента; может пригодиться в будущей заметке об аудите или восприятии. |
| Beads issue `#3313` и release-gating examples | Хорошие детали о стоимости обслуживания Dolt/Beads, но слишком частный уровень для первого B3. Основной текст ограничился архитектурными limits и DoltHub workflow. |
| Источники LangGraph/Temporal/CRDT/STORM/Task Master из PWG dossier | Они нужны для границы PWG в A4, но B3 не должен заново доказывать PWG и не должен распыляться на сравнительный landscape. |
| Внешние фигуры Gas Town из Medium | Не вставлены без asset-pass и проверки прав/статуса. Занесены в `B3_figure_candidates.md`. |
| README/Mermaid workflow diagrams and architecture diagrams | Признаны реальными внешними визуалами, а не приглашением рисовать текстовую копию. До asset-pass и проверки прав остаются только кандидатами. |

## Примечание к source-pass `63247c64`

В этом pass внешние ссылки были раскрыты вокруг уже написанного текста. Две ссылки скорректированы: архитектурный источник заменён на current `docs/design/architecture.md`, а старый `MAIL_PROTOCOL.md` заменён на current `docs/design/polecat-lifecycle-patrol.md`, где mail-based channel и lifecycle signals описаны вместе с patrol/recovery контекстом.

Medium-статья Steve Yegge сохранена как источник для ролей, GUPP/hook culture, agent-not-session и цены frontier-системы. Её storage-детали не используются как текущая архитектурная опора: для Beads backend B3 опирается на current Beads Architecture and DoltHub workflow sources, где Dolt описан как source of truth.

## Provenance-check `dd3dc3e2`

Публичный фрагмент `B3_gas_town_beyond_pwg.md` не использует внутренние dossier, plans или reports как inline evidence. Внутренние документы остаются рабочими источниками композиции и anti-degradation контроля; фактические утверждения в основном тексте опираются на первичные внешние источники, перечисленные выше.

## Residual provenance note `35eab4eb`

Остаточный pass не добавлял новых источников. Проверка публичного `B3_gas_town_beyond_pwg.md` показала, что internal working files are not used as inline evidence; they remain companion-level planning/provenance context only.

## Repair-note `b3_style_boundary_repair_2026_06_11`

Этот pass не добавлял новых первичных источников. Основной B3 был отремонтирован по языку и композиции: убраны лишний английский клей, кальки вроде `контрольная плоскость`, публичная таблица русифицирована, а визуальный companion исправлен: локальные Gas Town assets признаны существующими, но не вставлены автоматически из-за риска дублирования A5 и смещения B3 в technical atlas.
