# C5. Кандидаты фигур

Этот файл применяет визуальную проверку до любого вставления в основной текст. Ни один кандидат ниже не вставлен в основной текст C5. Готовые изображения не заменяются текстовыми суррогатами; внешние кандидаты требуют проверки прав, скачивания, локализации и качества.

## Реестр кандидатов C5 и будущих статей

| ID | Статус | Источник / основа | Что показывает | Решение |
| --- | --- | --- | --- | --- |
| `fig-c5-after-abc-to-concept-route` | `synthetic_figure` | Архитектурный переход C5 после A/B/C | A/B/C дают маршрут от теории; C5 открывает маршрут от концепции; A10 остаётся отдельной картой выбора режима; после post-import validation граница синхронизирована. | Кандидат только если будущий читатель теряет композиционную границу; сейчас не вставлять в основной текст. |
| `fig-c5-two-reading-trajectories` | `synthetic_figure` | Аргумент C5 + ADR-0011 | Чтение от теории и чтение от концепции как два входа в один SDLC-материал. | Кандидат для C5, не вставлять без решения о визуальной плотности. |
| `fig-c5-concept-article-model` | `synthetic_figure` | Раздел `Модель самостоятельной статьи атласа` | Читательский вопрос → проблема → механизм → рабочие поверхности → источникные оговорки → границы → смысловые обратные связи. | Сильный кандидат для введения атласа. |
| `fig-c5-article-tier-map` | `synthetic_figure` | `C5_concept_atlas_article_map.md` | Пять уровней: базовая концепция, метод, инструментальная форма, заметка об источнике/кейсе, отложено. | Кандидат, если таблица реестра станет слишком тяжёлой. |
| `fig-c5-routing-boundary` | `synthetic_figure` | Раздел C5 о маршрутизации материала + CORE_NODES plan | Практическая проверка: теоретический фрагмент → статья концептуального атласа → источниковая/историческая заметка → Handbook/Fieldbook в зависимости от функции материала. | Кандидат только если будущий читатель теряет границу между слоями; не вставлять ради декоративной карты. |
| `fig-c5-reverse-semantic-navigation` | `synthetic_figure` | Раздел `Двусторонняя навигация` + карта статей и смысловые обратные связи | Из статьи атласа читатель возвращается к теоретическому вопросу и уходит в источниковую/историческую заметку, Handbook или Fieldbook по функции материала. | Кандидат только если обратные переходы останутся непонятными в прозе; сейчас не вставлять в основной текст. |
| `fig-roast-routing-triad` | `editorial_visual_idea` | Shopify Roast story dossier | Roast как развилка: концептуальная статья о механизме исполнения рабочих процессов, историческая заметка о Boba/Shopify, источниковая заметка о README/API/PR/скриншотах. | Идея для будущего прохода; не рисовать без свежей проверки README, PR и прав на скриншоты. |
| `fig-spdd-reasons-canvas` | `external_real_image_candidate` | Fowler/Thoughtworks SPDD | REASONS Canvas как форма удержания намерения, дизайна, исполнения и управления. | Кандидат для статьи SPDD; проверить локальный файл, права и атрибуцию. |
| `fig-spdd-workflow` | `external_real_image_candidate` | Fowler/Thoughtworks SPDD | Рабочая петля: business input → structured prompt → generation → проверка/ревью → sync. | Кандидат для статьи SPDD. |
| `fig-openspdd-command-lifecycle` | `synthetic_figure` | README и шаблоны OpenSPDD | `/spdd-analysis` → `/spdd-reasons-canvas` → `/spdd-generate` → `/spdd-api-test` / `/spdd-code-review` → `/spdd-prompt-update` / `/spdd-sync`. | Кандидат для статьи SPDD; лучше собственная схема. |
| `fig-speckit-sdd-cycle` | `synthetic_figure` | Spec Kit README / Quick Start | `constitution → specify → clarify/checklist → plan → tasks → analyze → implement`, включая человеческие проверки качества. | Кандидат для статьи Spec Kit; это авторская схема по командам, не замена внешнему изображению. |
| `fig-speckit-integration-topology` | `synthetic_figure` | Spec Kit Integrations docs | Агентные интеграции как разные поверхности: команды со slash-префиксом, навыки-интеграции, рецепты, обёртки, общий каталог команд. | Сильный кандидат для границы «переносимый процесс ≠ одинаковая поверхность». |
| `fig-speckit-active-feature-resolution` | `synthetic_figure` | Spec Kit scripts/Core Commands dossier notes | `.specify/feature.json`, текущая Git-ветка, каталог фичи и скрипты разрешения активной фичи. | Кандидат для технической статьи, не для C5. |
| `fig-kiro-feature-spec-lifecycle` | `synthetic_figure` | Kiro Feature Specs / Web Specs docs | `requirements.md` → `design.md` → `tasks.md` → выполнение задач, включая контрольные точки ревью; Web-поверхность даёт отдельные UI/скриншот-кандидаты. | Кандидат для статьи Kiro, но реальные скриншоты Kiro не заменять этой схемой. |
| `fig-kiro-web-spec-artifacts-ui` | `external_real_image_candidate` | Kiro Web Specs docs | Браузерное ревью requirements/design/tasks, загрузка `.md`, элементы управления Run all tasks / Run specific tasks. | Внешний UI/скриншот-кандидат; не перерисовывать без прохода по ассетам и проверки прав. |
| `fig-gsd-core-pi-split` | `synthetic_figure` | GSD Core / GSD Pi README + moved gsd-2 note | `gsd-core` как фазовая петля против `gsd-pi` как local-first CLI/память проекта, с границей свежести и версии. | Кандидат только для статьи GSD; не нужен в основном C5. |
| `fig-kiro-mode-switch` | `synthetic_figure` | Kiro Vibe vs Spec sessions | Vibe session для быстрых вопросов → Spec session для формального плана и прогресса. | Кандидат для границы между свободной и спецификационной работой. |
| `fig-kiro-task-control-stack` | `synthetic_figure` | Kiro Autopilot / Run all Tasks / Hooks / Checkpoints | Выполнение задач с Supervised/Autopilot, checkpoints, hooks и подтверждения на уровне файлов. | Кандидат после свежей проверки UI и источников. |
| `fig-constitutional-sdd-hierarchy` | `external_real_image_candidate` | Marri arXiv/ar5iv | Constitution → spec → plan → tasks → AI generation → implementation → трассируемость соответствия. | Сильный кандидат; лучше собственная схема, если права на рисунок неясны. |
| `fig-csdd-traceability-matrix` | `external_real_image_candidate` | Marri arXiv/ar5iv, banking repo, Mad Devs / Foundry notes | Principle/CWE/control → file/line/implementation technique → свидетельство/гейт. | Кандидат для статьи CSDD. |
| `fig-tdad-two-lines` | `synthetic_figure` | TDAD comparative dossier | Линия 1: behavioral spec → tests → compiled agent definition; линия 2: code-test graph → затронутые тесты → regression guard. | Обязательный кандидат для границы статьи TDAD. |
| `fig-tdad-agent-definition-pipeline` | `external_real_image_candidate` | Test-Driven AI Agent Definition HTML/PDF | TestSmith, PromptSmith, Compiled Agent, hidden tests, MutationSmith. | Кандидат; проверить права и качество фигуры. |
| `fig-tdad-code-test-graph` | `external_real_image_candidate` | Test-Driven Agentic Development HTML/PDF / TDAD repo | AST parser → graph builder → test linker → impact analyzer → `test_map.txt` → coding agent. | Кандидат для второй линии TDAD. |
| `fig-adr-lifecycle-status-origin` | `synthetic_figure` | Nygard/Fowler/MADR + ADR dossier | Жизненный цикл статуса рядом с происхождением: authored/reconstructed; рядом план confirmation. | Сильный кандидат для статьи ADR. |
| `fig-madr-template-slice` | `synthetic_figure` | MADR template | Considered Options, Decision Outcome, Consequences, Confirmation. | Кандидат; при локализации не копировать длинные шаблонные фрагменты. |
| `fig-gsd-phase-artifact-flow` | `synthetic_figure` | GSD dossier / Open GSD docs | Discuss → Plan → Execute → Verify → Ship через `.planning/` и артефакты. | Кандидат для GSD. |
| `fig-gsd-command-routing` | `synthetic_figure` | GSD User Guide | Намерение пользователя → маршрутизатор пространства имён → конкретная команда → слой рабочего процесса/агента/справки. | Кандидат для объяснения экономии токенов и контекста. |
| `fig-gsd-pi-state-projection` | `synthetic_figure` | GSD Pi docs | SQLite как состояние исполнения → markdown-проекции `.gsd/` → ревью/git/промпты/история. | Кандидат для границы GSD-core/GSD-pi. |
| `fig-bmad-workflow-map` | `external_real_image_candidate` | BMAD Workflow Map | Четыре фазы, персоны, поток контекста, Quick Flow. | Кандидат; лучше собственная схема по источнику. |
| `fig-bmad-output-tree` | `synthetic_figure` | BMAD Getting Started | `_bmad/`, `_bmad-output/planning-artifacts`, `_bmad-output/implementation-artifacts`, `project-context.md`. | Кандидат для статьи BMAD. |
| `fig-bmad-sprint-status-machine` | `synthetic_figure` | BMAD sprint planning/status docs | Жизненный цикл story: backlog → ready-for-dev → in-progress → review → done. | Кандидат для статуса работы между агентами и человеком. |
| `fig-pwg-core-object-model` | `synthetic_figure` | PWG dossier + Beads docs | Рабочий узел/bead с зависимостью, владельцем, гейтом, передачей работы, пакетом свидетельств и состоянием восстановления. | Сильный кандидат для PWG. |
| `fig-pwg-ready-blocked-flow` | `synthetic_figure` | Beads dependencies / `bd ready` | Граф зависимостей: незаблокированная работа попадает в очередь готовности, заблокированная работа указывает на гейт или зависимость. | Кандидат для PWG. |
| `fig-pwg-gate-lifecycle` | `synthetic_figure` | `bd gate` docs | Human/timer/GitHub run/GitHub PR gate как устойчивый объект ожидания. | Кандидат для PWG, свидетельств и полномочий. |
| `fig-bd-prime-rehydration` | `synthetic_figure` | `bd prime` docs | SessionStart/PostCompact → `bd prime` → компактный контекст → продолжение работы. | Кандидат для восстановления после сжатия контекста. |
| `fig-gastown-architecture-readme` | `external_real_image_candidate` | Gas Town README / B3 asset notes | Mayor, Town, Rigs, Crew, Hooks, Polecats, Git worktrees. | Кандидат; нужно проверить локальные ассеты и текущий README. |
| `fig-gastown-scheduler-backpressure` | `synthetic_figure` | Gas Town dossier | Очередь, ёмкость, circuit breaker, convoys/polecats и обратное давление. | Кандидат после более глубокой источниковой проверки. |
| `fig-humanlayer-harness` | `editorial_visual_idea` | Только сигнал из `WORKING_DOCUMENTS_MAP.md` | Harness, research-plan-implement, бюджет контекста, BAML. | Не рисовать без исторического или источникового досье. |
| `fig-roast-cog-chain` | `synthetic_figure` | Shopify Roast README / tutorial / releases | Рабочий процесс `execute do`: `cmd` → `agent`/`chat` → `ruby`/`map`/`repeat`/`call`, с передачей выходов по имени шага. | Кандидат для будущей концептуальной статьи Roast; не вставлять в C5 и не использовать вместо API/источниковой заметки. |
| `fig-roast-readme-screenshots-logo` | `external_real_image_candidate` | Shopify Roast README / tutorial | Логотип, скриншоты или визуальные материалы README, если они полезны источниковой заметке. | Внешний кандидат ассета; требуется проверка прав и свежести. |
| `fig-sandvault-policy-surface` | `editorial_visual_idea` | Только слабый будущий сравнительный сигнал | Политика/инструментальная поверхность, если появится источниковое досье. | Не фиксировать сейчас. |


