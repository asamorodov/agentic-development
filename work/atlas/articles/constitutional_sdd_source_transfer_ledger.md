# constitutional_sdd — source transfer ledger

Статус: P26 guarded final style sync. Ledger синхронизирован с финальными заголовками и стилевыми правками; source decisions не менялись.

| Материал | Решение в P01 | Где в статье | Почему так | Долг / проверка |
|---|---|---|---|---|
| Marri CSDD framing | inserted | Ввод, reader question, workflow | Нужна главная ось статьи: Constitution над локальной фичей | Проверить последнюю arXiv версию перед финалом. |
| Constitution structure: ID, CWE, MUST/SHOULD/MAY, implementation pattern, rationale | inserted | `Что такое Constitution в CSDD` | Технический якорь, без которого Constitution выглядит лозунгом | Сверить формулировки с PDF. |
| 15 principles / 4 groups | inserted with caution | `Что такое Constitution в CSDD` | Даёт масштаб paper example | Не смешивать с broader repo Constitution. |
| Broader reference `.specify/memory/constitution.md` | inserted | Constitution, gates, lifecycle repair | Показывает governance and non-security breadth | Требуется comparison pass: compact article vs raw Constitution. |
| Banking `spec.md` | inserted | `Почему spec.md, plan.md и tasks.md не одно и то же` | Показывает, где security входит в feature spec | Нужна возможная поздняя точная сверка FR coverage. |
| Banking `plan.md` drift observation | inserted cautiously | Same section | Хороший risk anchor для weak `PASS` | Не утверждать defect без полного source-depth. |
| Banking `tasks.md` missing explicit `SEC-*` trace | inserted cautiously | Same section, typical failures | Показывает task-level weakening | Проверить, есть ли другие task/context files, компенсирующие это. |
| `CONSTITUTION_COMPLIANCE.md` auto-generated claim | inserted with open question | Compliance matrix | Центральный technical anchor | Найти/проверить генератор или пометить как manual/uncertain. |
| Compliance matrix examples | inserted | Compliance matrix | Показывает principle->file/line/technique | Позже сверить точные line ranges if article quotes them more strictly. |
| Two-week case and 16h/64h cost | inserted with caveat | Workflow | Показывает цену метода | Не использовать как universal productivity claim. |
| 73% metric and other Table 3 numbers | inserted with strong caution | Verification section | Needed but dangerous | Перед финалом держать рядом with threats to validity. |
| Context window selection 3–5 principles vs all 15 | inserted | Context files | Strong AI-SDLC lesson | Verify exact percentages from PDF/ar5iv. |
| `CLAUDE.md` as context file and placeholder risk | inserted | Context files | Shows context files as enforcement surface | Need inspect `.claude/commands` in later pass only if allowed. |
| Spec Kit command chain | inserted | Spec/plan/tasks, gates | Provides wider artifact machine | Freshness check needed. |
| `/speckit.analyze` read-only gate | inserted | Human gates | Strong pre-code check | Freshness check needed. |
| Issue #697 | inserted as public feedback | Human gates | Concrete gate failure example | Keep marked as issue, not official doctrine. |
| Issue #40 | inserted as public feedback | Typical failures | Concrete risk of unclear Constitution authorship | Keep marked as issue, not official doctrine. |
| Mad Devs threat model and PR-template | inserted | Matrix, context files, gates, runtime caveat | Provides operational detail absent from paper | Keep separate from Marri metrics. |
| DocGuard guard/trace/diagnose | inserted | Matrix, context files, extension trust | Tooling shape for traceability | Need code/license/release review before stronger claims. |
| Spec Kit Community Extensions warning | inserted | Typical failures | Trust boundary for community gates | Do not imply audit/endorsement. |
| Cisco Foundry priority rule | inserted | Foundry section, lifecycle repair | Strong neighbor example for Constitution authority | Keep separate from CSDD evidence. |
| Foundry evidence gate | inserted lightly | Foundry section and matrix analogy | Shows evidence quality and operator authority | Later pass can expand or move to theory links. |
| Project CodeGuard | deferred/context only | Not directly used except in source usage | Neighbor project, not core evidence for article | Revisit only if source-depth pass asks. |
| README architecture/auth/data-flow diagrams | deferred / rights hold | Not inline | License caveat prevents immediate insertion | Rights check required. |
| Figure 1 ar5iv | inserted as external placeholder | After intro | Key visual hierarchy | Download/rights/quality check. |
| Table 1 ar5iv | inserted as external placeholder | Compliance matrix | Key visual evidence surface | Download/rights/quality check. |
| Figure 2 ar5iv | deferred queue only | Bottom asset-pass list | Useful for metrics but not essential to P01 | Rights/readability check and decide inline. |
| PAPER.md Figure 4 | inserted as external placeholder | Workflow | Shows feedback loop | Check canonicality and rights. |
| Reconstructed diagrams from dossier | deferred | Image plan only | P01 already has three visual placeholders; synthetic diagrams can wait | Decide in visual pass. |

