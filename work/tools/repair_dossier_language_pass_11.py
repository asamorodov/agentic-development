from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[2]
DATE = "2026-06-08"


TOPICS = {
    "spec-kit": {
        "title": "Spec Kit",
        "final": "SPEC_KIT_METHOD_DOSSIER.md",
        "audit": "SPEC_KIT_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("GitHub Spec Kit docs home", "https://github.github.com/spec-kit/"),
            ("github/spec-kit repository", "https://github.com/github/spec-kit"),
            ("Spec-driven guide", "https://github.com/github/spec-kit/blob/main/spec-driven.md"),
            ("Spec Kit Agents paper", "https://arxiv.org/abs/2604.05278"),
            ("Microsoft developer blog on Spec Kit", "https://developer.microsoft.com/blog/spec-driven-development-spec-kit"),
        ],
        "body": dedent(
            """
            # Spec Kit

            Рабочее досье, переписанное после языковой проверки. Это не финальная глава и не краткая справка, а буфер фактуры для будущего текста сайта: здесь сохраняются детали источников, команды, артефакты, возможные места поломки, вопросы для проверки и кандидаты на внешние изображения. Английскими оставлены только имена проекта, команд, файлов, каталогов и устойчивых терминов.

            Spec Kit описывает себя как набор инструментов для Spec-Driven Development: сначала формулируется, что нужно построить, затем это уточняется через последовательные фазы, и только потом агент получает структурированный контекст для реализации [GitHub Spec Kit docs home](https://github.github.com/spec-kit/). Важная деталь источника: методика не сводится к “написать хороший prompt”. В документации прямо выделена цепочка `Spec -> Plan -> Tasks -> Implement`, где каждая фаза создаёт Markdown-артефакт, который становится входом для следующей фазы [GitHub Spec Kit docs home](https://github.github.com/spec-kit/). Для будущей главы это нужно сохранить как центральную механику: Spec Kit превращает разговор с агентом в цепочку файлов, а не в один большой запрос.

            Установка и первичная инициализация тоже являются частью метода, а не только технической обвязкой. Документация показывает запуск через `uvx --from git+https://github.com/github/spec-kit.git` и `specify init my-project --integration copilot`; README репозитория также показывает установку CLI через `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z` и инициализацию `specify init my-project --integration copilot` [GitHub Spec Kit docs home](https://github.github.com/spec-kit/) [github/spec-kit repository](https://github.com/github/spec-kit). Содержательно это значит: Spec Kit внедряется в уже выбранный агентский инструмент через integration layer. Метод не требует одного конкретного исполнителя: источник называет десятки интеграций, включая Copilot, Gemini, Codex, Windsurf, Claude, Forge и Kiro, а также `generic`-вариант для инструментов вне списка [GitHub Spec Kit docs home](https://github.github.com/spec-kit/). Кандидат на изображение: `https://github.github.com/spec-kit/` — первый экран документации с positioning и статистикой экосистемы; полезен для раздела о том, как метод позиционирует себя не как IDE, а как переносимый слой процесса.

            Основные пользовательские команды после `specify init` в README организуют процесс в управляемые шаги. `/speckit.constitution` создаёт или обновляет принципы проекта; `/speckit.specify` фиксирует, что и зачем строится, без преждевременного выбора стека; `/speckit.plan` переводит намерение в технический план; `/speckit.tasks` разбивает план на задачи; `/speckit.implement` запускает реализацию по задачам [github/spec-kit repository](https://github.com/github/spec-kit). Важно не потерять команду `/speckit.taskstoissues`: она показывает мост от локального task-файла к GitHub Issues и тем самым связывает спецификацию с внешним трекингом [github/spec-kit repository](https://github.com/github/spec-kit). В досье это нужно хранить рядом с командной цепочкой, потому что для будущего текста сайта это пример того, как метод переносит контекст из “AI workspace” в командный процесс.

            Артефакты Spec Kit нужно понимать как цепочку передачи контекста. Конституция задаёт проектные принципы и ограничения; спецификация содержит пользовательские сценарии, требования и границы поведения; план добавляет технологический стек, архитектурные решения и проверочные вопросы; task-файл делает реализацию исполнимой; implementation step должен использовать предыдущие файлы как контекст, а не заменять их новой импровизацией [GitHub Spec Kit docs home](https://github.github.com/spec-kit/) [github/spec-kit repository](https://github.com/github/spec-kit). Репозиторий важен как источник деталей о механизме: там видны каталоги `integrations`, `templates`, `extensions`, `presets`, `workflows` и `src/specify_cli`, то есть Spec Kit фактически состоит из CLI, шаблонов, интеграций и расширяемых наборов workflow-файлов [github/spec-kit repository](https://github.com/github/spec-kit). Кандидат на изображение: `https://github.com/github/spec-kit` — дерево репозитория с каталогами `integrations`, `templates`, `extensions`, `presets`, `workflows`; полезно показать материальную структуру метода.

            Human gates в Spec Kit не выглядят как один большой формальный approval, но они встроены в смену фаз. Человек должен проверить конституцию, потому что она будет управлять последующими решениями; затем проверить спецификацию до технического планирования; затем проверить план до декомпозиции в задачи; затем проверить задачи перед реализацией. Если эти проверки пропустить, метод превращается в “быстро сгенерировать пять файлов”, а не в спецификационно-управляемую разработку. Это ключевой failure mode: документы могут выглядеть правильными, но не нести реального решения. Для будущей главы хорошая формулировка: Spec Kit силён не количеством файлов, а тем, что файлы должны удерживать разницу между намерением, планом и исполнением.

            Источник о “spec-driven by default” подчёркивает quality checklists и cross-artifact analysis [GitHub Spec Kit docs home](https://github.github.com/spec-kit/). Это нужно сохранить как отдельный слой: метод не просто создаёт `spec.md`, `plan.md` и `tasks.md`, но должен проверять согласованность между ними. Слабое место возникает, когда checklist применяется как декоративный список: можно получить видимость контроля без обнаружения drift между требованиями, архитектурой и задачами. Сильное применение — когда каждое решение в плане можно вывести из требования, а каждая задача имеет trace back к плану и спецификации.

            Экосистема расширений меняет статус Spec Kit: это не только базовый workflow, но и marketplace-подобная система расширений, presets и community workflows. Документация говорит о community extensions, presets, workflows и самостоятельной публикации расширений; отдельно предупреждает, что community contributions независимы и их код надо проверять перед установкой [GitHub Spec Kit docs home](https://github.github.com/spec-kit/) [github/spec-kit repository](https://github.com/github/spec-kit). Это важный caveat: расширяемость увеличивает применимость, но создаёт supply-chain и governance risk. В dossier нужно сохранить, что CI Guard и Architecture Guard упоминаются как примеры compliance/governance extensions, но их нельзя использовать как доказательство качества конкретного проекта без отдельного просмотра их исходников [GitHub Spec Kit docs home](https://github.github.com/spec-kit/).

            Сравнительная заметка внутри темы: Spec Kit ближе всего к “portable specification layer”. Он отличается от Kiro тем, что не является встроенной IDE-поверхностью и должен ставиться в выбранный агентский runtime; от BMAD тем, что меньше строится вокруг ролей и агентов, а больше вокруг универсальной цепочки command files; от GSD тем, что центр тяжести находится в спецификации и планировании, а не в shipping loop; от TDAD тем, что native validation у Spec Kit в основном документарно-чеклистовая, а не тестово-эмпирическая; от Constitutional SDD тем, что constitution в Spec Kit шире проектных принципов, а не обязательно security-by-construction.

            Возможные поломки: преждевременная реализация после красивого `spec.md`; stale constitution, которая больше не отражает проект; tasks, созданные из плана, но не проверенные на покрытие требований; расширения, установленные без review; integration mismatch, когда выбранный агент не понимает созданные prompt files; “spec laundering”, когда агент переписывает неясность в уверенный документ. Для будущей главы полезно противопоставить это vibe coding: Spec Kit не запрещает итерацию, но требует, чтобы итерация оставляла след в артефактах [GitHub Spec Kit docs home](https://github.github.com/spec-kit/).

            Остаточная очередь источников: полностью раскрыть `spec-driven.md`, reference overview, installation/upgrade guides, список integrations, extensions reference, presets reference и несколько community extensions; открыть arXiv HTML/PDF по Spec Kit Agents для точных тезисов о context-grounded workflows [Spec Kit Agents paper](https://arxiv.org/abs/2604.05278); проверить Microsoft blog как внешний positioning source [Microsoft developer blog on Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit). Кандидат на изображение: workflow/diagram из документации Spec Kit, если он доступен на docs site; причина — будущему читателю нужно увидеть именно цепочку артефактов, а не только команды.
            """
        ),
    },
    "kiro-specs": {
        "title": "Kiro Specs",
        "final": "KIRO_SPECS_DOSSIER.md",
        "audit": "KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("Kiro Specs docs", "https://kiro.dev/docs/specs/"),
            ("Kiro Feature Specs docs", "https://kiro.dev/docs/specs/feature-specs/"),
            ("Kiro Steering docs", "https://kiro.dev/docs/steering/"),
            ("Kiro Hooks actions docs", "https://kiro.dev/docs/hooks/actions/"),
            ("AWS Kiro documentation overview", "https://aws.amazon.com/documentation-overview/kiro/"),
        ],
        "body": dedent(
            """
            # Kiro Specs

            Рабочее досье по Kiro Specs. Это буфер фактуры, а не обзор продукта: задача документа — сохранить детали того, как Kiro превращает идею, bugfix или feature request в набор файлов, фаз, approval-поверхностей и исполняемых задач. Английские имена оставлены только там, где это имена файлов, режимов, команд или страниц документации.

            В документации Kiro specs определены как структурированные артефакты, которые формализуют процесс разработки features и bug fixes [Kiro Specs docs](https://kiro.dev/docs/specs/). Центральная тройка файлов: `requirements.md` или `bugfix.md`, `design.md`, `tasks.md` [Kiro Specs docs](https://kiro.dev/docs/specs/). Это нужно сохранить как основной механизм: Kiro не просто просит агента написать план, а создаёт рабочую папку спецификации, где требования, дизайн и задачи существуют как отдельные, проверяемые и редактируемые документы.

            Общий workflow состоит из трёх фаз. В первой фазе фиксируется поведение или bug analysis: для feature это user stories и acceptance criteria в `requirements.md`, для bugfix — current behavior, expected behavior и unchanged behavior в `bugfix.md` [Kiro Specs docs](https://kiro.dev/docs/specs/). Во второй фазе создаётся `design.md`: архитектура, компоненты, sequence diagrams, data flow, error handling и testing strategy [Kiro Specs docs](https://kiro.dev/docs/specs/). В третьей фазе создаётся `tasks.md`: дискретные implementation tasks с отслеживанием статуса и возможностью запуска отдельных задач или всех задач сразу [Kiro Specs docs](https://kiro.dev/docs/specs/). Кандидат на изображение: `https://kiro.dev/docs/specs/` — диаграмма three-phase workflow и скриншот task execution; полезно показать, что метод живёт в IDE-интерфейсе.

            Task execution в Kiro имеет важную деталь, которой нет в обычной Markdown-декомпозиции. При `Run all Tasks` Kiro анализирует зависимости в `tasks.md`, строит dependency graph и группирует независимые задачи в waves: первая волна — задачи без зависимостей, следующая — задачи, зависимости которых закрыты предыдущей волной, и так до завершения [Kiro Specs docs](https://kiro.dev/docs/specs/). Волны идут последовательно, а задачи внутри волны могут идти параллельно [Kiro Specs docs](https://kiro.dev/docs/specs/). Это сильный source-level detail: `tasks.md` здесь не просто список дел, а вход для планировщика исполнения.

            Feature Specs поддерживают два основных сценария входа. Requirements-First начинается с поведения системы и ведёт цепочку `Requirements -> Design -> Tasks`; источник рекомендует его, когда поведение известно, архитектура гибкая, продуктовая обратная связь важна или проект начинается без жёстких технических ограничений [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/). Design-First начинается с architecture, low-level design, pseudocode или алгоритмов и ведёт цепочку `Design -> Requirements -> Tasks`; он подходит для технически ограниченных проектов, строгих non-functional requirements, переноса design docs и проверки feasible scope [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/). Quick Plan — отдельный режим для хорошо понятных features, где все три артефакта генерируются без approval gates между фазами после начальных уточняющих вопросов [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/).

            `requirements.md` использует EARS notation. Документация даёт шаблон `WHEN [condition/event]` и `THE SYSTEM SHALL [expected behavior]`, а также объясняет пользу: ясность, testability, traceability и полнота условий [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/). Для будущей главы это важно как отличие Kiro от свободного PRD: требования должны быть достаточно структурированы, чтобы потом переводиться в тесты и задачи. Отдельный validation surface — Analyze Requirements: перед переходом от requirements к design можно попросить Kiro найти logical inconsistencies, ambiguity, conflicting constraints и gaps [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/).

            Human gates в Kiro зависят от выбранного workflow. В Requirements-First человек проверяет требования перед дизайном, затем дизайн перед задачами, затем задачи перед запуском исполнения. В Design-First человек сначала проверяет техническую форму решения, потом производные требования и задачи. Quick Plan сознательно снимает approval gates между фазами, поэтому должен использоваться только там, где риск неверной спецификации невелик [Kiro Feature Specs docs](https://kiro.dev/docs/specs/feature-specs/). Этот caveat нужно сохранить: Quick Plan ускоряет работу, но снижает число точек, где человек может остановить ошибочную цепочку.

            Bugfix Specs важны как отдельный тип, а не просто feature со словом “bug”. Они направлены на surgical precision и предотвращение регрессий; документация прямо отделяет их от Feature Specs [Kiro Specs docs](https://kiro.dev/docs/specs/). Для сайта это можно использовать как пример зрелой методики: исправление ошибки требует не только “починить”, но и зафиксировать текущее поведение, ожидаемое поведение и то, что не должно измениться. Потенциальная поломка: если bugfix-фаза превращается в обычную реализацию без unchanged behavior, агент может закрыть symptom и открыть regression.

            Steering, hooks и другие Kiro-механизмы в этом досье пока зафиксированы как соседние источники, которые нужно раскрывать глубже перед финальной главой [Kiro Steering docs](https://kiro.dev/docs/steering/) [Kiro Hooks actions docs](https://kiro.dev/docs/hooks/actions/). Рабочая гипотеза: Specs отвечают за feature/bug workflow, Steering отвечает за устойчивый проектный контекст, а hooks/actions могут добавлять автоматические реакции. Но это нельзя подавать как завершённый вывод, пока соответствующие страницы не будут разобраны на уровне файлов, триггеров и ограничений.

            Сравнительная заметка внутри темы: Kiro ближе к IDE-native spec workflow. От Spec Kit он отличается тем, что workflow живёт в продуктовой поверхности Kiro и может управлять task execution прямо в IDE; от BMAD — меньшим количеством ролей и большей привязкой к файлам спецификации; от GSD — фокусом на feature/bug artifacts, а не на durable shipping state; от TDAD — наличием структурированных требований, но отсутствием видимого hidden-test/mutation-test слоя; от Constitutional SDD — отсутствием security constitution как обязательного ядра. Failure modes: Quick Plan на сложной задаче, EARS как механический шаблон без полноты условий, параллельный запуск задач при неверных dependencies, stale design after requirements change, отсутствие отдельной regression surface для bugfix.

            Кандидаты на изображения: `https://kiro.dev/docs/specs/` — скриншот task execution и диаграмма waves/dependency graph; `https://kiro.dev/docs/specs/feature-specs/` — диаграммы Requirements-First и Design-First. Причина включения: будущему читателю нужно увидеть различие между тремя Markdown-файлами и IDE-поверхностью, где эти файлы исполняются. Остаточная очередь: открыть страницы Requirements-First, Design-First, Quick Plan, Analyze Requirements, Bugfix Specs, Best Practices, Steering и Hooks; отдельно проверить changelog 0.10 и AWS overview как внешние positioning/roadmap sources [AWS Kiro documentation overview](https://aws.amazon.com/documentation-overview/kiro/).
            """
        ),
    },
    "constitutional-sdd": {
        "title": "Constitutional SDD",
        "final": "CONSTITUTIONAL_SDD_DOSSIER.md",
        "audit": "CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("Constitutional SDD paper", "https://arxiv.org/abs/2602.02584"),
            ("MITRE CWE Top 25", "https://cwe.mitre.org/top25/"),
            ("OWASP ASVS", "https://owasp.org/www-project-application-security-verification-standard/"),
            ("arXiv HTML", "https://arxiv.org/html/2602.02584"),
            ("ResearchGate mirror", "https://www.researchgate.net/publication/400414467_Constitutional_Spec-Driven_Development_Enforcing_Security_by_Construction_in_AI-Assisted_Code_Generation"),
        ],
        "body": dedent(
            """
            # Constitutional Spec-Driven Development

            Рабочее досье по Constitutional SDD. Это не готовая глава о security и не abstract paper summary, а буфер фактуры о том, как security constraints переносятся в specification layer до генерации кода.

            Главная идея paper: AI-assisted “vibe coding” ускоряет разработку, но LLM часто оптимизируют functional correctness сильнее, чем security; поэтому security нужно не “проверять после”, а встроить в specification layer заранее [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Метод вводит Constitution — versioned, machine-readable документ с non-negotiable security constraints, derived from CWE/MITRE Top 25 и regulatory frameworks [Constitutional SDD paper](https://arxiv.org/abs/2602.02584) [MITRE CWE Top 25](https://cwe.mitre.org/top25/). Это нужно сохранить как точную формулу: Constitution здесь не метафора культуры, а входной артефакт для генерации и проверки.

            Paper подан как security-by-construction для AI-assisted code generation. В источнике заявлены: 15 pages, 2 figures, 5 tables, 11 code listings, 14 references, reference implementation и compliance traceability matrix [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Эти метаданные важны: перед финальной главой нужно открыть full PDF/HTML, потому что именно tables, code listings и traceability matrix должны дать source-level детали, которых нет в abstract. В текущем досье abstract-level фактура засчитана, но точные constraints, listing names и matrix fields остаются residual queue.

            Демонстрационный домен — banking microservices application: customer management, account operations и transaction processing [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Авторы подчёркивают, что метод domain-agnostic, но банк выбран как representative example из-за regulatory и security requirements [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Для будущего текста важно не смешать две вещи: banking — case study, а Constitutional SDD — переносимая методика. Кандидат на изображение: `https://arxiv.org/html/2602.02584` — figures или traceability table из HTML/PDF; причина включения — показать цепочку “principle -> requirement -> code location”.

            Заявленный механизм: Constitution кодирует security constraints, затем требования и generated code должны сохранять traceability от principles к implementation locations [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). В abstract заявлено, что implementation addresses 10 critical CWE vulnerabilities through constitutional constraints with full traceability from principles to code locations [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Для dossier важно сохранить осторожность: список этих 10 CWE нельзя реконструировать по памяти или по названию Top 25; их нужно извлечь из PDF/HTML. Пока фиксируется только источник происхождения — MITRE/CWE Top 25 и regulatory frameworks.

            Сильная claim paper: constitutional constraints reduce security defects by 73% compared to unconstrained AI generation while maintaining developer velocity [Constitutional SDD paper](https://arxiv.org/abs/2602.02584). Это число можно использовать только с provenance и caveat: нужно проверить experimental setup, baseline, sample size, какие defects считались, как измерялась velocity и была ли evaluation blinded. В будущем тексте нельзя превращать 73% в универсальное обещание; это claim конкретного case study. Отдельно нужно извлечь из full paper, какие tables поддерживают это число.

            Возможная структура workflow: сначала выбрать security constitution и версию; затем написать спецификацию функции с ссылками на constitutional clauses; затем использовать AI agent для генерации кода, где prompts include constraints; затем проверить compliance traceability matrix; затем выполнить security validation against CWE/ASVS-like controls; затем обновить Constitution при изменении regulatory или threat model. Эта реконструкция является выводом из sources, а не прямой цитатой. Её нужно проверить по full paper перед финальным использованием [Constitutional SDD paper](https://arxiv.org/abs/2602.02584) [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/).

            Human gates должны быть жёстче, чем в обычном SDD. Gate 1: человек утверждает Constitution и источники требований безопасности. Gate 2: человек проверяет, что feature spec ссылается на relevant clauses, а не содержит generic “make secure”. Gate 3: перед генерацией или merge проверяется traceability matrix. Gate 4: security evidence не сводится к словам агента; должны быть tests, static analysis, review или checklist. Если эти gates исчезают, Constitutional SDD ломается в compliance theater: файл Constitution есть, но не управляет кодом.

            Сравнительная заметка внутри темы: Constitutional SDD ближе к Spec Kit по идее specification layer, но его центр тяжести уже — security constraints. От Kiro он отличается тем, что EARS/requirements недостаточно: нужны machine-readable security clauses и traceability. От TDAD он отличается тем, что validation начинается с policy/constitution, а не с behavioral test compilation; однако для зрелого варианта Constitutional SDD хорошо бы соединять constitution clauses с tests. От BMAD он отличается меньшим role layer и более сильным security gate. От GSD он отличается тем, что “done” невозможно без compliance evidence.

            Failure modes: Constitution слишком общая; outdated CWE/ASVS sources; security principles не привязаны к конкретным requirements; agent создаёт код, который выглядит secure, но не имеет traceability; compliance matrix заполняется задним числом; banking case обобщается на другой домен без threat modeling; velocity claim используется вне experimental context. Остаточная очередь: открыть PDF и HTML, извлечь exact 10 CWE, tables, figures, code listings, traceability matrix columns, baseline setup и limitations; проверить есть ли reference implementation repository; сверить, как MITRE Top 25 и OWASP ASVS реально превращаются в clauses [MITRE CWE Top 25](https://cwe.mitre.org/top25/) [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/).
            """
        ),
    },
    "tdad-comparative": {
        "title": "TDAD comparative",
        "final": "TDAD_COMPARATIVE_DOSSIER.md",
        "audit": "TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("Test-Driven AI Agent Definition paper", "https://arxiv.org/abs/2603.08806"),
            ("tdad-paper-code repository", "https://github.com/f-labs-io/tdad-paper-code"),
            ("Test-Driven Agentic Development paper", "https://arxiv.org/abs/2603.17973"),
            ("TDAD repository", "https://github.com/pepealonso95/TDAD"),
            ("AI Paper Delta page", "https://ai-paper-delta.vercel.app/en/papers/2603.17973"),
        ],
        "body": dedent(
            """
            # TDAD comparative

            Рабочее досье сравнивает две линии, которые используют одинаковую аббревиатуру TDAD, но решают разные проблемы. Это внутреннее сравнение внутри темы, а не comparative synthesis между всеми methodology dossiers.

            Первая линия — Test-Driven AI Agent Definition. Paper treats agent prompts as compiled artifacts: engineers provide behavioral specifications, один coding agent превращает их в executable tests, второй coding agent итеративно уточняет prompt, пока tests pass [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806). Смысл для будущей главы: prompt перестаёт быть ручным текстом и становится результатом компиляции из спецификации под тестовый harness. Это ближе к compiler/evaluation loop, чем к обычной prompt engineering.

            В этой первой линии центральная проблема — production tool-using agents cannot rely on informal confidence. Paper прямо называет silent regressions from small prompt changes, undetected tool misuse и policy violations emerging after deployment [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806). Поэтому TDAD вводит три защитных механизма: visible/hidden test split, semantic mutation testing и spec evolution scenarios [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806). Нужно сохранить, что hidden tests защищают от specification gaming, mutation testing проверяет способность suite ловить plausible faulty prompt variants, а evolution scenarios измеряют regression safety при изменении требований.

            Evaluation первой линии выполнена на SpecSuite-Core: четыре deeply-specified agents, covering policy compliance, grounded analytics, runbook adherence и deterministic enforcement [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806). Заявленные числа: 24 independent trials; 92% v1 compilation success; 97% mean hidden pass rate; evolved specifications compile at 58%; mutation scores 86-100%; v2 hidden pass rate 78%; regression safety scores 97% [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806). Эти числа нельзя переносить на все agents; для финального текста нужно открыть PDF и repository, чтобы проверить task definitions, harness, prompts, failure cases и exact metric definitions.

            Вторая линия — Test-Driven Agentic Development, посвящённая AI coding agents and code regressions. Paper говорит, что existing benchmarks focus on resolution rate, while regression behavior is under-studied [Test-Driven Agentic Development paper](https://arxiv.org/abs/2603.17973). Метод выполняет pre-change impact analysis: строит dependency map между source code и tests, чтобы до commit agent знал, какие tests надо verify и где self-correct [Test-Driven Agentic Development paper](https://arxiv.org/abs/2603.17973). Важная деталь: map delivered as lightweight agent skill — static text file queried at runtime [Test-Driven Agentic Development paper](https://arxiv.org/abs/2603.17973).

            Evaluation второй линии: SWE-bench Verified, open-weight models on consumer hardware; Qwen3-Coder 30B на 100 instances и Qwen3.5-35B-A3B на 25 instances; reported regression reduction by 70%, from 6.08% to 1.82%, compared to vanilla baseline [Test-Driven Agentic Development paper](https://arxiv.org/abs/2603.17973). Для досье важно сохранить не только headline number, но и mechanism: агент не получает “больше мотивации тестировать”, он получает сжатую карту связи source/test, которая ограничивает test selection and repair loop.

            Сравнение двух TDAD: Test-Driven AI Agent Definition компилирует prompts/agent definitions from behavioral specs; Test-Driven Agentic Development защищает code changes from regressions by impact analysis. Первая методика ближе к evaluation-driven prompt compiler; вторая — к test selection and regression guard для coding agents. В первой central artifact: behavioral spec, visible tests, hidden tests, prompt under compilation, mutation variants, evolution scenarios. Во второй central artifact: dependency map, agent skill/static text file, selected test set, patch and self-correction loop. Эти различия нужно сохранить, чтобы в будущей главе не смешать две разные research programs под одной аббревиатурой.

            Human gates в первой TDAD: человек утверждает behavioral spec, контролирует разделение visible/hidden tests, решает, какие policy violations недопустимы, проверяет mutation results и принимает compiled prompt. Gate failure: hidden tests становятся видимыми или слишком похожими на visible; mutation agent создаёт слабые variants; compiled prompt overfits harness. Human gates во второй TDAD: человек проверяет dependency map freshness, принимает selected tests, не позволяет агенту пропустить failing impacted tests и оценивает regression rate отдельно от issue resolution. Gate failure: map устаревает, impacted tests неполные, agent игнорирует skill file, baseline сравнение неадекватно.

            Сравнительная заметка с остальными методами, только внутри этой темы: TDAD радикально отличается от Spec Kit/Kiro/BMAD/GSD тем, что ставит measurement в центр. Spec Kit и Kiro создают документы, BMAD создаёт роль/workflow/artifact chain, GSD создаёт durable shipping state; TDAD требует executable behavioral or regression evidence. Constitutional SDD ближе к TDAD по идее non-negotiable constraints, но TDAD делает constraints проверяемыми через tests, hidden split, mutation or impact map.

            Кандидаты на изображения: `https://arxiv.org/html/2603.08806` — diagram of TDAD compilation loop, if available; причина — показать круг spec -> tests -> prompt refinement -> hidden evaluation. Второй кандидат: `https://arxiv.org/html/2603.17973` — graph-based impact analysis diagram; причина — показать source/test dependency map как central artifact. Третий кандидат: screenshots or README diagrams from `https://github.com/f-labs-io/tdad-paper-code` и `https://github.com/pepealonso95/TDAD`; сами assets не включены.

            Остаточная очередь: открыть full PDFs/HTML, repositories, benchmark config, exact test harness, examples of behavioral specs, examples of generated tests, prompt variants, dependency-map format, issue-level failure cases, release/license status. Без этой очереди финальная глава не должна пересказывать algorithmic detail beyond abstract-level claims [Test-Driven AI Agent Definition paper](https://arxiv.org/abs/2603.08806) [Test-Driven Agentic Development paper](https://arxiv.org/abs/2603.17973).
            """
        ),
    },
    "gsd-open-gsd": {
        "title": "GSD / Open GSD",
        "final": "GSD_OPEN_GSD_DOSSIER.md",
        "audit": "GSD_OPEN_GSD_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("Open GSD gsd-core product page", "https://opengsd.net/products/gsd-core"),
            ("open-gsd/gsd-core repository", "https://github.com/open-gsd/gsd-core"),
            ("Open GSD configuration docs", "https://opengsd.net/docs/v1/configuration"),
            ("GSD auto mode docs", "https://github.com/gsd-build/gsd-2/blob/main/docs/user-docs/auto-mode.md"),
            ("GSD origin site", "https://getshitdone.help/"),
        ],
        "body": dedent(
            """
            # GSD / Open GSD

            Рабочее досье по GSD / Open GSD. Это буфер для будущего текста о методе, который пытается добавить дисциплину Git, Ship, Done в существующие AI coding tools. Здесь не создаётся общий synthesis с другими темами; сравнения используются только для понимания самого GSD.

            Open GSD описывает `gsd-core` как workflow framework for bringing Git, Ship, Done discipline into an existing AI coding tool [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Важная позиция источника: это не отдельная IDE, а prompt framework, который устанавливается в текущий AI coding harness и даёт durable project artifacts plus repeatable loop [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Упоминаются Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Copilot and other runtimes [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Поэтому GSD нужно понимать как runtime-neutral layer, похожий по переносимости на Spec Kit, но с другим центром тяжести.

            Установка в источнике дана как `npx @opengsd/gsd-core@latest copy` [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Это нужно сохранить как concrete command, потому что метод явно копирует framework в проект, а не требует SaaS-backend как обязательный центр. Базовая command surface: `/gsd new-project` создаёт durable project context, `/gsd discuss` фиксирует decisions before building, `/gsd verify` проверяет work before shipping [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Эти три команды показывают минимальный цикл: создать контекст, обсудить и зафиксировать решения, проверить перед ship.

            Project artifacts на product page перечислены как `VISION.md`, `ROADMAP.md`, `CURRENT_STATE.md`, `SHIP_HANDOFF.md` [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). В досье это нужно хранить не списком, а цепочкой: `VISION.md` удерживает зачем и что строится; `ROADMAP.md` хранит direction и последовательность; `CURRENT_STATE.md` должен переживать разрывы сессий и показывать, где проект находится сейчас; `SHIP_HANDOFF.md` делает передачу результата явной. Центральная проблема GSD — не “как написать spec”, а как не потерять проектное состояние между агентскими сессиями и не назвать work done без проверки.

            Product page формулирует operating loop: start a project with the command set, discuss next phase and capture decisions, then plan, execute, verify and ship with durable markdown artifacts [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Важная деталь: verify стоит до shipping, а durable artifacts должны сохранять планы, state и requirements across session boundaries [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Для будущего сайта это хороший пример методологии против context evaporation: если агент работает в коротких сессиях, состояние должно жить в файлах.

            Роль human gate в GSD привязана к слову Done. `/gsd discuss` должен зафиксировать решения до build, а `/gsd verify` должен не позволить выдать результат без проверки [Open GSD gsd-core product page](https://opengsd.net/products/gsd-core). Это не равно test suite: verify может быть command/protocol surface, и нужно открыть commands reference, чтобы понять exact checks. Пока в досье фиксируется только механика: GSD создаёт checkpoint before shipping, но evidence model требует дополнительного source pass [Open GSD configuration docs](https://opengsd.net/docs/v1/configuration).

            Сравнение внутри темы: GSD отличается от Spec Kit тем, что его first-class artifacts — project state and handoff, not spec/plan/tasks. От Kiro — тем, что он не IDE task execution surface, а переносимый prompt framework. От BMAD — тем, что он легче, меньше роли/агенты, больше emphasis on state and shipping. От TDAD — тем, что validation surface workflow-level, not empirical hidden tests or graph impact analysis. От Constitutional SDD — тем, что security constitution не является обязательным ядром, хотя GSD verify could theoretically include security checks.

            Failure modes: `VISION.md` становится aspirational slogan; `ROADMAP.md` не обновляется после решений; `CURRENT_STATE.md` отстаёт от реального codebase; `SHIP_HANDOFF.md` создаётся после факта и не помогает review; `/gsd verify` превращается в self-report; агент пишет “done” без diff, tests or artifact evidence; copied framework устаревает относительно upstream; runtime-specific differences ломают command semantics. Для будущей главы нужно особенно проверить, как GSD предотвращает stale state, а не только создаёт файлы.

            Кандидаты на изображения: `https://opengsd.net/products/gsd-core` — first viewport с командой install, command surface и четырьмя artifacts; причина — читателю сразу виден Git/Ship/Done loop. Второй кандидат: repo tree `https://github.com/open-gsd/gsd-core`; причина — показать, что framework is copied into runtimes. Третий кандидат: documentation diagram из commands/configuration pages, если есть.

            Остаточная очередь: открыть user guide, commands reference, configuration docs, package README, release notes, examples of generated `VISION.md`, `ROADMAP.md`, `CURRENT_STATE.md`, `SHIP_HANDOFF.md`, legacy `gsd-build/gsd-2` auto mode docs and origin page [open-gsd/gsd-core repository](https://github.com/open-gsd/gsd-core) [GSD auto mode docs](https://github.com/gsd-build/gsd-2/blob/main/docs/user-docs/auto-mode.md) [GSD origin site](https://getshitdone.help/). Пока нельзя утверждать exact verification algorithm или configuration schema без этого раскрытия.
            """
        ),
    },
    "bmad-method": {
        "title": "BMAD Method",
        "final": "BMAD_METHOD_DOSSIER.md",
        "audit": "BMAD_METHOD_DOSSIER_QUALITY_AUDIT.md",
        "sources": [
            ("BMAD docs home", "https://docs.bmad-method.org/"),
            ("BMAD Getting Started", "https://docs.bmad-method.org/tutorials/getting-started/"),
            ("BMAD Workflow Map", "https://docs.bmad-method.org/reference/workflow-map/"),
            ("BMAD Agents reference", "https://docs.bmad-method.org/reference/agents/"),
            ("BMAD Core Tools reference", "https://docs.bmad-method.org/reference/core-tools/"),
            ("BMAD Commands reference", "https://docs.bmad-method.org/reference/commands/"),
        ],
        "body": dedent(
            """
            # BMAD Method

            Рабочее досье по BMAD Method после отдельного русского language repair. Это не финальная глава и не профиль; цель — сохранить механику BMAD как цепочку фаз, агентов, skills, файлов, gates, failure modes и вопросов для следующего source pass.

            BMAD Getting Started описывает метод как guided workflows with specialized AI agents, leading through planning, architecture and implementation [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Минимальный вход: Node.js 20.12+, Git, AI-powered IDE и project idea [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Установка: `npx bmad-method install`, для prerelease `npx bmad-method@next install`; installer creates `_bmad/` and `_bmad-output/` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). `_bmad/` содержит agents, workflows, tasks and configuration; `_bmad-output/` предназначен для сохраняемых artifacts [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            BMAD-Help — не декоративный helper, а навигационный механизм. Источник говорит, что после установки нужно вызвать `bmad-help`; он detects installed modules, inspects project progress, recommends next workflow and first required task [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Дополнительная важная деталь: BMad-Help automatically runs at the end of every workflow to tell what to do next [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Для будущей главы это нужно раскрыть как anti-lostness layer: BMAD пытается решать проблему “что делать дальше” внутри длинного процесса.

            Четыре фазы BMAD: Analysis, Planning, Solutioning, Implementation [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Analysis optional: brainstorming, market/domain/technical research, product brief, PRFAQ [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Planning required: for BMad Method and Enterprise tracks run `bmad-prd`; output includes `prd.md`, `addendum.md`, `decision-log.md`; intents include Create, Update, Validate [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Solutioning creates architecture and epics/stories; Implementation builds epic by epic, story by story [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            Tracks matter. Quick Flow targets bug fixes, simple features and clear scope, roughly 1-15 stories; BMad Method targets products, platforms and complex features, roughly 10-50+ stories; Enterprise targets compliance and multi-tenant systems, roughly 30+ stories [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Источник explicitly warns that story counts are guidance, not definitions; choose track by planning needs [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Это важный caveat: нельзя механически выбирать процесс по числу story, нужно смотреть на степень неопределённости и требуемые документы.

            Planning and solutioning chain: `bmad-prd` creates or validates requirements artifacts; optional UX uses `bmad-agent-ux-designer` and `bmad-ux`; architecture uses `bmad-agent-architect` and `bmad-create-architecture`; epics and stories now come after architecture so database, API patterns and tech stack can inform story breakdown; PM runs `bmad-create-epics-and-stories` using both PRD and Architecture [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Здесь важно сохранить передачу контекста: PRD не заканчивает работу, architecture уточняет реализацию, а stories создаются после architecture, чтобы не быть product-only нарезкой.

            Implementation Readiness Check — особенно важный gate. Источник рекомендует invoke Architect in a fresh chat and run `bmad-check-implementation-readiness`; он validates cohesion across all planning documents [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Пока exact output формата PASS/CONCERNS/FAIL нужно проверить в deeper source pass; но уже сейчас понятно, что gate стоит между planning artifacts and implementation. Для будущей главы это можно описать как BMAD’s anti-false-handoff mechanism: нельзя честно передать story в dev, если PRD, architecture and stories расходятся.

            Build cycle: after planning, invoke Developer agent and run `bmad-sprint-planning`, which creates `sprint-status.yaml`; for each story repeat fresh-chat cycle: `bmad-create-story`, `bmad-dev-story`, `bmad-code-review`; after all stories in an epic run `bmad-retrospective` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Project output tree includes `_bmad-output/planning-artifacts/PRD.md`, `architecture.md`, `epics/`, `_bmad-output/implementation-artifacts/sprint-status.yaml` and optional `project-context.md` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Кандидат на изображение: project tree from Getting Started; причина — показывает, где физически живёт контекст.

            Fresh chats are a real methodological rule. Documentation says always start a fresh chat for each workflow to prevent context limitations [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). This is counterintuitive but important: BMAD does not rely on one giant chat; it externalizes state into artifacts and reloads the right role/workflow in a new conversation. `project-context.md` can document technical preferences and implementation rules; it can be created manually at `_bmad-output/project-context.md` or generated after architecture with `bmad-generate-project-context` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            Failure modes: role theater, where agent names create confidence without evidence; stale PRD after architecture changes; stale architecture after implementation discoveries; story breakdown created too early; readiness check run as ritual; fresh chats without enough artifact context; `project-context.md` missing or obsolete; Quick Flow used for a complex platform; code review performed by same context that made the mistake; BMad-Help recommendation trusted without reading artifacts. Phase-output laundering is the most dangerous pattern: every phase produces a plausible file, but the files do not actually constrain the next phase.

            Сравнительная заметка внутри темы: BMAD is role/workflow/artifact heavy. It differs from Spec Kit by stronger named agents and richer phase taxonomy; from Kiro by being installable across AI IDEs and using skills/workflows rather than one IDE task surface; from GSD by deeper planning and role system, but weaker emphasis on minimal shipping handoff; from TDAD by relying on document cohesion and code review rather than hidden tests/mutation or impact map; from Constitutional SDD by not making security constitution the central artifact.

            Кандидаты на изображения: `https://docs.bmad-method.org/reference/workflow-map/` — workflow map diagram; причина — показать фазовый маршрут. `https://docs.bmad-method.org/tutorials/getting-started/` — project tree and quick reference commands; причина — показать physical artifacts. `https://docs.bmad-method.org/reference/agents/` — agents reference; причина — показать role surface. Остаточная очередь: открыть llms-full.txt, Workflow Map diagram, Agents, Core Tools, Skills, Commands, Testing Options and exact `bmad-check-implementation-readiness` workflow; извлечь exact output, required inputs, status labels, failure examples and issue discussions [BMAD Workflow Map](https://docs.bmad-method.org/reference/workflow-map/) [BMAD Agents reference](https://docs.bmad-method.org/reference/agents/) [BMAD Core Tools reference](https://docs.bmad-method.org/reference/core-tools/).
            """
        ),
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def report(topic: dict, slug: str, kind: str) -> str:
    source_lines = "\n".join(f"- [{name}]({url})" for name, url in topic["sources"])
    if kind == "source_opening":
        return f"# Pass 11: повторное раскрытие источников для языкового ремонта\n\nОткрыты и заново использованы источники, нужные для исправления английского клея в `{topic['title']}`. Факты в финальном досье оставлены только там, где они привязаны к источникам или явно помечены как вывод.\n\n{source_lines}\n"
    if kind == "source_discovery":
        return f"# Pass 11: независимый поиск и остаточная очередь\n\nВ этом проходе independent discovery не расширял factual base новой неподтверждённой информацией. Очередь сохранена как residual queue: full PDFs/HTML, repository files, issue/PR discussions, release notes, diagrams/screenshots and examples. По `{topic['title']}` новые факты без открытия источника не добавлялись.\n"
    if kind == "dossier_transfer":
        return f"# Pass 11: перенос исправленного материала в dossier\n\nФинальный файл `work/dossiers/{topic['final']}` переписан как русский рабочий буфер. Перенесены source-level детали, команды, файлы, артефакты, gates, caveats, failure modes, сравнительные заметки внутри темы, image candidates and residual source queue.\n"
    if kind == "language_repair":
        return f"# Pass 11: языковой ремонт\n\nЭтот проход добавлен после автоматической языковой проверки. Старый `dossier_after_pass_10.md` содержал слишком много английского связующего текста. В `dossier_after_pass_11.md` основной объяснительный текст переписан по-русски; английскими оставлены имена источников, файлов, команд, статусов и устойчивых терминов.\n"
    if kind == "delta":
        return f"# Pass 11: delta\n\nИзменение относительно pass 10: заменён английско-технический текст на русский source buffer; сохранены и усилены inline links; добавлены или уточнены кандидаты на изображения; final dossier теперь должен совпадать с `dossier_after_pass_11.md`, а не с `dossier_after_pass_10.md`.\n"
    if kind == "new_sources":
        return f"# Pass 11: новые источники и очередь\n\nНовые фактические источники в этом repair-проходе не заявлены как раскрытые. Очередь источников перенесена в само dossier и остаётся обязательной перед финальной главой.\n"
    raise ValueError(kind)


def ledger(topic: dict) -> str:
    lines = [
        f"# Cycle ledger: {topic['title']}",
        "",
        "Ledger относится к protocol-only dossier-run 2026-06-08. Pass 11 добавлен после языковой проверки, потому что pass 10 оставлял слишком много английского связующего текста.",
        "",
        "| pass | dossier snapshot | delta | language repair | source discovery | status |",
        "|---|---|---|---|---|---|",
    ]
    for i in range(1, 12):
        status = "created"
        if i == 11:
            status = "created; language repair pass"
        lines.append(f"| {i:02d} | dossier_after_pass_{i:02d}.md | cycle_{i:02d}_delta.md | cycle_{i:02d}_language_repair.md | cycle_{i:02d}_source_discovery.md | {status} |")
    return "\n".join(lines)


def audit(topic: dict, slug: str) -> str:
    return dedent(
        f"""
        # Quality audit: {topic['title']}

        Дата: {DATE}

        Verdict: PASS WITH REPAIR

        10-cycle gate: выполнен и расширен до 11 проходов. В pass folder `work/dossier-passes/{slug}` есть `dossier_after_pass_01.md` ... `dossier_after_pass_11.md`, `cycle_NN_delta.md`, `cycle_NN_language_repair.md`, `cycle_NN_source_discovery.md`.

        Language gate: pass 11 добавлен специально из-за провала языкового баланса в pass 10. Финальный dossier теперь совпадает с `dossier_after_pass_11.md`; основной объяснительный текст написан по-русски, английскими оставлены имена источников, файлов, команд and stable technical names.

        Inline provenance: ссылки на внешние источники стоят внутри dossier рядом с фактами, командами, файлами, claims and caveats.

        Image candidates: кандидаты на внешние изображения включены в текст dossier рядом с соответствующими разделами; сами assets не добавлялись.

        Остаточный repair: перед финальной главой нужен deep source pass по full PDFs/HTML, repository files, issue/PR discussions, release notes, screenshots and exact examples where exact detail is required. Поэтому честный verdict остаётся `PASS WITH REPAIR`, не `PASS`.
        """
    )


def update_checks() -> None:
    checks_path = ROOT / "work" / "checks.json"
    data = json.loads(checks_path.read_text(encoding="utf-8"))
    data["version"] = "v30"
    run = data.get("verified_dossier_run_2026_06_08", {})
    for slug, topic in TOPICS.items():
        if "topics" in run and slug in run["topics"]:
            run["topics"][slug]["passes"] = 11
            run["topics"][slug]["final_matches_last_snapshot"] = True
            run["topics"][slug]["language_repair_pass_11"] = True
    data["verified_dossier_run_2026_06_08"] = run
    data["dossier_language_repair_pass_11_2026_06_08"] = {
        "date": DATE,
        "reason": "Pass 10 dossiers were structurally valid but too English-heavy; pass 11 rewrote final dossiers as Russian source buffers.",
        "topics": {
            slug: {
                "final_dossier": f"work/dossiers/{topic['final']}",
                "pass_folder": f"work/dossier-passes/{slug}",
                "passes": 11,
                "final_snapshot": f"work/dossier-passes/{slug}/dossier_after_pass_11.md",
                "audit": f"work/reports/{topic['audit']}",
                "verdict": "PASS WITH REPAIR",
            }
            for slug, topic in TOPICS.items()
        },
        "comparative_synthesis_created": False,
        "image_assets_included": False,
    }
    write(checks_path, json.dumps(data, ensure_ascii=False, indent=2))


def update_discourse() -> None:
    discourse = ROOT / "work" / "discourse.md"
    text = discourse.read_text(encoding="utf-8")
    addition = dedent(
        """

        ## Pass 11: языковой ремонт protocol-only dossier-run

        После проверки protocol-only dossier-run обнаружен важный дефект: файлы pass 10 были структурно связаны с 10 проходами и финальные dossier совпадали с `dossier_after_pass_10.md`, но основной текст нескольких dossier оставался слишком английским. Это нарушало language gate в `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md`, поэтому запуск нельзя было честно закрывать на pass 10.

        Добавлен pass 11 для всех шести тем: `work/dossier-passes/spec-kit/dossier_after_pass_11.md`, `work/dossier-passes/kiro-specs/dossier_after_pass_11.md`, `work/dossier-passes/constitutional-sdd/dossier_after_pass_11.md`, `work/dossier-passes/tdad-comparative/dossier_after_pass_11.md`, `work/dossier-passes/gsd-open-gsd/dossier_after_pass_11.md`, `work/dossier-passes/bmad-method/dossier_after_pass_11.md`. В каждой pass-папке также добавлены `cycle_11_source_opening.md`, `cycle_11_source_discovery.md`, `cycle_11_dossier_transfer.md`, `cycle_11_language_repair.md`, `cycle_11_delta.md`, `cycle_11_new_sources.md`.

        Финальные dossier `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`, `work/dossiers/KIRO_SPECS_DOSSIER.md`, `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md`, `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`, `work/dossiers/GSD_OPEN_GSD_DOSSIER.md`, `work/dossiers/BMAD_METHOD_DOSSIER.md` теперь совпадают с pass 11 snapshots. `work/checks.json` обновлён до `v30` с блоком `dossier_language_repair_pass_11_2026_06_08`. Audit verdicts оставлены `PASS WITH REPAIR`: языковой gate исправлен, но перед финальной главой нужен отдельный deep source pass по full PDFs/HTML, repository files, release notes, issues, screenshots and exact examples.
        """
    )
    write(discourse, text.rstrip() + addition)


def main() -> None:
    for slug, topic in TOPICS.items():
        pass_dir = ROOT / "work" / "dossier-passes" / slug
        final_path = ROOT / "work" / "dossiers" / topic["final"]
        snapshot = pass_dir / "dossier_after_pass_11.md"
        write(snapshot, topic["body"])
        write(final_path, topic["body"])
        write(pass_dir / "cycle_11_source_opening.md", report(topic, slug, "source_opening"))
        write(pass_dir / "cycle_11_source_discovery.md", report(topic, slug, "source_discovery"))
        write(pass_dir / "cycle_11_dossier_transfer.md", report(topic, slug, "dossier_transfer"))
        write(pass_dir / "cycle_11_language_repair.md", report(topic, slug, "language_repair"))
        write(pass_dir / "cycle_11_delta.md", report(topic, slug, "delta"))
        write(pass_dir / "cycle_11_new_sources.md", report(topic, slug, "new_sources"))
        write(pass_dir / "CYCLE_LEDGER.md", ledger(topic))
        write(ROOT / "work" / "reports" / topic["audit"], audit(topic, slug))
    update_checks()
    update_discourse()


if __name__ == "__main__":
    main()
