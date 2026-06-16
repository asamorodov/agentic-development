# P04 — External discovery для главы IX

Статус: внешний поиск выполнен достаточно для текущего рабочего листа. Это не финальный библиографический список главы и не visual pass. Цель прохода — отделить источники, которые действительно должны войти в главу IX, от источников, которые нужно оставить в register, отложить или не использовать.

Главный результат discovery: глава IX должна быть написана не как обзор LangGraph, Temporal, Codex, Claude Code, MCP, Roast, Stripe или Sandvault, а как глава о том, что превращает действие агента из «модель сказала и что-то вызвала» в ограниченное, наблюдаемое, возобновляемое и подотчётное действие. Источники хорошо подтверждают четыре слоя из A6/C4, но добавляют несколько более точных различений: `sandbox` не равен approval policy; permission profile не покрывает все поверхности агента; MCP tool hints не являются договором доверия; браузер с сохранённой сессией переносит агента в область пользовательских credentials; durable execution сохраняет ход исполнения, но не создаёт само по себе ни evidence, ни право принять результат.

## 1. Что найдено и как это использовать

### 1.1. Codex / OpenAI docs: не один контроль, а несколько разных контуров

Использовать в главе обязательно. Официальные документы OpenAI полезны не только как справка по Codex, а как хороший текущий пример разложения агентской среды на несколько независимых контрольных плоскостей.

Что переносить в главу:

- В Codex явно разведены `sandbox mode` и `approval policy`: sandbox определяет, что агент технически может сделать сам; approval policy определяет, когда он должен просить разрешение на выход за пределы этой рамки или на рискованное действие. Это нужно использовать как один из главных примеров различия между технической границей и моментом человеческого подтверждения.
- Permission profiles (`:read-only`, `:workspace`, `:danger-full-access`) относятся прежде всего к sandboxed local command execution. Документация отдельно предупреждает, что connectors, MCP servers, browser/computer-use, cloud environments и approved escalations имеют собственные настройки и ограничения. Это важное уточнение против ложной фразы «мы включили read-only, значит агент безопасен вообще».
- Документация Codex отдельно говорит, что разрешение сетевого доступа к домену не делает этот домен доверенным. Это сильная формулировка для раздела про сеть и credentials: network allowlist — не trust decision.
- Rules в Codex работают на уровне argv-prefix и могут выбирать `allow`, `prompt`, `forbidden`; при совпадениях побеждает наиболее ограничительное решение. Но shell wrappers и compound commands могут скрывать несколько действий, поэтому правила команд не являются полным смысловым пониманием действия.
- Hooks в Codex — deterministic scripts during lifecycle: logging, prompt scanning, memory summaries, validation checks, directory-specific prompt customization. Их стоит использовать как пример детерминированного runtime-control, но не как замену evidence.
- MCP в Codex расширяет доступ к внешним tools/context; server instructions читаются и используются вместе с tools. Это важно для темы: tool surface одновременно даёт возможности и заносит инструкции/контекст в среду агента.
- Subagents в Codex описаны как явная оркестрация: Codex spawns, routes instructions, waits, closes threads; по документации он спаунит их только when explicitly asked. Это не основной фокус IX, но может поддержать мысль о runtime orchestration и изоляции контекстов.
- Worktrees in Codex app: local checkout vs worktree, background tasks, handoff between Local and Worktree, independent tasks, ignored files not moved. Это важно для execution boundary, но не надо превращать в UI-обзор.
- OS-level sandbox details: macOS Seatbelt, Linux Landlock/seccomp, Windows native sandbox. В главе достаточно показать, что «sandbox» в реальности не абстрактная метафора, а разные OS-backed enforcement mechanisms, поэтому portability и platform semantics важны.

Источники:

- OpenAI Codex, Agent approvals & security: https://developers.openai.com/codex/cli/security/
- OpenAI Codex, Sandbox: https://developers.openai.com/codex/cli/sandbox/
- OpenAI Codex, Permissions: https://developers.openai.com/codex/cli/permissions/
- OpenAI Codex, Rules: https://developers.openai.com/codex/cli/rules/
- OpenAI Codex, Hooks: https://developers.openai.com/codex/cli/hooks/
- OpenAI Codex, MCP: https://developers.openai.com/codex/cli/mcp/
- OpenAI Codex, Subagents: https://developers.openai.com/codex/cli/subagents/
- OpenAI Codex app, Worktrees: https://developers.openai.com/codex/app/worktrees/
- OpenAI Codex CLI sandbox source/options: https://github.com/openai/codex/blob/main/codex-cli/src/utils/agent/sandbox.ts and official docs excerpted via search.

Решение: integrate now. В главе ссылаться не кучей документов подряд, а при первом введении соответствующего различения.

### 1.2. Claude Code / Anthropic docs: permission, hooks, MCP, browser, worktree как отдельные поверхности

Использовать в главе обязательно, особенно рядом с Codex, чтобы не делать главу «про один продукт».

Что переносить:

- Claude Code docs describe strict read-only permissions by default: edits, tests, and command execution request permission; read-only commands can run without prompt. Это поддерживает базовый тезис: permission layer начинается ещё до workflow runtime.
- Sandboxed Bash ограничивает filesystem/network и пишет только в стартовую папку и подпапки, unless permission; Allowlist/Accept Edits уменьшают prompt fatigue. Это важный пример компромисса: контроль должен быть достаточно строгим, но не должен превращать работу в бесконечную серию подтверждений.
- `allowManagedHooksOnly` and HTTP hook URL allowlists: enterprise/managed controls can restrict which hooks are loaded. Это хороший пример того, что hooks сами становятся частью trust boundary.
- Hooks reference: hooks can be shell commands, HTTP endpoints, or LLM prompts at lifecycle points; handlers inspect JSON event and can return a decision. В главе надо развести deterministic hooks and LLM/prompt hooks: первые дают жёсткую процедуру, вторые добавляют ещё один judgement layer.
- MCP docs: once connected, Claude Code can read and act directly through tools, APIs, databases and services rather than pasted data. Это надо связать с тезисом: tool integration is not “context only”; it is operational capability.
- VS Code browser integration: `@browser` lets Claude test apps, debug console logs, automate browser workflows, and the browser shares login state. Это важный источник для credentials/session boundary. Браузер — не нейтральный экран, а доступ к уже авторизованному миру пользователя.
- CLI reference: `--tools` restricts built-in tools, but MCP tools are not affected; MCP requires separate disallow/strict config. Это ещё одно подтверждение, что controls are surface-specific.
- `--worktree` starts isolated git worktree under `.claude/worktrees/<name>`. Use only as supporting detail.

Источники:

- Claude Code, Security: https://code.claude.com/docs/en/security
- Claude Code, Settings: https://code.claude.com/docs/en/settings
- Claude Code, Hooks reference: https://code.claude.com/docs/en/hooks-reference
- Claude Code, Automate actions with hooks: https://code.claude.com/docs/en/hooks
- Claude Code, MCP: https://code.claude.com/docs/en/mcp
- Claude Code, VS Code integration / browser: https://code.claude.com/docs/en/ide-integrations
- Claude Code, Common workflows: https://code.claude.com/docs/en/common-workflows
- Claude Code, Subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code, Skills: https://code.claude.com/docs/en/skills
- Claude Code, CLI reference: https://code.claude.com/docs/en/cli-reference

Решение: integrate now. Особенно использовать browser/session-state point and surface-specific tool control.

### 1.3. MCP specification and security guidance: tools are model-controlled, hints are not trust contracts

Использовать в главе обязательно, но не уходить в отдельную security-главу. MCP здесь нужен как текущий язык tool boundary: что именно агенту даётся через protocol, где проходит consent, почему tool descriptions/hints нельзя считать безопасными сами по себе.

