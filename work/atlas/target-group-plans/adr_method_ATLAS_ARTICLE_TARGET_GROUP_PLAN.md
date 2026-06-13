# Target-group plan: статья атласа `adr_method` — ADR как метод архитектурной памяти

Статус: `ready_for_package_manufacture_after_manual_review`.  
Article id: `adr_method`  
Readiness status: `ready_for_package_manufacture_after_manual_review`.  
Рабочее название: `ADR как метод: архитектурное решение, подтверждение и замена`  
Уровень статьи: `method article`  
Режим будущего пакета: самодостаточный writing package.  
Внутренних ограничений объёма нет.

## 0. Режим создания

Chosen mode: `repair_existing_after_import`. Файл `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` уже существовал после manufactury-run. Текущая правка не перезаписывает план шаблонно, а усиливает именно ADR-логику: архитектурное решение, его статус, способы подтверждения, условия замены и риски использования ADR агентом как основания для действия.

## 1. Краткая ориентация по досье для планирования

Главное досье:

```text
work/dossiers/ADR_METHOD_DOSSIER.md
```

Досье позволяет написать не справку о шаблонах ADR, а самостоятельную статью о том, как архитектурное решение получает форму, статус, причины, последствия, способы подтверждения и условия замены. Для агентской разработки это особенно важно: агент может опираться на документ, который выглядит как принятое решение, хотя он устарел, был сгенерирован без достаточного основания или не связан с проверяемыми признаками соблюдения решения.

Статья должна соединить несколько источниковых слоёв:

- классические ADR-источники: Michael Nygard, Martin Fowler, MADR, adr-tools и практики ведения records;
- AI/ADR research: генерация ADR, восстановление ADR из кода, влияние контекстного окна, сравнение шаблонов, поиск violations, traceability и architecture memory;
- agentic practice: ADR skills, repo patterns, AI-assisted architecture workflows, generated/reconstructed ADR examples;
- проверяемые проекции решения: ArchUnit, CODEOWNERS, fitness functions, API compatibility, SLO/performance thresholds, rollout and operational signals;
- failure modes: устаревший ADR, неподтверждённое убеждение, сгенерированная traceability без provenance, видимость исполнимой проверки.

