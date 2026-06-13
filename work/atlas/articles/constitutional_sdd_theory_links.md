# constitutional_sdd — theory links

Статус: P26 guarded final style sync. Финальная теоретическая связка переименована и выровнена по тону без изменения роли CSDD в атласе.

## Article registry role

- Tier: `методическая статья`.
- Reader question: как ограничения безопасности и управления становятся верхним слоем спецификации, а не поздним checklist после генерации.
- Boundary: CSDD is not Spec Kit, not generic secure coding, not a full replacement for runtime security, and not an empirical standard based on one banking case.

## Theory feedback points

| Theory area | How the article links back | Current article section |
|---|---|---|
| Спецификационный слой | Constitution turns some requirements into higher-authority constraints that shape `spec.md`, `plan.md`, `tasks.md` and code. | Intro, reader question, spec/plan/tasks section |
| Намерение | Security/governance intent must survive context compression and feature decomposition. | Reader question, Context files |
| Полномочие | If Constitution conflicts with downstream artifacts, downstream artifacts are wrong unless a visible override is approved. | Foundry section, Human gates |
| Свидетельства | Compliance matrix turns a rule into file/line/technique/check evidence. | Compliance matrix, Verification |
| Контекст агента | `.specify/memory/constitution.md`, `CLAUDE.md`, `AGENTS.md`, commands and rules decide what the agent actually sees. | Context files |
| Process / gates | Constitution Check, `/speckit.analyze`, PR templates and CI gates show when process becomes an artifact. | Human gates, matrix-as-constraint, lifecycle repair |
| Среда исполнения | CSDD does not replace sandboxing, secret isolation, runtime monitoring or incident response. | What CSDD does not check |
| Последующий ремонт | Changing Constitution must update templates, commands, context files, tasks, checks and matrices. | Lifecycle repair |
| Mode selection | CSDD is justified when local feature work can violate durable security/policy constraints and when evidence matters for human acceptance. | Whole article, final theory section |

## Controlled repetition

Allowed repetition from theory:

- Specification as artifact of intent.
- Evidence as acceptance surface, not just observation.
- Authority of human/product/security owners over the agent.
- Lifecycle repair after accepted changes.

Duplication boundary:

- Do not rebuild full A/B/C theory in the article.
- Do not turn CSDD into a general SDD taxonomy.
- Do not let Spec Kit command detail consume the CSDD mechanism.

## P02 boundary map against neighboring atlas articles

| Neighbor | Difference to preserve | Article action |
|---|---|---|
| Spec Kit | Spec Kit supplies workflow and repository artifact machine; CSDD adds security/policy authority above local feature work. | Keep command details only when they show enforcement or traceability. |
| SPDD | SPDD stabilizes structured prompt/intent; CSDD stabilizes cross-feature security/governance constraints. | Use SPDD only as conceptual neighbor. |
| Kiro Specs | Kiro is productized spec state and human confirmation in an IDE/Web/CLI surface; CSDD is not a product surface. | Avoid UI/product tutorial drift. |
| ADR | ADR records why a specific architecture decision was accepted; Constitution states recurring constraints for many changes. | Use ADR only to clarify decision vs policy. |
| TDAD / A7 | Tests and evidence prove behavior; compliance matrix traces principle to implementation and must be linked to evidence. | Keep matrix/evidence distinction explicit. |
| PWG | PWG stores durable work state; CSDD defines constraints that can gate that work. | Do not turn article into work-graph discussion. |
| Security documentation | Documentation becomes CSDD only when it changes action and leaves traceable checks. | Keep action-influence criterion in intro contract. |

## P04 theory note — framing vs executable surface

The article now distinguishes between explanatory framing and executable repository surface. This supports the broader theory distinction between concept, artifact and action: a paper can explain a method; a repository artifact can constrain an agent; a gate needs a concrete check and authority. This distinction should be preserved in later passes when adding source depth or practical steps.

## P05 theory note — artifacts, state and expected outputs

The article now makes the statefulness of CSDD explicit: Constitution, spec, plan, tasks, context files, code/tests, matrix and exceptions each have a role, state and expected next output. This supports the broader theory claim that agentic SDLC needs external structure not as documentation volume but as durable state that changes what the agent and reviewer may do next.

## P06 theory note — traceability as authority in motion

