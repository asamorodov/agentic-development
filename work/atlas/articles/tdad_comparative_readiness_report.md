# TDAD Comparative — readiness report

Статус: `ready_for_P02_with_known_debts`

## Created outputs

- `work/atlas/articles/tdad_comparative.md`
- `work/atlas/articles/tdad_comparative_source_usage.md`
- `work/atlas/articles/tdad_comparative_source_transfer_ledger.md`
- `work/atlas/articles/tdad_comparative_image_plan.md`
- `work/atlas/articles/tdad_comparative_external_image_queue.md`
- `work/atlas/articles/tdad_comparative_open_questions.md`
- `work/atlas/articles/tdad_comparative_theory_links.md`
- `work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md`
- `work/atlas/articles/tdad_comparative_readiness_report.md`

## P01 result

Primary concept-first draft created. The article answers the reader question through the two-line TDAD split:

1. `Test-Driven AI Agent Definition`: tests compile and evaluate agent behavior before release.
2. `Test-Driven Agentic Development`: code-test impact map routes an AI coding agent toward relevant regression checks.

The central axis is explicit: tests/examples/benchmarks can define work for an agent before action, but passing score does not equal engineering acceptance and does not remove human judgment.

## Companion sync

- Source usage created and linked to external primary/readable sources.
- Source transfer ledger records transferred facts and deferrals.
- Image plan dispositioned all dossier image candidates.
- External image queue mirrors inline placeholders and queue-only candidates.
- Open questions capture source, visual and boundary debts.
- Theory links record C5/A10/A3/A7/C3 connections.
- Degradation audit records P01 risks and next-pass watchpoints.

## Known debts

- No external source refresh was performed in P01; the pass relied on allowed inputs and source links already present in the dossier.
- Figures are placeholders only. Download, rights check and quality check are pending.
- Conflicting source layers around first-line mutation results require commit/result-level provenance before stronger claims.
- Second-line experiment artifacts (`report.json`, `progress.log`, eval JSON) require targeted raw-file checks before instance-level claims.
- Later passes should strengthen article contract, source depth, visual decisions, language, editorial structure and final style.

## Gate

P01 gate status: pass for primary draft creation. Ready for next package pass.

## P02 update

Status: `article_contract_strengthened / ready_for_P03_with_known_debts`.

P02 added an explicit contract section to the article. The section fixes:

- reader question and positive scope;
- `TDAD ≠ A7`;
- `TDAD ≠ Spec Kit / SPDD / Kiro Specs / Constitutional SDD`;
- `TDAD ≠ CI/testing generally`;
- `benchmark pass ≠ acceptance`;
- `TDAD ≠ ADR / Persistent Work Graph`.

Companion sync completed: source usage, source transfer ledger, open questions, theory links, degradation audit, image plan and external image queue were updated. No image candidates changed.

## P04 update

Status: `line1_source_depth_strengthened / ready_for_P05_with_provenance_debts`.

P04 strengthened the first TDAD line by making explicit how `test_guidance`, examples, generated executable tests, visible/hidden split and deterministic fixtures turn expected agent behavior into a compilation surface. No new visual candidates were added. Companion sync completed across source usage, transfer ledger, image plan, external image queue, open questions, theory links and degradation audit.

Remaining P04 debts: verify concrete `test_guidance` / generated-test artifacts if future passes need examples; do not overstate mutation-score conflicts without commit/run-level evidence; keep first-line technical anchors concise so the article remains concept-first.

## P05 update

Status: `line2_source_depth_strengthened / ready_for_P06_with_artifact_verification_debts`.

P05 strengthened the second TDAD line as engineering practice. The article now distinguishes the paper-minimal runtime skill from the later published `tdad-skill`, explains the `EXP-026` → `EXP-028` packaging lesson, adds the auto-improvement loop, and makes benchmark telemetry part of the evidence story. Companion sync completed across source usage, transfer ledger, image plan, external image queue, open questions, theory links and degradation audit.

Remaining P05 debts: verify skill versioning, raw benchmark runner fields, exact eval artifacts and a real `.tdad/test_map.txt` / CLI visual before final publication.

## P06 update

Status: `score_interpretation_strengthened / ready_for_P07_with_metric_verification_debts`.

P06 added a standalone score-interpretation section. It explains what first-line and second-line scores measure, what they miss, how eval provenance affects results, and why human framing remains required. Companion sync completed across source usage, transfer ledger, image plan, external image queue, open questions, theory links and degradation audit.

Remaining P06 debts: verify exact metric definitions and raw telemetry schemas; later structure pass should decide whether `Как читать score` stays standalone or merges into the evidence section.

