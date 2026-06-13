# BMAD Method — open questions

Статус: P26 завершил guarded final style pass; текущие живые долги обновлены, исторические вопросы сохранены отдельно.

## Текущие живые долги после P26

1. **Свежесть источников.** Перед публикацией нужно проверить текущие версии BMAD, имена рабочих процессов, релизные изменения, структуру `_bmad/`, `_bmad-output/`, `manifest.yaml`, `bmad-prd`, `bmad-spec`, `bmad-ux`, web bundles, `bmad-automator`, `bmad-method-ui`, инструменты Official Modules и TEA/Enterprise.
2. **Asset-pass для Workflow Map.** Официальная Workflow Map остаётся единственным внешним реальным кандидатом: нужны скачивание или иной способ локализации, проверка прав, качества, атрибуции и решение по публичной вставке.
3. **Решение для публичной сборки по нижнему asset-разделу.** Нижний раздел «Внешние изображения для asset-pass» нужен pipeline-у, но перед публичной сборкой нужно решить, остаётся ли он в статье или переносится в companion/asset catalog.
4. **Терминология и точные labels из источников.** P25–P26 убрали основные кальки и шероховатые обороты, сохранив точные BMAD labels (`story`, `review`, `Quick Flow`, `Workflow Map`, `project-context.md`, YAML-статусы, `bmad-checkpoint-preview`). Перед публикацией нужен только финальный source-refresh, а не новый style rewrite.
5. **Плотность таблиц и синтетических фигур.** `fig-bmad-context-cascade`, таблица файлов восстановления, таблица человеческих контрольных точек и таблица brownfield-сканирования пока полезны, но финальный structure/style pass должен проверить, не дают ли они чрезмерную плотность.
6. **Согласованность между статьями.** Нет generic `C5/A10 sync pending`; остаются только конкретные будущие проверки якорей и терминов при сборке всего атласа и соседних статей.

## Закрыто или понижено до истории в P23–P26

- Раннее расположение контрактного раздела закрыто P20: boundary-блок стоит после минимального примера.
- Резкий переход от контрактного раздела к установке закрыт P21: добавлен связующий абзац.
- Служебная подпись Workflow Map закрыта P22: inline caption стал публичным.
- Ссылка на P12 в нижнем статусе статьи закрыта P22: в публичном тексте оставлен только текущий asset-pass долг.
- Generic C5/A10 pending не существует; C5 и A10 остаются read-only context, а конкретных несоответствий P23 не нашёл.

- P24 закрыл ранний style debt про «профиль, где артефакты имеют приоритет»: формулировка стала прямее и больше не звучит как псевдотермин.
- P24 снял часть метафорических дефектов: «театр», «красивая машина», «кормить следующего агента», «токенная цена» и «ложная полнота» заменены на более точные формулировки.

- P25 закрыл вопрос, оставлять ли `working source of truth`: в публичной статье теперь используется русская формула «артефакт задаёт рамку работы» и «ведущий артефакт».
- P25 снял style debt по слову «поверхность» в recovery-таблице: заголовок стал «Файл или место».

- P26 закрыл последние явные русско-английские шероховатости в публичной статье: «слеш-команды», «функция восстановления», более прямое описание TEA/Enterprise и theory-раздела.

## Исторические заметки предыдущих проходов

Ниже сохранена история вопросов по проходам. Текущими блокерами считаются пункты из верхнего раздела; исторические вопросы могут быть закрыты более поздними проходами.

## Source freshness and version questions

1. Насколько стабильны имена skill-файлов и структура `_bmad/` в текущей версии BMAD после v6.7/v6.8? P01 сохранил версионные оговорки, но не выполнял web-refresh.
2. Как в текущей документации разводятся `bmad-prd`, legacy PRD shims и возможные v7 changes?
3. Как именно текущий BMAD отделяет BMM, BMad-CORE и broader BMad Ecosystem? P01 использует официальную modules boundary из досье, но final article needs check.
4. Какой текущий status `bmad-spec`, `bmad-ux`, web bundles, `bmad-automator` and `bmad-method-ui`? These are release-sensitive surfaces.
5. Насколько Enterprise Security/DevOps exists beyond TEA in current BMAD modules? P01 treats TEA as the main sourced Enterprise extension.

