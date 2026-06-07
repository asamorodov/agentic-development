# Stage 0.12 source expansion report: architecture quality and test data/environments

Дата: 2026-06-07  
Режим: кумулятивный архив-оверлей, продолжение Stage 0.5–0.11.  
Статус: targeted search по двум сильным residual gaps. Главы не переписывались; `work/approved-ai-sdlc-plan.md` не изменялся.

## Зачем был нужен Stage 0.12

После Stage 0.11 оставались два кандидата на важный пропуск:

1. Architecture quality / fitness functions.
2. Test data / test environments.

Они похожи на ADR по типу опасности: это не один источник и не один инструмент, а классы инженерного смысла, которые легко растворить между spec, tests, CI and review. Поэтому по каждой теме было сделано три честных поисковых этапа с разными формулировками.

## 1. Architecture quality / fitness functions

### 1.1. Что показал поиск

Architecture quality is not just “architecture documentation”. Это отдельный слой:

- quality attributes;
- quality-attribute scenarios;
- tradeoff analysis;
- sensitivity points;
- architecture fitness functions;
- architecture tests;
- architecture drift / erosion;
- decision enforcement.

ATAM and related methods show that architecture is evaluated by scenarios and tradeoffs, not only by code correctness. Fitness functions / architecture tests show the executable side: some architecture qualities can be checked continuously. ArchUnit gives a concrete example: dependency, layer, cycle and modularity rules can run as automated tests. LLM/ATAM sources show that models can assist with scenario and risk analysis, but not replace human architectural judgment.

### 1.2. Why it matters for AI-driven SDLC

Agents can produce locally correct code that slowly breaks architecture:

- cross-layer dependency;
- hidden coupling;
- cycle;
- violation of modular boundary;
- degraded deployability;
- performance/security/reliability tradeoff;
- violation of architectural decision.

Unit tests may stay green. CI may pass. The damage appears at the quality-attribute level.

### 1.3. Relationship to existing patch

This layer belongs with several existing classes:

- intent/decision artifacts: quality attribute scenario, architectural constraint;
- execution/control artifacts: fitness function, architecture test;
- evidence artifacts: architecture test result, tradeoff review;
- lifecycle-tail artifacts: architecture drift, stale fitness function.

### 1.4. Recommended plan impact

Add a named medium-high subsection:

```text
architecture quality and fitness functions
```

Best location: Part X, with cross-links to Parts III, VIII and XII.

Do not create new top-level part. Do not make it another deep anchor. But give it more than a short mention.

## 2. Test data / test environments

### 2.1. Что показал поиск

Test data and test environment are not mere support details. They are part of evidence. Search confirmed several layers:

- test data management: creation, preparation, control and distribution of test data;
- test data types: positive, negative, edge cases, realistic scenarios, regression data;
- privacy and masking/subsetting;
- synthetic data with benefits and risks;
- test environment management;
- service virtualization;
- test dependencies as code via Testcontainers;
- LLM-generated tests and generated test data.

### 2.2. Why it matters for AI-driven SDLC

In agentic development, evidence can become circular:

```text
agent generates code;
agent generates tests;
agent generates test data;
agent interprets results.
```

If the data and oracle come from the same model assumptions, the evidence package can look strong but remain weak. Test data source, data freshness, environment identity and oracle independence become part of the proof.

### 2.3. Relationship to existing patch

This layer belongs with:

- execution environment: controlled test environment;
- evidence package: test data, fixtures, environment state, service virtualization;
- security/privacy: masked production-like data, synthetic data verification;
- lifecycle tail: stale fixtures, test data drift, environment drift.

### 2.4. Recommended plan impact

Add a named medium-high subsection inside Part X:

```text
test data, test environment and oracle independence
```

Also add to Part VIII:

```text
test environment as controlled execution surface
```

And Part XII:

```text
test data drift / stale fixtures / test environment cleanup
```

## 3. Should either become separate chapter/subchapter?

### Architecture quality

It probably deserves a **subchapter** or a strong subsection, not a separate top-level part.

Why:

- It is important enough to be explicitly named.
- It binds ADR, fitness functions, policy checks and evidence.
- But it is not a vertical deep case like SPDD or Gas Town.
- It fits naturally inside Part X as a type of evidence and Part VIII as executable constraint.

### Test data / environments

It also deserves a **subchapter** or strong subsection, likely in Part X.

Why:

- Evidence without controlled data/environment is weak.
- Agent-generated tests make the oracle/data problem sharper.
- But it is a support layer for evidence, not a full architecture of its own.

## 4. Updated synthesis

Stage 0.12 changes the five artifact classes from Stage 0.11 slightly.

### Add to “Артефакты намерения и решения”

- quality attribute scenario;
- architecture constraint;
- test oracle assumption.

### Add to “Артефакты среды исполнения и ограничений”

- architecture fitness function;
- architecture test;
- controlled test environment;
- service virtualization;
- test dependencies as code.

### Add to “Артефакты свидетельства и проверки”

- architecture fitness result;
- test data source;
- fixture/seed state;
- environment identity;
- oracle provenance;
- independent validation of generated tests.

### Add to lifecycle tail

- architecture drift;
- stale fitness functions;
- test data drift;
- stale fixtures;
- test environment drift.

## 5. Human-gate recommendation

Before updating `work/approved-ai-sdlc-plan.md`, ask the user to approve adding two medium-high subsections:

1. `Architecture quality and fitness functions`.
2. `Test data, test environments and oracle independence`.

These should be explicit in the plan, but controlled in size.
