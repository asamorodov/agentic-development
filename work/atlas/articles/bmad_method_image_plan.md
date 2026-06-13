# BMAD Method — image plan

Статус: P26 завершил guarded final style pass; image plan не изменился.

| Candidate | Asset class | Disposition P01 | Где / что сделать | Причина |
| --- | --- | --- | --- | --- |
| Official Workflow Map Diagram | external_real_image_candidate | inline external placeholder retained; P22 public caption cleaned | `fig-bmad-workflow-map`; mirrored in `bmad_method_external_image_queue.md` and bottom section «Внешние изображения для asset-pass». | Главная реальная диаграмма источника: четыре фазы, роли, артефакты, Quick Flow и поток контекста. |
| Дерево вывода из Getting Started (`_bmad/`, `_bmad-output/...`) | source_table_or_code_fragment / possible synthetic_figure | deferred; no external screenshot | В статье представлен как code block, не как figure. Будущая компактная схема возможна только если даст новую объяснительную пользу. | Источник — текстовое дерево; нет причины превращать его в внешний screenshot. |
| Машина состояний sprint status | synthetic_figure_candidate | inserted_inline_synthetic_figure | `fig-bmad-sprint-state-machine` | Нетривиально помогает увидеть status lifecycle. Не заменяет известное внешнее изображение. |
| Диаграмма потока контекста PRD → architecture → story → dev → review | synthetic_figure_candidate | inserted_inline_synthetic_figure | `fig-bmad-context-cascade` | Центральная ось статьи; figure connects artifacts, preserved context, human check. |
| Диаграмма границы Quick Dev | synthetic_figure_candidate | still deferred after P09 | Possible future figure near Quick Flow section. | P09 prose now explains mini-lifecycle and scope/repair boundary; adding a figure now would likely increase visual density. |
| Диаграмма сжатия SPEC | synthetic_figure_candidate | deferred | Possible future figure in `bmad-spec` subsection or separate source note. | Useful but not central enough for P01 inline. |
| Диаграмма границы QA/TEA | synthetic_figure_candidate | deferred | Possible future figure in quality section. | Needs TEA/source freshness check before visual commitment. |
| Диаграмма brownfield-сканирования | synthetic_figure_candidate | deferred | Possible future figure in Brownfield section. | Good candidate for later visual pass after verifying document-project current outputs. |
| Диаграмма проверки Document Project | synthetic_figure_candidate | deferred | Possible future figure or merged with brownfield scan figure. | Avoid duplicate figures in P01. |
| Диаграмма решения Correct Course | synthetic_figure_candidate | deferred | Possible future figure in Correct Course section. | P01 prose includes checklist path; later pass can decide if visual helps. |
| Лестница доказательств расследования | synthetic_figure_candidate | deferred | Possible future figure in Investigation section. | Not central enough for primary draft; keep for later. |
| Диаграмма release gate для Enterprise TEA | synthetic_figure_candidate | deferred | Possible future figure in Enterprise/TEA section. | TEA is extension, not base BMAD; avoid overweighting article in P01. |
| Диаграмма компромисса стоимости и глубины BMAD | synthetic_figure_candidate | deferred | Possible future figure after adoption-friction/source check. | Needs external/community evidence if framed around cost; not in P01. |
| Диаграмма устойчивости BMAD vs Gas Town | synthetic_figure_candidate / cross-article | deferred | Do not draw in BMAD P01 without Gas Town dossier sync. | Boundary with Gas Town must not be asserted from BMAD dossier alone. |

## Inline figures created in P01

- `fig-bmad-workflow-map` — external real placeholder; must be downloaded/localized or rejected in future asset-pass.
- `fig-bmad-context-cascade` — synthetic figure; initial usefulness: central mechanism of artifact cascade.
- `fig-bmad-sprint-state-machine` — synthetic figure; initial usefulness: compact state lifecycle.

## P01 visual guardrails

- No external image was redrawn as a synthetic replacement.
- No local asset was available in the allowed inputs.
- Captions in the article are public-facing and do not expose local file bookkeeping except in the mandated bottom asset-pass queue.
- Later visual pass should check whether two synthetic figures are still both necessary after article structure revisions.


## P02 visual sync

P02 added article-boundary concepts but did not add, move or reject any inline image. The existing figures still serve the article contract:

- `fig-bmad-context-cascade` maps the positive contract: artifact-to-artifact context narrowing.
- `fig-bmad-sprint-state-machine` maps the minimal state layer and supports the PWG boundary by showing what BMAD does and does not model.
- `fig-bmad-workflow-map` remains the only external-real candidate.

No new GSD/PWG/Gas Town comparison figure was added in P02. A comparative visual could easily shift the BMAD article into ecosystem overview; defer until cross-article sync.


## P04 visual/table sync

P04 added an inline handoff table in the main article. It is not an external image candidate, but it is a structural visual element.

