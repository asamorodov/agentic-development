# P08 — техническая фактура и текущая практика

## Задача прохода

Этот проход описывает внешнюю форму механизма главы VII: кто с ним взаимодействует, что он принимает на вход, что отдаёт на выход, какие состояния хранит, какие операции разрешает, какие границы действия задаёт и где чтение отличается от действия. Это не обзор рынка. Current-practice источники используются только там, где они показывают форму механизма: Beads, GitHub/Linear issue graph, Task Master, durable execution systems and selected story anchors.

## 1. Что является механизмом главы

Механизм главы — постоянный граф работы. Его задача не в том, чтобы «хранить всё» и не в том, чтобы исполнять работу. Он должен делать продолжение работы возможным и проверяемым после смены сессии, агента, среды, review-состояния or source state.

Рабочая формула:

> Persistent Work Graph — это durable state layer, где work items, dependencies, readiness, claims, gates, source state, проверочные основания, handoff/prime, recovery and cleanup представлены так, чтобы следующий actor мог продолжить работу без угадывания.

Главное техническое различение:

- conversation transcript stores path of attention;
- issue tracker stores cards and project coordination;
- runtime checkpoint stores execution progress;
- PWG stores continuation state of work.

## 2. Участники механизма

### Executor / implementing agent

Исполняющий агент читает work graph, берёт ready work, делает изменение, возвращает результат and updates state. Он не должен сам решать, что всё изменение done, если graph-level gates and acceptance conditions are open.

Типовые действия:

- read `prime` / restoration packet;
- inspect ready queue;
- claim work item;
- inspect dependencies and gates;
- produce artifact: diff, PR, test result, source note, report;
- update work item status;
- add discovered work;
- attach source state and check signals;
- release/renew claim;
- stop/escalate if gate or authority boundary reached.

### Research / subagent

Research/subagent читает часть источников или кода and returns an output. В PWG его результат не должен попадать как бесформенный summary. Он должен стать typed update:

- source note;
- accepted/rejected research result;
- discovered work item;
- blocker;
- gate proposal;
- evidence/check candidate;
- stale or source-bound claim.

HumanLayer and Jökull both support this distinction: subagent/reviewer output is signal, not command.

### Reviewer / acceptance owner

Reviewer may be human or constrained review agent, but acceptance owner differs from implementer. Reviewer can:

- accept work;
- request fix;
- dismiss false signal;
- escalate decision;
- close gate;
- create blocker;
- change acceptance basis.

Important boundary: review output does not automatically execute. Erikson’s read-only reviewer-agent and Jökull’s Fix/Dismiss/Escalate classification show why review signal must be triaged.

### Runtime / execution environment

Runtime executes actions, stores checkpoints, handles tools, sandbox, permissions, durable waits. It can return:

- run ID;
- logs;
- diff;
- failed command;
- CI signal;
- checkpoint;
- trace/span;
- PR link;
- error condition;
- proposed next step.

PWG decides whether these outputs change work state.

### Human coordinator / maintainer

Human coordinator may:

- set scope;
- close human gate;
- accept or reject architecture decision;
- release stale claim;
- decide cleanup;
- override graph state;
- define process profile for next step.

This role is not always the same as reviewer. In a one-person workflow, the same person may play several roles, but graph state should preserve the distinction.

## 3. Inputs to PWG

### Direct work inputs

- initial work item / issue / task;
- scope description;
- acceptance criteria or success condition;
- source references;
- initial dependencies;
- risk boundary;
- owner/claim assignment;
- process profile chosen elsewhere.

### Runtime outputs

- command results;
- test results;
- CI runs;
- diffs;
- PRs;
- traces/spans;
- screenshots or Replay artifacts;
- errors;
- interrupted execution state;
- tool permission failures;
- durable workflow signals.

### Human decisions

- approval/rejection;
- compatibility decision;
- architecture boundary decision;
- scope change;
- acceptance override;
- escalation response;
- claim release.

### Subagent/reviewer outputs

