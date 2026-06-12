# План написания несущих узлов теоретической главы

Статус: принятый рабочий план перед пакетным написанием теоретической главы.  
Дата: 2026-06-10.  
Основание: `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` v4.3-PWG, текущие досье, истории, story-dossiers, сравнительные отчёты и обсуждение порядка письма.

## Назначение

Этот документ фиксирует порядок написания самых важных фрагментов теоретического раздела до полного написания глав.

Идея: сначала написать не подряд все главы, а несущие узлы — сравнительные подглавы, мосты и итоговые тезисы глубоких опорных узлов. Эти фрагменты должны задать настоящую теорию, чтобы последующие главы не превратились в пересказ досье.

Затем каждая глава пишется отдельным пакетным заданием с учётом:

- текущего скелетона;
- соответствующих досье и историй;
- уже написанных несущих узлов;
- карты документов;
- языкового протокола;
- границы между теорией, историями и техническим атласом.

## Общая последовательность

```text
Фаза 0. Карта сквозных понятий и spine-map.
Фаза 1. Несущие синтетические узлы.
Фаза 2. Итоговые фрагменты глубоких опорных узлов.
Фаза 3. Переходные мосты между главами.
Фаза 4. Пакетное написание каждой главы.
Фаза 5. Композиционный проход по всей теории.
Фаза 6. Отдельный языковой проход.
Фаза 7. Отдельный стилевой проход.
```

Языковой и стилевой проходы не смешиваются с письмом. Source accumulation не выполняется внутри writing-pass, если только пакет явно не обнаружил нехватку фактуры и не остановился с требованием отдельного source-pass.

---

# Фаза 0. Spine-map и терминологический контракт

## 0.1. Карта сквозных понятий

Будущий файл:

```text
work/theory-writing/fragments/00_spine_map.md
```

Назначение: коротко зафиксировать сквозной каркас, чтобы все последующие фрагменты писались в одной системе понятий.

Обязательные понятия:

- программное изменение;
- жизненный цикл программного изменения;
- спецификация;
- память решения;
- устойчивый граф работы;
- среда исполнения;
- workflow engine;
- пакет свидетельств;
- право действовать;
- право завершать;
- последующий ремонт жизненного цикла;
- технический атлас.

Материалы прежде всего:

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`;
- `work/approved-ai-sdlc-plan.md`;
- `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`;
- `work/reports/SKELETON_V4_3_PWG_CONSOLIDATION_REPORT.md`;
- `work/reports/SKELETON_V4_3_PWG_MATERIAL_READINESS_SOURCES_UPDATE.md`;
- `work/theory-source-map-ai-driven-sdlc.md`;
- `content/Orientation.md`;
- `content/Cross_story_synthesis.md`.

Выход:

- короткий рабочий фрагмент, не публичная глава;
- словарь терминов;

Адресные усиления перед общими редакторскими проходами:

- проверка терминологического контракта под нагрузкой на SPDD, PWG, Gas Town, свидетельства, право действовать/признавать изменение принятым и последующую поддержку артефактов;
- проверка, что spine-map остался рабочим контрактом языка, а не оглавлением будущих глав;
- запрет на пересказ историй внутри теории;
- указание, что technical atlas работает как концептуально-технический атлас: даёт самостоятельные связные статьи по концепциям, но не заменяет поперечный синтез теории.

---

# Фаза 1. Несущие синтетические узлы

## A1. Единица анализа: программное изменение, а не prompt

Будущий файл:

```text
work/theory-writing/fragments/A1_change_not_prompt.md
```

Где используется: Введение, Часть I, заключение.

Задача: задать главный объект теории. Агентская разработка должна описываться не как `prompt → code`, а как жизненный цикл изменения.

Главный тезис:

```text
Prompt слишком мал как единица анализа. Изменение проходит через намерение, решение, рабочее состояние, исполнение, свидетельства, завершение и сопровождение.
```

Материалы прежде всего:

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`;
- `content/Orientation.md`;
- `content/Cross_story_synthesis.md`;
- `content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md`;
- `content/stories/03_simon_willison_agentic_research_reconstruction_connected.md`;
- `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md`;
- `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md`;
- `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`;
- `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md`;
- `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md`.

Проверка качества:

- не превращать в общее введение про ИИ;
- не пересказывать истории;
- дать ясное различие между prompt, task, change и lifecycle.

## A2. Сравнительный узел: specification / ADR / contract

Будущий файл:

```text
work/theory-writing/fragments/A2_specification_adr_contract.md
```