## P02 transfer decisions

| Материал | Решение в P02 | Где в статье | Почему так | Долг / проверка |
|---|---|---|---|---|
| Explicit article contract | inserted | `О чём говорит эта статья и что остаётся рядом` | Prevent generic security/governance overview | Keep contract near top through future edits. |
| Boundary with Spec Kit | inserted | Same section | CSDD uses repo workflow but adds policy authority | Do not expand into install/integration tutorial. |
| Boundary with SPDD | inserted | Same section | Both manage intent, but CSDD focuses on security/policy constraints above feature | Keep SPDD as neighbor, not source of CSDD claims. |
| Boundary with Kiro Specs | inserted | Same section | Product spec surface is not automatically constitutional layer | Freshness check for Kiro docs if details expand. |
| Boundary with ADR | inserted | Same section | ADR stores a decision; Constitution constrains many future actions | Later pass may add one short example if useful. |
| Boundary with TDAD/evidence | inserted | Same section | Compliance matrix can support evidence but is not evidence alone | Avoid conflating traceability with proof. |
| Boundary with PWG | inserted without new public citation | Same section | PWG stores work state; Constitution constrains work | Add PWG citation only if section grows. |
| Negative boundary against security manifesto/security documentation | inserted | Same section | Required by P02; protects article from generic governance | Maintain action-influence criterion. |

## P03 dossier inventory

Статус: инвентаризация по `CONSTITUTIONAL_SDD_DOSSIER.md` после P01/P02. Это не coverage matrix; цель — показать, где статья уже имеет рабочие опоры, где материал сознательно отложен и какие первоисточники надо открыть в следующих source-depth проходах.

### Перенесено и работает на reader question

| Зона досье | Статус | Где в статье | Комментарий |
|---|---|---|---|
| Центральная роль CSDD в AI SDLC | transferred | Intro, Reader question, Theory links | Статья держит CSDD как policy/Constitution layer над feature work. |
| Проблема prompt-level security requests: inconsistency, incompleteness, drift, unverifiability | transferred by synthesis | Intro, Reader question, Typical failures | Не перенесено как отдельный список, но встроено в объяснение потери правил между артефактами. |
| Minimal workflow: Constitution -> spec -> plan -> tasks -> generation -> matrix -> repair | transferred | Workflow, Spec/plan/tasks, Compliance matrix | Основная цепочка объяснена и технически закреплена файлами. |
| Two-week banking case and cost claims | transferred with caveat | Workflow | Использовано как case evidence, not universal claim. |
| Constitution fields and 15 principles | transferred | `Что такое Constitution в CSDD` | Даны ID/CWE/MUST/SHOULD/MAY/pattern/rationale and 15-principle scope. |
| Broader raw reference Constitution | transferred | Constitution, Human gates, Lifecycle repair | Использовано для governance and lifecycle repair. |
| `spec.md`, `plan.md`, `tasks.md` distinction | transferred | `Почему spec.md, plan.md и tasks.md не одно и то же` | Статья отдельно показывает слабое место task-level traceability. |
| Compliance matrix examples | transferred | Compliance matrix | Есть principle/CWE/file/technique examples and `CONSTITUTION_COMPLIANCE.md` caveat. |
| Mad Devs practical layer | transferred | Compliance matrix, Context files, Human gates, Limits | Использован как operational guide, not metric replication. |
| DocGuard as adjacent enforcement/tracing tool | transferred | Compliance matrix, Context files, Typical failures | Used as tooling shape, with community-extension trust caveat. |
| Spec Kit command/template mechanics | transferred selectively | Spec/plan/tasks, Human gates, Typical failures | Команды используются только where they explain CSDD gates and sync. |
| Issues #697 and #40 | transferred selectively | Human gates, Typical failures | Marked as public-feedback examples. |
| Foundry Constitution priority/evidence/lifecycle | transferred selectively | Foundry section, Lifecycle repair | Kept as neighbor source and not mixed with Marri metrics. |
| Strengths and risks | transferred by synthesis | What CSDD checks, Typical failures, Lifecycle repair | Основные risks covered: theater, vague rules, context overload, task weakening, prompt injection, template drift, client blind spot, n=1, runtime boundary. |
| Dossier image candidates | transferred into visual plan | Article placeholders, image_plan, external_image_queue | All candidates received disposition. |

