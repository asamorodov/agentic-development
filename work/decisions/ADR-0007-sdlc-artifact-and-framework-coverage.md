# ADR-0007: SDLC artifact and framework coverage before drafting

Status: Accepted  
Date accepted: 2026-06-07  
Scope: Theory rebuild / AI-driven SDLC architecture  
Accepted by: human owner in chat  
Supersedes: `work/decisions/PROPOSED_ADR-0007-sdlc-artifact-and-framework-coverage.md`

Related files:

- `work/approved-ai-sdlc-plan.md`
- `work/discourse.md`
- `work/theory-source-map-ai-driven-sdlc.md`
- `work/reports/SDLC_ARTIFACT_COVERAGE_AUDIT.md`
- `work/reports/AGENTIC_FRAMEWORKS_COVERAGE_AUDIT.md`
- `work/reports/TARGETED_SOURCE_EXPANSION_REPORT.md`
- `work/reports/TARGETED_SOURCE_EXPANSION_STAGE_0_7_REPORT.md`
- `work/reports/TARGETED_SOURCE_EXPANSION_STAGE_0_8_REPORT.md`
- `work/reports/TARGETED_SOURCE_EXPANSION_STAGE_0_9_REPORT.md`
- `work/reports/TARGETED_SOURCE_EXPANSION_STAGE_0_12_REPORT.md`
- `work/reports/DETAILED_CONSOLIDATED_PLAN_PATCH_AFTER_FULL_REREAD.md`
- `work/reports/UPDATED_PLAN_QUALITY_AUDIT.md`

## Context

The approved v3 architecture for the rebuilt theory was based on AI-driven SDLC as a lifecycle of software change:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

That architecture fixed several earlier failures:

- the expanded theory became a quarry, not the main draft;
- “map of currents” became a source/control layer, not top-level structure;
- SPDD became a separate deep part;
- Spec Kit / Kiro / TDAD / Constitutional SDD became deep neighboring specification regimes;
- Gas Town returned to deep anchor status;
- SPDD and Gas Town must be restored from old site baseline seeds before adaptation.

Stage 0.5–0.12 showed that the architecture remains correct, but it lacked an explicit cross-cutting layer of SDLC artifacts and process frameworks. Without that layer, the accumulated sources could again become a catalog.

## Decision

The theory rebuild will treat SDLC artifacts as first-class design objects.

The v4 plan adds five artifact classes:

1. Артефакты намерения и решения.
2. Артефакты состояния задачи и проекта.
3. Артефакты среды исполнения и ограничений.
4. Артефакты свидетельства и проверки.
5. Артефакты завершения и хвоста lifecycle.

The plan also explicitly accepts the following additional layers:

- decision provenance: ADR / RFC / design proposal / decision enforcement;
- process/framework layer: GSD, BMAD, Reversa, OpenSpec / AgentSPEX as medium candidates;
- lifecycle-tail artifacts: release, migration, rollback, runbook, incident, postmortem, dependency/deprecation, changelog;
- security/provenance artifacts: threat model, security review, audit log, provenance, secrets, SBOM, sensitive context boundary;
- traceability and contracts: traceability links, API/data contracts, contract tests;
- execution-environment artifacts: reproducible environment, policy-as-code, agent traces;
- ownership artifacts: CODEOWNERS, ownership map, review routing, completion authority;
- architecture quality: quality attribute scenarios, fitness functions, architecture tests, architecture drift;
- test data/environment layer: controlled test environments, test data sources, fixtures, service virtualization, oracle provenance.

## Consequences

### Positive

- Reduces risk of another hidden ADR-level omission.
- Prevents the theory from becoming a flat collection of sources.
- Gives Part X a stronger evidence-package theory.
- Gives Part XII a controlled lifecycle-tail structure.
- Gives Part VI–VIII a richer account of project state, environment and constraints.
- Keeps SPDD and Gas Town protected as deep anchors.
- Clarifies that GSD/BMAD are process/framework layer, not specification-zone competitors.

### Negative

- Adds complexity to the approved plan.
- Requires selected dossiers/notes before drafting.
- Increases the risk that Parts VI–XII become too large unless controlled.
- Requires careful Russian-language synthesis to avoid English-heavy report style.

## Alternatives considered

### Continue from v3 without patch

Rejected. Stage 0.5–0.12 revealed too many artifact and process gaps.

### Add a new top-level part for artifacts

Rejected. It would likely recreate catalog structure.

### Add a new top-level part for frameworks

Rejected for now. GSD/BMAD need dossiers, but not automatic deep-anchor status.

### Make architecture quality or test data separate top-level parts

Rejected. They deserve named medium-high subsections, primarily in Part X, with links to Parts III, VIII and XII.

### Continue broad source search

Rejected for now. The next step is selected dossiers/notes and skeleton, not more broad search.

## Human gates retained

Human approval is still required before:

1. Adding any new top-level part.
2. Promoting GSD, BMAD, Reversa, OpenSpec, AgentSPEX, Backstage, OPA or other new materials to deep anchor status.
3. Demoting SPDD or Gas Town.
4. Demoting Spec Kit, Kiro, TDAD or Constitutional SDD from deep treatment.
5. Compressing SPDD or Gas Town against baseline restore rule.
6. Expanding Part XII into a separate operational handbook.
7. Starting a broad new source-search cycle.

## Follow-up

After this ADR:

1. Use `work/approved-ai-sdlc-plan.md` v4 as the active architectural plan.
2. Create selected dossiers/notes.
3. Build skeleton v4.
4. Begin drafting only after relevant dossiers/notes exist.
