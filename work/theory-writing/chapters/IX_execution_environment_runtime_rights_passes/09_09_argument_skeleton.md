# P09 — Скелет аргумента главы IX

Статус: рабочий скелет будущей главы. Это не основной текст, не оглавление в финальном виде и не механическая сумма источников. Задача скелета — удержать единый аргумент: агентское действие не существует «вообще»; оно существует в среде, где техническая возможность, permission, approval, проверка и authority разведены.

## 1. Рабочее название и назначение главы

Возможное название:

```text
IX. Исполнение: среда агента, права действия и след запуска
```

Назначение главы в общей теории: после глав о контексте, спецификации, профилях и маршрутах действия показать нижний, но не второстепенный слой: где агент реально действует. До этой главы можно было говорить о намерении, задаче, профиле, маршруте, роли, контексте и интерфейсе. Здесь нужно показать, что всё это становится реальной работой только тогда, когда есть место исполнения: файлы, shell, browser/devtools, network, tools, secrets, approvals, sandbox, logs and run state.

Глава должна отвечать не на вопрос «какие инструменты бывают у агентов», а на вопрос:

> Что делает действие агента ограниченным, наблюдаемым, возобновляемым и подотчётным, но при этом не превращает его автоматически в принятое изменение?

## 2. Начальный практический сбой

Глава должна начинаться не с определения sandbox, а с узнаваемого практического провала.

### Сцена

Агенту дают задачу: «почини billing/UI: после checkout пользователь возвращается на `/billing`, но карточка тарифа показывает старый план». Агент читает код, правит frontend, запускает тесты, открывает браузер, видит проблему, хочет проверить внешний billing provider, просит network/secrets, получает подтверждение, создаёт test Checkout Session, возвращает PR with logs and screenshot.

Снаружи это выглядит как обычный успешный агентский запуск: код изменён, тесты зелёные, браузер показал новую карточку, PR готов. Но внутри одного запуска было несколько разных переходов:

- чтение кода;
- запись в worktree;
- запуск локальных команд;
- работа с browser/devtools;
- использование авторизованного браузера или тестового профиля;
- доступ к test secrets;
- network call to billing provider;
- tool/MCP call;
- hook/test feedback;
- workflow pause/resume;
- PR/report;
- human review.

Ошибка процесса возникает, когда эти переходы схлопываются в одну фразу: «агенту разрешили» или «агент справился». Разрешили что именно? Файловую запись? Команду? Сеть? Браузер? Test API? Создание PR? Merge? Принятие результата?

### Формулировка сбоя

Центральный сбой главы:

> Агент технически может выполнить действие, а процесс начинает обращаться с этим как с допустимым, безопасным или уже принятым результатом.

Глава должна сразу поставить различение:

- **technical capability** — процесс может выполнить действие;
- **permission** — среда/политика допускает класс действий;
- **approval** — конкретный опасный переход подтверждён;
- **verification feedback** — среда дала сигнал о результате;
- **evidence** — проверочный материал связан с обещанием изменения;
- **authority** — человек/проектное правило имеет право принять результат.

В этом различении вся глава. Все источники должны работать на него, а не заменять его собой.

## 3. Основной тезис главы

Сформулировать тезис после начальной сцены:

> В агентской разработке среда исполнения становится частью инженерного метода. Она не просто даёт агенту инструменты. Она задаёт, где агент может писать, что может запускать, какие внешние системы может трогать, когда обязан остановиться, какие следы оставляет и где человеческое решение остаётся отдельным. Чем сильнее агент, тем важнее не «дать ему больше доступа», а разложить доступ на поверхности действия, наблюдения, проверки, продолжения и принятия.

В финальном тексте эту формулу надо сделать менее декларативной, но сохранить содержание.

## 4. Логика главы по разделам

### Раздел 1. От поручения к среде действия

Задача раздела: объяснить, почему поручение агенту ещё не действие. Нужно ввести «место действия».

Содержание:

- Агент не действует в абстрактном проекте; он действует в checkout/worktree/devbox/container/local machine/cloud session.
- Первые вопросы: какие файлы видит, куда может писать, какие команды запускает, есть ли network, какие secrets exposed, какие local services reachable, какой browser profile used, where logs go.
- Billing example: worktree, project root, local app, test DB, dedicated browser profile, no production secrets.

Источники:

- A6 four-layer distinction.
- Codex sandbox docs for «sandbox applies to spawned commands» and technical boundary.
- Claude Code security docs for read-only default and write folder boundary.
- Mike/Sandvault as practical lower-level environment.

