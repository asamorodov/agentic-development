# ADR-0008: Protected methodology profiles and comparative syntheses

Status: Accepted  
Date accepted: 2026-06-07  
Scope: Theory rebuild / methodology coverage  
Accepted by: human owner in chat

Related files:

- `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`
- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`
- `work/approved-ai-sdlc-plan.md`
- `work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md`
- `work/reports/STRUCTURAL_RECOMMENDATION_BEFORE_SKELETON_V4.md`

## Context

After creating skeleton v4, the human owner raised a concern: important methodologies such as Spec Kit, Kiro, Constitutional SDD, GSD and BMAD might be “covered” architecturally but still reduced in final prose to vague three-page summaries. That would be unacceptable because the theory is also meant to work as a learning resource for the human owner.

Earlier planning mixed two different axes:

```text
role in theory architecture
depth of presentation
```

This created a risk: GSD/BMAD could be kept out of deep-anchor status for good architectural reasons, but then accidentally receive too little explanatory depth.

## Decision

Create the status **protected methodology profile**.

A protected methodology profile is not necessarily a deep anchor, but it has protected depth. It cannot be compressed into a shallow overview.

The following materials receive protected methodology profile status:

- Spec Kit;
- Kiro Specs;
- Constitutional SDD;
- TDAD: Test-Driven AI Agent Definition;
- TDAD: Test-Driven Agentic Development;
- GSD / Open GSD;
- BMAD Method.

SPDD remains deep anchor + full methodology profile. Gas Town remains deep anchor as organizational/operational environment case.

## Required profile structure

Each protected methodology profile must cover:

1. problem solved;
2. workflow;
3. artifacts;
4. context location;
5. roles/agents;
6. human gates;
7. validation;
8. lifecycle tail;
9. strengths;
10. failure modes and overuse risks;
11. contrast with neighboring methods;
12. what belongs in theory vs Handbook/Fieldbook.

## Comparative syntheses

The theory must include comparative syntheses as first-class sections, because they provide original value beyond source summary.

Required syntheses:

1. Specification methods: SPDD / Spec Kit / Kiro / TDAD / Constitutional SDD.
2. Process methods: Spec Kit / GSD / BMAD / Reversa / OpenSpec / AgentSPEX / Gas Town.
3. Evidence methods: TDAD / contract tests / architecture fitness / test data / agent traces.
4. Completion/governance: SASE / open-source policy cluster / CODEOWNERS / audit-provenance.

## Consequences

### Positive

- Prevents shallow coverage of key methodologies.
- Preserves learning value for the human owner.
- Keeps SPDD/Gas Town as anchors while protecting other methods.
- Gives comparative chapters a clear mandate.
- Reduces risk of “we mentioned it, but did not understand it”.

### Negative

- Requires more dossiers before drafting.
- May increase total length.
- Requires disciplined writing so protected profiles do not become mini-catalogs.
- Part V and Part VII become heavier and need stronger structure.

## Human gates

Human approval is required before:

- demoting protected methodology profile to short mention;
- removing a required profile element;
- merging GSD/BMAD into a shallow comparison;
- writing Part V or Part VII without methodology dossiers;
- removing required comparative syntheses.
