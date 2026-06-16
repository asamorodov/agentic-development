# P06 — Сквозной пример главы IX: billing/UI fix

Статус: рабочий пример для будущей главы. Это не готовый раздел, а материал, через который можно провести основные различения: execution boundary, tools/observation, secrets/network, approvals, sandbox, durable runtime, evidence и authority.

## 1. Исходная ситуация

В продукте есть billing UI. Пользователь меняет тариф, но экран после оплаты иногда показывает старый план. В issue написано: «После успешного Checkout Session клиент возвращается на `/billing`, но карточка тарифа остаётся в состоянии `Free`, пока страницу не обновить вручную. Нужно исправить поведение и не сломать existing subscription flows».

Задача выглядит как обычный frontend/backend bugfix, но для агентской разработки она сразу касается нескольких сред:

- репозиторий с frontend and backend code;
- локальное приложение с `make dev` or similar command;
- тестовая база or seed data;
- browser/devtools для проверки UI;
- billing provider in test mode, например Stripe-like API;
- secrets or test credentials;
- webhook/local tunnel or replay mechanism;
- issue tracker and docs search, possibly via MCP;
- CI/tests and review path.

Агенту поручают исправить баг. На уровне намерения это звучит просто: «fix stale billing status after checkout». Но глава IX должна показать, что реальное действие начинается только тогда, когда становится ясно, где агент действует и какие границы вокруг него построены.

## 2. Вход в рабочую среду: от поручения к месту действия

Хороший запуск не начинается с того, что агент сразу правит основной checkout. Он получает ограниченную рабочую область:

- отдельный `worktree` or isolated branch;
- sandboxed workspace, where writes outside project directory are blocked or require approval;
- local commands allowed under a permission profile, for example read/write in workspace and selected command execution;
- network disabled by default or limited to explicit domains;
- secrets not injected into environment unless the task crosses a confirmed boundary;
- browser profile either clean or intentionally prepared test profile, not the user’s ordinary logged-in session;
- logs and command outputs captured into a run directory.

На этом шаге видны сразу три различения.

First, `worktree` solves only part of the problem. It isolates the diff and lets several agents work in parallel, but it does not protect the whole machine, secrets, network or external APIs. It also does not know whether the work is correct.

Second, sandbox is an enforcement boundary. If the agent tries to write to `~/.ssh`, read browser cookies, edit files outside repository or run a command with wider system effect, the environment should stop it before human judgment is needed.

Third, approval is not the same thing as sandbox. If the agent needs to install a missing dependency, open network access, write outside workspace or run a migration-like command, the system may ask for confirmation. But that confirmation concerns a concrete action, not the whole task.

Possible failure at this step: the team gives the agent `danger-full-access` equivalent because otherwise it asks too many questions. Then the issue is no longer «can the model fix billing UI», but «what else can this model accidentally touch while fixing billing UI».

## 3. Reading the project: context is useful, but not a boundary

The agent reads:

- `AGENTS.md` or `CLAUDE.md`;
- `docs/billing.md`;
- existing tests in `billing/*.test.*`;
- route/controller code around checkout return;
- frontend state management around `/billing`;
- recent commits touching subscription refresh;
- issue thread and reproduction notes.

This belongs partly to chapter VI: project context becomes an interface for the agent. But IX must add a stricter point: the instruction «never use production secrets» is not enough. It is valuable as context, but it is not enforcement. The runtime must make production secrets unavailable or require a clearly logged boundary crossing.

Possible failure: `AGENTS.md` says «use only test data», but the environment exposes real `.env` values, the browser shares the developer’s signed-in production dashboard, and an MCP server can reach production issue links or API objects. The agent may still be «following instructions» according to its local reasoning while the environment has given it an unsafe surface.

Working lesson: context can tell the agent what not to do; environment determines whether it can do it anyway.

## 4. Running local services: scripts become agent-facing tools

The agent runs something like:

```bash
make dev
```

A good harness gives an agent-facing command, not just a human convenience script. It should behave well if called twice, fail quickly, and explain what happened. If services are already running, it should say so rather than spawning duplicate processes and causing port conflicts. It should write logs to a predictable place:

```bash
make tail-log
```

or

```bash
cat var/log/dev-server.log
```

This is where Ronacher-style local harness matters: logs, scripts, and failure messages are tools. They let the agent observe the running system without flooding context with irrelevant terminal output.

Possible failure: `make dev` hangs forever, starts duplicate services, produces huge unstructured output and gives no way to inspect recent logs. The agent then either wastes context, guesses from incomplete output or repeatedly restarts services. The runtime did not constrain the agent enough and did not expose the right observation surface.

Working lesson: a tool is not just a capability. It is a designed interface between the agent and the environment. For agents, fast errors and readable logs are often more valuable than broad autonomy.

## 5. First code change: filesystem permission and diff boundary

The agent identifies a likely cause: after returning from checkout, the UI uses cached subscription state and does not refetch the account billing summary. It changes something like:

- frontend billing page hook triggers a refetch when `checkout_success=true` is present;
- backend endpoint includes updated subscription state;
- test fixture gets a successful checkout return scenario.