## Заметки по ассетам после источниковой проверки

Источниковая проверка оставляет основной C5 без фигур в основном тексте. Наиболее важное изменение — не количество схем, а разделение реальных визуальных кандидатов и авторских диаграмм. UI Kiro, Mermaid/sequence-материалы README Gas Town, BMAD Workflow Map, изображения SPDD/Fowler, фигуры статей TDAD/CSDD и визуальные материалы README Roast остаются `external_real_image_candidate` до прохода по ассетам. Синтетические схемы допустимы только для нетривиальных границ: две траектории чтения, модель статьи, граница маршрутизации, командный путь Spec Kit, разделение GSD core/pi и цепочка `cog` в Roast.

## Решение по вставке в основной текст для текущего черновика

Текущий черновик C5 не вставляет фигуры в основной текст. Фрагмент работает как мостовая проза: он задаёт две траектории чтения, модель самостоятельной статьи атласа, короткий стресс-тест и реестр будущих статей. Визуальные возможности остаются в этом сопроводительном файле для будущей визуально-источниковой проверки. Это предотвращает два дефекта: декоративную синтетическую схему ради наличия рисунка и подмену реальных визуальных источников текстовыми приближениями до проверки прав и локализации.


## Общий редакторский проход 1: визуальная регрессия

Проверка не выявила готовых локальных изображений для вставки в основной C5. Новая идея `fig-c5-reverse-semantic-navigation` классифицирована как `synthetic_figure`, но не проходит обязательность вставки в основной текст: проза уже объясняет принцип двусторонней навигации, а схема может стать полезной только если будущий читатель потеряет границу между смысловой обратной связью, источниковой заметкой, историей, Handbook и Fieldbook. Реальные внешние кандидаты по SPDD, Kiro, TDAD/CSDD, BMAD, Gas Town и Roast остаются `external_real_image_candidate` до прохода по ассетам.

