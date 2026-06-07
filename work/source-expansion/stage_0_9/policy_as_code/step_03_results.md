# Search step 3 results — agentic policy generation and validation

## Источники

- `ARPaCCino` — agentic RAG system for generating Rego rules, checking IaC compliance and iteratively refining configurations.
- `Policy as Code, Policy as Type` — theoretical angle: policies distinguish allowed and disallowed actions, with stronger type/proof systems as an alternative to Rego-like approaches.
- AI-augmented CI/CD sources from Stage 0.7 — policy-as-code guardrails for staged autonomy.

## Оценка

Agents can help generate policies, but this adds another validation problem. Policy artifacts require their own tests/review, otherwise the system can enforce wrong constraints confidently.

## Влияние на план

Add “policy artifact must itself be reviewed/tested” as caution in Part VIII/XI.
