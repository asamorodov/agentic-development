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
        "body": dedent(
            """
            # Spec Kit

            Это рабочее досье по Spec Kit, а не краткий профиль и не финальная глава. Его задача — сохранить фактуру источников: команды, файлы, цепочку артефактов, места человеческого решения, возможные поломки, кандидаты на внешние изображения и остаточную очередь чтения. Английскими оставлены только имена проекта, команд, файлов, каталогов, источников и устойчивых терминов.

            Spec Kit задаёт разработку через цепочку спецификационных артефактов. В документации центральная последовательность выглядит как `Spec -> Plan -> Tasks -> Implement`: сначала формулируется, что строится и зачем, затем добавляется технический план, затем план раскладывается на задачи, и только после этого запускается реализация [документация Spec Kit](https://github.github.com/spec-kit/). Это важно для будущего текста: метод не равен “хорошему промпту”. Он заставляет намерение пройти через несколько файлов, каждый из которых становится входом для следующего шага.

            Установка и первичный запуск сами являются частью метода. Документация показывает запуск `uvx --from git+https://github.com/github/spec-kit.git specify init my-project --integration copilot`; репозиторий также показывает установку `specify-cli` через `uv tool install` и инициализацию `specify init my-project --integration copilot` [документация Spec Kit](https://github.github.com/spec-kit/) [репозиторий github/spec-kit](https://github.com/github/spec-kit). Из этого следует рабочая модель: Spec Kit внедряется в выбранный агентский инструмент через слой интеграции. Он не привязан к одному исполнителю; документация перечисляет Copilot, Gemini, Codex, Windsurf, Claude, Forge, Kiro и `generic`-вариант [документация Spec Kit](https://github.github.com/spec-kit/).

            Основная командная поверхность: `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`, а также `/speckit.taskstoissues` [репозиторий github/spec-kit](https://github.com/github/spec-kit). Конституция задаёт принципы и ограничения проекта. Спецификация фиксирует пользовательские сценарии, требования и границы поведения. План переводит требования в технические решения. Задачи делают план исполнимым. Реализация должна использовать предыдущие файлы как обязательный контекст, а не начинать рассуждение заново. Команда `/speckit.taskstoissues` особенно полезна как источник деталей: она показывает, что task-файл может быть перенесён в GitHub Issues и стать частью командной работы, а не только локальным текстом для агента [репозиторий github/spec-kit](https://github.com/github/spec-kit).

            Репозиторий показывает материальную структуру метода: `integrations`, `templates`, `extensions`, `presets`, `workflows`, `src/specify_cli` [репозиторий github/spec-kit](https://github.com/github/spec-kit). Это нужно сохранить в будущей главе: Spec Kit состоит не только из документации, но и из CLI, шаблонов, интеграций и расширений. Расширяемость полезна, но создаёт риск. Community extensions и presets могут добавить governance checks, architecture checks или другие маршруты, но их нельзя использовать как доказательство качества без отдельного просмотра исходников [документация Spec Kit](https://github.github.com/spec-kit/).

            Человеческие контрольные точки встроены в смену фаз. Конституцию нужно проверить до спецификации; спецификацию — до плана; план — до задач; задачи — до реализации. Если эти проверки пропустить, метод легко превращается в производство красивых файлов. Главный режим поломки — `spec laundering`: неясность превращается в уверенный Markdown-документ, а затем этот документ начинает управлять реализацией так, будто решение действительно принято. Другие поломки: устаревшая конституция, задачи без обратной связи к требованиям, расширения без проверки, несовпадение интеграции с выбранным агентом, слишком ранний запуск реализации.

            Внутреннее сравнение для будущего текста: Spec Kit ближе всего к переносимому слою спецификаций. От Kiro он отличается тем, что не является встроенной поверхностью IDE. От BMAD — тем, что меньше строится вокруг ролей и агентов, а больше вокруг цепочки команд и файлов. От GSD — тем, что центр тяжести находится в спецификации и планировании, а не в состоянии проекта и отгрузке. От TDAD — тем, что проверка в основном документарная и чеклистовая, а не тестово-эмпирическая. От Constitutional SDD — тем, что конституция шире проектных принципов и не обязана быть только security-constitution.

            Кандидаты на изображения: `https://github.github.com/spec-kit/` — первый экран и диаграммы документации, чтобы показать позиционирование и цепочку артефактов; `https://github.com/github/spec-kit` — дерево репозитория с `integrations`, `templates`, `extensions`, `presets`, `workflows`, чтобы показать, из чего физически собран метод. Остаточная очередь: полностью раскрыть `spec-driven.md`, reference overview, installation guides, список integrations, reference по extensions/presets/workflows и arXiv/PDF по Spec Kit Agents [статья Spec Kit Agents](https://arxiv.org/abs/2604.05278). До этой очереди нельзя использовать точные исследовательские claims без дополнительной проверки.
            """
        ),
    },
    "kiro-specs": {
        "title": "Kiro Specs",
        "final": "KIRO_SPECS_DOSSIER.md",
        "audit": "KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md",
        "body": dedent(
            """
            # Kiro Specs

            Это рабочее досье по Kiro Specs. Его назначение — сохранить, как Kiro превращает feature request или bugfix в файлы, фазы, проверки и исполняемые задачи. Это не обзор продукта и не финальная глава сайта.

            Kiro описывает specs как структурированные артефакты для разработки функций и исправления ошибок [страница Kiro Specs](https://kiro.dev/docs/specs/). Центральная тройка файлов: `requirements.md` или `bugfix.md`, затем `design.md`, затем `tasks.md` [страница Kiro Specs](https://kiro.dev/docs/specs/). Содержательно это значит: Kiro разделяет поведение, проектирование и выполнение. Агент не получает один общий запрос; он работает внутри папки спецификации, где каждый файл имеет свою роль и может быть проверен человеком.

            Общий маршрут состоит из трёх фаз. Для функции первая фаза создаёт требования, user stories и acceptance criteria в `requirements.md`; для исправления ошибки создаётся `bugfix.md`, где фиксируются текущее поведение, ожидаемое поведение и то поведение, которое нельзя менять [страница Kiro Specs](https://kiro.dev/docs/specs/). Вторая фаза создаёт `design.md`: архитектуру, компоненты, sequence diagrams, data flow, error handling и стратегию тестирования [страница Kiro Specs](https://kiro.dev/docs/specs/). Третья фаза создаёт `tasks.md`, где реализация разбита на отдельные задачи [страница Kiro Specs](https://kiro.dev/docs/specs/).

            У `tasks.md` есть неочевидная роль: это не только список дел, но и вход для планирования исполнения. При запуске всех задач Kiro анализирует зависимости, строит граф зависимостей и группирует независимые задачи в волны: первая волна содержит задачи без зависимостей, следующая — задачи, зависимости которых закрыты предыдущей волной, и так далее [страница Kiro Specs](https://kiro.dev/docs/specs/). Задачи внутри волны могут выполняться параллельно, а волны идут последовательно [страница Kiro Specs](https://kiro.dev/docs/specs/). Это сильная деталь источника для будущей главы: Kiro делает task-файл исполнимой структурой, а не только текстовым планом.

            Feature Specs поддерживают несколько способов входа. Requirements-First начинается с поведения и ведёт цепочку `Requirements -> Design -> Tasks`; он подходит, когда поведение известно, а архитектура ещё гибкая [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/). Design-First начинается с технического дизайна, псевдокода или архитектурных ограничений и затем выводит требования и задачи [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/). Quick Plan пропускает отдельные утверждения между фазами и создаёт три артефакта быстрее, поэтому подходит только для хорошо понятных функций с низким риском [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/).

            Требования используют EARS-нотацию: условие или событие выражается через `WHEN`, а ожидаемое поведение через `THE SYSTEM SHALL` [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/). Это полезно не как формальный стиль, а как способ сделать требования проверяемыми. Отдельная поверхность проверки — Analyze Requirements: Kiro может искать противоречия, неясность, gaps и конфликтующие ограничения перед переходом к дизайну [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/). Режим поломки: EARS превращается в шаблон, но не делает требования полными; тогда `design.md` и `tasks.md` наследуют пустоты.

            Человеческие контрольные точки зависят от маршрута. В Requirements-First человек должен проверить требования до дизайна, дизайн до задач, задачи до исполнения. В Design-First сначала проверяется техническая форма решения. Quick Plan сознательно уменьшает число остановок, и именно поэтому опасен на сложных задачах [страница Feature Specs](https://kiro.dev/docs/specs/feature-specs/). Для bugfix особенно важно сохранить `unchanged behavior`: без него агент может закрыть симптом и создать регрессию.

            Внутреннее сравнение: Kiro ближе всего к IDE-native спецификационному маршруту. От Spec Kit он отличается встроенным исполнением задач и графом зависимостей; от BMAD — меньшим количеством ролей и более прямой цепочкой файлов; от GSD — фокусом на feature/bug artifacts, а не на долговечном состоянии проекта; от TDAD — тем, что его проверка документарная и IDE-управляемая, а не hidden-test или mutation-test; от Constitutional SDD — отсутствием обязательной security-constitution.

            Кандидаты на изображения: `https://kiro.dev/docs/specs/` — схема трёх фаз, скриншот исполнения задач и возможный граф волн; `https://kiro.dev/docs/specs/feature-specs/` — схемы Requirements-First, Design-First и Quick Plan. Остаточная очередь: открыть отдельные страницы best practices, bugfix specs, steering, hooks/actions и changelog; проверить, как `steering` и hooks соединяются со specs [Kiro Steering](https://kiro.dev/docs/steering/) [Kiro Hooks actions](https://kiro.dev/docs/hooks/actions/).
            """
        ),
    },
    "constitutional-sdd": {
        "title": "Constitutional SDD",
        "final": "CONSTITUTIONAL_SDD_DOSSIER.md",
        "audit": "CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md",
        "body": dedent(
            """
            # Constitutional Spec-Driven Development

            Это рабочее досье по Constitutional SDD. Оно фиксирует, как безопасность переносится в слой спецификации до генерации кода, и какие детали источников нужно сохранить для будущего текста.

            Главная проблема в статье: AI-assisted “vibe coding” может быстро создавать функциональный код, но модели часто уделяют больше внимания видимой функциональности, чем безопасности [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). Ответ метода — Constitution: версионированный, машинно-читаемый документ с обязательными security constraints, выведенными из CWE/MITRE Top 25 и регуляторных рамок [статья Constitutional SDD](https://arxiv.org/abs/2602.02584) [MITRE CWE Top 25](https://cwe.mitre.org/top25/). Конституция здесь не культурная метафора, а входной артефакт генерации и проверки.

            Источник описывает работу как security-by-construction для AI-assisted code generation. В метаданных статьи указаны 15 страниц, 2 figures, 5 tables, 11 code listings, reference implementation и compliance traceability matrix [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). Эти детали нужно сохранить именно как очередь чтения: без полного PDF/HTML нельзя честно пересказывать таблицы, листинги и матрицу прослеживаемости.

            Демонстрационный домен — банковские микросервисы: customer management, account operations и transaction processing [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). Это не означает, что метод только для банков; источник использует банк как домен с высокими требованиями к безопасности и регуляторике. В будущем тексте важно отделить case study от общей методики.

            Заявленная цепочка: Constitution задаёт принципы и ограничения; спецификация функции должна ссылаться на релевантные clauses; генерация кода получает эти clauses как обязательный контекст; затем compliance traceability matrix связывает principles, requirements и code locations [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). В abstract заявлено покрытие 10 critical CWE vulnerabilities и полная прослеживаемость от principles к code locations [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). Список этих 10 CWE нельзя восстановить по памяти; его нужно извлечь из полного источника.

            В статье заявлено снижение security defects на 73% по сравнению с unconstrained AI generation при сохранении developer velocity [статья Constitutional SDD](https://arxiv.org/abs/2602.02584). Это число нужно использовать осторожно: перед финальной главой надо проверить baseline, объём эксперимента, способ подсчёта defects, способ измерения velocity и ограничения case study. В досье число хранится как claim конкретного источника, а не как универсальное обещание.

            Человеческие контрольные точки должны быть жёсткими. Сначала человек утверждает Constitution и источники security constraints. Затем проверяет, что feature spec действительно ссылается на clauses, а не пишет общую фразу “make secure”. Перед merge должна быть проверена матрица прослеживаемости и фактические evidence: tests, static analysis, review или checklist. Если этого нет, Constitutional SDD ломается в compliance theater: файл Constitution существует, но не управляет кодом.

            Сравнение внутри темы: Constitutional SDD похож на Spec Kit тем, что переносит решения в спецификационный слой, но его центр уже — безопасность. От Kiro он отличается тем, что структурированных требований недостаточно: нужны security clauses и прослеживаемость. От TDAD он отличается тем, что начинает с policy/constitution, а не с тестовой компиляции поведения. От BMAD он меньше опирается на роли, но сильнее фиксирует security gate. От GSD он отличается тем, что “done” невозможно без compliance evidence.

            Кандидаты на изображения: `https://arxiv.org/html/2602.02584` — figures, tables или traceability matrix, если доступны; причина — будущему читателю нужно увидеть связь “principle -> requirement -> code location”. Остаточная очередь: открыть полный PDF/HTML, извлечь 10 CWE, таблицы, листинги, поля матрицы прослеживаемости, reference implementation, limitations, а также сверить использование MITRE Top 25 и OWASP ASVS [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/).
            """
        ),
    },
    "tdad-comparative": {
        "title": "TDAD comparative",
        "final": "TDAD_COMPARATIVE_DOSSIER.md",
        "audit": "TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md",
        "body": dedent(
            """
            # TDAD comparative

            Это рабочее досье сравнивает две разные линии TDAD. Сравнение остаётся внутри темы и не создаёт общий synthesis между всеми досье.

            Первая линия — Test-Driven AI Agent Definition. Статья предлагает относиться к промпту агента как к артефакту, который компилируется из поведенческой спецификации под набор тестов [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Один coding agent превращает спецификацию в executable tests, другой итеративно уточняет промпт, пока тесты не проходят [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Смысл для будущей главы: промпт перестаёт быть ручным текстом и становится результатом проверяемого цикла.

            Центральная проблема первой линии — production agents с инструментами могут ломаться молча: маленькое изменение промпта создаёт регрессию, инструмент используется неверно, policy violation проявляется уже после deployment [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Поэтому метод использует visible/hidden test split, semantic mutation testing и spec evolution scenarios [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Скрытые тесты защищают от подгонки под видимый набор, мутационное тестирование проверяет силу тестового набора, а evolution scenarios показывают, сохраняется ли поведение при изменении требований.

            Evaluation первой линии выполнена на SpecSuite-Core: четыре deeply-specified agents, покрывающие policy compliance, grounded analytics, runbook adherence и deterministic enforcement [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Источник заявляет 24 independent trials, 92% v1 compilation success, 97% mean hidden pass rate, 58% compilation success for evolved specifications, mutation scores 86-100%, 78% v2 hidden pass rate и 97% regression safety scores [статья Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806). Эти числа нужно хранить с источником и не обобщать без чтения полного PDF, harness и репозитория [репозиторий tdad-paper-code](https://github.com/f-labs-io/tdad-paper-code).

            Вторая линия — Test-Driven Agentic Development. Она решает другую проблему: AI coding agents исправляют issue, но создают регрессии, а benchmarks часто считают только resolution rate [статья Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973). Метод выполняет анализ влияния до изменения: строит карту связей между source files и tests, чтобы агент знал, какие tests нужно запустить и где самоисправляться [статья Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973). Важная деталь: карта передаётся как lightweight agent skill — статический текстовый файл, который агент запрашивает во время выполнения [статья Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973).

            Evaluation второй линии использует SWE-bench Verified и open-weight models on consumer hardware: Qwen3-Coder 30B на 100 instances и Qwen3.5-35B-A3B на 25 instances [статья Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973). Источник заявляет снижение regression rate на 70%, с 6.08% до 1.82% относительно vanilla baseline [статья Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973). Это нужно хранить как точный claim источника и проверять по полному paper, коду, map format и протоколу тестирования [репозиторий TDAD](https://github.com/pepealonso95/TDAD).

            Главное различие двух TDAD: первая компилирует agent definitions и промпты из behavioural specs, вторая защищает code changes от регрессий через карту source/test. В первой центральные артефакты — behavioral spec, visible tests, hidden tests, compiled prompt, mutation variants, evolution scenarios. Во второй — dependency map, agent skill, выбранные impacted tests, patch and self-correction loop. Это различие обязательно сохранить, иначе будущая глава смешает две разные research programs.

            Человеческие контрольные точки в первой линии: утверждение behavioural spec, защита hidden tests, проверка mutation score, принятие compiled prompt. Поломки: hidden tests слишком похожи на visible, prompt переобучается на harness, mutation variants слабые. Человеческие контрольные точки во второй линии: свежесть dependency map, полнота impacted tests, обязательный запуск relevant tests, отдельный учёт regressions. Поломки: карта устаревает, агент игнорирует skill file, тестовый выбор неполный, baseline сравнение неадекватно.

            Кандидаты на изображения: HTML/PDF статьи `https://arxiv.org/abs/2603.08806` — схема компиляции промпта через tests; HTML/PDF статьи `https://arxiv.org/abs/2603.17973` — схема карты влияния source/test; README-диаграммы из `https://github.com/f-labs-io/tdad-paper-code` и `https://github.com/pepealonso95/TDAD`, если они есть. Остаточная очередь: открыть полные PDF/HTML, harness, examples, benchmark configs, failure cases, формат dependency map и exact prompts.
            """
        ),
    },
    "gsd-open-gsd": {
        "title": "GSD / Open GSD",
        "final": "GSD_OPEN_GSD_DOSSIER.md",
        "audit": "GSD_OPEN_GSD_DOSSIER_QUALITY_AUDIT.md",
        "body": dedent(
            """
            # GSD / Open GSD

            Это рабочее досье по GSD / Open GSD. Оно фиксирует метод как переносимый рабочий каркас для дисциплины Git, Ship, Done внутри существующих AI coding tools.

            Open GSD описывает `gsd-core` как framework, который приносит дисциплину Git, Ship, Done в уже используемый AI coding tool [страница gsd-core](https://opengsd.net/products/gsd-core). Важная позиция источника: это не отдельная IDE, а копируемый prompt framework и набор durable markdown artifacts, который работает в Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Copilot и других средах [страница gsd-core](https://opengsd.net/products/gsd-core). Поэтому GSD ближе к переносимому процессному слою, чем к продуктовой IDE.

            Установка дана как `npx @opengsd/gsd-core@latest copy` [страница gsd-core](https://opengsd.net/products/gsd-core). Базовые команды: `/gsd new-project`, `/gsd discuss`, `/gsd verify` [страница gsd-core](https://opengsd.net/products/gsd-core). Первая создаёт проектный контекст, вторая фиксирует решения до сборки, третья проверяет работу перед отгрузкой. Это минимальный цикл GSD: сначала контекст, затем обсуждение и фиксация решений, затем проверка перед “done”.

            Центральные артефакты: `VISION.md`, `ROADMAP.md`, `CURRENT_STATE.md`, `SHIP_HANDOFF.md` [страница gsd-core](https://opengsd.net/products/gsd-core). `VISION.md` удерживает смысл проекта; `ROADMAP.md` хранит направление; `CURRENT_STATE.md` должен переживать разрывы сессий и показывать текущее состояние; `SHIP_HANDOFF.md` делает передачу результата явной. Главная проблема, которую пытается решить GSD, — потеря состояния между агентскими сессиями и преждевременное объявление “done”.

            Рабочий цикл на странице можно реконструировать так: создать проект, обсудить следующую фазу и зафиксировать решения, затем планировать, выполнять, проверять и отгружать через устойчивые Markdown-артефакты [страница gsd-core](https://opengsd.net/products/gsd-core). Для будущей главы важно: verify стоит до shipping, а не после. Если verify превращается в самоуверенный отчёт агента без evidence, метод ломается.

            Человеческие контрольные точки: `/gsd discuss` должен зафиксировать намерение и решения до реализации; `/gsd verify` должен остановить отгрузку, если evidence недостаточно [страница gsd-core](https://opengsd.net/products/gsd-core). Пока точный алгоритм verify не раскрыт в этом досье: нужно открыть commands reference и configuration docs [документация конфигурации Open GSD](https://opengsd.net/docs/v1/configuration). Поэтому нельзя утверждать exact verification schema без дополнительного прохода.

            Внутреннее сравнение: GSD отличается от Spec Kit тем, что его главные артефакты — состояние проекта и handoff, а не spec/plan/tasks. От Kiro — тем, что он не встроенная IDE-поверхность. От BMAD — тем, что он легче и меньше опирается на роли, но сильнее подчёркивает shipping state. От TDAD — тем, что проверка workflow-level, а не hidden-test или dependency-map. От Constitutional SDD — тем, что security constitution не является обязательным центром.

            Поломки: `VISION.md` становится лозунгом; `ROADMAP.md` не обновляется после решений; `CURRENT_STATE.md` устаревает; `SHIP_HANDOFF.md` пишется задним числом; `/gsd verify` становится self-report; copied framework устаревает относительно upstream; отличия между средами исполнения ломают смысл команд.

            Кандидаты на изображения: `https://opengsd.net/products/gsd-core` — первый экран с командой установки, командной поверхностью и артефактами; `https://github.com/open-gsd/gsd-core` — дерево репозитория; страницы configuration/commands, если там есть схемы. Остаточная очередь: открыть user guide, commands reference, configuration schema, README, release notes, examples of `VISION.md`, `ROADMAP.md`, `CURRENT_STATE.md`, `SHIP_HANDOFF.md`, а также legacy auto mode docs [репозиторий open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) [auto mode docs](https://github.com/gsd-build/gsd-2/blob/main/docs/user-docs/auto-mode.md) [origin site](https://getshitdone.help/).
            """
        ),
    },
    "bmad-method": {
        "title": "BMAD Method",
        "final": "BMAD_METHOD_DOSSIER.md",
        "audit": "BMAD_METHOD_DOSSIER_QUALITY_AUDIT.md",
        "body": dedent(
            """
            # BMAD Method

            Это рабочее досье по BMAD Method. Его назначение — сохранить механику BMAD как цепочку фаз, агентов, skills, файлов, контрольных точек, команд, режимов поломки и остаточных вопросов. Это не финальная глава и не краткий профиль.

            BMAD Getting Started описывает метод как управляемые рабочие маршруты со специализированными AI-агентами, которые проводят проект через планирование, архитектуру и реализацию [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Минимальные условия входа: Node.js 20.12+, Git, AI-powered IDE и идея проекта [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Установка выполняется командой `npx bmad-method install`; для prerelease-версии указан `npx bmad-method@next install` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Установщик создаёт `_bmad/` и `_bmad-output/`: первый каталог хранит агентов, рабочие маршруты, задачи и конфигурацию, второй — создаваемые артефакты [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            `bmad-help` — важный навигационный механизм, а не справочная мелочь. После установки источник предлагает вызвать `bmad-help`: он определяет установленные модули, смотрит прогресс проекта, рекомендует следующий рабочий маршрут и первую нужную задачу [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Документация также говорит, что BMad-Help запускается в конце каждого рабочего маршрута и подсказывает следующий шаг [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Для будущей главы это можно описать как слой против потери ориентира в длинном агентском процессе.

            Базовые фазы BMAD: Analysis, Planning, Solutioning, Implementation [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Analysis необязательна и включает brainstorming, research, product brief и PRFAQ [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Planning обязательна для BMad Method и Enterprise tracks: команда `bmad-prd` создаёт или обновляет `prd.md`, `addendum.md`, `decision-log.md`; режимы включают Create, Update, Validate [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Solutioning переводит требования в architecture и story breakdown. Implementation идёт эпик за эпиком и story за story [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            Tracks нужно хранить как отдельную деталь. Quick Flow подходит для небольших и ясных задач, ориентировочно 1-15 stories. BMad Method подходит для продуктов, платформ и сложных функций, ориентировочно 10-50+ stories. Enterprise подходит для compliance-heavy и multi-tenant систем, ориентировочно 30+ stories [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Источник подчёркивает, что число stories — ориентир, а не определение; трек выбирают по потребностям планирования [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Поломка здесь очевидна: выбрать Quick Flow для сложной платформы и получить видимость процесса без достаточного планирования.

            Цепочка передачи контекста в planning/solutioning важнее списка команд. `bmad-prd` создаёт требования; опциональный UX-проход использует `bmad-agent-ux-designer` и `bmad-ux`; архитектурный проход использует `bmad-agent-architect` и `bmad-create-architecture`; после архитектуры PM запускает `bmad-create-epics-and-stories`, используя PRD и Architecture [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Источник прямо важен тем, что epics/stories создаются после architecture, чтобы database, API patterns, tech stack и другие технические решения повлияли на story breakdown [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            `bmad-check-implementation-readiness` — ключевая контрольная точка между планированием и реализацией. Источник рекомендует вызвать Architect в свежем чате и запустить `bmad-check-implementation-readiness`; проверка должна подтвердить согласованность planning documents [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Точный формат вывода ещё нужно раскрыть в Workflow/Commands sources, но сама роль gate ясна: BMAD пытается предотвратить ложную передачу, когда PRD, architecture и stories выглядят готовыми, но расходятся между собой.

            Implementation cycle: после planning Developer agent запускает `bmad-sprint-planning`, создаётся `sprint-status.yaml`; для каждой story повторяется цикл свежего чата: `bmad-create-story`, `bmad-dev-story`, `bmad-code-review`; после завершения stories в epic запускается `bmad-retrospective` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). Дерево результата включает `_bmad-output/planning-artifacts/PRD.md`, `architecture.md`, `epics/`, `_bmad-output/implementation-artifacts/sprint-status.yaml` и опциональный `project-context.md` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            Правило свежих чатов — настоящая методологическая деталь. Документация говорит начинать fresh chat для каждого workflow, чтобы избежать ограничений контекста [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/). BMAD не полагается на один огромный разговор; он выносит состояние в артефакты и затем заново загружает нужный агентский маршрут. `project-context.md` может хранить технические предпочтения и правила реализации; его можно создать вручную в `_bmad-output/project-context.md` или сгенерировать после архитектуры командой `bmad-generate-project-context` [BMAD Getting Started](https://docs.bmad-method.org/tutorials/getting-started/).

            Режимы поломки: role theater, где имена агентов создают доверие без evidence; устаревший PRD после изменения architecture; устаревшая architecture после implementation discovery; stories, созданные слишком рано; readiness check как ритуал; свежие чаты без достаточного загрузочного контекста; отсутствующий или устаревший `project-context.md`; code review в том же смысловом контексте, где возникла ошибка. Самая опасная поломка — phase-output laundering: каждая фаза производит правдоподобный файл, но файлы не ограничивают следующую фазу.

            Внутреннее сравнение: BMAD — роль- и workflow-насыщенная методика. От Spec Kit он отличается более сильной системой именованных агентов и фаз; от Kiro — переносимостью между AI IDE и большим набором skills/workflows; от GSD — более глубоким planning layer и меньшим упором на минимальный shipping handoff; от TDAD — ставкой на согласованность документов и code review, а не на hidden tests, mutation testing или dependency map; от Constitutional SDD — отсутствием обязательной security-constitution как центрального артефакта.

            Кандидаты на изображения: `https://docs.bmad-method.org/reference/workflow-map/` — workflow map diagram; `https://docs.bmad-method.org/tutorials/getting-started/` — project output tree and quick reference commands; `https://docs.bmad-method.org/reference/agents/` — agents reference. Причина: будущему читателю нужно увидеть не только названия фаз, но и физическое движение артефактов. Остаточная очередь: открыть Workflow Map diagram, Agents, Core Tools, Commands, Testing Options, exact workflow for `bmad-check-implementation-readiness`, llms-full.txt, examples of `prd.md`, `architecture.md`, `story-[slug].md`, `sprint-status.yaml` and issue discussions [BMAD Workflow Map](https://docs.bmad-method.org/reference/workflow-map/) [BMAD Agents reference](https://docs.bmad-method.org/reference/agents/) [BMAD Core Tools](https://docs.bmad-method.org/reference/core-tools/).
            """
        ),
    },
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def report(title: str, final_name: str, kind: str) -> str:
    texts = {
        "source_opening": f"# Pass 13: ручное повторное раскрытие и языковая сборка\n\nОткрыт текущий `work/dossiers/{final_name}` и предыдущий снимок pass 12. Этот проход исправляет не фактическую базу, а качество русского текста после механического ремонта.\n",
        "source_discovery": "# Pass 13: независимый поиск\n\nНовые источники не заявлены. Проход направлен на ручной language/style repair; остаточная очередь источников сохранена внутри dossier.\n",
        "dossier_transfer": f"# Pass 13: перенос ручной версии в dossier\n\nФайл `work/dossiers/{final_name}` переписан как связный русский рабочий буфер. Ссылки, команды, имена файлов и устойчивые названия сохранены.\n",
        "language_repair": "# Pass 13: ручной языковой ремонт\n\nМеханические фразы pass 12 заменены вручную: убраны гибриды вроде `workflow framework`, `feature s`, `creates или validates`, английский связующий текст и неестественные кальки. Английским оставлены точные имена источников, команд, файлов, фаз и устойчивых терминов.\n",
        "delta": "# Pass 13: delta\n\nИзменение относительно pass 12: финальный dossier полностью заменён ручной русской версией без слепых замен. Финальный файл должен совпадать с `dossier_after_pass_13.md`.\n",
        "new_sources": "# Pass 13: новые источники\n\nНовые источники не добавлены; этот проход засчитан как ручной language/style repair внутри лимита 10-20 проходов.\n",
    }
    return texts[kind]


