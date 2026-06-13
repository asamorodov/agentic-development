# BMAD Method — source transfer ledger

Статус: P26 завершил guarded final style pass; source-transfer decisions сохранены, финальная форма синхронизирована.

| Материал / источник | Решение P01 | Где в статье | Причина | Долг |
| --- | --- | --- | --- | --- |
| BMAD as BMM inside broader BMad Ecosystem; modules boundary | Transferred | Intro | Нужна граница: TEA и другие modules не являются обязательным ядром BMAD-проекта. | Проверить текущий status modules перед финалом. |
| Artifact-first framing: workflow documents inform next stage | Expanded in P10 | Intro; «Почему BMAD вообще нужен»; «Инвариант BMAD»; «Главная цепочка» | Центральная ось статьи; P10 turns it into a reader-path invariant. | Later structure pass should ensure the invariant does not duplicate the intro. |
| Installation command and `_bmad/` / `_bmad-output/` tree | Transferred | «Установка: где в репозитории живёт BMAD» | Показывает, что BMAD живёт в репозитории как files/config/artifacts. | Проверить current install output/version. |
| Manifest / `--pin` reproducibility / config evolution | Transferred | Installation caveats; failure modes | Важная source-specific оговорка о быстром изменении инструментов. | Нужна свежая проверка release docs. |
| Four phases and artifact chain | Transferred | «Главная цепочка» | Основной механизм статьи. | В future pass добавить больше точной phase-specific mechanics при необходимости. |
| PRD `Create` / `Update` / `Validate`; PRD shim v6.7 | Transferred | «Главная цепочка» | Показывает версионный конфликт и функцию PRD gate. | Проверить current v6/v7 names. |
| `bmad-spec` and `SPEC.md` compression | Transferred | «Главная цепочка» | Важен как короткий contract layer. | Может получить отдельную визуальную схему позже. |
| Roles Mary/John/Sally/Winston/Amelia and specialized agents | Transferred | «Роли как распределение суждения» | Нужны для reader question, но не как главный тезис. | Не раздувать в каталог персон. |
| `bmad-help` navigation mechanism | Transferred | Roles section | Показывает navigation over artifact state. | Проверить current help CSV/config paths. |
| Quick Flow / full BMAD / Enterprise modes | Transferred | «Три режима глубины» | Нужна граница достаточной process depth. | Синхронизировать с A10/P02 contract. |
| Quick Fixes / `bmad-quick-dev` | Expanded in P09 | Quick Flow section; failure modes | Показывает, что Quick Flow тоже artifact-bearing: short spec, diff, tests, local commit, `deferred-work.md`, layer-aware repair. | Проверить current Quick Dev outputs and exact deferred-work behavior. |
| UX condition and v6.8 `DESIGN.md`/`EXPERIENCE.md` | Transferred | Full BMAD mode | Technical anchor for UX handoff. | Проверить текущие docs/release. |
| Solutioning / Preventing Agent Conflicts | Transferred | Full BMAD mode; risks | Объясняет, зачем architecture предшествует stories. | Может быть усилено конкретным example в later source-depth. |
| `project-context.md` | Transferred | Dedicated section | Central technical anchor for project-specific rules. | Future pass: add minimal example/template if useful. |
| Established project cleanup | Transferred | project-context and brownfield sections | Важный failure mode: old artifacts as false context. | Future pass: link to handbook route. |
| `bmad-create-story` details | Transferred | Story section | Central implementation context contract. | Future pass: add exact story fields/checklist excerpt if allowed. |
| `bmad-dev-story` exact order and allowed story-file updates | Transferred | Story section | Shows disciplined implementation and limited mutation of story file. | Verify current allowed fields. |
| `sprint-status.yaml` statuses and `bmad-sprint-status` routing | Transferred | Sprint status section | Shows state machine between agents/human. | Future pass: decide if synthetic figure remains. |
| Readiness gate PASS/CONCERNS/FAIL | Transferred | Gates section | Human stop/repair point before implementation. | Add more detail if source-depth pass opens readiness docs. |
| Manual `review` → `done` join | Transferred | Gates/status sections | Shows human authority remains outside agent execution. | None for P01. |
| Code review adversarial layers | Transferred | Review section | Shows review as workflow, not casual second agent. | Future pass: consider whether layer labels should remain English. |
| Checkpoint Preview | Transferred | Review section | Useful for autonomous Quick Dev human review. | Maybe move to Fieldbook route later. |
| Built-in QA vs TEA | Transferred | Review/quality and Enterprise sections | Prevents false equivalence between generated tests and full quality governance. | Future pass: create QA/TEA boundary visual or defer. |
| Correct Course | Transferred | Dedicated section | Shows repair of planning artifacts during sprint. | Future pass: add impact-analysis structure if helpful. |
| Brownfield `bmad-document-project` | Transferred | Brownfield section | Important source-depth material: scan state, generated docs, validation. | Could use separate brownfield visual in later visual pass. |
| Documentation requirements CSV and deep-dive | Transferred | Brownfield section | Concrete technical anchors preventing generic prose. | Verify current CSV row/columns in future source check. |
| Investigation / grades / confidence | Transferred | Investigation section | Shows evidence discipline and diagnostic boundary. | Decide later if too detailed for method article. |
| Retrospective | Transferred | Investigation/retrospective section | Shows feedback into next work. | Future pass: connect more explicitly to lifecycle repair. |
| BMAD vs Gas Town / PWG boundary | Transferred | Theory and failure-mode sections | Protects article boundary and C5 map. | No Gas Town dossier opened in P01; keep comparison high-level only. |
| Community complaints / token cost signals | Deferred | Not in article except general failure-mode note on overhead | Dossier says weak/anecdotal; P01 should not use as fact. | Future source pass may examine external reports if allowed. |
| Issue #1629, #511, #813, Atlassian Rovo thread | Deferred | Not in article | Discussion/issue artifacts require careful freshness/source evaluation. | Future source-depth/free material pass. |
| External evaluation by Ran the Builder | Deferred | Not in article | Secondary evaluation; not needed for primary conceptual draft. | Possible adoption friction pass if allowed. |