### Сознательно отложено или не перенесено в основной текст

| Материал досье | Решение | Причина |
|---|---|---|
| Подробный статус GitHub repo: 0 issues, 0 PR, 0 releases, 6 commits, 0 stars, 1 fork | deferred to source-depth/source note | Useful for evidence-strength caveat, but would interrupt main mechanism in P01/P02. |
| Полное перечисление README security features | partially transferred | Article uses selected features only; full list belongs in reference implementation or Fieldbook section if needed. |
| Full Foundry role taxonomy | deferred | Could turn article into Foundry article. Only priority/evidence/lifecycle mechanics transferred. |
| Project CodeGuard details | deferred | Neighbor context; not needed for central CSDD reader question unless a future Foundry/neighbor section expands. |
| DocGuard PyPI and release metadata | deferred | Needed for trust/freshness pass, not main article mechanism. |
| Full Spec Kit workflow/presets/integrations | rejected for article body unless needed | P02 boundary says article must not become Spec Kit tutorial. |
| Handbook/Fieldbook checklists from dossier | deferred | Useful for future practical guide; article currently needs mechanism and boundaries. |
| Future work: automatic Constitution generation from PCI-DSS/HIPAA, real-time IDE validation, inheritance between projects | deferred | Could become closing paragraph later, but not article-critical in P03. |
| Search queries from dossier | not transferred | Operational notes only. |

### Первoисточники, которые нужно открыть / сверить в следующих проходах

| Source to open | Why |
|---|---|
| arXiv abstract and PDF for `2602.02584` | Verify latest version, exact title, DOI/status, tables, threats to validity, future work. |
| ar5iv full text | Verify Figure 1, Table 1, Figure 2, sections 5–6 and exact numbers. |
| `banking-ms-by-constitution` repo page and branch | Verify current commits/issues/releases/license and whether diagrams can be used. |
| `.specify/memory/constitution.md` | Compare broader raw Constitution against paper's compact 15 principles. |
| `CONSTITUTION_COMPLIANCE.md` | Verify `auto-generated from codebase analysis` and locate generation mechanism if any. |
| `spec.md`, `plan.md`, `tasks.md`, `CLAUDE.md`, `.claude/commands` if allowed later | Verify task-level traceability and whether other context files compensate for weak task references. |
| Spec Kit command/templates | Verify current behavior of `/speckit.constitution`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, hooks and Sync Impact Report. |
| Mad Devs guide | Verify current date/content and exact PR-template/traceability guidance. |
| DocGuard repo/PyPI/community extension listing | Verify license, release rhythm, GitHub Action, write permissions, and trust boundary. |
| Foundry README/spec/constitution | Verify current status, license, contribution/security docs before publication if the Foundry neighbor section grows. CodeGuard is not a current article blocker. |

### Возможные technical-anchor gaps

1. **Matrix generation gap.** Article currently says the `CONSTITUTION_COMPLIANCE.md` automation claim remains open. A later pass should find whether a concrete command/tool exists or soften this further.
2. **Task-level traceability gap.** Article observes weak explicit `SEC-*` references in `tasks.md`; later pass should check `.claude/commands` and other context files before making the claim stronger.
3. **Client security gap.** Article uses JWT-in-`localStorage` as a caution. Later pass should verify exact README wording, threat model relevance and whether matrix covers frontend decisions.
4. **Version/freshness gap.** Spec Kit, DocGuard, Kiro and related tools move quickly; current article uses them as boundary/supporting examples and should not include more command detail until fresh checked.
5. **Visual rights gap.** Figure placeholders are correct for P03, but no external image can become a real `<img>` without rights/download/quality check.
6. **Evidence distinction gap.** P02 added the matrix/evidence boundary; later passes should preserve it if adding more examples of tests/scanners/review.

