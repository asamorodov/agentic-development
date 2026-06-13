# Persistent Work Graph — image plan

Status: final package complete. Current article uses one synthetic figure and three local assets; all external candidates remain dispositioned outside the public body.

| Candidate ID | Classification | Intended role | Current disposition |
| --- | --- | --- | --- |
| `fig-persistent-work-graph-core` | `synthetic_figure` | Minimal node: dependency, owner, gate, handoff, evidence, prime, history | Keep for later synthetic pass. |
| `fig-beads-task-graph-memory` | `local_image_asset` candidate | Practical anchor for Beads/PWG memory and task graph | Not inserted in P01; P11 must inspect local asset index and asset file. |
| `fig-beads-ready-queue` | `synthetic_figure` | Explain ready/blocked queue from dependency graph | Candidate; may be more useful than a generic node diagram. |
| `fig-bd-prime-rehydration` | `synthetic_figure` | SessionStart/PostCompact → prime → compact work truth | Candidate if prime section remains central. |
| `fig-gates-as-durable-waits` | `synthetic_figure` | Human/timer/CI/PR/bead gates as durable waits | Candidate if gate section needs visual support. |
| `fig-work-graph-vs-execution-graph` | `synthetic_figure` | Separate work graph, execution graph, prime, evidence package | New editorial candidate from P01; useful for boundary clarity. |
| `fig-multi-pass-document-workflow-job-pass-gate` | `synthetic_figure` | Job/pass/gate/prime/recovery schema for document process | Candidate if article keeps applied design section. |

## P01 visual rule

No external real image candidate is used inline. No local asset is inserted until visual asset pass confirms path, relevance and rights/status.


## P06 local asset decision

| Candidate ID | Classification | Decision | Rationale |
| --- | --- | --- | --- |
| `fig-pwg-beads-task-graph-memory` | `local_image_asset` | inserted inline in `Beads как якорь, но не рецепт` | Local SVG exists at `content/assets/theory-images/beads-task-graph-memory.svg`; it directly supports Beads as dependency-aware task graph memory without using an external screenshot. |


## P08 synthetic candidate update

`fig-multi-pass-document-workflow-job-pass-gate` remains a useful synthetic candidate. The article now has enough structure to support a compact diagram: job → pass → worker returns → citation audit → synthesis pass → canonical article, with gates and recovery paths. Defer actual diagram to P13.


## P09 image candidate update

The new minimal schema block may reduce need for a separate synthetic table figure. Keep `fig-persistent-work-graph-core` as optional if later editorial pass finds the schema too dense.

## P10 image-plan update

The new five-layer table suggests a possible synthetic diagram: work graph as central coordination layer linking execution graph, evidence layer, source state and shared-editing coordination by stable IDs. No image was inserted in P10; hold this as a synthetic figure candidate if P13 decides the article needs one more explanatory visual.

## P11 local asset decisions

| Asset | Classification | Decision | Rationale |
| --- | --- | --- | --- |
| `content/assets/theory-images/beads-task-graph-memory.svg` | `local_image_asset` | keep inserted as `fig-pwg-beads-task-graph-memory` | Directly supports the core Beads/PWG mechanism: task graph, dependencies, claim and prime. |
| `content/assets/theory-images/gastown-architecture.svg` | `local_image_asset` | inserted as `fig-pwg-gastown-architecture-boundary` | Useful boundary visual: shows the upper Gas Town operating environment so PWG remains scoped as a lower work-state layer. |
| `content/assets/theory-images/gastown-basic-workflow.svg` | `local_image_asset` | not inserted | Too operational for this article; it would pull the text toward Gas Town workflow rather than PWG. |
| `content/assets/theory-images/anthropic-multi-agent-process-diagram.webp` | `local_image_asset` | inserted as `fig-pwg-anthropic-multi-agent-process` | Supports safe parallel source protocol, worker returns, citation audit and synthesis pass. |
| `content/assets/theory-images/anthropic-multi-agent-research-architecture.webp` | `local_image_asset` | not inserted | Redundant once the more process-oriented Anthropic diagram is used; the high-level architecture would add visual weight without a new PWG distinction. |

