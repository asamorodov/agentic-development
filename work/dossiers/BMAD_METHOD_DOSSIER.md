# BMAD Method

## Черновое назначение

Документ создан режимом fresh для накопления материала из первоисточников.

Досье собирает BMAD Method как рабочий процесс AI-driven SDLC: какие файлы метод создаёт, как они становятся контекстом для следующих шагов, где человек выбирает направление, где агентам дают готовый контекст, какие проверки и статусы удерживают работу от расползания. Это рабочий буфер для будущего текста сайта, а не финальная карточка методологии.

## Роль в AI-driven SDLC

BMAD Method описывает себя как open-source AI-native development framework и модуль BMad Method (BMM) внутри BMad Ecosystem. В README текущего репозитория он позиционируется как AI-driven agile development module, который должен адаптироваться от исправлений и малых фич до enterprise-систем. Практически это не один запрос, а установленный набор skills, агентов, рабочих процессов и файловых артефактов, которые живут в проекте после команды `npx bmad-method install`. Источник: https://github.com/bmad-code-org/BMAD-METHOD и raw README https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

Страница Official Modules помогает точнее развести BMM и остальную экосистему. Встроенный core и BMM остаются базой Agile-разработки, а дополнительные modules выбираются при установке и добавляют специализированных агентов, рабочие процессы и задачи поверх базовой рамки. Среди официальных модулей перечислены BMad Builder (`bmb`), Creative Intelligence Suite (`cis`), Game Dev Studio (`gds`) и Test Architect (`tea`). Для BMAD-досье это означает: TEA и BMad Builder нельзя описывать как обязательную часть каждого BMAD-проекта, но они являются официальными расширениями той же установочной и агентной модели. Источник: https://docs.bmad-method.org/reference/modules/

Для будущей теории важна не маркетинговая формула "AI-native", а устройство процесса: BMAD пытается заменить свободное общение с coding agent последовательностью документальных переходов. Сначала создаются или уточняются требования, затем архитектура, затем epics/stories, затем story-файлы используются как узкий контекст для реализации. Официальная Workflow Map описывает это как постепенное наращивание контекста через четыре фазы: каждый этап и каждый рабочий процесс производит документы, которые информируют следующий этап. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

## Проблема, которую решает

Главная проблема BMAD - нестабильность агентной разработки, когда AI IDE получает слишком общий запрос, сам додумывает требования, путает архитектурные решения, теряет контекст между задачами и делает разные решения в разных story. Официальный текст про `project-context.md` описывает это прямо: без явного контекста агенты могут применять общие практики, не совпадающие с кодовой базой, принимать непоследовательные решения между stories и пропускать проектные ограничения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

BMAD решает эту проблему через два слоя. Первый слой - фазовое накопление документов: product brief или PRFAQ, PRD, UX-документы, architecture, epics, story-файлы. Второй слой - установленная инфраструктура skills и конфигурации: `_bmad/` хранит agents, workflows, tasks and configuration, а `_bmad-output/` хранит созданные артефакты. Getting Started показывает эту пару каталогов как результат установки. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

## Установка и файловая рамка

Базовая установка:

```bash
npx bmad-method install
```

Текущий README указывает prerequisites: Node.js v20.12+, Python 3.10+ и `uv`; для prerelease-канала предлагается `npx bmad-method@next install`, с явной оговоркой про более высокую изменчивость. Для CI/CD или повторяемой установки есть non-interactive вариант:

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

Опции модуля можно переопределять через повторяемый `--set <module>.<key>=<value>`, например `--set bmm.project_knowledge=research` и `--set bmm.user_skill_level=expert`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

После установки ожидаемая рамка проекта выглядит так:

```text
your-project/
├── _bmad/                       # BMad configuration
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

Getting Started подчёркивает, что `_bmad/` содержит agents, workflows, tasks and configuration, а `_bmad-output/` является местом сохранения артефактов. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Установка имеет reproducibility-оговорки. В install guide сказано, что `_bmad/_config/manifest.yaml` записывает установленные модули, версии, канал, sha и repoUrl для git-backed modules. Stable-channel install при повторном запуске может подтянуть более новый released tag; для воспроизводимости нужно переводить зафиксированные версии из manifest в явные `--pin` flags. Там же указано ограничение GitHub API: anonymous calls ограничены 60/hour per IP, и для офисов, CI runners или VPN может понадобиться `GITHUB_TOKEN`. Источник: https://docs.bmad-method.org/how-to/install-bmad/

В release notes v6.8.0 есть важная версионная оговорка по слою конфигурации: установщик при повторном запуске теперь сначала читает центральный TOML, включая `_bmad/config.user.toml`, и только затем использует прежний `_bmad/<module>/config.yaml` как fallback. Это подтверждает, что структура `_bmad/` в v6 ещё эволюционирует; для финального текста лучше фиксировать дату/версию и не превращать конкретный путь config-файла в вечное свойство метода. Источник: https://github.com/bmad-code-org/BMAD-METHOD/releases

## Planning tracks

BMAD предлагает три planning tracks, которые выбираются не только по числу stories, а по потребности в планировании:

- `Quick Flow` - исправления, простые фичи, ясный объём, ориентир 1-15 stories, создаёт только tech-spec.
- `BMad Method` - продукты, платформы, сложные фичи, ориентир 10-50+ stories, создаёт PRD + Architecture + UX.
- `Enterprise` - compliance, multi-tenant systems, ориентир 30+ stories, добавляет Security + DevOps к PRD и Architecture.

Документация отдельно предупреждает: числа stories являются ориентиром, а не определением; track нужно выбирать по потребности в планировании, а не механически по размеру. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Enterprise track в текущей документации лучше читать вместе с TEA, а не только как "больше документов". TEA enterprise guide говорит, что такой режим нужен для compliance, security-critical applications, требований к audit trail и строгих NFR-порогов. Предпосылки: BMAD установлен с выбранным Enterprise track, TEA agent доступен, compliance requirements документированы, а ответственные участники для gate approvals известны заранее. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

Для теории это важная оговорка. BMAD не всегда требует полного длинного цикла: для малых и хорошо понятых изменений Quick Flow пропускает phases 1-3 и использует `bmad-quick-dev`, который должен пройти intent -> tech-spec -> working code. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md и https://docs.bmad-method.org/workflow-map-diagram.html

Официальная страница Quick Fixes уточняет практическую границу Quick Flow. `bmad-quick-dev` подходит для исправлений ошибок с ясной причиной, небольших рефакторингов в нескольких файлах, малых корректировок фич и обновлений зависимостей. Входом может быть свободный текст, путь к файлу с intent, GitHub issue URL или ссылка на трекер ошибок; workflow может задать уточняющие вопросы или показать короткую spec на утверждение перед реализацией. Результат ожидается как изменённые исходные файлы, пройденные тесты при их наличии и локальный commit, готовый к отправке, с conventional commit message. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Та же страница задаёт явный порог перехода к полному BMAD: если изменение затрагивает несколько систем, требует согласованных правок во многих файлах, имеет неясный объём или команде нужно сохранить требования и архитектурные решения для других участников, Quick Dev уже недостаточен. Это важнее, чем численный ориентир 1-15 stories: сам источник описывает переход через характер риска и потребность в предварительном прояснении задачи. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Объяснение Quick Dev уточняет, где именно остаётся человек. Workflow сначала сжимает исходное намерение в одну непротиворечивую цель, затем выбирает минимальный безопасный путь: совсем малое изменение может идти сразу в реализацию, всё остальное проходит через spec approval. Человеческие точки контроля вынесены в intent clarification, утверждение spec и review of final product; при сбое workflow должен определить, где возникла ошибка - в исходном intent, в слабой spec или в локальной реализации, - и возвращаться на соответствующий слой, а не чинить любой дефект прямо в diff. Источник: https://docs.bmad-method.org/explanation/quick-dev/

## Workflow: четыре фазы

### Phase 1: Analysis, optional

Цель - исследовать пространство проблемы и проверить идеи до обязательного планирования. Workflow Map перечисляет:

- `bmad-brainstorming` - guided brainstorming, результат `brainstorming-report.md`.
- `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` - проверка domain, market или technical assumptions, результат research findings.
- `bmad-product-brief` - фиксация strategic vision, результат `product-brief.md`.
- `bmad-prfaq` - Working Backwards для stress-test product concept, результат `prfaq-{project}.md`.

Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

В диаграмме workflow эти шаги связаны с agent/persona Mary; product brief и PRFAQ ведут стрелкой в Planning. Источник: https://docs.bmad-method.org/workflow-map-diagram.html

### Phase 2: Planning, required

Цель - определить, что строить и для кого. Для BMad Method и Enterprise track основной workflow - `bmad-prd`. Он имеет три intent:

- Create - управляемое discovery с нуля, результат `prd.md`, `addendum.md`, `decision-log.md`.
- Update - сверка существующего PRD с change signal, с выявлением конфликтов до применения изменений.
- Validate - проверка готового PRD по настраиваемому checklist, результат `validation-report.html` и `.md`.

Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Версионная оговорка по именам skills: часть официальной документации всё ещё показывает `bmad-create-prd`, а релизы v6.7.0 описывают переход к единому `bmad-prd` с intent Create/Update/Validate. В v6.7.0 старые create/edit/validate PRD skills сохранены как совместимые shim-обёртки, которые маршрутизируют в единый PRD skill, но заявлено, что эти обёртки должны быть удалены в 7.0.0. Это нужно сохранить в досье, чтобы будущий текст не выглядел устаревшим и одновременно не спорил с текущими tutorial pages. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.7.0

Core Tools вводит ещё один контрактный слой - `bmad-spec`. Он принимает brief, PRD, GDD, RFC, свободный dump, transcript, UX-папку или смешанный набор входов и сжимает их в `SPEC.md`: five-field kernel `Why`, `Capabilities`, `Constraints`, `Non-goals`, `Success signal`. Всё важное, что не помещается в ядро, уходит в companion files. Это не замена полному PRD во всех случаях, а компактный downstream contract, полезный там, где нужно зафиксировать WHAT before HOW и дать агентам короткий, пригодный для загрузки контракт вместо чтения всех upstream artifacts. Источник: https://docs.bmad-method.org/reference/core-tools/

Если продукт имеет UI, документация предлагает вызвать UX-Designer agent `bmad-agent-ux-designer` и запустить `bmad-ux` после PRD. Workflow Map описывает результат как пару `DESIGN.md` + `EXPERIENCE.md` и `.decision-log.md`: visual spine и behavioral spine. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

В v6.8.0 `bmad-ux` описан как замена старого single-spine UX skill: новый контракт разделяет `DESIGN.md` с визуальной идентичностью и `EXPERIENCE.md` с поведением, потоками, информационной архитектурой, состояниями и доступностью. Релиз подчёркивает, что handoff из дизайна в engineering должен быть sealed file contract, а не неформальным переводом намерений между агентами. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.8.0

### Phase 3: Solutioning

Для BMad Method и Enterprise track после PRD создаётся architecture:

- `bmad-create-architecture` через Architect agent `bmad-agent-architect`; результат - architecture document with technical decisions, в Workflow Map: `architecture.md` with ADRs.
- `bmad-create-epics-and-stories` через PM agent `bmad-agent-pm`; рабочий процесс использует PRD и Architecture, чтобы создать technically-informed stories.
- `bmad-check-implementation-readiness` через Architect agent; рекомендуемая gate check перед implementation, проверяющая согласованность planning documents и возвращающая PASS/CONCERNS/FAIL decision.

Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

Важная деталь v6: epics and stories теперь создаются после architecture. Документация объясняет это тем, что architecture decisions - database, API patterns, tech stack - прямо влияют на разбиение работы. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Официальное объяснение solutioning формулирует проблему через multi-agent conflicts: без общего architecture Agent 1 может реализовать Epic 1 через REST API, Agent 2 - Epic 2 через GraphQL, и интеграция станет несогласованной. Страница про preventing agent conflicts раскрывает механизм: ADR фиксирует context, considered options, decision, rationale and consequences; architecture также задаёт FR/NFR-specific guidance, directory structure, naming conventions, code organization и testing patterns. Источник: https://docs.bmad-method.org/explanation/architecture/why-solutioning-matters/ и https://docs.bmad-method.org/explanation/preventing-agent-conflicts/

Для Enterprise track solutioning получает тестово-комплаенсный хвост ещё до реализации. TEA guide предлагает на Phase 3 совместить architecture с `test-design` в system-level mode: проверить тестируемость security architecture, стратегию performance testing и связь compliance requirements с тестами. Отдельно планируются test infrastructure и CI/CD: разделённые test environments (`dev`, `staging`, `prod-mirror`), безопасная работа с test data для PHI/PII, audit logging in tests, управление секретами, изоляция тестов, хранение артефактов и access controls for production tests. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

### Phase 4: Implementation

Implementation строится story by story и обычно в fresh chats. Getting Started требует после завершения planning переходить к implementation и запускать каждый рабочий процесс в свежем чате. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Цикл:

- `bmad-sprint-planning` создаёт `sprint-status.yaml`, чтобы отслеживать epics and stories.
- `bmad-create-story` создаёт отдельный story file из epic.
- `bmad-dev-story` реализует story.
- `bmad-code-review` выполняет quality validation, recommended.
- после завершения всех stories в epic запускается `bmad-retrospective`.

Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md

Workflow Map добавляет дополнительные implementation workflows: `bmad-correct-course` для существенных изменений посреди sprint, `bmad-sprint-status` для обновления sprint status и `bmad-investigate` для forensic case investigation с результатом `{slug}-investigation.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

