# spdd_method_image_plan

Статус: P11 visual asset pass 1 — local assets.

Все перечисленные ниже файлы классифицированы как `local_image_asset`: они уже находятся в `content/assets/theory-images/` и вставлены в статью через `<figure class="image-asset"><img ...></figure>`. Путь в основном тексте дан относительно `work/atlas/articles/spdd_method.md`: `../../../content/assets/theory-images/<file>`.

## Inline placements

| Asset | Status | Placement | Why it is placed there |
| --- | --- | --- | --- |
| `content/assets/theory-images/fowler-spdd-overview.svg` | `local_image_asset`, inserted | After the opening definition of SPDD and before «Как читать эту статью». | Supports the central thesis that prompt becomes a versioned/reviewable delivery artifact. |
| `content/assets/theory-images/fowler-spdd-reasons-canvas.svg` | `local_image_asset`, inserted | In «REASONS Canvas как рабочий контракт», after the first REASONS-anatomy paragraph. | Shows the seven-part Canvas structure where the article explains the sections. |
| `content/assets/theory-images/fowler-spdd-analysis-review.png` | `local_image_asset`, inserted | In «Как пример с биллингом раскладывается по Canvas». | Grounds the billing example in a real source screenshot of edge cases and technical risks. |
| `content/assets/theory-images/fowler-spdd-workflow.svg` | `local_image_asset`, inserted | In «Рабочий процесс OpenSPDD», after the opening workflow paragraph. | Supports the workflow as a loop of analysis, prompt asset, code, validation, review and sync rather than a command gallery. |
| `content/assets/theory-images/fowler-spdd-api-test-script.png` | `local_image_asset`, inserted | In «Свидетельства поведения и ревью по намерению», immediately after the `/spdd-api-test` explanation. | Shows the human-reviewable test-case overview before execution. |
| `content/assets/theory-images/fowler-spdd-api-test-results.png` | `local_image_asset`, inserted | In the same evidence section, after the paragraph about artifact address and reviewability. | Shows expected/actual/result evidence after execution. |
| `content/assets/theory-images/fowler-spdd-code-review.svg` | `local_image_asset`, inserted | In the evidence/review section, after the `/spdd-code-review` explanation and before triage. | Shows review as a fork into prompt update versus code/sync adjustment. |
| `content/assets/theory-images/fowler-spdd-prompt-update.png` | `local_image_asset`, inserted | In «`prompt-update` и `sync`», after the minimal prompt-update paragraph. | Shows an accepted billing change written back into the prompt artifact. |

## Dossier candidate disposition

| Dossier candidate | Disposition |
| --- | --- |
| `fig-fowler-spdd-overview` | Inserted via local asset `fowler-spdd-overview.svg`. |
| `fig-fowler-spdd-рабочий процесс` / workflow | Inserted via local asset `fowler-spdd-workflow.svg`. |
| `fig-fowler-reasons-canvas` / REASONS Canvas | Inserted via local asset `fowler-spdd-reasons-canvas.svg`. |
| `fig-fowler-spdd-api-test-script` | Inserted via local asset `fowler-spdd-api-test-script.png`. |
| `fig-fowler-spdd-api-test-results` | Inserted via local asset `fowler-spdd-api-test-results.png`. |
| `fig-fowler-spdd-code-review` | Inserted via local asset `fowler-spdd-code-review.svg`. |
| `fig-fowler-spdd-prompt-update` | Inserted via local asset `fowler-spdd-prompt-update.png`. |
| `fig-spdd-analysis-review` / billing edge cases and risks | Inserted via local asset `fowler-spdd-analysis-review.png`. |
| `fig-openspdd-repo-vs-feature-artifacts` | Deferred as `editorial_visual_idea`; no local image asset exists in this pass. |
| `fig-spdd-prompt-code-evidence-sync` | Deferred as `editorial_visual_idea`; partly superseded by `fowler-spdd-workflow.svg` and the inserted API-test/code-review/prompt-update assets. |
| `fig-spdd-context-ingestion-gate` | Deferred as `editorial_visual_idea`; no local image asset exists in this pass. |
| `fig-spdd-risk-traceability` | Deferred as `editorial_visual_idea`; risk is currently covered by prose and prompt-update/sync assets. |
| `fig-spdd-reverse-lifecycle` | Deferred; `/spdd-reverse` remains README-level in the article because the v0.4.9 optional template was not verified in previous source-depth pass. |
| `fig-spdd-daily-planner-loop` | Deferred; daily planner remains a short application signal and has no local image. |
| `fig-spdd-integration-surface` | Deferred; no local image asset exists in this pass. |
| `fig-spdd-code-review-report`, `fig-openspdd-code-review-drift`, `fig-spdd-review-table` | Deferred as possible future synthetic or external candidates; current local `fowler-spdd-code-review.svg` already supports the correction-lane argument. |
| `fig-spdd-api-test-artifact`, `fig-spdd-api-test-shell` | Superseded by inserted local API-test script/results screenshots. |
| `fig-spdd-two-review-lanes`, `fig-spdd-two-correction-lanes`, `fig-spdd-correction-lanes-simple` | Superseded for now by `fowler-spdd-code-review.svg` and `fowler-spdd-prompt-update.png`; could be revisited only if a later synthetic figure pass is explicitly requested. |

