# RESUME — C3_PWG_TO_EVIDENCE

Status: `completed`
Readiness: `ready_with_known_debts`

## What this package contains

The C3 fragment is a theory bridge from Persistent Work Graph state to evidence-backed completion. Its central claim is that a graph cannot safely move a work item to `completed` just because an executor stopped, tests passed, a run finished or a review sounded positive. Completion must be an accepted transition supported by an addressed evidence package, an oracle matched to the promise and an acceptance owner who can take the residual risk.

## Main constructed elements

- `C3_pwg_to_evidence.md` contains the main argument and one inline synthetic figure, `fig-c3-completion-transition-guard`.
- `C3_source_usage.md` records how public sources support concrete claims and keeps internal dossiers out of citation targets.
- `C3_story_anchor_map.md` limits field stories to state-transition anchors.
- `C3_figure_candidates.md` classifies all visual candidates by asset policy and leaves only the approved synthetic figure inline.
- `C3_open_questions.md` records remaining publication and terminology debts.
- `C3_degradation_and_duplication_audit.md` records repair passes, regression checks and readiness.

## Known debts for the next stage

- Decide final terminology for machine-like fields and states such as `promise`, `attachment_address`, `completion_gate`, `accepted`, `completed`, `stale` and `needs_stronger_oracle`.
- Decide whether one or two example anchors should move from C3 into an atlas, fieldbook or operational evidence chapter if the assembled chapter becomes too example-heavy.
- Run a Stripe freshness/source pass if the Stripe Minions / integration benchmark anchor remains in the publication version.
- Run a later visual/composition pass to check the length and placement of `fig-c3-completion-transition-guard` against A7/A8.

## Continuation guidance

Use this package as a completed working result, not as a publication-final chapter. The fragment is ready for downstream writing with known debts explicitly recorded.
