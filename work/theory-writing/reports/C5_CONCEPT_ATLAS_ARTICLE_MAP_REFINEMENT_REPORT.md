# C5 concept atlas article map refinement report

Date: 2026-06-11

## Purpose

This report records a second refinement of `C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md` after the concept-first atlas decision. The C5 queue remains 17 working passes plus final verification; no new working pass was added.

## Problem found

The previous C5 plan already introduced a concept-first atlas and `C5_concept_atlas_article_map.md`, but the article map could still degrade in two opposite ways:

1. become a flat list of equally weighted topics;
2. become a premature miniature atlas with long article-like sections.

Both outcomes would weaken the C5 task. C5 should define the architecture of future concept-first atlas articles, not write those articles and not merely list candidate topics.

## Changes made

### P02

Added a short stress-test of the atlas article model on SPDD, PWG / Beads, Gas Town and ADR. The model must survive different concept types before it is used to update the article map.

### P03

Expanded the required `C5_concept_atlas_article_map.md` fields:

- article tier;
- reader question;
- source/dossier basis;
- article boundary;
- allowed theory repetition;
- commands/files/images/assets/caveats/source notes;
- asset/source readiness;
- semantic back-links to theory.

Added article tiers:

- `core concept article`;
- `method article`;
- `tool/form article`;
- `source note / case note`;
- `deferred / not enough material`.

Added boundary checks for dangerous overlap pairs:

- SPDD / OpenSPDD / Spec Kit / Kiro;
- PWG / Beads / Gas Town;
- GSD / BMAD / process profiles;
- TDAD / evidence / testing;
- ADR / lifecycle repair / specification.

### P05

Expanded the atlas distortion check from four risks to five. The added risk: the atlas becomes a flat list of equally weighted articles without tiers, reader questions, boundaries or priorities.

### P10

Strengthened two-way navigation: back-links must be semantic, not just navigation-only. Each key article should explain which theoretical question it helps understand.

### P17 and final verification

Strengthened the check that article map remains registry-level and does not become a miniature atlas or draft of the articles themselves.

## Files changed

- `START.md`
- `work/theory-writing/CORE_NODES_WRITING_PLAN.md`
- `work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md`
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md`
- `work/discourse.md`
- `work/APPLY_NOTES.md`
- `work/COMMIT_MESSAGE.txt`
- `work/checks.json`

## Result

C5 keeps the 17+final structure but now has a stronger article-map contract. The future package should produce an atlas architecture that is useful for concept-first reading without becoming the atlas itself.