### P03 main-text decision

No article-critical omission required immediate main-text insertion in P03. The primary article already contains the central mechanism, boundaries, technical anchors and most critical caveats. Missing materials are better handled by later source-depth, visual, Handbook/Fieldbook or companion passes.

## P04 source-depth 1 — paper framing vs repository workflow

| Material / claim | P04 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Academic paper as method/evaluation frame | clarified | `Paper framing и рабочая поверхность репозитория` | Prevents treating figures/metrics as executable workflow | Verify PDF/ar5iv exact claims in later source-depth. |
| Reference repo as executable/inspectable surface | clarified | Same section | Shows what agent/package can actually read/check/update | Later source-depth may open repo files directly if allowed. |
| Figure 1, Table 3, 73% metric | constrained | Same section | These are explanatory/evaluative, not gates | Keep metric caveats visible. |
| `.specify/memory/constitution.md`, `spec.md`, `plan.md`, `tasks.md`, `CLAUDE.md`, `CONSTITUTION_COMPLIANCE.md` | strengthened as workflow anchors | Same section | These are concrete surfaces for agent/package action | Need direct source verification for exact state. |
| Agent action boundary | added | Same section | Agent can check traces and consistency; cannot execute academic claims | Later pass can add a checklist if useful. |
| Demo-repo overfit risk | added | Same section | Prevents reducing CSDD to one repository state | Keep article general but sourced. |

## P05 source-depth 2 — constitution/spec/plan/tasks/context files

| Artifact material | P05 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Constitution fields and state | strengthened | `Карта артефактов` | Makes Constitution executable/inspectable rather than conceptual | Verify exact raw Constitution structure later. |
| `spec.md` role and state | strengthened | Same section | Shows where feature intent and security requirements live | Later source-depth should inspect exact security references. |
| `plan.md` role and Constitution Check | strengthened | Same section | Separates design constraint from declarative PASS | Check current plan downstream artifacts if allowed. |
| `tasks.md` as agent work queue | strengthened | Same section | Shows task-level traceability risk and expected state | Verify whether context/commands compensate for missing `SEC-*` refs. |
| Context files (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, Copilot instructions, `.claude/commands`) | strengthened | Same section | Explains where agent-visible state actually lives | Only `CLAUDE.md` is confirmed from current repo; other paths are general context surfaces from supporting sources. |
| Generated code/tests | added | Same section | Clarifies expected implementation/evidence outputs | Avoid claiming specific test suite until direct source check. |
| `CONSTITUTION_COMPLIANCE.md` / traceability matrix expected fields | strengthened | Same section | Connects compliance matrix to evidence/status/owner | Automation remains unresolved. |
| Override/exception record | added from Mad Devs/dossier logic | Same section | Makes policy override visible rather than informal bypass | Need primary-source details if article later gives template. |

## P06 source-depth 3 — compliance matrix and traceability as working constraint

| Material / claim | P06 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Matrix as process constraint | strengthened | `Как матрица ограничивает работу до слияния` | Shows that traceability must affect plan/tasks/review rather than remain an end-of-project report | Later pass should verify exact matrix fields and whether a generator exists. |
| `plan.md` pressure | added | Same section | `Constitution Check PASS` must be supported by downstream artifacts, decisions or exceptions | Re-check plan artifacts when direct primary-source pass is allowed. |
| `tasks.md` pressure | added | Same section | Agent-executable tasks need `SEC-*`, CWE/control, requirement or check linkage to avoid trace loss | Check `.claude/commands` and context files before making stronger claim. |
| PR/review pressure | added | Same section | Matrix becomes real when tied to PR-template, tests, scanners, owner review, commit links or explicit `N/A` | Keep Mad Devs as operational guidance, not empirical CSDD replication. |
| Reverse trace | added | Same section | Reviewer must be able to ask from code back to requirement/task/Constitution | Tooling remains open; DocGuard is only a neighbor example. |
| Constitution amendment pressure | added | Same section | Matrix must be recomputed after rule changes; gaps should block movement | Keep Foundry as neighbor example with stricter governance. |
| Formal-table failure mode | clarified | Same section | A green matrix without evidence or process effect is only intention/summary | Preserve matrix/evidence distinction from P02. |

## P07 source-depth 4 — boundary with Spec Kit, ADR and security documentation