## P02 transfer decisions

| Материал / источник | Решение P02 | Где в статье | Причина | Долг |
| --- | --- | --- | --- | --- |
| Article contract: BMAD as artifact-first SDLC profile | Transferred | New section «Контракт статьи» | Makes reader question enforceable and prevents persona/command catalog drift. | Recheck in editorial pass after source-depth additions. |
| Lifecycle-function inclusion rule | Transferred | «Контракт статьи» | P02 required every BMAD detail to create next input, narrow context, record state, create human decision point, produce evidence or repair path. | Use as audit criterion in later passes. |
| BMAD ≠ GSD | Transferred | «Контракт статьи»; theory section | Protects BMAD article from becoming GSD runtime/process-supervision article. | Fresh source check for current Open GSD docs/version before publication. |
| BMAD ≠ PWG / Beads | Transferred | «Контракт статьи»; theory section | Separates `sprint-status.yaml` from durable work graph semantics. | Future PWG article should own the full graph vocabulary. |
| BMAD ≠ Gas Town | Transferred | «Контракт статьи»; theory section | Separates methodology/process profile from operating environment and durable orchestration layer. | Needs Gas Town article/source sync later. |
| BMAD ≠ Spec Kit/Kiro/SPDD/TDAD | Transferred | «Контракт статьи»; theory section | Prevents BMAD from absorbing specification/test-first methods. | TDAD has no dossier in P02 allowed inputs; keep as boundary placeholder only. |
| ADR stores decisions, not whole execution method | Transferred | «Контракт статьи»; theory section | Keeps ADR inside architecture memory instead of letting ADR replace BMAD lifecycle. | Later ADR article can own agentic ADR details. |
| Negative boundary: not personas/commands/ecosystem overview/generic SDLC | Transferred | «Контракт статьи» | Explicit anti-degradation guard for future passes. | Continue checking after each expansion. |
| C5/A10 read-only context | Recorded | Companion files only | P02 says not to create generic sync-pending debts. | Only concrete inconsistencies should be logged later. |


## P03 dossier inventory

P03 checked `BMAD_METHOD_DOSSIER.md` against the current article, transfer ledger and image plan. This is not a total coverage matrix; it records only material useful for protecting the article.

