# Atlas usage — Chapter VII

## `work/atlas/articles/persistent_work_graph.md`

Фактически использован как главный conceptual baseline. Перенесены:

- PWG as durable work state outside session;
- work item identity and boundaries;
- ready/claim/gate/review/recovering states;
- relation semantics and ready queue;
- source state;
- prime/recovery;
- graph failure/cleanup.

Не переносить дословно большие таблицы и JSON schema; chapter uses billing/API example instead.

## `work/atlas/articles/gas_town.md`

Использовать только boundary:

- Gas Town = broader multi-agent environment;
- PWG = portable work-state mechanism inside such environment.

Не переносить Mayor/Deacon/Polecat/Rig vocabulary unless chapter X.

## Atlas visual assets

- Use `content/assets/theory-images/beads-task-graph-memory.svg`.
- Defer `gastown-architecture.svg`, `gastown-basic-workflow.svg`, `gastown-mayor-hub.webp` to chapter X.
