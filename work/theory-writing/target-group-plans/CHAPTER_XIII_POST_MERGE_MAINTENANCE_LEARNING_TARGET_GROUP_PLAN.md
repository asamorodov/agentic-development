# План целевой группы — Глава XIII: после слияния — сопровождение, обновление и обучение среды

Статус: рабочий план для пакета главы.  
Режим: профиль `D2`; тип пакета — `composition_heavy / discovery_heavy`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, актуальный blueprint для планов глав и материалы конкретной главы.

## 1. Назначение главы

Глава должна показать, что слияние кода не обязательно завершает жизненный цикл изменения. Если спецификации, ADR, правила, skills, hooks, рабочие графы и политики остаются старыми, следующий агент начинает из ложного состояния проекта.

Это глава про обновление среды после результата: prompt-update/sync, замена ADR, обновление constitution, очистка PWG, корректировка процесса, ретроспектива и сопровождение.

Она готовит заключение: выбор минимальной структуры зависит от того, что должно остаться живым после изменения.

Главная рабочая формула главы:

```text
Собрать ситуацию: изменение прошло, но следующий агент получает устаревший AGENTS.md, старую спецификацию, прошлый ADR и грязный рабочий граф; сопровождение должно обновить среду, а не только закрыть PR.
```

## 2. Риски и границы

- свести главу к техническому долгу в обычном смысле
- сделать общий список “не забудьте обновить документы”
- пересказать все методы ещё раз
- не показать, что сама среда агента учится или устаревает

Отдельное ограничение: план не должен становиться мини-главой. Он задаёт направление, материалы, риски и критерии, но не подсовывает исполнителю готовые объяснения, сцены, переходы и формулировки будущего текста.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/XIII_post_merge_maintenance_learning.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_source_register.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_fragment_usage.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_atlas_usage.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_dossier_gap_notes.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_external_discovery_log.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_story_anchors.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_figure_candidates.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_open_questions.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_degradation_and_duplication_audit.md
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/XIII_post_merge_maintenance_learning_passes/
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
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/A9_source_usage.md
work/theory-writing/fragments/A9_story_anchor_map.md
work/theory-writing/fragments/A9_figure_candidates.md
work/theory-writing/fragments/A9_open_questions.md
work/theory-writing/fragments/A9_degradation_and_duplication_audit.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C1_source_usage.md
work/theory-writing/fragments/C1_story_anchor_map.md
work/theory-writing/fragments/C1_figure_candidates.md
work/theory-writing/fragments/C1_open_questions.md
work/theory-writing/fragments/C1_degradation_and_duplication_audit.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C2_source_usage.md
work/theory-writing/fragments/C2_story_anchor_map.md
work/theory-writing/fragments/C2_figure_candidates.md
work/theory-writing/fragments/C2_open_questions.md
work/theory-writing/fragments/C2_degradation_and_duplication_audit.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C3_source_usage.md
work/theory-writing/fragments/C3_story_anchor_map.md
work/theory-writing/fragments/C3_figure_candidates.md
work/theory-writing/fragments/C3_open_questions.md
work/theory-writing/fragments/C3_degradation_and_duplication_audit.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C4_source_usage.md
work/theory-writing/fragments/C4_story_anchor_map.md
work/theory-writing/fragments/C4_figure_candidates.md
work/theory-writing/fragments/C4_open_questions.md
work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

Статьи Атласа и связанные файлы:

