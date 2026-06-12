# A6 composition / visual / style repair report

Date: 2026-06-11

## Evaluation before repair

A6 already performed its central theoretical task: it distinguished several layers that are often collapsed into “agent environment” — execution boundary, tool/sensor surface, workflow engine, platform agent and the boundary with Persistent Work Graph. The source base was strong and the examples were not merely retold as stories.

Before repair, the working value was about **8/10**, but publication readiness was closer to **6.5/10**.

## Diagnosed problems

1. **Visual overload.** The main text had 18 inline figures on about 240 lines. Many figures repeated adjacent prose or belonged to a technical atlas rather than the core theory.
2. **Recovered-asset captions.** Real local images were captioned as “recovered source screenshot / local file,” which exposes the assembly process instead of explaining the figure to the reader.
3. **Synthetic figure overuse.** Worktree lifecycle, sandbox permission boundary, logs/browser/local scripts, Roast DSL, Quix corridor and Stripe platform path all contained useful details, but too many of them were inline at once.
4. **English connective layer in figures.** Some retained diagrams used English connective prose that was not a command, product name or exact source term.
5. **Integration risk.** A6 was starting to take material that belongs in A7/evidence or technical atlas: MCP context-cost imagery, Selective Test Execution and detailed workflow/CI substrate diagrams.

## Applied changes

- Main A6 reduced from **18 figures** to **6 figures**.
- Kept as real local assets:
  - `fig-a6-sandvault-separate-user-worktrees`
  - `fig-a6-humanlayer-harness-components`
- Kept as synthetic figures:
  - `fig-a6-agent-environment-four-layers`
  - `fig-a6-agent-as-node-not-system`
  - `fig-a6-same-story-different-layer-matrix`
  - `fig-a6-runtime-vs-pwg-boundary`
- Removed from inline and moved to figure-candidate statuses:
  - `fig-a6-sandbox-permission-boundary`
  - `fig-a6-worktree-lifecycle-and-handoff`
  - `fig-a6-claude-codex-worktree-isolation`
  - `fig-a6-logs-browser-local-scripts-as-sensors`
  - `fig-a6-ronacher-logs-local-scripts`
  - `fig-a6-mcp-context-cost-vs-deterministic-code`
  - `fig-a6-pi-minimal-harness-extension-surface`
  - `fig-a6-roast-dsl-pipeline`
  - `fig-a6-quix-klaus-kode-deterministic-corridor`
  - `fig-a6-devbox-platform-agent-substrate`
  - `fig-a6-stripe-minion-platform-path`
  - `fig-a6-stripe-selective-test-execution-substrate`
- Rewrote captions for real image assets as public explanatory captions.
- Russianized remaining synthetic-figure connective prose where it was not an exact technical name.
- Preserved the core source facts and inline external citations.

## Evaluation after repair

- Working value: **~8.4/10**.
- Publication readiness: **~7.5/10**.
- Status: `ready_with_known_debts`.

A6 is now a stronger theoretical node and a better input for C4. It still has known debts: final composition may decide whether both real assets should remain in the main chapter, and technical atlas can recover the more detailed sandbox/worktree/Roast/Quix/Stripe diagrams.
