# A9 composition / visual / style repair report

Date: 2026-06-11

## Scope

Reviewed `work/theory-writing/fragments/A9_lifecycle_repair.md` against `A9_LIFECYCLE_REPAIR_TARGET_GROUP_PLAN.md`, the visual-asset protocol and the fragment-defect repair protocol. Repair was performed as a local composition / visual / style pass, not a source expansion pass.

## Evaluation before repair

A9 already performed its core theoretical function: it framed post-merge work as a lifecycle repair loop. The fragment correctly connected stale specification/ADR/rules/skills/hooks/work graph/workspace/release evidence to the future action of agents and humans. It also avoided treating Product Migration as independent proof of migration success.

Estimated pre-repair status:

| Criterion | Evaluation |
|---|---:|
| Working value | ~8/10 |
| Publication readiness | ~6.5/10 |
| Status | `ready_with_known_debts` |

Main defects:

1. Visual overload: 7 inline figures for a 128-line fragment.
2. Service caption on a real local image asset (`Восстановленная source-иллюстрация`, local path narration).
3. Three router/matrix figures duplicated one another and made the text look like a checklist/control table.
4. Some language remained pseudo-technical or too English-connected (`stale map`, `feedback signal`, tail/checklist phrasing).
5. Main text still risked crossing into technical atlas through detailed routing diagrams.

## Applied changes

- Reduced A9 inline figures from 7 to 4.
- Kept one real local image asset: `content/assets/theory-images/fowler-harness-continuous-feedback.png`.
- Rewrote the image caption as a public explanatory caption with no recovery-service text.
- Kept three nontrivial synthetic figures:
  - stale context → rational wrong action;
  - advisory memory vs enforceable guardrail;
  - migration oracle/evidence decision.
- Removed from inline and documented in `A9_figure_candidates.md`:
  - `fig-a9-artifact-freshness-matrix`;
  - `fig-a9-feedback-signal-router`;
  - `fig-a9-repair-target-selected-by-signal`.
- Replaced several awkward formulas around lifecycle tail, stale map and checklist drift with direct Russian phrasing.
- Preserved source-specific names and commands where they are actual mechanisms: `AGENT-BRIEF.md`, `/handoff`, `triage`, `PreToolUse`, `PostToolUse`, `bd gate`, `bd prime`, `can-i-deploy`, `AnalysisTemplate`, `AnalysisRun`, `worktree`, `cutover`, `rollback`.

## Evaluation after repair

| Criterion | Evaluation |
|---|---:|
| Working value | ~8.3/10 |
| Publication readiness | ~7.5/10 |
| Status | `ready_with_known_debts` |

A9 is now closer to surrounding repaired A-fragments: it has a clearer argument, fewer decorative/control figures, public asset captions and less service narration. It remains intentionally source-dense, because A9 is a bridge between ADR/spec repair, skills/hooks, PWG cleanup, migration, incident and release feedback.

## Remaining debts

- Final terminology pass should decide how aggressively to translate source terms like `skill`, `hook`, `gate`, `worktree`, `oracle`, `cutover`, `rollback`.
- ADR/release-specific real image candidates remain deferred to technical atlas until rights/quality/placement check.
- A future public incident/release case could strengthen this fragment, but only if it has PR/CI/release/postmortem artifacts.