| Material / claim | P07 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| CSDD over/near specification workflow | clarified | `Как CSDD ложится поверх спецификационного процесса` | Separates artifact workflow from higher security/governance authority | Keep final article from becoming a Spec Kit tutorial. |
| Spec Kit relation | clarified | Same section | Spec Kit can host the artifact chain, but does not itself guarantee CSDD | Cross-check with future Spec Kit article. |
| Security documentation relation | clarified | Same section | Security docs count only when they alter agent context, gates, traceability or review | Could become a Handbook criterion later. |
| ADR relation | clarified | Same section | ADR may justify an implementation decision but cannot replace recurring policy constraints | Cross-check with future ADR article. |
| `constitution.md` nominalism risk | added | Same section | A file name alone does not create CSDD | Preserve this criterion in style passes. |

## P08 source-depth 5 — failures, caveats and anti-summary

| Limit / caveat | P08 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Constitution as declaration | added | `Где CSDD может дать ложную уверенность` | Prevents “file named constitution.md” from counting as CSDD | Preserve concrete-principle requirement in style pass. |
| Compliance matrix as overconfidence | added | Same section | Separates green status from reproducible evidence | Verify exact evidence examples and matrix fields. |
| Policy not connected to action | added | Same section | Security documentation must reach artifacts/gates/context/review | Could become a reusable atlas criterion. |
| Missing evidence / generator uncertainty | added | Same section | Avoids treating `CONSTITUTION_COMPLIANCE.md` as proven automated enforcement | Find generator or keep open debt. |
| Human security responsibility | added | Same section | Makes governance, exception handling and residual risk human-owned | Preserve human-gate language in final edits. |

## P09 free expansion 1 — selected gap: task-sized Constitution context

| Editorial judgment | Added to main text | Source basis | Remaining debt |
|---|---|---|---|
| The article explained context files but not how to choose the Constitution subset an agent should see. | New section `Что дать агенту из Constitution для одной задачи`. | Marri context-selection result: full Constitution 78%, relevant 3–5 principles 96%, hierarchical 5–8 principles 91%; matrix examples and reference compliance report for implementation/evidence fields. | Verify exact experiment wording in PDF; public terminology resolved in P17/P18 as `пакет конституционных ограничений`. |
| The missing mechanism was task-local authority transfer. | Added fields: task scope, selected principles, forbidden shortcuts, required implementation pattern, evidence expectation. | Derived from dossier facts about Constitution fields, compliance matrix and context-selection trade-off. | Later style pass should decide whether to translate or retain `packet` terminology. |

## P10 free expansion 2 — selected gap: reader path through one feature

| Editorial judgment | Added to main text | Source basis | Remaining debt |
|---|---|---|---|
| The article had strong parts but needed a single reader path through the mechanism. | New section `Сквозной пример: перевод средств как цепочка артефактов`. | Marri qualitative transfer-endpoint example; reference `spec.md`, `plan.md`, `tasks.md`; existing Figure 4 feedback-loop idea. | Verify transfer example and exact artifacts against PDF/raw files in final source pass. |
| CSDD/SDD distinction needed a concrete feature-level contrast. | Added paragraph: SDD decomposes a feature; CSDD asks which constitutional constraints survive that decomposition and how evidence closes them. | C5 atlas model: article should explain mechanism, not just list files/commands. | Later style pass can shorten if section becomes too explanatory, but keep the bridge. |

## P11 visual asset pass 1 — local assets

| Local asset | Decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| `content/assets/theory-images/fowler-sdd-overview.png` | inserted as local image asset | `Как CSDD ложится поверх спецификационного процесса` | It illustrates generic SDD context — memory bank/specs around an agent — exactly where the article distinguishes SDD workflow from CSDD's added Constitution layer | Keep caption boundary explicit; do not let this image imply Fowler is a CSDD source. |
| Other local assets in index | not inserted | image plan | They concern SPDD, harnesses, agents, observability, worktrees or story screenshots rather than Constitutional SDD's priority visuals | No action unless a later article-specific pass expands scope. |

## P12 visual asset pass 2 — external real candidates

