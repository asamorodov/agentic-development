# A10 source usage

Статус: companion-файл к `A10_mode_selection_map.md` после второго стилевого прохода S02 и финальной упаковочной проверки. Он фиксирует, какие разрешённые входы использованы, где они вошли в основной текст и как проверялась граница: A10 должна быть картой выбора режима, а не новой теорией поверх A/B/C-узлов.

Во втором проходе внешние источники не открывались. В edge/source-pass добавлены пять внешних источников только под один edge case: policy-bound contributions. Остальная фактура A10 по-прежнему опирается на разрешённые внутренние материалы: скелетон, план несущих узлов, `Cross_story_synthesis.md`, карту источников и уже созданные companion-файлы A10. Ссылки на рабочие досье, планы и отчёты не добавлялись в основной текст как публичные цели цитирования.

## Использованные входы

| Вход | Роль в A10 | Где использован | Citation / provenance решение |
|---|---|---|---|
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | Композиционный контракт: финальная рамка `conversation → research / plan → specification → decision memory → persistent work graph → methodology / framework → controlled environment → evidence → completion → lifecycle repair`; вопросы об отказе, завершении и последующем ремонте. | Общая структура A10, таблица `fig-a10-mode-selection-map`, абзац об отказе как выходе из любой строки, финальная практическая диагностика. | Не цитируется в публичном тексте как источник факта: это рабочий скелетон и композиционное основание. |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | Target-функция A10 и карта функций A1–A9, B1–B3, C1–C5. Второй проход использовал именно этот файл для проверки, что A10 не придумывает новую теорию, а сжимает уже заданные различения. | Новый вводный абзац о том, что карта не добавляет отдельный метод; усиленные границы spec/PWG/runtime/process/evidence; таблица проверки ниже. | Не цитируется в публичном тексте: рабочий план. Внутренние названия A/B/C не превращены в публичные ссылки. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Рабочие границы companion-файлов и visual gate: A10 как синтетическая зона, а не обзор; inline-figure только как полезная synthetic figure; реестр candidates отдельно. | Решение оставить одну inline synthetic figure и не добавлять A/B/C-support diagram в основной текст. | Не цитируется в публичном тексте: рабочая карта документов. |
| `content/Cross_story_synthesis.md` | Главный фактический корпус для story anchors: лёгкий разговорный режим, plan-first, исследование кодом, браузерная проверка, PR-сопровождение, песочница, навыки/хуки, внешняя память, командная нагрузка. | Все фактические story anchors в основном тексте и `A10_story_anchor_map.md`. | Ссылки ставятся в основном тексте на публичные story anchors, а не на рабочие досье. |
| `work/theory-source-map-ai-driven-sdlc.md` | Фоновая проверка, что возможные внешние источники существуют для будущего source-rich pass, но не обязательны для текущей композиционной карты. В edge/source-pass из этой зоны использован только policy-bound edge case. | Источниковое решение и ограничение внешнего pass; пять внешних источников перечислены отдельно ниже. | Большинство внешних URL из карты источников не открывались; исключение — Zig policy / McQuaid maintainer text / Linux Foundation / EFF / OpenInfra policies для конкретного edge case. |
| `protocols/rules/russian-language.md`, `language-style-rules.md`, `human-technical-style.md`, `english-source-handling.md` | Языковой и стилевой контракт: русский технический текст, английские термины только где это рабочие имена, без summary-тона и декоративной гладкости. | Весь основной текст и companion-файлы; во втором проходе часть `runtime / process profile / evidence package` переведена на русский слой. | Правила исполнения, не цели цитирования. |
| `protocols/rules/source-and-provenance.md`, `content-preservation.md` | Provenance discipline: не ссылаться на планы/досье как первоисточник, не сглаживать story-фактуру, не добавлять неподтверждённые детали. | Решение не открывать новые внешние источники без конкретного утверждения; отдельное указание на долг полного A/B/C cross-check. | В публичный текст не добавлены факты без источниковой опоры или явного синтетического вывода из разрешённых материалов. |
| `protocols/rules/fragment-defect-analysis-and-repair.md`, `visual-assets-and-figures.md` | Repair-pass и visual gate: не превращать A10 в оглавление, не добавлять декоративные схемы, фиксировать readiness и долги. | `A10_open_questions.md`; обновление `A10_figure_candidates.md`; отказ от отдельной A/B/C provenance figure в основном тексте. | Правила исполнения, не цели цитирования. |


