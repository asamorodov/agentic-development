# IX. Source register

### Внутренние источники и рабочие материалы

| Источник | Как использован в главе IX | Статус |
|---|---|---|
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Задал позицию главы: execution environment, runtime rights, tools, permissions, continuation, след исполнения. | Использован как структурная рамка. |
| `work/theory-writing/fragments/00_spine_map.md` | Поддержал общую lifecycle-ось: изменение движется от намерения к проверке, принятию и устойчивому состоянию. | Использован как фон, без прямого пересказа. |
| `work/theory-writing/fragments/A6_execution_environment_distinctions.md` | Дал различение слоёв среды исполнения: место действия, инструменты/наблюдение, runtime/workflow, platform agent. | Сильно использован, но в P14 переписан в собственную ось главы. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Дал финальную границу: runtime state не равен work state; след запуска должен быть связан с claim/gate/PWG. | Сильно использован в финальных разделах. |
| `work/theory-writing/fragments/A6_figure_candidates.md` | Дал исходные решения по визуальному слою: Sandvault, HumanLayer, runtime/PWG. | Использован в P12; в P14 inline-фигуры не вставлялись. |
| `work/theory-writing/fragments/C4_figure_candidates.md` | Дал решения по trace→PWG and durable execution vs work graph. | Использован в P12 and final bridge. |
| `content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md` | Anchor для browser loop, allow/deny, запрет опасных команд and bypass-through-script failure. | Использован как story anchor. |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Anchor для harness engineering, tool surface pressure, skills/progressive disclosure, subagents/context firewall. | Использован как story anchor. |
| `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md` | Anchor для Sandvault, sandboxed user, worktrees, controlled transfer. | Использован как story anchor. |
| `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md` | Anchor для local harness: scripts, logs, browser, email stdout, code/CLI instead of everything-as-MCP. | Использован как story anchor. |
| `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` | Anchor для platform agents, Minions, realistic test environments and steering experiments. | Использован как story anchor. |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | Anchor для workflow runtime, Roast, Boba, cogs, session resume/forking. | Использован как story anchor. |
| `work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md` | Поддержал Ronacher/Pi фактуру. | Использован как secondary internal source. |
| `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md` | Поддержал Roast фактуру. | Использован как secondary internal source. |
| `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md` | Поддержал Stripe фактуру и осторожность с метриками. | Использован как secondary internal source. |

### Внешние источники, фактически вошедшие в P14

