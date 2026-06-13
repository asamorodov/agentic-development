# TDAD Comparative — image plan

Статус: P22 image plan. Публичный entry-sequence стал problem-first, а визуальный слой приведён к `protocols/rules/visual-assets-and-figures.md`: релевантные external_real_image_candidate возвращены в статью как inline `<figure data-asset-status="external-real-candidate">` без служебных captions; нижний раздел `Внешние изображения для asset-pass` восстановлен.

## Current article visual state after P22

| Figure id / group | Current disposition | Source | Article placement | Why it is useful | Local path proposal / status |
| --- | --- | --- | --- | --- | --- |
| `fig-tdad-definition-overview` | inline `external_real_image_candidate` | `arxiv:2603.08806` figure 1 / TDAD overview | First-line PromptSmith/compiled-agent explanation | Shows line 1 as a separated pipeline rather than a generic prompt-improvement loop | Proposed: `content/assets/atlas-images/tdad/tdad-definition-overview.png`; localization/rights/quality pending |
| `fig-tdad-definition-mutation` | inline `external_real_image_candidate` | `arxiv:2603.08806` semantic mutation figure | MutationScore / MutationSmith explanation | Separates mutation intent, activation probing, killed/non-activating mutants and metric boundaries | Proposed: `content/assets/atlas-images/tdad/tdad-definition-mutation-pipeline.png`; localization/rights/quality pending |
| `fig-tdad-development-pipeline` | inline `external_real_image_candidate` | `arxiv:2603.17973` workflow / pipeline figures | Second-line indexing/runtime split | Shows AST/graph/test-linking work before the coding-agent loop | Proposed: `content/assets/atlas-images/tdad/tdad-development-impact-pipeline.png`; localization/rights/quality pending |
| `fig-tdad-development-test-map` | inline `external_real_image_candidate` | `pepealonso95/TDAD` or `tdad-skill` source screenshot | Runtime surface / code block section | Makes visible the small textual `.tdad/test_map.txt`/CLI surface | Proposed: `content/assets/atlas-images/tdad/tdad-test-map-example.png`; localization/rights/quality pending |
| `fig-harness-types-verification-boundary` | inline `local_image_asset` | Local Fowler harness image | Evidence-boundary section | Boundary illustration only; caption states it is not a TDAD-source diagram | `content/assets/theory-images/fowler-harness-types.png`; already local |
| `fig-tdad-definition-repo-tree` | queue-only | `f-labs-io/tdad-paper-code` README/repo tree | Possible file-surface support | Code block already carries the current article role; screenshot only if readable | Proposed path retained; pending |
| `fig-tdad-development-p2p-failures` | queue-only / optional | `arxiv:2603.17973` P2P failures figure | Possible metrics support | Avoid leaderboard drift; include only if chart materially improves metrics reading | Proposed path retained; pending |
| `fig-tdflow-reproduction-tests` | queue-only / optional contrast | TDFlow workflow figure | Possible contrast section support | Avoid focus drift from TDAD to TDFlow | Proposed path retained; pending |

## Disposition for dossier image candidates

