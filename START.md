# START для восстановления рабочего контекста

Этот архив — срез репозитория сайта и рабочих материалов по теории AI-driven SDLC / agentic development.

Если пользователь просит «прочитай START.md», твоя задача — восстановить контекст проекта, а не сразу переписывать документы.

## Сначала прочитай

1. `work/discourse.md` — текущая смысловая линия и последние принятые решения.
2. `work/theory-writing/WORKING_DOCUMENTS_MAP.md` — карта рабочих документов и то, как они используются. Если файла нет, скажи об этом и временно ориентируйся по `work/approved-ai-sdlc-plan.md`, `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` и структуре `work/`.
3. Основные протоколы:
   - `protocols/rules/chat-github-repo-work-protocol.md`
   - `protocols/rules/discourse-maintenance-rules.md`
   - `protocols/rules/russian-language.md`
   - `protocols/rules/language-style-rules.md`
   - `protocols/rules/source-and-provenance.md`
   - `protocols/rules/content-preservation.md`
   - `protocols/rules/fragment-defect-analysis-and-repair.md`
4. Если задача связана с пакетами-заданиями, дополнительно прочитай:
   - `work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md`
   - `work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md`
   - `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md`

Не читай весь репозиторий подряд. После первичного восстановления контекста открывай только те документы, которые нужны для конкретной задачи.


## Post-Atlas active state

Concept-first Атлас завершён как baseline из 10 статей. Активный скелетон для следующих глав:

```text
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
```

`THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` остаётся историческим baseline. Новые chapter packages должны читать V5, `00_spine_map`, `CORE_NODES_WRITING_PLAN`, релевантные A/B/C-фрагменты, статьи Атласа, досье для gap-check и карты external discovery.

Внешние источники в будущих главах используются не только для подтверждения готовых claims и картинок. Если глава недоразработана, package должен запускать bounded source discovery: поиск, раскрытие найденных источников и integration decision.

---

## Как устроен репозиторий

- `content/` — публичные материалы сайта: ориентация, истории, теория, handbook/fieldbook.
- `content/stories/` — корпус историй. Они являются первым разделом сайта и фактической базой; теория может ссылаться на них, но не должна пересказывать их заново.
- `work/dossiers/` — рабочие досье по методологиям и механизмам. Это quarry-материал, не публичные источники для ссылок в теории.
- `work/story_dossiers/` — рабочие досье по историям.
- `work/skeletons/` — текущий скелетон теоретического раздела.
- `work/theory-writing/` — планы написания, target-group plans, фрагменты теории и кэш собранных пакетов.
- `work/theory-writing/target-group-plans/` — планы целевых групп. Их имена заканчиваются на `_TARGET_GROUP_PLAN.md`.
- `work/theory-writing/packages/` — кэш собранных исполнительных пакетов. Если пакет собран из одного плана, имя zip совпадает с именем плана без `_TARGET_GROUP_PLAN`.
- `work/protocols/`, `protocols/rules/`, `protocols/skills/` — рабочие правила и процедуры.
- `work/reports/` — отчёты, аудиты, карты источников и служебные документы.

## Важные правила работы

### Базовая линия для delta/overlay

Последний полный архив репозитория, загруженный пользователем как repo snapshot, считается текущей базовой линией. Если пользователь явно говорит, что изменения применены, закоммичены или что теперь нужно считать базой новое состояние, базовая линия переносится в эту точку.

Архивы и delta-zip, созданные ассистентом, не становятся новой базовой линией автоматически. Нельзя молча брать предыдущий assistant-generated overlay как основу следующей дельты.

Если нужно менять репозиторий, делай overlay/delta относительно последнего пользовательского baseline или явно названной commit/apply-точки. Перед сборкой архива в отчёте и `work/APPLY_NOTES.md` нужно назвать эту базу.

Если текущий архив должен включать ранее сделанные, но ещё не закоммиченные изменения, это должна быть кумулятивная дельта относительно той же базовой линии, а не дельта поверх предыдущего assistant-generated overlay. Если кумулятивность не требуется, делай узкую дельту только по текущей просьбе и прямо скажи, что она не включает прежние uncommitted overlays.

