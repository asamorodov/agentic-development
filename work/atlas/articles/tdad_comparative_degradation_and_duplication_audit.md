# TDAD Comparative — degradation and duplication audit

Статус: P01 audit. Первичный черновик создан, но не проходил P17–P26 language/editorial/style passes.

## Checks

| Check | P01 status | Notes |
| --- | --- | --- |
| Article is concept-first, not dossier summary | Pass with known debts | Черновик построен вокруг reader question and two-line TDAD split, not chronological dossier review |
| Two TDAD lines not collapsed | Pass | Separate line 1 / line 2 sections, separate artifacts and failure modes |
| `tests matter` slogan avoided | Pass | Central claim is role transfer: test as governing contour, not general testing advice |
| Passing score not treated as engineering answer | Pass | Repeated with concrete reasons: spec quality, hidden tests, map freshness, eval provenance, human gate |
| Technical anchors included | Pass | `spec.yaml`, `TestSmith`, `PromptSmith`, `respond`, `visible/hidden tests`, Docker volumes, `.tdad/test_map.txt`, `grep`, impact weights, `EXP-026`, `EXP-028`, `EVAL_JSON_PATH` |
| Internal dossier not cited as public source | Pass | Article uses external links from dossier, not dossier link |
| Visual candidates handled as external-real candidates | Pass | Inline placeholders and bottom asset-pass section created |
| Dossier image candidates all dispositioned | Pass | See image_plan |
| TDFlow kept as contrast, not TDAD fact | Mostly pass | One inline optional placeholder exists; future pass should decide if it distracts |
| Article not handbook | Mostly pass | Commands are anchors; future editor pass should watch command-heavy spots |
| Article not mini-theory | Mostly pass | A3/A7/A10 links are local; future pass should reduce repeated theory phrases if needed |
| Russian language | Pass with later style debts | English labels are source labels, commands, paths, metrics or method names |
| Human technical style | Ready for later passes | P01 still has structural rhythm and some comparison-heavy passages; P24/P25 should improve |
| No artificial volume cap | Pass | No internal length limit declared |

## Known degradation risks for next passes

1. Metrics sections may become too dense if P04–P08 add many more numbers. Keep numbers only where they explain mechanism or boundary.
2. TDFlow contrast is useful but can pull article toward a general survey. Keep it short unless future source-depth pass explicitly broadens boundary.
3. Visual placeholders are numerous. P12/P13 should decide which figures remain inline and which move to queue-only.
4. The article uses several `not only / but` style distinctions. Later style passes should reduce repetitive contrast syntax without losing the boundaries.
5. The first line's `ALWAYS_CREATE_TICKET` conflict is valuable but can overgrow. It should remain a provenance warning unless exact artifacts are opened.

## Readiness after P01

`ready_for_P02_with_known_debts`: article and all companion skeletons exist; central axis is present; source and image synchronization has been performed for P01-level changes. Not final for publication.

## P02 contract audit

| Check | Status | Notes |
| --- | --- | --- |
| Reader question explicit | Pass | Contract section restates exact reader question and object of article |
| Generic testing overview avoided | Pass with watchpoint | The article now says ordinary CI/testing is out of scope unless it shapes agent work before/during action |
| Benchmark leaderboard avoided | Pass | Benchmark pass explicitly separated from acceptance |
| A7 duplication controlled | Pass with future verification debt | Article states `TDAD ≠ A7`; direct A7 file was not in P02 allowed inputs |
| Spec Kit/SPDD/Kiro/CSDD duplication controlled | Pass | Boundary added with source links; no tutorial content imported |
| ADR/PWG duplication controlled | Pass | Negative boundary added; no ADR/PWG details expanded |
| First-screen load | Watchpoint | Contract section is useful but long; P22 may move part of neighbor-boundary text lower if entry feels heavy |

P02 readiness: `article_contract_strengthened / ready_for_P03_with_known_debts`.

## P04 audit — first-line expansion

