# Target-group plan: статья атласа `tdad_comparative` — TDAD Comparative

Статус: `ready_for_package_manufacture_after_manual_review`.  
Article id: `tdad_comparative`  
Readiness status: `ready_for_package_manufacture_after_manual_review`.  
Рабочее название: `TDAD Comparative`  
Уровень статьи: `comparative method article`  
Режим будущего пакета: самодостаточный writing package.  
Внутренних ограничений объёма нет.

## 0. Режим и актуальный контекст

Этот target-plan является самостоятельным рабочим контрактом для будущего article-writing package. Служебная история manufactury-run, старые `S02/S03/S04` заметки и default `C5/A10 sync pending` не являются частью активной инструкции.

C5 и A10 доступны как read-only context. Если будущий article-writing run обнаружит конкретное несогласование с concept atlas или mode-selection map, оно фиксируется как конкретный debt в `open_questions`/audit, а не как общий sync blocker.

## 1. Краткая ориентация по статье

Главное досье:

```text
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
```

Вопрос читателя: как тест, benchmark или executable example может определять задачу для агента, а не только проверять результат после работы, и где эта граница ломается?

Центральная ось статьи: TDAD интересно не тезисом “tests matter”, а переносом роли теста: тесты, examples, benchmarks and skill evaluations могут стать способом определить поведение агента до действия, но passing score не равен инженерному ответу и не снимает human judgment.

Соседние границы: TDAD ≠ A7: A7 разводит observation/evidence; TDAD раскрывает method families where tests/examples define agent behavior. TDAD ≠ Spec Kit/SPDD: там specification artifacts; здесь tests/examples/benchmarks as specification-like surface. TDAD ≠ CI/testing generally; benchmark pass ≠ acceptance.

Визуальный слой: Приоритетны реальные diagrams/tables from TDAD papers/repos: SpecSuite examples, benchmark tables, test definitions, evaluation flow, skill/example workflow. Synthetic diagrams allowed only for the two TDAD meanings or test-as-spec vs test-as-evidence boundary.

## 2. Article contract

Статья должна:

- быть самостоятельной concept-first статьёй атласа, а не technical appendix;
- раскрыть главную концепцию на базе досье и первоисточников без внутреннего ограничения объёма;
- перенести всю релевантную фактуру, которая укладывается в назначение статьи;
- использовать внешние источники как supplement для уточнения, свежести, primary details and real image candidates;
- активно работать с local assets и external real image candidates;
- сохранять controlled repetition with theory, но не копировать общую теорию;
- показывать границы с соседними atlas articles and theory fragments.

Статья не должна стать generic testing article, benchmark leaderboard или повтор A7 evidence chapter. Она должна сравнить две линии TDAD и показать, когда проверка определяет задачу, а когда только наблюдает результат.

## 2.1. Фактура без coverage-бюрократии

TDAD Comparative-статья опирается на досье и первоисточники, но package не должен снова превращать перенос фактуры в coverage/disposition-бюрократию. Жёсткий режим `dossier-backed completeness / relevant but untransferred` считается откатанным: не нужно строить тотальную matrix по всему досье и доказывать статус каждого релевантного фрагмента.

Рабочий ориентир проще: ключевые тезисы статьи должны иметь достаточные технические опоры. Для этой статьи особенно важны: tests, datasets/benchmarks, pass/fail evidence, human review boundaries and concrete failure modes. Если без такой детали раздел остаётся общей прозой, материал лучше встроить в основной текст. Если деталь не помогает reader question, относится к соседней статье или ломает последовательность, её не нужно вставлять ради отчётности.

`source_transfer_ledger`, `image_plan` и `open_questions` остаются companion-файлами для реальных решений, долгов и source gaps. Они не заменяют основной текст и не должны становиться главным продуктом прохода.

## 3. Предполагаемая форма будущей статьи (не текст статьи)

1. **Две линии TDAD: Test-Driven AI Agent Definition / SpecSuite and Test-Driven Agentic Development.**
2. **Тест как specification/oracle before action.**
3. **Benchmarks and datasets: what they define, what they hide.**
4. **Human decision points: what question the test actually answers.**
5. **Engineering practice: examples, skills, iterations, experimental results.**
6. **Boundaries with A7/evidence, Spec Kit/SPDD and ordinary verification.**
7. **Failure modes: wrong task, benchmark proxy, overfitting to examples, passing ≠ accepted.**

Эта форма важнее, чем точное число разделов. Будущий authoring package может менять композицию, если сохраняет reader question, центральную ось, source depth, visual decisions and theory links.

## 4. Обрабатываемые файлы будущего package

