# Execution control surfaces note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: VIII, XI, XII.  
Глубина: medium.

## Роль

Эта заметка сводит контроль среды исполнения: агент должен действовать не в абстрактном “репозитории”, а в ограниченной, воспроизводимой and наблюдаемой среде.

## Источники

- Harness Engineering.
- Codex / Copilot cloud agent / Claude Code / Jules docs.
- Dev Containers / Codespaces.
- Reproducible / attestable builds.
- Open Policy Agent / policy-as-code.
- MCP security materials.
- Secret leakage in LLM agent skills.
- AgentTrace / AgentSight / OpenTelemetry GenAI.

## Артефакты

- sandbox;
- permissions;
- worktree;
- dev container;
- setup/build/test commands;
- reproducible or attestable build;
- policy-as-code;
- MCP/tool boundary;
- secret scanning;
- credential inventory;
- sensitive context boundary;
- agent trace / tool-call log.

## Главная мысль

Среда исполнения должна не только позволять агенту действовать, но и отвечать:

- где он действует;
- какие права имеет;
- какие инструменты доступны;
- что нельзя читать or отправлять в контекст;
- как повторить его проверку;
- какие следы остаются;
- какие политики ограничивают действие.

## Failure modes

1. Tool access without permission boundary.
2. Sandbox mistaken for governance.
3. Reproducible setup absent.
4. Secrets leak through logs or skills.
5. Policy generated but not reviewed.
6. Agent trace missing, so result cannot be audited.

## Где в theory

- Part VIII: основной дом.
- Part XI: governance and completion rights.
- Part XII: maintenance of environment and policies.

## Ограничение

Не превращать Part VIII в каталог инструментов. Каждый элемент должен объяснять control, reproducibility, observability or boundary.
