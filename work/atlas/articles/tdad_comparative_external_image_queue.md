# TDAD Comparative — external image queue

Статус: P22 queue. Все entries остаются внешними кандидатами и требуют download/rights/quality check before local insertion. Четыре кандидата возвращены inline как `external-real-candidate`; остальные остаются queue-only/optional.

## 1. `fig-tdad-definition-overview`
- Source: `https://arxiv.org/html/2603.08806v1` / PDF `Test-Driven AI Agent Definition`, figure `TDAD overview`.
- Take: pipeline with `TestSmith`, `PromptSmith`, `Compiled Agent`, hidden evaluation, `MutationSmith`, spec evolution.
- Use: main article, after first explanation of line 1.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-definition-overview.png`.
- Status: inline `external-real-candidate` after P22; localization/rights/quality pending.

## 2. `fig-tdad-definition-repo-tree`
- Source: `https://github.com/f-labs-io/tdad-paper-code` / README.
- Take: repo tree or source visual showing `specs/core`, `tests_visible`, `tests_hidden`, `mutation_packs`, `agent_artifacts`, `scripts`, `results`.
- Use: main article, file-surface section of line 1.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-definition-repo-tree.png`.
- Status: queue-only after P22; may become generated screenshot of source tree if no source diagram exists.

## 3. `fig-tdad-definition-mutation`
- Source: `https://arxiv.org/html/2603.08806v1` / PDF figure 2.
- Take: semantic mutation testing pipeline with `activation probes` and non-activating mutants.
- Use: main article, mutation section of line 1.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-definition-mutation-pipeline.png`.
- Status: inline `external-real-candidate` after P22; localization/rights/quality pending.

## 4. `fig-tdad-development-pipeline`
- Source: `https://arxiv.org/html/2603.17973v2` / PDF figure 1 and/or figure 2.
- Take: `agentic workflow with TDAD` and especially `AST Parser → Graph Builder → Test Linker → Impact Analyzer → test_map.txt → AI Coding Agent`.
- Use: main article, second line mechanism.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-development-impact-pipeline.png`.
- Status: inline `external-real-candidate` after P22; localization/rights/quality pending.

## 5. `fig-tdad-development-test-map`
- Source: `https://github.com/pepealonso95/TDAD` or `https://github.com/pepealonso95/tdad-skill`.
- Take: `.tdad/test_map.txt` example, graph screenshot, `tdad impact` output, or README visual if available.
- Use: main article, runtime-surface section of line 2.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-test-map-example.png`.
- Status: inline `external-real-candidate` after P22; if no real visual exists, future pass should decide between text code block and no figure, not invent a decorative schema.

## 6. `fig-tdad-development-p2p-failures`
- Source: `https://arxiv.org/html/2603.17973v2` / PDF figure 3.
- Take: P2P test failures per approach.
- Use: main article, metrics section of line 2.
- Proposed local path: `content/assets/atlas-images/tdad/tdad-p2p-failures.png`.
- Status: queue-only / optional after P22; may become inline only if future structure needs the metric chart.

## 7. `fig-tdflow-reproduction-tests`
- Source: `https://ar5iv.org/html/2510.23761v2` / TDFlow figure 1.
- Take: workflow around reproduction tests, `Explore Files`, `Revise Patch`, `Debug One`.
- Use: optional contrast section only.
- Proposed local path: `content/assets/atlas-images/tdad/tdflow-reproduction-tests-workflow.png`.
- Status: queue-only / optional contrast after P22; removable if it distracts from TDAD.

## 8. TDFlow Bad Test Rate figures
- Source: `https://ar5iv.org/html/2510.23761v2` / figures 2/4.
- Take: Bad Test Rate and generated-test types (`generated tests`, `f2p`, `p2p`, `p2f`, `f2f`).
- Use: queue-only for future expansion on reproduction-test quality.
- Proposed local path: `content/assets/atlas-images/tdad/tdflow-bad-test-rate.png`.
- Status: `external_queue_only`; not inline in P01.

## P02 queue sync

No external image queue changes in P02. Boundary additions did not introduce visual candidates for Spec Kit, SPDD, Kiro, Constitutional SDD, ADR or PWG, because those would pull the TDAD article toward neighboring atlas articles.

## P04 queue sync

No new external image tasks were created. During asset-pass, prioritize the first-line figures in this order: `fig-tdad-definition-overview`, `fig-tdad-definition-mutation`, then `fig-tdad-definition-repo-tree`. The new `test_guidance` paragraph does not require a separate screenshot unless the source has a clear visual/table that can be used legally and cleanly.

## P05 queue sync

No image was downloaded and no new source was queued. For the second-line asset pass, prefer a real `test_map.txt` / CLI output over a decorative graph image, because the P05 text argues that the agent-facing artifact is a small textual working surface. If no real source visual is available, keep the code block and drop the figure rather than inventing a diagram.

## P06 queue sync

No new asset queued. If `fig-tdad-development-p2p-failures` is downloaded later, its caption must avoid leaderboard framing and explain what the chart does not measure: patch quality, unselected tests, freshness of the map and human acceptance.

## P07 queue sync

No external image queue change. Do not search for generic evidence/acceptance diagrams; they would pull the article toward a theory explainer rather than TDAD source material.

## P08 queue sync

No external image queue changes. No web/image search required for failure modes; they are grounded in existing source candidates.


## P09 queue sync

