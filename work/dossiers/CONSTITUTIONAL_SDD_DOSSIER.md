# Constitutional SDD

## Назначение досье

Это рабочее досье по Constitutional Spec-Driven Development, или CSDD. Оно собирает фактуру о том, как ограничения безопасности и управления становятся верхним слоем спецификации для AI-assisted разработки. Досье не является готовой главой и не должно превращаться в краткий пересказ abstract: для будущего текста важны артефакты, порядок работы, места человеческого утверждения, проверяемые evidence и слабые места метода.

Ключевой источник прохода 01 — статья Srinivas Rao Marri, [Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation](https://arxiv.org/abs/2602.02584), поданная 31 января 2026 года. Статья заявляет 15 страниц, 2 figures, 5 tables, 11 code listings, 14 references, reference implementation и compliance traceability matrix. Экспериментальная HTML-версия доступна через [ar5iv](https://ar5iv.labs.arxiv.org/html/2602.02584v1), а прямой PDF использован в проходе 02 для сверки таблиц, угроз валидности и будущих направлений [arXiv PDF](https://arxiv.org/pdf/2602.02584). В проходе 03 текущая страница arXiv сверена ещё раз: submission history показывает только `v1` от 31 января 2026 года и arXiv-issued DOI `10.48550/arXiv.2602.02584`; поздней версии на странице не видно [arXiv abstract](https://arxiv.org/abs/2602.02584). В проходе 04 повторный поиск не дал новой версии статьи или независимого основного источника; полезное пополнение пришло из более внимательного чтения уже найденных arXiv/ar5iv и reference implementation.

В референс-репозитории есть отдельный [PAPER.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md) с близким, но не полностью идентичным текстом: там используется заголовок `Secure by Constitution: Constitutional Specification-Driven Development for AI-Assisted Code Generation` и показана Figure 4 с трёхфазной рабочей цепочкой. Для досье этот файл полезен как черновой артефакт источника, но при конфликте формулировок приоритет остаётся за arXiv PDF.

В проходе 05 добавлен внешний практический источник: Pavel Zverev / Mad Devs, [From constitution.md to Compliance: A Practical Security Layer for SDD](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/), созданный 18 мая 2026 года. Это не peer-reviewed подтверждение результатов Marri и не новый primary paper, а руководство по тому, как `constitution.md` превращается в рабочий слой через agent guidance, automated checks, CI gates, PR checklist и traceability matrix. Его нужно использовать как источник операционных деталей и ограничений, а не как независимую репликацию метрик CSDD.

В проходе 06 добавлен ещё один слой источников вокруг Spec Kit: официальный [spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) и две публичные issue-страницы [#697](https://github.com/github/spec-kit/issues/697), [#40](https://github.com/github/spec-kit/issues/40). Это не источники о security case study Marri. Они полезны для понимания того, как общий SDD-инструментарий трактует specifications, constitutional gates, `/analyze`, качество через templates и где у пользователей возникает непонимание вокруг создания Constitution.

В проходе 07 добавлен источник из периферии Spec Kit: [DocGuard](https://github.com/raccioly/docguard) и его [PyPI-страница](https://pypi.org/project/docguard-cli/0.24.0/). Это не источник о Constitutional SDD Marri и не репликация его case study. Он полезен как пример того, как сообщество вокруг Spec Kit пытается превратить спецификационные артефакты, `constitution.md`, трассируемость, hooks и CI-gates в отдельный слой принудительной проверки. Официальная страница [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html) важна как ограничение: community extensions создаются независимыми авторами; мейнтейнеры проверяют полноту записи каталога, но не аудируют, не поддерживают и не одобряют код расширения.

В проходе 08 добавлен [Cisco Foundry Security Spec](https://github.com/CiscoDevNet/foundry-security-spec) и связанный [Project CodeGuard](https://github.com/cosai-oasis/project-codeguard). Это не источник о банковском case study Marri и не подтверждение его метрик. Foundry полезен как соседний пример, выведенный из production-опыта: security-governance Constitution ставится над `spec.md`, планами и задачами в Spec Kit-совместимом процессе. Репозиторий намеренно не содержит кода, его передаваемый артефакт — спецификация, а `constitution.md` фиксирует принципы, с которыми `/speckit.plan` и `/speckit.analyze` должны сверять производные артефакты [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md) [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md).

## Роль в AI-driven SDLC

CSDD находится в спецификационном слое AI-driven SDLC. Его задача — не просто написать требования до кода, а сделать часть требований неотменяемыми ограничениями для генерации и проверки кода. В статье это сформулировано как перенос security requirements в слой спецификации, чтобы AI-generated code соответствовал требованиям by construction, а не только после проверки постфактум [arXiv abstract](https://arxiv.org/abs/2602.02584).

В отличие от обычного запроса “сделай безопасно”, CSDD требует отдельный артефакт Constitution: версионированный, machine-readable документ с security constraints, CWE mappings, enforcement levels и rationale. Этот документ управляет следующими артефактами: `spec.md`, `plan.md`, `tasks.md`, запросами для генерации, реализацией и compliance traceability matrix [ar5iv §3.1-3.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

В статье вклад метода описан не как улучшенный “security prompt”, а как пять связанных результатов: формальная рамка constitutional security, complete development methodology, эмпирические данные из case study, сравнение с reactive security verification и lessons learned for AI-assisted development [ar5iv §1.3](https://ar5iv.labs.arxiv.org/html/2602.02584v1). Для будущей теории это важно: CSDD должен попасть в слой AI-driven SDLC как метод связывания намерения, генерации и проверяемых свидетельств, а не как список хороших security practices.

Официальный `spec-driven.md` помогает уточнить место CSDD в более широкой линии SDD: specifications становятся главным артефактом, implementation plans and code рассматриваются как производные артефакты, а сопровождение софта означает изменение спецификаций и implementation plans, а не только правку кода [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md). CSDD добавляет к этой общей инверсии более жёсткий слой безопасности и управления: Constitution становится не просто архитектурным style guide, а источником проверяемых constraints с CWE/control provenance и проверяемыми compliance-свидетельствами.

Foundry показывает близкую роль в другом домене: он не генерирует приложение, а задаёт blueprint для AI-assisted security evaluation system. Для досье важна сама форма: порядок работы security evaluation начинается не с кода инструмента, а с seed specification, маркеров уточнения, Constitution и success criteria. Эти артефакты затем должны породить план, задачи и реализацию в инфраструктуре конкретной организации [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md) [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md).

## Проблема, которую решает

Статья описывает проблему через “vibe coding”: AI coding assistant быстро выдаёт функциональный код, но оптимизирует прежде всего видимую functional correctness, а не security requirements конкретного deployment context. Примеры риска: SQL injection, XSS, missing authentication, недостаточная проверка входных данных и неправильная работа с секретами [ar5iv §1.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Источник выделяет четыре практических сбоя ad-hoc prompting:

- **Inconsistency**: security requirements приходится повторять в каждом запросе, и человек забывает включить важные ограничения.
- **Incompleteness**: разработчик считает часть требований очевидной, но модель не выводит их из контекста.
- **Drift**: security rules, заданные в начале проекта, не обязательно переносятся в более поздние features.
- **Unverifiability**: нет системного механизма, который показывает, что generated code соблюдает требования во всей кодовой базе.

Для будущей теории здесь важен не только угол безопасности. CSDD показывает более общий паттерн: если AI-generated code ускоряет производство, то устойчивые ограничения должны жить не в памяти чата, а в версионируемом проектном артефакте, который участвует в генерации, планировании, проверке и audit trail.

## Workflow

Минимальная рабочая цепочка CSDD выглядит так:

1. Команда утверждает Constitution: набор принципов, источники требований, CWE/regulatory mappings, enforcement levels `MUST` / `SHOULD` / `MAY`, rationale и amendment process.
2. Feature specification (`spec.md`) формулирует, что и зачем нужно построить, и должна ссылаться на релевантные constitutional clauses.
3. Implementation plan (`plan.md`) переводит spec в технические решения с учётом security constraints и выбранного стека.
4. Task definitions (`tasks.md`) разбивают план на атомарные работы, которые AI agent может выполнять без потери ограничений.
5. AI-assisted generation получает релевантные principles как обязательный контекст. По статье, лучше давать не весь Constitution, а 3-5 релевантных принципов на запрос, иначе context window может ухудшить соблюдение требований.
6. Compliance traceability matrix связывает principle, CWE, file, line numbers и implementation technique.
7. Verification проверяет не только наличие кода, но и то, что code locations действительно покрывают principles; при нарушениях код регенерируется или исправляется с явной ссылкой на clause.

`PAPER.md` в референс-репозитории показывает тот же процесс через три фазы: Constitutional Specification Creation, Specification-Driven Generation и Automated Compliance Verification. Между ними нарисована петля обратной связи: обнаруженные violations возвращаются не только в код, но и в запросы и спецификационные артефакты. Это важная рабочая деталь: CSDD предполагает, что compliance gap может означать ошибку не только реализации, но и разложения на `spec.md`, `plan.md` и `tasks.md` [PAPER.md Figure 4](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md).

В case study процесс занял две недели с одним developer и Claude как AI assistant. Первая неделя: дни 1-2 — Constitution ratification, дни 3-4 — feature specification для authentication, accounts и transactions, день 5 — implementation planning с 47 code locations. Вторая неделя: дни 1-3 — backend implementation with constitutional constraints, дни 4-5 — frontend, дни 6-7 — verification and compliance matrix generation [ar5iv §5.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Источник отдельно оценивает цену метода: два дня на Constitution и дополнительная работа с compliance matrix дали примерно 16 часов дополнительных затрат, но уменьшили число security review iterations с 4 до 1 и, по оценке автора, сэкономили около 64 часов исправлений по сравнению с reactive verification [ar5iv §6.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1). Это полезная оговорка для текста: CSDD не бесплатен, но источник утверждает, что раннее формализованное ограничение дешевле поздней серии security fixes.

В общей модели Spec Kit рабочий процесс начинается с идеи, превращается через диалог с AI в PRD/specification, затем в implementation plan, supporting documents and tasks. Источник отдельно подчёркивает specifications в ветках с командным ревью и постоянную проверку ambiguity, contradictions and gaps [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md). Для CSDD это даёт важное операционное прочтение: security Constitution должна попадать не только в prompt generation, но и в артефакты ветки, которые команда реально ревьюит; иначе команда не видит, на каком этапе security constraint был потерян.

DocGuard показывает соседний, более инструментальный вариант этого же хвоста рабочего процесса. В его Spec Kit integration цепочка выглядит как чередование генерации и проверки: `specify init`, `/speckit.specify`, `docguard guard`, `/speckit.plan`, снова `docguard guard`, `/speckit.tasks`, снова `docguard guard`, `/speckit.implement` и финальный `docguard guard` как CI/CD gate [DocGuard README](https://github.com/raccioly/docguard). Для CSDD это не заменяет security matrix Marri, но даёт полезную форму повторяемого цикла принудительной проверки: каждая граница между артефактами должна иметь проверку до перехода дальше, а не только итоговый audit после реализации.

Foundry даёт ещё один Spec Kit-совместимый порядок работы. Сначала читается `constitution.md`; затем он копируется в `your-project/.specify/memory/constitution.md`, регистрируется через `/speckit.constitution`, а `spec.md` копируется в `specs/001-foundry/spec.md`. После этого `/speckit.clarify` должен пройти все маркеры `[NEEDS CLARIFICATION: ...]`, `/speckit.specify` превращает seed в draft specification, затем clarify/specify повторяются до исчезновения маркеров и решений, чужих для конкретной организации. Только после этого запускаются `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`; после значимых milestones предлагается `/speckit.analyze` для проверки drift между `spec`, `plan`, `tasks` и кодом [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md). Для CSDD это сильная практическая оговорка: открытый вопрос в specification layer нельзя протаскивать в план как молчаливое предположение.

## Артефакты

### Constitution

Constitution в статье определяется как versioned document, который кодирует non-negotiable requirements как machine-readable principles. Каждый principle включает:

- identifier, например `SEC-002`;
- CWE reference, например `CWE-89`;
- enforcement level: `MUST`, `SHOULD` или `MAY`;
- constraint: что код обязан делать или не делать;
- implementation pattern: как выполнить ограничение;
- rationale: какой attack vector закрывается.

В paper example banking constitution version `1.0.0` содержит 15 security principles в четырёх группах: Security-First Principles, Input Validation Principles, Authentication & Authorization Principles, Secure Data Handling Principles [ar5iv §4.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Reference implementation хранит полный Constitution в [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md). Там он шире, чем краткий список в статье: кроме security-first и input validation есть bounded context & service isolation, API contract-first design, resilience & fault tolerance, observability & auditability, regulatory compliance, testing requirements, deployment requirements and governance. Это важная деталь: CSDD может начинаться как security methodology, но фактический Constitution в репозитории уже смешивает security, microservices architecture, API contracts, operations и governance.

Raw Constitution также показывает, как security Constitution превращается в проектную policy surface. Там есть правила управления версиями: major version для несовместимых изменений governance, minor version для новых principles или расширенных guidance, patch version для уточнений и исправлений. В amendment process заложены proposal documentation, team review, approval process and migration plan, а в governance section — quarterly compliance reviews and remediation timelines [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md). Для будущего текста это сильнее, чем абстрактная фраза “документ версионируется”: Constitution здесь ведёт себя как живой нормативный артефакт проекта.

Foundry Constitution version `0.2.0` полезен как другой формат такого верхнего слоя. Он содержит 11 principles, каждый из которых кодирует отгруженный, диагностированный и исправленный production failure: Evidence Over Assertion, Surface Only What Survives, Liveness By Heartbeat, Claims Are Atomic And Mortal, Coverage Before Yield, Exploited Means Demonstrated, Sandbox By Infrastructure, Not By Prompt, The Operator Outranks Every Agent, Persist Atomically and others. Governance section прямо задаёт precedence: если `constitution.md` конфликтует со `spec.md`, ошибочен `spec.md`; если конфликтуют generated `plan.md` или `tasks.md`, ошибочны они, и `/speckit.analyze` должен это подсветить [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Для CSDD это важный соседний пример: Constitution работает как authority layer with conflict resolution, а не как список ценностей.

### Specification layer

Статья явно называет три следующих артефакта:

- `spec.md` — feature specification, которая описывает what to build и functional requirements с respect to constitutional constraints;
- `plan.md` — implementation plan, где security considerations встраиваются в design-level decisions;
- `tasks.md` — атомарные работы для AI-assisted generation.

В reference implementation feature spec лежит в [specs/001-banking-crud/spec.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/spec.md). Он задаёт user stories для account management, customer profile management and transaction recording, edge cases вроде unauthorized access, negative amounts and duplicate account creation, а также functional requirements `FR-001`...`FR-022`. Security заметна не как отдельный appendix, а внутри acceptance/edge cases/cross-cutting requirements: authentication required, unauthorized access blocked, audit logging, input validation.

Implementation plan лежит в [specs/001-banking-crud/plan.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/plan.md). В доступной raw-версии он короткий: FastAPI backend, Pydantic validation, PostgreSQL persistence, OpenAPI documentation и React frontend. При этом `Constitution Check` внутри plan жёстче, чем фактическая структура: он требует authentication/authorization для всех endpoints, input validation, audit logging и separation of customer, account and transaction services, но ниже `Structure Decision` выбирает один backend/frontend project. Это не обязательно делает пример неверным, но показывает риск artifact drift: constitutional gate может быть заполнен сильнее, чем последующий technical plan [plan.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/plan.md).

Task list лежит в [specs/001-banking-crud/tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md). Он содержит 13 задач `T001`-`T013`: setup, tests, backend core, API, frontend, integration, polish. Задачи уже достаточно атомарны для агента: создать FastAPI skeleton, настроить PostgreSQL, создать Pydantic schemas, SQLAlchemy models, OAuth2/JWT, endpoints, React components и runbooks. Но в отличие от статьи, этот исходный `tasks.md` почти не несёт явных ссылок на constitutional clauses: security появляется как названия задач вроде “authentication and authorization” и “Pydantic schemas with validation”, а не как `SEC-002` или `CWE-89` рядом с конкретной работой. Для будущего текста это полезная оговорка: CSDD становится сильнее, когда clauses доходят до уровня задач, но сама рабочая цепочка не гарантирует этого автоматически.

Публичная issue [github/spec-kit #697](https://github.com/github/spec-kit/issues/697) даёт хороший внешний пример того, как это ослабление может выглядеть в обычном SDD-проекте. Автор приводит результат `/analyze`, где `tasks.md T006` помечен как `CRITICAL`, потому что CI setup назван optional, хотя Constitution требует mandatory tests and lint/format gates. В той же таблице есть `MEDIUM`-замечание: несколько tasks align to constitution, но не map to any spec requirement; предложенное исправление — добавить в spec короткий раздел `Non-functional/Constitutional Gates` или аннотировать tasks с указанием constitution principle [Spec Kit Issue #697](https://github.com/github/spec-kit/issues/697). Для CSDD это сильная практическая деталь: compliance trace должна идти в обе стороны — от security Constitution к задачам и от задач обратно к spec requirements.

Foundry `spec.md` подчёркивает разницу между seed and implementation spec. Файл имеет status `SEED`, intended use `Input to /speckit.clarify`, companion file `constitution.md` и явное предупреждение: не реализовывать систему напрямую из seed. Он содержит ~130 functional requirements с inline rationale, success criteria `SC-001`...`SC-009`, assumptions `A-1`...`A-9`, roles, finding lifecycle, coordination substrate, governance/safety requirements and open questions index. Организационно-зависимые решения помечены `[NEEDS CLARIFICATION: ...]`; после clarification `/speckit.specify` должен расширить и укрепить draft [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md). Для CSDD это полезный пример того, как constitutional workflow может явно запрещать прямую реализацию из недоуточнённого seed.

### Compliance traceability matrix

Compliance traceability matrix — центральный проверочный артефакт. В статье Table 1 мапит principle и CWE на file, line numbers и implementation technique. Примеры:

- Password Hashing / `CWE-522` -> `core/security.py` lines 14-24 -> bcrypt, cost 12.
- JWT Authentication / `CWE-287` -> `core/security.py` lines 27-81 -> `python-jose`, HS256.
- Authorization Check / `CWE-862` -> `services/account_service.py` lines 102-108 -> ownership verification.
- SQL Injection Prevention / `CWE-89` -> `services/*.py` -> SQLAlchemy ORM.
- Input Validation / `CWE-20` -> `schemas/*.py` -> Pydantic v2.
- Error Sanitization / `CWE-200` -> `main.py` lines 78-94 -> generic messages.

Reference implementation хранит похожий документ [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md). В нём mappings расширены: OAuth2 bearer dependency, CORS configuration, server-side validation, SQLAlchemy `select().where()`, sensitive field filtering, health checks, correlation IDs, audit trail, `.gitignore` для секретов. Документ помечен как auto-generated from codebase analysis, что важно для будущего текста: CSDD нуждается в tooling, иначе matrix быстро станет ручной декларацией.

Mad Devs даёт полезную практическую норму для matrix: одной колонки “какое правило затронуто” недостаточно. Нужны как минимум две связи: implementing artifact связывает constitutional rule с конкретным кодом или архитектурным решением, а verification method связывает этот код с тестом, Semgrep rule, secret scanner, PR review или другим проверяемым свидетельством. Без обеих связей matrix фиксирует намерение, а не покрытие. В их рабочем процессе traceability лежит в `/docs/compliance/traceability.md` и обновляется через обязательный блок PR template: изменения проверены against `constitution.md`, перечислены новые constraints или `N/A`, обновлена matrix с ссылкой на commit или `N/A`, указан constitutional override или `N/A` [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).

DocGuard добавляет к этому более общий угол трассируемости: команда `docguard trace` и guard-time Traceability validator работают с requirement IDs вроде `FR`, `SC`, `NFR`, `US`, `AC`, `T` и поддерживают прямую и обратную трассировку через `trace --reverse <file>` [DocGuard README](https://github.com/raccioly/docguard). Для CSDD это полезно как форма будущего требования к инструментам: security traceability должна уметь идти не только от `SEC-*` к коду, но и от файла кода обратно к требованиям, задачам и constitutional clauses. Иначе reviewer видит строку matrix, но не видит, какие изменения в коде стали orphaned относительно спецификации.

Foundry Constitution добавляет ещё одну форму traceability: при MINOR-or-greater release coverage matrix должна быть пересобрана как principle -> enforcing FRs, а любая строка `GAP` блокирует release. При изменении Constitution downstream artifacts должны быть заново проверены: `spec.md` должен сохранять хотя бы один enforcing FR на каждый principle, `README.md` должен согласоваться с количеством principles and workflow description, generated `plan.md` and `tasks.md` должны проходить `/speckit.analyze`, а agent guidance/system prompts должны сверяться, если они ссылаются на номера principles [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Это усиливает мысль досье: matrix нужна не только от principle к code line, но и от principle к specification requirements and agent-facing guidance.

### Reference implementation

Reference implementation: [srinivasraom/banking-ms-by-constitution](https://github.com/srinivasraom/banking-ms-by-constitution). GitHub page на момент прохода показывает branch `001-banking-crud`, 6 commits, folders `.claude/commands`, `.specify`, `backend`, `frontend`, `specs/001-banking-crud`, files `CLAUDE.md`, `CONSTITUTION_COMPLIANCE.md`, `PAPER.md`, `README.md`, `docker-compose.yml`, `start.sh`, `stop.sh`.

README описывает full-stack banking application: backend API на port `4001`, frontend на port `4002`, FastAPI + Python, React + TypeScript, SQLite/PostgreSQL, audit logs, middleware, service layer, repository layer. Security features включают JWT tokens, bcrypt password hashing, 15 minute access token, 7 day refresh token, resource-based access control, ownership verification, Pydantic schemas, E.164 phone validation, age verification 18+, decimal precision, SQLAlchemy ORM, CORS configuration, sensitive data filtering, structured JSON logging, correlation IDs and audit trail [GitHub README](https://github.com/srinivasraom/banking-ms-by-constitution).

README authentication flow показывает ещё одну неудобную деталь: после регистрации и login frontend сохраняет JWT tokens в `localStorage` [GitHub README](https://github.com/srinivasraom/banking-ms-by-constitution). Это не нужно превращать в самостоятельный обвинительный вывод без полного security review, но для досье важно сохранить риск: compliance matrix и Constitution могут хорошо покрывать хеширование паролей на backend, JWT verification, ownership checks и audit logging, но решение о хранении токенов во frontend тоже должно попадать в evidence surface, иначе часть security posture остаётся вне трассировки.

В проходе 03 дополнительно зафиксирован статус самого GitHub-источника: страница репозитория показывает 0 issues, 0 pull requests, 0 releases, 6 commits, 0 stars и 1 fork; README заканчивается license section `Private - All rights reserved` [GitHub repository](https://github.com/srinivasraom/banking-ms-by-constitution). Для досье это означает две вещи. Во-первых, из issues/PR сейчас почти нечего извлекать как свидетельство внедрения, исправлений или внешней проверки. Во-вторых, схемы README и код репозитория можно использовать как источник фактуры о методе, но нельзя автоматически считать их свободно переиспользуемыми иллюстрациями или шаблонами без отдельной проверки прав.

`CLAUDE.md` в репозитории работает как агентная память поверх `.specify` artifacts: он явно говорит, что файл auto-generated from active feature plans, и перечисляет constitutional requirements, development commands, technology stack and project structure [CLAUDE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CLAUDE.md). В нём есть полезная фактура о том, что агенту нужно держать в рабочем контексте: authentication/authorization, validation, audit logging, OpenAPI contracts, API versioning, environment variables and Docker commands. Одновременно там остались template traces вроде bracketed placeholders для структуры и команд. Это хороший маленький пример риска generated context documents: если такой файл воспринимается агентом как authoritative memory, нерешённые placeholders могут стать шумом или ложным сигналом.

## Роли и участники

Источник не строит сложный role layer. Главные участники:

- developer/team, которые формулируют и ратифицируют Constitution;
- AI assistant, который генерирует код под constraints;
- security reviewer или security team, которые утверждают изменения в security principles;
- architecture team или principle owners, если amendments затрагивают architecture или microservices rules;
- auditors/regulators как downstream consumers compliance matrix.

В reference Constitution governance section требует documentation, team review and explicit approval. Amendments проходят через pull request, security team review для security principles, architecture team review для microservices principles, минимум 2 approvals from principle owners и semantic versioning. Compliance review требует Constitution Check в каждом pull request, quarterly reviews и remediation timeline для violations [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md).

Foundry показывает более насыщенный role layer для соседнего security-evaluation процесса. Core roles: Operator, Orchestrator, Indexer, Cartographer, Detector, Triager, Validator, Reporter and Coverage-Guide; extension roles: Deep-Tester, Variant-Hunter, Attack-Mapper, Remediator and Self-Improver. Важно, что roles описаны не как personas для текста, а через purpose, triggers, inputs, outputs, functional requirements, invariants, rationale and cost of omitting/merging/splitting [Foundry spec.md §5](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md). Для CSDD это соседний пример того, как role layer может быть специфицирован как рабочая система, а не как список участников.

## Human gates

CSDD требует более жёстких human gates, чем обычное “спросить агента сделать безопасно”.

- Gate 1: человек утверждает Constitution, источники security constraints и границы domain-specific требований.
- Gate 2: feature spec проверяется на реальные references to constitutional clauses, а не на generic “make secure”.
- Gate 3: plan и tasks проверяются на то, что security constraints не выпали при техническом разложении.
- Gate 4: перед implementation полезен read-only consistency gate, если CSDD реализуется поверх Spec Kit: `/speckit.analyze` проверяет spec/plan/tasks against Constitution, а conflicts with MUST principles должны считаться critical, не косметическими замечаниями [Spec Kit analyze command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md).
- Gate 5: перед merge проверяется compliance traceability matrix: principle -> implementation artifact -> file/line -> technique.
- Gate 6: подтверждение не сводится к словам агента; нужны tests, SAST/DAST, dependency scanning, code review checklist или audit-ready matrix.
- Gate 7: если нужно нарушить constitutional rule, исключение оформляется как explicit override с обоснованием, сроком действия и следом в PR/checklist; без такого escape valve жёсткие правила начинают обходить неформально, и это хуже для governance, чем видимое исключение [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).

Issue #697 показывает полезную форму Gate 4 как проверку артефактов, а не абстрактный “review by AI”: `C1` ловит ситуацию, где plan отмечает Phase 0 and Phase 1 complete and Post-Design Constitution Check PASS, но `research.md`, `data-model.md`, `quickstart.md` and `contracts/` отсутствуют; рекомендация — создать отсутствующие артефакты или снять галочки и заново пройти Constitution checks [Spec Kit Issue #697](https://github.com/github/spec-kit/issues/697). Для CSDD это значит, что pass/fail gate должен проверять не только текст утверждения “Constitution Check PASS”, но и существование downstream artifacts, которые этот pass предполагает.

DocGuard даёт практический вариант Gate 4/Gate 5 как инструментального gate: `docguard guard` проверяет mandatory sections, IDs, phased tasks, расположение `constitution.md` и трассируемость, а `guard`/`diagnose --format json` делает результат машинно-читаемым для CI и агентов [DocGuard README](https://github.com/raccioly/docguard). Для CSDD это полезно не как готовая security verification, а как форма требования к инструментам: constitutional gate должен выдавать структурированный результат, который можно блокировать в CI и который агент может использовать для targeted remediation.

Reference Constitution прямо задаёт development gates: Design Review, Security Review, Contract Verification, Code Review with security checklist. Testing requirements включают unit tests >80% coverage, integration tests, end-to-end tests for critical user journeys and performance tests. Deployment requirements запрещают manual deployments, требуют CI/CD, blue-green/canary deployments, rollback procedures and backward-compatible database migrations [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md).

Есть ещё один gate, который легко потерять: amendment gate. Если меняется сам Constitution, человек утверждает не только новую формулировку principle, но и migration plan для существующих систем, ожидаемый version bump и влияние на зависимые артефакты [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md). Для CSDD это критично, потому что изменение Constitution без пересмотра `spec.md`, `plan.md`, `tasks.md`, agent memory and compliance matrix создаёт иллюзию governance.

Mad Devs предлагает ставить ещё один human gate до самой Constitution: threat model пишется параллельно с product spec, а Constitution выводится из этого threat model. Для каждой угрозы нужен хотя бы один запрет и хотя бы одна требуемая mitigation; каждое правило сразу классифицируется как machine-checkable или review-only. Это полезная детализация для CSDD: rule без соответствующей угрозы становится шумом, а угроза без соответствующего rule превращается в gap в specification layer [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).

Foundry добавляет human gates вокруг уточнения и governance. README прямо говорит: не переходить к `/speckit.plan`, пока маркеры `[NEEDS CLARIFICATION]` остаются, потому что маркер, доживший до plan, превращается в догадку, встроенную в design. Constitution governance требует, чтобы pull request, touching `spec.md` or `constitution.md`, identified affected principles and linked enforcing FRs; при MINOR-or-greater release regenerated coverage matrix blocks the release on any GAP row [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md) [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Для CSDD это переносимый gate: человек должен утвердить не только формулировку principle, но и то, где этот principle enforced downstream.

## Проверка результата

Статья даёт три слоя проверки.

Первый — qualitative prevention examples. В case study AI initially generated insecure code, а constitutional validation forced correction:

- raw SQL query through Python f-string violated `SEC-002` / `CWE-89`, затем был заменён на SQLAlchemy `select(Transaction).where(...)`;
- password in audit log violated `SEC-015` / `CWE-532`, затем sensitive fields were excluded;
- account retrieval without ownership check violated `SEC-010` / `CWE-862`, затем `customer_id` ownership verification был добавлен;
- transfer endpoint with `float` amount, negative amounts and unbounded precision violated `SEC-006` / `CWE-20` and `SEC-007` / `CWE-190`, затем Pydantic schema switched to `Decimal`, regex account numbers, positive amount, max `1000000`, `decimal_places=2` and same-account validation [ar5iv §5.2](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Второй — количественные metrics. Статья сравнивает constitutional implementation с unconstrained AI generation baseline, используя same banking application requirements, same AI assistant and same developer. Table 3 claims:

- CWE violations detected: 3 vs 11, 73% reduction;
- time to first secure build: 4 days vs 9 days, 56% faster;
- compliance documentation: 100% vs 23%, 4.3x coverage;
- security review iterations: 1 vs 4, 75% reduction;
- lines of security code: 847 vs 612, 38% more thorough [ar5iv §5.3](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Третий — compliance verification summary. Table 4 claims 15 constitutional principles defined, 15 fully implemented, 47 specific code locations mapped, 10 CWE vulnerabilities in scope, 10 addressed and 0 compliance gaps [ar5iv §5.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Эти числа нужно использовать осторожно. Threats to validity включают single development team with prior security training, possible Hawthorne effect, one banking domain with well-understood security requirements, reliance on static analysis and manual review, and small sample size `n=1 project` [ar5iv §6.6](https://ar5iv.labs.arxiv.org/html/2602.02584v1). В будущем тексте нельзя превращать 73% в универсальное обещание.

В verification section полезна ещё одна рабочая формула: compliance проверяется не как бинарное pass/fail, а как трасса от principle к implementation location and technique. Это можно перенести в будущую теорию как требование к evidence: ссылка на `SEC-*` без file/line/technique остаётся намерением, а не проверяемым доказательством [ar5iv §5.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Spec Kit расширяет это понимание проверки за пределы security matrix. В `spec-driven.md` templates описаны как ограничения поведения LLM: явные `[NEEDS CLARIFICATION]` markers не дают модели угадывать, checklists работают как self-review tests, порядок создания файлов продвигает contracts and tests до implementation, а constitutional gates требуют documented justification, если architectural principles не соблюдены [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md). В CSDD эту механику стоит читать строже: `SEC-*` clauses нужны не только в итоговых строках matrix, но и в ранних ambiguity markers, test-first constraints and gate failures, которые останавливают небезопасную implementation до появления кода.

DocGuard полезен здесь как пример разделения механических исправлений и исправлений, которые должен делать агент. README описывает deterministic fixes через `docguard fix --write` для сгенерированных sections и agent-routed fixes через `diagnose` / `fix --doc`, когда нужно переписать содержательный документ [DocGuard README](https://github.com/raccioly/docguard). Для CSDD это важная граница: часть compliance drift можно чинить механически, но изменение security rule, threat model, rationale or exception не должно автоматически переписываться инструментом без человеческого решения.

Foundry уточняет, что значит проверяемый security finding в агентной системе. `true-positive` требует evidence gate: cited code locations for reachability, trust boundary and impact; every cited location must be mechanically verified to resolve to real code, otherwise verdict is demoted to `needs-review`. `exploited` flag ставится только после независимого clean-room reproduction на live testbed, и это не должен делать тот же агент, который написал proof-of-concept [Foundry spec.md §7](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md) [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Для CSDD это не замена compliance matrix, но сильная проверочная норма: evidence должно быть воспроизводимым и отделённым от уверенности модели.

Foundry также задаёт done condition для security evaluation: coverage complete plus yield below threshold; одного условия недостаточно. Для CSDD это важно потому, что matrix со всеми заполненными строками не обязательно является полным сигналом готовности: source-scoped coverage, unresolved goals and diminishing yield — разные виды evidence, и их нельзя сводить к одной зелёной отметке [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md).

## Контекст и где он живёт

В CSDD важно разделение контекста:

- устойчивые principles живут в Constitution, например `.specify/memory/constitution.md`;
- requirements фичи живут в `spec.md`;
- technical choices живут в `plan.md`;
- actionable queue живёт в `tasks.md`;
- agent-facing project memory живёт в `CLAUDE.md` и `.claude/commands`;
- proof of compliance живёт в `CONSTITUTION_COMPLIANCE.md` или аналогичной matrix;
- generated code lives in implementation directories;
- agent command layer может жить в `.claude/commands` or Spec Kit commands.

Такое разделение снижает риск, что security constraints останутся только в истории запросов. Но оно создаёт другой риск: если артефакты расходятся, project получает несколько источников правды. Поэтому matrix и проверки согласованности артефактов важнее, чем само наличие файлов.

Практическое руководство Mad Devs уточняет слабое место этого разделения: сам файл `constitution.md` ничего не гарантирует, если агент его не читает. Для Cursor авторы различают root `AGENTS.md`, который читается автоматически, и `.cursor/rules/`, которые могут подгружаться по релевантности; для GitHub Copilot предлагают явно ссылаться на Constitution из repository custom instructions; для custom agents — добавлять Constitution как high-priority context перед task instruction. Отсюда рабочий вывод для CSDD: подключение Constitution к agent guidance является отдельным артефактом метода, а не технической мелочью после написания правил [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).

DocGuard показывает ту же проблему через генерацию конфигурационных файлов для агентов: `docguard init --with agents` создаёт `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/` and `.github/copilot-instructions.md`, а slash commands устанавливаются в `.github/commands/`, `.cursor/rules/`, `.gemini/commands/`, `.claude/commands/` and `.agents/workflows/` [DocGuard README](https://github.com/raccioly/docguard). Для CSDD это полезная фактура о месте контекста: Constitution должна быть связана с конкретными файлами поверхности, которые реально читает выбранный агент; “у нас есть constitution.md” недостаточно, если adapter агента не подхватывает этот файл.

Foundry раскладывает контекст security evaluation ещё детальнее: operator provides target, source code, optional testbed and evaluation goals; Indexer builds code index, Cartographer creates architecture, attack-surface, trust-boundary, data-flow and threat-model documents, Detector uses rule corpus and exploration, Triager reads candidates with index and security map, Validator receives only artifact and claim for clean reproduction, Reporter writes confirmed findings, Coverage-Guide tracks goals and done state [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md). Для CSDD это полезное напоминание: чем больше агентных ролей, тем важнее явно указать, какой контекст каждая роль может читать и записывать, и какие артефакты имеют authority.

Foundry Constitution also contains a rule about authority inside agent context: operator instructions outrank peer-agent messages and prior-agent notes. Agent notes are records of attempted work, not facts; otherwise agents can talk each other into skipping work and cite their own consensus as evidence [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Для Constitutional SDD это важная оговорка по governance: persistent agent notes and summaries не должны быть авторитетнее утверждённых Constitution, spec and operator intent.

## Связь со Spec Kit

Статья прямо ссылается на Speckit / GitHub Spec Kit и в конце перечисляет slash commands: `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement` [ar5iv §7.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

Актуальный README [github/spec-kit](https://github.com/github/spec-kit) подтверждает эти команды и добавляет важные детали: большинство агентов используют `/speckit.*`, а Codex CLI в skills mode использует `$speckit-*`; `/speckit.constitution` создаёт governing principles проекта в `.specify/memory/constitution.md`; `/speckit.specify` задаёт requirements and user stories; `/speckit.plan` создаёт technical implementation plans; `/speckit.tasks` генерирует task lists; дополнительные `/speckit.clarify`, `/speckit.analyze` and `/speckit.checklist` поддерживают уточнение требований, анализ согласованности и requirements-quality checklists [Spec Kit README](https://github.com/github/spec-kit).

Для этого досье важно не смешать две вещи. Spec Kit — общий toolkit для SDD workflow. CSDD — security/governance specialization, которая использует похожий или тот же artifact pipeline, но делает Constitution security-critical и связывает его с CWE/regulatory traceability.

Официальные command templates Spec Kit уточняют, как Constitution удерживается в рабочем процессе. `/speckit.constitution` не только создаёт файл `.specify/memory/constitution.md`: команда должна загрузить существующую Constitution, заполнить placeholder tokens, принять решение о semantic version bump, проверить dependent artifacts and templates, обновить `plan-template.md`, `spec-template.md`, `tasks-template.md` and command files при изменении принципов, а затем добавить Sync Impact Report в начало Constitution [Spec Kit constitution command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md). Это важная механика для CSDD: amendment не должен быть локальной правкой одного документа, иначе Constitution перестаёт управлять следующими артефактами.

`/speckit.plan` отдельно загружает feature spec и `/memory/constitution.md`, заполняет `Constitution Check`, оценивает gates, создаёт `research.md`, `data-model.md`, `contracts/`, `quickstart.md` и обновляет agent context, а затем повторно проверяет Constitution Check after design [Spec Kit plan command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md). В `plan-template.md` этот gate встроен в сам план: он должен пройти до Phase 0 research и быть перепроверен после Phase 1 design [Spec Kit plan template](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md). Для CSDD это даёт рабочую форму human/agent gate: если правило Constitution нарушено, нарушение надо явно остановить или обосновать, а не прятать в поздней реализации.

`/speckit.tasks` строит `tasks.md` из `plan.md`, `spec.md`, optional `data-model.md`, `contracts/`, `research.md`, `quickstart.md` и, если есть, `/memory/constitution.md`; задачи должны иметь ID, file paths, user-story labels, dependency order and independently testable increments [Spec Kit tasks command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/tasks.md). `tasks-template.md` добавляет Phase 2 Foundational как блокирующую фазу до любых user stories и включает примеры authentication/authorization, API routing, error handling, logging and environment configuration [Spec Kit tasks template](https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md). Это помогает объяснить, почему task-level dilution в reference implementation важен: общий Spec Kit уже требует исполнимые задачи, но CSDD требует ещё и видимую трассу от задач к security clauses.

`/speckit.analyze` добавляет ещё один проверочный слой перед implementation: команда строго read-only, запускается после `tasks.md`, строит cross-artifact consistency and coverage analysis across `spec.md`, `plan.md` and `tasks.md`, загружает Constitution, а conflicts with MUST principles считает `CRITICAL`; если нужно менять сам principle, это должно происходить отдельным explicit constitution update, не внутри analysis [Spec Kit analyze command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md). Для будущей теории это почти готовая формулировка gate: Constitution является authority, а spec/plan/tasks должны подстраиваться под неё, если конфликт обнаружен до реализации.

`spec-driven.md` описывает constitutional foundation через “Nine Articles of Development”: library-first, CLI interface, test-first, simplicity, anti-abstraction and integration-first testing. Эти articles не являются security Constitution Marri, но показывают форму enforcement: plan template превращает principles в checkpoints, например Simplicity Gate, Anti-Abstraction Gate and Integration-First Gate; если gate fails, justification goes to Complexity Tracking [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md). Для CSDD полезна сама форма: security principles должны становиться named checkpoints with explicit failure handling, а не фоновым советом.

Community extensions показывают, что Spec Kit уже развивается как ecosystem расширений, а не только как набор базовых slash commands. В каталоге есть `DocGuard — CDD Enforcement`, который валидирует, оценивает и трассирует project documentation через automated checks, AI workflows and spec-kit hooks; там же есть extension types `docs`, `code`, `process`, `integration`, `visibility` and effects `Read-only` / `Read+Write` [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html). Для CSDD это важная граница доверия: чем больше enforcement вынесен в extensions and hooks, тем больше нужно проверять не только Constitution, но и сам код/политику расширений, которые получают право читать или менять governance artifacts.

Foundry explicitly says the seed is written to be consumed by Spec Kit or any spec-driven development workflow: clarification resolves open questions against the organization environment, then the result becomes the organization's spec and implementation on its own stack [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md). Это полезный источник для границы между Spec Kit and CSDD: Spec Kit provides the artifact machine, а constitutional security sources могут давать domain-specific authority files and seed specifications поверх этой машины.

## Сильные стороны

CSDD хорошо показывает, как security можно сделать upstream constraint, а не проверкой в конце. Его сильные стороны:

- security constraints становятся repository artifact with versioning and governance;
- constraints получают CWE/regulatory provenance;
- feature specs and implementation plans должны учитывать constraints before generation;
- compliance matrix даёт audit surface: principle, CWE, file, line, technique;
- метод хорошо подходит для regulated domains, где auditability не менее важна, чем функциональность;
- case study сохраняет concrete rejected/accepted examples, которые показывают реальную форму failure prevention.

Ещё одна сильная деталь — урок по управлению контекстом. Статья показывает, что “дать агенту весь Constitution” хуже, чем выбрать task-relevant principles: full constitution 15 principles gave 78% compliance quality, relevant selection 3-5 principles gave 96%, hierarchical 5-8 principles gave 91% [ar5iv §6.2](https://ar5iv.labs.arxiv.org/html/2602.02584v1). Для AI-driven SDLC это важный counterexample против наивной идеи “больше контекста всегда лучше”.

Foundry добавляет к сильным сторонам CSDD ещё один переносимый паттерн: иногда публиковать нужно не tool, а spec, потому что implementation code слишком завязан на инфраструктуру. README explains that Cisco's internal systems were tightly coupled to its cloud provider, issue tracker, LLM gateway and deployment platform; what transfers is the design: roles, finding flow, done criteria, quality gates and shortcuts that hurt later [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md). Для будущей теории это помогает отделить методологический артефакт от reference implementation.

## Failure modes / overuse risks

- **Compliance theater**: Constitution существует, но feature spec, plan, tasks and code не ссылаются на clauses, а matrix заполняется задним числом.
- **Vague constitution**: правила вроде “follow secure coding practices” не дают enforceable constraints. Статья прямо пишет, что specificity enables enforcement; vague principles gave inconsistent compliance, CWE identifiers and implementation patterns improved compliance [ar5iv §6.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).
- **Constitution drift**: ad-hoc amendments ослабляют security. Нужны semantic versioning and approval workflows.
- **Specification poisoning / prompt injection**: Constitution itself becomes an attack surface because AI agents consume it as natural-language instruction. Source recommends treating constitution files like security-critical artifacts with access controls, code review and integrity verification [ar5iv §6.1, §6.5](https://ar5iv.labs.arxiv.org/html/2602.02584v1).
- **Known-vulnerability boundary**: CWE/OWASP-derived clauses cover known patterns, not zero-day classes.
- **Technical-only bias**: constraints help with injection/auth/storage/logging, but may miss business logic flaws specific to the application.
- **AI capability dependency**: method assumes the model can understand principles and translate them into correct implementation.
- **Context overload**: large Constitution can exceed or dilute model context; selecting principles is itself a workflow step.
- **Ослабление на уровне задач**: Constitution может быть сильным в `.specify/memory/constitution.md` и `plan.md`, но ослабнуть при переходе в `tasks.md`. В референс-репозитории `tasks.md` задаёт полезные инженерные задачи, однако не повторяет explicit `SEC-*`/CWE references рядом с задачами. Это создаёт место, где агент может выполнять правильные технические работы без явной трассы к конкретным clauses [tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md).
- **Template drift при amendment**: официальный `/speckit.constitution` требует после изменения Constitution проверить dependent templates and commands и добавить Sync Impact Report. Если организация меняет principles вручную, но не обновляет `plan-template.md`, `tasks-template.md`, commands and agent guidance, новый principle остаётся декларацией и не становится рабочим constraint [Spec Kit constitution command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md).
- **Hook opacity**: Spec Kit commands поддерживают extension hooks before/after constitution, plan, tasks and analyze. Это расширяет метод, но для security-critical CSDD создаёт дополнительный слой доверия: mandatory hook может фактически стать частью enforcement path, а optional hook может быть пропущен человеком [Spec Kit constitution command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md).
- **Граница доверия community extensions**: официальный каталог Spec Kit прямо предупреждает, что community extensions поддерживаются независимыми авторами; мейнтейнеры проверяют полноту catalog entry, но не аудируют и не поддерживают код расширения. Если CSDD полагается на extension вроде DocGuard как на gate, source review and version pinning становятся частью governance, а не необязательной настройкой [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html).
- **Шум в generated context**: agent memory files вроде `CLAUDE.md` помогают переносить правила между сессиями, но если в них остаются шаблонные placeholders или устаревшие команды, они становятся отдельным источником рассинхронизации. Это особенно опасно в CSDD, потому что agent-facing context фактически участвует в enforcement path [CLAUDE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CLAUDE.md).
- **Слепая зона client-side security**: README показывает хранение JWT tokens в `localStorage`. Если Constitution и matrix проверяют в основном backend files, такое решение может остаться вне line-level evidence. Это пример того, почему CSDD должен трассировать не только backend services, но и клиентские решения, которые меняют threat model [GitHub README](https://github.com/srinivasraom/banking-ms-by-constitution).
- **Weak empirical base**: `n=1` project, one team, one banking domain. Quantitative claims need replication.
- **Artifact inconsistency**: paper says 15 principles and 10 CWE vulnerabilities in scope; raw reference Constitution lists broader rules and more CWE references than the paper’s compact implementation table. This is not necessarily a contradiction, but the final text should avoid pretending the numbers are cleaner than the sources.
- **Неясность с tooling**: `CONSTITUTION_COMPLIANCE.md` заявляет auto-generation from codebase analysis, но в публичной source surface пока не видна именованная команда генератора. Пока это не проверено, matrix лучше считать evidence artifact плюс открытым вопросом по tooling, а не доказательством повторяемого автоматического checker [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md).
- **Thin public feedback surface**: reference repository currently shows 0 issues, 0 pull requests and no releases. Это не опровергает paper, но не даёт независимой истории внедрения, сообщений о сбоях, исправлений или community validation [GitHub repository](https://github.com/srinivasraom/banking-ms-by-constitution).
- **Reuse rights risk**: README репозитория публичен, но license section says `Private - All rights reserved`; diagrams and code лучше считать источником фактуры, а не переиспользуемыми site assets, пока права не проверены [GitHub repository](https://github.com/srinivasraom/banking-ms-by-constitution).
- **Aspirational rules**: если у constitutional rule нет enforcement path — автоматической проверки, checklist item, traceability entry или обязательного review — он остаётся текстом, а не рабочим constraint. Mad Devs формулирует это как границу между rule with defined enforcement path и rule that exists only as text [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).
- **Matrix staleness**: traceability matrix быстро устаревает в быстрых спринтах, если её обновление выглядит как дополнительная бумажная работа. Практическая рекомендация — сделать matrix update blocking PR checklist item, иначе compliance artifact будет собираться задним числом перед audit [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).
- **Spec security boundary**: Constitution усиливает specification-time security, но не заменяет runtime security. Даже compliant codebase может провалиться из-за misconfigured infrastructure, compromised dependencies или угроз, которых не было в исходном threat model; значит, CSDD должен жить рядом с monitoring, penetration testing and incident response, а не вместо них [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/).
- **Constitution authoring ambiguity**: Issue #40 in `github/spec-kit` показывает, что даже в официальном Spec Kit контексте пользователь может не понимать, должен ли он взять готовую “Nine Articles” Constitution, найти полный hidden template или создать project-specific Constitution himself. Для CSDD это опаснее, чем для обычного architecture guide: заимствованная generic Constitution может выглядеть authoritative, но не отражать threat model, regulatory controls and domain-specific security constraints [Spec Kit Issue #40](https://github.com/github/spec-kit/issues/40).
- **Seed mistaken for spec**: Foundry explicitly warns not to implement directly from `spec.md`; это seed для `/speckit.clarify`, а не законченная specification. Если команда берёт seed как готовый plan, маркеры `[NEEDS CLARIFICATION]` превращаются в скрытые design guesses, а Constitution начинает проверять артефакты against unresolved assumptions [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md).
- **Evidence dilution**: Foundry's Evidence Over Assertion principle exists because model confidence is not enough for a vulnerability verdict; citations must resolve and evidence must show reachability, trust boundary and impact. Для CSDD аналогичный риск — строка compliance matrix, которая называет файл, но не содержит evidence, достаточно сильного для воспроизведения security argument [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) [Foundry spec.md §7.3](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md).
- **Authority inversion inside agent memory**: Foundry warns that peer-agent notes and prior-agent conclusions must not outrank operator instructions. В CSDD такой же риск возникает, когда persistent summaries, `CLAUDE.md`, agent notes or generated reports считаются более актуальными, чем решения в Constitution/spec/plan [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md).

## Хвост жизненного цикла

CSDD не заканчивается реализацией. Хвост жизненного цикла включает:

- amendment process for Constitution changes;
- quarterly compliance reviews;
- remediation timelines for violations;
- updating Constitution when regulatory frameworks, threat models or architecture constraints change;
- regenerating or updating traceability matrix after code changes;
- targeted regression tests based on affected principles;
- отношение к constitution files как к security-critical artifacts with access control and review.

Future work in the paper also points to automated constitution generation from regulatory documents like PCI-DSS/HIPAA, real-time IDE validation, constitution inheritance across projects, and broader empirical studies across teams, domains and AI models [ar5iv §7.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1).

В reference Constitution хвост жизненного цикла выглядит более операционно: quarterly compliance reviews, remediation timelines for violations, update when threat model changes, mandatory code review with security checklist, CI/CD-only deployments, rollback procedures and backward-compatible database migrations [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md). Это стоит перенести в Handbook как пример того, что Constitution управляет не только генерацией кода, но и сопровождением изменения после merge.

Foundry показывает lifecycle for Constitution-as-seed: amendment requires documenting the scenario where the current principle produces worse outcome than violating it, version bump/date/rationale, PR-level affected-principle disclosure, periodic regeneration of principle -> enforcing FRs coverage matrix, and revalidation of `spec.md`, `README.md`, generated `plan.md`, generated `tasks.md` and agent guidance on MINOR-or-greater change [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md). Для CSDD это хороший материал для Handbook: изменение Constitution должно запускать downstream synchronization, а не только текстовое утверждение.

## Что должно попасть в теорию

Для теории AI-driven SDLC CSDD стоит использовать как strong case of governance-as-specification:

- Слой намерения может включать non-negotiable security and governance constraints, not only feature requirements.
- Constitution отличается от spec/plan/tasks: он стабильнее и управляет следующими артефактами.
- Traceability is the mechanism that prevents “security prompt” from becoming decoration.
- Context selection is an engineering decision: relevant clauses beat dumping the whole Constitution into the prompt.
- Amendment propagation is part of the method: if a Constitution changes, templates, commands, agent memory and downstream artifacts must be checked, otherwise governance lives in one file only.
- Read-only analysis before implementation is a useful pattern: `spec.md`, `plan.md` and `tasks.md` can be checked against Constitution before any code is generated.
- Human gates are part of the method, not optional overhead.
- Security evidence must be externalized: matrix, tests, static analysis, review records.
- Constitution amendment is a lifecycle event: version bump, migration plan and downstream artifact synchronization matter as much as the new principle text.
- A compliance matrix must include frontend and operational decisions when they affect the threat model; backend-only evidence can leave real security choices outside the method.
- Constitutional gates should verify downstream artifacts, not only checked boxes: если plan claims PASS, ожидаемые `research.md`, `contracts/`, tests, tasks and matrix rows должны существовать, иначе gate остаётся слабым как свидетельство.
- Enforcement tooling is part of the governance surface: CI gates, hooks, JSON reports, version pins and reverse traceability decide whether Constitution is executable or only textual.
- Seed specification может быть переносимым артефактом, когда code infrastructure-specific; тогда метод живёт в clarification questions, authority rules and artifact gates, а не в reusable binary.
- Качество evidence нужно задавать как отдельный gate: security verdict требует воспроизводимого evidence, а не confidence модели or гладкого объяснения.
- Claims about velocity/security improvement must remain source-scoped because the study is small.

## Что лучше уйдёт в Handbook / Fieldbook

- Template for a security Constitution: identifier, CWE, enforcement level, constraint, implementation pattern, rationale, owner, amendment rule.
- Checklist for feature spec review: every security-relevant requirement references clauses; no generic “make secure”.
- Checklist for compliance matrix: principle, CWE/control, file, line/range, implementation technique, test/evidence, owner.
- Prompt pattern: “use only these 3-5 relevant constitutional principles for this task”.
- Red flags: broad principle, no CWE/control mapping, no owner, no amendment process, matrix without line-level evidence.
- Practical mapping examples: `SEC-002` -> ORM queries; `SEC-010` -> ownership verification; `SEC-015` -> sensitive field redaction.
- Operational checklist for Constitution amendment: version bump, Sync Impact Report, dependent template review, command review, agent context update and explicit follow-up TODOs.
- Pre-implementation analysis checklist: no Constitution MUST conflicts, no security requirement without task coverage, no task that bypasses required artifact references, no unresolved placeholders in agent-facing context.
- Evidence checklist for client-side security: token storage, refresh flow, CORS/origin rules, sensitive data in frontend logs, and whether these decisions appear in traceability matrix.
- Шаблон учёта цены метода: initial Constitution effort, matrix maintenance time, предотвращённые security review iterations, defects found before merge and rework saved.
- Threat-model-first шаблон: assets, trust boundaries, top threats per boundary, для каждой угрозы — prohibition, required mitigation, enforcement type and review owner.
- PR template block for constitutional compliance: checked against `constitution.md`, new constraints listed or `N/A`, traceability matrix updated with commit link or `N/A`, override linked or `N/A`.
- Enforcement classification table: pattern-level prohibition -> Semgrep/custom linter; secrets -> secret scanner; dependency constraint -> dependency scanner/lockfile audit; data handling -> integration test/PR checklist; architecture invariant -> architecture test/review; process obligation -> PR template gate.
- Override protocol template: affected rule, reason, safer alternatives considered, approving owner, expiration/review date, compensating controls and follow-up task.
- Constitution authoring checklist: start from project threat model and domain constraints, not from copied generic “Nine Articles”; require owner, rationale, enforcement path, affected templates, and downstream review before treating the file as authoritative.
- Tool gate checklist: `docguard guard`/analog passes in CI, structured JSON output archived, reverse traceability checked for touched files, extension version pinned, and community extension source reviewed before granting it write access to governance artifacts.
- Seed-to-spec checklist: read Constitution, install/copy Constitution into `.specify/memory/constitution.md`, copy seed `spec.md`, run `/speckit.clarify`, resolve all markers, run `/speckit.specify`, repeat until no markers remain, then only proceed to plan/tasks/implementation.
- Evidence gate checklist for security findings: reachability citation, trust-boundary citation, impact citation, mechanically resolving code locations, independent reproduction for `exploited`, and demotion path to `needs-review`.
- Downstream revalidation checklist after Constitution change: affected principles in PR, enforcing FR links, regenerated principle -> FR coverage matrix, `spec.md`/`README.md` sync, generated plan/tasks re-analysis, agent guidance wording and numbering review.

## Источники

- [Constitutional Spec-Driven Development: Enforcing Security by Construction in AI-Assisted Code Generation](https://arxiv.org/abs/2602.02584) — primary paper. Использован для abstract claims, methodology, metrics, limitations, future work and metadata.
- [ar5iv HTML: Constitutional Spec-Driven Development](https://ar5iv.labs.arxiv.org/html/2602.02584v1) — readable full-text version. Использован для workflow details, principle structure, tables, listings, lessons learned and threats to validity.
- [arXiv PDF: Constitutional Spec-Driven Development](https://arxiv.org/pdf/2602.02584) — direct PDF. Использован в проходе 02 для сверки claims, tables, limitations and future work against ar5iv.
- [srinivasraom/banking-ms-by-constitution](https://github.com/srinivasraom/banking-ms-by-constitution) — reference implementation repository. Использован для repository structure, README architecture/security details, artifact names, public metadata, issue/release status and license caveat.
- [PAPER.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md) — repository paper draft / companion text. Использован для трёхфазной workflow Figure 4 and source-drift note; не должен перекрывать arXiv PDF при конфликте.
- [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md) — reference Constitution. Использован для governance, broader principles, development gates, testing and deployment requirements.
- [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) — compliance report. Использован для concrete principle-to-code mappings.
- [specs/001-banking-crud/spec.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/spec.md) — feature specification. Использован для user stories, functional requirements and edge cases.
- [specs/001-banking-crud/plan.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/plan.md) — implementation plan. Использован для tech stack, Constitution Check and artifact-drift caveat.
- [specs/001-banking-crud/tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md) — generated task list. Использован для task granularity and task-level dilution caveat.
- [CLAUDE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CLAUDE.md) — agent-facing project memory. Использован для context-location and generated-context-residue caveat.
- [github/spec-kit](https://github.com/github/spec-kit) — current Spec Kit README. Использован для command names, `.specify/memory/constitution.md`, additional commands and customization model.
- [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) — official SDD methodology note. Использован в проходе 06 для уточнения specification-as-source-of-truth, template-driven quality, constitutional gates, branch-reviewed specifications and lifecycle feedback.
- [Spec Kit command/template sources](https://github.com/github/spec-kit/tree/main/templates/commands) — official `constitution.md`, `plan.md`, `tasks.md`, `analyze.md`, `plan-template.md` and `tasks-template.md`. Использованы в проходе 03 для механики amendment propagation, Constitution Check, task generation, read-only analysis and extension hooks.
- [github/spec-kit Issue #697: Allow support for custom templates](https://github.com/github/spec-kit/issues/697) — public user issue. Использован в проходе 06 как слабый, но конкретный источник по `/analyze`, Constitution alignment, отсутствующим downstream artifacts and task/spec mapping gaps; не является официальной нормой CSDD.
- [github/spec-kit Issue #40: How to create a constitution?](https://github.com/github/spec-kit/issues/40) — public user issue. Использован в проходе 06 как источник риска Constitution authoring ambiguity; не является методологическим baseline.
- [Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/abs/2602.00180) — соседний SDD paper. В этом проходе использован только как contextual source for SDD spectrum; сравнительный синтез не делался.
- [From constitution.md to Compliance: A Practical Security Layer for SDD](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) — практическое руководство Pavel Zverev / Mad Devs от 18 мая 2026 года. Использовано в проходе 05 для подключения Constitution к agent guidance, классификации rules by enforcement path, threat-model-first workflow, PR checklist, сопровождения traceability matrix и runtime-security caveats. Ограничение: статья описывает практический workflow и constructed illustration, а не независимую репликацию метрик Marri.
- [DocGuard repository](https://github.com/raccioly/docguard) — community enforcement tool for Spec Kit/CDD. Использован в проходе 07 как источник по artifact validation loop, `guard`, `diagnose`, `trace`, reverse traceability, agent config generation, hooks and CI-gate mechanics. Ограничение: это соседний tooling source, не источник о CSDD Marri и не security replication.
- [docguard-cli on PyPI](https://pypi.org/project/docguard-cli/0.24.0/) — package metadata and release surface for DocGuard. Использован для сверки distribution/PyPI context and versioned package surface; не использован как независимое методологическое подтверждение.
- [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html) — official Spec Kit community catalog. Использован для статуса DocGuard as community extension and trust-boundary caveat: entries are checked for completeness, but extension code is not audited, endorsed or supported by maintainers.
- [Cisco Foundry Security Spec](https://github.com/CiscoDevNet/foundry-security-spec) — соседний production-derived seed specification для AI-assisted security evaluation. Использован в проходе 08 для workflow через Spec Kit, roles, evidence gates, done criteria, seed-vs-spec boundary, Constitution precedence and downstream revalidation. Ограничение: это не источник о CSDD Marri, не reference implementation banking case и не репликация quantitative claims.
- [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md) — источник по repository purpose, no-code/spec-as-deliverable choice, getting-started workflow, CodeGuard companion and detection-to-prevention flywheel.
- [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md) — seed specification. Использован для roles, success criteria, assumptions, finding lifecycle, evidence gate, open clarification markers and out-of-scope boundaries.
- [Foundry constitution.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) — Constitution with 11 principles. Использован для authority/precedence rules, Evidence Over Assertion, Sandbox By Infrastructure, Operator Outranks Every Agent, versioning, compliance review and downstream revalidation.
- [Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) — companion security skills/rules framework maintained as a CoSAI/OASIS open project. Использован только как context for Foundry's rule-corpus and detection-to-prevention flywheel; не использован как прямое подтверждение CSDD Marri.

## Поисковые формулировки

- `"Constitutional Spec-Driven Development" "Enforcing Security by Construction"`
- `"Constitutional Spec-Driven Development" arxiv 2602.02584`
- `"banking-ms-by-constitution" constitution`
- `"srinivasraom/banking-ms-by-constitution" ".specify/memory/constitution.md"`
- `"CONSTITUTION_COMPLIANCE.md" "Banking Microservices Application"`
- `"Spec Kit" "/speckit.constitution" ".specify/memory/constitution.md"`
- `"Constitutional SDD" "CWE" "traceability matrix"`
- `"software constitution" "CWE" "AI-assisted code generation"`
- `"specification poisoning" "constitutional documents" "AI agents"`
- `"banking-ms-by-constitution" "tasks.md" "T001"`
- `"banking-ms-by-constitution" "CLAUDE.md" "auto-generated"`
- `"Secure by Constitution" "Constitutional Specification-Driven Development"`
- `"github/spec-kit" "Sync Impact Report" "constitution.md"`
- `"github/spec-kit" "Constitution Check" "plan-template.md"`
- `"github/spec-kit" "Constitution Authority" "analyze.md"`
- `"banking-ms-by-constitution" "No releases published" "Private - All rights reserved"`
- `"banking-ms-by-constitution" "localStorage" "JWT tokens"`
- `"Constitutional Spec-Driven Development" "16 hours" "64 hours"`
- `"Constitutional Spec-Driven Development" "quarterly compliance reviews"`
- `"constitution.md" "Compliance" "Spec-Driven Development"`
- `"constitution.md" "AGENTS.md" "Project Rules" "Cursor"`
- `"constitution.md" "traceability matrix" "PR template"`
- `"constitutional SDD" "runtime security" "threat model"`
- `"github/spec-kit" "spec-driven.md" "Constitutional Enforcement Through Templates"`
- `"github/spec-kit" "#697" "Constitution alignment" "tasks.md" "constitution.md"`
- `"github/spec-kit" "#40" "How to create a constitution"`
- `"Spec Kit" "Non-functional/Constitutional Gates" "tasks"`
- `"DocGuard" "Spec Kit" "constitution.md" "traceability"`
- `"docguard-cli" "guard" "trace" "Spec Kit"`
- `"Spec Kit Community Extensions" "DocGuard" "CDD Enforcement"`
- `"Cisco Foundry Security Spec" "constitution.md" "Spec Kit"`
- `"Foundry Security Spec" "Evidence Over Assertion" "Operator Outranks Every Agent"`
- `"Project CodeGuard" "security skills and rules" "AI coding agents"`
- `"foundry-security-spec" "NEEDS CLARIFICATION" "/speckit.clarify"`

## Кандидаты на иллюстрации

- Figure 1 from [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2602.02584v1): architecture with Constitution at the apex, specification layer, AI-assisted generation, implementation and compliance traceability. Useful for theory section on artifact hierarchy.
- Table 1 from [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2602.02584v1): compliance traceability matrix. Useful for explaining evidence surface.
- Figure 2 from [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2602.02584v1): CWE vulnerability coverage by implementation effort. Candidate only if rights and readability are acceptable.
- README diagrams from [banking-ms-by-constitution](https://github.com/srinivasraom/banking-ms-by-constitution): architecture overview, authentication flow, account management flow, transaction flow, data model and security features. Candidate for Fieldbook, because they show how the reference implementation decomposes the system. Rights caveat: README license says `Private - All rights reserved`, so direct reuse should be avoided unless permission/license is clarified.
- Figure 4 from [PAPER.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md): three-phase Constitutional Spec-Driven Development pipeline. Use cautiously as repository draft material, not as the canonical arXiv figure.
- Screenshot or reconstructed diagram of `.specify/memory/constitution.md -> spec.md -> plan.md -> tasks.md -> code -> CONSTITUTION_COMPLIANCE.md`. Better as original site diagram than reused source figure, because it can show the methodology without copying paper graphics.
- Original reconstructed diagram from [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) workflow: product spec + threat model -> `constitution.md` -> technical spec -> agent guidance -> implementation artifacts -> traceability matrix -> CI/PR gates. Лучше рисовать заново, потому что источник является практической статьёй с собственными иллюстрациями, а права на прямое переиспользование не проверялись.
- Reconstructed diagram from DocGuard/Spec Kit integration: `/speckit.specify` -> `docguard guard` -> `/speckit.plan` -> `docguard guard` -> `/speckit.tasks` -> `docguard guard` -> `/speckit.implement` -> final CI gate. Лучше рисовать заново как generic enforcement-loop, а не использовать README diagram напрямую.
- Reconstructed diagram from Foundry: `constitution.md` + seed `spec.md` -> `/speckit.clarify` -> `/speckit.specify` -> `/speckit.plan` -> `/speckit.tasks` -> `/speckit.implement` -> `/speckit.analyze`, with `[NEEDS CLARIFICATION]` markers blocked before plan and principle -> enforcing FR matrix. Лучше рисовать заново, потому что source repository является spec, а README diagram — ASCII architecture, not a site-ready image.
- Reconstructed evidence-gate diagram from Foundry: candidate -> verdict -> evidence gate with reachability/trust-boundary/impact citations -> clean-room validation for `exploited` -> published finding. Полезно для сравнения compliance evidence and security finding evidence.

## Открытые вопросы

- Repository history and issues: проход 03 сверил публичную страницу репозитория и увидел 0 issues, 0 pull requests, 0 releases and 6 commits. Если нужна эволюция artifacts, следующий проход должен смотреть commit history, а не issues.
- Сверить exact relationship между “15 principles”, “10 CWE vulnerabilities in scope” and broader raw Constitution, где CWE list is larger.
- Later arXiv versions: проход 03 сверил текущую arXiv page; submission history показывает только `v1` от 31 января 2026 года. Перед финальной публикацией это всё равно стоит перепроверить.
- Проверить, насколько `CONSTITUTION_COMPLIANCE.md` действительно auto-generated and by what tool; если tool отсутствует, matrix может быть manual report despite wording.
- Проверить client-side security coverage: как Constitution и matrix относятся к README decision хранить JWT tokens in `localStorage`; это может быть нормальным demo simplification или настоящим gap.
- Проверить права на reuse README diagrams and repository code before using them as site visuals; текущий README license says `Private - All rights reserved`.
- Перед финальной главой решить, использовать ли 73% claim in main text or only in footnote/caveat.
- Если использовать Mad Devs в финальной главе, держать его отдельно от primary evidence: это practitioner workflow и constructed illustration, не эмпирическая проверка claims Marri.
- Если использовать GitHub issues #697 and #40, явно маркировать их как public feedback / user-reported examples, а не как official Spec Kit doctrine или evidence for Marri metrics.
- Если использовать DocGuard или другие community extensions как пример enforcement tooling, отдельно проверить source code, license, release cadence, GitHub Action behavior and write permissions; официальный каталог Spec Kit не является аудитом безопасности этих расширений.
- Если использовать Foundry как соседний пример, явно держать его отдельно от CSDD Marri: Foundry is seed specification for security evaluation systems, not a banking app generation methodology and not evidence for the 73% reduction claim.
- Проверить license and contribution model of Foundry/CodeGuard before reusing fragments, diagrams or rule examples; текущий проход использовал их только как source material and did not copy assets.
- Если развивать Foundry angle дальше, прочитать `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue/release history and CodeGuard rule format; pass 08 used README/spec/constitution/CodeGuard README only.
- Отдельно сравнить CSDD с Spec Kit, Kiro, TDAD, BMAD and GSD в сравнительном документе; в этом досье comparison intentionally minimal.
