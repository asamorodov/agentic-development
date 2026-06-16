# План целевой группы — Глава XII: завершение, ответственность и внешний контур

Статус: рабочий план для пакета главы.  
Режим: профиль `D3`; тип пакета — `discovery_heavy`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, актуальный blueprint для планов глав и материалы конкретной главы.

## 1. Назначение главы

Глава должна развести право действовать и право завершать. Агент может выполнять шаги, но принятие результата остаётся у человека, команды, мейнтейнера или политики управления.

Она должна собрать внешний контур: ADR status, CODEOWNERS, политики открытых проектов, корпоративные контрольные точки, ложное завершение и подмену проверочного материала.

Глава связывает XI с XIII: после принятия начинается сопровождение и обновление среды.

Главная рабочая формула главы:

```text
Собрать ситуацию: агент подготовил PR, проверки зелёные, но завершение зависит от владельца кода, политики проекта, статуса решения и внешнего контура доверия.
```

## 2. Риски и границы

- морализировать про ответственность вместо инженерного различения полномочий
- смешать проверочный материал с правом принять результат
- пересказать политики open-source проектов как новости
- забыть про ложное завершение: агент сделал действие, но работа не принята

Отдельное ограничение: план не должен становиться мини-главой. Он задаёт направление, материалы, риски и критерии, но не подсовывает исполнителю готовые объяснения, сцены, переходы и формулировки будущего текста.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/XII_authority_responsibility_outer_contour.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_source_register.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_fragment_usage.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_atlas_usage.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_dossier_gap_notes.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_external_discovery_log.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_story_anchors.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_figure_candidates.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_open_questions.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_degradation_and_duplication_audit.md
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/XII_authority_responsibility_outer_contour_passes/
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
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A8_source_usage.md
work/theory-writing/fragments/A8_story_anchor_map.md
work/theory-writing/fragments/A8_figure_candidates.md
work/theory-writing/fragments/A8_open_questions.md
work/theory-writing/fragments/A8_degradation_and_duplication_audit.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A2_source_usage.md
work/theory-writing/fragments/A2_story_anchor_map.md
work/theory-writing/fragments/A2_figure_candidates.md
work/theory-writing/fragments/A2_open_questions.md
work/theory-writing/fragments/A2_degradation_and_duplication_audit.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C3_source_usage.md
work/theory-writing/fragments/C3_story_anchor_map.md
work/theory-writing/fragments/C3_figure_candidates.md
work/theory-writing/fragments/C3_open_questions.md
work/theory-writing/fragments/C3_degradation_and_duplication_audit.md
```

Статьи Атласа и связанные файлы:

```text
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
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

Начальные темы внешнего поиска:

```text
CODEOWNERS
open source AI contribution policy
maintainer trust AI code
AI generated PR policy
software supply chain policy
human approval gates
sandbox security policy
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

- показать разницу между действовать, предлагать, завершать и принимать
- связать ADR status, CODEOWNERS, maintainer policy и human gates
- разобрать, как агент или платформа могут создать видимость завершения без настоящего принятия
- закрыть мостом к сопровождению после слияния

Профиль внешнего поиска для этой главы: `D3`. Поиск нужен только для названных лакун и не должен превращаться в обзор темы.

Не ограничивать будущую главу условным размером. Если материал требует большего объёма, глава должна получить этот объём. Если материал раскрыт, не раздувать текст ради симметрии.

## 6. Очередь проходов

Эта очередь сделана под конкретную главу, а не механически скопирована из blueprint. Её можно сжать при сборке пакета только если сохраняются: добор материала, русская перепись после содержательных изменений, решение по визуальному слою после устойчивого текста и финальная проверка потерь.

### P01 — рамка главы и границы с соседними главами

Восстановить задачу главы по скелетону, матрице входов и соседним главам. Зафиксировать, что глава получает от предыдущего слоя и что должна передать дальше. Не писать мини-главу и не расписывать будущие абзацы.

Особое внимание: Не писать юридико-этическую главу. Это инженерная глава о границе полномочий и завершения работы.

Пиши создаваемый текст естественным русским языком.

### P02 — рабочая модель главного предмета

Собрать рабочую модель предмета главы. Это должна быть не теория в миниатюре, а короткая опора для письма: какая ситуация открывает главу, какой переход она объясняет и где возникает основной риск.

Рабочая модель: Собрать ситуацию: агент подготовил PR, проверки зелёные, но завершение зависит от владельца кода, политики проекта, статуса решения и внешнего контура доверия.

Пиши создаваемый текст естественным русским языком.

### P03 — выбор внутренних материалов

Прочитать выбранные фрагменты, истории, статьи Атласа и досье. Для каждого материала определить функцию в главе: какое различение, сцену, техническую опору, границу или факт он даёт. Не пересказывать материалы по очереди и не строить одинаковые карточки по всем методам.

Пиши создаваемый текст естественным русским языком.

### P04 — содержательные лакуны

Проверить, чего не хватает внутренним материалам, чтобы глава была самостоятельной. Лакуна — это не любое интересное продолжение, а место, без которого глава остаётся тонкой, слишком быстрой или неубедительной.

Фокус проверки: Нужен двухшаговый поиск по политикам open-source проектов, CODEOWNERS, trust boundaries, AI-generated contributions и corporate approval gates.

Пиши создаваемый текст естественным русским языком.

### P05 — первый внешний поиск по подтверждённым лакунам

Провести первый внешний поиск по точным лакунам главы. Приоритет — первичные источники, документация, исследовательские статьи и тексты практиков. Не собирать общий обзор инструментов или методик.

Во время этого прохода отдельно смотреть на визуальные опоры источников: реальные скриншоты, diagrams, architecture/lifecycle схемы, UI-примеры, trace/dashboard fragments и таблицы. Не решать вставку автоматически; зафиксировать кандидат и предварительный тип: `source_real_image`, `external_real_image_candidate`, `source_backed_redraw`, `source_backed_synthetic_figure`, `synthetic_figure`, `defer` или `reject`.

Пиши создаваемый текст естественным русским языком.

### P06 — чтение первого круга источников

Прочитать источники первого круга и выписать только то, что реально меняет главу: новые термины, схемы, документы, типы сбоев, сравнительные рамки или визуальные кандидаты.

Пиши создаваемый текст естественным русским языком.

### P07 — второй внешний поиск только при необходимости

Запустить второй круг поиска только если первый круг вывел на важный документ, автора, термин, диаграмму или линию аргументации, без которых глава останется слабой. Не использовать второй круг как разрешение на общий обзор.

Пиши создаваемый текст естественным русским языком.

### P08 — решение по внешним источникам

Для каждого источника принять решение: встроить сейчас, оставить в реестре, записать как материал для другой главы или отклонить. Если источник встроен, ссылка ставится в месте использования.

Пиши создаваемый текст естественным русским языком.

### P09 — порядок объяснения главы

Собрать порядок объяснения в пяти-семи пунктах. Не писать будущие абзацы. Не переносить формулировки этого шага в основной текст. Порядок должен вести от понятной ситуации к главному различению главы и дальше к мосту в следующую главу.

Пиши создаваемый текст естественным русским языком.

### P10 — первый связный черновик

Написать первый черновик главы по выбранной логике. Не включать всё подряд: все истории, все фрагменты и все источники. Главный критерий — после чтения понятно, зачем эта глава нужна в общей теории.

Не ограничивать размер заранее. Если для самостоятельной главы нужны дополнительные объяснения, примеры, переходы и различения, добавить их уже в первом черновике. Не сокращать материал только потому, что глава получается длиннее соседних.

Пиши создаваемый текст естественным русским языком.

### P11 — первая русская перепись

Сразу после черновика переписать главу как естественный русский текст. Не редактировать косметически, а свободно пересобрать фразы и абзацы. Черновик — материал, а не набор формулировок, которые нужно сохранить.

Сохранить смысл, источники, факты, важные различения и общий ход аргумента. Словарь смыслового перевода учитывать как справочник, но не писать языком словаря.

Переписывай текст естественным русским языком.

### P12 — интеграция фрагментов

Вернуться к выбранным фрагментам и проверить, не потеряны ли сильные различения. Переносить не абзацы целиком, а смысл в форме главы. Если фрагменты требуют расширить главу, расширить её. Не сжимать перенос ради условного размера.

Пиши создаваемый текст естественным русским языком.

### P13 — русская перепись после интеграции фрагментов

Переписать затронутые места так, чтобы добавленный материал не выглядел вставкой из рабочего фрагмента. Если интеграция изменила ход аргумента, переписать весь раздел. Не удалять содержательно нужные детали ради гладкости.

Переписывай текст естественным русским языком.

### P14 — интеграция историй, Атласа и досье

Встроить опорные эпизоды и технические материалы по функции, а не по списку источников. Истории не должны стоять одинаковыми карточками. Статьи Атласа и досье не должны превращаться в отдельные обзоры. Если сильный эпизод или техническая опора требуют больше места, дать им место.

Пиши создаваемый текст естественным русским языком.

### P15 — русская перепись после интеграции внутренних материалов

Переписать места, куда вошли истории, Атлас или досье. Убрать карточный ритм, одинаковые вводные формулы и служебные переходы. Опорный эпизод должен входить в ход мысли главы, а не висеть примером после тезиса.

Переписывай текст естественным русским языком.

### P16 — интеграция внешних источников

Встроить только те внешние источники, которые реально закрывают лакуны или усиливают различения главы. Если внешний источник нужен, переносить достаточно материала для понятного различения, а не одну формальную ссылку. Ссылку ставить в месте использования.

Пиши создаваемый текст естественным русским языком.

### P17 — русская перепись после внешних источников

Переписать места, куда вошли внешние источники, чтобы они не выглядели поздними вставками. Сохранить ссылки и факты, но убрать обзорный ритм и служебные формулы.

Переписывай текст естественным русским языком.

### P18 — ссылки сразу при вводе источника

Проверить, что новые утверждения, факты, цитируемые различения и визуальные материалы получили ссылку в месте использования. Эта проверка не является редакторским проходом: она только находит пропуски опоры. Если нужно переписать абзац, сделать это как локальную русскую перепись.

Пиши создаваемый текст естественным русским языком.

### P19 — добор слабых мест без потолка объёма

Найти места, где глава остаётся тонкой: важный переход пройден слишком быстро, пример не раскрыт, источник использован слишком формально, связь с общей теорией не видна. Усиливать эти места прямо в тексте. Размер добавлений заранее не ограничивать.

Пиши создаваемый текст естественным русским языком.

### P20 — русская перепись после добора

После добора переписать затронутые разделы так, чтобы глава снова читалась как цельный текст. Не удалять содержательно нужный материал ради гладкости. Всю главу переписывать только если поздние добавления изменили общий ход аргумента.

Переписывай текст естественным русским языком.

### P21 — убрать обзорность и выбрать сильные сцены или технические опоры

Проверить, не превратилась ли глава в каталог методов, инструментов, историй или документов. Если каталог появился, не просто сокращать список: выбрать те сцены, различения или технические опоры, которые действительно держат аргумент, и встроить их в ход главы. Остальное вынести в сопутствующие файлы или оставить краткой ссылкой.

Пиши создаваемый текст естественным русским языком.

### P22 — визуальный слой главы и ремонт ссылок на визуальные материалы

Решение принимать только после устойчивого текста. Не спрашивать только, нужна ли одна фигура. Нужно прочитать главу как объяснительную структуру и решить, нужен ли ей визуальный слой: один реальный source image, несколько локальных схем, source-backed redraw, synthetic figure по аргументу главы или честный отказ от изображений.

Визуальная политика этой главы: визуальный слой нужен только если он помогает различить право действовать, право завершить, ответственность человека и внешний контур контроля. Возможные узлы: decision gate, escalation path, human acceptance boundary, policy/approval loop. Не превращать главу в набор security-комиксов или интерфейсных скриншотов.

Для каждого кандидата указать, что именно он объясняет, где должен стоять в тексте и какой тип имеет:

- `source_real_image` / `local_image_asset` — если важна фактура источника: UI, dashboard, trace, screenshot, реальная диаграмма, конкретный документ или интерфейс;
- `source_backed_redraw` — если источник даёт сильную структуру, но её нужно перевести, упростить, привести к единому стилю или объединить с близкими источниками;
- `source_backed_synthetic_figure` / `synthetic_figure` — если изображение объясняет собственный аргумент главы, а не воспроизводит один внешний источник;
- `defer` / `reject` — если кандидат декоративен, плохо читается, дублирует текст, уводит в соседнюю тему или требует отдельного asset-pass.

Не заменять реальные source images синтетическими схемами ради закрытия визуального пункта. Не вставлять source images автоматически только потому, что они найдены. Если изображение вставляется, оно должно стоять рядом с тем местом, которое объясняет, иметь локальный путь, стабильный `figure id`, нормальный `alt` и публичный caption без executor notes.

Если пакет умеет создавать SVG/PNG assets, утверждённые redraw/synthetic figures нужно довести до локальных файлов и вставить в главу. Если среда не умеет создавать изображения, расширить `<chapter_id>_figure_candidates.md` как visual brief: placement, source basis, caption, alt и prompt/diagram spec.

При генерации изображений формулировать prompts нейтральным архитектурным языком: `architecture diagram`, `lifecycle checkpoint`, `validation step`, `confirmation`, `review gate`, `controlled access`, `generic adapter`, `state update`. Слова вроде `dangerous action`, `exploit`, `attack`, `shell access`, `external actions`, `stop unsafe behavior` переформулировать как «действия, требующие проверки», «контрольная точка», «подтверждение», «ограничение радиуса действия», если это не искажает смысл. Для MCP, hooks, permissions и внешних сервисов использовать generic labels вместо брендов и логотипов, если конкретный UI не является предметом изображения.

Пиши создаваемый текст естественным русским языком.

### P23 — начало, структура и границы главы

Проверить начало главы, заголовки, порядок разделов и границы с соседними главами. Чинить только структурные сбои: не запускать общий стилевой проход и не переписывать весь текст без необходимости.

Пиши создаваемый текст естественным русским языком.

### P24 — убрать последние неестественные места

Найти места, где текст всё ещё звучит как план, отчёт, перевод с английского или внутренняя инструкция. Переписать только эти места. Не добавлять новый материал и не менять структуру без причины.

Переписывай текст естественным русским языком.

### P25 — проверка потерь, сопутствующие файлы и готовность

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
- решение по визуальному слою принимается после устойчивого текста; полезные кандидаты классифицируются как `source_real_image`, `local_image_asset`, `source_backed_redraw`, `source_backed_synthetic_figure`, `synthetic_figure`, `defer` или `reject`;
- план не является мини-главой и не специфицирует будущий текст чрезмерно подробно.