Граница с соседями:

- Не уходить в главу VI о context interface. `AGENTS.md` mentioned only to show it guides but does not enforce.
- Не уходить в chapter X/route selection; здесь уже выбран route: agent acts.

### Раздел 2. Sandbox, permission profile and approval are different things

Задача раздела: ввести центральное техническое различение.

Содержание:

- Sandbox: enforced technical boundary, often OS/container/devbox backed.
- Permission profile/mode: posture of allowed classes of actions.
- Approval policy: when to stop and ask for boundary crossing.
- Approval scope: one action, session, category, broad mode; scope matters.
- Approval fatigue: too many prompts leads to unsafe habituation; too few constraints leads to YOLO risk.

Sources:

- Codex docs: sandbox vs approval; permission profiles; network off; network allowlist not trust; Auto-review as reviewer swap not permission grant.
- Claude docs: read-only default, acceptEdits, plan mode, auto mode, bypass permissions restrictions.
- Mike McQuaid: confirmation fatigue and Sandvault as middle path.

Example insertion:

Billing agent can write frontend file in worktree, but still needs separate approval to call external billing API with test key. Approving test API call does not approve production dashboard access or merge.

Necessary distinction:

- `danger-full-access` / `bypassPermissions` / YOLO should be presented only as acceptable inside externally hardened environment, not as default autonomy.

### Раздел 3. Command rules: useful mechanics with semantic limits

Задача раздела: показать, что command policy is necessary but not enough.

Содержание:

- Rules/allowlists reduce friction for safe routine: tests, build, lint, local scripts.
- Rules can block dangerous commands: DB wipe/migration/fresh reset, production commands, broad network fetches.
- Codex `prefix_rule` and Claude/Arvid `allow`/`deny` are examples of current practice.
- Problem: command string is not action meaning.
- Shell wrappers and generated scripts can hide forbidden action.
- Writes to build scripts, hooks, package scripts, startup files are sensitive because they execute later.

Sources:

- Codex rules docs.
- Codex permissions docs for sensitive writes.
- Arvid Kahl’s `settings.local.json`, `allow`, `deny`, Laravel DB examples, bash-script bypass.

Example insertion:

Agent cannot run `db:wipe`, but writes `reset-local.sh` that calls it. The process must catch blast radius, not only command text.

Boundary:

- This is still runtime rights; do not move into full security chapter.

### Раздел 4. Tools and MCP are operational surfaces, not context attachments

Задача раздела: repair the weak phrase «MCP даёт контекст».

Saying to avoid: «MCP gives context» as if harmless.

Better statement:

> MCP may provide context, but it can also expose actions, data, credentials, prompts and external systems to the agent. Tool surface is part of runtime rights.

Content:

- Tools expose DBs/APIs/computation/browser/docs/Figma.
- Server instructions enter model guidance.
- Tool annotations/hints help but are not guarantees.
- Trusted server vs untrusted server matters.
- OAuth/authorization/audit are runtime architecture, not product polish.
- Read tool vs write/destructive tool vs open-world tool.
- Hooks can match MCP tool calls, but only if policy is configured.

Sources:

- MCP spec/security/authorization/tool annotations.
- Codex MCP docs: STDIO/HTTP, bearer/OAuth, server instructions.
- Claude MCP/security docs.
- HumanLayer: MCP tool bloat and CLI alternative.
- Ronacher: code/CLI as better compositional tool surface than huge MCP catalog.

Example insertion:

Billing MCP exposes `get_customer`, `create_test_checkout`, `cancel_subscription`, `update_issue`. These are not equivalent. Tool descriptions cannot replace approval policy.

Boundary:

- Do not turn into MCP security treatise. Keep to execution rights.

### Раздел 5. Browser/devtools: observation becomes action when session state is present

Задача раздела: make browser surface visible.

Content:

- Browser is an observation surface: DOM, console, network, screenshot, user path.
- Browser is also action surface: clicks/forms/navigation can mutate state.
- If browser shares login state, it carries user credentials/authority.
- Dedicated test profile vs real logged-in user profile.
- Browser traces are useful, but can contain sensitive data.
- Sandbox bridges like Sandvault’s browser endpoint need their own boundary.

Sources:

- Claude Chrome docs: shares browser login state; can access logged-in sites; debug console, automate forms, extract data.
- Arvid: `--chrome`, route/action/screenshot/DOM/console/recheck cycle.
- Sandvault: host browser/CDP bridge, `SV_BROWSER_ENDPOINT`, iOS bridge.
- Stripe integration benchmark: realistic payment flow needs browser/API artifacts.

Example insertion:

Agent opens `/billing?checkout_success=true` locally and checks network refetch. Safe if test user/profile. Dangerous if it silently uses real developer session to inspect production billing dashboard.

Boundary with XI:

- Browser observation becomes evidence only when tied to original claim and safe scope.

### Раздел 6. Hooks and sensors: feedback before review, not review itself

Задача раздела: show hooks as runtime feedback/control.

Content:

- Hooks can run tests, lint, scan prompt, block destructive command, add context, route approvals, notify, stop/restart loop.
- Hooks have lifecycle events: before/after tool use, stop, session start, file changed, worktree create, config change, compact.
- Deterministic command hook differs from HTTP/MCP/prompt/agent hook.
- Hooks themselves need trust: project hook can be untrusted; changed hook must be reviewed; managed hooks may be policy-trusted.
- Hook success/failure gives feedback, not final acceptance.

Sources:

- Claude hooks reference: events, `PreToolUse`, `Stop`, hook handler types, `rm -rf` block example, silence not approval.
- Codex hooks docs: trust exact hash, `/hooks`, managed hooks.
- Kiro hooks docs: IDE event → agent prompt/shell command; mainstream product shape.
- Fowler harness engineering: guides vs sensors, computational vs inferential feedback.
- Arvid: Ralph Wiggum stop hook loop.
- HumanLayer: hooks/back-pressure/verification/control flow.

Example insertion:

After billing change, `PostToolUse` hook runs targeted tests after edits; `Stop` hook prevents finish until browser scenario checked. If hook passes, PR still needs domain review.

Boundary:

- Avoid saying hooks “prove”. They only produce signals.

### Раздел 7. Designed local harness: logs/scripts are tools

Задача раздела: prevent chapter from becoming only security. Environment also needs affordances.

Content:

- Agent needs scripts that behave well: `make dev`, `make tail-log`, targeted tests, seed data, login test helpers.
- Logs should be predictable and readable; commands should fail quickly and explain.
- A bad harness produces context flood and guesswork.
- Good harness turns local environment into usable observation surface.

Sources:

- Ronacher: scripts/logs/browser/debug email stdout; tools should be fast, clear, protected, observable.
- Fowler: feedback sensors.
- HumanLayer/Ronacher: too many tools and context bloat; prefer narrow CLIs where possible.

Example insertion:

If `make dev` hangs and logs are unreadable, agent starts guessing or restarting. If `make tail-log` and a test login helper exist, browser cycle becomes feasible.

Boundary with VI:

- Context files guide; harness lets agent observe and act.

### Раздел 8. Worktrees and devboxes: isolated writing, not correctness

Задача раздела: place worktree/devbox in the model.

Content:

- Worktree gives separate file tree/diff/branch for parallel work.
- Devbox/cloud session gives prepared environment and maybe scoped credentials.
- Sandvault adds lower-privilege user; worktree adds parallel write separation.
- Setup/bootstrap matters: fresh worktree without deps wastes agent time.
- Worktree can be handed off to local checkout for inspection.
- It does not make code correct or accepted.

Sources:

- Codex app worktrees docs.
- Claude worktree/events through hooks.
- Mike McQuaid/Sandvault/Superset worktree setup.
- Stripe Minions platform direction, cautiously.

Example insertion:

Billing fix happens in a worktree. That protects the main checkout and allows review. It does not mean the test key was safe, browser profile was safe, or PR can merge.

Boundary:

- Preserve difference between worktree and PWG. Worktree is place/diff; PWG is work meaning/gate/evidence/owner.

### Раздел 9. Workflow runtime and durable execution: continuing the run

Задача раздела: show when a single session is not enough.

Content:

- Long agent tasks need workflow runtime: deterministic steps, agent steps, pauses, approvals, retries, resume, timers, side-effect tracking.
- Roast: workflow/cogs; Boba deterministic-agentic sandwich; `cmd`/`ruby`/`chat`/`agent`/`map`/`repeat`/session resumption.
- Quix: deterministic orchestration around Claude Code, not huge prompt/tool catalog.
- LangGraph/Temporal/Restate/DBOS: interrupt, signal, event history, journal, replay, resume.
- Side effects must be idempotent or recorded; otherwise resume creates duplicate external objects.