## Общий редакторский проход 2: визуальное решение

Свежий проход не выявил необходимости вставлять фигуру в основной C5. Слабый переход к проверке тяжёлых случаев исправлен прозой, а не схемой; это лучше соответствует проверке полезности и нетривиальности. Кандидаты `fig-c5-after-abc-to-concept-route`, `fig-c5-two-reading-trajectories`, `fig-c5-concept-article-model`, `fig-c5-routing-boundary` и `fig-c5-reverse-semantic-navigation` остаются в реестре как возможные синтетические фигуры, но ни один не повышен до фигуры в основном тексте без отдельного решения о визуальной плотности.

## Общий редакторский проход 3: визуальная регрессия

Третий проход не выявил фигуру, которую нужно было бы держать в основном тексте для выполнения функции C5. Удаление служебной ссылки на рабочий файл реестра не требует новой схемы: проблема была мета-композиционной, а не визуальной. Все синтетические кандидаты уровня C5 остаются отложенными; внешние реальные кандидаты по будущим статьям по-прежнему требуют прохода по ассетам.

## Проверка после второго стилевого прохода

Второй стилевой проход не вставлял фигуры в основной C5. Таблица остаётся реестром визуальных кандидатов: реальные внешние изображения сохранены как `external_real_image_candidate`, синтетические схемы остаются `synthetic_figure` только после проверки полезности и нетривиальности, а редакционные идеи не превращены в схемы без источникового или ассетного основания. Идентификаторы фигур, статусы и решения по правам/свежести сохранены.
