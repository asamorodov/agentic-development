# Plan patch recommendations after Stage 0.12

Дата: 2026-06-07  
Статус: дополняет Stage 0.11 detailed patch; не меняет approved plan напрямую.

## Summary

Stage 0.12 confirms two remaining gaps deserve explicit treatment:

1. Architecture quality / fitness functions.
2. Test data / test environments.

They do not require new top-level parts, but they deserve named medium-high subsections.

## Patch item 1 — architecture quality and fitness functions

### Add to Part III

When distinguishing intent artifacts, include:

```text
quality attribute scenario
architecture constraint
```

These are not ADRs and not ordinary requirements. They express qualities the architecture must preserve.

### Add to Part VIII

Add:

```text
architecture fitness function / architecture test
```

as executable constraints inside the agent environment.

### Add to Part X

Add a named subsection:

```text
Architecture quality and fitness functions
```

Content:

- quality attribute scenarios;
- tradeoffs and sensitivity points;
- architecture tests;
- layer/dependency/cycle rules;
- architecture drift;
- limits of automated checks.

### Add to Part XII

Add:

```text
architecture drift
stale fitness functions
fitness-function maintenance
```

## Patch item 2 — test data, test environments and oracle independence

### Add to Part VIII

Add:

```text
controlled test environment
test dependencies as code
service virtualization
```

### Add to Part X

Add a named subsection:

```text
Test data, test environments and oracle independence
```

Content:

- test data management;
- fixtures, seeds and test datasets;
- masked production-like data;
- synthetic data;
- service virtualization;
- Testcontainers-style dependencies as code;
- generated tests and generated test data;
- oracle independence;
- environment identity in evidence package.

### Add to Part XII

Add:

```text
test data drift
stale fixtures
test environment drift
test data privacy cleanup
```

## Relationship to earlier patch

These two additions should be folded into the five artifact classes:

1. Intent and decision artifacts.
2. Task/project state artifacts.
3. Execution environment and constraint artifacts.
4. Evidence and review artifacts.
5. Completion and lifecycle-tail artifacts.

They should not create a sixth class unless the writing phase shows that architecture-quality and evidence-control need their own framing.
