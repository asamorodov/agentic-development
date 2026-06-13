# S02 targeted strengthening note: `spdd_method`

Mode: `repair_existing`.

## Problems found

- The S01 plan was structurally strong but did not yet state explicitly why the full 25-pass queue fits this specific article.
- The reader question could still be read too broadly as “what is SPDD?” rather than the sharper engineering question about making feature intent explicit before generation and keeping it reviewable/synchronizable afterwards.
- Visual handling needed a stronger SPDD-specific instruction because local Fowler-derived assets already exist and should be treated as first-class article material.
- Final verification needed article-specific anti-drift checks: generic structured prompting, B1/A3 duplication, command-reference drift, evidence/PWG drift and image-gallery drift.
- G03 path conventions still contained the earlier inferred `spdd` id; the explicit S01 worksheet uses `spdd_method`.

## Decisions

- Keep the full 25-pass blueprint. It fits SPDD because this article has a rich primary source, OpenSPDD implementation details, local visual assets, evidence/review mechanics, sync failure modes and several high-risk boundaries.
- Treat source-depth passes as weighted rather than evenly distributed: Fowler/OpenSPDD/failure modes are central; neighboring dossiers are boundary material.
- Keep C5/A10 as later sync debts, not blockers.
- Align path conventions to `spdd_method` for this article id.

## Changes made

- Added a targeted S02 judgment under the future prompt queue.
- Added `S02 targeted strengthening: article-specific requirements` to the plan.
- Strengthened reader question, source-depth emphasis, visual/assets emphasis and final verification criteria.
- Updated `work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PATHS.md` from `spdd` to `spdd_method` to match the explicit worksheet id.

No article text was written. No article-writing package was built.