| Dossier candidate | Disposition | Reason |
| --- | --- | --- |
| HTML/PDF `2603.08806`: схема цикла `behavioral spec → tests → prompt refinement → hidden evaluation`, если в полной версии есть рисунок | `merged_into_inline_external_candidate_after_P22` → `fig-tdad-definition-overview` | Более точный dossier candidate уже называет figure `TDAD overview`; один future asset slot достаточно покрывает эту визуальную роль |
| HTML/PDF `2603.08806`: figure 1 `TDAD overview` with `TestSmith`, `PromptSmith`, `Compiled Agent`, `MutationSmith`, spec evolution | `inline_external_real_candidate_after_P22` | Поддерживает центральный механизм первой линии |
| HTML/PDF `2603.08806`: figure 2 semantic mutation testing pipeline | `inline_external_real_candidate_after_P22` | Нужна для границы `mutation score` и non-activating mutants |
| `f-labs-io/tdad-paper-code`: дерево директорий | `queue_only_after_P22` | Нужна для файловой формы первой линии |
| HTML/PDF `2603.17973`: схема карты зависимости кода и тестов / impact analysis, если есть | `merged_into_inline_external_candidate_after_P22` → `fig-tdad-development-pipeline` | Более точный candidate figure 1/2 покрывает эту роль |
| HTML/PDF `2603.17973`: figure 1 `agentic workflow with TDAD` and figure 2 pipeline `AST Parser → ... → test_map.txt` | `inline_external_real_candidate_after_P22` | Нужна для различения preliminary indexing и runtime skill |
| HTML/PDF `2603.17973`: figure 3 P2P test failures per approach | `queue_only_optional_after_P22` | Уместна рядом с Phase 1 числами; future pass may decide queue-only if article becomes visually heavy |
| `pepealonso95/TDAD` or `tdad-skill`: example `.tdad/test_map.txt`, graph or CLI output | `inline_external_real_candidate_after_P22` | Поддерживает runtime surface второй линии |
| HTML/PDF `TDFlow`: figure 1 workflow `Generate Tests` / human tests → `Explore Files` → reports → next iteration | `queue_only_optional_after_P22` | Не факт о TDAD; допустим только как соседний контраст в разделе о третьем режиме тестов |
| HTML/PDF `TDFlow`: figure 2/4 Bad Test Rate and generated-test types | `external_queue_only` | Может пригодиться для будущего раздела о качестве reproduction tests, но P01 не вставляет, чтобы не размывать фокус TDAD |

## Synthetic figures

P01 не создаёт синтетические схемы. Причина: в досье уже есть достаточно внешних реальных visual candidates, а blueprint запрещает подменять source diagrams поспешными собственными схемами. Возможная future synthetic figure допустима только после P13, если нужно показать различение «test as specification / route / task» и оно плохо держится прозой.

## P02 visual sync

No visual candidates were added, removed or moved in P02. Boundary work did not change image dispositions. External candidates still require future asset-pass verification before any article insertion.

## P04 visual sync

No figure candidate was added, removed or moved. The first-line expansion strengthens the reason for keeping `fig-tdad-definition-overview`: it should show how `specification`, `test_guidance`/generated tests, `PromptSmith`, hidden evaluation and `MutationSmith` are separate roles. `fig-tdad-definition-mutation` remains necessary if the article keeps the mutation-score caution.

## P05 visual sync

No new visual candidate was added. The line-2 practice expansion increases the value of `fig-tdad-development-test-map`: a real `.tdad/test_map.txt` or CLI example now supports both the runtime-surface explanation and the distinction between minimal paper skill and published practical skill. `fig-tdad-development-pipeline` remains useful for showing that graph work happens before the agent loop; `fig-tdad-development-p2p-failures` remains optional and should only be kept if metrics discussion stays in the article.

## P06 visual sync

No visual candidate added. The new `Как читать score` section makes `fig-tdad-development-p2p-failures` more justifiable if the article keeps the metrics discussion, but it should remain optional: if rights/quality are weak or the section is later shortened, move the figure to queue-only. No synthetic score table is planned in P06.

## P07 visual sync

No visual candidate added. A future synthetic ladder figure for `наблюдение → свидетельство → принятие` could help, but P07 does not request it and the blueprint prefers real source figures first. Keep this as a possible later structural decision, not an image-plan commitment.

## P08 visual sync

No visual candidate added. Do not add a generic failure diagram. Existing source figures already cover the mechanisms; failure interpretation should remain prose unless a later structure pass decides to create a small synthetic comparison table.


## P09 visual sync

No new figure candidate was added. The new domain-specific paragraph strengthens the need for `fig-tdad-definition-overview`, because that figure should make clear how domain specification, test guidance/generated tests, hidden evaluation and mutation testing are separate roles. A separate four-domain table is not planned unless a later structure pass finds the prose too dense.

## P10 visual sync

No new visual candidate was added. The new reader-route section could later support a small synthetic comparison figure (`object → surface → decision`), but P10 deliberately leaves it out because the article already has a comparison table and several source-figure candidates. A later structure/visual pass should decide whether the prose route is enough.

## P11 local asset pass

| Asset | Classification | Decision | Placement | Notes |
| --- | --- | --- | --- | --- |
| `content/assets/theory-images/fowler-harness-types.png` | `local_image_asset` | Inserted inline as `fig-harness-types-verification-boundary` | `Что считать свидетельством, а что только наблюдением` | Useful because it shows `Test Suite` as one behavior-regulating sensor inside a wider harness. It supports the TDAD boundary without pretending to be a TDAD source diagram |
| Other local assets in `LOCAL_ASSET_INDEX.md` | `local_image_asset / neighboring-topic` | Rejected/deferred for this article | — | Most support SPDD, SDD/Kiro, PWG/Beads, Gas Town, Codex UI, HumanLayer harness or story examples. They would dilute the TDAD-specific visual plan |

