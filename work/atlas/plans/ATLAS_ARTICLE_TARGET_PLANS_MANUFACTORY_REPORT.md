# Atlas article target-plans manufactury report

Status: final report for target-group plan manufactury package.

## Summary

- Target-group plans produced/checked: 10.
- Blocked plans: none.
- Plans allowed for executor package manufacture immediately without human review: none, because each plan intentionally uses `ready_for_package_manufacture_after_manual_review`.
- Plans allowed after manual review: all current target-group plans.
- Article text was not written and article-writing packages were not built.

## Ready after manual review

- `spdd_method` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P1 — specification anchor. Caveat: High visual density: Fowler/OpenSPDD/local SPDD assets; boundary with Spec Kit/Kiro/TDAD/ADR/PWG.
- `persistent_work_graph` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P0 — core mechanism. Caveat: High boundary risk: Beads vs Gas Town; source/design synthesis must be marked; many mechanism figures.
- `gas_town` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P0/P1 — organizational edge case. Caveat: Must use/reject existing local Gas Town assets; normalize from old gas_town_beads id; high terminology/hype risk.
- `adr_method` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P2 — decision-memory support. Caveat: Boundary with specification methods and executable evidence; risk of becoming template catalog.
- `spec_kit_method` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P1 — current tool-form anchor. Caveat: High risk of CLI reference; official docs/images currentness needed.
- `kiro_specs` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P2 — tool-form contrast. Caveat: Needs visual/UI/source handling; risk of generic requirements workflow.
- `tdad_comparative` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P2 — evidence/test contrast. Caveat: Comparative article; evidence/testing boundary must not swallow SPDD/ADR/PWG.
- `constitutional_sdd` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P2 — constraint/governance contrast. Caveat: Risk of becoming generic governance essay; keep constitutional constraints as method mechanism.
- `gsd_open_gsd` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P1/P2 — lifecycle/runtime profile. Caveat: Risk of command reference; keep lifecycle/runtime framing and gsd-core vs gsd-pi distinction.
- `bmad_method` — `ready_for_package_manufacture_after_manual_review`; package manufacture allowed after manual review. Priority: P1/P2 — process profile. Caveat: Risk of command/persona catalogue; keep artifact-first SDLC process profile; many visual candidates.

## Blockers

- No article-specific primary dossier blocker found.
- No missing target-group plan file for ledger article ids after F01 repair.
- No missing exact read-only path found in the created plans during F01 path scans.

## Global debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` exists in the post-import repo state; the previous absence was a package snapshot artifact and is now resolved for future package manufacture.
- C5 sync resolved at the plan level: current C5 and article map are available as read-only context. Future package runs should still verify article-specific semantic links.
- A10 sync resolved at the plan level: current A10 mode-selection map/matrix/stress tests are available as read-only context. Future package runs should still verify article-specific reader routing if relevant.
- Human review should approve normalized ids: `bmad_method`, `tdad_comparative`, `adr_method`, `gas_town`.

## Recommended manufacture order

1. `persistent_work_graph` — central mechanism for later articles.
2. `gas_town` — organizational edge case that depends on PWG boundary clarity.
3. `spdd_method` — specification anchor and already source-rich visual candidate.
4. `spec_kit_method` and `kiro_specs` — current tool-form comparison after SPDD framing.
5. `bmad_method` and `gsd_open_gsd` — process/runtime profiles after PWG and specification cluster are stable.
6. `adr_method`, `tdad_comparative`, `constitutional_sdd` — supporting/contrast articles for decision memory, evidence/testing and constraints.

## Completion note

F02 produced readiness matrix, boundary matrix and this final report. It did not change target plans except through prior F01 repairs and did not create any article-writing package.

## Post-import manual repair: `spdd_method`

`spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` был дополнительно отремонтирован после ручного review. Из target-plan удалена история manufactury-run, усилена центральная логика SPDD/OpenSPDD, source-depth проходы сделаны SPDD-specific, visual passes очищены от дублирующего boilerplate, а C5/A10 зафиксированы как доступный read-only context без стандартного `sync pending`. Article package для SPDD пока не собирался.


## 2026-06-12 — Persistent Work Graph plan repaired

`persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` repaired to reduce blueprint/template residue and strengthen the article-specific logic: durable work state, Beads-as-anchor, boundaries with Gas Town/durable execution/issue trackers/CRDT-STORM, and document-process transfer. Package manufactured after repair.


## 2026-06-12 — Gas Town plan repaired

`gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` repaired to reduce blueprint/template residue and strengthen the article-specific logic: operational pressure, Beads/PWG/Gas Town boundary, work grammar as operational functions, queue/scheduler/backpressure/recovery, local assets and failure modes. Package manufactured after repair.


## 2026-06-12 — remaining atlas plans repaired and packages built

- `spec_kit_method` → `work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `kiro_specs` → `work/atlas/packages/kiro_specs_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `constitutional_sdd` → `work/atlas/packages/constitutional_sdd_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `tdad_comparative` → `work/atlas/packages/tdad_comparative_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `gsd_open_gsd` → `work/atlas/packages/gsd_open_gsd_ATLAS_ARTICLE.zip` (self-contained; 66 files).
- `bmad_method` → `work/atlas/packages/bmad_method_ATLAS_ARTICLE.zip` (self-contained; 68 files).