| Check | Status | Notes |
| --- | --- | --- |
| Tests/examples as behavior-definition surface made explicit | Pass | Added `test_guidance` and behavior chain in line 1 |
| Internal dossier kept out of article citations | Pass | Main-text citation points to HTML article, not dossier |
| Article avoids post-hoc-only framing for line 1 | Improved | Visible tests now clearly appear as compilation input, not late QA |
| Risk of implementation over-detail | Watchpoint | New material adds `canary values`; later editor pass should keep it as anchor, not expand into full TestSmith handbook |
| Visual plan synchronized | Pass | No new figure candidate; first-line figure priorities clarified |

P04 readiness: `line1_source_depth_strengthened / ready_for_P05_with_provenance_debts`.

## P05 audit — second-line practice expansion

| Check | Status | Notes |
| --- | --- | --- |
| Engineering practice layer explicit | Pass | Added practical skill packaging, auto-improvement loop and benchmark telemetry |
| Skill version confusion controlled | Improved with watchpoint | Main text now warns not to attach article numbers to later skill packaging automatically |
| Benchmark numbers kept with caveats | Mostly pass | New auto-loop numbers add density; later editor pass should prune if article feels too numeric |
| Handbook drift | Watchpoint | Installation and CLI details are anchors, not instructions; avoid adding more commands unless source pass requires |
| Visual plan synchronized | Pass | No new candidate; line-2 asset priority updated |

P05 readiness: `line2_source_depth_strengthened / ready_for_P06_with_artifact_verification_debts`.

## P06 audit — result interpretation

| Check | Status | Notes |
| --- | --- | --- |
| Leaderboard reading avoided | Pass | New section explains what scores measure and miss |
| Human framing made explicit | Pass | Final paragraph of score section names acceptance decisions for both lines |
| Risk of repetition with evidence section | Watchpoint | `Как читать score` and `Что считать свидетельством` are adjacent and may need merging later |
| Metrics density | Watchpoint | Many metric names now appear; P22/P24 should prune or smooth if reader flow suffers |
| Visual sync | Pass | No new figures; P2P figure remains optional |

P06 readiness: `score_interpretation_strengthened / ready_for_P07_with_metric_verification_debts`.

## P07 audit — human decision boundary

| Check | Status | Notes |
| --- | --- | --- |
| Human decision points explicit | Pass | New section names first-line, second-line and TDFlow contrast decision points |
| Evidence/observation/acceptance separated | Pass | Section uses Russian terms and TDAD examples |
| A7 duplication risk | Watchpoint | Useful boundary, but may become too theory-heavy if expanded further |
| Repetition risk | Watchpoint | Adjacent score/evidence/human-decision sections may need consolidation |
| Visual sync | Pass | No generic diagram added |

P07 readiness: `human_verification_boundary_strengthened / ready_for_P08_with_structure_watchpoint`.

## P08 audit — failures and anti-summary

| Check | Status | Notes |
| --- | --- | --- |
| Required failure modes added | Pass | Wrong task, benchmark-as-understanding, optimization-to-check, passing examples as insufficient evidence |
| Overclaim controlled | Mostly pass | Anti-summary is explicit, but dense; later pass may split for readability |
| TDFlow contrast controlled | Watchpoint | Still useful but appears again; structure pass should monitor proportion |
| Visual sync | Pass | No generic failure image added |

P08 readiness: `failure_modes_strengthened / ready_for_P09_with_density_watchpoint`.

## P09 audit — free expansion 1

| Check | Status | Notes |
| --- | --- | --- |
| Main factual gap identified | Pass | The weakest point was the nominal treatment of the four SpecSuite domains |
| Source-specific material added | Pass | Added concrete obligations per domain from the first-line source |
| Article focus preserved | Pass | Addition supports line 1; it does not introduce a new neighboring method |
| Density risk | Watchpoint | The paragraph contains many technical nouns; later style pass may smooth or table it |
| Visual sync | Pass | No new image debt introduced |

P09 readiness: `domain_specificity_strengthened / ready_for_P10_with_primary_spec_verification_debt`.

