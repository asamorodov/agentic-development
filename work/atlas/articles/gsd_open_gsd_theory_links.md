# GSD / Open GSD — theory links

Статус: Final verification / theory links synchronized for current package.

## Основная роль в теории

GSD / Open GSD связан с общей теорией как пример process-runtime profile: внешняя структура задаёт фазы, роли, артефакты, политики инструментов, git-изоляцию, надзор и проверку, но не обязана становиться полной моделью Persistent Work Graph.

## Links to C5 concept-first atlas

- Статья следует модели C5: открывается reader question, объясняет давление, механизм, технические поверхности, source caveats, failures и theory return.
- Controlled repetition оправдано для терминов `context rot`, долговечное состояние, witness/evidence, process vs PWG, потому что без этих повторов читатель не поймёт GSD как самостоятельную концепцию.
- Статья не должна становиться mini-theory: раздел про PWG ограничен boundary, а не разворачивает всю теорию рабочего графа.

## Links to A10 mode selection map

- GSD расположен между лёгким разговором/планом и тяжёлыми формами внешней структуры.
- GSD выбирается, когда риск в агентной задаче связан с context rot, преждевременным кодом, потерей состояния, слабой проверкой, необходимостью контроля инструментов или длительным autonomous run.
- Если основное состояние работы должно переживать сессии как узлы, зависимости, владельцы, blocking/ready, handoff и evidence, GSD может быть недостаточен без PWG.
- Если изменение создаёт архитектурное обязательство, GSD должен остановиться и передать решение в ADR-like форму, а не скрывать решение внутри `PLAN.md`.
- Если риск связан с правами, секретами, production access или внешним PR, нужна среда исполнения и human acceptance, а не только хороший фазовый процесс.

## Boundary statements для будущих проходов

- GSD не равен Spec Kit: GSD управляет процессом и runtime-петлёй; Spec Kit-like формы фиксируют спецификационное намерение.
- GSD не равен ADR: GSD может обнаружить потребность в архитектурном решении, но не заменяет запись решения и последствий.
- GSD не равен PWG: `.planning/`, `.gsd`, SQLite, workstreams и graphs могут поддерживать рабочее состояние, но не гарантируют полный граф с владельцами, блокировками, readiness, handoff и evidence.
- GSD не равен browser evidence: `gsd-browser` может подкреплять UAT, но остаётся сопутствующим evidence backend.
- GSD не равен распределённому флоту агентов: у `gsd-pi` есть локальная граница SQLite/WAL; для межхостовой оркестрации нужен другой координатор.

## P02: контракт статьи и границы с соседними концепциями

- Контракт статьи теперь явно ограничивает её вопросом lifecycle control: фазы, восстановление контекста, supervision/evidence, tool policy, git isolation, verification, цена церемонии.
- Граница с PWG усилена: файлы состояния GSD и runtime-состояние помогают восстановлению, но сами по себе не гарантируют графовое состояние с зависимостями, владельцами, gate-условиями и семантикой ready/blocked.
- Граница с BMAD: BMAD трактуется как artifact-first профиль SDLC; GSD — как runtime/process supervision.
- Граница с Gas Town: Gas Town трактуется как многоагентная операционная среда; GSD — как проектный/локальный рабочий процесс и runtime-профиль.
- Граница со Spec Kit/Kiro/SPDD: это спецификационные рабочие процессы, поверхности и артефакты; GSD — process/runtime loop, который может потреблять такие входы.
- Общий долг `C5/A10 pending` не добавлен; C5 и A10 остаются согласованными для P02. Конкретный будущий долг: добавить article-to-article back-links, когда появятся соседние статьи атласа.


## P04: lifecycle control как theory bridge

- Новый subsection делает связь с общей теорией более явной: процессная форма определяется не набором файлов, а переходами “можно продолжать / нужно остановиться / нужен человек”.
- Это усиливает границу с PWG: GSD хорошо описывает фазовый runtime-route, но таблица намеренно не превращает каждый stop-сигнал в долговечный узел рабочего графа.
- Это усиливает A10 mode-selection: GSD выбирается там, где внешняя структура нужна для контроля движения и остановки, но задача ещё не требует отдельного корпоративного work graph или многоагентной операционной среды.


## P05: runtime discipline как theory bridge

- GSD теперь сильнее связан с общей теорией runtime governance: методология определяется не только фазами, но и тем, как команды, конфигурация, tool policy, git isolation, audit, recovery и evidence ограничивают действие агента.
- Это усиливает отличие от чисто документных SDLC: `config.json`, `ToolsPolicy`, worktrees, audit traces и headless query являются исполняемыми контурами, а не только описательными файлами.
- Это усиливает boundary с PWG: runtime discipline может производить signals для work graph, но не заменяет durable graph semantics сам по себе.


## P06: continuation/recovery as theory bridge

