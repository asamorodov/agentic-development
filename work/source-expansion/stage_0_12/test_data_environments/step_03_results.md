# Search step 3 results — LLM-generated tests / generated test data / oracle problem

## Источники

- `HardTests` — synthetic high-quality tests for coding tasks can catch disguised wrong solutions better than existing tests; but this is benchmark/coding-problem context.
- `Large Language Models for Unit Testing: A Systematic Literature Review` — LLMs are used for test generation and oracle generation, but the field still has open challenges.
- `Test Case Generation from Bug Reports via LLMs` — LLM-generated tests can struggle under identifier mutations and depend strongly on structured technical elements.
- Synthetic data for LLM judges — useful analogy: synthetic cases can help refine criteria, but must be generated and evaluated carefully.

## Оценка

This is the critical warning: in AI-driven SDLC, the same agentic/LLM machinery can generate both code and tests/test data. That creates a “same-system evidence” risk: tests may mirror the model’s assumptions.

## Влияние на план

Add to Part X:

```text
generated test data and agent-generated tests require independent validation;
test data source and oracle source should be part of evidence package.
```

This may deserve a named subsection inside Part X.