```yaml
- path: work/atlas/articles/tdad_comparative.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_source_transfer_ledger.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_image_plan.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_external_image_queue.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_theory_links.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
- path: work/atlas/articles/tdad_comparative_readiness_report.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the TDAD atlas article."
```

Group mode: `linked-target-edit`.

## 5. Точные read-only inputs для включения в будущий пакет

```text
START.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_ORIENTATION.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_LEDGER.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PATHS.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/terminology-and-translation.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
content/Theoretical_synthesis.md
content/Cross_story_synthesis.md
work/theory-writing/fragments/00_spine_map_source_usage.md
work/theory-writing/fragments/00_spine_map_figure_candidates.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
content/assets/theory-images/MANIFEST.md
content/assets/theory-images/fowler-sdd-overview.png
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_READINESS_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLANS_MANUFACTORY_REPORT.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
content/assets/theory-images/fowler-harness-types.png
work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

## 6. Внешние источники для будущего package

```text
https://arxiv.org/abs/2603.08806
https://arxiv.org/abs/2603.17973
https://raw.githubusercontent.com/f-labs-io/tdad-paper-code/main/README.md
https://arxiv.org/html/2603.08806v1
https://github.com/f-labs-io/tdad-paper-code
https://huggingface.co/datasets/f-labs-io/SpecSuite-Core
https://raw.githubusercontent.com/pepealonso95/tdad-skill/main/SKILL.md
https://github.com/pepealonso95/TDAD
https://github.com/pepealonso95/tdad-skill/blob/main/SKILL.md
https://github.com/pepealonso95/tdad-skill
https://arxiv.org/html/2603.17973v2
https://raw.githubusercontent.com/pepealonso95/TDAD/main/claudecode_n_codex_swebench/run_benchmark.py
https://raw.githubusercontent.com/pepealonso95/TDAD/main/EXPERIMENTS.md
https://github.com/pepealonso95/TDAD/commits/main/
https://arxiv.org/abs/2510.23761
https://ar5iv.org/html/2510.23761v2
https://ai-paper-delta.vercel.app/en/papers/2603.17973
```

Дополнительно будущий пакет может открывать первичные ссылки из основного досье and source usage files. Внешний поиск разрешён для проверки, свежести, primary sources and visual candidates, но не для создания новых article topics.

## 7. Почему очередь подходит статье

Подходит ли выбранная очередь проходов именно этой статье? Да: выбранная очередь сохраняет сильный atlas article blueprint, но адаптирована к статье **TDAD Comparative**. Обязательны source-depth, свободные доборы, visual asset layer, concept reinforcement, три общих редакторских прохода, companion sync, язык/стиль and final verification. Количество проходов не является самоцелью; здесь сохранены P01–P26 + Final, потому что досье и границы статьи достаточно богаты, а цель — получить большую source-grounded статью без дальнейшей механической доводки.

## 8. Очередь будущих prompt-ов

### P01 — первичный концептуальный черновик
```text
Прочитай сначала:
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/A10_mode_selection_map.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Создай `work/atlas/articles/tdad_comparative.md` как большую самостоятельную concept-first статью атласа: **TDAD Comparative**. Не вводи внутренний лимит объёма. Статья должна отвечать на вопрос читателя: как тест, benchmark или executable example может определять задачу для агента, а не только проверять результат после работы, и где эта граница ломается?

Центральная ось статьи: TDAD интересно не тезисом “tests matter”, а переносом роли теста: тесты, examples, benchmarks and skill evaluations могут стать способом определить поведение агента до действия, но passing score не равен инженерному ответу и не снимает human judgment.

Сразу создай skeleton/status для всех companion-файлов из target outputs, даже если часть будет заполнена позже. Не пиши обзор досье подряд; выстрой статью вокруг reader question, механизма, границ, технической фактуры, visual layer and theory links.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P02 — контракт статьи и границы
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/A10_mode_selection_map.md
- protocols/rules/source-and-provenance.md

Укрепи article contract внутри статьи и companion-файлов. Проверь, что статья не стала generic overview, product/tutorial reference, повтором теории или дублем соседней статьи.

Reader question: как тест, benchmark или executable example может определять задачу для агента, а не только проверять результат после работы, и где эта граница ломается?

Граница статьи: TDAD ≠ A7: A7 разводит observation/evidence; TDAD раскрывает method families where tests/examples define agent behavior. TDAD ≠ Spec Kit/SPDD: там specification artifacts; здесь tests/examples/benchmarks as specification-like surface. TDAD ≠ CI/testing generally; benchmark pass ≠ acceptance.