- P06 делает границу с общей теорией PWG точнее: durable files are recovery affordances, not graph semantics by themselves.
- `STATE.md`, phase docs, handoff files and `.gsd` projections show how a process can survive context loss, but they still need an executing consumer, authority rules and promotion semantics.
- This supports A10 mode selection: GSD is appropriate when the project needs process memory and recovery, while PWG becomes necessary when remaining work must become a durable dependency network with readiness, blockers, ownership, evidence and repair semantics.


## P07: `gsd-pi` unit lifecycle as theory bridge

- P07 strengthens the idea that agentic SDLC quality is produced by a runtime contour: state authority, permission boundary, execution trace, verification and recovery.
- This connects GSD to the broader theory of externalized agency: the agent does not merely “remember” the task; the environment reconstitutes a bounded unit of work and decides whether it may continue.
- The PWG boundary remains intact: a unit lifecycle can generate graph signals, but it is still a runtime progression model unless durable graph semantics are made explicit.


## P08: limits as theory bridge

- P08 prevents GSD from collapsing into a summary formula. The method is not “phases exist”; it is “phase transitions are controlled by freshness, gates, tool policy, evidence and state consumption.”
- The added no-full-graph-state boundary strengthens the distinction between process runtime and PWG.
- The ceremony limit supports the broader mode-selection map: use GSD when risk justifies process overhead; shrink or avoid it when the task is too small.


## P09: issue ingress as theory bridge

- P09 strengthens the theory that GSD is an ingress-and-control process, not only an execution loop.
- External trackers are treated as sources of candidate work; GSD inserts classification and human review before tracker items become phase commitments.
- This supports the PWG boundary: issue trackers and sync mappings can provide graph inputs, but authority and continuation semantics remain inside the chosen process/runtime unless a full work graph is explicitly modeled.


## P10: reader path as theory bridge

- P10 makes the process-runtime profile visible through one change lifecycle.
- The example maps the local concept back to theory: candidate work, planning authority, execution boundary, evidence, completion authority and lifecycle repair.
- It also protects against tool summary: the important part is not the command sequence, but the changing question at each transition.


## P11: local visual asset as theory bridge

- The inserted image supports the “evidence” part of the theory: UI validation is stronger when it creates repeatable action/snapshot/runtime-event traces, not just a claim that the interface was inspected.
- The caption preserves conceptual boundary: Codex is an analogy for browser-evidence contour, while GSD's own source-specific surface remains `gsd-browser`.
- Rejecting the dashboard and harness-feedback images keeps the GSD article from drifting into a generic coding-agent or harness-engineering article.

## P12/P13 visual theory bridge

- P12 reinforces a theory boundary: absence of a source screenshot is not evidence that the concept should be redrawn synthetically. Real images, local image assets and author synthetic figures have different epistemic roles.
- P13 keeps the article from becoming a poster of process diagrams. The synthetic figures that remain are those that explain nontrivial boundaries: runtime profile, artifact consumption, state authority and PWG distinction.
- The visual layer now mirrors the conceptual claim: GSD is a process-runtime profile, so the diagrams should clarify authority, handoff, state and evidence rather than decorate every command surface.

## P14 standalone theory bridge

- P14 makes the article self-sufficient by naming the minimal theory needed for GSD: intent, working state, authority, evidence and lifecycle repair.
- The bridge remains local: each term is immediately mapped to `CONTEXT.md`, `STATE.md`, `.gsd`, SQLite, agent roles, checkpoints, UAT/browser evidence and post-ship updates.
- This protects the article from two failures: assuming the reader has read the entire theory, or copying the entire theory into the article.

## P15 mechanism/failure theory bridge

- P15 translates the general theory of process failure into a local GSD test: transition, consumer and stop condition.
- It strengthens the PWG boundary by naming what graph state would need to exist before GSD-like artifacts become a true Persistent Work Graph.
- It also ties evidence and ceremony back to mode selection: weak evidence and too-heavy process are both failures of the same runtime profile, not separate footnotes.

## P16 semantic back-links to theory fragments

| Theory fragment | Semantic question answered by the GSD article | GSD anchor in the article |
|---|---|---|
| `00_spine_map` | How does one software change move from intention to execution, evidence, acceptance and later maintenance without losing responsibility? | The article treats GSD as a process-runtime profile for one change lifecycle: Discuss, Plan, Execute, Verify, Ship and post-ship repair. |
| `A3_specification_methodologies_synthesis` | When is a process consuming specification-like intent rather than becoming a specification methodology itself? | GSD accepts Discuss output, requirements, issue classification, ingest-docs and UI/spec inputs, but it does not replace Spec Kit, Kiro, SPDD or ADR. |
| `A5_process_methodologies_synthesis` | What makes a process an artifact rather than a sequence of reminders? | GSD demonstrates that a process matters only when phases create consumed state, gates, fresh execution contexts, verification and recoverable handoff. |
| `A7_observation_vs_evidence` | When does an agent's observation become evidence that a human can use to accept or reject the result? | The Verify/Ship and `gsd-browser` sections distinguish UAT, commands, CI/PR status, screenshots, traces, HAR and browser assertions from an agent's summary. |
| `A9_lifecycle_repair` | Why does merge/ship not finish the lifecycle of an agentic change? | The article tracks post-ship updates to `STATE.md`, code maps, requirements, decisions, tests, hooks, skills and global learnings. |
| `A10_mode_selection_map` | When is GSD the right amount of structure, and when should the mode be lighter or heavier? | GSD is positioned between one-prompt work and PWG/Gas Town-like heavier forms; quick/fast paths cover small reversible tasks, while durable graph needs push beyond GSD. |
| `C5_theory_to_technical_atlas` | How should a concept-first atlas article repeat theory without becoming the theory chapter? | P14/P15 make the article standalone through local distinctions and a negative mechanism test rather than a full theory reprise. |