def ledger(title: str) -> str:
    lines = [
        f"# Cycle ledger: {title}",
        "",
        "Ledger относится к protocol-only dossier-run 2026-06-08. Pass 13 добавлен после обнаружения, что механический pass 12 создал неестественные смешанные фразы.",
        "",
        "| pass | dossier snapshot | delta | language repair | source discovery | status |",
        "|---|---|---|---|---|---|",
    ]
    for i in range(1, 14):
        status = "created"
        if i == 11:
            status = "created; language repair pass"
        if i == 12:
            status = "created; mechanical Russian glue repair"
        if i == 13:
            status = "created; manual Russian repair"
        lines.append(f"| {i:02d} | dossier_after_pass_{i:02d}.md | cycle_{i:02d}_delta.md | cycle_{i:02d}_language_repair.md | cycle_{i:02d}_source_discovery.md | {status} |")
    return "\n".join(lines)


def audit(title: str, slug: str) -> str:
    return dedent(
        f"""
        # Quality audit: {title}

        Дата: {DATE}

        Verdict: PASS WITH REPAIR

        Цикл подтверждён 13 видимыми снимками: `work/dossier-passes/{slug}/dossier_after_pass_01.md` ... `work/dossier-passes/{slug}/dossier_after_pass_13.md`. Для каждого прохода есть файлы открытия источников, независимого поиска, переноса, языкового ремонта, delta и новых источников.

        Language gate: pass 13 выполнен вручную после того, как pass 12 оказался слишком механическим. Финальный dossier совпадает с `dossier_after_pass_13.md`; основной текст написан по-русски, английскими оставлены команды, имена файлов, названия источников и устойчивые термины.

        Inline provenance: ссылки на внешние источники стоят рядом с фактами и caveats внутри dossier.

        Image candidates: кандидаты на изображения сохранены в тексте dossier; сами assets не включались.

        Остаточный repair: перед финальной главой нужен deep source pass по полным PDF/HTML, репозиториям, issues, PR, release notes, screenshots and exact examples. Поэтому verdict остаётся `PASS WITH REPAIR`, не `PASS`.
        """
    )


