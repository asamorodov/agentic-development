# BMAD Method — theory links

Статус: P26 завершил guarded final style pass; semantic map сохранена, локальная формулировка инварианта стабилизирована.


## P16 semantic backlink map

Этот проход фиксирует не только направление “из теории в статью”, но и обратный вклад статьи: какой вопрос общей рамки BMAD помогает проверить на конкретном методе.

| Theory fragment | Theoretical question clarified by BMAD | BMAD article answer / constraint | Article location |
| --- | --- | --- | --- |
| 00 — spine / unit of change | What must survive as a software change moves from intent to decision, work, evidence, acceptance and maintenance? | BMAD shows one complete process-profile answer: the surviving carrier changes from PRD/product frame to architecture, story, sprint state, review findings, investigation, retrospective and correct-course proposal. | Intro; “artifact that frames the next step”; main chain; repair sections. |
| A3 — specification layer | When is a specification more than pre-coding prose, and where does human permission enter before action? | BMAD keeps PRD/spec/story as bounded inputs to later agents, but also shows that specification alone is insufficient: architecture, sprint state, review and repair must also carry authority. | Boundaries with Spec Kit/Kiro/SPDD; PRD/readiness gates; create-story/dev-story. |
| A5 — process methodologies | When does a repeated process become a useful artifact-bearing workflow rather than ceremony? | BMAD is useful where repeated agent failures involve lost context, premature coding, stale decisions or unverified status; it degrades when personas or documents stop changing the next input, gate or evidence surface. | Contract; invariant; roles; typical failures. |
| A7 — observation vs evidence | Which agent-produced signals are only observations for the next step, and which become evidence for human acceptance? | BMAD separates investigation grades, review findings, checkpoint preview, built-in QA and TEA release evidence; the agent may prepare signals, but acceptance requires a human decision or gate. | Review/checkpoint/evidence; investigation; gates; TEA boundary. |
| A9 — lifecycle repair | After a result or failure, which surface must be updated so the next agent does not inherit false context? | BMAD makes repair concrete through correct-course, retrospective, investigation, project-context updates, architecture/story lessons and stale-artifact cleanup. | Correct Course; investigation/retrospective; failure modes; practical reading. |
| A10 — mode selection | How much external structure is enough for the risk of this change? | BMAD supplies three visible depths: Quick Flow for local reversible work, full BMM for multi-stage context transfer, and TEA/Enterprise only when traceability, NFR, compliance or release evidence justify the cost. | Three modes; TEA section; typical failures; practical reading. |
| C5 — theory-to-atlas bridge | How can a technical atlas article be standalone without copying the full theory? | The article keeps a local reader question and mechanism, then returns theory links through compact questions rather than importing the whole A/B/C framework. | Intro; contract; “Where BMAD helps theory”; companion files. |

| Theory node / fragment | Why BMAD links there | Article sections carrying the link | P01 status |
| --- | --- | --- | --- |
| A5 — методологии процесса / process profiles | BMAD shows how a repeatable process can become an artifact-bearing workflow for agents: PRD, architecture, stories, sprint status, review, retrospective and correct-course. | Intro; «Главная цепочка»; «Где BMAD помогает общей теории». | Strong. |
| C2 — PWG → process profiles boundary | BMAD has stateful sprint artifacts, but baseline BMAD is not a full Persistent Work Graph. It helps define the boundary between process/status and durable work graph. | `sprint-status.yaml` section; theory section. | Strong; avoid overclaiming without PWG/Gas Town sources. |
| A9 — lifecycle repair | BMAD has explicit repair surfaces: correct-course, retrospective, investigation, project-context updates, stale artifact cleanup. | Correct Course; Investigation/retrospective; failure modes. | Strong; later pass can strengthen post-merge repair. |
| A10 — mode selection map | BMAD modes show why external structure is selected by risk: Quick Flow for small reversible work, full BMAD for multi-stage context, Enterprise/TEA for evidence-heavy work. | Three modes; practical reading section; failure modes. | Strong; keep A10 as decision support, not article structure. |
| A7 — evidence / testing | Review, checkpoint preview, built-in QA, TEA and investigation grades show how BMAD separates observation during work from evidence for human acceptance. | Review/quality; Investigation; TEA. | Medium; may need tighter wording in later passes. |
| A8 — authority / completion | Manual status update, release gates and approver signatures show that agent execution does not equal authority to accept risk. | Gates; TEA; practical reading. | Medium-strong. |
| C5 — concept-first atlas contract | BMAD article should be standalone and methodical: reader question, local theory minimum, mechanism, source surfaces, boundaries, failures and return links. | Whole article structure. | Strong. |
| GSD / BMAD dangerous pair | BMAD should not absorb GSD. BMAD is centered on PRD/architecture/story/sprint-status document transitions; GSD focuses on phase loop, `.planning/`/`.gsd/`, orchestrator/subagents and verification/runtime supervision. | New contract section; theory section. | P02 strengthened from allowed GSD dossier. |
| Gas Town / BMAD dangerous pair | BMAD is document/status process; Gas Town is heavier multi-agent operating environment with durable orchestration and Beads/PWG-style work graph surfaces. | Contract section; theory boundary and image plan. | P02 strengthened from allowed Gas Town/PWG dossiers; still avoids Gas Town handbook details. |


