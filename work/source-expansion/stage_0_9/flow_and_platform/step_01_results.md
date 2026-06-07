# Search step 1 results — поток ценности и ограничения метрик

## Источники

- DORA / Google Research — рамка для оценки software delivery по lead time, deployment frequency, change failure rate and MTTR. Для нашей теории важен не набор метрик сам по себе, а мысль: ускорение генерации кода не означает улучшение потока поставки.
- Value stream / value-stream mapping — полезны как общий язык: смотреть на путь от запроса до полученной ценности, а не на локальную активность.
- `Knowledge Value Stream Framework For Complex Product Design Decisions` — важен как мост к decision provenance: сложные продуктовые решения продвигаются через поток знания, а не только через поток задач.
- `Orchestrating Human-AI Software Delivery` — полезный AI-specific source: показывает программную поставку не как отдельный agent task, а как согласованный процесс analysis → planning → implementation → validation.

## Оценка

Эти источники нужны не для отдельной части, а для защиты единого замысла. Все новые артефакты после Stage 0.5–0.8 должны задаваться вопросом: где они снимают узкое место в жизненном цикле изменения?

## Влияние на план

Добавить в Part I короткий guardrail: артефакт нужен не потому, что “так принято в SDLC”, а потому что он переносит намерение, решение, проверку, ответственность or learning дальше по потоку изменения.