P11 did not alter external TDAD figure priorities. The inserted local asset is cross-source and should be removed or demoted if later TDAD-native diagrams make the evidence-boundary point without adding noise.

## P12 external real image pass

| Dossier / catalog candidate | Classification | P12 disposition | Article id | Notes |
| --- | --- | --- | --- | --- |
| `ext-tdad-2603-08806-fig1` / TDAD overview | `external_real_image_candidate` | Candidate retained outside article after P20; caption rewritten as public caption | `fig-tdad-definition-overview` | High priority; source page exposes Figure 1 caption |
| `ext-tdad-2603-08806-fig2` / semantic mutation pipeline | `external_real_image_candidate` | Candidate retained outside article after P20; caption rewritten | `fig-tdad-definition-mutation` | Keep because mutation-score caveat is central |
| `tdad-paper-code` repo tree / file surface | `source_screenshot_candidate` | Candidate retained outside article after P20 | `fig-tdad-definition-repo-tree` | Candidate may be a source-tree screenshot rather than a paper figure |
| `ext-tdad-2603-17973-fig1` / agentic workflow | `external_real_image_candidate` | Merged/deferred into development-pipeline slot | `fig-tdad-development-pipeline` | Avoid inserting both workflow and pipeline unless layout needs both |
| `ext-tdad-2603-17973-fig2` / AST → graph → impact → test_map pipeline | `external_real_image_candidate` | Candidate retained outside article after P20; caption rewritten | `fig-tdad-development-pipeline` | Highest priority for second line |
| `ext-tdad-2603-17973-fig3` / P2P failures | `external_real_image_candidate` | Candidate retained outside article after P20 but optional | `fig-tdad-development-p2p-failures` | Remove if metrics discussion is compressed |
| `.tdad/test_map.txt` / CLI / README source fragment | `source_table_or_code_fragment_or_screenshot` | Candidate retained outside article after P20 | `fig-tdad-development-test-map` | Verify a real readable fragment before final asset localization |
| `ext-tdflow-workflow-fig1` | `external_real_image_candidate` | Candidate retained outside article after P20 as contrast only | `fig-tdflow-reproduction-tests` | Keep only if third-mode contrast stays |
| TDFlow Bad Test Rate figures | `external_real_image_candidate` | Queue-only, not inline | — | Would pull the article too far into TDFlow/test-generation quality |

P12 also rewrote inline external-candidate captions so they no longer read like internal working notes. Images are still not downloaded.

## P13 synthetic figure pass

No synthetic figure was inserted.

| Idea | Classification | Decision | Reason |
| --- | --- | --- | --- |
| `Объект → поверхность → решение` | `editorial_visual_idea` | Deferred | Potentially useful, but P10 already added this reader route in prose and the opening comparison table covers the two TDAD lines |
| `Тест как спецификация / маршрут / задача` | `editorial_visual_idea` | Deferred | Useful distinction, but the article already has a dedicated section plus external-real candidates; a homemade diagram would compete with source figures |
| `Наблюдение → свидетельство → принятие` | `synthetic_figure_candidate` | Rejected for now | Would duplicate the A7/evidence bridge and the inserted Fowler harness image |

P13 keeps the visual plan source-first: use real TDAD paper/repo figures before adding authorial diagrams.

## P14 visual sync — standalone glossary

No visual asset was added or removed in P14. The glossary is a prose orientation layer, not a new visual requirement. Existing priorities remain unchanged: TDAD-native source figures first, local Fowler harness image as optional evidence-boundary support, and synthetic diagrams deferred unless later pruning creates a real explanatory gap.

## P15 visual sync — mechanism/failure pass

No figure was added or removed in P15. The strengthened failure mechanism remains prose because a diagram here would likely duplicate the earlier comparison table, source figures and evidence-boundary image. Existing visual priorities and pruning watchpoints remain unchanged.

## P16 visual sync — theory back-links

