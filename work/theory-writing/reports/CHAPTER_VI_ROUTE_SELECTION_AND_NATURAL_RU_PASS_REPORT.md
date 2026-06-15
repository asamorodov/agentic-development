# Chapter VI route selection and natural Russian pass report

Date: 2026-06-15

## Baseline

The overlay is built cumulatively relative to the full repository snapshot uploaded by the user in the current chat as `git.zip`.

The work was performed on the integrated filesystem chapter file:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

## User request

1. Expand `Маршруты действия: как проект выбирает способ работы` slightly because removing it would be structurally inconvenient, while the current text was too short.
2. Run a natural Russian rewrite over the whole chapter.

## Changes to Chapter VI

### Route-selection section

The section `Маршруты действия: как проект выбирает способ работы` was expanded from a short transition into a real argument node.

Added functions:

- route-selection error / ошибка выбора маршрута as a distinct class of failure;
- criteria for choosing between skill, MCP, subagent and hook;
- the idea that routes can be combined in one workflow;
- the requirement that a route leaves a trace in working state: what was done, which form of work was chosen, which checks passed, what remains constrained and where human acceptance is needed.

The larger mechanism sections remain top-level chapter sections:

```text
## Skills: повторяемые процедуры как часть проекта
## MCP-сервер: управляемый внешний интерфейс
## Subagents: разные исполнители для разных частей задачи
## Где инструкция становится вмешательством
```

### Natural Russian pass

The whole chapter was reviewed and rewritten for more natural Russian without removing technical content or links.

Representative fixes:

- softened protocol-like phrasing in the introduction;
- replaced self-referential or draft-facing wording;
- fixed awkward Russian and typos such as `файл статусаы` and `приоритетный список находки`;
- translated avoidable English glue where it was not a technical identifier: `context, not enforced configuration`, `repository environment`, `issue tracker`, `formatter`, `lint`, `security scan`, `diff review`, `curated lists`, `test-first`;
- preserved technical names, protocol primitives, event names, source titles, file names and API terms where translating them would reduce precision.

## Provenance

No new external sources were added in this pass. Existing inline external links from the previous MCP and hooks expansions were preserved. URL comparison against the previous integrated Chapter VI version found no lost links.

## Checks

- Chapter file updated in the integrated filesystem path.
- Headings checked after restructuring.
- Existing external URLs preserved.
- Synthetic figure ids preserved:
  - `fig-vi-project-interface-layers`
  - `fig-vi-mcp-server-interface`
- Checked for known bad translation/style markers: `свидетельство`, `стенограмма`, `трасса сессии`, `выживание результата`, `файл статусаы`, `приоритетный список находки`, `context, not enforced configuration`, `repository environment`, `issue tracker`, `formatter`, `security scan`, `hook-like`.
- Overlay built in repository-root form.