| Dossier area | Inventory decision | Article impact | Source-depth need |
| --- | --- | --- | --- |
| Core role in AI-agent SDLC; BMM inside BMad Ecosystem | Already transferred | Intro and contract section keep BMAD as BMM/profile rather than whole ecosystem. | Fresh modules/core boundary check before final. |
| Installation and filesystem frame | Mostly transferred | Article has install command, `_bmad/`, `_bmad-output/`, manifest/pinning/config evolution. | Low-level `--set`, `GITHUB_TOKEN`, CI/API-rate details deferred unless installation section becomes handbook-like. |
| Planning modes | Transferred | Quick Flow/full BMAD/Enterprise used to show process-depth selection. | Need current docs if exact story-count ranges or mode labels change. |
| Four workflow phases | Transferred at concept level | Article has analysis → planning → UX/architecture → implementation chain. | Phase-1 artifact details (`brainstorming-report`, PRFAQ variants) are enough for article; no need to expand into workflow catalog now. |
| Artifact cascade and context | Transferred | Central figure and sections show PRD/architecture/story/status/review/repair handoff. | None for P03. |
| `project-context.md` | Transferred | Dedicated section explains local project rules and stale-context risk. | Could add minimal template/example later, but not article-critical now. |
| Core tools / `bmad-help` / `bmad-spec` | Partially transferred | `bmad-help` and `bmad-spec` included because they affect navigation/compression of context. | Party Mode, sharding/indexing helpers and broad core-tools catalog deferred. |
| Roles and personas | Transferred with guardrail | Article names major roles but says roles matter only through artifacts and judgment. | Do not add persona catalog unless a later pass finds missing lifecycle function. |
| Human decisions and gates | Transferred | Article covers mode choice, PRD intent, readiness gate, UX inclusion, manual `review`→`done`, release gate. | Exact readiness report structure can be a future source-depth target. |
| Quality / code review / checkpoint preview / testing / TEA | Transferred selectively | Article separates review, checkpoint preview, built-in QA and TEA. | More exact QA/TEA workflow details deferred to avoid overweighting Enterprise. |
| Sprint status | Transferred | Synthetic state-machine figure and status-routing section. | Exact YAML schema and legacy normalization map can be checked later if article becomes more technical. |
| Story context | Transferred strongly | Article treats story as primary implementation contract and includes create/dev story mechanics. | Exact checklist fields and story template anatomy remain future technical anchors. |
| Post-implementation lifecycle | Transferred | Correct Course, investigation and retrospective present as repair/evidence loops. | Sprint Change Proposal anatomy, investigation case-file fields and retrospective report sections can be source-depth additions. |
| Brownfield `bmad-document-project` | Transferred strongly but not exhaustively | Article includes scan/resume/deep-dive/checklist/CSV principle. | Do not import all 12 project types / 24 CSV columns unless a brownfield-focused pass requires it. |
| Strong sides and risks | Transferred into mechanism/failure sections | Benefits and risks appear as artifact-first strengths, overhead, stale context, quick/full mismatch, TEA cost. | Community/token-cost reports remain deferred until explicit external/source pass. |
| Analytical notes / handbook transfers | Mostly used as orientation | Main article absorbed only concept-level insights; handbook material not imported as procedural recipe. | Future Handbook/Fieldbook route should own step-by-step operations. |
| BMAD vs Gas Town local distinction | Superseded by P02 boundary | Contract section now has broader boundary with Gas Town/PWG/GSD/spec methods/ADR. | Needs cross-article sync later. |
| Source list | Used as provenance inventory | Most primary BMAD sources already appear in `source_usage`. | Several source candidates are recorded below as `not used unless expanded`. |
| Search formulations | Deferred | Not article content. | Use only in later allowed web/source pass. |
| Illustration candidates | Already dispositioned | `image_plan` covers every candidate and article has one external placeholder + two synthetic figures. | Rights/asset pass still needed. |
| Dossier open questions | Mostly mirrored | Open questions companion already tracks version, adoption, TEA, naming and image rights. | Keep concrete, avoid generic pending debts. |

### P03 source-depth candidates not yet promoted into the article

These are not omissions in the current concept article, but they are the most useful future technical anchors:

1. Quick Dev explanation page: human approval of short spec, layer diagnosis and `deferred-work.md` behavior.
2. Exact readiness/checklist output of `bmad-check-implementation-readiness` if a later pass wants more than `PASS/CONCERNS/FAIL`.
3. Story template/checklist anatomy: fields beyond the current article’s high-level story contract.
4. Correct Course `Sprint Change Proposal` structure and approval handoff.
5. Investigation case-file fields, confidence labels and route outputs.
6. Brownfield `documentation-requirements.csv` full schema and when each project-type flag matters.
7. Release-sensitive ecosystem surfaces: web bundles, `bmad-automator`, `bmad-method-ui`, PRD Coach and any current BMad-CORE/BMM naming split.
8. Community/adoption-friction sources: Ran the Builder, Reddit, issues #511/#813/#1629 and Rovo thread. These require explicit source evaluation before any claim enters the main article.

P03 changed no main-article text because no article-critical missing material was found.


