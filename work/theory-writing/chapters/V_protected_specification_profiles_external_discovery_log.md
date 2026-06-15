# External discovery log — глава V

Дата проверки: 2026-06-14.

## P04 — проверка первичных источников

### Spec Kit

Проверены первичные источники:

- https://github.github.com/spec-kit/
- https://github.github.com/spec-kit/quickstart.html
- https://github.github.com/spec-kit/reference/workflows.html
- https://github.com/github/spec-kit

Вывод: внутренний материал в целом актуален, но официальная документация стала богаче, чем атласная выжимка. Главная текущая формула остаётся `Spec → Plan → Tasks → Implement`; для production features и неоднозначной работы документация рекомендует полный путь через `/speckit.constitution`, `/speckit.specify`, `/speckit.clarify`, `/speckit.checklist`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, `/speckit.implement`. Отдельно полезны workflows with gates, pause/resume/status. Для главы это важно как материал о переходах между состояниями, но не как повод превращать текст в обзор версии Spec Kit.

Решение для главы: использовать Spec Kit как сильный пример переносимой цепочки артефактов и контрольных переходов. Текущие количественные claims о количестве интеграций, extensions, stars и релизов не включать в основной текст.

### Kiro Specs

Проверены первичные источники:

- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/specs/feature-specs/
- https://kiro.dev/docs/specs/bugfix-specs/
- https://kiro.dev/docs/specs/quick-plan/
- https://kiro.dev/docs/specs/analyze-requirements/
- https://kiro.dev/docs/specs/best-practices/

Вывод: внутренний материал подходит. Официальная документация подтверждает три ключевых файла Specs: `requirements.md` или `bugfix.md`, `design.md`, `tasks.md`; Feature Specs ведут от требований к дизайну и планированию; Bugfix Specs отдельно моделируют root cause, fix design и regression prevention; Quick Plan создаёт requirements/design/tasks за один проход; Analyze Requirements проверяет логические несогласованности, неоднозначности, конфликтующие constraints and assumptions до перехода к design.

Решение для главы: использовать Kiro как пример product-native specification state. Не переносить подробности CLI/Web/Powers/Enterprise в V, кроме одного граничного замечания: спецификация в Kiro живёт рядом с более широкой средой, но сама не равна всей среде агента.

### TDAD

Проверены первичные источники:

- https://arxiv.org/abs/2603.08806
- https://github.com/f-labs-io/tdad-paper-code
- https://arxiv.org/abs/2603.17973
- https://github.com/pepealonso95/TDAD
- https://raw.githubusercontent.com/pepealonso95/tdad-skill/main/SKILL.md

Вывод: внутреннее различение двух TDAD-линий нужно сохранить. `Test-Driven AI Agent Definition` — это про компиляцию tool-using agents из behavioral specifications через видимые/скрытые тесты, mutation testing и spec evolution. `Test-Driven Agentic Development` — это про снижение регрессий кодовых агентов через graph-based impact analysis и agent skill, который подсказывает затронутые тесты.

Решение для главы: TDAD не должен выглядеть как единый зрелый продукт или как обычный TDD. В V его надо использовать как пример test/spec carrier: поведение можно сделать исполнимым, а регрессионный риск — маршрутизируемым. Сильные численные результаты лучше оставить будущей главе о проверке.

### Constitutional SDD / соседние constitution-подходы

Проверены первичные источники:

- https://arxiv.org/abs/2602.02584
- https://github.com/srinivasraom/banking-ms-by-constitution
- https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md
- https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md
- https://github.com/CiscoDevNet/foundry-security-spec
- https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md
- https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md
- https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md

Вывод: Constitutional SDD как термин и методологическая линия пока выглядит исследовательско-демонстрационной, а не массово принятой практикой. Banking example полезен как worked example: `constitution.md` задаёт security-first правила, а compliance report связывает их с кодом. Cisco Foundry Security Spec — не тот же метод, но сильный соседний пример specification-as-deliverable: specification and constitution as blueprint/invariants/guardrails, no code in repo by design.

Решение для главы: формулировать осторожно. Писать не «так индустрия решает compliance», а «этот подход показывает, что часть спецификации можно поднять в слой правил выше локальной фичи». Cisco Foundry можно использовать только как короткое дополнительное подтверждение широкой идеи specification/constitution as deliverable, если понадобится; не смешивать его с CSDD.

## P05 — внешний поиск по подтверждённым пробелам

Поиск был ограничен подтверждёнными пробелами из P04: текущие первичные источники Spec Kit/Kiro; разделение двух TDAD-линий; статус CSDD и соседних constitution/specification-as-deliverable материалов. Широкие обзоры и SEO-сравнения не использовались как источники содержания.

### Что добавил поиск