- Purpose: show each documentary handoff as input → output → usable context for the next contour.
- Relation to `fig-bmad-context-cascade`: overlapping but not identical. The table is source-depth / mechanism; the synthetic figure is conceptual. Later visual/editorial pass should decide whether both remain.
- No new image asset was introduced.


## P05 visual/table sync

P05 added a second inline table, “Файл или место / Что восстанавливает / Следующий шаг / Риск”. It is a structural Markdown table, not an image asset.

Watchpoint: the article now contains two dense mechanism tables before the existing figures. Later visual/editorial pass should check whether one table should be shortened or folded into a figure.


## P06 visual/table sync

P06 added an inline scan-level table in the Brownfield section. This is not an external image. It may become a future synthetic figure candidate if the article becomes too table-heavy.

New watchpoint: the article now has three significant tables/structured visuals plus two synthetic figures. Later visual pass should decide whether to convert the brownfield scan-level table into a compact diagram or leave it as prose/table.


## P07 visual/table sync

P07 added an inline decision map table under «Gates и человеческие решения». It is a Markdown table, not an external image.

Watchpoint escalated: early/middle article now contains multiple mechanism tables. Later visual pass should decide whether the human-gates table should become a compact “decision ladder” figure or remain as table.


## P08 visual sync

P08 added no new figures or tables. Existing deferred candidate “cost/depth tradeoff” remains deferred because P08 intentionally avoided using anecdotal cost reports as evidence. TEA release-gate figure remains deferred to avoid overweighting Enterprise.

## P09 visual sync

P09 added no new figure or table. The Quick Dev boundary diagram remains a deferred synthetic candidate, but its urgency decreased because the main text now explains the mini-lifecycle, `deferred-work.md` scope guard and layer-aware repair in prose. Keep this candidate only if a later visual pass reduces table density elsewhere or decides that Quick Flow needs a compact lifecycle diagram.

## P10 visual sync

P10 added a connective prose section and no new visual asset. A future synthetic overview diagram could show “artifact that frames the next step” movement across PRD → architecture → story → review/repair, but the existing `fig-bmad-context-cascade` already serves most of that function. Do not add another overview diagram unless a later visual pass removes or merges existing structural tables/figures.

## P11 local asset pass

Reviewed local assets from the required catalogs and the explicitly listed files:

| Local asset | Classification | Decision | Reason |
| --- | --- | --- | --- |
| `content/assets/theory-images/fowler-harness-overview.png` | `local_image_asset` | rejected for BMAD article | Shows Fowler harness engineering: guides, sensors, feedforward/feedback around a coding agent. Useful for a harness article, but not a BMAD-specific workflow/role/artifact surface. |
| `content/assets/theory-images/fowler-harness-templates.png` | `local_image_asset` | rejected for BMAD article | Shows harness templates by application topology. It does not show `_bmad/`, `_bmad-output/`, BMAD install output, BMAD workflows or stories. |
| `content/assets/theory-images/fowler-harness-change-lifecycle.png` | `local_image_asset` | rejected for BMAD article | Shows feedforward/feedback across a generic change lifecycle. It overlaps thematically with BMAD review/repair, but its source vocabulary is harness-specific and would blur article boundaries. |
| Other indexed local assets | `local_image_asset` / synthetic-from-other-articles | not inserted | The index contains SPDD, Beads, Gas Town, Humanlayer, OpenAI/Codex, Fowler and story assets, but no ready BMAD workflow map, BMAD role/artifact diagram, BMAD file tree, sprint-state image, brownfield flow, checkpoint/correct-course surface or TEA release-gate visual. |

No local image was inserted. Existing inline visuals remain: one external-real placeholder (`fig-bmad-workflow-map`) and two synthetic figures (`fig-bmad-context-cascade`, `fig-bmad-sprint-state-machine`).

## P12 external real image pass

P12 inspected dossier image candidates and the external-real candidate catalog. Results:

| Candidate class | P12 disposition | Reason |
| --- | --- | --- |
| Official BMAD Workflow Map Diagram | keep as inline `external-real-candidate` | It is the only real BMAD-specific source visual and already placed after the main chain. |
| Getting Started project tree | keep as text/code block; no external image | Better as a readable source-like tree than as screenshot. |
| Sprint status / context cascade | keep existing synthetic figures | These are article-authored explanations, not recovered source images. |
| Quick Dev / SPEC / QA-TEA / brownfield / Document Project validation / Correct Course / investigation / release gate | remain deferred synthetic/editorial candidates | No real external image identified in the dossier/source queue; creating them now would be a synthetic design pass, not external-asset pass. |
| BMAD cost-depth and BMAD vs Gas Town | remain deferred | Need stronger source/cross-article sync before visual commitment. |

No external image was downloaded. `fig-bmad-workflow-map` still needs rights/quality/attribution/localization before publication.

## P13 synthetic figure pass

No new synthetic figure was added. The current visual layer already has:

- one real external candidate: `fig-bmad-workflow-map`;
- two inline synthetic figures: `fig-bmad-context-cascade` and `fig-bmad-sprint-state-machine`;
- several dense inline mechanism tables from P04–P07.

Decision: every remaining synthetic candidate stays deferred. The strongest near-term candidate is not a new figure but a later consolidation: replace the brownfield scan-level table or the human-gates table with a compact diagram if the article becomes too table-heavy. Until then, adding another synthetic figure would violate the “rare, unusually useful, non-decorative” rule.

## P14 visual sync

P14 added a prose example, not a figure. No new visual candidate was created. If a future visual pass finds the example too long, it should first consider whether existing `fig-bmad-context-cascade` already supplies the needed visual model before creating a new scenario diagram.

## P15 visual sync

P15 added no figure. It strengthened failure-mode prose around the existing “artifact that frames the next step” invariant. No visual candidate was created because the same material is already served by `fig-bmad-context-cascade`, the sprint-state figure and prose.

## P16 visual sync

P16 added no figure, table or image. The semantic backlink matrix lives in the companion `theory_links`, not in the public article visual layer. No change to `fig-bmad-workflow-map`, `fig-bmad-context-cascade` or `fig-bmad-sprint-state-machine`.

## P17 visual sync

P17 changed captions and prose wording only. No figure, table, image status or asset path decision changed. Broken auto-replacement risks were checked for URLs, figure ids and local asset paths; `fig-bmad-workflow-map` and `fig-bmad-sprint-state-machine` remain intact.

## P18 — языковая синхронизация визуального слоя

P18 изменил только формулировки вокруг визуальных материалов. Placeholder для `fig-bmad-workflow-map` теперь по-русски описывает официальную диаграмму Workflow Map, сохраняя точное имя источника, роли, поток артефактов и статус `external-real-candidate`. Нижний раздел переименован в «Внешние изображения для прохода по ассетам». Новых изображений не добавлено, локальные изображения не вставлялись, решения по синтетическим фигурам не менялись.

## P19 — визуальная синхронизация после редакторского прохода

P19 не менял визуальную структуру статьи. Новая четырёхвопросная проверка в практическом разделе не требует отдельной схемы: она работает как короткий текстовый критерий и не оправдывает добавление новой synthetic figure. `fig-bmad-workflow-map`, `fig-bmad-context-cascade` и `fig-bmad-sprint-state-machine` остаются без изменения.

## P20 — визуальная синхронизация после перестановки разделов

P20 переставил контрактный раздел, но не менял расположение фигур. Основные визуальные элементы остаются привязаны к тем же смысловым местам: внешний кандидат Workflow Map после главной цепочки, синтетическая таблица сужения контекста рядом с этой цепочкой, минимальная машина состояния в разделе `sprint-status.yaml`. Новая схема не требуется.

## P21 — визуальная синхронизация после правки заголовков

P21 не менял фигуры, изображения или их расположение. Уточнение заголовков делает навигацию по статье яснее, но не создаёт новой визуальной потребности. Очередь Workflow Map и две синтетические фигуры остаются без изменений.

## P22 — public-structure visual sync

P22 проверил первый экран, порядок разделов, баланс текста и фигур и служебные подписи. `fig-bmad-workflow-map` остаётся inline `external-real-candidate`, но его caption больше не говорит «здесь нужна» и не содержит executor note о будущей проверке. Нижний раздел статьи теперь снова называется «Внешние изображения для asset-pass», а его статус не ссылается на P12. Новая фигура, локальный asset или внешний кандидат не добавлялись.

## P23 — image plan companion sync

P23 обновил текущие строки image plan: `fig-bmad-workflow-map` теперь описан как сохранённый inline external placeholder с публичной подписью после P22; нижний раздел статьи назван «Внешние изображения для asset-pass». Дерево Getting Started оставлено code block, а не screenshot. Текущая карта визуального слоя соответствует статье: один external-real candidate, две inline synthetic figures, остальные идеи deferred.

## P24 visual sync

P24 не добавлял, не удалял и не переставлял изображения. Точечные языковые правки не затронули `fig-bmad-workflow-map`, `fig-bmad-context-cascade` и `fig-bmad-sprint-state-machine`.

Watchpoint остаётся прежним: перед публичной сборкой нужно решить судьбу нижнего asset-pass раздела и проверить, не создают ли таблицы и две синтетические фигуры чрезмерную плотность.

## P25 visual sync

P25 не менял визуальные решения. Единственное синхронное уточнение: markdown-таблица восстановления в статье теперь называется через «Файл или место», а не через «поверхность». Это не создаёт нового image candidate и не меняет `fig-bmad-workflow-map`, `fig-bmad-context-cascade` или `fig-bmad-sprint-state-machine`.

## P26 visual sync

P26 не менял визуальные решения и не создавал новых candidates. `fig-bmad-workflow-map`, `fig-bmad-context-cascade` и `fig-bmad-sprint-state-machine` сохранены без изменения ID, места и функции.
