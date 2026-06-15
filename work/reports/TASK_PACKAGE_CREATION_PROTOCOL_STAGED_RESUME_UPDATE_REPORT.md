# TASK_PACKAGE_CREATION_PROTOCOL — staged/resume hardening update

Status: protocol update completed.
Date: 2026-06-13.

## Reason

The Chapter I pilot package showed a failure mode: after an unexpected stop, a weaker model inspected visible package clues (`START.md`, full `TARGET_PLAN_SNAPSHOT.md`, decodable future records) and produced pass reports and final outputs too quickly. The result looked like post-factum reconstruction rather than honest execution of each materialized worksheet.

## Updated files

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md
```

## Main changes

1. Full target plans are no longer normal runtime artifacts. A regular executor package must not include an open `TARGET_PLAN_SNAPSHOT.md`, full queue, final artifact inventory, or readiness checklist. The full target plan remains build-time material.
2. Optional `PUBLIC_CONTRACT.md` is allowed only if it does not reveal future pass sequence, final outputs, or readiness criteria.
3. Added staged package mode: package builder may receive `stage_count` or `max_passes_per_stage`. The target plan is not changed; the builder only inserts planned stage stops into the record chain.
4. Stage boundaries must be real stops: stage status, stage-result archive/checkpoint, `STAGE_STOP.md`, and no automatic materialization of the next stage in the same action.
5. Added interruption/resume protocol: vague continuation after a stop means continue the current real worksheet or run the runner once if the required output exists. It never means reconstruct missing pass outputs, jump to final, or bulk-create future reports.
6. Added explicit anti-peeking requirements: do not decode future payload, do not read runner source to infer future steps, do not open a full target plan if accidentally present.
7. Added explicit bans on reconstructing missing previous pass outputs and bulk-creating future pass reports.
8. Added execution footer requirement for each substantive pass.
9. Added `INTERRUPTION_STATE.md` diagnostic requirement for emergency packaging.
10. Final `VERIFY.md` must check chain integrity, not only file existence.

## Scope boundaries

This update changes package-building protocols only. It does not rewrite existing target plans, Skeleton, Atlas articles, or Chapter I content. Existing old packages remain historical artifacts; new heavy packages should be built under this hardened protocol.

## Follow-up

Recommended next step: rebuild `CHAPTER_I_UNIT_OF_ANALYSIS` as a staged package before rerunning it on a weaker model. Do not accept the earlier ordinary-model result as clean execution of the package chain.
