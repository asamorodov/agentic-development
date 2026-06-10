# BMAD Method

## Назначение досье

Досье собирает BMAD Method как рабочий процесс SDLC с AI-агентами: какие файлы метод создаёт, как они становятся контекстом для следующих шагов, где человек выбирает направление, где агентам дают готовый контекст, какие проверки и статусы удерживают работу от расползания. Это рабочий буфер для будущего текста сайта, а не финальная карточка методологии.

## Роль в SDLC с AI-агентами

BMAD Method описывает себя как фреймворк разработки AI-native с открытым исходным кодом и модуль BMad Method (BMM) внутри BMad Ecosystem. В README текущего репозитория он позиционируется как модуль гибкой разработки с AI-агентами, который должен адаптироваться от исправлений и малых фич до корпоративных систем. Практически это не один запрос, а установленный набор skill-файлов, агентов, рабочих процессов и файловых артефактов, которые живут в проекте после команды `npx bmad-method install`. Источник: https://github.com/bmad-code-org/BMAD-METHOD и сырой README https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

Страница Official Modules помогает точнее развести BMM и остальную экосистему. Встроенное ядро и BMM остаются базой Agile-разработки, а дополнительные модули выбираются при установке и добавляют специализированных агентов, рабочие процессы и задачи поверх базовой рамки. Среди официальных модулей перечислены BMad Builder (`bmb`), Creative Intelligence Suite (`cis`), Game Dev Studio (`gds`) и Test Architect (`tea`). Для BMAD-досье это означает: TEA и BMad Builder нельзя описывать как обязательную часть каждого BMAD-проекта, но они являются официальными расширениями той же установочной и агентной модели. Источник: https://docs.bmad-method.org/reference/modules/

Для будущей теории важна не маркетинговая формула "AI-native", а устройство процесса: BMAD пытается заменить свободное общение с кодовым агентом последовательностью документальных переходов. Сначала создаются или уточняются требования, затем архитектура, затем эпики и истории, затем story-файлы используются как узкий контекст для реализации. Официальная Workflow Map описывает это как постепенное наращивание контекста через четыре фазы: каждый этап и каждый рабочий процесс производит документы, которые информируют следующий этап. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

## Краткая рабочая карта BMAD

BMAD Method лучше читать не как «набор промптов для агентов», а как попытку заменить длинный хрупкий разговор с кодовым агентом цепочкой файловых контрактов. В базовой схеме метод делает четыре вещи:

- устанавливает в проект `_bmad/` и `_bmad-output/`, то есть отделяет конфигурацию/skill-файлы/рабочие процессы от создаваемых планировочных и реализационных артефактов;
- заставляет выбрать масштаб работы: `Quick Flow`, полный `BMad Method` или `Enterprise`, причём выбор должен зависеть от риска, неопределённости и числа затронутых систем, а не только от формального количества историй;
- наращивает контекст через документы: бриф/исследование → PRD → UX/архитектура → эпики и истории → `sprint-status.yaml` → реализация/ревью/ретро;
- перед реализацией снова сужает контекст: story-файл, `project-context.md`, состояние спринта, сведения из предыдущей story и след ревью должны дать dev-агенту достаточно конкретную рамку без загрузки всего предыдущего обсуждения.

Сильная идея BMAD не в том, что «документов должно быть больше», а в том, что контекст, решения, статус и проверка работы становятся проверяемыми файлами. Эти файлы можно перечитать в свежем чате, передать другому агенту или персоне, положить в Git и использовать как след для ревью.

## Проблема, которую решает

Главная проблема BMAD - нестабильность агентной разработки, когда AI IDE получает слишком общий запрос, сам додумывает требования, путает архитектурные решения, теряет контекст между задачами и делает разные решения в разных историях. Официальный текст про `project-context.md` описывает это прямо: без явного контекста агенты могут применять общие практики, не совпадающие с кодовой базой, принимать непоследовательные решения между историями и пропускать проектные ограничения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

BMAD решает эту проблему через два слоя. Первый слой - фазовое накопление документов: продуктовый бриф или PRFAQ, PRD, UX-документы, архитектура, эпики, story-файлы. Второй слой - установленная инфраструктура skill-файлов и конфигурации: `_bmad/` хранит агентов, рабочие процессы, задачи и конфигурацию, а `_bmad-output/` хранит созданные артефакты. Getting Started показывает эту пару каталогов как результат установки. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

## Установка и файловая рамка

Базовая установка:

```bash
npx bmad-method install
```

Текущий README указывает предварительные требования: Node.js v20.12+, Python 3.10+ и `uv`; для канала предварительных выпусков предлагается `npx bmad-method@next install`, с явной оговоркой про более высокую изменчивость. Для CI/CD или повторяемой установки есть неинтерактивный вариант:

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

Опции модуля можно переопределять через повторяемый `--set <module>.<key>=<value>`, например `--set bmm.project_knowledge=research` и `--set bmm.user_skill_level=expert`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

После установки ожидаемая рамка проекта выглядит так:

```text
your-project/
├── _bmad/                       # конфигурация BMad
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md
│   │   ├── architecture.md
│   │   └── epics/
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml
│   └── project-context.md
└── ...
```

Getting Started подчёркивает, что `_bmad/` содержит агентов, рабочие процессы, задачи и конфигурацию, а `_bmad-output/` является местом сохранения артефактов. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Установка имеет оговорки о воспроизводимости. В руководстве по установке сказано, что `_bmad/_config/manifest.yaml` записывает установленные модули, версии, канал, `sha` и `repoUrl` для модулей с Git-источником. Установка из стабильного канала при повторном запуске может подтянуть более новый выпущенный тег; для воспроизводимости нужно переводить зафиксированные версии из manifest в явные флаги `--pin`. Там же указано ограничение GitHub API: анонимные вызовы ограничены 60 в час на IP, и для офисов, CI-runner или VPN может понадобиться `GITHUB_TOKEN`. Источник: https://docs.bmad-method.org/how-to/install-bmad/

В заметках к выпуску v6.8.0 есть важная версионная оговорка по слою конфигурации: установщик при повторном запуске теперь сначала читает центральный TOML, включая `_bmad/config.user.toml`, и только затем использует прежний `_bmad/<module>/config.yaml` как резервный вариант. Это подтверждает, что структура `_bmad/` в v6 ещё эволюционирует; для финального текста лучше фиксировать дату/версию и не превращать конкретный путь конфигурационного файла в вечное свойство метода. Источник: https://github.com/bmad-code-org/BMAD-METHOD/releases

## Режимы планирования

BMAD предлагает три режима планирования, которые выбираются не только по числу историй, а по потребности в планировании:

- `Quick Flow` - исправления, простые фичи, ясный объём, ориентир 1-15 историй, создаёт только техническую спецификацию.
- `BMad Method` - продукты, платформы, сложные фичи, ориентир 10-50+ историй, создаёт PRD + архитектуру + UX.
- `Enterprise` - требования соответствия и мультитенантные системы, ориентир 30+ историй, добавляет безопасность и DevOps к PRD и архитектуре.

Документация отдельно предупреждает: количество историй является ориентиром, а не определением; режим нужно выбирать по потребности в планировании, а не механически по размеру. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Enterprise-режим в текущей документации лучше читать вместе с TEA, а не только как "больше документов". Enterprise-руководство TEA говорит, что такой режим нужен для соответствия требованиям, критичных к безопасности приложений, требований к следу аудита и строгих NFR-порогов. Предпосылки: BMAD установлен с выбранным Enterprise-режимом, TEA-агент доступен, требования соответствия документированы, а ответственные участники для утверждения на контрольной точке известны заранее. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

Для теории это важная оговорка. BMAD не всегда требует полного длинного цикла: для малых и хорошо понятых изменений Quick Flow пропускает фазы 1-3 и использует `bmad-quick-dev`, который должен пройти путь от намерения к технической спецификации и рабочему коду. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md и https://docs.bmad-method.org/workflow-map-diagram.html

Официальная страница Quick Fixes уточняет практическую границу Quick Flow. `bmad-quick-dev` подходит для исправлений ошибок с ясной причиной, небольших рефакторингов в нескольких файлах, малых корректировок фич и обновлений зависимостей. Входом может быть свободный текст, путь к файлу с намерением, URL GitHub issue или ссылка на трекер ошибок; рабочий процесс может задать уточняющие вопросы или показать короткую спецификацию на утверждение перед реализацией. Результат ожидается как изменённые исходные файлы, пройденные тесты при их наличии и локальный коммит, готовый к отправке, с сообщением в формате Conventional Commits. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Та же страница задаёт явный порог перехода к полному BMAD: если изменение затрагивает несколько систем, требует согласованных правок во многих файлах, имеет неясный объём или команде нужно сохранить требования и архитектурные решения для других участников, Quick Dev уже недостаточен. Это важнее, чем численный ориентир 1-15 историй: сам источник описывает переход через характер риска и потребность в предварительном прояснении задачи. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Объяснение Quick Dev уточняет, где именно остаётся человек. Рабочий процесс сначала сжимает исходное намерение в одну непротиворечивую цель, затем выбирает минимальный безопасный путь: совсем малое изменение может идти сразу в реализацию, всё остальное проходит через утверждение спецификации. Человеческие точки контроля вынесены в уточнение намерения, утверждение спецификации и ревью итогового результата; при сбое рабочий процесс должен определить, где возникла ошибка - в исходном намерении, в слабой спецификации или в локальной реализации, - и возвращаться на соответствующий слой, а не чинить любой дефект прямо в diff. Источник: https://docs.bmad-method.org/explanation/quick-dev/

## Рабочий процесс: четыре фазы

### Фаза 1: анализ, необязательная фаза

Цель - исследовать пространство проблемы и проверить идеи до обязательного планирования. Workflow Map перечисляет:

- `bmad-brainstorming` - направляемый брейнсторминг, результат `brainstorming-report.md`.
- `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` - проверка предметных, рыночных или технических допущений, результат — исследовательские наблюдения.
- `bmad-product-brief` - фиксация стратегического видения, результат `product-brief.md`.
- `bmad-prfaq` - Working Backwards для стресс-теста продуктовой концепции, результат `prfaq-{project}.md`.

Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

В диаграмме рабочего процесса эти шаги связаны с агентом/персоной Mary; продуктовый бриф и PRFAQ ведут стрелкой к планированию. Источник: https://docs.bmad-method.org/workflow-map-diagram.html

### Фаза 2: планирование, обязательная фаза