Связанные фрагменты теории:

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/A10_mode_selection_map.md
content/Theoretical_synthesis.md
content/Cross_story_synthesis.md
```

Соседние досье для проверки границ:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Главные риски дублирования: ADR легко смешать со specification, проверочным контрактом/оракулом, PWG-состоянием, TDAD evidence и CSDD compliance. Статья должна отличаться так: ADR фиксирует принятое архитектурное решение, его основание, последствия, условия подтверждения и условия замены. Он не хранит всё состояние работы как PWG, не описывает желаемое изменение как specification, не является тестовым оракулом сам по себе и не заменяет отдельные свидетельства.

Визуальный слой:

```text
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
content/assets/theory-images/MANIFEST.md
content/assets/theory-images/fowler-sdd-overview.png
```

ADR-specific visual candidates: реальные ADR templates, MADR examples, generated/reconstructed ADR examples from AgenticAKM, decision lifecycle diagrams, ArchUnit / CODEOWNERS / fitness-function screenshots, diagrams from AI/ADR papers and operational confirmation examples. Если они не локализованы, будущий article package должен ставить их как external real image candidates, а не заменять текстовыми схемами.

## 2. Article contract

Вопрос читателя: как ADR помогает сохранить архитектурное решение так, чтобы оно оставалось понятным, проверяемым и заменяемым в AI-assisted / agentic development?

Центральная мысль: ADR нужен не потому, что архитектуру надо “задокументировать”, а потому что решение должно пережить смену сессий, агентов, контекста, проверок и последующую замену. Хороший ADR хранит не только выбранный вариант, но и причины, отвергнутые альтернативы, последствия, уровень подтверждения и признаки, по которым решение надо пересмотреть.

Статья должна:

- объяснить Nygard ADR, Fowler ADR и MADR как разные формы записи решения, а не как каталог шаблонов;
- показать, почему AI/ADR generation не равна принятию решения, reconstructed ADR не равен provenance, violation detection не равен пониманию архитектурного смысла, а большое контекстное окно не решает проблему статуса решения;
- разобрать три ADR-ошибки: мёртвая запись, неподтверждённое убеждение, неправомерное основание для действия агента;
- объяснить способы подтверждения решения человечески: по каким признакам видно, что решение действительно соблюдается или что его пора пересмотреть;
- показать уровни подтверждения: review, ownership, ArchUnit, CODEOWNERS, API compatibility, SLO/performance, rollout and operational signals;
- провести границу между specification, ADR, проверочным контрактом/оракулом, TDAD, CSDD и PWG;
- показать ADR в агентном workflow: до implementation, во время implementation, на review, после merge и в lifecycle repair;
- сохранить практические примеры, исследовательские детали, executable/operational checks, governance/review mechanisms and failure modes.

Отрицательная граница: статья не должна стать справкой о шаблонах ADR, списком architecture-governance tools или повтором A2/A9. Её задача — раскрыть ADR как метод сохранения архитектурного решения, его статуса, подтверждения и замены.

## 2.1. Фактура без coverage-бюрократии

ADR-статья опирается на досье и первоисточники, но package не должен снова превращать перенос фактуры в coverage/disposition-бюрократию. Жёсткий режим `dossier-backed completeness / relevant but untransferred` считается откатанным: не нужно строить тотальную matrix по всему досье и доказывать статус каждого релевантного фрагмента.

Мягкий ориентир остаётся: ключевые тезисы статьи должны иметь технические опоры. Если раздел объясняет статус архитектурного решения, его подтверждение, замену, AI/ADR generation/reconstruction, violation detection, traceability, ArchUnit, CODEOWNERS, fitness functions, API compatibility, SLO/performance или agentic workflow, читателю обычно нужны конкретные детали: пример ADR, источник, template, check, сигнал, failure mode, ограничение или визуальный кандидат. Если без такой опоры раздел звучит общей прозой, деталь лучше встроить в основной текст. Если деталь не помогает reader question, относится к соседней статье или ломает ход объяснения, её не нужно вставлять ради отчётности.

`source_transfer_ledger`, `image_plan` и `open_questions` остаются журналами реальных решений, долгов и source gaps. Они не заменяют статью и не должны становиться главным результатом прохода.

## 3. Предполагаемая форма будущей статьи (не текст статьи)

1. **Зачем ADR нужен агентской разработке.** Решение может выглядеть записанным, но агенту всё ещё неясно, имеет ли оно статус, подтверждение и условия замены.
2. **Минимальная форма архитектурного решения.** Nygard, Fowler, MADR, статус, контекст, альтернативы, последствия.
3. **AI/ADR research без иллюзии автоматического решения.** Generation, reconstruction, context window, violation detection, traceability and architecture memory.
4. **Подтверждение решения.** От rationale and review до executable/operational projections: ArchUnit, CODEOWNERS, compatibility, SLO, rollout.
5. **ADR в агентном lifecycle.** До реализации, во время реализации, на review, после merge, при устаревании и замене.
6. **Три вида ошибок.** Мёртвая запись, неподтверждённое убеждение, неправомерное основание для действия агента.
7. **Границы.** Specification vs ADR vs проверочный контракт/оракул; ADR vs PWG/evidence/SDD methods.

## 4. Главный редакторский риск и способ его снять

Главный риск ADR article package — превратить ADR в каталог шаблонов, инструментов или архитектурного управления. Хорошая статья должна удерживать цепочку:

- решение принято или восстановлено;
- известны его причины, ограничения и отвергнутые альтернативы;
- понятны последствия и условия замены;
- задан подходящий уровень подтверждения;
- агентная реализация и review используют record как основание для рассуждения, но не как неизменный закон.

Будущий authoring package должен проверять каждый новый материал: помогает ли он понять статус решения, его подтверждение, замену или риск неправильного использования агентом? Если материал только расширяет список инструментов/шаблонов, его надо связать с этой дугой или перенести в supporting notes.

## 5. Обрабатываемые файлы будущего package

```yaml
- path: work/atlas/articles/adr_method.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_source_transfer_ledger.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_image_plan.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_external_image_queue.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_theory_links.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
- path: work/atlas/articles/adr_method_readiness_report.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Future output for the ADR as method / decision memory atlas article."
```

Group mode: `linked-target-edit`.

## 6. Точные read-only inputs для включения в будущий пакет

```text
START.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/C5_source_usage.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
work/theory-writing/fragments/A10_source_usage.md
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
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
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
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
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

## 7. Внешние источники для будущего package