## P10 audit — reader path and cohesion

| Check | Status | Notes |
| --- | --- | --- |
| Cohesion gap identified | Pass | Added a route that connects the two TDAD lines and TDFlow contrast before details begin |
| Premature style polish avoided | Pass | Addition changes reader path and conceptual framing, not wording only |
| C5 boundary respected | Pass | Uses C5 as structure guidance without making the article a C5 recap |
| Duplication risk | Watchpoint | The route may overlap with `Быстрая развилка`; structure pass should decide whether both are needed |
| Visual sync | Pass | No new external image debt introduced |

P10 readiness: `reader_path_strengthened / ready_for_P11_with_structure_duplication_watchpoint`.

## P11 audit — local visual asset pass

| Check | Status | Notes |
| --- | --- | --- |
| Insert-or-explain rule followed | Pass | `fowler-harness-types.png` inserted; other local assets explained as neighboring-topic/deferred |
| TDAD visual priority preserved | Mostly pass | Inserted image is not TDAD-native, but it supports the evidence boundary; TDAD-native figures remain queued |
| No image-to-text degradation | Pass | Used real `<figure><img>` block rather than rewriting the image as a prose diagram |
| Publication rights | Watchpoint | Local copy still needs rights/licensing check before public publication |
| Visual density | Watchpoint | Remove if later TDAD-native images make the same boundary clear enough |

P11 readiness: `local_asset_inserted / ready_for_P12_with_rights_and_visual_density_watchpoints`.

## P12 audit — external visual candidates

| Check | Status | Notes |
| --- | --- | --- |
| Dossier candidates dispositioned | Pass | All TDAD/TDFlow image candidates have inline, merged, queue-only or optional disposition |
| Captions public-facing | Pass | Rewrote “здесь нужна...” working captions into normal explanatory captions |
| No downloads | Pass | P12 explicitly leaves files for future rights/quality/localization pass |
| Visual overload | Watchpoint | Article now has many placeholders; later structure pass should prune optional P2P/TDFlow/repo-tree slots if needed |
| Source-specific priority | Pass | TDAD paper/repo candidates remain primary; Fowler local image remains boundary support only |

P12 readiness: `external_candidates_dispositioned / ready_for_P13_with_visual_pruning_watchpoint`.

## P13 audit — synthetic figure pass

| Check | Status | Notes |
| --- | --- | --- |
| Synthetic figure usefulness gate applied | Pass | Three ideas considered; none inserted |
| No replacement of real images | Pass | Source figures remain the priority |
| Visual overload controlled | Pass | Deferred diagrams instead of adding another layer |
| Future option preserved | Pass | `object → surface → decision` remains a deferred idea if structure pruning creates a gap |

P13 readiness: `synthetic_visuals_deferred / ready_for_P14_with_visual_overload_controlled`.

## P14 audit — standalone concept-first reinforcement

| Check | Status | Notes |
| --- | --- | --- |
| Standalone concept minimum | Pass | Added early local glossary for the article's core terms |
| Controlled repetition | Pass | Glossary repeats only local TDAD vocabulary needed for concept-first reading |
| Source discipline | Pass | No new factual source introduced; C5 used structurally |
| Visual discipline | Pass | No decorative diagram added for vocabulary |
| Duplication risk | Watchpoint | Glossary may overlap with quick split table and evidence sections; later structure pass should decide whether to merge |
| Language risk | Watchpoint | English technical terms need a stable treatment in later Russian-language passes |

P14 readiness: `standalone_glossary_added / ready_for_P15_with_glossary_duplication_watchpoint`.

## P15 audit — mechanism, boundaries, failure modes

