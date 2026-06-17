# Apply notes — Atlas parity, article map, and theory attachment map

Date: 2026-06-17.

This overlay is cumulative for the current chat branch. It includes the earlier corpus-cuts / Git-layer / theory-skeleton routing changes and adds the latest decisions about Atlas parity, Russian public names for practical parts, detailed Atlas article planning, and the living map of what attaches to Theory chapters.

Baseline rule: apply this overlay relative to the latest full repository archive uploaded by the user in this chat (`git.zip`), unless the user has already applied a previous overlay from this chain. If either previous overlay from this chain was already applied, this overlay can still be applied as a replacement/overwrite of the same files plus new files.

## What changed

1. Added `work/decisions/ADR-0014-public-corpus-part-names-and-atlas-parity.md`.
2. Updated `work/approved-decisions.md`: Atlas is now a peer major part, not an appendix to Theory; practical sections should prefer Russian public names.
3. Added `work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md`: detailed A1–A8 map for future Atlas target-group plans, including required topics, mini-dossier queues, artifacts, selection criteria and boundaries.
4. Added `work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md`: living map of Atlas/fragments/dossiers/story anchors attached to each Theory chapter.
5. Updated `work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md` to point to the detailed Atlas map as planning source.
6. Updated `work/theory-writing/reports/CORPUS_PROJECTION_CUTS_UPDATE_2026_06_17.md` with Atlas parity and Russian naming note.
7. Updated `work/theory-writing/WORKING_DOCUMENTS_MAP.md` and `work/discourse.md` so future packages see the new maps.

## Intended interpretation

- Theory can later be renamed toward `Жизненный цикл программного изменения`, but for now `Теория` remains the short working name.
- Atlas is equal in importance to Theory and has its own acceptance gate.
- `Handbook` should be treated as the old/internal label for what is likely `Рабочие сценарии` or possibly `Практикум`.
- `Fieldbook` should be treated as the old/internal label for `Каталог проблем и решений`.
- Future Atlas plans should start from `ATLAS_V2_LAYER_ARTICLE_MAP.md`.
- Future Theory chapter plans should consult `THEORY_CHAPTER_ATTACHMENT_MAP.md` and update it when Atlas or fragments change.


## 2026-06-17 — atlas expanded core A1-A15

Updated Atlas planning documents after acceptance of Browser/GUI/app feedback and model/provider routing layers. Added ADR-0015, expanded the detailed Atlas map to A1–A15, updated the Atlas status report, updated the Theory chapter attachment map, and recorded source hints for future technical dossiers.


## 2026-06-17 — atlas A16 and navigation review

This overlay is cumulative over the current 2026-06-17 corpus-cuts / Atlas-expansion chain. It adds ADR-0016, expands the Atlas Level 1 map to A1–A16, adds a legacy article routing note, and records a site entrypoint/navigation review note. It does not change public site navigation or rename public routes.

## 2026-06-17 — multilingual readiness layer

This overlay adds ADR-0017 and a first multilingual preparation layer for the future English version of the corpus. It does not translate current materials and does not change public routes. It adds a protocol, bilingual term registry, multilingual readiness report, and updates the Russian terminology protocol with a note that natural Russian prose should be preserved while stable IDs, source provenance and translation notes are added for future English transfer.


## 2026-06-17 — Harness Engineering in Theory skeleton

This overlay adds ADR-0018 and a skeleton-routing note for Harness Engineering. It does not add a new Theory chapter and does not change public navigation. Future chapter packages should use the new `harness-frame check` together with the existing `atlas-technical-grounding check`.

Added/updated:

```text
work/decisions/ADR-0018-harness-engineering-in-theory-skeleton.md
work/theory-writing/reports/HARNESS_ENGINEERING_THEORY_SKELETON_NOTE_2026_06_17.md
work/theory-writing/reports/THEORY_SKELETON_IMPLICATIONS_AFTER_ATLAS_CUTS_2026_06_17.md
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
work/multilingual/BILINGUAL_TERM_REGISTRY.md
```

## 2026-06-17 — corrected Harness retrofit handling

Supersedes the un-applied `harness_retrofit_patch_map_overlay_2026_06_17.zip`. Do not apply that previous overlay.

This corrected overlay does **not** add a separate `WRITTEN_THEORY_ARTICLES_HARNESS_RETROFIT_PATCH_MAP_2026_06_17.md`. Instead, it folds the already-written-chapter harness retrofit rule into the existing synchronization document:

```text
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
```

Reason: all retrofit decisions for written Theory chapters must be coordinated in the same map that already routes Atlas layers, ex-A3, old fragments, story anchors and future source attachments. Otherwise future chapter packages would receive conflicting patch maps.


## 2026-06-17 — Atlas skeleton, A17-A19, and Cross-story routing

This overlay is cumulative over the current 2026-06-17 corpus/Atlas branch. It adds ADR-0019, creates `work/atlas/ATLAS_V2_SKELETON.md`, expands Atlas Level 1 to A1–A19, and records that Atlas also contains additional Level 2/3 profile/method/case articles beyond A1–A19.

It also routes `dark matter of software` to Cross-story synthesis rather than Atlas Level 1, and strengthens existing Atlas routing:

```text
A16 — include machine-readable application/service descriptors and topology.
A4  — include discoverable, role-scoped agent-facing CLI/API commands.
A15 — focus on model/process fit and real-work trials, not rankings.
A19 — core layer for release/deployment/production monitoring/incident-remediation.
AgenticOps — Level 2 integrated platform profile, not A20.
```

Public site navigation is not changed by this overlay.
