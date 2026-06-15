# Chapter VI — external discovery log

Статус: P07 выполнен. Источники не только найдены, но и распределены по решению: что встроить, что использовать выборочно, что не трогать без дополнительного добора.

## Принцип отбора

Источник входит в главу только если помогает объяснить проектный интерфейс агента:

1. правила и проектные инструкции;
2. рабочее состояние;
3. маршруты действия и способности;
4. границу между пассивным контекстом и исполнением.

Всё, что ведёт к каталогу IDE, tutorial, security deep dive или повтору главы V, отложено.

## Встроить в основной текст

### Rules layer

- Codex `AGENTS.md`: `https://developers.openai.com/codex/guides/agents-md`
- Claude Code memory / `CLAUDE.md`: `https://code.claude.com/docs/en/memory`
- Kiro Steering: `https://kiro.dev/docs/steering/`
- AGENTS.md standard: `https://agents.md/`

Решение: взять как группу, где видно, что проектные правила становятся agent-facing surface. Главное различие: context is not enforcement; для enforcement нужны hooks/permissions/runtime mechanisms.

### Working state

- Kiro Specs: `https://kiro.dev/docs/specs/`
- BMAD Getting Started: `https://docs.bmad-method.org/tutorials/getting-started/`
- BMAD Project Context: `https://docs.bmad-method.org/how-to/project-context/`
- GSD Core: `https://github.com/open-gsd/gsd-core`
- Spec Kit: `https://github.com/github/spec-kit`

Решение: взять не как сравнение методик, а как примеры того, что состояние работы должно жить в files/status artifacts/tasks/phase notes, а не в памяти текущего чата.

### Action routes

- Claude Code skills: `https://code.claude.com/docs/en/skills`
- Kiro Powers: `https://kiro.dev/docs/powers/`
- Claude Code subagents: `https://code.claude.com/docs/en/sub-agents`
- Kiro subagents: `https://kiro.dev/docs/chat/subagents/`

Решение: использовать как опору для тезиса, что проектный интерфейс должен давать агенту не только знания, но и именованные способы действовать: skills, powers, delegated contexts, restricted tools.

### Boundary with execution

- Kiro Hooks: `https://kiro.dev/docs/hooks/`
- Claude Code Hooks: `https://code.claude.com/docs/en/hooks`
- MCP intro: `https://modelcontextprotocol.io/docs/getting-started/intro`
- MCP tools specification: `https://modelcontextprotocol.io/specification/2025-06-18/server/tools`
- Claude MCP: `https://code.claude.com/docs/en/mcp`
- Kiro MCP: `https://kiro.dev/docs/mcp/`

Решение: использовать компактно. Hooks показывают rule → event. MCP показывает tools/resources/prompts as trusted surface. Детали безопасности и прав — не тема VI.

## Использовать выборочно

- Open GSD product page: `https://opengsd.net/`
  - Использовать только если нужно коротко подкрепить explicit plans / clean execution contexts / verification outside GitHub README.

- BMAD GitHub explanation of project-context: `https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md`
  - Использовать вместо docs-page только если нужен более точный язык про `project-context.md` как implementation guide.

## Не использовать сейчас

- Mark Erikson / OpenCode exact workflow details.
  - Причина: нет отдельной первичной ссылки в P06/P07. Можно оставить как внутренний пример сбоя интерфейса, но без точной публичной продуктовой детализации.

- Mae Capozzi / InstructionsLoaded exact details.
  - Причина: не добран отдельный source pass. Содержательную функцию лучше выразить через проверенные Claude/Kiro/Codex sources.

- HumanLayer / Ronacher / Quix MCP-risk materials.
  - Причина: относятся скорее к IX. Для VI достаточно MCP spec и docs Claude/Kiro.

- Secondary Medium/blog explainers по BMAD/GSD/Spec Kit.
  - Причина: primary docs/repo достаточны, а вторичные источники создадут лишний шум.

## Практическое решение для черновика

Главу можно писать без нового внешнего поиска. На этапе черновика важно не перечислить источники подряд, а встроить их в рассуждение:

1. плохой агентный результат часто начинается не в модели, а в плохом интерфейсе проекта;
2. интерфейс состоит как минимум из правил, состояния и маршрутов действия;
3. правила без state дают дисциплинированную, но слепую работу;
4. state без action routes даёт понимание без надёжного исполнения;
5. action routes без границ дают шум, слишком широкие tools и размытую ответственность;
6. PWG появляется в следующей главе как более сильный способ держать состояние, зависимости и проверочные материалы.

## P21 — дополнительная интеграция story-источников

При интеграции P19/P20 в главе появились точные практические детали из историй. Для них добавлены ссылки рядом с соответствующим материалом, чтобы не оставлять story-фактуру без внешней опоры.

Использованные группы источников:

- Mark Erikson: блоговая статья о workflow и публичный пример конфигурации OpenCode.
- Mae Capozzi: статья о `hub-team` / Claude Orchestrator и `InstructionsLoaded`.
- Matt Pocock: публичный репозиторий skills и страницы/файлы по `/grill-me`, `/handoff`, `/diagnose`, `/tdd`.
- Armin Ronacher: материалы о малой программируемой поверхности и критике больших MCP-каталогов.
- Stripe: официальные статьи Minions Part 1/Part 2 про blueprints, отбор контекста, tools и PR.

Новый поиск не расширял главу новыми механизмами. Он только закрепил уже добавленные story-опоры источниками.

## P22 — перепись после ссылок

Внешние ссылки после P21 оставлены, но язык вокруг них выровнен. Новых источников не добавлялось. Проверочный критерий: ссылка должна поддерживать конкретный механизм, а не превращать абзац в каталог современных агентских инструментов.

## P24 — источники не расширялись

В P24 добавлен собственный синтетический материал главы: диагностические вопросы, условия входа/выхода для маршрутов действия и обслуживание интерфейса агента. Новых внешних источников не требовалось, потому что добавления развивают уже подтверждённые механизмы, а не вводят новый внешний инструмент или факт.

## P30 final discovery status

Финальная проверка не требует нового внешнего discovery. Источники P06/P07 закрыли базовые механизмы, а P21 добавил ссылки для story-фактуры, которая вошла в основной текст. Ни один новый факт P24–P30 не вводит внешнюю сущность без источника: диагностические вопросы, условия входа/выхода маршрутов и требование обслуживания интерфейса являются собственным синтетическим материалом главы.

Ранний список «не использовать сейчас» нужно читать с поправкой P21: Mark Erikson, Mae Capozzi, Matt Pocock, Ronacher и Stripe теперь частично использованы, но только там, где в тексте стоят конкретные публичные ссылки.