Back-link rule for future article pages: link to the theory fragment only when the reader is asking that semantic question. Do not add generic “see A3/A5/A10” references that merely point to neighboring chapters.


## P17 language bridge

P17 уточнил языковую связь между локальной теорией статьи и русским изложением. `process-runtime profile` теперь проводится как `профиль процесса в среде выполнения`; `evidence` как `свидетельство`; `recovery` как `восстановление`; `gate` как `проверочный барьер`; `checkpoint` в пользовательском объяснении как `контрольная остановка`. Это помогает связать GSD с теориями процесса, свидетельства, ремонта жизненного цикла и выбора режима без английской связки в основном тексте.

## P18 language bridge

P18 закрепил более естественную русскую форму ключевой рамки: статья теперь говорит о `профиле работы в среде выполнения`. Это оставляет связь с process/runtime-theory, но звучит менее как калька. Языковой мост к теории сохраняет четыре опорных смысла: внешний процесс против context rot, потребляемое состояние против архива, свидетельства против summary агента и граница GSD/PWG по полноте графа работы.

## P19 editorial theory link note

P19 усилил концептуальный финал без добавления новой теории: статья теперь заканчивается разделом `Как читать GSD в атласе`, где GSD возвращается к карте режимов, границам со Spec Kit/ADR/PWG/browser evidence и практической силе внешнего процесса. Asset-status вынесен обратно в companion слой, чтобы теория и вывод не смешивались с редакционным журналом.

## P20 editorial theory link note

P20 сделал вход в теорию менее редакционным: раздел `Что важно удержать` теперь напрямую называет четыре рабочие вещи — context rot, потребляемое состояние, разделение надзора/свидетельств/приёмки и границу с PWG. Это укрепляет связь с theory links без добавления новой теории.

## P21 editorial theory link note

P21 сохранил теоретические опоры, но убрал внутренний тон. `Намерение`, `рабочее состояние`, `полномочие`, `свидетельство` и `ремонт жизненного цикла` теперь вводятся как пять опор для чтения GSD, а не как абстрактные местные различения.

## P22 theory link note

P22 улучшил порядок входа в концепт без добавления новой теории. Теперь статья идёт по последовательности: проблема длинной агентной работы → рабочая рамка чтения → границы с соседними концепциями → механизм GSD как профиля работы в среде выполнения. Это помогает читать GSD как ответ на lifecycle failure, а не как taxonomy-first справочник инструментов.

## P23 theory-link sync

Theory links now match the article state: C5/A10 are not pending generic sync items. The concrete links are process lifecycle, mode selection, artifact consumption, evidence, lifecycle repair and the boundary with PWG/ADR/specification/browser-evidence/multi-agent-operating-environment. Future work is limited to article-to-article links when neighboring atlas entries exist.

## P24 style/theory note

P24 не менял теоретическую роль GSD. Для читательского текста внутренний термин `ремонт жизненного цикла` смягчён до `обновление после поставки`; связь с lifecycle repair сохраняется через смысл: после ship нужно решить, какие требования, карты, тесты, hooks, skills or `global_learnings` становятся новым постоянным состоянием проекта.

## P25 style/theory note

P25 kept the same theory links while making public prose less dependent on atlas-internal phrasing. The article still returns to the same semantic points: process/runtime profile, state consumption, evidence, lifecycle update after ship, and the GSD/PWG boundary.

## P26 final style theory note

P26 сохранил теоретические границы и сделал их менее служебными в пользовательском тексте. `Process/runtime profile` по-прежнему передан как `профиль работы в среде выполнения`; lifecycle repair остается публично выражен через `обновление после поставки`; GSD/PWG distinction remains unchanged.

## Final verification theory note

Связь с C5/A10 остаётся конкретной: статья удерживает GSD как самостоятельную concept-first статью атласа и как process-runtime profile, который может питать PWG, но сам не создаёт полноценный граф состояния. Финальная стилевая правка убрала внутренний термин `ремонт жизненного цикла` из читательского текста; смысл сохранён как обновление долговечных артефактов после поставки.