Отрицательная граница: Статья не должна стать generic testing article, benchmark leaderboard или повтор A7 evidence chapter. Она должна сравнить две линии TDAD и показать, когда проверка определяет задачу, а когда только наблюдает результат.

C5 и A10 доступны как read-only context. Они не являются sync-pending blocker-ами; если обнаружено конкретное несогласование, фиксируй конкретный debt в `open_questions`, а не общий `C5/A10 pending`.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P03 — dossier inventory
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Сделай inventory досье: что уже перенесено, что осталось неперенесённым, что требует открытия первоисточников, где у будущей статьи могут не хватать технические опоры. Обнови основной текст только при явном пропуске article-critical материала. Запиши результат в `tdad_comparative_source_transfer_ledger.md` and `tdad_comparative_source_usage.md`.

Не строй тотальную coverage matrix по всему досье. Ledger должен помогать статье, а не заменять её.
```
### P04 — source-depth 1: TDAD line 1 — tests as agent definition
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/content-preservation.md

Раскрой Test-Driven AI Agent Definition / SpecSuite: how tests/examples define expected agent behavior, not just post-hoc verification.


Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P05 — source-depth 2: TDAD line 2 — engineering practice
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/content-preservation.md

Раскрой Test-Driven Agentic Development as practice: skills, benchmark experiments, iteration, examples and agent improvement.


Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P06 — source-depth 3: benchmark/dataset/result interpretation
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/content-preservation.md

Покажи what score measures, what it misses, how result interpretation requires human framing.


Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P07 — source-depth 4: human decision points and verification boundary
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/content-preservation.md

Покажи where humans decide whether a test answers the engineering question, and where evidence/observation/acceptance diverge.


Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P08 — source-depth 5: failures and anti-summary
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/content-preservation.md

Добавь failure modes: wrong task encoded, benchmark substitute for understanding, agent optimized to check, passing examples mistaken for sufficient evidence.


Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P09 — свободный добор материала 1
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_open_questions.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md

Свободно выбери главный недобор фактуры или технической конкретики. Не заранее заданная тема, а твоя редакторская оценка: где статья всё ещё слишком конспективна, где досье раскрыто поверхностно, где source-specific детали не встроены в механизм?

Добери материал и встрои его в основной текст. В companion-файлах запиши: что счёл недобором, что добавил, откуда взял материал и что осталось долгом.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P10 — свободный добор материала 2
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_open_questions.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md

Свободно выбери главный недобор связности, границы или reader path. Где статья раскрывает детали, но ещё не даёт достаточно цельного понимания концепции? Где нужна дополнительная фактура, переход, пример, ограничение или сравнение?

Добор должен быть именно добором материала и связности, а не преждевременной стилистической шлифовкой краткого обзора.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P11 — visual asset pass 1: локальные assets
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- content/assets/theory-images/MANIFEST.md
- protocols/rules/visual-assets-and-figures.md
- content/assets/theory-images/fowler-harness-types.png

Проведи local asset pass. Правило: relevant local assets работают по insert-or-explain. Если локальный asset релевантен статье, вставь его по месту применения как `<figure><img src="...">...</figure>` с публичной подписью; если не вставляешь — запиши причину в `work/atlas/articles/tdad_comparative_image_plan.md`.

Visual priorities для этой статьи: Приоритетны реальные diagrams/tables from TDAD papers/repos: SpecSuite examples, benchmark tables, test definitions, evaluation flow, skill/example workflow. Synthetic diagrams allowed only for the two TDAD meanings or test-as-spec vs test-as-evidence boundary.

Не пересказывай готовую картинку текстовой схемой и не пиши служебные подписи вроде “локальный файл найден”.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P12 — visual asset pass 2: внешние реальные изображения
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_external_image_queue.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- protocols/rules/visual-assets-and-figures.md

Начни с разделов досье вроде `Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` и похожих списков. Затем, если нужно, используй внешние первоисточники из плана и web/source access для поиска реальных diagrams/screenshots/tables.

Релевантный внешний кандидат ставь inline по месту применения как `<figure data-asset-status="external-real-candidate">` с нормальной подписью и зеркаль в нижний раздел `## Внешние изображения для asset-pass` плюс `work/atlas/articles/tdad_comparative_external_image_queue.md`. Изображения не скачивай. Каждый кандидат из досье должен получить disposition в `image_plan`.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P13 — visual asset pass 3: редкие синтетические схемы
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_external_image_queue.md
- protocols/rules/visual-assets-and-figures.md

