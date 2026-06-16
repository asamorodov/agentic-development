# 07 — добор по главным source families главы VIII

Цель этого прохода — добрать фактуру, которая пригодится для основной главы: команды, артефакты, статусы, ограничения, переходы, сбои и рабочие детали. Это ещё не глава и не финальный порядок изложения.

## 1. A5 / C2 / B3: внутренняя теоретическая ось

### 1.1. A5: процесс интересен только там, где удерживает состояние работы

Фрагмент A5 даёт главный фильтр для главы. Процесс нельзя описывать как набор фаз, названий ролей и красивых папок. Он важен там, где берёт на себя рабочую нагрузку: помогает остановить опасный шаг, восстановить контекст после разрыва, передать работу другому агенту или человеку, проверить доказательства и изменить допустимое следующее действие.

Фактура, которую нужно сохранить:

- GSD, BMAD, PWG и Gas Town не являются ступенями одной лестницы зрелости. Они отвечают на разные разрывы.
- GSD отвечает на вопрос: что должно пережить следующую сессию?
- BMAD отвечает на вопрос: кто производит какой контекст до реализации?
- PWG отвечает на вопрос: какая единица работы может быть остановлена, передана, заблокирована и восстановлена?
- Gas Town отвечает на более тяжёлый вопрос: как организовать множество таких работ в среде многих агентов.
- Процесс становится артефактом, если по нему можно продолжить работу без автора, остановить опасный шаг, восстановить утраченный контекст, проверить evidence или передать рабочий объект.
- Имитация процесса начинается там, где роль имеет название, но не имеет выхода, адресата и права блокировки; документ существует, но не имеет потребителя; checkpoint объявлен, но не останавливает движение.

Для основной главы это значит: нельзя писать «процесс нужен, потому что иначе хаос». Нужно писать точнее: процесс нужен, когда он отвечает за выбор следующего режима и оставляет артефакт, который этот выбор меняет.

### 1.2. C2: процесс задаёт ход, PWG удерживает продолжимость

C2 даёт самую близкую к VIII формулу. GSD и BMAD могут производить состояния для PWG, но не становятся PWG. Они задают ритм, роль, фазу и форму вывода. PWG должен удержать рабочие последствия: готовность, блокеры, владение, evidence, handoff, последнюю валидную границу, открытые решения и разрешённый следующий шаг.

Фактура, которую нужно сохранить:

- Если профиль задаёт фазу `plan`, он должен оставить выход, который следующий шаг обязан прочитать.
- Если профиль вводит роль architect, PM, developer или QA, вывод этой роли должен иметь адресата и последствия.
- `CONTEXT.md` полезен только когда решения реально переходят в `PLAN.md` и могут быть проверены.
- `PLAN.md` задаёт ограниченную единицу работы, открытые зависимости и критерии приёмки; список шагов сам по себе недостаточен.
- Story file даёт dev agent технические ограничения, прошлую информацию и условия завершения.
- Approval имеет вес только когда закрывает явную точку ожидания.
- Gate работает только когда движение останавливается до решения человека, теста, ревью или другого внешнего события.

Для основной главы важно развести два уровня. Процессный профиль говорит: «сейчас обсуждение», «сейчас план», «сейчас исполнение», «сейчас расследование», «сейчас correct-course». PWG говорит: «этот выход относится к такому-то узлу, имеет такого-то владельца, такую-то свежесть, такие блокировки и такие evidence». Без PWG процесс может создавать документы, но не всегда удерживает продолжимость. Без процессного профиля PWG может удерживать состояние, но не всегда выбрать правильный режим входа.

### 1.3. B3 / Gas Town boundary: когда процесс превращается в операционную среду

B3 и Gas Town нужны как верхняя граница. Они не должны перетянуть главу, но дают важный контраст: отдельный процессный профиль ещё не равен среде многих агентов.

Фактура, которую нужно сохранить:

