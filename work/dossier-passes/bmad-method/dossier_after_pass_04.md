# BMAD Method

Рабочий dossier. Создан заново 2026-06-08 по `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md` без использования task prompt. Это не финальная глава и не профиль: документ сохраняет source-level детали, команды, файлы, gates, ограничения, кандидаты на изображения и остаточную очередь источников.

## BMAD как agent/workflow framework, а не просто Agile glossary

BMAD Method нужно держать как AI-driven development framework module inside BMad Method Ecosystem, covering ideation/planning through agentic implementation [BMAD docs home](https://docs.bmad-method.org/). Official home says it provides specialized AI agents, guided workflows and intelligent planning adapting to complexity from bug fix to enterprise platform [BMAD docs home](https://docs.bmad-method.org/). Это не только набор ролей. Механизм BMAD — guided workflows plus generated skills plus phase map plus artifacts in `_bmad-output/`.

V6 docs mention Skills Architecture, BMad Builder v1, Dev Loop Automation and roadmap [BMAD docs home](https://docs.bmad-method.org/). It works with AI coding assistants supporting custom prompts/project context, including Claude Code, Cursor and Codex CLI [BMAD docs home](https://docs.bmad-method.org/). For dossier, do not translate BMad into «агенты изображают команду». Нужно раскрывать, какие agents/workflows/tools create and consume which artifacts.

## BMad-Help as routing and state inspection surface

`bmad-help` is the fastest way to start: it inspects project state, shows options based on installed modules, recommends next step including first required task, and answers natural-language questions [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). It can be invoked as `bmad-help` or with a query, e.g. `bmad-help I have an idea for a SaaS product...` [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). It also runs at the end of every workflow to say exactly what to do next [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

This is a context transfer mechanism: instead of user remembering phase map, BMAD Help reads artifacts/modules and routes. Failure mode: if artifacts are stale or modules misinstalled, guidance can be wrong. But BMAD’s design makes navigation itself a tool, not a static doc. In future theory, `bmad-help` can be compared to GSD state-driven dispatcher and Kiro task UI.

## Four phases and planning tracks

Getting Started gives four phases: Analysis, Planning, Solutioning, Implementation [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Phase 1 covers brainstorming/research/product brief/PRFAQ optional work; Phase 2 creates requirements PRD/spec; Phase 3 designs architecture for BMad Method/Enterprise; Phase 4 builds epic by epic, story by story [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Planning tracks: Quick Flow for bug fixes/simple features/clear scope 1-15 stories with tech-spec only; BMad Method for products/platforms/complex features 10-50+ stories with PRD + Architecture + UX; Enterprise for compliance/multi-tenant systems 30+ stories with PRD + Architecture + Security + DevOps [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

This detail matters because BMAD scales process by complexity. If future text says BMAD always creates PRD+architecture+stories, it will misrepresent Quick Flow. If it ignores Enterprise track, it will miss security/devops artifacts and governance.

## Installation, folders and direct workflow invocation

Installation: run `npx bmad-method install`; prerelease via `npx bmad-method@next install`; select BMad Method module [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Installer creates `_bmad/` for agents/workflows/tasks/configuration and `_bmad-output/` where artifacts are saved [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). After install, user opens AI IDE and runs `bmad-help`; workflows can be invoked by skill name such as `bmad-prd`, and agent skill can be invoked directly such as `bmad-agent-pm` [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

Fresh chats are explicitly recommended for each workflow to avoid context limitations [Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). This is a key BMAD context-management rule: each workflow should start with clean enough context, while artifacts transfer state between phases. Similar idea to GSD fresh contexts, but in BMAD it is user/process discipline rather than state-machine auto-dispatch.
