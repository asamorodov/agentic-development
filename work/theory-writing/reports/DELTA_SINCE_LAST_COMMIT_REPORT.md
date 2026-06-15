# Delta since last user-committed baseline

Baseline interpreted as the point where the user said: “Состояние зафиксировано, можно строить дельту отсюда”.

This overlay contains the post-baseline theory-writing changes that should be applied on top of that commit. It deliberately excludes the rejected `CHAPTER_I_UNIT_OF_ANALYSIS_RESULT.zip` produced by the interrupted/cheating run.

## Included groups

1. Post-Atlas chapter planning blueprints: global preparation blueprint and per-chapter writing blueprint.
2. Skeleton V5 language/style cleanups.
3. Global corpus routing plan, package, and accepted routing result.
4. Updated task-package creation/manufactory protocols with no-final-hints, interruption/resume, staged-package and chain-integrity rules.
5. Chapter I target plan and current packages: staged-3 and no-stage variants under the new protocol.
6. Chapter II and III target plans, individuality/language patches, packages, and accepted result files.
7. Chapter IV, V, VI target plans and individuality/language patches.
8. Updated reports, working map, discourse, checks, apply notes and commit message.

## Not included

- Rejected `CHAPTER_I_UNIT_OF_ANALYSIS_RESULT.zip` from the interrupted run.
- Raw temporary smoke-test directories.
- Generated one-off helper scripts in `/mnt/data`.

## Apply note

Apply this overlay to the repository state from the baseline commit. It should supersede the many smaller overlays produced after that point.
