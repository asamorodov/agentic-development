# SPDD rollback dossier-completeness experiment package report

Дата: 2026-06-12.

## Что сделано

Создан экспериментальный вариант SPDD article-writing package:

```text
work/atlas/packages/spdd_method_ATLAS_ARTICLE_rollback_dossier_completeness.zip
```

Пакет предназначен для сравнительного запуска против canonical `spdd_method_ATLAS_ARTICLE.zip`, собранного после dossier-backed completeness усиления.

## Что откатили

Откат относится только к экспериментальному SPDD-пакету и variant target-plan:

- убран hard gate `Dossier-backed completeness`;
- убрана обязательная coverage matrix по каждому существенному разделу досье;
- убран final blocker `relevant but untransferred`;
- убраны source-depth transfer-audit абзацы, добавленные последним completeness-усилением.

## Что сохранено

- SPDD-specific центральная ось: SPDD / OpenSPDD как сопровождаемый артефакт намерения;
- P01–P25 + Final;
- source-depth проходы;
- свободные доборные проходы;
- visual asset rules, local assets, external image candidates;
- отсутствие внутренних лимитов объёма;
- concept-first standalone article;
- self-contained package inputs.

## Почему это нужно

Сравнение двух ADR результатов показало риск: усиленное dossier completeness правило может увеличивать отчётность/ledger, но не обязательно увеличивает основной текст и может ухудшать последовательность читательской статьи. Этот пакет нужен для контрольного сравнения на SPDD.

## Проверка

- package `unzip -t` проходит;
- runner smoke-test: первый переход создаёт `01_P01_.md`;
- второй переход после фиктивного `spdd_method.md` создаёт `02_P02_article_contract_and_boundaries.md`;
- canonical SPDD target-plan и canonical SPDD package не заменены.
