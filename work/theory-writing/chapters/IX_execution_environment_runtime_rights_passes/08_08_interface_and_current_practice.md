# P08 — Техническая фактура и текущая практика для главы IX

Статус: рабочее раскрытие механизмов. Это не обзор рынка и не основной текст главы. Цель прохода — разложить главные механизмы IX по внешней форме: участники, входы, выходы, состояния, операции, границы действия, чтение vs действие. Текущая практика проверялась по официальным документам Codex/OpenAI, Claude Code/Anthropic, MCP and Kiro; для durable execution используются официальные docs LangGraph/Temporal/Restate/DBOS from previous discovery.

Важное обновление source register: несколько OpenAI Codex URLs из раннего прохода имеют старую форму `developers.openai.com/codex/cli/...`. Текущие найденные официальные страницы используют в основном `developers.openai.com/codex/...`, например:

- `https://developers.openai.com/codex/agent-approvals-security`
- `https://developers.openai.com/codex/concepts/sandboxing`
- `https://developers.openai.com/codex/permissions`
- `https://developers.openai.com/codex/rules`
- `https://developers.openai.com/codex/hooks`
- `https://developers.openai.com/codex/mcp`
- `https://developers.openai.com/codex/app/worktrees`
- `https://developers.openai.com/codex/concepts/sandboxing/auto-review`

Это нужно учесть в финальном citation/source pass.

## 1. Основная механическая карта главы

В главе есть не один механизм, а несколько вложенных механизмов. Их нельзя объяснять одним словом «доступ».

| Механизм | Участники | Входы | Выходы | Состояния | Граница |
|---|---|---|---|---|---|
| Sandbox / execution boundary | agent process, spawned commands, OS/container/devbox, filesystem/network policy | command, file operation, tool execution needing local process | allowed run, blocked action, approval request, sandbox error | read-only, workspace-write, danger/full access, custom roots, network off/on | техническая возможность действия |
| Permission / approval | user/admin policy, agent, approval prompt, sometimes reviewer agent | proposed action, command, tool call, escalation request | approve once, approve session, deny, ask/auto-review decision | default, acceptEdits, plan, auto, bypass, on-request/never | допустимость конкретного перехода |
| Command rules | rule file, argv matcher, shell parser, admin requirements | argv prefix or parsed shell command | allow/prompt/forbidden, justification | user rules, project rules, managed rules, trusted/untrusted project | локальная политика для команд |
| Hooks | event source, matcher, handler command/HTTP/MCP/prompt/agent | lifecycle event + JSON context | block/allow/add context/log/run check/retry/notification | SessionStart, PreToolUse, PostToolUse, Stop, FileChanged, WorktreeCreate, etc. | runtime feedback/control; hook itself is trust surface |
| Browser/devtools | agent, browser extension/CDP bridge, visible browser, session cookies, web app | URL, DOM, console, network, form actions, credentials/session state | observation, screenshot, data entry, state-changing click, saved trace | local app, authenticated site, test profile, shared user profile | UI observation + credentialed web action |
| MCP/tools | host/client, MCP server, model, external API/DB/service, auth layer | tool description, tool call, resources/prompts, credentials | data read, mutation, external side effect, tool result, elicitation | trusted/untrusted server, read-only/destructive/idempotent/open-world hints | operational surface; not just context |
| Worktree/devbox | git repository, worktree manager, agent session, setup script, reviewer | branch/base, task prompt, environment setup | diff, commit/PR, run artifacts, handoff | local checkout, worktree, detached HEAD, background task, cloud VM/devbox | isolated place of work, not acceptance |
| Durable workflow runtime | workflow engine, agent step, deterministic step, human signal, journal/checkpoint | workflow definition, run id, event, interrupt, side effect | resumed step, event history, journal, retry, cancellation, timeout | running, waiting, interrupted, failed, resumed, completed | continuity of execution, not work meaning |
| Platform-agent workflow | Slack/IDE/issue trigger, platform runner, blueprint, devbox, tools, PR, reviewer | human request, issue, codebase, org policy | PR/proposed change, review packet, metrics, audit | queued, running, waiting review, merged/rejected | org-level action pipeline; authority remains separate |