```text
work/atlas/articles/spdd_method.md
work/atlas/articles/spdd_method_theory_links.md
work/atlas/articles/spdd_method_source_usage.md
work/atlas/articles/spdd_method_image_plan.md
work/atlas/articles/spdd_method_external_image_queue.md
work/atlas/articles/spdd_method_open_questions.md
work/atlas/articles/adr_method.md
work/atlas/articles/adr_method_theory_links.md
work/atlas/articles/adr_method_source_usage.md
work/atlas/articles/adr_method_image_plan.md
work/atlas/articles/adr_method_external_image_queue.md
work/atlas/articles/adr_method_open_questions.md
work/atlas/articles/constitutional_sdd.md
work/atlas/articles/constitutional_sdd_theory_links.md
work/atlas/articles/constitutional_sdd_source_usage.md
work/atlas/articles/constitutional_sdd_image_plan.md
work/atlas/articles/constitutional_sdd_external_image_queue.md
work/atlas/articles/constitutional_sdd_open_questions.md
work/atlas/articles/spec_kit_method.md
work/atlas/articles/spec_kit_method_theory_links.md
work/atlas/articles/spec_kit_method_source_usage.md
work/atlas/articles/spec_kit_method_image_plan.md
work/atlas/articles/spec_kit_method_external_image_queue.md
work/atlas/articles/spec_kit_method_open_questions.md
work/atlas/articles/kiro_specs.md
work/atlas/articles/kiro_specs_theory_links.md
work/atlas/articles/kiro_specs_source_usage.md
work/atlas/articles/kiro_specs_image_plan.md
work/atlas/articles/kiro_specs_external_image_queue.md
work/atlas/articles/kiro_specs_open_questions.md
work/atlas/articles/gsd_open_gsd.md
work/atlas/articles/gsd_open_gsd_theory_links.md
work/atlas/articles/gsd_open_gsd_source_usage.md
work/atlas/articles/gsd_open_gsd_image_plan.md
work/atlas/articles/gsd_open_gsd_external_image_queue.md
work/atlas/articles/gsd_open_gsd_open_questions.md
work/atlas/articles/bmad_method.md
work/atlas/articles/bmad_method_theory_links.md
work/atlas/articles/bmad_method_source_usage.md
work/atlas/articles/bmad_method_image_plan.md
work/atlas/articles/bmad_method_external_image_queue.md
work/atlas/articles/bmad_method_open_questions.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/persistent_work_graph_theory_links.md
work/atlas/articles/persistent_work_graph_source_usage.md
work/atlas/articles/persistent_work_graph_image_plan.md
work/atlas/articles/persistent_work_graph_external_image_queue.md
work/atlas/articles/persistent_work_graph_open_questions.md
```

Досье:

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
```

Начальные темы внешнего поиска:

```text
post-merge maintenance AI agents
incident-driven policy update
SBOM supply chain maintenance
dependency policy update
agent memory maintenance
retrospective workflow update
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

- начать с разрыва: код слит, но окружающие артефакты не обновлены
- показать несколько типов последующего обновления: спецификация, ADR, constitution, process state, PWG, skills/rules/hooks
- разобрать, как инцидент или изменение требований возвращает работу в цикл
- закрыть мостом к заключению о выборе режима

Профиль внешнего поиска для этой главы: `D2`. Поиск нужен только для названных лакун и не должен превращаться в обзор темы.

Не ограничивать будущую главу условным размером. Если материал требует большего объёма, глава должна получить этот объём. Если материал раскрыт, не раздувать текст ради симметрии.

## 6. Очередь проходов

Эта очередь сделана под конкретную главу, а не механически скопирована из blueprint. Её можно сжать при сборке пакета только если сохраняются: добор материала, русская перепись после содержательных изменений, решение по изображению после устойчивого текста и финальная проверка потерь.

### P01 — рамка главы и границы с соседними главами

Восстановить задачу главы по скелетону, матрице входов и соседним главам. Зафиксировать, что глава получает от предыдущего слоя и что должна передать дальше. Не писать мини-главу и не расписывать будущие абзацы.

Особое внимание: Не использовать “долг” как универсальное слово. Если речь о technical debt, можно назвать технический долг; в остальных случаях писать конкретно: устаревшее правило, отложенная задача, не обновлённая спецификация, открытый вопрос.

Пиши создаваемый текст естественным русским языком.

### P02 — рабочая модель главного предмета

Собрать рабочую модель предмета главы. Это должна быть не теория в миниатюре, а короткая опора для письма: какая ситуация открывает главу, какой переход она объясняет и где возникает основной риск.

Рабочая модель: Собрать ситуацию: изменение прошло, но следующий агент получает устаревший AGENTS.md, старую спецификацию, прошлый ADR и грязный рабочий граф; сопровождение должно обновить среду, а не только закрыть PR.

Пиши создаваемый текст естественным русским языком.

### P03 — выбор внутренних материалов