| Check | Status | Notes |
| --- | --- | --- |
| Old catalog risk reduced | Pass | Replaced numbered failure list with mechanism-oriented explanation |
| Wrong-task risk | Pass | Integrated into first paragraph with first-line TDAD and TDFlow contrast |
| Benchmark surrogate / leakage risk | Pass | Added leakage/overfitting framing around hidden tests, mutation intents and benchmark answers |
| Narrow oracle | Pass | Added explicit oracle paragraph |
| Passing examples as insufficient acceptance | Pass | Integrated into mechanism and evidence continuity |
| Generic testing drift | Pass | Section now states why these risks matter specifically for TDAD |
| Repetition risk | Watchpoint | Score/evidence/human-decision sections still need later compression |

P15 readiness: `mechanism_boundaries_strengthened / ready_for_P16_with_score_evidence_repetition_watchpoint`.

## P16 audit — semantic back-links to theory

| Check | Status | Notes |
| --- | --- | --- |
| Semantic back-links added | Pass | `theory_links` now maps each theory fragment to the question TDAD clarifies |
| Main text connected to theory | Pass | Mode section rewritten around specification, process, evidence and repair links |
| Theory over-import avoided | Pass | No full A3/A5/A7/A9/A10 recap added |
| TDAD focus preserved | Pass | Source-specific mechanism sections unchanged |
| Duplication risk | Watchpoint | New mode section overlaps partly with final theory paragraph |
| Public routing | Watchpoint | Decide later whether to expose internal theory fragment links in article body |

P16 readiness: `semantic_theory_backlinks_added / ready_for_P17_with_theory_return_duplication_watchpoint`.

## P17 audit — language pass 1

| Check | Status | Notes |
| --- | --- | --- |
| Russian mode | Pass | Many English-glue phrases translated into Russian prose. |
| Source labels preserved | Pass | Titles, metrics, commands, paths, fields and figure IDs retained where exact. |
| Fact preservation | Pass | No factual deletion or argumentative change. |
| Remaining English labels | Watchpoint | Metrics/source labels still need second language pass. |
| Visual text | Mostly pass | Bottom image notes and local image `alt` text normalized; machine-readable statuses retained. |

P17 readiness: `language_pass_1_completed / ready_for_P18_with_metric_label_watchpoint`.

## P18 audit — language pass 2

| Check | Status | Notes |
| --- | --- | --- |
| Заголовки | Pass | Уточнены итоговый заголовок и нижний блок изображений. |
| Captions / alt | Pass | Подписи сохранены как source-bound; локальный `alt` русифицирован. |
| Таблица сравнения | Pass | Таблица не переписана, так как source labels и артефакты нужны для различения двух линий. |
| Bottom asset section | Pass | Раздел переоформлен как будущая проверка прав и качества, без обещания скачивания. |
| Фактура | Pass | Числа, источники и технические артефакты сохранены. |
| Стиль | Pass with watchpoint | Улучшена русская связность; остаётся риск повторов слова `контур`. |

P18 readiness: `language_pass_2_completed / ready_for_next_gate_with_contour_repetition_watchpoint`.

## P19 audit — editorial pass 1

### Сначала найденные проблемы

1. Основной текст заканчивался служебным списком внешних изображений. Это ломало standalone article voice: вместо финального тезиса читатель видел внутренний asset-инвентарь.
2. Термин `контур` повторялся слишком часто и начинал звучать как модельная свёртка, хотя не везде был нужен.
3. Нижний блок изображений дублировал image_plan/external queue и создавал риск рассинхронизации.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Standalone ending | Pass | Статья теперь заканчивается итоговым тезисом, а не служебным asset-разделом. |
| Fact preservation | Pass | Из основного текста удалён только служебный visual inventory; факты и источники сохранены в companion-файлах. |
| Repetition | Improved | Повтор `контур` снижен с 22 до 8 употреблений. |
| Visual plan sync | Pass | Image decisions retained in image_plan/external_image_queue; inline placeholders remain. |
| Concept-first task | Improved | Main article now reads more like publication text and less like work package ledger. |

P19 readiness: `editorial_pass_1_completed / ready_for_next_gate_with_inline_placeholder_watchpoint`.

## P20 audit — editorial pass 2

### Сначала найденные проблемы

