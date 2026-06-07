# Search step 1 results — architecture quality / ATAM / quality attributes

## Источники

- `Architecture Tradeoff Analysis Method` / SEI line — ATAM разбирает business drivers, quality attributes, quality-attribute scenarios, architectural approaches, tradeoffs, sensitivity points and risks. Это метод раннего выявления архитектурных рисков и tradeoffs.
- Software architecture sources — подчёркивают, что архитектура состоит из структур, элементов, связей and properties; architectural decisions are often costly to change.
- ATRAF / SATAM follow-up sources — показывают современные продолжения scenario/tradeoff thinking, включая security-aware migration contexts.

## Оценка

Это действительно отдельный слой. Он не совпадает с ADR:

- ADR фиксирует принятое решение и его причины.
- Quality attribute scenario формулирует качество, которое должна сохранять архитектура.
- Fitness function / architecture test делает часть этого качества проверяемой.
- Tradeoff analysis показывает, где качества конфликтуют.

## Влияние на план

Добавить в patch новую группу:

```text
architecture quality artifacts:
  quality attribute scenario;
  utility tree / quality priority;
  architecture fitness function;
  architecture test;
  tradeoff/risk record.
```

Эта группа должна распределяться между Part III, Part VIII, Part X and Part XII. Она не требует новой top-level части, но требует заметной подглавы или блока.