## P02 boundary map

| Adjacent article / mechanism | Boundary sentence now enforced in BMAD article | Duplication risk controlled |
| --- | --- | --- |
| GSD | BMAD is artifact-first SDLC profile; GSD is phase loop plus process/runtime supervision, `.planning/`, `.gsd`/SQLite projections in `gsd-pi`, thin orchestration, subagents and verification. | BMAD article should not explain GSD namespaces, model routing, cost supervision or auto-mode mechanics except as boundary. |
| PWG / Beads | BMAD has `sprint-status.yaml` but not a full durable graph of work objects, dependencies, owners, gates, recovery and handoff notes. | PWG article should own graph vocabulary; BMAD article should only show why sprint status is less than PWG. |
| Gas Town | BMAD may prepare planning artifacts for a larger operating environment; Gas Town owns town/crew/orchestration vocabulary and durable coordination layer. | Avoids turning BMAD into ecosystem overview. |
| Spec Kit | BMAD can consume or coexist with specs, but Spec Kit owns the `spec → plan → tasks → implement` specification workflow. | Avoids duplicating specification-driven article. |
| Kiro Specs | BMAD uses specs and stories; Kiro owns IDE/CLI spec-state product surface around requirements/design/tasks. | Avoids product tutorial drift. |
| SPDD | BMAD includes promptable artifacts; SPDD owns structured prompt as core intent artifact and its review/sync loop. | Avoids prompt-method duplication. |
| TDAD-like test/spec methods | BMAD includes testing and gates, but does not define TDAD-specific practice in this article. | Concrete TDAD facts deferred until a TDAD dossier/source pass exists. |
| ADR | ADR records architecture decisions and status/consequences; BMAD uses ADR within architecture handoff but does not reduce lifecycle to ADR. | ADR article should own decision-record lifecycle and agentic ADR tooling. |

C5 and A10 remain read-only context in P02. No concrete contradiction found.


## P04 handoff theory reinforcement

P04 strengthens the A5/process-profile and C5/concept-first links: BMAD is now shown as a chain of documentary handoff contracts, not as a persona list. It also strengthens A8/evidence and A9/repair because the final handoff rows explicitly route review, investigation, retrospective and correct-course findings into next work.

No new cross-article boundary was added in P04.


## P05 recovery-surface theory reinforcement

P05 strengthens the link between BMAD and lifecycle recovery: files are now framed as surfaces that restore method version, planning intent, project rules, sprint state and story execution point. This reinforces A9/repair and the PWG boundary: BMAD has recovery surfaces in documents and status files, but it still is not a full durable work graph.


## P06 brownfield theory reinforcement

P06 strengthens BMAD as knowledge creation for future agents: brownfield scan levels now describe different epistemic depths, `project-scan-report.json` preserves the creation state, and `index.md` routes later agents to generated docs or missing-doc markers. This reinforces A9/recovery and A7/evidence while preserving the article boundary: the full brownfield handbook remains outside this article.


## P07 gate/evidence/repair theory reinforcement

P07 strengthens A7/evidence, A8/authority and A9/repair. The article now states that BMAD agents can prepare evidence, diagnosis, proposal and route, but humans decide product, architecture, status and process changes. This also reinforces the negative boundary: BMAD is not autonomous acceptance of work.


## P08 extension/failure-mode theory reinforcement

P08 strengthens A10/mode selection and A8/authority: TEA/Enterprise is framed as an evidence/release extension for high-risk work, while token cost, ceremony, stale artifacts and module confusion explain why BMAD depth must be selected by risk. The article still avoids using weak community signals as proof.

## P09 Quick Dev theory reinforcement

P09 strengthens A10 and A9. Quick Flow is now described as a distinct compressed mode, not as absence of method: it has intent compression, a minimal spec/approval layer, deferred unrelated work and layer-aware repair. This supports the A10 claim that process depth should follow risk, and the A9 claim that repair starts by locating the failed layer rather than by blindly adding another implementation patch.

It also strengthens A8/authority: even in the lightest BMAD mode, the agent prepares a plan, diff and local result, while the human keeps authority over scope, spec approval, final review and push/revert decisions.

## P10 reader-path theory reinforcement

P10 strengthens the C5 contract directly. The BMAD article now gives concept-first readers an invariant before the technical surfaces: “which artifact is the artifact that frames the next step for the next step?” This preserves article independence while keeping theory linkage precise.

The section also strengthens A5/process profiles and A8/authority. A process profile is visible as repeated transfer of authority between artifacts and human decisions, not as a list of personas or commands. It also reinforces A9/repair because review, status, lessons and correct-course are described as returning facts into the next working artifact.

## P11 visual-boundary theory sync