Если в теоретическом тексте используется материал из внутреннего досье, ссылка должна вести не на досье, а на первичный источник, указанный или выводимый из досье. Если первоисточник нельзя уверенно восстановить, ссылку лучше не ставить.

Внешние ссылки и внутренние ссылки ставятся сразу там, где вводится материал. Визуальные кандидаты проходят обязательную asset-классификацию до inline-вставки: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate`, `editorial_visual_idea`. Синтетические схемы можно вставлять через `<figure>` по месту применения только если они действительно полезны, нетривиальны и проясняют то, что плохо держится в прозе; готовые иллюстрации, скриншоты, source diagrams и локальные assets нельзя пересказывать текстом, перерисовывать или ухудшать без отдельного явного решения. Если asset-pass/rights-check/download/quality-check ещё не сделан, кандидат фиксируется в `*_figure_candidates.md` и asset catalog, но не подменяется текстовой схемой.
Для задач с `<figure>`, изображениями, screenshots, diagrams или asset-pass дополнительно читать `protocols/rules/visual-assets-and-figures.md`; это правило запрещает подменять готовые иллюстрации текстовыми схемами, требует asset-классификации и ограничивает создание собственных схем случаями явной нетривиальной пользы.
Для concept-atlas article packages визуальный проход обязан читать не только общий asset catalog, но и основной dossier article: разделы `Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` и похожие списки являются обязательными источниками visual decisions. Каждый кандидат из досье получает disposition в `<article_id>_image_plan.md`; релевантные внешние кандидаты ставятся inline как `<figure data-asset-status="external-real-candidate">` и зеркалятся в нижнем разделе `Внешние изображения для asset-pass` и external image queue. Локальные assets работают по правилу insert-or-explain: вставить как `<figure><img ...></figure>` или явно отклонить с причиной.


Для repair-pass и анализа уже сделанных фрагментов дополнительно читать `protocols/rules/fragment-defect-analysis-and-repair.md`. Repair начинается с диагностики функции фрагмента и типов дефектов, а не с переписывания. После правки нужен regression audit и readiness status, особенно если результат станет входом для B/C-фрагментов или composition pass.

Для ещё не построенных writing-фрагментов target-group plan должен включать не один общий repair-pass после стиля, а 2–3 общих редакторских прохода после первичной русификации/языковых проходов и до финальных стилевых проходов. Языковые проходы должны идти раньше repair/style, чтобы repair работал уже с русским текстом и мог чинить смысловые проблемы, возникшие после перевода. Редакторские проходы сохраняют общность: «оцени текст, насколько он хорошо выполняет поставленную задачу; после формулирования проблем исправь их», без заранее назначенной специальной темы вроде визуального слоя, источников или стиля.

Если будущий фрагмент имеет сильный специфический риск, target-group plan может добавлять 1–3 адресных прохода усиления основной функции **между системным выравниванием и общей редакторской тройкой**. Такие проходы допустимо формулировать специально: например проверить терминологический контракт под нагрузкой, переход между слоями, практическую применимость карты или границу runtime/PWG. Они не заменяют общие редакторские проходы и не должны превращать их в специальные visual/source/style checks.

Технический атлас теперь трактуется как **концептуально-технический атлас**, а не как узкое техническое приложение. Его разделы должны быть самостоятельными связными статьями по конкретным концепциям, методологиям и инструментальным формам: SPDD, PWG, Gas Town / Beads, GSD, BMAD, TDAD, Spec Kit, Kiro, ADR и т.п. Контролируемое повторение тезисов из теории допустимо, если оно нужно, чтобы читатель понял конкретную концепцию без сборки материала из разных глав. Теория при этом остаётся поперечный SDLC-синтезом; атлас не должен механически копировать теорию целиком и не должен становиться свалкой деталей, но имеет самостоятельную концептуально-техническую ценность.


Для writing-пакетов целевой группы по умолчанию self-contained: источники, перечисленные в плане, упаковываются в исполнительный пакет. Repo-snapshot-bound режим используется только если это явно указано.

## Текущая линия работы

Главная текущая линия — post-atlas написание теоретического раздела по Skeleton V5, готовым A/B/C-фрагментам, Атласу, досье gap-check и внешнему source discovery там, где главы недособраны.

Принята стратегия: сначала пишутся несущие узлы и мосты, затем отдельные главы, затем composition pass, языковые и стилевые проходы.

Ключевые опорные узлы скелетона:

- SPDD — глубокий опорный случай спецификационного жизненного цикла.
- Persistent Work Graph — глубокий опорный механизм жизненного цикла рабочего состояния.
- Gas Town / Beads — глубокий опорный случай организационно-операционного жизненного цикла.
- ADR — защищённый профиль архитектурного решения, но не отдельный deep anchor.

Перед любой конкретной работой сначала уточни, с каким файлом, планом или пакетом пользователь хочет работать, затем открывай только релевантные материалы.


## C5 concept-first atlas plan: 17 passes + final verification

Действующее решение для `C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md`: C5 пишется поздно относительно основного набора A/B/C, но его package-gate — готовность `00` и `C1–C4`, а не готовый A10. A10 полезен как later-sync input для будущей сверки с картой выбора режимов, но не является hard gate. C5 задаёт concept-first / concept atlas как второй режим чтения. План C5 должен содержать 17 рабочих проходов плюс отдельную финальную проверку package-run. Обязательные элементы: модель самостоятельной статьи атласа, `C5_concept_atlas_article_map.md`, три адресных прохода перед общей редакторской тройкой (самостоятельная ценность статьи, контролируемое повторение, двусторонняя навигация theory-first / concept-first). Article map должен быть картой уровня реестра, а не мини-атласом: tiers, reader questions, article boundaries, готовность ассетов/источников, semantic back-links и boundary checks для опасных пар статей обязательны.

Ранний `A10_MODE_SELECTION_MAP.zip` считается premature/superseded и не используется. В текущем состоянии после интеграции результатов `00` и `C1–C4` новый A10 package уже можно собирать заново по обновлённому 17-pass плану, используя `C1–C4` как read-only inputs.

Действующее решение для `A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md`: A10 пишется только после C1–C4. План A10 теперь содержит 17 рабочих проходов плюс отдельную финальную проверку: синтез входов A/B/C, рабочую `A10_mode_selection_matrix.md`, `A10_decision_stress_tests.md`, адресные проходы по критериям выбора, переходам/деэскалации, сочетаниям режимов и scenario stress-test, затем три общих редакторских прохода, public decision-map / visual-artifact pass, два языковых и два стилевых прохода. A10 не должен стать резюме A1–A9, maturity model или статической классификацией.

## Current package status after C/00 integration

`work/theory-writing/packages/A10_MODE_SELECTION_MAP.zip` has been rebuilt after `00` and `C1`–`C4` were imported and repaired. This is the active A10 package; earlier A10 packages built before C results are premature/superseded and must not be used.

Correction: `C5_THEORY_TO_TECHNICAL_ATLAS.zip` may be built after `00` and `C1`–`C4` exist. `A10_mode_selection_map.md` is optional later-sync for C5, not a hard package blocker; if A10 is absent, record `A10 sync pending` in C5 open questions/audit.

## Atlas article package blueprint

Для будущих статей концептуально-технического атласа действует отдельный blueprint:

```text
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
```

Atlas article package не использует короткую очередь обычных A/B/C-фрагментов. Базовая форма — 26 рабочих проходов плюс финальная проверка: несколько source-depth проходов, два свободных прохода добора материала, отдельные visual asset passes, concept reinforcement, два языковых прохода, три общих редакторских прохода, public/article-structure / entry-sequence pass, companion sync, style defect audit, selective natural rewrite и guarded final human technical style pass. Внутренние ограничения на объём запрещены. Внешние первоисточники разрешены, особенно для поиска реальных изображений; локальные релевантные assets должны вставляться в статью, а внешние реальные изображения фиксируются inline как candidates и в нижнем разделе для asset-pass. C5 полезен для синхронизации article map, но не является hard gate для разработки blueprint или первых планов статей; если C5 отсутствует, фиксируется `C5 sync pending`.

## Atlas article target-plan manufactury

Для будущего создания target-group plans статей концептуально-технического атласа действует отдельный план:

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

Этот meta-package должен запускаться прямо на машине с развёрнутым репозиторием. Входные архивы, досье или assets от пользователя не требуются: исполнитель читает `START.md`, blueprint, карту документов, досье, asset catalog, текущие фрагменты и протоколы из файловой системы. Список статей не придумывается внешним поиском: он берётся из known dossier-backed set в плане. Для каждой статьи meta-package сначала создаёт target-group plan, затем улучшает именно этот plan через S02–S04 и readiness stamp. Он не пишет сами статьи и не собирает article executor packages без отдельной команды.

## Atlas article target-plan manufactury package status

Package available:

```text
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
```

Use it only in the root of a deployed repository. It does not bundle dossiers/assets and does not write atlas articles; it creates and repairs target-group plans for dossier-backed atlas article packages.

## Atlas article target-plan manufactury refinement

The current package is:

```text
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
```

It has been rebuilt after refining the manufactury plan: S02 is targeted plan strengthening, S03 is free editorial strengthening, and boundary debts do not automatically block a dossier-backed article plan if the article goal is clear.

## Atlas article target-plan manufactury self-contained refinement

Current package:

```text
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
```

It has been rebuilt after refining the manufactury plan. Generated article target-group plans must now support independent/self-contained article-writing packages: exact bundled read-only inputs, idempotent plan creation, package-buildability checks, S02 targeted strengthening, S03 free editorial strengthening, and boundary debts that do not automatically block a clear dossier-backed article.

## A10 result imported and post-import repaired

`work/theory-writing/fragments/A10_mode_selection_map.md` has been imported from the completed A10 result archive. During integration, two missing target outputs were created: `A10_mode_selection_matrix.md` and `A10_decision_stress_tests.md`. The initial result companion files claimed that factual A/B/C fragments had not been opened; this was closed by a post-import sync against actual `A1`–`A9`, `B1`–`B3`, and `C1`–`C4` fragments in the repository. A10 is now usable as a ready input for later sync, with ordinary publication checks remaining for story anchors and final assembly. Report: `work/theory-writing/reports/A10_RESULT_INTEGRATION_EVALUATION_REPAIR_REPORT.md`.


## A10 second repair and free-pass diagnosis

`A10_mode_selection_map.md` получил второй post-import repair после повторной пользовательской проверки. Исправлены остаточные дефекты: `Слой` в основной карте заменён на `Форма внешней структуры`, `субстрат работы` заменён на прямое `состояние работы`, supporting outputs очищены от остаточных English labels, а companion-файлы больше не считают фактическую A/B/C-сверку открытым blocker-ом.

Процессный вывод зафиксирован отдельно: три встроенных общих редакторских прохода не нужно автоматически увеличивать, но для поздних синтетических фрагментов и linked-target groups требуется независимая post-import validation в развёрнутом репозитории. Missing target outputs и непрочитанные mandatory upstream files являются механическим дефектом результата, а не обычным `ready_with_known_debts`.

Report: `work/theory-writing/reports/A10_SECOND_REPAIR_AND_FREE_PASS_DIAGNOSIS_REPORT.md`.


## C5 result imported and synced with A10

`work/theory-writing/fragments/C5_theory_to_technical_atlas.md` and companion files have been imported from the completed C5 result archive. C5 now has `C5_concept_atlas_article_map.md` as a registry-level map for future concept-first atlas articles. Post-import validation synced C5 with the now-present A10 outputs (`A10_mode_selection_map.md`, `A10_mode_selection_matrix.md`, `A10_decision_stress_tests.md`): the old `A10 sync pending` status is closed and replaced with `ready_with_known_debts / A10 synced`. Report: `work/theory-writing/reports/C5_RESULT_INTEGRATION_EVALUATION_REPAIR_REPORT.md`.

## Atlas article target plans imported

`ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_RESULT.zip` has been imported. The repo now contains 10 target-group plans for dossier-backed concept-atlas articles under:

```text
work/atlas/target-group-plans/
```

The readiness and boundary control files are:

```text
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_READINESS_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLANS_MANUFACTORY_REPORT.md
work/atlas/plans/reports/ATLAS_ARTICLE_TARGET_PLANS_IMPORT_EVALUATION_REPAIR_REPORT.md
```

Post-import repair closed stale default C5/A10 sync debts and added explicit `Prompt-record manifest for package builder` sections. Current status: all 10 article target plans are usable after manual review. One article-writing package has now been built for ADR: `work/atlas/packages/adr_method_ATLAS_ARTICLE.zip`.


## ADR atlas article package

The first atlas article-writing package has been built after targeted repair of the ADR article target plan:

```text
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
```

This package is self-contained: it bundles the exact read-only inputs listed by the target plan, with repository `START.md` embedded as a snapshot inside package `START.md` to avoid conflict with launch instructions. It contains 26 gated records: P01–P25 plus Final. The package should be executed only after manual review of:

```text
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Report:

```text
work/atlas/plans/reports/adr_method_PLAN_REPAIR_AND_PACKAGE_REPORT.md
```

## Current atlas-plan note: SPDD target-plan second repair

`work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` has been manually repaired after the atlas article target-plan manufactury result. It is now more SPDD-specific: central axis, Fowler/OpenSPDD split, failure modes, SPDD-specific source-depth passes, cleaner visual passes and current C5/A10 context. No SPDD article-writing package has been built yet. See `work/atlas/plans/reports/spdd_method_PLAN_SECOND_REPAIR_REPORT.md`.


## Current atlas article fact-transfer rule

Действующее правило после SPDD/Gas Town сравнений — `Фактура без coverage-бюрократии`. Досье и первоисточники остаются основной базой статей атласа, но hard `coverage matrix / relevant but untransferred` gate не является текущим управляющим механизмом. Пакет должен ставить достаточные technical anchors в основной текст, если без них ключевой тезис превращается в общую прозу. `source_transfer_ledger`, `image_plan` и `open_questions` остаются companion-файлами для реальных решений, долгов и source gaps, но не заменяют статью.


## Current atlas package status update

- `work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip` is available as a self-contained article-writing package for `spdd_method`; it was built after the dossier-completeness and visual-candidate rule updates.


## Current atlas package status update