`bmad-correct-course` устроен как workflow управления изменениями, а не как быстрый фикс кода. Его собственный skill требует широкий проектный контекст: PRD и Epics обязательны, Architecture, UX, Spec и Document Project загружаются при наличии; sharded documents сначала раскрываются через `index.md`, а для Document Project применяется index-guided loading только релевантных секций. Результат пишется в `{planning_artifacts}/sprint-change-proposal-{date}.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md

Change Navigation Checklist внутри `bmad-correct-course` заставляет пройти шесть групп вопросов: что именно стало trigger story/problem, как это влияет на текущий epic и будущие epics, какие конфликты появились в PRD/Architecture/UI/UX/CI/CD/testing/docs, какой путь выбрать - direct adjustment, rollback или PRD MVP review, какие конкретные правки нужны в artifacts, и кто дальше отвечает за handoff. Важная точка человеческого контроля: workflow не должен продолжать proposal без complete impact analysis, не должен выполнять изменения без explicit approval и должен явно определить, кто исполняет предложенные изменения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md

`bmad-sprint-status` закрывает другой промежуточный разрыв: он не создаёт новую работу, а читает `{implementation_artifacts}/sprint-status.yaml`, классифицирует ключи как epics, stories и retrospectives, нормализует legacy statuses (`drafted` -> `ready-for-dev`, `contexted` -> `in-progress`), считает статусы, ищет риски и рекомендует следующий workflow. Его приоритеты простые: сначала продолжить `in-progress` story через `dev-story`, затем отправить `review` story в `code-review`, затем взять `ready-for-dev`, затем создать story из backlog, затем retrospective. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md

Для Quick Dev хвост реализации устроен иначе, чем для story loop. Quick Fixes говорит, что workflow сам реализует изменение, проверяет собственную работу, исправляет найденные проблемы и делает локальный commit; после этого человеку нужно просмотреть diff, подтвердить соответствие исходному намерению и отправить commit в remote. Если уже отправленное изменение вызвало неожиданные проблемы, документация предлагает `git revert HEAD`, затем fresh chat и новый запуск Quick Dev. Источник: https://docs.bmad-method.org/how-to/quick-fixes/

Встроенный QA workflow появляется именно в Phase 4, но не как замена code review. Страница Testing options говорит, что `bmad-qa-generate-e2e-tests` доступен через Developer agent (`QA`) и обычно запускается после завершения полного epic, когда все stories реализованы и прошли code review. Он определяет test framework по `package.json` и существующим тестам, выбирает или обнаруживает функции, генерирует API and E2E tests, запускает их и чинит базовые сбои. Источник: https://docs.bmad-method.org/reference/testing/

TEA enterprise lifecycle расширяет Phase 4 по каждому epic: `test-design` в epic-level mode для compliance/security/performance, необязательный `atdd` для acceptance tests, обычная реализация story, `automate` для расширения покрытия, `test-review` с quality score и `trace Phase 1` для обновления coverage. На release gate порядок становится ещё строже: `nfr-assess`, полный `test-review`, затем `trace Phase 2` с решением `PASS/CONCERNS/FAIL/WAIVED`; для Phase 2 gate нужны фактические результаты выполнения тестов, иначе gate step пропускается. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

Enterprise guide показывает, какие артефакты становятся доказательствами: `traceability-matrix.md`, `test-review.md`, `nfr-assessment.md`, `gate-decision-release-{version}.md`, результаты тестов, отчёты о покрытии, security scans и подписи утверждающих участников. Он даже предлагает пример папки `compliance/{period}/release-{version}/` и ориентиры хранения вроде 7 years for HIPAA или 3 years for SOC 2. Для теории это важно: Enterprise BMAD переносит "качество" из устного доверия к агенту в архивируемый evidence package, где у каждого решения есть проверяемое происхождение. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

`bmad-investigate` вводит отдельную ветку расследования внутри Phase 4. Skill принимает ticket ID, log file, diagnostic archive, error message, code area name, problem description или путь к существующему case file; старый case можно возобновить, а новый записывается как `{implementation_artifacts}/{workflow.case_file_subdir}/{workflow.case_file_filename}`. Принципиальная граница: investigation останавливается на diagnosis; для дальнейшего действия skill предлагает `bmad-quick-dev`, `bmad-correct-course`, `bmad-create-story` или `bmad-code-review` в зависимости от вывода. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md и https://docs.bmad-method.org/explanation/forensic-investigation/

## Артефакты и как они становятся входами

Ключевая цепочка:

```text
brainstorming-report.md / research findings / product-brief.md / prfaq-{project}.md
→ prd.md + addendum.md + decision-log.md
→ DESIGN.md + EXPERIENCE.md + .decision-log.md, если нужен UX
→ architecture.md with ADRs
→ epics / stories
→ sprint-status.yaml
→ story-[slug].md
→ working code + tests
→ code-review: approved or changes requested
→ QA / TEA tests after epic, если нужны дополнительные тесты
→ retrospective: lessons learned
```

Диаграмма workflow показывает стрелки artifact flow: `product-brief.md` или `prfaq.md` ведут к `prd.md`, затем UX и architecture ведут к epics, затем `sprint-status.yaml`, `story-[slug].md`, code, approval, updated plan и lessons. Источник: https://docs.bmad-method.org/workflow-map-diagram.html

Контекстный переход зафиксирован явно: PRD сообщает architect, какие constraints важны; architecture сообщает dev agent, какие patterns follow; story files дают focused, complete context для implementation. Без такой структуры, по формулировке Workflow Map, agents make inconsistent decisions. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md

`SPEC.md` добавляет более короткий контекстный переход для задач, где полный набор upstream documents слишком тяжёлый: он хранит ядро намерения, возможностей, ограничений, non-goals и success signal, а companion files удерживают тяжёлые детали отдельно. Для теории это полезно как пример двухскоростного контекста: компактный контракт для обычного downstream consumption и отдельные материалы для случаев, когда агенту нужно глубже читать происхождение решения. Источник: https://docs.bmad-method.org/reference/core-tools/

## Контекст

BMAD делит контекст на несколько уровней:

- Документы planning chain: PRD, UX, architecture, epics, story files.
- Project-wide rules в `_bmad-output/project-context.md`.
- Runtime/config слой в `_bmad/`, включая module config and skill customization.
- Sprint state в `_bmad-output/implementation-artifacts/sprint-status.yaml`.
- Review trail в Quick Dev / Checkpoint Preview: spec file после Quick Dev может содержать suggested review order, который используется как карта чтения изменений; если такого trail нет, workflow генерирует его из diff и codebase context. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/

`project-context.md` особенно важен для переноса в теорию. Он описан как implementation guide для AI agents: technology stack and versions, critical implementation rules, conventions and preferences. Он автоматически загружается implementation workflows, если существует; architect workflow тоже загружает его, чтобы учитывать technical preferences during solutioning. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

Создать `project-context.md` можно вручную в `_bmad-output/project-context.md` до architecture, сгенерировать после architecture через `bmad-generate-project-context`, или запустить генерацию в existing project, чтобы обнаружить established conventions. Документация подчёркивает, что документ должен фиксировать unobvious things, которые agents might not infer from reading code snippets, а не универсальные стандартные практики. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md

Для established projects официальный guide добавляет отдельную hygiene-операцию до генерации контекста: если прежние PRD epics/stories уже завершены, их нужно archive/delete или оставить только в version history; не держать завершённые planning artifacts в `docs/`, `_bmad-output/planning-artifacts/` или `_bmad-output/implementation-artifacts/`. Иначе агенты могут прочитать старые документы как актуальные требования. Источник: https://docs.bmad-method.org/how-to/established-projects/

В established project `bmad-generate-project-context` должен просканировать codebase и зафиксировать стек технологий и версии, паттерны организации кода, соглашения об именовании, подходы к тестированию и паттерны конкретного фреймворка. После генерации человек должен проверить и уточнить файл; для сложных проектов guide предлагает `bmad-document-project`, который сканирует проект и документирует его актуальное состояние. Источник: https://docs.bmad-method.org/how-to/established-projects/

Источник `bmad-document-project` показывает, что это не единый markdown-дамп. Маршрутизатор ищет `{project_knowledge}/project-scan-report.json`, умеет возобновлять работу, начинать заново, делать full rescan, deep-dive и архивировать старый state в `{project_knowledge}/.archive/project-scan-report-{timestamp}.json`; если уже есть `{project_knowledge}/index.md`, он предлагает re-scan entire project, deep-dive specific area или cancel. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md

Full Project Scan использует `documentation-requirements.csv` как scan guide для 12 project types: web, mobile, backend, cli, library, desktop, game, data, extension, infra, embedded. Scan level выбирается человеком: Quick Scan читает в основном конфиги, manifests и структуру каталогов; Deep Scan читает critical directories; Exhaustive Scan читает все source files, кроме типичных generated/heavy folders. State-файл обновляется после каждого шага с timestamp, current_step, completed_steps, outputs_generated и краткими findings; workflow явно требует очищать подробные findings из контекста после записи документов, чтобы не держать весь codebase в разговоре. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md

Артефакты `bmad-document-project` могут включать `project-overview.md`, `source-tree-analysis.md`, `architecture.md` или `architecture-{part_id}.md`, `component-inventory.md`, `development-guide.md`, `deployment-guide.md`, `contribution-guide.md`, `api-contracts.md`, `data-models.md`, `integration-architecture.md`, `project-parts.json` и `index.md`. Неполные документы помечаются ровно как `_(To be generated)_`, чтобы последующий шаг мог найти их и предложить сгенерировать. Для brownfield-части теории это важная деталь: BMAD не просто "читает код", а строит навигируемую базу знаний проекта, которую потом могут загружать другие workflows через `index.md`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md

Validation checklist для `bmad-document-project` уточняет, что именно считается качественным scan. Quick scan не должен читать source files, deep scan читает critical directories по типу проекта, exhaustive scan читает все source files кроме `node_modules`, `dist`, `build`. Deep/exhaustive scans должны идти пакетами по subfolder, а не по случайному числу файлов; каждый пакет читает файлы, извлекает сведения, пишет результат, валидирует и очищает контекст. Checklist также привязывает полноту сканирования к флагам из `documentation-requirements.csv`: если `requires_api_scan = true`, нужны API endpoints; если `requires_data_models = true`, нужны data models; если `requires_state_management = true`, нужны state patterns; если `requires_ui_components = true`, нужен inventory UI components. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md

## Роли, агенты и участники

Официальные материалы называют Specialized Agents: PM, Architect, Developer, UX and more; README говорит о 12+ domain experts и Party Mode, где несколько personas могут участвовать в одной сессии. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md

В workflow diagram видны конкретные имена/personas по основному пути:

- Mary - analysis: brainstorming, research, product brief, PRFAQ.
- John - planning and PM-переходы: PRD, epics/stories, correct-course; в диаграмме также показан на readiness gate.
- Sally - UX.
- Winston - architecture.
- Amelia - implementation: sprint planning, create story, dev story, code review, retrospective, investigate.

Источник: https://docs.bmad-method.org/workflow-map-diagram.html

`bmad-help` является не ролью в продуктовой цепочке, а навигационным механизмом. Его purpose: понять, где пользователь находится в workflow, что уже завершено, что делать дальше, как вызвать следующий skill, и не перегружать пользователя полным каталогом. Он читает catalog `_bmad/_config/bmad-help.csv`, config files, найденные artifacts и project knowledge, а также module docs rows. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md

## Человеческие решения и checkpoints

Человек принимает решения в нескольких местах:

- Выбор planning track: Quick Flow, BMad Method или Enterprise; документация предупреждает выбирать по planning needs, not story math. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- Выбор intent для `bmad-prd`: Create, Update или Validate. Если intent не указан, skill должен спросить. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- UX включается conditionally: если у проекта есть UI, вызывается UX-Designer и `bmad-ux`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- В established project UX work зависит не от того, "есть ли UX", а от того, затрагивает ли изменение UX или требует новых UX patterns; simple updates to existing screens могут обойтись без полного UX process. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `project-context.md` можно создать вручную до architecture, если у человека уже есть сильные technical preferences, или сгенерировать после architecture. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- Implementation readiness check даёт PASS/CONCERNS/FAIL decision перед реализацией; это место для остановки или исправления несогласованных planning docs. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- В `bmad-create-story` user intervention исключается почти полностью, кроме initial epic/story selection или missing documents; если нет `sprint-status.yaml`, workflow предлагает run sprint-planning, provide specific epic-story number или provide path to story documents. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- В retrospective workflow человек подтверждает, какой epic review проводится, и может выбрать partial retrospective, если epic ещё не завершён. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- В Quick Dev человек утверждает short spec/plan до реализации, затем проверяет diff после локального commit и принимает решение о push; если изменение оказалось неудачным после push, official fallback - `git revert HEAD` и fresh chat с новым запуском. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- `bmad-checkpoint-preview` добавляет отдельный human-in-the-loop review после автономной реализации, особенно после `bmad-quick-dev`. Workflow принимает PR, commit, branch, spec file или текущее git-состояние; сначала даёт one-line intent summary и surface area stats, затем ведёт walkthrough по concerns с `path:line` stops, потом показывает 2-5 мест с наибольшим blast radius и предлагает ручные наблюдения для проверки результата. Он не выносит pass/fail verdict и не заменяет linters, type checks или test suites; это structured reading guide, чтобы человек мог решить ship, rework или dig deeper. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/
- В `bmad-correct-course` человек выбирает incremental или batch mode, утверждает или правит каждое edit proposal и затем явно отвечает yes/no/revise на весь Sprint Change Proposal. Это не скрытый автопатч planning artifacts: сам skill требует получить explicit user approval before implementation и только затем направить работу к Developer, Product Owner / Developer или Product Manager / Architect в зависимости от масштаба изменения. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md
- В `bmad-document-project` человек выбирает scan level, подтверждает классификацию проекта, может указать дополнительные документы или key areas, а после генерации решает, нужно ли достраивать incomplete documentation markers. Это место человеческого контроля особенно важно для brownfield: неверная классификация проекта или слишком поверхностный scan level даст последующим агентам убедительную, но неполную базу знаний проекта. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- В Enterprise/TEA человек задаёт ответственных участников до gate-проходов, а release gate требует approver signatures. Пример approval structure включает QA Lead, Tech Lead, Security Lead, Product Manager, Compliance Officer и, для крупных релизов, VP Engineering/CTO. Это уже не обычное "посмотреть diff": метод переносит часть решения в формальную матрицу технического, продуктового и compliance approval. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/

## Проверка готовности и качества

Проверки распределены по цепочке:

- `bmad-prd` в режиме Validate проверяет PRD по checklist и создаёт HTML/Markdown validation report. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Релиз v6.7.0 уточняет форму PRD validation: новый pipeline заменил adversarial reviewer на synthesis pass по quality rubric, который выдаёт HTML и Markdown-отчёты; на сайте BMad также упоминается PRD Coach со встроенной проверкой по семи измерениям. Это похоже на активную зону изменений, поэтому перед финальным текстом нужно сверить документацию и release notes. Источники: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://www.bmadcode.com/
- `bmad-check-implementation-readiness` является gate check before implementation и возвращает PASS/CONCERNS/FAIL decision. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- `bmad-sprint-planning` валидирует полноту `sprint-status.yaml`: every epic, every story, retrospective entry, absence of orphan items, legal status values and valid YAML syntax. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md
- `bmad-sprint-status` повторно валидирует `sprint-status.yaml`: проверяет required metadata (`generated`, `project`, `project_key`, `tracking_system`, `story_location`), наличие `development_status`, допустимость status values, orphaned stories, stale timestamp, `in-progress` epic without stories и неизвестные значения статусов. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md
- `bmad-create-story` валидирует story file against `./checklist.md`, обновляет story status на `ready-for-dev` и меняет `sprint-status.yaml`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- `bmad-dev-story` должен выполнять steps in exact order, не останавливаться на "milestones" или "session boundaries" и продолжать, пока story complete, unless HALT condition or user instruction. Он обновляет только разрешённые области story file: `baseline_commit`, checkboxes, Dev Agent Record, File List, Change Log and Status. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- `bmad-code-review` описан как adversarial review с parallel review layers: Blind Hunter, Edge Case Hunter, Acceptance Auditor; архитектура выполнения требует читать current step file полностью, follow sequence, wait for input at checkpoints and load next. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md
- Implementation FAQ говорит, что после dev-story and code-review passes пользователь должен открыть `sprint-status.yaml`, поменять status story from `review` to `done` и сохранить файл. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Built-in QA (`bmad-qa-generate-e2e-tests`) генерирует только тесты и не отвечает за validation stories или code review. Его стандартные паттерны: использовать API существующего test framework без внешних утилит, в UI-тестах предпочитать semantic locators, держать тесты независимыми, не вставлять hardcoded waits/sleeps и писать описания, которые читаются как feature documentation. Источник: https://docs.bmad-method.org/reference/testing/
- Для более тяжёлого тестового governance существует отдельный TEA module: installable Test Architect module с Murat agent и девятью workflows, включая Test Design, ATDD, Automate, Test Review, Traceability, NFR Assessment, CI Setup, Framework Scaffolding и Release Gate. В отличие от built-in QA, TEA рассчитан на traceability, compliance, risk-based prioritization P0-P3 и quality gates. Источник: https://docs.bmad-method.org/reference/testing/
- Страница TEA welcome уточняет рабочие триггеры и форму module: `bmad-tea` загружает TEA agent/menu, `test-design` запускает Test Design, а core workflows имеют короткие triggers вроде `TD`, `TF`, `CI`, `AT`, `TA`, `RV`, `NR`, `TR`. `GATE` в меню TEA не является самостоятельным workflow: это routing helper через release gate sequence, который не производит отдельный артефакт. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/
- Enterprise TEA gate проверяет не только наличие тестов. Для `nfr-assess` нужны threshold categories вроде Security, Performance, Reliability, Maintainability и подтверждения вроде security scans, penetration tests или compliance audits; `trace Phase 2` создаёт gate decision с references на evidence, approver signatures, compliance checklist and decision rationale. Результат gate выражается как `PASS/CONCERNS/FAIL/WAIVED`, а не как общий "tests passed". Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- `bmad-investigate` проверяет не готовность к ship, а качество расследования. Findings получают grade: Confirmed требует прямой ссылки на `path:line`, log timestamp или commit hash; Deduced должен показывать цепочку рассуждения от Confirmed evidence; Hypothesized обязан назвать, что подтвердит или опровергнет гипотезу. Гипотезы не удаляются: status меняется на Open, Confirmed или Refuted, а resolution объясняет, какие evidence закрыли ветку. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md

## Sprint-status state machine

`bmad-sprint-planning` создаёт `sprint-status.yaml` как ordered inventory epics and stories. Он конвертирует story headers вроде `### Story 1.1: User Authentication` в key `1-1-user-authentication`, добавляет epic entry `epic-{num}`, story entries и `epic-{num}-retrospective`. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md