## P07 update

Status: `human_verification_boundary_strengthened / ready_for_P08_with_structure_watchpoint`.

P07 added a section separating observation, evidence and acceptance through TDAD-specific examples. It identifies where humans decide whether tests actually answer the engineering question in the first TDAD line, the second TDAD line and the TDFlow contrast. Companion sync completed across all required files.

Remaining P07 debt: later structure pass should consolidate adjacent score/evidence/human-decision material if it becomes repetitive.

## P08 update

Status: `failure_modes_strengthened / ready_for_P09_with_density_watchpoint`.

P08 added an anti-summary in the failure section: wrong task encoded, benchmark as substitute for understanding, agent optimized to check, and passing examples mistaken for sufficient evidence. Companion sync completed across all required files.

Remaining P08 debt: later editorial passes should reduce density and keep TDFlow as contrast only.

## P09 update

Status: `domain_specificity_strengthened / ready_for_P10_with_primary_spec_verification_debt`.

P09 filled the largest remaining concrete gap in the first TDAD line: the article now explains what the four SpecSuite-Core domains make testable. `SupportOps`, `DataInsights`, `IncidentRunbook` and `ExpenseGuard` are presented as different forms of agent obligation rather than as four benchmark labels. Companion sync completed across all required files.

Remaining P09 debt: verify the exact per-domain examples against primary spec/generated-test artifacts if later passes expand this into examples or a table.

## P10 update

Status: `reader_path_strengthened / ready_for_P11_with_structure_duplication_watchpoint`.

P10 added an early reader-route section: object under control, agent-facing test surface, and human decision supported by the signal. This turns the article's many technical details into a clearer path through the two TDAD lines and the TDFlow contrast. Companion sync completed across all required files.

Remaining P10 debt: later structure editing should decide whether this section stays standalone or merges with the quick split table, and whether the later evidence/human-decision sections can be tightened around the same triad.

## P11 update

Status: `local_asset_inserted / ready_for_P12_with_rights_and_visual_density_watchpoints`.

P11 inserted the local `fowler-harness-types.png` figure in the evidence-boundary section. The image supports the claim that a test suite can regulate behavior but remains one surface inside a broader harness, not a replacement for specification, architecture fitness, maintainability or human acceptance. Other local assets were deferred because they belong to neighboring atlas topics rather than this TDAD comparison. Companion sync completed across all required files.

Remaining P11 debts: verify image rights before publication and reconsider this cross-source image after TDAD-native figures are localized.

## P12 update

Status: `external_candidates_dispositioned / ready_for_P13_with_visual_pruning_watchpoint`.

P12 verified and dispositioned the external real image candidates from the TDAD dossier. Existing inline placeholders were retained but rewritten with public-facing captions, and each dossier candidate now has a decision: inline, merged/deferred, optional or queue-only. No images were downloaded. Companion sync completed across all required files.

Remaining P12 debts: rights/quality checks, exact figure choice for the second-line pipeline, and possible pruning of optional P2P/TDFlow visuals after structure compression.

## P13 update

Status: `synthetic_visuals_deferred / ready_for_P14_with_visual_overload_controlled`.

P13 added no synthetic figure. The pass considered three authorial visuals but deferred or rejected them because the article already has a comparison table, a reader-route section, multiple TDAD source-figure candidates and a local harness boundary image. Companion sync completed across all required files.

Remaining P13 debt: revisit a single compact synthetic comparison only after later structure pruning, not before.

## P14 update

Status: `standalone_glossary_added / ready_for_P15_with_glossary_duplication_watchpoint`.

P14 added an early `Минимальный словарь статьи` section defining `agent definition`, `visible tests`, `hidden tests`, `mutation intent`, `test map` and `свидетельство` in the article's own terms. This strengthens the article as a standalone concept-first atlas entry: the reader no longer has to infer the local vocabulary from later source-specific sections or from broader theory fragments. Companion sync completed across source usage, transfer ledger, image plan, external image queue, open questions, theory links and degradation audit.

Remaining P14 debts: later structure editing should check whether the glossary duplicates the quick comparison table or evidence sections, and language passes should stabilize the Russian/English treatment of repeated technical terms.

## P15 update

Status: `mechanism_boundaries_strengthened / ready_for_P16_with_score_evidence_repetition_watchpoint`.

