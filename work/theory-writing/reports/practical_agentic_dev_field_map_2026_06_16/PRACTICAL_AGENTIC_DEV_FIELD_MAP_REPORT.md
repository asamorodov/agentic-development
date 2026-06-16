# Практическая карта поля agentic development

Дата обзора: 2026-06-16  
Назначение: рабочая исследовательская карта для теоретического труда об agentic development и для дальнейшей настройки собственного doc-first / package-driven цикла разработки.

## 0. Главный вывод

Обзор не требует пересобирать уже выбранную ось труда. Базовая формула — **агентская разработка меняет жизненный цикл программного изменения, от намерения до принятия, восстановления контекста и передачи работы между сессиями, людьми и агентами** — остаётся правильной.

Но поле показывает четыре недоучтённых слоя.

Во-первых, нужна короткая генеалогия агентской петли: **reasoning + acting**, маршрутизация к инструментам, самонаблюдение, поиск по нескольким вариантам. ReAct, MRKL, Toolformer, Reflexion и Tree of Thoughts не надо превращать в большую историческую главу, но они хорошо объясняют, почему современный coding agent — не просто автодополнение и не просто чат с функциями.

Во-вторых, практическая разработка сместилась от «агент может редактировать код» к **конфигурационной поверхности репозитория**. `AGENTS.md`, `CLAUDE.md`, Cursor Rules, Kiro steering, hooks, skills, subagents, powers, custom agents, workspace instructions — это уже не мелкие настройки. Это слой, через который команда задаёт рабочие границы, стиль изменений, команды проверки, роли агентов, допустимые инструменты, локальную память и ритуалы.

В-третьих, надо сильнее развести **runtime graph / harness / observability** и **project working state**. LangGraph, Google ADK, OpenAI Agents SDK, Microsoft Agent Framework, CrewAI, LlamaIndex Workflows, OpenHands и SWE-agent дают исполняемую обвязку: графы, состояния выполнения, трассировки, handoff, tool calls, human-in-the-loop, песочницы, evals. Но это не то же самое, что Persistent Work Graph как рабочее состояние проекта. Runtime graph отвечает за конкретный прогон. Project working state отвечает за то, что проект уже знает, какие решения приняты, какие долги остались, какие артефакты канонические и что можно безопасно продолжать в другой сессии.

В-четвёртых, эмпирические данные о coding agents добавляют трезвый слой. Исследования GitHub PR показывают: агенты уже проходят в реальные процессы, но успешность зависит от типа задачи. Документация, CI, build и зависимости выглядят устойчивее; performance и bug-fix сложнее. Неуспешные PR часто упираются не только в компиляцию, но и в дубли, слабое взаимодействие с ревьюером, лишние features, stale context и несоответствие проектному ожиданию.

Итоговое решение: **не добавлять новую корневую часть**, но расширить несколько глав и завести отдельную очередь статей Атласа. Самые важные статьи: ранняя агентская петля; Instructions-as-Code; traces/evals/verification; AI-authored PRs in the wild; MCP/A2A security; coding-agent surfaces.

---

## 1. Недооценённые классы материала

### 1.1. Ранние агентские петли: не история ради истории

Ранние papers дают словарь для описания современного agentic development без маркетинговой путаницы.

