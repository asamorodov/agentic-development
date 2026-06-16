# P07 — добор по главным source families

## Назначение прохода

Этот проход собирает дополнительную фактуру по главным семействам источников главы VII. Здесь не пишется основной текст. Цель — не потерять практические детали: команды, статусы, режимы сбоя, переходы между фазами, ограничения, странные operational edge cases и примеры, которые делают будущую главу плотной, а не декларативной.

Главная проверка для переноса: факт должен помогать объяснить механизм постоянного графа работы — work items, dependencies, ready state, claims, gates, проверочные основания, source state, handoff/prime, recovery or cleanup. Если факт только интересен сам по себе, но ведёт в соседнюю главу, он фиксируется как boundary/defer.

## 1. Внутренние фрагменты A4/B2/C2/C3/C4: что добрать в главу

### A4 — граница рабочего состояния

A4 даёт отрицательную рамку главы: отчёт «сделано много» не является состоянием работы. Важно перенести не только эту фразу, но и конкретные формы распада:

- technical loss of context;
- незакрытое человеческое решение;
- ожидание review;
- ожидание CI;
- проверка цитаты or source claim;
- согласование формулировки;
- конфликт между соседними ветками работы;
- текст появился раньше проверочного основания;
- статус `done` поставлен до закрытия нужной точки ожидания;
- два агента прочитали один источник and diverged in transferred claim;
- следующая сессия продолжает по stale snapshot;
- человек должен принять решение, но агент заменяет его гладкой формулировкой;
- source note remains in work map and never gets synthesized.

Это хороший список для раннего раздела главы. Он показывает, что проблема не одна: PWG нужен потому, что длинная работа распадается сразу по нескольким осям.

A4 также даёт формулу положения PWG: между разговором и организацией. Разговор хранит локальную траекторию внимания, но плохо хранит обязательства. Организация хранит роли and responsibility, but does not necessarily know which source was read, which evidence supported a claim, which waiting point is still open. Эта формула полезна для границы с Gas Town и с обычным process management.

Ключевая деталь A4: в документной работе источники сами имеют state. Source может быть:

- found;
- opened/read;
- used in main text;
- rejected with reason;
- queued for reopening;
- transferred into canonical text;
- stale because the target text changed;
- seen only as a link but not actually inspected.

Это нужно перенести в главу как general source state, not only document-work peculiarity. В коде аналогами будут commit, branch, PR, CI run, API doc version, package version.

### B2 — вклад PWG в общую теорию

B2 формулирует сильную мысль: работа как долговечный объект. Это нужно развить не как метафору, а как набор свойств work item:

- identity: work item survives session;
- boundary: scope of work is known;
- dependencies: what it waits on and what it blocks;
- readiness: whether it can be picked up;
- owner/claim: who currently holds write/action responsibility;
- gates: what external conditions must resolve;
- acceptance basis: what would make closure valid;
- source state: what code/docs/run it is based on;
- artifacts: where produced material lives;
- handoff/recovery: how another actor resumes;
- cleanup: what must be closed or removed after transition.

B2 also warns against treating Task Master as enough. Task Master can carry task dependencies and test strategy, but the chapter needs more: right to close, source state, handoff, cleanup, evidence/acceptance state. This contrast is useful because readers may otherwise think «это просто tasks.json with dependencies».

### C2 — bridge to process profiles

C2’s key distinction: process задаёт ход; PWG удерживает продолжимость. This should shape the end of chapter VII.

Facts to preserve:

- A profile like research→plan→implement can produce several state transitions, not just one output.
- A role becomes real only through its consequences in state: reviewer, implementer, researcher, gate owner, acceptance owner.
- Process imitation begins when outputs do not change work state: a plan that does not create work items; a review that does not block/accept anything; a summary that does not update source state.

For the final bridge to VIII, use C2’s language carefully: VII should not prescribe the process profile. It should show the node’s current state so the next chapter can choose the profile.

### C3 — transition to evidence/acceptance

C3 is useful but dangerous for VII. Need pull only the minimal layer:

- completion is a state transition, not a declaration;
- evidence/acceptance object must outlive the executor;
- owner of acceptance may differ from executor;
- oracle must be chosen by the promise of the work, not by what is convenient for the agent;
- `completed` is not valid if acceptance basis is missing or mismatched.

Terminology caution: avoid making «свидетельство» central. Use `evidence` where source-native; otherwise use «проверочные основания», «состояние проверок», «основания принятия», «сигналы проверки». Chapter VII needs graph state, not full evidence theory.

### C4 — execution runtime vs PWG

C4 gives the clean boundary with runtime:

