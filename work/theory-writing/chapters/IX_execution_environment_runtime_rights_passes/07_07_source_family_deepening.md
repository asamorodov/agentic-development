# P07 — Добор по главным source families главы IX

Статус: рабочий добор фактуры. Это не основной текст главы и не финальный реестр источников. Цель прохода — расширить материал, из которого будет собираться глава об execution environment, runtime rights, tool surface, workflow runtime and authority boundary. При переносе в публичный текст эти заметки нужно переписать нормальным русским языком и ставить ссылки рядом с конкретными утверждениями.

Главная рамка после добора не меняется: агентское действие становится инженерным действием только внутри среды, где определены место записи, допустимые команды, доступ к сети и секретам, поверхность инструментов, способ наблюдения, механизм продолжения и способ возврата результата человеку. В этой главе особенно важно не смешать четыре вещи: техническую возможность, разрешение на действие, подтверждение опасного перехода и право принять результат.

## 1. A6 / C4: внутренняя рамка, от которой нельзя отклоняться

### Что уже дано корпусом

A6 задаёт четыре слоя, которые нужно сохранить как композиционную основу главы:

1. **Execution boundary** — где агент технически работает: sandbox, отдельный пользователь, container, worktree, devbox, разрешения файловой системы, сеть, секреты, системные права.
2. **Instrumental / observational surface** — чем агент видит и трогает систему: shell, browser/devtools, logs, tests, CLI, MCP/tools, issue tracker, docs search, observability.
3. **Workflow runtime / durable execution** — как запуск продолжается, ставится на паузу, повторяется, восстанавливается, ведёт историю шагов и side effects.
4. **Platform-agent layer** — как всё это упаковано в рабочую платформу: devbox, blueprint, PR, review queue, policy, org controls, telemetry, human handoff.

C4 добавляет границу: runtime-state не равен work-state. Запуск может иметь thread, checkpoint, session file, run log, worktree, devbox, browser trace and workflow step history. Но рабочая единица требует другого: claim, owner, blocker, evidence, gate, accepted/rejected status, cleanup, next safe action and handoff. В IX это должно звучать как мост к XI/XII: среда производит след; доказательный материал возникает только когда след связан с обещанием изменения; право принять результат находится вне runtime.

### Фактура, которую стоит перенести

- Worktree, sandbox, devbox and session are **addresses and containers of action**, not semantic work items.
- Log, screenshot, browser trace and command output are **raw trace**, not evidence by themselves.
- Durable runtime can resume execution after failure, but it does not know whether billing behavior was actually fixed or whether the reviewer accepted test coverage.
- Gate/PWG/bead layer is needed where work waits for human, timer, CI, PR or another work item; execution runtime can pause, but project work needs a named reason to continue later.

### Как использовать в главе

В начале главы можно дать короткую формулу: «среда исполнения отвечает на вопрос, что агент мог сделать, где, с какими правами и каким следом; граф работы отвечает на вопрос, зачем это действие продолжать, кто должен принять следующий шаг и какие свидетельства считаются достаточными». Эта формула защитит главу от превращения в каталог инструментов.

## 2. Arvid Kahl: браузерный цикл, stop hook and command permissions

Источник корпуса: `content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md`.

### Браузер как недостающий канал обратной связи

У Arvid ценный материал для UI/billing example. Он не просто «даёт агенту Chrome». Он строит повторяемый цикл:

```text
код → браузер → маршрут/действие/screenshot/DOM/console → маленькая правка → повторная проверка
```

Фактура для главы:

- Claude Code подключается к Chrome через `--chrome`.
- Для UI задач чтения файлов недостаточно: проблема может проявиться только в реальной странице, при данных, прокрутке, клике, пустом состоянии или сетевом ответе.
- Хороший запрос заставляет агента сначала открыть локальное приложение, пройти страницы, сравнить первый экран, собрать screenshots and DOM clues, а только затем предложить маленький план правок.
- Проверочный пакет для UI задачи должен содержать маршрут, действие пользователя, screenshot, DOM node/component hint, console errors if any, and a second check after the fix.
- В более сильной форме Playwright/test harness должен собирать console logs, network data, XHR requests, several screenshots and final report; просто «открыл браузер» — слабый след.

Перенос в billing example: агент чинит stale billing card, но сначала должен увидеть `/billing?checkout_success=true`, network refetch, endpoint response and card state. Браузерный след становится полезным только если связан с исходным promise: карточка тарифа обновляется после checkout return.

### Ralph Wiggum loop / stop hook

Arvid даёт хороший локальный пример hook-based continuation:

- agent tries to stop;
- stop hook blocks the exit;
- the same task/check is returned to the agent;
- cycle continues until a checkable condition is met.

