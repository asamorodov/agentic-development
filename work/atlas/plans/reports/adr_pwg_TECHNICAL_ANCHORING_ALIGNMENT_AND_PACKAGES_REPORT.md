# ADR and PWG technical-anchoring alignment and package rebuild

Date: 2026-06-13  
Baseline: user-uploaded full repository snapshot `git(10).zip`.  
Scope: bring `adr_method` and `persistent_work_graph` atlas article target plans into alignment with the current softened atlas blueprint, then rebuild only their article-writing packages.

## Updated files

```text
START.md
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/atlas/plans/reports/adr_pwg_TECHNICAL_ANCHORING_ALIGNMENT_AND_PACKAGES_REPORT.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

## Plan changes

Both plans now follow the current `ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` shape:

```text
P01–P16 — content/source/visual/concept passes
P17–P18 — language passes
P19–P21 — general editorial passes
P22 — public/article structure and entry-sequence
P23 — companion sync
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style
Final — final verification / package-readiness
```

Shared changes:

- replaced hard `coverage matrix / relevant but untransferred` logic with rollback-like `dossier inventory`;
- removed repeated `transfer-audit` phrasing from source-depth passes;
- kept only soft technical anchoring: key claims should have concrete technical anchors when otherwise they become general prose;
- preserved article-specific spines rather than rewriting the plans generically;
- used the current style tail: `style defect audit`, `selective natural rewrite`, and `guarded final human technical style`;
- ensured language passes run before general repair/editorial.

ADR-specific changes:

- P04–P08 now separately target classic ADR sources/tooling, AI/ADR research, executable/operational confirmation, lifecycle/failure modes/boundaries, and anti-summary source check.
- Technical anchoring is framed around decision status, confirmation, replacement, AI/ADR generation/reconstruction, violation detection, traceability, ArchUnit, CODEOWNERS, fitness functions, API compatibility and operational signals.

PWG-specific changes:

- P03 is now dossier inventory, not coverage matrix.
- P04–P08 keep the existing PWG spine but drop transfer-audit endings and use soft anchoring around identity, dependencies, ready queue, owner/claim, control conditions, evidence links, prime/recovery, Beads/Dolt/CLI/MCP and document-process transfer.
- Final readiness no longer blocks on `relevant but untransferred`; it blocks if key claims are closed by general prose where technical anchors are needed.

## Package changes

Rebuilt:

```text
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip
```

Both packages are self-contained and bundle the exact read-only inputs listed by their target plans plus current plan files.

Payload:

```text
27 gated records each: P01–P26 + Final
```

## Checks performed

- `unzip -t /mnt/data/adr_method_ATLAS_ARTICLE_technical_anchoring.zip` — passed.
- `unzip -t /mnt/data/persistent_work_graph_ATLAS_ARTICLE_technical_anchoring.zip` — passed.
- Runner first transition for ADR — passed: creates `01_p01_primary_article_draft.md`.
- Runner second transition for ADR after minimal target-output skeleton — passed: creates `02_p02_article_contract_and_boundaries.md`.
- Runner first transition for PWG — passed: creates `01_p01_первичный_концептуальный_черновик_статьи.md`.
- Runner second transition for PWG after minimal target-output skeleton — passed: creates `02_p02_article_contract_and_boundaries.md`.
- Payload audit — passed: 27 records in order for both packages; `P17`/`P18` are language passes; `P24`/`P25`/`P26` are style audit / selective rewrite / guarded final style.

## Notes

This change does not execute the article-writing packages and does not create `work/atlas/articles/adr_method.md` or `work/atlas/articles/persistent_work_graph.md`. It only updates the plans and rebuilds the executor packages.

The overlay is cumulative relative to `git(10).zip`: it includes the previously prepared atlas blueprint/style/SPDD/Gas Town technical-anchoring updates because the user did not declare those assistant-generated overlays applied as a new baseline.