- запуск создаёт след, но не завершает работу;
- durable execution and durable work are different;
- worktree isolates write, but does not coordinate meaning;
- evidence package links execution environment to work lifecycle;
- cleanup belongs to the work graph, not only filesystem maintenance.

Important operational details:

- Runtime can return run ID, artifacts, logs, diff/report, errors, limits, proposed next step.
- PWG decides whether this result becomes a state transition.
- Git worktree can be pruned/repaired technically, but cannot decide whether candidate work is still needed for review or recovery.
- Worktree isolation solves write conflict, not semantic conflict.

This should support a concise boundary section: a durable process can resume; a graph of work decides what should be resumed, accepted, rejected, blocked or cleaned.

## 2. Beads / PWG source family: detailed facts

### Beads as direct practice anchor

Beads should be the main current-practice anchor, but not the subject of the chapter. Use it as proof that several pieces of PWG are not hypothetical:

- distributed graph issue tracker for AI agents;
- persistent structured memory for coding agents;
- dependency-aware graph for long-horizon tasks;
- Dolt as source of truth;
- JSON output for agents/scripts;
- graph links and dependency tracking;
- auto-ready detection;
- hash IDs;
- compaction;
- CLI commands that are agent-readable and scriptable.

The chapter should avoid version fragility: current release page warns that v1.0.5 is gated and v1.0.4 is latest. Therefore, do not anchor the conceptual text on “current version 1.0.5”. Anchor on commands/mechanisms.

### `AGENTS.md` / `bd init` protocol

The Beads README says `bd init` updates `AGENTS.md` with minimal Beads workflow instructions. This is useful because it shows that PWG is not only a database. It must be connected to the agent’s startup protocol.

Commands named in minimal protocol:

- `bd prime` — load context / workflow surface;
- `bd ready` — find ready work;
- `bd show` — inspect issue;
- `bd update --claim` — claim work;
- `bd close` — close work;
- `bd remember` — store project memory;
- warning: do not use Markdown TODO lists.

Potential chapter transfer:

A project that wants agentic continuation must tell the agent at startup where the work graph is and how to use it. Otherwise the graph exists but the agent returns to chat-local memory or TODO markdown.

### `bd ready`: readiness is computed

Relevant command facts:

- Shows open issues with no active blockers.
- Excludes `in_progress`, `blocked`, `deferred`, `hooked`.
- Same semantics as `bd list --ready`.
- `--claim` atomically claims first ready issue.
- `--gated`, `--mol`, `--explain` exist as useful options around execution/gated work/readiness explanation.

Chapter transfer:

Ready is not a human adjective. It is a graph answer. A node becomes ready through dependency/gate/status/claim conditions. This is the strongest way to separate “agent says done” from “graph says the next work is claimable.”

Failure details from troubleshooting:

- `bd ready` showing nothing may mean open blockers.
- Use `bd blocked`, `bd dep tree`, `bd show`, `bd ready --json` to inspect.
- Only `blocks` dependencies affect ready work.
- Complex dependency trees confuse agents; simplify dependency structure or use labels for loose relationships.

Chapter transfer:

Readiness itself can fail if graph semantics are misused. Too many hard blockers or wrong relation types can hide valid work.

### `bd gate`: durable wait conditions

Relevant facts:

- Gates are asynchronous wait conditions blocking workflow steps.
- Gate types include `human`, `timer`, `gh:run`, `gh:pr`, `bead`.
- `bd gate check` resolves gates when conditions are met.
- GitHub run gate resolves on completed/success; PR gate resolves when merged; timer resolves after timeout; bead gate resolves when target is closed.
- Failure/cancellation/closed PR can escalate.
- An ad hoc gate issue can block another issue until resolved.

Chapter transfer:

Gate is the missing object between “we are waiting for something” and “the task is ready.” In the billing/API example:

- compatibility decision = human gate;
- architecture boundary review = human/review gate;
- integration CI = `gh:run`-like gate;
- PR merge = `gh:pr` gate.

Do not overcomplicate with Beads syntax in main prose. The conceptual point: a gate stores pending external condition and its consequences for work readiness.

### `bd prime`: restoration after session start/compaction

Relevant facts:

- Outputs essential Beads workflow context in AI-optimized Markdown.
- Adapts between MCP mode and CLI mode.
- CLI mode can output full reference roughly 1–2k tokens.
- Designed for Claude Code, Gemini CLI, Codex SessionStart hooks.
- Purpose includes avoiding forgotten Beads workflow after context compaction.
- Supports `.beads/PRIME.md`, `--export`, `--memories-only`.

Codex integration details:

- `bd setup codex`.
- Uses skill, managed `AGENTS.md`, hooks.
- Codex 0.129.0+ supports hooks/compact lifecycle/hook-provided developer context.
- SessionStart injects full `bd prime`.
- PreCompact checks memories-only and warns, but does not inject full context because Codex ignores plain stdout from compact hooks.
- PostCompact records need refresh.
- UserPromptSubmit injects full prime once after compaction.