Sources:

- Shopify Roast article/repo and Boba.
- Quix/Klaus Kode.
- LangGraph, Temporal, Restate, DBOS docs.

Example insertion:

Billing workflow pauses when test API key is needed; resumes after approval; records created test Checkout Session ID; does not repeat side effect after crash.

Boundary:

- Durable execution continues the run; PWG/evidence/authority continue the work.

### Раздел 10. Platform agents: PR factory still returns candidates

Задача раздела: scale up without collapsing authority.

Content:

- Platform-agent environment can start from Slack/issue, prepare devbox, run blueprint, call tools, produce PR.
- Stripe Minions is useful as direction but exact architecture/metrics need cautious sourcing.
- Official Stripe benchmark and Sessions materials more reliable for current, visible claims.
- High PR volume shifts bottleneck to review, evidence and policy.
- Shopify Roast gives workflow-platform form at smaller/productized level.

Sources:

- Stripe Minions Part 1/2 with caveat.
- Stripe integration benchmark: 11 environments, code/DB/scripts/test keys, API/UI/Stripe artifact graders.
- Stripe Sessions docs-cleanup Minion scene.
- Homebrew AI PR policy as human responsibility/social gate.

Example insertion:

A Minion-like agent can submit a docs or billing cleanup PR. It still returns a proposed change. Human review and project authority decide merge.

Boundary with XII:

- This section should explicitly hand off to authority/acceptance: production pipeline is not authority by itself.

### Раздел 11. Trace, evidence and authority: final bridge

Задача раздела: close chapter and point to XI/XII.

Content:

Execution environment can leave:

- worktree diff;
- changed files list;
- command log;
- tests/typecheck/lint output;
- browser screenshot/trace;
- console/network logs;
- external test object IDs;
- approval records;
- MCP/tool call log;
- workflow event history;
- PR summary.

But these are not automatically evidence. Evidence requires link to claim:

- promised behavior: billing card updates after checkout return;
- negative promise: existing subscription flows not broken;
- environment scope: test provider, test account, local app;
- limitations: not production, not all cache paths;
- reviewer-relevant evidence: browser scenario, endpoint refetch, test object.

Authority remains separate:

- approval to call test API is not authority to merge;
- green tests are not authority to accept product behavior;
- hook success is not review;
- workflow completion is not project acceptance.

Sources:

- C4 runtime vs PWG.
- PWG/Beads gates as bridge.
- Homebrew policy / Stripe review caveats / Mike local review.

Final bridge sentence:

> Среда исполнения может показать, что агент сделал, где он это сделал и какие границы переходил. Но только следующий слой связывает этот след с обещанием изменения, а ещё следующий — решает, имеет ли результат право войти в проект.

## 5. Where each source family enters

| Source family | Primary role in argument | Where to cite/use | Keep out |
|---|---|---|---|
| A6 | Four-layer model | opening frame and transitions | as abstract taxonomy without example |
| C4 | runtime state vs work state | final bridge, durable runtime boundary | replacing IX with PWG chapter |
| Codex docs | current sandbox/approval/profile/rules/hooks/worktrees | sections 2–4, 8 | product tour |
| Claude docs | current permissions, browser, hooks, modes | sections 2, 5, 6 | full Claude tutorial |
| MCP spec | tools/annotations/authorization | section 4 | security rabbit hole |
| Kiro hooks/steering | mainstream hook/steering shape | sections 6, light mention | Kiro overview |
| Fowler harness | guides/sensors vocabulary | sections 6–7 | buzzword framing |
| Arvid | browser loop, `allow`/`deny`, stop hook | sections 3, 5, 6 | universalizing Claude-specific mechanics |
| HumanLayer | model+harness, tool bloat, hooks, subagents | sections 4, 6, 7 | subagent chapter |
| Mike/Sandvault | OS/user sandbox + worktrees | sections 2, 5, 8 | macOS-only recommendation as universal |
| Ronacher/Pi | minimal scripts/logs/browser and runtime failure | section 7; optional runtime caveat | Pi product chapter |
| Shopify Roast | executable workflow, Boba, cogs, resume | section 9 | exhaustive DSL documentation |
| Quix | deterministic orchestration around agent | section 9 | too much implementation detail |
| Stripe | platform-agent scale, payment benchmark | section 10 and billing evidence | unverified architecture/metrics overclaim |
| PWG/Beads | gates/evidence/work state bridge | section 11 | turning IX into Beads guide |
| GSD/BMAD/Gas Town | secondary boundary/process donors | light support only | dragging all prior methods into IX |

