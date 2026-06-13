# Persistent Work Graph — source transfer ledger

Status: final package complete. Ledger remains a compact transfer record, not a substitute for article prose.

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG is durable work state outside chat/session/TODO list | PWG dossier; A4; B2 | Opening; "Почему отчёт..."; "Минимальная единица" | transferred |
| Work item needs durable identity, dependencies, owner, gates, evidence, history, prime, recovery | PWG dossier; A4 | "Минимальная единица" table | transferred |
| Beads as anchor but not recipe/product overview | PWG dossier; C5 | Opening; "Beads как якорь" | transferred, needs later boundary audit |
| Beads dependencies / `bd ready` / blocking vs non-blocking relations | PWG dossier | "Зависимости и очередь готовой работы" | transferred |
| GitHub / Linear baseline issue relations | PWG dossier; A4 | "Зависимости..." | transferred |
| Ownership, pinning, handoff and locks for multi-agent work | PWG dossier; A4 | "Владение, handoff..." | transferred |
| `bd gate` as durable wait | PWG dossier; A4 | "Gate как долговечное ожидание" | transferred |
| `bd prime` as compact recovery context | PWG dossier; A4 | "Prime" | transferred |
| Recovery/status/doctor/blocked and operational hygiene | PWG dossier | "Восстановление..." | transferred |
| Source-state lifecycle and intermediate artifacts | PWG dossier; B2 | "Источники и промежуточные артефакты" | transferred |
| Durable execution boundary | PWG dossier; C4 | "Граф работы и граф выполнения" | transferred |
| Taskmaster as lightweight file-based contrast | PWG dossier | "Beads как якорь" | transferred |
| Gas Town boundary | PWG dossier; C5; B3 not yet read in P01 | "Где проходит граница с Gas Town" | provisional, must be audited in P02/P07 |
| Parallelism boundaries: CodeCRDT, STORM, MAST | PWG dossier | "Параллельность" | transferred |
| Multi-pass document process as PWG design test | PWG dossier; C5; A10 | "Модель для многопроходного документного процесса" | transferred |
| Failure modes | PWG dossier; A10 | "Ошибки применения PWG" | transferred |
| Mode selection: when PWG is unnecessary/needed | A10; PWG dossier | "Когда PWG избыточен..." | transferred |

## Known P01 debts

- Gas Town boundary must be checked against `GAS_TOWN_METHOD_DOSSIER.md` and `B3_gas_town_beyond_pwg.md` in a later pass.
- Local assets were not inserted during P01; visual passes must classify and decide them.
- External real image candidates were not reopened; P12 should handle queue/disposition.


## P02 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG article contract: not Beads review, Gas Town model, process profile, issue tracker alone, durable execution, CRDT/shared editor or TS-loop implementation plan | P02 worksheet; PWG dossier; B3; C2; C4 | `Контракт статьи` | transferred |
| Beads is mechanism check: storage, commands, dependencies, ready queue, history, prime, recovery | PWG dossier; B3 | `Контракт статьи`; opening | transferred |
| Gas Town is organizational-operational environment above PWG, with roles/queues/mail/observability/human control surface | Gas Town dossier; B3 | `Где проходит граница с Gas Town` | transferred |
| GSD/BMAD process profiles set rhythm/roles/documents; PWG holds consequences as state | C2 | `Контракт статьи` table | transferred |


# P03 dossier inventory — selective, not total coverage

This is not a total coverage matrix. It records whether the article has enough technical anchors for its current concept contract.

## Already transferred into article-critical text