Chapter transfer:

This is a very strong bridge between VI and VII. Hooks/session lifecycle deliver context, but what they deliver is a restoration packet derived from work graph. `prime` should be framed as protocol/state refresh, not a narrative summary.

### Dolt/source-of-truth / sync / recovery details

Relevant Beads architecture facts:

- Dolt is sole storage backend and source of truth.
- Every write auto-commits.
- Embedded mode default; server mode for multiple agents/orchestrator.
- Recovery through `bd dolt pull` or backup restore.
- Dolt gives version-controlled SQL, cell-level merge, multi-writer server, offline operation, JSONL export.
- Multi-machine sync requires push before switching, pull before creating issues, avoid parallel edits unless server mode.
- `bd doctor --fix` can be dangerous if it removes semantically valid dependencies that look circular.
- Beads not ideal for large teams 10+, non-developers, real-time collaboration, cross-repo tracking, rich media.

Chapter transfer:

PWG has infrastructure risk. It is not “put tasks in a graph and forget.” Its own storage, sync, migrations, repair and cleanup become part of work reliability. This can support a late section on graph hygiene, but should not derail the main chapter.

### Troubleshooting / sandbox details

Useful facts:

- Debug env vars: `BD_DEBUG`, `BD_DEBUG_RPC`, `BD_DEBUG_SYNC`, `BD_DEBUG_ROUTING`, `BD_DEBUG_FRESHNESS`.
- Port/server confusion can make `bd` show 0 issues although DB has data.
- Dolt journal corruption after unclean shutdown requires careful recovery, not blind file deletion.
- `database is locked` — do not remove Dolt internal lock files; risk of data corruption.
- Sandboxed environments can cause out-of-sync errors because sandbox cannot signal/kill existing Dolt server process.
- Issue #3313: maintenance commands `bd admin cleanup` / `bd admin compact` failed in embedded mode; workaround forced direct SQL and bypassed audit trail.

Chapter transfer:

These details are probably too operational for the main body, but they give one important caution: work-state infrastructure can itself have stale, corrupted or inconsistent state. A chapter sentence can say PWG requires operational discipline; a footnote/source-linked aside can mention sync/recovery/maintenance.

## 3. GitHub / Linear / Task Master: baseline issue graph and task graph

### GitHub Issues and sub-issues

Facts:

- Issues plan, discuss and track work.
- Sub-issues break larger work into hierarchy and can display progress in projects.
- Issue dependencies express blocked-by/blocking relationships.
- PR keywords can close issues.
- Assignees communicate responsibility.
- Sub-issue limits: 100 sub-issues per parent, up to eight nested levels.

Chapter transfer:

GitHub shows that hierarchy and dependencies are already mainstream. Use it as baseline, not as PWG. Parent-child hierarchy is not the same as blocker graph.

### GitHub CLI issue dependencies for agents

Fresh fact:

- June 10, 2026 GitHub CLI added/exposed issue types, parent/sub-issue relationships and issue dependencies from terminal.
- Options include `--parent`, `--blocked-by`, `--blocking` and JSON fields.
- Changelog explicitly mentions scripts and coding agents relying on `gh`.

Chapter transfer:

This is strong support for the claim that agent-readable issue structure is becoming current practice. It helps say: for agents, relationships hidden only in UI are not enough; they must be accessible through CLI/API/JSON.

### Linear issue relations

Facts:

- Supports blocking, related, duplicate.
- Blocked-by shows an orange flag; blocking shows red flag.
- Resolved blocker turns blocked flag green and moves relationship under Related.
- Duplicate moves to reserved Duplicate status.

Chapter transfer:

Good visual/semantic baseline. Use to explain relation semantics. But PWG needs this state to participate in ready/claim/prime/acceptance, not only project UI.

### Task Master

Task structure facts:

- `tasks.json` fields: `id`, `title`, `description`, `status`, `dependencies`, `priority`, `details`, `testStrategy`, `subtasks`, `metadata`.
- Individual task files preserve dependency list and test strategy.
- Designed for humans and AI assistants.

Clusters facts:

- Detects execution clusters: groups of tasks that can run in parallel, sequenced by dependency DAG.
- `tm clusters` visualizes topology.
- Tags at same level can run in parallel; higher levels depend on lower levels.
- Task-level clusters group tasks with same topological level and no dependencies on each other.
- Output formats: table, ASCII tree, Mermaid, raw Mermaid, JSON.
- `tm clusters start` builds execution plan, shows plan for review, launches Claude Code with agent teams mode.
- Options: `--dry-run`, `--parallel <n>`, `--resume`, `--continue-on-failure`, `--json`.
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set for agent teams.
- Navigation link for Loop was 404; do not use Loop facts.