- research findings;
- review comments;
- edge cases;
- false positives;
- recommended fixes;
- uncertainty notes;
- source coverage gaps;
- failed assumptions.

### Source-state changes

- branch moved;
- target branch advanced;
- PR updated;
- source doc changed;
- dependency version changed;
- CI run replaced by newer run;
- generated artifact superseded;
- old worktree removed;
- issue dependency resolved elsewhere.

## 4. Outputs from PWG

### Ready queue

A list of work items that can be acted on now, with reasons. Current practice anchor: Beads `bd ready` shows open issues without active blockers and can atomically claim a ready issue.

For chapter prose, ready output should include explanation, not only item ID:

```text
W-106 is ready: integration CI failed; no human gate needed for investigation.
W-107 is not ready: public docs depend on G-201 compatibility decision.
W-100 is not done: blocked by W-104, W-105, W-106.
```

### Blocked/gated view

A list of what cannot proceed and why:

- blocked by work item;
- blocked by human decision;
- waiting on timer;
- waiting on CI/PR;
- waiting on source refresh;
- waiting on review;
- held by active claim;
- held by stale claim needing cleanup.

Current practice anchor: Beads gates can represent human, timer, GitHub run, GitHub PR and another bead; Linear/GitHub can show blocked/blocking relationships.

### Restoration packet / prime

A compact context for the next actor:

- current work item;
- ready items;
- blockers;
- gates;
- active/stale claims;
- source state;
- last valid artifacts;
- caution notes;
- what not to redo;
- minimal protocol for using the graph.

Current practice anchor: `bd prime` produces AI-optimized workflow context, and Beads Codex integration injects it on SessionStart or after compaction-related lifecycle.

### Handoff / transfer report

Handoff differs from prime. Prime prepares a new session to operate in the work graph. Handoff transfers responsibility for a specific node:

- what was done;
- what remains;
- what cannot be decided by receiver;
- what checks are attached;
- what source state applies;
- what claim is being released/transferred;
- what next action is allowed.

### Cleanup queue

PWG should be able to emit cleanup needs:

- stale claims;
- resolved gates still open;
- old CI signal superseded;
- dead worktree;
- duplicate items;
- source notes never synthesized;
- abandoned branch;
- obsolete subagent output;
- old blocker relation that no longer blocks.

Cleanup output belongs in VII only insofar as it preserves graph truth. Broader technical debt stays for later.

## 5. Core states

### Work item statuses

Minimum useful statuses:

- open;
- in progress / claimed;
- blocked;
- gated;
- ready;
- deferred;
- closed;
- rejected/obsolete;
- needs recovery;
- needs cleanup.

Beads uses statuses such as open/in_progress/closed and excludes blocked/deferred/hooked from ready semantics. The exact vocabulary can differ; the chapter should focus on semantic function.

### Claim states

Claim state should include:

- owner;
- scope of claim;
- timestamp/heartbeat;
- source/worktree/branch/session reference;
- active/stale/released/transferred;
- whether claim blocks ready queue.

Failure modes:

- no claim → duplicate parallel work;
- stale claim → real work hidden;
- overbroad claim → blocks unrelated work;
- invisible claim → two actors overwrite each other;
- claim without source/worktree → hard recovery.

### Gate states

Gate state should include:

- type: human, timer, CI, PR, work item, source refresh, review;
- owner or resolving system;
- resolution condition;
- affected work items;
- state: pending, resolved, failed, canceled, timed out, escalated;
- source reference: PR/CI run/review thread;
- consequences on readiness.

The key current-practice detail: a gate can resolve negatively. Failed CI or closed PR is not just “not done”; it can create escalation or new work.

### Source states

Useful source-state vocabulary:

- found;
- opened/read;
- used;
- rejected;
- stale;
- superseded;
- needs reread;
- linked to commit/run/doc version;
- verified against current branch;
- unresolved conflict with newer source.

For code:

- branch;
- commit;
- PR;
- worktree;
- base branch;
- CI run ID;
- dependency version;
- migration state.

For document/source work:

- source discovered;
- read;
- transferred into text;
- linked at point of transfer;
- rejected with reason;
- figure candidate queued;
- needs asset pass.

