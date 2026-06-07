# Search step 2 results — fitness functions / architecture tests / executable constraints

## Источники

- Evolutionary architecture / continuous design sources — формулируют fitness functions as fast feedback loops and automated governance for architecture.
- `ArchUnit` official docs — конкретный инструментальный пример: архитектурные правила проверяют package/class dependencies, layers, cycles, modularization and can run through normal Java test frameworks.
- Continuous delivery/testing sources — поддерживают общий принцип: проверки должны двигаться ближе к pipeline and give early feedback.

## Оценка

Это самая сильная часть темы. Fitness functions are a missing bridge between architecture decisions and evidence package.

Для AI-driven SDLC это особенно важно: агент может вносить локально правильные изменения, которые медленно разрушают архитектурную форму. Обычный unit test этого не увидит.

## Влияние на план

В Part X добавить не только tests/benchmarks, а architecture fitness / architecture tests as evidence type.  
В Part VIII добавить executable architecture constraints as environment/harness artifact.  
В Part XII добавить architectural drift / stale fitness functions.