Chapter transfer:

Task Master supports the “topology” part of the chapter. It shows task graph becoming execution topology, not just a planning artifact. But it should not be overused: parallel execution belongs closer to VIII/IX; VII uses it to justify readiness/dependencies/source state.

## 4. Jökull Sólberg: PR as a work object with gates and triage

### `/babysit-pr` facts

`/babysit-pr` is a Claude Code skill: markdown procedure, around 170 lines. It treats PR as an object to escort through external checks and review loops.

Workflow steps:

1. Detect current PR through `gh pr view`.
2. Wait for CI and Greptile in parallel.
3. Process whichever source finishes first while the other is still running.
4. Run local `codex review --base main`.
5. Classify all feedback as Fix / Dismiss / Escalate.
6. Fix valid items.
7. Run linter.
8. Commit and push.
9. Run checks again.
10. Repeat until clean state or iteration limit.

Exit criteria:

- CI green;
- no untriaged issues;
- PR ready to merge.

Limit:

- maximum three iterations;
- if not clean after several passes, human probably needs to inspect.

Chapter transfer:

This is almost a concrete instance of gates/readiness. PR is not ready just because code was pushed. It is ready when external checks are resolved and feedback triaged. The iteration limit is also important: autonomous loops need a stop condition and escalation path.

### Fix / Dismiss / Escalate

Categories:

- Fix: valid issue, local fix clear, scope allowed.
- Dismiss: false, wrong assumption, not related to current change.
- Escalate: human needed for product boundary, architecture choice, risk beyond scope.

Important nuance:

- CI failures are fixed by default.
- Codex review leans toward Fix because local review catches logical gaps.
- Greptile comments are evaluated separately.
- Small issues can be dismissed if nontrivial to fix and not meaningful.

Chapter transfer:

This is the best story anchor for “review signal is not command.” In graph terms, a feedback item must become one of: work item, rejected signal, human gate. Without triage, one model mechanically obeys another.

### Multiple check sources

Three checking layers:

- CI: objective formal failures — typecheck, lint, test regressions.
- Greptile: reads PR in codebase context, can find architecture problems, sometimes noisy.
- Codex review: independent local review, catches naming inconsistencies, edge cases, logical holes.

Jökull’s real example:

- CI green: build, lint, typecheck, tests.
- Greptile high confidence and one observation about best-effort webhook delivery; dismissed as operational question, not code bug.
- Codex found two real issues: UI text inconsistent with new behavior; unpublish→republish left tour in wrong state.
- After fixes, second pass: CI still green, Greptile no new issues, auto-merge queued.
- Main lesson: formal checks and Greptile missed semantic problems; Codex found them; triage prevented blind obedience.

Chapter transfer:

Use to show that different signals affect graph differently. CI green is a check signal, not total acceptance. A code review comment can be work, dismissed, or human gate. Ready-to-merge is a derived state after multiple signals, not a feeling.

### Skill and durable procedure

Jökull moves repeated processes into skills and `CLAUDE.md`:

- skill contains conditions, inputs, sequence, tools, result format, check rules, examples, stop/human escalation rules;
- if an agent learned a procedure or domain rule, prompts include:
  - `Summarize everything you learned and create a new Claude skill`
  - `Add the context I explained to the right CLAUDE.md`

Chapter transfer:

This belongs mainly to VI, but for VII it shows that procedure memory and work-state memory must meet. `/babysit-pr` is not PWG; it is a process/skill that should read and update PR work state.

### Context transition

Jökull’s context management:

- when long session reaches roughly 5–10% context remaining, better transition to fresh context;
- ask Claude to make concrete plan with checkable steps;
- split large work into pieces for parallel execution.

Chapter transfer:

Useful as support for restoration packet. When a session is close to context limit, summary alone is not enough; a plan/checkable state must be transferred into durable form.

## 5. HumanLayer: harness, research→plan→implement, subagent outputs

### Research → plan → implement

HumanLayer’s strongest sequence:

- research can be wrong;
- bad research should sometimes be thrown away rather than polished;
- plan without research may still produce working code but worse fit architecture;
- research-informed plan changes where the code should be changed and what tests should be written;
- checking research/plan has higher leverage than reviewing final diff.

BAML positive example:

- large Rust codebase around 300k LOC;
- Dex was amateur Rust developer and new to codebase;
- process `research → plan → implement` produced bugfix PR approved next morning;
- initial research incorrectly concluded codebase was correct; it was discarded and re-run with better steering;
- two plan passes were compared: without research and with corrected research;
- research-informed plan matched codebase conventions and test strategy better.