Now the file boundary matters:

- writing to files inside the `worktree` is allowed;
- editing generated files, migration files or package manager lockfiles may be allowed but should be visible;
- writing outside the repository should be blocked or require approval;
- changing scripts that later run with broader permissions is sensitive even if the immediate edit is inside workspace.

This is where permission profiles can be misleading. A write inside workspace may still be dangerous if the agent edits `package.json` scripts, build hooks, CI config or test setup in a way that will execute later. The permission boundary is necessary, but it cannot be the only semantic review.

Possible failure: the agent cannot reproduce the bug quickly and edits a global auth/billing cache layer, causing broad behavioral changes. The sandbox contains the damage to the worktree, but the diff is still risky. Sandbox limits blast radius; it does not make the design correct.

Working lesson: filesystem isolation produces a reviewable diff. It does not decide whether the diff is acceptable.

## 6. Tests and hooks: deterministic feedback before human review

A reasonable environment now runs:

```bash
npm test -- billing
npm run typecheck
npm run lint
```

or equivalent project commands. Some of these may be invoked by the agent; some may be invoked automatically by hooks when the agent stops or changes files. A hook can run a formatter or typecheck and return errors to the agent, forcing another correction before the session is considered ready.

This is useful because it turns part of verification into runtime feedback. But the chapter must keep the boundary clear:

- hook feedback is not human review;
- passing typecheck is not proof that billing behavior is correct;
- a test added by the agent is not automatically trustworthy;
- automatic retry after failing tests can hide repeated guesswork unless the attempt history is logged.

Possible failure: the hook runs tests and passes, so the process reports the task as done. But the tests only cover the component render and never simulate the checkout return path. Runtime feedback produced a green signal, but not sufficient evidence.

Working lesson: deterministic feedback is part of the execution environment. Evidence begins only when the feedback is tied to the promised behavior.

## 7. Browser/devtools check: observation with session boundaries

The agent opens a browser against local app:

- signs in as a test user;
- starts a test checkout or uses seeded successful checkout state;
- returns to `/billing?checkout_success=true`;
- watches whether the plan card updates;
- checks console errors and network requests;
- confirms that the subscription summary endpoint refetches.

Browser and DevTools give the agent a rich observation surface. This is often necessary because billing/UI bugs are not visible from unit tests alone.

But browser use introduces a separate boundary. If the browser shares the developer’s real login state, saved cookies, internal admin sessions or password manager access, then the agent is not just «testing UI». It may act in an authenticated user world. Even local browser automation can cross into real external services if the app points to real endpoints.

Safer version:

- dedicated browser profile for agent runs;
- test-only accounts;
- local/staging URLs clearly separated from production;
- no password manager/session reuse;
- network restrictions or domain allowlists;
- screenshots/logs saved into run artifacts only when useful and safe.

Possible failure: the agent sees that checkout cannot complete because it needs payment provider credentials. It opens the developer’s already logged-in billing dashboard in the same browser profile, reads live account data, and tries to diagnose from there. The action may be technically possible, but the environment has crossed a credentials boundary without explicit decision.

Working lesson: browser is not a passive viewport. It is an operational tool whose authority depends on session state.

## 8. External service boundary: test secrets, staging and approval

To reproduce the bug fully, the agent may need a Stripe-like test checkout flow. This can involve:

- test API key;
- webhook signing secret;
- local webhook forwarding;
- test customer/subscription objects;
- external API calls;
- documentation search;
- network access to provider domain.

Here the difference between permission and approval becomes visible. The environment may allow local file edits and tests by default, but external billing calls should require a more explicit route:

- use preconfigured test credentials, not production credentials;
- make the target environment visible in the prompt and logs;
- ask approval before enabling network or calling external service;
- prevent production API keys from being available;
- record what was called, with which test account and what object IDs were created.

A good approval prompt is narrow: «Allow agent to call Stripe test API using test key `sk_test_...` for this billing reproduction?» It should not mean «the agent now has general permission to use network and secrets as needed».

Possible failure: the agent asks to «enable network for docs and checkout testing»; the user approves; the system treats this as broad network permission; the agent then fetches docs, calls API, sends telemetry, accesses unrelated services and mixes external content into its context. The approval was too wide.

Working lesson: approval is a scoped crossing of a boundary, not a global transfer of trust.

## 9. MCP/tools: capability, context and trust surface at once

The agent may use MCP servers or tools for:

- issue tracker: read issue, update status, post comment;
- docs search: find provider API behavior;
- browser automation;
- test data setup;
- billing provider API;
- log/observability platform.

The easy but dangerous summary is «MCP gives context». The better chapter IX framing: MCP gives the agent an operational surface. Tool definitions enter the agent context; tool calls may read data, mutate systems, invoke APIs or return untrusted content. Tool annotations can help categorize risk, but they are not enforcement by themselves.

A mature environment should know:

- which MCP servers are trusted;
- whether they run locally or over HTTP;
- what credentials they hold;
- whether tool calls are read-only, destructive, idempotent or open-world;
- which calls require human confirmation;
- how tool results are logged;
- whether tool descriptions themselves can steer the agent.