## P04 documentary handoff transfer

| Change | Decision P04 | Where | Reason | Follow-up |
| --- | --- | --- | --- | --- |
| Core artifact chain reframed as handoff contracts | Added to article | «Главная цепочка» before figures | Makes the chain explicitly documentary rather than persona conversation. | Later language pass can smooth remaining English artifact names without losing source terms. |
| Handoff table | Added to article | «Главная цепочка» | Shows input, output and next-contour value for each major BMAD transition. | Editorial pass should decide whether this table and synthetic context-cascade figure both remain or one is merged. |
| Roles as quality of handoff | Added to article | «Роли как распределение суждения» | Prevents role section from becoming persona catalog; each role is tied to a produced artifact or reproducible trace. | Keep future role additions under lifecycle-function rule. |
| New primary facts | None beyond already tracked BMAD sources | Source usage only | P04 used existing BMAD dossier/source map; no external refresh. | Fresh source check still needed before final. |


## P05 file mechanics and recovery transfer

| Change | Decision P05 | Where | Reason | Follow-up |
| --- | --- | --- | --- | --- |
| File surfaces as recovery surfaces | Added | «Установка: где в репозитории живёт BMAD» | Shows `_bmad/`, `_bmad-output/`, manifest, planning artifacts, project context, sprint state and story files as recovery/next-action surfaces. | Later language pass should smooth ordinary English around artifact names. |
| Recovery table | Added | Same section | Makes file mechanics explicit without turning section into install tutorial. | Later visual/editorial pass may merge with P04 handoff table if dense. |
| Sprint-status recovery paragraph | Added | `sprint-status.yaml` section | Makes `bmad-sprint-status` not just state reporting but next-action recovery. | Keep PWG boundary intact. |
| New sources | None | Source usage only | Used existing tracked BMAD primary sources: Getting Started, Install BMad, sprint-status skill, dev-story skill. | Fresh source check still needed before final. |


## P06 brownfield/document-project transfer

| Change | Decision P06 | Where | Reason | Follow-up |
| --- | --- | --- | --- | --- |
| Scan levels as knowledge levels | Added | Brownfield section | Shows Quick/Deep/Exhaustive/Deep Dive as different knowledge-creation surfaces for future agents. | Later editorial pass should manage table density. |
| `project-scan-report.json` as state of knowledge creation | Added | Brownfield section | Connects resume/re-scan/deep-dive mechanics to recovery and next-agent use. | Verify exact state fields on source refresh. |
| `index.md` as navigation map | Added | Brownfield section | Shows generated docs/index as route to future-agent context, not static docs dump. | Could become a synthetic figure later if useful. |
| Stale brownfield docs risk | Strengthened | Brownfield section | Makes old PRD/stories/scan docs a specific failure mode. | Keep in failure section sync later. |
| New sources | None | Source usage only | Used existing BMAD document-project and Established Projects sources. | Fresh check still needed. |


## P07 review/correct-course/human gates transfer

| Change | Decision P07 | Where | Reason | Follow-up |
| --- | --- | --- | --- | --- |
| Distributed human decision map | Added | «Gates и человеческие решения» | Shows PRD validation, readiness, create-story, review/status, checkpoint preview, investigation, correct-course and retrospective as separate human decision points. | Table density watchpoint remains. |
| PRD validation and readiness tied to artifacts | Strengthened | Gates/review sections | Connects early validation to later implementation readiness. | Exact validation report shape is version-sensitive. |
| Checkpoint preview located as human review interface | Strengthened | Gates table + review section | Clarifies it is not pass/fail and requires human judgement. | None. |
| Investigation/correct-course/retrospective located as repair decisions | Strengthened | Gates table + dedicated sections | Makes repair routes explicit rather than postscript. | Later pass may consolidate with A9 theory link. |
| New sources | None | Source usage only | Used existing BMAD primary sources already tracked. | Fresh source check still needed. |


## P08 evidence/release extension and limits transfer

