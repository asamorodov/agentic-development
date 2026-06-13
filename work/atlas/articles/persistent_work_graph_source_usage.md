# Persistent Work Graph — source usage

Status: final package complete. Source usage is synced through final style/package pass; P24-P26 and Final changed wording/package metadata, not factual source claims.

| Source | Role in article | Current use |
| --- | --- | --- |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Primary dossier for PWG mechanism | Core definition, Beads anchor, dependencies, gates, prime, recovery, document-process transfer, failure modes, source state. |
| `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` | Theory boundary | Problem framing: report is not work state; PWG stores continuation state, readiness, gates, owner, evidence. |
| `work/theory-writing/fragments/B2_pwg_contribution.md` | Contribution to general theory | Work as durable object; premature closure; source state; handoff; recovery. |
| `work/theory-writing/fragments/C1_specification_to_pwg.md` | Spec-to-work bridge | Specification obligations become working state when continuation requires dependency/owner/evidence tracking. |
| `work/theory-writing/fragments/C3_pwg_to_evidence.md` | Evidence bridge | `done` requires evidence package, not agent self-report. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Runtime boundary | Durable execution and sandbox/runtime are adjacent but not identical to PWG. |
| `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` | Atlas article model | Article is concept-first: self-contained, controlled repetition, not a Beads/Gas Town duplicate. |
| `work/theory-writing/fragments/A10_mode_selection_map.md` | Mode-selection context | Criteria for when PWG is overkill versus needed. |
| Beads documentation / repository / architecture / dependencies / gates / prime / recovery / coordination / routing | Primary external anchor through dossier | Inline cited as practical anchor for PWG properties, not as product overview. |
| GitHub Issues and Linear issue relations | Baseline comparison | Used to show ordinary issue graphs as minimum, not sufficient AI work state. |
| Taskmaster docs | Lightweight contrast | Used to show file-based task graph alternative. |
| LangGraph, Temporal, Pydantic AI, DBOS, Restate | Durable execution boundary | Used to distinguish graph of work from graph of execution. |
| CodeCRDT, STORM, MAST | Parallelism boundary | Used to warn that shared state / write validation / multi-agent coordination do not solve semantic synthesis by themselves. |
| Intermediate Artifacts, SKILL.nb, AEGIS | Adjacent mechanisms | Used for source/intermediate artifact state, validation gates, and permission-gate framing. |

## P01 note

The article currently relies on source facts already present in the bundled dossier and theory fragments. No external source was reopened during P01.


## P02 boundary inputs

- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` and `B3_gas_town_beyond_pwg.md` used to strengthen boundary: Gas Town = organizational-operational environment above PWG, with Town/Rig, roles, convoys, queues, mail, observability and human control surface.
- `C2_pwg_to_process_profiles.md` used to clarify BMAD/GSD boundary: process profiles set phases/roles/documents; PWG preserves their consequences as work state.
- `C4_execution_runtime_to_pwg.md` reinforced durable-execution/runtime boundary.


## P03 inventory update

Primary dossier inventory confirms that the article has enough anchors for the initial concept contract. The strongest transferred anchors are: durable identity, dependency readiness, owner/handoff, gate, prime, recovery, source-state lifecycle, durable-execution boundary, parallelism boundary and failure modes.

Not transferred by design: detailed Beads troubleshooting/debug flags, full Gas Town operating model, full GSD/BMAD exposition, full TS-loop implementation schema and full parallel-source protocol. These remain available as background, not article obligations.

Future source strengthening should focus on exact Beads hook/prime lifecycle and perhaps one clean visual explanation of work graph vs execution graph; it should not become a total coverage matrix.


## P04 source-depth update

`A1_change_not_prompt.md`, `A4_persistent_work_graph_boundary.md` and `B2_pwg_contribution.md` were used to strengthen the opening problem: prompt/chat/transcript/TODO/issue/local plan each preserve some surface but lose durable work identity, dependencies, ready-state, claim/owner, gates, evidence, compact recovery and history.


## P05 source-depth update

`C1_specification_to_pwg.md` and `C3_pwg_to_evidence.md` were used to make the minimal work item properties operate as a mechanism: specification/work signal → work item → ready queue → claim → gate/control condition → handoff → prime/recovery → evidence-backed state transition.


## P06 Beads anchor update

Beads anchor strengthened with concrete mechanism surface: Dolt storage/history/branch-merge-diff-push-pull, hash IDs, `bd ready`, `bd blocked`, `bd graph`, pin/claim/handoff, `bd gate`, `bd prime`, routing/hydration and operational caveats. Local SVG asset inserted as `fig-pwg-beads-task-graph-memory`.


## P07 boundary update

Boundary table added to the article: issue tracker, durable execution, CRDT/shared editor, STORM/write-time validation, MAST-like failure analysis and Gas Town each answer different questions than PWG. This uses PWG dossier, Gas Town dossier, B3 and C4.


## P08 document-process transfer update

Document-process workflow strengthened as second proof of concept: job/pass/gate/prime/recovery, source states, worker returns, citation audit, synthesis pass and safe parallel source protocol were added as portable PWG primitives. The article explicitly states this is not a TypeScript implementation plan.


## P09 free material update

Weakest fact area selected: durable state schema semantics. Added a minimal work item schema and explicit state-transition interpretation (`ready`, `claimed`, `review`, `recovering`) plus forbidden transitions. This was derived from the PWG dossier's job/pass/gate/recovery and Beads-ready semantics.

## P10 free material update

`B2_pwg_contribution.md`, `C4_execution_runtime_to_pwg.md` and `C3_pwg_to_evidence.md` were used to strengthen conceptual separation among work graph, execution graph, evidence layer, source state and shared-editing coordination. No new external source was introduced; the pass reorganized already sourced boundary material into a five-layer state table.

## P11 local visual asset update

Local asset pass used only files explicitly listed in P11. `beads-task-graph-memory.svg` was already inserted in P06 and remains the primary PWG mechanism visual. `gastown-architecture.svg` was inserted as a boundary visual for the upper Gas Town operating environment. `anthropic-multi-agent-process-diagram.webp` was inserted as an adjacent multi-agent research-process visual supporting the safe parallel worker-return / citation-audit / synthesis-pass explanation. `gastown-basic-workflow.svg` and `anthropic-multi-agent-research-architecture.webp` were not inserted because they would duplicate already-covered operational or architectural context without adding to the PWG-specific argument.

## P12 external visual candidate update

P12 read the PWG dossier illustration-candidate section and `EXTERNAL_REAL_IMAGE_CANDIDATES.md`. No new textual fact source was added and no external image placeholder was inserted. Image dispositions were recorded in the image plan and external image queue; the already-local Anthropic multi-agent process asset supersedes the corresponding external candidate.

## P13 synthetic visual update

P13 added one authorial synthetic figure, `fig-pwg-work-state-hub`, based only on the current article and image plan. No new source or external image was introduced.

## P14 self-contained article update

`00_spine_map.md` and `B2_pwg_contribution.md` were used to add a self-contained lifecycle map for readers who arrive directly at the PWG/Beads article. The new section explains where PWG sits between intention/specification, execution, evidence and acceptance without requiring the reader to have read the general theory.

## P15 mechanism/failure update

P15 used the current degradation/duplication audit to expand PWG-specific failure modes: stale graph, dependency removal without evidence, false control from owner/claim, `ready` not meaning safe, `prime` not restoring all meaning, bureaucratic gates, graph-gaming behavior and premature storage complexity.

## P16 theory-link update

P16 used A4/A5/A7/A8/A9 and C1/C2/C3/C4 to strengthen the final theory-link section. The article now maps PWG to semantic questions in the broader theory: prompt-to-change, process-to-state, observation-to-evidence, authority-to-act vs authority-to-complete, runtime-to-work and post-result repair.

## P17 language pass note

P17 performed a Russian-language normalization pass over the main article. It did not add new sources or factual claims; it repaired terminology, code-fragment formatting and source-specific link text where prior wording risked confusing commands, URLs or field names with translated prose.

## P19 source usage note

P19 did not add new sources. It made the article's existing source-backed mechanism more explicit by adding a behavioral control test and clarifying that the Beads table is a mechanism check rather than a product feature tour.

## P21 source usage note

`work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` was used to sharpen the Gas Town boundary: PWG is the durable state of individual work; Gas Town is the organizational-operational layer around many such works.

## P23 companion sync

P23 reconciled the companion set after the public-structure pass. No new article claim was added. The current source map is:

| Source group | Current article role | Companion status |
| --- | --- | --- |
| PWG mechanism dossier | Core PWG definition, Beads anchor, dependency readiness, owner/claim/handoff, gates, prime/recovery, source state, document-process transfer and failure modes | fully represented in article and ledger |
| A4 / B2 / C1 / C3 / C4 / C5 / A10 | Boundary, lifecycle, evidence, execution-runtime separation, atlas-article style and mode-selection support | represented in article and theory-link map |
| A5 / A7 / A8 / A9 / `00_spine_map.md` | Final theory-navigation links: process-to-state, observation/evidence, authority split and lifecycle repair | represented in the final theory-link section, not expanded into duplicate theory prose |
| B3 and Gas Town dossier | Upper boundary: PWG is durable state of one work unit; Gas Town is operating environment around many works | represented in Gas Town section, image plan and audit |
| Local assets in `content/assets/theory-images` | Beads mechanism visual, Gas Town boundary visual and Anthropic multi-agent process visual | represented in image plan; no additional local asset needed |
| External visual candidates | GitHub/Linear/MAST/extra Beads/Gas Town/process screenshots | recorded in external image queue; intentionally kept out of inline article |

Obsolete debts removed from the active question set: B3/C2 audit, local-image decision, P13 synthetic choice and external screenshot decision. Remaining checks are final style, path/package integrity and source-link hygiene.

## Final source-usage check

Final check found no unresolved source-use blocker. Key source-backed claims remain in the article body rather than only in the ledger: Beads mechanics, dependency readiness, gate/prime/recovery, source state, durable-execution boundary, Gas Town boundary, parallelism boundary, document-process transfer and failure modes.

The final pass removed the public bottom `Внешние изображения для asset-pass` section because no inline external-real placeholder remains in this version. External candidate dispositions stay in the image plan and external queue.
