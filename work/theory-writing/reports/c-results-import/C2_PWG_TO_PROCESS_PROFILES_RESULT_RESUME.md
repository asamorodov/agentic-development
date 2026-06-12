# RESUME — C2_PWG_TO_PROCESS_PROFILES

Status: completed
Readiness: `ready_with_known_debts`

## What was built

The target group now contains a completed C2 bridge fragment. The main argument distinguishes process profiles from PWG: GSD and BMAD can provide phases, roles, documents, checkpoints and recovery behavior, but PWG is the durable work-state layer that makes those outputs actionable across sessions, handoffs, context compression, parallel work and human decisions.

## Current main-file shape

- Opening: separates PWG from process profiles and defines the criterion of state consequence.
- GSD section: phase rhythm, `.planning/`, `STATE.md`, `CONTEXT.md`, `PLAN.md`, `VERIFICATION.md`, checkpoints, UAT/ship and `gsd-pi` Auto Mode as recovery example.
- Inline synthetic figure: maps process outputs to PWG state responsibilities.
- BMAD section: roles, phases, PRD/architecture/story/status lifecycle, `SPEC.md`, `.decision-log.md`, readiness outcomes, story creation/dev/correct-course/investigation and manual status decision.
- Process-theater section: explains failure mode when roles, plans, handoffs or gates do not change durable work state.
- Boundary section: uses Beads/PWG as practical anchor and Gas Town as upper organizational boundary.

## Companion files

- `C2_source_usage.md` records every external source used and the claim it supports.
- `C2_story_anchor_map.md` confirms C2 does not retell narrative stories and keeps them as neighboring anchors.
- `C2_figure_candidates.md` records the one inline synthetic figure and deferred/rejected candidates, including BMAD workflow map as an external real image candidate.
- `C2_open_questions.md` records publication debts.
- `C2_degradation_and_duplication_audit.md` records general repair passes, language passes, style passes, regression checks and readiness.

## Remaining debts

- Freshness-check GSD/Open GSD, BMAD and Gas Town public pages before publication.
- Decide during a broader C-group visual pass whether the single synthetic figure is enough.
- Consider moving detailed `gsd-pi` Auto Mode or Gas Town lifecycle facts into profile/atlas material if later fragments need more depth.

No emergency packaging was required.