Mark Erikson’s cachebro/OpenCode mismatch is a useful example: one layer’s source/read state did not satisfy another layer’s edit-safety state.

### Checking / acceptance state

Minimum categories:

- not checked;
- check pending;
- check passed;
- check failed;
- check obsolete/stale;
- review requested;
- review accepted;
- review rejected;
- human decision pending;
- accepted with caveat;
- rejected as false signal.

Jökull’s Fix/Dismiss/Escalate is the cleanest story anchor for this state: review signal must be classified before becoming action or blocker.

## 6. Core operations

### Read operations

Read operations should be safe and should not mutate graph state unless explicitly recorded as observation.

Examples:

- list ready work;
- show work item;
- show dependency tree;
- show blocked/gated items;
- show source state;
- show claim owner;
- show restoration packet;
- inspect artifacts/checks;
- explain why item is not ready.

Current practice anchors:

- Beads `bd ready`, `bd show`, `bd dep tree`, `bd blocked`, `bd ready --json`, `bd ready --explain`.
- GitHub CLI JSON fields for issue dependencies.
- Task Master JSON / Mermaid topology.

### Claim/update operations

Action operations mutate work state:

- claim item;
- release claim;
- mark status;
- add dependency;
- remove dependency;
- create gate;
- resolve/escalate gate;
- attach artifact;
- attach CI/review result;
- create discovered work;
- mark source stale;
- close item;
- reopen item;
- cleanup stale relation.

Danger: mutation must respect authority. An executor can attach artifact or mark local step done, but may not close human gate unless authorized.

### Gate operations

- create gate;
- check gate condition;
- resolve gate;
- timeout gate;
- escalate gate;
- convert failed gate into work item;
- link gate to affected items.

Example in billing/API:

- create human gate for compatibility decision;
- create CI gate for integration run;
- integration failure creates or updates W-106;
- human decision resolves G-201 and makes W-107 ready.

### Recovery operations

- detect interrupted session;
- inspect active/stale claims;
- locate branch/worktree/artifacts;
- compare source state with current state;
- rebuild restoration packet;
- reopen or close mistaken items;
- mark unverifiable outputs as needs review;
- transfer ownership.

Recovery must not silently invent completed work. If artifact missing, status should become uncertain or needs recovery, not done.

### Cleanup operations

- close resolved gates;
- clear stale claims;
- mark obsolete source notes;
- merge duplicate items;
- prune abandoned worktrees only after artifacts accepted or rejected;
- remove loose blockers;
- archive superseded subagent reports;
- regenerate prime after graph changes.

## 7. Reading vs acting

This distinction matters because agents often collapse observation into action.

### Reading

Reading asks:

- What is true or believed about current work state?
- What is ready?
- What is blocked?
- What signals exist?
- What source were they based on?
- What does next actor need to know?

Reading should be broadly available, safe, and machine-readable.

### Acting

Acting changes graph state or external artifacts:

- claim;
- close;
- update dependency;
- resolve gate;
- push code;
- dismiss review comment;
- accept evidence;
- delete worktree;
- merge PR.

Acting should require authority and appropriate runtime permissions. A system can read a human gate but not close it. A reviewer can mark must-fix but not modify code. A runtime can rerun CI but not declare product compatibility.

### Why this matters for chapter VII

If reading and acting are not separated, the model may treat every signal as a command. This is exactly what Jökull’s Fix/Dismiss/Escalate and Erikson’s read-only reviewer prevent. Review output should first change graph state; only then a process profile decides whether to edit.

## 8. Current-practice map without market overview

### Beads

Current form relevant to chapter:

- graph issue tracker for AI agents;
- Dolt source of truth;
- `bd ready` computed ready work;
- `bd gate` async wait conditions;
- `bd prime` restoration context;
- `bd update --claim` ownership;
- `AGENTS.md` integration;
- Codex hooks/skill setup;
- troubleshooting around blockers, sync, sandbox.

Use as primary concrete anchor.

### GitHub / Linear