The article now separates a matrix as a static report from traceability as a working constraint. This strengthens the broader theory distinction between intention, implementation and evidence: a rule has authority only if it changes planning, task generation, review, exception handling or amendment synchronization. A trace row without process pressure is a map of intent; a trace row tied to gates and evidence becomes part of the SDLC control surface.

## P07 theory note — layer boundary

The article now explicitly separates the specification workflow from the constitutional layer. This strengthens the atlas model of external structure: not every artifact is equal. Some artifacts carry feature intent, some carry decisions, and some carry authority over future work. CSDD belongs to the third class only when that authority reaches gates, context and evidence.

## P08 theory note — anti-summary and false confidence

The article now explicitly names the failure mode where external structure becomes ceremonial. This strengthens the atlas distinction between artifact, authority and assurance: an artifact can look formal without carrying authority, and authority can still fail without evidence and human ownership of risk.

## P09 theory note — task-local authority transfer

The article now adds a bridge between global authority and local agent action. A Constitution is too broad to be useful if passed wholesale into every task; a task-sized packet transfers just enough authority to constrain generation while preserving traceability to the full policy. This supports the atlas idea that good external structure is selected and activated, not merely stored.

## P10 theory note — reader path through a change

The article now shows one concrete feature as a path through CSDD. This supports the C5 atlas model: a concept article should not merely list files or commands; it should let the reader see how a local change becomes governed, implemented, evidenced and repaired.

## P11 theory note — local SDD visual as boundary support

The inserted Fowler SDD overview supports the layer boundary: it visualizes the generic agent/spec/memory shape that CSDD builds over. The caption keeps the image in a subordinate role, so the article still treats Constitution, traceability and evidence as the distinct CSDD contribution.

## P12 theory note — source visuals over decorative diagrams

The visual plan now preserves the hierarchy between real source visuals and future synthetic explanations. For CSDD, Marri's architecture figure and traceability table carry source-specific meaning; synthetic diagrams should only add explanatory value and must not replace source evidence without an explicit rights/readability decision.

## P13 theory note — restraint on synthetic diagrams

The article now records an explicit decision not to add author-created diagrams before source visuals are resolved. This supports the atlas rule that synthetic figures should clarify a real conceptual knot, not compensate for missing asset localization or decorative needs.

## P14 theory note — standalone concept-first entry

The article now has its own minimal vocabulary and local theory bridge. It should be readable from the concept alone: the reader sees what CSDD moves, which artifacts carry it, where the agent sees it, and what evidence closes it. This is controlled repetition, not a replacement for the broader theory.

## P15 theory note — failure modes inside the mechanism

The article now treats CSDD failure modes as broken transfers of authority rather than as a separate checklist of mistakes. Constitution fails when it does not change a downstream artifact; matrix fails when traceability lacks evidence; context fails when the agent reads stale or untrusted instructions; gates fail when they accept checklist wording without changed behavior. This reinforces the atlas distinction between artifacts as documents and artifacts as control surfaces.

## P16 semantic back-links to theory fragments

P16 adds semantic back-links: each theory connection is phrased as the theoretical question that the CSDD article helps answer, not as a reading pointer.

| Theory fragment | Theoretical question this article clarifies | CSDD answer from the article | Article anchor / boundary |
|---|---|---|---|
| `00_spine_map` | How does one software change preserve intent, responsibility and evidence across lifecycle transitions? | CSDD shows a change whose local feature intent is not enough: security/governance constraints must travel from Constitution through spec, plan, tasks, context, code, evidence and синхронизацию после слияния. | Final theory section; keep it as a local application of the spine, not a restatement of the full lifecycle. |
| `A3_specification_methodologies_synthesis` | Which object becomes governable before the agent is allowed to act? | CSDD's governable object is not the feature spec itself but the higher-authority Constitution/policy layer that constrains feature specs. | Layer model, reader question, Constitution section. |
| `A5_process_methodologies_synthesis` | When is a process a real artifact rather than ceremony? | A CSDD process is real only if a rule changes the next allowed action: blocks plan, changes task, appears in agent context, gates PR or requires an exception. | P15 “next action changed” invariant; avoid turning this into a generic process-methodology article. |
| `A7_observation_vs_evidence` | What makes an agent's claim acceptable to a human reviewer? | A compliance row is evidence only when tied to file/line/technique plus test, scanner, review decision, commit or explicit exception; otherwise it is only a trace of assertion. | Matrix sections and caveat table. |
| `A9_lifecycle_repair` | What becomes obsolete after a change is accepted? | Constitution amendments should trigger sync of templates, commands, context files, tasks, checks and matrices; otherwise future agents read stale authority. | `Что должно обновляться после слияния`. |
| `C5_theory_to_technical_atlas` | What belongs in a standalone technical-atlas article rather than the general theory? | This article holds source-specific facts, files, commands, matrices, caveats and image candidates while repeating only enough theory for local comprehension. | Contract section, source usage, image plan; avoid rebuilding A/B/C chapters. |
| `A10_mode_selection_map` | When should a team choose this heavier external structure instead of a lighter plan/chat/review loop? | Choose CSDD when local work can violate durable cross-feature rules, the agent must see selected policy, humans need traceable evidence, and синхронизация после слияния matters. | Final theory section and mode-selection note. |