## Adoption and boundary questions

1. Насколько часто команды реально используют full BMAD versus Quick Flow or external automators? Dossier signals are anecdotal; P01 did not use them as evidence.
2. Do community reports about token cost, documentation overhead and messy agent files support stable failure-mode claims? Requires separate source pass.
3. Should `bmad-investigate` be presented as core BMAD implementation workflow or optional implementation-side workflow? P01 includes it but marks it as a separate diagnostic branch.
4. How much TEA detail belongs in a BMAD article without making readers think Enterprise is the default BMAD path?
5. Should `bmad-spec` stay inside BMAD article or be cross-linked to a separate Spec Kit / specification-methods route later?

## Visual / asset questions

1. What rights and attribution apply to the official Workflow Map Diagram?
2. Should the Getting Started tree be converted into a synthetic figure, or is the code block enough?
3. Does the article need a Quick Dev boundary figure, or is the explanation sufficient?
4. Should Brownfield Document Project get its own figure, or would that shift the article toward a handbook?
5. Should BMAD vs Gas Town visual boundary wait until Gas Town article/source sync? P01 says yes.


## P02 concrete boundary debts

1. GSD boundary should be rechecked against current Open GSD public docs before final publication, because `gsd-core`, `gsd-pi`, namespace routing and verification surfaces are version-sensitive.
2. PWG boundary currently uses Beads as the primary public work-graph example. A future PWG article should decide whether Beads remains the canonical example or one example among several durable work graph systems.
3. Gas Town boundary should be synchronized with the future Gas Town article so BMAD does not over-describe Mayor/Town/Rig/Crew/Polecats vocabulary or hide the Beads dependency layer.
4. Spec Kit, Kiro Specs and SPDD boundaries were added from allowed dossiers and their public source links. A future source pass should refresh exact command/file names before cross-article linking.
5. TDAD is named in the P02 boundary instruction, but no TDAD dossier was included in the allowed inputs for this pass. The main article mentions only `TDAD-подобные` test-first approaches as a boundary placeholder and does not introduce TDAD-specific facts.
6. ADR boundary is now explicit, but the BMAD article should not import agentic ADR tooling details; those belong in the ADR article unless needed to explain BMAD architecture handoff.
7. No concrete C5/A10 inconsistency was found in P02. Therefore there is no generic `C5/A10 pending` debt.


## P04 open questions

1. The new handoff table partly overlaps with `fig-bmad-context-cascade`. A later editorial/visual pass should decide whether both are useful or whether the figure should absorb the table’s input/output logic.
2. The handoff wording keeps several source terms (`story`, `review`, `retrospective`, `correct-course`, `sprint-status`) because they are artifact/workflow names. A later language pass should translate ordinary English around them without changing names of files, commands or workflows.


## P05 open questions

1. The file-recovery table introduces another dense table early in the article. Later structure pass should decide whether it should remain as-is, be shortened, or be moved after the core chain.
2. The recovery-surface framing depends on current BMAD paths (`_bmad/`, `_bmad-output/`, manifest path, config fallback). These are explicitly version-sensitive and must be refreshed before publication.
3. The article now says story files recover execution state through fields such as `baseline_commit`, Dev Agent Record, File List, Change Log and Status. Later source-depth pass should verify exact field names if the BMAD skill changes.


## P06 open questions

1. Brownfield scan-level table may be useful enough to remain, but it increases table density. Later visual/editorial pass should decide whether to convert it into a diagram or compress it.
2. Exact `project-scan-report.json` fields and `documentation-requirements.csv` schema remain source-refresh targets; P06 keeps them at concept/article level.
3. Stale brownfield documentation is now a stronger failure mode. Later failure-mode pass should check whether it duplicates or should merge with the existing stale `project-context.md`/old artifacts discussion.


## P07 open questions

1. The human-gates decision table may be useful but increases structural density. Later visual/editorial pass should decide whether to keep, compress or turn it into a figure.
2. PRD validation pipeline and report shape are explicitly version-sensitive; source refresh must verify current `bmad-prd Validate` naming and output.
3. P07 uses investigation/correct-course/retrospective as repair gates; later article-shape pass should check whether these are overrepresented relative to core BMAD workflow.