Внешние источники сгруппированы по функции, чтобы будущий package не воспринимал их как плоский список ссылок. Досье остаётся главным источниковым основанием статьи; внешние источники уточняют, углубляют, проверяют и дают real image candidates.

```text
### Классические ADR-источники, шаблоны и процессы
https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
https://adr.github.io/madr/
https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
https://en.wikipedia.org/wiki/Architectural_decision
https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
https://docs.cloud.google.com/architecture/architecture-decision-records
https://github.com/adr/madr

### AI/ADR research и восстановление архитектурной памяти
https://arxiv.org/abs/2403.01709
https://arxiv.org/abs/2504.08207
https://arxiv.org/abs/2604.03826
https://arxiv.org/abs/2604.27333
https://arxiv.org/abs/2602.07609
https://arxiv.org/abs/1704.04798
https://arxiv.org/abs/1610.09240
https://arxiv.org/abs/2309.14164
https://arxiv.org/abs/2212.13866
https://arxiv.org/abs/2511.02434
https://arxiv.org/abs/2602.04445
https://arxiv.org/html/2602.04445v1
https://github.com/sa4s-serc/AgenticAKM
https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Code/AdrAgents.py
https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Code/main.ipynb
https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Code/CodeToAdr.ipynb
https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Generated_ADRs/adyanshkakran_RL_project/dir4/001_Per-algorithm_monolithic_training_scripts.md
https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Generated_ADRs/Poorvi-HC_DIP-Project/dir4/001_Stage-based_file-backed_pipeline.md
https://arxiv.org/abs/2112.01644
https://arxiv.org/abs/2604.04990
https://arxiv.org/abs/2512.05551
https://arxiv.org/abs/2602.11988
https://arxiv.org/abs/2604.11088
https://github.com/sa4s-serc/AgenticAKM/tree/main/Generated_ADRs
https://arxiv.org/abs/2605.05584

### Инструменты, skills и практические ADR-процессы
https://github.com/npryce/adr-tools
https://7tonshark.com/posts/claude-adr-pattern/
https://github.com/vercel/ai/blob/main/skills/adr-skill/SKILL.md
https://github.com/YotpoLtd/cADR/
https://github.com/wagov-dtt/architecture-decision-records
https://github.com/wagov-dtt/architecture-decision-records/blob/main/CONTRIBUTING.md
https://github.com/wagov-dtt/architecture-decision-records/blob/main/decision-finder.md
https://www.softwareimprovementgroup.com/blog/using-architecture-decision-records-to-guide-your-architecture-choice/
https://github.com/marketplace/actions/adr-sync
https://mnemehq.com/demo/adr-compiler/

### Проверяемые архитектурные правила и совместимость
https://www.archunit.org/userguide/html/000_Index.html
https://github.com/BenMorris/NetArchTest
https://import-linter.readthedocs.io/en/stable/
https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md
https://nx.dev/docs/features/enforce-module-boundaries
https://www.conftest.dev/
https://www.openpolicyagent.org/docs
https://github.com/oasdiff/oasdiff
https://docs.pact.io/
https://docs.pact.io/pact_broker/can_i_deploy

### Операционные сигналы и rollout-подтверждение
https://www.thoughtworks.com/en-us/insights/books/building-evolutionary-architectures
https://grafana.com/docs/k6/latest/using-k6/thresholds/
https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/
https://sre.google/workbook/implementing-slos/
https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/
https://argo-rollouts.readthedocs.io/en/stable/features/analysis/
https://github.com/fluxcd/flagger
https://openfeature.dev/docs/reference/concepts/intro/

### Практические agentic examples и source notes
https://adolfi.dev/blog/ai-generated-adr/
https://www.angulararchitects.io/blog/verlaessliche-angular-architekturen-mit-ai-assisted-coding/
https://github.com/anthropics/claude-code/issues/13853
https://www.linkedin.com/posts/mattwynne_working-in-a-new-repo-shared-by-a-bunch-of-activity-7438400774834958337-ezHC
https://github.com/github/gh-aw/actions/runs/24966700524/agentic_workflow
https://gist.github.com/joshrotenberg/a3ffd160f161c98a61c739392e953764

### Прочие источники из досье
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
```

Дополнительно будущий пакет может открывать первичные ссылки из `ADR_METHOD_DOSSIER.md` and source usage files. Внешний поиск разрешён для проверки свежести, primary sources and visual candidates, но не для создания новых article topics.