| Dossier cluster | Transfer status | Notes |
| --- | --- | --- |
| Core definition: durable work state outside prompt/transcript/TODO | transferred | Drives opening and first sections. |
| Minimal work node: identity, dependencies, owner, gates, handoff, evidence, history, prime, recovery | transferred | Appears in minimal unit table and later sections. |
| Beads as anchor: Dolt, CLI/MCP, ready queue, gates, prime, recovery | transferred | Present as mechanism check, not product review. |
| Dependency readiness: blocking/non-blocking relations, `bd ready`, `bd blocked`, cycles/graph | transferred | Enough for concept article. |
| Ownership and handoff: pin/hook/claim/lock/fan-out/fan-in | transferred | Present, but later Beads source-depth pass can add more exactness. |
| Gate as durable wait | transferred | Present with `bd gate` and Temporal contrast. |
| Prime and compact context recovery | transferred | Present with `bd prime`. |
| Recovery and operational hygiene | transferred | Present with Beads recovery/architecture. |
| Source-state lifecycle and intermediate artifacts | transferred | Present; important to this article's document-workflow example. |
| Durable execution boundary | transferred | Present with LangGraph/Temporal/Pydantic/DBOS/Restate distinction. |
| Parallelism boundary: CodeCRDT/STORM/MAST | transferred | Present as caution against shared-state optimism. |
| Multi-pass document process as design test | transferred | Present but must remain example, not implementation plan. |
| Failure modes: theater, stale graph, false done, wrong authority, storage complexity, metadata leak, semantic convergence | transferred | Present in errors section. |

## Partially transferred; may need strengthening only if later passes find article weakness

| Dossier cluster | Current article handling | Possible strengthening |
| --- | --- | --- |
| Beads routing / hydration | Mentioned only indirectly as cross-repo/routing state | Add one sentence if cross-repo continuation becomes central. |
| Beads Codex hooks / `SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit` | Article mentions compact recovery but not exact hook lifecycle | Source-depth pass may add as technical anchor for prime/recovery. |
| Taskmaster tags / clusters / loop | Lightweight contrast included | Keep brief; not article-critical. |
| Operation-log gap / agent-first version control | Not transferred | Probably not needed in core article unless failure-mode section expands. |
| Debug flags / RPC/sync/freshness diagnostics | Not transferred | Useful for Gas Town/Beads detail, but may overload concept article. |
| Safe parallel source protocol | Partially transferred as source state + synthesis gate | Keep as document-process example; do not turn into full protocol. |
| Visual candidates list | Not transferred to text | Handled by `image_plan` and later visual passes. |

## Left untransferred by design

- Full Beads command surface, plugin workflow details and troubleshooting catalog.
- Full Gas Town roles, convoys, feed, queue, mail and patrol details.
- Full GSD/BMAD process exposition.
- Full implementation schema for a future TS orchestrator.
- Full source-search protocol for parallel source discovery.

These are intentionally outside the article contract unless a later pass identifies a concrete explanatory gap.

## Requires primary-source opening before stronger claims

- Any new claim about current Beads implementation beyond details already cited from the dossier should reopen the relevant Beads docs page.
- Any stronger claim about Gas Town maturity, cost or role behavior should use Gas Town README/docs/Medium source directly rather than the internal dossier.
- Any quantitative claim about CodeCRDT speedup/slowdown or semantic conflicts should remain linked to the paper and should not be paraphrased more strongly without reopening the paper.
- Any claim about exact current capabilities of Claude Code/Codex worktrees or hooks should be rechecked if it becomes central, because these surfaces can change.

## Technical anchor gaps after P03

- Prime/recovery section would benefit from one concrete hook lifecycle detail in a later pass.
- Work graph vs execution graph distinction is clear but may benefit from a figure/table later.
- Multi-pass document example is useful but should be guarded against becoming a TypeScript implementation plan.


## P04 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Prompt is not the unit of analysis; program change moves through intent, specification, decision, work state, execution, evidence, completion and maintenance | `A1_change_not_prompt.md` | `Почему отчёт...` after substrate table | transferred |
| Chat/transcript/TODO/ordinary issue/local plan each lose different work-state properties | A4; B2; PWG dossier | `Почему отчёт...` table | transferred |
| Missing properties: identity, dependency, ready-state, owner/claim, gate, evidence, compact recovery, history | P04 instruction; A4; B2 | `Почему отчёт...` table and paragraph | transferred |


## P05 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Specification/issue/signal must produce a work item where continuation state lives | C1; PWG dossier | `Минимальная единица` mechanism paragraph | transferred |
| Minimal fields must change next admissible action, not merely describe work | PWG dossier; C1 | `Минимальная единица` mechanism paragraph | transferred |
| Evidence package connects status transitions to proof; `done`/`accepted` cannot be self-report | C3 | `Минимальная единица`; later evidence sections | transferred |
| Prime/recovery close the loop when current executor disappears or work state becomes stale | PWG dossier; C1/C3 | `Минимальная единица` mechanism paragraph | transferred |