Цель - определить, что строить и для кого. Для BMad Method и Enterprise-режима основной рабочий процесс - `bmad-prd`. У него есть три намерения:

- `Create` - управляемое исследование с нуля, результат `prd.md`, `addendum.md`, `decision-log.md`.
- `Update` - сверка существующего PRD с сигналом изменения, с выявлением конфликтов до применения изменений.
- `Validate` - проверка готового PRD по настраиваемому чеклисту, результат `validation-report.html` и `.md`.

Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Версионная оговорка по именам skill-файлов: часть официальной документации всё ещё показывает `bmad-create-prd`, а релизы v6.7.0 описывают переход к единому `bmad-prd` с намерениями `Create`/`Update`/`Validate`. В v6.7.0 старые PRD skill-файлы для создания, редактирования и проверки сохранены как совместимые обёртки (`shim`), которые маршрутизируют в единый PRD skill, но заявлено, что эти обёртки должны быть удалены в 7.0.0. Это нужно сохранить в досье, чтобы будущий текст не выглядел устаревшим и одновременно не спорил с текущими учебными страницами. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.7.0

Core Tools вводит ещё один контрактный слой - `bmad-spec`. Он принимает бриф, PRD, GDD, RFC, свободный дамп, стенограмму, UX-папку или смешанный набор входов и сжимает их в `SPEC.md`: ядро из пяти полей `Why`, `Capabilities`, `Constraints`, `Non-goals`, `Success signal`. Всё важное, что не помещается в ядро, уходит в сопутствующие файлы. Это не замена полному PRD во всех случаях, а компактный контракт для следующих шагов, полезный там, где нужно зафиксировать "что" до "как" и дать агентам короткий, пригодный для загрузки контракт вместо чтения всех предыдущих артефактов. Источник: https://docs.bmad-method.org/reference/core-tools/

Если продукт имеет UI, документация предлагает вызвать UX-Designer-агента `bmad-agent-ux-designer` и запустить `bmad-ux` после PRD. Workflow Map описывает результат как пару `DESIGN.md` + `EXPERIENCE.md` и `.decision-log.md`: визуальная ось и поведенческая ось. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

В v6.8.0 `bmad-ux` описан как замена старого UX skill с единой осью: новый контракт разделяет `DESIGN.md` с визуальной идентичностью и `EXPERIENCE.md` с поведением, потоками, информационной архитектурой, состояниями и доступностью. Релиз подчёркивает, что передача из дизайна в инженерную реализацию должна быть запечатанным файловым контрактом, а не неформальным переводом намерений между агентами. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.8.0

### Фаза 3: проектное решение

Для BMad Method и Enterprise-режима после PRD создаётся архитектура:

- `bmad-create-architecture` через Architect-агента `bmad-agent-architect`; результат - архитектурный документ с техническими решениями, в Workflow Map: `architecture.md` с ADR.
- `bmad-create-epics-and-stories` через PM-агента `bmad-agent-pm`; рабочий процесс использует PRD и Architecture, чтобы создать технически обоснованные истории.
- `bmad-check-implementation-readiness` через Architect-агента; рекомендуемая gate-проверка перед реализацией, проверяющая согласованность планировочных документов и возвращающая решение PASS/CONCERNS/FAIL.

Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

Важная деталь v6: эпики и story-файлы теперь создаются после архитектуры. Документация объясняет это тем, что архитектурные решения - база данных, паттерны API, технологический стек - прямо влияют на разбиение работы. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Официальное объяснение проектного решения формулирует проблему через конфликты между агентами: без общей архитектуры агент 1 может реализовать эпик 1 через REST API, агент 2 - эпик 2 через GraphQL, и интеграция станет несогласованной. Страница про Preventing Agent Conflicts раскрывает механизм: ADR фиксирует `context`, `considered options`, `decision`, `rationale` и `consequences`; архитектура также задаёт указания по FR/NFR, структуру каталогов, соглашения об именовании, организацию кода и паттерны тестирования. Источник: https://docs.bmad-method.org/explanation/architecture/why-solutioning-matters/ и https://docs.bmad-method.org/explanation/preventing-agent-conflicts/

В Enterprise-режиме проектное решение получает тестовый и комплаенсный хвост ещё до реализации. Руководство TEA предлагает на фазе 3 совместить архитектуру с `test-design` в режиме системного уровня: проверить тестируемость архитектуры безопасности, стратегию тестирования производительности и связь требований соответствия с тестами. Отдельно планируются тестовая инфраструктура и CI/CD: разделённые тестовые окружения (`dev`, `staging`, `prod-mirror`), безопасная работа с тестовыми данными для PHI/PII, аудитное логирование в тестах, управление секретами, изоляция тестов, хранение артефактов и контроль доступа для production-тестов. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

### Фаза 4: реализация

Реализация строится история за историей и обычно в свежих чатах. Getting Started требует после завершения планирования переходить к реализации и запускать каждый рабочий процесс в свежем чате. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Цикл:

- `bmad-sprint-planning` создаёт `sprint-status.yaml`, чтобы отслеживать эпики и истории.
- `bmad-create-story` создаёт отдельный story-файл из эпика.
- `bmad-dev-story` реализует story.
- `bmad-code-review` выполняет проверку качества; рекомендуется.
- после завершения всех историй в эпике запускается `bmad-retrospective`.

Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Workflow Map добавляет дополнительные рабочие процессы реализации: `bmad-correct-course` для существенных изменений посреди спринта, `bmad-sprint-status` для обновления статуса спринта и `bmad-investigate` для форензик-расследования случая с результатом `{slug}-investigation.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

`bmad-correct-course` устроен как рабочий процесс управления изменениями, а не как быстрый фикс кода. Его собственный skill-файл требует широкий проектный контекст: PRD и Epics обязательны, Architecture, UX, Spec и Document Project загружаются при наличии; разделённые документы сначала раскрываются через `index.md`, а для Document Project применяется загрузка по `index.md` только релевантных секций. Результат пишется в `{planning_artifacts}/sprint-change-proposal-{date}.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md

Change Navigation Checklist внутри `bmad-correct-course` заставляет пройти шесть групп вопросов: что именно стало триггерной историей или проблемой, как это влияет на текущий эпик и будущие эпики, какие конфликты появились в PRD/Architecture/UI/UX/CI/CD/testing/docs, какой путь выбрать - прямую корректировку (`direct adjustment`), откат (`rollback`) или пересмотр PRD/MVP (`PRD MVP review`), какие конкретные правки нужны в артефактах, и кто дальше отвечает за передачу. Важная точка человеческого контроля: рабочий процесс не должен продолжать предложение (`proposal`) без полного анализа влияния, не должен выполнять изменения без явного утверждения и должен явно определить, кто исполняет предложенные изменения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md

`bmad-sprint-status` закрывает другой промежуточный разрыв: он не создаёт новую работу, а читает `{implementation_artifacts}/sprint-status.yaml`, классифицирует ключи как эпики, истории и ретроспективы, нормализует устаревшие статусы (`drafted` -> `ready-for-dev`, `contexted` -> `in-progress`), считает статусы, ищет риски и рекомендует следующий рабочий процесс. Его приоритеты простые: сначала продолжить story со статусом `in-progress` через `dev-story`, затем отправить story со статусом `review` в `code-review`, затем взять `ready-for-dev`, затем создать story из backlog, затем провести ретроспективу. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md

Для Quick Dev хвост реализации устроен иначе, чем для story-цикла. Quick Fixes говорит, что рабочий процесс сам реализует изменение, проверяет собственную работу, исправляет найденные проблемы и делает локальный коммит; после этого человеку нужно просмотреть diff, подтвердить соответствие исходному намерению и отправить коммит в удалённый репозиторий. Если уже отправленное изменение вызвало неожиданные проблемы, документация предлагает `git revert HEAD`, затем свежий чат и новый запуск Quick Dev. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Встроенный QA-рабочий процесс появляется именно в фазе 4, но не как замена ревью кода. Страница Testing options говорит, что `bmad-qa-generate-e2e-tests` доступен через Developer agent (`QA`) и обычно запускается после завершения полного эпика, когда все истории реализованы и прошли ревью кода. Он определяет тестовый фреймворк по `package.json` и существующим тестам, выбирает или обнаруживает функции, генерирует API- и E2E-тесты, запускает их и чинит базовые сбои. Источник: https://docs.bmad-method.org/reference/testing/

Enterprise-жизненный цикл TEA расширяет фазу 4 по каждому эпику: `test-design` в режиме уровня эпика для соответствия требованиям, безопасности и производительности, необязательный `atdd` для приёмочных тестов, обычная реализация story, `automate` для расширения покрытия, `test-review` с оценкой качества и `trace Phase 1` для обновления покрытия. На release gate порядок становится ещё строже: `nfr-assess`, полный `test-review`, затем `trace Phase 2` с решением `PASS/CONCERNS/FAIL/WAIVED`; для Phase 2 gate нужны фактические результаты выполнения тестов, иначе шаг gate пропускается. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

Enterprise-руководство показывает, какие артефакты становятся доказательствами: `traceability-matrix.md`, `test-review.md`, `nfr-assessment.md`, `gate-decision-release-{version}.md`, результаты тестов, отчёты о покрытии, security-сканы и подписи утверждающих участников. Он даже предлагает пример папки `compliance/{period}/release-{version}/` и ориентиры хранения вроде 7 лет для HIPAA или 3 года для SOC 2. Для теории это важно: Enterprise BMAD переносит "качество" из устного доверия к агенту в архивируемый пакет доказательств, где у каждого решения есть проверяемое происхождение. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

`bmad-investigate` вводит отдельную ветку расследования внутри фазы 4. Skill принимает ID тикета, лог-файл, диагностический архив, сообщение об ошибке, имя области кода, описание проблемы или путь к существующему case file; старый case можно возобновить, а новый записывается как `{implementation_artifacts}/{workflow.case_file_subdir}/{workflow.case_file_filename}`. Принципиальная граница: расследование останавливается на диагностическом выводе; для дальнейшего действия skill-файл предлагает `bmad-quick-dev`, `bmad-correct-course`, `bmad-create-story` или `bmad-code-review` в зависимости от вывода. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md и https://docs.bmad-method.org/explanation/forensic-investigation/

## Артефакты и как они становятся входами

Ключевая цепочка:

```text
brainstorming-report.md / исследовательские наблюдения / product-brief.md / prfaq-{project}.md
→ prd.md + addendum.md + decision-log.md
→ DESIGN.md + EXPERIENCE.md + .decision-log.md, если нужен UX
→ architecture.md с ADR
→ epics / stories
→ sprint-status.yaml
→ story-[slug].md
→ рабочий код + тесты
→ code-review: approved или changes requested
→ тесты QA / TEA после эпика, если нужны дополнительные тесты
→ retrospective: извлечённые уроки
```

Диаграмма рабочего процесса показывает поток артефактов: `product-brief.md` или `prfaq.md` ведут к `prd.md`, затем UX и архитектура ведут к эпикам, затем `sprint-status.yaml`, `story-[slug].md`, код, утверждение, обновлённый план и уроки. Источник: https://docs.bmad-method.org/workflow-map-diagram.html

Контекстный переход зафиксирован явно: PRD сообщает архитектору, какие ограничения важны; архитектура сообщает dev-агенту, каким паттернам следовать; story-файлы дают сфокусированный и полный контекст для реализации. Без такой структуры, по формулировке Workflow Map, агенты принимают непоследовательные решения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

`SPEC.md` добавляет более короткий контекстный переход для задач, где полный набор предыдущих документов слишком тяжёлый: он хранит ядро намерения, возможностей, ограничений, не-целей и сигнала успеха, а сопутствующие файлы удерживают тяжёлые детали отдельно. Для теории это полезно как пример двухскоростного контекста: компактный контракт для обычного использования на следующих шагах и отдельные материалы для случаев, когда агенту нужно глубже читать происхождение решения. Источник: https://docs.bmad-method.org/reference/core-tools/

## Контекст

BMAD делит контекст на несколько уровней:

- Документы цепочки планирования: PRD, UX, архитектура, эпики, story-файлы.
- Правила уровня проекта в `_bmad-output/project-context.md`.
- Слой выполнения/конфигурации в `_bmad/`, включая конфигурацию модулей и настройку skill-файлов.
- Состояние спринта в `_bmad-output/implementation-artifacts/sprint-status.yaml`.
- След ревью в Quick Dev / Checkpoint Preview: файл спецификации после Quick Dev может содержать предложенный порядок ревью, который используется как карта чтения изменений; если такого следа нет, рабочий процесс генерирует его из diff и контекста кодовой базы. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/

`project-context.md` особенно важен для переноса в теорию. Он описан как руководство по реализации для AI-агентов: стек технологий и версии, критические правила реализации, соглашения и предпочтения проекта. Он автоматически загружается в рабочие процессы реализации, если существует; рабочий процесс архитектора тоже загружает его, чтобы учитывать технические предпочтения на фазе проектного решения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

Создать `project-context.md` можно вручную в `_bmad-output/project-context.md` до архитектуры, сгенерировать после архитектуры через `bmad-generate-project-context`, или запустить генерацию в существующем проекте, чтобы обнаружить устоявшиеся соглашения. Документация подчёркивает, что документ должен фиксировать неочевидные вещи, которые агенты могут не вывести из чтения отдельных фрагментов кода, а не универсальные стандартные практики. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

Для существующих проектов официальное руководство добавляет отдельную операцию гигиены до генерации контекста: если прежние PRD, эпики и истории уже завершены, их нужно архивировать/удалить или оставить только в истории версий; не держать завершённые планировочные артефакты в `docs/`, `_bmad-output/planning-artifacts/` или `_bmad-output/implementation-artifacts/`. Иначе агенты могут прочитать старые документы как актуальные требования. Источник: https://docs.bmad-method.org/how-to/established-projects/

В существующем проекте `bmad-generate-project-context` должен просканировать кодовую базу и зафиксировать стек технологий и версии, паттерны организации кода, соглашения об именовании, подходы к тестированию и паттерны конкретного фреймворка. После генерации человек должен проверить и уточнить файл; для сложных проектов руководство предлагает `bmad-document-project`, который сканирует проект и документирует его актуальное состояние. Источник: https://docs.bmad-method.org/how-to/established-projects/

Источник `bmad-document-project` показывает, что это не единый Markdown-дамп. Маршрутизатор ищет `{project_knowledge}/project-scan-report.json`, умеет возобновлять работу, начинать заново, делать полное повторное сканирование, deep-dive и архивировать старое состояние в `{project_knowledge}/.archive/project-scan-report-{timestamp}.json`; если уже есть `{project_knowledge}/index.md`, он предлагает повторно просканировать весь проект (`re-scan entire project`), глубоко разобрать конкретную область (`deep-dive specific area`) или отменить (`cancel`). Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md

Full Project Scan использует `documentation-requirements.csv` как руководство по сканированию для 12 типов проектов: web, mobile, backend, cli, library, desktop, game, data, extension, infra, embedded. Уровень сканирования выбирается человеком: Quick Scan читает в основном конфиги, манифесты и структуру каталогов; Deep Scan читает критические каталоги; Exhaustive Scan читает все исходные файлы, кроме типичных сгенерированных и тяжёлых каталогов. Файл состояния обновляется после каждого шага с `timestamp`, `current_step`, `completed_steps`, списком сгенерированных результатов и краткими наблюдениями; рабочий процесс явно требует очищать подробные наблюдения из контекста после записи документов, чтобы не держать всю кодовую базу в разговоре. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md

