# Правило восстановления исходных anchor-разделов SPDD и Gas Town

Дата: 2026-06-05  
Статус: **жёсткое правило процесса для пересборки теории**

## 1. Суть правила

При работе с разделами **SPDD** и **Gas Town / Beads** нельзя брать за старт последнюю expanded/synthesis-версию, потому что в ней оба кейса уже подвергались структурному сжатию и частично потеряли композиционную силу.

Правильный порядок:

1. Найти полный текст соответствующего раздела в **документе из сайта / старом baseline**.
2. Перенести этот раздел в rebuilt-документ **целиком и без изменений** как исходный seed.
3. Только после этого адаптировать раздел к новой рамке `AI-driven SDLC`.
4. Любое сокращение, перестановка или перенос деталей должен проходить explicit anti-degradation check.
5. Добавлять новую фактуру можно; уменьшать плотность деталей нельзя без отдельного решения пользователя.

Короткая формула:

```text
old site baseline first → unchanged seed → additive/adaptive rewrite → anti-degradation check
```

## 2. Почему это нужно

SPDD и Gas Town — два главных deep anchor cases текущей теории:

- **SPDD** показывает intent/specification lifecycle: как намерение превращается в управляемый, версионируемый, проверяемый и синхронизируемый артефакт.
- **Gas Town / Beads** показывает organizational/operational lifecycle: как агентская разработка становится средой ролей, памяти, рабочих идентичностей, handoff-поверхностей, hooks и обслуживающих агентов.

В expanded-версии уже произошла деградация Gas Town: старый самостоятельный раздел из сайта был сжат до одного `###`-раздела. Новые детали там полезны, но форма и глубина стали слабее. Для SPDD риск такой же: если начать с сжатой версии, легко сохранить ссылки и общие тезисы, но потерять методологическую полноту.

## 3. Обязательные артефакты перед переписыванием SPDD

До финального draft Части IV создать:

```text
baseline_extracts/SPDD_FROM_SITE_BASELINE.md
drafts/part_iv_spdd_seed_unchanged.md
reports/SPDD_BASELINE_STRUCTURE_MAP.md
reports/SPDD_BASELINE_DETAIL_INVENTORY.md
reports/SPDD_ADAPTATION_PLAN.md
reports/SPDD_ANTI_DEGRADATION_CHECK.md
```

Требование: `part_iv_spdd_seed_unchanged.md` должен быть прямым переносом старого сайта без редакторской правки. Адаптация начинается только после этого.

## 4. Обязательные артефакты перед переписыванием Gas Town

До финального draft части Gas Town создать:

```text
baseline_extracts/GAS_TOWN_FROM_SITE_BASELINE.md
drafts/part_ix_gas_town_seed_unchanged.md
reports/GAS_TOWN_BASELINE_STRUCTURE_MAP.md
reports/GAS_TOWN_BASELINE_DETAIL_INVENTORY.md
reports/GAS_TOWN_ADAPTATION_PLAN.md
reports/GAS_TOWN_ANTI_DEGRADATION_CHECK.md
```

Требование: Gas Town должен стартовать из полного старого раздела сайта, а не из последнего сжатого синтеза. Новые детали из expanded-версии (`gt nudge`, `gt seance`, DoltHub negative evaluation и т.п.) можно добавлять только поверх восстановленного baseline.

## 5. Anti-degradation check

Для каждого из двух anchor cases проверка должна ответить:

1. Все ли старые подразделы сохранены, интегрированы или явно перенесены?
2. Не исчезли ли конкретные механизмы, роли, команды, артефакты, ограничения и цены?
3. Не заменены ли фактические детали общими пересказами?
4. Не стали ли SPDD/Gas Town просто иллюстрациями вместо deep anchor cases?
5. Что добавлено из новых источников?
6. Что изменено ради новой SDLC-рамки?
7. Какие потери допустимы только после human gate?

Правило по умолчанию: если деталь была в старом сайте и не мешает новой структуре, она должна остаться.

## 6. Human gate

Перед утверждением SPDD и Gas Town частей пользователь должен получить:

- baseline extract;
- adapted draft;
- baseline-vs-draft comparison;
- список сохранённых деталей;
- список добавленных деталей;
- список возможных потерь или переносов.

Без этого нельзя считать раздел завершённым.
