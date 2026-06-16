# План целевой группы — Глава VII: Persistent Work Graph как граф продолжения работы

Статус: рабочий план для пакета главы.  
Режим внешнего поиска: `D1`; тип пакета — `normal_synthesis`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, обновлённый blueprint и материалы главы VII.

## 1. Зачем нужна эта глава

Глава VII должна сделать первый большой шаг за пределы агентской сессии. До неё уже показано, что сессия даёт след работы, спецификация и ADR удерживают намерение и решение, а глава VI описывает проектный интерфейс агента. Теперь нужно объяснить другое: длинная агентская работа не продолжается из одного сообщения, одного `done`, одного handoff или одного списка задач. После нескольких сессий появляются ветви работы, зависимости, заблокированные решения, разные владельцы, частично прикреплённые проверки, устаревающие источники и несколько возможных следующих ходов.

Главная ось главы — переход от линейной памяти к графу продолжения работы. Пока работа короткая, её можно передать одной запиской: что сделали, что проверили, что дальше. Но как только изменение переживает несколько сессий, CI-сигналы, ревью, дочерние исследования и человеческие решения, краткое резюме уже не удерживает состояние. Нужен слой, где видно, какой объект работы открыт, что от чего зависит, почему что-то заблокировано, какой `claim` действует, какой `gate` ещё не пройден, какие свидетельства к чему относятся и какой компактный ввод должен получить следующий агент.

PWG нужно раскрывать не как трекер задач и не как красивую метафору графа, а как рабочую форму продолжения агентского изменения. Обычный tracker чаще отвечает на вопрос, какие задачи есть и в каком они статусе. PWG отвечает на более жёсткий вопрос: что нужно знать, чтобы следующий человек или агент безопасно продолжил работу, не начав заново и не приняв локальное `done` за завершение изменения проекта.

План задаёт работу, а не готовый текст главы. Исполнитель не должен переносить формулировки плана в основной текст без переписывания. Все выходные материалы — сама глава, журналы поиска, реестры, отчёты и проходы — пишутся нормальным русским языком. Технические имена файлов, команд, моделей, методов и полей сохраняются точно там, где это нужно для источника.

У главы нет целевого объёма, нормальной длины и скрытого ориентира вроде 40 тысяч знаков. Текст должен стать таким длинным, каким требует исходный материал: плотность источников, число важных различений, количество нужных сцен, визуальный слой и объём фактуры из Атласа, досье, фрагментов, историй и внешних источников. Если после первого черновика остаются значимые недоразобранные источники или тонкие места, работу нужно продолжать, а не полировать прежний объём.


## 2. Границы главы

Глава не должна уходить в Gas Town раньше времени. Beads и Gas Town важны как источники фактуры, но предмет этой главы шире конкретного инструмента: устойчивое рабочее состояние, пригодное для продолжения. Gas Town как организация множества исполнителей должен в полной мере раскрыться в главе X.

Глава также не должна становиться главой про runtime. Среда исполнения, права, sandbox, worktree и подтверждение команд относятся к IX. Здесь важно другое: даже если среда ограничена, следующая сессия всё равно должна понять, где находится работа и что она может продолжать.