Артефакты `bmad-document-project` могут включать `project-overview.md`, `source-tree-analysis.md`, `architecture.md` или `architecture-{part_id}.md`, `component-inventory.md`, `development-guide.md`, `deployment-guide.md`, `contribution-guide.md`, `api-contracts.md`, `data-models.md`, `integration-architecture.md`, `project-parts.json` и `index.md`. Неполные документы помечаются ровно как `_(To be generated)_`, чтобы последующий шаг мог найти их и предложить сгенерировать. Для brownfield-части теории это важная деталь: BMAD не просто "читает код", а строит навигируемую базу знаний проекта, которую потом могут загружать другие рабочие процессы через `index.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md

Validation checklist для `bmad-document-project` уточняет, что именно считается качественным сканированием. Quick scan не должен читать исходные файлы, deep scan читает критические каталоги по типу проекта, exhaustive scan читает все исходные файлы кроме `node_modules`, `dist`, `build`. Deep/exhaustive scans должны идти пакетами по подкаталогам, а не по случайному числу файлов; каждый пакет читает файлы, извлекает сведения, пишет результат, валидирует и очищает контекст. Чеклист также привязывает полноту сканирования к флагам из `documentation-requirements.csv`: если `requires_api_scan = true`, нужны API endpoints; если `requires_data_models = true`, нужны модели данных; если `requires_state_management = true`, нужны паттерны состояния; если `requires_ui_components = true`, нужен реестр UI-компонентов. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md

Новый проход раскрыл сам `documentation-requirements.csv`, а не только checklist. Файл действительно является компактной таблицей на 12 строк типов проектов и 24 колонки: `project_type_id`, булевы флаги вроде `requires_api_scan`, `requires_data_models`, `requires_state_management`, `requires_ui_components`, затем группы паттернов (`key_file_patterns`, `critical_directories`, `integration_scan_patterns`, `test_file_patterns`, `auth_security_patterns`, `schema_migration_patterns`, `ci_cd_patterns`, `asset_patterns`, `protocol_schema_patterns` и другие). Это закрывает прежний открытый вопрос о том, существует ли таблица только как пересказ в документации рабочего процесса: она читается напрямую и показывает управляемый данными характер `bmad-document-project`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/documentation-requirements.csv

Deep-dive-режим оказался жёстче обычного сканирования. `deep-dive-instructions.md` прямо запрещает выборочное чтение, догадки и опору только на вывод инструментов (`sampling/guessing/relying solely on tooling output`) и требует буквального полного чтения файлов выбранной области (`literal full-file review`); пользователь сначала подтверждает цель, тип, путь и оценочное число файлов, затем рабочий процесс читает каждый файл в этой области. Для теории это важное уточнение: BMAD различает быстрый обзор проекта, глубокое документирование brownfield-кода и точечный exhaustive deep-dive перед рискованной работой над фичей. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/deep-dive-instructions.md

## Что в BMAD является ядром, а что расширением

Для будущего текста важно не смешивать несколько уровней. Ядро этого досье — BMM как модуль Agile/SDLC-работы: установка, файловые артефакты, рабочие процессы анализа, планирования, архитектуры, story-файлы, реализации, ревью и статуса спринта. BMad Ecosystem шире: официальные модули вроде TEA, BMad Builder, Creative Intelligence Suite и Game Dev Studio могут добавлять собственных агентов, задачи и рабочие процессы поверх базовой рамки. Их полезно описывать как расширения той же установочной и агентной модели, но не как обязательные шаги каждого BMAD-проекта.

Отсюда редакционное правило: TEA и Enterprise-ветку можно использовать для объяснения предельного варианта BMAD с жизненным циклом доказательств, NFR, release gate и архивом соответствия, но основной рассказ о BMAD должен сначала показать базовую цепочку документов и stories. Иначе читатель решит, что BMAD всегда означает тяжёлый регулируемый процесс, хотя источники одновременно описывают Quick Flow, полный Method-режим и отдельные расширения.

## Роли, агенты и участники

Официальные материалы называют Specialized Agents: PM, Architect, Developer, UX и другие; README говорит о 12+ предметных экспертах (`domain experts`) и Party Mode, где несколько персон могут участвовать в одной сессии. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

В диаграмме рабочего процесса видны конкретные имена/персоны по основному пути:

- Mary - анализ: брейнсторминг, исследование, продуктовый бриф, PRFAQ.
- John - планирование и PM-переходы: PRD, эпики и истории, correct-course; в диаграмме также показан на проверке готовности.
- Sally - UX.
- Winston - архитектура.
- Amelia - реализация: планирование спринта, создание story, dev-story, code review, retrospective, investigate.

Источник: https://docs.bmad-method.org/workflow-map-diagram.html

`bmad-help` является не ролью в продуктовой цепочке, а навигационным механизмом. Его назначение: понять, где пользователь находится в рабочем процессе, что уже завершено, что делать дальше, как вызвать следующий skill-файл, и не перегружать пользователя полным каталогом. Он читает каталог `_bmad/_config/bmad-help.csv`, файлы конфигурации, найденные артефакты и знания проекта, а также строки документации модулей. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md

## Человеческие решения и контрольные точки

Человек принимает решения в нескольких местах:

- Выбор режима планирования: Quick Flow, BMad Method или Enterprise; документация предупреждает выбирать по потребностям планирования, а не арифметике историй. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- Выбор намерения для `bmad-prd`: `Create`, `Update` или `Validate`. Если намерение не указано, skill-файл должен спросить. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- UX включается условно: если у проекта есть UI, вызывается UX-Designer и `bmad-ux`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- В существующем проекте UX-работа зависит не от того, "есть ли UX", а от того, затрагивает ли изменение UX или требует новых UX-паттернов; простые обновления существующих экранов могут обойтись без полного UX-процесса. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `project-context.md` можно создать вручную до архитектуры, если у человека уже есть сильные технические предпочтения, или сгенерировать после архитектуры. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- Проверка готовности к реализации даёт решение PASS/CONCERNS/FAIL перед реализацией; это место для остановки или исправления несогласованных планировочных документов. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- В `bmad-create-story` вмешательство пользователя исключается почти полностью, кроме начального выбора epic/story или отсутствующих документов; если нет `sprint-status.yaml`, рабочий процесс предлагает запустить sprint-planning, указать конкретный номер epic-story или дать путь к story-документам. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- В workflow ретроспективы человек подтверждает, какое ревью эпика проводится, и может выбрать частичную ретроспективу, если эпик ещё не завершён. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- В Quick Dev человек утверждает короткую спецификацию/план до реализации, затем проверяет diff после локального коммита и принимает решение об отправке; если изменение оказалось неудачным после отправки, официальный резервный путь - `git revert HEAD` и свежий чат с новым запуском. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- `bmad-checkpoint-preview` добавляет отдельное ревью с участием человека после автономной реализации, особенно после `bmad-quick-dev`. Рабочий процесс принимает PR, commit, branch, spec file или текущее git-состояние; сначала даёт однострочное резюме намерения и статистику области изменений, затем ведёт пошаговый разбор замечаний (`concerns`) с остановками `path:line`, потом показывает 2-5 мест с наибольшим blast radius и предлагает ручные наблюдения для проверки результата. Он не выносит вердикт pass/fail и не заменяет линтеры, проверки типов или тестовые наборы; это структурированная карта чтения, чтобы человек мог решить, отправлять, переделывать или разбираться глубже. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/
- В `bmad-correct-course` человек выбирает пошаговый или пакетный режим (`incremental` или `batch mode`), утверждает или правит каждое предложение правки (`edit proposal`) и затем явно отвечает `yes`/`no`/`revise` на весь Sprint Change Proposal. Это не скрытый автопатч планировочных артефактов: сам skill-файл требует получить явное утверждение пользователя до реализации и только затем направить работу к Developer, Product Owner / Developer или Product Manager / Architect в зависимости от масштаба изменения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md
- В `bmad-document-project` человек выбирает уровень сканирования, подтверждает классификацию проекта, может указать дополнительные документы или ключевые области, а после генерации решает, нужно ли достраивать маркеры неполной документации. Это место человеческого контроля особенно важно для brownfield: неверная классификация проекта или слишком поверхностный уровень сканирования даст последующим агентам убедительную, но неполную базу знаний проекта. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- В Enterprise/TEA человек задаёт ответственных участников до контрольных gate-проходов, а release gate требует подписей утверждающих участников (`approver signatures`). Пример структуры утверждения (`approval structure`) включает QA Lead, Tech Lead, Security Lead, Product Manager, Compliance Officer и, для крупных релизов, VP Engineering/CTO. Это уже не обычное "посмотреть diff": метод переносит часть решения в формальную матрицу технического, продуктового и комплаенс-утверждения. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

## Проверка готовности и качества

Проверки распределены по цепочке:

- `bmad-prd` в режиме Validate проверяет PRD по чеклисту и создаёт HTML/Markdown-отчёт валидации. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Релиз v6.7.0 уточняет форму проверки PRD: новый конвейер проверки заменил состязательного рецензента (`adversarial reviewer`) на синтезирующий проход (`synthesis pass`) по рубрике качества (`quality rubric`), который выдаёт HTML и Markdown-отчёты; на сайте BMad также упоминается PRD Coach со встроенной проверкой по семи измерениям. Это похоже на активную зону изменений, поэтому перед финальным текстом нужно сверить документацию и заметки к выпуску. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://www.bmadcode.com/
- Релиз v6.8.0 добавляет ещё один важный поворот: `bmad-spec` становится core skill, вытесняя прежний `bmad-distillator`, а `bmad-ux` заменяет прежнюю UX-связку двумя файлами `DESIGN.md` и `EXPERIENCE.md`; передача из дизайна в инженерную реализацию описана как запечатанный файловый контракт (`sealed file contract`). Там же указаны веб-бандлы для Gemini Gems и ChatGPT Custom GPTs, `bmad-automator` на канале `next` и `bmad-method-ui` в статусе community-alpha. Для досье это не отдельный BMAD-рабочий процесс, а сигнал быстрой эволюции поверхности и перехода к более формализованным файловым контрактам. Источник: https://github.com/bmad-code-org/BMAD-METHOD/releases
- `bmad-check-implementation-readiness` является gate-проверкой до реализации и возвращает решение PASS/CONCERNS/FAIL. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- `bmad-sprint-planning` валидирует полноту `sprint-status.yaml`: каждый epic, каждую story, запись retrospective, отсутствие осиротевших элементов (`orphan items`), допустимые значения статуса и корректный YAML-синтаксис. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md
- `bmad-sprint-status` повторно валидирует `sprint-status.yaml`: проверяет обязательные метаданные (`generated`, `project`, `project_key`, `tracking_system`, `story_location`), наличие `development_status`, допустимость значений статусов, осиротевшие истории (`orphaned stories`), устаревший timestamp, epic со статусом `in-progress` без story и неизвестные значения статусов. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md
- `bmad-create-story` валидирует story-файл по `./checklist.md`, обновляет статус story на `ready-for-dev` и меняет `sprint-status.yaml`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- `bmad-dev-story` должен выполнять шаги в точном порядке (`steps in exact order`), не останавливаться на "milestones" или "session boundaries" и продолжать, пока story complete, если нет HALT-условия или инструкции пользователя. Он обновляет только разрешённые области story-файла: `baseline_commit`, checkboxes, Dev Agent Record, File List, Change Log and Status. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- `bmad-code-review` описан как состязательное ревью (`adversarial review`) с параллельными слоями ревью: Blind Hunter, Edge Case Hunter, Acceptance Auditor; архитектура выполнения требует полностью читать файл текущего шага (`current step file`), следовать последовательности, ждать ввода на контрольных точках и загрузить следующий шаг. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md
- Implementation FAQ говорит, что после прохождения dev-story и code-review пользователь должен открыть `sprint-status.yaml`, поменять статус story с `review` на `done` и сохранить файл. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Встроенный QA (`bmad-qa-generate-e2e-tests`) генерирует только тесты и не отвечает за валидацию story или code review. Его стандартные паттерны: использовать API существующего тестового фреймворка без внешних утилит, в UI-тестах предпочитать семантические локаторы (`semantic locators`), держать тесты независимыми, не вставлять жёстко заданные ожидания или паузы (`hardcoded waits/sleeps`) и писать описания, которые читаются как документация фичи. Источник: https://docs.bmad-method.org/reference/testing/
- Для более тяжёлого тестового управления существует отдельный модуль TEA: устанавливаемый модуль Test Architect с Murat-агентом и девятью рабочими процессами, включая Test Design, ATDD, Automate, Test Review, Traceability, NFR Assessment, CI Setup, Framework Scaffolding и Release Gate. В отличие от встроенного QA, TEA рассчитан на отслеживаемость, соответствие требованиям, приоритизацию по риску P0-P3 и контрольные точки качества. Источник: https://docs.bmad-method.org/reference/testing/
- Страница TEA welcome уточняет рабочие триггеры и форму модуля: `bmad-tea` загружает TEA agent/menu, `test-design` запускает Test Design, а core workflows имеют короткие триггеры вроде `TD`, `TF`, `CI`, `AT`, `TA`, `RV`, `NR`, `TR`. `GATE` в меню TEA не является самостоятельным workflow: это routing helper через последовательность release gate, который не производит отдельный артефакт. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/
- Enterprise TEA gate проверяет не только наличие тестов. Для `nfr-assess` нужны пороговые категории (`threshold categories`) вроде Security, Performance, Reliability, Maintainability и подтверждения вроде security-сканов, penetration tests или compliance audits; `trace Phase 2` создаёт gate-решение со ссылками на доказательства (`evidence`), подписи утверждающих участников (`approver signatures`), чеклист соответствия и обоснование решения. Результат gate выражается как `PASS/CONCERNS/FAIL/WAIVED`, а не как общий "tests passed". Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- `bmad-investigate` проверяет не готовность к отправке, а качество расследования. Находки получают оценку (`grade`): Confirmed требует прямой ссылки на `path:line`, timestamp лога или commit hash; Deduced должен показывать цепочку рассуждения от подтверждённого доказательства (`Confirmed evidence`); Hypothesized обязан назвать, что подтвердит или опровергнет гипотезу. Гипотезы не удаляются: status меняется на Open, Confirmed или Refuted, а resolution объясняет, какие доказательства закрыли ветку. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md

## Sprint-status как автомат состояний

`bmad-sprint-planning` создаёт `sprint-status.yaml` как упорядоченный реестр эпиков и story. Он конвертирует story-заголовки вроде `### Story 1.1: User Authentication` в ключ `1-1-user-authentication`, добавляет запись эпика `epic-{num}`, записи story и `epic-{num}-retrospective`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md

Состояния:

```text
Epic: backlog → in-progress → done
Story: backlog → ready-for-dev → in-progress → review → done
Retrospective: optional ↔ done
```

Заметки рабочего процесса уточняют: epic переходит в `in-progress` автоматически, когда создаётся первая story; истории обычно выполняются по порядку, но параллельная работа поддерживается; review должен проходить перед `done`; следующая story обычно создаётся после того, как предыдущая получила `done`, чтобы перенести извлечённые уроки. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md

## Story как основной контекст реализации

`bmad-create-story` - центральный механизм защиты реализации от потери контекста. Его цель: создать полный story-файл, который даёт dev-агенту всё необходимое для реализации. В самом skill-файле перечислены ошибки, которые он должен предотвращать: повторное изобретение готовых решений, неверные библиотеки, неверные расположения файлов, регрессии, игнорирование UX, расплывчатые реализации, ложные заявления о завершении и отсутствие обучения на прошлой работе. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

