# Chapters VII–X natural-Russian rewrite report

Date: 2026-06-15

## Scope

This pass rewrote the currently integrated Chapter VII–X texts in-place for natural Russian prose. It did not add new source material, change the factual/source base, remove figures, or alter the chapter-level argument. The task was editorial: reduce English connective prose, mixed-language sentences, self-commentary, awkward кальки, and over-technical wording while preserving source links, figures, examples, and the existing structure.

Changed chapter files:

- `work/theory-writing/chapters/VII_persistent_work_graph.md`
- `work/theory-writing/chapters/VIII_protected_process_profiles.md`
- `work/theory-writing/chapters/IX_execution_environment_runtime_rights.md`
- `work/theory-writing/chapters/X_gas_town_beads.md`

## What was changed

- Chapter VII: cleaned the PWG/restoration/cleanup sections, reduced English connective prose around reviewer/subagent/PWG examples, and rewrote the final boundary section in normal Russian.
- Chapter VIII: kept the GSD integration repair intact, reduced residual terminology problems, and preserved the shift from “профили” to “способы продолжения работы”.
- Chapter IX: performed the largest rewrite. The opening, sandbox/permission/approval distinctions, command/tool/browser sections, durable execution, platformization and final synthesis were rewritten to remove half-English explanatory prose.
- Chapter X: kept Gas Town/Beads terms where they are source terms, but rewrote explanatory passages so that Gas Town appears as an organizational layer rather than a source vocabulary dump.

## Preserved

- All Markdown external links are preserved.
- Figure blocks and HTML figure/table fragments are preserved.
- The main examples remain: Chapter VII billing/API/PWG, Chapter VIII billing/API/GSD/BMAD, Chapter IX billing execution environment, Chapter X payment webhook/Gas Town.
- Source-specific terms remain where useful: `sandbox`, `permission`, `approval`, `runtime`, `worktree`, `MCP`, `tool`, `hook`, `Gate`, `Beads`, `Mayor`, `rig`, `GUPP`, etc. The pass removed English glue, not all technical English terms.

## Resulting sizes

- `VII_persistent_work_graph.md` — 41526 characters, 399 lines.
- `VIII_protected_process_profiles.md` — 34204 characters, 209 lines.
- `IX_execution_environment_runtime_rights.md` — 40465 characters, 192 lines.
- `X_gas_town_beads.md` — 38343 characters, 229 lines.

## Checks

- No heading duplicates were found in the four chapter files.
- Markdown external links were left intact.
- Image/figure references were preserved. They are site-relative/project-relative references already present in the integrated chapters.
- The pass intentionally does not claim canonical acceptance: Chapter VII still deserves a separate source-intake audit, and VIII–X may still need later visual or chapter-specific polish. This pass resolves the immediate language problem.