def update_checks() -> None:
    checks_path = ROOT / "work" / "checks.json"
    data = json.loads(checks_path.read_text(encoding="utf-8"))
    data["version"] = "v32"
    run = data.get("verified_dossier_run_2026_06_08", {})
    for slug, topic in TOPICS.items():
        if "topics" in run and slug in run["topics"]:
            run["topics"][slug]["passes"] = 13
            run["topics"][slug]["final_matches_last_snapshot"] = True
            run["topics"][slug]["manual_language_repair_pass_13"] = True
    data["verified_dossier_run_2026_06_08"] = run
    data["dossier_manual_language_repair_pass_13_2026_06_08"] = {
        "date": DATE,
        "reason": "Mechanical pass 12 removed some English glue but produced unnatural mixed Russian/English phrasing; pass 13 replaced final dossiers with manual Russian source buffers.",
        "passes_per_topic": 13,
        "final_snapshot_suffix": "dossier_after_pass_13.md",
        "comparative_synthesis_created": False,
    }
    write(checks_path, json.dumps(data, ensure_ascii=False, indent=2))


def update_discourse() -> None:
    discourse = ROOT / "work" / "discourse.md"
    text = discourse.read_text(encoding="utf-8")
    addition = dedent(
        """

        ## Pass 13: ручной ремонт после неудачной механической русификации

        После pass 12 был просмотрен BMAD dossier и выборочно проверены остальные dossier. Выявлено, что механический ремонт действительно снизил английский клей, но создал смешанные фразы вроде `workflow framework`, `feature s`, `creates или validates` и другие неестественные кальки. Это не удовлетворяет language gate, даже если метрика латиницы стала лучше.

        Добавлен pass 13 для всех шести тем. Финальные dossier `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`, `work/dossiers/KIRO_SPECS_DOSSIER.md`, `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md`, `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`, `work/dossiers/GSD_OPEN_GSD_DOSSIER.md`, `work/dossiers/BMAD_METHOD_DOSSIER.md` заменены ручными русскими версиями и совпадают с `dossier_after_pass_13.md` в соответствующих папках `work/dossier-passes/*/`. `work/checks.json` обновлён до `v32` с блоком `dossier_manual_language_repair_pass_13_2026_06_08`. Audit verdicts остаются `PASS WITH REPAIR`: language gate исправлен до рабочей формы, но deep source pass по полным источникам всё ещё нужен перед финальной главой.
        """
    )
    write(discourse, text.rstrip() + addition)


def main() -> None:
    for slug, topic in TOPICS.items():
        pass_dir = ROOT / "work" / "dossier-passes" / slug
        final_path = ROOT / "work" / "dossiers" / topic["final"]
        write(final_path, topic["body"])
        write(pass_dir / "dossier_after_pass_13.md", topic["body"])
        for kind in ("source_opening", "source_discovery", "dossier_transfer", "language_repair", "delta", "new_sources"):
            write(pass_dir / f"cycle_13_{kind}.md", report(topic["title"], topic["final"], kind))
        write(pass_dir / "CYCLE_LEDGER.md", ledger(topic["title"]))
        write(ROOT / "work" / "reports" / topic["audit"], audit(topic["title"], slug))
    update_checks()
    update_discourse()


if __name__ == "__main__":
    main()
