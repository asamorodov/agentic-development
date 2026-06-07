# Stage 0.7 second-order source expansion report

Дата: 2026-06-07  
Режим: cumulative archive overlay, continuing from Stage 0.5 + Stage 0.6.  
Статус: second-order source expansion. Главы не переписывались; `work/approved-ai-sdlc-plan.md` не изменялся.

## Почему понадобился Stage 0.7

Stage 0.5 выявил слабые зоны. Stage 0.6 подтвердил их через targeted source expansion. Но анализ Stage 0.6 сам открыл новые углы:

1. `context files` and project instructions are not automatically helpful; they can become configuration debt.
2. API/data contracts are not just specs; they are compatibility/evidence artifacts.
3. Workflow specification and portability are separate from feature specification.
4. Deployment safety needs artifacts like feature flags, migration plans and rollback plans.
5. ADRs can be generated and checked by LLMs, but only under strong limits.

Stage 0.7 проверяет эти second-order gaps. Для каждой темы сделано три search steps with different query formulations.

## Темы и результаты

### 1. Codebase readiness and context quality

Sources:

- `The AI Codebase Maturity Model`;
- `Agent READMEs`;
- `An Empirical Study of Developer-Provided Context`;
- `Evaluating AGENTS.md`.

Findings:

- Codebase readiness should become explicit. AI autonomy depends on feedback loops, tests, instructions, metrics and runnable checks.
- Context files are not just helpful documentation. They evolve like configuration code and can contain too much or wrong guidance.
- `AGENTS.md` / Cursor rules / Agent READMEs need quality discipline: minimal, relevant, current, tested against real tasks.

Plan impact:

- Strengthen Part VI “project as agent interface”.
- Add `codebase readiness` as medium concept.
- Add context-file quality/debt to Part XII.

### 2. Contracts and interfaces

Sources:

- OpenAPI / contract-first development;
- consumer-driven contracts / Pact;
- data contracts / Open Data Contract Standard;
- schema evolution and migration;
- `Do Large Language Models Respect Contracts?`;
- robust contract evolution in microservices.

Findings:

- API/data contracts are distinct artifacts. They are not just “specifications” in the SPDD sense.
- Contract tests connect intent/specification to CI evidence.
- AI-generated code may pass functional tests and still violate preconditions, constraints or compatibility contracts.

Plan impact:

- Add API/interface contract and data contract to artifact taxonomy.
- Mention contract-adherence evidence in Part X.
- Use contracts in Part XII for migration/compatibility.

### 3. Workflow specification and portability

Sources:

- `From Prompt to Process`;
- `AgentSPEX`;
- declarative language for LLM-powered workflows;
- Open Agent Specification / Agent Spec.

Findings:

- There is a process-as-artifact subfamily: agent workflows can be specified declaratively with control flow, state, verification, logging and portability.
- This differs from feature/specification layer. It describes the agent process itself.

Plan impact:

- Add “agent workflow specification” to Part VII/VIII as medium artifact.
- Use OpenSpec/AgentSPEX as source-map/medium support, not deep anchors.

### 4. Delivery safety and operational release

Sources:

- feature flags / feature toggles;
- continuous deployment;
- schema migration / Liquibase;
- `AI-Augmented CI/CD Pipelines`;
- `ICAN-Deploy`.

Findings:

- Release/rollback is a real artifact layer. AI-driven SDLC must not stop at merge.
- Feature flags and canary rollout are operational control artifacts, but create toggle debt.
- Database/schema migrations make rollback and compatibility explicit.

Plan impact:

- Strengthen Part XII with feature flags, migration plan, rollback plan, release plan.
- Mention AI-augmented CI/CD cautiously as emerging source, not deep anchor.

### 5. Decision enforcement

Sources:

- LLM-generated ADR / architectural decisions papers;
- `Evaluating LLMs for Detecting Architectural Decision Violations`;
- design rationale / architectural decision lifecycle sources.

Findings:

- ADRs can be agent-assisted in generation and compliance checking.
- LLMs can detect explicit code-inferable decision violations, but struggle with implicit/deployment/organizational decisions.
- Decision provenance itself has lifecycle: identify → propose → decide → document → enforce/review → revisit.

Plan impact:

- Strengthen ADR proposal from Stage 0.5/0.6.
- Add decision enforcement as bridge between Part III, Part VI, Part X/XI and Part XII.

## New recommendations

1. Add **codebase readiness** to the plan as a medium concept.
2. Add **context file quality/debt** to Part VI/XII.
3. Add **API/data contracts** as explicit artifact category.
4. Add **contract adherence** to Part X evidence.
5. Add **agent workflow specification** as process artifact, distinct from feature specification.
6. Add **feature flags / progressive delivery / migration rollback** to Part XII.
7. Add **ADR compliance checking** and **decision enforcement** as part of decision provenance.
8. Do not create new top-level parts yet. First patch the approved plan and create dossiers/notes.

## Updated dossier recommendations

Add to prior list:

```text
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_NOTE.md
work/dossiers/AGENT_WORKFLOW_SPECIFICATION_NOTE.md
work/dossiers/DELIVERY_SAFETY_AND_ROLLBACK_NOTE.md
work/dossiers/DECISION_ENFORCEMENT_NOTE.md
```

These are not all deep dossiers. They are notes to prevent silent omissions before drafting.

## Human gates

Human approval required before:

- adding a new top-level part for codebase readiness or workflow specification;
- promoting GSD/BMAD/OpenSpec/AgentSPEX to deep anchors;
- making Part XII large enough to compete with SPDD/Gas Town;
- changing approved plan;
- starting drafting without applying/rejecting Stage 0.7 patch.
