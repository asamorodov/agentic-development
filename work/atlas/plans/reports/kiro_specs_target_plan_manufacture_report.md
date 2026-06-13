# Manufacture report: `kiro_specs` atlas article target plan

Status: `ready_for_package_manufacture_after_manual_review`.

## S01 mode

S01 used `create_new`: `work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` did not exist. No manual user edits were overwritten.

## Problems found and repaired in S02–S04

### S02

Problems:

- The plan could have produced a general Kiro product overview instead of an atlas article about Specs as lifecycle form.
- The article contract needed stronger distinction between product surface and lifecycle mechanism.
- Source-depth priorities needed to separate Feature Specs, workflow variants, context/execution, verification/control and governance.

Changes:

- Rewrote the article contract around IDE/Web/CLI lifecycle for complex feature/bugfix/requirements work.
- Preserved the full 25-pass queue and justified it specifically for Kiro.
- Added final failure modes: generic Kiro overview and UI/command inventory without lifecycle explanation.

### S03

Problems:

- Kiro has many product surfaces, so a mechanically complete pass could still become a feature catalogue.
- The plan lacked a simple editorial rule that forces every product detail to serve the lifecycle explanation.

Changes:

- Added `Главный редакторский риск и способ его снять`.
- Added the rule that every source addition must show lifecycle mechanism, not merely product capability.
- Added `S03 editorial strengthening`.

### S04

Problems:

- Some companion outputs and visual outputs needed stronger required-output language.
- The plan needed explicit guardrails for real Kiro-specific UI/images and exact final-file checks.

Changes:

- Strengthened P04–P08 source companion updates.
- Strengthened P11–P13 around image plan, external image queue and real screenshots/diagrams.
- Strengthened P17–P19, P21 and final verification.
- Added `S04 integrated guardrails`.

## Remaining debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` is missing from the repo snapshot. This weakens provenance of the global known set but does not block this article plan because S01 explicitly specified `kiro_specs`.
- `C5 sync pending`: after C5/article map exists, sync article tier, boundary, semantic back-links and atlas placement.
- `A10 sync pending`: after A10 exists, sync reader routing and mode-selection placement if relevant.
- Human review should confirm that `tool/form article` is the desired tier and that Kiro deserves the full 25-pass queue.

## Package manufacture allowance

Executor package manufacture is allowed after manual review. The plan is mechanically buildable: exact read-only paths were checked in the current snapshot; no missing article-specific read-only file was found.

## Sync pass requirement

Later sync pass required after C5/A10 if those fragments introduce article-map tiers, semantic back-links, or mode-selection decisions that affect this article.