| Источник | URL | Использование в главе |
|---|---|---|
| OpenAI Codex sandboxing | `https://developers.openai.com/codex/concepts/sandboxing` | Разведение sandbox and approval policy; рабочая область, network, spawned commands. |
| OpenAI Codex Agent approvals & security | `https://developers.openai.com/codex/agent-approvals-security` | Default local network off, OS-enforced sandbox, security framing. |
| OpenAI Codex permissions | `https://developers.openai.com/codex/permissions` | Permission profiles, `:read-only`, `:workspace`, `:danger-full-access`; separate controls for app connectors, MCP, browser, cloud, approved escalations; network trust nuance. |
| OpenAI Codex Auto-review | `https://developers.openai.com/codex/concepts/sandboxing/auto-review` | Reviewer swap not permission grant; denial should not trigger workaround/circumvention. |
| OpenAI Codex rules | `https://developers.openai.com/codex/rules` | `prefix_rule`, allow/prompt/forbid, most restrictive wins, shell splitting. |
| OpenAI Codex MCP | `https://developers.openai.com/codex/mcp` | MCP as external tools/context surface; STDIO/HTTP, auth, server instructions. |
| OpenAI Codex worktrees | `https://developers.openai.com/codex/app/worktrees` | Multiple independent tasks in background worktrees, handoff. |
| Claude Code Security | `https://code.claude.com/docs/en/security` | Read-only default, explicit permissions, MCP trust caveat. |
| Claude Code permission modes | `https://code.claude.com/docs/en/permission-modes` | `acceptEdits`, `plan`, `auto`, `bypassPermissions`; review boundary. |
| Claude Code Chrome extension | `https://code.claude.com/docs/en/chrome` | Browser/devtools as observation and action surface; login-state risk. |
| Claude Code hooks | `https://code.claude.com/docs/en/hooks` | Hooks events and handler types: shell, HTTP, prompts, lifecycle. |
| Kiro hooks | `https://kiro.dev/docs/hooks/` | IDE hook pattern: events, predefined agent prompts or shell commands. |
| MCP tools specification | `https://modelcontextprotocol.io/specification/draft/server/tools` | Tools as model-controlled capabilities for external systems. |
| MCP Authorization specification | `https://modelcontextprotocol.io/specification/draft/basic/authorization` | Authorization/trust boundary. |
| MCP Security best practices | `https://modelcontextprotocol.io/specification/draft/basic/security_best_practices` | Confused deputy, security framing, trust concerns. |
| Arvid Kahl, “How to actually use Claude Code to build serious software” | `https://thebootstrappedfounder.com/how-to-actually-use-claude-code-to-build-serious-software/` | allow/deny, browser loop, command bypass story. |
| HumanLayer, “Skill Issue” | `https://www.humanlayer.dev/blog/skill-issue` | Harness engineering, tools, skills, subagents/context firewall. |
| HumanLayer, “Skill Issue: Harness Engineering for Coding Agents” | `https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents` | Tool overload, harness as agent environment. |
| Mike McQuaid, “Sandboxed Agent Worktrees” | `https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/` | Sandvault, sandboxed user, worktrees, controlled transfer. |
| Sandvault repository | `https://github.com/webcoyote/sandvault` | Commands and implementation anchor for Sandvault. |
| Fowler, “Harness engineering for coding agents” | `https://martinfowler.com/articles/harness-engineering.html` | guides/feedforward, sensors/feedback, LLM-oriented feedback. |
| Armin Ronacher, “Agentic Coding” | `https://lucumr.pocoo.org/2025/6/12/agentic-coding/` | Local harness, scripts/logs/browser/runtime details. |
| Armin Ronacher, “Code MCPs” | `https://lucumr.pocoo.org/2025/8/18/code-mcps/` | Code/CLI vs MCP; local tool surface. |
| Pi repository | `https://github.com/earendil-works/pi` | Minimal local harness anchor. |
| Shopify Engineering, “Introducing Roast” | `https://shopify.engineering/introducing-roast` | Roast, Boba, deterministic work + bounded agent + checks. |
| Shopify Roast repository | `https://github.com/Shopify/roast` | `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call`, session resume/forking. |
| Daniel Doubrovkine, Roast walkthrough | `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html` | Ordinary runtime facts: API key, model routing, workflow edits. |
| LangGraph durable execution | `https://langchain-ai.github.io/langgraph/concepts/durable_execution/` | Persistence, interrupts, HITL around tool calls. |
| Temporal documentation | `https://docs.temporal.io/workflows` | Durable workflows, event history, signals/timers/replay. |
| Restate documentation | `https://docs.restate.dev/` | Journaled steps/side effects and replay/skip completed work. |
| DBOS workflow tutorial | `https://docs.dbos.dev/python/tutorials/workflow-tutorial` | Workflow IDs, resuming from last completed step. |
| Stripe integration benchmark | `https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations` | Realistic environments, test Stripe API keys, deterministic graders. |
| Stripe steering experiments | `https://stripe.dev/blog/ai-steering-experiments` | “Don’t whisper”: put guidance on execution path. |
| Homebrew CONTRIBUTING | `https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md` | AI-assisted PR policy and contributor/review responsibility. |

### Источники, использованные в discovery, но не вошедшие явно в P14

| Источник / семейство | Статус | Причина |
|---|---|---|
| OpenAI Codex dashboard / terminal logs / citations UI assets | Использованы только для P12 visual layer. | P14 не вставлял inline-фигуры. |
| Stripe Minions Part 1 / Part 2 / Sessions 2026 | Использованы как фон story anchor. | P14 предпочёл Stripe integration benchmark and steering experiments; Minions PR-counts deliberately not foregrounded. |
| Quix / Klaus Kode primary source | Использован по discovery summary, но без прямой ссылки в P14. | Нужен source audit: если Quix paragraph останется, лучше добавить точный первоисточник или вынести пример в companion/open question. |
| GSD / BMAD / Gas Town atlas | Использованы только как границы соседних глав, не как фактура P14. | Не добавлять их в chapter body без необходимости, чтобы IX не потеряла собственную ось. |
