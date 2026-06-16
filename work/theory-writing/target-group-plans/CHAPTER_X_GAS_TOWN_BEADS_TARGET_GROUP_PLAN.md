# План целевой группы — Глава X: Gas Town / Beads и организация многоагентной рабочей среды

Статус: рабочий план для пакета главы.  
Режим внешнего поиска: `D1`; тип пакета — `normal_synthesis`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, обновлённый blueprint и материалы главы X.

## 1. Зачем нужна эта глава

Глава X должна показать Gas Town / Beads не как любопытный проект с городскими названиями, а как пример того, как проект организует работу многих агентов и рабочих площадок. После VII–IX уже есть состояние работы, выбранный способ продолжения и среда исполнения. Теперь возникает новая проблема: рабочих потоков много, они идут параллельно, зависают, нарушают порядок, требуют сервисных ролей и должны возвращать результат в общее состояние.

PWG остаётся предшественником и границей. Он показывает, где находится работа. Gas Town / Beads показывают, что происходит, когда таких работ несколько и их нужно обслуживать как поток: держать очередь, видеть зависания, ограничивать рабочие площадки, возвращать результаты, поднимать сигнал человеку и чинить сам ход работы, а не только отдельную задачу.

Главная формула главы: когда рабочих потоков становится много, проекту уже недостаточно знать состояние отдельной работы, выбрать способ продолжения и ограничить среду исполнения. Ему нужно обслуживать сам поток: очереди, рабочие площадки, зависания, нарушения, сервисные роли, обратные сигналы и возврат результатов в общее состояние.

План задаёт работу, а не готовый текст главы. Исполнитель не должен переносить формулировки плана в основной текст без переписывания. Все выходные материалы — сама глава, журналы поиска, реестры, отчёты и проходы — пишутся нормальным русским языком. Технические имена файлов, команд, моделей, методов и полей сохраняются точно там, где это нужно для источника.

У главы нет целевого объёма, нормальной длины и скрытого ориентира вроде 40 тысяч знаков. Текст должен стать таким длинным, каким требует исходный материал: плотность источников, число важных различений, количество нужных сцен, визуальный слой и объём фактуры из Атласа, досье, фрагментов, историй и внешних источников. Если после первого черновика остаются значимые недоразобранные источники или тонкие места, работу нужно продолжать, а не полировать прежний объём.


## 2. Границы главы

Главный риск — превратить главу в экскурсию по Gas Town. Mayor, town, rig, crew, polecat и другие имена нужно сохранять как имена источника, но не строить русский текст вокруг городской метафоры. Объяснение должно говорить о видимости для человека, рабочих площадках, исполнителях, сервисных ролях, очередях, нарушениях процесса, обратных сигналах и возврате результата.

Вторая граница — не повторить VI про subagents. Subagent выполняет часть задачи. Service agent в этой главе обслуживает среду работы: следит за очередью, проверяет нарушение порядка, собирает состояние, обновляет Beads, чистит мусор, возвращает результаты и поднимает сигнал человеку. Это различие нужно держать явно.

Третья граница — не превратить X в полную теорию проверки. Gas Town может организовать поток, вернуть результат в состояние и показать, где работа застряла. Но организация потока ещё не доказывает, что результат достаточно проверен. Это должен забрать следующий блок про проверочный материал.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/X_gas_town_beads.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/X_gas_town_beads_source_register.md
work/theory-writing/chapters/X_gas_town_beads_fragment_usage.md
work/theory-writing/chapters/X_gas_town_beads_atlas_usage.md
work/theory-writing/chapters/X_gas_town_beads_dossier_gap_notes.md
work/theory-writing/chapters/X_gas_town_beads_external_discovery_log.md
work/theory-writing/chapters/X_gas_town_beads_story_anchors.md
work/theory-writing/chapters/X_gas_town_beads_figure_candidates.md
work/theory-writing/chapters/X_gas_town_beads_open_questions.md
work/theory-writing/chapters/X_gas_town_beads_degradation_and_duplication_audit.md
work/theory-writing/chapters/X_gas_town_beads_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/X_gas_town_beads_passes/
```

Пиши создаваемый текст естественным русским языком. Это относится к главе, рабочим заметкам, журналам поиска, реестрам, отчётам, сопутствующим файлам и записям в проходах.

Формулировки этого плана не являются текстом главы. План задаёт работу и критерии, но не даёт готовые фразы для переноса в основной текст.

## 4. Входные файлы только для чтения

Управляющие документы:

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md
work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md
work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
```

Фрагменты:

```text
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/B3_source_usage.md
work/theory-writing/fragments/B3_story_anchor_map.md
work/theory-writing/fragments/B3_figure_candidates.md
work/theory-writing/fragments/B3_open_questions.md
work/theory-writing/fragments/B3_degradation_and_duplication_audit.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C2_source_usage.md
work/theory-writing/fragments/C2_story_anchor_map.md
work/theory-writing/fragments/C2_figure_candidates.md
work/theory-writing/fragments/C2_open_questions.md
work/theory-writing/fragments/C2_degradation_and_duplication_audit.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C4_source_usage.md
work/theory-writing/fragments/C4_story_anchor_map.md
work/theory-writing/fragments/C4_figure_candidates.md
work/theory-writing/fragments/C4_open_questions.md
work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

Статьи Атласа и связанные файлы:

```text
work/atlas/articles/gas_town.md
work/atlas/articles/gas_town_theory_links.md
work/atlas/articles/gas_town_source_usage.md
work/atlas/articles/gas_town_image_plan.md
work/atlas/articles/gas_town_external_image_queue.md
work/atlas/articles/gas_town_open_questions.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/persistent_work_graph_theory_links.md
work/atlas/articles/persistent_work_graph_source_usage.md
work/atlas/articles/persistent_work_graph_image_plan.md
work/atlas/articles/persistent_work_graph_external_image_queue.md
work/atlas/articles/persistent_work_graph_open_questions.md
```

Досье:

```text
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md
```

Начальные темы внешнего поиска:

```text
Gas Town Beads
GUPP Violation
multi-agent work coordination
agent service roles
```

Правила языка, стиля, источников и изображений:

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/terminology-and-translation.md
protocols/rules/conceptual-translation-glossary.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
```

