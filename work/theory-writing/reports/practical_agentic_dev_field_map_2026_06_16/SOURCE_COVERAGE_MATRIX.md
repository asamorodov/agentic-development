# Source Coverage Matrix

Дата обзора: 2026-06-16  
Назначение: показать, какие классы источников были проверены, что они дают теории и как их использовать.

| Класс | Статус | Основные источники | Что даёт | Решение |
|---|---:|---|---|---|
| Early agent loop / tool-use | Достаточно для карты | ReAct, MRKL, Toolformer | Историко-технический мост от LLM к agent loop/tools | Короткая вставка + статья Атласа |
| Planning / reflection / search | Достаточно | Reflexion, Tree of Thoughts | Repair-loop, branching, candidate selection | Короткая вставка + статья Атласа |
| Coding-agent surfaces | Достаточно для типологии | Codex, Claude Code, Copilot, Cursor, Kiro, Jules, OpenHands, Aider, Amp, Junie, Replit | Типология поверхностей действия | Глава VI + Atlas article |
| Repository configuration | Хорошо | AGENTS.md, Claude docs, Kiro docs, GitHub instructions, Amp, Replit, Configuring paper, Instructions-as-Code paper | Instructions-as-Code как новый слой процесса | Расширить главу VI; обязательная статья Атласа |
| Runtime frameworks | Достаточно | LangGraph, LangSmith, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, CrewAI, LlamaIndex Workflows | Runtime graph, tracing, handoff, human-in-loop | Атлас + развести runtime state and project state |
| Open harness / research platforms | Умеренно | SWE-agent, OpenHands, Software-Agent-SDK, Aider | Reproducible experiments, sandbox, logs | Dev-cycle experiments + Atlas B article |
| Interoperability protocols | Достаточно | MCP, A2A, protocol comparison papers | Tools/resources/prompts and agent communication | Расширить главу IX |
| Authorization / identity / security | Достаточно | MCP auth/security, AIP, authenticated workflows, MCP security papers | Protocol is not permission | Расширить главу IX; Atlas article |
| Observability / tracing | Достаточно | LangSmith, OpenAI tracing, LangSmith evaluators | След выполнения, tool calls, spans, evaluators | Глава XI; Atlas article |
| Verification / benchmarks | Умеренно | Agentproof, Agent-Diff, SWE-MERA, SWE-smith, RepoForge | Различить trace/eval/test/state-contract/acceptance | Глава XI |
| Empirical PR studies | Хорошо | Where Do AI Coding Agents Fail?, AIDev, Agentic Refactoring, docs PRs, Instructions-as-Code | Реальная успешность зависит от типа задачи and review/merge process | Главы XII–XIII; Atlas article |
| Enterprise / process fabric | Выборочно | GitHub Agent HQ signals, Microsoft Agent Framework, LangSmith enterprise docs | Agents enter organizational workflow | Monitor + осторожные вставки |
| App-builder / hosted environments | Выборочно | Replit Agent docs/changelog, incident reporting | Quick build surface; production risk | Dev-cycle caution |
| Serving/cost/economics | Почти не раскрыто | Prompt caching / serving material only noted | Future product concern | Monitor |

---

## 1. Early agent loop / tool-use