- В Gas Town работа становится объектом, а не просто темой разговора.
- Есть два уровня состояния: coordination state и implementation state. Один держит очереди, владение, handoffs, gates; другой живёт в рабочем дереве, коммитах, тестах, локальном контексте.
- Роли в Gas Town — функции жизненного цикла: кто принимает работу, кто исследует, кто делает, кто проверяет, кто замечает застревание, кто убирает мусор.
- Очередь и обратное давление важны, когда работ много: нельзя просто породить больше агентов и надеяться, что они не начнут конфликтовать.
- `prime`, `gate`, handoff, routing, service work и наблюдаемость показывают, что восстановление и координация должны быть частью среды, а не только сессии.

Для основной главы это граница: VIII объясняет, как выбрать способ продолжения отдельной линии работы; X будет объяснять, как организовать множество линий, ролей, очередей и рабочих пространств.

## 2. Open GSD / GSD: фактура для процессного профиля восстановления

### 2.1. Основная функция GSD в главе

GSD нужно читать как профиль восстановления длинной агентской работы. Его предмет не просто `.planning/` и не просто command set. Он отвечает на разрыв: длинная агентская сессия теряет ранние решения, контекст становится шумным, новый агент не понимает, где остановились, а завершение легко объявляется без достаточной проверки.

### 2.2. Фазовый цикл

Внешние документы и локальный Атлас сходятся на цикле:

```text
Discuss → UI design when needed → Plan → Execute → Verify → Ship
```

Для главы важны не названия фаз, а их рабочие последствия.

- Discuss должен вывести решения из разговора в контекст фазы. Если решения не записаны, planner будет угадывать.
- UI design включается там, где неопределённость интерфейса нельзя безопасно оставить исполнителю.
- Plan должен собрать исполнимые задачи, критерии успеха, зависимости, команды проверки и stop points.
- Execute должен получить ограниченный план, выполнить атомарную работу, записать summary, остановиться на контрольной точке или коммитить результат.
- Verify должен сверить цель, требования, решения, план и наблюдаемое поведение.
- Ship не должен быть просто «код написан»: нужен PR body, summary, evidence, status update и, если требуется, UAT.

### 2.3. Файлы состояния и их рабочие роли

GSD даёт много конкретики, которую можно использовать как материал главы:

- `PROJECT.md` — источник правды и правила эволюции проекта; каждый агент должен читать его первым.
- `REQUIREMENTS.md` — требования, их tiers и traceability chain.
- `ROADMAP.md` — фазовый маршрут, который нельзя просто заменить текущей фантазией агента.
- `STATE.md` — текущая позиция, фаза, active decisions, blockers, metrics, recovery, complete/pending plans.
- `CONTEXT.md` — решения и rationale из обсуждения; его должны читать planner, plan-checker, verifier.
- `PLAN-*.md` — задачи, acceptance criteria, read_first, must_haves, dependency, checks.
- `SUMMARY-*.md` — что сделал executor и что нужно будущему планировщику или следующему шагу.
- `VERIFICATION-*.md` — PASS/FAIL evidence, команды, результаты, причины провала.
- `UAT-*.md` — manual acceptance testing и человеческое подтверждение там, где автоматических тестов недостаточно.
- `HANDOFF.json` / `.continue-here.md` — возобновление после разрыва.

Главная деталь: файл важен только если следующий профиль его потребляет. `PLAN.md`, который никто не читает; `STATE.md`, который не обновляется; `VERIFICATION.md`, который не блокирует ship, — это имитация состояния.

### 2.4. Свежие агентские контексты и роли

GSD показывает, что роль — это не «персона». Planner, plan-checker, executor, verifier and code-reviewer должны иметь разные входы, разные права и разные выходы.

Фактура:

- specialist agent запускается со свежим контекстом;
- ему передаются нужные артефакты, а не вся история разговора;
- planner создаёт plans;
- plan-checker проверяет coverage, atomicity, dependencies, file scope, verification commands, context fit, gaps and context budget;
- executor читает конкретный `PLAN.md`, выполняет задачу, пишет `SUMMARY`, делает atomic commit or stops;
- verifier пишет `VERIFICATION` with PASS/FAIL evidence;
- read-only roles не должны иметь Edit access;
- researchers can search/read but not write code;
- executor — единственная роль с правом менять код, если такая политика задана.