Наконец, глава не должна сводиться к доказательствам и проверкам. Свидетельства в PWG важны, но XI будет отдельно разбирать, что именно можно считать достаточным проверочным материалом. В VII нужно показать, как свидетельства прикрепляются к узлам работы и помогают продолжению, не превращая эту тему в полную теорию верификации.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/VII_persistent_work_graph_source_register.md
work/theory-writing/chapters/VII_persistent_work_graph_fragment_usage.md
work/theory-writing/chapters/VII_persistent_work_graph_atlas_usage.md
work/theory-writing/chapters/VII_persistent_work_graph_dossier_gap_notes.md
work/theory-writing/chapters/VII_persistent_work_graph_external_discovery_log.md
work/theory-writing/chapters/VII_persistent_work_graph_story_anchors.md
work/theory-writing/chapters/VII_persistent_work_graph_figure_candidates.md
work/theory-writing/chapters/VII_persistent_work_graph_open_questions.md
work/theory-writing/chapters/VII_persistent_work_graph_degradation_and_duplication_audit.md
work/theory-writing/chapters/VII_persistent_work_graph_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/VII_persistent_work_graph_passes/
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
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A4_source_usage.md
work/theory-writing/fragments/A4_story_anchor_map.md
work/theory-writing/fragments/A4_figure_candidates.md
work/theory-writing/fragments/A4_open_questions.md
work/theory-writing/fragments/A4_degradation_and_duplication_audit.md
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B2_source_usage.md
work/theory-writing/fragments/B2_story_anchor_map.md
work/theory-writing/fragments/B2_figure_candidates.md
work/theory-writing/fragments/B2_open_questions.md
work/theory-writing/fragments/B2_degradation_and_duplication_audit.md
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
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/persistent_work_graph_theory_links.md
work/atlas/articles/persistent_work_graph_source_usage.md
work/atlas/articles/persistent_work_graph_image_plan.md
work/atlas/articles/persistent_work_graph_external_image_queue.md
work/atlas/articles/persistent_work_graph_open_questions.md
work/atlas/articles/gas_town.md
work/atlas/articles/gas_town_theory_links.md
work/atlas/articles/gas_town_source_usage.md
work/atlas/articles/gas_town_image_plan.md
work/atlas/articles/gas_town_external_image_queue.md
work/atlas/articles/gas_town_open_questions.md
```

Досье:

```text
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md
```

Начальные темы внешнего поиска:

```text
Beads issue tracker
persistent work graph
durable work state
agent work queue state
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

Глава должна начинаться с практического сбоя: после нескольких агентских сессий у проекта есть переписка, диффы, проверки и отдельные заметки, но нет ясной рабочей картины. Что сейчас открыто? Что действительно готово? Что только выглядит готовым? Какой сигнал CI относится к новому контракту, а какой оказался старой нестабильной проверкой? Какое ревью открыло архитектурное ограничение? Что нашёл subagent, и почему его вывод ещё не стал принятым состоянием?

Сквозной пример нужен именно для этого. Пусть изменение почти реализовано, но зависит от спорного edge case; CI дал два разных сигнала; ревью указало на архитектурную границу; дочернее исследование принесло полезный вывод, но его ещё нужно встроить в общее состояние. Следующая сессия не должна читать весь прошлый шум. Она должна получить компактную картину: открытые узлы, блокировки, действующие claims, связанные свидетельства, нужные источники и следующий безопасный ход.

Узел PWG стоит объяснять как маленький контракт продолжения, а не как карточку задачи. Он говорит, что считается открытым объектом работы, какие условия делают его готовым, что держит его заблокированным, кто сейчас удерживает claim, какой gate ещё не пройден, какие свидетельства уже прикреплены и какой source state считается актуальным. Это не обязательно один файл и не обязательно один тип записи. Важно, что следующий исполнитель видит не просто статус, а условия дальнейшего действия.

Отдельно нужно провести через главу сбой локального `done`. Агент мог завершить сессию, задача могла выглядеть закрытой, один тест мог пройти, но связанное решение ещё не принято, проверочный материал не привязан к обещанию, flaky-сигнал не классифицирован, а следующая сессия не знает, что делать. PWG нужен, чтобы такие локальные признаки завершения не стирали незавершённые зависимости, gates, claims и человеческие решения.

Restoration packet должен стать проверкой всей идеи. Если граф работает, новая сессия получает не архив всего прошлого, а короткий, точный ввод: что сейчас открыто, что заблокировано, какие claims действуют, какие свидетельства уже есть, какие источники актуальны и где следующий безопасный ход. Если из графа нельзя собрать такой ввод, граф остаётся сложной записью, но не решает проблему продолжения.