## P06 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Beads exposes PWG properties through Dolt storage, hash identity, dependency-aware ready queue, graph commands, claims, gates, prime, routing and recovery | PWG dossier; local asset | `Beads как якорь, но не рецепт` table | transferred |
| Dolt-like substrate adds operational caveats and maintenance | PWG dossier | `Beads как якорь...` operational limitations paragraph | transferred |
| Local Beads task graph memory asset supports Beads anchor | `content/assets/theory-images/beads-task-graph-memory.svg`; local asset index | inline figure | inserted |


## P07 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Issue tracker stores task/discussion; PWG stores continuation state and admissible next action | PWG dossier; A4/B2 context | `Контракт статьи` adjacent-layer table | transferred |
| Durable execution recovers run/checkpoint; PWG assigns meaning/authority/evidence to work state transition | C4; PWG dossier | adjacent-layer table; `Граф работы и граф выполнения` | transferred |
| CRDT/STORM reduce coordination/write conflicts but do not replace semantic work state and acceptance | PWG dossier | adjacent-layer table; `Параллельность` | transferred |
| Gas Town organizes multi-agent operating environment; PWG is durable work unit inside/below it | Gas Town dossier; B3 | adjacent-layer table; Gas Town section | transferred |


## P08 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Multi-pass document writing can be modeled as PWG even without product issue graph | PWG dossier; prompt queue protocol; manufactury plan | `Модель для многопроходного документного процесса` | transferred |
| Job/pass/gate/prime/recovery are portable work-state primitives | PWG dossier; prompt queue protocol | document-process table | transferred |
| Source states and intermediate artifacts make source transfer durable and auditable | PWG dossier; prompt queue protocol | document-process table and source-state section | transferred |
| Worker returns, citation audit, synthesis pass and safe parallel source protocol protect parallel source work | PWG dossier; prompt queue protocol | document-process section | transferred |
| The document-process example is not a TS-loop implementation plan | P08 worksheet; article contract | document-process final paragraph | transferred |


## P09 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Minimal PWG schema should encode work item id, target, state, claim, dependencies, gates, evidence, prime and recovery | PWG dossier; article needs identified in P09 | `Минимальная единица` schema block | added |
| State names matter only if they restrict transitions and next actions | PWG dossier dependency/gate/recovery semantics | `Минимальная единица` after schema | added |
| Forbidden transitions protect against premature closure and overwritten claims | PWG dossier failure modes | `Минимальная единица` after schema | added |

## P10 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Work graph, execution graph, evidence layer, source state and shared-editing coordination must remain separate but address-linked layers | B2; C4; C3; existing article boundary material | `Граф работы и граф выполнения — разные слои` | transferred |
| Execution run IDs, evidence packages, source IDs and reservations must not substitute for work item status or acceptance | C4; C3 | `Граф работы и граф выполнения — разные слои` | transferred |

## P11 local visual transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Gas Town is an upper operating environment around PWG, not PWG itself | `gastown-architecture.svg`; manifest; existing Gas Town boundary text | `Где проходит граница с Gas Town` | local figure inserted |
| Parallel research workers should return evidence packages into audit/synthesis rather than directly writing canonical text | `anthropic-multi-agent-process-diagram.webp`; manifest; existing document-process section | `Модель для многопроходного документного процесса` | local figure inserted |
| Gas Town basic workflow and Anthropic high-level architecture are relevant but redundant for this article | P11 local asset review | Image plan / audit | intentionally not inserted |

## P12 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| External real image candidates are not needed inline beyond already-local assets | PWG dossier illustration list; external image candidate catalog; current article | Image plan / external image queue | transferred as disposition metadata |
| Anthropic multi-agent process external candidate is already covered by a local asset | PWG dossier; local asset inserted P11 | `Модель для многопроходного документного процесса` | `superseded_by_local_asset` |