| Change | Decision P08 | Where | Reason | Follow-up |
| --- | --- | --- | --- | --- |
| TEA/Enterprise as extension/evidence layer | Strengthened | Review/testing section; failure modes | Keeps TEA as upper boundary for traceability/NFR/compliance/release gate, not base BMAD. | Later source refresh for TEA docs. |
| Token/context cost as structural limit | Added | Failure modes | Explains cost mechanism through document reading and context cleanup without relying on anecdotal community reports. | Community/token reports remain source-pass candidates. |
| Overplanning / excessive ceremony | Strengthened | Failure modes | Ties full BMAD/Correct Course/TEA overhead to risk-based use. | None. |
| Stale artifacts | Already present; reinforced by P06/P08 context | Failure modes and brownfield | Keeps false-context risk central. | Later editing can consolidate duplicates. |
| Module confusion | Added | Failure modes | Separates BMM/core/modules/web bundles/automator/UI/TEA to avoid ecosystem drift. | Needs current module/release source check. |
| New sources | None | Source usage only | Used existing Official Modules, Releases, TEA, create-story and full-scan sources. | Fresh check still needed. |

## P09 free expansion transfer: Quick Dev as compressed lifecycle

| Недобор / источник | Решение P09 | Где в статье | Почему добавлено | Остаточный долг |
| --- | --- | --- | --- | --- |
| Quick Dev explanation page | Transferred | «Три режима глубины» | Quick Flow was too close to “fast path with commit”; P09 reframed it as a miniature lifecycle with intent compression, short spec approval and human review. | Refresh current docs/version before final. |
| Quick Fixes `deferred-work.md` behavior | Transferred | «Три режима глубины» | Shows how Quick Dev avoids hidden scope creep and preserves the BMAD principle of explicit intermediate artifacts. | Verify exact output location/name and whether current workflow always writes this file. |
| Quick Dev failure diagnosis by intent/spec/implementation layer | Transferred | «Три режима глубины» | Strengthens lifecycle repair: a failed quick fix is not always an implementation bug. | Later editorial pass may merge with general failure-mode section to reduce repetition. |

P09 did not add community/adoption evidence, cost claims or external benchmarks. It used only BMAD primary-source details already present in the allowed dossier/current source map.

## P10 free expansion transfer: artifact-framing invariant

| Недобор / источник | Решение P10 | Где в статье | Почему добавлено | Остаточный долг |
| --- | --- | --- | --- | --- |
| C5 atlas article model | Transferred as editorial structure | New section «Инвариант BMAD» | The article needed a concept-first reader path that ties pressure, mechanism, surfaces and later sections together. | Later edit should check whether this section overlaps with intro/practical reading. |
| Workflow Map progressive context building | Reframed | New section «Инвариант BMAD» | Shows that workflow order is a смена артефакта, задающего рамку работы, not a persona calendar. | Source names and phase outputs remain version-sensitive. |
| Four properties of BMAD artifacts | Added as synthesis | New section «Инвариант BMAD» | Gives a portable rule for deciding which details belong in the article: narrowness, explicitness, source-linkedness, liveliness for feedback/repair. | Not a direct source quote; keep as interpretive synthesis backed by article mechanisms. |

P10 did not add new commands, files, roles or images. It added a reader path that should reduce, not increase, future glossary/catalog drift.

## P11 visual transfer ledger: local assets

| Asset / source | Decision P11 | Article impact | Reason | Remaining debt |
| --- | --- | --- | --- | --- |
| `content/assets/theory-images/fowler-harness-overview.png` | Not inserted | None | Conceptually adjacent to guidance/sensors/feedback, but it would shift BMAD into harness-engineering theory rather than BMAD’s own artifact workflow. | None for BMAD; use in harness/source article if needed. |
| `content/assets/theory-images/fowler-harness-templates.png` | Not inserted | None | Explains app/harness templates, not BMAD installation, `_bmad/` layout or BMAD workflow surfaces. | None for BMAD. |
| `content/assets/theory-images/fowler-harness-change-lifecycle.png` | Not inserted | None | Feedforward/feedback lifecycle overlaps abstractly with BMAD review/repair, but the visual vocabulary is Fowler harness-specific and would confuse method boundary. | If a future cross-theory comparison is written, reconsider outside this BMAD article. |
| Local asset index overall | No BMAD-specific ready asset found | None | Index contains SPDD, Gas Town, Beads, Humanlayer, OpenAI, Fowler harness and story assets, but no ready BMAD workflow map, role/artifact diagram, `_bmad` tree or sprint/brownfield visual. | External BMAD workflow map still needs asset pass. |

P11 did not add or remove article text. It satisfied insert-or-explain by recording rejection reasons in the image plan and this ledger.

## P12 visual transfer ledger: external real candidates