| Candidate | Decision | Main text / queue action | Reason | Follow-up |
|---|---|---|---|---|
| Marri Figure 1 | retained inline placeholder, caption normalized | `fig-csdd-architecture` | High-priority source diagram for CSDD hierarchy | Download/rights/quality/PDF check. |
| Marri Table 1 | retained inline placeholder, caption normalized | `fig-csdd-compliance-matrix` | High-priority visual/table for traceability matrix | Decide image vs redrawn table after rights/readability check. |
| `PAPER.md` Figure 4 | retained inline placeholder, caption normalized | `fig-csdd-three-phase-loop` | Shows feedback loop from compliance check to spec/generation | Check canonicality and rights. |
| Marri Figure 2 | queue only | `queued-csdd-cwe-effort-figure` | Metrics figure could over-center quantitative claim | Use only if metrics section expands with caveats. |
| Reference README diagrams | rights hold / queue only | `queued-banking-readme-diagrams` | Useful for Fieldbook/reference implementation, but rights unclear | Do not inline until license/rights resolved. |
| Mad Devs, DocGuard, Foundry workflow/evidence visuals | deferred as original synthetic ideas | image plan only | Better to redraw from facts than copy source graphics | Consider in later synthetic visual pass. |

## P13 visual asset pass 3 — synthetic figures

| Synthetic idea | Decision | Reason | Follow-up |
|---|---|---|---|
| `Constitution -> selected 3–5 principles -> task -> evidence` | deferred | The `пакет конституционных ограничений` table already carries the mechanism; a figure may be useful later but is not unusually necessary now. | Reconsider only if visual density is still low after real source figures are localized. |
| `one feature trace: spec -> plan -> tasks -> packet -> code -> matrix -> repair` | deferred | The transfer-endpoint walkthrough plus `PAPER.md` Figure 4 candidate already cover the reader path. | Could become an original sidebar/diagram in a later design pass. |
| `CSDD layer over generic SDD` | not added | P11 inserted a local Fowler SDD context image and P07 added a layer table. | Do not duplicate unless the section is redesigned. |

## P14 concept reinforcement 1 — standalone article

| Reinforcement | Article action | Source basis | Why | Remaining debt |
|---|---|---|---|---|
| Standalone vocabulary | Added `Минимальный словарь этой статьи` after reader question | ar5iv artifact chain, reference Constitution, compliance report; C5 standalone article contract | Lets a direct reader understand Constitution/spec/plan/tasks/context/matrix without assembling theory chapters | Later style pass can decide whether to keep as separate section or fold into intro. |
| Controlled theory repetition | Added short concept summary: security moves from chat memory into artifacts with authority, agent visibility and trace | C5 concept-first model | Provides local minimum theory without copying general framework | Avoid expanding into full A/C theory. |

## P15 concept reinforcement — embedded failure modes

| Material / claim | P15 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Standalone `Типовые сбои` catalog | Removed as separate section and distributed through the mechanism | Constitution, workflow, `spec/plan/tasks`, matrix, context files, gates, caveats | The worksheet required limitations to be embedded in explanation rather than collected as an error catalog | Re-check in style pass that no new generic failure list appears. |
| Constitution as declaration / copied Constitution | Embedded in `Что такое Constitution в CSDD` | Constitution section | Keeps the risk next to the definition of enforceable principles | Verify issue #40 status/comments before final publication. |
| Policy not connected to next action | Embedded as “what changed because of the rule?” invariant | Workflow section | Makes the mechanism testable at every handoff | Preserve this as a central diagnostic phrase. |
| Model optimizes checklist wording | Added to `spec/plan/tasks` and caveat table | Artifact transition and limits sections | Directly addresses `PASS`/`MUST`/`SEC-*` words without changed behavior | Later language pass can polish English terms without weakening the warning. |
| Traceability without evidence | Strengthened in matrix section and caveat table | Matrix sections | Separates route-of-assertion from force-of-check | Confirm matrix generator/reproducibility. |
| Client/runtime blind spot | Moved from removed failure catalog into matrix boundary paragraph | Matrix-as-constraint section | Shows coverage boundary without overclaiming a vulnerability | Needs separate client-security review. |
| Prompt injection / context-file integrity | Embedded in context files mechanism | Context files section | Treats context artifacts as part of the enforcement channel | Verify exact Marri wording in PDF. |
| Community extension trust | Embedded in human gates | Human gates section | A blocking guard is itself part of the trust boundary | Re-check catalog/extension status. |

## P16 theory-link transfer