Словарь смыслового перевода используется как справочник при выборе русских слов. План не дублирует словарь и не создаёт локальный список спорных терминов.

## 5. Содержательное направление

Глава должна начинаться не с описания терминов Gas Town, а со сцены распада общей картины. Есть несколько связанных задач; часть агентов работает в отдельных рабочих площадках; один удерживает claim, но застрял; другой сделал полезную находку, но не вернул её в общее состояние; третий нарушил рабочее правило; человеку нельзя показывать весь шум логов, но он должен увидеть, где нужна остановка или решение. Нужна не новая “личность” агента, а организация среды: очередь, видимость, сервисные роли, реакция на нарушение, возврат результата и сигнал человеку.

Beads стоит раскрывать как операционный носитель очереди и состояния работы. В VII PWG был общей теоретической формой: объект работы, зависимости, готовность, gates, claims, evidence, restoration. В X Beads ближе к рабочей дисциплине: что находится в очереди, кто взял работу, где блокировка, что готово, что нужно вернуть в состояние, какой следующий кусок можно брать.

Mayor нужно объяснять как поверхность видимости и вмешательства человека. В многоагентной среде человеку нельзя отдавать весь поток событий. Ему нужна поверхность, где видны очереди, зависшие работы, нарушения, результаты сервисных агентов, узкие места и решения, которые нельзя принимать автоматически.

GUPP и hooks стоит раскрывать как обратный сигнал на нарушение порядка. Если агент нарушает рабочее правило, система не должна просто записать это в лог. Она должна вернуть сигнал туда, где ход работы может измениться: остановить, перенаправить, поставить в очередь, потребовать исправления, обновить состояние или поднять вопрос человеку.

В конце глава должна связать X с IX и XI. IX ограничивает отдельное действие в среде исполнения. X организует поток многих действий и рабочих площадок. XI должна спросить, какие материалы проверки позволяют принять результат, потому что даже хорошо организованный поток ещё не является доказательством качества.

## 6. Как вести работу над главой

Начать нужно с фрагментов B3, C2 и C4, статей Атласа по Gas Town и PWG, досье и историй Jökull Sólberg, Stripe Minions, Shopify Roast и Mae Capozzi. При чтении собирать не словарь проекта, а функции: очередь, claim, рабочая площадка, сервисная роль, сигнал человеку, нарушение процесса, возврат результата, ограничение шума, организация множества workers.

Внешний поиск должен сначала поднять первоисточники Gas Town / Beads и связанные документы по GUPP Violation, service roles и multi-agent coordination. Если внешние источники дают мало нового, это нужно зафиксировать и опираться на Атлас, досье и локальные assets, а не растягивать главу пустым поиском.

Перед черновиком собрать сквозную сцену. Она должна заставить организационный слой работать: несколько рабочих площадок, зависший claim, сервисный агент, нарушение правила, возврат результата в Beads/PWG и сигнал человеку. Через эту сцену объяснять элементы Gas Town по функции, а не по названию.

Первый черновик писать как главу об организации многоагентной рабочей среды. Gas Town / Beads — главный источник фактуры, но не единственный смысл главы. Если текст начинает выглядеть как обзор компонентов Gas Town, нужно вернуть его к вопросу: что происходит, когда рабочих потоков много и проект должен удержать их в управляемой форме.

После черновика провести активный добор без потолка объёма. Если тонкими остались Beads как очередь и состояние, Mayor как видимость и вмешательство, GUPP/hooks как обратный сигнал, service agents как обслуживание среды, отличие от subagents, связь с IX и мост к XI, нужно заново открыть источники, Атлас, досье и истории. Не останавливаться на привычной длине текста, если глава требует больше фактуры.

Визуальный слой здесь особенно полезен. Проверить локальные assets Gas Town/Beads, схемы Mayor, workflow, pressure-to-mechanism stack, worker roles, service agents vs subagents и поток “нарушение → сигнал → исправление → возврат в состояние”. Сильные схемы вставлять рядом с местом, которое они объясняют, а не в конец как приложение.

После каждого добора переписывать текст естественным русским языком. Городские имена источника сохранять, но объяснение не должно звучать как внутренняя мифология проекта. Писать: рабочая среда, очередь, исполнитель, сервисная роль, нарушение порядка, возврат результата, сигнал человеку.

## 7. Готовность

Глава готова, если она не является экскурсией по Gas Town. После чтения должно быть ясно, почему многоагентная работа требует организации потока: очередей, рабочих площадок, сервисных ролей, обратных сигналов, видимости для человека и возвращения результатов в общее состояние. Beads и Gas Town должны работать как источник фактуры для этой мысли, а не как самостоятельный каталог компонентов.

Сопутствующие файлы должны показать, какие источники реально использованы, какие visual assets вставлены или отложены, какие истории поддерживают главу и какие границы с VII–IX и XI сохранены. Финальная проверка должна искать городскую метафорику, которая вытесняет смысл, повторы из Атласа, протокольный язык и искусственные формулы.
