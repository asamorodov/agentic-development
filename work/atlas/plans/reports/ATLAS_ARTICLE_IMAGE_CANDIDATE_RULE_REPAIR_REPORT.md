# Atlas article image-candidate rule repair report

Date: 2026-06-12

## Scope

Updated the visual/image handling rules for atlas article target-group plans after review of `adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`.

The defect was that article plans generally required local assets and external-real candidates, but did not reliably force the future article-writing package to start from the main dossier's own image-candidate section, such as `## Кандидаты на иллюстрации`. This meant that already collected real image candidates from dossiers could be missed, even while new external images were searched.

## Changes made

- Updated all 10 atlas article target-group plans in `work/atlas/target-group-plans/`.
- Updated `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`.
- Updated `protocols/rules/visual-assets-and-figures.md`.
- Updated `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` so future plan-generation runs preserve the same rule.
- Rebuilt `work/atlas/packages/adr_method_ATLAS_ARTICLE.zip` and exported the matching `/mnt/data/adr_method_ATLAS_ARTICLE.zip`.

## New rule

For atlas article packages, visual work must use three sources:

1. local asset catalogs and manifests;
2. repository-level external image candidate catalogs;
3. the main dossier's own image-candidate section.

For every image candidate listed in the main dossier, the future article-writing package must record a disposition in `<article_id>_image_plan.md`:

- `inserted_inline_external_placeholder`;
- `external_queue_only`;
- `deferred`;
- `rejected`;
- `superseded_by_local_asset`;
- `not_found_in_source`.

If the candidate is useful in the article, it must be placed as an inline `<figure data-asset-status="external-real-candidate">` at the point of use, mirrored in the bottom section `Внешние изображения для asset-pass`, and recorded in `<article_id>_external_image_queue.md`.

Relevant local assets now follow insert-or-explain: insert as `<figure><img ...></figure>` or explicitly reject with reason in image plan.

## ADR package rebuild

The ADR article package was rebuilt after updating the ADR target plan.

Validation:

- 26 gated records: P01–P25 plus Final.
- P11–P13 prompt block now reads `work/dossiers/ADR_METHOD_DOSSIER.md` and includes the dossier-candidate disposition rule.
- Final verification includes dossier image candidate disposition checks.
- Package includes exact read-only inputs and remains self-contained.
- Smoke-test first and second runner transitions passed.

## Remaining notes

This repair changes the plans and the ADR package. It does not modify already-written atlas articles, because they do not exist yet. Other article packages should be built or rebuilt from the updated target plans when needed.