## 8. Почему очередь подходит статье

Подходит ли выбранная очередь проходов именно этой статье? Да. ADR dossier unusually dense: classic ADR method, AI/ADR research, agentic practice, executable checks, operational confirmation, lifecycle failures and boundary with specification/test/PWG. Короткая очередь почти наверняка сведёт статью либо к каталогу ADR-шаблонов, либо к общему обзору architecture governance.

S02 фиксирует причины сохранения полной очереди:

- **Источниковая глубина нужна по нескольким слоям.** Nygard/Fowler/MADR, ADR tools, AI/ADR papers, agentic examples and executable/operational confirmation cannot be merged without losing provenance.
- **Подтверждение решения — центральный механизм.** Это не один тест, а цепочка от rationale/review до архитектурных правил, compatibility, SLO/performance and rollout signals.
- **Свободные проходы добора необходимы.** Слабое место может оказаться в AI/ADR research, generated ADR examples, failure modes, operational projection or distinction between decision and check.
- **Визуальные проходы несут смысловую нагрузку.** Templates, decision lifecycle diagrams, research figures, generated ADR examples and check/policy screenshots are real source candidates.
- **Финальная проверка должна блокировать две деградации:** ADR template catalogue and generic architecture-governance overview without decision-status/confirmation/replacement mechanism.

Приоритеты source-depth для этой статьи:

1. classic ADR sources: Nygard, Fowler, MADR and tooling;
2. AI/ADR research: generation, context, template comparison, violation detection, traceability, architecture memory;
3. practical agentic examples: ADR skills, repo patterns, AI-assisted architecture workflows;
4. executable/operational confirmation: ArchUnit, CODEOWNERS, fitness functions, API compatibility, SLO/performance, rollout signals;
5. lifecycle and failure modes: stale ADR, unsupported belief, hallucinated traceability, видимость исполнимой проверки;
6. boundaries with specification, проверочным контрактом/оракулом, TDAD, CSDD and PWG;
7. C5/A10 sync verification after article map and mode-selection map stabilize.

Самодостаточность будущего package: план перечисляет exact read-only inputs and external primary URLs. Будущий package-builder должен bundle-ить эти входы. External search may supplement freshness and primary visual candidates, but must not create new article topics.

### Синхронизация с C5/A10 и provenance manufactury-процесса

```text
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/C5_source_usage.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
work/theory-writing/fragments/A10_source_usage.md
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

Эти файлы существуют в текущем репозиторном состоянии и должны входить в future self-contained bundle как read-only inputs. C5 задаёт concept-first atlas architecture and article map; A10 задаёт mode-selection / reader-routing context. Они не являются hard blockers для каждой статьи, но больше не считаются отсутствующими sync debts. Если future article-writing run обнаружит реальное несогласование, оно фиксируется как конкретный debt, а не как default `C5/A10 sync status`.

## 9. Очередь будущих prompt-ов

### P01 — первичный черновик
```text
Прочитай сначала:
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/theory-writing/fragments/A2_specification_adr_contract.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/A10_mode_selection_map.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Создай `work/atlas/articles/adr_method.md` как самостоятельную статью атласа по ADR как методу архитектурной памяти. Не ограничивай объём. Не пересказывай досье подряд: выстрой статью вокруг статуса архитектурного решения, его подтверждения, условий замены, AI/ADR research, executable/operational projections, failures and boundaries.

Сразу создай все companion-файлы из раздела target outputs. Если часть companion-файлов пока содержит только skeleton/status, всё равно создай файл и явно запиши, что он будет заполняться дальше. Это нужно, чтобы future gated runner не пропустил отсутствующий output.
```

### P02 — контракт статьи и границы
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- protocols/rules/source-and-provenance.md

Уточни вопрос читателя, tier, boundaries, neighboring articles and C5/A10 sync status. Исправь статью, если она превращается в ADR template catalogue, generic governance overview, повтор A2/A9 или справку о проверках вместо статьи о статусе решения и подтверждении.
```

### P03 — dossier inventory
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Сделай inventory досье без тотальной coverage matrix.

Проверь, какие разделы досье уже перенесены, какие отсутствуют, какие требуют открытия первоисточников, и где статье могут не хватать технические опоры для понимания статуса решения, подтверждения или замены. Обнови article and transfer ledger только при явном пропуске article-critical материала или настоящего долга. Не превращай inventory в мини-статью и не строй disposition-таблицу по всему досье.

