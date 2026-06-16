# Atlas Article Queue

Дата обзора: 2026-06-16  
Назначение: очередь возможных статей Атласа после обзора practical agentic development field map.

## Priority A — add soon

### A1. Instructions-as-Code: AGENTS.md, CLAUDE.md, steering, skills, subagents, hooks

**Status:** highest priority new article.

**Task:** описать repository-native instruction layer как процессный артефакт: scope, versioning, review, repair, conflict, tests, allowed tools.

**Must cover:** AGENTS.md, Claude Code `CLAUDE.md`/hooks/skills/subagents, Kiro steering/specs/hooks/powers, GitHub custom instructions, Cursor Rules/Skills, Amp manual, Replit workspace instructions.

**Why it matters:** самый сильный прямой вклад в главу VI и пользовательский package-driven workflow.

**Theory links:** Chapter VI, chapter IX, chapter XIII, Handbook.

**Sources:** [AGENTS.md](https://agents.md/), [Configuring Agentic AI Coding Tools](https://arxiv.org/abs/2602.14690), [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449), [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview), [Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks), [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills), [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents), [Kiro steering](https://kiro.dev/docs/kiro/steering/), [Kiro specs](https://kiro.dev/docs/kiro/specs/), [GitHub repository instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

### A2. Agent traces are not proof: observability, evals, state-diff and verification

**Status:** new article.

**Task:** различить trace, run log, eval, benchmark, test, state contract, static verification and acceptance.

**Must cover:** LangSmith, OpenAI Agents SDK tracing, Agentproof, Agent-Diff, SWE-MERA, SWE-smith, RepoForge.

**Why it matters:** напрямую кормит главу XI.

**Theory links:** Chapter II, XI, XII, provenance discipline.

**Sources:** [LangSmith observability](https://docs.langchain.com/langsmith/observability-concepts), [OpenAI Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/), [Agentproof](https://arxiv.org/abs/2603.20356), [Agent-Diff](https://arxiv.org/html/2602.11224v1), [SWE-MERA](https://arxiv.org/abs/2507.11059), [SWE-smith](https://arxiv.org/abs/2504.21798), [RepoForge](https://arxiv.org/html/2508.01550v1).

### A3. AI-authored PRs in the wild: что проходит, что не проходит и почему

**Status:** new article.

**Task:** synthesize empirical studies of agent-authored PRs, adoption, failure, refactoring, testing and documentation.

**Must cover:** task-type success differences; human merge governance; reviewer engagement; stale/duplicate work; documentation and CI strengths; bug-fix/performance weaknesses; instruction-file effects.

**Why it matters:** reality check for chapters XII–XIII.

**Theory links:** Chapter X, XII, XIII.

**Sources:** [Where Do AI Coding Agents Fail?](https://arxiv.org/abs/2601.15195), [AIDev](https://arxiv.org/abs/2602.09185), [Agentic Refactoring](https://arxiv.org/abs/2511.04824), [How AI Coding Agents Modify Code](https://arxiv.org/abs/2601.17581), [How AI Coding Agents Communicate](https://arxiv.org/abs/2602.17084), [Who Writes the Docs in SE 3.0?](https://arxiv.org/abs/2601.20171), [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449), [Agentic Much?](https://arxiv.org/abs/2601.18341).

### A4. MCP/A2A security and authorization: protocol is not permission

**Status:** new article.

**Task:** explain protocol/action/identity/authorization boundaries for agentic development.

**Must cover:** MCP tools/resources/prompts; OAuth and consent; A2A agent communication; identity/delegation; tool poisoning; prompt injection; secrets; audit/revocation.

**Why it matters:** strengthens chapter IX and prevents naive connector optimism.

**Theory links:** Chapter IX, runtime rights, protected profiles.

**Sources:** [MCP Introduction](https://modelcontextprotocol.io/introduction), [MCP Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization), [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), [A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), [Interoperability Protocols for Agentic AI](https://arxiv.org/abs/2605.04206), [Agent Identity Protocol](https://arxiv.org/abs/2603.24775), [Authenticated Workflows](https://arxiv.org/abs/2602.10465), [MCP Safety Audit](https://arxiv.org/abs/2504.03767).

### A5. Coding-agent surfaces: terminal, IDE, cloud PR, app-builder, spec-driven IDE

**Status:** new article.

**Task:** classify modern coding-agent products by action surface and process role, not by vendor ranking.

**Must cover:** Codex CLI/cloud, Claude Code, GitHub Copilot coding agent, Cursor, Kiro, Jules, OpenHands, Aider, Amp, Junie, Replit Agent.

**Why it matters:** gives practical taxonomy for mode selection and Handbook.

**Theory links:** Chapter VI, VIII, IX, conclusion.

### A6. ReAct → Toolformer → Reflexion: ранняя агентская петля как генеалогия разработки

**Status:** new article.

**Task:** explain early loop/tool/reflection/search papers as prehistory of modern coding agents, without making them the whole theory.

**Must cover:** ReAct, MRKL, Toolformer, Reflexion, Tree of Thoughts.

**Why it matters:** gives compact bridge for introduction and chapter II.

**Theory links:** Introduction, chapter II, chapter XI.

**Sources:** [ReAct](https://arxiv.org/abs/2210.03629), [MRKL](https://arxiv.org/abs/2205.00445), [Toolformer](https://arxiv.org/abs/2302.04761), [Reflexion](https://arxiv.org/abs/2303.11366), [Tree of Thoughts](https://arxiv.org/abs/2305.10601).

### A7. Kiro, specs and the productization of spec-driven agentic development

**Status:** new or extension of SPDD Atlas article.

**Task:** compare Kiro’s requirements/design/tasks, steering, hooks and powers with SPDD without reducing SPDD to one product.

**Why it matters:** Kiro is the most directly relevant contemporary product case for spec-driven development.

**Theory links:** Chapter IV, VI, Handbook.

---

## Priority B — valuable, but after A queue

### B1. LangGraph / ADK / OpenAI Agents SDK / Microsoft Agent Framework: runtime graph is not SDLC

**Task:** compare runtime/orchestration frameworks and draw the boundary between execution graph, workflow state and project state.

**Why B, not A:** important, but less immediately actionable than Instructions-as-Code and verification.

### B2. Subagents and parallel work: Claude Code, Copilot, Replit, OpenHands

**Task:** examine subagents, parallel sessions, cloud tasks and multi-agent roles as practical orchestration, with a warning about review burden.

**Why B:** can be folded partly into chapter X and A5 first.

### B3. OpenHands / SWE-agent / Aider as harness labs

**Task:** use open-source tools as laboratories for reproducible coding-agent experiments, not necessarily as production recommendations.

**Why B:** useful for the user’s own dev-cycle experiments.

### B4. Agentic documentation and docs quality

**Task:** focus on documentation PRs, agent-created docs, docs review and maintenance.

**Why B:** likely useful for site/theory workflow, but can wait until chapter XIII.

### B5. Enterprise process fabric

**Task:** discuss how organizations integrate agents into issue trackers, PRs, observability and governance.

**Why B:** field is moving fast; better monitor before central claims.

---

## Priority C — monitor

### C1. Workflow serving, cost, caching and inference economics

Important for product strategy, less required for current theoretical chapters.

### C2. Agent identity protocols beyond current MCP/A2A security

Track AIP, SMCP, authenticated workflows and related standards.

### C3. Benchmark/data-generation ecosystem

SWE-MERA, SWE-smith, RepoForge and related benchmarks should feed chapter XI but not dominate it.

---

## Recommended order of work

1. Instructions-as-Code.
2. Agent traces are not proof.
3. AI-authored PRs in the wild.
4. MCP/A2A security and authorization.
5. Coding-agent surfaces.
6. ReAct → Toolformer → Reflexion.
7. Kiro/spec-driven productization.
