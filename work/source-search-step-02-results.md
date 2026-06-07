# Шаг 02. Результаты поиска — Платформы и workflow-примитивы AI-driven SDLC

## Акцент

Искать не общие статьи, а официальные документы инструментов, где lifecycle уже выражен в продуктовых примитивах: repo task, plan, sandbox, branch/PR, logs, tests, custom instructions, MCP, hooks, skills, governance.

## Найденные источники и решение

### OpenAI, Introducing Codex

- URL: https://openai.com/index/introducing-codex/
- Решение: `include`
- Пояснение: Официальный источник: cloud-based SWE agent, parallel tasks, isolated environments, terminal logs/test outputs as evidence, AGENTS.md guidance. Отлично ложится на lifecycle: task → sandbox → commands/tests → evidence → review.

### OpenAI Codex product page

- URL: https://openai.com/codex/
- Решение: `include`
- Пояснение: Дополнительный продуктовый источник о multi-agent workflows, worktrees, cloud environments. Использовать как фон к Codex-process и platform layer.

### OpenAI Codex docs: Custom instructions with AGENTS.md

- URL: https://developers.openai.com/codex/guides/agents-md
- Решение: `include`
- Пояснение: Уточняет AGENTS.md как repo-level guidance для Codex; важен для слоя “проект как интерфейс агента”.

### GitHub Docs: About Copilot cloud agent

- URL: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- Решение: `include`
- Пояснение: Официальный lifecycle-источник: research repo → plan → branch changes → logs/tests → PR/iteration; custom agents, MCP, hooks, skills, metrics.

### GitHub Well-Architected: Governing agents in GitHub Enterprise

- URL: https://wellarchitected.github.com/library/governance/recommendations/governing-agents/
- Решение: `include`
- Пояснение: Сильный governance bridge: trust boundaries, auditability, cost/security controls, model/tool access. Очень полезен для “право завершения / организационная граница”.

### Google Jules product page

- URL: https://jules.google/
- Решение: `include`
- Пояснение: Официальный пример async agent workflow: repo/branch → prompt → plan → diff → PR. Хорош как короткий contrast/platform example.

### Google Labs blog: Build with Jules

- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/
- Решение: `candidate`
- Пояснение: Поясняет public beta, secure cloud environment, GitHub integration. Можно использовать, если нужен официальный запуск/контекст.

### Claude Code Docs: Extend Claude Code / features overview

- URL: https://code.claude.com/docs/en/features-overview
- Решение: `include`
- Пояснение: Официальный источник по plugins как packaging layer для skills/hooks/subagents/MCP servers. Включить в среду/обвязку агента.

### Dive into Claude Code: The Design Space of Today’s and Future AI Agent Systems

- URL: https://arxiv.org/abs/2604.14228
- Решение: `already_or_include`
- Пояснение: Уже был в карте, но теперь его надо читать как архитектурное подтверждение lifecycle primitives: loop, permissions, compaction, extensibility, session storage.

## Итог шага


Шаг подтвердил, что современные инструменты уже материализуют lifecycle-примитивы: изолированные среды, план, branch/PR, logs/tests/evidence, repo instructions, MCP/hooks/skills, governance. Это не просто набор IDE-фич.
