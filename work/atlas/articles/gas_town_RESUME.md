# RESUME — gas_town article package

## Current state

START.md workflow completed through P26 and Final readiness. The resulting article package is editorially ready as a draft package, but not directly publishable until external-image and freshness blockers are resolved.

## Main article

- `work/atlas/articles/gas_town.md`
- H1: `Gas Town: какие организационные механизмы нужны, когда агентная работа выходит за пределы одного чата, одного рабочего дерева и ручного наблюдения?`

## Companion files

- `gas_town_source_usage.md`
- `gas_town_source_transfer_ledger.md`
- `gas_town_image_plan.md`
- `gas_town_external_image_queue.md`
- `gas_town_open_questions.md`
- `gas_town_theory_links.md`
- `gas_town_degradation_and_duplication_audit.md`
- `gas_town_readiness_report.md`
- `gas_town_VERIFY.json`

## Final blockers before publication

1. Resolve `fig-gastown-two-tier-beads-flow`: source is Steve Yegge, `Welcome to Gas Town`, Figure 6, `Two-Tier Beads Flow`; proposed local path is `content/assets/atlas-images/gas-town/two-tier-beads-flow.webp`.
2. Resolve `fig-gastown-worker-roles`: source is Steve Yegge, `Welcome to Gas Town`, Figure 5, `Gas Town’s Worker Roles`; proposed local path is `content/assets/atlas-images/gas-town/worker-roles.webp`.
3. Run freshness-check for version-sensitive facts: Gas Town CHANGELOG, Scheduler design, Beads Releases, DoltHub workflow context and troubleshooting/sandbox details.
4. Decide whether the Hacker News perception signal remains in the public article or moves to source notes only.

## Verification

`VERIFY.md` and `work/atlas/articles/gas_town_VERIFY.json` record the final automated checks. All checks passed at package time. The checks confirm file presence, local asset path existence, external-placeholder mirroring, companion population and absence of several internal markers in the main article.