## P13 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| Work item / PWG node acts as a hub linking run IDs, source IDs, claims/reservations and evidence packages without collapsing them | Current article after P10; image plan | `Граф работы и граф выполнения — разные слои` | transferred as synthetic figure |

## P14 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG occupies the work-state middle of the change lifecycle, between intention/specification and execution/evidence/acceptance | `00_spine_map.md`; B2 | `Где PWG стоит в жизненном цикле изменения` | transferred |
| Minimal PWG walkthrough: signal → node → ready queue → claim → gate → artifacts/evidence → review/accept/recover | B2; current article | `Где PWG стоит...` | transferred |

## P15 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG failure modes include stale graph, evidence-free dependency removal, false claim control, unsafe ready, weak prime, bureaucratic gate, graph gaming and premature storage | Current article; degradation/duplication audit | `Ошибки применения PWG` | transferred |

## P16 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG is the work-state carrier between specification, execution, evidence, acceptance and repair | A4; C1; C3; C4; A9 | `Связь с общей теорией AI-driven SDLC` | transferred |
| Process profiles leave consequences that PWG can store; observation/evidence and authority/acceptance remain distinct | A5; C2; A7; A8 | `Связь с общей теорией AI-driven SDLC` | transferred |

## P17 language pass note

No new factual transfer. The pass only normalized Russian prose and protected source-specific names, commands, fields and links from accidental translation.

## P19 editorial transfer note

No new source material was introduced. The new control-test paragraph is a synthesis of already transferred PWG mechanism claims: dependency readiness, gate blocking, claim/right-of-write, evidence-backed transition, prime and recovery.

## P20 editorial transfer note

No new external source material was introduced. The document-process section now explicitly frames its job/pass/gate/source-state material as a portability proof, preserving the P08 transfer rather than adding a new claim.

## P21 transfers

| Claim / material transferred | Source basis | Article location | Status |
| --- | --- | --- | --- |
| PWG is durability of an individual work unit; Gas Town is durability of organization around many work units | `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` | `Где проходит граница с Gas Town` | transferred |
| Gas Town roles, patrols, merge queues, mail routing and Mayor surface belong to the neighboring Gas Town article unless needed for the work-unit boundary | B3 | `Где проходит граница с Gas Town` | transferred as boundary guard |

## P23 compact transfer summary

P23 did not transfer new article material. It reconciled the ledger with the current article shape:

| Article function | Transferred material now considered current | Status |
| --- | --- | --- |
| Core problem | Chat transcript, TODO, ordinary issue and local plan do not preserve enough continuation state | stable |
| PWG contract | Durable work identity, dependencies, owner/claim, gates, evidence links, history, prime and recovery | stable |
| Behavioral control | A field belongs in PWG only if it changes permitted behavior, recovery, evidence, transition logic or handoff | stable after P19 |
| Beads anchor | Dolt-backed task graph, ready/blocked graph, claim/pin/handoff, gate, prime and recovery as mechanism check | stable; not a product tour |
| Neighboring layers | Issue trackers, durable execution, evidence packaging, shared editing/CRDT, STORM/MAST and Gas Town answer adjacent questions | stable; boundary table retained |
| Gas Town boundary | PWG gives durability to one work unit; Gas Town gives durability to organization around many works | stable after B3 audit |
| Document-process proof | Job/pass/gate/prime/recovery, source lifecycle, worker returns, citation audit and synthesis pass are portable PWG primitives | stable; not an internal pipeline report |
| Visual disposition | Four inline visuals retained; external screenshots rejected/deferred into queue | stable |
| Theory navigation | Final table maps PWG to process, evidence, authority, execution and repair links without retelling theory chapters | stable |

The intentionally omitted material remains omitted: full Beads troubleshooting/product documentation, full Gas Town operating model, implementation-specific TypeScript loop details, product screenshots for issue trackers and metric-heavy boundary figures.

## Final ledger check

Final check confirmed that the ledger does not replace the article: the main article itself explains source-state mechanics, citation audit, control conditions, document-process transfer and neighbor boundaries with technical anchors. P24-P26/final packaging did not add or remove transferred facts.
