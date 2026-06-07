# Consolidated plan patch after Stage 0.5–0.9

Дата: 2026-06-07  
Режим: кумулятивный архив-оверлей.  
Статус: проект изменения `work/approved-ai-sdlc-plan.md`; сам approved plan этим файлом не меняется.

Этот документ сводит Stage 0.5–0.9 в один patch к утверждённой архитектуре. Он нужен потому, что отдельные отчёты уже начали расходиться по разным слоям: артефакты SDLC, агентские методологии, хвост жизненного цикла, безопасность, трассируемость, supply chain, наблюдаемость, review capacity, платформенные поверхности. Если переносить их в план по одному, теория снова рискует стать каталогом правильных тем.

Главный вывод: верхняя архитектура сохраняется. Новая рамка по-прежнему:

```text
Агентская разработка и AI-driven SDLC:
как меняется жизненный цикл программного изменения
```

Рамка по-прежнему понимается как жизненный цикл программного изменения, а не как корпоративная таблица фаз.

Но к утверждённому плану нужно добавить один интегрирующий слой:

```text
AI-driven SDLC — это управляемое прохождение программного изменения через связанные артефакты, проверяемые среды, права завершения и петли обратной связи.
```

Эта формула не заменяет прежний план. Она нужна как защита от распада найденных материалов на неоднородную коллекцию.

## 1. Что не меняется

### 1.1. Master architecture остаётся AI-driven SDLC

Не нужно возвращаться к “карте течений” как верхней структуре. Она остаётся источниковым и аналитическим слоем.

### 1.2. SPDD остаётся отдельной частью

Часть IV остаётся deep case: SPDD как спецификационный жизненный цикл. Нельзя снова сжать SPDD в подраздел Части III.

### 1.3. Spec Kit / Kiro / TDAD / Constitutional SDD остаются глубокой спецификационной зоной

Они не превращаются в короткие контрасты. Они показывают соседние способы превратить намерение в управляемую инфраструктуру.

### 1.4. Gas Town остаётся отдельным deep case

Часть IX остаётся deep case: организационно-операционный жизненный цикл. Gas Town не должен снова стать одним обзорным подразделом.

### 1.5. Baseline restore rule остаётся жёстким

Для SPDD и Gas Town начальная точка — старый сайт целиком, а не expanded quarry.

### 1.6. Expanded quarry остаётся quarry

Новая expanded-версия не становится main draft. Из неё берутся факты, ссылки и удачные фрагменты, но не каталожная форма.

## 2. Главный patch: добавить слой связанных артефактов

В текущем approved plan уже есть стадии жизненного цикла. Но после Stage 0.5–0.9 стало ясно, что нужно явно сказать: SDLC держится не только стадиями и кейсами, но и артефактами, которые переносят смысл между стадиями.

Добавить в раздел “0. Зафиксированные решения” новый пункт:

```text
0.9. SDLC artifacts are first-class objects

В финальном тексте нужно отслеживать не только стадии жизненного цикла и кейсы, но и артефакты, которые несут намерение, контекст, решение, проверку, права владения, выпуск и сопровождение. Артефакт попадает в основную теорию не потому, что он “важен в SDLC”, а потому что переносит изменение через одну из границ жизненного цикла: от намерения к контексту, от контекста к исполнению, от исполнения к свидетельствам, от свидетельств к ревью, от ревью к праву завершения, от завершения к сопровождению и обучению среды.
```

В финальном русском тексте эту мысль лучше формулировать не как список, а как рабочий тезис:

```text
Агентская разработка меняет не только исполнителя работы. Она требует связать намерение, контекст, решение, среду, проверку, владельца и сопровождение через артефакты, которые можно читать, проверять, обновлять и использовать в следующем цикле.
```

## 3. Patch по частям

## Введение

Добавить предупреждение: AI-driven SDLC не измеряется количеством кода, созданного агентом. Метрики активности, рост числа PR или ускорение локального coding не равны росту delivered value.

Материалы:

- DORA / Bain;
- SPACE / DevEx;
- исследования о supervisory engineering and AI-assisted productivity perception.

Функция: сразу защитить текст от второй ошибки после “prompt-centric” картины — от “activity-centric” картины.

## Часть I. Единица анализа: программное изменение, а не prompt

Добавить правило отбора артефактов. Часть I должна объяснить, почему в документ входят не все найденные важные вещи, а только те, что работают на прохождение изменения через жизненный цикл.

Добавить различение:

```text
prompt
plan
specification
ADR
RFC / design proposal
handoff
traceability link
evidence package
ownership artifact
release artifact
```