**Sources**

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [MRKL Systems](https://arxiv.org/abs/2205.00445)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [Reflexion](https://arxiv.org/abs/2303.11366)
- [Tree of Thoughts](https://arxiv.org/abs/2305.10601)

**Use.** Compact genealogy: modern coding agents inherit thought/action/tool-use/reflection/search loop. This explains why agentic development is not just better autocomplete.

**Risk.** Do not overstate direct lineage. Modern products include product, sandbox, permission and PR layers absent from early papers.

## 2. Coding-agent products and surfaces

**Sources**

- [OpenAI Codex CLI](https://developers.openai.com/codex/cli/)
- [Introducing Codex](https://openai.com/index/introducing-codex/)
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/overview)
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent)
- [Cursor docs](https://docs.cursor.com/)
- [Kiro docs](https://kiro.dev/docs/)
- [Jules docs](https://jules.google/docs/)
- [OpenHands](https://github.com/All-Hands-AI/OpenHands)
- [Aider](https://aider.chat/)
- [Amp Manual](https://ampcode.com/manual)
- [Junie docs](https://www.jetbrains.com/help/junie/get-started.html)
- [Replit Agent](https://docs.replit.com/replitai/agent)

**Use.** Build typology, not catalogue. The main analytical difference is action surface: terminal, IDE, cloud PR, app-builder, spec-driven, open harness.

**Risk.** Product docs change quickly. Use dated claims and keep theory conceptual.

## 3. Repository configuration / Instructions-as-Code

**Sources**

- [AGENTS.md](https://agents.md/)
- [Configuring Agentic AI Coding Tools](https://arxiv.org/abs/2602.14690)
- [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449)
- [GitHub repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Kiro steering](https://kiro.dev/docs/kiro/steering/)
- [Kiro specs](https://kiro.dev/docs/kiro/specs/)
- [Kiro hooks](https://kiro.dev/docs/kiro/hooks/)
- [Kiro powers](https://kiro.dev/docs/powers/)

**Use.** Strongest new practical layer. It should alter chapter VI and the Handbook: instructions are operational assets, not prompt decoration.

**Risk.** Instruction-file optimism is unsafe. Presence of instruction files is not enough; structure, scope and repair matter.

## 4. Runtime / frameworks / orchestration

**Sources**

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangSmith observability](https://docs.langchain.com/langsmith/observability-concepts)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/)
- [Google ADK](https://google.github.io/adk-docs/)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)
- [AutoGen human-in-the-loop](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html)
- [CrewAI docs](https://docs.crewai.com/)
- [LlamaIndex Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/)
- [ADK Arena](https://arxiv.org/abs/2606.05548)

**Use.** Explain runtime graph vs project working state. Use these as supporting examples in chapters VII, IX and XI.

**Risk.** Framework comparisons become stale quickly; keep article about boundaries and roles.

## 5. Protocols / security / authorization

**Sources**

- [MCP Introduction](https://modelcontextprotocol.io/introduction)
- [MCP Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [A2A GitHub](https://github.com/a2aproject/A2A)
- [Interoperability Protocols for Agentic AI](https://arxiv.org/abs/2605.04206)
- [Agent Identity Protocol](https://arxiv.org/abs/2603.24775)
- [Authenticated Workflows for LLM Agents](https://arxiv.org/abs/2602.10465)
- [MCP Safety Audit](https://arxiv.org/abs/2504.03767)
- [Breaking the Protocol](https://arxiv.org/abs/2601.17549)
- [SMCP](https://arxiv.org/abs/2602.01129)

**Use.** Chapter IX: protocol is not permission; connector is not governance; agent identity and delegation need explicit treatment.

**Risk.** Security papers are fast-moving. Treat them as risk map, not settled final taxonomy.

## 6. Empirical PR/process studies

**Sources**

- [Where Do AI Coding Agents Fail?](https://arxiv.org/abs/2601.15195)
- [AIDev: Studying AI Coding Agents on GitHub](https://arxiv.org/abs/2602.09185)
- [Agentic Refactoring](https://arxiv.org/abs/2511.04824)
- [How AI Coding Agents Modify Code](https://arxiv.org/abs/2601.17581)
- [How AI Coding Agents Communicate](https://arxiv.org/abs/2602.17084)
- [Who Writes the Docs in SE 3.0?](https://arxiv.org/abs/2601.20171)
- [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449)
- [Agentic Much? Adoption of Coding Agents on GitHub](https://arxiv.org/abs/2601.18341)

**Use.** Chapters XII–XIII: acceptance and maintenance are socio-technical; PR is a process object, not only a code diff.

**Risk.** Very recent evidence; useful, but should not be overgeneralized as stable consensus.
