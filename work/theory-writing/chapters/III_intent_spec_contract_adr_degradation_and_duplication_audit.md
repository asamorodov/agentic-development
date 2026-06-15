# III. Degradation and duplication audit

## Preserved

- Chapter remains conceptual, not a method catalog.
- Specification, contract and ADR are separated.
- ADR/status boundary is strong.
- Generated/reconstructed ADR candidate boundary is strong.
- `Confirmation` does not become an evidence chapter.
- SPDD is a bridge to IV, not a deep treatment.
- PWG / work-state is only bridged.
- Design Decision Gate remains a pattern for stopping automatic flow, not a governance chapter.

## Remaining risks

- Section 2 names SPDD/Spec Kit/CSDD in one paragraph; responsibility framing must keep leading.
- Section 4 contains several examples; do not expand it into a tool list.
- Section 7 uses one external AI/ADR paper; avoid adding more unless the chapter scope changes.
- Some source-native terms remain English; preserve exact names, but avoid adding new English glue.

## Duplication check

The chapter does not duplicate chapter IV. SPDD is introduced only as the next deep case. The chapter also does not duplicate Evidence or Authority chapters: `Confirmation`, CODEOWNERS and Design Decision Gate remain boundary examples.

## P16 — проверка ссылок при вводе источника

Проверка не выявила потерянных опор. Внешние утверждения не вынесены в конец главы и не заменены внутренними документами: ссылка стоит в том же абзаце, где источник вводится.

Риск остаётся только стилевой: если при будущей переписи абзацы будут дробиться, ссылки нельзя отделять от поддерживаемого утверждения.

## P19 — проверка обзорности

Обзорность снижена в разделе 2: вместо перечисления SPDD / Spec Kit / Constitutional SDD оставлены две короткие опоры, подчинённые главной линии. Глава держится на трёх рабочих опорах: документ как следующий предмет работы, контракт как наблюдаемая граница, ADR/`Confirmation`/origin-status как различение решения, проверки и полномочия.

Деградации в сторону каталога источников не обнаружено после правки: внешние ссылки остаются точечными, а примеры не расширяются в обзор инструментов.

## P21 — начало, структура и границы

Начало главы удерживает правильную границу с главой II: агентская сессия остаётся локальным исполнением, а III начинается там, где намерению нужна форма вне разговора.

Структура сохраняет последовательность: следы сессии → спецификация → контракт → `Confirmation` → ADR → рабочая проекция → generated ADR → подготовленный артефакт и принятие → переход к SPDD и соседним главам.

Граница с IV сохранена: SPDD назван как следующий сильный случай, но не раскрыт в деталях. Граница с XI сохранена: `Confirmation` и результаты проверки только подготавливают будущий разговор о достаточности. Граница с XII сохранена: полномочие принятия названо, но не превращено в отдельную governance-главу.

## P23 — итоговая проверка потерь и дублирования

Ключевые различения сохранены: спецификация не стала ADR, контракт не стал полной приёмкой, `Confirmation` не заменило проверочную главу, ADR не получила право принятия сама по себе.

Дублирования соседних глав нет. IV остаётся местом для SPDD; V — для защищённых спецификационных профилей; VI–VII — для рабочего состояния; XI — для достаточности проверки; XII — для полномочия признать изменение завершённым.

Потерь после языковых проходов не найдено.
