# Figure candidates — Chapter IV SPDD specification lifecycle

## Decision after SPDD patch

Фигура вставлена в основной текст главы.

- Inserted asset: `content/assets/theory-images/fowler-spdd-workflow.svg`.
- Placement: after `## Полный рабочий цикл`.
- Function: показать SPDD как цикл, а не как каталог команд: намерение превращается в Canvas, Canvas ведёт генерацию, ревью и проверки возвращают уточнения в спецификацию через `prompt-update` и `sync`.
- Source: Fowler/Thoughtworks, `Structured-Prompt-Driven Development`.

## Why this figure, not a Canvas table

Здесь важнее не полный вид REASONS Canvas, а движение спецификации во времени. Canvas-таблица полезна в Атласе, но в основном тексте она могла бы сместить внимание к справочнику по структуре Canvas. Схема цикла лучше держит главный вопрос: зачем SPDD нужен как спецификационный жизненный цикл.
