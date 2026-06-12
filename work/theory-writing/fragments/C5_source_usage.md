# C5. Использование источников

Этот файл фиксирует, какие входы использованы в `C5_theory_to_technical_atlas.md` и `C5_concept_atlas_article_map.md`. Внутренние досье и планы использованы как рабочие входы для ориентации; публичные фактические утверждения должны в будущих статьях опираться на первичные источники, а не на внутренние досье как целевая публичная цитата.

## Внутренние входы

| Вход | Как использован | Ограничение |
| --- | --- | --- |
| `work/decisions/ADR-0011-concept-first-technical-atlas.md` | Задал принятое решение: атлас является концептуально-техническим слоем, а не складом деталей; C5 должен объяснить две траектории чтения и самостоятельную статью атласа. | Не цитируется как внешний источник фактов. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Задал C5 как поздний мост, обязательные элементы карты статей, опасные пары границ и сигналы по HumanLayer, Roast, Stripe Minions, Quix. | Использован как карта состояния корпуса; не заменяет исторические/источниковые досье. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | Подтвердил верхнюю границу: теория идёт по жизненным напряжениям, атлас является концептуально-техническим слоем, а методологические профили должны видеть границу теория / Handbook / Fieldbook. | Использован как композиционная рамка, не как внешний источник фактов. |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | Подтвердил C5 как поздний мост с картой статей, границами уровня реестра, смысловыми обратными связями и будущим переходом к Handbook / Fieldbook. | Использован для маршрутизации слоёв; не заменяет досье и первоисточники. |
| `work/dossiers/SPDD_METHOD_DOSSIER.md` | Дал рабочую карту SPDD / OpenSPDD, REASONS Canvas, команд OpenSPDD, ревью, синхронизации и визуальных кандидатов Fowler/OpenSPDD. | Фактические утверждения будущей статьи должны ссылаться на Fowler/Thoughtworks и OpenSPDD. |
| `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | Дал карту Spec Kit: `specify init`, интеграции, `.specify`, `spec.md`, `plan.md`, `tasks.md`, рабочих процессов, пресетов, расширений, оговорки по CLI/цепочке поставки. | Для публикации нужна свежая источниковая проверка по текущей версии CLI. |
| `work/dossiers/KIRO_SPECS_DOSSIER.md` | Дал карту Kiro Specs: `.kiro/specs`, requirements/design/tasks, Bugfix Specs, Quick Plan, Analyze Requirements, steering, hooks, Sync Files, Web/CLI/оговорки governance. | Продуктовая поверхность меняется; перед статьёй нужна свежая проверка источников и UI. |
| `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | Дал карту CSDD: Constitution, spec/plan/tasks, матрицу трассируемости, гейты соответствия, Marri arXiv, Mad Devs, DocGuard, Cisco Foundry. | Источники имеют разную доказательную силу; не смешивать arXiv, практическое руководство и community extension. |
| `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | Дал две линии TDAD: компиляция определения агента из behavioral specs и регрессионный код-тестовый граф для coding agents. | В карте обязательна граница: TDAD не один метод. |
| `work/dossiers/GSD_METHOD_DOSSIER.md` | Дал карту GSD / Open GSD: `gsd-core`, `gsd-pi`, `.planning/`, `.gsd/`, фазы, маршрутизация команд, контекст, контрольные точки, проверку, gsd-browser. | Перед статьёй нужны проверка свежести и версий. |
| `work/dossiers/BMAD_METHOD_DOSSIER.md` | Дал карту BMAD: `_bmad/`, `_bmad-output/`, PRD/architecture/story/sprint-status, Quick Flow, Correct Course, TEA, карту рабочего процесса. | Структура v6 меняется; перед статьёй нужна проверка версии. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Дал карту PWG / Beads: рабочий граф, Dolt, зависимости, `bd ready`, `bd prime`, `bd gate`, восстановление, диагностику и соседние источники о долговечном исполнении. | Beads — якорь, не определение PWG. |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Дал карту Gas Town: роли, пространства, хуки, слой данных/управления Beads, очереди, convoys, сервисных агентов, обратное давление и утверждения о локальных ассетах. | Локальные ассеты и свежесть Gas Town/Beads требуют отдельной проверки. |
| `work/dossiers/ADR_METHOD_DOSSIER.md` | Дал карту ADR / MADR / Nygard: статус, происхождение, замещение, confirmation, агентно-ориентированную проекцию, реконструированную ADR и исполнимые проверки. | Не превращать ADR в спецификацию или тест; исследовательские и практические источники разделять по доказательной силе. |
| `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md` | Дал материал для маршрутной развилки Roast: Boba/Shopify как история, Ruby DSL и cogs как возможную концептуальную поверхность, README/релизы/PR/скриншоты как слой источниковой заметки. | Не использовать историческое досье как доказательство текущего API без свежей проверки первичных источников. |
| `protocols/rules/*.md` | Задали русский язык, перенос англоязычных источников, происхождение материала, сохранение фактуры и запрет подмены реальных изображений текстовыми суррогатами. | Применены как рабочие правила; не цитируются в публичном тексте. |

## Первичная источниковая база, указанная в карте статей

| Кандидат | Первичная источниковая база для будущей статьи | Статус в этом C5-проходе |
| --- | --- | --- |
| SPDD / OpenSPDD | Fowler/Thoughtworks SPDD; README и шаблоны OpenSPDD/design philosophy. | Уже использовано в основном тексте; источникная база готова для реестра. |
| Spec Kit | Spec Kit documentation, Quick Start, Installation, Core Commands, Integrations, Workflows, Presets, Extensions, `spec-driven.md`, Spec Kit Agents. | Добавлено в карту по разрешённому досье; не раскрывается подробно в основном C5. |
| Kiro Specs | Kiro Specs/Feature Specs docs; Requirements-First/Design-First; Analyze Requirements; Vibe vs Spec; Steering/Hooks/Autopilot/Subagents/Web/Governance notes. | Добавлено в карту по разрешённому досье; нуждается в свежей проверке UI и источников. |
| TDAD | `Test-Driven AI Agent Definition`; `tdad-paper-code`; SpecSuite-Core; `Test-Driven Agentic Development`; `pepealonso95/TDAD`; `tdad-skill`; TDFlow как соседний источник. | Добавлено как сравнительная методическая статья; две линии разведены. |
| Constitutional SDD | Marri arXiv/ar5iv/PDF; banking reference repo/PAPER.md; Mad Devs practical guide; Spec Kit `spec-driven.md`; DocGuard; Cisco Foundry; Project CodeGuard. | Добавлено как методическая статья с оговорками. |
| ADR / MADR / Nygard | Nygard; Fowler ADR; MADR; агентские ADR-практики; AI/ADR research; исполняемые проверки и источники policy-as-code. | Уже есть базовая поддержка в основном тексте; карта уточняет будущую статью. |
| GSD / Open GSD | Open GSD site; `gsd-core`; `gsd-pi`; roadmap; architecture; user guide; configuration; commands; gsd-browser notes. | Добавлено как процессная методическая статья; проверка свежести релизов отложена. |
| BMAD | BMAD README/docs; Workflow Map; Getting Started; Installation; Quick Fixes; Project Context; Sprint Status; TEA Enterprise docs. | Добавлено как процессная методическая статья; проверка версии отложена. |
| PWG / Beads | Beads docs, architecture, dependencies, multi-agent coordination, `bd prime`, `bd gate`, recovery/troubleshooting; lighter neighboring graph/durable sources from dossier. | Уже базовый слот базового концепта; граница с Gas Town усилена. |
| Gas Town | Gas Town README; Beads docs; Gas Town/Beads заметки досье о ролях, hooks, convoys, polecats, обратном давлении и утверждениях о локальных ассетах. | Слот базового концепта/кейса; долги по ассетам и свежести сохранены. |
| Sandvault | В этом рабочем листе нет разрешённого досье или источника; только слабый будущий сравнительный сигнал в SPDD-досье. | `отложено / недостаточно материала`. |
| HumanLayer harness | Только `WORKING_DOCUMENTS_MAP.md`: harness, research-plan-implement, context budget, BAML. | Кандидат уровня инструмента/формы; недостаточно материала для статьи. |
| Roast | `SHOPIFY_ROAST_STORY_DOSSIER.md`; Shopify Engineering Roast; `Shopify/roast` README/tutorial snippets; релизы; PR-линия события блоков; draft architecture docs. | Получил маршрутную развилку: концептуальная статья возможна только при свежей проверке API/кода/скриншотов; историческая заметка держит Boba/Shopify и YAML → Ruby DSL; источниковая заметка держит README, релизы, настройку провайдера, события блоков и версионные расхождения. |


## Новые внешние источники, раскрытые в источниковой проверке

| Источник | Что проверено рядом с текущим текстом | Решение для C5 |
| --- | --- | --- |
| [Fowler/Thoughtworks SPDD](https://martinfowler.com/articles/structured-prompt-driven/) | SPDD формулирует prompts as first-class delivery artifacts: versioned, reviewed, reused and improved, with requirements, domain language, design intent, constraints and task breakdown. | Подтверждает уже выбранный базовый слот SPDD; не расширять основной C5 дополнительными деталями REASONS Canvas. |
| [Spec Kit README](https://github.com/github/spec-kit) и [Quick Start](https://github.github.com/spec-kit/quickstart.html) | Официальная поверхность сочетает `specify init`, `.specify/memory/constitution.md`, путь команд со slash-префиксом `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` и гейты качества `/speckit.clarify`, `/speckit.checklist`, `/speckit.analyze`. | Усилить карту Spec Kit: текущие команды — слой источниковой заметки, чувствительный к свежести, а не теория. |
| [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) и [Kiro Web Specs](https://kiro.dev/docs/web/specs/) | IDE и Web поверхности обе ведут requirements/design/tasks, но Web-документация добавляет браузерное ревью, загрузку `.md`-артефактов и кнопки выполнения задач. | Усилить границу Spec Kit/Kiro: Kiro — продуктовая поверхность и UI/session режим, не переносимая универсальная цепочка инструментов. |
| [GSD Core](https://github.com/open-gsd/gsd-core), [GSD Pi](https://github.com/open-gsd/gsd-pi), [старый gsd-2 move note](https://github.com/gsd-build/gsd-2) | `gsd-core` описывает фазовую петлю context-engineering/spec-driven; `gsd-pi` описывает local-first CLI, worktree-aware automation и память проекта `.gsd/`; старый `gsd-2` указывает на перенос активного развития в Open GSD. | Карта должна держать GSD как семейство поверхностей с оговоркой по свежести и возможным разделением core/pi. |
| [BMAD Workflow Map](https://docs.bmad-method.org/reference/workflow-map/), [Workflow Diagram](https://docs.bmad-method.org/workflow-map-diagram.html), [Project Context](https://docs.bmad-method.org/explanation/project-context/), [issue #811](https://github.com/bmad-code-org/BMAD-METHOD/issues/811) | Workflow Map подтверждает каскад контекста PRD → architecture → story-файлы; diagram даёт визуальный кандидат; project-context.md служит руководством реализации; issue #811 показывает риск дрейфа документации/версий. | Усилить BMAD как процесс, оформленный артефактами; версии/команды оставить в источниковой заметке. |
| [TDAD arXiv HTML](https://arxiv.org/html/2603.17973v2) | Источниковая проверка подтвердила границу: сама статья различает Test-Driven Agentic Development для кодовых изменений от Rehan’s Test-Driven AI Agent Definition; TDAD конвейер строит код-тестовый граф и экспортирует `test_map.txt`. | Усилить требование не смешивать две линии TDAD; численные утверждения и фигуры только с прямой ссылкой в будущей статье. |
| [Constitutional SDD arXiv HTML](https://arxiv.org/html/2602.02584v1) | Constitution описан как версионируемый машиночитаемый документ с CWE/MITRE ограничениями, трассируемостью и эмпирическими утверждениями. | Усилить CSDD как методическую статью с оговоркой по свидетельствам; не переносить числа в основной C5. |
| [Beads README](https://github.com/gastownhall/beads) и [Gas Town README](https://github.com/gastownhall/gastown) | Beads README подтверждает распределённый графовый трекер issue-записей, Dolt, `bd ready`, `bd prime`, `bd remember` и настройку агента; Gas Town README даёт реальные Mermaid/sequence-кандидаты и операционную модель Mayor/Town/Rig/Crew/Polecats/Hooks/Convoys. | Усилить PWG/Gas Town границу и классифицировать диаграммы Gas Town как `external_real_image_candidate`. |
| [Nygard ADR](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), [Fowler ADR](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html), [MADR](https://adr.github.io/madr/) | Nygard подтверждает последовательную нумерацию, статус/контекст/решение/последствия и замещение; MADR подтверждает поля шаблона, включая Confirmation. | Подтверждает уже существующую ADR границу; новые факты не нужны в основной теории, кроме готовности источников. |
| [Shopify Engineering Roast](https://shopify.engineering/introducing-roast), [Roast README](https://github.com/Shopify/roast), [Roast tutorial](https://github.com/Shopify/roast/blob/main/tutorial/README.md), [Roast releases](https://github.com/Shopify/roast/releases) | История 2025 описывает YAML/Markdown ограничители рабочего процесса; текущие публичные README/tutorial/релизы описывают Ruby DSL, `execute`, cogs, возобновление сессии и переписывание 1.0 вокруг Ruby DSL. | Уточнить маршрут Roast: историческая заметка для Shopify/Boba/эволюции, источниковая заметка для API/README/релизов, концептуальная статья только после свежей проверки API и прохода по ассетам. |

## Проверка происхождения материала после пятого прохода

- Основной C5-фрагмент не превращён в список всех будущих статей; туда добавлены только выводы о типологии, границах, антидеградационных правилах и маршрутизации материала между теоретическим фрагментом, статьёй концептуального атласа, источниковой заметкой, исторической заметкой, Handbook и Fieldbook.
- `C5_concept_atlas_article_map.md` расширен до реестра с полями `Уровень статьи`, `Вопрос читателя`, `Источниковая база`, `Граница статьи`, `Допустимый повтор`, `Вероятные технические/визуальные поверхности`, готовностью ассетов/источников, семантическими обратными связями, маршрутными примерами и антидеградационными правилами.
- Sandvault и HumanLayer harness не получили фактического раскрытия без разрешённой источниковой базы; Roast получил только маршрутную развилку, а не полноценную статью.
- Опасные пары границ явно проверены в карте: SPDD/OpenSPDD/Spec Kit/Kiro; PWG/Beads/Gas Town; GSD/BMAD/профили процесса; TDAD/свидетельства/тестирование; ADR/ремонт жизненного цикла/спецификация; Roast как концепция/история/источник.
- Визуальные источники не вставлены в основной текст; кандидаты перенесены в `C5_figure_candidates.md`.
- Создан `C5_degradation_and_duplication_audit.md`: отдельная проверка пяти рисков деградации и дублирования с указанными правками.

## Проверка происхождения материала после источниковой проверки

- Новый проход открыл первичные источники только там, где они проверяют уже выбранные границы: SPDD/OpenSPDD, Spec Kit, Kiro, GSD, BMAD, TDAD, Constitutional SDD, PWG/Beads, Gas Town, ADR и Roast.
- Основной C5 получил не каталог новых фактов, а два редакторских вывода: разделять устойчивый механизм и быстро меняющуюся поверхность; не переносить утверждения уровня статьи, скриншоты, заметки о релизах и API-срезы в теорию.
- `C5_concept_atlas_article_map.md` синхронизирован с источниковой проверкой: Spec Kit/Kiro/GSD/BMAD/Roast получили более явные оговорки по свежести и источниковой заметке; TDAD и CSDD получили более строгие оговорки по свидетельствам.
- `C5_figure_candidates.md` приведён ближе к правилу классификации ассетов: реальные диаграммы и скриншоты README/docs остаются `external_real_image_candidate`, а синтетические схемы сохраняются только как будущие кандидаты для объяснения.

## Архитектурное выравнивание e6c4665a

| Вход | Что проверено | Решение |
| --- | --- | --- |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | Теория идёт по жизненным напряжениям и рабочим субстратам; атлас даёт статьи, читаемые от конкретной концепции, но не заменяет поперечный синтез. | В основном C5 добавлен переход после A/B/C-фрагментов; детали источниковой проверки сокращены, чтобы C5 не стал мини-атласом. |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | C5 описан как поздний мост после A/B/C и C1–C4; A10 — отдельная карта выбора минимально достаточного режима. | C5 явно отделён от A10: он не выбирает режим работы и не строит матрицу решений. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | C5 мог быть выполнен до A10; после появления A10 статус синхронизирован. | `C5_open_questions.md` и audit получили явный `A10 synced`, как закрытый post-import sync, а не как блокер. |
| `work/decisions/ADR-0011-concept-first-technical-atlas.md` | Атлас трактуется как концептуально-технический слой самостоятельных статей, а не узкое приложение команд и скриншотов. | `C5_concept_atlas_article_map.md` усилен как карта уровня реестра роли статей, а не список тем или черновик атласа. |



## Общий редакторский проход 1: происхождение материала и границы

| Проверка | Итог |
| --- | --- |
| Новые внешние источники | Не добавлялись. Проход оценивал уже собранный C5 против плана целевой группы, скелетона, плана CORE_NODES, ADR-0011 и карты документов. |
| Публичные фактические утверждения | Ссылки в основном C5 оставлены у утверждений, где используются первичные источники; внутренние планы не превращены в публичные ссылки. |
| Композиционная правка | Основной C5 оставлен мостом, а не мини-атласом: усилены язык, двусторонняя навигация и границы, без добавления новых фактических утверждений. |
| Терминологическая правка | В публичном тексте сокращён лишний английский связующий слой: `controlled repetition`, `source dossier`, `concept article`, `task tracker`, `package names`, `paper-level claims` заменены русскими формулировками или оставлены только как точные рабочие метки там, где это рабочий термин. |
| Ассеты / происхождение материала | Фигуры в основном тексте не добавлялись. Все реальные визуальные кандидаты остаются в `C5_figure_candidates.md` до прохода по ассетам. |

## Общий редакторский проход 2: происхождение материала и минимальная коррекция

| Проверка | Итог |
| --- | --- |
| Новые внешние источники | Не добавлялись. Проход перечитал уже исправленный C5 как мостовой фрагмент и проверял композицию против плана целевой группы, скелетона, плана CORE_NODES, рабочей карты и ADR-0011. |
| Публичные фактические утверждения | Ссылки на первичные источники не менялись и не расширялись. Правка не добавляла новых источникно-специфичных утверждений. |
| Мета-текст в основном фрагменте | Служебная формула `source-depth pass` снята из публичного заголовка: раздел теперь называется источниковой проверкой, а не названием внутреннего рабочего прохода. |
| Переходы и границы | Добавлен короткий публичный переход к проверке тяжёлых случаев: стресс-проверка не пишет статьи атласа, а проверяет границу между теорией, статьёй, источниковой фактурой и будущей практикой. |
| Ассеты / происхождение материала | Фигуры в основном тексте снова не добавлялись. Решение по визуальному слою остаётся прежним: кандидаты живут в `C5_figure_candidates.md` до отдельного прохода по ассетам или явной проверки полезности. |

## Общий редакторский проход 3: готовность и очистка мета-текста

| Проверка | Итог |
| --- | --- |
| Новые внешние источники | Не добавлялись. Проход был общей редакторской проверкой после двух ремонтов, а не источниковой проверкой. |
| Источникно-специфичные детали | Ссылки, команды, имена инструментов и источниковая фактура в основном C5 сохранены. |
| Мета-текст | Из публичного раздела о реестре удалена ссылка на `C5_concept_atlas_article_map.md` как на «рабочий файл». Основной текст теперь говорит о функции реестра, а не о сопровождающем файле. |
| Готовность | Существенных новых источниковых пробелов и пробелов происхождения материала для самого мостового фрагмента не найдено. Готовность остаётся `ready_with_known_debts / A10 synced`. |

## Финальная проверка упаковки

Финальная упаковка не добавляла новых внешних источников. Основной C5 сохраняет первичные ссылки; `C5_source_usage.md` остаётся файлом происхождения материала и источниковой дисциплины, а не публичной статьёй. Изображения не вставлялись; реальные визуальные кандидаты остаются в `C5_figure_candidates.md` до отдельного прохода по ассетам. Готовность: `ready_with_known_debts / A10 synced`.

## Post-import source sync with A10

| Источник | Что использовано | Как применено |
| --- | --- | --- |
| `work/theory-writing/fragments/A10_mode_selection_map.md` | A10 выбирает минимально достаточную внешнюю структуру для конкретного изменения и не является атласным реестром. | В основной C5 добавлено уточнение: A10 помогает переходу от понимания концепции к выбору режима, но C5 не дублирует матрицу решений. |
| `work/theory-writing/fragments/A10_mode_selection_matrix.md` | Рабочая матрица признаков выбора режима. | Использована как проверка границы: article map не должен превращаться в таблицу выбора режима. |
| `work/theory-writing/fragments/A10_decision_stress_tests.md` | Сценарии проверки практической применимости карты выбора режима. | Подтверждает, что Handbook/Fieldbook-переходы и выбор режима остаются задачей A10/практических материалов, а не C5. |
