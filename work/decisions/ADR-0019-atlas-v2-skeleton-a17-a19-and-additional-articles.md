# ADR-0019 — Atlas V2 skeleton, A17–A19, and additional Atlas article levels

Status: Accepted  
Date: 2026-06-17

## Context

After ADR-0012 through ADR-0018, the public corpus is understood as one shared knowledge field projected through different cuts. Atlas is a peer major part, not a technical appendix to Theory. Its top-level cut is technical layers and competing ways to build each layer.

The user asked for another outside check of missing Atlas topics. The second check showed that A1–A16 cover the main foundation, but still under-represent three practically important layers:

1. structured program feedback: compilers, typecheckers, language servers, debuggers, static analysis, profiler and runtime-log signals;
2. autonomous testing and QA artifacts: test generation, bug reproduction, regression tests, test repair and governance of generated tests;
3. release, deployment, production monitoring and incident/remediation agents.

The user also accepted the idea that “dark matter of software” is more appropriate for Cross-story synthesis than as an Atlas layer. The user further clarified that Atlas contains additional articles besides A1–A19: older concept-first and product/method/case profiles such as Kiro, SPDD, Persistent Work Graph, ADR, Gas Town/Beads, Spec Kit and AgenticOps should not be discarded.

## Decision

1. Expand Atlas Level 1 from A1–A16 to A1–A19:
   - A17. Structured program feedback;
   - A18. Autonomous testing and QA artifacts;
   - A19. Release, deployment, production monitoring and incident/remediation agents.

2. Treat A19 as core, not merely a candidate. It is the post-merge and production-facing counterpart of A7: A7 handles engineering acceptance gates, while A19 covers release, runtime observation, rollback/remediation and incident learning.

3. Create a dedicated Atlas skeleton document:

   ```text
   work/atlas/ATLAS_V2_SKELETON.md
   ```

   This document is the Atlas-level analogue of the Theory skeleton. It defines Atlas composition, Level 1 layer articles, Level 2 profile/method/case articles, acceptance gates, and the relation between Atlas and Theory.

4. Keep `work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md` as the operational planning map for target-group plans. The skeleton explains composition and article roles; the layer map feeds package construction.

5. Record that Atlas has additional articles beyond A1–A19. A1–A19 are Level 1 layer articles. Older concept-first and product/method/case articles remain useful as Level 2/3 profiles and source nodes:
   - SPDD;
   - Persistent Work Graph;
   - ADR;
   - Kiro / Kiro Specs;
   - Spec Kit;
   - TDAD;
   - Constitutional SDD;
   - BMAD / GSD / Open GSD;
   - Gas Town / Beads;
   - AgenticOps / agent-facing platform engineering;
   - selected product/tool profiles when they explain several layers at once.

6. Route “dark matter of software” to Cross-story synthesis. It is not a new Atlas layer. It helps explain why many AI-generated/agent-assisted artifacts may not appear as visible products: internal tools, personal utilities, one-off automations, reports and private workflow software can become economically viable while remaining mostly invisible to public product markets.

7. Strengthen existing layer boundaries:
   - A16 should explicitly include machine-readable application/service descriptors, topology, ownership, environments, resource bindings, log/trace locations, deployment units and operational capabilities.
   - A4 should explicitly cover agent-facing CLI/API design: simple/discoverable commands, `SKILL.md`-like tool guidance, role-scoped commands and safe outputs for next-step reasoning.
   - A15 should focus on model/process fit, local evals, real-work trials, routing, cost and inference constraints, not model rankings.
   - AgenticOps should be an integrated Level 2 profile rather than a new Level 1 layer, because it combines A4, A6, A7, A9, A15, A16 and A19.

## Consequences

- Atlas now has a larger Level 1 layer map, but it remains bounded: the new layers correspond to technical subsystems, not arbitrary products.
- Older Atlas articles are preserved and become easier to route: they are profiles or method nodes, not failed top-level layers.
- Future Atlas packages must state whether they build a Level 1 layer article or a Level 2 profile/method/case article.
- Future Theory chapter packages should use `THEORY_CHAPTER_ATTACHMENT_MAP.md` to attach A17–A19 where needed, but should not expand them technically inside Theory chapters.
- Cross-story synthesis should be updated later to include “dark matter of software” as a reader-facing pattern.

## Non-goals

- This ADR does not rewrite public site navigation.
- This ADR does not create final public prose for A17–A19.
- This ADR does not decide final slugs or public route order.
- This ADR does not move Kiro/SPDD/PWG/Gas Town into the new Level 1 layer list.