Состояния:

```text
Epic: backlog → in-progress → done
Story: backlog → ready-for-dev → in-progress → review → done
Retrospective: optional ↔ done
```

Workflow notes уточняют: epic переходит в `in-progress` автоматически, когда создаётся первая story; stories usually worked in order, но parallel work supported; review should happen before done; next story обычно создаётся после previous one `done`, чтобы перенести learnings. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md

## Story как основной implementation context

`bmad-create-story` - центральный механизм защиты implementation от потери контекста. Его goal: создать comprehensive story file, который даёт dev agent everything needed for implementation. В самом skill перечислены ошибки, которые он должен предотвращать: reinventing wheels, wrong libraries, wrong file locations, breaking regressions, ignoring UX, vague implementations, lying about completion, not learning from past work. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

Этот workflow не просто копирует epic. Он должен загрузить PRD, architecture, UX, epics, previous story intelligence, recent git commits, relevant UPDATE files, testing standards, API patterns, database schemas, security requirements, performance requirements and latest technical knowledge for critical libraries. Странная, но важная деталь источника: create-story прямо требует читать файлы, которые story будет менять, потому что skipping this is the primary cause of implementation failures and review cycles. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

В story file должны попасть guardrails для dev agent: technical requirements, architecture compliance, library/framework requirements, file structure requirements, testing requirements, previous story intelligence, git intelligence summary, latest tech information, project context reference and story completion status. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md