Этот рабочий процесс не просто копирует эпик. Он должен загрузить PRD, architecture, UX, эпики, сведения из предыдущей story, свежие git-коммиты, релевантные UPDATE-файлы, стандарты тестирования, паттерны API, схемы базы данных, требования безопасности, требования производительности и свежие технические сведения по критическим библиотекам. Странная, но важная деталь источника: create-story прямо требует читать файлы, которые story будет менять, потому что пропуск этого является основной причиной сбоев реализации и циклов ревью. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

В story-файл должны попасть ограничители для dev-агента: технические требования, соответствие архитектуре, требования к библиотекам/фреймворкам, требования к файловой структуре, требования к тестированию, сведения из предыдущей story, сводка git-сведений, актуальная техническая информация, ссылка на проектный контекст и статус завершения story. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

## Жизненный цикл после реализации

После реализации story проходит ревью, обновление статуса и ретроспективу:

- `bmad-dev-story` переводит story в работу, фиксирует `baseline_commit` через `git rev-parse HEAD` или `NO_VCS`, обновляет статус спринта и запись story. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- Если code review создал последующие задачи (`follow-up items`), `bmad-dev-story` умеет распознать секцию `Senior Developer Review (AI)` и subsection `Review Follow-ups (AI)`, затем сначала выполняет задачи из follow-up ревью, а уже потом обычные задачи. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- Story считается окончательно завершённой после прохождения dev-story и code-review, а затем ручного обновления `sprint-status.yaml` из `review` в `done`. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Если во время реализации обнаружен не локальный дефект, а изменение понимания задачи, `bmad-correct-course` переводит это в Sprint Change Proposal: анализ влияния (`impact analysis`), рекомендуемый подход (`recommended approach`), подробные предложения изменений (`detailed change proposals`) и передачу на реализацию (`implementation handoff`). Он может привести к прямой корректировке stories, откату недавно завершённой работы (`rollback`) или пересмотру PRD/MVP. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md
- Retrospective запускается после завершения всех историй в эпике. Implementation FAQ подчёркивает, что ждать конца всего проекта не нужно: ретроспектива после каждого эпика поддерживает непрерывное улучшение. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Рабочий процесс Retrospective читает записи story, обратную связь ревью, заметки тестирования, технический долг, предыдущую ретроспективу и следующий эпик, чтобы извлечь уроки, повторяющиеся паттерны, нерешённый долг и подготовительные задачи. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- Если нужен тестовый слой после эпика, BMAD предлагает сначала встроенный QA-рабочий процесс, а при требованиях отслеживаемости, соответствия требованиям или формальных контрольных точек качества - TEA. Важная граница: встроенный QA работает напрямую от исходного кода и не загружает PRD/architecture, а TEA может связываться с вышестоящими планировочными артефактами для отслеживаемости. Источник: https://docs.bmad-method.org/reference/testing/
- Если проблема требует расследования до планирования исправления, `bmad-investigate` создаёт или продолжает case file, отделяет подтверждённые наблюдениями выводы (`confirmed`) от выводов и гипотез (`deductions/hypotheses`), реконструирует хронологию (`timeline`), фиксирует недостающие доказательства (`missing evidence`) и завершает работу понятной передачей. Финальный результат содержит уровень уверенности: High для подтверждённой первопричины с детерминированным воспроизведением, Medium для вывода с небольшой неопределённостью, Low для гипотезы с явным пробелом данных. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md

## Сильные стороны

- Хорошо выраженная цепочка артефактов. Документы не просто архивируются: каждый становится входом для следующего рабочего процесса, что важно для AI-агентов с ограниченным и хрупким контекстом. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Есть масштабирование глубины: Quick Flow для малых изменений, полный BMad Method для продуктов и платформ, Enterprise для соответствия требованиям и мультитенантных систем. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- `project-context.md` даёт место для правил, которые агент плохо выводит сам: версии, запрещённые библиотеки, локальные паттерны, соглашения о тестировании. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- Контекст story создаётся перед реализацией и должен включать сведения из предыдущей story, git-сведения, соответствие архитектуре и список изменяемых файлов. Это отвечает на типичный сбой кодовых агентов: они реализуют локальный AC, но ломают существующее поведение. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- `sprint-status.yaml` делает состояние процесса видимым и машинно читаемым: backlog, ready-for-dev, in-progress, review, done. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md
- `bmad-help` снижает необходимость помнить весь каталог skill-файлов: он инспектирует состояние проекта и артефакты, а затем предлагает следующие обязательные/необязательные шаги. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md
- `bmad-spec` даёт компактную поверхность контракта для следующей работы: вместо того чтобы каждый следующий workflow заново читал все черновики и обсуждения, он может получить `SPEC.md` с коротким ядром и сопутствующие файлы для опорных деталей. Источник: https://docs.bmad-method.org/reference/core-tools/
- Для существующей кодовой базы BMAD предлагает не начинать с пустого PRD, а сначала привести в порядок старые планировочные артефакты, создать/проверить `project-context.md` и при необходимости запустить `bmad-document-project`. Это даёт методологии brownfield-вариант, где планирование опирается на актуальное фактическое состояние, а не на выдуманную архитектуру. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `bmad-document-project` делает brownfield-контекст воспроизводимее: состояние сканирования живёт в `project-scan-report.json`, сгенерированные документы связаны через `index.md`, а большой scan работает пакетно с промежуточной записью на диск. Это снижает риск, что агент "понял кодовую базу" только внутри исчезающего чата. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- `bmad-document-project` имеет отдельный чеклист валидации, который проверяет уровень сканирования, возобновляемость, запись по ходу работы, пакетную обработку, классификацию проекта, технологический стек, полноту сканирования источников, качество архитектуры, индекс/навигацию и готовность brownfield PRD. Это делает brownfield-документацию не просто "сгенерированным описанием", а проверяемым входом для следующего шага PRD/рабочего процесса. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- Страница Official Modules показывает, что BMAD масштабируется не только глубиной одного рабочего процесса BMM, но и подключаемыми предметными модулями. Для будущей теории это хороший пример "расширяемой методологии": базовый процесс остаётся artifact-first, а поверх него добавляются специализированные агенты и рабочие процессы, например TEA для тестирования корпоративного уровня. Источник: https://docs.bmad-method.org/reference/modules/
- `bmad-investigate` отделяет расследование от исправления. Для сложных багов это сильная сторона: ложные ветки, недостающие доказательства и опровергнутые гипотезы становятся частью case file, а не теряются в длинном чате с правками. Источник: https://docs.bmad-method.org/explanation/forensic-investigation/

## Риски, сбои и чрезмерное применение

- Для малых задач полный BMad Method может быть чрезмерным. Сама документация признаёт отдельный Quick Flow, который пропускает фазы 1-3 для малых, хорошо понятных изменений. Если команда всё равно запускает PRD + архитектуру + эпики + story-цикл для простого исправления, метод превращается в накладные расходы. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Обратный риск: Quick Dev может быть использован там, где уже нужна формальная цепочка планирования. Руководство Quick Fixes рекомендует полный BMad Method, когда изменение затрагивает несколько систем, требует согласованных правок во многих файлах, имеет неясный объём или нуждается в документированных архитектурных решениях. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- Выбор режима нельзя делать по количеству историй. Официальная оговорка "story counts are guidance, not definitions" нужна именно потому, что механическое следование числам может завести в слишком лёгкий или слишком тяжёлый процесс. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- Свежие чаты уменьшают загрязнение контекста, но создают зависимость от качества файловых артефактов. Если PRD, архитектура, `project-context.md` или story-файл неполные, следующий агент честно загрузит слабый контекст и будет уверенно продолжать ошибку.
- `project-context.md` является живым документом. Если архитектурные решения или соглашения меняются, а файл не обновляется, рабочие процессы реализации будут продолжать тянуть старые правила. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- В существующем проекте старые завершённые артефакты могут стать ложным контекстом, если их оставить в `docs/` или `_bmad-output/`. Официальное руководство прямо требует очистить завершённые планировочные артефакты перед дальнейшей работой. Источник: https://docs.bmad-method.org/how-to/established-projects/
- Репродуцируемость установки не гарантируется одной и той же командой на стабильном канале: новые выпущенные теги могут изменить установленные модули. Для повторяемости нужны `manifest.yaml` и `--pin`. Источник: https://docs.bmad-method.org/how-to/install-bmad/
- Версионная нестабильность имён уже видна в источниках: docs/tutorials могут говорить `bmad-create-prd`, а заметки к выпуску v6.7.0 - `bmad-prd` и shims до 7.0.0. Будущий текст должен либо фиксировать дату/версию, либо объяснять слой alias/shim, иначе читатель получит конфликтующие команды. Источники: https://docs.bmad-method.org/tutorials/getting-started/ и https://github.com/bmad-code-org/BMAD-METHOD/releases
- В реализации есть ручные стыки: после review пользователь должен обновить `sprint-status.yaml` до `done`; retrospective требует подтверждения эпика и может быть запущен частично. Эти места могут расходиться с реальным состоянием кода, если человек не дисциплинирован. Источники: https://docs.bmad-method.org/explanation/faq/implementation-faq/ и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- Архитектура тоже может стать источником сбоя. Официальная страница про Preventing Agent Conflicts называет три антипаттерна: неявные решения (`implicit decisions`), чрезмерное документирование (`over-documentation`) и устаревшая архитектура (`stale architecture`). То есть BMAD требует не просто один раз написать архитектуру, а документировать решения между эпиками, фокусироваться на зонах вероятных конфликтов, обновлять архитектуру по мере обучения и использовать `bmad-correct-course` для существенных изменений. Источник: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/
- `bmad-document-project` может создать ложную уверенность, если выбран Quick Scan там, где нужен Deep/Exhaustive Scan. В таком режиме рабочий процесс почти не читает исходные файлы и опирается на паттерны, манифесты и структуру каталогов; это полезно для обзора, но недостаточно для рискованных brownfield-изменений. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- `bmad-correct-course` защищает от тихого смещения курса, но сам добавляет организационную тяжесть. Для действительно малого отклонения (`small deviation`) он может быть чрезмерным; его чеклист явно рассчитан на существенные изменения направления проекта (`significant changes affecting project direction`) и требует доказательств, анализа влияния, предложения, утверждения и передачи. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md
- `bmad-investigate` не должен подменять реализацию. Skill прямо ограничивает себя диагностическим выводом и предлагает дальнейший маршрут только после заключения. Если команда ждёт от него автоматического исправления, процесс может показаться медленным; его ценность проявляется там, где важны след доказательств, воспроизводимость и передача расследования другому инженеру. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md
- Встроенный QA может дать ложное чувство полного тестового покрытия: страница Testing options прямо ограничивает его область генерацией тестов и рекомендует Code Review для валидации story. Для регулируемых/сложных доменов нужен TEA или иной полноценный слой тестовой стратегии; иначе быстрые API/E2E-тесты могут выглядеть как завершённый контроль качества, хотя это только один рабочий процесс после эпика. Источник: https://docs.bmad-method.org/reference/testing/
- TEA сам по себе добавляет существенную стоимость координации. Enterprise guide требует заранее определить ответственных участников, собирать доказательства, вести папки соответствия требованиям, поддерживать подписи утверждающих участников и политику хранения (`approver signatures and retention policy`). Для проектов без реальных требований соответствия, безопасности и NFR такой слой может стать процессной имитацией, а не полезной проверкой. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- У `bmad-document-project` есть отдельный риск ложной полноты: чеклист требует, чтобы документы не содержали обобщённых placeholders/TODO, а final validation включает утверждение пользователя и brownfield PRD readiness. Если команда не проходит этот чеклист, `index.md` и сгенерированные документы могут выглядеть официально, но не давать агенту нужных деталей API/data/state/security. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- Сигналы сообщества показывают реальные опасения по стоимости токенов, документационным накладным расходам и нестрогому следованию agent files, но это не первоисточник и требует отдельной проверки перед использованием в теории как факта. Кандидаты: ветки Reddit "BMAD method sucks", "Burning too many tokens with BMAD full flow", "BMAD is kinda messy?".

