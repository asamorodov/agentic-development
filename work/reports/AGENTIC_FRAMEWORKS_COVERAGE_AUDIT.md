# Agentic frameworks coverage audit

Дата: 2026-06-07  
Режим: ChatGPT / локальный snapshot archive → archive handoff overlay  
Ветка-источник: `work/theory-ai-sdlc-rebuild`  
Статус: рабочий audit перед writing/rewrite глав. Главы не переписывались.

Этот audit проверяет класс источников, который был недостаточно представлен в approved plan: **agentic development frameworks / operational methodologies**. Это не то же самое, что specification layer, product platforms or deep anchor cases.

Текущий approved plan уже глубоко учитывает SPDD, Spec Kit, Kiro, TDAD and Constitutional SDD. Но после обсуждения ADR возник второй late gap: GSD, BMAD and related frameworks were not structurally placed.

## Зачем этот audit нужен

В новой рамке AI-driven SDLC есть несколько разных типов материала:

- SPDD / Spec Kit / Kiro / TDAD / Constitutional SDD — specification layer.
- Codex / Copilot cloud agent / Claude Code / Jules — platform/workflow surfaces.
- Gas Town / Beads — organizational/operational deep case.
- SWE-chat / Programming by Chat — empirical session surface.
- Open-source policies — completion/governance boundary.
- GSD / BMAD / OpenSpec / Reversa / Spec Kitty — process/framework layer.

Этот последний слой отвечает не только на вопрос “как писать specification”, а на вопрос “как установить повторяемый агентский процесс”: context, roles, execution loop, validation, portability.

## Точечно проверенные внешние источники

- `From Prompt to Process` — taxonomy paper comparing GitHub Spec Kit, OpenSpec, BMAD Method, GSD, Spec Kitty and Reversa across specification, context, roles, execution, validation and portability.
- BMAD Method docs — BMAD presents itself as an AI-driven development framework from ideation/planning to agentic implementation, with specialized agents and guided workflows.
- GSD / Open GSD — GSD is described as lightweight meta-prompting, context engineering and spec-driven development; the older `gsd-build/get-shit-done` repo points to Open GSD / GSD Core as the current home.
- Open Agent Specification / Agent Spec — declarative agent/workflow specification for portability/interoperability across frameworks.
- Reversa — candidate medium case for recovering operational specifications from legacy systems.
- Spec Kitty — taxonomy item; primary-source depth not yet sufficient in current read set.

## Сравнительная таблица

| Framework | Current coverage | Specification | Context | Roles | Execution | Validation | Portability | Lifecycle stage | Source depth | Structural fit | Recommendation |
|---|---|---|---|---|---|---|---|---|---:|---:|---|
| Spec Kit | Deep Part V in approved plan | High: spec/plan/tasks/constitution | Medium-high through templates/scripts/extensions | Medium | High: specify/plan/tasks/implement | High: analyze/checklist/validation extensions | High: many integrations and ecosystem | Intent/specification → execution handoff | 9 | 9 | Keep deep in Part V; add ecosystem/portability emphasis |
| GSD / Open GSD | Mostly absent from approved plan | Medium: spec-driven planning loop | High: context rot, fresh subagents, `STATE.md`, `CONTEXT.md` | Medium-high: subagents / divided work | High: Discuss → Plan → Execute → Verify → Ship | Medium-high: Verify step, fix plans before phase close | High: multiple agentic coding environments | Context/process/delegation layer | 8–8.5 | 9 | Add medium-deep section in Part VI/VII; create `GSD_DOSSIER.md` |
| BMAD Method | Mostly absent from approved plan | Medium: planning/architecture artifacts | Medium: guided workflows and planning context | High: specialized AI agents / domain experts | Medium-high: analysis, planning, architecture, implementation | Medium: process gates less independently evaluated | Medium-high: several AI coding assistants | Role/process layer from ideation to implementation | 7.5–8.5 | 8.5 | Add medium-deep process-framework section; create `BMAD_DOSSIER.md` |
| OpenSpec / Open Agent Specification | Not in approved plan | Medium-high: declarative specs for agents/workflows | Medium | Medium | Medium | Unknown/medium | High: interoperability goal | Portability/interoperability layer | 6.5–7.5 | 6.5–7.5 | Source-map / short mention unless primary source becomes richer |
| Spec Kitty | Not in approved plan | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Candidate framework from taxonomy | 2–3 until primary source found | 3 | Source-map-only until primary source is found |
| Reversa | Not in approved plan | High: reverse-engineered operational specs | High: legacy implicit rules → explicit context | High: multi-agent pipeline | Medium | Medium-high: confidence marking, parity scenarios, gaps for human validation | Medium | Legacy modernization / migration / context extraction | 7.5–8 | 8 | Add medium case under Part VI/XII or source map; not deep anchor |
| Spec Kit Agents | Source map only | Medium-high as Spec Kit extension | High: discovery hooks / validation hooks | Medium | Medium | High | Medium-high | Bridge between specification and context/harness | 7.5–8 | 8 | Use as bridge inside Part V/VI, not separate framework |
| AI Codebase Maturity Model | Candidate in source map | Low/medium | High as codebase readiness | Low | Medium | Medium | Medium | Readiness / lifecycle maturity | 6.5–7.5 | 7.5 | Keep as candidate for Part I/VI/XII; not central until read deeply |

