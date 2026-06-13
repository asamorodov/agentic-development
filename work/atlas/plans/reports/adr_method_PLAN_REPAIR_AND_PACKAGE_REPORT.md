# ADR method atlas article target-plan repair and package report

## Context

The user reviewed `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` and asked how to make it less template-like. The plan was repaired, then an article-writing executor package was built immediately from the repaired plan.

## Plan repair

Repaired file:

```text
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Main changes:

- Sharpened the article around ADR as architectural decision memory: decision status, rationale, consequences, confirmation, replacement conditions and agent misuse risks.
- Reframed the central problem away from “ADR template catalogue” and toward the lifecycle of an architectural decision in AI-assisted / agentic development.
- Added three ADR-specific failure modes: dead record, unsupported belief, and improper action basis for an agent.
- Integrated AI/ADR research into the article logic: generation is not acceptance, reconstruction is not provenance, violation detection is not architectural understanding, and context size does not solve decision status.
- Rewrote confirmation in plain language: how to know whether the decision is still observed or should be revisited.
- Strengthened boundaries with A2/A9/PWG/specification/test/CSDD/TDAD.
- Grouped external sources by role instead of treating them as a flat URL list.
- Strengthened ADR-specific visual requirements: ADR templates, MADR examples, generated/reconstructed ADRs, decision lifecycle diagrams, ArchUnit/CODEOWNERS/fitness-function examples and AI/ADR research figures.
- P01 now requires creating all target outputs at least as skeleton/status files, so a future gated runner cannot silently miss mandatory outputs.

## Package built

Created self-contained article-writing package:

```text
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
```

The exported user-facing package is also available as:

```text
/mnt/data/adr_method_ATLAS_ARTICLE.zip
```

Package properties:

- 26 gated records: P01–P25 + Final.
- All P04–P08, P09–P10, P11–P13, P14–P16, P17–P19, P22–P23 and P24–P25 ranges are expanded into separate records.
- The package bundles exact read-only repository inputs listed by the repaired target plan, except that repository `START.md` is embedded inside the package `START.md` under a snapshot section to avoid path collision with package launch instructions.
- The binary local asset `content/assets/theory-images/fowler-sdd-overview.png` is bundled.
- The runner checks mandatory target outputs after P01, because P01 must create all target outputs as files.

## Validation

Validation performed:

- Repaired ADR target plan exists and contains the sharpened ADR article contract.
- Package zip passes `unzip -t`.
- Package first-run smoke test emits P01 instruction.
- After writing smoke target outputs, the second runner invocation emits P02.
- Read-only input bundle had no missing files.
- The package is stored in `work/atlas/packages/` and in `/mnt/data/`.

## Status

`adr_method_ATLAS_ARTICLE.zip` is ready for execution after manual review of the repaired ADR target plan.


## 2026-06-12 image-candidate rule rebuild

ADR package was rebuilt after strengthening visual passes. P11–P13 now read `work/dossiers/ADR_METHOD_DOSSIER.md`, start external-image decisions from the dossier's `Кандидаты на иллюстрации` section, require a disposition for every dossier image candidate, and final verification checks inline placeholders / bottom asset-pass section / external queue consistency.