P15 replaced the earlier numbered failure list with a mechanism-oriented section, `Как управляющий тестовый контур даёт сбой`. The article now explains failure modes as reversals of the TDAD mechanism: a test can define the wrong task, a narrow oracle can hide nearby risks, hidden/eval surfaces can leak into the optimizer, a benchmark can become a surrogate for understanding, and passing examples can be mistaken for acceptance. Companion sync completed across source usage, transfer ledger, image plan, external image queue, open questions, theory links and degradation audit.

Remaining P15 debt: later editorial passes should reduce repetition across the new mechanism section, score interpretation, evidence boundary and human-decision sections without losing the TDAD-specific failure logic.

## P16 update

Status: `semantic_theory_backlinks_added / ready_for_P17_with_theory_return_duplication_watchpoint`.

P16 added semantic back-links in `tdad_comparative_theory_links.md`: TDAD now links back to 00, A3, A5, A7, A9, A10 and C5 by the theory question it clarifies, not by simple “see also” references. The main article section formerly titled `Как TDAD связан с выбором режима работы` was rewritten as `Как TDAD возвращается в общую карту режима`, connecting TDAD to specification, process, evidence and repair without importing the full theory chapter. Companion sync completed across all required files.

Remaining P16 debt: later structure editing should check overlap between the new theory-return section and the final summary paragraph, and publication planning should decide whether body links should point directly to theory fragments or remain companion-only.

## P17 update

Status: `language_pass_1_completed / ready_for_P18_with_metric_label_watchpoint`.

P17 performed first Russian-language normalization of the main article. Accidental English glue and hybrid phrasing were reduced without changing the factual argument: benchmark/provenance/evidence/workflow/score/oracle/acceptance/runtime/eval terminology now reads in Russian prose. Source-stable English remains for article titles, repository names, commands, paths, metrics, code fields and figure IDs.

Remaining P17 debt: a later language pass should confirm metric labels and source-specific labels (`resolution rate`, `generation rate`, `test-level regression rate`, Kiro `requirements/design/tasks`, TDFlow `Bad Test Rate`) are intentionally retained.

## P18 update

Status: `language_pass_2_completed / ready_for_next_gate_with_contour_repetition_watchpoint`.

P18 вычитал основной текст после P17: улучшены заголовки и подписи, таблица оставлена без потери source-specific меток, нижний блок внешних изображений переоформлен как будущая проверка прав и качества, а несколько калькированных оборотов заменены на более естественные русские фразы. Companion-файлы синхронизированы: source usage, transfer ledger, image plan, external queue, open questions, theory links и audit.

Оставшийся долг P18: будущий редакторский проход должен проверить повторы слова `контур` и решить, остаётся ли нижний блок внешних изображений в основном тексте или уходит в companion-only слой перед публикацией.

## P19 update

Status: `editorial_pass_1_completed / ready_for_next_gate_with_inline_placeholder_watchpoint`.

P19 сначала сформулировал реальные проблемы: служебный блок внешних изображений ломал финал статьи, повторы `контур` делали часть прозы механической, а визуальный инвентарь дублировал companion-файлы. Исправления выполнены: нижний asset-инвентарь удалён из основного текста и оставлен в image_plan/external queue, повторы `контур` снижены с 22 до 8, факты и source-bound детали сохранены. Companion sync completed across source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Remaining P19 debt: следующий проход должен проверить inline placeholders. Если реальные изображения не будут локализованы, пустые `<figure>` нужно заменить на обычный текст или удалить перед публикацией.

## P20 update

Status: `editorial_pass_2_completed / ready_for_next_gate_with_visual_candidates_companion_only`.

P20 сначала сформулировал проблему: после удаления нижнего asset-инвентаря в статье всё ещё оставались пустые внешние `<figure>`-заготовки, которые не показывали изображения и мешали читать текст как standalone article. Исправление выполнено: все external placeholder-фигуры удалены из основного текста, локальная реальная фигура `fig-harness-types-verification-boundary` сохранена, визуальные кандидаты остались в `image_plan` и `external_image_queue`. Companion-файлы синхронизированы: source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшийся долг P20: будущий asset-pass должен возвращать внешние TDAD-рисунки только как локализованные изображения с проверенными правами и качеством, а не как пустые placeholders.

## P21 update

Status: `editorial_pass_3_completed / ready_for_next_gate_with_visual_provenance_aligned`.

P21 сначала сформулировал проблему визуального provenance: после P20 статья уже не содержала пустых внешних фигур, но image_plan и external queue всё ещё местами говорили языком прежних inline placeholders. Исправление выполнено: текущий статус image_plan переписан, очередь внешних кандидатов на P21 была уточнена как companion-only before localization; that historical status is superseded by P22, где четыре кандидата возвращены inline, а подпись единственной локальной `fig-harness-types-verification-boundary` в статье теперь прямо говорит, что это граничная harness-иллюстрация, не TDAD-source diagram. Companion-файлы синхронизированы: source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшийся долг P21: будущие визуальные проходы не должны возвращать external TDAD-кандидаты в основной текст без реального файла, правовой проверки, качества и публичной подписи.