## Аналитические заметки предыдущих проходов

Эти заметки оставлены как исторический хвост предыдущих проходов. Они не являются основной структурой исходного досье и не должны автоматически маршрутизировать материал в будущие документы. При сборке теории их можно использовать только как вспомогательные наблюдения после повторного просмотра фактуры выше.

### Возможные выводы для теории
- BMAD как пример агентного SDLC с первичностью артефактов (`artifact-first`): не "дай агенту задачу", а "создай цепочку документов, где каждый следующий агент получает суженный и проверенный контекст".
- Различение BMAD Method и Quick Flow: BMAD не обязательно равен длинному ритуалу в духе waterfall; у него есть документированный короткий путь для малых хорошо понятных изменений.
- Quick Flow нужен в теории как отдельный режим, а не как короткая сноска: он принимает свободно сформулированное намерение, может строить короткую спецификацию, реализует, проверяет сам себя, делает локальный коммит и откладывает несвязанную или уже существовавшую работу в `deferred-work.md`. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- `bmad-spec` нужен как отдельный элемент BMAD-картины: это способ сжать разнообразные входы в `SPEC.md` с ядром и сопутствующими файлами, а не просто ещё одно имя для PRD. Источник: https://docs.bmad-method.org/reference/core-tools/
- Checkpoint Preview нужен как пример возвращения управления человеку после длинного автономного прохода: ревью человеком получает упорядоченный пошаговый разбор замечаний (`concerns`), участки с высоким blast radius и ручные проверки, а не сырой diff как единственный интерфейс понимания. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/
- Story-файл как ключевая операционная единица: create-story делает больше, чем нарезка требований; он собирает архитектуру, предыдущие уроки, git-контекст, файлы для изменения и свежие технические знания.
- `project-context.md` как аналог локальной "конституции" проекта: не общие best practices, а неочевидные правила конкретного проекта.
- Архитектуру в BMAD нужно описывать через предотвращение конфликтов агентов: стиль API, именование базы данных, управление состоянием, паттерны тестирования и другие решения между эпиками фиксируются до реализации, иначе несколько агентов могут честно реализовать несовместимые решения. Источник: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/
- Brownfield-угол: для существующих проектов BMAD начинается с очистки старых артефактов и генерации/вычитки `project-context.md`; иначе метод может формально работать, но кормить агентов устаревшим контекстом. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `bmad-document-project` как отдельный brownfield-механизм: из кодовой базы создаётся база знаний проекта с индексом, деревом исходников, архитектурой, документацией API/data/components и файлом состояния для возобновления, а не просто "агент прочитал репозиторий".
- В теории стоит показать `bmad-document-project` как сканирование с записью по ходу работы (`write-as-you-go scan`): файл состояния, пакетные сводки, немедленная запись документов и валидация по чеклисту. Это полезно для объяснения, как BMAD борется с исчезающим контекстом длинного сканирования кодовой базы. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- `sprint-status.yaml` как минимальная машина состояний между агентами и человеком.
- `bmad-sprint-status` как навигатор по этой машине состояний, ориентированный на чтение и ремонт: показывает следующее действие, риски устаревших/осиротевших статусов и уменьшает ручное чтение YAML.
- Проверка готовности и code review как контрмеры против уверенной, но несогласованной реализации.
- `bmad-correct-course` как формализованное перепланирование посреди спринта: доказательства → анализ влияния → дальнейший путь → предложенные правки артефактов → явное утверждение → передача.
- `bmad-investigate` как отдельная дисциплина диагностики: сначала `stronghold`, оценивание доказательств, не удаляемые гипотезы (`hypotheses never deleted`), backlog расследования, воспроизведение/направление исправления после вывода.
- Тестовый хвост лучше показывать двухслойно: встроенный QA как быстрый генератор тестов после эпика и TEA как отдельный модуль управления качеством для отслеживаемости, NFR, CI и release gate. Источник: https://docs.bmad-method.org/reference/testing/
- Enterprise-режим лучше раскрывать через жизненный цикл доказательств: NFR-пороги в PRD/test-design → тестовая инфраструктура и CI в проектном решении → TEA review/trace по каждому эпику → release gate → архивированные доказательства соответствия требованиям. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- Ограничение: эффективность метода зависит от качества исходных документов и дисциплины обновления файлов состояния/контекста.

### Возможные практические переносы в Handbook / Fieldbook
- Практический рецепт установки:

```bash
npx bmad-method install
bmad-help
```

- Когда выбирать Quick Flow, а когда полный BMad Method.
- Как запускать Quick Dev: свежий чат, намерение как текст/файл/URL issue, ответы на уточняющие вопросы, утверждение короткой спецификации, ревью diff, отправка в удалённый репозиторий, `git revert HEAD` при неудачной отправке.
- Как использовать `bmad-spec`: собрать бриф/PRD/RFC/стенограмму/смешанные входы, получить `SPEC.md` с ядром, проверить сопутствующие файлы и только затем отдавать контракт дальше по цепочке.
- Как проводить Checkpoint Preview после Quick Dev: открыть spec-след ревью, пройти ориентацию, пошаговый разбор замечаний (`concerns`), детальный проход по зонам высокого риска и ручные наблюдения перед решением отправить/переделать.
- Шаблон минимального `_bmad-output/project-context.md` для существующего проекта.
- Чеклист очистки для существующего проекта: убрать завершённые PRD/эпики и stories из `docs/`, `_bmad-output/planning-artifacts/`, `_bmad-output/implementation-artifacts/`; затем запустить или вручную подготовить `project-context.md`.
- Как выбирать уровень сканирования в `bmad-document-project`: Quick Scan для ориентации, Deep Scan для brownfield PRD, Exhaustive Scan для migration/audit.
- Как проходить чеклист валидации (`validation checklist`) `bmad-document-project`: проверить, что уровень сканирования выбран сознательно, критические каталоги прочитаны по типу проекта, детали API/data/state/UI/security собраны по флагам, `index.md` связан со сгенерированными документами, а утверждение пользователя получено до использования документов в brownfield PRD.
- Чеклист перед `bmad-create-story`: есть ли `prd.md`, `architecture.md`, epics, актуальный `sprint-status.yaml`, проектный контекст, последние изменения в git.
- Чеклист для архитектуры: какие решения между эпиками требуют ADR, где нужны указания по FR/NFR, какие соглашения naming/testing/state/API нельзя оставлять неявными.
- Шаблон использования `bmad-sprint-status`: когда смотреть статус, как интерпретировать риски, что делать с `review`, `in-progress`, `ready-for-dev` и устаревшим трекером.
- Как запускать `bmad-correct-course`: собрать триггерную story, доказательства, затронутые артефакты, выбрать прямую корректировку (`direct adjustment`), откат (`rollback`) или пересмотр PRD/MVP (`PRD MVP review`), получить явное утверждение и передать работу дальше.
- Как запускать `bmad-investigate`: дать ticket/log/stack trace/code area, согласовать slug, открыть case file, не просить сразу правку кода, а довести до вывода с оценкой доказательств.
- Когда достаточно встроенного QA, а когда нужен TEA: быстрое покрытие малых и средних задач против регулируемых/сложных проектов с отслеживаемостью и формальными gates.
- Как запускать жизненный цикл Enterprise TEA: определить ответственных участников, вписать NFR/compliance в PRD, сделать system-level `test-design`, подготовить фреймворк/CI/хранилище доказательств, обновлять trace по каждому эпику и закрывать выпуск через `nfr-assess` + `test-review` + `trace Phase 2`.
- Ритуал свежего чата на каждый рабочий процесс: PRD, архитектура, create-story, dev-story, code-review.
- Как руками проверить `sprint-status.yaml` после code review.
- Как не запускать полный BMAD для однофайлового исправления.

## Локальное различение: не путать BMAD с Gas Town

BMAD Method - установленный фреймворк skill-файлов, рабочих процессов и артефактов вокруг проекта: `_bmad/`, `_bmad-output/`, `bmad-help`, `bmad-prd`, `bmad-create-story`, `sprint-status.yaml`. Gas Town в текущей теоретической работе не нужно использовать как синоним BMAD: если Gas Town описывает другой режим или историю, BMAD должен остаться примером формализованного фреймворка рабочих процессов с проектными артефактами. Это локальное различение нужно только чтобы не смешать источники в будущем тексте; полноценное сравнение сюда не входит.

## Источники

- Официальный сайт BMad Method: https://www.bmadcode.com/bmad-method/  
  Роль: актуальная витрина проекта, экосистема модулей, команда установки, сигналы журнала изменений. Ограничение: маркетинговый слой, мало деталей рабочего процесса.
- GitHub-репозиторий `bmad-code-org/BMAD-METHOD`: https://github.com/bmad-code-org/BMAD-METHOD  
  Роль: первичный источник README, кода skill-файлов, структуры репозитория, issues. Ограничение: ветка `main` быстро меняется.
- Сырой README: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md  
  Роль: позиционирование, быстрый старт, предварительные требования, команды установки, модули, веб-бандлы.
- Сырой документ Workflow Map: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md  
  Роль: основная карта фаз, рабочих процессов, результатов и управления контекстом.
