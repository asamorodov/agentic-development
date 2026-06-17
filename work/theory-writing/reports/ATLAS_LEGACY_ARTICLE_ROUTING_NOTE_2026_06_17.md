# Atlas legacy article routing note — 2026-06-17

## Purpose

This note records how older concept-first Atlas articles should be treated after the Level 1 Atlas map moved to A1–A16 technical layers.

## Decision

Do not delete or discard old Atlas articles. They are useful, but they no longer define the top-level Atlas architecture.

## Routing

### Level 1 — technical layer map

A1–A16 are the primary Atlas layer articles. They answer: what technical layer exists, what technologies and formats implement it, what artifacts it produces, how approaches differ, how to choose, and where the layer fails.

### Level 2 — concept/method articles

SPDD, Persistent Work Graph, ADR, Spec Kit, Kiro Specs, TDAD, Constitutional SDD, BMAD, GSD and similar articles should be treated as concept/method profiles. They can remain standalone, but they should link to the relevant layers instead of competing with them.

### Level 3 — dense private/product/case forms

Gas Town / Beads, Kiro as an integrated IDE/spec case, OpenHands/SWE-agent-style harnesses and similar forms should be routed as dense cases or product profiles.

## Kiro

Kiro should not be abandoned. It is valuable because it combines specs, steering, hooks, IDE workflow and MCP integrations in one product surface. Future Kiro expansion should position it as a product-specific integrated case, not as the whole specification layer. It should link to A1, A2, A4, A8, A11 and A14.

## Process implication

Future packages for old articles should not use the same template as Level 1 layer articles. They need a profile template: what the method/product is, what layer(s) it touches, what artifacts it creates, what is distinctive, where it fits, and what should not be generalized from it.