Possible failure: an MCP server exposes both `get_customer` and `cancel_subscription`; the tool descriptions say one is read-only and one is destructive, but the client treats those as informational. The agent accidentally calls the wrong tool or follows a malicious instruction embedded in returned data. The problem is not that MCP exists; the problem is that tool surface was treated as trustworthy context rather than governed capability.

Working lesson: connected tools are part of runtime rights, not documentation attachments.

## 10. Durable runtime: continuing the run is not continuing the work

Suppose this task is not a single chat session. It runs in a structured workflow:

1. prepare worktree/devbox;
2. read issue and project context;
3. run reproduction script;
4. let agent patch code;
5. run tests;
6. open browser scenario;
7. if external service is needed, pause for approval;
8. resume after approval;
9. collect run artifacts;
10. prepare PR summary.

A workflow runtime can persist state, resume after crash, retry failed steps and pause for human input. In a Roast-like workflow, deterministic steps and agent steps can be interleaved. In a Temporal/LangGraph/Restate/DBOS-like durable runtime, checkpoints, event histories, journals or workflow steps can make the execution recoverable.

This is necessary once agent tasks last longer than a single prompt. But it has a sharp boundary: resuming the execution is not the same as knowing the project state. A runtime may know that step 6 failed and step 7 is waiting for approval. It may not know whether the code change still satisfies the issue, whether a new blocker appeared, whether the user accepted the test scope, or whether this PR should be merged.

Possible failure: the workflow resumes after a crash and continues from the last completed step, but the external service test object was already created before the crash. If the side effect was not idempotent or recorded properly, rerun creates duplicate billing objects or produces confusing state. Durable execution is useful only when side effects and idempotency are part of the design.

Working lesson: durable runtime manages execution continuity. Persistent work state and acceptance require another layer.

## 11. Run artifacts: trace before evidence

At the end of a healthy run, the environment can produce artifacts:

- diff in the worktree;
- changed files list;
- command log;
- test results;
- typecheck/lint output;
- browser observation notes;
- screenshot or trace if appropriate;
- network/API call log for test environment;
- approvals requested and granted/denied;
- external objects created in test mode;
- workflow step history;
- agent summary.

These artifacts are valuable, but chapter IX should be strict: they are a trace of execution, not yet sufficient evidence. To become evidence, they must be attached to the claim being checked:

- promised behavior: billing page updates after successful checkout return;
- negative promise: existing subscription flows are not broken;
- test material: unit/integration/browser scenario;
- relevant logs: endpoint refetch and response state;
- limitations: tested only with test provider, not production data;
- remaining risks: cache invalidation elsewhere, webhook delay, stale server data.

Possible failure: the agent returns a long transcript and says «tests passed». The reviewer cannot see which test corresponds to the original bug, which environment was used, what external calls happened or whether the browser check used real credentials. The trace exists, but it is not reviewable evidence.

Working lesson: the execution environment can generate raw material. The evidence layer organizes it around the promise of the change.

## 12. Returning the result: PR is not acceptance

The agent prepares a PR or patch:

- summary of the bug and change;
- files changed;
- tests run;
- browser scenario checked;
- external test objects created;
- approvals requested;
- known limitations;
- rollback or cleanup notes.

This is where authority must remain separate. The agent can create a PR; the workflow can pass tests; the user can approve a network call; CI can go green; the sandbox can isolate the diff. None of these automatically means the result is accepted. Someone or some project rule still has to decide whether the change should enter the codebase.

Possible failure: the process sees a green workflow and auto-merges because the agent ran in a sandbox and all its configured checks passed. But billing code may require domain owner review, security review, product acceptance or a stricter integration test. The runtime has produced a candidate, not a legitimate conclusion.

Working lesson: approval to perform an action and authority to accept a result are different gates.

## 13. Compact version for use inside the chapter

If the final chapter needs a shorter recurrent example, it can compress the scenario like this:

An agent is asked to fix a stale billing card after checkout. It receives a separate `worktree`, runs `make dev`, edits the billing page, runs tests, opens the local app in a browser, watches DevTools, tries to reproduce a Stripe-like test checkout, asks for permission to use test credentials and network, calls a docs/API tool, resumes a workflow after a failed test, and returns a PR with logs and screenshots. Each step looks like «the agent is doing the task», but each step sits on a different boundary: filesystem, command execution, browser session, MCP trust, external service, secret handling, approval, retry, evidence, review. The chapter’s job is to prevent those boundaries from collapsing into one vague statement that «the agent had access and passed tests».

## 14. What the example protects against compositionally

This example is useful because it prevents the chapter from becoming too abstract in four directions.

1. It prevents a pure sandbox chapter: worktree/sandbox is only the first part.
2. It prevents a pure tool chapter: tools matter because they act inside runtime rights.
3. It prevents a pure workflow chapter: durable execution continues the run, not the work’s meaning.
4. It prevents a pure evidence chapter: logs and browser checks are only raw material until linked to the promise.

The example should therefore appear repeatedly, but not as a long story every time. Each major distinction can be introduced by returning to one step of the same billing fix.
