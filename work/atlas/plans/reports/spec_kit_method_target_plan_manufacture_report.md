# Manufacture report: `spec_kit_method` atlas article target plan

Status: `ready_for_package_manufacture_after_manual_review`.

## S01 mode

S01 used `create_new`: `work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` did not exist. No manual user edits were overwritten.

## Problems found and repaired in S02–S04

### S02

Problems:

- The primary risk was that Spec Kit could become either a generic SDD overview or a CLI/command reference.
- The article contract did not yet sharply explain the reader path from feature intent to specification, plan, tasks, implementation, evidence and repair.
- Visual policy needed to distinguish local contextual SDD assets from Spec Kit-specific external real image candidates.

Changes:

- Sharpened the article contract around feature intent → specification → plan/tasks → implementation/evidence.
- Kept the full 25-pass queue and justified it specifically for Spec Kit.
- Added article-specific source-depth priorities: official docs, repository surface, command templates, scripts, integrations, constitution/checklists, human confirmations, verification, caveats and boundaries.
- Added explicit final failure modes: generic SDD overview and command dump without lifecycle explanation.

### S03

Problems:

- The S02 plan was structurally strong but could still be executed mechanically.
- It lacked a separate compositional layer describing the desired shape of the future article.
- Some English service-language remained in prose.

Changes:

- Added `Предполагаемая форма будущей статьи (не текст статьи)`.
- Defined the future article's explanatory arc: why Spec Kit exists, what mechanism it provides, where state appears, where human judgment remains, what it does not guarantee, and how it differs from neighboring methods.
- Cleaned some English glue while preserving tool names, command names and file names.

### S04

Problems:

- Some companion outputs were declared but not strongly required by the corresponding future passes.
- The visual pass needed stronger guarantees around image plan, external image queue and preservation of real images.
- Final verification needed to check concrete files and companion names, not only conceptual readiness.

Changes:

- Strengthened P04–P08 to update explicit source companion files.
- Strengthened P11–P13 to require `spec_kit_method_image_plan.md` and `spec_kit_method_external_image_queue.md` and to protect real screenshots/diagrams from textual replacement.
- Strengthened P17–P19, P21 and Final verification around companion sync, degradation audit, readiness report and real output checks.
- Added `S04 integrated guardrails`.

## Remaining debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` is missing from the repo snapshot. This weakens provenance of the global known set but does not block this article plan because S01 explicitly specified `spec_kit_method`.
- `C5 sync pending`: after C5/article map exists, sync article tier, boundary, semantic back-links and atlas placement.
- `A10 sync pending`: after A10 exists, sync reader routing and mode-selection placement if relevant.
- Human review should confirm that `method / tool-form article` is the desired tier and that Spec Kit deserves the full 25-pass queue.

## Package manufacture allowance

Executor package manufacture is allowed after manual review. The plan is mechanically buildable: exact read-only paths were checked in the current snapshot; no missing article-specific read-only file was found.

## Sync pass requirement

Later sync pass required after C5/A10 if those fragments introduce article-map tiers, semantic back-links, or mode-selection decisions that affect this article.
