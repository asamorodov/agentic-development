# A1 plan — second natural Russian rewrite and terminology update

Date: 2026-06-16

## What changed

Rewrote `work/atlas/target-group-plans/agent_facing_repository_interface_ATLAS_V2_ARTICLE_TARGET_GROUP_PLAN.md` one more time in a more natural Russian working style.

The pass preserved the accepted content of the plan:

- A1 remains a public Atlas V2 article about the repository as an interface for agents.
- The plan still includes the same mini-dossiers.
- Chapter VI seeds for skills, MCP, subagents and hooks remain strong source material, not weak drafts.
- The checkpoint after mini-dossiers remains in the plan.
- The article should not become a catalogue of instruction files or a setup template.

## Language decisions

The pass used the existing terminology rules. Where the plan needed more precise terms for A1, the existing terminology file was extended with a dedicated Atlas V2/A1 section.

Added or clarified terms include:

- `agent-facing repository interface` → `репозиторий как интерфейс для агента` / `интерфейс проекта для агента`;
- `repository-level context file` → `файл проектного контекста на уровне репозитория` / `постоянная инструкция репозитория`;
- `tool-specific instruction` → `инструкция конкретного инструмента`;
- `scope` → `область действия`;
- `instruction noise` → `шум от лишних инструкций`;
- `instruction repair` → `исправление и поддержка инструкций`;
- `task-specific instruction` → `временная инструкция для конкретной задачи`.

The pass avoided mechanical replacement where it would damage file names, URLs, product names or accepted tool terms.

## Files changed

```text
work/atlas/target-group-plans/agent_facing_repository_interface_ATLAS_V2_ARTICLE_TARGET_GROUP_PLAN.md
protocols/rules/terminology-and-translation.md
work/atlas/plans/reports/agent_facing_repository_interface_A1_NATURAL_RUSSIAN_REWRITE_2_REPORT_2026_06_16.md
```

No chapter text, Atlas article text, or executor package was changed.