## Жизненный цикл после реализации

После реализации story проходит review, status и retrospective:

- `bmad-dev-story` переводит story в работу, фиксирует `baseline_commit` через `git rev-parse HEAD` или `NO_VCS`, обновляет sprint status и story record. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- Если code review создал follow-up items, `bmad-dev-story` умеет распознать секцию `Senior Developer Review (AI)` и subsection `Review Follow-ups (AI)`, затем prioritizes review follow-up tasks before regular tasks. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md
- Story считается окончательно done после прохождения dev-story and code-review, а затем ручного обновления `sprint-status.yaml` из `review` в `done`. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Если во время реализации обнаружен не локальный дефект, а изменение понимания задачи, `bmad-correct-course` переводит это в Sprint Change Proposal: impact analysis, recommended approach, detailed change proposals и implementation handoff. Он может привести к прямой корректировке stories, rollback недавно завершённой работы или пересмотру PRD/MVP. Источники: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md
- Retrospective запускается after completing all stories in an epic. Implementation FAQ подчёркивает, что ждать конца всего проекта не нужно: retrospective после каждого epic поддерживает continuous improvement. Источник: https://docs.bmad-method.org/explanation/faq/implementation-faq/
- Retrospective workflow читает story records, review feedback, testing notes, technical debt, previous retrospective and next epic, чтобы извлечь lessons, recurring patterns, unresolved debt and preparation tasks. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- Если нужен тестовый слой после epic, BMAD предлагает сначала встроенный QA workflow, а при требованиях traceability, compliance или formal quality gates - TEA. Важная граница: built-in QA работает напрямую от source code и не загружает PRD/architecture, а TEA может связываться с upstream planning artifacts для traceability. Источник: https://docs.bmad-method.org/reference/testing/
- Если проблема требует расследования до планирования исправления, `bmad-investigate` создаёт или продолжает case file, отделяет confirmed findings от deductions/hypotheses, реконструирует timeline, фиксирует missing evidence и завершает работу понятной передачей. Финальный outcome содержит confidence: High для confirmed root cause with deterministic repro, Medium для deduction with minor uncertainty, Low для hypothesis with clear data gap. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md

## Сильные стороны

- Хорошо выраженная artifact chain. Документы не просто архивируются: каждый становится входом для следующего workflow, что важно для AI agents with limited and fragile context. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Есть масштабирование глубины: Quick Flow для малых изменений, полный BMad Method для продуктов и платформ, Enterprise для compliance/multi-tenant systems. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- `project-context.md` даёт место для правил, которые агент плохо выводит сам: версии, запрещённые библиотеки, локальные patterns, testing conventions. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- Story context создаётся перед implementation и должен включать previous story intelligence, git intelligence, architecture compliance and files being modified. Это отвечает на типичный сбой coding agents: они реализуют локальный AC, но ломают существующее поведение. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md
- `sprint-status.yaml` делает состояние процесса видимым и машинно читаемым: backlog, ready-for-dev, in-progress, review, done. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md
- `bmad-help` снижает необходимость помнить весь каталог skills: он инспектирует project state and artifacts и предлагает next required/optional steps. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md
- `bmad-spec` даёт компактный contract surface для downstream work: вместо того чтобы каждый следующий workflow заново читал все черновики и обсуждения, он может получить `SPEC.md` с коротким kernel и companion files для load-bearing details. Источник: https://docs.bmad-method.org/reference/core-tools/
- Для existing codebase BMAD предлагает не начинать с пустого PRD, а сначала привести в порядок старые planning artifacts, создать/проверить `project-context.md` и при необходимости запустить `bmad-document-project`. Это даёт методологии brownfield-вариант, где planning опирается на actual current state, а не на выдуманную архитектуру. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `bmad-document-project` делает brownfield-контекст воспроизводимее: scan state живёт в `project-scan-report.json`, generated docs связаны через `index.md`, а большой scan работает batch-wise с промежуточной записью на диск. Это снижает риск, что агент "понял кодовую базу" только внутри исчезающего чата. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- `bmad-document-project` имеет отдельный validation checklist, который проверяет scan level, resumability, write-as-you-go, batching, классификацию проекта, technology stack, completeness of source scan, architecture quality, index/navigation и brownfield PRD readiness. Это делает brownfield-документацию не просто "сгенерированным описанием", а проверяемым входом для следующего PRD/workflow шага. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- Страница Official Modules показывает, что BMAD масштабируется не только глубиной одного BMM workflow, но и подключаемыми domain modules. Для будущей теории это хороший пример "расширяемой методологии": базовый процесс остаётся artifact-first, а поверх него добавляются специализированные агенты и workflows, например TEA для enterprise-grade testing. Источник: https://docs.bmad-method.org/reference/modules/
- `bmad-investigate` отделяет расследование от исправления. Для сложных багов это сильная сторона: ложные ветки, missing evidence и refuted hypotheses становятся частью case file, а не теряются в длинном чате с правками. Источник: https://docs.bmad-method.org/explanation/forensic-investigation/

## Failure modes / overuse risks