1. После P19 статья уже имела чистый финал, но внутри текста оставались пустые внешние `<figure>` placeholders.
2. Эти заготовки не давали читателю изображения и выглядели как незавершённая сборка.
3. Риск потери визуальных кандидатов отсутствует, потому что `image_plan` и external queue уже хранят полный список.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Empty external figures | Removed | Все `data-asset-status="external-real-candidate"` figure-блоки удалены из основного текста. |
| Real local image | Kept | `fig-harness-types-verification-boundary` сохранён, потому что содержит реальный `img`. |
| Visual candidate preservation | Pass | Кандидаты сохранены в `image_plan` и `external_image_queue`. |
| Standalone article voice | Improved | Текст больше не прерывается пустыми asset-заготовками. |
| Fact preservation | Pass | Удалены только визуальные placeholders; фактическая аргументация не менялась. |

P20 readiness: `editorial_pass_2_completed / ready_for_next_gate_with_visual_candidates_companion_only`.

## P21 audit — editorial pass 3

### Сначала найденные проблемы

1. После P20 статья была очищена от пустых external figures, но image_plan и external queue всё ещё содержали формулировки, которые могли читаться как текущие inline placeholders.
2. Единственная оставшаяся фигура была полезной, но требовала более явной границы: это harness-boundary visual, а не TDAD-source diagram.
3. Риск для standalone article заключался не в фактах, а в visual provenance: читатель или следующий проход мог перепутать текущую статью с asset-планом.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Current article figures | Pass | В статье осталась одна локальная фигура с реальным `img`; external placeholders отсутствуют. |
| Figure caption provenance | Improved | Caption теперь прямо говорит, что harness-фигура не является TDAD-source diagram. |
| Image plan current state | Superseded by P22 | P21 companion-only state was later replaced by P22 inline/queue balance. |
| External queue state | Pass | P12 disposition table and queue status aligned with companion-only current state. |
| Fact preservation | Pass | Изменены только визуальные статусы, подпись и companion sync; TDAD claims не менялись. |

P21 readiness: `editorial_pass_3_completed / ready_for_next_gate_with_visual_provenance_aligned`.

## P22 audit — public/article structure and entry sequence

### Сначала найденные проблемы

1. Первый экран начинался с taxonomy под одной аббревиатурой TDAD. Это было корректно, но не problem-first: читатель видел классификацию раньше инженерной проблемы.
2. После P20/P21 визуальный слой стал clean, но перестал соответствовать правилу для concept-atlas article packages: relevant external real image candidates должны иметь inline slots или явный queue-only disposition, а bottom asset-pass section должен зеркалить решения.
3. Нужен был баланс: вернуть source-figure placeholders без превращения статьи в набор картинок или служебный asset ledger.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| First screen | Improved | Opening rewritten as problem → reader question → two TDAD lines. |
| Taxonomy position | Pass | Taxonomy remains early, but no longer first. |
| Visual protocol | Pass | Four key external candidates restored inline as `external-real-candidate`; bottom asset-pass section restored. |
| Visual balance | Pass with watchpoint | Repo-tree, P2P chart and TDFlow workflow kept queue-only/optional. |
| Caption quality | Pass | Inline captions are public-facing; no executor notes. |
| Source preservation | Pass | No new factual claims or numbers added. |

P22 readiness: `public_entry_sequence_completed / ready_for_next_gate_with_asset_localization_watchpoint`.

## P23 audit — companion sync

### Сначала найденные проблемы

1. `open_questions` had accumulated pass-specific debts, including obsolete P22-forward-looking items.
2. P21 visual companion-only notes could be misread as current state after P22 restored inline external candidates.
3. Ledger risked becoming coverage bureaucracy unless active blockers were centralized.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Open questions | Rewritten | Only active source/provenance, asset, structure and theory watchpoints remain. |
| Visual state | Synced | Image plan and external queue match current article: four external slots + one local figure. |
| Stale debts | Removed/marked superseded | Old “if P22…” and P21 companion-only state no longer read as active. |
| Generic theory sync | Pass | No generic theory-sync debt remains; theory debts are concrete. |
| Ledger discipline | Pass | P23 adds no coverage table; future ledger entries should record real transfer/status changes only. |

