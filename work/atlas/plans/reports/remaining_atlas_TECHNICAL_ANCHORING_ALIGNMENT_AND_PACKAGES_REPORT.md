# Remaining atlas target plans — technical anchoring alignment and package rebuild

Date: 2026-06-13

Baseline: user-provided full repository snapshot `git(10).zip`.

## Scope

This report covers the six canonical atlas target plans that still predated the accepted technical-anchoring/style-tail blueprint after SPDD, Gas Town, ADR and PWG had already been aligned:

- `work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`

The experimental SPDD rollback plan under `work/atlas/target-group-plans/experiments/` was not changed.

## Applied plan changes

Each plan was aligned with the current `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`:

- removed the old hard `coverage matrix / relevant but untransferred` direction;
- converted `P03` to `dossier inventory` without total dossier coverage proof;
- removed repeated `transfer-audit` endings from `P04`–`P08`;
- kept technical anchoring as a short, soft orientation: key claims should have concrete technical anchors when otherwise they become generic prose;
- reordered the tail to the accepted sequence:
  - `P17` — language pass 1;
  - `P18` — language pass 2;
  - `P19`–`P21` — general editorial/repair passes;
  - `P22` — public/article structure and entry-sequence pass;
  - `P23` — companion sync;
  - `P24` — style defect audit;
  - `P25` — selective natural rewrite;
  - `P26` — guarded final human technical style pass;
  - `Final` — final verification and packaging.

## Rebuilt packages

The following self-contained executor packages were rebuilt and written to `work/atlas/packages/`:

- `work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip`
- `work/atlas/packages/kiro_specs_ATLAS_ARTICLE.zip`
- `work/atlas/packages/constitutional_sdd_ATLAS_ARTICLE.zip`
- `work/atlas/packages/tdad_comparative_ATLAS_ARTICLE.zip`
- `work/atlas/packages/gsd_open_gsd_ATLAS_ARTICLE.zip`
- `work/atlas/packages/bmad_method_ATLAS_ARTICLE.zip`

Equivalent artifact copies were also produced under `/mnt/data/` with `_technical_anchoring` names.

## Checks performed

For each of the six packages:

- `unzip -tq` passed;
- first runner transition passed and emitted `01_P01_primary_article_draft.md`;
- second runner transition passed after a minimal article stub and emitted `02_P02_article_contract_and_boundaries.md`;
- payload audit found 27 records (`P01`–`P26` + `Final`);
- payload order contains the accepted tail:
  - `17_P17_language_pass_1.md`;
  - `18_P18_language_pass_2.md`;
  - `24_P24_style_defect_audit.md`;
  - `25_P25_selective_natural_rewrite.md`;
  - `26_P26_guarded_final_style.md`;
  - `27_Final_final_verification.md`.

A canonical-plan scan also confirmed that all ten canonical atlas target plans now have `P26` and the accepted tail, and none of them retain old canonical `P03 coverage matrix`, `transfer-audit`, `P22 language pass`, or `P24/P25 old style pass` markers.

## Notes

The rebuild changes executor packages only. It does not execute the article-writing packages and does not create completed article files under `work/atlas/articles/`.

The current decision is to keep the accepted style/technical-anchoring blueprint stable rather than add more process rules.