- Для малых задач полный BMad Method может быть чрезмерным. Сама документация признаёт отдельный Quick Flow, который пропускает phases 1-3 для small, well-understood changes. Если команда всё равно запускает PRD + architecture + epics + story cycle для простого исправления, метод превращается в overhead. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md
- Обратный риск: Quick Dev может быть использован там, где уже нужна формальная цепочка планирования. Официальный Quick Fixes guide рекомендует полный BMad Method, когда изменение затрагивает несколько систем, требует согласованных правок во многих файлах, имеет неясный объём или нуждается в документированных архитектурных решениях. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- Track selection нельзя делать по story count. Официальная оговорка "story counts are guidance, not definitions" нужна именно потому, что механическое следование числам может завести в слишком лёгкий или слишком тяжёлый процесс. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md
- Свежие чаты уменьшают context pollution, но создают зависимость от качества файловых артефактов. Если PRD, architecture, `project-context.md` или story file неполные, следующий agent честно загрузит слабый контекст и будет уверенно продолжать ошибку.
- `project-context.md` является living document. Если architecture decisions или conventions меняются, а файл не обновляется, implementation workflows будут продолжать тянуть старые правила. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md
- В existing projects старые завершённые artifacts могут стать ложным контекстом, если их оставить в `docs/` или `_bmad-output/`. Official guide прямо требует cleanup completed planning artifacts перед дальнейшей работой. Источник: https://docs.bmad-method.org/how-to/established-projects/
- Репродуцируемость установки не гарантируется одной и той же командой на stable channel: новые released tags могут изменить installed modules. Для повторяемости нужны `manifest.yaml` и `--pin`. Источник: https://docs.bmad-method.org/how-to/install-bmad/
- Версионная нестабильность имён уже видна в источниках: docs/tutorials могут говорить `bmad-create-prd`, а release notes v6.7.0 - `bmad-prd` и shims до 7.0.0. Будущий текст должен либо фиксировать дату/версию, либо объяснять alias/shim слой, иначе читатель получит конфликтующие команды. Источники: https://docs.bmad-method.org/tutorials/getting-started/ и https://github.com/bmad-code-org/BMAD-METHOD/releases
- В implementation есть ручные стыки: после review пользователь должен обновить `sprint-status.yaml` до `done`; retrospective требует подтверждения epic и может быть запущен частично. Эти места могут расходиться с реальным состоянием кода, если человек не дисциплинирован. Источники: https://docs.bmad-method.org/explanation/faq/implementation-faq/ и https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md
- Architecture тоже может стать источником сбоя. Официальная страница про preventing agent conflicts называет три anti-patterns: implicit decisions, over-documentation и stale architecture. То есть BMAD требует не просто написать architecture once, а документировать cross-epic decisions, фокусироваться на conflict-prone areas, обновлять architecture по мере обучения и использовать `bmad-correct-course` для существенных изменений. Источник: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/
- `bmad-document-project` может создать ложную уверенность, если выбран Quick Scan там, где нужен Deep/Exhaustive Scan. В таком режиме workflow почти не читает source files и опирается на patterns, manifests и directory structure; это полезно для обзора, но недостаточно для рискованных brownfield changes. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md
- `bmad-correct-course` защищает от тихого смещения курса, но сам добавляет организационную тяжесть. Для действительно small deviation он может быть чрезмерным; его checklist явно рассчитан на significant changes affecting project direction и требует evidence, impact analysis, proposal, approval and handoff. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md
- `bmad-investigate` не должен подменять реализацию. Skill прямо ограничивает себя diagnosis и предлагает дальнейший route только после conclusion. Если команда ждёт от него автоматического исправления, процесс может показаться медленным; его ценность проявляется там, где важны evidence trail, reproducibility и передача расследования другому инженеру. Источник: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md
- Built-in QA может дать ложное чувство полного тестового покрытия: страница Testing options прямо ограничивает его scope генерацией тестов и рекомендует Code Review для story validation. Для regulated/complex domains нужен TEA или иной полноценный test strategy layer; иначе быстрые API/E2E tests могут выглядеть как завершённый quality gate, хотя это только один workflow после epic. Источник: https://docs.bmad-method.org/reference/testing/
- TEA сам по себе добавляет существенную стоимость координации. Enterprise guide требует заранее определить ответственных участников, собирать evidence, вести compliance folders, поддерживать approver signatures and retention policy. Для проектов без реальных compliance/security/NFR требований такой слой может стать процессной имитацией, а не полезной проверкой. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- У `bmad-document-project` есть отдельный риск ложной полноты: checklist требует, чтобы документы не содержали generic placeholders/TODO, а final validation включает user approval и brownfield PRD readiness. Если команда не проходит этот checklist, `index.md` и generated docs могут выглядеть официально, но не давать агенту нужных API/data/state/security details. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- Community-сигналы показывают реальные опасения по token cost, документационному overhead и нестрогому следованию agent files, но это не primary source и требует отдельной проверки перед использованием в теории как факта. Кандидаты: Reddit threads "BMAD method sucks", "Burning too many tokens with BMAD full flow", "BMAD is kinda messy?".

## Что должно попасть в теорию

- BMAD как пример artifact-first agentic SDLC: не "дай агенту задачу", а "создай цепочку документов, где каждый следующий агент получает суженный и проверенный контекст".
- Различение BMAD Method и Quick Flow: BMAD не обязательно равен длинному waterfall-like ritual; у него есть documented shortcut для малых well-understood changes.
- Quick Flow нужен в теории как отдельный режим, а не как короткая сноска: он принимает free-form intent, может строить short spec, реализует, проверяет сам себя, делает локальный commit и откладывает unrelated/pre-existing work в `deferred-work.md`. Источник: https://docs.bmad-method.org/how-to/quick-fixes/
- `bmad-spec` нужен как отдельный элемент BMAD-картины: это способ сжать разнообразные входы в `SPEC.md` с kernel и companion files, а не просто ещё одно имя для PRD. Источник: https://docs.bmad-method.org/reference/core-tools/
- Checkpoint Preview нужен как пример возвращения управления человеку после длинного автономного прохода: human review получает ordered walkthrough по concerns, high-blast-radius spots и ручные проверки, а не сырой diff как единственный интерфейс понимания. Источник: https://docs.bmad-method.org/explanation/checkpoint-preview/
- Story file как ключевой operational unit: create-story делает больше, чем нарезка требований; он собирает архитектуру, предыдущие уроки, git context, файлы для изменения and latest tech knowledge.
- `project-context.md` как аналог локальной "конституции" проекта: не общие best practices, а unobvious project-specific rules.
- Architecture в BMAD нужно описывать через предотвращение agent conflicts: API style, database naming, state management, testing patterns и другие cross-epic решения фиксируются до implementation, иначе несколько agents могут честно реализовать несовместимые решения. Источник: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/
- Brownfield-угол: для существующих проектов BMAD начинается с cleanup старых artifacts и генерации/вычитки `project-context.md`; иначе метод может формально работать, но кормить агентов устаревшим контекстом. Источник: https://docs.bmad-method.org/how-to/established-projects/
- `bmad-document-project` как отдельный brownfield-механизм: из codebase создаётся project knowledge base с index, source tree, architecture, API/data/component docs и state file для resume, а не просто "агент прочитал репозиторий".
- В теории стоит показать `bmad-document-project` как write-as-you-go scan: state file + batch summaries + немедленная запись документов + checklist validation. Это полезно для объяснения, как BMAD борется с исчезающим контекстом длинного codebase scan. Источник: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md
- `sprint-status.yaml` как минимальная state machine между агентами и человеком.
- `bmad-sprint-status` как read-only/repair-oriented navigator по этой state machine: показывает next action, риски stale/orphan status и уменьшает ручное чтение YAML.
- Readiness gate и code review как контрмеры против уверенной, но несогласованной реализации.
- `bmad-correct-course` как формализованный mid-sprint replanning: evidence -> impact analysis -> path forward -> proposed artifact edits -> explicit approval -> handoff.
- `bmad-investigate` как отдельная дисциплина диагностики: stronghold first, evidence grading, hypotheses never deleted, investigation backlog, reproduction/fix direction после вывода.
- Тестовый хвост лучше показывать двухслойно: built-in QA как быстрый генератор tests после epic и TEA как отдельный governance module для traceability, NFR, CI and release gate. Источник: https://docs.bmad-method.org/reference/testing/
- Enterprise track лучше раскрывать через evidence lifecycle: NFR thresholds in PRD/test-design -> test infrastructure and CI in solutioning -> per-epic TEA review/trace -> release gate -> archived compliance evidence. Источник: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/
- Ограничение: эффективность метода зависит от качества исходных документов и дисциплины обновления state/context files.

## Что лучше уйдёт в Handbook / Fieldbook

- Практический рецепт установки:

```bash
npx bmad-method install
bmad-help
```

