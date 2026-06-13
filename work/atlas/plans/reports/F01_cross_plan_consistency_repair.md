# F01 cross-plan consistency and anti-template repair

## Scope

F01 read the created atlas target-group plans, per-article reports and ledger, then checked cross-plan consistency. It did not write any atlas article and did not build article-writing packages.

## Article set

All current plans are dossier-backed and match ledger rows after normalization of preliminary ids. Current article ids:

- `adr_method`
- `bmad_method`
- `constitutional_sdd`
- `gas_town`
- `gsd_open_gsd`
- `kiro_specs`
- `persistent_work_graph`
- `spdd_method`
- `spec_kit_method`
- `tdad_comparative`

## Automated consistency checks

- Plans found: 10.
- Ledger article rows parsed: 10.
- Plan ids missing in ledger: none.
- Ledger ids without plan file: none.
- `adr_method`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `bmad_method`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `constitutional_sdd`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `gas_town`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `gsd_open_gsd`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `kiro_specs`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `persistent_work_graph`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `spdd_method`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `spec_kit_method`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.
- `tdad_comparative`: missing read-only paths `0`; missing required output refs `0`; general editorial passes present `True`; C5/A10 mentioned `True`; readiness status present `True`.

## Repairs made

- `spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`: repaired stale top status from post-S03 wording to `ready_for_package_manufacture_after_manual_review`.
- `spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`: normalized neighboring article ids from preliminary `spec_kit` / `tdad` / `adr` to current `spec_kit_method` / `tdad_comparative` / `adr_method`.
- `spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`: repaired stale S03 wording that described S04/S05 as remaining future work even though readiness had already been stamped.

## Cross-plan conclusions

- No article topic was found without a dossier-backed basis.
- Volume/source/image rules are materially consistent: no internal length limits; source-depth/free-expansion/visual/concept/editorial/language/style/final verification are present across plans.
- Companion roles use the shared output set: article file, source usage, source transfer ledger, image plan, external image queue, open questions, theory links, degradation/duplication audit and readiness report.
- C5/A10 are consistently treated as later sync debts, not blockers.
- Boundaries are consistent at the load-bearing points: SPDD/Spec Kit/Kiro/Constitutional SDD/TDAD/ADR stay in specification/decision cluster; PWG stays as durable work substrate; Gas Town stays as organizational/operational environment; BMAD/GSD stay method/process profiles.
- The plans are not mechanical copies of the blueprint: each has article-specific source-depth zones, degradation gates, visual candidates and neighboring-boundary risks. Older early plans use a grouped prompt-queue style while later plans use a more explicit pass-by-pass style, but both preserve the required 25-pass structure and final verification.

## Remaining known debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` is still missing from the snapshot; this remains a global provenance debt rather than an article-specific blocker.
- Human review is still recommended before manufacturing article-writing packages, especially for tier labels and boundary overlaps after C5/A10 exist.