Для главы это надо подать как пример protected role profile. Роль задаёт не стиль ответа, а допустимую операцию.

### 2.5. Проверка и право завершения

GSD даёт материал для темы ложного завершения. Готовность должна быть локальной и проверяемой:

- план может быть `NEEDS_REVISION` или blocked by missing input;
- UAT failure создаёт fix plan;
- verification должен дать PASS/FAIL/CONCERNS-like evidence, а не просто красивую сводку;
- ship создаёт PR body с summary, changes, requirements, verification and key decisions;
- `STATE.md` обновляется после поставки или после перехода.

В основной главе это можно связать с billing/API: compatibility suite не зелёная — значит story не может стать done, даже если executor считает код завершённым.

### 2.6. Сбои GSD и ограничения

Нужно не романтизировать GSD. Из локального Атласа и внешних документов вытекают рабочие риски:

- если команда создаёт `.planning/`, но артефакты не потребляются, процесс становится архивом;
- если fresh contexts запускаются без нужных входов, они теряют смысл;
- если autonomous mode не имеет stop rules and human checkpoints, риск просто скрывается;
- если задача мала, полный фазовый цикл может стать overhead;
- если GSD начинает имитировать PWG через scattered files, но не держит явные dependencies, owners, blockers and evidence, он не заменяет долговечный граф работы.

## 3. BMAD: фактура для фазовой передачи артефактов и смены режима

### 3.1. Основная функция BMAD в главе

BMAD нужно читать как профиль передачи контекста через роли, фазы и документы. Он отвечает на другой разрыв: модель легко смешивает product judgment, architecture judgment, implementation and review в одном потоке. BMAD пытается разнести эти суждения по артефактам и workflow.

### 3.2. Фазы и workflow map

Фактура для основной главы:

- Analysis phase: problem exploration, research, product brief, brainstorming.
- Planning phase: PRD, UX where needed, product decisions.
- Solutioning phase: architecture, epics/stories, implementation readiness check.
- Implementation phase: sprint planning, create story, dev story, code review, correct-course, sprint status, retrospective, investigate.
- Quick Flow skips phases 1–3 for small, well-understood work and uses `bmad-quick-dev`.
- Full BMad Method / Enterprise uses heavier planning and solutioning.
- Each workflow can be run through skill or via agent menu; fresh chat per workflow is recommended.

В главе это можно свернуть до различения: BMAD не просто говорит «сначала планируй». Он создаёт документы, которые становятся входами следующего режима.

### 3.3. `bmad-help` как next-action router

Текущие docs сильнее подчёркивают `bmad-help`, чем локальные черновики. Это стоит использовать.

Фактура:

- `bmad-help` inspects project state;
- detects completed artifacts;
- recommends the next step;
- knows installed modules and workflows;
- runs automatically at the end of every workflow according to current getting-started docs;
- can answer “what should I do next?” or “I’m stuck on workflow X”.

Для главы это хороший пример: protected process profile может иметь интерфейс маршрутизации. Но в основном тексте надо не рекламировать `bmad-help`, а показать принцип: следующий режим должен выбираться по состоянию проекта and available artifacts, not by agent inertia.

### 3.4. `bmad-spec`, PRD, architecture and story chain

Фактура:

- `bmad-spec` creates `SPEC.md` with Why, Capabilities, Constraints, Non-goals and Success signal;
- `.decision-log.md` tracks decisions so continuation and later modifications have memory;
- PRD captures requirements and can be created, updated or validated;
- architecture makes technical decisions explicit, including ADR-like material;
- epics/stories are created after architecture in current v6 flow, because architecture decisions affect how work is broken down;
- implementation readiness check can return PASS / CONCERNS / FAIL;
- story file is the focused context for implementation.

В основной главе это можно использовать как цепочку: intent becomes SPEC/PRD; PRD becomes architecture; architecture plus PRD becomes epics/stories; story becomes dev input; review and sprint status update back into process state.

### 3.5. `sprint-status.yaml` and story cycle

Фактура:

- `bmad-sprint-planning` creates `sprint-status.yaml`;
- story cycle repeats: `bmad-create-story` → `bmad-dev-story` → `bmad-code-review`;
- retrospective follows epic completion;
- `bmad-create-story` reads `sprint-status.yaml` and finds the first backlog story in order;
- story statuses in local materials include `backlog`, `ready-for-dev`, `in-progress`, `review`, `done`;
- if no backlog story is found, the workflow can halt and recommend sprint refresh, correct-course or retrospective.

Для billing/API пример: один status может route to story creation, another to dev-story, another to retrospective or correct-course. Status is valuable only if it changes action.

### 3.6. `bmad-create-story` as context engine

Внешний `SKILL.md` даёт очень сильную формулировку: workflow is not supposed to copy from epics, but to create a comprehensive optimized story file for dev agent. It lists concrete LLM mistakes to prevent.

Фактура:

- prevent reinventing wheels;
- wrong libraries;
- wrong file locations;
- breaking regressions;
- ignoring UX;
- vague implementations;
- lying about completion;
- not learning from past work;
- use subprocesses/subagents when available;
- save questions for the end, after complete analysis;
- zero user intervention except initial selection or missing docs;
- load PRD, architecture, UX and epics selectively;
- read full `sprint-status.yaml` in order.

Для основной главы это отличный материал. Story file — не маленькая задача, а адаптер между широким planning context и узким implementation context.

### 3.7. `bmad-dev-story` and implementation discipline

Из локального C2 и Атласа:

- dev-story фиксирует `baseline_commit`;
- обновляет только разрешённые области story file;
- должен продолжать точную последовательность до завершения, если нет HALT condition or user instruction;
- implementation не должна самовольно менять scope, requirements or acceptance criteria;
- статус story должен быть связан с review and manual update, not only agent declaration.

В главе это можно использовать как пример: режим execution не является «делай что хочешь в коде». Он ограничен story contract and stop conditions.

### 3.8. `bmad-correct-course` as recovery profile

Фактура из external source and atlas:

- trigger: significant change during sprint execution;
- goal: analyze impact across all project artifacts and produce Sprint Change Proposal;
- input files: PRD, Epics, Architecture, UX Design, Spec, Document Project;
- PRD and Epics are essential; Architecture/UX/Spec optional but loaded if available;
- workflow asks for change trigger and mode preference: incremental or batch;
- systematic checklist records Done / N/A / Action-needed;
- proposals show old → new text for story changes;
- PRD changes include impact on MVP scope;
- architecture changes include affected components and ripple effects;
- final proposal includes Issue Summary, Impact Analysis, Recommended Approach, Detailed Change Proposals;
- possible path: Direct Adjustment, Potential Rollback, MVP Review.

Это главный пример смены режима. Если billing/API обнаружил, что старый план ломает контракт, агент не должен продолжать dev-story. Он должен перейти в correct-course и вернуть изменение в planning artifacts.

### 3.9. Brownfield / established projects

Локальный Атлас содержит больше фактуры, чем внешний P04 успел включить. Это стоит перенести в главу, если будет место.

Фактура:

- Established Projects require cleaning completed old artifacts before starting;
- create/validate `project-context.md`;
- run `bmad-document-project` when needed;
- `project-context.md` stores implementation rules: technology stack, versions, critical project patterns, constraints, conventions;
- implementation workflows load `project-context.md` if it exists;
- `bmad-document-project` can resume, restart, full rescan, deep-dive and archive old scan state;
- `project-scan-report.json` has timestamp, current_step, completed_steps, generated outputs and observations;
- `index.md` is a map for future agents;
- Quick Scan, Deep Scan, Exhaustive Scan and Deep Dive have different evidence levels;
- deep-dive forbids sampling, guessing and relying solely on tooling output;
- generated docs can include project-overview, source-tree-analysis, architecture, component-inventory, development-guide, deployment-guide, contribution-guide, api-contracts, data-models, integration-architecture, project-parts and index.