Глава должна говорить и об очистке состояния. Хороший PWG не только сохраняет. Он закрывает узлы, снимает блокировки, заменяет устаревшие claims, отделяет историческое свидетельство от действующего и не отдаёт следующей сессии старый шум как актуальную картину. Это важный противовес желанию “запомнить всё”.

## 6. Как вести работу над главой

Начинать нужно не с черновика, а с восстановления материала. Открыть фрагменты A4, B2, C2, C3 и C4, статью Атласа о PWG, связку Beads/Gas Town, досье и истории Jökull Sólberg, Mark Erikson, HumanLayer и Mae Capozzi. При чтении сразу отмечать не “интересные места вообще”, а фактуру, которая помогает главе: claims, gates, блокировки, handoff, compact context, restoration, связь свидетельств с обещанием, очистка устаревшего состояния.

После этого нужно добрать внешние источники. Поиск не должен ограничиваться названиями `persistent work graph` или `Beads`: важно проверить близкие темы вроде durable work state, agent work queue state, claim-based task ownership, restoration context, graph state для coding agents. Если источник не даёт главе нового материала, его нужно честно отклонить в журнале, а не ссылаться на него ради количества.

Перед первым черновиком собрать сквозной пример и решить порядок объяснения. Хорошая структура главы идёт от сбоя линейной передачи к объекту работы, затем к зависимостям, готовности, claims/gates, свидетельствам и source state, после чего приходит к restoration packet и очистке состояния. В конце должен появиться естественный мост к VIII: граф показывает, где находится работа, но ещё не говорит, в каком режиме с ней действовать.

Первый черновик нужно писать свободно, но не отрывать от источников. Не включать всё подряд из Beads, Gas Town, историй и досье. Главный критерий: после чтения должно быть понятно, почему агентской разработке нужен граф продолжения работы, а не более длинное summary, не один handoff, не обычный tracker и не dashboard проверок.

После черновика обязательно пройтись по слабым местам без потолка объёма. Если тонкими остались переход от линии к графу, локальное `done`, узел как контракт продолжения, отличие PWG от tracker/summary/CI dashboard, связь evidence с конкретным обещанием, restoration после compaction или очистка устаревшего состояния, нужно заново открыть соответствующие источники и добрать фактуру. Этот проход завершается не потому, что глава стала “достаточно длинной”, а потому что значимые материалы действительно перенесены или признаны нерелевантными.

Визуальный слой проектируется после устойчивого текста. Минимально проверить кандидаты: структура узла PWG, граф зависимостей и блокировок, переход session trace → persistent work graph, Beads/PWG redraw, compact restoration packet. Если среда позволяет создавать локальные assets, сильные схемы нужно довести до файлов и вставить в текст. В prompts для генерации использовать нейтральный архитектурный язык, без тревожных или театральных формулировок.

После каждого крупного добора текст нужно переписывать по-русски, а не просто вклеивать новые абзацы. Проверить, не стал ли Beads главным предметом вместо PWG, не выглядит ли глава как набор полей модели данных, не появились ли самокомментарии вроде “этот раздел нужен, чтобы показать”. Слова `claim`, `gate`, `ready`, `blocked`, `prime`, `work item`, `persistent` объяснять по-русски, сохраняя точные имена только там, где они являются терминами источника.

## 7. Готовность

План считается выполненным, если глава удерживает свою собственную ось: переход от линейного handoff к графу продолжения работы. Должны быть ясно различены переписка, summary, tracker, CI-сигнал, ADR/spec и PWG. Сквозной пример должен работать по всей главе, а не появляться один раз. Внутренние и внешние источники должны быть перенесены с достаточной фактурой, ссылки должны стоять рядом с использованными утверждениями, сопутствующие файлы должны быть синхронизированы без пустой отчётности.

Финальная проверка должна искать не только потерянные источники, но и остатки рабочего языка: кальки, случайный английский клей, самокомментарии, внутренние названия проходов и искусственные термины из планов. Если проблема смысловая, исправлять нужно фрагмент, а не одно слово.