This table can become a hidden drafting guide, not necessarily a public table. Public text should probably move through the billing example rather than list mechanisms mechanically.

## 2. Sandbox / permissions / approvals: external form

### Participants

- User/developer who starts the run.
- Agent/model process that proposes actions.
- Local CLI/IDE/app host that mediates commands and tool calls.
- OS or container/devbox enforcement layer.
- Admin/managed policy when present.
- Optional reviewer agent or auto-review mechanism.

### Inputs

- User prompt / task.
- Project root/current workspace.
- Sandbox mode / permission profile.
- Approval policy.
- Network access policy.
- Writable roots/protected paths.
- Managed requirements.
- Proposed command/tool call/escalation.

### Outputs

- Command runs inside boundary.
- Command blocked by sandbox.
- Approval request appears.
- Approval is granted for narrow scope or session scope.
- Denial with reason.
- Agent changes path, asks user, or stops.
- Logs/audit events.

### Current practice: Codex

OpenAI’s current Codex docs are unusually useful because they explicitly separate sandbox and approvals. Current docs say the sandbox is the constrained environment in which Codex local commands run, while the approval policy decides when Codex must stop and ask before crossing boundaries. They also state that the sandbox applies to spawned commands such as `git`, package managers and test runners, not only built-in file operations.

Current Codex permission profile facts to use:

- Built-in profiles include `:read-only`, `:workspace`, `:danger-full-access`.
- Permission profiles define local sandboxed command execution boundaries.
- App connectors, MCP servers, browser/computer-use surfaces, Codex cloud environment settings and approved escalations have their own controls.
- Writes to scripts, build steps, package manager hooks, shell startup files and shared directories are sensitive because later tools/users can execute them outside the original sandbox context.
- Network domain rules control destinations but do not establish trust; wildcard rules remain broad.
- Local/private network targets are blocked by default unless explicitly opened.

Current Codex docs also add an important new mechanism: **Auto-review**. It replaces manual approval at the sandbox boundary with a separate reviewer agent, but does not expand writable roots, enable network or weaken protected paths. It reviews eligible escalation requests: sandbox permission escalation, blocked network requests, writes outside allowed roots, MCP/app tool approvals and browser access to new domains. Denial instructs the main agent not to pursue workaround/policy circumvention and to find a materially safer path or stop.

This is strong material for IX because it shows that even auto-approval/reviewer automation is still about a particular boundary crossing. It is not authority to accept the result.

### Current practice: Claude Code

Anthropic’s current Claude Code docs support the same decomposition but with different vocabulary:

- Claude Code uses strict read-only permissions by default.
- Editing files, running tests and executing commands require explicit permission; read-only commands such as `ls`, `cat`, `git status` may run without prompt.
- Sandboxed Bash gives filesystem and network isolation and can reduce prompts while keeping boundaries.
- Write access is restricted to the start folder/subfolders unless explicitly permitted.
- Allowlisting and Accept Edits mode reduce prompt fatigue.
- Accept Edits auto-approves file edits and common filesystem commands such as `mkdir`, `touch`, `rm`, `mv`, `cp`, `sed` when paths stay in scope; out-of-scope/protected paths and other Bash commands still prompt.
- Plan mode lets Claude research and propose changes without editing source; approving a plan exits plan mode and switches into an edit/execution mode.
- Auto mode uses a separate classifier model to reduce routine prompts; docs explicitly call it a research preview and not a replacement for review on sensitive operations.
- Bypass permissions is not available in some surfaces such as cloud/Remote Control contexts and requires explicit enabling in local UI contexts.

This gives an excellent public distinction:

- **Plan mode** changes whether the agent writes.
- **Accept Edits** changes whether file edits prompt.
- **Auto mode** changes who/what checks routine actions before they run.
- **Sandbox** changes what commands can technically reach.
- **Review** remains outside all of these.

### Reading vs action