Ledger должен помогать статье, а не заменять её.
```

### P04 — source-depth 1: Nygard/Fowler/MADR and ADR tooling
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/atlas/articles/adr_method_source_usage.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md

Усиль слой классических ADR-источников: Nygard, Fowler, MADR, adr-tools and repository practices. Переноси не обзор шаблонов, а фактуру, которая помогает понять форму решения, статус, контекст, альтернативы, последствия and replacement semantics. Ссылки ставь сразу при введении материала. Обнови `adr_method_source_usage.md` и `adr_method_source_transfer_ledger.md` только как журналы реальных решений и долгов.
```

### P05 — source-depth 2: AI/ADR research and agentic examples
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/atlas/articles/adr_method_source_usage.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md

Усиль слой AI/ADR research and practical agentic examples: generation, reconstruction, context-window limits, violation detection, traceability and architecture memory. Не превращай это в literature review; показывай, где automatic ADR text is not decision status, reconstructed ADR is not provenance, and traceability without evidence can mislead agents.
```

### P06 — source-depth 3: executable/operational confirmation levels
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/atlas/articles/adr_method_source_usage.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md

Усиль слой подтверждения решения: review, ownership, ArchUnit, CODEOWNERS, fitness functions, API compatibility, SLO/performance thresholds, rollout and operational signals. Покажи, что executable/operational checks are projections of confirmation, not substitutes for the ADR itself. Если раздел звучит общей прозой, добавь конкретные technical anchors.
```

### P07 — source-depth 4: lifecycle, failure modes and boundaries
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/atlas/articles/adr_method_source_usage.md
- protocols/rules/source-and-provenance.md

Усиль lifecycle/failure-mode слой: dead record, unsupported belief, generated traceability without provenance, false executable-check visibility, stale decision, improper action basis for an agent. Проведи границы с specification, проверочным контрактом/оракулом, TDAD, CSDD and PWG через функции в lifecycle, а не через список соседей.
```

### P08 — source-depth 5: anti-summary check against raw sources
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/atlas/articles/adr_method_source_usage.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Проверь, не стала ли статья гладким summary о полезности ADR. Добери конкретику, которая помогает понять механизм, границы, техническую фактуру, ограничения и source-specific texture: examples, templates, research caveats, generated/reconstructed ADR examples, checks, governance/review signals. Не строй coverage matrix; если фактура не помогает reader question, не вставляй её ради отчётности.
```

### P09–P10 — свободный добор материала
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- work/atlas/articles/adr_method_open_questions.md
- work/dossiers/ADR_METHOD_DOSSIER.md

P09 сам выбирает главный недобор фактуры: AI/ADR research, executable confirmation, failure modes, practical agent examples or decision/spec/test boundary. P10 сам выбирает главный недобор связности, границ or reader path. В каждом проходе запиши, что счёл недобором, что добавил, откуда взял материал and что осталось долгом.

Свободный добор должен быть именно добором: сам найди, где статья всё ещё недобирает фактуру, техническую конкретику, ограничения, source-specific детали или связность из досье/первоисточников. Расширь основной текст и companion-файлы; не превращай проход в преждевременную стилистическую шлифовку краткого обзора.

```

### P11–P13 — visual asset passes
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- content/assets/theory-images/MANIFEST.md
- protocols/rules/visual-assets-and-figures.md

P11 классифицирует local assets и создаёт/обновляет `work/atlas/articles/adr_method_image_plan.md`. P12 ищет ADR-specific external real image candidates: templates, decision lifecycle diagrams, research figures, generated ADR examples, executable-check screenshots; ставит inline placeholders, нижний раздел `Внешние изображения для asset-pass` и обновляет `work/atlas/articles/adr_method_external_image_queue.md`; изображения не скачивает. P13 добавляет synthetic figures только при usefulness/nontriviality gate и никогда не заменяет real diagrams/templates/examples текстовой реконструкцией.

Обязательное правило для кандидатов из досье:
- Начни работу с внешними изображениями с основного досье статьи и его разделов вроде `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` или похожих списков.
- Для каждого кандидата на изображение из досье зафиксируй disposition в `<article_id>_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset` или `not_found_in_source`, с короткой причиной.
- Если кандидат реально помогает конкретному месту статьи, поставь `<figure data-asset-status="external-real-candidate">` непосредственно в текст главы и добавь ту же позицию в нижний раздел `Внешние изображения для asset-pass` и `<article_id>_external_image_queue.md`.
- Если релевантный локальный asset уже существует, действует правило insert-or-explain: вставь его как `<figure><img ...></figure>` по месту применения либо явно объясни отказ в image plan. Не игнорируй локальные assets только потому, что тяжёлый файл не был загружен в текущий чат.

```

