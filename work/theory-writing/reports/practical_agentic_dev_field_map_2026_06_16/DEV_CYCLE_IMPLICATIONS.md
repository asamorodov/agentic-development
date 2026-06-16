# Dev Cycle Implications

Дата обзора: 2026-06-16  
Назначение: практические выводы для собственного doc-first / package-driven / agentic development процесса.

## 1. Main operational shift

Следующее улучшение dev-cycle — не «попробовать больше агентов». Более точная формула:

> Сделать repository instructions, task packages, verification bars, run logs and acceptance material дисциплинированным версионируемым слоем процесса, которым могут пользоваться разные агенты.

Поле показывает, что выигрышная единица — не clever prompt. Выигрышная единица — repeatable working package with:

- explicit task boundary;
- canonical input files;
- allowed output files;
- allowed tools and forbidden actions;
- expected verification commands;
- rollback/emergency packaging rule;
- acceptance criteria;
- human-readable run summary;
- update path for instructions after failure.

Это хорошо совпадает с текущим package workflow. Внешнее поле добавляет имена, сравнительные примеры и предупреждения.

---

## 2. What to add to every serious task package

### 2.1. Agent-facing contract

Каждый пакет должен иметь compact agent-facing contract:

- What is the task?
- What is out of scope?
- Which files are canonical inputs?
- Which files may be edited?
- Which files are read-only?
- What output artifacts are mandatory?
- What counts as normal completion?
- What counts as emergency stop?
- What must be packaged if interrupted?

Это уже частично есть в текущих пакетах, но стоит стандартизировать.

### 2.2. Verification bar

Пакет должен заранее задавать verification bar:

- commands to run;
- text-level checks;
- source-link checks;
- no-degradation checks;
- chapter-specific checks;
- expected report files;
- unresolved-risk section.

Verification bar должен быть конкретнее, чем “review the result”.

### 2.3. Run log without private chain-of-thought

Output должен содержать run log / execution summary, not private chain-of-thought:

- files read;
- files changed;
- external sources used;
- commands run;
- checks passed/failed;
- manual decisions made;
- unresolved risks;
- recommended next actions.

Так сохраняется полезная continuity без скрытого reasoning.

### 2.4. Instruction repair section

Каждый failed or partially successful package должен спрашивать:

- Was the task boundary unclear?
- Were allowed files/tools underspecified?
- Was the verification bar too weak?
- Did the agent miss a project convention?
- Did a repository instruction become stale?
- Should `AGENTS.md` / package template / style protocol / chapter plan be changed?

Это практическое значение Instructions-as-Code.

---

## 3. Repository instruction strategy

### 3.1. Create a cross-agent `AGENTS.md`

Репозиторию нужен conservative cross-agent `AGENTS.md` at root. Он не должен дублировать всю документацию. Он должен говорить агентам, как безопасно работать в этом репозитории.

Recommended sections:

1. Project role and current artifact map.
2. Language/style rules.
3. Source/provenance rules.
4. Editing rules: minimal changes, no unexplained rewrites, preserve detail density.
5. Package execution rules.
6. File-system and overlay rules.
7. Verification/reporting requirements.
8. Forbidden shortcuts.
9. Emergency stop packaging.
10. Where to find richer instructions.

Keep it short enough to be used. Long protocols should remain linked files.

### 3.2. Keep tool-specific files as adapters

`CLAUDE.md`, Cursor rules, Kiro steering, Codex instructions or Amp instructions should adapt the shared process to a tool. They should not become independent contradictory truth.

A useful structure:

- `AGENTS.md` — cross-agent root instructions.
- Tool-specific instruction files — adapter layer.
- Package `START.md` and hidden instruction chain — task-specific layer.
- Chapter/style/source protocols — detailed reference layer.

### 3.3. Version instructions like code

Instruction files should have:

- reason for change;
- scope;
- affected workflows;
- validation method;
- rollback plan when risky.

For solo work this can be lightweight, but the mental model matters: instructions are operational artifacts, not decorative prose.

---

## 4. Agent mode selection for experiments

### 4.1. Local terminal agent

**Candidates:** Codex CLI, Claude Code, Aider, Amp.

**Best first use:** isolated edits in disposable worktree; Markdown/source transformations; small code changes; controlled script runs.

**Test package:** take one chapter or Atlas article repair task and compare instruction compliance, file-boundary discipline, source-link preservation, checks and final report quality.

**Precaution:** no production secrets; no broad filesystem access; one worktree per run.

### 4.2. IDE agent

**Candidates:** Cursor, Junie, Claude Code IDE integration, Copilot agent mode.

**Best first use:** multi-file refactor where visual diff and project navigation matter.

**Precaution:** require plan before edits; require final file list; keep changes reviewable.

### 4.3. Spec-driven IDE

**Candidate:** Kiro.

**Best first use:** one feature/bugfix where requirements/design/tasks can be compared with SPDD/package workflow.

