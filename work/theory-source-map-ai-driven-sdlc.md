# Обновлённая карта источников для пересборки теоретической части вокруг AI-driven SDLC

Дата исходной карты: 2026-06-03.
Дата обновления: 2026-06-05.

Эта версия берёт исходную карту течений и добавляет к ней рамочный слой для возможной пересборки теории вокруг **AI-driven / agentic SDLC**. Новые источники встроены не как отдельный хвост, а как рамка и как уточнения к уже существующим разделам.

Важно: карта всё ещё не является финальным оглавлением теории. Это карта первоисточников и их функций. В новой пересборке структурной единицей должен быть не источник и не кейс, а линия части: какой участок жизненного цикла программного изменения она объясняет.

## 0. Рамочные источники для AI-driven / Agentic SDLC

Эти источники добавлены для возможной пересборки теоретической части вокруг жизненного цикла программного изменения. Их задача — не заменить существующие истории и deep cases, а дать системный каркас: AI меняет не только написание кода, но весь контур от намерения и контекста до исполнения, свидетельств, ревью, сопровождения, governance и права завершения.

- DORA / Google Research, `DORA 2025 State of AI-assisted Software Development Report` — AI как усилитель существующей организационной системы: https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
- DORA report page — https://dora.dev/dora-report-2025/
- Bain, `From Pilots to Payoff: Generative AI in Software Development` — value comes from applying AI across the software lifecycle and redesigning processes, not just coding faster: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
- `Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering` — прямой A-SDLC survey / reference architecture; использовать как карту внешней дискуссии, не как готовую теорию: https://arxiv.org/abs/2604.26275
- `Assistance to Autonomy: A Systematic Literature Review of Agentic AI across the Software Development Life Cycle` — SLR по agentic AI across SDLC; особенно важны verifiability, bounded spaces и зрелость поздних фаз: https://arxiv.org/abs/2605.15245
- `The AI-Native Software Development Lifecycle: A Theoretical and Practical New Methodology` — V-Bounce / ранняя AI-native SDLC рамка; использовать осторожно как контраст к слишком фазовой/корпоративной модели: https://arxiv.org/abs/2408.03416

### Как использовать этот раздел в новой теории

- Не строить новую структуру как классическую таблицу `requirements → design → coding → testing → deployment`.
- Использовать SDLC как жизненный цикл изменения: намерение → контекст → делегирование → исполнение → свидетельства → ревью → завершение → сопровождение/обучение среды.
- DORA и Bain — рамочные источники для тезиса, что AI-driven SDLC требует системного redesign, иначе ускорение кода превращается в downstream bottlenecks.
- A-SDLC и SLR — источники внешней терминологии и проверки, но не должны вытеснять нашу собственную линию: контур ответственности, evidence и право завершения.

## 1. Реальные сессии, вмешательства и поведение разработчиков

- `SWE-chat: Coding Agent Interactions From Real Users in the Wild` — реальные сессии, вызовы инструментов, доля агентского кода, дошедшего до коммитов: https://arxiv.org/html/2604.20779v1
- `Programming by Chat` — 11 579 IDE-сессий, интенты сообщений, архетипы сессий, постепенная спецификация: https://arxiv.org/html/2604.00436v1
- `Why AI Agents Still Need You` — наблюдение 19 разработчиков и 33 реальных issues; пошаговая совместная работа успешнее one-shot подхода: https://arxiv.org/html/2506.12347v3
- `How Coding Agents Fail Their Users` — семь форм рассогласования в 20 574 реальных сессиях: https://arxiv.org/html/2605.29442v1
- `How Do Developers Interact with AI?` — модель поведения разработчика через намерение, действие, поддерживающий инструмент и эмоцию: https://arxiv.org/abs/2604.16393

## 2. Изменение работы разработчика и человеческий опыт

- `The Impact of AI Coding Assistants on Software Engineering` — смещение от создания к проверке, supervisory engineering work, парадокс продуктивности и опыта: https://arxiv.org/html/2605.23135v1
- `Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants` — удовлетворённость, modest time savings, долгосрочные риски и developer experience: https://arxiv.org/html/2602.03593v1
- `From Developer Pairs to AI Copilots` — передача знания, принятие предложений AI с меньшей критичностью, напоминание деталей: https://arxiv.org/abs/2506.04785
- `Usage, Effects and Requirements for AI Coding Assistants` — ожидания разработчиков и различие use cases в разных доменах: https://arxiv.org/html/2601.20112v1
- `Human-AI Experience in Integrated Development Environments` — что меняется в месте, где код пишут, проверяют и запускают: https://arxiv.org/html/2503.06195v2

## 3. Агенты как участники проекта, PR и слияние