No visual change. The semantic back-links are companion-level navigation and a short prose theory-return section, not a new figure requirement. Existing visual density and pruning watchpoints remain.

## P17 синхронизация визуального плана — язык

Визуальное решение не изменилось. В статье переведены статусы внешних кандидатов и заметка P12; локализован `alt` для локального изображения. ID ассетов и статусные метки оставлены машиночитаемыми.

## P18 визуальный синк — подписи и нижний блок

Визуальная стратегия не изменилась. В статье уточнены подписи и нижний блок: раздел переименован в `Внешние изображения для будущей проверки прав и качества`; решение P12 теперь прямо говорит, что изображения не добавлены и требуют отдельной проверки прав/качества перед вставкой.

## P19 визуальный синк — asset-инвентарь вынесен из статьи

Основной текст больше не содержит нижний служебный раздел со списком внешних изображений. Это улучшает standalone article voice. Все решения P12/P18 по внешним кандидатам остаются в этом image_plan и в external_image_queue; после P20/P21 внешние кандидаты сохранены только в companion-плане и очереди.

## P20 визуальный синк — inline placeholders removed

Стратегия изменилась для основного текста: внешние кандидаты больше не вставлены как пустые inline `<figure>` placeholders. Они остаются в плане и очереди до реальной локализации, проверки прав и проверки качества. Единственная фигура в статье сейчас — локальная `fig-harness-types-verification-boundary` с реальным `img`. Если будущий asset-pass скачает и проверит внешние TDAD-рисунки, их можно вернуть как нормальные изображения, а не пустые заготовки.

## P21 визуальный синк — current plan reconciled

Историческая P21 companion-only стратегия superseded by P22: текущий верх image_plan теперь фиксирует четыре inline external candidates и три queue-only/optional candidates. Локальная фигура `fig-harness-types-verification-boundary` сохранена, но её подпись в статье уточнена: это граничная иллюстрация harness, не TDAD-source diagram и не источник фактов для двух TDAD-линий.

## P22 визуальный синк — public article structure restored

P22 применил `visual-assets-and-figures.md`. Предыдущая P20/P21 стратегия companion-only для всех внешних кандидатов была слишком жёсткой для concept-atlas article package: правило требует сохранять релевантные source images как inline `external-real-candidate` placeholders и зеркалить их в нижнем asset-pass разделе. Поэтому четыре ключевых кандидата возвращены inline (`fig-tdad-definition-overview`, `fig-tdad-definition-mutation`, `fig-tdad-development-pipeline`, `fig-tdad-development-test-map`), а repo-tree, P2P failures и TDFlow workflow оставлены queue-only/optional ради баланса. Captions переписаны как публичные подписи без executor notes.

## P23 визуальный синк — current article state confirmed

Текущая статья содержит пять figures: четыре inline `external-real-candidate` source slots (`fig-tdad-definition-overview`, `fig-tdad-definition-mutation`, `fig-tdad-development-pipeline`, `fig-tdad-development-test-map`) и один local image asset (`fig-harness-types-verification-boundary`). Image plan now matches article state after P22. Active remaining blockers are localization/rights/quality checks and final pruning after real assets are available.

## P24 визуальный синк — стиль подписей и asset-раздела

Визуальные решения не изменились: статья по-прежнему содержит четыре inline `external-real-candidate` source slots и одну локальную harness-фигуру. P24 только улучшил язык подписи `fig-harness-types-verification-boundary` и нижнего asset-pass table: `runtime-инструкция`, `CLI-поверхность`, `chart`, `leaderboard` и `test-as-task` заменены на более прямые русские формулировки. Статусы, figure IDs, source labels and proposed local paths сохранены.

## P25 визуальный синк — no asset movement

P25 не изменил визуальные решения. Inline external candidates, queue-only candidates, local harness figure and proposed local paths remain as after P24. Only non-visual article headings and prose were selectively naturalized.

## P26 визуальный синк — final table/caption language

Визуальные решения не изменились. P26 только выровнял пользовательский язык: `Внешние изображения для asset-pass` сохранено как protocol-required heading, а заголовки нижней таблицы переведены на русский, а source/status labels оставлены как технические метки. Подпись локальной harness-фигуры стала прямее: она не описывает TDAD напрямую, а задаёт ограничение про место тестового набора внутри более широкой инженерной обвязки.
