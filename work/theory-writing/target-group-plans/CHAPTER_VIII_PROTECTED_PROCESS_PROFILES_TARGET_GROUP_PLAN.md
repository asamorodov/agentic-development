# План целевой группы — Глава VIII: защищённые способы продолжения работы

Статус: рабочий план для пакета главы.  
Режим внешнего поиска: `D2`; тип пакета — `composition_heavy`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, обновлённый blueprint и материалы главы VIII.

## 1. Зачем нужна эта глава

Глава VIII должна сделать следующий шаг после PWG. Глава VII показывает, где находится работа: какие узлы открыты, что заблокировано, какие свидетельства прикреплены и откуда продолжать. Но состояние само по себе не выбирает способ действия. Один и тот же узел можно продолжать как исследование, реализацию, ревью, исправление курса, brownfield-навигацию или передачу владельцу. Если агент входит в работу не тем способом, аккуратно записанное состояние снова перестаёт помогать.

Поэтому глава не должна быть обзором GSD и BMAD. Эти методологии нужны как сильные конкретные случаи, через которые видно, как процесс защищает следующий ход: задаёт фазу, роль, входной артефакт, точку остановки, форму выхода и возврат результата в рабочее состояние после сбоя. Gas Town остаётся не третьей равной карточкой, а границей: там, где отдельных способов продолжения уже мало, начинается организация постоянной многоагентной среды.

Главная формула главы простая: PWG показывает, где находится работа; защищённый способ продолжения показывает, как в неё входить, какую роль брать, где останавливаться и как возвращать результат обратно в состояние.

План задаёт работу, а не готовый текст главы. Исполнитель не должен переносить формулировки плана в основной текст без переписывания. Все выходные материалы — сама глава, журналы поиска, реестры, отчёты и проходы — пишутся нормальным русским языком. Технические имена файлов, команд, моделей, методов и полей сохраняются точно там, где это нужно для источника.

У главы нет целевого объёма, нормальной длины и скрытого ориентира вроде 40 тысяч знаков. Текст должен стать таким длинным, каким требует исходный материал: плотность источников, число важных различений, количество нужных сцен, визуальный слой и объём фактуры из Атласа, досье, фрагментов, историй и внешних источников. Если после первого черновика остаются значимые недоразобранные источники или тонкие места, работу нужно продолжать, а не полировать прежний объём.


## 2. Границы главы

Главный риск — написать методологический обзор: GSD делает одно, BMAD другое, Gas Town третье. Такой текст может быть информативным, но он не даст главе собственного хода. Здесь нужно раскрыть другой сбой: работа уже имеет состояние, но следующий агент выбирает неправильный режим. Он реализует там, где нужно исследовать; планирует там, где нужно уточнить story; чинит там, где требуется вернуться к владельцу решения; ведёт себя как greenfield-исполнитель в brownfield-коде.

Глава также не должна смешаться с V и VII. В V речь шла о способах защитить спецификацию и поведение изменения. В VII — о графе состояния работы. VIII занимает промежуточный слой: состояние уже есть, но для продолжения нужен подход, который задаёт фазу, ответственность, артефакт, контрольную точку и возврат результата.

С другой стороны, VIII ещё не должна становиться Gas Town. Если появляются постоянные crew, Mayor, hooks, сервисные роли и организация множества workers, это уже глава X.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/VIII_protected_process_profiles_source_register.md
work/theory-writing/chapters/VIII_protected_process_profiles_fragment_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_atlas_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_dossier_gap_notes.md
work/theory-writing/chapters/VIII_protected_process_profiles_external_discovery_log.md
work/theory-writing/chapters/VIII_protected_process_profiles_story_anchors.md
work/theory-writing/chapters/VIII_protected_process_profiles_figure_candidates.md
work/theory-writing/chapters/VIII_protected_process_profiles_open_questions.md
work/theory-writing/chapters/VIII_protected_process_profiles_degradation_and_duplication_audit.md
work/theory-writing/chapters/VIII_protected_process_profiles_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/VIII_protected_process_profiles_passes/
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
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
work/theory-writing/fragments/A5_source_usage.md
work/theory-writing/fragments/A5_story_anchor_map.md
work/theory-writing/fragments/A5_figure_candidates.md
work/theory-writing/fragments/A5_open_questions.md
work/theory-writing/fragments/A5_degradation_and_duplication_audit.md
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
```

Статьи Атласа и связанные файлы:

```text
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
work/atlas/articles/gas_town.md
work/atlas/articles/gas_town_theory_links.md
work/atlas/articles/gas_town_source_usage.md
work/atlas/articles/gas_town_image_plan.md
work/atlas/articles/gas_town_external_image_queue.md
work/atlas/articles/gas_town_open_questions.md
```

Досье:

```text
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
```

Начальные темы внешнего поиска:

```text
Open GSD docs
BMAD method docs
agent process approaches
role-based agent workflows
correct-course process
brownfield agent workflow
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

