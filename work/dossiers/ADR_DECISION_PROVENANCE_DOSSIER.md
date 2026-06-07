# ADR and decision provenance dossier

Дата: 2026-06-07  
Статус: selected dossier before skeleton v4.  
Связанные части плана: III, VI, X, XI, XII.  
Глубина: medium-deep.

## Роль в AI-driven SDLC

ADR и более широкий слой decision provenance закрывают слабое место, которое поздно всплыло в обсуждении: спецификация отвечает на вопрос “что должно быть сделано”, план — “как двигаться”, но не хватает артефакта, который удерживает “почему было принято именно это решение”, какие альтернативы были отвергнуты, какие последствия приняты and where this decision later constrains code.

Для агентской разработки это особенно важно: агенту нельзя давать только текущую задачу и `README`. Если в проекте есть архитектурные решения, ограничения, запреты, trade-offs and accepted consequences, они должны быть доступны как долговременная проектная память.

## Основные источники и материалы

- ADR practice sources: Nygard-style ADR, MADR/templates, `adr.github.io`, `joelparkerhenderson/architecture-decision-record`.
- AI/LLM ADR sources: LLM-generated architectural decisions, DRAFT-ing architectural decisions, LLM design rationale, LLM detection of architectural decision violations.
- Architectural decision literature: design rationale, decision backlog, architectural knowledge management.
- Внутренние файлы:
  - `work/reports/SDLC_ARTIFACT_COVERAGE_AUDIT.md`;
  - `work/source-expansion/stage_0_6/decision_provenance/`;
  - `work/source-expansion/stage_0_7/decision_enforcement/`;
  - `work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md`;
  - `work/approved-ai-sdlc-plan.md`.

## Что этот слой объясняет лучше других

SPDD объясняет, как намерение становится спецификационным контуром. ADR объясняет другое: как решение остаётся понятным после того, как код уже изменился.

Без ADR/reasoning layer агент видит только текущее состояние кода и, возможно, спецификацию. Он может не знать, что решение было принято из-за производительности, юридического ограничения, инфраструктурного компромисса, обратной совместимости, предыдущего инцидента or team ownership boundary.

## Внутренний workflow

Decision provenance should be represented as a small lifecycle:

```text
problem / context → alternatives → decision → consequences → constraints → enforcement / revisit
```

Это отличается от обычной спецификации:

```text
desired behavior → constraints → acceptance criteria → implementation
```

И отличается от плана:

```text
goal → steps → execution → status
```

## Артефакты

- ADR / decision record;
- RFC / design proposal;
- decision backlog;
- design rationale note;
- accepted consequence;
- rejected alternative;
- architecture constraint;
- decision enforcement check;
- stale decision / decision debt note.

## Human decision points

Human gate required when:

- решение меняет архитектуру документа or codebase architecture;
- агент предлагает изменить accepted ADR;
- есть конфликт между spec and ADR;
- обнаружено нарушение architectural decision;
- нужно решить, устарел ли ADR.

## Evidence / validation mechanisms

- review of decision rationale;
- trace from ADR to code/config/policy/test;
- LLM-assisted ADR violation detection for explicit code-inferable decisions;
- human review for implicit organizational/deployment decisions;
- architecture fitness functions if decision can be encoded as rule.

## Failure modes

1. **ADR as bureaucracy.** Слишком много мелких решений превращает ADR в шум.
2. **Stale ADR.** Решение осталось, но контекст изменился.
3. **False machine confidence.** LLM finds “violation” where decision is not code-inferable.
4. **Hidden decision.** Агент меняет код, не зная rejected alternative.
5. **Spec/ADR collapse.** Спецификация начинает отвечать за rationale, хотя это другая функция.

## Где в rebuilt theory

- Part III: различить spec, plan, ADR, RFC.
- Part VI: ADR как часть project memory.
- Part X: decision enforcement / ADR violation evidence.
- Part XI: governance and completion rights.
- Part XII: stale decisions and decision debt.

## Что не сжимать

- Различие ADR/RFC/spec/plan.
- Логику “decision provenance” как отдельную функцию.
- Ограничение: LLM может помогать, но не заменяет human architectural judgment.
- Связь ADR с architecture quality / fitness functions.

## Что уходит в Handbook / Fieldbook

- Шаблоны ADR.
- Правила именования ADR.
- Минимальные workflow для ADR в одиночном проекте.
- Примеры “когда ADR не нужен”.