P11 reinforces the atlas visual rule: concept articles should use ready local assets when they directly support the local mechanism, but adjacent-theory images should not be imported merely because they are visually related. Fowler harness images remain better suited to harness/source-theory material; BMAD still needs BMAD-specific real workflow/artifact visuals or carefully bounded synthetic diagrams.

## P12 external visual-boundary sync

P12 reinforces the C5 visual boundary: real source visuals are valuable when they directly anchor the concept, but source-table/code fragments and editorial diagram ideas should not be screenshot merely to make the article look richer. For BMAD, the official Workflow Map is a true source visual; the rest of the current BMAD visual layer is better handled as text, synthetic figures or deferred design work.

## P13 synthetic visual-boundary sync

P13 reinforces the C5 rule that visuals should serve the local concept rather than decorate it. BMAD already has enough visual support for artifact handoff and minimal sprint state; deferred diagrams should either replace dense structures or move to handbook/fieldbook surfaces where their lifecycle detail becomes operational.

## P14 standalone concept theory sync

P14 strengthens the C5 standalone-article contract. The BMAD article now includes a minimal local example of a risky change moving through PRD, architecture/ADR, story, sprint status, review and repair. This is controlled repetition of the process-profile idea: the reader sees why BMAD is an artifact-first method without needing the broader A5/C2/A9 theory first.

The example also reinforces A10: small low-risk changes can stay in Quick Dev, while changes mixing product, architecture, security and data require the fuller process.

## P15 mechanism/failure theory sync

P15 strengthens A5, A8, A9 and A10 simultaneously. A process profile fails when its roles and documents do not change the next-step artifact; authority fails when a document cannot support a human decision; repair fails when stale artifacts become authoritative; mode selection fails when Quick, Full and Enterprise depth are chosen by habit rather than risk.

The update also preserves C2/PWG and GSD/Gas Town boundaries by keeping BMAD failures inside the document/status process profile instead of importing durable graph or orchestration semantics.

## P17 language theory sync

P17 does not change the semantic backlink map. It only aligns the main article’s theory-facing prose with Russian mode: ordinary English glue is translated, while theory node labels and BMAD/source terms remain stable where needed for cross-article navigation.

## P18 — языковая синхронизация теоретических связей

P18 не менял карту смысловых backlinks. Он только сделал теоретически значимые формулировки в основной статье более читаемыми по-русски: `project-context.md` трактуется как точное имя артефакта BMAD, а окружающее объяснение говорит о сужении контекста, последующем ремонте и читаемых для человека артефактах по-русски.

## P19 — редакторская синхронизация теоретических связей

P19 усилил локальный мост к общей теории без добавления новой теоретической главы. Четыре практических вопроса в конце статьи прямо связывают BMAD с темами артефакта, задающего рамку работы, передачи контекста, человеческого решения и ремонта после сбоя. Это делает теоретическую связь проверяемой на конкретном применении метода, а не только на уровне описания разделов.

## P20 — структурная синхронизация теоретических связей

P20 перенёс контрактный раздел после минимального примера. Это делает связь с C5/C10-подобной standalone-логикой сильнее: читатель сначала получает внутреннюю механику BMAD, затем сравнительные границы с соседними концепциями. Смысловые backlinks не изменены.

## P21 — редакторская синхронизация теоретических связей

P21 не менял теоретические backlinks. Уточнение перехода от сравнительных границ к устройству метода помогает удержать concept-first статью: теория и соседние методы задают границы, но основной текст возвращается к практической файловой механике BMAD.

## P22 — public-structure theory sync

P22 не менял теоретические тезисы. Первый экран остался problem-first, поэтому теория и границы не захватывают entry sequence. Визуальный placeholder Workflow Map теперь служит читательскому объяснению artifact flow, а не показывает рабочую заметку исполнителя.

## P23 — theory links companion sync

P23 проверил, что theory links остаются semantic backlinks, а не source coverage list. Перестановка контрактного раздела, публичная подпись Workflow Map и текущая консолидация open questions не меняют карту связей. Generic `C5/A10 sync pending` не добавлялся.

## P24 — theory link sync

P24 не менял теоретические связи статьи. Терминологическая правка «артефакты имеют приоритет» сохраняет тот же смысл, что и прежняя artifact-first формула, но делает его менее похожим на отдельный псевдотермин.

Связи с A5, A7, A9, A10 и C5 остаются теми же: процесс как носитель изменения, различение наблюдений и свидетельств, ремонт жизненного цикла, выбор глубины режима и standalone-статья без повторения всей теории.

## P25 — theory link sync

P25 не менял теоретические связи, но заменил кальку `working source of truth` на более естественную формулу: артефакт задаёт рамку следующего шага, а Workflow Map показывает смену ведущего артефакта между фазами. Это сохраняет связь с A5/A9/A10 и делает локальный инвариант понятнее без новой теоретической главы.

## P26 — theory link sync

P26 не менял theoretical backlinks. Theory section стал чуть прямее: BMAD занимает место среди process profiles, а вклад описан как дисциплина переходов между артефактами. Связи с A5/A9/A10/C5 сохранены.