## P12 external real image candidate dispositions

P12 checked the PWG dossier illustration list and `EXTERNAL_REAL_IMAGE_CANDIDATES.md`. No new external placeholder was inserted into the article: the most useful real external candidate for this article, Anthropic's multi-agent process diagram, is already present locally and was inserted in P11. Baseline product screenshots would add visual weight without improving the PWG argument, so they are rejected or left as queue-only for a different article.

| Candidate | Candidate kind | Disposition | Reason |
| --- | --- | --- | --- |
| `fig-persistent-work-graph-core` | synthetic | `deferred` | Good synthetic candidate for P13, but not an external image. |
| `fig-beads-dolt-stack` | external/synthetic-redraw candidate | `deferred` | May be useful as a synthetic stack diagram, but local Beads graph already anchors the article. |
| `fig-beads-ready-queue` / `ext-beads-ready-queue` | synthetic-redraw preferred | `deferred` | Useful if P13 replaces a table with a compact ready/blocked diagram. |
| `fig-bd-prime-rehydration` | synthetic | `deferred` | Optional synthetic figure; current prose is sufficient. |
| `fig-gates-as-durable-waits` | synthetic | `deferred` | Optional synthetic figure; no external screenshot needed. |
| `fig-routing-hydration` | synthetic | `rejected` | Routing is secondary in this article; detailed figure would overfit to Beads. |
| `fig-taskmaster-tasks-json` | source excerpt/synthetic | `rejected` | Taskmaster remains a lightweight contrast, not a visual focus. |
| `fig-taskmaster-loop` | synthetic | `rejected` | Would shift article toward Taskmaster loop mechanics. |
| `fig-langgraph-checkpoint-thread` | external/synthetic-redraw candidate | `deferred` | Potential future boundary diagram, but five-layer table now covers the distinction. |
| `fig-github-subissues-baseline` / `ext-pwg-github-subissues` | external real candidate | `rejected` | Baseline issue hierarchy is already explained; screenshot would be low-value and rights-check heavy. |
| `fig-linear-blocked-flag-baseline` / `ext-pwg-linear-blocked-flag` | external real candidate | `rejected` | Same reason as GitHub baseline: useful baseline fact, weak article image. |
| `fig-multi-pass-document-workflow-future-state` | synthetic | `deferred` | Strong P13 candidate if synthetic visual pass keeps one document-process diagram. |
| `fig-multi-pass-document-workflow-job-pass-state-machine` | synthetic | `deferred` | Useful but potentially redundant with schema/table. |
| `fig-multi-pass-document-workflow-source-state-flow` | synthetic | `deferred` | Good candidate only if source-state explanation needs visual relief. |
| `fig-aegis-permission-gate` | external/synthetic-redraw candidate | `rejected` | AEGIS is a permissions boundary example, not a central PWG visual. |
| `fig-skillnb-gated-workflow` | external/synthetic-redraw candidate | `rejected` | SKILL.nb is an adjacent gate analogy; visual would dilute scope. |
| `fig-codecrdt-observation-driven-coordination` | synthetic | `deferred` | Could support shared-editing boundary, but current table/prose is enough. |
| `fig-codecrdt-speedup-tradeoff` | synthetic mini-chart | `rejected` | Metrics are a warning, not a central quantitative argument. |
| `fig-storm-write-time-validation` | synthetic | `deferred` | Possible future boundary diagram; no external image required. |
| `fig-mast-failure-distribution` / `ext-pwg-mast-failure-distribution` | external real candidate | `rejected` | MAST failure taxonomy is only a boundary warning here. |
| `fig-parallel-loop-read-snapshot` | synthetic | `deferred` | Stronger as a P13 synthetic candidate than as an external image. |
| `fig-anthropic-multi-agent-research-process` / `ext-pwg-anthropic-multi-agent-process` | external real candidate already local | `superseded_by_local_asset` | Inserted in P11 from `content/assets/theory-images/anthropic-multi-agent-process-diagram.webp`. |
| `fig-safe-parallel-source-protocol` | synthetic | `deferred` | Strong candidate for P13 if the article needs one authorial protocol diagram. |
| `fig-source-claim-lifecycle` | synthetic | `deferred` | Optional; current source-state flow text may be enough. |
| `fig-worktree-isolated-source-workers` | synthetic | `rejected` | Worktree isolation is a boundary detail, not a PWG core image. |
| `fig-citation-audit-gate` | synthetic | `deferred` | Could be merged into `fig-safe-parallel-source-protocol`. |
| `fig-synthesis-pass-conflict-matrix` | synthetic | `deferred` | Candidate for an editorial table/diagram, not an external image. |
| `ext-gastown-two-tier-beads-flow` | external real candidate | `external_queue_only` | Potentially useful for a Gas Town / Beads-specific article; current PWG article is already anchored by local Beads and Gas Town visuals. |

