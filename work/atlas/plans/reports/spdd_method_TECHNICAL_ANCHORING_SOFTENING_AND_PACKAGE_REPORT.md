# SPDD technical-anchoring softening and package rebuild report

Дата: 2026-06-13

## Цель

Пользователь попросил изменить правила добора технической фактуры в режиме: сначала откатить разросшуюся спецификацию к состоянию после rollback, затем добавить только короткий мягкий ориентир про технические детали без жёстких определений, coverage matrix, `relevant but untransferred` gate и повторяющихся section-local checks.

Работа выполнена как cumulative overlay относительно пользовательского baseline `git(10).zip` с учётом ранее подготовленных стилевых правок SPDD/blueprint.

## Изменения

### Blueprint

Файл: `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`.

Изменён раздел `3.1`: прежняя `main-text-first / section-local enrichment` логика заменена на более короткую схему `Фактура без coverage-бюрократии`.

Новая логика:

- досье и первоисточники остаются основной базой статьи;
- жёсткая `dossier-backed completeness / relevant but untransferred` логика откатана;
- пакет не обязан доказывать полный обход досье статусами и disposition-таблицами;
- ключевые тезисы должны иметь достаточные технические опоры, если без них раздел превращается в общую прозу;
- ledger/image/open questions остаются companion-файлами для реальных решений, долгов и source gaps, а не заменой основного текста.

### SPDD target plan

Файл: `work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`.

Изменения:

- раздел `2.1` переписан под короткое правило `Фактура без coverage-бюрократии`;
- `P03` возвращён к rollback-like dossier inventory без coverage matrix;
- из `P04`–`P08` убраны повторяющиеся section-local enrichment checks;
- мягкий technical-anchoring ориентир оставлен только там, где он помогает не уйти в общий конспект: `P03`, `P08`, `P09` и `Final`;
- сохранены текущие стилевые правки: `P24 style defect audit`, `P25 selective natural rewrite`, `P26 guarded final human technical style`;
- сохранён порядок `language → repair/editorial → entry-sequence → companion sync → style tail`.

### START / status

`START.md` обновлён, чтобы текущим правилом для atlas article packages была не hard dossier completeness, а мягкая проверка технических опор в основном тексте.

### Package

Пересобран:

```text
work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip
```

Пакет содержит 27 gated records:

```text
P01–P26 + Final
```

## Проверки

- `unzip -t work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip` — passed.
- Smoke test first runner transition — `python q8v4m.py` creates `01_P01_primary_article_draft.md`.
- Smoke test second runner transition after minimal `work/atlas/articles/spdd_method.md` — creates `02_P02_article_contract_and_boundaries.md`.
- Payload audit — 27 records, ordered `P01`–`P26` + `Final`; `P17`/`P18` are language passes; `P24`/`P25`/`P26` are style audit / selective rewrite / guarded final style.

## Не выполнялось

- Сам article-writing package не запускался до конца.
- Текст `work/atlas/articles/spdd_method.md` не создавался и не редактировался в репозитории.
- Остальные atlas target plans/packages не пересобирались.

## Вывод

Это не возврат hard completeness и не чистый откат без защиты от общих формулировок. Текущая пробная схема: rollback-like source-depth/free-expansion process + короткий technical-anchoring ориентир, без матриц, жёстких disposition status и повторяющихся section-local gates.
