# A3. Использование источников

Этот файл фиксирует первичные источники, которые использованы для черновика `A3_specification_methodologies_synthesis.md`. Внутренние досье и планы использовались как навигация, но не как цитируемые основания для утверждений основного фрагмента.

## SPDD / OpenSPDD

- [Martin Fowler / Thoughtworks: Structured Prompt Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — использован для тезиса о structured prompt как поддерживаемом, reviewable/reusable/governable delivery artifact; для REASONS Canvas; для workflow, где prompt и code должны синхронизироваться.
- [OpenSPDD REASONS Canvas template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) — использован для структуры Canvas и роли входного контекста `@file` / `@folder`.
- [OpenSPDD generate command](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) — использован для утверждения, что генерация должна опираться на Operations, Norms и Safeguards, а не импровизировать поверх свободного запроса.
- [OpenSPDD API test command](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md), [code review command](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md), [sync command](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) — использованы для механизма evidence и prompt/code synchronization.

Ограничение: SPDD в черновике трактуется как метод управления смыслом делегирования, а не как универсальная замена всем lightweight режимам разработки.

## Spec Kit

- [Spec Kit documentation](https://github.github.com/spec-kit/) и [Quick Start](https://github.github.com/spec-kit/quickstart.html) — использованы для базовой и расширенной последовательности команд.
- [Spec-driven development](https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md) — использован для формулировки Spec Kit как specification-driven workflow, где артефакты переводят намерение в план и задачи.
- [Command templates](https://github.com/github/spec-kit/tree/main/templates/commands) — использованы как источник для ролей `constitution`, `specify`, `clarify`, `checklist`, `plan`, `tasks`, `analyze`, `implement`.
- [Workflows](https://github.github.com/spec-kit/reference/workflows.html) и [Integrations](https://github.github.com/spec-kit/reference/integrations.html) — использованы для утверждения о portable toolkit, workflow runs, checkpoints и adapter surface.

Ограничение: черновик не описывает все команды как инструкцию по использованию; он использует их только для оси “управление переводами между артефактами”.

## Kiro Specs

- [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) и [requirements-first workflow](https://kiro.dev/docs/specs/feature-specs/requirements-first/) — использованы для структуры `.kiro/specs/{spec-name}/`, requirements/design/tasks и approval gates.
- [Kiro Quick Plan](https://kiro.dev/docs/specs/quick-plan/) — использован для различения standard Feature Specs и one-pass generation без промежуточных gates.
- [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/) — использован для claim о поиске inconsistent, ambiguous, conflicting и missing requirements.
- [Correctness with property-based testing](https://kiro.dev/docs/specs/correctness/) — использован для claim о переводе natural-language specs в executable properties и об ограничении: это stronger evidence, not formal proof.
- [Steering](https://kiro.dev/docs/steering/) и [Chat context](https://kiro.dev/docs/chat/) — использовались как фоновое основание для роли IDE-local state, steering files и context providers; в основном тексте упомянуты коротко.

Ограничение: фрагмент не оценивает Kiro как продукт целиком; он рассматривает только функцию IDE surface в specification-layer.

## TDAD: две разные методологии

- [Test-Driven AI Agent Definition: Compiling Tool-Using Agents from Behavioral Specifications](https://arxiv.org/html/2603.08806v1) — использован для pipeline TestSmith / PromptSmith / MutationSmith, YAML behavioral specification, visible/hidden tests, mutation testing, spec evolution и compiled agent artifact.
- [tdad-paper-code repository](https://github.com/f-labs-io/tdad-paper-code) — использован как reference implementation anchor; в основном фрагменте не разбирается подробно.
- [TDAD: Test-Driven Agentic Development — Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis](https://arxiv.org/html/2603.17973v2) — использован для code–test dependency graph, `test_map.txt`, static text skill, experiment claim о TDD procedural instructions и regression reduction в указанной постановке.
- [tdad-skill](https://raw.githubusercontent.com/pepealonso95/tdad-skill/main/SKILL.md) — использован для runtime-инструкций: построить index при отсутствии `.tdad/test_map.txt`, искать impacted tests по changed files, запускать связанные тесты, добавлять regression test.

Ограничение: в черновике намеренно не смешиваются две TDAD. Одна компилирует поведение агента из behavioral specification, другая маршрутизирует проверки для изменения кода.

## Constitutional SDD

- [Constitutional Spec-Driven Development](https://arxiv.org/html/2602.02584v1) и [arXiv abstract](https://arxiv.org/abs/2602.02584) — использованы для определения Constitution, структуры principle, CWE mappings, enforcement levels, compliance traceability matrix и ограниченного статуса case study.
- [Reference banking constitution](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md) — использована для примеров non-negotiable rules: SQL injection, input validation, authentication/authorization, password hashing.
- [Reference feature spec](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/spec.md) — использован как подтверждение связи Constitution с feature specification; в основном тексте не раскрыт подробно.
- [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) — использован для claim о file:line traceability evidence.

Ограничение: заявленные quantitative results CSDD не вынесены в главный ход аргумента как обобщённое доказательство; они требуют явной привязки к одному case study.


## Источники, добавленные при усилении фактуры

- [OpenSPDD prompt update](https://raw.githubusercontent.com/gszhangwei/open-spdd/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) — добавлен для утверждения, что SPDD-update сохраняет REASONS-структуру, меняет только затронутые секции и проверяет cross-section consistency. Использован в абзаце о SPDD как living specification, а не one-way handoff.
- [OpenSPDD sync](https://raw.githubusercontent.com/gszhangwei/open-spdd/v0.4.9/internal/templates/data/core/spdd-sync.md) — добавлен для утверждения о reverse flow code → prompt, приоритетах секций и principle “structured prompt should reflect actual implementation”. Использован в SPDD-блоке.
- [OpenSPDD optional code review](https://raw.githubusercontent.com/gszhangwei/open-spdd/v0.4.9/internal/templates/data/optional/spdd-code-review.md) — добавлен для деталей о positive/negative/direction drift, implicit decisions, safeguard violations и review report как triage artifact. Использован в SPDD-блоке; заменяет ошибочную ссылку на core-path.
- [Spec Kit constitution command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md) — добавлен для semantic versioning, Sync Impact Report и propagation через dependent templates/commands. Использован в Spec Kit-блоке.
- [Spec Kit analyze command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md) — добавлен для read-only cross-artifact analysis и правила, что conflict with constitution MUST является critical. Использован в Spec Kit-блоке.
- [Kiro Steering](https://kiro.dev/docs/steering/) — добавлен для workspace/global steering, inclusion modes и file references. Использован в Kiro-блоке о routing of context.
- [Kiro Chat context providers](https://kiro.dev/docs/chat/) — добавлен для `#spec`, `#terminal`, `#git diff`, `#steering` и других context providers. Использован в Kiro-блоке о IDE surface.
- [Kiro Deep Spec Analysis](https://kiro.dev/blog/deep-spec-analysis/) — добавлен для refinement → auto-formalization → logical analysis и двухвариантных вопросов человеку. Использован в Kiro-блоке как пример того, что формальный анализ возвращает решение человеку.
- [Constitutional SDD lessons / limitations](https://arxiv.org/html/2602.02584v1) — повторно использован для деталей, которых не было в первом черновике: task-relevant selection 3–5 principles, constitutional documents as attack surface, boundedness by known vulnerability classes and threats to validity. Использован в CSDD-блоке.


## Дополнение по двум TDAD-линиям

- [TDAD A paper, methodology section](https://arxiv.org/html/2603.08806v1) — использован для формулы “specification is source, behavioral tests are intermediate representation, prompt/configuration is compiled artifact”; для YAML spec fields, test guidance, MFT/INV/DIR taxonomy, deterministic fixtures, structured `respond` tool, visible/hidden split и semantic mutation testing. Использован в TDAD A-блоке основного фрагмента.
- [TDAD A reference implementation README](https://raw.githubusercontent.com/f-labs-io/tdad-paper-code/main/README.md) — добавлен для artifact layout: specs, visible/hidden tests, mutation packs, agent artifacts, pipeline services `testsmith`, `compiler`, `evaluate`, `mutation`. Использован как подтверждение, что pipeline генерирует artifacts from spec alone и что shipped artifact — prompt/agent definition with regression suite.
- [TDAD B paper, system design and discussion](https://arxiv.org/html/2603.17973v2) — использован для явного разведения двух TDAD: agent behavior compliance vs agent-generated code patches; для code–test graph schema, static `test_map.txt`, 20-line skill, context over procedure, limitations по SWE-bench Verified / Python / sparse tests / monorepos.
- [tdad-skill raw SKILL.md](https://raw.githubusercontent.com/pepealonso95/tdad-skill/main/SKILL.md) — добавлен вместо GitHub-rendered страницы для точных runtime-инструкций: build `.tdad/test_map.txt`, `grep` по changed files, run impacted tests, add regression test, fallback when map missing.

Редакторское решение: в основном тексте не добавлялись все метрики и таблицы TDAD. Усилены только детали, которые разводят tests as behavioral specification и tests as regression steering surface.

## Осевой проход 7ae5d267a1

Новые внешние источники на этом шаге не добавлялись. Основной фрагмент был перестроен по пяти осям сравнения: центральный артефакт, человеческая точка остановки, тип проверки, порядок обновления артефакта и характерный сбой. Все фактические утверждения были перенесены из уже учтённых первичных источников выше.

Использование источников после перестройки:

- SPDD / OpenSPDD оставлены как источник фактуры о REASONS Canvas, `@file` / `@folder`, Operations / Norms / Safeguards, API-test, code-review, prompt-update и sync. В новом тексте они поддерживают оси “центральный артефакт”, “проверка относительно намерения” и “синхронизация prompt ↔ code после реализации”.
- Spec Kit оставлен как источник фактуры о `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`, `/speckit.constitution`, `/speckit.clarify`, `/speckit.checklist`, `/speckit.analyze`, Sync Impact Report, semantic versioning и конфликте с constitution как critical. В новом тексте он поддерживает ось “цепочка переводов между артефактами”.
- Kiro оставлен как источник фактуры о `.kiro/specs/{spec-name}/`, `requirements.md`, `design.md`, `tasks.md`, approval gates, Quick Plan, Analyze Requirements, Deep Spec Analysis, steering и context providers. В новом тексте он поддерживает ось “IDE-состояние как specification-layer”.
- TDAD A оставлена как источник фактуры о YAML behavioral specification, TestSmith, PromptSmith, MutationSmith, открытых/скрытых тестах, mutation testing, SURS и shipped agent artifact. В новом тексте она поддерживает ось “тесты как промежуточное представление поведения агента”.
- TDAD B оставлена как источник фактуры о code–test graph, `test_map.txt`, `tdad-skill`, impacted tests, regression test и limitations по неполным зависимостям. В новом тексте она поддерживает ось “тесты как карта регрессионного риска”.
- Constitutional SDD оставлена как источник фактуры о versioned Constitution, CWE mappings, enforcement levels, amendment procedures, compliance traceability matrix, task-relevant principle selection и Constitution как attack surface. В новом тексте она поддерживает ось “верхний слой непререкаемых ограничений”.

Редакторское решение: методологии больше не выстроены как последовательный каталог. Таблица в начале задаёт оси, а последующие абзацы раскрывают, как каждая методология стабилизирует намерение через свой объект управления. Внутренние досье снова использовались только как навигация и не стали citation targets.

## Source/depth pass 25011c0b10

Новые источники добавлены только там, где они усиливают уже написанную осевую композицию, а не расширяют список методологий.

- [OpenSPDD design philosophy](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/docs/design-philosophy.md) — добавлен как первичный источник для различения capability dimension и control dimension, а также для мотива negative space: сильная модель может лучше выводить соглашения проекта, но не имеет права самостоятельно выбирать бизнес- и архитектурные компромиссы среди нескольких допустимых решений. Использован в SPDD-абзаце как объяснение, почему управляемым объектом является смысл делегирования.
- [Spec Kit plan command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md) — добавлен для деталей `plan`-гейта: загрузка feature spec и `/memory/constitution.md`, заполнение Constitution Check, остановка при необоснованных нарушениях или unresolved clarifications, генерация `research.md`, `data-model.md`, `contracts/`, `quickstart.md`, обновление контекста агента.
- [Spec Kit plan template](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md) — добавлен для факта, что Constitution Check должен пройти до Phase 0 research и повторно провериться после Phase 1 design. Использован в Spec Kit-абзаце как уточнение человеческой точки остановки и проверки цепочки переводов.

Редакторское решение: источники про Claude/AGENTS.md, DocGuard и внешние практические гайды в основной фрагмент не добавлялись. Они полезны для будущих разделов о контекстных файлах и governance, но в A3 могли бы увести текст от текущей осевой задачи.


## Source/repair check 7b0bfcf401

Короткий план починки для этого прохода:

1. Проверить, не попали ли в основной фрагмент ссылки на внутренние досье, планы, отчёты или рабочие карты вместо публичных источников.
2. Проверить наиболее процедурные утверждения, которые могли прийти из внутренних файлов: OpenSPDD review/sync, Spec Kit `plan`, Kiro gates/Quick Plan, две линии TDAD и CSDD traceability.
3. Убрать остатки dossier-языка, где термин оставался без объяснения, особенно `SURS`.
4. Не расширять фрагмент новыми источниками; править только реальные дефекты.

Результат проверки:

- В основном фрагменте не найдено внутренних citation targets вида `work/`, `content/`, `protocols/`, `reports/` или относительных ссылок на рабочий пакет. Все 34 markdown-ссылки ведут на внешние публично читаемые источники.
- Новые источники в этом проходе не добавлялись. Использовались уже введённые первичные источники и документация: OpenSPDD templates/design notes, Spec Kit command templates и документация, Kiro Feature Specs/Quick Plan/Analyze Requirements/Deep Spec Analysis, две TDAD-статьи и их репозитории, CSDD paper и reference constitution/compliance files.
- Единственная правка фактуры в основном фрагменте — пояснить `SURS` как оценку регрессии при обновлении спецификации. Это не новый claim, а раскрытие уже использованной метрики TDAD A.
- Фрагмент не ссылается на story map, skeleton, writing plan или предыдущие отчёты как на источники. Эти документы остаются provenance/coordination layer, а не citation layer.

Осторожность перед публикацией:

- Ссылку OpenSPDD design philosophy на `main` лучше закрепить на commit или tag, если будет нужна воспроизводимая формулировка capability/control и negative space.
- Документация Kiro и Spec Kit может меняться; перед финальным выпуском нужен link/source freshness check, но текущий проход не нашёл необходимости заменять уже поставленные источники.


## Residual repair check 35d7693d33

План остаточной починки был ограничен редакционными дефектами после source/repair-pass: повтор в заключении, англо-русские generic labels в figure candidates и проверка, не появились ли новые сомнительные citation targets.

Что изменено:

- Основной фрагмент не получил новых ссылок и не потерял существующие источники; заключительный блок de-duplicated, чтобы не повторять карту выбора артефакта два раза подряд.
- Figure candidates отредактированы языково: переведены общие слова вроде `gate`, `evidence`, `maintenance tail`, `artifact translation chain`, `visual cue`, где они не являются именами источников.
- Source-specific имена и команды сохранены: REASONS Canvas, Feature Specs, Quick Plan, Analyze Requirements, Deep Spec Analysis, Constitution, TDAD, `test_map.txt`, `prompt/configuration`, `prompt/agent definition`.

Новые внешние источники не использовались. Проверка citation targets осталась прежней: основной фрагмент не ссылается на внутренние рабочие документы.