## Notes for later passes

- The figures are intentionally distributed near the arguments they support. They should not be moved into a gallery.
- Captions are public-facing; they do not contain executor notes or asset-pass metadata except machine-readable `data-asset-status` and `data-repo-path` attributes.
- If a later site assembly pass rewrites paths, preserve `data-repo-path` as the source of truth.
- Do not replace these local images with text tables; visual-assets rule requires preserving ready local image assets.

## P12 — внешние реальные кандидаты

| Кандидат | Классификация | Решение | Источник | Предлагаемый локальный путь |
| --- | --- | --- | --- | --- |
| `fig-ext-openspdd-plan-vs-reasons-canvas` | `external_real_image_candidate` | Вставлен как inline placeholder `external-real-candidate` и продублирован в нижнем разделе `Внешние изображения для asset-pass`; остаётся на asset-pass. | Таблица OpenSPDD README “Why OpenSPDD?”, где обычные планы сравниваются с REASONS Canvas. | `content/assets/theory-images/openspdd-plan-vs-reasons-canvas.png` |
| `fig-ext-openspdd-code-review-report` | `external_real_image_candidate` | Вставлен как inline placeholder `external-real-candidate` и продублирован в нижнем разделе `Внешние изображения для asset-pass`; остаётся на asset-pass. | Раздел шаблона OpenSPDD `/spdd-code-review` с формой выходного отчёта. | `content/assets/theory-images/openspdd-code-review-report.png` |
| `fig-ext-openspdd-sync-bidirectional-flow` | `external_real_image_candidate` | Вставлен как inline placeholder `external-real-candidate` и продублирован в нижнем разделе `Внешние изображения для asset-pass`; остаётся на asset-pass. | Диаграмма двунаправленной синхронизации из шаблона OpenSPDD `/spdd-sync`; контекст риска — из design philosophy. | `content/assets/theory-images/openspdd-sync-bidirectional-flow.png` |
| `fig-ext-openspdd-repo-vs-feature-artifacts` | `editorial_visual_idea` | Не вставлен; первоисточник содержит полезную прозу, но не содержит реального изображения или таблицы, подходящих для внешнего реального кандидата. | OpenSPDD design philosophy. | `content/assets/theory-images/openspdd-repo-vs-feature-artifacts.png` |
| `fig-spdd-reverse-lifecycle` | `deferred_source_gap` | Не вставлен; `/spdd-reverse` остаётся в статье только на уровне README, потому что пробел по источнику шаблона сохраняется. | OpenSPDD README. | `content/assets/theory-images/openspdd-reverse-lifecycle.png` |

### P12 notes

- В P12 изображения не скачивались. В Final-проходе три полезных внешних кандидата возвращены в статью как package placeholders `external-real-candidate` и продублированы в нижнем разделе `Внешние изображения для asset-pass`, потому что финальный blueprint требует подготовить точную очередь для будущего asset-pass.
- Локальные ассеты Fowler/Thoughtworks остаются основным встроенным визуальным слоем, пока эти кандидаты не пройдут скачивание, проверку прав и качества.
- Внешние кандидаты отражены в `spdd_method_external_image_queue.md`; нижний раздел статьи восстановлен в Final-проходе как временный asset-pass список, а не как публикационная иллюстрация.