| Theory material | P16 decision | Article / companion location | Why | Boundary |
|---|---|---|---|---|
| Software change as unit of analysis | Condensed into final theory section | `Что CSDD добавляет к общей теории SDLC с ИИ` | Grounds CSDD in lifecycle without restating 00 | No full spine recap. |
| Specification layer question | Mapped to CSDD as higher-authority Constitution | `theory_links` and final section | Shows CSDD's distinct governable object | Avoid duplicating A3 comparison table. |
| Process vs imitation | Transferred as “rule changes next action” | Final section and P15/P16 theory notes | Connects mechanism to process theory | Keep source/tool details local to CSDD. |
| Observation vs evidence | Transferred as matrix row must support human risk acceptance | Final section and matrix sections | Keeps compliance matrix from being overclaimed | Do not convert article into evidence-layer survey. |
| Lifecycle repair | Transferred as Constitution amendment synchronization | `Что должно обновляться после слияния` and final section | Connects CSDD to синхронизацию после слияния | Keep repair list scoped. |
| Atlas boundary | Transferred into theory_links only | Companion file | Prevents article from rewriting general theory | Public article remains standalone but narrow. |
| Mode selection | Transferred as when to choose CSDD | Final section and theory_links | Helps reader understand when CSDD is justified | Do not imply every project needs CSDD. |


## P17 transfer note — language normalization

| Item | P17 action | Transfer impact |
|---|---|---|
| English glue in public prose | Переведены случайные англоязычные связки: `AI-assisted code generation`, `prompt`, `endpoint`, `runtime`, `traceability`, `audit table`, `compliance pass`, `download/rights/quality check required`. | Смысл и источники не перемещались; улучшена читаемость русского пользовательского текста. |
| Старый гибридный термин для task-local packet | Публичный термин заменён на `пакет конституционных ограничений`. | Сохранён P09-механизм task-local selection; убран лишний гибридный термин. |
| Visual candidate statuses | Статусы и назначение внешних кандидатов описаны по-русски. | Нет новых изображений, отказов или загрузок; решения P12/P13 сохранены. |
| Allowed English | Оставлены имена источников, проектов, файлов, команд, source labels, exact principles and code-like relation strings where exact form matters. | Соответствует языковым правилам: не считать source labels новой фактурой. |

## P18 — второй языковой проход

| Элемент | Действие P18 | Влияние на перенос |
|---|---|---|
| Подписи и нижняя очередь изображений | Повторно вычитаны подписи и очередь внешних изображений; русские пояснения сохранены, source labels в поле источника оставлены точными. | Визуальные решения не изменились; новые изображения, отказы или загрузки не добавлены. |
| Подписи ссылок и обычный английский | Переведены непредметные английские подписи ссылок и обычные слова вроде `diff`, `pull request`, `guard-инструмент`. | Источники, факты, ограничения и ссылки остались теми же. |
| Таблицы | Проверены таблицы артефактов, матрицы и рисков; внесены точечные правки падежей и русской связности. | Табличная структура и содержательные критерии сохранены. |

## P19 — редакторский проход 1

| Найденная проблема | Исправление в статье | Влияние на перенос |
|---|---|---|
| Статья давала много механики, но ранний критерий узнавания CSDD был размазан между несколькими разделами. | После вводного ответа добавлена короткая проверка: взять одно правило Constitution и пройти его через `spec.md`, `plan.md`, задачу агента, код и свидетельство. | Фактура не добавлена; существующий инвариант «правило меняет следующий шаг» стал видимым раньше. |
| Режим применения был в основном спрятан в финальной теоретической связке. | Добавлен раздел `Когда CSDD оправдан` перед Foundry: когда долговечные правила политики стоят расходов на документы, гейты и синхронизацию, а когда достаточно обычного SDD, тестов и ревью. | Переносит тезис о выборе режима из companion/финала в основной standalone-текст без новых источников. |
| Foundry и материал о жизненном цикле могли восприниматься как продолжение основного банковского кейса без практического фильтра. | Новый раздел отделяет критерий применения от соседнего примера Foundry. | Граница Marri case vs Foundry neighbor сохранена. |

## P20 — редакторский проход 2