Для основной главы это полезно как brownfield contrast: old codebase требует не execution, а knowledge creation profile. Но не стоит делать из этого отдельную главу о BMAD document-project; достаточно использовать на billing/API как вариант “сначала сделать старый API читаемым для агента”.

### 3.10. `bmad-investigate` and retrospective

Фактура:

- `bmad-investigate` accepts issue id, log file, diagnostic archive, error message, code area, description or existing investigation file;
- old investigation can be resumed;
- output is investigation file in implementation artifacts;
- finding grades: Confirmed, Deduced, Hypothesized;
- Confirmed requires direct evidence such as path:line, log timestamp or commit hash;
- Deduced requires reasoning chain from confirmed evidence;
- Hypothesized must say what would confirm or refute;
- final confidence: High / Medium / Low based on evidence and reproducibility;
- investigation should not silently turn into fix; after diagnostic output it may route to quick-dev, correct-course, create-story or code-review;
- retrospective reads story records, review feedback, testing notes, technical debt, previous retrospective and next epic;
- retrospective should turn lessons into future process changes, not just a report.

Для главы это важная точка: investigation is a role profile distinct from fixing. It prevents premature repair.

### 3.11. BMAD failure modes

Нужно сохранить критичность:

- roles can become persona theater if outputs do not govern next actions;
- `sprint-status.yaml` can say done without sufficient evidence if status transitions are not tied to review and manual decision;
- `project-context.md` can become stale and falsely authoritative;
- old PRDs/stories in established project can mislead agent;
- correct-course can itself create source-of-truth problems if it modifies already completed stories without clear immutability rules;
- file-system-based skills may not fit large organizations without integration into real work-management system;
- skills and docs can drift, so chapter should cite current primary docs and avoid overconfident claims about exact current CLI surface unless sourced.

## 4. Gas Town / Beads: boundary facts, not main body

### 4.1. What to take

From Gas Town / Beads, VIII should take only boundary facts:

- work should be object, not chat topic;
- Beads issues have statuses, priorities, labels and dependencies;
- gates can represent asynchronous waiting conditions;
- `bd prime` restores compact context;
- multi-agent coordination needs claiming, handoff, reservation, blockers and ready queues;
- Gas Town has town/rig distinction: shared coordination layer versus execution workspaces;
- service roles like watchdog/cleanup/observer show that at scale process becomes operations.

### 4.2. What not to take

Do not unfold Mayor, Crew, Polecats, Convoys, Refinery, Witness, Deacon and Dogs in detail unless a single example is needed. Otherwise VIII will become chapter X. For VIII enough:

> Когда процессных профилей and PWG-узлов становится много, возникает отдельная задача операционной среды. Это следующий слой.

## 5. Story anchors: практические носители процессных профилей

### 5.1. Jesse Vincent

Jesse Vincent is the best story anchor for process exoskeleton.

Relevant facts:

- early workflow separated task discussion from implementation;
- plan becomes a portable prompt for a future agent;
- architecture session and implementation session are different contexts;
- context must be cleaned, not just accumulated;
- verification comments should not automatically become tasks;
- adversarial review with fresh context improves quality;
- Superpowers turn manual practices into skills;
- skill must be tested under pressure, not in calm quiz;
- following process matters more than understanding process verbally;
- checkers can overreach if they inherit too much session context;
- spec-review and code-review answer different questions: did we build what we planned, and is it well built?;
- rules can be rationalized, gates are harder to bypass;
- deleting tests story shows how formal pressure can destroy the meaning of a process;
- hooks can protect flow from unnecessary stops;
- controller/session-driver shows persistent worker contexts and a manager-like coordination role.

How to use in VIII:

- not as biography;
- not as full history of Superpowers;
- use to show that process profile needs real behavioral gates;
- especially useful for role boundary: checker should receive only spec/code/criteria, not entire session noise;
- use deletion-of-tests story as warning: a process rule can be optimized against unless it specifies what must not be sacrificed.

### 5.2. HumanLayer

HumanLayer should be secondary but useful:

- research → plan → implement is a contour for preserving meaning;
- human attention should be closer to where the important delta is born;
- artifacts are for team alignment, not only model context;
- `CLAUDE.md` / `AGENTS.md` should be short стартовый контекст, not encyclopedia;
- gradual disclosure: point to sources instead of copying them all;
- conditional blocks should activate at right moment;
- subagents are firewall/context compaction, not a team of magical specialists;
- hooks manage flow and return signal;
- stop hook can return failed checks back to work;
- feedback loop should send signal, not noise.

How to use in VIII:

- show that process profile protects transition from research to plan to implementation;
- use subagents/firewall idea to support role-specific context;
- keep detailed tool/hook discussion for IX.

### 5.3. Matt Pocock

Matt Pocock is important for smaller process units: skills as procedural memory.

Relevant facts:

- `/grill-me` stops premature understanding;
- `/grill-with-docs` uses domain docs to ask concrete questions and catch terminology collisions;
- `/prototype` replaces talk with small runnable test when behavior is uncertain;
- `/to-prd` compresses conversation into portable intention;
- `/to-issues` cuts PRD into vertical issues;
- agent brief makes issue suitable for an agent;
- `/triage` makes backlog ready before implementation;
- `/tdd` forces red test before implementation;
- `/handoff` transfers session state without dragging old noise;
- Ralph loop needs small steps, progress file, completion marker and observable output;
- `/diagnose` asks for pass/fail signal before fixing;
- `git-guardrails` protects Git history;
- status line and `caveman` are observability/communication controls.

How to use in VIII:

- not as list of cool skills;
- use as evidence that protected process profile can be small and local;
- each skill answers one recurring wrong-entry failure: agent acts before asking, codes before test, implements before triage, continues after context became dirty, fixes before diagnosing.

### 5.4. Shopify Roast

Use lightly. It shows executable workflow steps and replayable evaluation. It is helpful to contrast process profile with workflow runtime. But too much detail pulls chapter toward IX.

Potential use:

- workflow step can be executable and observable;
- process has value when it generates replayable evidence;
- keep as bridge to execution/runtime.

### 5.5. Mae Capozzi

Use as bridge to team process wrapper:

- work happens through Linear/Figma/platform checks and team coordination;
- agentic process is constrained by the organization’s existing work surfaces;
- useful as a reminder that protected process profile ultimately connects to human team practices.

But Mae belongs closer to organizational layer and should not become main evidence for VIII.

## 6. Material to add to the main chapter if space permits

1. A small table of wrong-entry failures:

| Work state says | Wrong entry | Correct process profile |
|---|---|---|
| story exists but unclear acceptance criteria | implementation | story creation / clarification |
| legacy behavior unknown | implementation | brownfield investigation |
| plan contradicted by new evidence | continue old plan | correct-course |
| code complete but evidence weak | ship | verification / UAT |
| issue in backlog but not ready | dev-story | triage / agent brief |
| test failure unexplained | fix immediately | diagnose / investigate |
| decision changes scope | agent decides | human checkpoint |

2. A distinction between role profile and persona:

```text
Persona: how the model speaks.
Role profile: what it may read, what it may change, what it must produce, what stops it, who consumes the result.
```

3. A distinction between process profile and runtime:

```text
Process profile: what kind of work is allowed now.
Execution environment: where and with what rights that work happens.
```

4. A distinction between process profile and PWG:

```text
Process profile chooses and structures action.
PWG preserves action consequences as durable work state.
```

5. A strong critical criterion:

```text
If the process artifact does not block, allow, reroute, verify or restore the next action, it is not a protected process profile.
```

## 7. Gaps after this pass

1. Need exact source link placement in the main chapter. The source report already lists current Open GSD and BMAD URLs; main text must add links immediately when using specific facts.

2. If the main chapter expands `bmad-investigate`, open the current primary docs/skill again and cite them directly.

3. If the main chapter expands brownfield/document-project, verify current official established-project docs. Local atlas has strong detail but the main chapter should not cite atlas as public source.

4. If the main chapter mentions GSD tool permissions and policy, keep it minimal or defer to IX.

5. Avoid duplicating full A5/C2. VIII should use the material to write a new chapter around wrong-entry failure, not copy the fragment structure.
