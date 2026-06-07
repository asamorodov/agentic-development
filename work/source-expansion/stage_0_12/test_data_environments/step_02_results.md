# Search step 2 results — test environments / dependencies / service virtualization

## Источники

- Test environment management — функция, обеспечивающая validated, stable and usable test environments, including environment inventory, allocation, monitoring, housekeeping, incident/problem management and test data availability.
- `Testcontainers` official — dependencies as code: disposable, lightweight containers for databases, brokers, browsers and other dependencies; tests start dependencies and delete them, often with known state.
- Service virtualization — emulates unavailable, costly, unstable or restricted dependent components, including services, databases and third-party systems.
- Continuous testing sources — emphasize production-like environments, virtualization, service virtualization and test data management.

## Оценка

Test environment is a separate artifact/control surface. It is part of execution environment and evidence package. For agents, it determines whether evidence is reproducible or anecdotal.

## Влияние на план

Part VIII should include:

```text
test environment as controlled execution surface;
test dependencies as code;
service virtualization for unavailable dependencies.
```

Part X should include environment identity in evidence package.
