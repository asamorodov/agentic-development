# Test data, environments and oracle independence note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: VIII, X, XII.  
Глубина: medium-high.

## Роль

Stage 0.12 подтвердил: тестовые данные and тестовая среда — не вспомогательная деталь, а часть доказательства.

## Источники

- Test data management.
- Test environment management.
- Testcontainers.
- Service virtualization.
- Synthetic data sources.
- LLM unit testing SLR.
- HardTests.
- Bug-report-to-test generation sources.

## Главный риск

В AI-driven SDLC possible evidence loop:

```text
агент генерирует код →
агент генерирует тесты →
агент генерирует тестовые данные →
агент интерпретирует результат
```

Если код, тест, данные and oracle рождаются из одной модели or same assumptions, evidence package can look strong but be weak.

## Артефакты

- test data source;
- fixture / seed state;
- test dataset;
- masked production-like data;
- synthetic data note;
- controlled test environment;
- service virtualization;
- test dependencies as code;
- environment identity;
- oracle provenance;
- independent validation of generated tests;
- stale fixture note;
- test data drift note.

## Где в theory

- Part VIII: controlled environment and dependencies.
- Part X: named subsection `Тестовые данные, тестовая среда и независимость оракула`.
- Part XII: stale fixtures, test data drift, environment drift and privacy cleanup.

## Failure modes

1. Generated tests mirror generated code.
2. Test data does not represent real cases.
3. Synthetic data carries bias or wrong distribution.
4. Environment not reproducible.
5. External dependency mocked incorrectly.
6. Oracle is just model expectation.
7. Production-like data leaks sensitive information.

## Формула

> Свидетельство состоит не только из факта, что тест прошёл. Важно, на каких данных, в какой среде, с каким оракулом and насколько независимо от проверяемого изменения оно было получено.
