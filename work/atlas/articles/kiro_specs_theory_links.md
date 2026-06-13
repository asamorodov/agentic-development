# kiro_specs — theory links

Статус: `P26_guarded_final_style_current`. Файл фиксирует смысловые обратные связи текущей статьи с общей картой SDLC. Он не является публичным source list и не создаёт общего долга синхронизации C5/A10: C5/A10 используются как read-only context for article shape and mode selection.

## Current article role from C5/A10

- Уровень: статья об инструментальной форме.
- Главный вопрос: что меняется, когда слой спецификации живёт внутри IDE/Web/CLI-среды продукта, а не только в файлах или переносимой CLI-дисциплине.
- Controlled repetition: можно локально объяснять слой спецификации, рабочую поверхность, слой свидетельств, контекст среды and human authority; нельзя заново писать всю теорию specification/process/evidence/PWG.
- Mode-selection link: Vibe session, Quick Plan, Feature Spec and Bugfix Spec are explained by uncertainty/risk, not by a blanket rule to always use full Specs.

## Semantic back-links

| Theory node | Theoretical question illuminated by Kiro Specs | Kiro-specific answer / boundary in article |
| --- | --- | --- |
| 00 spine map | What carrier lets a software change move from intent to maintenance without losing meaning, evidence or responsibility? | Kiro makes part of the chain visible as `requirements.md → design.md → tasks.md → execution → Sync Files`; it does not close ADR memory, full PWG state or final acceptance authority by itself. |
| A3 specification methodologies | When must intent become a reviewable artifact before an agent acts? | Feature Specs/Bugfix Specs turn intent or defect into files with approvals and downstream design/tasks. |
| A5 process methodologies | When does process become an artifact rather than habit? | Kiro productizes workflow steps, task statuses, hooks and modes, but this is not automatically a full durable work graph. |
| A6 product execution environment | What changes when the method is embedded in product surfaces? | Kiro links specs to IDE/Web/CLI surfaces, chat context, task launch, hooks, MCP, checkpoints and governance. |
| A7 observation vs evidence | When does a signal from agent work become evidence for acceptance? | Task status, hook output, monitoring and prompt logs are observations until tied to requirements/design/tasks/diff/tests/PBT and a human decision. |
| A8 authority and human confirmation | Where does human authority remain? | Requirements/design approvals, task launch, Supervised/Autopilot choice, MCP/tool approvals, diff review and final acceptance remain human decision points. |
| A9 lifecycle repair | What must be updated after code changes? | Sync Files, steering, Powers, hooks and tests are surfaces where stale artifacts can be repaired; merge/task completion does not end lifecycle automatically. |
| A10 mode selection | Which external structure is sufficient for this change? | Kiro offers Vibe, Quick Plan, Feature Spec and Bugfix Spec; choice follows uncertainty, reversibility, task dependency and evidence needs. |
| C5 concept-first atlas | How can the article be self-contained while still connected to theory? | The article begins with the practical problem, defines local terms and keeps theory links as semantic back-links, not prerequisites. |

## Neighbor boundaries retained in article

| Neighbor method / article route | Boundary decision in Kiro Specs article |
| --- | --- |
| Spec Kit | Neighboring portable repo/CLI SDD toolchain; Kiro’s emphasis is productized specification environment. |
| SPDD / OpenSPDD | Neighboring prompt/Canvas intent-artifact method; Kiro’s unit is spec session and files used by product surface. |
| TDAD | Useful when discussing tests/evidence; Kiro PBT is an evidence layer around Specs, not a TDAD frame. |
| Constitutional SDD | Useful for policy/constraint comparison; Kiro enterprise governance is access/policy layer, not a constitutional spec layer. |
| ADR | Useful for decision memory; Kiro `design.md` is not an ADR by default. |
| Persistent Work Graph / Beads | Useful for durable ownership/gates/recovery; Kiro `tasks.md`, statuses and hooks are not enough to claim PWG. |
| Handbook / Fieldbook | Practical checklists and failure playbooks are intentionally deferred; the article remains a concept-first technical atlas entry. |

## P23 sync note

- Theory links now reflect the problem-first first screen and current section order.
- Earlier pass notes were compacted into current semantic links.
- No generic C5/A10 or theory synchronization debt remains; only concrete source/asset blockers live in `kiro_specs_open_questions.md`.
## P24 theory-link note

Semantic links are unchanged. The public article now explains the theory bridge without naming internal C5 logic, which improves standalone readability while keeping C5/A10 as companion-only context.
## P25 theory-link note

Theory links are unchanged. The theory section was made more natural by replacing meta-language with direct explanations of artifacts, evidence, repair and mode selection.

## P26 theory-link note

Theory links are semantically unchanged. P26 made the public theory bridge more direct and less meta-heavy while keeping Kiro as a productized specification environment, not a full replacement for Spec Kit, SPDD, TDAD, Constitutional SDD, ADR or PWG.
