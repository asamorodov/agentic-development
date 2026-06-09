# Kiro Specs

## Черновое назначение

Документ создан для накопления фактуры о Kiro Specs как методологическом режиме спецификационного управления разработкой. Это рабочее досье, а не готовая глава сайта. Его задача — сохранить устройство процесса, имена артефактов, места принятия решений человеком, ограничения и детали продуктовой реализации, чтобы позже можно было написать плотный раздел о Kiro в части про соседние спецификационные режимы.

В текущей архитектуре теории Kiro Specs нужен как пример productized spec workflow внутри IDE: спецификация становится не внешним документом и не только набором команд, а частью поверхности разработки, task execution и контекстной подстановки для агента. Это назначение зафиксировано в `work/specification-cluster-deep-plan.md` и `work/approved-ai-sdlc-plan.md`.

## Роль в AI-driven SDLC

Kiro помещает спецификацию между намерением человека и агентским исполнением внутри IDE. В базовом описании Specs называются способом разбить сложную фичу на requirements, design и implementation tasks, чтобы двигаться от идеи к работающему изменению через ревьюируемые промежуточные артефакты, а не через один длинный запрос к агенту. Источник: [Kiro Docs: Specs](https://kiro.dev/docs/specs/).

Для AI-driven SDLC это важно по двум причинам.

Во-первых, Kiro делает lifecycle видимым в продуктовой среде. Пользователь не просто просит агента “сделай фичу”; он получает набор файлов в `.kiro/specs/{spec-name}/`, где намерение, дизайн и задачи лежат отдельно и могут быть просмотрены до реализации. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Во-вторых, Kiro связывает спецификацию с исполнением. Tasks из `tasks.md` становятся единицами, которые агент может выполнять по одной; рядом с задачей меняется статус, а IDE показывает прогресс спецификации. Это превращает спецификацию в рабочий интерфейс для делегирования, а не только в справочный документ. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Kiro не нужно смешивать со Spec Kit. Spec Kit важен как переносимый toolkit с templates, scripts и command-driven workflow. Kiro важен как встроенная IDE-поверхность: пользователь проходит требования, дизайн, задачи, task execution, контекст `#spec`, Sync Files, hooks и steering внутри одного продукта. Это локальное различение нужно только для понимания Kiro; полноценное сравнение относится к отдельному проходу.

Внутри самого Kiro важно различать Vibe sessions и Spec sessions. Vibe session рассчитана на быстрые вопросы, объяснения и исследовательскую работу в разговорном режиме; Spec session выбирается через session picker и ведёт сложную задачу через формализованный план, последовательное исполнение и отслеживание прогресса. Для методологии это уточняет границу применения: Kiro не заставляет каждую работу проходить через Specs, но выделяет Specs как режим для сложных фич, существенного рефакторинга, командной документации и задач, где требования и дизайн требуют итераций. Источник: [Vibe vs Spec sessions](https://kiro.dev/docs/chat/vibe/).

## Проблема, которую решает Kiro Specs

Kiro явно отталкивается от ограничения “vibe coding”: быстрый интерактивный агентский режим удобен для прототипов, но теряет устойчивость, когда фича становится сложной, требует нескольких файлов, архитектурных решений, edge cases и последовательной реализации. В представлении Kiro Specs должны сохранить скорость AI-assisted разработки, но добавить структуру: сначала выяснить требования, затем зафиксировать технический дизайн, затем разбить реализацию на задачи. Источники: [Introducing Kiro](https://kiro.dev/blog/introducing-kiro/) и [Kiro Docs: Specs](https://kiro.dev/docs/specs/).

Практическая проблема выглядит так: агент может быстро написать код, но плохо удерживает полный набор требований, скрытые зависимости, ограничения существующей архитектуры и последовательность безопасных изменений. Kiro переносит часть этой нагрузки в файлы спецификации. Требования становятся проверяемым списком поведения, дизайн — местом архитектурного решения, задачи — очередью реализации. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Отдельная проблема — уже существующий код. Документация Kiro допускает создание спецификации не только для новой фичи, но и через анализ существующих требований или текущей кодовой базы. В режиме Analyze Requirements Kiro должен изучить существующие документы или код, найти неясности, противоречия, неполные требования и предложить дополнительные вопросы или уточнения. Источник: [Kiro Docs: Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/).

Блог Kiro про анализ требований уточняет, какие именно ошибки требований особенно опасны для агентской разработки: неверный уровень детализации, неоднозначность, противоречивость и неполнота. Важная для теории деталь: авторы связывают рост риска именно с AI-assisted engineering, потому что начальный запрос фактически становится требованием, а агент быстро превращает недосказанность в кодовые решения, которые человек может не успеть заметить. Источник: [Requirements analysis: catching requirement bugs before they become code](https://kiro.dev/blog/deep-spec-analysis/).

Там же приведены численные ориентиры из внешних исследований: при мутации ясных запросов в неоднозначные, неполные или противоречивые Pass@1 падал на 20-40%, а 60-90% синтаксически валидного кода оказывалось семантически неверным; отдельная работа по underspecification описывает, что недоопределённые запросы примерно вдвое чаще регрессируют при смене модели или запроса. Эти цифры не нужно превращать в универсальную метрику Kiro, но они полезны как обоснование, почему спецификационный слой нужен до генерации кода. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/).

## Базовый workflow Feature Specs

Feature Spec — основной сценарий Kiro для новой фичи. Он строится вокруг трёх файлов:

- `requirements.md`;
- `design.md`;
- `tasks.md`.

Все они создаются в `.kiro/specs/{spec-name}/`. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Feature Specs поддерживают два варианта рабочего процесса: Requirements-First и Design-First. В Requirements-First пользователь начинает с поведения системы, Kiro формализует его в требования, затем строит дизайн и задачи. В Design-First пользователь начинает с технической архитектуры, pseudocode, low-level design или уже существующего design document; Kiro сначала создаёт `design.md`, затем выводит требования, которые должны быть технически осуществимы в рамках подтверждённой архитектуры, и после этого создаёт tasks. Источники: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/), [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/) и [Design-First Workflow](https://kiro.dev/docs/specs/feature-specs/tech-design-first/).

### 1. Requirements

Первый шаг в Requirements-First — формулирование требований. Kiro просит описать фичу в чате или через интерфейс Specs и затем генерирует `requirements.md`. В документации требования описаны через user stories, acceptance criteria и EARS notation. Базовая форма требования выглядит как `WHEN [condition/event] THE SYSTEM SHALL [expected behavior]`. Для будущей теории важно сохранить именно эту деталь: Kiro не ограничивается произвольным “описанием фичи”, а пытается получить поведенческую форму, которую можно ревьюить и затем трассировать к реализации. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

У требований есть человеческий gate. Пользователь должен открыть `requirements.md`, проверить полноту и точность, при необходимости продолжить диалог с Kiro и подтвердить переход дальше. В нормальном Feature Spec Kiro не должен автоматически перескакивать к дизайну без review. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

### 2. Design

После подтверждения требований Kiro создаёт `design.md`. Этот файл должен описать архитектурный подход, компоненты, интерфейсы, модели данных, обработку ошибок и стратегию тестирования. Для досье важен сам переход: `requirements.md` становится входом для `design.md`, а дизайн должен объяснить, как требования будут реализованы технически. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Здесь возникает второй human gate. Пользователь просматривает дизайн, уточняет спорные решения и только затем разрешает перейти к задачам. Это место, где человек должен отловить архитектурно неверное направление до того, как агент начнёт массово менять код. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

В Design-First этот порядок разворачивается: design становится первым артефактом, а requirements выводятся из подтверждённой архитектуры. Kiro различает High Level Design и Low Level Design. High Level Design подходит для системной архитектуры, компонентов, взаимодействий и non-functional properties; Low Level Design — для алгоритмических деталей, interfaces, contracts и структур данных. Источник: [Design-First Workflow](https://kiro.dev/docs/specs/feature-specs/tech-design-first/).

### 3. Tasks

После подтверждения дизайна Kiro создаёт `tasks.md`: упорядоченный список implementation tasks. Важная особенность — задачи должны быть достаточно малыми, чтобы их можно было выполнять последовательно и отслеживать статус. В Requirements-First документации для `tasks.md` отдельно названы discrete trackable tasks, descriptions and expected outcomes, dependencies between tasks и optional vs required tasks. Это делает task phase не только списком шагов, но и местом, где человек может отделить обязательный MVP-путь от дополнительных задач. Источник: [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/).

Здесь есть третий gate: пользователь смотрит task breakdown, меняет приоритеты, отмечает optional tasks и подтверждает, что порядок, granularity и охват подходят для реализации. После этого задачи можно запускать из интерфейса Kiro. Источник: [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/).

### 4. Task execution

На этапе реализации пользователь выбирает задачу из `tasks.md`, а Kiro выполняет её с учётом spec context. Статус задачи меняется по мере выполнения. В будущей теории это нужно описывать как productized delegation unit: единицей поручения становится не весь prompt и не вся фича, а конкретная задача из утверждённой спецификации. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Общая страница Specs уточняет интерфейсные статусы task execution: для `tasks.md` Kiro показывает real-time status updates, а задачи обновляются как `in-progress` или `completed`. Официальный transcript на главной странице Kiro показывает ту же механику на примере spec `email-opt-in`: у задачи `Set up backend API foundation` actionable label `Start task` переходит в `Task in progress`, затем в зелёный `Task completed`; checkbox становится отмеченным, рядом появляются `View changes` и `View execution`, а в chat panel видна status card `Status: Completed`. Это закрывает часть вопроса о видимых статусах, но не доказывает, что статус хранится прямо в `tasks.md`, а не в metadata IDE. Источники: [Kiro Docs: Specs](https://kiro.dev/docs/specs/) и [Kiro home page transcript](https://kiro.dev/).

Kiro может запускать все задачи разом. В этом режиме он строит dependency graph из `tasks.md`, группирует независимые tasks в waves и выполняет задачи внутри одной wave параллельно, а waves — последовательно. Это важная деталь: task list в Kiro не просто checklist, а потенциальный план параллельного исполнения с зависимостями. Источник: [Kiro Docs: Specs](https://kiro.dev/docs/specs/).

Пост `Specs just got faster (and smarter)` раскрывает правила параллельного исполнения подробнее. Kiro не запускает параллельно задачи, которые пишут в одни и те же файлы; настройка и инфраструктурные работы идут первыми; тестовые задачи ждут код, который они проверяют; каждая параллельная задача получает изолированный контекст, чтобы состояние одной задачи не протекало в другую. Если одна задача падает, остальные независимые задачи продолжают выполняться, а пользователь видит, какие задачи завершились и какие требуют внимания. Источник: [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/).

Более ранний пост про `Run all Tasks` важен как история продуктового ограничения. Kiro изначально не давал кнопку запуска всех задач, потому что команда хотела сохранить видимость и контроль: пользователь должен был видеть исполнение каждой задачи и ловить ошибки рано. Кнопку добавили только после появления дополнительных опор: property-based tests, dev servers, LSP diagnostics, subagents и real-time visibility. В том же посте Kiro ограничивает сильный сценарий: `Run all Tasks` особенно уместен для небольших Feature Specs, а предварительная проверка spec остаётся обязательной частью работы. Источник: [Run all tasks: the feature we refused to ship](https://kiro.dev/blog/run-all-tasks/).

По best practices `Run all Tasks` запускает только незавершённые tasks, которые помечены как required. Это важно для чтения `tasks.md`: optional tasks не должны автоматически становиться частью пакетного запуска, а уже реализованные tasks нужно предварительно синхронизировать или явно пометить. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Kiro также поддерживает task execution hooks: автоматические действия до начала задачи или после её завершения. Это связывает Specs с broader IDE automation. Например, pre-task hook может подготовить окружение или подтянуть контекст, а post-task hook — запустить форматирование, тесты или другую проверку. Источник: [Kiro Docs: Hooks](https://kiro.dev/docs/hooks/) и [Kiro Docs: Hook Triggers](https://kiro.dev/docs/hooks/types/).

Отдельный слой контроля появляется уже во время исполнения задачи: Kiro различает режимы Autopilot и Supervised. В Autopilot агент может менять файлы и выполнять многошаговую работу без подтверждения каждого действия; пользователь сохраняет контроль через просмотр всех изменений, Revert и возможность остановить исполнение. В Supervised Kiro останавливается после каждого хода с файловыми изменениями и показывает правки для подтверждения; этот режим работает и в обычном чате, и в spec chat sessions. Для Specs это важная деталь: review gates перед `requirements.md`, `design.md` и `tasks.md` не являются единственной точкой человеческого контроля; после старта реализации человек может дополнительно включить проверку изменений на уровне файлов или отдельных hunks. Источник: [Kiro Docs: Autopilot](https://kiro.dev/docs/chat/autopilot/).

## Bugfix Specs

Bugfix Specs используют похожую трёхфазную структуру, но первая фаза меняется. Вместо `requirements.md` появляется `bugfix.md`. В нём фиксируются текущее поведение, ожидаемое поведение, steps to reproduce, scope и ограничения. Затем Kiro создаёт `design.md` и `tasks.md`. Источник: [Kiro Docs: Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/).

Это важное отличие: Kiro признаёт, что исправление дефекта требует другого входного артефакта, чем новая фича. Для bugfix спецификация начинается с диагностики расхождения между текущим и ожидаемым поведением, а не с user story. Это делает Kiro полезным не только для планирования новых возможностей, но и для repair workflow.

В документации Bugfix Specs отдельно выделено unchanged behavior: спецификация должна фиксировать, что должно продолжить работать после исправления. В `bugfix.md` это выражается формой вроде `WHEN [condition] THEN the system SHALL CONTINUE TO [existing behavior]`. Затем `design.md` должен включить root cause analysis, proposed fix approach и свойства, которые нужно проверить: дефект воспроизводится в текущей реализации, исправленная реализация даёт правильное поведение, неизменяемое поведение продолжает работать. Tasks phase генерирует implementation tasks с property-based tests для воспроизведения бага, проверки исправления и предотвращения регрессий. Источник: [Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/).

В AI-driven SDLC это показывает, что specification layer может обслуживать разные типы изменения. Для новой фичи нужен файл намерений и критериев приёмки; для бага — файл воспроизведения и границ исправления. Обе ветки сходятся в `design.md` и `tasks.md`, потому что реализация всё равно требует технического решения и последовательного выполнения.

## Quick Plan

Quick Plan — укороченный режим для понятных или малых задач. Он создаёт те же артефакты, что и стандартный Spec session, но делает это за один проход: Kiro задаёт уточняющие вопросы заранее, затем генерирует `requirements.md`, `design.md` и `tasks.md` без approval gates между фазами. Источник: [Kiro Docs: Quick Plan](https://kiro.dev/docs/specs/quick-plan/).

Для досье особенно важна граница применимости. Quick Plan не отменяет Specs; он показывает, что Kiro не требует полного `requirements.md` → `design.md` → `tasks.md` цикла для каждой мелкой операции. Если задача понятна, риск низкий, а пользователь не нуждается в отдельном ревью требований и дизайна, Quick Plan уменьшает накладные расходы. Источник: [Kiro Docs: Quick Plan](https://kiro.dev/docs/specs/quick-plan/).

Блог Kiro уточняет, что перед вопросами Quick Plan сканирует workspace, чтобы определить язык, фреймворки и структуру проекта, а затем задаёт вопросы по четырём областям: границы и ограничения, неоднозначности в описании, развилки реализации и направляющие решения о форме фичи. После генерации пользователь сразу попадает к списку задач, но артефакты всё равно сохраняются и используются агентом при исполнении. Если пользователь меняет задачу, Kiro регенерирует только задачи; если меняет дизайн, перестраивает дизайн и задачи; если меняет границы, запускает цепочку от требований заново. Источник: [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/).

С точки зрения failure modes это двойственная деталь. Quick Plan полезен как защита от overuse полного spec workflow. Но он же может стать способом преждевременно обойти важные gates, если задача кажется простой только на поверхности. В будущей теории стоит показать, что Kiro не даёт универсального ответа “всегда писать spec”; он вводит несколько режимов, и ответственность за выбор режима остаётся у человека.

## Analyze Requirements

Analyze Requirements — режим, где Kiro помогает не сразу создавать спецификацию, а сначала анализирует существующие материалы. В документации речь идёт о том, что Kiro может читать текущие requirement documents или codebase, выявлять gaps, ambiguities и inconsistencies, а затем предлагать уточнения. Источник: [Kiro Docs: Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/).

Это важный слой перед обычным Feature Spec. В сложной организации требования редко приходят как чистый prompt. Они могут быть разбросаны по тикетам, документации, старому коду и разговорам. Analyze Requirements превращает Kiro в помощника по нормализации входа: до проектирования он должен помочь человеку увидеть, какие требования ещё не готовы для реализации.

Human gate здесь находится в ответе на уточнения. Если Kiro нашёл неоднозначность, человек должен решить, какое поведение действительно нужно. Иначе спецификация будет выглядеть полной, но закрепит неверное понимание. Для будущего текста это хороший пример того, что спецификационный workflow не устраняет judgment; он делает места judgment более явными.

Документация подчёркивает, что этот анализ занимает минуты, а не секунды, потому что Kiro рассуждает по всему набору требований. Находки приходят как clarifying questions: для каждого вопроса указываются затронутые требования, объяснение проблемы и proposed fixes; человек может выбрать исправление, дать собственный ответ или отклонить вопрос, если неоднозначность намеренная. По мере разрешения вопросов Kiro обновляет `requirements.md`. Источник: [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/).

`Deep Spec Analysis` раскрывает внутреннюю модель этого шага как три стадии. Сначала refinement доводит грубые acceptance criteria до уровня, где названы события, входы, состояния, выходы и условия между ними; при этом Kiro ищет неправильное использование EARS-паттернов, расплывчатые уточнители и язык уровня реализации. Затем auto-formalization переводит требования в SMT-lib: schema с entities, attributes, events, inputs и outputs, assertions как логические implications и background assertions для неявных ограничений домена. Третья стадия — logical analysis, где automated reasoning ищет противоречия, gaps, accepted scenarios и rejected scenarios. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/).

Для досье особенно важен интерфейс findings. Технические находки не показываются пользователю как формальная логика; Kiro переводит их в короткие вопросы с двумя вариантами ответа. В посте перечислены пять типов findings: ambiguity questions, conflict questions, completeness questions, accepted-scenario questions и rejected-scenario questions. Вариант A означает оставить требование как есть, вариант B — изменить его конкретным предложенным способом; после ответа LLM переписывает затронутые требования так, чтобы выбор человека стал явным в `requirements.md`. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/).

Ограничение этого механизма тоже важно сохранить. Auto-formalization зависит от того, насколько хорошо явная спецификация и background assertions описывают домен. В посте прямо сказано, что самая перспективная зона для улучшения — построение хороших formal domain models: без явной модели возможного и невозможного reasoning engine может находить проблемы в сценариях, которые невозможны в реальном домене. Текущая реализация частично компенсирует это множественным sampling background knowledge assertions и частотным порогом, но не снимает проблему полностью. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/).

## Context: где живёт знание

В Kiro контекст распределён по нескольким слоям.

Первый слой — файлы конкретной спецификации в `.kiro/specs/{spec-name}/`: `requirements.md` или `bugfix.md`, `design.md`, `tasks.md`. Это локальный контекст изменения. Источник: [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/) и [Kiro Docs: Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/).

Второй слой — steering files в `.kiro/steering/`. Steering задаёт долгоживущий проектный контекст: product overview, technology stack, project structure, conventions и другие правила, которые должны повторно использоваться в разных задачах. Kiro может сгенерировать три foundational files: `product.md`, `tech.md` и `structure.md`; они по умолчанию включаются в каждое взаимодействие. Steering бывает workspace-level в `.kiro/steering/` и global-level в `~/.kiro/steering/`; при конфликте workspace steering имеет приоритет. Источник: [Kiro Docs: Steering](https://kiro.dev/docs/steering/).

Руководство `Your first project` показывает, что генерация steering не является абстрактной анкетой: при `Generate Steering Docs` Kiro анализирует репозиторий и читает файлы вроде `package.json`, `README.md`, `vite.config.js`, `App.tsx` и `CartContext.tsx`, после чего складывает project steering в `.kiro/steering/`. Для методологии это значит, что долговременный контекст можно первично собрать из фактической структуры проекта, но его всё равно нужно ревьюить как сгенерированную документацию. Источник: [Your first project](https://kiro.dev/docs/getting-started/first-project/).

Steering files имеют inclusion modes: `always`, `fileMatch`, `manual` и `auto`. Это важно для контекстной экономики: не вся проектная память должна грузиться всегда. Workspace-wide standards можно держать always-on, file-specific правила включать по паттернам, тяжёлые справочные документы подключать вручную или через auto description. Источник: [Steering](https://kiro.dev/docs/steering/).

Третий слой — chat context providers. Для Specs важен `#spec`: пользователь может выбрать spec из списка или сослаться на конкретную спецификацию вроде `#spec:user-authentication`. Kiro автоматически включает все spec files — `requirements.md`, `design.md` и `tasks.md` — в контекст разговора. Это позволяет обсуждать реализацию, уточнения, проверку соответствия и причины архитектурных решений, не пересказывая спецификацию вручную. Источник: [Kiro Docs: Chat](https://kiro.dev/docs/chat/).

Отдельно рядом со Specs стоит IDE MCP. MCP добавляет в Kiro внешние инструменты, prompts и resource templates; они могут появляться в `#` mention list, а инструменты можно вызывать по смысловому запросу или явно в форме вроде `#[aws-docs] search_documentation ...`. Для Specs это важно в двух местах: на входе, когда требования или дизайн импортируются из внешних систем, и на исполнении, когда task может опираться на внешнюю документацию, API или доменную базу знаний. Источники: [MCP](https://kiro.dev/docs/mcp/) и [MCP Tools](https://kiro.dev/docs/mcp/usage/).

У IDE MCP есть собственная модель управления риском. Конфигурация лежит на уровне workspace в `.kiro/settings/mcp.json` и на уровне пользователя в `~/.kiro/settings/mcp.json`; настройки workspace имеют приоритет. Для каждого server можно задавать `autoApprove` и `disabledTools`, временно отключать server или отдельные tools, а Kiro перед запуском MCP tool показывает пользователю запрос подтверждения с деталями инструмента и параметрами. Если MCP server просит дополнительные данные во время выполнения, Kiro показывает elicitation form или URL-based request, а пользователь может отправить ответ, отклонить запрос или закрыть его. Источники: [MCP Configuration](https://kiro.dev/docs/mcp/configuration/) и [MCP Tools](https://kiro.dev/docs/mcp/usage/).

Steering можно связывать с живыми файлами workspace через markdown-ссылки вида `#[[file:<relative_file_name>]]`. Это важная практическая деталь: steering не обязан быть только ручным пересказом стандартов, он может ссылаться на `api/openapi.yaml`, `.env.example`, UI patterns или другие текущие файлы проекта. Kiro также поддерживает `AGENTS.md` как steering directive; такие файлы можно положить в корень workspace или в `~/.kiro/steering/`, но в отличие от Kiro steering files они всегда включаются и не поддерживают inclusion modes. Источник: [Kiro Docs: Steering](https://kiro.dev/docs/steering/).

Четвёртый слой — Sync Files. Kiro может синхронизировать spec files с текущим состоянием проекта, в том числе учитывать уже выполненные задачи. Для досье это важный хвост жизненного цикла: спецификация не обязана умереть после первого generation step; её можно приводить в соответствие с изменившейся реальностью проекта. Источник: [Kiro Docs: Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Best practices дают конкретный сценарий для уже реализованных tasks: если коллега или сам пользователь выполнил часть работы в другой сессии, можно открыть `tasks.md` и нажать `Sync Files`, чтобы Kiro автоматически отметил завершённые задачи. Альтернатива — в spec chat попросить Kiro проверить, какие задачи уже завершены; тогда он анализирует codebase, выявляет реализованную функциональность и обновляет task spec. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Пятый слой — CLI-поверхность вокруг той же `.kiro` конфигурации, но с важной оговоркой. Официальный блог о Kiro CLI говорит, что конфигурация `.kiro` работает и в IDE, и в CLI: Kiro CLI может использовать те же steering files и MCP servers, а проектная документация и `.kiro` configuration переносятся между средами. Это не означает, что CLI-документация описывает тот же визуальный Specs workflow с gates, но означает, что долговременный контекст Specs-соседних механизмов не ограничен IDE. Источник: [Bring Kiro agents to your terminal with Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/).

Для CLI особенно важна разница между обычными steering files и custom agents. CLI steering в `.kiro/steering/` становится доступен в CLI chat sessions, но документация отдельно предупреждает: custom agents не получают steering files автоматически; их нужно явно добавить в `resources`, например `file://.kiro/steering/**/*.md`. Для методологии это существенная неудобная деталь: если команда создаёт специализированного агента для ревью, backend или тестов, проектная память может не попасть к нему сама по себе. Источник: [Kiro CLI: Steering](https://kiro.dev/docs/cli/steering/).

Шестой слой — Powers в IDE. Это не часть основного порядка Specs, но соседний механизм, который влияет на то, какие знания и инструменты агент получает при исполнении задач, связанных со спецификацией. Powers упаковывают `POWER.md`, конфигурацию MCP server и, опционально, steering/hooks; Kiro активирует релевантные powers по ключевым словам в разговоре, вместо того чтобы заранее загружать все описания MCP tools. В документации проблема описана через перегрузку контекста: несколько MCP servers могут загрузить сотни описаний инструментов и занять значительную часть окна контекста ещё до первого запроса. Для Kiro Specs это важно как ещё один контекстный слой рядом со steering и hooks: он может усилить реализацию и проверки, но его автоматическая активация не заменяет явное ревью spec files. Источники: [Kiro Docs: Powers](https://kiro.dev/docs/powers/) и [Create powers](https://kiro.dev/docs/powers/create/).

Практическая деталь Powers: если power включает MCP, при установке Kiro регистрирует MCP server в `~/.kiro/settings/mcp.json` в секции Powers; custom power минимально требует `POWER.md`, а `mcp.json` и `steering/` добавляются по необходимости. Это делает Powers удобной упаковкой доменной экспертизы, но также создаёт ещё один источник изменения доступных инструментов и контекста, который команда должна понимать при разборе поведения агента. Источники: [Install powers](https://kiro.dev/docs/powers/installation/) и [Create powers](https://kiro.dev/docs/powers/create/).

Седьмой слой — enterprise governance. Для методологии это не фаза Specs, а организационная рамка, которая заранее ограничивает, какие модели, MCP servers, API keys и web tools вообще доступны агенту в IDE и CLI. В Kiro console администратор может включить model access management, собрать allow list моделей, назначить default model, полностью выключить MCP или подключить MCP registry с vetted servers, разрешить или запретить генерацию API keys для CLI automation и выключить `web_search`/`web_fetch`. Источник: [Governance](https://kiro.dev/docs/enterprise/governance/).

MCP governance особенно важен для Specs, потому что external tools могут стать входом требований, источником доменного знания или частью исполнения task. Официальная документация описывает два уровня: MCP on/off toggle и MCP registry URL в Kiro Profile. Registry — это JSON-файл, который обслуживается по HTTPS; Kiro clients получают его при старте и затем синхронизируют примерно раз в 24 часа. Если server удалён из registry, Kiro прекращает его использование и не даёт добавить обратно; если версия в registry изменилась, client перезапускает server с registry-defined version. У этого контроля есть граница: документация прямо предупреждает, что enforcement client-side и пользователь с административным доступом к машине может его обойти. Источник: [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/).

CLI registry docs добавляют неудобную деталь: даже при активном registry personal MCP servers из `mcp.json` могут загружаться рядом с registry-managed servers, а `/mcp add` picker показывает только registry entries. Пользователь также может задавать registry overrides для `env`, `headers` и `timeout`; registry задаёт основу server, но authentication keys, team headers и timeout могут оставаться локальной настройкой. Для будущего текста это важно как граница между централизованной политикой и фактической конфигурацией developer environment. Источник: [Kiro CLI: MCP Registry](https://kiro.dev/docs/cli/mcp/registry/).

Восьмой слой — enterprise monitoring and tracking. Это не часть внутренней цепочки Specs, но важный слой наблюдаемости вокруг IDE/CLI-работы: администраторы могут включить dashboard агрегированных метрик, per-user activity reports, prompt logging в S3, а также опираться на AWS CloudTrail и Amazon CloudWatch для событий и метрик AWS-аккаунта. Для Kiro Specs это закрывает отдельный вопрос provenance: часть работы становится видимой не только через `requirements.md`, `design.md`, `tasks.md`, diffs и hooks, но и через административные журналы использования. При этом эти журналы не являются spec traceability model: dashboard и user activity reports говорят о подписках, клиентах, сообщениях, credits, моделях и некоторых старых метриках принятия/отклонения кода, а prompt logs фиксируют prompts/responses и inline suggestions; они не заменяют чтение spec files и review execution history. Источники: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing Kiro usage on the dashboard](https://kiro.dev/docs/enterprise/monitor-and-track/dashboard), [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).

Слой данных и приватности нужно держать рядом с monitoring. Kiro docs по data protection говорят, что Kiro хранит questions, responses и additional context вроде code для генерации ответов; для Free Tier и individual subscribers контент хранится в `us-east-1`, а для enterprise users источник формулирует более жёсткую границу: data is not stored. Там же указано, что enterprise content не используется для service improvement, enterprise users automatically opted out of telemetry and content collection by AWS, а настройки telemetry для user activity reports контролирует администратор в Kiro console. Для методологии это важная оговорка: если Specs используются в корпоративном контуре, контроль доступа, logging и хранение данных становятся частью процесса внедрения, а не только вопросом удобства IDE. Источник: [Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/).

## Артефакты

Основные артефакты Kiro Specs:

- `.kiro/specs/{spec-name}/requirements.md` — требования для новой фичи: user stories, acceptance criteria, уточнённое поведение.
- `.kiro/specs/{spec-name}/bugfix.md` — входной файл для исправления дефекта: текущее поведение, ожидаемое поведение, воспроизведение, scope.
- `.kiro/specs/{spec-name}/design.md` — технический дизайн: архитектура, компоненты, data models, interfaces, error handling, testing strategy.
- `.kiro/specs/{spec-name}/tasks.md` — упорядоченный список задач реализации с ожидаемыми результатами, зависимостями и разделением optional vs required tasks.
- imported requirement sources — существующие PRD, JIRA tickets, Confluence pages, GitHub issues, артефакты из подключённых через MCP систем или загруженные документы, из которых Kiro может создать requirements в Requirements-First режиме.
- imported design sources — existing design document, architecture diagram, pseudocode, low-level design или технический документ, из которого Kiro может начать Design-First spec; best practices отдельно допускают PNG/JPG diagrams, экспорт из draw.io или Lucidchart и фотографии эскизов на доске.
- `.kiro/steering/product.md`, `.kiro/steering/tech.md`, `.kiro/steering/structure.md` — foundational steering files для продуктового, технологического и структурного контекста проекта.
- другие файлы в `.kiro/steering/` или `~/.kiro/steering/` — долгоживущие проектные правила и контекст, которые Kiro может использовать между спецификациями.
- `AGENTS.md` — дополнительный формат steering directives, который Kiro подхватывает из корня workspace или из `~/.kiro/steering/`, но включает всегда.
- ссылки `#[[file:<relative_file_name>]]` внутри steering files — способ привязать steering к живым файлам workspace.
- `.kiro/settings/mcp.json` и `~/.kiro/settings/mcp.json` для IDE MCP — workspace и user конфигурация внешних tools, prompts и resources; через `autoApprove` и `disabledTools` команда управляет тем, что Kiro может вызывать без повторного подтверждения и какие tools вообще скрыты от агента.
- MCP prompts и resource templates в `#` mention list — внешние prompt templates и параметризованные resources, которые пользователь добавляет в spec chat как контекст.
- MCP elicitation requests — встроенные формы или URL requests в ленте выполнения, через которые внешний MCP server просит у человека недостающие данные во время выполнения tool.
- Kiro Profile shared settings — enterprise-level настройки вроде `model_config`, `mcpEnabled`, `mcpRegistryUrl`, `apiKeysEnabled`, `webSearchEnabled` и `webFetchEnabled`, которые администратор публикует из Kiro console, а Kiro clients получают при старте. Источник: [Governance](https://kiro.dev/docs/enterprise/governance/).
- MCP registry JSON — централизованный allow list MCP servers, который Kiro clients читают по HTTPS; он может управлять server version и configuration, но остаётся client-side enforcement и требует сетевой доступ к registry URL. Источник: [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/).
- model allow list и default model — governance-артефакты, которые ограничивают выбор моделей для пользователей группы, но требуют предварительно включённого model access management. Источник: [Model Governance](https://kiro.dev/docs/enterprise/governance/model/).
- API key generation toggle и web tools toggles — настройки, которые разрешают или запрещают генерацию API keys для CLI automation и доступ к `web_search`/`web_fetch`. Источники: [API key Governance](https://kiro.dev/docs/enterprise/governance/api-keys/) и [Web Tools Governance](https://kiro.dev/docs/enterprise/governance/web-tools/).
- Kiro usage dashboard — административная dashboard с агрегированными метриками IDE/CLI: subscriptions, active users, credits consumed, client type, subscription tier и programming language filters. Источник: [Viewing Kiro usage on the dashboard](https://kiro.dev/docs/enterprise/monitor-and-track/dashboard).
- user activity report CSV — ежедневный отчёт по пользователям, client type (`KIRO_IDE`, `KIRO_CLI`, `PLUGIN`), сообщениям, conversations, credits, overage, model-name message counts и старым метрикам accepted/rejected/dismissed generated lines. Отчёт пишется в S3 по пути вида `s3://bucketName/prefix/AWSLogs/accountId/KiroLogs/user_report/region/year/month/day/00/clientType_accountId_user_report_timestamp.csv`; при числе пользователей больше 1000 за день Kiro разбивает отчёт на несколько CSV. Источник: [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/).
- prompt logs in S3 — журналы inline suggestions и IDE chat conversations, где при включённой настройке Kiro пишет user prompts и Kiro responses в S3 bucket в аккаунте клиента; примеры полей включают `prompt`, `assistantResponse`, `conversationId`, `utteranceId`, `requestId`, `leftContext`, `rightContext`, `fileName`, `userId` и `timeStamp`. Источник: [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).
- AWS CloudTrail и Amazon CloudWatch — внешние AWS-механизмы наблюдаемости вокруг Kiro activity: CloudTrail фиксирует API calls/events в S3, CloudWatch позволяет собирать metrics, dashboards и alarms, например по количеству invocations или daily active users. Источник: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/).
- `.kiro/agents/` и `~/.kiro/agents/` — CLI custom agents; они задают инструменты, разрешения, resources, MCP servers и prompt для специализированных рабочих режимов.
- `.kiro/settings/mcp.json` и `~/.kiro/settings/mcp.json` — CLI MCP configuration на уровне проекта и пользователя; agent-level `mcpServers` и `includeMcpJson` могут менять, какие внешние инструменты доступны конкретному агенту.
- CLI resources вроде `file://README.md`, `file://.kiro/steering/**/*.md`, `skill://.kiro/skills/**/SKILL.md` и knowledge base resources — явная упаковка контекста для custom agents.
- `POWER.md`, `mcp.json` и `steering/` внутри каталога power — упаковка динамически подключаемого контекста, MCP tools и инструкций для конкретного рабочего режима IDE Powers; это соседний механизм Kiro, который может влиять на исполнение спецификации через доступные инструменты и steering, но не заменяет `requirements.md`, `design.md` и `tasks.md`.
- Hook definitions — автоматизация, которая может срабатывать на события IDE, включая spec task execution.
- Chat references вроде `#spec` — способ явно добавить spec context в разговор.

Источники: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/), [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/), [Design-First Workflow](https://kiro.dev/docs/specs/feature-specs/tech-design-first/), [Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/), [Steering](https://kiro.dev/docs/steering/), [Hooks](https://kiro.dev/docs/hooks/), [Context](https://kiro.dev/docs/chat/context/), [MCP Configuration](https://kiro.dev/docs/mcp/configuration/), [MCP Tools](https://kiro.dev/docs/mcp/usage/), [Kiro CLI: Custom agents](https://kiro.dev/docs/cli/custom-agents/), [Kiro CLI: MCP](https://kiro.dev/docs/cli/mcp/), [Kiro CLI: Agent configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/), [Create powers](https://kiro.dev/docs/powers/create/), [Governance](https://kiro.dev/docs/enterprise/governance/), [Model Governance](https://kiro.dev/docs/enterprise/governance/model/), [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/), [API key Governance](https://kiro.dev/docs/enterprise/governance/api-keys/), [Web Tools Governance](https://kiro.dev/docs/enterprise/governance/web-tools/), [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).

## Как один артефакт становится входом для следующего

В Feature Specs цепочка выглядит так:

1. Описание фичи в чате или интерфейсе Specs становится `requirements.md`; входом также могут быть существующие требования из PRD, JIRA, Confluence, GitHub issues, MCP-подключённых систем или загруженных документов.
2. Подтверждённый `requirements.md` становится входом для `design.md`.
3. Подтверждённый `design.md` становится входом для `tasks.md`.
4. `tasks.md` становится интерфейсом последовательного agent execution.
5. При запуске всех задач Kiro может построить dependency graph, выполнить независимые tasks параллельно по waves и обновлять progress.
6. Результаты выполнения задач могут быть отражены в task status и через Sync Files возвращены в spec files.

Источники: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/), [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/) и [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Best practices дают две конкретные дорожки импорта существующих требований. Если источник требований доступен через MCP, его можно подключить напрямую к spec session; если это обычный файл в репозитории, документация предлагает положить его рядом с кодом и в spec chat сказать примерно `#foo-prfaq.md Generate a spec from it`. Тогда внешний PRD, выгрузка задач или другой документ становится входом для генерации requirements and design specs, а не остаётся ссылкой в голове пользователя. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

В Design-First цепочка другая:

1. Техническая идея, architecture description, pseudocode, existing design document или architecture diagram становится `design.md`.
2. Подтверждённый `design.md` становится входом для вывода `requirements.md`.
3. Подтверждённые requirements и design становятся входом для `tasks.md`.
4. `tasks.md` переходит в task execution.

Источник: [Design-First Workflow](https://kiro.dev/docs/specs/feature-specs/tech-design-first/).

Best practices добавляют ограничение, которое легко потерять при гладком пересказе: порядок работы выбирается при создании spec и не переключается внутри уже начатой спецификации. Если команда начала Requirements-First, а затем поняла, что нужен Design-First, нужно создать новую Feature Spec и при необходимости перенести релевантный материал. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

В Bugfix Specs цепочка похожа, но первый файл другой:

1. Описание дефекта становится `bugfix.md`.
2. Подтверждённый `bugfix.md` становится входом для `design.md`.
3. Подтверждённый `design.md` становится входом для `tasks.md`.
4. Задачи выполняются по одной и меняют код.

Источник: [Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/).

Это делает Kiro хорошим примером staged agency. Агент не получает всё сразу как одно поручение; он участвует в цепочке, где каждый следующий шаг зависит от человечески подтверждённого предыдущего артефакта.

## Роли и участники

В Kiro Specs нет отдельной многоагентной социальной модели вроде Gas Town или BMAD. Основные участники проще:

- человек-заказчик или инженер формулирует намерение, отвечает на вопросы, утверждает требования, дизайн и задачи;
- Kiro Agent генерирует spec files, анализирует требования, предлагает дизайн, разбивает работу на задачи и выполняет selected tasks;
- IDE surface показывает specs, task status, hooks, chat context и связь с codebase;
- steering files выступают как долговременная память проекта, но их всё равно создаёт и поддерживает человек или команда.
- enterprise admin задаёт организационную политику: какие модели доступны, включён ли MCP, используется ли MCP registry, можно ли выпускать API keys для CLI и доступны ли web tools. Это роль до начала конкретной spec session, но она влияет на то, чем агент сможет пользоваться при создании и исполнении спецификации. Источник: [Governance](https://kiro.dev/docs/enterprise/governance/).
- в CLI custom agents могут задавать специализированные роли через `tools`, `allowedTools`, `resources`, `mcpServers`, `includeMcpJson` и prompt; это уже не отдельная фаза Specs, а способ ограничить инструменты, заранее загрузить контекст и уменьшить количество permission prompts в повторяемом рабочем режиме. Источники: [Kiro CLI: Custom agents](https://kiro.dev/docs/cli/custom-agents/) и [Agent configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/).
- CLI subagents позволяют вынести focused task в изолированный контекст, запускать до четырёх subagents одновременно, строить DAG с зависимостями и возвращать summary в основной разговор. Это соседний агентский механизм Kiro, который может обслуживать сложную работу вокруг кода, но официальные источники не показывают его как обязательную часть IDE Specs workflow. Источник: [Kiro CLI: Subagents](https://kiro.dev/docs/cli/chat/subagents/).
- IDE subagents дают похожую идею изолированного контекста: Kiro может запускать встроенный context gathering subagent или general purpose subagent, а также custom subagents из `~/.kiro/agents` или `.kiro/agents`. Но для Specs есть жёсткая граница: steering files и MCP servers работают в subagents, а Specs недоступны и Hooks внутри subagents не срабатывают. Поэтому subagent нельзя автоматически считать полноценным исполнителем spec task с теми же гарантиями видимости и автоматизации, что у основного порядка Specs. Источник: [Kiro Docs: Subagents](https://kiro.dev/docs/chat/subagents/).

Для теории важно не преувеличивать автономность Kiro. Это не fully autonomous developer. Сила Kiro Specs именно в том, что агентское исполнение вставлено в последовательность человеческих approvals и файлов, которые можно читать.

## Человеческие подтверждения

Kiro Specs устроены вокруг review gates:

- подтверждение `requirements.md` перед генерацией `design.md`;
- подтверждение `design.md` перед генерацией `tasks.md`;
- подтверждение `tasks.md` перед task execution;
- решение, какие tasks считать optional, а какие входят в обязательный путь реализации;
- выбор конкретной task для выполнения;
- решения по уточнениям, если Analyze Requirements нашёл gaps, ambiguities или inconsistencies.

Источники: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/) и [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/).

Quick Plan намеренно ослабляет эти gates. Поэтому Kiro содержит не только механизм approvals, но и продуктовый выбор между полным spec workflow и быстрым планированием. Источник: [Quick Plan](https://kiro.dev/docs/specs/quick-plan/).

После перехода к реализации есть ещё один тип подтверждения: режим Supervised. Он не меняет структуру spec files, но заставляет Kiro останавливаться после ходов с файловыми изменениями и ждать решения человека по diff на уровне файлов или отдельных hunks. Это полезно для критичных кодовых баз и незнакомого кода, где одних предварительных gates недостаточно: даже правильный `tasks.md` может привести к спорным конкретным изменениям. Источник: [Autopilot](https://kiro.dev/docs/chat/autopilot/).

Если spec session использует MCP tools, появляется ещё один человеческий gate: подтверждение конкретного tool call. Kiro показывает, какой tool будет вызван и с какими параметрами; пользователь может разрешить или запретить вызов. Для часто используемых доверенных tools можно настроить `autoApprove`, но это уже сознательное ослабление остановки на каждом вызове. Elicitation requests добавляют обратный ход: внешний server может остановиться во время выполнения tool и попросить недостающие данные через форму или URL, а пользователь решает, отвечать, отклонить или закрыть запрос. Источник: [MCP Tools](https://kiro.dev/docs/mcp/usage/).

Enterprise governance добавляет gate другого типа: решение принимает не исполнитель отдельной задачи, а администратор группы до начала работы. Model governance может ограничить пользователя только approved models и назначить default model; API key governance решает, сможет ли пользователь запускать CLI automation с personal API key; web tools governance включает или выключает `web_search` и `web_fetch`; MCP governance определяет, доступны ли MCP servers вообще и берутся ли они из централизованного registry. Это не заменяет review `requirements.md`, `design.md` и `tasks.md`, но задаёт верхнюю границу того, чем агент может пользоваться во время spec work. Источники: [Model Governance](https://kiro.dev/docs/enterprise/governance/model/), [API key Governance](https://kiro.dev/docs/enterprise/governance/api-keys/), [Web Tools Governance](https://kiro.dev/docs/enterprise/governance/web-tools/) и [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/).

Monitoring and tracking добавляет ещё одно административное решение: включать ли user activity reports и prompt logging и в какой S3 bucket писать данные. Это не human gate внутри spec session, но важный policy gate вокруг процесса: prompt logging может сохранять prompts/responses и контекст inline suggestions, а значит, команда должна заранее решить, какие репозитории, данные и пользователи допустимы для такого режима наблюдаемости. Источники: [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).

## Проверка результата

Проверка в Kiro Specs распределена по нескольким местам.

На уровне требований проверяется полнота и точность поведения. Acceptance criteria в `requirements.md` дают человеку материал для ревью до дизайна. Источник: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

На уровне дизайна проверяются архитектурные решения, компоненты, интерфейсы и test strategy. Здесь риск в том, что агент может предложить технически правдоподобный, но не подходящий проекту путь; поэтому review design — обязательный gate. Источник: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

На уровне задач проверяются granularity, зависимости, expected outcomes и граница optional vs required tasks. `tasks.md` должен быть достаточно конкретным, чтобы task execution не превращался в крупное неограниченное поручение, но при этом не заставлял агента выполнять второстепенные улучшения как обязательную часть MVP. Источник: [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/).

После выполнения задач hooks могут запускать дополнительные проверки. Документация Kiro описывает hooks как автоматизацию, которая реагирует на события, включая pre и post task execution. Более точная деталь: `Pre Task Execution` срабатывает до начала spec task, когда статус меняется на `in_progress`, а `Post Task Execution` — после завершения, когда статус меняется на `completed`; примеры use cases включают подготовку окружения, проверку prerequisites, запуск tests, linting/formatting и уведомление внешних систем. В теории это можно использовать как связку specification → execution → evidence, но нужно аккуратно: сами docs не утверждают, что hooks гарантируют качество; они дают механизм автоматизации проверок. Источник: [Hooks](https://kiro.dev/docs/hooks/) и [Hook Triggers](https://kiro.dev/docs/hooks/types/).

Hooks также могут вмешиваться на уровне tools. `Pre Tool Use` и `Post Tool Use` поддерживают категории built-in tools, включая `read`, `write`, `shell`, `web`, `spec`, а также prefix filters `@mcp`, `@powers`, `@builtin` и `*` для всех tools. Для Kiro Specs это практический механизм контроля вокруг spec tools, MCP tools и Powers tools: команда может блокировать часть вызовов, добавить инструкции перед tool call или ревьюить файлы после write. Источник: [Hook Triggers](https://kiro.dev/docs/hooks/types/).

Режим Supervised добавляет проверку самих изменений, а не только результатов тестов. В этом режиме Kiro показывает правки после хода, позволяет принять или отклонить изменения по файлам, а для file modifications — по отдельным hunks. Это особенно важно для Specs, где task может быть корректно выбрана, но конкретная реализация затрагивает неожиданные места. Источник: [Autopilot](https://kiro.dev/docs/chat/autopilot/).

В CLI custom agents проверка результата может быть усилена через заранее заданные tools и permissions, но это другой тип контроля. `allowedTools` определяет, какие инструменты агент может использовать без запроса разрешения; `toolsSettings` может ограничивать операции, например через allowed paths; MCP tools можно добавлять на уровне agent configuration. Это полезно для повторяемых рабочих ролей, но одновременно расширяет поверхность риска: документация подчёркивает, что write tools работают с правами пользователя, а write-capable MCP tools требуют осторожного включения. Источник: [Agent configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/).

Отдельная линия проверки появилась в changelog 0.6 и отдельной странице `Correctness with Property-based tests`: Kiro извлекает properties из EARS-formatted requirements, определяет, какие из них можно логически тестировать, и генерирует большое число случайных cases при запуске PBT. В design phase property можно связать с исходным requirement и linked task; во время execution Kiro запускает PBT against implementation, а при сбое показывает конкретный failure scenario. Источники: [Kiro IDE changelog 0.6](https://kiro.dev/changelog/ide/0-6) и [Correctness with Property-based tests](https://kiro.dev/docs/specs/correctness/).

Ограничение PBT нужно писать явно. Документация Kiro говорит, что PBT не является formal verification и не доказывает отсутствие всех bugs; это более сильное evidence, чем одни example-based tests, особенно для edge cases и counter-examples. В интерфейсной логике Kiro PBT optional by default, чтобы пользователь мог сначала сосредоточиться на основной реализации, а затем прогнать свойства и решить, что исправлять: implementation, test или requirement. Источник: [Correctness with Property-based tests](https://kiro.dev/docs/specs/correctness/).

Enterprise monitoring даёт проверку другого уровня: не “эта task корректно реализована”, а “кто и как использовал Kiro, какие модели и клиенты участвовали, сколько сообщений и credits было потрачено, какие prompts/responses были сохранены”. Для методологии это полезно как audit/provenance layer вокруг AI-driven SDLC, но его нельзя подменять проверкой качества. Prompt logs могут помочь восстановить ход разговора и inline suggestion context, а CloudTrail/CloudWatch — отследить события AWS-аккаунта и метрики сервиса; ни один из этих источников сам по себе не подтверждает, что `requirements.md`, `design.md`, `tasks.md` и итоговый diff согласованы. Источники: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing Kiro usage on the dashboard](https://kiro.dev/docs/enterprise/monitor-and-track/dashboard) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).

## Хвост жизненного цикла

После реализации спецификация остаётся полезной как trace of intent, design rationale и список выполненных задач. Sync Files особенно важен для хвоста: он позволяет привести spec files к текущему состоянию проекта и отметить уже реализованное. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

В Requirements-First документации есть практический repair path для случая, когда требования меняются после дизайна: пользователь редактирует `requirements.md`, затем нажимает `Refine` в `design.md`, и Kiro обновляет design и tasks под новые требования. В Quick Plan похожая логика описана как частичная регенерация: изменение task меняет только задачи, изменение design перестраивает design и tasks, изменение границ запускает цепочку от requirements. Источники: [Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/) и [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/).

Checkpointing добавляет ещё один слой защиты вокруг реализации, но его нельзя считать заменой Git или spec review. В IDE каждый prompt создаёт checkpoint в chat history; Restore откатывает изменения в codebase и отбрасывает context additions после выбранной точки. Механизм работает через снимки файлов, которые Kiro менял встроенными file modification tools, и не отслеживает изменения, сделанные вручную, форматтерами, MCP tools или bash commands. Revert отличается от checkpoint тем, что откатывает только последний turn и только file changes, тогда как checkpoint может откатить несколько turns и разговорный контекст. Источник: [Kiro Docs: Checkpoints](https://kiro.dev/docs/chat/checkpoints/).

Kiro также поддерживает несколько specs в одном проекте. Это позволяет разделять крупную работу на независимые спецификации, но создаёт риск расхождения между specs, steering files и кодом. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

CLI добавляет ещё один хвост жизненного цикла: headless mode для CI/CD. Он запускается через `kiro-cli chat --no-interactive`, требует `KIRO_API_KEY`, не позволяет mid-session user input и поэтому требует заранее доверить инструменты через `--trust-all-tools` или `--trust-tools`; если pipeline зависит от MCP, можно включить `--require-mcp-startup`, чтобы быстро падать при недоступных MCP servers. Для Kiro Specs это не прямое продолжение visual spec workflow, но важный соседний путь: часть проверки, ревью PR или генерации тестов можно вынести в неинтерактивный lifecycle после реализации, если команда принимает связанные permission risks. Источник: [Kiro CLI: Headless mode](https://kiro.dev/docs/cli/headless/).

По состоянию официальных источников на 9 июня 2026 года Kiro Web нужно держать отдельно от IDE Specs. Web docs описывают preview-поверхность, где пользователь выбирает репозитории, работает интерактивно или включает Autonomous mode, агент задаёт уточняющие вопросы, строит план, использует specialized sub-agents и открывает pull request; Web может работать по нескольким репозиториям и читает `.kiro/steering/`. Отдельный блог от 18 мая 2026 года говорит, что Specs планируется принести в Kiro Web, чтобы итерировать требования и дизайн и затем передавать работу автономному агенту, но текущие Web docs не подтверждают полноценный IDE Specs workflow с `requirements.md`, `design.md`, `tasks.md` и gates в Web. Источники: [Kiro Web](https://kiro.dev/docs/web/), [Autonomous mode](https://kiro.dev/docs/web/autonomous-mode/), [Creating tasks](https://kiro.dev/docs/web/using-the-agent/creating-tasks/) и [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/).

У Web Preview есть отдельные ограничения governance и MCP. Документация по AWS IAM Identity Center говорит, что Web Preview требует Identity Center, но shared settings вроде MCP, model availability, MCP registry URL и Customer Managed Keys на Web Preview не применяются; пользовательские настройки Web хранятся отдельно, а enterprise governance features вроде model selection и web tool controls для Web Preview ещё недоступны. Страница Web MCP уточняет другую границу: MCP servers загружаются только при создании sandbox, могут быть HTTP или local, а stdio MCP servers работают вне agent tool-execution sandbox и могут читать код, secrets и environment variables. Поэтому Web MCP нельзя автоматически приравнивать к IDE/CLI MCP governance. Источники: [AWS Identity Center](https://kiro.dev/docs/web/identity-center/) и [Kiro Web: Powers and MCP](https://kiro.dev/docs/web/sandbox/mcp/).

Для будущего текста стоит показать, что Kiro Specs — это не только pre-coding planning. В зрелом использовании specs становятся частью ongoing project memory: они объясняют, почему изменение было сделано именно так, какие tasks были пройдены и как текущая реализация связана с исходным намерением.

## Сильные стороны

Главная сила Kiro — productized discipline. Многие spec-driven подходы требуют внешних scripts, discipline или ручного переноса контекста. Kiro встраивает requirements, design, tasks, task execution, steering и hooks в IDE. Для команды это снижает трение: спецификация лежит рядом с кодом и агентом. Источник: [Kiro Docs: Specs](https://kiro.dev/docs/specs/).

Вторая сильная сторона — явные gates. Требования, дизайн и задачи можно проверять до реализации. Это особенно полезно там, где ошибка в понимании дороже, чем время на review. Источник: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

Третья сильная сторона — разные режимы. Feature Specs, Bugfix Specs, Analyze Requirements и Quick Plan закрывают разные ситуации. Kiro не требует одинакового процесса для новой фичи, дефекта, анализа существующих требований и маленькой понятной задачи. Источники: [Feature Specs](https://kiro.dev/docs/specs/feature-specs/), [Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/), [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/), [Quick Plan](https://kiro.dev/docs/specs/quick-plan/).

Четвёртая сильная сторона — сочетание локального и долговременного контекста. `.kiro/specs/` хранит контекст конкретного изменения, `.kiro/steering/` — устойчивые правила проекта, `#spec` позволяет явно добавить спецификацию в чат. Источники: [Steering](https://kiro.dev/docs/steering/) и [Context](https://kiro.dev/docs/chat/context/).

Пятая сильная сторона — переносимость части контекста за пределы IDE. Kiro CLI официально использует ту же `.kiro`-конфигурацию для steering и MCP, а custom agents позволяют сделать повторяемые роли с собственными tools, resources и permission model. Это не заменяет Specs, но расширяет методологическую рамку: спецификационные файлы и project steering могут жить рядом с терминальными агентами, headless runs и специализированными ролями. Источники: [Kiro CLI blog](https://kiro.dev/blog/introducing-kiro-cli/), [Kiro CLI: Custom agents](https://kiro.dev/docs/cli/custom-agents/) и [Kiro CLI: Configuration](https://kiro.dev/docs/cli/chat/configuration/).

Шестая сильная сторона — Kiro связывает пакетное исполнение с проверками, а не только с ускорением. История `Run all Tasks` показывает, что продуктовая команда сначала отказалась от полного автозапуска задач, а затем вернула его после PBT, IDE diagnostics, dev servers, subagents и real-time visibility. Для теории это полезная деталь: автономность в Kiro подаётся как результат накопления механизмов защиты, а не как самоценная кнопка. Источник: [Run all tasks: the feature we refused to ship](https://kiro.dev/blog/run-all-tasks/).

Седьмая сильная сторона — Specs-соседние механизмы можно вписать в организационную политику. Governance не делает спецификацию качественной, но позволяет заранее сузить модельный выбор, отключить MCP, перевести MCP на registry-managed servers, запретить API key generation для CLI automation или выключить web tools. Для командного AI-driven SDLC это полезно как слой над индивидуальными approvals: ограничения не приходится заново объяснять каждому пользователю в каждой spec session. Источник: [Governance](https://kiro.dev/docs/enterprise/governance/).

## Failure modes / overuse risks

Первый риск — ложная полнота. `requirements.md`, `design.md` и `tasks.md` могут выглядеть аккуратно, даже если исходная постановка неверна. Kiro делает материал ревьюируемым, но не заменяет judgment человека. Особенно это видно в Analyze Requirements: если найденные gaps или ambiguities не разобрать, спецификация закрепит неопределённость вместо того, чтобы её снять. Источник: [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/).

Второй риск — overuse полного workflow. Для малой задачи полный проход через requirements, design и tasks может быть лишним. Quick Plan существует именно как product answer на этот риск, но выбор режима остаётся за человеком. Источник: [Quick Plan](https://kiro.dev/docs/specs/quick-plan/).

Третий риск — преждевременный Quick Plan. Если задача кажется простой, но затрагивает архитектуру, безопасность, совместимость или несколько подсистем, отказ от gates может вернуть пользователя к обычному агентскому “сделай быстро”. Это не баг Kiro, а риск неправильного выбора режима.

Четвёртый риск — спецификация отстаёт от кода. Sync Files снижает этот риск, но сам факт наличия механизма синхронизации показывает проблему: specs и реализация могут разойтись. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Пятый риск — продуктовая поверхность скрывает стоимость инженерного суждения. Встроенная IDE-поверхность делает процесс удобным, но может скрыть, что важные решения всё равно требуют инженерного чтения: acceptance criteria, design tradeoffs, task granularity, testing strategy и границы bugfix. Это особенно важно для будущего раздела: Kiro нельзя подавать как автоматическое решение проблемы specification quality.

Отдельный риск хвоста жизненного цикла связан с checkpointing. Restore может вернуть файлы и контекст к прежнему состоянию, но Kiro docs прямо ограничивают покрытие: не отслеживаются ручные правки, formatting tools, MCP tools и bash commands. Если пользователь смешивает агентские изменения с внешними правками между checkpoint и restore, откат может потерять человеческие изменения или не покрыть внешне сделанные изменения. Источник: [Kiro Docs: Checkpoints](https://kiro.dev/docs/chat/checkpoints/).

Ещё один риск — неправильный выбор входного порядка работы. Requirements-First и Design-First можно использовать в одном проекте через разные specs, но нельзя переключить уже начатую spec на другой режим. Если команда поздно понимает, что сначала нужна техническая проверка осуществимости, ей придётся создавать новую Feature Spec и переносить материал. Источник: [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/).

Шестой риск — false positives в анализе требований из-за слабой доменной модели. Если background assertions неполные или неверные, automated reasoning может показать конфликт, gap или surprising scenario там, где реальный домен уже запрещает соответствующее состояние. В `Deep Spec Analysis` это названо главным направлением дальнейшего улучшения: без хороших formal domain models требования можно формально анализировать, но часть выводов останется зависимой от качества скрытой доменной модели. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/).

Седьмой риск — потеря проектного контекста при переходе к custom agents. В обычных CLI chat sessions steering files автоматически доступны, но custom agents требуют явного добавления steering в `resources`. Если этого не сделать, специализированный агент может иметь правильные tools и permissions, но не знать командных правил, архитектурных ограничений или актуальных project conventions. Источник: [Kiro CLI: Steering](https://kiro.dev/docs/cli/steering/).

Восьмой риск — смешение permission convenience с качеством процесса. Custom agents и headless mode позволяют заранее доверять tools, MCP servers и write operations, чтобы не прерывать работу разрешениями. Это удобно для CI/CD и повторяемых ролей, но Kiro docs отдельно предупреждают, что write tools и write-capable MCP tools действуют с правами пользователя; значит, методология должна различать “меньше prompts на разрешение” и “лучше проверенный результат”. Источники: [Agent configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/) и [Headless mode](https://kiro.dev/docs/cli/headless/).

Девятый риск — ошибочно считать subagents продолжением Specs. В IDE subagents могут ускорить исследование или параллельную работу, но официальная документация прямо ограничивает их: они не имеют доступа к Specs, а Hooks в них не срабатывают. Если команда вынесет часть spec-related проверки или реализации в subagent, нужно отдельно передать ему нужные факты из `requirements.md`, `design.md` и `tasks.md` и не ожидать автоматических spec hooks. Источник: [Kiro Docs: Subagents](https://kiro.dev/docs/chat/subagents/).

Десятый риск — невидимая смена контекста через Powers. Динамическая загрузка полезна против перегрузки контекста, но при разборе результата важно понимать, какие powers активировались, какие MCP tools они добавили и какие steering instructions принесли. Иначе два похожих исполнения спецификации могут отличаться не из-за spec files, а из-за разного набора активированных powers. Источник: [Kiro Docs: Powers](https://kiro.dev/docs/powers/).

Одиннадцатый риск — слишком широкое доверие к MCP tools. MCP полезен для импорта требований, чтения документации и обращения к внешним системам во время spec work, но `autoApprove` и write-capable tools меняют границу человеческого контроля. Если команда включает auto-approval для удобства или не использует `disabledTools` для опасных операций, Specs могут выглядеть дисциплинированно на уровне `requirements.md`/`design.md`/`tasks.md`, но фактическое исполнение получит слишком широкий доступ к внешним действиям. Источники: [MCP Configuration](https://kiro.dev/docs/mcp/configuration/) и [MCP Tools](https://kiro.dev/docs/mcp/usage/).

Двенадцатый риск — преждевременно описывать Kiro Web как Specs-поверхность. Web уже добавляет автономные PR-oriented задачи, работу по нескольким репозиториям, sandbox и steering, а блог обещает перенос Specs в Web. Но до появления текущей документации по Web Specs это нужно держать как roadmap/preview-направление, а не как подтверждённый workflow IDE Specs. Источники: [Kiro Web](https://kiro.dev/docs/web/) и [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/).

Тринадцатый риск — переоценить enterprise governance как техническую гарантию. MCP governance docs прямо называют enforcement client-side; registry-managed servers синхронизируются при старте и примерно раз в сутки, а пользователь с административным доступом к машине может обойти ограничения. CLI registry при этом не запрещает personal MCP servers из `mcp.json`. Значит, governance полезен как организационный контроль и default-политика, но не заменяет локальный аудит конфигурации и ревью фактического окружения агента. Источники: [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/) и [Kiro CLI: MCP Registry](https://kiro.dev/docs/cli/mcp/registry/).

Четырнадцатый риск — смешать Web Preview controls с IDE/CLI controls. Для Kiro Web Preview shared settings из Identity Center не применяются, enterprise governance features ещё недоступны, а Web MCP server может иметь доступ к коду, secrets и environment variables вне agent tool sandbox. Это означает, что даже если IDE Specs и CLI ограничены через Kiro Profile и MCP registry, Web Preview нужно проверять отдельно. Источники: [AWS Identity Center](https://kiro.dev/docs/web/identity-center/) и [Kiro Web: Powers and MCP](https://kiro.dev/docs/web/sandbox/mcp/).

Пятнадцатый риск — принять monitoring за traceability спецификации. Dashboard, user activity reports, prompt logs, CloudTrail и CloudWatch полезны для административной видимости, расследований и FinOps, но они не строят автоматическую связь `requirement → design decision → task → diff → test evidence`. Более того, prompt logging само становится чувствительным артефактом: в logs могут попасть prompts, responses и code context для inline suggestions, поэтому включение такого режима требует отдельной политики хранения, доступа и очистки. Источники: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/), [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/) и [Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/).

## Что должно попасть в теорию

Kiro должен войти в теорию как пример того, что specification layer может стать продуктовой поверхностью SDLC. Он показывает не только “пишите спецификацию перед кодом”, а конкретную цепочку файлов и gates:

```text
feature idea
→ requirements.md
→ design.md
→ tasks.md
→ task execution
→ status / Sync Files / hooks
```

Для bugfix:

```text
bug report
→ bugfix.md
→ design.md
→ tasks.md
→ task execution
```

В будущем тексте стоит раскрыть:

- почему `prompt` слишком слаб как единственная единица управления сложной фичей;
- как Kiro превращает requirements/design/tasks в observable SDLC artifacts;
- как Kiro различает Vibe sessions и Spec sessions: быстрый разговорный режим не исчезает, но сложные задачи переводятся в формальный spec session с отслеживанием прогресса;
- как review gates удерживают человека в loop;
- почему Analyze Requirements нужно описывать не как “LLM перечитал требования”, а как связку refinement, auto-formalization и logical analysis с человеческими two-option questions;
- почему Quick Plan важен как защита от бюрократизации spec workflow;
- почему parallel task execution превращает `tasks.md` в dependency-aware execution plan, а не только список дел;
- как режимы Autopilot и Supervised добавляют слой контроля над фактическими файловыми изменениями после spec gates;
- почему IDE subagents нельзя описывать как полноценный spec executor: Specs недоступны subagents, а Hooks в них не срабатывают;
- как Powers добавляют динамически подключаемый контекст и MCP tools, но остаются соседним механизмом Kiro, а не частью основной цепочки `requirements.md` → `design.md` → `tasks.md`;
- как MCP становится внешним инструментальным слоем вокруг Specs: импорт требований и дизайна, prompt/resource templates, подтверждение tool calls, `autoApprove`, `disabledTools` и elicitation requests;
- как enterprise governance ограничивает доступные модели, MCP servers, API keys и web tools до начала spec session, но остаётся организационным и client-side контролем, а не доказательством качества результата;
- как enterprise monitoring добавляет административную наблюдаемость вокруг IDE/CLI, но не заменяет traceability самой спецификации;
- почему Web/autonomous mode нужно описывать как соседнюю и развивающуюся поверхность Kiro: она использует steering и PR lifecycle, но официальная Web-документация пока не доказывает тот же IDE Specs workflow;
- как `.kiro/steering/`, `#spec`, hooks и Sync Files расширяют spec beyond one chat session;
- как CLI, custom agents, MCP configuration и headless mode расширяют Kiro за пределы IDE, но не должны описываться как тот же самый Specs workflow без отдельного подтверждения;
- где Kiro остаётся зависимым от человеческого judgment.

## Что лучше уйдёт в Handbook / Fieldbook

В Handbook / Fieldbook лучше вынести практические правила выбора режима:

- когда использовать полный Feature Spec;
- когда оставаться в Vibe session, а когда переходить в Spec session через `Generate spec`;
- когда Bugfix Spec лучше обычного bug prompt;
- когда достаточно Quick Plan;
- как читать `requirements.md` перед подтверждением;
- что проверять в `design.md`;
- как оценивать granularity задач в `tasks.md`;
- как читать findings Analyze Requirements: ambiguity, conflict, completeness, accepted-scenario и rejected-scenario questions;
- когда не доверять формальному finding без проверки доменной предпосылки;
- как использовать parallel `Run all Tasks`, если задачи независимы, и когда лучше запускать их по одной;
- когда запускать Sync Files;
- какие hooks стоит привязать к spec task execution;
- как поддерживать `.kiro/steering/`, чтобы она не стала устаревшим мусором.
- когда запускать spec task в режиме Autopilot, а когда включать Supervised и принимать hunks вручную;
- как использовать subagents для исследования вокруг spec, не предполагая, что им доступны Specs и Hooks;
- как проверять, какие Powers активировались и какие MCP tools или steering instructions они добавили к работе;
- какие MCP servers и tools разрешены в spec session, какие tools надо добавить в `disabledTools`, а какие допустимо включить в `autoApprove`;
- как реагировать на MCP elicitation requests и какие данные нельзя отдавать внешнему server;
- как проверять Kiro Profile shared settings: model allow list, MCP on/off, MCP registry URL, API key generation и web tools;
- как настраивать monitoring/tracking: кто имеет доступ к usage dashboard, user activity reports и prompt logs, в какой S3 bucket пишутся данные и какие retention/access rules применяются;
- как читать MCP registry как allow list: какие servers управляются централизованно, какие personal servers всё ещё загружаются из `mcp.json`, какие overrides допустимы локально;
- как отдельно проверять Kiro Web Preview: какие настройки Identity Center реально применяются, какие governance controls не действуют и какие MCP servers попадают в sandbox;
- как создавать CLI custom agents так, чтобы они явно получали нужные steering files через `resources`;
- когда для headless mode допустимы `--trust-tools` или `--trust-all-tools`, а когда требуется более узкая permission model;
- как проверять MCP configuration priority: Agent > Project > Global для MCP servers и Project > Global для steering.

Туда же можно вынести чек-лист ревью:

- требования содержат проверяемые acceptance criteria;
- design явно говорит о компонентах, интерфейсах, данных, ошибках и тестах;
- tasks достаточно малы и упорядочены;
- Quick Plan не используется для задачи с высокой неопределённостью;
- после реализации spec синхронизирован с фактическим состоянием проекта.

## Источники

- [Kiro Docs: Specs](https://kiro.dev/docs/specs/) — главный вход в официальную документацию Specs; нужен для общей модели requirements/design/tasks и назначения Specs.
- [Kiro Docs: Feature Specs](https://kiro.dev/docs/specs/feature-specs/) — основной источник по `requirements.md`, `design.md`, `tasks.md`, review gates и task execution.
- [Kiro Docs: Requirements-First Workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/) — источник по стандартному ходу от user stories и EARS acceptance criteria к design и tasks.
- [Kiro Docs: Design-First Workflow](https://kiro.dev/docs/specs/feature-specs/tech-design-first/) — источник по варианту, где первым артефактом становится `design.md`, а requirements выводятся после подтверждения технического дизайна.
- [Kiro Docs: Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/) — источник по `bugfix.md` и bugfix-ветке workflow.
- [Kiro Docs: Quick Plan](https://kiro.dev/docs/specs/quick-plan/) — источник по укороченному режиму и снятию части review overhead.
- [Kiro Docs: Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/) — источник по предварительному анализу существующих требований и поиску gaps, ambiguities, inconsistencies.
- [Kiro Docs: Correctness with Property-based tests](https://kiro.dev/docs/specs/correctness/) — источник по извлечению properties из EARS requirements, связи property с requirement/task, запуску PBT during execution и обработке failure scenarios.
- [Kiro Docs: Specs Best Practices](https://kiro.dev/docs/specs/best-practices/) — источник по Sync Files, multiple specs и сопровождению спецификаций.
- [Kiro Docs: Steering](https://kiro.dev/docs/steering/) — источник по `.kiro/steering/` как долговременному проектному контексту.
- [Kiro Docs: Vibe vs Spec sessions](https://kiro.dev/docs/chat/vibe/) — источник по различению быстрых Vibe sessions и формальных Spec sessions, включая выбор через session picker и `Generate spec`.
- [Kiro Docs: Context](https://kiro.dev/docs/chat/context/) — источник по chat context providers, включая `#spec`.
- [Kiro Docs: Chat](https://kiro.dev/docs/chat/) — актуальный источник по context providers, включая синтаксис `#spec:user-authentication`, `#steering`, `#terminal`, `#repository` и другие поставщики контекста.
- [Kiro Docs: Checkpoints](https://kiro.dev/docs/chat/checkpoints/) — источник по checkpointing, Restore, Revert и ограничениям покрытия внешних изменений.
- [Kiro Docs: Autopilot](https://kiro.dev/docs/chat/autopilot/) — источник по режимам Autopilot/Supervised, ревью на уровне hunks и применимости Supervised в spec chat sessions.
- [Kiro Docs: Subagents](https://kiro.dev/docs/chat/subagents/) — источник по IDE subagents, custom subagents и ограничению: subagents не имеют доступа к Specs, а Hooks в них не срабатывают.
- [Kiro Docs: Hooks](https://kiro.dev/docs/hooks/) и [Hook Triggers](https://kiro.dev/docs/hooks/types/) — источники по автоматизации вокруг IDE events и task execution.
- [Kiro Docs: MCP](https://kiro.dev/docs/mcp/) — источник по MCP как расширению Kiro внешними tools, prompts и resources.
- [Kiro Docs: MCP Configuration](https://kiro.dev/docs/mcp/configuration/) — источник по `.kiro/settings/mcp.json`, `~/.kiro/settings/mcp.json`, workspace priority, `autoApprove` и `disabledTools`.
- [Kiro Docs: MCP Tools](https://kiro.dev/docs/mcp/usage/) — источник по запросам подтверждения, explicit tool calls, `#` mention list, prompts/resource templates и elicitation requests.
- [Kiro Docs: Powers](https://kiro.dev/docs/powers/) — источник по динамической загрузке MCP, `POWER.md`, MCP configuration и steering/hooks внутри power.
- [Kiro Docs: Create powers](https://kiro.dev/docs/powers/create/) — источник по структуре power directory, `POWER.md`, `mcp.json`, `steering/`, локальному тестированию и публикации.
- [Kiro Docs: Install powers](https://kiro.dev/docs/powers/installation/) — источник по установке powers и регистрации MCP server в `~/.kiro/settings/mcp.json`.
- [Your first project](https://kiro.dev/docs/getting-started/first-project/) — официальный getting started walkthrough; нужен для конкретного примера генерации steering docs из файлов проекта и spec task execution в demo-приложении.
- [Kiro home page transcript](https://kiro.dev/) — официальный transcript демонстрации spec execution; нужен для видимых UI states `Start task`, `Task in progress`, `Task completed`, checkbox, `View changes`, `View execution` и status card.
- [Introducing Kiro](https://kiro.dev/blog/introducing-kiro/) — продуктовый источник по позиционированию Kiro против ограничений vibe coding и по идее spec-driven development inside IDE.
- [Bring Kiro agents to your terminal with Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/) — официальный блог-пост о CLI как terminal surface, который использует `.kiro` configuration, steering и MCP наряду с IDE.
- [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/) — официальный блог-пост от 12 мая 2026 про parallel task execution, Quick Plan refinement loop и Analyze Requirements как Neurosymbolic AI.
- [Run all tasks: the feature we refused to ship](https://kiro.dev/blog/run-all-tasks/) — официальный блог-пост про историю `Run all Tasks`, причину первоначального отказа от кнопки, required tasks и механизмы защиты перед пакетным запуском.
- [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/) — официальный технический блог-пост от 12 мая 2026 про requirement bugs, три стадии requirements analysis, SMT-lib formalization, semantic entropy, accepted/rejected scenarios и ограничения доменной модели.
- [Kiro IDE changelog](https://kiro.dev/changelog/ide/) — источник по истории появления Quick Plan, Analyze Requirements, parallel task execution, `#spec` context provider и другим изменениям IDE.
- [Kiro IDE changelog 0.6](https://kiro.dev/changelog/ide/0-6) — источник по property-based testing, checkpointing, Kiro CLI, настройкам context providers и line ranges для file context.
- [Kiro CLI: Quick start](https://kiro.dev/docs/cli/quick-start/) — источник по базовой terminal-сессии, headless примером и `--print` для scripting; полезен как вход в CLI-поверхность, но не как источник по Specs gates.
- [Kiro CLI: Steering](https://kiro.dev/docs/cli/steering/) — источник по steering в CLI и важной оговорке, что custom agents не получают steering автоматически без `resources`.
- [Kiro CLI: Custom agents](https://kiro.dev/docs/cli/custom-agents/) — источник по `.kiro/agents/`, специализированным ролям, tools, resources и agent-level MCP.
- [Kiro CLI: Agent configuration reference](https://kiro.dev/docs/cli/custom-agents/configuration-reference/) — источник по `allowedTools`, `toolsSettings`, `mcpServers`, `includeMcpJson`, resources и приоритету конфигурации.
- [Kiro CLI: MCP](https://kiro.dev/docs/cli/mcp/) — источник по `.kiro/settings/mcp.json`, `~/.kiro/settings/mcp.json`, authentication и доступу CLI agents к external tools.
- [Kiro CLI: Configuration](https://kiro.dev/docs/cli/chat/configuration/) — источник по priority Project > Global для steering и Agent > Project > Global для MCP servers.
- [Kiro CLI: Subagents](https://kiro.dev/docs/cli/chat/subagents/) — источник по изолированному контексту subagents, максимум четырём параллельным subagents и DAG dependencies.
- [Kiro CLI: Headless mode](https://kiro.dev/docs/cli/headless/) — источник по `--no-interactive`, `KIRO_API_KEY`, `--trust-tools`, `--trust-all-tools` и `--require-mcp-startup` для CI/CD.
- [Kiro Docs: Web](https://kiro.dev/docs/web/) — источник по preview-поверхности Kiro Web, репозиториям, interactive/autonomous modes, sandbox и steering.
- [Kiro Docs: Web Autonomous mode](https://kiro.dev/docs/web/autonomous-mode/) — источник по autonomous loop: уточняющие вопросы, план, specialized sub-agents, tests и pull request.
- [Kiro Docs: Web Creating tasks](https://kiro.dev/docs/web/using-the-agent/creating-tasks/) — источник по созданию tasks в Kiro Web и кнопке `Start task`.
- [Kiro Web: AWS Identity Center](https://kiro.dev/docs/web/identity-center/) — источник по настройке Web Preview через Identity Center и ограничениям shared settings/governance для Web Preview.
- [Kiro Web: Powers and MCP](https://kiro.dev/docs/web/sandbox/mcp/) — источник по MCP внутри Web sandbox, загрузке HTTP/local servers при создании sandbox и границам доступа stdio MCP servers.
- [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/) — официальный блог от 18 мая 2026 года; нужен как roadmap-свидетельство, что Specs планируют перенести в Kiro Web, но не как доказательство текущего Web Specs workflow.
- [Kiro Docs: Governance](https://kiro.dev/docs/enterprise/governance/) — источник по Kiro Profile shared settings и enterprise policy surface для моделей, MCP, API keys и web tools.
- [Kiro Docs: Model Governance](https://kiro.dev/docs/enterprise/governance/model/) — источник по model access management, allow list и default model.
- [Kiro Docs: MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/) — источник по MCP on/off, MCP registry URL, sync behavior и client-side enforcement.
- [Kiro CLI: MCP Registry](https://kiro.dev/docs/cli/mcp/registry/) — источник по registry-managed MCP servers в CLI, personal MCP servers и local overrides.
- [Kiro Docs: API key Governance](https://kiro.dev/docs/enterprise/governance/api-keys/) — источник по запрету или разрешению API key generation для CLI automation.
- [Kiro Docs: Web Tools Governance](https://kiro.dev/docs/enterprise/governance/web-tools/) — источник по централизованному включению/выключению `web_search` и `web_fetch`.
- [Kiro Docs: Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/) — источник по CloudTrail, CloudWatch, CloudWatch Logs, user activity reports и prompt logs как административной наблюдаемости вокруг Kiro.
- [Kiro Docs: Usage dashboard](https://kiro.dev/docs/enterprise/monitor-and-track/dashboard) — источник по dashboard агрегированных метрик usage, client type, subscription tier, credits, active users и language filters.
- [Kiro Docs: Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) — источник по daily CSV reports в S3, client type, model-name message counts, credits и ограничениям старых code generation metrics.
- [Kiro Docs: Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/) — источник по prompt logs в S3 для inline suggestions и IDE chat conversations.
- [Kiro Docs: Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/) — источник по хранению questions/responses/context, telemetry/content collection и границам enterprise data handling.
- `work/specification-cluster-deep-plan.md` — внутренний план, где Kiro назначен как productized IDE surface для Part V.
- `work/approved-ai-sdlc-plan.md` — внутренний утверждённый план, где Kiro Specs перечислены среди глубоких соседних спецификационных режимов.

## Поисковые формулировки

Использованы в проходе 01:

- `Kiro specs documentation feature specs requirements design tasks`
- `Kiro documentation specs steering hooks requirements design tasks`
- `Kiro docs spec driven development specs requirements design tasks`
- `site:kiro.dev/docs/specs bugfix specs bugfix.md Kiro current expected unchanged behavior`
- `site:kiro.dev/docs/specs quick plan approval gates Kiro requirements.md design.md tasks.md`
- `site:kiro.dev/docs/specs analyze requirements inconsistencies ambiguities Kiro`
- `site:kiro.dev/docs/steering/ Kiro steering .kiro/steering`
- `site:kiro.dev/docs/hooks Kiro hooks agent hooks triggers task execution`
- `site:kiro.dev/docs "Sync Files" "#spec" Kiro specs`
- `site:kiro.dev/docs/chat/context Kiro #spec`

Поисковые углы для следующих проходов:

- `Kiro changelog specs sync files task status`
- `Kiro deep spec analysis blog requirements design tasks`
- `Kiro agent hooks spec task execution examples`
- `Kiro steering files product.md tech.md structure.md`
- `Kiro specs collaboration review gates`
- `Kiro specs limitations quick plan overuse`

Использованы в проходе 02:

- `Kiro Deep Spec Analysis Kiro blog`
- `site:kiro.dev/blog Kiro "Specs just got faster" "parallel task execution"`
- `site:kiro.dev/docs/chat/context "#spec" Kiro context providers`
- `site:kiro.dev/changelog/ide "Spec correctness" "property-based tests" Kiro`
- `site:kiro.dev/docs/steering "AGENTS.md" "file references"`
- `site:kiro.dev/docs/specs/correctness "Property-based tests" "EARS" Kiro`
- `site:kiro.dev/docs/specs/feature-specs/requirements-first "Optional vs required tasks" Kiro`

Поисковые углы, которые ещё имеют смысл:

- `site:kiro.dev/docs/cli Kiro CLI specs steering files`
- `site:kiro.dev/docs/specs "MVP tasks" optional tasks Kiro`
- `site:kiro.dev/showcase Kiro specs demo screenshots review gates`
- `site:kiro.dev/changelog/ide "checkpointing" "spec chat" Kiro`

Использованы в проходе 03:

- `site:kiro.dev/docs/cli Kiro CLI specs steering files`
- `site:kiro.dev/docs Kiro CLI MCP custom agents steering specs`
- `site:kiro.dev/changelog/ide "checkpointing" "spec chat" Kiro`
- `site:kiro.dev/showcase Kiro specs demo screenshots review gates`
- `Kiro showcase specs review gates task execution Sync Files`
- `Kiro home page transcript spec task in progress task completed View changes View execution`
- `site:kiro.dev/docs/cli custom agents resources steering includeMcpJson allowedTools`
- `site:kiro.dev/docs/cli subagents DAG dependencies isolated context Kiro`
- `site:kiro.dev/docs/cli headless trust-tools require-mcp-startup Kiro`

Поисковые углы, которые ещё имеют смысл после прохода 03:

- `site:kiro.dev/docs/specs "Sync Files" "completed" "in-progress" Kiro`
- `site:kiro.dev/changelog/ide "Sync Files" "Task completed" Kiro`
- `site:kiro.dev/docs/specs "checkpoint" "View execution" Kiro`
- `site:kiro.dev/docs/cli specs "requirements.md" "tasks.md" Kiro`

Использованы в проходе 04:

- `site:kiro.dev/docs/specs "Sync Files" "completed" "in-progress" Kiro`
- `site:kiro.dev/changelog/ide "Sync Files" "Task completed" Kiro`
- `site:kiro.dev/docs/specs "checkpoint" "View execution" Kiro`
- `site:kiro.dev/docs/cli specs "requirements.md" "tasks.md" Kiro`
- `Kiro docs checkpoints revert changes checkpointing`
- `site:kiro.dev/docs "Checkpoints" "Revert" "Kiro"`
- `Kiro "Run all Tasks" "Agent Coordination and Steering"`
- `site:kiro.dev/blog "Run all Tasks" "Kiro"`
- `site:kiro.dev/docs/getting-started "first project" "Generate Steering"`
- `site:kiro.dev/docs/getting-started "spec" "requirements" "design" "tasks" "Kiro"`

Поисковые углы после прохода 04, если нужен ещё один официальный pass:

- `site:kiro.dev/docs/specs "import" "JIRA" "Confluence" "GitHub issues" Kiro`
- `site:kiro.dev/docs/specs "cannot switch" "Requirements-First" "Design-First" Kiro`
- `site:kiro.dev/docs "Run all Tasks" "required" "optional" Kiro`
- `site:kiro.dev/docs/chat/checkpoints MCP bash formatter Restore Kiro`

Использованы в проходе 05:

- `site:kiro.dev/docs/chat/subagents Kiro subagents specs hooks not supported`
- `site:kiro.dev/docs/powers Kiro Powers MCP steering hooks project rules`
- `site:kiro.dev/changelog/ide Kiro Powers specs hooks subagents`
- `site:kiro.dev/docs/chat/subagents "Specs" "hooks"`
- `site:kiro.dev/docs/specs "Spec mode" "tools" Kiro`
- `site:kiro.dev/docs/specs "supervised mode" "spec chat" Kiro`
- `site:kiro.dev/docs/specs "approval gates" "Task" "Kiro"`

Использованы в проходе 06:

- `site:kiro.dev/docs/specs "MCP" "Specs" Kiro`
- `site:kiro.dev/docs/specs "vibe" "spec" Kiro`
- `site:kiro.dev/docs "Spec Mode" "Kiro" "tools"`
- `site:kiro.dev/docs/specs "Auto" "requirements.md" "design.md" "tasks.md" Kiro`
- `site:kiro.dev/docs/web specs Kiro`
- `site:kiro.dev/docs/web "spec" "Kiro Web"`
- `site:kiro.dev/docs "Kiro Web" "specs" "pull requests"`
- `site:kiro.dev/docs/specs/import Kiro import requirements design MCP PRD JIRA Confluence GitHub issues`
- `site:kiro.dev/docs/specs "Import" "JIRA" "Confluence" "GitHub issues"`
- `site:kiro.dev/docs/specs/feature-specs/requirements-first "MCP" "JIRA" "Confluence"`
- `site:kiro.dev/docs/getting-started "Generate Steering" "Spec" "Kiro"`
- `site:kiro.dev/docs/getting-started "Create Spec" "requirements" "design"`
- `site:kiro.dev/docs/web Kiro Web specs documentation June 2026`
- `site:kiro.dev/docs/web "Specs" "Kiro Web"`
- `site:kiro.dev/changelog "Kiro Web" "specs" "June"`

Использованы в проходе 07:

- `site:kiro.dev/docs/enterprise/governance Kiro model governance MCP registry API keys web tools`
- `site:kiro.dev/docs/enterprise/governance/model Kiro model allow list default model`
- `site:kiro.dev/docs/enterprise/governance/mcp Kiro MCP registry client-side enforcement`
- `site:kiro.dev/docs/cli/mcp/registry Kiro MCP registry personal servers overrides`
- `site:kiro.dev/docs/enterprise/governance/api-keys Kiro CLI API key generation governance`
- `site:kiro.dev/docs/enterprise/governance/web-tools Kiro web_search web_fetch governance`
- `site:kiro.dev/docs/web/identity-center Kiro Web Preview shared settings governance limitations`
- `site:kiro.dev/docs/web/sandbox/mcp Kiro Web MCP sandbox HTTP local stdio secrets environment variables`

Использованы в проходе 08:

- `site:kiro.dev/docs/enterprise audit logs Kiro governance activity logs`
- `site:kiro.dev/docs/enterprise Kiro audit logs admin activity`
- `site:kiro.dev/docs/specs Kiro specs audit logs View execution`
- `site:kiro.dev/changelog/ide Kiro specs June 2026`
- `site:kiro.dev/docs/enterprise/monitor-and-track Kiro prompt logging usage dashboard`
- `site:kiro.dev/docs/enterprise/monitor-and-track Kiro prompts logs S3`
- `site:kiro.dev/docs/enterprise/security Kiro encryption at rest customer managed key`
- `site:kiro.dev/docs/enterprise Kiro data privacy training prompts`
- `site:kiro.dev/docs/enterprise/monitor-and-track/user-activity "Viewing per-user activity" Kiro`
- `site:kiro.dev/docs/enterprise/monitor-and-track/dashboard "Viewing Kiro usage on the dashboard"`
- `site:kiro.dev/docs/enterprise/monitor-and-track/prompt-logging "Prompt log examples" Kiro`

## Кандидаты на иллюстрации

- Схема `requirements.md → design.md → tasks.md → task execution`. Источник: Kiro Docs Feature Specs. Назначение: показать staged SDLC внутри IDE. Статус: кандидат, лучше перерисовать как собственную схему.
- Разветвление `Feature Spec` vs `Bugfix Spec`: `requirements.md` или `bugfix.md` сходятся в `design.md` и `tasks.md`. Источник: Feature Specs и Bugfix Specs. Назначение: показать, что Kiro различает типы изменений. Статус: кандидат, лучше перерисовать.
- Диаграмма контекста: `.kiro/specs/`, `.kiro/steering/`, `#spec`, hooks, Sync Files. Источники: Specs, Steering, Context, Hooks, Best Practices. Назначение: показать, где живёт контекст и как он возвращается в исполнение. Статус: кандидат.
- Сравнительная мини-лента gates vs Quick Plan. Источник: Feature Specs и Quick Plan. Назначение: показать, что Kiro содержит и полный рабочий процесс, и быстрый путь. Статус: кандидат.
- Диаграмма parallel task execution waves: dependency graph, setup-first, concurrent waves, tests-after-code, failed task does not stop independent tasks. Источник: [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/). Назначение: показать, что `tasks.md` может стать планом параллельного исполнения, а не только списком. Статус: официальный image-кандидат, лучше перерисовать.
- Диаграмма requirements analysis pipeline: refinement → auto-formalization → logical analysis → two-option questions → rewritten `requirements.md`. Источник: [Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/). Назначение: показать, где автоматическая проверка заканчивается и где человек выбирает смысл. Статус: официальный image-кандидат, лучше перерисовать.
- Диаграмма property-based testing workflow: EARS requirement → extracted property → linked task → generated cases → failure scenario → fix implementation/test/requirement. Источник: [Correctness with Property-based tests](https://kiro.dev/docs/specs/correctness/). Назначение: показать, как spec становится проверяемым поведением, но не превращается в формальную гарантию. Статус: официальный image-кандидат, лучше перерисовать.
- Мини-скрин или перерисованная sequence strip из официального homepage transcript: `Start task → Task in progress → Task completed → View changes / View execution`. Источник: [Kiro home page transcript](https://kiro.dev/). Назначение: показать видимый task status как часть productized delegation. Статус: кандидат, лучше перерисовать; transcript полезнее как фактическое подтверждение UI states, чем как готовый ассет.
- Диаграмма CLI context bridge: `.kiro/steering/` и MCP используются IDE и CLI, но custom agents требуют явных `resources`; subagents имеют isolated context; headless mode требует заранее доверенных tools. Источники: [Kiro CLI blog](https://kiro.dev/blog/introducing-kiro-cli/), [Kiro CLI: Steering](https://kiro.dev/docs/cli/steering/), [Custom agents](https://kiro.dev/docs/cli/custom-agents/) и [Headless mode](https://kiro.dev/docs/cli/headless/). Назначение: показать, что Kiro-методология расширяется за пределы Specs UI, но с другими контрактами контекста и безопасности. Статус: кандидат для Handbook/Fieldbook, не для основного сравнения Specs.
- Диаграмма защитного стека для `Run all Tasks`: spec validation → required tasks only → dependency graph → PBT/dev servers/LSP diagnostics/subagents → real-time visibility. Источник: [Run all tasks](https://kiro.dev/blog/run-all-tasks/) и [Specs Best Practices](https://kiro.dev/docs/specs/best-practices/). Назначение: показать, что пакетное исполнение в Kiro опирается на дополнительные проверки и ограничения. Статус: кандидат, лучше перерисовать.
- Мини-схема покрытия checkpoint: prompt checkpoint → Restore/Revert → покрываются built-in file modifications; не покрываются manual changes, formatting tools, MCP tools, bash commands. Источник: [Checkpoints](https://kiro.dev/docs/chat/checkpoints/). Назначение: показать защитный механизм и его границы. Статус: кандидат для Handbook/Fieldbook.
- Мини-схема контроля исполнения: spec gates → task execution → Autopilot/Supervised toggle → подтверждение на уровне файлов или hunks → Revert/checkpoint. Источник: [Autopilot](https://kiro.dev/docs/chat/autopilot/). Назначение: показать, что контроль человека продолжается после утверждения `tasks.md`. Статус: кандидат для Handbook/Fieldbook.
- Схема границ subagents: основной Specs workflow имеет Specs/Hooks, subagents имеют steering и MCP, но не имеют Specs и не запускают Hooks. Источник: [Subagents](https://kiro.dev/docs/chat/subagents/). Назначение: не дать будущему тексту ошибочно описать subagents как полноценное окружение spec execution. Статус: кандидат.
- Схема Powers как динамически подключаемого контекстного слоя: ключевые слова запроса → активированный power → `POWER.md` + MCP + steering/hooks → исполнение агентом. Источник: [Powers](https://kiro.dev/docs/powers/). Назначение: показать, как Kiro снижает MCP context overload рядом со Specs. Статус: кандидат, не для основной схемы Specs.
- Мини-схема выбора режима: Vibe session для быстрого разговора и исследования → `Generate spec` / session picker → Spec session для формального плана, последовательного исполнения и отслеживания прогресса. Источник: [Vibe vs Spec sessions](https://kiro.dev/docs/chat/vibe/). Назначение: показать, что Kiro не бюрократизирует все задачи, а предлагает переключатель режима. Статус: кандидат.
- Схема IDE MCP вокруг Specs: внешние системы / prompts / resource templates → `#` mention или explicit `#[server] tool` → approval/elicitation → вход спецификации или task execution. Источники: [MCP](https://kiro.dev/docs/mcp/) и [MCP Tools](https://kiro.dev/docs/mcp/usage/). Назначение: показать внешний контекст и человеческие подтверждения tool calls. Статус: кандидат для Handbook/Fieldbook.
- Схема hook/tool control: spec task status `in_progress`/`completed` → pre/post task hooks; tool categories `spec`, `@mcp`, `@powers`, `write`, `shell` → pre/post tool hooks. Источник: [Hook Triggers](https://kiro.dev/docs/hooks/types/). Назначение: показать, как проверки и ограничения можно привязать к spec execution и tools. Статус: кандидат.
- Схема разведения IDE Specs и Kiro Web: IDE Specs имеют `requirements.md`/`design.md`/`tasks.md` и gates; Web preview имеет autonomous PR loop, sandbox и steering; блог от 18 мая 2026 обещает перенос Specs в Web. Источники: [Kiro Web](https://kiro.dev/docs/web/) и [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/). Назначение: не дать будущему тексту преждевременно склеить текущий IDE workflow и Web roadmap. Статус: кандидат для открытых вопросов/сравнительной схемы.
- Схема enterprise governance вокруг Specs: Kiro Profile shared settings → model allow list/default model, MCP on/off/registry URL, API key generation, web tools → IDE/CLI spec work. Источники: [Governance](https://kiro.dev/docs/enterprise/governance/), [Model Governance](https://kiro.dev/docs/enterprise/governance/model/), [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/), [API key Governance](https://kiro.dev/docs/enterprise/governance/api-keys/) и [Web Tools Governance](https://kiro.dev/docs/enterprise/governance/web-tools/). Назначение: показать, что часть контроля над agentic SDLC находится выше конкретной spec session. Статус: кандидат для Handbook/Fieldbook.
- Мини-схема границ MCP registry: registry-managed servers синхронизируются централизованно, personal MCP servers из `mcp.json` могут сосуществовать, local overrides задают env/headers/timeout, enforcement client-side. Источники: [MCP Governance](https://kiro.dev/docs/enterprise/governance/mcp/) и [Kiro CLI: MCP Registry](https://kiro.dev/docs/cli/mcp/registry/). Назначение: не дать будущему тексту описать registry как абсолютный technical sandbox. Статус: кандидат для раздела рисков.
- Схема разведения Web governance и IDE/CLI governance: Identity Center включает доступ к Web Preview, но shared settings/governance не применяются к Web; Web MCP загружается в sandbox, поддерживает HTTP/local servers, а stdio servers имеют доступ вне tool sandbox. Источники: [AWS Identity Center](https://kiro.dev/docs/web/identity-center/) и [Kiro Web: Powers and MCP](https://kiro.dev/docs/web/sandbox/mcp/). Назначение: показать, почему Web Preview требует отдельной проверки policy surface. Статус: кандидат для открытых вопросов/Fieldbook.
- Схема monitoring/provenance вокруг Specs: IDE/CLI spec work → usage dashboard / user activity CSV / prompt logs in S3 / CloudTrail / CloudWatch; рядом отдельная стрелка “не заменяет requirement-task-diff-test traceability”. Источники: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/). Назначение: показать, что административная наблюдаемость и методологическая трассировка Specs — разные слои. Статус: кандидат для Handbook/Fieldbook.

## Открытые вопросы

- Закрыто в проходе 02: default foundational steering files в текущей документации названы как `product.md`, `tech.md` и `structure.md`; они включаются в каждое взаимодействие по умолчанию. Источник: [Steering](https://kiro.dev/docs/steering/).
- Закрыто в проходе 02: `Deep Spec Analysis` прочитан и использован для деталей refinement, auto-formalization, logical analysis, semantic entropy, five finding types и ограничения доменной модели.
- Закрыто в проходе 02: `#spec` может ссылаться на конкретную спецификацию в форме `#spec:user-authentication` и включает requirements, design и tasks. Источник: [Chat](https://kiro.dev/docs/chat/).
- Частично закрыто в проходе 03: task execution statuses видны как `in-progress` и `completed` в Specs docs, а официальный homepage transcript показывает `Start task`, `Task in progress`, `Task completed`, checkbox, `View changes`, `View execution` и status card. Остаётся неизвестным, записываются ли эти статусы прямо в `tasks.md` или хранятся отдельно в metadata IDE.
- Частично закрыто в проходе 03: официальный demo/transcript для task execution найден на главной странице Kiro, но отдельного официального материала, где одновременно хорошо видны review gates и Sync Files, пока нет. Иллюстрации лучше перерисовывать.
- Частично закрыто в проходе 02: официальные image-кандидаты найдены для parallel task execution, Quick Plan, requirements analysis и PBT, но их лучше перерисовывать и отдельно проверять права.
- Частично закрыто в проходе 03: Kiro CLI проверен по официальным docs и blog. CLI использует `.kiro` configuration, steering и MCP, поддерживает custom agents, subagents и headless mode, но найденные источники не доказывают, что CLI полностью повторяет IDE Specs workflow с review gates. Для теории это нужно описывать как соседнюю поверхность Kiro, а не как прямую замену Specs UI.
- Частично закрыто в проходе 04: Sync Files уточнён по best practices как способ отметить уже реализованные tasks и привести spec files к текущему состоянию. Остаётся неизвестным, где именно технически хранится task status: прямо в `tasks.md` или в metadata IDE.
- Частично закрыто в проходе 04: `Run all Tasks` уточнён как пакетный запуск только для незавершённых required tasks и как продуктовый компромисс после добавления механизмов защиты. Остаётся проверить, есть ли отдельная текущая docs-страница, где этот режим описан не только в blog/best practices.
- Частично закрыто в проходе 04: checkpointing добавлен как слой защиты, но с явным ограничением: Restore/Revert не покрывают manual changes, formatting tools, MCP tools и bash commands.
- Поиск прохода 04 не нашёл официального подтверждения, что CLI умеет полноценно запускать или редактировать IDE Specs workflow с gates, `Sync Files` и task execution из терминала. До появления такого источника CLI нужно оставлять соседней поверхностью Kiro, а не заменой Specs UI.
- Закрыто в проходе 05: для IDE subagents найдено официальное ограничение — steering files и MCP servers работают, но subagents не имеют доступа к Specs, а Hooks в них не срабатывают. Источник: [Subagents](https://kiro.dev/docs/chat/subagents/).
- Закрыто в проходе 05: режим Supervised работает в spec chat sessions и даёт подтверждение на уровне файлов или hunks после ходов с файловыми изменениями. Источник: [Autopilot](https://kiro.dev/docs/chat/autopilot/).
- Частично закрыто в проходе 05: Powers уточнены как динамически подключаемая упаковка `POWER.md`, MCP configuration и steering/hooks. Остаётся не использовать Powers как доказательство возможностей Specs: найденные источники показывают контекстный и инструментальный слой IDE, но не отдельный Specs workflow.
- Закрыто в проходе 06: различие Vibe sessions и Spec sessions найдено в официальной документации. Для Kiro Specs это важно как граница применения: быстрый разговорный режим сохраняется, а сложная работа переводится в Spec session через session picker или `Generate spec`. Источник: [Vibe vs Spec sessions](https://kiro.dev/docs/chat/vibe/).
- Закрыто в проходе 06: IDE MCP уточнён как отдельный контекстно-инструментальный слой вокруг Specs: workspace/user config, tools/prompts/resources, `autoApprove`, `disabledTools`, подтверждение tool calls и elicitation requests. Источники: [MCP Configuration](https://kiro.dev/docs/mcp/configuration/) и [MCP Tools](https://kiro.dev/docs/mcp/usage/).
- Частично закрыто в проходе 06: hook triggers уточнены до pre/post spec task execution и pre/post tool use categories, включая `spec`, `@mcp`, `@powers`, `write`, `shell`. Это подтверждает механизм автоматизации проверок, но не доказывает качество самих проверок. Источник: [Hook Triggers](https://kiro.dev/docs/hooks/types/).
- Частично закрыто в проходе 06: Kiro Web проверен по официальной документации и блогу от 18 мая 2026. Web docs показывают autonomous PR-oriented loop, sandbox, steering и multi-repo execution; блог говорит, что Specs будут перенесены в Web. Но текущие найденные Web docs не подтверждают полноценный Specs workflow с `requirements.md`, `design.md`, `tasks.md` и gates в Web.
- Закрыто в проходе 07: enterprise governance проверен по официальным docs. Для IDE/CLI Kiro Profile может централизованно управлять model allow list/default model, MCP on/off, MCP registry URL, API key generation и web tools. Это нужно описывать как policy layer вокруг Specs, а не как часть `requirements.md` → `design.md` → `tasks.md`.
- Частично закрыто в проходе 07: MCP registry уточнён как централизованный allow list с client-side enforcement, синхронизацией при старте и примерно раз в сутки, но personal MCP servers и local overrides в CLI остаются важной границей. Открытым остаётся вопрос, как это выглядит в реальных enterprise installations и какие audit logs доступны администраторам.
- Частично закрыто в проходе 07: Kiro Web Preview уточнён по Identity Center и Web MCP docs. Shared settings/governance не применяются к Web Preview, а stdio MCP servers могут иметь доступ вне agent tool sandbox. Открытым остаётся вопрос, когда Web Preview получит полноценные enterprise governance controls и как это изменит связь Web с будущими Web Specs.
- Частично закрыто в проходе 08: найден официальный enterprise monitoring слой — usage dashboard, user activity CSV reports, prompt logs in S3, CloudTrail и CloudWatch. Это отвечает на вопрос о documented administrative visibility, но не показывает полноценную traceability `requirement → design → task → diff → tests`; такую связку нужно считать отдельной методологической практикой или открытым вопросом продукта. Источники: [Monitoring and tracking](https://kiro.dev/docs/enterprise/monitor-and-track/), [Viewing per-user activity](https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/) и [Logging user prompts](https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/).
- Частично закрыто в проходе 08: data protection docs уточняют, что Kiro может хранить questions, responses и additional context для Free Tier/individual users, а для enterprise users формулирует `data is not stored` и opt-out from telemetry/content collection by AWS. Остаётся проверить, как это соотносится с customer-enabled prompt logging в S3 и фактическими retention policies конкретной организации. Источник: [Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/).