- Когда выбирать Quick Flow, а когда полный BMad Method.
- Как запускать Quick Dev: fresh chat, intent as text/file/issue URL, ответы на уточняющие вопросы, approval short spec, review diff, push, `git revert HEAD` при неудачном push.
- Как использовать `bmad-spec`: собрать brief/PRD/RFC/transcript/mixed inputs, получить `SPEC.md` с kernel, проверить companion files и только затем отдавать contract downstream.
- Как проводить Checkpoint Preview после Quick Dev: открыть spec review trail, пройти orientation, walkthrough по concerns, detail pass по high-risk spots и ручные observations перед ship/rework decision.
- Шаблон минимального `_bmad-output/project-context.md` для существующего проекта.
- Cleanup checklist для established project: убрать завершённые PRD/epics/stories из `docs/`, `_bmad-output/planning-artifacts/`, `_bmad-output/implementation-artifacts/`; затем запустить или вручную подготовить `project-context.md`.
- Как выбирать scan level в `bmad-document-project`: Quick Scan для ориентации, Deep Scan для brownfield PRD, Exhaustive Scan для migration/audit.
- Как проходить validation checklist `bmad-document-project`: проверить, что scan level выбран сознательно, critical directories прочитаны по типу проекта, API/data/state/UI/security details собраны по flags, `index.md` связан с generated docs, а user approval получен до использования документов в brownfield PRD.
- Checklist перед `bmad-create-story`: есть ли `prd.md`, `architecture.md`, epics, актуальный `sprint-status.yaml`, project context, последние изменения в git.
- Checklist для architecture: какие cross-epic decisions требуют ADR, где нужны FR/NFR-specific guidance, какие naming/testing/state/API conventions нельзя оставлять implicit.
- Шаблон использования `bmad-sprint-status`: когда смотреть статус, как интерпретировать risks, что делать с `review`, `in-progress`, `ready-for-dev` и stale tracker.
- Как запускать `bmad-correct-course`: собрать trigger story, evidence, affected artifacts, выбрать direct adjustment / rollback / PRD MVP review, получить explicit approval и handoff.
- Как запускать `bmad-investigate`: дать ticket/log/stack trace/code area, согласовать slug, открыть case file, не просить сразу правку кода, а довести до evidence-graded conclusion.
- Когда достаточно built-in QA, а когда нужен TEA: small-medium quick coverage против regulated/complex projects с traceability и formal gates.
- Как запускать Enterprise TEA lifecycle: определить ответственных участников, вписать NFR/compliance в PRD, сделать system-level `test-design`, подготовить framework/CI/evidence storage, обновлять trace per epic и закрывать release через `nfr-assess` + `test-review` + `trace Phase 2`.
- Ритуал fresh chat per workflow: PRD, architecture, create-story, dev-story, code-review.
- Как руками проверить `sprint-status.yaml` после code review.
- Как не запускать полный BMAD для однофайлового исправления.

## Локальное различение: не путать BMAD с Gas Town

BMAD Method - установленный фреймворк skills/workflows/artifacts вокруг проекта: `_bmad/`, `_bmad-output/`, `bmad-help`, `bmad-prd`, `bmad-create-story`, `sprint-status.yaml`. Gas Town в текущей теоретической работе не нужно использовать как синоним BMAD: если Gas Town описывает другой режим или историю, BMAD должен остаться примером формализованного workflow framework with project artifacts. Это локальное различение нужно только чтобы не смешать источники в будущем тексте; полноценное сравнение сюда не входит.

## Источники

- Официальный сайт BMad Method: https://www.bmadcode.com/bmad-method/  
  Роль: актуальная витрина проекта, экосистема модулей, команда установки, changelog-сигналы. Ограничение: маркетинговый слой, мало деталей workflow.
- GitHub repository `bmad-code-org/BMAD-METHOD`: https://github.com/bmad-code-org/BMAD-METHOD  
  Роль: первичный источник README, кода skills, структуры репозитория, issues. Ограничение: ветка `main` быстро меняется.
- Raw README: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md  
  Роль: positioning, quick start, prerequisites, install commands, modules, web bundles.
- Workflow Map raw docs: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md  
  Роль: основная карта phases, workflows, outputs, context management.
- Getting Started raw docs: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md  
  Роль: практический tutorial, planning tracks, phase order, output tree, fresh chat rule, build cycle.
- Project Context raw docs: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md  
  Роль: объяснение `project-context.md`, когда создавать, что писать, какие workflows загружают.
- Install guide: https://docs.bmad-method.org/how-to/install-bmad/  
  Роль: installer channels, manifest, pinning, GitHub API rate limits, troubleshooting.
- Core Tools docs: https://docs.bmad-method.org/reference/core-tools/  
  Роль: список core tools и описание `bmad-help`, brainstorming, party mode, review helpers, sharding/indexing, `bmad-spec` и контракта `SPEC.md`.
- Quick Dev explanation: https://docs.bmad-method.org/explanation/quick-dev/  
  Роль: человеческие checkpoints в Quick Dev, утверждение spec, диагностика сбоя по слоям intent/spec/implementation.
- Checkpoint Preview explanation: https://docs.bmad-method.org/explanation/checkpoint-preview/  
  Роль: human review после реализации, review trail, участки с высоким blast radius, границы относительно тестов и pass/fail-вердикта.
- Why Solutioning Matters: https://docs.bmad-method.org/explanation/architecture/why-solutioning-matters/  
  Роль: architecture как защита от multi-agent conflicts и несогласованной реализации между epics.
- Preventing Agent Conflicts: https://docs.bmad-method.org/explanation/preventing-agent-conflicts/  
  Роль: структура ADR, FR/NFR-specific guidance, conventions, stale architecture и over-documentation anti-patterns.
- Testing options reference: https://docs.bmad-method.org/reference/testing/  
  Роль: built-in QA workflow, TEA module, API/E2E test generation, traceability, NFR, CI и release gates.
- Workflow diagram: https://docs.bmad-method.org/workflow-map-diagram.html  
  Роль: визуальный artifact flow, имена personas, context flow between create-story/dev-story/code-review/quick-dev.
- Implementation FAQ: https://docs.bmad-method.org/explanation/faq/implementation-faq/  
  Роль: done status, параллельные stories, retrospective timing, create-story context.
- Quick Fixes guide: https://docs.bmad-method.org/how-to/quick-fixes/  
  Роль: практическая граница `bmad-quick-dev`, free-form intent, approval short spec, self-review, local commit, `deferred-work.md`, когда переходить к полному BMAD.
- Established Projects guide: https://docs.bmad-method.org/how-to/established-projects/  
  Роль: brownfield workflow, cleanup completed artifacts, `bmad-generate-project-context`, `bmad-document-project`, UX/architecture considerations for existing codebases.
- Forensic Investigation explanation: https://docs.bmad-method.org/explanation/forensic-investigation/  
  Роль: rationale для `bmad-investigate`, граница diagnosis vs fix, evidence trail, use cases для сложных багов и production incidents.
- GitHub Releases / changelog: https://github.com/bmad-code-org/BMAD-METHOD/releases и https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md  
  Роль: актуальные изменения v6.7.0/v6.8.0, `bmad-prd`/`bmad-brief`, `bmad-ux`, `bmad-spec`, shim-слой старых PRD skills, активная зона несовпадения docs и release notes.
- NewReleases mirrors for v6.7.0/v6.8.0: https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.7.0 и https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.8.0  
  Роль: удобочитаемый снимок release notes; использовать как вспомогательный источник к GitHub Releases, не как primary замену.
- `bmad-help` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md  
  Роль: как help определяет project state, outputs, required/optional next steps.
- `bmad-sprint-planning` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md  
  Роль: sprint-status state machine, story key conversion, validation checks.
- `bmad-sprint-status` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md  
  Роль: чтение и проверка `sprint-status.yaml`, next-action routing, risk detection, legacy status normalization.
- `bmad-create-story` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md  
  Роль: самый важный источник по story context, artifact loading, previous story/git intelligence, guardrails.
- `bmad-dev-story` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md  
  Роль: implementation discipline, allowed story-file edits, `baseline_commit`, continuation after review.
- `bmad-code-review` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md  
  Роль: adversarial review layers, step-file architecture and checkpoints.
- `bmad-retrospective` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md  
  Роль: post-epic review, partial retrospective handling, previous-retro continuity, lessons extraction.
- `bmad-correct-course` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md  
  Роль: mid-sprint change-management workflow, loading strategy, Sprint Change Proposal, approval/handoff gates.
- `bmad-correct-course` checklist raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md  
  Роль: impact analysis, artifact conflict checks, path selection direct adjustment / rollback / PRD MVP review, explicit approval guardrails.