## P13 synthetic figure decision

Created exactly one synthetic figure: `fig-pwg-work-state-hub`. It addresses the strongest remaining visual need after P10: state of work vs state of execution, evidence, source lifecycle and shared-editing coordination. Deferred synthetic candidates for job/pass/gate/source-state and ready queue remain in the plan but were not created to avoid visual overproduction.

## P14 image-plan update

The new self-contained lifecycle section uses a text sequence rather than another figure. No image changes required.

## P15 image-plan update

No figure changes. The expanded failure modes are textual; turning them into a diagram would add visual noise.

## P16 image-plan update

No figure change. Theory back-links are expressed as a semantic table rather than a new image.

## P20 image-plan audit

No image changes. The current four visuals still have distinct roles: one synthetic state-hub diagram, one Beads mechanism anchor, one Gas Town boundary visual and one parallel-source-process visual. Additional ready-queue or document-process diagrams remain deferred because they would likely duplicate the schema/table material.

## P22 public structure image note

Added bottom section `Внешние изображения для asset-pass` to the article. It states that no additional external images are needed and explains why product screenshots or extra boundary diagrams would dilute the core PWG argument. Current inline visuals remain unchanged.

## P23 current image set

Current inline visuals are intentionally limited to four distinct roles:

| Figure id | Kind | Role in article | Current decision |
| --- | --- | --- | --- |
| `fig-pwg-work-state-hub` | authorial synthetic figure | Separates PWG work state from execution run, evidence package, source lifecycle and shared-editing coordination | keep |
| `fig-pwg-beads-task-graph-memory` | local SVG asset | Concrete mechanism anchor for dependency graph, readiness and continuation memory | keep |
| `fig-pwg-gastown-architecture-boundary` | local SVG asset | Upper-boundary reminder: Gas Town is broader than PWG | keep, caption-boundary only |
| `fig-pwg-anthropic-multi-agent-process` | local WEBP asset | Adjacent parallel-worker process reminder for worker returns, audit and synthesis | keep |

No additional external image is needed for this version. Product screenshots for GitHub/Linear, additional Beads screenshots, MAST/CRDT/STORM figures and extra workflow diagrams remain out because they would turn a concept article into a survey or product comparison.

## Final image-package decision

Final package decision: keep four inline figures and remove the public bottom asset-pass section because this article version has no inline `external_real_image_candidate` placeholder. The image candidate dispositions remain in this file and in `persistent_work_graph_external_image_queue.md`.

Path check passed for packaged local assets:

| Asset | Article src | Package action |
| --- | --- | --- |
| `beads-task-graph-memory.svg` | `../../../content/assets/theory-images/beads-task-graph-memory.svg` | included |
| `gastown-architecture.svg` | `../../../content/assets/theory-images/gastown-architecture.svg` | included |
| `anthropic-multi-agent-process-diagram.webp` | `../../../content/assets/theory-images/anthropic-multi-agent-process-diagram.webp` | included |
