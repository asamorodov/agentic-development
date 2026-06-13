# Persistent Work Graph — external image queue

Status: final package complete. No external image is inline; queue records rejected/deferred/superseded candidates for future asset-pass work.

| Candidate | Source basis | Proposed disposition |
| --- | --- | --- |
| Beads architecture diagram or screenshot | Beads Architecture / docs | Hold for P12; likely safer to use synthetic diagram rather than screenshot unless rights/status clear. |
| GitHub sub-issues screenshot | GitHub docs | Hold for P12; baseline comparison only, not central enough for inline use yet. |
| Linear blocked/blocking screenshot | Linear docs | Hold for P12; baseline comparison only. |
| LangGraph checkpoint/thread diagram | LangGraph docs | Hold for P12; maybe synthesize instead. |
| STORM read/write validation figure | STORM paper/repo | Hold for P12; boundary topic, maybe synthesize. |
| CodeCRDT coordination diagram/results | CodeCRDT paper | Hold for P12; boundary topic, likely not core enough. |

P01 did not perform web/right checks.

## P10 external image queue update

No external image candidate was added. The layer-separation material is better served by a synthetic diagram or table than by a product screenshot.

## P11 local asset note

No external image was added to the queue. P11 only used local assets already present in `content/assets/theory-images`. Rejected local assets are recorded in `persistent_work_graph_image_plan.md` rather than here.

## P12 external real image candidate queue and refusals

No external placeholder was inserted inline in P12. The article already uses local assets for the two strongest real visual anchors: Beads task graph memory and Anthropic multi-agent process.

| Candidate | Disposition | Article action | Notes |
| --- | --- | --- | --- |
| `ext-pwg-anthropic-multi-agent-process` | `superseded_by_local_asset` | already inserted as `fig-pwg-anthropic-multi-agent-process` | Local WEBP exists and is more reliable than adding a new external placeholder. |
| `ext-pwg-github-subissues` | `rejected` | no inline figure | Baseline screenshot would not add enough to the article's concept. |
| `ext-pwg-linear-blocked-flag` | `rejected` | no inline figure | Same baseline-screenshot issue. |
| `ext-pwg-mast-failure-distribution` | `rejected` | no inline figure | MAST is boundary evidence, not a central visual claim. |
| `ext-beads-ready-queue` | `deferred` | no external figure | Prefer synthetic ready/blocked diagram if needed. |
| `ext-gastown-two-tier-beads-flow` | `external_queue_only` | no inline figure in PWG article | Keep for Gas Town/Beads-focused visual work, not this article. |

## P13 external queue update

No external image was added. P13 used one synthetic inline figure and left external-image dispositions from P12 unchanged.

## P14 external queue update

No change. The self-contained lifecycle explanation did not introduce external image needs.

## P15 external queue update

No change. Failure-mode expansion did not add external image needs.

## P16 external queue update

No change. Theory-link reinforcement did not introduce external image needs.

## P22 bottom-section sync

The article now includes a bottom section `Внешние изображения для asset-pass`. It keeps all external real image candidates out of the public body for this version and points future asset-pass work back to this queue rather than adding screenshots inline.

## P23 active external disposition

The public article's bottom asset-pass section now matches this queue: no additional external image should be inserted in the current version.

| Candidate group | Current disposition | Reason |
| --- | --- | --- |
| GitHub / Linear screenshots | rejected | Useful only as baseline product examples; the article already explains why issue graphs are insufficient. |
| Extra Beads screenshots or architecture captures | rejected/deferred | Beads already has the local mechanism visual; more screenshots would shift focus to product documentation. |
| LangGraph / Temporal / DBOS / Restate diagrams | deferred | Runtime boundary is textual/table-driven here; adding diagrams would create a durable-execution survey. |
| CodeCRDT / STORM / MAST figures | rejected/deferred | Boundary warnings are present, but metric or validation figures are not central PWG evidence. |
| Anthropic multi-agent process | superseded by local asset | The local WEBP is already inline and sufficient. |
| Gas Town two-tier or workflow visuals | external-queue only | Better suited to a Gas Town or Beads-specific visual article, not this PWG concept article. |

## Final external-image decision

Final article body does not include a public asset-pass appendix. That appendix would be appropriate only for inline external-real placeholders. Since all external candidates are rejected, deferred, external-queue-only or superseded by local assets, the queue remains here as companion metadata.
