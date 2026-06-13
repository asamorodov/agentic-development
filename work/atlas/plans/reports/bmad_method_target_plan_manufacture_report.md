# Manufacture report: `bmad_method` atlas article target plan

Status: `ready_for_package_manufacture_after_manual_review`.

## S01 mode

S01 used `create_new`: `work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` did not exist as a valid target plan for the explicit worksheet id. No manual user edits were overwritten.

The preliminary ledger used older id `bmad`; this report normalizes it to `bmad_method`.

## Problems found and repaired in S02–S04

### S02

Problems:

- The S01 plan needed clearer justification for why BMAD deserves the full atlas queue.
- The article contract risked becoming broad feature coverage rather than an explanation of the file-mediated lifecycle mechanism.
- Visual requirements needed stronger protection for real workflow/status/review diagrams and screenshots.
- Final verification needed sharper BMAD-specific blockers.

Changes:

- Added central explanation around document/status → next-step context → human decision → evidence/repair.
- Added `S02 targeted strengthening` with queue-fit judgment, source-depth partition, visual requirements, editorial degradation gates and bundle requirement.
- Strengthened final verification blockers around lifecycle/evidence mechanics and visual provenance.

### S03

Problems:

- BMAD could become several disconnected mini-articles: Quick Flow, full Method, brownfield documentation, TEA/Enterprise, roles/personas and review tools.
- The plan needed one composition principle to prevent feature-list drift.
- Applicability needed explicit treatment.

Changes:

- Added `S03 free editorial strengthening`.
- Added the composition principle: every BMAD detail must serve a lifecycle function — next-step input, narrowed implementation context, state, human gate, evidence or repair path.
- Expanded intended article structure with an applicability layer.
- Strengthened final blockers against disconnected subtopics and uncontrasted process depths.

### S04

Problems:

- The plan needed an integrated guardrail section tying path grounding, output naming, visual treatment, companion synchronization and final verification.
- External-real image candidates needed all required recording locations.
- Source-depth and free-expansion requirements needed a stronger anti-overview guardrail.

Changes:

- Added `S04 integrated guardrails`.
- Added path/output audit statements.
- Strengthened companion invariants around image candidates and source ledger updates.
- Confirmed BMAD-specific adaptation rather than mechanical blueprint copying.

## Remaining debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` is missing from the repo snapshot. This weakens provenance of the global known set but does not block this article plan because S01 explicitly specified `bmad_method`.
- `C5 sync pending`: after C5/article map exists, sync article tier, boundary, semantic back-links and atlas placement.
- `A10 sync pending`: after A10 exists, sync reader routing and mode-selection placement if relevant.
- Human review should confirm that `method article` is the desired tier or whether BMAD should later receive a hybrid `method article + process profile` taxonomy label.

## Package manufacture allowance

Executor package manufacture is allowed after manual review. The plan is mechanically buildable: exact read-only paths were checked in the current snapshot; no missing article-specific read-only file was found.

## Sync pass requirement

Later sync pass required after C5/A10 if those fragments introduce article-map tiers, semantic back-links, boundaries or mode-selection decisions that affect this article.
