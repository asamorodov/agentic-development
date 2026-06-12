# A9 figure candidates

Статус после composition / visual / style repair: основной A9 больше не хранит все кандидаты inline. В тексте оставлены только четыре фигуры, которые действительно поддерживают нетривиальные различения A9. Остальные кандидаты сохранены здесь как side/atlas material, merged или rejected for main flow.

## Inline in `A9_lifecycle_repair.md`

| Figure id | Type | Decision | Why it remains inline |
|---|---|---|---|
| `fig-a9-post-merge-repair-loop` | `local_image_asset` | kept inline | Локальный Fowler/Thoughtworks asset показывает continuous feedback / drift sensors / harness update и работает как внешний визуальный якорь для всего A9. Подпись очищена от recovery-служебности. |
| `fig-a9-stale-map-wrong-next-action` | `synthetic_figure` | kept inline | Нетривиальная причинная цепочка: устаревший контекст делает ошибку агента рациональной. Это центральная мысль A9, плохо заменяемая одним абзацем. |
| `fig-a9-advisory-memory-vs-enforceable-guardrail` | `synthetic_figure` | kept inline | Удерживает важную границу: memory/rule подсказывают, skill оформляет повторяемую процедуру, hook/permission/gate ограничивают действие. |
| `fig-a9-migration-oracle-repair-evidence` | `synthetic_figure` | kept inline | Миграционный пример легко съезжает в “удалить старый путь”; схема удерживает требование внешней поверхности сравнения и решения владельца. |

## Removed from inline / merged / deferred

| Former figure | Type | Decision | Reason |
|---|---|---|---|
| `fig-a9-artifact-freshness-matrix` | `synthetic_figure` | removed from inline; deferred to technical atlas or sidebar | Матрица полезна как authoring/control surface, но в основном A9 возвращает текст к чек-листовой интонации. Смысл оставлен в прозе про spec/ADR/memory/skill/hook/PWG. |
| `fig-a9-feedback-signal-router` | `synthetic_figure` | merged into prose and opening loop | Дублировала основную repair-loop логику и перегружала середину фрагмента. |
| `fig-a9-repair-target-selected-by-signal` | `synthetic_figure` | removed from inline; possible sidebar | Таблица полезна как контрольный конспект, но слишком дидактична для основного потока и повторяет финальный раздел. |

## Local asset decision

`content/assets/theory-images/fowler-harness-continuous-feedback.png` остаётся единственным реальным image asset в основном A9. Он вставлен как `<figure class="image-asset">` с repo-relative truth in `data-repo-path` and public caption. Никакие реальные внешние картинки не были перерисованы в текстовые схемы.

## External real image candidates still deferred

Следующие реальные или source-table candidates из общего asset catalog остаются вне основного A9 до отдельного asset-pass / rights-check / quality-check:

- `ext-adr-nygard-minimal-adr`
- `ext-adr-madr-template-confirmation`
- `ext-adr-aws-lifecycle`
- `ext-adr-pact-can-i-deploy`
- `ext-adr-argo-analysis-template`
- `ext-adr-sync-marketplace`
- `ext-tdflow-workflow-fig1`

Причина: A9 сейчас должен объяснить repair loop, а не превращаться в визуальный каталог ADR/release/tooling surfaces. Если эти изображения понадобятся, их нужно локализовать и вставлять как реальные assets, а не заменять синтетическими суррогатами.

## Readiness note

Current readiness: `ready_with_known_debts`. Визуальный слой теперь соответствует правилам: local asset preserved as image, synthetic figures kept only when nontrivial, deferred candidates documented. Оставшийся долг — финальный atlas/sidebar decision for release/ADR-specific visuals.