Parquet/Hadoop negative example:

- attempt to remove Hadoop dependencies from parquet-java;
- about seven hours spent;
- research not deep enough through dependency tree;
- plan assumed classes could move upstream, but deeper Hadoop dependencies broke premise;
- failure chain: shallow research → wrong dependency map → plausible plan → real graph breaks delta.

Chapter transfer:

This is source-state/dependency-state material. A research output is not truth; it is a candidate graph update. If research is wrong or too shallow, it should not become plan/done. PWG should mark research state: accepted, rejected, stale, needs deeper pass, blocks implementation.

### Human alignment and artifacts

HumanLayer emphasizes that large AI PRs create loss of shared understanding:

- teams cannot review 2k-line generated Go PRs every few days by reconstructing intent from diff;
- research, specs, plans, tests and criteria become human-inspectable artifacts;
- transition required about eight weeks and changed professional posture: less heroic line-by-line review, more early/high-leverage artifact review.

Chapter transfer:

PWG is not only for agents. It must also be human-inspectable. If the graph is only machine-readable, it loses social function.

### `CLAUDE.md` / `AGENTS.md` and progressive disclosure

HumanLayer facts:

- good startup instructions answer WHAT / WHY / HOW;
- should be short, not encyclopedia;
- their own file is reportedly under about 60 lines;
- generated agentfiles can hurt; human-written ones provide small benefit; long/generic directory listings rarely help;
- progressive disclosure: point to sources, don’t copy everything into initial context;
- conditional blocks should activate when relevant.

Chapter transfer:

This supports `prime` and restoration packet: context must be compact and relevant. PWG should not dump entire graph; it should show right work surface.

### Subagents as context firewall / compaction

HumanLayer treats subagents less as a team of specialists and more as context firewall:

- subagent isolates noisy research/search/tool output;
- parent receives compressed result;
- subagent can perform research and return summary/artifact;
- but summary can lose evidence, assumptions and source coverage.

Chapter transfer:

Subagent output must return to PWG as typed state: work item, source note, evidence candidate, blocker, gate, rejected hypothesis. Otherwise it becomes just another prose summary.

### Hooks and stop hooks

HumanLayer facts:

- hooks manage flow, not another request;
- Stop hook can run checks and return error to agent, forcing it back into work;
- mechanical checks should be tools, not model instructions.

Chapter transfer:

Hooks are VI/IX boundary, but the chapter can mention that a hook/check must update graph state or gate status if it affects continuation.

### Ralph autonomous loop

HumanLayer facts:

- autonomous loop strengthens specification but does not replace it;
- desired state must be small for refactoring;
- loop does not solve weak spec.

Chapter transfer:

Useful caution: autonomy over a weak/unstable work item produces noise. PWG should hold desired state and stop/escalation condition.

## 6. Mark Erikson: external state/context, permission/state mismatch, reviewer role

### Context navigation and file state

Erikson’s environment gives detailed source-state facts:

- agent should navigate code through hierarchy: directory overview, `grepika toc`, search, outline, line ranges, symbol search, call graph, cache reading;
- quality of context matters more than quantity;
- `cachebro` caches file reads and returns unchanged or diff on reread;
- but OpenCode’s internal edit permission logic did not know files read through cachebro MCP were read;
- Erikson built `cachebro-bridge` via Plugin API to propagate file access time to OpenCode.

Chapter transfer:

This is an excellent concrete source-state mismatch: one tool knows a file was read; another layer that controls editing does not. For PWG, source state must be shared across the relevant execution/permission/work graph layers, or the system produces false blockers or unsafe edits.

### Failed context optimization

`rtk grep` was disabled because compressed grep output changed format too much and confused the agent, causing loops.

Chapter transfer:

A compact artifact is not automatically better. Restoration packet/prime must preserve the structure a model can actually use. Overcompressed work state can create false understanding.

### Session tools and context pruning

Facts:

- `/tokens` calls `context_usage` and returns category/tool breakdown: system, user, assistant, tools, reasoning.
- `/session-reload` initially exported OpenCode session JSON to markdown.
- OpenCode moved from JSON files to SQLite; Erikson rewrote session history plugin through `client.session`.
- Tools: `search_sessions`, `read_session`, `reload_session` with regex search, temporal decay, snippets, transcript reading, compaction messages filtered by default.
- Dynamic Context Pruning plugin provides `compress`: preserves relevant parts rather than one giant summary.

Chapter transfer:

This supports the difference between transcript/history and PWG. Session search/reload helps recover conversation context, but PWG should not rely only on transcript search. Still, these tools are useful for recovery when graph state is incomplete.

### Permissions and human authority

Facts:

- Read/edit allowed; Bash default ask.
- Safe commands allowed: `git status`, `git diff`, `git log`, `ls`, `pwd`, `rg`, `cat`, `pnpm test *`, `pnpm build`, `pnpm typecheck`, `rtk *`.
- Dangerous commands denied: `sudo *`, root/home `rm -rf`, force push, `git reset --hard`.
- Custom permission checker auto-approves file ops for dev-plans/temp paths, analyzes shell commands, logs decisions.
- Handles inline `bun -e`, heredocs, command substitution, process substitution, redirection, `sed -i`, command chains.
- OpenCode permission refactor broke plugin return status; Erikson maintained local fork.

Chapter transfer:

Permission state is not PWG, but it affects which work transitions are allowed. A graph item can be ready, while runtime permission prevents action. Conversely, runtime permission can allow action while graph state says human gate blocks final decision.

### Replay MCP and observability as source state

Facts:

- React 19 PR broke Playwright E2E.
- Human saw `findDOMNode is not a function` in Replay quickly.
- Agent wandered for 10–15 minutes because `ConsoleMessages` tool was broken.
- Screenshot revealed error overlay; logpoint extracted error.
- Erikson built Replay MCP tools: `RecordingOverview`, `ReactRenders`, `ReduxActions`, Zustand/TanStack Query tools.
- With right observation channel, same type of problem could be found under a minute or under ten minutes.

Chapter transfer:

Observation tool output can become source state/evidence. But if the observation tool is broken, the work item should not be closed. PWG can distinguish “test failed”, “observation channel broken”, “runtime state not visible”, “needs replay artifact.”

### DiffLoupe and reviewer-agent

Facts:

- `/code-review` runs DiffLoupe over staged/unstaged/HEAD/branch/PR/commit.
- Produces derived intent, risk assessment, intent alignment.
- Reviewer agent is read-only: `edit: deny`; allowed commands include `git diff`, `git show`, `git log`, `git blame`, `rg`, `wc`, `head`, `tail`.
- Reviewer philosophy: diffs alone are not enough; read full modified files; do not invent hypothetical problems; do not nitpick linter style; only review changed code; distinguish must fix / should fix / consider.

Chapter transfer:

This supports reviewer role as separate from implementer. Review output should become graph state, not automatic code edits. It also strengthens “intent alignment” as a check distinct from tests.

## 7. Mae Capozzi: platform work, artifacts, traces, observability and cleanup

### Common workflow structure

Mae’s reconstructed workflow has a useful sequence:

1. Scope task.
2. Use plan mode or turn plan into Linear tickets.
3. Give agent real context: Figma MCP, `tsconfig`, build setup, changelog, current config, CI scripts, PR, dependency version, status, Honeycomb MCP.
4. Move work into isolated/limited environment: `git worktree`, `/tmp/linear-{issueId}`, PR comment, telemetry draft.
5. Produce checkable artifact: PR, Linear ticket, test branch, GitHub Action comment, trace, span, migration branch, summary of check, Git checkpoint.
6. Human classifies: diff, type errors, Honeycomb UI, `/review`, dependency recommendation, merge decision, lint/backstop if recurring risk.
7. Environment improves: lint rule, codemod, hook telemetry, `TRACEPARENT`, Honeycomb board for adoption/cost/cache/tool latency/rejected actions.

Chapter transfer:

This is almost a “work returns to graph” sequence. Each agent run produces artifact and observation; human classification changes status; recurring risk becomes environment rule. Use Mae to show PWG is not just code tasks: traces, spans, dashboards and backstops become work-state artifacts.

### `hub-team` / orchestrator details

Facts from source map:

- `hub-team` includes six phases and restoration points.
- Planning coordinator and specialists.
- Uses `child_process.spawn()`.
- Timeouts: 15/10 minutes.
- Negative PID detail.
- `git worktree` in `/tmp/linear-{issueId}`.
- `TRACEPARENT` and Honeycomb trace.
- Current limitations acknowledged.

Chapter transfer:

Do not turn VII into orchestrator chapter. Use only as evidence that multi-agent systems need traceable restoration points and shared identifiers (`TRACEPARENT`) to understand which child process/specialist produced which result.

### Telemetry / Honeycomb facts

Facts:

