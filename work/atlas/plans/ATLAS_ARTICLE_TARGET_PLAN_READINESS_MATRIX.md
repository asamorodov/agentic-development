# Atlas article target-plan readiness matrix

Status: final matrix for target-group plans produced by `ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY`.

| Article id | Dossier | Target-group plan | Readiness status | Package manufacture | Sync debts | Asset/readiness caveats | Priority suggestion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `spdd_method` | `work/dossiers/SPDD_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | High visual density: Fowler/OpenSPDD/local SPDD assets; boundary with Spec Kit/Kiro/TDAD/ADR/PWG | P1 — specification anchor |
| `persistent_work_graph` | `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | `work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | High boundary risk: Beads vs Gas Town; source/design synthesis must be marked; many mechanism figures | P0 — core mechanism |
| `gas_town` | `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Must use/reject existing local Gas Town assets; normalize from old gas_town_beads id; high terminology/hype risk | P0/P1 — organizational edge case |
| `adr_method` | `work/dossiers/ADR_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Boundary with specification methods and executable evidence; risk of becoming template catalog | P2 — decision-memory support |
| `spec_kit_method` | `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | High risk of CLI reference; official docs/images currentness needed | P1 — current tool-form anchor |
| `kiro_specs` | `work/dossiers/KIRO_SPECS_DOSSIER.md` | `work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Needs visual/UI/source handling; risk of generic requirements workflow | P2 — tool-form contrast |
| `tdad_comparative` | `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | `work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Comparative article; evidence/testing boundary must not swallow SPDD/ADR/PWG | P2 — evidence/test contrast |
| `constitutional_sdd` | `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | `work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Risk of becoming generic governance essay; keep constitutional constraints as method mechanism | P2 — constraint/governance contrast |
| `gsd_open_gsd` | `work/dossiers/GSD_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Risk of command reference; keep lifecycle/runtime framing and gsd-core vs gsd-pi distinction | P1/P2 — lifecycle/runtime profile |
| `bmad_method` | `work/dossiers/BMAD_METHOD_DOSSIER.md` | `work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | allowed after manual review | C5/A10 synced; verify article-specific links at package time | Risk of command/persona catalogue; keep artifact-first SDLC process profile; many visual candidates | P1/P2 — process profile |

## Interpretation

- No target plan is blocked by missing primary dossier.
- All target plans require human review before manufacturing executor/article-writing packages because every readiness status is `ready_for_package_manufacture_after_manual_review`.
- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` exists in the post-import repo state and is included as manufactury provenance context for future packages.
- C5/A10 are available and have been added as read-only context; future article packages should verify article-specific links and routing, not treat sync as a default blocker.


## 2026-06-12 — remaining atlas plans repaired and packages built

- `spec_kit_method` → `work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `kiro_specs` → `work/atlas/packages/kiro_specs_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `constitutional_sdd` → `work/atlas/packages/constitutional_sdd_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `tdad_comparative` → `work/atlas/packages/tdad_comparative_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `gsd_open_gsd` → `work/atlas/packages/gsd_open_gsd_ATLAS_ARTICLE.zip` (self-contained; 66 files).
- `bmad_method` → `work/atlas/packages/bmad_method_ATLAS_ARTICLE.zip` (self-contained; 68 files).


## 2026-06-12 — package status for remaining six articles

The following article target plans have been repaired and packages built: `spec_kit_method`, `kiro_specs`, `constitutional_sdd`, `tdad_comparative`, `gsd_open_gsd`, `bmad_method`. Status: `ready_for_package_manufacture_after_manual_review`; packages exist in `work/atlas/packages/`.