Прочитать выбранные фрагменты, истории, статьи Атласа и досье. Для каждого материала определить функцию в главе: какое различение, сцену, техническую опору, границу или факт он даёт. Не пересказывать материалы по очереди и не строить одинаковые карточки по всем методам.

Пиши создаваемый текст естественным русским языком.

### P04 — содержательные лакуны

Проверить, чего не хватает внутренним материалам, чтобы глава была самостоятельной. Лакуна — это не любое интересное продолжение, а место, без которого глава остаётся тонкой, слишком быстрой или неубедительной.

Фокус проверки: Внешний поиск нужен, если глава выходит к incident learning, supply chain, SBOM, dependency policy или платформенной памяти. Не расширять до общего DevOps-обзора.

Пиши создаваемый текст естественным русским языком.

### P05 — внешний поиск по подтверждённым лакунам

Искать внешние источники только по лакунам, найденным в предыдущем проходе. Источник должен давать новое различение, точный факт, рабочий пример, тип сбоя, визуальный материал или более ясное объяснение перехода главы. Не собирать общий обзор темы.

Пиши создаваемый текст естественным русским языком.

### P06 — чтение источников и решение по каждому

Прочитать найденные источники и принять решение по каждому: встроить в основной текст, оставить в реестре, записать как материал для другой главы или отклонить. Если источник открывает большую соседнюю тему, не расширять текущую главу незаметно.

Пиши создаваемый текст естественным русским языком.

### P07 — порядок объяснения главы

Собрать порядок объяснения в пяти-семи пунктах. Не писать будущие абзацы. Не переносить формулировки этого шага в основной текст. Порядок должен вести от понятной ситуации к главному различению главы и дальше к мосту в следующую главу.

Пиши создаваемый текст естественным русским языком.

### P08 — первый связный черновик

Написать первый черновик главы по выбранной логике. Не включать всё подряд: все истории, все фрагменты и все источники. Главный критерий — после чтения понятно, зачем эта глава нужна в общей теории.

Не ограничивать размер заранее. Если для самостоятельной главы нужны дополнительные объяснения, примеры, переходы и различения, добавить их уже в первом черновике. Не сокращать материал только потому, что глава получается длиннее соседних.

Пиши создаваемый текст естественным русским языком.

### P09 — первая русская перепись

Сразу после черновика переписать главу как естественный русский текст. Не редактировать косметически, а свободно пересобрать фразы и абзацы. Черновик — материал, а не набор формулировок, которые нужно сохранить.

Сохранить смысл, источники, факты, важные различения и общий ход аргумента. Словарь смыслового перевода учитывать как справочник, но не писать языком словаря.

Переписывай текст естественным русским языком.

### P10 — интеграция фрагментов

Вернуться к выбранным фрагментам и проверить, не потеряны ли сильные различения. Переносить не абзацы целиком, а смысл в форме главы. Если фрагменты требуют расширить главу, расширить её. Не сжимать перенос ради условного размера.

Пиши создаваемый текст естественным русским языком.

### P11 — русская перепись после интеграции фрагментов

Переписать затронутые места так, чтобы добавленный материал не выглядел вставкой из рабочего фрагмента. Если интеграция изменила ход аргумента, переписать весь раздел. Не удалять содержательно нужные детали ради гладкости.

Переписывай текст естественным русским языком.

### P12 — интеграция историй, Атласа и досье

Встроить опорные эпизоды и технические материалы по функции, а не по списку источников. Истории не должны стоять одинаковыми карточками. Статьи Атласа и досье не должны превращаться в отдельные обзоры. Если сильный эпизод или техническая опора требуют больше места, дать им место.

Пиши создаваемый текст естественным русским языком.

### P13 — русская перепись после интеграции внутренних материалов

Переписать места, куда вошли истории, Атлас или досье. Убрать карточный ритм, одинаковые вводные формулы и служебные переходы. Опорный эпизод должен входить в ход мысли главы, а не висеть примером после тезиса.

Переписывай текст естественным русским языком.

### P14 — интеграция внешних источников

Встроить только те внешние источники, которые реально закрывают лакуны или усиливают различения главы. Если внешний источник нужен, переносить достаточно материала для понятного различения, а не одну формальную ссылку. Ссылку ставить в месте использования.

Пиши создаваемый текст естественным русским языком.