- Claude writes OpenTelemetry boilerplate.
- Honeycomb MCP gives production signal.
- Verification happens through Honeycomb UI.
- Claude Code hooks / `.claude/settings.json` can produce spans/events: `InstructionsLoaded`, `SessionStart`, `UserPromptSubmit`, `ToolUse`, `SessionEnd`.
- Attribute example: `instructions.file_path`.
- Honeycomb Claude Code ROI/adoption setup: `CLAUDE_CODE_ENABLE_TELEMETRY`, OTLP metrics/logs exporters.
- Query: `COUNT | GROUP BY event.name`.
- Event types include `api_request`, `tool_result`, `api_error`, `tool_decision`, `user_prompt`.
- MCP command: `claude mcp add honeycomb --transport http https://mcp.honeycomb.io/mcp`.
- Board fields include adoption, ROI, cost, tool latency, prompt caching, rejected actions, `user.account_uuid`, `session.id`, `terminal.type`, `claude_code.cost.usage`, `tool_name`, `decision`.

Chapter transfer:

These are strong but mostly VI/IX/XI facts. For VII, use only the state angle: observability events can identify which instructions loaded, which session/tool action occurred, and whether a result is attributable. They can support PWG recovery and source state, but trace ≠ work graph.

### Migration and backstop facts

Facts:

- UI/design system: Claude 3.7 hallucinated requirements, reinvented components, preferred Tailwind; Claude 4 + `CLAUDE.md`, Figma Dev Mode MCP, richer design system reused `Button` and `DropdownMenu` and CSS modules.
- Migrations often get stuck around 80%; need lint rule/backstop before migration to prevent new old-pattern usage.
- Agents are bad at one-shot complex migrations but useful for codemods and semi-automated tail processing.
- `tsc`→`tsgo` migration used separate `git worktree`, informal prompt with `tsconfig` and build setup, then human reviewed type errors; build time 44s→7s in the story.
- Platform toil reduction includes research probes, CI test PRs, dependency reviews, instrumentation before deploy, cleanup/deletion work.
- Dependency review: Conductor GUI for multiple Claude Code instances with git worktrees, role `Goalie`, GitHub Action, 15-minute timeout, flaky tests, no auto-merge.

Chapter transfer:

Backstops are graph-relevant as gates/acceptance conditions. Migration state needs more than “80% done”; it needs blocked tail, source patterns, backstop status, failing cases, owner decisions. Dependency review is PR/state review, not auto-merge.

## 8. Gas Town: boundary-only facts

Gas Town should not take over chapter VII. Use only boundary facts from atlas/dossier:

- Gas Town is broader agentic environment; PWG/Beads can live inside it as substrate.
- Gas Town has town/rig/roles/workflow levels; chapter X likely expands this.
- For VII: use one short pointer that PWG is not whole town/organization/cast of roles.

Avoid:

- importing Mayor/Deacon/Polecat/Witness roles unless chapter explicitly needs boundary sentence;
- explaining gas stations;
- using Gas Town images unless figure pass asks.

## 9. Durable execution family: boundary and useful contrasts

### LangGraph

Facts:

- Checkpointers persist thread graph state for conversation continuity, human-in-the-loop, time travel, fault tolerance.
- Stores persist application-defined data across threads for facts/preferences/shared knowledge.
- Interrupts pause graph execution, save graph state, wait indefinitely, resume via `Command`.
- Rules: do not wrap interrupts in try/except; do not reorder interrupt calls within node; side effects before interrupt must be idempotent.

Chapter transfer:

Good boundary: runtime can pause and resume graph execution. PWG must still show work semantics: what decision is pending, what item is blocked, what evidence resolves it.

### Temporal

Facts:

- Human-in-the-loop example: LLM proposes action; risky action waits for human approval via Temporal Signal; executes, cancels, rejects or times out.
- Can wait for hours/days/indefinitely without compute while waiting.
- Durable timers survive disruption.
- Audit trail records decisions.

Chapter transfer:

Use as implementation-shaped example of durable human gate. But approval signal is not entire PWG.

### Pydantic AI / Temporal / DBOS / Restate

Facts:

- Pydantic AI supports durable agents through Temporal, DBOS, Prefect, Restate.
- Durable agents preserve progress across transient API failures, application errors/restarts, long-running asynchronous and human-in-loop workflows.
- Temporal: replay mechanism, saves inputs/decisions, deterministic workflows vs non-deterministic activities; workflow code generally cannot do network/disk I/O; activities can do I/O but restart from beginning on failure.
- Restate: journal every execution step; replay journal, skip completed steps, resume exactly where left off; persisted LLM calls avoid refetching; tool executions wrapped in durable steps to avoid duplicated side effects.
- DBOS: wraps agent run loop as workflows and model/MCP requests as steps; custom tool functions/event handlers may need explicit `@DBOS.step` or can be skipped if durability not needed.

Chapter transfer:

Use to say: durable execution is real and important, but it solves another layer. It stores process progress and side-effect safety. PWG stores work semantics and readiness.

## 10. Visual/assets family

Primary visual asset for VII:

- `content/assets/theory-images/beads-task-graph-memory.svg`