| Найденная проблема | Исправление в статье | Влияние на перенос |
|---|---|---|
| Заголовок `Матрица соответствия: где намерение становится свидетельством` мог противоречить собственному ограничению статьи: матрица даёт трассу, но свидетельство требует проверки. | Заголовок заменён на `Матрица соответствия: от правила к свидетельству`. | Уточнён тезис о матрице без изменения источников и примеров. |
| В публичном тексте оставался след внутренней редакторской истории: `практический пробел в первом черновике`. | Формулировка заменена на нейтральную: слабое место часто в выборе части Constitution для конкретной задачи агента. | Убрана служебная мета-рамка, фактура про 78/96/91% сохранена. |
| Финальная теоретическая связь повторяла раздел `Когда CSDD оправдан`. | Последний теоретический абзац сфокусирован на ремонте после изменения Constitution, а критерий применимости остаётся в отдельном практическом разделе. | Дублирование уменьшено; тезис A10 о выборе режима не потерян. |

## P21 — редакторский проход 3

| Найденная проблема | Исправление в статье | Влияние на перенос |
|---|---|---|
| Несколько заголовков были точными по смыслу, но звучали тяжело или неестественно для standalone-статьи. | `Сквозной пример` переименован в `перевод средств как цепочка артефактов`, `Человеческие гейты` — в `Человеческие контрольные точки`, `Что должно жить после слияния` — в `Что должно обновляться после слияния`. | Навигация стала яснее; источники, факты и порядок аргумента не изменились. |
| Companion-ссылки на старые заголовки могли устареть. | Обновлены ссылки в transfer ledger и theory links на новое название раздела о синхронизации после слияния. | Внутренняя трасса пакета снова совпадает с публичной структурой статьи. |

## P22 — public/article structure and entry sequence

| Найденная проблема | Исправление в статье | Влияние на перенос |
|---|---|---|
| Первый экран слишком рано показывал внешний visual placeholder до явного reader question. | `fig-csdd-architecture` перенесён после раздела `О чём эта статья` и короткой проверки CSDD. | Источник и решение по изображению не изменились; поменялось место в публичной последовательности. |
| Подписи Figure 1 и Figure 4 звучали частично как редакторское указание (`в статье`, `для этой статьи`). | Подписи переписаны как публичные объяснения: Figure 1 даёт карту полномочий, Figure 4 показывает петлю ремонта. | Caption смысл сохранён, служебный тон убран. |
| Нижний asset-pass раздел имел более общий заголовок. | Заголовок заменён на `Внешние изображения для asset-pass`, как требует структурный проход. | Очередь и статусы не изменились. |


## P23 companion sync

- Ledger сохранён как журнал решений, а не как тотальная coverage matrix по досье.
- Удалены или переоформлены устаревшие долги: старый гибридный packet-термин, общий C5/A10-sync label и CodeGuard-as-blocker.
- Актуальные нерешённые вопросы остаются конкретными: freshness/PDF checks, generator provenance, visual rights/readability, client/runtime coverage and traceability checks.

## P24 style-defect sync

- Решения по переносу источников не менялись: pass был стилевым, а не source-depth.
- Ledger обновил текущие заголовки и термины: `Артефактная карта` → `Карта артефактов`, matrix process section → `Как матрица ограничивает работу до слияния`, lifecycle repair → синхронизация после изменения правил.
- Фактура Marri/repo/Mad Devs/DocGuard/Foundry сохранена; новых coverage obligations не добавлено.

## P25 selective natural rewrite sync

- Source transfer decisions не изменились.
- Текущая статья стала естественнее в нескольких местах: reader answer, figure captions, PWG boundary, risk table, Foundry boundary and final theory section.
- Ledger не превращён в список всех стилевых правок; он фиксирует только то, что фактура и границы источников сохранены.

## P26 guarded final style ledger sync

| Material / claim | P26 decision | Article location | Why | Follow-up |
|---|---|---|---|---|
| Public headings for article contract, CSDD-over-SDD layer, Constitution, matrix, context package, limits, Foundry and final theory | renamed for human technical style | Current section headings | Improves navigation without changing source transfer decisions | Future edits should use current headings, not P24/P25 transitional names. |
| Heavy formulas around authority/enforcement/trace | rewritten as priority, link to checks, visible trace/evidence | Intro, layer section, context files, Foundry, final theory | Removes pseudo-term drift while preserving claim that Constitution has higher priority than feature artifacts | Keep source-specific labels and quoted Foundry principles intact. |
| Figure 1 and Figure 4 captions | style-tightened only | Inline figure placeholders | Avoids over-metaphorical wording while preserving visual intent | Rights/download/PDF checks remain open. |