Добавляй собственные synthetic figures только если они необычно полезны и нетривиальны: они должны прояснять механизм, границу, lifecycle transition или сравнение, которое плохо держится в прозе. Не создавай схемы ради визуального разнообразия и не замещай ими реальные local/external изображения.

Если synthetic figure добавлена, она должна быть inline по месту применения, с русскими labels, без служебного мета-текста. Если спорна — оставь её в image plan как deferred.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P14 — concept reinforcement 1: самостоятельность статьи
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md

Усиль статью как standalone concept-first article. Читатель должен понять **TDAD Comparative** без предварительной сборки материала из всех глав теории. Контролируемые повторы с теорией допустимы, если нужны для понимания конкретной концепции; механический copy-paste общей теории запрещён.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P15 — concept reinforcement 2: механизм, границы, ошибки
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md

Усиль механизм, границы и failure modes. Не делай отдельный каталог ошибок: встрой ограничения в объяснение концепции.

Особенно проверь: test defines wrong task; benchmark becomes surrogate understanding; passing examples treated as sufficient acceptance; data leakage/overfitting to benchmark; test oracle too narrow; article becomes generic testing chapter.

Если статья стала обзором features/sources вместо объяснения механизма, исправь основной текст.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P16 — concept reinforcement 3: связь с общей теорией
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/theory-writing/fragments/00_spine_map.md
- work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
- work/theory-writing/fragments/A5_process_methodologies_synthesis.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A9_lifecycle_repair.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/A10_mode_selection_map.md

Добавь semantic back-links в `theory_links`: не просто “см. A3/A5/A10”, а какой теоретический вопрос эта статья помогает понять. Исправь основной текст, если он либо не связан с общей рамкой, либо пытается заново написать всю теорию.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P17 — языковой проход 1
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай первый языковой проход по основному тексту. Приведи пользовательский текст к русскому режиму: убери случайный English glue, гибридные фразы и машинные кальки. Английский оставляй только для имён инструментов, команд, файлов, путей, source labels and устойчивых технических терминов. Не меняй аргумент и не выбрасывай фактуру.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P18 — языковой проход 2
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Повторно вычитай русский текст после P17. Проверь заголовки, captions, таблицы, bottom asset-pass section and companion-facing text. Сохрани source-specific names, команды и техническую конкретику, но сделай объяснение человеческим и связным.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P19 — общий редакторский проход 1
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- work/atlas/articles/tdad_comparative_readiness_report.md

Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их. Не ограничивайся заранее ожидаемыми дефектами: найди то, что реально мешает статье стать сильной standalone concept-first article.

После правки обнови audit and readiness status. Не переписывай удачные части без необходимости; не сглаживай фактуру.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P20 — общий редакторский проход 2
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- work/atlas/articles/tdad_comparative_readiness_report.md

Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их. Не ограничивайся заранее ожидаемыми дефектами: найди то, что реально мешает статье стать сильной standalone concept-first article.

После правки обнови audit and readiness status. Не переписывай удачные части без необходимости; не сглаживай фактуру.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P21 — общий редакторский проход 3
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- work/atlas/articles/tdad_comparative_readiness_report.md

Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их. Не ограничивайся заранее ожидаемыми дефектами: найди то, что реально мешает статье стать сильной standalone concept-first article.

После правки обнови audit and readiness status. Не переписывай удачные части без необходимости; не сглаживай фактуру.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P22 — public/article structure and entry-sequence pass
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_external_image_queue.md
- protocols/rules/visual-assets-and-figures.md

Проверь публичную форму статьи: первый экран, порядок разделов, подзаголовки, переходы, баланс текста и фигур, нижний раздел `Внешние изображения для asset-pass`, отсутствие служебных captions and executor notes. Первый экран должен problem-first вводить объект статьи и reader question, а не начинаться с taxonomy/atlas-boundary. Исправь структуру, если статья стала справочником, мини-теорией, tutorial или набором картинок.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P23 — companion sync
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_external_image_queue.md
- work/atlas/articles/tdad_comparative_open_questions.md
- work/atlas/articles/tdad_comparative_theory_links.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- work/atlas/articles/tdad_comparative_readiness_report.md

Синхронизируй companion-файлы со статьёй. Удали устаревшие долги, сохрани настоящие blockers, не оставляй стандартных `C5/A10 sync pending`: C5 и A10 доступны как read-only context, а любые проблемы должны быть конкретными долгами статьи. Проверь, что source usage, image plan, external image queue и theory links соответствуют фактической статье. Ledger не должен раздуваться как coverage-бюрократия вместо переноса фактуры в основной текст.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P24 — style defect audit
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Сделай стилевой аудит без тотального переписывания. Найди реальные дефекты: смысловые свёртки, псевдотермины, кальки, тяжёлые цепочки родительного падежа, неестественные заголовки, канцелярит и обратный дефект — механическое разворачивание нормальной мысли в протокольную конструкцию. Отметь места, где правка действительно нужна, и не трогай компактные фразы, если они звучат нормально по-русски и не прячут смысл.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P25 — selective natural rewrite
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/language-style-rules.md
- protocols/rules/content-preservation.md