Existing A4 already uses this as image asset with caption: Beads as graph of tasks, dependencies, ownership and memory. Must preserve as image reference, not rewrite into synthetic text diagram by default.

Possible figure functions for VII:

1. Minimal PWG node: work item, dependencies, gates, claim, source state, acceptance basis, restoration packet.
2. Summary vs PWG comparison: same billing/API state as prose vs graph-ready state.
3. Durable execution vs PWG boundary: runtime checkpoint/resume versus work graph readiness/claim/gate.
4. Signal triage: CI/Greptile/Codex/reviewer → Fix/Dismiss/Escalate/Gate/Done.

Need respect visual memory: existing real assets should remain images; synthetic figures only if newly authored conceptual tables/diagrams.

## 11. Candidate details for main chapter insertion

### Detail 1 — Ready can be empty for good reason or bad graph hygiene

From Beads troubleshooting: `bd ready` may show nothing because all open issues have blockers. This can be correct. But it can also mean dependency types were misused. In text, this can support graph hygiene: a PWG is only useful if relation semantics remain clean.

### Detail 2 — Gate resolution is not always success

From Beads gate: GitHub run can fail/cancel and escalate; PR can close rather than merge. In the billing example, CI gate should not become a binary “done/not done”; failed gate may create new work item or human escalation.

### Detail 3 — Agent-readable CLI/API is becoming mainstream

GitHub CLI issue relationship update is useful: issue dependencies are moving from UI-only to CLI/JSON usable by scripts and coding agents. This supports the broader claim that AI-era work state must be machine-readable.

### Detail 4 — Review signal requires classification

Jökull’s Fix/Dismiss/Escalate and Erikson’s reviewer-agent both show the same principle: review output is not a command. It must be triaged and attached to graph state.

### Detail 5 — Source state mismatch can be between tools

Erikson’s cachebro/OpenCode mismatch is a concrete example of state split across layers. One tool’s read state did not satisfy another tool’s edit-safety state. This can illustrate why PWG cannot be isolated from execution/permission state, even if layers differ.

### Detail 6 — Trace is not enough, but trace helps recovery

Mae/Honeycomb and Erikson/Replay show trace/observability artifacts. They do not replace work graph, but they can provide source/evidence for it: session ID, tool decision, error overlay, spans, traceparent.

### Detail 7 — Backstop before migration

Mae’s backstop principle can appear as a gate: migration work should not progress to mass automated tail if new old-pattern uses are still allowed. This may be better for a later chapter, but it supports “done” must include prevention of regression, not just changed files.

### Detail 8 — Prime should be right-sized

HumanLayer warns against encyclopedic startup context; Beads `prime` adapts context; Mark’s `rtk grep` failure shows overcompressed output can confuse. Restoration packet must be compact but structurally faithful.

## 12. Material to avoid or defer

Defer to VI:

- full discussion of hooks, skills, MCP surfaces;
- detailed `CLAUDE.md`/`AGENTS.md` design;
- HumanLayer progressive disclosure as a whole.

Defer to VIII:

- detailed process profiles;
- research→plan→implement as full method;
- Task Master clusters as orchestration plan;
- subagent personalities/roles.

Defer to IX:

- worktree implementation details;
- sandbox/permissions syntax;
- durable execution runtimes;
- DBOS/Temporal/Restate mechanics.

Defer to X:

- Gas Town organizational structure and role taxonomy.

Defer to XI/XII:

- full theory of evidence, acceptance, oracle choice;
- rollout/canary evidence;
- migration benchmarks and acceptance metrics.

Keep in VII:

- only the parts that affect visibility of work state and whether next action/closure is allowed.

## 13. Suggested source family priority for drafting

1. Start from internal A4/B2/C4 frame: summary ≠ work state; local done ≠ graph done; runtime ≠ PWG.
2. Use billing/API example from P06 as narrative spine.
3. Bring Beads after conceptual frame, using `ready`, `gate`, `prime`, Dolt/source-of-truth.
4. Use GitHub/Linear/Task Master as baseline, not main object.
5. Insert Jökull as PR-gate/triage story anchor.
6. Insert HumanLayer/Erikson/Mae only where needed:
   - HumanLayer: research output and subagent result must be triaged into state;
   - Erikson: source/tool state mismatch and reviewer role;
   - Mae: artifact/trace/human classification/backstop pattern.
7. Close with durable execution boundary and bridge to VIII.

## 14. One-sentence synthesis after deepening

The strongest evidence across source families points to the same mechanism: agentic work cannot be safely continued from transcript memory because every serious continuation depends on typed state — which node is open, what blocks it, what signal has been triaged, what source state the signal belongs to, who owns the next action, what external gate is pending, and what compact restoration packet makes the next session competent without making it omniscient.