- Сырой документ Getting Started: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md  
  Роль: практическое руководство, режимы планирования, порядок фаз, дерево вывода, правило свежего чата, цикл сборки.
- Сырой документ Project Context: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md  
  Роль: объяснение `project-context.md`, когда создавать, что писать, какие рабочие процессы загружают.
- Руководство по установке: https://docs.bmad-method.org/how-to/install-bmad/  
  Роль: каналы установщика, manifest, pinning, лимиты GitHub API и диагностика проблем.
- Документация Core Tools: https://docs.bmad-method.org/reference/core-tools/  
  Роль: список core tools и описание `bmad-help`, brainstorming, party mode, помощников ревью, sharding/indexing, `bmad-spec` и контракта `SPEC.md`.
- Объяснение Quick Dev: https://docs.bmad-method.org/explanation/quick-dev/  
  Роль: человеческие контрольные точки в Quick Dev, утверждение спецификации, диагностика сбоя по слоям намерения, спецификации и реализации.
- Объяснение Checkpoint Preview: https://docs.bmad-method.org/explanation/checkpoint-preview/  
  Роль: ревью человеком после реализации, след ревью, участки с высоким blast radius, границы относительно тестов и вердикта pass/fail.
- Why Solutioning Matters: https://docs.bmad-method.org/explanation/architecture/why-solutioning-matters/  
  Роль: архитектура как защита от конфликтов между агентами и несогласованной реализации между эпиками.
- Preventing Agent Conflicts: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/  
  Роль: структура ADR, указания по FR/NFR, соглашения, устаревшая архитектура и антипаттерны чрезмерного документирования.
- Справочник Testing options: https://docs.bmad-method.org/reference/testing/  
  Роль: встроенный QA-рабочий процесс, модуль TEA, генерация API/E2E-тестов, отслеживаемость, NFR, CI и release gates.
- Диаграмма рабочего процесса: https://docs.bmad-method.org/workflow-map-diagram.html  
  Роль: визуальный поток артефактов, имена персон, поток контекста между create-story/dev-story/code-review/quick-dev.
- Implementation FAQ: https://docs.bmad-method.org/explanation/faq/implementation-faq/  
  Роль: статус done, параллельные истории, время ретроспективы, контекст create-story.
- Руководство Quick Fixes: https://docs.bmad-method.org/how-to/quick-fixes/  
  Роль: практическая граница `bmad-quick-dev`, свободно сформулированное намерение, утверждение короткой спецификации, самопроверка, локальный коммит, `deferred-work.md`, когда переходить к полному BMAD.
- Руководство Established Projects: https://docs.bmad-method.org/how-to/established-projects/  
  Роль: brownfield-рабочий процесс, очистка завершённых артефактов, `bmad-generate-project-context`, `bmad-document-project`, UX/architecture-оговорки для существующих кодовых баз.
- Объяснение Forensic Investigation: https://docs.bmad-method.org/explanation/forensic-investigation/  
  Роль: обоснование для `bmad-investigate`, граница диагностики и исправления, след доказательств, сценарии использования для сложных багов и production incidents.
- GitHub Releases / changelog: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md  
  Роль: актуальные изменения v6.7.0/v6.8.0, `bmad-prd`/`bmad-brief`, `bmad-ux`, `bmad-spec`, shim-слой старых PRD skill-файлов, активная зона несовпадения docs и заметок к выпуску.
- NewReleases mirrors for v6.7.0/v6.8.0: https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.7.0 и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.8.0  
  Роль: удобочитаемый снимок заметок к выпуску; использовать как вспомогательный источник к GitHub Releases, не как замену первоисточника.
- `bmad-help` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md  
  Роль: как help определяет состояние проекта, результаты и обязательные/необязательные следующие шаги.
- `bmad-sprint-planning` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md  
  Роль: машина состояний sprint-status, преобразование ключей story, проверки валидации.
- `bmad-sprint-status` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md  
  Роль: чтение и проверка `sprint-status.yaml`, маршрутизация следующего действия, обнаружение рисков, нормализация устаревших статусов.
- `bmad-create-story` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md  
  Роль: самый важный источник по контексту story, загрузка артефактов, сведения из предыдущей story и git, ограничители.
- `bmad-dev-story` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md  
  Роль: дисциплина реализации, разрешённые правки story-файла, `baseline_commit`, продолжение после ревью.
- `bmad-code-review` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md  
  Роль: слои состязательного ревью, step-file architecture и контрольные точки.
- `bmad-retrospective` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md  
  Роль: ревью после эпика, обработка частичной ретроспективы, непрерывность предыдущего retro, извлечение уроков.
- `bmad-correct-course` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md  
  Роль: рабочий процесс управления изменениями посреди спринта, стратегия загрузки, Sprint Change Proposal, точки утверждения и передачи.
- `bmad-correct-course` checklist raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md  
  Роль: анализ влияния, проверки конфликтов артефактов, выбор пути direct adjustment / rollback / PRD MVP review, ограничители явного утверждения.
- `bmad-investigate` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md  
  Роль: рабочий процесс расследования case, оценивание доказательств, обработка гипотез, граница только диагностики и маршрутизация передачи.
- `bmad-document-project` instructions raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md  
  Роль: маршрутизатор для документации проекта, состояние scan report, пути возобновления, нового запуска, повторного сканирования, deep-dive и архивации.
- Сырой файл инструкций full scan для `bmad-document-project`: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md  
  Роль: уровни сканирования, определение типа проекта, протокол файла состояния, набор сгенерированных документов, база знаний проекта с навигацией через index.
- `bmad-document-project` validation checklist: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md  
  Роль: полнота сканирования, запись по ходу работы, пакетная обработка, флаги из `documentation-requirements.csv`, готовность brownfield PRD, финальная проверка и утверждение пользователя.
- Official Modules: https://docs.bmad-method.org/reference/modules/  
  Роль: граница между core/BMM и официальными дополнительными модулями; TEA как отдельный модуль, а не обязательная часть каждого BMAD-рабочего процесса.
- Вводная документация TEA: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/  
  Роль: TEA как модуль Test Engineering Architect, быстрая установка, триггер agent/menu `bmad-tea`, основные рабочие процессы и граница helper `GATE`.
- enterprise-руководство TEA: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/  
  Роль: Enterprise-режим для compliance/security/audit/NFR, жизненный цикл по фазам, сбор доказательств, утверждающие участники, release gate и хранение.
- GitHub issue #1629: https://github.com/bmad-code-org/BMAD-METHOD/issues/1629  
  Роль: полезный, но не канонический разбор BMAD-архитектуры: исполнитель рабочего процесса, цикл меню агента, каскад конфигурации, манифесты. Использовать осторожно как артефакт обсуждения (`discussion artifact`), не как стабильную документацию.
- Кандидаты Reddit/community, непрочитанные глубоко и не первичные: "BMAD method sucks", "Burning too many tokens with BMAD full flow", "BMAD is kinda messy?", "I built auto-bmad".  
  Роль: кандидаты для будущего прохода по реальным рискам и трению внедрения (`adoption friction`); не использовать как подтверждение деталей без отдельного чтения.

- `documentation-requirements.csv` raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/documentation-requirements.csv  
  Роль: прямой источник по 12 типам проектов и схеме из 24 колонок для `bmad-document-project`; закрывает прежний вопрос о полной таблице флагов типов проектов и паттернов сканирования.
- Сырой файл deep-dive instructions для `bmad-document-project`: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/deep-dive-instructions.md  
  Роль: граница deep-dive режима: буквальное полное чтение файлов выбранной области (`literal full-file review`), без выборочного чтения и догадок.
- Обёртка full scan для `bmad-document-project`: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-workflow.md  
  Роль: показывает, что full scan является отдельным подпроцессом (`sub-workflow`) с загрузкой конфигурации, `communication_language`, `document_output_language` и gate-точками пользовательского ввода.
- Внешняя оценка “I Tested Three Spec-Driven AI Tools. Here’s My Honest Take”: https://ranthebuilder.cloud/blog/i-tested-three-spec-driven-ai-tools-here-s-my-honest-take/  
  Роль: не первоисточник, но конкретный сравнительный отчёт опыта по BMAD Full / BMAD Quick / Spec-Kit / OpenSpec на одной фиче; полезен для рисков времени, стоимости, ревью и параллельной работы. Ограничение: авторская оценка, не BMAD-документация.
- Ветка Reddit “Burning too many tokens with BMAD full flow”: https://www.reddit.com/r/ClaudeCode/comments/1rurgdd/burning_too_many_tokens_with_bmad_full_flow/  
  Роль: слабый сигнал сообщества по токенным накладным расходам полного BMAD flow; использовать только как анекдотический сигнал риска, не как статистику.
- GitHub issue #511 “big tokens cost”: https://github.com/bmad-code-org/BMAD-METHOD/issues/511  
  Роль: сигнал уровня issue о повторном чтении файлов и стоимости токенов в `/dev`; слабый источник, но полезен для сценариев сбоя.
- GitHub issue #813 про `document-project` path/reference failure: https://github.com/bmad-code-org/BMAD-METHOD/issues/813  
  Роль: пример хрупкости между инструментами и путями в v6 document-project; использовать осторожно, потому что issue относится к конкретной версии/среде.
- Ветка Atlassian community про поддержку Rovo Dev: https://community.developer.atlassian.com/t/rovo-dev-support-in-bmad-method/99157  
  Роль: слабый, но показательный источник по трудности матрицы поддержки для агентных IDE: сопровождающий пишет, что поддержку Rovo Dev хочется сохранять, но основная команда не использует его активно.
- Secondary comparison BMAD / Claude Flow / Gas Town: https://re-cinq.com/blog/multi-agent-orchestration-bmad-claude-flow-gastown  
  Роль: внешнее обрамление для компромисса “documentation vs memory vs git persistence”; не использовать как первичный источник деталей BMAD.

## Поисковые формулировки