## P13 synthetic figures

| Candidate | Classification | Usefulness gate | Disposition | Placement |
| --- | --- | --- | --- | --- |
| `fig-spdd-artifact-ownership-boundary` | `synthetic_figure` | Passes: it explains a nontrivial boundary between REASONS Canvas, evidence artifacts, ADR, repo-level instructions and persistent work graph. This boundary is not covered by the local Fowler assets or by the P12 external candidates. | Inserted inline as an HTML table figure. | In `Где SPDD заканчивается`, after the paragraph that states the artifact-ownership test. |
| `fig-spdd-wrong-canvas-risk` | `editorial_visual_idea` | Rejected for this pass: the failure chain is already covered in prose and would risk duplicating the `Сценарии сбоев` section. | Not inserted. | — |
| `fig-spdd-fowler-vs-openspdd-boundary` | `editorial_visual_idea` | Rejected for this pass: local Fowler/Thoughtworks assets and P12 OpenSPDD placeholders already cover the source/practice split; a new diagram would mostly restate prose. | Not inserted. | — |
| `fig-spdd-prompt-code-evidence-sync` | `editorial_visual_idea` | Rejected for this pass: the workflow, API-test, code-review, prompt-update and P12 sync candidates already cover the lifecycle. | Not inserted. | — |

### P13 notes

- The inserted synthetic figure is public-facing, not a replacement for a local or external source image.
- No synthetic figure was created for risks already covered by real/source assets.
- В статье теперь одна авторская схема; весь оставшийся встроенный визуальный материал опирается на локальные ассеты из источников. Внешние реальные кандидаты остаются в сопроводительных очередях до проверки ассетов.

## P23 article sync

- Текущая статья содержит локальные source-backed изображения, одну синтетическую схему и три inline placeholders для внешних реальных кандидатов, ожидающих asset-pass.
- Нижний временный раздел `Внешние изображения для asset-pass` восстановлен в Final-проходе, чтобы пакет соответствовал atlas article blueprint; перед публикацией его нужно заменить локализованными ассетами или удалить после решения по кандидатам.
- `spdd_method_external_image_queue.md` остаётся authoritative queue для внешних кандидатов; inline placeholders и нижний раздел только зеркалят три кандидата, которые полезны текущей статье.
- Подписи в основном тексте остаются читательскими; служебные статусы допустимы только в machine-readable атрибутах локальных `<figure>`.


## Final verification visual sync

- Основной текст содержит 8 локальных image assets, 1 синтетическую таблицу и 3 внешних real-image placeholders.
- Три внешних кандидата (`fig-ext-openspdd-plan-vs-reasons-canvas`, `fig-ext-openspdd-code-review-report`, `fig-ext-openspdd-sync-bidirectional-flow`) имеют inline `<figure data-asset-status="external-real-candidate">`, нижний раздел `Внешние изображения для asset-pass` и запись в external image queue.
- Два кандидата (`fig-ext-open-spdd-command-index`, `fig-ext-gh-aw-daily-issue`) остаются rejected-for-now: первый слишком похож на справочник команд, второй слишком project-specific.


## Patch: localized source-excerpt assets

Three previous external-real placeholders are now represented by local SVG source-excerpt assets:

| Figure | Local asset | Source basis |
|---|---|---|
| `fig-openspdd-plan-vs-reasons-canvas` | `content/assets/theory-images/openspdd-plan-vs-reasons-canvas.svg` | OpenSPDD README Plan vs REASONS Canvas comparison |
| `fig-openspdd-code-review-report` | `content/assets/theory-images/openspdd-code-review-report.svg` | OpenSPDD `/spdd-code-review` template report structure |
| `fig-openspdd-sync-bidirectional-flow` | `content/assets/theory-images/openspdd-sync-bidirectional-flow.svg` | OpenSPDD `/spdd-sync` template sync flow and Prompt Sync Plan |

These are rendered source excerpts, not screenshots. Publication readiness still requires a final source/rights/quality check, but the article no longer carries empty inline external placeholders for these three nodes.