Reading source files is not the same as writing. Reading docs is not the same as calling an API. Reading browser DOM is not the same as clicking a destructive button. Running `npm test` is not the same as running `php artisan db:wipe`. These distinctions are visible in current product docs, but final chapter should use billing example to make them concrete.

For billing/UI:

- reading billing code: usually low-risk;
- editing frontend hook: workspace write;
- running targeted tests: command execution;
- starting dev server: long-running local command;
- opening local browser: observation/action boundary;
- using existing logged-in Stripe dashboard: credentialed external action;
- calling Stripe test API: network+secret boundary;
- posting issue comment or creating PR: external mutation and authority-adjacent action.

## 3. Command rules: string policy, not meaning policy

### External form

Participants:

- rule author: user/admin/project;
- active config layer;
- agent proposing command;
- matcher that sees argv/prefix or parsed shell command;
- execution host.

Inputs:

- `.rules` file or managed `requirements.toml` entry;
- command argument list;
- optional `match` / `not_match` examples;
- justification.

Outputs:

- `allow`: run outside sandbox without prompting;
- `prompt`: ask each time;
- `forbidden`: block;
- surfaced justification or recommended alternative;
- possible validation failure if rule examples do not match expected behavior.

States:

- user-layer rule;
- project-local rule loaded only when project config is trusted;
- admin/managed rule;
- smart approval suggestion that user must inspect.

### Current practice: Codex rules

Current Codex rules docs say rules control which commands Codex can run outside the sandbox. `prefix_rule()` matches command argument prefixes and has decisions `allow`, `prompt`, `forbidden`; most restrictive match wins. Rules include inline unit-test-like examples via `match` and `not_match`. Codex treats a command as an argument list, like `execvp(3)`, not as raw prose.

Important technical nuance: when a shell script is a simple linear chain of plain words joined by safe operators like `&&`, `||`, `;`, `|`, Codex can parse/split it before applying rules. But this does not remove the deeper problem: command policy is still a syntactic control. Arvid’s example where an agent writes a bash wrapper around a forbidden migration-style command belongs here.

Public chapter should say: command rules are useful precisely because they are mechanical; they are insufficient precisely because they are mechanical. They reduce risk and approval fatigue, but they cannot fully understand intent or blast radius.

## 4. Hooks: lifecycle control and its own trust boundary

### External form

Participants:

- agent host;
- lifecycle event source;
- matcher group;
- hook handler: shell command, HTTP endpoint, MCP tool, prompt hook or agent hook;
- optional admin/managed policy;
- user who reviews/trusts hooks.

Inputs:

- event name;
- JSON context about session/tool/permission/file/worktree/etc.;
- matcher and optional `if` filter;
- hook handler definition;
- environment variables and project paths.

Outputs:

- log;
- added context;
- permission decision;
- denial reason;
- notification;
- async command output;
- re-engagement or stop block;
- external side effect if HTTP/MCP hook calls out.

States:

- untrusted project hook;
- trusted exact hook hash;
- managed hook;
- disabled hook;
- hook changed and needs re-review;
- async/background hook;
- prompt-based/agent-based hook.

### Current practice: Claude hooks

Claude Code’s current hooks reference makes this especially concrete. Hooks are shell commands, HTTP endpoints or LLM prompts that fire at session lifecycle points. Events include `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PermissionDenied`, `SubagentStart`, `TaskCreated`, `Stop`, `ConfigChange`, `FileChanged`, `WorktreeCreate`, `PreCompact`, `PostCompact`, `SessionEnd`, and MCP elicitation events.

The reference’s destructive-command example is useful: a `PreToolUse` hook matches `Bash`, narrows further to `Bash(rm *)`, runs a script that reads JSON from stdin, and returns a `permissionDecision: "deny"` with a reason if it sees `rm -rf`. Exit code 0 with no output means no hook decision, so normal permission flow continues; silence is not approval.

This is a perfect technical distinction for IX:

- hook can block a call;
- hook can add feedback;
- hook can route/observe;
- hook can stay silent;
- hook success/failure still does not equal final acceptance.

### Current practice: Codex hooks

Current Codex hooks docs add a trust-review shape:

- Codex lists configured hooks before deciding which can run.
- Non-managed command hooks must be reviewed and trusted by exact definition/hash.
- Changed hooks become untrusted until reviewed again.
- `/hooks` lets user inspect sources, review/trust/disable hooks.
- Managed hooks from system/MDM/cloud/requirements are policy-trusted and cannot be disabled from user hook browser.
- Config has event → matcher group → hook handlers.

This is important because hooks themselves can become a supply-chain/security boundary. A project-local hook is code that runs during agent work. If the agent edits a hook file or a repo contains malicious hooks, the runtime must not blindly execute them.

### Current practice: Kiro hooks

Kiro’s current docs show the mainstream IDE form of the same mechanism:

- agent hooks execute predefined agent prompts or shell commands on events;
- events include saving/creating/deleting files, user prompt submission, agent turn completion, before/after tool invocations, before/after spec tasks, manual triggers;
- hook system is event detection → automated action;
- actions can be agent prompt (“Ask Kiro”) or shell command;
- examples include tests, docs refresh, security scanning, code quality consistency.

Kiro is useful in final chapter as a short proof that hooks are not exotic custom tooling; they are becoming a standard UI/runtime feature. But do not turn IX into a Kiro section.

### Deterministic vs inferential hooks

The public chapter needs a clean distinction:

- deterministic command hook: runs formatter, typecheck, grep, static check, test script;
- HTTP hook: crosses network boundary and may expose data to service;
- MCP hook: invokes tool/server with its own credentials and trust model;
- prompt/agent hook: adds another model judgment.

Only the first category gives conventional mechanical feedback. The others may be valuable, but they add another authority/trust surface.

## 5. Browser/devtools: observation surface plus credentialed action

### External form

Participants:

- agent;
- browser/extension/CDP bridge;
- user browser profile or dedicated test profile;
- local/staging/production web app;
- login state/cookies/password manager/session;
- network endpoints;
- screenshot/trace/log collector.

Inputs:

- URL/route;
- action script or natural-language browser task;
- DOM/console/network state;
- session cookies/logged-in sites;
- test account or real account;
- local server status.

Outputs:

- observation report;
- screenshot/GIF/trace;
- console logs;
- network requests/responses;
- form submissions;
- changed app state;
- external mutations if browser is authenticated.

States:

- local unauthenticated page;
- test user session;
- developer’s real logged-in session;
- production admin/dashboard session;
- visible browser window vs headless bridge;
- same-profile vs dedicated-agent-profile.

### Current practice: Claude Chrome

Claude Code’s current Chrome docs are a strong source because they explicitly state the double nature of browser integration: it lets Claude test web apps, debug console logs, automate form filling and extract data; it opens new tabs and shares the browser’s login state, so it can access sites the user is already signed into. It can interact with Google Docs, Gmail, Notion and other logged-in apps without API connectors.

That is the chapter’s best current-practice support for this rule:

> Browser is not a viewport; it is a credentialed action surface when it shares user session state.

Billing example should show two safe/unsafe variants:

- safe: dedicated browser profile, local app, test user, test provider, no password manager, screenshots/logs attached only to run artifacts;
- unsafe: real browser profile, live billing dashboard, production-like account, broad form automation, external state changes hidden inside “debugging”.

### Sandvault browser/iOS bridge as boundary bridge

Sandvault adds a useful technical variant. GUI apps do not run directly inside the sandbox user, so browser automation is exposed through a host-side headless browser and endpoint like `SV_BROWSER_ENDPOINT`. iOS Simulator similarly crosses via `SV_IOS_SIMULATOR_ENDPOINT`. This shows that observation often uses **bridges** through the sandbox. A bridge must have its own command set, path restrictions, logging and credential policy. It is not automatically covered by the filesystem sandbox.

## 6. MCP/tools: tool surface as read/write/action boundary

### External form

Participants:

- host application/client;
- MCP server;
- model/agent;
- external service/data/API/DB/browser/Figma/docs;
- auth provider/OAuth/token store;
- user/admin approval policy.

Inputs:

