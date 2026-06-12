# A7 degradation and duplication audit

## Проверка против задания

- Основной фрагмент `A7_observation_vs_evidence.md` сохранён как теоретический раздел, а не каталог тестов, логов или историй.
- Главная функция A7 сохранена: наблюдение помогает агенту продолжить работу; свидетельство даёт человеку материал для принятия, отклонения или остановки изменения.
- В тексте сохранены обязательные элементы: область действия, проверочный критерий, сохранённая трасса, воспроизводимость, связь с требованием/контрактом/ADR, владелец проверки, критерий отказа и переход состояния работы.
- Самоотчёт агента по-прежнему не считается свидетельством.
- ADR по-прежнему не считается доказательством реализации: он задаёт, что надо подтвердить и кто может это принять.
- `completed` без пакета свидетельств теперь описывается как преждевременное или неподтверждённое завершение, а не как полноценное состояние работы.

## Источники и трасса происхождения

- В основном фрагменте ссылки стоят на внешние/публичные источники, а не на внутренние досье.
- Новые источники в repair-pass не добавлялись; правка была композиционной, визуальной и языковой.
- Сохранены источниковые линии: Arvid Kahl для браузерной проверки, TDAD A/B для двух типов проверочного критерия, Nygard/MADR/AWS/Vercel для ADR и `Confirmation`, Shopify Roast/Doubrovkine для журнала исполняемого workflow, Simon Willison для research/Showboat/Rodney/transcripts, Stripe для независимого проверяющего взгляда и PR/benchmark, Anthropic/TechChannel/Augmented Code для миграционных свидетельств.
- `A7_source_usage.md` не требует новой источниковой базы; при будущей сборке можно только уточнить места применения после финального сокращения текста.

## Проверка против соседних фрагментов

- A7 не дублирует A6: браузер, DOM, логи и runtime-сигналы используются как примеры статуса рабочего следа, а не как раздел о среде исполнения.
- A7 не дублирует A3/TDAD: TDAD используется как пример качества проверочного критерия, а не как самостоятельный обзор test-driven методологий.
- A7 не дублирует A2/ADR: ADR используется как память решения и поверхность `Confirmation`, а не как отдельная глава об ADR.
- A7 не дублирует A4/B2/PWG: рабочий граф нужен только для тезиса, что состояние работы не должно закрываться без пакета свидетельств и владельца проверки.
- A7 не превращает Simon/Arvid/Shopify/Stripe/Product Migration в пересказ историй; они работают как короткие якоря для типов рабочих следов и свидетельств.

## Visual regression audit after repair

- Inline-фигуры сокращены с 13 до 5.
- Оставлены 3 synthetic figures:
  - `fig-a7-observation-to-evidence-chain`
  - `fig-a7-evidence-type-by-promise`
  - `fig-a7-evidence-chain-pwg`
- Оставлены 2 real local image assets:
  - `fig-a7-browser-observation-evidence`
  - `fig-a7-showboat-rodney-replay`
- Убраны из inline и перенесены в `A7_figure_candidates.md` как merged/deferred:
  - `fig-a7-observation-status-ladder`
  - `fig-a7-working-traces-matrix`
  - `fig-a7-transcript-status`
  - `fig-a7-tdad-two-oracles`
  - `fig-a7-adr-confirmation-surface`
  - `fig-a7-roast-trace-not-truth`
  - `fig-a7-stripe-minion-evidence-loop`
  - `fig-a7-migration-parity-gate`
  - `fig-a7-pwg-false-completion`
- Реальные локальные изображения не переписаны в текстовые схемы. `openai-codex-citations-evidence.webp` сохранён как local asset candidate и отложен для technical atlas / Codex evidence surface.
- Служебные captions “Восстановленная source-иллюстрация” / “Локальный файл” убраны из основного A7.

## Языковой и стилевой repair

- Английские labels внутри оставшихся synthetic figures заменены на русские объяснительные формулировки там, где это не имена команд, файлов, статусов или источников.
- Сохранены точные технические имена: `respond`, `.tdad/test_map.txt`, `Confirmation`, `Accepted`, `Rejected`, `Rework`, `roast execute`, `.roast/sessions/.../final_output.txt`, `showboat exec`, `showboat image`, `verify`, `extract`, `rodney open`, `rodney js`, `rodney click`, `rodney screenshot`, `completed`.
- Формулы с “ложным завершением” заменены более прямыми: преждевременное завершение, неподтверждённое завершение, `completed` без пакета свидетельств.
- Основной текст не переписывался ради гладкости; фактические якоря и конфликтные ограничения сохранены.

## Readiness

Статус: `ready_with_known_debts`.

A7 стал чище как теоретический узел и лучше подходит как вход для C3. Оставшиеся долги: финальный link/freshness check, решение по термину `replay`, и возможное сокращение второго real asset при сборке всей теории, если визуальный слой главы окажется слишком плотным.