## Внешние источники, добавленные в edge/source-pass

| Источник | Почему добавлен | Какое утверждение поддерживает | Где использован |
|---|---|---|---|
| Zig Code of Conduct, `Strict No LLM / No AI Policy` — https://ziglang.org/code-of-conduct/ | Рабочий лист запросил edge case `policy-bound contributions`, а разрешённые внутренние материалы указывали на Zig no-AI policy как короткий governance-якорь. | Явная политика проекта может запретить LLM-generated content и тем самым изменить режим: агент может помогать локально только в пределах, не нарушающих правила участия, а отправка вклада определяется policy boundary. | Новый абзац “Пять граничных случаев...” в `A10_mode_selection_map.md`; `A10_story_anchor_map.md`; `A10_open_questions.md`. |
| Mike McQuaid, Open Source Initiative maintainer profile — https://opensource.org/maintainers/mikemcquaid | `Cross_story_synthesis.md` ссылался на внешний текст McQuaid об ответственности перед мейнтейнерами; для публичного утверждения был открыт первоисточник. | Участник может пользоваться AI-инструментами, но должен сам внимательно проверить результат и не перекладывать ревью AI-generated output на мейнтейнеров; это поддерживает слой completion/authority. | Новый абзац “Пять граничных случаев...” в `A10_mode_selection_map.md`; `A10_story_anchor_map.md`; `A10_open_questions.md`. |
| Linux Foundation guidance regarding use of generative AI tools — https://www.linuxfoundation.org/legal/generative-ai | Свободный source/depth pass проверил, не слишком ли A10 сужает policy-bound contribution до запрета или maintainer etiquette. | Условно-разрешающая политика может позволять AI-generated content, но связывать вклад с проверкой прав, лицензий, IP policies и проектными правилами. | Уточнение в edge-case абзаце `A10_mode_selection_map.md`; source/open questions. |
| EFF policy on LLM-assisted contributions — https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects | Нужен промежуточный policy-case между полным запретом и мягкой рекомендацией McQuaid. | Политика может разрешать LLM-assisted contributions, но требовать, чтобы участники понимали отправляемый код; comments/docs должны быть authored by a human. | Уточнение в edge-case абзаце `A10_mode_selection_map.md`; source/open questions. |
| OpenInfra Foundation policy for AI-generated content — https://openinfra.org/legal/ai-policy/ | Нужен policy-case, где contribution boundary выражен как labels, human-in-the-loop и reviewer scrutiny. | Contributors remain responsible; AI output should be treated as untrusted, disclosure labels such as `Generated-By` / `Assisted-By` help reviewers understand origin and context. | Уточнение в edge-case абзаце `A10_mode_selection_map.md`; source/open questions. |

## P06 criteria-strengthening note

Адресный проход по критериям выбора режима не добавил новых источников и не изменил provenance. Правка была композиционной: после основной таблицы в `A10_mode_selection_map.md` добавлен ряд рабочих признаков, которые связывают каждый режим с сигналом недостаточности более лёгкой формы. Это использует уже перечисленные внутренние опоры и policy-bound источники; новых ссылок или внешних visual assets не появилось.

## P07 transition-strengthening note

Адресный проход по переходам между режимами не добавил новых источников и не изменил source ledger. Правка уточнила композиционную логику A10: следующий слой структуры появляется, когда цена опоздавшей структуры выше цены её ведения; преждевременное усложнение отклоняется, если проверка близка, откат дешёв и новый артефакт не будет поддерживаться.

## P08 practical-applicability note

Адресный проход по практической применимости не добавил новых источников. Правка опирается на уже зафиксированную функцию A10 в скелетоне и target-group plan: карта должна помогать выбрать рабочий режим. В основном тексте добавлено правило выбора самого лёгкого достаточного режима и три признака пересмотра режима вверх или вниз.

## P09 general editor pass note

