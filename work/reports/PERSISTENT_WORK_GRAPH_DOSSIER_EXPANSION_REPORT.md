# Persistent Work Graph dossier expansion report — cycles 01–04

Дата: 2026-06-09.

База: пользовательский архив `git(5).zip`.

Цель текущего overlay: кумулятивно расширить `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` по всем текущим PWG-проходам: Beads/Taskmaster/durable-execution, проектные примитивы многопроходного документного процесса, parallel-agent coordination and safe parallel source-work protocol.

## Cycle 01

Первый проход расширил досье за пределы Beads-only framing:

- GitHub / Linear как baseline обычных issue-графов;
- Taskmaster как более лёгкий file/CLI AI-task graph;
- LangGraph / Temporal / Pydantic AI как соседний durable execution layer;
- новые inline links, source register, image candidates and language repair.

## Cycle 02

Второй проход перевёл материал в проектные примитивы для многопроходного документного процесса:

- `job/pass/gate/prime/recovery`;
- source state and image candidate state;
- recovery model;
- permission gates;
- durable intermediate artifacts;
- file/ledger-first recommendation before SQLite/Dolt-like storage.

Новые источники: DBOS, Restate, Intermediate Artifacts, SKILL.nb, AEGIS.

## Cycle 03

Третий проход добавил shared-state / parallel-agent coordination слой:

- CodeCRDT: observation-driven coordination, TODO claim protocol, speedup/slowdown limits, semantic conflicts;
- STORM: read snapshots, write-time validation, stale dependency rejection, reservations and intent annotations;
- MAST: multi-agent failures from organizational design and coordination;
- правила для многопроходного документного процесса: independent source shards, lock per canonical target, re-prime after stale read, merge/synthesis pass.

## Cycle 04

Четвёртый проход добавил protocol sketch безопасной параллельной работы с источниками:

- Anthropic multi-agent research system as evidence for lead-agent decomposition, source shards, subagent task boundaries, CitationAgent and duplicate-work failure modes;
- Claude Code subagents / agent teams / worktrees as practical surfaces for isolated work;
- Codex Worktrees and Git worktree as file-isolation layer;
- LangChain multi-agent docs as general vocabulary for subagents, handoffs and routing;
- protocol rule: parallelize discovery/opening, but keep canonical dossier write and final synthesis under a separate owner/gate;
- worker return package: source IDs, opened URLs, factual claims, quotes within limits, image candidates, confidence, conflicts, rejected sources and next-step hints;
- citation/source audit and synthesis pass before canonical update.

## Terminology cleanup

The internal shorthand previously used in some working materials was removed from public/readable text. The dossier now uses neutral terms:

- `многопроходный документный процесс`;
- `параллельная работа с источниками`;
- `пакет свидетельств`;
- `проход синтеза`.

A cleanup note is included for one old pass-02 filename from the earlier overlay if it already exists in an applied working copy.

## Boundary preserved

Persistent Work Graph не отождествлён с Beads, CRDT editor, STORM-like file mediator, worktree isolation or durable execution runtime. Итоговая формула:

```text
Persistent Work Graph = durable work state: task/job, dependencies, owner, gate, readiness, handoff, prime, recovery.
```

Соседние слои:

- durable execution resumes runs;
- shared-state coordination helps concurrent agents observe each other;
- worktree isolation reduces file collisions;
- file mediation can reject stale writes;
- evidence/language/source gates decide whether dossier output is acceptable.

## Checks

Performed in local workspace:

```text
python3 -m json.tool work/checks.json
unzip -t persistent_work_graph_dossier_cycles_01_04_delta_from_git5.zip
```

## Rollback note for cycle 05

`cycle_05` was rejected and must not be treated as part of the canonical PWG dossier line. The canonical state is `cycles_01_04`. The rejected pass moved too far from source-backed dossier expansion into a provisional implementation sketch. If the implementation sketch is useful later, it must be reintroduced as a separately approved technical note, not as part of the current PWG mechanism dossier.

See `work/reports/PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md`.