### P15 — русская перепись после внешних источников

Переписать места, куда вошли внешние источники, чтобы они не выглядели поздними вставками. Сохранить ссылки и факты, но убрать обзорный ритм и служебные формулы.

Переписывай текст естественным русским языком.

### P16 — ссылки сразу при вводе источника

Проверить, что новые утверждения, факты, цитируемые различения и визуальные материалы получили ссылку в месте использования. Эта проверка не является редакторским проходом: она только находит пропуски опоры. Если нужно переписать абзац, сделать это как локальную русскую перепись.

Пиши создаваемый текст естественным русским языком.

### P17 — добор слабых мест без потолка объёма

Найти места, где глава остаётся тонкой: важный переход пройден слишком быстро, пример не раскрыт, источник использован слишком формально, связь с общей теорией не видна. Усиливать эти места прямо в тексте. Размер добавлений заранее не ограничивать.

Пиши создаваемый текст естественным русским языком.

### P18 — русская перепись после добора

После добора переписать затронутые разделы так, чтобы глава снова читалась как цельный текст. Не удалять содержательно нужный материал ради гладкости. Всю главу переписывать только если поздние добавления изменили общий ход аргумента.

Переписывай текст естественным русским языком.

### P19 — убрать обзорность и выбрать сильные сцены или технические опоры

Проверить, не превратилась ли глава в каталог методов, инструментов, историй или документов. Если каталог появился, не просто сокращать список: выбрать те сцены, различения или технические опоры, которые действительно держат аргумент, и встроить их в ход главы. Остальное вынести в сопутствующие файлы или оставить краткой ссылкой.

Пиши создаваемый текст естественным русским языком.

### P20 — решение по изображению и ремонт ссылок на визуальные материалы

Решение по изображению принимать только после устойчивого текста. Если полезный кандидат помогает главе и его можно использовать, баланс смещён в сторону фиксации или вставки сейчас: потом восстановить его из нескольких уровней документов трудно.

Визуальная политика этой главы: изображения про repair/update использовать только если они помогают показать продолжение жизненного цикла после merge

Если изображение вставляется, основной текст должен объяснить, зачем оно здесь. Если кандидат пока не готов, оставить конкретную запись для последующей работы: источник, что взять, где поставить и зачем это главе.

Пиши создаваемый текст естественным русским языком.

### P21 — начало, структура и границы главы

Проверить начало главы, заголовки, порядок разделов и границы с соседними главами. Чинить только структурные сбои: не запускать общий стилевой проход и не переписывать весь текст без необходимости.

Пиши создаваемый текст естественным русским языком.

### P22 — убрать последние неестественные места

Найти места, где текст всё ещё звучит как план, отчёт, перевод с английского или внутренняя инструкция. Переписать только эти места. Не добавлять новый материал и не менять структуру без причины.

Переписывай текст естественным русским языком.

### P23 — проверка потерь, сопутствующие файлы и готовность

Сначала проверить основной текст против входных материалов: не потеряны ли важные тезисы, источники, различения, изображения и открытые вопросы. Затем внести только необходимые локальные исправления. После этого синхронизировать сопутствующие файлы: реестр источников, использование фрагментов, Атласа, историй, внешнего поиска, изображений, открытых вопросов, проверку деградации и отчёт о готовности.

Сопутствующие файлы могут быть короткими, если материала мало, но не должны быть пустой имитацией отчёта.

Пиши создаваемый текст естественным русским языком.

## 7. Критерии готовности плана

Перед сборкой исполнительного пакета план должен пройти отдельную русскую перепись. Эта перепись не меняет очередь проходов и не добавляет требований; она убирает протокольный ритм, искусственные рабочие термины, повторы и фразы, похожие на готовые абзацы будущей главы.

Пакет можно собирать, если:

- профиль внешнего поиска выбран явно;
- целевые файлы названы конкретно;
- входные документы перечислены путями;
- в плане сохранён добор материала без искусственного потолка объёма;
- после каждого существенного содержательного изменения предусмотрена русская перепись затронутого текста;
- решение по изображению принимается после устойчивого текста и фиксирует полезного кандидата, если он найден;
- план не является мини-главой и не специфицирует будущий текст чрезмерно подробно.