Где используется: Часть III, Часть XI, technical atlas ADR.

Задача: развести три типа артефактов, которые часто смешиваются.

Главное различение:

```text
specification — что должно измениться и в каких границах;
contract — какое проверяемое ожидание нельзя сломать;
ADR — почему архитектурное решение принято и каков его статус.
```

Обязательные внутренние узлы:

- specification как рабочая поверхность агента;
- contract как проверяемое ожидание;
- ADR как память архитектурного решения;
- Nygard и MADR как основания теории ADR;
- status vs origin;
- reconstructed ADR;
- operational projection для агента;
- confirmation beyond owner review.

Материалы прежде всего:

- `work/dossiers/ADR_METHOD_DOSSIER.md`;
- `work/dossiers/SPDD_METHOD_DOSSIER.md`;
- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`;
- `work/dossiers/KIRO_SPECS_DOSSIER.md`;
- `work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md`;
- `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`;
- `work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md`;
- `work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`.

Проверка качества:

- Nygard и MADR должны быть в теории, не только в атласе;
- ADR не должен разрастись до отдельного deep case;
- reconstructed ADR не должен становиться accepted ADR;
- operational projection не должна заменять full ADR.

## A3. Сравнительный синтез specification methodologies

Будущий файл:

```text
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
```

Где используется: Часть V.

Задача: написать не обзор методологий, а синтез способов, которыми намерение становится управляемым артефактом.

Сравниваемые узлы:

- SPDD;
- Spec Kit;
- Kiro Specs;
- TDAD: Test-Driven AI Agent Definition;
- TDAD: Test-Driven Agentic Development;
- Constitutional SDD.

Оси сравнения:

- центральный артефакт;
- человеческий gate;
- что считается проверкой;
- что устаревает;
- какой тип сбоя наиболее вероятен;
- что уходит в Handbook / Fieldbook.

Материалы прежде всего:

- `work/dossiers/SPDD_METHOD_DOSSIER.md`;
- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`;
- `work/dossiers/KIRO_SPECS_DOSSIER.md`;
- `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`;
- `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md`;
- `work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md`;
- `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`;
- `work/reports/SPEC_KIT_DOSSIER_QUALITY_AUDIT.md`;
- `work/reports/KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md`;
- `work/reports/TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md`;
- `work/reports/CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md`.

Проверка качества:

- не пересказывать каждую методологию по очереди;
- извлечь сравнительный механизм;
- удержать protected methodology depth;
- не потерять различие двух TDAD.

## A4. Persistent Work Graph: границы механизма

Будущий файл:

```text
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
```

Где используется: Часть VII, Часть X, Часть XI, Часть XIII, technical atlas PWG.

Задача: зафиксировать PWG как самостоятельный глубокий механизм рабочего состояния.

Главный тезис:

```text
Persistent Work Graph — не трекер задач и не execution runtime, а долговечный рабочий субстрат: работа, зависимости, владелец, gate, готовность, handoff, prime, пакет свидетельств, recovery и cleanup.
```

Обязательные различения:

- PWG ≠ GitHub Issues / Linear;
- PWG ≠ Taskmaster;
- PWG ≠ LangGraph / Temporal / durable execution;
- PWG ≠ CRDT editor;
- PWG ≠ STORM-like mediator;
- PWG ≠ Gas Town целиком.

Материалы прежде всего:

- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md`;
- `work/reports/PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md`;
- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md`;
- `work/dossiers/GSD_METHOD_DOSSIER.md`;
- `work/dossiers/BMAD_METHOD_DOSSIER.md`;
- `work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md`;
- `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md`;
- `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`.

Проверка качества:

- не свести PWG к Beads;
- не свести PWG к будущей файловой реализации;
- не использовать отклонённый cycle 05 как основание;
- показать source work / citation audit как важный частный случай для документной работы.

## A5. Сравнительный синтез process methodologies: когда процесс становится артефактом

Будущий файл:

```text
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
```

Где используется: Часть VIII.

Задача: объяснить лестницу внешней процессной структуры.

Сравниваемые узлы:

- разговор;
- research / plan;
- spec-first;
- GSD / Open GSD;
- BMAD;
- Reversa / OpenSpec / AgentSPEX;
- PWG;
- Gas Town.

Ось:

```text
conversation → plan → spec-first → лёгкое внешнее состояние → role-based process → persistent work graph → organizational environment
```

Материалы прежде всего:

- `work/dossiers/GSD_METHOD_DOSSIER.md`;
- `work/dossiers/BMAD_METHOD_DOSSIER.md`;
- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md`;
- `work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md`;
- `content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md`;
- `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md`;
- `content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md`.

Проверка качества:

- не сделать каталог process-methods;
- показать, когда дополнительная структура полезна, а когда вредна;
- связать GSD/BMAD с PWG, но не растворить их в PWG.

## A6. Execution envelope / workflow engine / platform agent

Будущий файл:

```text
work/theory-writing/fragments/A6_execution_environment_distinctions.md
```

Где используется: Часть IX.

Задача: развести несколько разных слоёв, которые часто сливаются в “агентная среда”.

Различения:

- execution envelope: sandbox, worktree, devbox, permissions, approvals;
- tool / sensor surface: CLI, browser, logs, database, MCP, scripts;
- workflow engine: structured run, replay, resumability, observability, failure recovery;
- platform agent: internal developer platform, blueprints, CI limits, human review.

Материалы прежде всего:

- `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md`;
- `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md`;
- `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md`;
- `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md`;
- `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`;
- `work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md`;
- `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md`;
- `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md`;
- `work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md`;
- `work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`.

Проверка качества:

- не смешать Roast, Stripe Minions, Quix, Armin, Sandvault и HumanLayer в один тип;
- показать, что worktree не решает semantic coordination;
- показать, что workflow engine не заменяет PWG.

## A7. Наблюдение vs свидетельство

Будущий файл:

```text
work/theory-writing/fragments/A7_observation_vs_evidence.md
```

Где используется: Часть XI.

Главная формула:

```text
Наблюдение помогает агенту продолжить работу. Свидетельство позволяет человеку принять или отклонить изменение.
```

Материалы прежде всего:

- `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`;
- `work/dossiers/ADR_METHOD_DOSSIER.md`;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `content/stories/03_simon_willison_agentic_research_reconstruction_connected.md`;
- `content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md`;
- `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md`;
- `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md`;
- `work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md`;
- `work/reports/PRODUCT_MIGRATION_CLAUDE_CODE_ANTI_DEGRADATION_REPORT.md`.

Проверка качества:

- summary агента не считается свидетельством;
- replay/transcript может быть наблюдением или свидетельством в зависимости от использования;
- `completed` в PWG без evidence package не является завершением.

## A8. Право действовать vs право завершать

Будущий файл:

```text
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
```

Где используется: Часть XII.

Главный тезис:

```text
Агент может получить право действовать, но не право самостоятельно считать изменение принятым.
```

Материалы прежде всего:

- `work/dossiers/ADR_METHOD_DOSSIER.md`;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md`;
- `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md`;
- `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md`;
- `work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md`;
- `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md`;
- `work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`.

Проверка качества:

- не превращать Zig в “этическую вставку”;
- показать contribution boundary как governance-механизм;
- связать authority с CODEOWNERS, human review, ADR status и PWG gate.

## A9. Lifecycle repair: что должно обновиться после merge

Будущий файл:

```text
work/theory-writing/fragments/A9_lifecycle_repair.md
```

Где используется: Часть XIII, заключение.

Главный тезис:

```text
Merge не завершает жизненный цикл. После merge остаётся работа по возвращению последствий изменения в спецификации, ADR, operational projections, правила, skills, граф работы и evidence gates.
```

Материалы прежде всего:

- `work/dossiers/ADR_METHOD_DOSSIER.md`;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `work/dossiers/GSD_METHOD_DOSSIER.md`;
- `work/dossiers/BMAD_METHOD_DOSSIER.md`;
- `content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md`;
- `content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md`;
- `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md`;
- `work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md`.

Проверка качества:

- не свести последующий repair к набору “cleanup tasks”;
- показать learning loop среды;
- связать stale artifacts с будущей ошибкой агента.

## A10. Карта выбора режима

Будущий основной файл:

```text
work/theory-writing/fragments/A10_mode_selection_map.md
```

Дополнительные рабочие выходы:

```text
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
```

Где используется: заключение, composition pass, будущий Handbook / Fieldbook.

Dependency gate: `A10` пишется после `C1`–`C4`, а не параллельно с ними. После интеграции результатов `00` и `C1`–`C4` новый пакет A10 можно собирать заново по обновлённому 17-pass плану; ранний `A10_MODE_SELECTION_MAP.zip` остаётся premature/superseded и не используется.