| Candidate | Decision P12 | Article impact | Reason | Remaining debt |
| --- | --- | --- | --- | --- |
| Official BMAD Workflow Map Diagram | Kept inline as `external-real-candidate` | Article bottom status updated; main inline placeholder retained | It is the only dossier-listed BMAD-specific real external visual and directly supports artifact flow / roles / Quick Flow. | Download/capture, rights, quality, attribution, localization. |
| Getting Started project tree | Not added as external image | Existing code block retained | This is source text/code-like material and is already clearer as a text tree. | Maybe redraw as synthetic figure in a later design pass. |
| Other BMAD dossier visual candidates | No external image added | Existing synthetic figures/tables/prose retained | They are editorial/synthetic ideas, not real source diagrams. | Future visual pass can create/merge synthetic diagrams if needed. |

P12 did not add new factual article claims beyond visual-candidate status.

## P13 synthetic visual transfer ledger

| Candidate | Decision P13 | Reason | Remaining debt |
| --- | --- | --- | --- |
| Quick Dev boundary diagram | Deferred | P09 prose now covers intent/spec/diff/deferred-work/repair; adding a figure would likely duplicate text. | Reconsider only if later structure pass removes prose or needs a compact mini-lifecycle. |
| SPEC compression diagram | Deferred | `bmad-spec` is important but not central enough to justify another figure in the BMAD article. | Could belong in a future source note or handbook page. |
| Brownfield / Document Project diagrams | Deferred | P06 table is already dense; a figure should replace, not add to, that table. | Later visual-edit pass can merge table into a diagram. |
| Correct Course / investigation / TEA release-gate diagrams | Deferred | Useful ideas, but current article already has multiple tables and figures; TEA should not overweight the base BMAD article. | Reconsider if those sections become separate handbook/fieldbook entries. |
| BMAD vs GSD/PWG/Gas Town boundary diagram | Deferred | Boundary prose is sufficient and a comparison figure risks turning BMAD into ecosystem overview. | Wait for cross-article sync. |

P13 transferred no new material into the article body.

## P14 standalone concept transfer

| Material | Decision P14 | Where in article | Why added | Remaining debt |
| --- | --- | --- | --- | --- |
| C5 standalone article contract | Transferred as structure | New section «Минимальный пример» | Gives concept-first readers a local route through BMAD without prior theory chapters. | Later edit should check for overlap with invariant and practical-reading sections. |
| Audit-report illustrative scenario | Added as authorial example | New section «Минимальный пример» | Shows how one risky change is split across PRD, architecture/ADR, story, status, review and repair. | Ensure final copy does not imply official source case. |
| Controlled theory repeat: documents/statuses narrow context | Reinforced | New section «Минимальный пример» | Makes the local minimum theory concrete inside BMAD rather than abstract. | Later style pass may shorten. |

P14 added no new visual assets and no new external sources.

## P15 mechanism/failure transfer

| Failure / boundary | Decision P15 | Where in article | Why added | Remaining debt |
| --- | --- | --- | --- | --- |
| Personas become theater | Reinforced | «Инвариант BMAD» and «Роли» | Makes role value conditional on artifact/gate/next-input change. | Later style pass can shorten repeated “not persona theater” wording. |
| Documents do not become next-step inputs | Reinforced | «Инвариант BMAD» | Distinguishes working artifact from dead archive. | Later structure pass should avoid repeating this in too many sections. |
| Stale artifacts | Reinforced | «Инвариант BMAD» | Makes stale PRD/story/scan/project-context a core mechanism failure, not only a late risk list. | Final source refresh for exact paths/outputs. |
| Quick/Full/Enterprise confusion and overplanning | Reinforced | «Инвариант BMAD» | Integrates mode-selection errors into mechanism rather than separate error catalog. | Later A10 sync may refine phrasing. |
| Evidence layer treated as mandatory core | Reinforced | «Инвариант BMAD» | Keeps TEA/Enterprise as upper boundary, not default BMAD. | Keep TEA proportion controlled. |

No new visual assets or external sources were added.

## P16 transfer ledger — semantic backlinks

| Item | Decision | Destination | Reason | Residual debt |
| --- | --- | --- | --- | --- |
| Semantic theory questions from 00/A3/A5/A7/A9/A10/C5 | Transferred as backlinks | `bmad_method_theory_links.md`; short guard paragraph in main article | The working sheet required article-to-theory links that state what BMAD helps understand, not generic “see also” references. | Later cross-article pass should ensure names and anchors match final theory fragment filenames. |
| Full theory exposition | Rejected | Main article | The article should remain standalone and concept-first, not become a compressed copy of the general theory. | Keep only compact local theory section. |
| New source facts about BMAD | Not added | N/A | P16 was a theory-linking pass, not a public source refresh. | Current BMAD docs still need final freshness check in a dedicated pass. |