- `BMAD Method official documentation GitHub BMAD Method AI software development`
- `BMAD Method bmad-code-org BMAD-METHOD GitHub docs`
- `site:github.com BMAD METHOD BMad Method README`
- `site:docs.bmad-method.org BMad "architecture" "sprint-status.yaml" "project-context.md"`
- `site:docs.bmad-method.org BMad "bmad-correct-course" "sprint-status.yaml"`
- `BMAD-METHOD "bmad-create-story" "story-[slug].md"`
- `BMAD Method workflow map project-context.md create-story dev-story code-review`
- `BMAD Method "bmad-prd" "bmad-create-prd" shim v6.7`
- `BMAD Method "bmad-ux" "DESIGN.md" "EXPERIENCE.md" v6.8`
- `site:docs.bmad-method.org BMAD "established projects" "bmad-generate-project-context"`
- `BMAD-METHOD "bmad-document-project" "project-scan-report.json" "index.md"`
- `BMAD-METHOD "full-scan-instructions" "documentation-requirements.csv"`
- `site:docs.bmad-method.org BMAD "quick fixes" "deferred-work.md"`
- `site:docs.bmad-method.org BMAD "bmad-spec" "SPEC.md" "Success signal"`
- `site:docs.bmad-method.org BMAD "checkpoint-preview" "blast radius"`
- `site:docs.bmad-method.org BMAD "preventing agent conflicts" ADR`
- `site:docs.bmad-method.org BMAD "TEA" "Traceability" "Release Gate"`
- `BMAD-METHOD "bmad-correct-course" "sprint-change-proposal"`
- `BMAD-METHOD "Change Navigation Checklist" "PRD MVP review"`
- `BMAD-METHOD "bmad-sprint-status" "legacy_status_map"`
- `BMAD-METHOD "bmad-investigate" "Confirmed" "Deduced" "Hypothesized"`
- `site:docs.bmad-method.org BMAD "forensic investigation" "diagnosis"`
- `site:docs.bmad-method.org BMAD "Official Modules" "Test Architect" "tea"`
- `site:bmad-code-org.github.io/bmad-method-test-architecture-enterprise "release gate" "nfr-assess" "trace Phase 2"`
- `BMAD-METHOD "bmad-document-project" "requires_api_scan" "Brownfield PRD Readiness"`
- `BMAD-METHOD "config.user.toml" "legacy" "_bmad/<module>/config.yaml"`
- `BMAD Method token cost full flow`
- `BMAD Method documentation messy agent files`

- `BMAD Method external evaluation BMAD Quick OpenSpec Spec-Kit cost time PR`
- `BMAD Method "Burning too many tokens" "full flow"`
- `BMAD-METHOD "big tokens cost" issue`
- `BMAD Method document-project "documentation-requirements.csv" raw`
- `BMAD Method "Deep-Dive Documentation Instructions" "literal full-file review"`
- `BMAD Method Gemini CLI document-project missing files issue`
- `BMAD Claude Flow Gas Town comparison BMAD planning tokens`

## Кандидаты на иллюстрации

- Official Workflow Map Diagram: https://docs.bmad-method.org/workflow-map-diagram.html  
  Что изображено: четыре фазы, персоны, стрелки артефактов, Quick Flow, поток контекста.  
  Зачем пригодится: основная схема для будущего объяснения "документ становится входом следующего шага".  
  Где использовать: теория или раздел Handbook про рабочий процесс BMAD.  
  Статус: кандидат; перед публикацией проверить права/лицензию и возможность пересобрать собственную схему.
- Дерево вывода из Getting Started (`_bmad/`, `_bmad-output/planning-artifacts`, `_bmad-output/implementation-artifacts`, `project-context.md`).  
  Что изображено: файловая рамка установленного проекта.  
  Зачем пригодится: показать, что метод живёт в репозитории как артефакты/config, а не только в чате.  
  Где использовать: Handbook/Fieldbook.  
  Статус: лучше перерисовать самостоятельно.
- Машина состояний sprint status из `bmad-sprint-planning`: статусы Epic, Story, Retrospective.  
  Что изображено: `backlog → ready-for-dev → in-progress → review → done`.  
  Зачем пригодится: показать жизненный цикл между агентами и человеком.  
  Где использовать: теория или практический раздел.  
  Статус: лучше сделать собственную компактную схему.
- Диаграмма потока контекста: PRD → архитектура → story → разработка → ревью.  
  Что изображено: переходы контекста по BMAD.  
  Зачем пригодится: объяснить отличие рабочего процесса с первичностью артефактов (`artifact-first`) от кодинга в одном чате.  
  Где использовать: теория.  
  Статус: создать собственную иллюстрацию на основе источников.
- Диаграмма границы Quick Dev.  
  Что изображено: свободно сформулированное намерение → утверждение короткой спецификации → реализация/ревью/commit → ревью diff/отправка; отдельно стрелка в `deferred-work.md` для несвязанной или уже существовавшей работы и стрелка "переход к полному BMAD" при изменениях с несколькими системами или неясным объёмом.  
  Зачем пригодится: показать, что Quick Flow не просто "без документов", а отдельный малый жизненный цикл.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Диаграмма сжатия SPEC.  
  Что изображено: бриф/PRD/RFC/стенограмма/смешанные входы → `SPEC.md` с ядром (`Why`, `Capabilities`, `Constraints`, `Non-goals`, `Success signal`) + сопутствующие файлы → следующие рабочие процессы.  
  Зачем пригодится: показать, что BMAD умеет не только расширять документы, но и сжимать разношёрстный вход в компактный контракт.  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.
- Диаграмма границы QA/TEA.  
  Что изображено: после эпика → встроенные QA API/E2E-тесты; отдельная ветка к TEA для отслеживаемости, NFR, CI и release gate.  
  Зачем пригодится: не дать читателю принять быструю генерацию тестов за полноценное управление качеством.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Диаграмма brownfield-сканирования.  
  Что изображено: репозиторий → `project-scan-report.json` → уровень сканирования → сгенерированные документы (`project-overview.md`, `architecture.md`, `component-inventory.md`, `index.md`) → загрузка на следующих шагах другими рабочими процессами.  
  Зачем пригодится: показать, что BMAD в brownfield-работе строит базу знаний проекта, а не полагается на разовое чтение кода.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Диаграмма проверки Document Project.  
  Что изображено: уровень сканирования → флаги типов проекта (`requires_api_scan`, `requires_data_models`, `requires_state_management`, `requires_ui_components`) → пакетная запись по ходу работы → чеклист → утверждение пользователя → готовность brownfield PRD.  
  Зачем пригодится: показать, что сгенерированные документы должны пройти явную проверку полноты, а не просто появиться в папке знаний проекта (`project knowledge`).  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Диаграмма решения Correct Course.  
  Что изображено: триггерная story/проблема → анализ влияния → прямая корректировка (`direct adjustment`) / откат (`rollback`) / пересмотр PRD MVP (`PRD MVP review`) → Sprint Change Proposal → утверждение → передача.  
  Зачем пригодится: объяснить перепланирование посреди спринта как отдельный жизненный цикл, а не как "попросить агента переделать".  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.
- Лестница доказательств расследования.  
  Что изображено: сырые доказательства → Confirmed наблюдениями → Deduced наблюдениями → Hypothesized branches → уверенность вывода → маршрут к quick-dev/correct-course/create-story/code-review.  
  Зачем пригодится: показать границу расследования и исправления в BMAD.  
  Где использовать: Fieldbook.  
  Статус: создать собственную схему.
- Диаграмма release gate для Enterprise TEA.  
  Что изображено: PRD NFR/compliance → system-level `test-design` → framework/CI/хранилище доказательств → review/trace по каждому эпику → `nfr-assess` + полный `test-review` + `trace Phase 2` → `PASS/CONCERNS/FAIL/WAIVED` → архив соответствия.  
  Зачем пригодится: показать, что Enterprise-режим строит жизненный цикл доказательств и утверждений, а не просто добавляет "безопасность + DevOps" строкой в режиме планирования.  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.

- Диаграмма компромисса стоимости и глубины BMAD.  
  Что изображено: `BMAD Full` как глубокий путь планирования/доказательств, `BMAD Quick` как компактный путь спецификации/реализации, рядом внешние риски проверяемости, времени и стоимости.  
  Зачем пригодится: показать, что BMAD не должен применяться одинаково к любой задаче.  
  Где использовать: теория или Fieldbook.  
  Статус: создать собственную схему; внешнюю оценку использовать только как один опыт, не как норму.
- Диаграмма устойчивости BMAD vs Gas Town.  
  Что изображено: BMAD сохраняет решение в PRD/architecture/story/status docs; Gas Town сохраняет долгоживущую работу через Git-backed orchestration.  
  Зачем пригодится: уточнить локальное различение “документальная передача” против “durable task/orchestration layer”.  
  Где использовать: Cross-Story / теория.  
  Статус: кандидат; не рисовать без сверки с Gas Town dossier.

## Открытые вопросы

- Насколько стабильны названия skill-файлов и структура `_bmad/` между релизами v6? README и docs указывают на быструю эволюцию и канал предварительных выпусков; нужно проверять перед финальным текстом.
- Как именно BMad Method соотносится с BMad-CORE и BMad Ecosystem в текущей версии: где заканчивается BMM и начинается общий core-слой?
- Насколько часто реальные команды используют полный Method-режим, а не Quick Flow или внешние автоматизаторы? Этот проход нашёл несколько внешних сигналов, но они остаются анекдотическими / сравнительными, а не статистикой. Нужен отдельный проход по отчётам опыта (`experience reports`), если BMAD станет крупной частью теории.
- Насколько отчёты сообщества об опыте (`community experience reports`) подтверждают устойчивую стратегию “BMAD Full for planning, lean/quick flow for execution”? Пока это видно как гипотеза из Reddit/внешней оценки, но не как доказанная практика.
- Вопрос о прямом доступе к `documentation-requirements.csv` в этом проходе закрыт: raw-файл прочитан, таблица содержит 12 типов проектов и схему из 24 колонок. Остаётся не вопрос доступа, а вопрос, насколько подробно эту таблицу переносить в финальную теорию: вероятно, достаточно показать 3–4 флага и сам принцип управляемого данными руководства по сканированию.
- Каков текущий статус интеграции Enterprise Security/DevOps в v6 за пределами TEA: testing/compliance/CI частично прояснены через enterprise-руководство TEA, но отдельные Security/DevOps modules или рабочие процессы (`workflows`), если они есть, требуют дополнительной сверки.
- Как синхронизировать именование в финальном тексте: `bmad-create-prd` в части docs против `bmad-prd` в заметках к выпуску v6.7+ и формулировок v6.8 вокруг web-bundle?
- Нужно ли описывать `bmad-investigate` как часть core BMAD Method или как необязательный рабочий процесс на стороне реализации (`implementation-side workflow`): источник присутствует в BMM implementation skills, но для финального сайта важно не перегрузить основной рассказ.
- Какие права на использование официальной диаграммы рабочего процесса и баннера? Для сайта лучше делать свою схему.