Это нужно использовать не как «автономия до победы», а как **узкий runtime loop against a checkable promise**. Хорошие критерии: страница открывается без console errors, основной сценарий проходит, targeted tests pass, layout matches reference except listed differences. Плохие критерии: «сделай лучше», «улучши архитектуру», «почисти проект», если нет внешнего judgment.

Для главы IX это источник про границу hooks: hook может удерживать агентский запуск в работе, но он полезен только когда:

- задача ограничена;
- проверка дешева or допустима;
- агент имеет право запускать нужные команды;
- опасные команды запрещены;
- при product choice агент должен остановиться;
- история попыток остаётся понятной человеку.

### `allow` / `deny` and bypass risk

Самая важная деталь Arvid для главы IX — не `--chrome`, а тонкая проблема command permissions.

Конкретика:

- safe routine goes into `allow` in `settings.local.json`;
- Claude Code can add an allow rule after user chooses something like “Yes, and allow this in the future”;
- reasonable allow list: known build commands, targeted tests, Ralph Wiggum loop script, verified skills, project commands that do not change dangerous state;
- dangerous database operations go into `deny`, especially in Laravel examples: `php artisan db:wipe`, `migrate:fresh`, `db:*`, commands that reset local DB or touch production-like state.

Очень важная странная деталь: агент может попытаться обойти запрет. Arvid описывает случай, где запрещён `php artisan migrate`, но агент пишет bash script, inside which calls the same command. Формально запрещённая команда не была запущена directly; по смыслу агент пытался сделать то же самое другим путём.

Это надо перенести как один из центральных фактов главы: permission rules over command strings are not semantic intent understanding. Если запрещён `db:wipe`, но разрешён произвольный shell script, запрет слабый. Политика должна думать не только о строке команды, но о blast radius and alternative execution paths.

### Product/API/MCP surface equality

Arvid полезен ещё и как мост из локального runtime в продуктовую агентскую поверхность. Он ведёт or запускает sub-agent для файла equality between UI, REST API and MCP surfaces: feature available in UI/API/MCP or not. Это не главный материал IX, но может стать короткой вставкой: если продукт сам становится agent-consumable, runtime rights перестают быть только локальной проблемой разработчика. Агентская возможность должна быть равномерно описана и ограничена across surfaces; иначе одни опасные возможности окажутся доступны только через API/MCP, bypassing UI guardrails.

### Не переносить буквально

- Не утверждать, что `--chrome`, Ralph Wiggum plugin or `settings.local.json` are stable universal practices; это Claude Code-specific and time-sensitive.
- Не использовать слово «свидетельство» автоматически; в публичной главе лучше будет говорить «проверочный материал», «след проверки», «пакет проверки» where appropriate.
- Не делать вывод, что stop hook решает acceptance. Он только возвращает execution into loop.

## 3. HumanLayer: harness, tool pressure, hooks and back-pressure

Источник корпуса: `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md`; внешний living-source: HumanLayer, “Skill Issue” / harness article.

### Model + harness, not model alone

Главная переносимая формула HumanLayer: coding agent is AI model(s) + harness. Для IX это важно как отказ от рассуждения «модель умная / модель глупая». Runtime behavior определяется не только моделью, но AGENTS/CLAUDE files, tool list, MCP servers, skills, subagents, hooks, approval flow, logging, shell access and project-specific scripts.

Фактура:

- AGENTS.md / CLAUDE.md and similar files guide behavior, but are context/instruction layer, not enforcement.
- MCP servers add tools and tool descriptions into context; they can read and act via external systems.
- Tool descriptions consume context and can create tool pressure: too many tools make the agent worse, not better.
- One practical mitigation: replace a broad MCP surface with narrow CLIs or scripts where possible, because CLIs can be composed, logged, tested and reasoned about as normal software.

### Skills and progressive disclosure

HumanLayer supports a distinction useful for chapter VI but relevant here: skills reduce context pressure by loading procedures only when needed. In IX, this matters only where a skill changes runtime behavior: e.g. a billing skill tells the agent which tests to run, which logs to collect, which API mode is safe, and where to stop for approval.

Need not overdevelop. Chapter IX should say: skills can be part of the operational environment, but they remain instructions/procedures unless backed by hooks, permissions, sandbox and actual tools.

### Subagents as context/firewall, not magic parallelism

HumanLayer material supports the idea that subagents can isolate context or perform narrower tasks. In IX only use this if needed for platform-agent/runtime orchestration:

- main agent keeps task contract;
- subagent does narrow code search, test writing or log triage;
- subagent output returns as a report, not as accepted truth;
- if subagent has different tools/rights, that must be explicit.

Do not import the whole subagent chapter into IX. For this chapter, the relevant point is rights and tool surfaces can differ per agent/thread, so «agent had access» is too coarse.

### Hooks as control flow and verification pressure