P23 readiness: `companion_sync_completed / ready_for_next_gate_with_active_blockers_only`.

## P24 audit — style defect pass

### Сначала найденные проблемы

1. В тексте оставались псевдотехнические свёртки и кальки: `человеческое обрамление`, `фронт проверки`, `CLI-поверхность`, `runtime-инструкция`, `leaderboard`, `test-as-task`.
2. Несколько фраз звучали как модельные метки вместо инженерного объяснения: `контрольный шлюз`, `поверхности сбоя`, `рабочая оболочка`.
3. Подпись локальной harness-фигуры и нижний asset table местами читались как внутренний asset-pass, а не как публичная часть статьи.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Fact preservation | Pass | Ссылки, числа, команды, source-bound labels and article claims сохранены. |
| Style defects | Improved | Псевдотермины заменены на прямые формулировки: решение человека, набор проверок, рабочая инструкция, CLI-след. |
| No total rewrite | Pass | Правки точечные; компактные source-specific labels не раскрывались механически. |
| Visual wording | Improved | Caption локальной harness-фигуры и роли нижних визуальных кандидатов стали публичнее. |
| Companion sync | Pass | Source usage, ledger, image plan, external queue, open questions, theory links and readiness updated. |

P24 readiness: `style_defect_audit_completed / ready_for_next_gate_with_asset_and_provenance_blockers`.

## P25 audit — selective natural rewrite

### Сначала найденные проблемы

1. После P24 оставались несколько удачных по смыслу, но неестественных формулировок: `Читательский вопрос`, `методические семьи`, `поведенческая оболочка`, `мутационный угол`, `TDAD-контракт`.
2. Некоторые заголовки звучали как внутренние метки (`Читательский маршрут`, `Как управляющий тестовый контур даёт сбой`, `Как TDAD возвращается...`).
3. В теоретическом возврате одна фраза всё ещё говорила через абстрактную `поверхность`, хотя смысл был проще: внешний артефакт нужен только там, где без него теряется намерение, нужные проверки или право завершить.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Selectivity | Pass | Переписаны только реальные дефекты; таблицы, метрики и плотные технические абзацы сохранены. |
| Natural Russian | Improved | Заголовки и несколько связок стали ближе к нормальному инженерному объяснению. |
| Content preservation | Pass | Factual claims, citations, source-specific terms and visual statuses unchanged. |
| Duplication risk | Pass | No new explanatory section or table added. |
| Companion sync | Pass | Required companion files updated. |

P25 readiness: `selective_natural_rewrite_completed / ready_for_next_gate_with_nonstyle_blockers`.

## P26 audit — guarded final human technical style

### Сначала найденные проблемы

1. В нижней таблице визуальных кандидатов оставались английские UI-метки (`Figure ID`, `Proposed local path`, `or`, `screenshot`), которые не были source-specific настолько, чтобы оставаться в русской прозе.
2. Несколько фраз в словаре и подписи всё ещё использовали абстрактный язык `surface`, хотя конкретная инженерная формулировка была яснее.
3. Финальный проход должен был сохранить плотные технические секции, а не сгладить их в summary.

### Исправления

| Check | Status | Notes |
| --- | --- | --- |
| Русский пользовательский язык | Improved | Заголовки нижнего visual-раздела и обычные описания теперь русские; технические метки сохранены. |
| Человеческий технический стиль | Improved | Словарь и подпись harness-фигуры используют прямые фразы вместо модельных абстракций. |
| Сохранение фактов | Pass | Числа, команды, метрики, citations, source labels, figure IDs and visual dispositions сохранены. |
| Без сглаживания | Pass | Плотные source-абзацы и таблица сравнения сохранены. |
| Companion sync | Pass | Обязательные companion-файлы обновлены. |

P26 readiness: `guarded_final_style_completed / ready_for_next_gate_with_source_and_asset_blockers`.
