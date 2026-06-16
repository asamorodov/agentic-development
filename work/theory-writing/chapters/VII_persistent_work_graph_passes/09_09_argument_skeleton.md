# P09 — скелет аргумента главы VII

## Проверка задачи

Глава VII не должна стать каталогом инструментов: Beads, GitHub, Linear, Task Master, LangGraph, Temporal, HumanLayer, Jökull, Mae, Erikson. Все источники должны войти только через одну линию аргумента: длинная агентская работа распадается, если её состояние хранится как summary/transcript/local done; для продолжения нужен постоянный граф работы, где готовность, блокировки, claims, gates, source state and closure conditions are explicit.

Скелет ниже — не оглавление в финальной форме, а последовательность аргумента. В каждом блоке указано: какую функцию он выполняет, какую фактуру использует и чего избегать.

## 1. Начальная сцена: «почти готово», которое нельзя продолжить

### Функция

Открыть главу не определением, а практическим сбоем. Читатель должен сразу увидеть знакомую ситуацию: первая сессия действительно много сделала, но следующая не может безопасно продолжить из summary.

### Материал

Billing/API example:

- endpoint `POST /subscriptions/change-plan`;
- add `billingPlanId`;
- DTO/mapping/tests locally done;
- legacy mobile payload edge case;
- unit CI green;
- integration CI failed/pending;
- architecture boundary review open;
- compatibility decision pending;
- subagent result about old API contract;
- branch/source advanced;
- stale claim from previous agent.

### Главная мысль

Summary says “almost done.” Work state says: some nodes are closed, some blocked, some gated, some stale, some ready for investigation.

### Чего избегать

Не начинать с Beads or PWG definition. Не делать сцену слишком длинной. Достаточно показать, что prose summary loses state needed for action.

## 2. Центральный сбой: локальное `done` не равно завершению изменения

### Функция

Назвать главный failure pressure. Это сердцевина главы.

### Логика

Agent A can honestly finish local patch. But graph-level work remains open:

- implementation node closed;
- compatibility gate open;
- review gate open;
- CI gate failed;
- source state stale;
- docs blocked;
- claim needs cleanup.

### Формулировка для будущего текста

Не «модель врёт», а «локальный конец принят за конец работы на неправильном уровне». Это делает тезис сильнее и взрослее.

### Связанные источники

- Jökull: PR not ready until CI/Greptile/Codex feedback triaged and clean.
- C3: completion as state transition.
- C4: run trace does not close work.

### Чего избегать

Не превращать в обвинение моделей. Не уходить в полную теорию evidence.

## 3. Почему summary, transcript, issue list and checkpoint insufficient

### Функция

Развести соседние формы до введения PWG.

### Последовательность различений

1. Summary: narrative of what happened; cannot compute readiness.
2. Transcript: rich path of attention; too noisy and not structured for continuation.
3. Issue list: useful project coordination; may not know gates, source state, evidence, claims, restoration context.
4. Runtime checkpoint: can resume process; not equivalent to work-state semantics.

### Материал

- A4: “отчёт сделано много” not state.
- B2/C4: durable execution vs durable work.
- LangGraph/Temporal/Pydantic/DBOS/Restate as boundary facts.
- GitHub/Linear as baseline issue graph.

### Чего избегать

Не обесценивать issue trackers and runtime. Нужно признать их полезность, затем показать недостающий слой.

## 4. Введение PWG как формы продолжения

### Функция

Дать центральное определение главы после того, как необходимость уже показана.

### Определение

Persistent Work Graph — долговечный граф work items, relations, readiness, claims, gates, source state, checking/acceptance state, handoff/prime and cleanup, который позволяет следующему actor понять, что можно продолжать, что нельзя, почему нельзя и что требуется для закрытия.

### Акценты

- Work item is durable object.
- Readiness is computed from graph state.
- Gate is durable wait condition.
- Claim protects parallel work but can become stale.
- Source state makes outputs non-floating.
- Restoration packet prepares next session.
- Cleanup keeps graph truthful.

### Источники

- Beads as current practice anchor, but after definition.
- Internal PWG atlas/dossier.

### Чего избегать

Не давать длинную database schema. Не делать список полей без narrative pressure.

## 5. Разбор work item and relation semantics через пример

### Функция

Показать, что PWG не просто «task graph». Relation types matter.

### Материал из примера

- W-100 billing/API change;
- W-101 DTO/validation closed locally;
- W-104 legacy compatibility;
- W-105 architecture boundary;
- W-106 integration failure;
- W-107 docs;
- G-201 compatibility decision;
- G-202 architecture review;
- G-203 CI run.