Выборочно исправь только реальные стилевые дефекты, найденные в P24 и при повторном чтении. Не переписывай всю статью ради красоты, не превращай сильные технические места в гладкое summary и не заменяй конкретику таблицами без необходимости. Если фраза плоха, скажи её нормальным русским техническим текстом: иногда раскрыть, иногда сократить, иногда перестроить предложение или заголовок.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### P26 — guarded final human technical style pass
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- protocols/rules/human-technical-style.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Финально выровняй тон, ритм, переходы, подзаголовки и человеческую техническую фразу. Можно сильно менять форму, если сохраняются смысл, источниковая фактура, команды, числа, ограничения и границы. Нельзя возвращать псевдотермины, нельзя выбрасывать конкретику ради гладкости и нельзя превращать прозу в протокольные конструкции вида «кто действует / что проверяется / чем подтверждается» там, где можно сказать проще.

Синхронизация companion-файлов обязательна: если проход добавляет, переносит, отклоняет или переставляет фактуру, источник, границу, изображение, схему, термин или тезис, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit/readiness-файлы.
```
### Final — финальная проверка и упаковка результата
```text
Прочитай сначала:
- work/atlas/articles/tdad_comparative.md
- work/atlas/articles/tdad_comparative_source_usage.md
- work/atlas/articles/tdad_comparative_source_transfer_ledger.md
- work/atlas/articles/tdad_comparative_image_plan.md
- work/atlas/articles/tdad_comparative_external_image_queue.md
- work/atlas/articles/tdad_comparative_open_questions.md
- work/atlas/articles/tdad_comparative_theory_links.md
- work/atlas/articles/tdad_comparative_degradation_and_duplication_audit.md
- work/atlas/articles/tdad_comparative_readiness_report.md
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md
- protocols/rules/human-technical-style.md

Проведи финальную проверку article package result.

Обязательные checks:
- все target outputs существуют;
- основной article не имеет внутреннего лимита объёма и не выглядит как краткий overview;
- source usage и source transfer ledger заполнены как companion к статье, но не заменяют основной текст;
- ключевые тезисы не закрыты одной общей прозой там, где для понимания нужны технические опоры;
- нет `relevant but untransferred` как hard coverage blocker; реальные долги названы конкретно;
- каждый dossier image candidate имеет disposition;
- relevant local assets вставлены или explicitly rejected with reason;
- external real image candidates стоят inline там, где нужны, и зеркалятся в нижнем разделе `Внешние изображения для asset-pass` and external queue;
- synthetic figures не подменяют real images;
- C5/A10 sync представлен как concrete links/debts, not generic pending;
- captions публичные, без “локальный файл” / “восстановленная иллюстрация” / executor notes;
- стиль не вернулся к псевдотерминам и не ушёл в механическое протокольное разворачивание;
- финальный style pass не выбросил техническую конкретику ради гладкости;
- `readiness_report` честно фиксирует статус.

Собери result archive с overlay-путями всех target outputs, `MANIFEST.md`, `VERIFY.md`, `RESUME.md` and readiness summary. Если какой-то обязательный output отсутствует, результат нельзя помечать completed: собери interrupted archive.
```
## Visual candidate disposition guarantee

В P11–P13 и Final каждый visual candidate из основного досье, asset catalog and external search получает disposition. Relevant local assets вставляются или получают explicit rejection. External real image candidates должны стоять inline как `<figure data-asset-status="external-real-candidate">` и отражаться в нижнем разделе `Внешние изображения для asset-pass` and external queue. Synthetic figures допустимы только при необычной нетривиальной пользе.

## Prompt-record manifest for package builder

```text
P01
P02
P03
P04
P05
P06
P07
P08
P09
P10
P11
P12
P13
P14
P15
P16
P17
P18
P19
P20
P21
P22
P23
P24
P25
P26
Final
```

## 9. Readiness stamp

Статус: `ready_for_package_manufacture_after_manual_review`.

Пакет можно собирать как self-contained article-writing package после ручного review этого target-plan. Все input-пути указаны явно; package-builder должен bundle-ить эти файлы и не полагаться на неявный repo context.
