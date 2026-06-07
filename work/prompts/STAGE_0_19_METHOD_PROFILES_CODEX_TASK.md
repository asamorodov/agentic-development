# Stage 0.19 Codex task prompt — protected methodology dossiers

Use this prompt in Codex after the readiness check succeeds.

## Task

Run Stage 0.19: create protected methodology dossiers for Spec Kit, Kiro, Constitutional SDD, TDAD, GSD and BMAD.

Do not write final theory chapters.

## First read

Read in this order:

```text
AGENTS.md
project/repository-structure.md
project/source-precedence.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/theory-rebuild-rules.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/english-source-handling.md
work/discourse.md
work/approved-ai-sdlc-plan.md
work/decisions/ADR-0008-protected-methodology-profiles.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
```

Then read all relevant existing reports and notes in `work/reports/`, `work/dossiers/`, `work/source-expansion/`.

## Required outputs

Create pass files:

```text
work/methodology-passes/spec-kit/pass_01_source_inventory.md
work/methodology-passes/spec-kit/pass_02_workflow_reconstruction.md
work/methodology-passes/spec-kit/pass_03_artifact_and_gate_map.md
work/methodology-passes/spec-kit/pass_04_missing_detail_pass.md
work/methodology-passes/spec-kit/pass_05_comparative_pass.md
work/methodology-passes/spec-kit/pass_06_anti_shallow_audit.md
```

Repeat the same pattern for:

```text
kiro
constitutional-sdd
tdad
gsd
bmad
```

Create final dossiers:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
```

Create comparative reports:

```text
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/METHODOLOGY_DOSSIERS_QUALITY_AUDIT.md
```

Update:

```text
work/discourse.md
work/CHECKS.json
```

## Method

Follow:

```text
work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md
```

Do not replace it with your own process.

## Mandatory quality requirements

Each final dossier must cover:

```text
problem
workflow
artifacts
context
roles / agents
human gates
validation
lifecycle tail
strengths
failure modes
contrast with neighboring methods
theory vs Handbook / Fieldbook split
```

If a dossier lacks these, repair it before finishing.

## Stop conditions

Stop and ask for human decision if:

- source depth for a protected methodology is too weak;
- you want to demote a protected methodology;
- you think GSD/BMAD should become deep anchors;
- you need a broad new source search;
- you need to change approved plan or skeleton;
- you are unable to read required documents.

## Final response

Report:

1. Files created.
2. Methodologies completed.
3. Any failed or weak dossiers.
4. Which sources were primary.
5. Whether Part V and Part VII are ready for drafting.
6. Open human gates.