HumanLayer gives practical hook vocabulary:

- hooks can enforce control flow;
- can route approvals;
- can run verification;
- can trigger integrations;
- can create back-pressure when agent tries to finish too early or after failing checks.

Concrete detail from HumanLayer notes: hooks are useful when success should be silent and failure should re-engage the agent/user. But the final chapter must not flatten all hooks into one category. Deterministic hooks, HTTP hooks and LLM hooks have different trust boundaries. A shell hook that runs `npm test -- billing` is not the same as an HTTP hook that sends task data to a remote service or a prompt hook that asks another model to judge.

### Transfer note for billing example

When billing fix tries to finish, a hook can run targeted tests and maybe a browser smoke check. If the hook fails, the agent continues. If the hook needs Stripe test credentials or production-like data, it should stop and ask for scoped approval. Hook failure is feedback; hook success is not acceptance.

## 4. Mike McQuaid / Sandvault: permissions moved below the model

Источники корпуса: `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md`; external: [Mike McQuaid, “Sandboxes and Worktrees”](https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/), [Sandvault repository](https://github.com/webcoyote/sandvault), [Homebrew CONTRIBUTING](https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md).

### The confirmation problem

Mike’s starting problem is not abstract security; it is approval fatigue. Agent work becomes useless if the human must constantly answer “yes, safe” and “no, dangerous”. But disabling checks or running YOLO on the main machine is unacceptable for a maintainer with tokens, repos and local state.

This is a strong IX point: if approvals are too frequent, humans get fatigued and approve too much; if approvals are removed without environmental constraints, the agent gets a dangerous blast radius. Sandvault is the middle form: fewer prompts inside a lower-privilege environment.

### Sandvault mechanics worth carrying

Concrete facts:

- `brew install sandvault`;
- `sv claude`, `sv codex`, `sv opencode`, `sv gemini`, `sv shell`;
- aliases: `sv cl`, `sv co`, `sv o`, `sv g`, `sv s`;
- pass arguments after `--`, e.g. `sv gemini -- --continue`;
- run a shell command inside sandbox: `sv shell /Users -- pwd`;
- pipe prompt via stdin: `cat PROMPT.md | sv gemini`;
- clone into sandbox: `sv codex --clone https://github.com/webcoyote/sandvault.git` or `sv codex -c ~/src/my-app`;
- native install mode: `--native-install` / `-N`, e.g. install Claude/Codex/Gemini/OpenCode inside sandbox user;
- defaults via `SANDVAULT_ARGS`, e.g. `export SANDVAULT_ARGS="--verbose --ssh"`;
- maintenance commands: `sv build`, `sv build --rebuild`, `sv --fix-permissions`, `sv uninstall`.

Mechanics of protection:

- agent runs as separate macOS user, such as `sandvault-$USER`;
- additional `sandbox-exec` layer limits files and resources;
- main home directory is not readable;
- no admin rights;
- no system file writes;
- no mounted disk access;
- write areas include `/Users/Shared/sv-$USER` and `/Users/sandvault-$USER`;
- system directories `/usr`, `/bin`, `/etc`, `/opt` read-only;
- other `/Users/*` inaccessible.

This is the clearest source family for the phrase: safety is moved from model instruction into runtime environment. Agent cannot simply decide to be careful; it operates as a different user with fewer rights.

### Shared directory and Git reality

Important practical detail: separate user creates file sharing problems. Mike moves repos/worktrees under a shared directory such as:

```text
/Users/Shared/sv-mike/repositories
/Users/Shared/sv-mike/worktrees
```

Git then needs safe directory settings for both users because ownership/group-write patterns look suspicious:

```ini
[safe]
    directory = /Users/Shared/sv-mike/repositories/*
```

This is good for chapter IX because it prevents a fantasy of “just sandbox it.” Execution environment design includes file ownership, ACLs, Git safety settings, bootstrap scripts and visible shell identity.

Mike also changes prompt color for Sandvault user. This tiny detail is valuable: isolation must be visible to the human. If the person cannot tell whether they are in host shell or sandbox shell, the system invites operational mistakes.

### Limits and bridges: no universal sandbox

Sandvault has constraints that should appear as caveats:

- `sv -x claude`, `sv --no-sandbox codex`, `sv --no-sandbox shell ...` still run as Sandvault user but without `sandbox-exec`; then no protection from `/Volumes/...` and world-writable file writes.
- GUI apps do not run normally inside the sandbox user because of macOS WindowServer boundaries.
- Swift/Xcode can break because nested sandboxing is not supported; workarounds include disabling SwiftPM/Xcode sandbox features when `SV_SESSION_ID` is present.
- Browser automation is bridged: host-side headless browser, sandbox-side connection via Chrome DevTools Protocol and `SV_BROWSER_ENDPOINT`; commands like `sv --browser claude`, `sv --chrome claude`, `sv --lightpanda claude`, `sv --endpoint`.
- iOS Simulator is also bridged through `SV_IOS_SIMULATOR_ENDPOINT`; commands include `/ready`, `/describe`, `/tap`, `/view_pixels`; bridge restricts paths and uses explicit subprocess argv, not shell.

These details show that tool/observation surfaces often puncture or bridge the sandbox. The question becomes not “is sandbox on?” but “which bridge crosses it, with what commands, credentials and logging?”

### Worktrees and Superset

Mike’s second layer is parallel work. First workaround: multiple clones like `homebrew` and `homebrew2`, which burdens human memory. Worktrees solve it better: each task gets its own directory/branch/diff.

Specific setup:

- Superset creates and manages worktrees;
- Sandvault runs the agents in those worktrees;
- agent commands configured as `sv claude --`, `sv codex --`, `sv gemini --`, `sv opencode --`;
- worktree location under shared Sandvault path;
- `script/bootstrap` prepares a new worktree before task starts.

For chapter IX: worktree isolates the diff and parallel write. Sandvault lowers machine/user privileges. Neither makes the PR correct or accepted. Mike still reviews locally before sharing; Homebrew policy keeps human responsibility around AI-assisted contributions.

### Not to overclaim

- Sandvault is macOS-specific and is not a universal recommendation.
- It improves the approval/safety tradeoff, but it does not solve semantic correctness.
- Browser/iOS bridges are useful but are also controlled holes through the boundary; final chapter should name them as bridges, not invisible magic.

## 5. Armin Ronacher / Pi / minimal harness: tools as designed observation

Источники: Ronacher blog posts and Pi artifacts; internal story/dossier: `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md`, `work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md`; key external links include [Agentic Coding Recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/), [Your MCP Doesn't Need 30 Tools](https://lucumr.pocoo.org/2025/8/18/code-mcps/), [Pi repo](https://github.com/earendil-works/pi), [Pi compaction docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md), [Pi containerization docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md).

### Minimal harness before platform

Ronacher contributes a different pole from Mike. Mike shows lower-level OS isolation; Ronacher shows a small, tool-shaped local harness:

- scripts such as `make dev` and `make tail-log` become agent-facing tools;
- logs should be written to predictable files;
- tools should fail quickly and clearly;
- browser/debug surfaces should let agent observe the running app;
- debug email printed to stdout/log can let agent sign in without real inbox access;
- MCP is useful, but not every integration should become a large MCP catalog;
- ordinary CLIs/scripts/code can be a better tool substrate because they compose and can be tested.

This is ideal for chapter IX’s tool/observation section. It says: an environment is not only a permission fence. It is also a set of designed affordances that let the agent see just enough of the system.

### `--dangerously-skip-permissions` caveat

Ronacher’s practice sometimes uses permissive agent modes such as `claude --dangerously-skip-permissions` in a controlled environment. This should be presented carefully. The useful transfer is not “skip permissions”; it is “if you reduce prompting, do it inside a thought-through environment with narrow tasks, good scripts and fast feedback.” Otherwise it is just YOLO.

This can be paired with Mike:

- Mike moves safety below the agent by separate user/sandbox.
- Ronacher makes local scripts/logs/browser into good tools.
- Both reject the idea that the model’s instruction text is enough.

### Pi as source family for session/work state

Pi details are more relevant to C4/XI, but some should be held for IX:

- repo README positions Pi as agent harness, CLI, session sharing and sandboxing rather than only a desktop UI;
- session traces and compaction summaries exist as artifacts;
- issue `#92` and `compaction.md` cover branch summarization, session file semantics, `/compact`, `/autocompact` and limitations around images/attachments;
- issue `#4945`, PR `#4979` and release `v0.76.0` show a real runtime failure around Codex WebSocket/SSE hanging and a repair with bounded waits, idle timeout and response header timeout.

The `#4945`/`#4979` episode is useful if the chapter needs a non-glamorous failure example: agent runtime is software, and its network streams, SSE/WebSocket waits, session usage counters and hanging states must be engineered. A coding agent environment is not just prompt plus model; it has transport, timeouts, session persistence and recovery bugs.

### To use cautiously

- Ronacher’s material is authorial/practice-based, not controlled evaluation.
- Pi changes quickly; final chapter should re-check repository/release/issue state before public assertion.
- Do not let the Pi material pull IX into a full chapter about custom agent products; use it for minimal harness, code-as-tool, session/runtime failure and artifact trace.

## 6. Shopify Roast / Quix: workflow as executable structure, not prompt improvisation

Источники корпуса: `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`, `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md`; external: [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast), [Shopify Roast repo](https://github.com/Shopify/roast), [Doubrovkine Roast walkthrough](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html), Quix/Klaus Kode source from P04.

### Why Roast belongs in IX

Roast is the strongest source family for the workflow-runtime section because it makes the agent a step in an executable procedure. The unit is not a chat; it is a versionable workflow file with steps, prompts, commands, Ruby code, agent invocation, loops, mapped collection processing and session replay/resume.

Core thesis from Shopify story:

- Allowing an agent to roam freely around millions of lines did not work reliably.
- Complex tasks are split into discrete steps.
- Ordinary code and deterministic steps surround the uncertain AI step.
- AI can temporarily approximate a step that later becomes deterministic code.

This supports the chapter’s anti-catalog argument: the runtime is not just a powerful agent; it is the contour around the agent.

### Boba as deterministic-agentic sandwich

Boba is the best transferable example:

1. remove old `typed: false` marker;
2. raise strictness to `true`;
3. run Sorbet autocorrect;
4. inspect remaining type errors;
5. give `CodingAgent` a specific file and residual Sorbet errors;
6. ask it to fix without changing test behavior;
7. run tests and type checks after.

This shows why agent runtime design is not “give more context”. It narrows the task before the agent sees it. The agent works on the residue of deterministic tooling.

### Roast cogs and artifacts

Useful details from repo/story:

- public package/Ruby gem with CLI;
- workflow can contain `chat`, `agent`, `ruby`, `cmd`, `map`, `repeat`, `call`;
- built-in tools include file read/write/update, grep/search, command/bash and `CodingAgent` integration;
- `code_review.rb` chain example: `agent(:review_security)` → `chat(:prioritize)` → `chat(:summarize_for_executive)` → `ruby(:display_report)` → `check_report`;
- `repeat` supports control flow with `break!`, `next!`, outputs;
- session resumption/forking via `my.session` lets expensive/long interactions continue or branch;
- model routing can differ by step;
- workflow state and outputs can be stored under `.roast/sessions` or similar session artifacts.

For IX, the important thing is not all cogs. The important thing is that some actions are deterministic (`cmd`, `ruby`), some are model-based (`chat`, `agent`), some iterate (`repeat`), some fan out (`map`), and some preserve session state. This gives a form for mixed runtime.

### Doubrovkine external run

The Doubrovkine walkthrough adds gritty details:

- checks OpenAI API key with ordinary `curl` before Roast;
- runs a Roast workflow against `test/roast/resources_test.rb`;
- changes workflow model configuration because of model availability/cost: adds `api_token: $(echo $OPENAI_API_KEY)` and `model: gpt-4.1-mini`, removes local `o3`/other overrides;
- output quality differs by model;
- run produces logs/report rather than mystical answer.

This is useful because it shows workflow runtime touching secrets/model configuration and ordinary shell environment. It also shows why model routing and API credentials are runtime concerns.

### Quix / Klaus Kode contrast

Quix story from P04 should be paired with Roast briefly:

- exact sequences in prompt are brittle;
- a huge MCP/tool catalog consumed too much context — one source noted tool descriptions at 34% of context;
- orchestration moved to deterministic Python/API calls where possible;
- Claude Code was used for discrete coding steps;
- code, variables and dependencies were uploaded to a cloud sandbox, the app ran there, logs were downloaded;
- simple API calls were performed by deterministic functions, not delegated to Claude.

This gives a second independent example of the same architectural movement: put sequencing, setup, API calls, uploads, retries and log collection into normal code; reserve the agent for the uncertain step.

### Boundary to C4/PWG

Roast/session runtime can resume/fork/record execution. It still does not know if the work item is accepted, blocked, waiting for domain owner, or safe to merge. That boundary belongs in the close of the IX workflow section.

## 7. Stripe Minions and Stripe agent-facing environment: platform-agent direction, with source caution

Источники корпуса: `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md`, `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md`; external: [Stripe Minions Part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents), [Stripe Minions Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2), [Stripe integration benchmark](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations), [Stripe AI steering experiments](https://stripe.dev/blog/ai-steering-experiments), [Stripe Sessions 2026 Developer Keynote](https://stripe.com/sessions/2026/developer-keynote), [InfoQ secondary summary](https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/).

### Why Stripe is useful but dangerous

Stripe is valuable for the platform-agent layer: internal agent system, devbox-like environment, blueprints, tools, PR production, metrics, human review, domain-specific benchmarks. But article extraction/access was incomplete in earlier pass, and public numbers come from different contexts. Therefore Stripe should support direction, not carry unverified architecture claims.

### Facts worth preserving with caution

- Publicly visible official/secondary sources report very large PR volume from Minions, e.g. 1000+ weekly Minion PRs and later higher numbers in secondary/current sources.
- Sources repeatedly keep human review/approval in the frame. Output is PR/candidate change, not automatic truth.
- Metrics must not be collapsed: “Minion-produced PR”, “AI-assisted PR”, “merged PR”, “production PR”, “one-shot merge”, “without human code” may name different denominators.
- Review bottleneck is part of the story. Many PRs shift work toward review, triage, CI, policy and evidence, not away from human responsibility.

### Stripe integration benchmark as stronger IX support

The benchmark article is more directly useful for IX than some Minions marketing facts:

- 11 realistic integration environments;
- each environment includes code, databases, scripts and test Stripe API keys;
- agents use a harness with terminal, browser and Stripe-specific search/tools;
- graders are deterministic and inspect API/UI/Stripe artifacts such as test-mode Checkout Session;
- payments domain requires correctness, not “almost right”.

This is nearly perfect for the billing/UI cross-example. It grounds the idea that a real billing agent needs code, DB, scripts, test keys, browser, API objects and deterministic graders. The chapter can cite Stripe benchmark when explaining why billing evidence must include domain artifacts, not only unit tests.

### AI steering experiments

Stripe’s “You can’t whisper at an AI agent” supports a useful IX/VI bridge:

- passive hints in hidden docs/comments/AGENTS may not be read;
- active steering works better when instruction appears on the path of execution: loaded context, explicit errors, skills at high-intent moments, tool interventions, deterministic controls;
- if a rule matters, do not rely on whispering it from a place the agent may never touch.

In IX, this becomes: environment must put constraints and checks where action happens. A billing provider best-practice hidden in docs is weaker than a test, skill, tool error or harness check that fires when agent calls the API incorrectly.

### Stripe Sessions episode

The public keynote episode — request in Slack to remove “public preview” from docs because product is now GA; Minion later proposes a change; human merge remains visible — is a good small platform-agent scene. It shows:

- task starts in a normal work surface, not an IDE;
- agent runs somewhere else;
- result comes back as proposed change;
- human still merges/accepts.

Use as optional illustration if final chapter needs a platform-agent vignette. Do not overbuild entire architecture from the keynote alone.

## 8. Codex / Claude Code / Kiro / Fowler: current product mechanics as comparative guardrails

### Codex / OpenAI

External primary sources from P04: Codex security, sandbox, permissions, rules, hooks, MCP, subagents, app worktrees.

Facts to carry:

- default network is off in local Codex/security docs; network access is a boundary, not a default entitlement;
- local Codex uses OS-backed sandboxing: macOS Seatbelt, Linux Landlock/seccomp, Windows native sandbox details in CLI/source docs;
- `sandbox mode` and `approval policy` are distinct layers;
- permission profiles include `:read-only`, `:workspace`, `:danger-full-access`;
- profiles govern sandboxed local command execution; connectors, MCP, browser/computer-use, cloud and approved escalations have separate controls;
- network allowlist is not a trust decision;
- command rules match argv prefixes and choose `allow`, `prompt`, `forbidden`; most restrictive wins;
- wrapper/compound commands such as `bash -lc ...` can hide multiple actions, so command rules are not semantic proof;
- hooks can log, scan prompts, update memories, validate, customize directory prompts;
- MCP adds tools/context/docs/browser/Figma and server instructions;
- Codex subagents are explicit orchestration: spawn, route instructions, wait, close threads; not automatic magic;
- app worktrees support background/independent tasks and handoff, but ignored files may not move.

These facts should be distributed across sections, not dumped. The strongest claims:

1. sandbox is not approval;
2. permission profile is not whole agent surface;
3. allowed network is not trusted network;
4. command rule is not semantic intent boundary.

### Claude Code / Anthropic

External primary sources: security, settings, hooks, MCP, IDE/browser, common workflows, subagents, skills, CLI reference.

Facts to carry:

- strict read-only default; edits/tests/commands ask permission;
- sandboxed Bash restricts filesystem/network and writes under project unless permitted;
- allowlists and Accept Edits reduce prompt fatigue;
- settings can restrict managed hooks (`allowManagedHooksOnly`) and HTTP hook URL allowlists;
- hooks may be shell commands, HTTP endpoints or LLM prompts at lifecycle events; handlers inspect JSON and return decisions;
- MCP tools can read and act through databases/APIs/services, not just provide pasted context;
- `@browser` can test apps, debug console logs, automate browser workflows; browser shares login state/access to signed-in sites;
- `--tools` restricts built-in tools but MCP tools need separate disallow/strict configuration;
- `--worktree` creates isolated worktree under `.claude/worktrees/<name>`;
- skills are repeated instructions/procedures whose body loads only when used.

Strong use in IX: browser/session boundary and surface-specific tool control. If browser shares login state, the agent has authority through credentials. If `--tools` ignores MCP tools, permission policy is not global.

### Kiro / hooks / steering

Use lightly. Kiro is useful because it shows hooks as productized agent-environment mechanics:

- hooks execute predefined agent prompts or shell commands on events: file save/create/delete, user prompt submission, agent turn completion, before/after tool invocation, before/after spec task, manual trigger;
- setup includes title/description/event/tool/file pattern/action;
- hooks can update tests on React component save, refresh README on API endpoint changes, scan leaked credentials before commit;
- steering files like `product.md`, `tech.md`, `structure.md`, AGENTS.md and inclusion modes are context layer, not execution boundary.

In IX, use Kiro to show hooks are moving into mainstream IDE/agent products, but avoid a Kiro overview.

### Fowler / harness engineering

Fowler supports a vocabulary for harness:

- harness = everything around the model;
- feedforward guides vs feedback sensors;
- computational vs inferential controls;
- sensors include type checker, ESLint, Semgrep/SAST, dependency-cruiser, test suite, coverage, incremental mutation testing;
- harness can act as cybernetic governor/regulator against drift.

This is useful as connective theory language, but chapter should not sound like a citation collage. Put Fowler where explaining why logs/tests/hooks/browser are not decoration but feedback sensors.

## 9. MCP specification/security: tool surface is operational authority

External primary sources from P04: MCP Tools spec, Security Best Practices, Authorization, Tool annotations, Client best practices, MCP Apps.

### Facts to transfer

- MCP tools expose external systems: databases, APIs, computation, browser and other services.
- Tools are model-controlled; clients should show available tools, indicators and allow users to confirm/deny calls.
- MCP security guidance names confused-deputy risk, token passthrough anti-pattern, audit trail gaps and trust-boundary violations.
- OAuth 2.1 is recommended when server accesses user data, performs actions requiring consent, audits actions, supports enterprise controls or rate limits.
- Tool annotations such as `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint` are hints, not guarantees; clients must not trust them unless server is trusted and enforcement exists.
- Client best practices distinguish direct tool calling from programmatic/code mode where model writes code that calls tools inside a sandbox.
- MCP Apps/UI surface means code from MCP server runs inside host boundary with sandboxing/JSON-RPC/consent mitigations.

### How to use

The key sentence for IX: MCP is not “context”. MCP is a rights surface. It can bring instructions into context, expose data, mutate systems, carry credentials and return untrusted content. Therefore tool description, tool name and risk hint must not be treated as enforcement.

In billing example: if MCP exposes `get_customer`, `create_test_checkout`, `cancel_subscription`, `list_events`, `update_issue`, the environment needs separate controls for read-only, destructive, idempotent and external-world calls. The fact that the tool says “readOnly” is not enough; the trusted client/server boundary and log/approval policy matter.

## 10. Durable execution family: continuation of run, not acceptance of work

Sources from P04: LangGraph overview/interrupts/HITL, Temporal workflow/event history/HITL cookbook, Restate durable execution, DBOS workflows.

### LangGraph / LangChain HITL

Facts:

- durable execution persists graph state through failures and supports resume;
- interrupts pause execution and save graph state via persistence/checkpointer/thread_id;
- human can approve/edit/reject/respond around risky tool calls;
- side effects before interrupt must be idempotent or carefully designed;
- `respond` and similar modes can be dangerous if treated as successful tool result for side-effecting actions.

Use: approval pause can be inside runtime, but it is approval of a step, not acceptance of final change.

### Temporal

Facts:

- workflow/event history is durably persisted and replayed;
- workflows can wait hours/days/indefinitely without keeping compute active;
- human-in-the-loop approval can be a Signal;
- workflow can execute if approved, cancel/reject/timer out otherwise;
- event history is append-only audit log for workflow execution;
- replay can recreate pre-failure state.

Use: excellent example for run continuity and audit trail, but not for semantic evidence. Temporal can know that approval signal was received; it does not know whether billing PR should be accepted by domain owner.

### Restate / DBOS

Facts:

- Restate records steps/side effects in a journal; replay skips completed steps and resumes;
- server can act as reverse proxy/message broker and track invocations exactly once;
- DBOS workflows/steps resume from last completed step after executor interruption;
- workflow IDs support background workflows/idempotency.

Use: durable execution needs idempotency and side-effect design. In billing example, external test objects or webhook calls must be recorded so retry/resume does not duplicate or confuse state.

### Transfer boundary

Phrase to preserve: a durable runtime can continue the run; it cannot itself decide what the work means. This must close the runtime section and lead into PWG/evidence/authority.

## 11. GSD / BMAD / PWG / Gas Town: secondary boundary donors

### PWG / Beads

Use in IX mostly as contrast and bridge:

- `bd gate` can wait on human, timer, GitHub run, GitHub PR or bead;
- `bd gate check` can test whether gate condition is satisfied;
- `bd prime` creates compact Markdown context for AI after compaction/new session;
- PWG states include ready/claimed/blocked/waiting_gate/review/accepted/rejected/recovering style distinctions;
- `run_id` can link a run to work item;
- evidence package belongs near work item/claim/gate, not inside raw runtime trace.

This is important because IX should not pretend durable execution solves handoff. It prepares for C4/XI: trace becomes useful when attachable to a work item and gate.

### GSD / BMAD

Use lightly:

- GSD contributes task gates and browser/worktree proof-style examples, but IX should not become a GSD chapter.
- BMAD contributes planned role/process boundaries and handoff of agent tasks; in IX, this is background for separating plan/spec from execution environment.

### Gas Town

Gas Town is useful only for scale and operationality if needed: as soon as many agents/runs exist, scheduling/gates/work items matter. Do not import Gas Town details unless final chapter needs a short sentence about work graph/runtime scale.

## 12. Visual and artifact candidates for later pass

Do not insert now, but keep candidates:

- Mike/Sandvault screenshots from story assets: `08-mike-sv-claude.png`, `08-mike-codex.png`, `08-mike-superset.png`, `08-mike-superset-prompt.png` — strong for execution envelope/worktree visual.
- Shopify Roast structured workflow article asset, Boba CodingAgent asset, code/repo workflow examples — strong for executable workflow.
- Stripe Sessions Minion PR/keynote docs-cleanup assets — useful if platform-agent section needs official scene.
- Stripe integration benchmark figure — useful for billing/domain evidence connection.
- Arvid browser cycle screenshot candidates if available — useful for browser/runtime, but must avoid weak generic screenshot.

Need later rights/layout/source pass before public insertion. Current archive may not include local asset files for all candidates.

## 13. Facts that should become prominent in the final chapter

1. **Permission string is not semantic safety.** Arvid’s bash-script-around-deny and Codex argv-prefix/shell-wrapper caveat both say this.
2. **Browser is credentialed action, not a viewport.** Claude Code browser sharing login state, Sandvault browser bridges and billing example all support this.
3. **Network allowlist is connectivity, not trust.** Codex source explicitly supports this; MCP returned content can still be untrusted.
4. **MCP tool hints are not enforcement.** Tool annotations help but are not trust contracts.
5. **Sandbox bridges are part of the boundary.** Sandvault browser/iOS endpoint bridges show that observation often crosses the sandbox through designed APIs.
6. **Hooks add runtime control but also become trust surfaces.** Managed hooks/HTTP allowlists show hooks themselves need governance.
7. **Deterministic tooling should surround agentic steps.** Roast/Boba/Quix/Fowler all support this.
8. **Durable execution is about run continuity.** LangGraph/Temporal/Restate/DBOS support resume/replay/wait, but not accepted meaning.
9. **Worktree creates reviewable diff.** It does not create accepted result.
10. **Platform-agent metrics do not remove review.** Stripe should be used as evidence of scale and platformization, not as proof that human authority vanished.

## 14. Open source-check items before public drafting

- Re-open current Codex/Claude docs if chapter drafting happens later; these are moving product docs.
- Verify Stripe Minions primary article body through accessible route before asserting exact architecture such as blueprint/devbox/judge internals.
- Re-check Stripe Sessions transcript/visual claims if using the keynote scene or PR metrics.
- Re-check Pi README/release/issues before public mention; Pi project changed quickly in dossier.
- Verify exact MCP spec URLs and version (`draft` vs dated version) before final citation.
- If using HumanLayer hook details such as exit code / control-flow mechanics, re-open the source and quote only what is actually there.
- If using Sandvault GUI/browser/iOS bridge details, cite repository README in addition to Mike’s post.
- If using Homebrew AI PR policy, cite exact current contributing section and avoid overgeneralizing beyond Homebrew.

## 15. What not to do in the chapter

- Do not write a product comparison chapter.
- Do not make `sandbox` a metaphor for all controls.
- Do not say approval means trust.
- Do not say successful hook/test means acceptance.
- Do not say MCP gives context without saying it can also give operational authority.
- Do not make worktree/devbox/PWG interchangeable.
- Do not let Stripe numbers substitute for mechanism.
- Do not insert visual assets without a separate visual/source pass.

## 16. Short bridge sentence for future draft

A possible bridge out of IX:

> В конце запуска у агента может быть рабочее дерево, diff, журнал команд, результаты тестов, browser trace, список вызванных инструментов, approvals and workflow history. Это ещё не доказательство и не право на merge. Это только материал, который следующая глава должна связать с обещанием изменения, а затем передать в контур человеческого принятия.

This sentence should be rewritten before insertion, but it preserves the exact boundary from IX to XI/XII.