### P14–P16 — concept reinforcement
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/A2_specification_adr_contract.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- protocols/rules/human-technical-style.md

P14 усиливает самостоятельное объяснение: ADR как память архитектурного решения и мост к подтверждению решения. P15 уточняет механизм, границы и типичные ошибки: мёртвая запись, неподтверждённое убеждение, сгенерированная traceability без provenance, видимость исполнимой проверки. P16 связывает статью с общей AI-driven SDLC рамкой without turning it into a theory chapter. Обнови theory links and degradation audit.
```

### P17 — языковой проход 1
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай первый языковой проход по основному тексту: русский пользовательский текст, английский только для допустимых имён, команд, файлов, статусов, source terms and exact titles. Не меняй аргумент и не выбрасывай фактуру.
```

### P18 — языковой проход 2
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай второй языковой проход: убери английский клей, кальки и случайное смешение языков. ADR, MADR, ArchUnit, CODEOWNERS, SLO, API compatibility and source titles остаются на английском, если это точные названия или устойчивые technical terms. Repair-проходы дальше должны работать уже с русским текстом.
```

### P19 — общий редакторский проход 1
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- work/atlas/articles/adr_method_image_plan.md
- work/atlas/articles/adr_method_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Оцени, насколько статья выполняет задачу; сначала сформулируй проблемы, затем исправь их. Не подменяй этот проход source, visual, language или style pass. Проверь, удержана ли дуга: decision status → rationale/alternatives/consequences → confirmation → replacement → agentic misuse risks.
```

### P20 — общий редакторский проход 2
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- work/atlas/articles/adr_method_image_plan.md
- work/atlas/articles/adr_method_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Перечитай после P19. Сначала сформулируй проблемы, затем исправь их. Проверь последствия ремонта: не потерялась ли фактура, не стала ли статья template catalogue, не распался ли главный вопрос, не остались ли ключевые тезисы без технических опор.
```

### P21 — общий редакторский проход 3
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_degradation_and_duplication_audit.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Проведи адверсариальное чтение. Сначала сформулируй проблемы, затем исправь их. Проверь: статья не стала generic architecture governance overview, повтором specification/PWG, справкой о проверках или набором ADR tools без объяснения статуса решения, подтверждения и замены.
```

### P22 — public/article structure and entry-sequence pass
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md

Проверь вход, headings, reader path, first screen and public article structure. Читатель должен быстро понять, что ADR здесь рассматривается как метод сохранения архитектурного решения, его статуса, подтверждения и условий замены. Не начинай статью с каталога шаблонов, tool list или research survey. Если boundary/taxonomy перегружает вход, перенеси её ниже.
```

### P23 — companion sync
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_source_usage.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- work/atlas/articles/adr_method_image_plan.md
- work/atlas/articles/adr_method_external_image_queue.md
- work/atlas/articles/adr_method_open_questions.md
- work/atlas/articles/adr_method_theory_links.md
- work/atlas/articles/adr_method_degradation_and_duplication_audit.md

Синхронизируй companion-файлы со статьёй. Удали устаревшие долги, сохрани настоящие blockers, не оставляй стандартных `C5/A10 sync pending`: C5 и A10 доступны как read-only context, а любые проблемы должны быть конкретными долгами статьи. Проверь, что source usage, image plan, external image queue и theory links соответствуют фактической статье. Ledger не должен раздуваться как coverage-бюрократия вместо переноса фактуры в основной текст.
```

### P24 — style defect audit
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Сделай стилевой аудит без тотального переписывания. Найди реальные дефекты: смысловые свёртки, псевдотермины, кальки, тяжёлые цепочки родительного падежа, неестественные заголовки, канцелярит и обратный дефект — механическое разворачивание нормальной мысли в протокольную конструкцию. Отметь места, где правка действительно нужна, и не трогай компактные фразы, если они звучат нормально по-русски и не прячут смысл.
```

### P25 — selective natural rewrite
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Выборочно перепиши только реально плохие места из style defect audit. Цель — нормальный русский технический текст, а не тотальное разжатие, не канцелярит и не новая компактная псевдотерминология. Можно менять заголовки, порядок слов и синтаксис; нельзя выбрасывать источниковую фактуру, команды, числа, ограничения, границы или technical anchors.
```