- **ReAct** формализует чередование reasoning traces and actions. Для разработки это предок обычного цикла: понять задачу, открыть файл, проверить гипотезу, запустить команду, обновить план, внести правку, снова проверить. Источник: [ReAct](https://arxiv.org/abs/2210.03629).
- **MRKL** показывает композицию языковой модели с внешними модулями. Для разработки это предок tool routing: tests, linter, grep, browser, issue tracker, CI, code search, sandbox. Источник: [MRKL Systems](https://arxiv.org/abs/2205.00445).
- **Toolformer** важен как сдвиг от «модель сама всё знает» к «модель умеет вовремя вызвать инструмент». Источник: [Toolformer](https://arxiv.org/abs/2302.04761).
- **Reflexion** вводит словесную обратную связь после ошибки как материал следующей попытки. Это близко к repair-loop: плохой прогон должен обновлять инструкции, tests, verification bar или runbook. Источник: [Reflexion](https://arxiv.org/abs/2303.11366).
- **Tree of Thoughts** важен как предок ветвления и отбора вариантов. Для coding tasks это не значит, что надо буквально строить дерево мыслей, но подтверждает ценность удержания нескольких кандидатов. Источник: [Tree of Thoughts](https://arxiv.org/abs/2305.10601).

**Решение:** короткая вставка во введение или главу II + отдельная статья Атласа.

### 1.2. Coding-agent surfaces: поле стало многоформатным

Современный coding agent — не один интерфейс. В поле одновременно существуют:

- локальный терминальный агент;
- IDE-agent;
- cloud issue-to-PR agent;
- hosted app-builder;
- spec-driven IDE;
- subagent / multi-agent режим;
- open harness для воспроизводимых экспериментов.

Продукты различаются не только моделью, а рабочей ролью: где лежит состояние, кто владеет branch/worktree/container, как задаются инструкции, какие tests запускаются, где появляется diff, кто имеет право читать секреты и внешние API, как устроен approval, что остаётся после прогона.

Ключевые поверхности:

- **OpenAI Codex**: local CLI, cloud software engineering agent, IDE/cloud workflow. Источники: [Codex CLI](https://developers.openai.com/codex/cli/), [Introducing Codex](https://openai.com/index/introducing-codex/), [Codex upgrades](https://openai.com/index/codex-upgrades/).
- **Claude Code**: терминальный/IDE coding agent с богатой конфигурацией: `CLAUDE.md`, hooks, skills, subagents, MCP, plugins, settings. Источники: [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/overview), [Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks), [Skills](https://docs.anthropic.com/en/docs/claude-code/skills), [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents).
- **GitHub Copilot coding agent**: cloud PR surface, где агенту можно назначать issue/task, а результат приходит в branch/PR. Источники: [Copilot coding agent](https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent), [Assign issues to Copilot](https://github.blog/ai-and-ml/github-copilot/assign-issues-to-copilot-from-github-com/).
- **Cursor**: IDE-first surface с agent mode, rules, skills, MCP and teams/enterprise context. Источники: [Cursor docs](https://docs.cursor.com/), [Cursor best practices](https://www.cursor.com/blog/ai-coding-best-practices).
- **Kiro**: spec-driven IDE с steering, specs, hooks, MCP and powers; особенно близок к SPDD-теме. Источники: [Kiro docs](https://kiro.dev/docs/), [Steering](https://kiro.dev/docs/kiro/steering/), [Specs](https://kiro.dev/docs/kiro/specs/), [Hooks](https://kiro.dev/docs/kiro/hooks/), [Powers](https://kiro.dev/docs/powers/).
- **Jules / OpenHands / Aider / Amp / Junie / Replit Agent**: соответственно cloud GitHub agent, open-source harness, terminal pair-programming, repository-instruction agent, JetBrains IDE-agent, hosted app-builder. Источники: [Jules](https://jules.google/docs/), [OpenHands](https://github.com/All-Hands-AI/OpenHands), [Aider](https://aider.chat/), [Amp Manual](https://ampcode.com/manual), [Junie](https://www.jetbrains.com/help/junie/get-started.html), [Replit Agent](https://docs.replit.com/replitai/agent).

**Решение:** не делать product catalogue; сделать типологию action surfaces в главе VI и отдельную статью Атласа.

### 1.3. Repository configuration: инструкции становятся кодом процесса

Самая важная практическая недооценка — repository-native instruction layer.

`AGENTS.md` позиционируется как открытый формат инструкций для coding agents, своего рода README for agents. GitHub Copilot coding agent поддерживает `AGENTS.md`; OpenAI Codex и Amp также используют repository instructions; Claude Code имеет `CLAUDE.md`, skills, subagents and hooks; Cursor использует Rules/Skills; Kiro — steering/specs/hooks/powers; Replit — workspace instructions and skills. Источники: [AGENTS.md](https://agents.md/), [GitHub repository instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot), [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview), [Kiro steering](https://kiro.dev/docs/kiro/steering/), [Amp Manual](https://ampcode.com/manual), [Replit customization](https://docs.replit.com/replitai/customization).

Исследование [Configuring Agentic AI Coding Tools](https://arxiv.org/abs/2602.14690) показывает, что конфигурационные механизмы уже стали реальным слоем практики: авторы анализируют Claude Code, GitHub Copilot, Cursor, Gemini and Codex, а также 2,926 GitHub repositories. Важные выводы: context files dominate; `AGENTS.md` emerges as interoperable standard; advanced mechanisms such as Skills and Subagents are still shallowly adopted.

Работа [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449) особенно важна для нашего процесса: она изучает 15,549 agentic PRs and показывает, что instruction files сами по себе не дают гарантированного улучшения; эффект зависит от качества, структуры and maintenance. Это прямо поддерживает идею: инструкции надо писать, ревьюить и чинить как процессный код.

**Решение:** расширить главу VI; добавить статью Атласа “Instructions-as-Code: AGENTS.md, CLAUDE.md, steering, skills, subagents, hooks”.

### 1.4. Runtime frameworks: полезны, но не заменяют методологию разработки

LangGraph, LangSmith, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, CrewAI и LlamaIndex Workflows образуют runtime/orchestration layer.

- **LangGraph**: durable execution, streaming, human-in-the-loop, state management. Источник: [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview).
- **LangSmith**: traces, metrics, debugging, evaluators. Источник: [LangSmith observability](https://docs.langchain.com/langsmith/observability-concepts).
- **OpenAI Agents SDK**: agents, tools, handoffs, sessions, guardrails, tracing. Источники: [Agents SDK](https://openai.github.io/openai-agents-python/), [Tracing](https://openai.github.io/openai-agents-python/tracing/).
- **Google ADK**: framework for agent applications with tools, integrations and evaluation. Источники: [ADK docs](https://google.github.io/adk-docs/), [ADK announcement](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/).
- **Microsoft Agent Framework / AutoGen / Semantic Kernel line**: enterprise agent framework with state, telemetry, workflows, human-in-loop patterns. Источники: [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/), [AutoGen human-in-the-loop](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html).
- **CrewAI / LlamaIndex Workflows**: crews, flows, memory, knowledge, event-driven workflows. Источники: [CrewAI](https://docs.crewai.com/), [LlamaIndex Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/).

Главная опасность — принять runtime framework за зрелую методологию разработки. Framework может дать graph, tool execution, tracing, retry, memory object, human approval. Но он не решает сам: как формулировать change intent; как держать project state между сессиями; как связывать specs, ADR, tests, PR and release notes; как отличать рабочую гипотезу от принятого решения; как чинить instructions after failure.

**Решение:** в теории явно закрепить различие: runtime state is not project state; agent trace is not project memory; workflow graph is not SDLC.

### 1.5. Observability, evals, traces: след выполнения не равен доказательству

LangSmith and OpenAI Agents SDK дают traces, spans, model calls, tool calls, handoffs, guardrail events and evaluators. Это помогает восстановить, что делала система. Но trace не доказывает корректность результата.

Надо различать:

- trace: восстановление хода выполнения;
- run log: человеческий журнал действий, файлов, команд and результатов;
- eval: оценка поведения системы на наборе случаев;
- benchmark: внешняя сравнительная мера;
- test: проектная проверка конкретного изменения;
- static verification: проверка свойств workflow graph;
- state-diff contract: проверка ожидаемого изменения состояния;
- acceptance: решение принять результат в project state.

Новые источники полезны как попытки укрепить слой проверки: [Agentproof](https://arxiv.org/abs/2603.20356) проверяет workflow graph properties; [Agent-Diff](https://arxiv.org/html/2602.11224v1) использует state-difference contracts for enterprise API tasks; [SWE-MERA](https://arxiv.org/abs/2507.11059), [SWE-smith](https://arxiv.org/abs/2504.21798), [RepoForge](https://arxiv.org/html/2508.01550v1) развивают benchmark/data-generation layer for software engineering agents.

**Решение:** глава XI должна строиться вокруг layered evidence, not around one gate.

### 1.6. MCP, A2A, identity and authorization: protocol is not permission

MCP and A2A нельзя обсуждать как «агентам дали инструменты» или «агенты смогут общаться». Практически важнее: протокол увеличивает площадь действия и требует модели прав, identity, delegation, consent, secrets, audit and revocation.

MCP описывает open standard для связи AI applications with external systems through tools/resources/prompts. Официальные материалы по authorization говорят про OAuth 2.1, consent, audit and rate limiting for user data/admin/enterprise cases. Источники: [MCP Introduction](https://modelcontextprotocol.io/introduction), [MCP Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization), [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices).

A2A от Google описывается как protocol for agents to communicate, exchange information and coordinate actions across enterprise applications. Источники: [A2A announcement](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), [A2A GitHub](https://github.com/a2aproject/A2A).

Сравнительные и security papers важны как risk map: [Interoperability Protocols for Agentic AI](https://arxiv.org/abs/2605.04206), [Agent Identity Protocol](https://arxiv.org/abs/2603.24775), [Authenticated Workflows for LLM Agents](https://arxiv.org/abs/2602.10465), [MCP Safety Audit](https://arxiv.org/abs/2504.03767), [Breaking the Protocol](https://arxiv.org/abs/2601.17549), [SMCP](https://arxiv.org/abs/2602.01129).

**Решение:** расширить главу IX. Формула: protocol opens a channel; it does not create a right to act.

### 1.7. Empirical PR evidence: агентский PR — социально-технический объект

Эмпирические studies дают reality check.

[Where Do AI Coding Agents Fail?](https://arxiv.org/abs/2601.15195) анализирует 33k agent-authored PRs and показывает: documentation, CI and build updates have highest merge success; performance and bug-fix tasks perform worst; not-merged PRs often involve larger changes, CI/CD issues, lack of reviewer engagement, duplicate PRs, unwanted features and misalignment.

[AIDev](https://arxiv.org/abs/2602.09185) aggregates 932,791 agentic PRs produced by five agents across 116,211 repositories, with curated subset of 33,596 PRs. Это делает поле достаточно большим для исследования, а не только для анекдотов.

[Agentic Refactoring](https://arxiv.org/abs/2511.04824) показывает, что agentic refactoring часто тяготеет к low-level consistency-oriented edits. [Who Writes the Docs in SE 3.0?](https://arxiv.org/abs/2601.20171) показывает значительную роль агентов в documentation PRs и поднимает вопрос качества human review. [How AI Coding Agents Modify Code](https://arxiv.org/abs/2601.17581) and [How AI Coding Agents Communicate](https://arxiv.org/abs/2602.17084) дают материал о code changes and PR descriptions/reviewer responses. [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449) связывает PR outcomes with instruction files.

**Решение:** главы XII–XIII должны говорить не только о human review output, а о PR as acceptance object: agent can produce branch/diff/tests/docs, but project still decides whether this change enters working state.

---

## 2. Стратегическая позиция

Теорию лучше держать как layered stack:

1. Agent loop lineage — ReAct, MRKL, Toolformer, Reflexion, ToT.
2. Coding-agent surfaces — terminal, IDE, cloud PR, hosted app-builder, spec-driven IDE, open harness.
3. Repository instructions — AGENTS.md, CLAUDE.md, rules, steering, skills, hooks, subagents, powers.
4. Runtime/orchestration — LangGraph, ADK, OpenAI Agents SDK, Microsoft Agent Framework, CrewAI, LlamaIndex Workflows.
5. Protocols and rights — MCP, A2A, identity, OAuth, secrets, sandbox, approvals, audit.
6. Observability and verification — traces, evals, benchmarks, static verification, state-diff contracts, project tests.
7. PR/process reality — review, merge governance, docs, CI, duplication, stale work, acceptance.
8. Project memory — persistent working state, ADR/spec/ledger/provenance, repair loops, handoff.

Сильная позиция автора остаётся в слоях 3, 6, 7 and 8: не просто «агенты могут действовать», а «проекту нужна дисциплина, делающая агентское действие продолжимым, проверяемым, восстанавливаемым и принимаемым».

---

## 3. Что не делать

1. Не превращать труд в каталог agent frameworks.
2. Не смешивать agent runtime and development methodology.
3. Не считать `AGENTS.md` универсальным решением: quality and maintenance matter.
4. Не принимать trace за доказательство корректности.
5. Не считать protocol равным permission.
6. Не романтизировать multi-agent orchestration: параллельность умножает acceptance work.
7. Не переносить app-builder optimism into production without strict isolation.