## Framework-by-framework notes

### Spec Kit

Spec Kit is already correctly placed as a deep neighboring specification regime in Part V. It should not be demoted. It adds a different shape than SPDD: portable toolkit/ecosystem rather than single closed-loop methodology.

Important mechanisms to preserve:

- `constitution`;
- `specify`;
- `plan`;
- `tasks`;
- `implement`;
- templates and scripts;
- extensions and presets;
- multi-agent integrations;
- organization-controlled customization.

Patch needed: emphasize ecosystem/portability and extension catalogs more explicitly. Spec Kit should show how specification becomes portable workflow infrastructure.

### GSD / Open GSD

GSD was underrepresented. It should not be folded into Spec Kit, because its center of gravity is different: context engineering and process continuity. Its strongest contribution to the theory is the treatment of context rot and the decision to externalize state into artifacts while using fresh-context subagents for heavy phases.

Useful structure:

```text
Discuss → Plan → Execute → Verify → Ship
```

Key artifacts / mechanisms:

- `STATE.md`;
- `CONTEXT.md`;
- fresh-context subagents;
- small checkable plans;
- verification before phase closure;
- portability across several agentic coding environments.

Proposed role: medium-deep case in Part VI “project as agent interface” and Part VII “delegation mode”. It can become a process-framework example, not a deep anchor like SPDD/Gas Town.

### BMAD Method

BMAD was also underrepresented. Its value is role/process organization: specialized agents, agile-like workflows, analysis/planning/architecture/implementation, scale-adaptive planning.

It is relevant because it shows a different answer to the process layer: instead of one specification toolkit or one context loop, it defines a multi-role AI development framework.

Proposed role: medium-deep section in Part VII. It should be compared with GSD:

- GSD: context continuity and lightweight process loop.
- BMAD: roles, domain agents and guided workflows.
- Spec Kit: executable specification toolkit.
- Gas Town: organizational/operational deep environment.

BMAD should not become a deep anchor unless a dossier finds substantially more primary-source detail than currently known.

### OpenSpec / Open Agent Specification

Useful mostly for the portability dimension. It may matter if the theory needs to discuss frameworks that define agents/workflows in a declarative cross-framework form. At current source depth, it should not drive a part.

Proposed role: source-map / short contrast in process/framework layer.

### Spec Kitty

At the moment, Spec Kitty is a taxonomy item without enough primary-source material in the read set. It should be marked as source gap and not used as a real case until primary source is found.

### Reversa

Reversa is promising because it handles the reverse direction: not “write a spec before code”, but “recover operational specs from legacy code”. That is highly relevant to AI-driven SDLC because real projects often start with legacy systems and implicit rules.

Potential fit:

- Part VI: project as interface; making hidden context explicit.
- Part XII: migration/maintenance/lifecycle tail.
- Artifact coverage: migration plan, operational spec, confidence gaps.

It is not yet deep anchor material, but it can be a strong medium case.

## Patch recommendation for document architecture

Do not create a new top-level part immediately. Add a visible process/framework layer in the existing architecture:

1. In Part VI, after context/project interface, add GSD as a medium-deep case about context engineering and fresh-context execution.
2. In Part VII, add a subsection like:
   ```text
   Agentic development frameworks: process as installed artifact
   ```
   covering GSD, BMAD, and a short comparison to Spec Kit.
3. In Part XII, include Reversa if migration/legacy recovery becomes important.
4. Put OpenSpec / Spec Kitty into source map or short contrast unless deeper primary sources are added.
5. Create dossiers before drafting:
   - `work/dossiers/GSD_DOSSIER.md`
   - `work/dossiers/BMAD_DOSSIER.md`
   - `work/dossiers/REVERSA_NOTE.md`
   - optional `work/dossiers/AGENTIC_FRAMEWORKS_TAXONOMY_NOTE.md`

## Human gates

Human approval is needed if any of these changes are proposed:

1. Add a new top-level part just for agentic frameworks.
2. Promote GSD or BMAD to deep anchor status.
3. Move Spec Kit out of Part V.
4. Demote Spec Kit/Kiro/TDAD/Constitutional SDD from deep treatment.
5. Add another large source-search cycle.