## P17 transfer ledger — language only

| Item | Decision | Destination | Reason | Residual debt |
| --- | --- | --- | --- | --- |
| Accidental English glue in article prose | Reworded | `bmad_method.md` | Russian mode required translating ordinary connectors and explanatory terms while keeping exact names of tools, commands, paths and source labels. | Later language pass should do a slower full-line polish for remaining accepted technical English. |
| Source facts / article argument | Preserved | Main article and companions | P17 was not a source pass and did not add or remove factual material. | Dedicated freshness/source pass still needed before publication. |

## P18 — ledger второго языкового прохода

| Материал | Решение P18 | Где отражено | Обоснование | Оставшийся долг |
| --- | --- | --- | --- | --- |
| Заголовки, подписи и таблицы основной статьи | Языковая правка без изменения фактуры | `bmad_method.md` | Нужно убрать гибридные формулировки после P17 и сделать article-facing text читабельнее. | Финальные редакторские проходы могут ещё сгладить плотные места, но не должны ломать точные имена из источников. |
| Внешний кандидат Workflow Map | Решение не изменено; описание сделано более русским | Inline-placeholder, нижний раздел для прохода по ассетам, image plan / queue | P18 не является проходом по ассетам и не скачивает изображение. | Права, качество, локальный файл и атрибуция остаются открыты. |
| Фактические источники BMAD | Сохранены | Source usage и основной текст | P18 не был source-depth проходом. | Нужна свежая проверка версии/релизов перед публикацией. |

## P19 — ledger первого общего редакторского прохода

| Материал | Решение P19 | Где отражено | Обоснование | Оставшийся долг |
| --- | --- | --- | --- | --- |
| Формулировка контрактного раздела | Уточнена | Заголовок «Контракт статьи: BMAD как профиль передачи работы через артефакты» | Прежний заголовок сильнее звучал как граница с соседями; новый лучше показывает положительную функцию статьи. | Следующие редакторские проходы должны проверить, не слишком ли рано идёт сравнительная граница. |
| Ограничение включения деталей | Переформулировано | Конец контрактного раздела | Убрана абстрактная «отрицательная граница»; сохранён критерий включения деталей. | Нет. |
| Четырёхвопросный критерий применения BMAD | Добавлен как редакторский синтез | «Практический способ читать BMAD» | Статья стала сильнее как standalone article: читатель получает проверку, не распался ли BMAD на роли/файлы/команды без передачи следующего шага. | Проверить в следующих проходах, не дублирует ли критерий инвариант слишком близко. |
| Источниковая фактура и визуальные решения | Сохранены | Вся статья и companion-файлы | P19 не добавлял внешние источники и не менял image decisions. | Freshness/source pass остаётся открытым. |

## P20 — ledger второго общего редакторского прохода

| Материал | Решение P20 | Где отражено | Обоснование | Оставшийся долг |
| --- | --- | --- | --- | --- |
| Контрактный раздел с границами BMAD | Переставлен ниже минимального примера | Между «Минимальный пример» и «Установка» | В ранней позиции сравнительные границы перегружали standalone-вход. Теперь читатель сначала видит проблему, инвариант и пример, затем получает границы статьи. | Следующий редакторский проход должен проверить плавность перехода от контракта к установке. |
| Маршрут читателя после инварианта | Обновлён | Абзац «Такой инвариант задаёт читательский маршрут…» | После перестановки нужно явно назвать минимальный пример и контрактный раздел. | Нет. |
| Фактические источники и визуальные решения | Сохранены | Вся статья и companion-файлы | P20 был структурным редакторским проходом, а не source-depth или visual pass. | Freshness/source pass и asset-pass остаются открыты. |

## P21 — ledger третьего общего редакторского прохода

| Материал | Решение P21 | Где отражено | Обоснование | Оставшийся долг |
| --- | --- | --- | --- | --- |
| Переход от границ к устройству метода | Добавлен | Конец контрактного раздела | После перестановки P20 нужен явный мост от сравнения к файловой механике BMAD. | Нет. |
| Заголовок ревью-раздела | Уточнён | «Ревью, `bmad-checkpoint-preview` и свидетельства» | Официальное имя рабочего процесса важнее размыто английского `checkpoint preview`. | Проверить текущую форму команды в финальном source check. |
| Brownfield-раздел | Уточнён | «Brownfield-проект: сначала сделать код читаемым для агента» | Заголовок теперь говорит о практической функции раздела, а не только о source-label. | Нет. |
| Investigation-раздел | Русифицирован | «Расследование и retrospective: факты после реализации» | Обычное объяснение стало русским, при сохранении source-specific retrospective. | Можно решить на финальном стиле, оставлять ли retrospective латиницей как BMAD/source label. |

