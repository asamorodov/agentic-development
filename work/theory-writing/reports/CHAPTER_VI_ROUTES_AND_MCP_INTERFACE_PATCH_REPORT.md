# Chapter VI routes and MCP interface patch — 2026-06-15

## Trigger

The user pointed out two issues in Chapter VI:

1. The subsections under `Маршруты действия: как здесь принято делать работу` had grown too large and should become higher-level sections.
2. The MCP section needed more technical facts about how an MCP server is structured as an external interface, based on external sources.

## Files changed

Changed chapter file:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

Updated state / closeout files:

```text
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

## Structural change

The previous section:

```text
## Маршруты действия: как здесь принято делать работу
### Skills: повторяемые процедуры как часть проекта
### MCP: управляемый доступ к внешнему миру
### Subagents: разные исполнители для разных частей задачи
```

was reshaped into:

```text
## Маршруты действия: как проект выбирает способ работы
## Skills: повторяемые процедуры как часть проекта
## MCP-сервер: управляемый внешний интерфейс
## Subagents: разные исполнители для разных частей задачи
```

`Маршруты действия` now works as a short conceptual hinge. `Skills`, `MCP` and `Subagents` are no longer nested as small subpoints, because each one already carries a substantial part of the chapter argument.

## MCP technical expansion

The MCP section was expanded with the external-interface layer that was previously missing:

- host / MCP client / MCP server relation;
- JSON-RPC 2.0 requests, responses and notifications;
- stateful session and initialization handshake;
- capability negotiation through `initialize` and `notifications/initialized`;
- `stdio` and Streamable HTTP transports;
- server features: `resources`, `prompts`, `tools`;
- discovery / invocation methods such as `tools/list`, `tools/call`, `resources/list`, `resources/read`, `prompts/list`, `prompts/get`;
- practical difference between read-oriented resources, user-controlled prompts and model-controlled tools;
- a small synthetic figure `fig-vi-mcp-server-interface`.

## External sources used

Primary MCP sources used for this patch:

```text
https://modelcontextprotocol.io/specification/2025-11-25
https://modelcontextprotocol.io/specification/2025-11-25/basic
https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle
https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
https://modelcontextprotocol.io/specification/2025-11-25/server/resources
https://modelcontextprotocol.io/specification/2025-11-25/server/prompts
https://modelcontextprotocol.io/specification/2025-11-25/server/tools
https://modelcontextprotocol.io/docs/learn/architecture
https://modelcontextprotocol.io/docs/learn/server-concepts
```

## Small language repairs

Two local language mistakes in the subagents section were corrected while touching the same area:

- `команда агентовs` → `команде агентов` / `команда агентов`;
- sentence start after a period fixed from lowercase `работу` to `Работу`.

## Result

Chapter VI now has a clearer top-level structure around the project-interface mechanisms. The MCP section no longer treats MCP only as a generic source of context; it explains the server as a protocol surface with transport, handshake, capability discovery and separate primitives for data, prompt templates and executable tools.