No external image queue changes. Do not add decorative screenshots for the four SpecSuite domains. If an asset pass later finds a compact source table or repository tree that shows domain/spec/test separation, it can support `fig-tdad-definition-repo-tree`; otherwise keep the domain details as prose.

## P10 queue sync

No external image queue changes. Do not search for a generic roadmap image. If the reader-route idea becomes visual, it should be an editor-created synthetic figure after structure stabilization, not an external decorative asset.

## P11 queue sync

No external image was downloaded or queued in P11. The inserted Fowler harness image was already local, so TDAD-specific external candidates remain unchanged. During future asset-pass, do not treat `fig-harness-types-verification-boundary` as a substitute for TDAD paper diagrams; it only supports the broader verification-boundary argument.

## P12 external image queue sync

P12 confirmed the external candidates from the dossier without downloading them. Current dispositions:

| Queue item | P12 disposition |
| --- | --- |
| `fig-tdad-definition-overview` | Inline after P22; high-priority asset localization |
| `fig-tdad-definition-repo-tree` | Queue-only after P22 as source-tree/screenshot candidate |
| `fig-tdad-definition-mutation` | Inline after P22; high-priority if mutation section remains |
| `fig-tdad-development-pipeline` | Inline after P22; choose paper figure 2 over figure 1 unless both are needed |
| `fig-tdad-development-test-map` | Inline after P22 as source-fragment/screenshot candidate; remove if no readable source visual exists |
| `fig-tdad-development-p2p-failures` | Queue-only/optional after P22; tied to metrics section |
| `fig-tdflow-reproduction-tests` | Queue-only/optional after P22 as contrast only |
| TDFlow Bad Test Rate figures | Queue-only; no inline placement |

No image files were downloaded in P12. Rights, quality and exact cropping remain future asset-pass tasks.

## P13 queue sync

No external image queue changes. P13 intentionally did not create a synthetic figure that would replace or visually compete with the external TDAD candidates. The existing external queue remains the priority for future asset localization.

## P14 external queue sync

No external image queue changes. The standalone glossary does not create a new real-image candidate and does not alter the P12 dispositions for TDAD paper/repo figures or the TDFlow contrast figure.

## P15 external queue sync

No external image queue changes. The P15 failure/mechanism rewrite does not introduce a new source figure candidate and does not change prior external candidates.

## P16 external queue sync

No external image queue changes. P16 used internal theory fragments only and did not create or modify any external real-image candidates.

## P17 языковая синхронизация очереди

Очередь не изменилась. В статье нормализованы только русские описания external-кандидатов и нижнего блока изображений. Машиночитаемые ID, названия источников и статусные метки не менялись.

## P18 очередь — подписи

Очередь внешних изображений не изменилась. P18 только сделал формулировки статьи более человеческими: внешние кандидаты остаются `external-real-candidate`, а скачивание, права и качество остаются будущим действием.

## P19 очередь — companion-only inventory

Очередь не менялась по составу. P19 только перенёс нижний список кандидатов из основного текста в companion-only слой: кандидаты, пути, статусы, права и quality-check долги сохраняются здесь и в image_plan.

## P20 очередь — external candidates retained after article cleanup

Состав очереди не изменён. P20 удалил из основного текста пустые inline-заготовки, но не отклонил сами внешние кандидаты. Все прежние кандидаты остаются `external-real-candidate` до скачивания, проверки прав и качества.

## P21 очередь — current statuses aligned

Состав очереди не изменён, но текущий статус уточнён: внешние TDAD-кандидаты больше не считаются inline placeholders в статье. Они являются companion-only кандидатами на будущую локализацию. Возврат в статью допустим только после реального файла, проверки прав, качества и подписи, которая не будет выглядеть как служебная заготовка.

## P22 очередь — inline/queue balance restored

P22 применил visual-assets protocol для concept-atlas article: внешние реальные изображения нельзя заменять текстовыми схемами и релевантные source candidates должны иметь inline slot или явный queue-only disposition. Inline возвращены четыре кандидата: overview первой линии, mutation pipeline, development pipeline и test-map/runtime screenshot. Repo-tree, P2P failures и TDFlow workflow оставлены queue-only/optional ради баланса и фокуса статьи.

## P23 очередь — current queue confirmed

Очередь синхронизирована с текущей статьёй: четыре внешних кандидата inline, три major candidates queue-only/optional, TDFlow Bad Test Rate figures remain queue-only for possible future expansion. No candidate was downloaded or removed. Active queue blockers are rights, quality, crop, caption fidelity and finding a readable real test-map screenshot/CLI trace.

## P24 очередь — style sync only

Очередь не изменилась: ничего не скачано, не удалено и не переведено из queue-only в inline. P24 только синхронизировал публичные формулировки ролей: pipeline slot теперь описан как разделение индексации и короткой рабочей инструкции, test-map slot — как `.tdad/test_map.txt`, `tdad impact` или другой CLI-след, P2P slot — как график, а TDFlow slot — как контраст, где тесты задают задачу ремонта. Блокеры прав, качества, crop and caption fidelity остаются активными.

## P25 очередь — no change

Очередь внешних изображений не изменилась. P25 не скачивал источники, не менял статусы кандидатов и не создавал synthetic visual debt.

## P26 очередь — final style only

Очередь не изменилась. P26 не скачивал изображения и не менял решения inline/queue-only. Публичные формулировки в таблице статьи теперь русские; машиночитаемые IDs кандидатов, status labels и proposed paths сохранены для будущей локализации ассетов.