- `work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip` is available as a self-contained article-writing package for the Persistent Work Graph / Beads concept atlas article. It was built after PWG-specific plan repair and dossier-completeness / visual-candidate rule updates.


## Current generated atlas article packages

- `work/atlas/packages/gas_town_ATLAS_ARTICLE.zip` — self-contained package for the Gas Town atlas article.


## Current atlas package status update — remaining atlas article packages built

The following self-contained atlas article-writing packages are available: `spec_kit_method_ATLAS_ARTICLE.zip`, `kiro_specs_ATLAS_ARTICLE.zip`, `constitutional_sdd_ATLAS_ARTICLE.zip`, `tdad_comparative_ATLAS_ARTICLE.zip`, `gsd_open_gsd_ATLAS_ARTICLE.zip`, `bmad_method_ATLAS_ARTICLE.zip`. They were built after article-specific plan repairs and use exact bundled read-only inputs, dossier-backed completeness, visual candidate disposition and C5/A10 as read-only context.


## Current atlas package status update — remaining six plans

The remaining atlas article target plans have been repaired and article-writing packages built for:

- `spec_kit_method`
- `kiro_specs`
- `constitutional_sdd`
- `tdad_comparative`
- `gsd_open_gsd`
- `bmad_method`

All packages are self-contained, include exact read-only inputs, and use the dossier-backed completeness and visual-candidate disposition rules.


## SPDD rollback dossier-completeness experiment package

Created experimental package:

```text
work/atlas/packages/spdd_method_ATLAS_ARTICLE_rollback_dossier_completeness.zip
```

It is a control variant for SPDD article generation. It does not replace the canonical SPDD article package. It rolls back the latest dossier-backed completeness hard gate for SPDD only, while preserving source-depth, free expansion, visual asset handling, external image candidates, local assets and no internal length limits.

## 2026-06-13 — ADR and PWG packages aligned with current atlas blueprint

`work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` and `work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` have been aligned with the current softened atlas blueprint: rollback-like dossier inventory, no hard coverage matrix, no repeated transfer-audit checks, soft technical anchoring, language passes before general repair/editorial, entry-sequence pass, companion sync, `style defect audit`, `selective natural rewrite`, and guarded final human technical style.

Rebuilt packages:

```text
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip
```

Both packages contain 27 gated records (`P01`–`P26` + `Final`) and exact bundled read-only inputs. The article-writing packages have not been executed; no `work/atlas/articles/adr_method.md` or `work/atlas/articles/persistent_work_graph.md` article result was created in the repository.