- server initialization;
- server `instructions`;
- tool list/descriptions/schemas;
- resources/prompts if exposed;
- tool call arguments;
- credentials/tokens;
- user approvals/elicitation.

Outputs:

- tool result;
- external read;
- mutation/side effect;
- error;
- audit log;
- user elicitation request;
- context/instruction injection into agent.

States:

- trusted/untrusted server;
- local STDIO server;
- remote HTTP server;
- authenticated via bearer/OAuth;
- read-only/destructive/idempotent/open-world hints;
- direct tool call vs code/programmatic mode;
- disabled/allowed server/tool.

### Current practice: MCP spec

MCP tools spec says tools expose external systems such as databases, APIs and computation and are model-controlled. Applications should show available tools, indicators and let users confirm or deny tool calls. Tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) describe behavior but are hints; clients must treat them as untrusted unless the server is trusted and enforcement exists.

MCP security guidance adds confused-deputy, token-passthrough and audit/trust-boundary risks. Authorization guidance recommends OAuth 2.1 when a server accesses user data, performs actions requiring consent, audits actions, enterprise controls or rate limits.

### Current practice: Codex / Claude Code MCP

Codex current MCP docs say MCP gives Codex access to third-party tools and context, including documentation, browser or Figma; STDIO and streamable HTTP servers are supported; HTTP servers may use bearer token or OAuth; server `instructions` are read during initialization and used as server-wide guidance alongside tools.

Claude Code security docs emphasize using MCP servers from providers you trust and that Anthropic does not security-audit/manage every MCP server. Claude hook docs show MCP tools appear in hook events as regular tools with names like `mcp__server__tool`, so hooks can log/block/validate them. This is useful: tool calls can be governed in the same lifecycle as Bash/Edit/Write, but only if policy actually matches them.

### Reading vs action

The final chapter should force this distinction:

- `get_customer` is read but still may expose sensitive data;
- `create_test_checkout_session` is a write/action in test environment;
- `cancel_subscription` is destructive action;
- `search_docs` returns untrusted external text;
- `update_issue` mutates work state/communication;
- `browser_click` can mutate state even if the API/tool name looks generic.

Tool names and annotations help routing; they are not the authority boundary.

## 7. Worktree/devbox/platform: place of write and place of review

### External form

Participants:

- repository/local checkout;
- worktree manager;
- agent thread/session;
- setup/bootstrap script;
- sandbox/devbox/cloud VM;
- human reviewer/maintainer;
- CI/PR system.

Inputs:

- base branch/current branch;
- prompt/task;
- environment setup script;
- project dependencies;
- secrets/test credentials if approved;
- worktree location;
- handoff command.

Outputs:

- separate file tree;
- branch/diff/commit;
- run log;
- PR;
- local inspection path;
- cleanup/removal.

States:

- Local checkout;
- worktree;
- detached HEAD;
- background task;
- ready for handoff;
- PR created;
- merged/rejected;
- stale worktree needing cleanup.

### Current practice: Codex app worktrees

Current Codex app worktrees docs say worktrees let Codex run multiple independent tasks in the same project without interfering with current local setup. Background automations run on dedicated background worktrees in Git repositories; Handoff can move a thread between Local and Worktree. A worktree is a second checkout with its own file copies while sharing Git metadata; Codex creates one based on selected branch and by default works in detached HEAD.

Chapter IX use: worktree is a place of write and parallelism. It does not protect secrets, network, local services or production APIs by itself. It does not validate the result.

### Current practice: Claude Code worktree/planning surfaces

Claude Code current docs add adjacent forms:

- plan mode can read/explore/write a plan without editing source;
- plan approval can switch into auto/accept-edits/manual-edit mode;
- VS Code extension supports multiple conversations/tabs and plan review;
- worktree isolation appears as a supported mode in docs and hook lifecycle includes `WorktreeCreate` / `WorktreeRemove` events.

This can help the final chapter distinguish planning state from execution state. A plan approved by user is not the same as permission to do all future dangerous actions; it shifts session mode but subsequent boundaries still matter.

### Platform-agent layer

