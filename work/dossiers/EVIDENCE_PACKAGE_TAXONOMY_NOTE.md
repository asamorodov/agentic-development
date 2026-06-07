# Evidence package taxonomy note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: X, VIII, XI, XII.  
Глубина: medium-high.

## Роль

Part X должна стать не частью “про тесты”, а частью про доказательность результата. Evidence package depends on change type.

## Источники

- SWE-chat / Programming by Chat.
- UTBoost, SWE-Bench-related sources, benchmark validity.
- PR / review studies.
- TDAD code-test graph.
- Contract tests.
- Architecture fitness functions.
- Test data / environment sources.
- Agent traces / observability sources.
- Security/provenance sources.

## Основной тезис

Нет одного универсального evidence package. Для разных изменений нужны разные свидетельства.

## Возможные компоненты

- test outputs;
- CI logs;
- contract tests;
- traceability links;
- benchmark results;
- PR description;
- review comments;
- agent trace / tool-call log;
- architecture fitness result;
- test data source;
- environment identity;
- oracle provenance;
- policy check result;
- security review;
- SBOM/provenance evidence;
- reproducible build evidence.

## Типы изменений и evidence

### Small local bugfix

- failing test before;
- passing test after;
- minimal diff;
- reproduction note.

### API contract change

- contract update;
- consumer-driven tests;
- migration/compatibility note;
- traceability link.

### Architectural change

- ADR;
- quality attribute scenario;
- architecture fitness result;
- tradeoff review.

### Agent workflow / context change

- context diff;
- regression check;
- trace of agent behavior;
- stale instruction cleanup.

### Security-sensitive change

- threat model note;
- security review;
- policy check;
- secret scanning;
- provenance record.

## Failure modes

1. Agent summary as fake evidence.
2. Green tests without relevant data.
3. Benchmark overfit.
4. PR description not checked against diff.
5. Review comments treated as commands.
6. Trace unavailable.
7. Evidence not usable by next step.

## Формула

> Свидетельство — это не один файл. Это пакет, достаточный для следующего решения: продолжить, ревьюить, сливать, выпускать or возвращать в работу.