Но не раскрывать всё подробно. Часть I должна дать карту, а не каталог.

## Часть II. Реальная агентская сессия

Добавить осторожно: session trace is not enough. Трасса сессии показывает prompts, tool calls, corrections and generated code survival, но не заменяет долгоживущие артефакты: decision records, contracts, release state, ownership, SBOM, traceability.

Это усилит переход к Части III.

## Часть III. Намерение: почему prompt слишком слаб как единица управления

Добавить блок “разные артефакты намерения и решения”:

- `prompt` — одноразовый вход или локальная инструкция;
- `plan` — путь выполнения;
- `specification` — целевое поведение, ограничения and acceptance expectations;
- `ADR` — принятое решение, причины, альтернативы, последствия;
- `RFC/design proposal` — поверхность обсуждения до решения;
- `contract` — граница интеграции или данных;
- `traceability link` — связь намерения с реализацией и проверкой.

Задача: не смешивать всё в один “документальный слой”.

## Часть IV. SPDD

Не менять место и глубину. Но при writing помнить: SPDD силён потому, что создаёт связанный lifecycle намерения, а не просто потому, что “там есть prompt as artifact”. В SPDD нужно явно показать, как story, analysis, Canvas, generation, tests, review, prompt update and sync создают замкнутую цепочку.

## Часть V. Соседние спецификационные режимы

Добавить к Spec Kit / Kiro / TDAD / Constitutional SDD несколько связок:

- Spec Kit: portable/executable specification toolkit.
- Kiro: productized IDE surface for specifications and tasks.
- TDAD: behavior/tests and test-impact graph как мост к evidence.
- Constitutional SDD: security/governance constraints as specification layer.
- Contracts and traceability: не заменяют эти режимы, но показывают соседние forms of boundary/specification artifacts.

Не добавлять сюда GSD/BMAD как ещё две “спецификации”. Их место — process/framework layer.

## Часть VI. Контекст и рабочее состояние: проект как интерфейс агента

Добавить несколько новых элементов:

1. `research.md`, `plan.md`, handoff, progress log and ADR as project memory.
2. Codebase readiness: тесты, CI, инструкции, контекстные файлы, метрики, наблюдаемость and feedback loops.
3. Context file quality/debt: `AGENTS.md`, Cursor rules, Agent READMEs and similar files can help or harm.
4. Воспроизводимая среда: dev container, setup commands, test runners.
5. Каталог/платформа: catalog of components, APIs, owners, systems and lifecycle metadata as a surface that helps humans and agents navigate project state.

Это не должно стать отдельной энциклопедией platform engineering. Функция части: показать, что проект сам становится интерфейсом агента.

## Часть VII. Делегирование: выбор режима работы, а не выбор инструмента

Добавить subsection:

```text
Agentic development frameworks: process as installed artifact
```

Раскрыть средне-глубоко:

- GSD / Open GSD — лёгкий процесс externalized state and context engineering.
- BMAD — role-based agile AI-driven methodology.
- OpenSpec / Agent Spec / AgentSPEX — process/workflow specification and portability, коротко или средне.
- Reversa — possible medium case for recovering operational specs from legacy code.

Решение о deep anchor для GSD/BMAD не принимать автоматически. Нужны dossiers and human gate.

## Часть VIII. Исполнение: среда агента, harness, tools, permissions

Добавить:

1. Воспроизводимая среда выполнения.
2. Агентская трасса: prompts, tool calls, state changes, command outputs, environment effects.
3. Policy-as-code as executable constraint layer.
4. Secret scanning, credential inventory and sensitive-context boundary.
5. MCP/tool boundary and permissions as security/provenance artifacts.
6. Agent workflow specification as process artifact, but not deep case.

Функция: показать, что execution environment is not only tool access. It is controlled, observable, reproducible and policy-bounded environment.

## Часть IX. Gas Town

Не менять место. Но при writing Gas Town нужно связать с artifact graph:

- Beads as task memory and control plane.
- Mayor as visibility/control surface.
- roles/identities as organizational artifacts.
- hooks/molecules/wisps as workflow continuity.
- service agents as self-maintenance.

Gas Town должен показать, как артефакты и роли становятся организационной средой, а не просто набором агентов.

## Часть X. Свидетельства, тесты, ревью и benchmark validity

Добавить evidence package taxonomy:

- test outputs;
- CI evidence;
- benchmark results;
- contract tests;
- traceability links;
- review comments;
- PR description;
- agent trace / tool-call log;
- policy check results;
- security review outputs;
- SBOM/provenance evidence where relevant.

Добавить отдельную мысль: evidence is not one artifact. Evidence package depends on change type.

