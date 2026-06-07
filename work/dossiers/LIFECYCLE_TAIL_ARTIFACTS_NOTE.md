# Lifecycle tail artifacts note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: XII, X, XI.  
Глубина: medium.

## Роль

Part XII должна замкнуть lifecycle, но не стать эксплуатационным handbook. Эта заметка группирует хвостовые артефакты, чтобы они не выглядели складом.

## Группы артефактов

### Release and operational control

- release plan;
- feature flags;
- canary rollout;
- migration plan;
- rollback plan;
- runbook.

### Learning and repair

- incident report;
- postmortem;
- stale ADR;
- context file cleanup;
- prompt/context regression;
- observability debt.

### Architecture and test evidence tail

- architecture drift;
- stale fitness functions;
- architecture-test maintenance;
- test data drift;
- stale fixtures;
- test environment drift;
- test data privacy cleanup.

### Supply-chain and security tail

- SBOM;
- dependency/license inventory;
- secret rotation;
- credential follow-up;
- provenance record.

### Communication and external memory

- changelog;
- release notes;
- traceability to PR/issues/contracts.

## Главная мысль

Merge is not the end. Change enters operation, produces failures/drift/debt, and returns to earlier artifacts: specs, tests, ADRs, policies, context files, skills and workflow gates.

## Failure modes

1. Part XII becomes ops checklist.
2. Tail omitted, making theory code-centric.
3. Every artifact receives equal space.
4. Incidents do not update earlier artifacts.
5. Release notes/changelog treated as optional decoration.

## Как писать

Use controlled clusters. Show feedback loops. Move practical recipes to Handbook.