- `Agentic Software Engineering: Foundational Pillars and a Research Roadmap` — ACE/AEE, engineering activities, BriefingScript, LoopScript, MentorScript, Consultation Request Pack, Merge-Readiness Pack, Version Controlled Resolution: https://arxiv.org/html/2509.06216v2
- `Collaborator or Assistant?` — operational agency и merge governance: https://arxiv.org/html/2605.08017v1
- `Are We All Using Agents the Same Way?` — различие core и peripheral developers при работе с агентскими PR: https://arxiv.org/html/2601.20106v1
- `AIDev` — крупный набор данных агентских PR: https://arxiv.org/abs/2602.09185
- `How AI Coding Agents Modify Code` — форма агентских PR и связь описания с diff: https://arxiv.org/abs/2601.17581
- `AgenticFlict` — конфликты слияния в агентских PR: https://arxiv.org/abs/2604.03551

## 4. Интерфейс агента, среда выполнения и обвязка

- `SWE-agent` — интерфейс агента с компьютером как фактор качества: https://arxiv.org/abs/2405.15793
- `AI Harness Engineering` — обвязка как среда выполнения, обязанности и уровни H0–H3: https://arxiv.org/html/2605.13357v1
- `Agentic Harness Engineering` — самоизменяющаяся обвязка через наблюдаемость и проверяемые изменения: https://arxiv.org/abs/2604.25850
- `Dive into Claude Code` — архитектура Claude Code: режимы прав, сжатие контекста, MCP, plugins, skills, hooks, subagents, session storage: https://arxiv.org/abs/2604.14228
- HumanLayer / 12 Factor Agents — практическая инженерия среды агента: https://github.com/humanlayer/12-factor-agents
- Fowler / Thoughtworks Harness Engineering — пользовательская обвязка coding agents: https://martinfowler.com/articles/harness-engineering.html

### Дополнение 2026-06-05: официальные platform/workflow источники для AI-driven SDLC

- OpenAI, `Introducing Codex` — cloud-based software engineering agent: отдельные sandbox environments, чтение/редактирование файлов, запуск tests/linters/type checkers, terminal logs/test outputs as evidence, AGENTS.md как repo guidance: https://openai.com/index/introducing-codex/
- OpenAI Codex product page — Codex app как command center for agentic coding, worktrees, cloud environments, multi-agent workflows: https://openai.com/codex/
- GitHub Docs, `About GitHub Copilot cloud agent` — repo research, implementation plan, branch changes, PR workflow, ephemeral development environment, hooks, skills, MCP, custom agents, metrics: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- GitHub Well-Architected, `Governing agents in GitHub Enterprise` — trust boundaries, auditability, model/tool access, cost controls, security boundaries for agents as codebase contributors: https://wellarchitected.github.com/library/governance/recommendations/governing-agents/
- Google, `Jules - An Autonomous Coding Agent` — async coding workflow: repository/branch selection, prompt, plan, diff, PR: https://jules.google/
- Google Labs, `Build with Jules, your asynchronous coding agent` — public beta / cloud/GitHub integration context: https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/
- Claude Code Docs, `Extend Claude Code` / features overview — plugins as packaging layer for skills, hooks, subagents, MCP servers: https://code.claude.com/docs/en/features-overview

## 5. Конфигурация, инструкции, навыки и контекстные файлы

- `Configuring Agentic AI Coding Tools` — восемь механизмов настройки, доминирование контекстных файлов, раннее состояние skills/subagents: https://arxiv.org/abs/2602.14690
- `Beyond the Prompt: An Empirical Study of Cursor Rules` — типы правил Cursor и контекст, заданный разработчиками: https://arxiv.org/abs/2512.18925
- `AGENTS.md` — формат инструкций для агентов: https://agents.md/
- `On the Impact of AGENTS.md Files` — влияние `AGENTS.md` на время, токены и качество: https://arxiv.org/html/2601.20404v1
- `Agentic Context Engineering` — коллапс контекста и эволюционирующие рабочие инструкции: https://openreview.net/forum?id=eC4ygDs02R
- `A Comprehensive Survey on Agent Skills` — навыки как переиспользуемые процедурные артефакты: https://arxiv.org/abs/2605.07358
- Anthropic `Agent Skills` — практическая модель навыков: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### Дополнение 2026-06-05: repo-level instructions как SDLC-интерфейс

- OpenAI Codex Docs, `Custom instructions with AGENTS.md` — Codex reads AGENTS.md before work; важен как официальный пример того, что проект получает machine-readable рабочую память/инструкции для агента: https://developers.openai.com/codex/guides/agents-md
- GitHub Copilot cloud agent docs, sections on custom instructions, Copilot Memory, MCP servers, hooks and skills — читать вместе с разделом 4 как platform-level реализацию “проект как интерфейс агента”: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent

## 6. Спецификации, SPDD и артефакты намерения

- `Structured Prompt-Driven Development` — подробный случай SPDD: https://martinfowler.com/articles/structured-prompt-driven/
- OpenSPDD commands and templates — команды `/spdd-story`, `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-api-test`, `/spdd-prompt-update`, `/spdd-sync`: https://github.com/open-spdd/open-spdd
- Fowler / Thoughtworks SDD — spec-first, spec-anchored, spec-as-source: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- `Prompts as Software Engineering Artifacts` — запросы как артефакты разработки: https://arxiv.org/html/2509.17548v1
- GitHub Spec Kit — практический спецификационный набор: https://github.com/github/spec-kit
- Kiro Specs — `requirements.md`, `design.md`, `tasks.md`: https://kiro.dev/docs/specs/
- `Spec Kit Agents` — discovery hooks и validation hooks для Spec Kit: https://arxiv.org/html/2604.05278v1
- `Constitutional Spec-Driven Development` — ограничения безопасности как машинно-читаемая спецификация: https://arxiv.org/html/2602.02584v1
- `Test-Driven Agent Development` — поведение агента как тестируемый артефакт: https://arxiv.org/html/2603.08806v1
- `Mise en Place for Agentic Coding` — подготовка как контекстная дисциплина: https://arxiv.org/abs/2605.05400

## 7. Качество кода, сопровождение и долг

- `Debt Behind the AI Boom` — долг от AI-authored commits в реальных репозиториях: https://arxiv.org/abs/2603.28592
- `To What Extent Does Agent-generated Code Require Maintenance?` — сопровождение AI-generated files после принятия: https://arxiv.org/html/2605.06464v1
- `From Technical Debt to Cognitive and Intent Debt` — технический, когнитивный долг и долг намерения: https://arxiv.org/pdf/2603.22106
- `Agentic Refactoring` — типы и мотивы агентских рефакторингов: https://arxiv.org/abs/2511.04824
- `Do AI Agents Really Improve Code Readability?` — риск ухудшения традиционных метрик читабельности: https://arxiv.org/abs/2603.13723
- `Security Vulnerabilities in AI-Generated Code` — уязвимости в AI-generated code across GitHub repositories: https://arxiv.org/abs/2510.26103

### Дополнение 2026-06-05: агентский долг и lifecycle-tail

- `Governing Technical Debt in Agentic AI Systems` — вводит Agentic Technical Debt как долг prompts, memory, tool schemas, orchestration graphs, control policies, observability routines; Stochastic Tax как постоянную операционную цену удержания вероятностного поведения в границах: https://arxiv.org/abs/2605.29129
- `AI Codebase Maturity Model: From Assisted Coding to Agentic Engineering` — кандидат на отдельную проверку; потенциально полезен для тезиса, что состояние codebase становится условием эффективности агентов: https://arxiv.org/pdf/2604.09388

### Как использовать раздел 7 в AI-driven SDLC пересборке

Раздел не должен быть просто списком дефектов AI-кода. Его функция — показать хвост жизненного цикла: ускорение генерации переносит нагрузку в сопровождение, внутреннюю понятность, review capacity, observability и governance. Источники про долг и сопровождение должны связываться с Part VIII/IX, а не оставаться отдельными предупреждениями.

## 8. Тесты, свидетельства, бенчмарки и последовательное развитие

- `UTBoost` — недостаточность части тестов SWE-Bench: https://arxiv.org/html/2506.09289v1
- `Are Coding Agents Generating Over-Mocked Tests?` — склонность агентов к mock-heavy тестам: https://arxiv.org/abs/2602.00409
- `Testing with AI Agents` — структура и покрытие тестов, созданных агентами: https://arxiv.org/abs/2603.13724
- `Saving SWE-Bench` — реальные запросы разработчиков отличаются от формальных GitHub issues: https://arxiv.org/html/2510.08996v2
- SWE-PolyBench — многоязычная проверка агентов: https://amazon-science.github.io/SWE-PolyBench/
- `SWE-bench Goes Live!` — свежесть задач и загрязнение данных: https://arxiv.org/abs/2505.23419
- SlopCodeBench — деградация при последовательной эволюции кода: https://arxiv.org/abs/2603.24755
- `Beyond Isolated Tasks` — цепочки зависимых изменений: https://arxiv.org/abs/2604.03035
- `Code Review Agent Benchmark` — бенчмарк для агентов ревью: https://arxiv.org/abs/2603.23448

## 9. PR, ревью и коммуникация