## Часть XI. Завершение, governance и внешний контур

Добавить concrete ownership artifacts:

- CODEOWNERS;
- ownership map;
- review routing;
- escalation path;
- protected branch / required review;
- release authority;
- audit/provenance record.

Усилить формулу:

```text
право исполнять ≠ обязанность ревьюить ≠ право сливать ≠ право выпускать
```

Open-source policy cluster остаётся сильным boundary anchor, но теперь получает более конкретный artifact layer.

## Часть XII. Хвост lifecycle: сопровождение, долг и обучение среды

Добавить controlled artifact cluster:

- release plan;
- migration plan;
- rollback plan;
- runbook;
- incident report;
- postmortem;
- dependency policy;
- deprecation policy;
- changelog / release notes;
- SBOM / dependency and license inventory;
- secret rotation / credential follow-up;
- observability debt;
- stale ADR / decision debt;
- context file cleanup.

Не делать Part XII слишком большой. Её функция — замкнуть жизненный цикл and show feedback to earlier artifacts.

## Заключение

Усилить мысль: итоговая карта — не список источников, а карта выбора режима изменения. В зависимости от риска, обратимости, контекста, прав завершения and lifecycle tail выбирается depth of artifacts.

## 4. Новые dossiers / notes перед drafting

Перед writing нужны не все большие dossiers, а разные типы заметок:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_DOSSIER.md
work/dossiers/BMAD_DOSSIER.md
work/dossiers/REVERSA_NOTE.md
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_NOTE.md
work/dossiers/AGENT_WORKFLOW_SPECIFICATION_NOTE.md
work/dossiers/DELIVERY_SAFETY_AND_ROLLBACK_NOTE.md
work/dossiers/DECISION_ENFORCEMENT_NOTE.md
work/dossiers/TRACEABILITY_AND_REQUIREMENTS_LINKS_NOTE.md
work/dossiers/SBOM_AND_DEPENDENCY_POLICY_NOTE.md
work/dossiers/SECRETS_AND_SENSITIVE_CONTEXT_BOUNDARY_NOTE.md
work/dossiers/AGENT_OBSERVABILITY_AND_TRACES_NOTE.md
work/dossiers/HUMAN_REVIEW_CAPACITY_AND_DEVEX_NOTE.md
work/dossiers/POLICY_AS_CODE_NOTE.md
work/dossiers/REPRODUCIBLE_ENVIRONMENT_NOTE.md
work/dossiers/ARTIFACT_GRAPH_AND_PLATFORM_SURFACES_NOTE.md
```

Не все эти файлы должны быть одинакового размера. Некоторые должны быть короткими notes. Главная цель — не добавить объём, а не потерять роль артефакта перед writing.

## 5. Что уходит в source map or short mention

Short / source-map-only unless later promoted:

- OpenSpec / Agent Spec;
- AgentSPEX;
- Backstage / software catalog;
- OPA / policy-as-code tooling;
- SBOM tool ecosystem details;
- dev containers / Nix / Bazel / reproducible builds;
- ChainForge;
- promptware engineering beyond SPDD;
- value stream tooling;
- vendor/news posts;
- Spec Kitty until primary-source depth is stronger.

## 6. Human gates

Human approval required before:

1. Applying this patch to `work/approved-ai-sdlc-plan.md`.
2. Adding any new top-level part.
3. Promoting GSD/BMAD/Reversa/OpenSpec/AgentSPEX/Backstage/OPA to deep anchor.
4. Demoting SPDD, Gas Town or the deep specification cluster.
5. Expanding Part XII beyond a controlled tail.
6. Starting drafting before accepting/rejecting this consolidated patch.
7. Launching another broad source-search cycle.

## 7. Recommended next step

Stop broad source expansion now. Next step should be a human decision:

```text
accept / amend / reject consolidated patch
```

If accepted, update:

```text
work/approved-ai-sdlc-plan.md
work/decisions/PROPOSED_ADR-0007-sdlc-artifact-and-framework-coverage.md
work/discourse.md
```

Then create selected dossiers/notes and only after that start skeleton/drafting.

## Stage 0.12 addendum

После отдельного поиска по двум residual gaps consolidated patch должен включать ещё два named medium-high blocks:

1. **Architecture quality / fitness functions** — quality attribute scenarios, architecture constraints, fitness functions, architecture tests, architecture drift.
2. **Test data / test environments** — test data management, controlled test environments, service virtualization, test dependencies as code, oracle independence, generated tests/test data risks.

Эти блоки уточняют Part X as evidence package theory and connect to Parts III, VIII and XII. Они не создают новых top-level parts.