Общий редакторский проход P09 не добавил новых внешних источников и не изменил source ledger. Исправления были структурно-композиционными: плотный критерий выбора и edge-case paragraph разделены, ссылка на Simon Willison в evidence-разделе сделана явной, а visual layer оставлен без изменений.

## P10 general editor pass note

Повторный общий редакторский проход P10 не добавил источников и не изменил provenance. Точечная правка заменила две разговорные формулы в основном тексте на более точные технические выражения; source usage, policy links and figure decisions остались прежними.

## P11 general editor pass note

Третий общий редакторский проход не добавил источников и не изменил provenance. Проверка подтвердила, что A10 не требует нового source-pass: внешняя опора ограничена пятью policy-bound источниками, а остальная карта остаётся синтезом разрешённых внутренних планов, скелетона, story synthesis и companion-аудитов.

## Фактическая сверка с A/B/C-узлами после импорта

Статус: обновлено во время второго post-import repair. Первичный executor-result оставил устаревший долг: он утверждал, что фактические A/B/C-фрагменты не были разрешёнными входами. При интеграции результата и повторной оценке A10 эти фрагменты были открыты из текущего репозитория и сверены с основным текстом A10, матрицей выбора и stress-tests.

| Узел / группа | Что A10 берёт | Проверка после фактического чтения |
|---|---|---|
| A1 | Единица выбора — программное изменение, а не промпт. | A10 удерживает изменение как единицу анализа и не строит отдельную prompt-типологию. |
| A2–A3 | Различение спецификации, проверочного ожидания, ADR и specification-methodologies. | A10 оставляет только критерии выбора: когда намерение, проверка или память решения должны стать внешними артефактами. |
| A4 / B2 / C1 / C4 | PWG как долговечное состояние работы, отличное от документа, трекера и следа запуска. | A10 не называет PWG универсальным уровнем зрелости; он нужен только при готовности, владельцах, контрольных условиях, свидетельствах, передаче и восстановлении. |
| A5 / C2 / B3 | Process profiles и Gas Town как ответ на повторяемый сбой и организационную среду. | A10 не превращает процесс в обязательную ступень; процесс добавляется только когда локальная коррекция уже повторяется. |
| A6 / C4 | Среда исполнения как контроль ущерба и прав, а не память работы. | A10 удерживает границу: runtime-поверхность показывает, что было выполнено, но не решает, почему продолжение разрешено и кто принимает риск. |
| A7 / C3 | Наблюдение против свидетельства. | A10 требует связывать свидетельство с обещанием изменения; простой лог, скриншот или summary не считаются достаточным завершением. |
| A8 | Право действовать против права признать изменение принятым. | A10 связывает завершение с владельцем риска и не передаёт принятие агенту. |
| A9 | Последующий ремонт устаревших артефактов. | A10 удерживает repair как часть выбора режима: после принятого изменения могут устареть specifications, ADR, rules, skills, hooks, tests, context files и work graph. |
| B1 | SPDD как вклад в specification lifecycle, но не вся модель SDLC. | A10 использует SPDD как глубокий случай спецификационного слоя и не делает его универсальной рамкой. |
| B3 | Gas Town как организационная среда сверх одного графа работы. | A10 не растворяет Gas Town в PWG и не делает организационную среду обязательной для каждой задачи. |
| C1–C4 | Мосты specification → PWG, PWG → process, PWG → evidence, runtime → PWG. | A10 использует мосты как условия перехода между формами, а не как новые обязательные сущности. |

Вывод сверки: основной текст A10 потребовал только локальных уточнений языка и чтения карты. Его функция сохраняется: карта выбирает минимально достаточную форму внешней структуры для конкретного изменения, а не повторяет весь корпус A/B/C.

## Неиспользованные потенциальные источники

