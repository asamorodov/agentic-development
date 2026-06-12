# Process methods comparative synthesis

Дата: 2026-06-08
Статус: repaired synthesis after source-consolidation dossier pass.

Главный вопрос: когда процесс сам становится артефактом?

## Основной вывод

Spec Kit, GSD and BMAD all turn process into artifacts, but at different widths and depths.

Spec Kit turns a feature process into a chain: constitution, spec, plan, tasks, implementation (https://github.github.com/spec-kit/). GSD turns ongoing agent work into durable project state: `VISION.md`, `ROADMAP.md`, `CURRENT_STATE.md`, `SHIP_HANDOFF.md`, verification commands and gates (https://opengsd.net/products/gsd-core, https://opengsd.net/docs/v1/configuration). BMAD turns product/process work into role-based phase flow: Analysis, Planning, Solutioning and Implementation, with PRD, architecture, stories, sprint status, review and retrospectives (https://docs.bmad-method.org/reference/workflow-map/).

Gas Town remains the deep environment/case anchor. GSD and BMAD are protected medium-deep process profiles, not replacements for Gas Town.

## Spectrum

| Method | Process width | Main artifacts | Main strength | Main overuse risk |
|---|---|---|---|---|
| Spec Kit | feature spec-to-code | constitution, spec, plan, tasks | makes feature intent executable | artifact ritual |
| GSD / Open GSD | stateful agent work loop | VISION, ROADMAP, CURRENT_STATE, SHIP_HANDOFF, verification config | continuity, verification, handoff | stale state / over-automation |
| BMAD Method | role-based product-to-implementation process | product brief, PRD, architecture, stories, sprint status, review, retrospectives | progressive context by role and phase | process heaviness / role theater |
| Reversa / OpenSpec / AgentSPEX | adjacent comparison layer | varies | prevents false uniqueness | outside current protected scope |
| Gas Town | full environment / deep case | narrative and organizational setting | deep anchor | protected baseline separately |

## GSD vs BMAD

GSD’s strongest contribution is durable state. `CURRENT_STATE.md` and `SHIP_HANDOFF.md` are not just notes; they are continuity artifacts for future agent runs (https://opengsd.net/products/gsd-core). Configuration gates and verification commands make process explicit (https://opengsd.net/docs/v1/configuration). Auto mode shows that autonomy needs state-machine, repair and pause behavior (https://www.opengsd.net/docs/v2/auto-mode).

BMAD’s strongest contribution is role/phase context construction. Workflow map makes documents flow from Analysis to Planning to Solutioning to Implementation (https://docs.bmad-method.org/reference/workflow-map/). Agents reference grounds roles like Analyst, PM, Architect and Developer in workflows (https://docs.bmad-method.org/reference/agents/). The implementation readiness check gives a concrete gate (https://docs.bmad-method.org/reference/workflow-map/).

The contrast is useful:

- GSD asks: what must survive the next session?
- BMAD asks: who produces which context before implementation?

## What Part VII should do

Part VII should avoid product manual style. It should use methods as comparative lenses:

1. Spec Kit: process as feature artifact chain.
2. GSD: process as durable state and verification loop.
3. BMAD: process as role/phase document flow.
4. Gas Town: process as full environment and organizational case.

## Failure modes to carry forward

- Process artifacts can be generated without genuine judgment.
- State files can go stale.
- Verification commands can be too narrow.
- Agent personas can become theater.
- Full process can be overkill for small work.
- Deep-anchor promotion of GSD/BMAD would distort the approved architecture.

## Handbook / Fieldbook split

Theory should keep the comparison and lifecycle meaning.

Handbook should contain:

- Spec Kit command examples.
- GSD state file templates and verification command setup.
- BMAD track selection and agent/workflow operation.
- Checklists for stale state, stale PRD, and false readiness.
