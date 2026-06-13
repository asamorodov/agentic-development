# Remaining atlas article plans repair and package report

Дата: 2026-06-12.

## Scope

Исправлены оставшиеся необработанные atlas article target plans и собраны self-contained article-writing packages для:

- `spec_kit_method`
- `kiro_specs`
- `constitutional_sdd`
- `tdad_comparative`
- `gsd_open_gsd`
- `bmad_method`

SPDD, ADR, PWG and Gas Town already had targeted repairs and packages before this pass.

## Что исправлено в планах

- Убраны служебные следы manufactury-run (`S02/S03/S04`, `Post-import sync`, default `C5/A10 pending`) как активные инструкции.
- Каждый target-plan теперь звучит как самостоятельный рабочий контракт статьи, not blueprint copy.
- Усилены article contracts, центральные оси, reader questions and negative boundaries for each article.
- `P04`–`P08` развернуты как article-specific source-depth цепочки, not grouped generic ranges.
- Visual priorities уточнены per article: local assets insert-or-explain, dossier image candidates disposition, external-real candidates inline + bottom asset-pass queue.
- Dossier-backed completeness rule сделан operational in `P03`, `P04`–`P08`, `P09`–`P10`, and `Final`.
- C5/A10 are current read-only context, not generic sync debts.
- Prompt ranges are expanded into explicit `P01`–`P25` records, ready for package manufacture.

## Packages

| Article id | Package | Records | Target outputs | Bundled read-only inputs |
| --- | --- | ---: | ---: | ---: |
| `spec_kit_method` | `spec_kit_method_ATLAS_ARTICLE.zip` | 26 | 9 | 62 |
| `kiro_specs` | `kiro_specs_ATLAS_ARTICLE.zip` | 26 | 9 | 61 |
| `constitutional_sdd` | `constitutional_sdd_ATLAS_ARTICLE.zip` | 26 | 9 | 62 |
| `tdad_comparative` | `tdad_comparative_ATLAS_ARTICLE.zip` | 26 | 9 | 61 |
| `gsd_open_gsd` | `gsd_open_gsd_ATLAS_ARTICLE.zip` | 26 | 9 | 52 |
| `bmad_method` | `bmad_method_ATLAS_ARTICLE.zip` | 26 | 9 | 61 |

## Проверки

- Every package has 26 gated records (`P01`–`P25` + `Final`).
- Every package is self-contained and bundles exact read-only inputs from its plan.
- `unzip -t` passed for all six packages.
- Smoke-test passed for first and second runner transitions for all six packages.
- The overlay was control-applied to the original `git.zip` baseline.

## Остаточные долги

Результаты статей ещё не выполнялись and not imported. Перед запуском каждого package желательно сделать human review of the corresponding target plan, but there are no mechanical blockers known after this pass.
