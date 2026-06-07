# Plan patch recommendations after Stage 0.7

Дата: 2026-06-07  
Статус: дополняет `work/reports/PLAN_PATCH_RECOMMENDATIONS.md`; не меняет approved plan напрямую.

## Дополнительные patch items после Stage 0.7

Stage 0.5/0.6 recommendations remain valid. Stage 0.7 adds five second-order patch items.

### 1. Codebase readiness

Add to Part VI or Part XII:

```text
Codebase readiness is not a model property. It is the state of tests, instructions, context files, metrics, CI, observability and feedback loops that make agent work reliable.
```

Use ACMM, Agent READMEs, developer-provided context and AGENTS.md evaluation.

### 2. Context file quality/debt

Add to Part VI/XII:

```text
AGENTS.md / Cursor rules / Agent READMEs are configuration-like artifacts. They can help, but can also add unnecessary constraints, increase cost and degrade task success.
```

### 3. API/data contracts

Add to Part III/V/X/XII:

```text
API contracts, data contracts and contract tests are boundary artifacts. They constrain compatibility, data meaning and integration behavior. They are not equivalent to feature specifications.
```

### 4. Agent workflow specification

Add to Part VII/VIII:

```text
Some frameworks specify the agent workflow itself: explicit control flow, state, branching, verification, logging and portability. This is process-as-artifact, not feature-specification.
```

Use AgentSPEX/Open Agent Specification as medium/short support.

### 5. Delivery safety

Add to Part XII:

```text
Feature flags, canary rollout, migration plans, rollback plans and runbooks are operational control artifacts. They let the lifecycle continue after merge and prevent irreversible AI-generated changes.
```

### 6. Decision enforcement

Add to ADR layer:

```text
ADR is not only a record after a decision. Decision records can become compliance targets: LLMs may help detect code-inferable decision violations, while implicit/deployment/organizational decisions still require human/contextual judgment.
```

## Do not do yet

- Do not add new top-level parts for all these topics.
- Do not expand Part XII into a second theory.
- Do not demote SPDD/Gas Town.
- Do not start drafting before human approves which patch items enter `approved-ai-sdlc-plan.md`.