## P08 open questions

1. Token/context cost is now included as a structural limit, not as a measured statistic. A future allowed source pass can evaluate community/issue reports before any stronger claim.
2. Module confusion is now explicit. Final publication must refresh Official Modules and Releases so BMM/core/TEA/web bundles/automator/UI status is current.
3. TEA/Enterprise is kept as extension. Later article-shape pass should verify that TEA detail remains proportionate and does not swallow base BMAD.

## P09 open questions

1. Quick Dev is now explained as a compressed lifecycle, but exact current generated artifacts still need refresh: short spec trace, review hints and `deferred-work.md` location/format.
2. The Quick Dev boundary figure is less necessary after P09 prose expansion, but a later visual pass should decide whether a compact mini-lifecycle diagram would replace some text.
3. The failure-layer paragraph overlaps conceptually with the general lifecycle-repair section. Later structure pass should decide whether to keep both or cross-reference one from the other.

## P10 open questions

1. The new “artifact that frames the next step” section may overlap with the intro, the context-cascade figure and «Практический способ читать BMAD». A later structure pass should decide whether to keep all three or merge the repeated reader guidance.
2. The four artifact properties are interpretive synthesis, not source vocabulary. Later fact-check pass should ensure no reader mistakes them for official BMAD terminology.
3. The section improves concept-first readability, but a later language pass should decide whether to keep “artifact that frames the next step” as a borrowed term or translate it more fully.

## P11 open questions

1. No ready local BMAD image exists in the current asset catalog. The official BMAD Workflow Map remains the priority asset-pass target.
2. A future BMAD-specific local asset could be created or captured for `_bmad/` + `_bmad-output/`, sprint-status state, brownfield document-project flow or TEA/release-gate visuals, but P11 did not create synthetic replacements.
3. Fowler harness visuals should not be imported into this BMAD article unless a later cross-article comparison explicitly explains the boundary between harness engineering and BMAD as an SDLC method profile.

## P12 open questions

1. The official Workflow Map still needs a rights/quality/attribution/localization decision before publication.
2. If the Workflow Map page is HTML/SVG-like rather than a simple downloadable image, the asset pass should decide whether to capture it, rebuild an original localized version, or keep a live link only.
3. No new real external BMAD visuals were found/selected in P12; later synthetic visual work should be deliberate rather than disguised as external asset recovery.

## P13 open questions

1. Later visual editing should decide whether to consolidate existing tables into figures instead of adding new visuals.
2. If Quick Dev, brownfield, Correct Course or TEA grows into a separate handbook/fieldbook page, their deferred diagrams may become more useful there than in the BMAD concept article.
3. Cross-boundary visuals with GSD/PWG/Gas Town should wait for cross-article sync to avoid creating a misleading comparison.

## P14 open questions

1. The new audit-report example may overlap with the invariant and the practical-reading section. A later structure pass should decide whether to keep all three or compress one.
2. The example uses an invented scenario. Final editing must keep it clearly illustrative, not sourced as an official BMAD case.
3. If the article becomes too long, the example should be shortened rather than removed, because it is the main standalone bridge for concept-first readers.

## P15 open questions

1. The “role theater” warning appears in both the invariant and role sections. Later structure/style pass should keep the stronger version and remove unnecessary repetition.
2. Stale artifact risk now appears in invariant, project-context, brownfield and failure-mode sections. Later edit should ensure it reads as one mechanism, not four warnings.
3. Mode-confusion wording should be rechecked against A10 and current BMAD docs before final publication.

## P16 open questions

1. Final cross-article sync should verify that semantic backlink labels (`00`, `A3`, `A5`, `A7`, `A9`, `A10`, `C5`) match the final published theory structure and anchors.
2. The main article now names theory questions explicitly. A later style pass should ensure this reads as local explanation, not as an abstract theory chapter.
3. The phrase “artifact that frames the next step” remains an interpretive synthesis. Final edit should either keep it consistently or choose a Russian equivalent throughout.

## P17 open questions

