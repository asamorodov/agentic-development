# Manufacture report: `spdd_method` atlas article target plan

Status: `ready_for_package_manufacture_after_manual_review`.

## Current state after post-import repair

`spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` was created by the atlas article target-plan manufactury run and then manually repaired after review. The current plan should be treated as the active SPDD/OpenSPDD article target-group plan.

## Main repairs after review

- Removed manufactury-run history from the target plan itself; provenance remains in reports.
- Sharpened the central article logic: SPDD is not merely structured prompting, but a way to make feature intent a reviewable, checkable, syncable artifact.
- Made the central risk explicit: REASONS Canvas can be coherent and persuasive while still being wrong, stale, or too costly for the scale of change.
- Separated Fowler SPDD from OpenSPDD: conceptual frame versus operational system of commands/templates/sync/review.
- Turned failure modes into an article-critical axis rather than a secondary caveat list.
- Rewrote source-depth prompts to be SPDD-specific rather than generic atlas-plan prompts.
- Cleaned visual passes: local assets, external candidates and synthetic figures now have separate roles without repeated boilerplate in P11–P13.
- Replaced stale default C5/A10 sync debts with current read-only context.

## Remaining manual-review points

- Human review should confirm the article tier: `core concept / method article`.
- Human review should approve the boundary between SPDD/OpenSPDD and neighboring articles: Spec Kit, Kiro, Constitutional SDD, TDAD, ADR and Persistent Work Graph.
- Article-writing package manufacture is allowed after that review; the package itself has not been built in this repair.