For Stripe/Shopify/Roast-like environments, the place of action may not be the developer’s local machine:

- task starts in Slack/IDE/issue/workflow;
- platform prepares devbox/worktree/sandbox;
- blueprint/workflow narrows task;
- agent edits/runs/tests/browses;
- platform returns PR/report/artifacts;
- human or org policy decides merge/acceptance.

This layer should be shown as composition of lower mechanisms, not as a separate magical type of agent.

## 8. Durable workflow runtime: states and boundaries

### External form

Participants:

- workflow engine;
- workflow definition/code;
- deterministic step;
- agent step;
- external service/API;
- human approver/signal sender;
- checkpoint/journal/event history;
- worker/executor.

Inputs:

- workflow run id;
- initial task parameters;
- step outputs;
- side effects;
- interrupt/approval request;
- signal/event;
- retry policy/timer;
- durable storage.

Outputs:

- step completion;
- checkpoint/event history/journal;
- retry/resume;
- human approval/rejection path;
- cancellation/timeout;
- final workflow result;
- audit trail of execution.

States:

- running;
- waiting on human;
- waiting on timer/external event;
- failed/retrying;
- resumed;
- cancelled/timed out;
- completed.

### Mechanism distinctions

LangGraph-like runtimes: graph state, checkpointer/thread id, interrupts, human decisions around tool calls.

Temporal-like runtimes: durable workflow, event history, replay, signals, timers, long waits without compute.

Restate-like runtimes: journaled steps/side effects, invocation tracking, replay skipping completed steps.

DBOS-like runtimes: workflows/steps, resume from last completed step, workflow IDs for idempotency/background workflows.

Roast-like workflow: versioned workflow file, deterministic cogs (`cmd`, `ruby`) and model/agent cogs (`chat`, `agent`), loops/maps/calls, session resumption/forking.

### Boundary

The final chapter should not let durable execution absorb PWG/evidence/acceptance. A runtime can know: step 7 is waiting for approval, signal received, API call completed, browser check failed, retry scheduled. It cannot by itself know: the billing change has enough evidence, the domain owner accepted the risk, the PR should merge, the next work item is unblocked, the feature promise is satisfied.

## 9. Billing/UI mechanism map

To keep final prose grounded, use the same billing task as a walkthrough of mechanisms.

### Phase 1 — task enters environment

Participants: user, agent, project, worktree/devbox.
Inputs: issue text, repo, `AGENTS.md`, base branch, permission profile.
Operations: create worktree, load instructions, run setup.
Outputs: isolated branch/worktree, initial log.
Boundary: agent can read/explore, but not yet call external billing APIs.

### Phase 2 — reading and local diagnosis

Participants: agent, filesystem, search, tests, logs.
Inputs: billing docs, route/controller, frontend state, tests.
Operations: read/search/run safe commands.
Outputs: hypothesis, changed files candidates.
Boundary: context/instructions are not enforcement; production secrets must not be present just because docs say not to use them.

### Phase 3 — local write

Participants: agent, editor/tool, sandbox.
Inputs: planned patch.
Operations: edit files inside worktree.
Outputs: diff.
Boundary: write allowed in workspace; editing scripts/build hooks/CI remains sensitive because later execution may escape the original context.

### Phase 4 — deterministic feedback

Participants: tests, hooks, typechecker, linter, workflow.
Inputs: changed files, test command.
Operations: run targeted tests/typecheck/lint; hooks may block stop or re-engage.
Outputs: pass/fail, logs, retry.
Boundary: pass is feedback, not final evidence.

### Phase 5 — browser observation

Participants: agent, browser, local app, test user.
Inputs: URL `/billing?checkout_success=true`, test login, local server.
Operations: click, watch network/console, inspect DOM/state.
Outputs: screenshot, console log, network request evidence.
Boundary: browser session must be test/dedicated, not developer’s production credentials.

### Phase 6 — external billing service

Participants: agent, MCP/API/browser, test secret, approval flow.
Inputs: test key, webhook secret, docs/API tool, network allowance.
Operations: create/check test-mode checkout, replay webhook, inspect test artifact.
Outputs: external object IDs, call log, approval record.
Boundary: scoped approval for test API does not imply broad network/secrets trust.