**Precaution:** do not let Kiro redefine the project methodology. Treat it as evidence and experiment.

### 4.4. Cloud issue-to-PR agent

**Candidates:** GitHub Copilot coding agent, Codex cloud, Jules.

**Best first use:** docs, CI/build, dependency update, lint/test cleanup, generated report update — not core product logic.

**Precaution:** require branch/PR; no automatic merge; review PR as process object.

### 4.5. Open harness

**Candidates:** OpenHands, SWE-agent, Software-Agent-SDK.

**Best first use:** reproducible experiments, not daily production work.

**Precaution:** sandbox strongly; preserve logs; use toy repos first.

### 4.6. App-builder

**Candidate:** Replit Agent.

**Best first use:** prototype, throwaway app, UI exploration, small demo.

**Not first use:** production-affecting repositories or databases.

**Precaution:** no real data; explicit rollback/export plan; treat output as prototype until reviewed outside the platform.

---

## 5. New process artifacts to consider

### 5.1. `AGENTS.md`

Root cross-agent instruction file.

### 5.2. `work/agent-runs/`

Directory for human-readable run summaries:

- date;
- package/task;
- agent/tool;
- input baseline;
- output archive;
- files changed;
- checks;
- unresolved risks;
- instruction repair suggestions.

### 5.3. `work/instruction-ledger.md`

Lightweight ledger of instruction changes:

- what changed;
- why;
- what failure or need caused it;
- where it applies;
- whether it should be removed later.

### 5.4. `work/agent-mode-tests/`

Small suite of controlled experiments comparing tools/modes.

Possible tests:

1. Markdown chapter natural-language rewrite with source-link preservation.
2. Atlas article source transfer with depth-over-breadth rule.
3. Small TypeScript utility with tests.
4. Repo map update after file changes.
5. Emergency stop packaging.

### 5.5. `work/acceptance-notes/`

Short human acceptance records for major agent outputs:

- accepted / rejected / partially accepted;
- reason;
- applied overlay or not;
- new canonical baseline;
- follow-up debts.

This prevents confusion about which archive became canonical.

---

## 6. Practical rules after the field review

1. Prefer PR-shaped outputs for code. Even in solo work, treat branch/diff/report as the acceptance unit.
2. Keep one agent per isolated worktree/container when possible. Parallel work only helps if merge/review costs are planned.
3. Require explicit verification material: tests run, checks passed/failed, files changed, unresolved risks.
4. Use cloud agents first for low-risk maintenance: docs, CI, build, dependency update, generated reports.
5. Keep core algorithm/design work under tighter human control. For intellectually central logic, require pseudocode/spec before agent implementation.
6. Treat instruction files as living process code. Update them after repeated failures, not after every minor annoyance.
7. Do not overfit to one vendor’s instruction format. Keep cross-agent root instructions and tool-specific adapters.
8. Use traces as reconstruction aids, not correctness proofs.
9. Every connector/tool server needs a rights card: read/write scope, identity, revocation, audit.
10. Avoid product-catalog drift. Tool experiments should answer process questions, not “which agent is trendy?”

---

## 7. Recommended first experiments

### Experiment 1 — Root `AGENTS.md` draft

Create a root `AGENTS.md` for the current repository. Use it with one simple task in two different agents. Measure whether the instruction helps or adds noise.

**Success criteria:** agent respects language rules, source links, overlay packaging and no-degradation rules without restating everything in the prompt.

### Experiment 2 — Same package in local terminal agent vs current ChatGPT execution

Take a small article or chapter repair package and execute it in a local terminal agent. Compare instruction compliance, file handling, report quality, source-link preservation and interruption handling.

### Experiment 3 — Cloud PR agent for docs/CI maintenance

Use a cloud PR agent only for a low-risk maintenance task. Require a PR description with commands run and acceptance notes.

### Experiment 4 — Kiro/SPDD comparison

Use Kiro on a toy feature. Compare its requirements/design/tasks with SPDD package artifacts.

### Experiment 5 — Trace/eval mini-harness

Build a tiny local convention for logging agent runs even without a full LangSmith-style system:

- prompt/package id;
- tool used;
- commands run;
- changed files;
- tests;
- final risk notes.

Later this can be replaced or augmented by LangSmith/OpenAI tracing if useful.

---

## 8. What not to change

Do not abandon the lazy self-revealing package pattern. The field review supports it: hiding the whole task composition from the executing model can reduce over-optimization around final scenario and preserve local task discipline.

Do not replace doc-first process with a framework. LangGraph/ADK/CrewAI can help execute agent systems, but they do not define project memory, source discipline, chapter acceptance, overlay rules or theory-writing standards.

Do not prematurely build a heavy internal platform. First stabilize repository instructions, run logs, acceptance notes and tool experiments. Then decide what belongs in Noveia or a dev-process plugin.