- `How AI Coding Agents Communicate` — PR descriptions и реакция людей: https://arxiv.org/abs/2602.17084
- `Human-AI Synergy in Agentic Code Review` — роли человека и AI-агента в ревью: https://arxiv.org/html/2603.15911v1
- `From Industry Claims to Empirical Reality` — ограничения PR, прошедших только автоматическое ревью: https://arxiv.org/html/2604.03196v1
- `AgenticFlict` — конфликты слияния в агентских PR: https://arxiv.org/abs/2604.03551
- Jökull Sólberg — практический Fix / Dismiss / Escalate и сопровождение PR.

## 10. Безопасность, права и цепочка поставки

- `From Preventive to Reactive` — безопасность переносится из написания в ревью: https://arxiv.org/abs/2605.23130
- `Prompt Injection Attacks on Agentic Coding Assistants` — атаки на навыки, инструменты и протокольные экосистемы: https://arxiv.org/abs/2601.17548
- `Breaking the Protocol` — протокольный анализ MCP: https://arxiv.org/abs/2601.17549
- `Are AI-assisted Development Tools Immune to Prompt Injection?` — эмпирический анализ MCP clients: https://arxiv.org/abs/2603.21642
- `Model Context Protocol Threat Modeling` — threat modeling MCP implementations: https://arxiv.org/abs/2603.22489
- MCP Security Best Practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- OpenSSF материалы по securing agentic AI — использовать осторожно как внешний security-фон: https://openssf.org/newsletter/2026/04/21/openssf-newsletter-april-2026/

### Дополнение 2026-06-05: security/governance внутри agentic development lifecycle

- OpenSSF, `Securing Agentic AI in Practice: From OpenSSF Guidance to Real-World Implementation` — практическая security/governance линия для agentic AI: https://openssf.org/blog/2026/03/13/securing-agentic-ai-in-practice-from-openssf-guidance-to-real-world-implementation/
- OpenSSF, `Tech Talk Recap: Securing Agentic AI` — Secure AI/ML-Driven Software Development course, AI/ML Security WG, SAFE-MCP: https://openssf.org/blog/2026/04/08/openssf-tech-talk-recap-securing-agentic-ai/
- Snyk, `The New Security Risks of the Agentic Development Lifecycle` — vendor/security framing: risk enters through what agents use, what agents do and what agents generate; использовать осторожно как язык риска, не как нейтральную академическую основу: https://snyk.io/blog/agentic-development-lifecycle/
- GitHub Well-Architected, `Governing agents in GitHub Enterprise` — дублируется здесь как governance/security источник: https://wellarchitected.github.com/library/governance/recommendations/governing-agents/

### Как использовать раздел 10 в AI-driven SDLC пересборке

Security не должна появляться только после кода. Agentic SDLC требует контролировать входы агента, действия агента, среду выполнения, разрешения, MCP/skills/hooks, provenance, audit trail и generated artifacts. Поэтому раздел 10 должен связываться не только с внешними policy boundaries, но и с Part VI/VIII: среда агента и evidence package.

## 11. Радикальные и периферийные линии

- Gas Town / Beads — граф задач, организация агентов, многоагентный рабочий процесс.
- `Live-SWE-agent` — самоизменяющийся агент; использовать осторожно как крайний случай: https://arxiv.org/abs/2511.13646
- `Engineering Robustness into Personal Agents with the AI Workflow Store` — переиспользуемые рабочие процессы как более надёжная альтернатива импровизированным цепочкам инструментов: https://arxiv.org/html/2605.10907
- `Agentic Artificial Intelligence: Architectures, Taxonomies, and Evaluation` — широкий survey по agent architectures: https://arxiv.org/abs/2601.12560
- `Agentic Software Issue Resolution with Large Language Models` — обзор issue resolution как поля исследований: https://arxiv.org/abs/2512.22256

## 12. Источники для осторожного использования

- Новости о массовом внедрении и изменении профессии — использовать только как фон, не как несущую основу.
- Medium-посты без конкретной механики — использовать только если они дают первичный рабочий пример.
- Страницы конференций без полного текста — помечать как кандидаты, не строить на них основные утверждения.

- McKinsey `The State of AI: Global Survey 2025` — общий enterprise-AI фон; не software-specific enough для несущей роли в теории: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- EPAM `Agentic Development Lifecycle` — соседняя тема про lifecycle создания AI-native systems, где LLM является ядром продуктового поведения; не смешивать автоматически с AI-driven SDLC обычной разработки ПО: https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained
- Snyk ADLC security — полезен, но vendor framing; использовать только рядом с более нейтральными/официальными OpenSSF/GitHub/security источниками.
- News/market posts о “AI has broken SDLC / outages / coding time slashed” — не использовать как несущие источники без первичного отчёта или данных.