- Свободный source/depth pass проверил текущие inline-ссылки, source ledger, figure candidates и ближайший внешний source map, но не стал превращать A10 в обзор источников.
- Внешние источники из `work/theory-source-map-ai-driven-sdlc.md` в целом не открывались. Исключение — пять источников для edge case `policy-bound contributions`: Zig Code of Conduct, текст McQuaid на сайте Open Source Initiative, Linux Foundation guidance, EFF policy и OpenInfra policy. Если поздний chapter pass захочет усилить финальное заключение внешней рамкой про AI-driven SDLC, review effort, governance или agentic security, нужен отдельный source-pass с открытием первоисточников.
- Рабочие досье как отдельный корпус не открывались: для A10 достаточно фактических A/B/C-фрагментов, B/C companion-файлов, source usage и уже перенесённых story anchors. Фактические тексты A1–A9, B1–B3 и C1–C4 открыты при post-import sync; этот долг закрыт.
- Визуальные кандидаты из source map и figure registry не использованы как доказательства: локальный поиск в архиве не нашёл image assets для A10, а внешние screenshots/диаграммы требуют отдельного rights/download/localization pass.

## Readiness note

`ready_with_known_debts`: `A10_mode_selection_map.md` пригоден как поздний синтетический узел. После post-import sync и второго repair закрыты механические долги результата: отсутствующие target outputs созданы, фактические A/B/C-фрагменты прочитаны, основная figure очищена от лестничной формулировки `слой`, а companion-файлы больше не представляют A/B/C-сверку как незакрытый blocker. Оставшиеся долги обычные для публикационной сборки: проверить публичные anchors, решить, нужны ли дополнительные внешние источники для policy-bound edge case, и согласовать A10 с будущим C5/atlas-routing.


## Post-import sync with actual A/B/C fragments

Статус: выполнено при интеграции результата A10 в рабочую файловую систему. Первичный executor-result оставил долг: фактические A/B/C-фрагменты якобы не были разрешёнными входами. В post-import pass они открыты из текущего репозитория, и основной текст A10 проверен против их фактических формулировок.

Прочитанные upstream-фрагменты:

- `work/theory-writing/fragments/A1_change_not_prompt.md`
- `work/theory-writing/fragments/A2_specification_adr_contract.md`
- `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md`
- `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md`
- `work/theory-writing/fragments/A5_process_methodologies_synthesis.md`
- `work/theory-writing/fragments/A6_execution_environment_distinctions.md`
- `work/theory-writing/fragments/A7_observation_vs_evidence.md`
- `work/theory-writing/fragments/A8_authority_to_act_vs_complete.md`
- `work/theory-writing/fragments/A9_lifecycle_repair.md`
- `work/theory-writing/fragments/B1_spdd_contribution_and_limits.md`
- `work/theory-writing/fragments/B2_pwg_contribution.md`
- `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md`
- `work/theory-writing/fragments/C1_specification_to_pwg.md`
- `work/theory-writing/fragments/C2_pwg_to_process_profiles.md`
- `work/theory-writing/fragments/C3_pwg_to_evidence.md`
- `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`

Результат сверки: главный текст A10 не потребовал переписывания по фактическим A/B/C-фрагментам. Его центральные различения совпадают с текущей структурой: изменение шире промпта; specification/contract/ADR разведены; PWG описан как долговечное состояние работы; процесс добавляется после повторяемого сбоя; среда исполнения отвечает за радиус ущерба; свидетельство отделено от наблюдения; завершение связано с владельцем принятия; последующий ремонт закрывает устаревшие артефакты. В основной текст добавлена только одна уточняющая связка о комбинациях режимов, потому что план A10 требовал проверять не только отдельные режимы, но и их минимально достаточные сочетания.


## Second post-import repair note

Повторная пользовательская проверка A10 выявила не новый содержательный провал, а остаточные дефекты чтения карты и companion-state:

- заголовок первой колонки и подпись к figure использовали слово `слой`, хотя A10 специально защищается от maturity-ladder чтения;
- в основном тексте оставалось слабое выражение `полный субстрат работы`;
- `A10_source_usage.md` и `A10_open_questions.md` сохраняли устаревший долг о непрочитанных A/B/C-фрагментах после того, как post-import sync уже был выполнен;
- `A10_mode_selection_matrix.md` и `A10_decision_stress_tests.md` сохраняли несколько остаточных английских labels (`rollback path`, `evidence-state`).

Правки: `Слой` заменён на `Форма внешней структуры`, `субстрат работы` — на `состояние работы`, supporting outputs очищены от остаточных labels, а companion-файлы синхронизированы с фактическим post-import состоянием. Источниковая опора и список story anchors не менялись.