- `bmad-investigate` skill raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md  
  Роль: forensic case workflow, evidence grading, hypothesis handling, diagnosis-only boundary and handoff routing.
- `bmad-document-project` instructions raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md  
  Роль: router для project documentation, scan report state, resume/fresh/rescan/deep-dive/archive paths.
- `bmad-document-project` full scan instructions raw: https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md  
  Роль: scan levels, project type detection, state-file protocol, generated document set, index-guided project knowledge base.
- `bmad-document-project` validation checklist: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md  
  Роль: полнота scan, write-as-you-go, batching, flags from `documentation-requirements.csv`, brownfield PRD readiness, final validation and user approval.
- Official Modules: https://docs.bmad-method.org/reference/modules/  
  Роль: граница между core/BMM и official add-on modules; TEA как отдельный module, а не обязательная часть каждого BMAD workflow.
- TEA welcome docs: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/  
  Роль: TEA как Test Engineering Architect module, quick install, agent/menu trigger `bmad-tea`, core workflows and `GATE` helper boundary.
- TEA enterprise guide: https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/  
  Роль: Enterprise track для compliance/security/audit/NFR, lifecycle by phases, evidence collection, approvers, release gate and retention.
- GitHub issue #1629: https://github.com/bmad-code-org/BMAD-METHOD/issues/1629  
  Роль: полезный, но не canonical, разбор BMAD architecture: workflow runner, agent menu loop, config cascade, manifests. Использовать осторожно как discussion artifact, не как стабильную документацию.
- Reddit/community candidates, непрочитанные глубоко и не primary: "BMAD method sucks", "Burning too many tokens with BMAD full flow", "BMAD is kinda messy?", "I built auto-bmad".  
  Роль: кандидаты для будущего прохода по real-world risks and adoption friction; не использовать как подтверждение деталей без отдельного чтения.

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

## Кандидаты на иллюстрации

- Official Workflow Map Diagram: https://docs.bmad-method.org/workflow-map-diagram.html  
  Что изображено: четыре фазы, personas, artifact arrows, Quick Flow, context flow.  
  Зачем пригодится: основная схема для будущего объяснения "документ становится входом следующего шага".  
  Где использовать: теория или Handbook-раздел про BMAD workflow.  
  Статус: кандидат; перед публикацией проверить права/лицензию и возможность пересобрать собственную схему.
- Output tree from Getting Started (`_bmad/`, `_bmad-output/planning-artifacts`, `_bmad-output/implementation-artifacts`, `project-context.md`).  
  Что изображено: файловая рамка installed project.  
  Зачем пригодится: показать, что метод живёт в репозитории как artifacts/config, а не только в чате.  
  Где использовать: Handbook/Fieldbook.  
  Статус: лучше перерисовать самостоятельно.
- Sprint status state machine из `bmad-sprint-planning`: Epic, Story, Retrospective statuses.  
  Что изображено: `backlog → ready-for-dev → in-progress → review → done`.  
  Зачем пригодится: показать lifecycle между агентами и человеком.  
  Где использовать: теория или практический раздел.  
  Статус: лучше сделать собственную компактную схему.
- Context flow diagram: PRD -> Architecture -> Story -> Dev -> Review.  
  Что изображено: переходы контекста по BMAD.  
  Зачем пригодится: объяснить отличие artifact-first workflow от single-chat coding.  
  Где использовать: теория.  
  Статус: создать собственную иллюстрацию на основе источников.
- Quick Dev boundary diagram.  
  Что изображено: free-form intent -> short spec approval -> implementation/review/commit -> diff review/push; отдельно стрелка в `deferred-work.md` для unrelated/pre-existing work и стрелка "upgrade to full BMAD" при multi-system/uncertain-scope changes.  
  Зачем пригодится: показать, что Quick Flow не просто "без документов", а отдельный малый lifecycle.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- SPEC compression diagram.  
  Что изображено: brief/PRD/RFC/transcript/mixed inputs -> `SPEC.md` kernel (`Why`, `Capabilities`, `Constraints`, `Non-goals`, `Success signal`) + companion files -> downstream workflows.  
  Зачем пригодится: показать, что BMAD умеет не только расширять документы, но и сжимать разношёрстный вход в компактный контракт.  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.
- QA/TEA boundary diagram.  
  Что изображено: after epic -> built-in QA API/E2E tests; separate branch to TEA for traceability, NFR, CI, release gate.  
  Зачем пригодится: не дать читателю принять quick test generation за полный quality governance.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Brownfield scan diagram.  
  Что изображено: repository -> `project-scan-report.json` -> scan level -> generated docs (`project-overview.md`, `architecture.md`, `component-inventory.md`, `index.md`) -> downstream loading by other workflows.  
  Зачем пригодится: показать, что BMAD brownfield work строит project knowledge base, а не полагается на разовое чтение кода.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Document Project validation diagram.  
  Что изображено: scan level -> project type flags (`requires_api_scan`, `requires_data_models`, `requires_state_management`, `requires_ui_components`) -> batch write-as-you-go -> checklist -> user approval -> brownfield PRD readiness.  
  Зачем пригодится: показать, что generated docs должны пройти явную проверку полноты, а не просто появиться в папке project knowledge.  
  Где использовать: Handbook/Fieldbook.  
  Статус: создать собственную схему.
- Correct Course decision diagram.  
  Что изображено: trigger story/problem -> impact analysis -> direct adjustment / rollback / PRD MVP review -> Sprint Change Proposal -> approval -> handoff.  
  Зачем пригодится: объяснить mid-sprint replanning как отдельный lifecycle, а не как "попросить агента переделать".  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.
- Investigation evidence ladder.  
  Что изображено: raw evidence -> Confirmed findings -> Deduced findings -> Hypothesized branches -> conclusion confidence -> route to quick-dev/correct-course/create-story/code-review.  
  Зачем пригодится: показать границу расследования и исправления в BMAD.  
  Где использовать: Fieldbook.  
  Статус: создать собственную схему.
- Enterprise TEA release gate diagram.  
  Что изображено: PRD NFR/compliance -> system-level `test-design` -> framework/CI/evidence storage -> per-epic review/trace -> `nfr-assess` + full `test-review` + `trace Phase 2` -> `PASS/CONCERNS/FAIL/WAIVED` -> compliance archive.  
  Зачем пригодится: показать, что Enterprise track строит evidence lifecycle и approvals, а не просто добавляет "Security + DevOps" строкой в planning track.  
  Где использовать: теория или Handbook.  
  Статус: создать собственную схему.

## Открытые вопросы

- Насколько стабильны названия skills и структура `_bmad/` между v6 releases? README и docs указывают на быструю эволюцию и prerelease channel; нужно проверять перед финальным текстом.
- Как именно BMad Method соотносится с BMad-CORE и BMad Ecosystem в текущей версии: где заканчивается BMM и начинается общий core layer?
- Насколько часто реальные команды используют полный Method track, а не Quick Flow или внешние automators? Нужен отдельный проход по experience reports.
- Как практически читать полный `documentation-requirements.csv` для `bmad-document-project`: checklist подтвердил ключевые flags (`requires_api_scan`, `requires_data_models`, `requires_state_management`, `requires_ui_components`), но сам CSV напрямую не удалось прочитать из-за cache miss raw/GitHub и закрытого network в shell. Для финального текста достаточно checklist-уровня, но для полной таблицы project types нужен отдельный доступ к raw file.
- Каков текущий статус Enterprise Security/DevOps integration в v6 за пределами TEA: testing/compliance/CI частично прояснены через TEA enterprise guide, но отдельные Security/DevOps modules или workflows, если они есть, требуют дополнительной сверки.
- Как синхронизировать naming в финальном тексте: `bmad-create-prd` в части docs против `bmad-prd` в v6.7+ release notes и v6.8 web-bundle framing?
- Нужно ли описывать `bmad-investigate` как часть core BMAD Method или как optional implementation-side workflow: source присутствует в BMM implementation skills, но для финального сайта важно не перегрузить основной рассказ.
- Какие права на использование official workflow diagram и banner? Для сайта лучше делать свою схему.