1. A second language pass should decide how consistently to handle `story`, `epic`, `review`, `retrospective`, `brownfield`, `checkpoint preview` and `traceability`: several are stable source/BMAD terms, but the article should not look half-translated.
2. Source labels and official workflow names were intentionally left in English where exact names matter; final copyedit should check that readers can distinguish names from ordinary prose.
3. The article now uses “профиль, где артефакты имеют приоритет” for artifact-first. Later style pass may choose a shorter fixed Russian equivalent if the atlas standardizes one.

## P18 — открытые вопросы

- Финальный редакторский проход должен сохранить source-specific labels (`story`, `review`, `Quick Flow`, `Workflow Map`, `project-context.md`, статусы YAML) там, где они являются рабочими именами BMAD, но не оставлять английские связки в обычном объяснении.
- Нижний asset-pass section уже переведён на русский, но фактическая asset-задача не закрыта: права, скачивание, качество, локализация и атрибуция Workflow Map остаются отдельным проходом.
- P18 не решал долги свежести по релизам, командам, путям и документации BMAD. Они остаются для финальной проверки источников и актуальности.

## P19 — открытые вопросы после первого редакторского прохода

- Следующий редакторский проход должен проверить, не слишком ли ранний контрактный раздел перегружает читателя сравнением с соседними методами до того, как он увидел механику BMAD. P19 не переносил раздел, чтобы не ломать уже выстроенные границы.
- Четырёхвопросный критерий в практическом разделе усиливает standalone-ценность статьи; нужно следить, чтобы он не превратился в повтор инварианта без новой функции.
- Визуальный слой не изменён: новая проверка пока лучше работает текстом, а не отдельной схемой.

## P20 — открытые вопросы после второго редакторского прохода

- После перестановки контрактного раздела следующий проход должен проверить, не слишком ли резкий переход от сравнительных границ к установке.
- Сравнительные границы теперь идут после практического примера; нужно сохранить это преимущество и не вернуть boundary-блок в самое начало без причины.
- Визуальные решения не менялись, но финальный structure pass должен проверить, что Workflow Map действительно стоит после главной цепочки, а не после контракта.

## P21 — открытые вопросы после третьего редакторского прохода

- Финальные стилевые проходы должны решить, какие source labels оставлять латиницей в заголовках: `bmad-checkpoint-preview` явно нужен, а `retrospective` можно оставить как BMAD/source label или русифицировать в обычной прозе.
- После добавления перехода от контракта к установке structure pass должен проверить, что статья не стала слишком «маршрутной» и не объясняет собственную структуру больше, чем метод.

## P22 — открытые вопросы после public/article structure pass

- Финальный asset-pass должен решить, остаётся ли inline `external-real-candidate` placeholder в публичной версии или заменяется локальным `<figure><img ...></figure>` после скачивания и проверки прав.
- Нижний раздел «Внешние изображения для asset-pass» полезен для pipeline, но перед публичной сборкой нужно решить, показывается ли он читателю или остаётся companion/asset-catalog материалом.
- Синтетические фигуры пока проходят usefulness gate; финальный structure/style pass должен проверить, не дублирует ли `fig-bmad-context-cascade` соседнюю таблицу слишком близко.

## P23 — companion open-question sync note

P23 не добавил generic `C5/A10 sync pending`. Текущие блокеры находятся в верхнем разделе: свежесть источников, asset-pass для Workflow Map, решение о публичной сборке нижнего asset-раздела, терминология/source labels, плотность таблиц/фигур и согласованность между статьями.

## P24 style audit notes

P24 был selective pass, а не rewrite-pass. Текущие открытые вопросы после него остаются не про «переписать всё», а про финальную проверку точных labels, table/figure density и source freshness. Новых фактических или визуальных долгов проход не создал.

## P25 selective rewrite notes

P25 не создал новых фактических долгов. После него живыми остаются source freshness, Workflow Map asset-pass, решение по нижнему asset-pass разделу, финальная проверка точных labels и плотность таблиц/фигур.

## P26 guarded style notes

P26 не создал новых открытых вопросов. Остаются только внешние к стилю долги: source freshness, Workflow Map asset-pass, решение по нижнему asset-pass разделу, плотность таблиц/фигур и межстатейная согласованность.