### Phase 7 — durable continuation

Participants: workflow runtime, agent, human approver.
Inputs: pending approval, failed check, checkpoint.
Operations: pause/resume/retry/timer.
Outputs: run history.
Boundary: resumed run still needs work-state claim/evidence/gate.

### Phase 8 — return candidate

Participants: agent, PR system, reviewer.
Inputs: diff, logs, tests, browser trace, external objects.
Operations: prepare PR/report.
Outputs: PR, run artifacts, limitations.
Boundary: PR is candidate; merge/acceptance belongs to authority layer.

## 10. Interface wording for public draft

Potential natural-language interface vocabulary:

- «место действия» — worktree/devbox/sandbox/project root;
- «граница исполнения» — sandbox/filesystem/network/secrets;
- «поверхность наблюдения» — logs, tests, browser, devtools;
- «поверхность действия» — shell, MCP tools, browser clicks, API calls;
- «подтверждение перехода» — approval for a specific boundary crossing;
- «режим допуска» — permission profile/mode;
- «след запуска» — command log, trace, workflow history;
- «проверочный материал» — subset of trace tied to claim;
- «право принять» — maintainer/domain owner/project policy, not runtime.

Avoid in final prose:

- «дал доступ» as a single phrase;
- «агент прошёл проверку» unless naming which check;
- «tool is read-only» unless stating whether read-only is enforced or just hinted;
- «браузер посмотрел» when the browser may be logged in and able to mutate state;
- «workflow решил» when the workflow only resumed or routed.

## 11. Current-practice claims that need citations in final draft

Place source links exactly where introduced:

- Codex sandbox/approval/network distinction — `https://developers.openai.com/codex/agent-approvals-security` and `https://developers.openai.com/codex/concepts/sandboxing`.
- Codex permission profile scope and separate controls for MCP/browser/connectors/cloud — `https://developers.openai.com/codex/permissions`.
- Codex rules/prefix_rule semantics and shell splitting — `https://developers.openai.com/codex/rules`.
- Codex hook trust model — `https://developers.openai.com/codex/hooks`.
- Codex Auto-review as reviewer swap, not permission grant — `https://developers.openai.com/codex/concepts/sandboxing/auto-review`.
- Claude read-only/default permissions/sandbox/write restrictions — `https://code.claude.com/docs/en/security`.
- Claude permission modes (`acceptEdits`, `plan`, `auto`, `bypassPermissions`) — `https://code.claude.com/docs/en/permission-modes`.
- Claude Chrome login-state/browser automation — `https://code.claude.com/docs/en/chrome`.
- Claude hooks lifecycle/events and `PreToolUse` example — `https://code.claude.com/docs/en/hooks`.
- Kiro agent hooks events/actions — `https://kiro.dev/docs/hooks/`, `https://kiro.dev/docs/hooks/actions/`.
- Kiro steering/AGENTS.md — `https://kiro.dev/docs/steering/`.
- MCP tools/annotations/security/authorization — `https://modelcontextprotocol.io/specification/draft/server/tools`, `https://modelcontextprotocol.io/specification/draft/basic/security_best_practices`, `https://modelcontextprotocol.io/specification/draft/basic/authorization`.
- Fowler harness engineering — `https://martinfowler.com/articles/harness-engineering.html` and sensors article if maintainability sensors enter final text.

## 12. Public chapter implication

The final chapter should not explain these mechanisms as a list. It should move through one real task and reveal mechanisms only when the task crosses a boundary:

1. agent reads repo;
2. agent writes in worktree;
3. agent runs tests;
4. hook blocks stop or runs check;
5. browser sees UI and may carry credentials;
6. MCP/API exposes real actions;
7. external service needs scoped approval;
8. durable runtime pauses/resumes;
9. PR returns;
10. human authority accepts or rejects.

The mechanism map is a safeguard against collapse: permission ≠ approval ≠ sandbox ≠ authority; trace ≠ evidence; workflow completion ≠ accepted work.
