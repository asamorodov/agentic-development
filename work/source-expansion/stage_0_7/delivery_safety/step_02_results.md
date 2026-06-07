# Search step 2 results — database migration and rollback

## Selected sources

- Schema migration / database migration — version-controlled, incremental and sometimes reversible database changes.
- Liquibase — change logs, rollback commands, generated SQL for updates/rollbacks, database diff reports.
- Dual write / dual read / backfill patterns — migration as staged operational process rather than single code diff.

## Evaluation

Migration plan/rollback plan are necessary artifact types. AI agents can produce code diffs, but the risk often sits in data state and compatibility.

## Impact on theory

Part XII must include migration plan and rollback plan as examples of artifacts that extend SDLC beyond merge.
