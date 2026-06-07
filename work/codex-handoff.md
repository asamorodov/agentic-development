# Codex handoff

This file explains how Codex should be used for the theory rebuild.

## Core principle

Codex should not be treated as an unconstrained author. It should be treated as a workflow executor around Markdown documents.

It should do:

- inventory;
- skeleton creation;
- dossier creation;
- controlled rewrites;
- anti-catalog audit;
- source-depth audit;
- anti-degradation checks;
- reports, ledgers, matrices and diffs.

It should not independently decide:

- whether SPDD remains a separate part;
- whether Gas Town remains a separate part;
- which cases are deep anchors;
- whether a part is “good theory” rather than a dossier;
- whether detail may be removed from old SPDD/Gas Town baseline sections.

## Recommended stages

```text
Stage 0. Repository/workspace inventory
Stage 1. Skeleton creation for Theoretical_synthesis_rebuilt.md
Stage 2. Anchor and framework dossiers
Stage 3. Part design / part briefs
Stage 4. Draft rebuild by approved batches
Stage 5. Anti-catalog audit
Stage 6. Source-depth repair
Stage 7. Anti-degradation check against old baseline
Stage 8. Final integration report
```

## First major writing batches

Do not write the whole theory at once. Recommended order:

1. Introduction + Parts I–II to validate voice and lifecycle framing.
2. Parts III–V specification zone.
3. Parts VI–VIII context/delegation/execution.
4. Part IX Gas Town / Beads with baseline restoration.
5. Parts X–XII evidence/governance/maintenance tail.
6. Conclusion.

## Required external traces

For every non-trivial Codex task, create:

- task report;
- files changed list;
- source integration ledger;
- untransferred queue;
- anti-catalog or anti-degradation report, if relevant;
- `CHECKS.json` or equivalent artifact-completion file.

## Stop conditions

Codex must stop and ask for human decision when:

- it would compress SPDD or Gas Town details;
- it cannot find the old baseline seed section;
- it wants to move a deep anchor into a short contrast;
- it detects that a part is becoming a source catalogue;
- it lacks primary-source support for a claimed mechanism;
- it needs to decide whether to drop or relocate a case.
