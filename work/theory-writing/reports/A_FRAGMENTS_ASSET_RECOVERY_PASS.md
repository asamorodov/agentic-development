# A-fragments asset recovery pass

## Scope

This pass was run after the correction that ready source illustrations must not be degraded into textual diagrams. It operates on A-fragments in `work/theory-writing/fragments/` and creates a catalog under `work/theory-writing/asset-catalog/`.

## What changed in main fragments

Fifteen inline figures were recovered from synthetic/text placeholders to existing local assets:

| Fragment | Figure | Asset |
| --- | --- | --- |
| A1 | `fig-a1-change-lifecycle-overview` | `content/assets/story-images/01-boris-agentic-lifecycle.svg` |
| A1 | `fig-a1-evidence-and-authority` | `content/assets/theory-images/openai-codex-citations-evidence.webp` |
| A1 | `fig-a1-session-trace-vs-durable-state` | `content/assets/theory-images/beads-task-graph-memory.svg` |
| A3 | `fig-a3-spdd-closed-loop` | `content/assets/theory-images/fowler-spdd-workflow.svg` |
| A3 | `fig-a3-drift-taxonomy` | `content/assets/theory-images/fowler-spdd-code-review.svg` |
| A4 | `fig-a4-pwg-minimal-node` | `content/assets/theory-images/beads-task-graph-memory.svg` |
| A5 | `fig-a5-method-pwg-organization-stack` | `content/assets/theory-images/gastown-architecture.svg` |
| A6 | `fig-a6-humanlayer-harness-components` | `content/assets/story-images/07-humanlayer-harness-components.png` |
| A6 | `fig-a6-sandvault-separate-user-worktrees` | `content/assets/story-images/08-mike-sv-claude.png` |
| A6 | `fig-a6-mcp-context-cost-vs-deterministic-code` | `content/assets/theory-images/humanlayer-too-many-mcp-tools.png` |
| A7 | `fig-a7-browser-observation-evidence` | `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` |
| A7 | `fig-a7-showboat-rodney-replay` | `content/assets/story-images/03-simon-showboat-curl-demo.jpg` |
| A7 | `fig-a7-working-traces-matrix` | `content/assets/theory-images/openai-codex-citations-evidence.webp` |
| A8 | `fig-a8-local-sandbox-action-boundary` | `content/assets/theory-images/mike-superset-worktrees.png` |
| A9 | `fig-a9-post-merge-repair-loop` | `content/assets/theory-images/fowler-harness-continuous-feedback.png` |

The rest of the A-fragment figures remain synthetic because they are conceptual state machines, comparison tables, method maps or authorial diagrams rather than known lost source images.

## External candidates not downloaded

External candidates from dossiers were cataloged but not downloaded. They include BMAD workflow map, Spec Kit Mermaid workflow, Kiro blog diagrams, Constitutional SDD ar5iv/PDF figures, TDAD arXiv figures, Gas Town/Beads diagrams, AWS ADR diagrams and several source screenshots/code fragments. The pass deliberately stops before downloading because each one needs a rights/quality/placement decision.

## Path convention

Inline fragment images use `src="../../../content/assets/..."` and duplicate the repo-relative asset path in `data-repo-path`. This keeps the fragment directly viewable in the repository while preserving the asset identity for later site assembly, where paths may need rewriting to `assets/...`.

## Remaining queue

1. Decide which external candidates deserve localization rather than redrawing.
2. For selected external candidates, run a separate `download/rights/quality` pass.
3. Add dimensions/alt text after actual image localization.
4. During final site assembly, rewrite fragment-local paths if the fragment is moved under `content/`.
