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

## Workflow map: artifacts and gates

Workflow Map Phase 1: `bmad-brainstorming` produces `brainstorming-report.md`; `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` produce research findings; `bmad-product-brief` produces `product-brief.md`; `bmad-prfaq` produces `prfaq-{project}.md` [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/). Phase 2: `bmad-prd` creates/updates/validates PRD; create/update can produce `prd.md`, `addendum.md`, `decision-log.md`; validate produces `validation-report.html` and `.md`; `bmad-ux` produces `DESIGN.md`, `EXPERIENCE.md`, `.decision-log.md` [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/).

Important source detail: `bmad-prd` has three intents in one skill: Create, Update, Validate; if invoked without intent, it asks [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/). Product brief upstream can be source-extracted during PRD discovery, but neither skill strictly requires the other [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/). This shows BMAD preserves optional upstream artifacts but does not make every path mandatory.

## Agents and their responsibilities

Agents page lists default BMM Agile suite agents installed with BMad Method. Each agent is invoked as a skill; skill ID such as `bmad-agent-dev` invokes agent; triggers are short menu codes and fuzzy matches [Agents](https://docs.bmad-method.org/reference/agents/). Visible agents include Analyst (Mary), PM (John), Architect (Winston); PM primary workflows include Create/Update/Validate PRD, Create Epics and Stories, Implementation Readiness, Correct Course; Architect handles Create Architecture and Implementation Readiness [Agents](https://docs.bmad-method.org/reference/agents/).

This should be represented as responsibility surfaces, not theatrical personas. Analyst explores and frames; PM owns requirements and story decomposition; Architect owns technical design/readiness; Developer implements; QA/test workflows add testing. QA test generation is handled by `bmad-qa-generate-e2e-tests` workflow skill available through Developer agent, while full Test Architect TEA is separate module [Agents](https://docs.bmad-method.org/reference/agents/).

## Implementation readiness gate

Workflow Map search result and localized pages show `bmad-check-implementation-readiness` as gate check before implementation, producing PASS/CONCERNS/FAIL decision [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/). Even if detailed page needs another pass, this gate is central: it checks whether PRD/architecture/story artifacts are ready before agent implementation. In the artifact chain, readiness consumes planning/solutioning outputs and decides whether Phase 4 can safely begin.

Dossier should preserve gate semantics: PASS means proceed; CONCERNS means proceed only with named risks/repairs; FAIL means implementation should not start. Failure mode: readiness gate can become checkbox if reviewer does not inspect stale PRD/architecture, missing decisions, or contradictions. It is also a place where role theater can appear: PM/Architect agents may produce formal approvals without real evidence.

## Core tools and review surfaces

Core Tools page lists always-available skills across projects/modules/phases [Core Tools](https://docs.bmad-method.org/reference/core-tools/). Examples: `bmad-help`, `bmad-brainstorming`, `bmad-party-mode`, `bmad-spec`, `bmad-advanced-elicitation`, `bmad-review-adversarial-general`, `bmad-review-edge-case-hunter`, `bmad-editorial-review-prose`, `bmad-editorial-review-structure`, `bmad-shard-doc`, `bmad-index-docs`, `bmad-customize` [Core Tools](https://docs.bmad-method.org/reference/core-tools/). `bmad-help` scans artifacts/modules and outputs prioritized next steps with skill commands [Core Tools](https://docs.bmad-method.org/reference/core-tools/).

`bmad-brainstorming` loads creative technique library, guides through technique after technique, uses anti-bias protocol shifting creative domain every 10 ideas, targets 100+ ideas before organization and produces append-only session document [Core Tools](https://docs.bmad-method.org/reference/core-tools/). `bmad-party-mode` loads agent manifest, selects 2-3 relevant agents, facilitates cross-talk and disagreement, rotates participation [Core Tools](https://docs.bmad-method.org/reference/core-tools/). These tools are not only pre-project fluff; they define how BMAD tries to make ideation and review less single-agent.

## Skills/commands generation and stale skill failure

Commands/Skills reference distinguishes skill invocation from agent menu triggers. Skill name directly loads agent, runs workflow or task; menu trigger requires active agent session and stays in character [Skills reference](https://docs.bmad-method.org/reference/commands/). Installer reads manifests for selected modules and writes one skill per agent/workflow/task/tool; each skill directory contains `SKILL.md` that tells AI to load source file and follow instructions [Skills reference](https://docs.bmad-method.org/reference/commands/). Claude Code path example: `.claude/skills/`; Cursor/Windsurf: `.agents/skills/` [Skills reference](https://docs.bmad-method.org/reference/commands/).

Important caveat: re-running installer regenerates files to match current module selection, but if skills from removed module still appear, installer does not delete old skill files automatically; user must remove stale directories or delete entire skills directory and re-run install [Skills reference](https://docs.bmad-method.org/reference/commands/). This is a real failure mode: stale skills can make agent use outdated workflows.

## Итоговая рабочая модель and failure modes

Итоговая формулировка: BMAD Method is an installable agent/workflow system that externalizes product discovery, requirements, UX, architecture, story breakdown, readiness and implementation through named skills, agents and artifacts. Its strength is guided handoff between specialized responsibilities; its risk is role theater and artifact laundering when PRD, architecture, stories and readiness decisions look complete but do not carry enough concrete context [BMAD docs home](https://docs.bmad-method.org/) [Workflow Map](https://docs.bmad-method.org/reference/workflow-map/).

Failure modes: stale PRD/architecture, overprocess for small tasks, false handoff between agents, stale skill files after module changes, missing project-context, readiness gate without evidence, context loss if fresh chats are not used, and treating agent persona output as expert review. Comparative note: BMAD differs from Spec Kit/Kiro by role/workflow richness; from GSD by less explicit ship/context engine; from TDAD by weaker native executable verification unless QA/TEA modules are used. Остаточная очередь: open exact implementation readiness workflow, architecture workflow, story/dev/code-review workflows, testing reference/TEA docs and GitHub issues before final chapter.