## P17 terminology sync

- Теоретическая связь P09 теперь ссылается на `пакет конституционных ограничений`; старый гибридный термин не используется как текущий долг.
- Общая рамка SDLC с ИИ сохранена: терминология в публичном тексте переведена на русский, при этом имена артефактов (`Constitution`, `spec.md`, `plan.md`, `tasks.md`) оставлены точными.
- Смысловые back-links P16 не менялись.

## P18 — синхронизация терминологии

- Теоретические связи P16 не изменились.
- Публичный текст теперь использует русские объяснительные формы для обычных слов и оставляет английский только там, где это имя метода, файла, команды, принципа, точный указатель источника или устойчивое техническое обозначение.
- Это поддерживает границу C5: статья остаётся самостоятельной и читаемой, но не превращает companion-файлы в новый теоретический раздел.

## P19 — синхронизация с теорией

- Тезис A10 о выборе режима теперь отражён не только в финальной теоретической связке, но и в основном разделе `Когда CSDD оправдан`.
- Это не расширяет теорию: раздел переводит уже существующую границу в практический критерий для самостоятельного читателя.

## P20 — синхронизация с теорией

- Финальная теория больше не несёт основную нагрузку по A10/mode selection; этот критерий теперь находится в практическом разделе `Когда CSDD оправдан`.
- Связь с A7 уточнена редакторски: матрица связывает намерение со свидетельством, но сама не является достаточным свидетельством без теста, сканера, ревью, коммита или исключения.

## P21 — синхронизация с теорией

- Переименование `Что должно обновляться после слияния` усиливает связь с A9 lifecycle repair: акцент теперь на обязательной синхронизации зависимых артефактов, а не на расплывчатом «жить после».
- Теоретические тезисы не изменились.

## P22 — синхронизация с публичной структурой

- Первый экран теперь лучше соответствует concept-first entry: сначала проблема и reader question, затем визуальная карта CSDD.
- Теоретические связи не изменились; перестановка Figure 1 не меняет аргумент о Constitution как верхнем слое полномочий.


## P23 — синхронизация companion-файлов

- Заголовки и ссылки на текущую статью согласованы после P21/P22: `Когда CSDD оправдан`, `Что должно обновляться после слияния`, `Внешние изображения для asset-pass`.
- C5/A10 не имеют отдельного общего sync-долга; они остаются рамкой для конкретных boundary checks и mode-selection объяснения.
- `theory_links` остаётся картой вопросов, которые CSDD проясняет, а не вторым теоретическим эссе.

## P24 — синхронизация теоретических формулировок

- Финальная связь с общей теорией теперь говорит о `синхронизации после изменения правил`, а не о метафорическом «ремонте».
- Формулировка про единицу анализа очищена от псевдотермина `смысловая дельта`; смысл остался тем же: программное изменение должно пройти от намерения до результата и поддержки связанных артефактов.
- Back-links остаются вопросами к теории, а не новым самостоятельным теоретическим разделом.

## P25 — естественная правка финальной связки

- Финальная теория стала менее академичной: `теоретический вклад` заменён на прямое объяснение, что метод показывает артефакт с более высоким полномочием, чем локальная спецификация.
- Смысл связи с lifecycle, evidence and mode selection не изменился.

## P26 theory-link style sync

The final article section is now titled `Что CSDD добавляет к общей теории SDLC с ИИ`. The role is unchanged: CSDD remains a concrete case for durable policy above a feature, evidence-bearing traceability, context management and lifecycle synchronization after rule changes.
