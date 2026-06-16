# Chapters I–V visual-layer completion report

Date: 2026-06-15

## Scope

This pass continues from the interrupted visual-layer work and completes the figure integration for Chapters I–V. It uses the existing intermediate chapter overlay, keeps the already inserted figures, restores the missing Chapter III/IV figure insertions, and adds the remaining useful explanatory/source-backed figures rather than being overly sparse.

## Result by chapter

### Chapter I — Unit of analysis

- `fig-i-entry-points-before-prompt` → `content/assets/theory-images/i-entry-points-before-prompt.svg`
- `fig-i-partial-carriers-vs-software-change` → `content/assets/theory-images/i-unit-of-analysis-carriers.png`
- `fig-i-minimal-change-axis` → `content/assets/theory-images/i-minimal-change-axis.png`

### Chapter II — Agentic session trace

- `fig-ii-session-wider-than-chat` → `content/assets/theory-images/ii-session-wider-than-chat.png`
- `fig-ii-session-trace-to-state` → `content/assets/theory-images/ii-trace-to-work-state.png`
- `fig-ii-agent-trace-provenance` → `content/assets/theory-images/ii-agent-trace-provenance.svg`

### Chapter III — Intent / spec / contract / ADR

- `fig-iii-spec-contract-adr-boundaries` → `content/assets/theory-images/iii-spec-contract-adr-boundaries.svg`
- `fig-iii-adr-minimal-record` → `content/assets/atlas-images/adr/adr-nygard-minimal-record.svg`
- `fig-iii-adr-lifecycle` → `content/assets/atlas-images/adr/adr-aws-lifecycle-process.svg`
- `fig-iii-adr-confirmation` → `content/assets/atlas-images/adr/adr-madr-template-confirmation.svg`
- `fig-iii-adr-agent-projection` → `content/assets/theory-images/iii-adr-agent-projection.svg`

### Chapter IV — SPDD lifecycle

- `fig-fowler-spdd-overview` → `content/assets/theory-images/fowler-spdd-overview.svg`
- `fig-fowler-spdd-reasons-canvas` → `content/assets/theory-images/fowler-spdd-reasons-canvas.svg`
- `fig-fowler-spdd-code-review` → `content/assets/theory-images/fowler-spdd-code-review.svg`
- `fig-fowler-spdd-workflow` → `content/assets/theory-images/fowler-spdd-workflow.svg`
- `fig-openspdd-sync-bidirectional-flow` → `content/assets/theory-images/openspdd-sync-bidirectional-flow.svg`

### Chapter V — Protected specification profiles

- `fig-v-speckit-workflow` → `content/assets/theory-images/v-speckit-workflow.svg`
- `fig-v-kiro-specs-surface` → `content/assets/theory-images/v-kiro-specs-surface.svg`
- `fig-v-tdad-pipeline` → `content/assets/theory-images/v-tdad-pipeline.png`
- `fig-v-constitutional-sdd-traceability` → `content/assets/theory-images/v-constitutional-sdd-traceability.png`
- `fig-v-protected-specification-profiles-matrix` → `content/assets/theory-images/v-protected-specification-profiles-matrix.png`

## Editorial decision

No previously useful figure was removed. Additional figures were added only where they explain a distinct mechanism or source-backed distinction: pre-prompt entry points, Agent Trace/provenance, the boundaries between specification/contract/ADR, ADR projection for agents, Spec Kit workflow, and Kiro Specs surface.

## Checks

- All figure references point to existing local files.
- All figure IDs are unique within each chapter.
- Captions are public-facing, not executor notes.
- Source-backed redraws and synthetic figures are labeled as local assets rather than external screenshots.