### Различения

- `parent-child` ≠ `blocks`;
- `related` ≠ blocker;
- `discovered-from` ≠ hard dependency;
- source note ≠ work item;
- review signal ≠ command;
- check signal ≠ acceptance.

### Источники

- Beads core concepts: dependency types, only blocks affects ready work.
- GitHub/Linear: mainstream blocked/blocking/sub-issue baseline.
- Task Master: task dependencies and execution topology.

### Чего избегать

Не перегрузить читателя псевдосхемой. Использовать пример как объяснение, not as tool spec.

## 6. Ready, claim, gate: operational heart of the chapter

### Функция

Дать центральный механизм: how the graph answers “what can happen now.”

### Ready

Ready is computed. It should show not only items but reasons. Example:

- W-106 ready for investigation;
- W-107 not ready until G-201;
- W-100 not done.

Beads `bd ready` is the main external anchor.

### Claim

Claim prevents duplicate parallel work and creates recovery obligations. Need introduce stale claim as own failure mode:

- active claim;
- stale claim;
- claim scope;
- claim cleanup.

### Gate

Gate is a durable wait:

- human decision;
- CI run;
- PR merge;
- timer;
- another work item;
- source refresh.

Beads `bd gate` is the main external anchor. Jökull’s CI/review loop and Temporal human-in-the-loop can be used as nearby examples.

### Чего избегать

Не углубляться в CLI syntax. Not “how to use Beads,” but “what the mechanism makes explicit.”

## 7. Signals and checking state: review output must be triaged

### Функция

Развести signal, evidence/check, gate and action. This prevents chapter from being too static.

### Material

Jökull’s `/babysit-pr`:

- waits for CI and Greptile;
- runs `codex review --base main`;
- classifies feedback as Fix/Dismiss/Escalate;
- iterates until clean state or max three iterations;
- exit criteria: CI green, no untriaged issues, PR ready to merge.

Jökull real case:

- CI green;
- Greptile observation dismissed;
- Codex found two real semantic problems;
- second pass clean and auto-merge queued.

Erikson:

- DiffLoupe intent alignment;
- read-only reviewer-agent; `edit: deny`;
- reviewer distinguishes must fix / should fix / consider.

Mae:

- human classifies diff, type errors, Honeycomb UI, `/review`, dependency recommendation;
- no auto-merge in dependency review.

### Argument

A signal does not automatically tell the system what to do. It must enter PWG as classified state: fix item, dismissed signal, human gate, accepted check, failed check, stale signal.

### Чего избегать

Не перетаскивать всю историю Jökull/Mae/Erikson. Use one compact example and maybe one supporting sentence.

## 8. Source state: work is tied to changing sources

### Функция

Добавить недостающий слой, который часто теряется: outputs are only valid relative to source state.

### Billing/API examples

- subagent report based on old docs;
- unit CI belongs to commit `b12d44f`;
- target branch advanced;
- docs changed;
- review comment may refer to old version;
- integration run failure may be stale after rebase.

### Source family facts

- A4 document source states: found/opened/used/rejected/needs reopen/transferred/stale.
- Mark Erikson cachebro/OpenCode mismatch: read state known to MCP but not to edit permission layer.
- Mae/Honeycomb and Erikson/Replay: traces and recordings are source artifacts for runtime observation.

### Argument

PWG does not need full history of everything. It needs the source-state markers that affect continuation and closure.

### Чего избегать

Не turn into provenance chapter. Keep tied to readiness and stale state.

## 9. Prime / restoration packet: how next session becomes competent

### Функция

Show how PWG becomes usable across session boundaries.

### Distinctions

- Prime/restoration packet ≠ full summary.
- Handoff ≠ prime.
- Recovery ≠ normal handoff.

### Material

Beads `bd prime`:

- AI-optimized markdown context;
- session start/compaction use;
- Codex hooks integration;
- memories-only, full reference, `.beads/PRIME.md`.

HumanLayer:

- startup context should be short and relevant;
- progressive disclosure;
- avoid encyclopedic `AGENTS.md`.

Mark Erikson:

- session search/reload and context pruning help recovery but are not graph state;
- overcompressed output can confuse agent.

### Argument

A good restoration packet should show ready/gated/blocked/stale/claims/source state and safe next actions. It should not dump transcript.

### Чего избегать

Не дублировать главу VI on hooks/skills. Keep focus: graph supplies restoration content; interfaces deliver it.

## 10. Current-practice external anchor section

### Функция

Ground chapter in external tools after conceptual mechanism is clear.

### Order

