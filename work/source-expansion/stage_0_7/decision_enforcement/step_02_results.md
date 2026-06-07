# Search step 2 results — ADR violation detection and architectural compliance

## Selected sources

- `Evaluating Large Language Models for Detecting Architectural Decision Violations` — studies 980 ADRs across 109 GitHub repositories; models perform well for explicit code-inferable decisions but not for implicit/deployment/organizational ones.

## Evaluation

This source is crucial. ADR can become a machine-assisted audit target, but only if decisions are explicit and code-inferable. It also shows the boundary of automation.

## Impact on theory

Add distinction:

```text
explicit code-inferable decision → possible LLM/check assistance
implicit organizational/deployment decision → human/operational context required
```
