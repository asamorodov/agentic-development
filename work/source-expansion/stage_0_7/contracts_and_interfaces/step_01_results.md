# Search step 1 results — API contracts and contract-first development

## Selected sources

- OpenAPI Specification — machine-readable interface description for APIs; OpenAPI descriptions can generate docs, clients, server stubs and test cases.
- Contract-first development — agreeing on an API contract before business logic; enables downstream development/mocking and shift-left testing.
- Consumer-driven contract testing / Pact — contracts between consumer and provider checked in CI.

## Evaluation

API contracts are different from feature specs. They govern integration boundaries and compatibility. In AI-driven SDLC, agents need contract artifacts to avoid changing behavior that other services/users depend on.

## Impact on theory

Add “API/interface contract” to artifact taxonomy. It fits Part III/V as spec-like artifact, Part X as contract tests, and Part XII as compatibility/migration.