Сквозной пример лучше строить как продолжение VII. Есть PWG-узел: изменение billing/API уже имеет открытые зависимости, CI-сигналы, ревью и блокировки. Но следующая сессия не знает, как входить в работу. Можно продолжать реализацию, вернуться к уточнению требований, провести brownfield-анализ, исправить курс после проваленного ревью или передать story владельцу. Глава должна показать, что выбор способа продолжения — это отдельное инженерное решение, а не побочная деталь.

GSD и BMAD раскрывать асимметрично. GSD нужен как пример фазовой дисциплины: как работа удерживает направление, как возвращается после расползания, как сессия не превращается в бесконечное движение по инерции. BMAD нужен как пример ролево-артефактного подхода: кто действует, какой документ ведёт работу, как story становится рабочей единицей, где нужен correct course и как результат возвращается в состояние. Не делать из них равные карточки. Важно показать, какой сбой каждый подход помогает удержать.

Роль в этой главе не должна звучать как persona. Роль — это не характер агента и не театральная маска. Это допустимый набор действий, входной артефакт, ответственность, точка остановки и формат выхода. Если агент “исследователь”, это значит, что он читает, картирует и возвращает вывод, а не правит файлы. Если он “исполнитель”, он работает по принятому артефакту и возвращает результат в состояние. Если он “корректировщик курса”, он ищет расхождение между текущей траекторией и реальностью, а не продолжает прежний план.

Особенно важно раскрыть момент исправления курса. Способ продолжения нужен не только до начала работы, но и после сбоя: ревью отклонило часть решения, story оказалась неполной, brownfield-код противоречит ожиданиям, агент выбрал неверную фазу. Хороший процессный подход не просто ведёт вперёд; он возвращает работу на правильную траекторию.

В конце нужно провести двойной мост. К IX: способ продолжения говорит, что агент сейчас должен делать, но не ограничивает файловую систему, команды, сеть, secrets, approvals и sandbox. К X: когда таких потоков становится много и появляются постоянные исполнители, сервисные роли и рабочие площадки, отдельного подхода к продолжению уже мало.

## 6. Как вести работу над главой

Начать нужно с внимательного чтения фрагментов A5, B3 и C2, статей Атласа по GSD, BMAD и Gas Town, досье и историй Jesse Vincent, HumanLayer, Mae Capozzi, Shopify Roast и Matt Pocock. При чтении собирать не обзор методологий, а фактуру о фазах, ролях, story, course correction, brownfield-навигации, handoff, критериях остановки и возврате результата в состояние.

Внешний поиск должен идти по официальным материалам GSD и BMAD, а также по близким текущим практикам: role-based agent workflows, brownfield agent workflow, correct-course process, story-driven AI workflows. Цель поиска — не собрать рынок подходов, а понять, как в реальной практике задают фазу работы, входной артефакт, роль, границу действия и возврат результата.

Перед черновиком нужно выбрать порядок объяснения: сначала показать, почему одного состояния недостаточно; затем вывести ошибку неправильного режима продолжения; потом раскрыть GSD и BMAD как разные ответы на этот сбой; дальше показать, где подходы становятся избыточными или недостаточными; в конце подготовить переход к IX и X.

Первый черновик писать как главу о выборе способа продолжения, а не как обзор GSD/BMAD. Если текст начинает перечислять методы, нужно вернуть его к вопросу: какой следующий ход становится безопасным, а какой нет.

После черновика провести активный добор слабых мест без потолка объёма. Если тонкими остались GSD, BMAD, story, course correction, brownfield-навигация, роль как ответственность, граница с Gas Town или мост к IX, нужно заново открыть фрагменты, Атлас, досье, источники и истории. Добор завершается не потому, что объём стал привычным, а потому что значимая фактура действительно вошла в главу или осознанно отклонена.

Визуальный слой проектируется после устойчивого текста. Проверить кандидаты: состояние работы → способ продолжения; GSD как фазовая дисциплина; BMAD как story/role/artifact flow; ошибка входа в неправильный режим работы; переход к runtime и к Gas Town. Сильные схемы доводить до локальных assets, если среда это позволяет.

После каждого добора делать русскую перепись. Убирать язык планов, искусственные слова, самоописание текста и чрезмерно абстрактную терминологию там, где естественнее “способ”, “подход”, “режим работы” или “методология”. Английское `profile` сохранять только там, где оно действительно является техническим именем файла, источника или принятой внутренней категории.

## 7. Готовность

Глава готова, если она не читается как обзор методологий. После чтения должно быть ясно: состояние работы не выбирает следующий ход само; для продолжения нужен способ работы, который задаёт фазу, роль, артефакт, остановку и возврат результата. GSD, BMAD и Gas Town должны быть подчинены этому ходу, а не соревноваться за место в каталоге методов.

Сопутствующие файлы должны фиксировать, какие источники использованы, какие фрагменты и истории реально вошли в текст, какие визуальные решения приняты и где остаются открытые вопросы. Финальная проверка ищет не только пропущенную фактуру, но и остатки протокольного языка, искусственные термины и самокомментарии.