1. Beads: `ready`, `gate`, `prime`, Dolt source-of-truth, `AGENTS.md`, claim/update, troubleshooting caveats.
2. GitHub/Linear: mainstream dependencies/relations.
3. Task Master: task graph and clusters as lighter AI task topology.
4. Durable execution stack: boundary contrast.

### Style

Use sources as supports, not as a catalogue. Each source should answer one question:

- Beads: what does a PWG-like practice look like?
- GitHub/Linear: what does mainstream issue graph already know?
- Task Master: how does task topology become agent-facing?
- Durable execution: what is not PWG?

### Чего избегать

Do not list products. Do not include URLs in main text without source purpose. Do not overuse release/version details.

## 11. How PWG itself fails

### Функция

Prevent idealization. Show graph needs hygiene.

### Failures

- wrong dependency types;
- all relations treated as blockers;
- ready queue empty due to overblocking;
- stale claims;
- resolved gates remain open;
- failed gates not escalated;
- source state stale;
- subagent output untriaged;
- overgrown graph unreadable;
- repair removes semantically valid relation;
- sync/storage/migration issue in work graph infrastructure;
- cleanup deletes materials before review.

### Sources

- Beads troubleshooting;
- Beads architecture cautions;
- Mark `rtk grep` bad compaction;
- Mae “not committed state” issue from LinkedIn note;
- C4 cleanup section.

### Argument

PWG is not magic. It gives a place to maintain work truth; it can also become a source of false truth if not maintained.

### Чего избегать

Do not make this a gloomy operational appendix. Keep it as part of mechanism: graph truth requires cleanup.

## 12. Boundary with neighboring chapters

### VI

VI: project interface, skills, hooks, MCP, route selection. VII: state left by those routes.

Bridge example: hooks may deliver `bd prime`; PWG contains what prime needs.

### VIII

VII: where the work is and what is known. VIII: which process profile should act next.

Final bridge: when graph shows W-106 ready, W-104 gated, W-107 blocked, next question is not “what happened?” but “which mode of action fits this node?”

### IX

IX: execution environment, sandbox, worktree, durable runtime, rights. VII: work-state semantics.

Boundary: worktree isolates write but not meaning; durable execution resumes run but not work decision.

### X

X: Gas Town broader organization. VII: minimum portable work graph. Beads can anchor VII without importing whole Gas Town.

### XI/XII

XI/XII: evidence/authority/acceptance. VII: enough checking state to prevent false done.

### XIII

XIII: cleanup/debt more broadly. VII: cleanup of graph truth only.

## 13. Possible final chapter flow

Working structure:

1. **A session ends with “almost done”** — billing/API scene.
2. **Why local done is the wrong level** — done at patch level vs graph level.
3. **Why summary, transcript, issue list and checkpoint are insufficient** — distinctions.
4. **Persistent Work Graph as continuation state** — definition and promise.
5. **The work node is not a task card** — relations, source state, artifacts.
6. **Ready, claims and gates** — operational heart.
7. **Signals must be triaged** — Jökull + reviewer examples.
8. **Source state makes continuation honest** — stale sources, branch/CI/doc versions.
9. **Prime and recovery** — next session gets compact work picture.
10. **Current practice: Beads and neighbors** — Beads, GitHub/Linear, Task Master, durable execution boundary.
11. **How the graph lies if not cleaned** — failure modes.
12. **Bridge to process profiles** — graph shows state; next chapter chooses method.

## 14. Anti-catalog checks

Before drafting, verify each source insertion by asking:

- Which work-state transition does this source explain?
- Does it support ready, gate, claim, source state, signal triage, prime, recovery or cleanup?
- Would the chapter still move forward if this source paragraph were removed?
- Is the source being used as evidence or as an accidental mini-review of a tool?
- Does it pull the reader into VI/VIII/IX/X/XI/XII/XIII?

If a source fails this test, keep it in pass file or footnote queue, not in main prose.

## 15. Drafting thesis in one paragraph

The future chapter should be able to compress to this argument:

> In agentic development, work often outlives the session that produced the most visible result. A patch can be locally done while the change remains blocked by review, CI, source freshness, a human decision, an unresolved edge case or an untriaged subagent output. A summary can describe this situation, but it cannot reliably compute what is ready, what is blocked, who owns it, what evidence belongs to which source state, and what the next session may safely do. Therefore long-running agentic work needs a persistent work graph: a durable, machine-readable and human-inspectable state of work items, dependencies, claims, gates, source states, checking signals and restoration packets. This graph does not replace the runtime, the issue tracker, the reviewer or the process profile. It makes their outputs usable for continuation.
