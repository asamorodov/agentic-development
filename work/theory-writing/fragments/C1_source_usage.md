# C1 source usage

Статус: companion-файл финальной упаковки `C1_specification_to_pwg.md`; набор первоисточников после третьего общего repair-pass не расширялся.

## Использованные первоисточники в основном тексте

| Источник | Какое утверждение поддерживает | Где использован | Статус |
| --- | --- | --- | --- |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | SPDD удерживает структурированный prompt как артефакт намерения и управления изменением. | Первый смысловой ход о силе спецификационного артефакта. | Использован как первичный методологический источник. |
| [`spdd-reasons-canvas.md`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) | `/spdd-reasons-canvas` создаёт Canvas с секциями `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards` и сохраняет файл prompt. | Первый смысловой ход; точная фактура Canvas. | Использован. |
| [`spdd-generate.md`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) | Генерация должна читать весь prompt-файл и секции Canvas перед кодогенерацией. | Первый смысловой ход; граница “спецификация как вход исполнения”. | Использован. |
| [`spdd-prompt-update.md`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) | `/spdd-prompt-update` обновляет существующий SPDD prompt при новых требованиях, архитектурных изменениях или constraint updates, сохраняя REASONS Canvas и проверяя cross-section consistency. | Раздел “Что должно перейти…”: спецификация может сама поддерживаться после изменений, но PWG хранит состояние работы над этим изменением. | Добавлен в companion во втором/третьем проходе; ссылка уже используется в основном тексте. |
| [`spdd-sync.md`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) | `/spdd-sync` синхронизирует изменения реализации обратно в structured prompt: анализирует изменения, сравнивает с prompt, планирует обновления, обновляет prompt и проверяет consistency/traceability/completeness. | Абзац о SPDD и новый абзац readiness/gates/recovery: prompt может отстать от кода, поэтому PWG должен хранить sync-gate и восстановительный след. | Добавлен в companion во втором/третьем проходе; ссылка уже используется в основном тексте. |
| [Spec Kit Quick Start Guide](https://github.github.com/spec-kit/quickstart.html) | Рекомендуемая последовательность `/speckit.specify → /speckit.plan → /speckit.tasks → /speckit.implement` и расширенный путь с уточнениями и проверками. | Переход к продуктовой форме specification-to-tasks. | Использован. |
| [Spec Kit Workflows](https://github.github.com/spec-kit/reference/workflows.html) | `Full SDD Cycle` связывает `specify`, `review-spec`, `plan`, `review-plan`, `tasks` и `implement`; workflow может останавливаться на gate, хранит состояние запуска в `.specify/workflows/runs/<run_id>/` (`state.json`, `inputs.json`, `log.jsonl`) и возобновляется точным шагом через `specify workflow resume <run_id>`. | Вводный мост после Spec Kit/Kiro и новый абзац readiness/gates/recovery: workflow-gate полезен, но состояние запуска команды не заменяет PWG readiness/evidence/owner. | Добавлен во втором проходе; повторно использован в третьем. |
| [`plan.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md) | Фаза plan создаёт исследование, модель данных, контракты, quickstart и обновляет контекст агента. | Переход от спецификации к пакету проектных артефактов. | Использован. |
| [`tasks.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/tasks.md) | `tasks.md` организует задачи по пользовательским историям, зависимостям, параллельным примерам и MVP-first стратегии. | Фактура о том, как план становится исполнимым списком работ. | Использован. |
| [`implement.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/implement.md) | `/speckit.implement` проверяет незакрытые checklists, читает рабочие артефакты и отмечает задачи выполненными. | Аргумент о том, что execution-status появляется, но требует PWG-обвязки. | Использован. |
| [`clarify.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/clarify.md) | Уточнения возвращаются в `spec.md` как записанный раздел Clarifications. | Раздел “Что должно перейти из спецификации в состояние работы”; новый абзац readiness/gates/recovery. | Использован; повторно задействован в третьем проходе. |
| [`checklist.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/checklist.md) | Checklists проверяют качество требований и помечают gaps/ambiguities/conflicts. | Раздел о преобразовании проверок спецификации в контрольные условия PWG; новый абзац readiness/gates/recovery. | Использован; повторно задействован в третьем проходе. |
| [`analyze.md`](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md) | Анализ читает `spec.md`, `plan.md`, `tasks.md` и constitution без записи, ищет несогласованности и требует отдельного разрешения на правки. | Раздел о человеческой контрольной точке перед реализацией; новый абзац readiness/gates/recovery. | Использован; повторно задействован в третьем проходе. |
| [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) | Feature Specs создают `requirements.md`, `design.md`, `tasks.md` и требуют проверки фаз пользователем. | Переход к IDE-поверхности specification-to-tasks. | Использован. |
| [Kiro Specs](https://kiro.dev/docs/specs/) | Kiro показывает статусы задач и связывает исполнение с `tasks.md`. | Первый смысловой ход; граница статуса задачи. | Использован. |
| [Run all tasks](https://kiro.dev/blog/run-all-tasks/) | Пакетное исполнение задач требует дополнительных опор: visibility/control, property-based tests, dev servers, LSP diagnostics, subagents и real-time visibility. | Раздел о Kiro: evidence pressure после batch execution — проверка среды должна стать привязанным свидетельством в PWG, а не только зелёным статусом. | Использован в первом проходе; уточнён в пятом source-depth pass. |
| [Specs just got faster](https://kiro.dev/blog/faster-smarter-specs/) | `Run all Tasks` строит dependency graph, группирует независимые задачи, не запускает одновременно задачи с записью в одни и те же файлы, ждёт код перед тестами, даёт каждой задаче isolated context и не останавливает независимые задачи из-за одного падения. | Раздел “Что должно перейти из спецификации в состояние работы”, абзац о Kiro и unresolved continuation после параллельного исполнения. | Добавлен во втором проходе. |
| [Kiro Specs Best Practices](https://kiro.dev/docs/specs/best-practices/) | Specs требуют continuous refinement; `Sync Files` в `tasks.md` обновляет задачи после изменения requirements/design; `Run all Tasks` запускает незавершённые required tasks. | Абзац о Kiro и новый readiness bridge: task-снимок может устареть, поэтому PWG должен знать, что именно готово к запуску после sync. | Добавлен во втором проходе; повторно использован в третьем. |
| [Beads Dependencies](https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md) | Блокирующие зависимости влияют на готовность работы через dependency graph. | Раздел о готовности и блокировке после старта работы. | Использован; в пятом проходе дополнен CLI reference источниками для `bd ready`/`bd blocked`. |
| [`bd ready`](https://gastownhall.github.io/beads/cli-reference/ready) | `bd ready` показывает open issues без active blockers, исключает `in_progress`, `blocked`, `deferred`, `hooked`, использует blocker-aware semantics, поддерживает `--claim`, `--gated` и `--explain`. | Beads-абзац о readiness как вычислимом праве продолжения/claim, а не просто следующем пункте task-list. | Добавлен в пятом source-depth pass. |
| [`bd blocked`](https://gastownhall.github.io/beads/cli-reference/blocked) | `bd blocked` показывает blocked issues; это минимальный CLI-язык для явного статуса “не готово”. | Beads-абзац о блокировке и различии между готовым, занятым, заблокированным и отложенным work. | Добавлен в пятом source-depth pass. |
| [Beads Multi-Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination) | Закрепление через `bd pin`, проверка закреплённой работы через `bd hook`, последовательный handoff Agent A → Agent B, параллельная работа, fan-out/fan-in, reservations/file locking и best practices по ownership, документированному handoff, labels, reservations и status checks. | Раздел о владельце, безопасном продолжении, передаче между агентами и недостающем состоянии после clear spec. | Уточнён во втором проходе. |
| [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate) | `bd gate` моделирует долговечные ожидания: human, timer, GitHub run, GitHub PR, bead; gate может блокировать workflow step, иметь waiter и закрываться вручную или watcher-ом. | Раздел о контрольные условиях как состоянии работы; новый абзац, где gate противопоставлен эфемерному “попросить подтверждение”. | Использован; уточнён в третьем проходе. |
| [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime) | `bd prime` даёт AI-optimized Markdown-контекст; CLI mode рассчитан примерно на 1–2k tokens, а назначение связано с SessionStart hooks и предотвращением забывания workflow после context compaction. | Раздел о восстановительной сводке; новый абзац recovery как короткий вход из текущего state. | Использован; уточнён в третьем проходе. |
| [Beads Recovery Overview](https://gastownhall.github.io/beads/recovery) | Recovery-инструкции структурируются через Symptoms, Diagnosis, Solution и Prevention; быстрые диагностики включают status/doctor/blocked. | Раздел о восстановлении после обрыва; новый абзац recovery как диагностируемый, а не риторический summary. | Использован; уточнён в третьем проходе. |

## Внутренние входы, использованные как навигация и композиционные ограничения

В основном тексте нет ссылок на внутренние досье, планы или соседние фрагменты как на подтверждение фактов. Они использованы для композиционной роли C1, границы с A2/A4 и выбора первоисточников:

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` — задал место моста между specification/ADR/contract и PWG.
- `work/theory-writing/CORE_NODES_WRITING_PLAN.md` — подтвердил задачу C1: почему спецификация не хранит owner, gates, readiness, source state и recovery.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` — подтвердил готовность C1–C4 после B-фрагментов и правило не превращать теорию в пересказ досье.
- `work/theory-writing/fragments/A2_specification_adr_contract.md` — использован для недублирования уже сформулированного различения спецификации, контракта и ADR.
- `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` — использован для недублирования общего определения PWG и его границ.
- Досье SPDD, Spec Kit, Kiro Specs и PWG — использованы как quarry для поиска первичных ссылок и точной фактуры; в основном тексте citation target ведёт к внешнему источнику.

## Неиспользованные или отложенные источники

| Источник / группа | Решение | Причина |
| --- | --- | --- |
| Public story anchors | Не использованы в первом черновике. | C1 выполняет методологический мост; фактические якоря взяты из первичных документов SPDD / Spec Kit / Kiro / Beads, чтобы не превращать фрагмент в пересказ историй. |
| Taskmaster, LangGraph, Temporal, STORM, CodeCRDT | В основном тексте не раскрывались. | Эти источники уже работают в A4 и лучше подходят для C2–C4 или technical atlas; C1 держит узкую промежуточную зону specification → PWG. |
| Kiro PBT, Autopilot, hooks | Упомянуты только косвенно через общий режим `Run all Tasks` и ограничения исполнения. | Полное раскрытие проверок и среды исполнения относится к C3/C4. |
| Внешние изображения из документации Kiro / Spec Kit / Beads | Не вставлялись inline. | Нет asset-pass, rights-check, download/localization и quality-check. Решения зафиксированы в `C1_figure_candidates.md`. |

## Изменения четвёртого прохода

Новые внешние источники не добавлялись. Правка основного текста использует уже внесённые источники и усиливает композиционную границу: C1 начинается после task decomposition, когда `Operations`, `tasks.md`, workflow-step или IDE-задача уже дают право начать изменение, но устойчивого PWG-состояния ещё нет.

## Изменения пятого source-depth pass

Открыты дополнительные источники, вытекающие из уже написанного текста и source usage: Kiro `Run all tasks`, Kiro Specs, Beads `bd ready` и `bd blocked`. В основной текст добавлено только полезное усиление: Kiro batch execution создаёт evidence pressure, а Beads `bd ready`/`bd blocked` уточняют readiness/blocking как вычислимое состояние. Визуальные материалы из Kiro страниц классифицированы как external real image candidates и не вставлены без asset-pass/rights-check.

## Изменения седьмого адресного прохода

Новые внешние источники не добавлялись. Основной текст усилен концептуальной механикой перехода artifact → responsibility: intent → work node goal, scope → write boundary, unresolved questions → owned waits, acceptance criteria → readiness/closure conditions, blockers → dependencies/gates, ownership → право продолжения/handoff, ожиданий по свидетельствам → привязанные свидетельства.

## Изменения восьмого адресного прохода

Новые внешние источники не добавлялись. Основной текст уточняет boundary: спецификационный слой остаётся владельцем исходного намерения/scope/acceptance criteria, а PWG хранит operational projection, ссылку на снимок, blockers, ownership, ожиданий по свидетельствам and recovery state.

## Изменения первого общего repair-pass

Новые внешние источники не добавлялись. Правка была композиционно-языковой: механика перехода artifact → responsibility сохранена, но переписана в более связный публичный ход с русскими опорами для scope/unresolved questions/acceptance criteria/blockers/ownership/ожиданий по свидетельствам.

## Изменения второго общего repair-pass

Новые внешние источники не добавлялись. Правка не меняла фактическую опору текста: она сократила обзорный крен в абзаце о Kiro, сохранив source-specific детали о dependency graph, waves, same-file ограничения, проверках среды и `Sync Files`, но вернув их к мостовому тезису о свидетельствах и продолжении работы. Также русифицированы связующие формулы вокруг Spec Kit Workflows, переход от артефакта к ответственности, readiness/gate/recovery and inline synthetic figure.

## Изменения третьего общего repair-pass

Новые внешние источники не добавлялись. Единственная содержательная правка сжала Beads-абзац в основном тексте: сохранены зависимости, `bd ready`/`bd blocked`, multi-agent coordination и `bd gate`, но детали вроде полного перечня исключаемых статусов, labels/reservations/status checks оставлены в source usage и не разворачиваются в мостовом фрагменте. Это снижает риск дублирования A4 и technical atlas.

## Readiness

`ready_with_known_debts` — источниковая база достаточна для финальной упаковки этой целевой группы. После третьего общего repair-pass новые источники не добавлялись; долги остаются публикационными: source freshness check по быстро меняющимся документациям Spec Kit, Kiro и Beads, а также отдельный asset-pass для внешних визуальных кандидатов.

## Финальная проверка упаковки

- Основной текст ссылается на первоисточники, а не на внутренние рабочие досье.
- Provenance по каждому использованному источнику вынесен в этот companion-файл.
- Новых внешних источников на стадии упаковки не открывалось и не добавлялось.