Current form relevant to chapter:

- mainstream issue dependencies/sub-issues and blocked/blocking semantics;
- GitHub CLI now exposes relationships to scripts and coding agents;
- Linear UI shows blocked/blocking/related/duplicate states.

Use as baseline: PWG extends issue graph into continuation state.

### Task Master

Current form relevant to chapter:

- AI-oriented tasks with dependencies, details, test strategy, subtasks;
- clusters detect parallel execution topology;
- JSON/Mermaid outputs;
- checkpoint/resume for clusters start.

Use as secondary anchor for dependency topology and agent-facing task structure.

### Durable execution stack

Current form relevant to chapter:

- LangGraph checkpointers/stores/interrupts;
- Temporal Signals/timers/audit trail;
- Pydantic AI integrations with Temporal/DBOS/Prefect/Restate;
- Restate journal/replay/skipped completed steps;
- DBOS workflows/steps.

Use as boundary: runtime durability is not work-state durability.

### Story practice anchors

- Jökull: PR escort through CI, Greptile, Codex review; triage; iteration limit; ready-to-merge criteria.
- HumanLayer: research→plan→implement; bad research discarded; subagents as context firewall; hooks return signal.
- Erikson: source/tool state mismatch; reviewer-agent read-only role; DiffLoupe intent alignment; session reload/search.
- Mae: artifact production, human classification, trace/span/Honeycomb, worktrees, backstops, no auto-merge dependency review.

Use story anchors only for concrete transitions, not as mini-essays.

## 9. Boundaries of action

### PWG does not decide product meaning alone

It can hold a compatibility gate, but it cannot decide product compatibility unless the authorized actor does so.

### PWG does not run tests

It can attach CI/test status, mark gate resolved/failed, and block closure. The runtime/harness runs tests.

### PWG does not replace review

It can preserve review output and triage state. It does not make every review signal true.

### PWG does not replace source reading

It can mark sources as read/used/stale. It does not guarantee the reading was sufficient unless evidence/coverage conditions exist.

### PWG does not guarantee parallel speedup

It can coordinate claims and dependencies. It cannot remove semantic merge, synthesis and authority bottlenecks.

### PWG does not scale indefinitely without hygiene

Wrong dependency semantics, stale claims, stale source states and overgrown graph can make it worse than summary.

## 10. Interface sketch for billing/API example

### Input

```text
Create W-100: Add billingPlanId to change-plan endpoint.
Scope: DTO, validation, billing mapping, tests, docs.
Acceptance: unit + integration CI green; compatibility decision resolved; architecture boundary accepted; docs updated.
Source: main@8f31c2a, branch feature/billing-plan-id.
```

### During Agent A

```text
claim W-100 by Agent A
close W-101 DTO/validation locally
close W-102 mapping locally
close W-103 unit tests
attach ci/unit/18452 success
create W-104 legacy mobile compatibility discovered-from W-101
create G-201 human compatibility decision blocks W-104/W-107/W-100
create W-105 architecture boundary review
create G-202 review gate from PR thread
attach ci/integration/18453 failed
create W-106 integration failure blocks W-100
mark branch source feature@b12d44f, base main@8f31c2a
```

### At next session

```text
prime W-100
show ready:
  W-106 investigate integration failure
show gated:
  W-104 final decision pending G-201
  W-105 pending G-202
  W-107 blocked by G-201
show stale:
  source docs changed at main@9c77b40
  Agent A claim possibly stale
```

### Allowed action for Agent B

```text
recover claim state
inspect W-106
prepare options for W-104
refresh source docs
do not close W-100
do not finalize public docs before G-201
```

This sketch can be simplified in main prose.

## 11. Final drafting rule from this pass

When writing the chapter, avoid presenting PWG as a static data model. Present it as an interface for continuation:

- read what can be done;
- know why something cannot be done;
- claim only what is safe to claim;
- turn signals into typed state;
- keep source freshness visible;
- restore the next session without dumping transcript;
- close work only when graph-level conditions are satisfied;
- clean stale state so the graph remains truthful.