### P26 — guarded final human technical style pass
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Финально выровняй тон, ритм, переходы, подзаголовки и человеческую техническую фразу. Можно сильно менять форму, если сохраняются смысл, источниковая фактура, команды, числа, ограничения и границы. Нельзя возвращать псевдотермины, нельзя выбрасывать конкретику ради гладкости и нельзя превращать прозу в протокольные конструкции вида «кто действует / что проверяется / чем подтверждается» там, где можно сказать проще.
```

### Final — финальная проверка и package-readiness
```text
Прочитай сначала:
- work/atlas/articles/adr_method.md
- work/atlas/articles/adr_method_source_usage.md
- work/atlas/articles/adr_method_source_transfer_ledger.md
- work/atlas/articles/adr_method_image_plan.md
- work/atlas/articles/adr_method_external_image_queue.md
- work/atlas/articles/adr_method_open_questions.md
- work/atlas/articles/adr_method_theory_links.md
- work/atlas/articles/adr_method_degradation_and_duplication_audit.md
- work/atlas/articles/adr_method_readiness_report.md
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- protocols/rules/visual-assets-and-figures.md

Проверь реальные файлы результата: article exists and not empty, companion files synchronized, source usage and transfer ledger filled, provenance present, local assets handled as real image figures, external candidates have inline placeholders/bottom section/queue, synthetic figures rare, controlled repetition justified. Отдельно заблокируй две деградации: статья не должна быть ADR template catalogue и не должна быть generic architecture-governance overview without decision-status/confirmation/replacement mechanism; она должна объяснять архитектурное решение, его статус, способы подтверждения and replacement conditions. Запиши readiness report, MANIFEST/VERIFY/RESUME и final readiness status.

Technical anchoring final check:
- ключевые тезисы не закрыты общей прозой там, где для понимания нужны технические опоры;
- source transfer ledger не заменяет основной текст и не заполнен общими словами;
- source-depth and free-expansion проходы действительно перенесли фактуру, которая помогает понять механизм, границы, техническую конкретику и ограничения ADR as method.

Final visual/source check:
- every dossier image candidate has a disposition in `<article_id>_image_plan.md`;
- every inline external-real placeholder also appears in the bottom `Внешние изображения для asset-pass` section and in `<article_id>_external_image_queue.md`;
- every relevant local asset is either inserted as a real `<img>` figure or explicitly rejected with reason;
- no real source image or local asset is replaced by a text/synthetic diagram.

Style final check:
- после style defect audit / selective rewrite не остались заметные псевдотермины и неестественные заголовки;
- текст не ушёл в обратный дефект: механическое разворачивание, тяжёлые именные группы и протокольные конструкции вместо нормальной русской технической фразы.
```

## Visual candidate disposition guarantee

Every generated article plan must ensure that the future article-writing package starts image work from three sources at once:

1. local asset catalogs and manifests;
2. repository-level external image candidate catalogs;
3. the main dossier's own image-candidate section, especially headings such as `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates`, or equivalent lists.

For each dossier image candidate the future article package must record a disposition in the article image plan: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset`, or `not_found_in_source`, with a short reason.

If a candidate belongs in the article, the package must put an inline `<figure data-asset-status="external-real-candidate">` at the place where the image will be used and mirror the same item in the bottom section `Внешние изображения для asset-pass` and in `<article_id>_external_image_queue.md`.

If a relevant local asset already exists, use insert-or-explain: insert it as `<figure><img ...></figure>` at the relevant point, or explicitly reject it in the image plan. Never replace a real image, screenshot, diagram, template, table or local asset with a synthetic text diagram unless the user explicitly asks for a redraw/replacement.

## Prompt-record manifest for package builder

Этот manifest разворачивает очередь будущего article-writing package в отдельные prompt records. При сборке executor-пакета нельзя оставлять сгруппированные диапазоны вроде `P04–P08` или `P17–P19` одним record: каждый пункт ниже должен стать отдельным gated prompt.

