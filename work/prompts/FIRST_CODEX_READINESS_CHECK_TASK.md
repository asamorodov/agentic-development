# First Codex readiness check task

Use this as the first task in Codex before running Stage 0.19.

## Task

Verify that Codex can work with this repository and understands the current theory-rebuild workflow.

Do not write theory chapters.
Do not create methodology dossiers yet.
Do not modify `work/approved-ai-sdlc-plan.md`.
Do not modify `/content`.

This is a readiness and comprehension check only.

## Read in order

```text
AGENTS.md
project/repository-structure.md
project/source-precedence.md
project/branching-and-task-model.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/theory-rebuild-rules.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/english-source-handling.md
work/discourse.md
work/approved-ai-sdlc-plan.md
work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md
work/decisions/ADR-0008-protected-methodology-profiles.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/reports/SKELETON_V4_QUALITY_AUDIT.md
```

Then inspect:

```text
work/dossiers/
work/reports/
work/source-expansion/
work/prompts/
```

## Create

```text
work/reports/CODEX_READINESS_CHECK.md
work/reports/CODEX_DOCUMENT_VISIBILITY_INVENTORY.md
work/reports/CODEX_UNDERSTANDING_SUMMARY.md
work/reports/CODEX_NEXT_TASK_RISK_ASSESSMENT.md
work/CHECKS.json
work/discourse.md
```

## What to verify

### 1. Repository and document visibility

Confirm:

- you see the `work/` directory;
- you see `work/discourse.md`;
- you see `work/approved-ai-sdlc-plan.md`;
- you see ADR-0007 and ADR-0008;
- you see methodology depth contract;
- you see skeleton v4;
- you see selected dossiers;
- you see source-expansion materials.

### 2. Current work state

Explain in Russian:

- why the project moved from old theory to AI-driven SDLC;
- why expanded theory is quarry, not main draft;
- why SPDD and Gas Town are protected deep anchors;
- what protected methodology profile means;
- why GSD/BMAD are not shallow mentions;
- why Parts VI–XII must not become artifact catalogs;
- what Stage 0.19 is supposed to do.

### 3. Protocol compliance

Confirm:

- you understand Russian language requirements;
- you understand baseline restore rule;
- you understand not to write chapters yet;
- you understand not to change approved plan;
- you understand human gates.

### 4. Readiness for complex tasks

State whether you are ready to run Stage 0.19. If not ready, explain why.

## Required output details

`work/reports/CODEX_READINESS_CHECK.md` must include:

```text
status: READY / READY_WITH_WARNINGS / NOT_READY
documents_read:
missing_documents:
understanding_summary:
risks:
recommended_next_task:
human_gates:
```

`work/reports/CODEX_DOCUMENT_VISIBILITY_INVENTORY.md` must list required files and whether they were found.

`work/reports/CODEX_UNDERSTANDING_SUMMARY.md` must be a narrative summary of the current workflow, not a checklist.

`work/reports/CODEX_NEXT_TASK_RISK_ASSESSMENT.md` must name risks before Stage 0.19.

## Stop condition

If any required core document is missing, do not proceed to Stage 0.19. Create the reports and ask for human decision.