## P22 — ledger public/article structure pass

| Материал | Решение P22 | Где отражено | Обоснование | Оставшийся долг |
| --- | --- | --- | --- | --- |
| Первый экран | Проверен, без перестановки | Начало статьи | Статья теперь начинается problem-first: объект, reader question, короткий ответ, затем проблема потери контекста. Taxonomy/boundary block не стоит первым. | Нет. |
| Inline Workflow Map placeholder | Переписан | `fig-bmad-workflow-map` | Убраны фразы «здесь нужна» и «должна пройти проверку» из caption; подпись стала публичной. | Asset-pass, права, скачивание, качество и атрибуция остаются открыты. |
| Нижний section для external image | Уточнён | «Внешние изображения для asset-pass» | Название оставлено как явный workflow label для будущего asset-pass; P12 executor-note удалён из статуса. | Перед публикацией нужно решить, остаётся ли эта служебная секция в публичной сборке или уходит в companion. |
| Баланс текста и фигур | Сохранён | Главная цепочка и `sprint-status.yaml` | Новые фигуры не нужны; существующие визуальные места соответствуют смысловым узлам. | Финальный visual/asset pass должен локализовать Workflow Map или убрать placeholder. |

## P23 — companion transfer sync

| Область | Решение P23 | Где отражено | Обоснование | Текущий долг |
| --- | --- | --- | --- | --- |
| Source usage | Синхронизирован | `bmad_method_source_usage.md` | Workflow Map больше не описывается как P12-only queue note; source map соответствует текущему inline candidate. | Freshness check BMAD docs/releases. |
| Image plan / external queue | Синхронизированы | `bmad_method_image_plan.md`, `bmad_method_external_image_queue.md` | Текущий статус Workflow Map: inline external placeholder с публичной подписью, без скачивания. | Download/rights/quality/attribution/localization. |
| Open questions | Реструктурированы | `bmad_method_open_questions.md` | Живые блокеры вынесены наверх; устаревшие P19–P22 редакторские вопросы закрыты или понижены до истории. | См. верхний раздел open questions. |
| Ledger size | Не расширялся coverage-матрицей | Этот раздел | P23 добавляет только синхронизационные решения, а не новую тотальную coverage-бюрократию. | При финальной сборке можно архивировать pass-history отдельно, если нужен короткий companion. |

## P24 — style defect audit ledger

P24 не менял source-transfer decisions. Исправления касались формы: более прямые русские формулировки заменили псевдотермины, театральные метафоры, тяжёлые заголовки и неточные слова вроде «контур» там, где речь шла об участниках или этапах процесса.

Ключевое решение P24: не переписывать статью целиком и не трогать компактные рабочие термины BMAD (`story`, `Quick Flow`, `Workflow Map`, `project-context.md`, `sprint-status.yaml`, названия skill-файлов), потому что они являются source labels, а не стилевыми дефектами.

## P25 — selective natural rewrite ledger

P25 не переносил фактуру и не менял границы статьи. Он изменил только публичную формулировку нескольких синтетических терминов:

| Было | Стало | Причина |
| --- | --- | --- |
| `working source of truth` / «рабочий источник правды» | «артефакт задаёт рамку работы» / «ведущий артефакт» | Убрать кальку и сохранить механизм смены артефактов. |
| «рабочая файловая рамка» в установке | «где в репозитории живёт BMAD» | Заголовок стал естественным и конкретным. |
| «поверхности восстановления» в таблице | «файл или место» / «места, по которым восстанавливают работу» | Убрать псевдотермин без потери recovery-функции. |
| Ритм `не X, а Y` в ролях и Enterprise | Более прямое описание функций роли и условия Enterprise | Сохранить различение, но убрать презентационный ритм. |

Все source labels и имена BMAD-артефактов сохранены.

## P26 — guarded final style ledger

P26 не переносил source material. Изменения были формальными и сохраняли P25-решение: статья говорит о BMAD через артефакты, файлы, статусы, контрольные точки и ремонт, а не через каталог персон или команд.

Правки: убраны последние шероховатые обороты вроде «команды со слешем», «recovery-функция», «ошибка может жить»; сохранены точные имена BMAD-команд, статусы, пути, ссылки, figure IDs и boundary decisions.