```text
P01 — primary article draft
P02 — article contract and boundaries
P03 — dossier inventory
P04 — source-depth pass 1
P05 — source-depth pass 2
P06 — source-depth pass 3
P07 — source-depth pass 4
P08 — source-depth pass 5 / anti-summary check
P09 — free material-expansion pass 1
P10 — free material-expansion pass 2
P11 — visual asset pass 1: local assets
P12 — visual asset pass 2: external real image candidates
P13 — visual asset pass 3: rare nontrivial synthetic figures
P14 — concept reinforcement 1: standalone concept explanation
P15 — concept reinforcement 2: mechanism, boundaries, typical mistakes
P16 — concept reinforcement 3: links to broader theory without rewriting it
P17 — language pass 1
P18 — language pass 2
P19 — general editorial pass 1
P20 — general editorial pass 2
P21 — general editorial pass 3
P22 — public/article structure and entry-sequence pass
P23 — companion sync / source ledger / image queue pass
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style pass
Final — final verification, package output, readiness status
```

The article-specific queue above this manifest may describe several passes together for readability, but package manufacturing must expand them according to this manifest and preserve the article-specific emphasis written in the queue and Article contract.


## 10. S02 integrated strengthening

S02 усилил план до article-specific form:

- reader question sharpened around architecture decision status, confirmation and replacement;
- ADR framed as method of preserving architectural decisions in AI-assisted lifecycle, not template catalogue;
- three ADR-specific failure modes made central: dead record, unsupported belief, improper action basis for an agent;
- AI/ADR research integrated into the argument as source of generation/reconstruction/violation-detection risks, not as separate literature review;
- confirmation reframed in plain language: how to know whether the decision is still observed or should be revisited;
- pass queue justified specifically for classic sources, AI/ADR research, agentic examples and executable/operational confirmation;
- final verification now blocks ADR template catalogue and generic governance overview;
- C5/A10 sync is available context, not blocker for package manufacture.

## 11. S03 editorial strengthening

S03 reviewed the plan as a whole and repaired the main composition risk: ADR must not become a tool/template catalogue. It now has an explicit editorial rule: every source addition should clarify decision status, confirmation, replacement or risk of agent misuse.

For the future authoring package this means:

- executable checks are not substitutes for ADR; they are projections of confirmation;
- AI-generated/reconstructed ADRs require provenance and evidence, not just plausible text;
- old ADRs can be wrong, stale or over-authoritative; replacement semantics must remain visible;
- comparison with specification/test/PWG should explain different roles in the lifecycle.

S04/S05 should now focus on buildability and readiness, not on inventing another article concept.

## 12. S04 integrated guardrails

S04 проверяет, что будущий article-writing package можно собрать без неявных допущений.

Buildability fixes embedded in this plan:

- все target outputs имеют конкретные пути в `work/atlas/articles/`;
- все companion outputs из раздела 5 упомянуты в prompt queue and final verification;
- P01 требует создать все target outputs хотя бы как skeleton/status, чтобы future runner не пропустил отсутствующие файлы;
- source-depth проходы обязаны переносить classic ADR, AI/ADR research, practical examples and executable confirmation, а не писать ADR-template overview;
- free expansion passes должны находить реальный недобор: research details, confirmation levels, practical agent examples, failure modes, decision/spec/test boundaries;
- visual pass различает local image asset, external real image candidate and synthetic figure;
- ADR templates, decision lifecycle diagrams, research figures, generated ADR examples and executable-check screenshots must be external real candidates when not localized;
- external real image candidates должны появляться как inline placeholders, нижний раздел `Внешние изображения для asset-pass` and `adr_method_external_image_queue.md`;
- synthetic figures допускаются только через usefulness/nontriviality gate and не заменяют real diagrams/templates/examples;
- final verification checks real output files and exact companion names;
- внутренних ограничений объёма нет; summary-provoking wording is explicitly blocked;
- external search allowed only as supplement for freshness, primary sources and visual candidates, not for creating new article topics.


## 13. Проверки S04–S05

S04 должен проверить buildability, exact paths, companion names, output coverage, no internal length limits, visual guardrails and package contract. S05 должен поставить readiness status and update ledger.

## Post-import sync note

После импорта результата manufactury-пакета в актуальное репозиторное состояние C5 и A10 уже доступны. План синхронизирован с ними как с контекстом для чтения; оставшиеся долги должны быть конкретными долгами отдельной статьи, а не стандартной пометкой о незавершённой синхронизации с C5/A10.