1. **Spec Kit.** Поиск подтвердил, что главным источником остаётся официальная документация и репозиторий GitHub. Вторичные материалы вроде Microsoft Developer Blog или частных гайдов можно игнорировать: они не дают главе ничего, чего нет в первичных источниках.

2. **Kiro.** Поиск подтвердил, что документация Kiro прямо формулирует Specs как structured artifacts for features and bug fixes и отдельно выделяет Feature Specs, Quick Plan, Analyze Requirements, Bugfix Specs and Best Practices. Это достаточно для главы; вторичные посты Kiro/dev.to можно не использовать.

3. **TDAD.** Поиск подтвердил два разных источника: arXiv 2603.08806 про Test-Driven AI Agent Definition и arXiv 2603.17973 про Test-Driven Agentic Development. Появились сторонние порты/репозитории, но они не нужны для главы: достаточно primary papers + official repos.

4. **CSDD.** Поиск не нашёл сильной независимой практики, которая превратила бы Constitutional SDD в зрелый отраслевой стандарт. Основной источник остаётся arXiv paper and banking worked example. ResearchGate/LinkedIn/YouTube-дубли не использовать. Cisco Foundry Security Spec остаётся adjacent optional source, не CSDD.

### Отклонённые источники

- YouTube-гайды по Spec Kit/Kiro/CSDD: не нужны для теоретической главы.
- SEO-сравнения и vendor-vs-vendor страницы: могут исказить тон главы и не являются первичными источниками.
- ResearchGate mirror of CSDD: дублирует arXiv, не добавляет содержания.
- Dev.to/Promptz материалы по Kiro: подтверждают общеизвестные пункты, но официальная документация лучше.
- Сторонние TDAD-порты: интересны для future tool note, но не нужны для аргумента V.

## P06 — решение по участию источников

После чтения и сравнения источников для главы выбраны четыре рабочих подхода.

### 1. Spec Kit

Использовать как подход переносимой цепочки артефактов. В текст попадёт не каталог команд, а смысл цепочки: намерение фичи нельзя сразу отправить в код; его нужно провести через спецификацию, уточнение, план, задачи, анализ и реализацию. Главный вклад источников Spec Kit — показать защищённые переходы между состояниями.

Не переносить: количественные claims, changelog/release details, длинные списки интеграций.

### 2. Kiro Specs

Использовать как подход specification state inside the development environment. В главу попадёт `requirements.md` / `bugfix.md`, `design.md`, `tasks.md`, Feature Specs, Bugfix Specs, Quick Plan and Analyze Requirements. Главная разница с Spec Kit: Kiro важен не только как цепочка, а как состояние продуктовой задачи внутри среды.

Не переносить: общий обзор Kiro as IDE, hooks/MCP/Powers/Web details, enterprise/product-surface tour.

### 3. TDAD

Использовать как test-as-specification approach. Сохранить две линии: agent definition through behavioral tests and code-agent regression route through impact analysis. В главу попадёт только то, что показывает: тест может быть не постфактум-проверкой, а исполнимым носителем требования.

Не переносить: детальные численные результаты, спор о benchmark/evidence, широкий TDD background.

### 4. Constitutional SDD

Использовать как approach of rules above a feature. В главу попадёт constitution as constraints, trace/compliance mapping, human checkpoints, security-first worked example. Статус формулировать осторожно: proposed/research/demo line, not industry standard.

Не переносить: утверждение о зрелой adoption, автоматическое доказательство security/compliance, смешение с Foundry.

### Optional adjacent source

Cisco Foundry Security Spec оставить optional. Он может дать одну фразу о broader specification/constitution-as-deliverable trend, но не должен становиться частью подхода CSDD.

## Практическое правило для черновика

Основной текст должен двигаться не от источника к источнику, а от общего вопроса к подходу: что именно этот подход делает устойчивым в жизненном цикле изменения. Источник вводится только там, где помогает ответить на этот вопрос.

## P14 — интеграция ссылок в основной текст

Ссылки проверены по месту переноса. Дополнительно в текст внесена official Spec Kit workflows page, потому что она поддерживает не продуктовую деталь, а центральный тезис главы: подход Spec Kit держит переходы между шагами и может переживать не один ответ агента.

Kiro, TDAD and CSDD sources оставлены без расширения: текущих primary sources достаточно, вторичные источники не вводятся.

## P15 — после русской переписи

Абзац про Spec Kit workflows переписан как часть аргумента о переходах между шагами. Новые внешние источники не добавлялись.

## P17 — внешние источники

Новые внешние источники не добавлялись. Доработка была концептуальной: усилена ось человеческого решения на основе уже встроенных материалов.

## P23 — final external discovery status

No new external search was required after P14. Primary sources remain sufficient. Secondary sources remain excluded. Current product claims are intentionally limited to stable documentation-level statements.