## 6. The recurring billing example: exact placement

Use the same example repeatedly, but not as one long story. Each section should pick the relevant step.

1. Opening: whole task compressed.
2. Sandbox/approval: file edit allowed vs external test API approval.
3. Rules: allowed tests vs forbidden DB reset/migration.
4. MCP/tools: docs/customer/checkout/cancel/update tools differ.
5. Browser: local test profile vs real logged-in dashboard.
6. Hooks: targeted tests/browser check before stop.
7. Harness: `make dev`, `make tail-log`, readable logs.
8. Worktree: diff isolated from main checkout.
9. Durable runtime: pause for secret/approval, resume without duplicating test objects.
10. Platform: PR returned to reviewer.
11. Bridge: trace becomes evidence only when linked to billing claim.

This recurring example prevents catalog structure. If a section cannot be tied back to the billing example, it probably belongs elsewhere or should be cut.

## 7. Boundaries with neighboring chapters

### With VI — Context / working state / interface

VI says context and working state become interface. IX says interface is not enough: the environment must enforce/write/run/observe. `AGENTS.md`, steering files and skills are useful, but they are not sandbox, not approval and not authority.

### With VII/VIII — profiles/routes

Profiles/routes decide how work is attempted. IX begins after a route requiring execution is chosen: what rights and surfaces does that attempt get?

### With X — maybe orchestration/action route chapter

If neighboring chapter handles routes/action selection, IX should not repeat method taxonomy. It should cover runtime consequences of chosen route.

### With XI — evidence/verification

IX produces trace and feedback. XI must decide how trace becomes evidence. A browser screenshot is not evidence until tied to a claim and scope.

### With XII — acceptance/authority

IX includes approvals but must not mistake them for acceptance. Approval lets a step cross a boundary; authority lets result enter project. This distinction should be explicit at the end.

## 8. Structural risks and repairs

### Risk 1: Tool catalog

Symptom: sections become “Codex does this, Claude does this, MCP does this, Roast does this”.

Repair: every source must support one boundary crossing in billing example.

### Risk 2: Security chapter

Symptom: MCP confused-deputy, tokens, browser credentials and sandbox escapes consume everything.

Repair: use security facts only to show rights boundaries. Defer detailed threat model.

### Risk 3: Workflow runtime overreach

Symptom: LangGraph/Temporal/Restate/DBOS become the chapter’s center.

Repair: use them only to explain run continuation; close with durable execution ≠ durable work state.

### Risk 4: Evidence drift

Symptom: the chapter starts explaining verification/evidence in full.

Repair: only say runtime creates trace/check material. Full evidence belongs to XI.

### Risk 5: Authority drift

Symptom: chapter ends with “PR ready” and sounds accepted.

Repair: final paragraphs explicitly separate approval, verification feedback and project acceptance.

### Risk 6: English-glue style

Symptom: text fills with “execution boundary”, “tool surface”, “runtime” without Russian explanation.

Repair: keep source-native terms where needed, but introduce Russian equivalents: «граница исполнения», «поверхность действия», «след запуска», «проверочный материал», «право принять».

## 9. Drafting order recommendation

When writing the actual chapter, start from the billing example and write through the argument in order. Do not start by writing sections from source families. Use source families as support after the section’s own problem is clear.

Suggested drafting sequence:

1. Opening scene and failure.
2. Four-part distinction: capability / permission / approval / authority.
3. Environment as four layers from A6.
4. Sandbox/permissions/approval section.
5. Command rules and bypass section.
6. Tools/MCP and browser sections.
7. Hooks/harness section.
8. Worktree/devbox section.
9. Durable workflow runtime section.
10. Platform-agent scale section.
11. Trace → evidence → authority close.

After first draft, do one natural Russian pass immediately before source expansion, because mechanical terms from this skeleton can easily contaminate prose.

## 10. Minimal internal thesis for future prompt

If the future writing prompt needs one compact thesis, use this:

> Глава IX должна показать, что агентская работа зависит не только от модели и не только от инструкции. Она зависит от среды, в которой действие агента получает место, права, инструменты, наблюдение, продолжение и след. Но эта же глава должна удержать границу: разрешение на действие, успешный запуск, зелёный тест, браузерный след и готовый PR ещё не означают, что изменение доказано и принято.