Финальная рамка: A10 — это не резюме A1–A9 и не maturity model. Это карта выбора минимально достаточного режима работы с агентом: когда достаточно разговора; когда нужен план; когда спецификация; когда ADR; когда PWG; когда процессный профиль; когда дисциплина среды исполнения; когда нужны свидетельства; когда возникает граница полномочий; когда нужна последующая поддержка артефактов после merge; и когда всё это не нужно.

Материалы прежде всего:

- все фрагменты A1–A9;
- B1–B3;
- C1–C4 и их companion-файлы;
- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`;
- `work/approved-ai-sdlc-plan.md`;
- `content/Cross_story_synthesis.md`;
- `work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`;
- `work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md`.

Проверка качества:

- карта должна помогать выбирать режим изменения, а не повторять оглавление;
- режимы должны комбинироваться, а не выстраиваться в скрытую лестницу зрелости;
- должны быть видны эскалация и деэскалация структуры;
- `A10_mode_selection_matrix.md` должен хранить рабочие критерии выбора;
- `A10_decision_stress_tests.md` должен проверять карту на реальных сценариях;
- в A10 должен быть виден переход к Handbook / Fieldbook.

Адресные усиления перед общими редакторскими проходами:

- критерии выбора режима;
- переходы, эскалация и деэскалация;
- сочетания режимов и минимально достаточная структура;
- сценарный stress-test практической применимости.

После общей редакторской тройки нужен отдельный public decision-map / visual-artifact pass: A10 должен быть применимой картой решения, а не только хорошим эссе.

---

# Фаза 2. Итоговые фрагменты глубоких опорных узлов

## B1. Что SPDD даёт AI-driven SDLC — и чего не решает

Будущий файл:

```text
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
```

Главный тезис:

```text
SPDD превращает prompt в delivery artifact и specification lifecycle, но не решает durable work state, ownership, gates, handoff and recovery.
```

Материалы прежде всего:

- `work/dossiers/SPDD_METHOD_DOSSIER.md`;
- `work/anchor-seed-spdd-old-site.md`;
- `work/old-site-theoretical-synthesis-baseline.md`;
- `content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md`;
- `work/reports/SPDD_LANGUAGE_SANITY_PASS_REPORT.md`.

## B2. Что PWG даёт общей теории

Будущий файл:

```text
work/theory-writing/fragments/B2_pwg_contribution.md
```

Главный тезис:

```text
Работа живёт не в prompt-е, не в стенограмме и не только в issue, а в долговечном графе состояний, gates, свидетельств и артефактов.
```

Материалы прежде всего:

- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md`;
- `work/reports/PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md`;
- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md`;
- `work/reports/SKELETON_V4_3_PWG_CONSOLIDATION_REPORT.md`.

## B3. Что Gas Town даёт сверх PWG

Будущий файл:

```text
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
```

Главный тезис:

```text
PWG даёт долговечное состояние работы; Gas Town добавляет организационную среду, роли, Mayor, service agents, операционную культуру и стоимость оркестрации.
```

Материалы прежде всего:

- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md`;
- `work/anchor-seed-gas-town-old-site.md`;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`;
- `work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md`.

---

# Фаза 3. Переходные мосты

Переходные мосты пишутся после фрагментов A и B, но до полных глав. Для тогда ещё не построенных узлов `00`, `C1`–`C4` в соответствующие target-group plans добавлены адресные проходы усиления основной функции перед общей редакторской тройкой. `A10` пишется позднее, после `C1`–`C4`, потому что финальная карта выбора режимов должна учитывать переходные мосты. `C5` получил отдельную позднюю очередь: 17 рабочих проходов плюс финальная проверка, с моделью самостоятельной статьи концептуально-технического атласа, картой будущих статей атласа и тремя адресными проходами по самостоятельной ценности, контролируемому повторению и двусторонней навигации theory-first / concept-first. Карта статей атласа должна различать tiers статей, reader questions, boundaries, готовность ассетов/источников и semantic back-links; она не должна превращаться в мини-атлас до написания самого атласа.

## C1. Specification → PWG

Будущий файл:

```text
work/theory-writing/fragments/C1_specification_to_pwg.md
```

Задача: объяснить, почему спецификация не хранит всю динамику работы: owner, gates, readiness, source state, recovery.

## C2. PWG → процессный профильs

Будущий файл:

```text
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
```

Задача: показать, почему GSD/BMAD — лёгкие forms внешнего состояния, но не полноценный PWG.

## C3. PWG → evidence

Будущий файл:

```text
work/theory-writing/fragments/C3_pwg_to_evidence.md
```

Задача: показать, почему статус `completed` без привязанных к обещаниям изменения свидетельств превращается в преждевременное закрытие работы.

## C4. Execution runtime → PWG

Будущий файл:

```text
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
```

Задача: показать, что runtime выполняет шаг и хранит следы запуска, но не хранит сам по себе смысл работы, право продолжения, контрольные условия и последующую поддержку артефактов.

## C5. Theory ↔ concept-first atlas

Будущий файл:

```text
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
```

Задача: зафиксировать две траектории чтения. Теория даёт поперечный SDLC-синтез; концептуально-технический атлас даёт самостоятельные concept-first articles по конкретным методологиям и инструментальным формам. C5 должен задать модель atlas article, карту будущих статей и правила controlled repetition без превращения атласа ни в склад деталей, ни во вторую копию всей теории. Article map должна быть не плоским списком тем, а registry-level картой: tier, reader question, article boundary, allowed repetition, asset/source readiness and semantic back-links.

---

# Фаза 4. Пакетное написание глав

Каждая глава пишется отдельным package-run. Пакет должен читать:

- скелетон;
- соответствующие досье;
- соответствующие опубликованные истории;
- соответствующие story-dossiers;
- уже написанные несущие фрагменты;
- карту документов;
- языковой протокол;
- quality gates.

Каждый пакет должен создать:

```text
draft.md
source_usage.md
story_anchor_map.md
used_fragments.md
omitted_material.md
open_questions.md
degradation_audit.md
```

Глава не должна пересказывать истории. Она должна использовать истории как короткие фактические якоря и ссылки.

---

# Фаза 5. Композиционный проход

После написания всех глав нужен отдельный composition pass.

Задачи:

- проверить порядок аргумента;
- убрать повторы между фрагментами и главами;
- выровнять термины;
- проверить мосты между главами;
- убрать внутренние ссылки на рабочие материалы;
- расставить ссылки на истории;
- проверить, что технический атлас не заменяет поперечный синтез теории, но и не сводится к складу технических деталей;
- проверить, что теория не стала taxonomy of methods.

Обязательный ledger:

```text
work/theory-writing/duplication_ledger.md
```

---

# Фаза 6–7. Язык и стиль

После composition pass выполняются отдельно:

1. языковой проход по `protocols/rules/russian-language.md`;
2. стилевой проход по `protocols/rules/human-technical-style.md` и связанным правилам;
3. проверка ссылок, raw URL and Markdown targets;
4. проверка, что code-like элементы, source titles, file paths, commands and API names не были испорчены.

Эти проходы не должны добавлять новую фактуру и не должны менять теоретическую структуру.

## Package status: A10 built, C5 blocked until A10 result

After importing and repairing `00` and `C1`–`C4`, a new `A10_MODE_SELECTION_MAP.zip` package has been built from the 17-pass A10 plan. This package supersedes any earlier A10 package created before C results existed.

C5 remains downstream of A10. Do not build `C5_THEORY_TO_TECHNICAL_ATLAS.zip` until `A10_mode_selection_map.md` has been produced, imported and repaired.

## 2026-06-12 correction: C5 may be packaged before A10 result

After reviewing the concept-first atlas decision, the dependency gate for C5 was relaxed. C5 is an architectural bridge for the concept-first atlas, not a continuation of the A10 mode-selection map. Required upstreams are `00`, A/B fragments, B1–B3, C1–C4, ADR-0011, dossiers and source/asset maps. A10 remains useful for later synchronization, but its absence should be recorded as `A10 sync pending`, not treated as a package blocker.

### 2026-06-12 — blueprint for future concept-atlas article packages

Для будущих статей концептуально-технического атласа добавлен отдельный blueprint: `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`. Он не заменяет C5, а задаёт общий шаблон планов статей атласа: 25 рабочих проходов плюс финальная проверка, отсутствие внутренних лимитов объёма, несколько source-depth проходов, два свободных прохода добора материала, активное использование локальных и внешних изображений, controlled repetition with theory and companion/source/image ledgers. C5 полезен для последующей синхронизации article map, но не является hard gate для разработки blueprint или первых конкретных article plans.


## 2026-06-12 — C5 result imported and synced

C5 result files have been imported and evaluated. C5 now performs the bridge between theory-first and concept-first reading routes and includes `C5_concept_atlas_article_map.md` as a registry-level map for future atlas articles. Since A10 is now present, C5 was post-import synchronized with `A10_mode_selection_map.md`, `A10_mode_selection_matrix.md` and `A10_decision_stress_tests.md`. Current status: `ready_with_known_debts / A10 synced`.