Что переносить:

- MCP tools expose external systems such as databases, APIs and computation; tools are model-controlled. Client applications should display available tools, show indicators, and allow users to confirm or deny tool calls.
- MCP security best practices describe confused-deputy risks, token passthrough as an anti-pattern, audit trail problems and trust-boundary violations. В IX эти детали лучше не раскрывать глубоко, но надо добавить короткое замечание: как только tool server получает полномочия действовать от имени пользователя, мы вышли за рамку «дать модели больше контекста».
- Authorization guidance: OAuth 2.1 is recommended when server accesses user data, performs actions requiring consent, audits actions, enterprise controls, rate limiting. Это полезно для фразы о том, что authorization is part of runtime architecture, not optional product polish.
- Tool annotations/risk hints: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint` describe behavior, but are hints rather than guarantees; clients must treat them as untrusted unless server is trusted. Это один из самых важных найденных источников для главы: labels are not enforcement.
- Client best practices distinguish direct tool calling and programmatic/code mode, where model writes code that calls tools inside a sandbox. Это поддерживает мост к «code as tool» and sandbox requirement.
- MCP Apps guidance: running UI from MCP servers means code you did not write runs inside MCP host; mitigations include iframe sandbox, pre-declared templates, auditable JSON-RPC and user consent. Это likely source-register / optional short mention; not central unless visual/platform UI section grows.

Источники:

- MCP Security Best Practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices
- MCP Authorization: https://modelcontextprotocol.io/specification/draft/basic/authorization
- MCP Tools: https://modelcontextprotocol.io/specification/draft/server/tools
- MCP Tool annotations: https://modelcontextprotocol.io/specification/draft/schema#toolannotations
- MCP Client best practices: https://modelcontextprotocol.io/development/client
- MCP Apps: https://modelcontextprotocol.io/docs/learn/apps

Решение: integrate now selectively. Не превращать IX в OWASP/MCP security article; security research papers оставить в register.

### 1.4. Durable execution / workflow runtimes: сохраняют ход, но не заменяют принятие результата

Использовать в главе как концептуальный слой, но не делать обзор фреймворков.

Что переносить:

- LangGraph: позиционируется как orchestration runtime for durable execution, streaming, human-in-the-loop and persistence. Interrupts pause graph execution, save graph state using persistence, and resume with a thread ID/checkpointer. HITL middleware can approve/edit/reject/respond around risky tool calls; important caveat: `respond` is not for denying side-effecting tools because its message is treated as a successful tool result.
- Temporal: workflows can wait for human approval via signals, wait hours/days/indefinitely without consuming compute, durable timers survive disruptions, decisions can be logged. Temporal Event History is durable, append-only, enables recovery/replay and serves as an audit log for debugging. This is strong support for durable runtime state, but it is still not the same as project evidence or semantic acceptance.
- Restate: tracks invocations through completion; records steps and side-effecting operation results in a journal; on failure replays journal, skips completed steps and resumes. Useful as clean explanation of durable execution.
- DBOS: workflows wrap ordinary TypeScript/JavaScript functions into steps; if interrupted, program resumes from last completed step; workflow IDs can act as idempotency keys. Good source if the chapter needs a short current-practice breadth point.

Sources:

- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangGraph interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- LangChain/LangGraph Human-in-the-loop middleware: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- Temporal Human-in-the-Loop AI Agent cookbook: https://docs.temporal.io/ai-cookbook/human-in-the-loop-python
- Temporal Workflow/Event History docs: https://docs.temporal.io/workflow-execution/event and https://docs.temporal.io/workflows
- Restate key concepts: https://docs.restate.dev/foundations/key-concepts
- DBOS Workflows docs: https://docs.dbos.dev/typescript/tutorials/workflow-tutorial

Решение: integrate now, but with strict boundary. Формула для будущего текста: durable runtime can resume an execution; it does not know by itself whether the execution produced acceptable work.

### 1.5. HumanLayer / harness engineering: сильный общий язык, но не источник для всех claims

Использовать как один из основных живых внешних anchors. Текст хорошо ложится на IX, но в главе нужно избегать рекламы термина harness engineering and not over-adopt the blog’s voice.

Что переносить:

- Coding agent = AI model + harness. Harness as runtime/peripherals: tools, MCP servers, subagents, skills, hooks, AGENTS/CLAUDE files, back-pressure.
- MCP servers add tool descriptions and arguments into the agent context; untrusted servers are prompt-injection risk; client-side STDIO servers can execute code on host. This reinforces MCP trust boundary.
- Tool overload / context bloat: too many MCP tools inflate context and reduce quality; HumanLayer’s example of replacing broad Linear MCP with small CLI is useful as practical move, but not central to IX unless tools section needs concreteness.
- Skills as progressive disclosure; subagents as context control rather than role cosplay; hooks as control flow; hooks can enforce approvals, integrations, verification and back-pressure.
- The hook example that silently runs build/typecheck and only surfaces errors is particularly useful for distinguishing runtime feedback from verbose evidence: failures return to the agent; success stays silent.

Source:

- HumanLayer, “Skill Issue: Harness Engineering for Coding Agents”: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents

Решение: integrate now. Use as external live anchor for “model + harness”; avoid repeating all tactical advice.

### 1.6. Armin Ronacher / local tools: everything observable can be a tool

Использовать as human-practice anchor for small local harness. Это хорошо связывает IX with ordinary engineering rather than enterprise platform only.

Что переносить:

- Ronacher treats shell scripts, MCP servers, and log files as tools if the agent can interact with or observe them.
- Tools must be fast, clear, protected against misuse, and provide debuggability/observability.
- `make dev` with pidfile and useful failure message prevents duplicate server starts; logging output to a file lets the agent diagnose running services. This is an excellent small example of a tool designed not for humans only, but for an agent that will misuse it.
- Debug-mode email links logged to stdout let the agent complete sign-in through browser automation. This should be used carefully: it proves power of observation, but also introduces secret/session boundary.
- Ronacher’s MCP/code post supports the idea that for many tasks a small programmable code surface or CLI is better than a large MCP catalog. Use this as supporting point, not as IX’s main argument.

Sources:

- Armin Ronacher, “Agentic Coding Recommendations”: https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- Armin Ronacher, “Your MCP Doesn’t Need 30 Tools: It Needs Code”: https://lucumr.pocoo.org/2025/8/18/code-mcps/

Решение: integrate now. Use as one concrete example in tools/observation section.

### 1.7. Sandvault / worktrees: boundary of filesystem, user account and review surface

Использовать as concrete boundary example. Не делать из него security solution вообще; Sandvault is macOS-specific and practical.

Что переносить:

- Sandvault manages a limited macOS user account for AI agents and shell commands; it is positioned as lightweight alternative to VM isolation.
- Features include shared workspace, AI agent support, web/iOS automation, and defense in depth via limited user account + `sandbox-exec`.
- Sandvault has nested sandbox caveats around Swift/Xcode; this is useful to mention only if the chapter needs to show that sandboxing has platform/toolchain friction.
- Mike McQuaid’s setup combines Sandvault commands with worktrees and review. He uses sandboxed worktrees to spin up agents, sometimes multiple agents with different approaches, then reviews locally before sharing. This is useful because it ties execution isolation to review boundary: worktree/sandbox helps produce work, but the human review step remains separate.
- Homebrew AI PR policy belongs more to acceptance/authority chapters; in IX mention only as boundary: execution environment does not by itself settle maintainer policy.

Sources:

- Sandvault repository: https://github.com/webcoyote/sandvault
- Mike McQuaid, “Sandboxes and Worktrees”: https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/
- Git worktree docs, if needed for canonical semantics: https://git-scm.com/docs/git-worktree

Решение: integrate now. Keep factual, no claim of universal security.

### 1.8. Shopify Roast / Quix: executable workflows as middle layer between free agent and deterministic pipeline

Использовать as current-practice anchor for workflow execution around agents.

What to transfer:

- Shopify Roast is described as a convention-oriented workflow orchestration framework for structured AI workflows that interleave non-deterministic AI behavior with normal code execution. It uses YAML/markdown in the blog article, while the current README frames it as a Ruby DSL with cogs; the chapter should avoid assuming one surface as final unless citing a specific source/date.
- Roast’s key point for IX: complex AI work becomes reproducible/testable workflow; deterministic steps and agent steps are interleaved; session replay/resume reduces rerunning expensive AI operations; cogs include `chat`, `agent`, `ruby`, `cmd`, `map`, `repeat`, `call`.
- Roast iterative workflow tutorial gives concrete `repeat`, `break!`, `next!`, outputs and iteration state. Useful if chapter wants a precise example of structured runtime control.
- Quix/Klaus Kode article gives a complementary example: prompting Claude to follow a multi-step API/sandbox/deploy sequence was brittle; the author moved orchestration into deterministic code, using Claude Code for discrete agentic steps and deterministic Python/API calls for sequence. This is especially useful for the claim: not every action in an agentic workflow should be an agent action.

Sources:

- Shopify Engineering, “Introducing Roast”: https://shopify.engineering/introducing-roast
- Shopify/roast README: https://github.com/Shopify/roast/blob/main/README.md
- Roast iterative workflows tutorial: https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md
- Roast session resumption example: https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb
- Quix, “Claude Code wouldn’t behave…”: https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it

Решение: integrate now. Use Roast/Quix for workflow-runtime layer, not as full product walkthroughs.

### 1.9. Stripe Minions: useful platform-agent case, but extraction/source caution remains

Use with caution. The official Stripe dev pages were available but the fetched article text was poorly extracted: metadata and related-article snippets were visible, but much article body was not. Search snippets and secondary summaries recover useful facts, but main chapter should avoid relying on non-visible details unless final pass reopens a better source or uses a transcript/page with explicit provenance.

What can be used safely now:

- Official visible metadata: Part 1 published 2026-02-09, Part 2 published 2026-02-19, both by Alistair Gray; related snippet says Minions are Stripe’s homegrown coding agents and responsible for more than a thousand merged PRs per week with human review and no human-written code.
- Stripe benchmark article is fully readable and useful for adjacent evidence: real-world integrations require planning, persistent state management and recovery from failure; benchmark environments included full codebases, databases, scripts, test Stripe API keys, graders, browser/API tests, and a goose-based harness with terminal/browser/Stripe search tools. This source is more XI/evidence but supports IX’s claim that runtime environment matters.
- Secondary sources mention blueprints, isolated devboxes, curated tools, CI retry caps, but these should be treated as secondary unless official article body is accessible.

Sources:

- Stripe Minions Part 1: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- Stripe Minions Part 2: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
- Stripe integration benchmark: https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations
- InfoQ secondary article: https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/

Решение: source-register and cautious integration. Main chapter can use Stripe as a platform-agent direction, but not overbuild exact architecture from inaccessible article text.

## 2. External discovery log

| Source | Status | Use in chapter IX | Notes |
|---|---|---|---|
| OpenAI Codex security/approvals/sandbox docs | integrate now | Sandbox vs approval policy; network off by default; OS sandboxing | Strong primary source |
| OpenAI Codex permissions docs | integrate now | Permission profile scope; other surfaces have separate controls | Very important distinction |
| OpenAI Codex rules docs | integrate now | `allow`/`prompt`/`forbidden`, argv-prefix, shell-wrapper limits | Use briefly |
| OpenAI Codex hooks docs | integrate now | Deterministic lifecycle scripts | Not enough alone for evidence |
| OpenAI Codex MCP docs | integrate now | MCP adds tools/context/instructions | Pair with MCP spec |
| OpenAI Codex subagents docs | integrate selectively | Runtime orchestration / explicit spawning | More VI/advanced orchestration than IX |
| OpenAI Codex worktrees docs | integrate selectively | Local vs worktree, handoff, background work | Avoid UI tour |
| Claude Code security docs | integrate now | Read-only default, permission prompts, sandboxed Bash | Strong cross-vendor primary source |
| Claude Code hooks/settings docs | integrate now | Managed hooks, HTTP allowlists, lifecycle events | Use hooks as trust surface |
| Claude Code MCP docs | integrate now | Connected tools/dbs/APIs allow action, not only pasted context | Pair with MCP spec |
| Claude Code browser docs | integrate now | Browser automation shares login state | Important credentials/session point |
| Claude Code CLI/worktree docs | integrate selectively | Built-in tools vs MCP restrictions; worktree isolation | Useful nuance |
| MCP Security Best Practices | integrate now | Confused deputy, token passthrough, audit/trust boundary | Keep concise |
| MCP Authorization | integrate now | OAuth/user data/actions/audit/enterprise controls | Use for authority boundary |
| MCP Tools spec | integrate now | Tools are external systems and model-controlled; confirmation | Core source |
| MCP Tool annotations | integrate now | Hints are not guarantees | Very strong distinction |
| MCP Client best practices / Apps | source register | Programmatic tool calling needs sandbox; UI from MCP server risk | Optional; avoid overexpansion |
| LangGraph overview/interrupts/HITL | integrate now | Persistence, interrupts, human decisions around tool calls | Do not make chapter LangGraph-centered |
| Temporal workflow/event history/HITL docs | integrate now | Durable waits, signals, event history, replay/recovery | Strong durable runtime source |
| Restate key concepts | integrate now | Journal, side effects, retry/resume | Clean explanation |
| DBOS workflows | integrate selectively | Durable steps, background workflows, workflow ID/idempotency | Useful breadth point |
| HumanLayer “Skill Issue” | integrate now | `model + harness`, MCP/tool bloat, skills/subagents/hooks/back-pressure | Good living anchor, not official spec |
| Ronacher “Agentic Coding Recommendations” | integrate now | Logs/scripts/browser as tools; fast clear tools; `make dev`/`make tail-log` | Strong small-harness example |
| Ronacher “Your MCP Doesn’t Need 30 Tools” | integrate selectively | Code/CLI as better tool surface than large MCP catalog | Use to avoid MCP fetish |
| Sandvault repo | integrate now | Limited macOS user + `sandbox-exec`; shared workspace; caveats | macOS-specific; no universal claim |
| Mike McQuaid Sandboxes and Worktrees | integrate now | Sandvault + worktrees + local review | Great practice story |
| Shopify Roast blog and repo | integrate now | Structured AI workflow, deterministic + agent steps, session replay, cogs | Main workflow-runtime anchor |
| Quix Klaus Kode article | integrate now | Deterministic workflow around Claude Code; avoid gigantic prompt/MCP orchestration | Useful contrast |
| Stripe Minions official Part 1/2 | source register / cautious | Platform-agent direction; thousand+ PRs with human review | Article body poorly extracted; do not overclaim |
| Stripe integration benchmark | integrate selectively | Realistic environment, harness, browser/terminal/search tools, graders | More evidence chapter, but supports IX |
| InfoQ / ByteByteGo / secondary Stripe summaries | defer / secondary only | Architectural details if official source unavailable | Mark as secondary, do not make primary claims |
| MCP vulnerability papers and arXiv work | defer | Security chapter/register; not central to IX | Avoid security rabbit hole |
| Product-market lists / tool roundups | reject | Would turn IX into catalog | Not needed |
| Visual assets/screenshots from sources | defer to visual pass | Some images could help, but rights/layout need separate pass | Do not decide here |

## 3. New working distinctions to carry forward

1. **Sandbox is not approval policy.** Sandbox is an enforcement boundary around what the process can do; approval policy is a decision rule for when the agent must ask to exceed or perform something risky. They can be configured together, but they solve different problems.

2. **Permission profile is not the whole agent surface.** A profile may govern local command execution, while MCP, browser, connectors, cloud environments, approved escalations and hooks each have their own trust and control boundary.

3. **Allowed network is not trusted network.** A domain allowed for network access can still return malicious, misleading or irrelevant content; allowlisting is connectivity control, not semantic trust.

4. **Browser automation is credentialed action.** When the agent uses a browser sharing login state, it is not merely “seeing the UI.” It can operate inside an authenticated session unless the environment prevents that.

5. **Tool descriptions and annotations are not contracts.** MCP hints such as read-only/destructive/idempotent/open-world can help clients and models choose behavior, but they are not guarantees unless backed by a trusted server and enforcement.

6. **Hooks are not one thing.** Deterministic hooks can enforce checks, block commands or surface build errors. LLM/prompt hooks or hooks calling external HTTP endpoints are different: they add another judgment or network boundary and must be governed as part of the runtime.

7. **Observation is not evidence.** A log file, browser view or command output may let the agent steer itself. It becomes evidence for the work lifecycle only when captured, interpreted and made available for review/acceptance.

8. **Durable execution is not durable work state.** LangGraph/Temporal/Restate/DBOS can resume or replay execution, but they do not by themselves know the owner, blocker, semantic claim, accepted evidence, downstream obligation or right-to-continue. That belongs to PWG/evidence/acceptance layers.

9. **Workflow runtime is often partly deterministic by design.** Roast and Quix show a common pattern: let agents handle the uncertain step, but put sequencing, API calls, retries, uploads, deployments and validation in ordinary code or workflow cogs when possible.

10. **Worktree/sandbox produces reviewable work, not accepted work.** Sandvault/worktrees isolate and organize action; review, merge, disclosure and project authority remain separate.

## 4. Candidate structure changes implied by discovery

A good chapter sequence after discovery:

1. Start from a concrete danger: the model can now act, but action without environment boundaries is not engineering work.
2. Define the four layers: execution boundary; tool/observation surface; workflow/durable runtime; platform-agent environment.
3. Explain sandbox/permissions/approvals using Codex and Claude Code.
4. Explain tools as operational surfaces, not context accessories: MCP, browser, logs, CLI, scripts.
5. Explain hooks/skills/subagents only insofar as they change runtime behavior and tool/context pressure.
6. Explain workflow runtimes: durable execution, interrupts, replay, deterministic/agentic step composition.
7. Explain platform agents/devboxes/worktrees with Sandvault/Roast/Stripe as examples.
8. Close with boundaries: runtime does not equal evidence, acceptance or authority.

## 5. Gaps and cautions for later passes

- Need a final primary-source citation pass when drafting the public chapter, because Codex/Claude/MCP docs are current product docs and can change.
- Stripe Minions official article extraction is incomplete. Use only visible official facts or reopen via another route before asserting exact architecture.
- Do not use asset screenshots yet. Visual candidates need separate rights/layout/source pass.
- Do not overuse security research. Security concerns are real, but IX is about execution environment/runtime rights; a full MCP threat model would consume the chapter.
- Keep terminology stable: `sandbox`, `approval policy`, `permission profile`, `hook`, `MCP server`, `workflow runtime`, `durable execution`, `worktree`, `devbox`, `browser session`.
- Preserve boundary with chapter XI: runtime observation and replay are not the same as evidence sufficient for acceptance.
- Preserve boundary with chapter XII: human review and maintainer policy are not generated by sandbox/workflow machinery.