## P22 update

Status: `public_entry_sequence_completed / ready_for_next_gate_with_asset_localization_watchpoint`.

P22 проверил публичную форму статьи. Главная правка: первый экран теперь начинается с проблемы — тест как ранняя рабочая поверхность агента — затем задаёт reader question и только после этого вводит две TDAD-линии. Это убирает ощущение taxonomy-first opening.

Визуальный слой также синхронизирован с `visual-assets-and-figures.md`: четыре ключевых external real image candidates возвращены inline как `external-real-candidate`, нижний раздел `Внешние изображения для asset-pass` восстановлен, а repo-tree, P2P failures и TDFlow workflow оставлены queue-only/optional ради баланса. Captions переписаны как публичные подписи без executor notes. Companion-файлы синхронизированы: source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшийся долг P22: будущий asset-pass должен локализовать inline external candidates, проверить права/качество и решить, нужен ли каждый visual slot после появления реальных изображений.

## P23 update

Status: `companion_sync_completed / ready_for_next_gate_with_active_blockers_only`.

P23 синхронизировал companion-файлы с текущей статьёй. `open_questions` переписан как active blockers list instead of pass-by-pass backlog. Stale P21 companion-only visual state is marked as superseded by P22. Image plan and external queue now match the article: four inline external candidates, one local figure, and queue-only optional visuals. No generic theory-sync debt remains; theory debts are concrete article watchpoints.

Оставшиеся blockers: source/provenance verification for mutation-result conflict and benchmark artifacts, external image localization/rights/quality, readable `test_map` visual, licensing for the local harness image, and final pruning after real assets are available.

## P24 update

Status: `style_defect_audit_completed / ready_for_next_gate_with_asset_and_provenance_blockers`.

P24 выполнил точечный стилевой аудит без тотального переписывания. Исправлены реальные дефекты русской технической прозы: псевдотермины и кальки (`человеческое обрамление`, `фронт проверки`, `runtime-инструкция`, `CLI-поверхность`, `leaderboard`, `test-as-task`), несколько механических формул (`контрольный шлюз`, `поверхности сбоя`, `рабочая оболочка`) и служебный оттенок подписи локальной harness-фигуры / нижнего asset-раздела. Факты, source-bound labels, ссылки, метрики и визуальные статусы сохранены. Companion sync completed across source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшиеся blockers после P24 не стилевые: проверка provenance для спорного mutation-result эпизода, raw artifacts/benchmark provenance при усилении claims, локализация и rights/quality проверка внешних изображений, читаемый test-map visual и финальная визуальная pruning-проверка.

## P25 update

Status: `selective_natural_rewrite_completed / ready_for_next_gate_with_nonstyle_blockers`.

P25 сделал выборочную естественную правку после P24: не переписывал статью целиком, а исправил оставшиеся неестественные заголовки и связки (`Читательский маршрут`, `методические семьи`, `поведенческая оболочка`, `мутационный угол`, `TDAD-контракт`, теоретическое `усложнять поверхность`). Техническая конкретика, таблица различий, source-bound labels, метрики, ссылки, команды и visual dispositions сохранены. Companion sync completed across source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшиеся blockers после P25 остаются теми же: provenance/raw artifact verification для спорных и benchmark claims, external image localization/rights/quality, readable test-map visual, local harness licensing and final pruning after assets.

## P26 update

Status: `guarded_final_style_completed / ready_for_next_gate_with_source_and_asset_blockers`.

P26 выполнил финальный guarded style pass: выровнял пользовательский русский в словаре, подписи и нижней таблице; перевёл обычные английские UI-labels нижней visual-таблицы (`Figure ID`, `Proposed local path`, `or`, `screenshot`); сохранил technical labels там, где они нужны; не сгладил плотный source-specific материал. Факты статьи, citations, команды, пути, метрики, figure IDs, inline/queue statuses и границы сохранены. Companion sync completed across source usage, transfer ledger, image plan, external queue, open questions, theory links and audit.

Оставшиеся blockers после P26: mutation-result provenance, raw artifact/eval provenance if claims are strengthened, external image localization and rights/quality/crop/caption checks, readable test-map visual, local harness licensing, and final figure pruning after real assets.
