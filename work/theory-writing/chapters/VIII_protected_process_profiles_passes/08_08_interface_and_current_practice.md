# 08 — техническая фактура и текущая практика

Задача прохода — раскрыть внешнюю форму механизма главы: кто участвует, что читает, что производит, какие состояния меняются, где чтение отличается от действия и где находится граница с execution environment. Это рабочая карта для написания, не готовый раздел.

## 1. Базовая интерфейсная модель protected process profile

Процессный профиль можно описывать как интерфейс между рабочим состоянием и действием.

```text
work state / signal
  → profile selection
  → role-specific read set
  → allowed action set
  → required output
  → gate / stop / reroute condition
  → durable state update
```

Эта модель полезнее, чем абстрактная фраза «процесс организует работу». Она показывает, что профиль состоит из нескольких рабочих поверхностей.

## 2. Участники

### 2.1. Human operator / product owner / reviewer

Человек не просто «наблюдает». В защищённом процессе человек появляется в нескольких разных функциях:

- задаёт намерение или изменение;
- утверждает roadmap / plan / acceptance criteria;
- отвечает на product tradeoff;
- принимает risk at gate;
- подтверждает UAT или отклоняет результат;
- выбирает между direct adjustment, rollback, MVP scope review;
- решает, когда стоимость процесса выше риска задачи.

Важная граница: процессный профиль должен возвращать человеку не поток технического шума, а точку решения. Human checkpoint не должен выглядеть как «почитай весь лог». Он должен говорить: какое решение требуется, какие варианты есть, какие consequences and evidence известны.

### 2.2. Orchestrator / guide

В GSD это может быть основной command loop / controller; в BMAD — `bmad-help` или пользователь, запускающий следующий workflow. Функция не в том, чтобы «думать лучше всех», а в выборе следующего режима.

Операции:

- посмотреть на текущие artifacts and status;
- понять, какой workflow/profile уместен;
- не запускать executor там, где нужен planner, verifier or correct-course;
- передать правильные входы правильной роли;
- зафиксировать результат обратно в состояние.

### 2.3. Planner / analyst / PM / architect

Эти роли производят не код, а рамку будущего действия.

Их выходы:

- clarified intent;
- `SPEC.md`, PRD, architecture, ADRs;
- epics/stories;
- implementation-ready story;
- decision log;
- open questions;
- constraints;
- readiness decision.

Критерий: такой выход должен стать обязательным входом для будущего execution, review or correction. Иначе роль остаётся разговорной маской.

### 2.4. Executor / dev agent

Executor действует внутри уже выбранного режима. Его нельзя использовать как универсального агента для всех неопределённостей.

Интерфейс executor:

- читает story or `PLAN.md`, limited context, project rules, relevant previous summary;
- меняет только разрешённые файлы / scope;
- запускает указанные проверки;
- пишет summary;
- фиксирует commit or patch;
- останавливается при missing input, changed assumptions, unsafe scope expansion, failed precondition.

### 2.5. Verifier / reviewer / QA

Verifier не должен быть тем же режимом, что executor. Его задача не «продолжить улучшение», а проверить соответствие.

Интерфейс verifier:

- читает spec/story/plan, diff, tests, previous decisions;
- не принимает на себя всю историю сессии, если это загрязняет роль;
- проверяет goal fit and quality separately;
- выдаёт PASS / FAIL / CONCERNS or review comments;
- может вернуть fix items;
- не должен подменять human acceptance там, где нужен human gate.

### 2.6. Investigator / brownfield navigator

Investigator отличается от fixer.

Интерфейс:

- читает старый код, logs, tests, docs, tickets, production traces;
- различает confirmed, deduced and hypothesized facts;
- строит карту поведения;
- указывает missing evidence;
- не исправляет молча;
- возвращает report and recommended next profile.

Для billing/API это критично: старое странное поведение может быть внешним контрактом, а не мусором.

## 3. Входы

### 3.1. Рабочее состояние

Входом может быть PWG node, issue, story status, `STATE.md`, `sprint-status.yaml`, failed CI, review comments, change trigger, error report or human request.

Важно: вход не всегда является разрешением действовать. Например, failing test is signal, not permission to edit. Review comment is signal, not automatic task. Change trigger is signal to assess impact, not permission to mutate plan.

### 3.2. Источники чтения

Разные профили читают разные источники:

| Профиль | Что должен читать |
|---|---|
| clarification / discussion | user intent, previous decisions, open questions, project constraints |
| planning | requirements, decisions, research, roadmap, known blockers |
| story creation | PRD, architecture, UX/API docs, epics, sprint status, old story, previous summaries, git history, project-context |
| execution | story/plan, acceptance criteria, read_first files, project rules, tests, previous summary |
| review / verification | spec/story/plan, diff, tests, evidence, review criteria |
| correct-course | PRD, epics, architecture, UX, spec, current story, change trigger, project docs |
| brownfield investigation | source code, logs, contract tests, production examples, SDK usage, project docs, previous scan |
| human checkpoint | facts, options, risks, consequences, recommended decision boundary |

Смысл таблицы: контекст не должен быть максимальным. Он должен соответствовать роли. Слишком широкий контекст может разрушить роль reviewer; слишком узкий контекст разрушит brownfield analysis.

### 3.3. Внешняя текущая практика: Open GSD

Текущая документация Open GSD / GSD Core показывает практику с явными файлами и командами:

- project initialization creates `.planning/` files: `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, config and research directories;
- phase loop is Discuss → UI design → Plan → Execute → Verify → Ship;
- `.planning/` is committable root project state;
- `STATE.md` contains current position, active decisions, blockers, metrics, recovery;
- `CONTEXT.md` captures implementation decisions that later planner/executor/verifier read;
- `PLAN.md` includes tasks, acceptance criteria, read_first, must_haves, dependencies and verification commands;
- specialist agents run in fresh contexts;
- planner, plan-checker, executor and verifier have different outputs and tool permissions;
- verification produces PASS/FAIL evidence and UAT can record manual acceptance;
- autonomous mode exists, but its meaning for this chapter is limited to checkpoint boundaries and mode selection.

Для основной главы это current-practice confirmation: реальные методы уже не полагаются только на prompt memory. Они делают process artifacts readable and executable by subsequent roles.

### 3.4. Внешняя текущая практика: BMAD Method

Текущие документы BMAD / BMM дают другую форму:

- workflow map frames BMM as context engineering and planning across four phases;
- documents from one phase inform the next phase;
- `bmad-help` can inspect project state and recommend next step;
- workflows can be run through skills directly or through agent menu;
- fresh chat per workflow is recommended;
- implementation phase includes sprint planning, create story, dev story, code review, correct-course, sprint status, retrospective and investigate;
- `bmad-sprint-planning` creates `sprint-status.yaml`;
- `bmad-create-story` reads sprint status and creates story file with all context for dev agent;
- `bmad-correct-course` loads broad planning artifacts and produces Sprint Change Proposal;
- `project-context.md` works as implementation guide for project rules, especially in existing projects;
- v6.7/v6.8 current materials emphasize `.decision-log`, `bmad-investigate`, intent-oriented PRD/spec skills, skill architecture and activation guardrails.

Для главы это показывает: в BMAD профиль действия выбирается через phase/workflow, а состояние представлено через документы and status files. Но точные docs быстро меняются, поэтому основной текст должен ссылаться на первичные текущие sources and avoid overclaiming exact commands if not needed.

## 4. Выходы

### 4.1. Выходы, которые сужают действие

Примеры:

- story file narrows implementation context;
- `PLAN.md` narrows executor task;
- agent brief turns issue into agent-ready work;
- `project-context.md` narrows allowed conventions;
- TDD red test narrows expected behavior;
- `read_first` list narrows source reading.

Такие выходы говорят: «делай именно это, в этих границах, по этим критериям».

### 4.2. Выходы, которые расширяют действие

Примеры:

- brownfield scan opens broader codebase understanding;
- investigation report opens root-cause analysis;
- correct-course opens impact analysis across PRD/epics/architecture;
- architecture review opens systemic change area.

Такие выходы говорят: «не делай локальную правку; нужно расширить рамку, потому что текущий план недостаточен».

### 4.3. Выходы, которые останавливают действие

Примеры:

- human decision request;
- implementation readiness FAIL;
- verification FAIL;
- unresolved product blocker;
- stale project-context;
- missing PRD/epics for correct-course;
- failed compatibility suite;
- hypothesis without evidence;
- checkpoint waiting for UAT.

Такие выходы говорят: «следующий автоматический ход запрещён».

### 4.4. Выходы, которые перенаправляют действие

Примеры:

- investigation recommends `quick-dev`, `correct-course`, `create-story` or code-review;
- no backlog story found recommends sprint refresh, correct-course or retrospective;
- failed plan-checker recommends revision or missing input;
- retrospective recommends process updates or debt items;
- `bmad-help` recommends next workflow based on state.

Такие выходы важны для главы особенно: они показывают profile selection as explicit mechanism.

## 5. Состояния и переходы

### 5.1. Состояния story/process

В BMAD-like frame:

```text
backlog → story creation → ready-for-dev → in-progress → review → done
                     ↘ blocked / correct-course / investigate / retrospective
```

Статус полезен только если он выбирает allowed action:

- backlog → create story;
- ready-for-dev → dev story;
- in-progress with blocker → resolve blocker or correct-course;
- review → code review / verification;
- done → retrospective or next story;
- unknown behavior → investigate;
- plan contradiction → correct-course.

### 5.2. Состояния GSD-like phase

```text
discuss → plan → execute → verify → ship
          ↘ missing input / revise plan / checkpoint / UAT fail / repair plan
```

Смысл:

- discuss without decisions cannot become plan;
- plan without checks cannot become execution;
- execution without summary/evidence cannot become verify;
- verify without PASS/UAT cannot become ship;
- ship without state update leaves future continuation broken.

### 5.3. Состояния evidence

Для investigation and verification useful states:

- Confirmed;
- Deduced;
- Hypothesized;
- Refuted;
- Open;
- PASS;
- FAIL;
- CONCERNS;
- Evidence missing;
- Human acceptance pending.

В главе это можно использовать для мысли: факты тоже имеют процессный статус. Гипотеза не имеет права стать implementation decision.

## 6. Чтение и действие

Одна из самых важных границ главы — различие чтения и действия.

Agent may read broadly without permission to mutate broadly. Brownfield investigator can read old API, logs and project docs, but should not rewrite code. Correct-course profile can read PRD, epics, architecture and stories, but may need approval before changing them. Reviewer can read diff and tests, but should not silently modify implementation while reviewing. Executor can edit code, but usually should not edit requirements.

Таблица для основной главы:

| Режим | Read radius | Write/action radius |
|---|---|---|
| story creation | broad planning/project context | story file, questions, status recommendation |
| execution | narrow story/plan context | code and tests in story scope, summary |
| review | spec/story/diff/tests | review decision, fix items; usually no code changes |
| correct-course | broad planning artifacts | proposal first; artifact edits only after approval |
| investigation | broad code/log/docs evidence | investigation report; not fix by default |
| human checkpoint | facts/options/risk summary | decision request; blocks action |

Это место хорошо готовит мост к IX: selected profile should later map to sandbox, tools and permissions.

## 7. Практические ошибки интерфейса

### 7.1. Слишком общий «Developer»

Если Developer значит всё — уточнение, архитектура, код, ревью, расследование — профиль не защищает работу. Нужно различать dev-story, create-story, investigate, correct-course, code-review.

### 7.2. Состояние без маршрутизации

`STATE.md` or PWG node can be accurate but still not tell what to do next. Нужна функция выбора профиля.

### 7.3. Маршрутизация без evidence

Workflow can route to done or ship without evidence. Then process only hides risk.

### 7.4. Ревью с загрязнённым контекстом

Reviewer that inherits full session history may overreach, rationalize or evaluate wrong object. Better review input: spec, code/diff, criteria, tests, maybe relevant decisions — not all conversation noise.

### 7.5. Brownfield knowledge without freshness

`project-context.md`, scan report or generated architecture can become dangerous if stale. Process profile needs freshness/re-scan/deep-dive rules.

### 7.6. Correct-course without source-of-truth discipline

Changing already completed stories or epics can create history corruption. Correct-course needs explicit change proposal, affected artifact list, human decision and state update.

### 7.7. Skill present but inert

A skill installed in repo or IDE is not proof that process exists. It must be invoked at the right condition, consume correct input, produce output and change next action.

## 8. Что должно попасть в основную главу

1. Не описывать инструменты как product tour.
2. Для GSD показать external form through phase/files/roles/evidence.
3. Для BMAD показать external form through phase/workflow/status/story/correct-course/investigate/project-context.
4. Ввести small interface model: signal → profile → read set → allowed action → output → gate/reroute → state update.
5. Сильно различить чтение и действие.
6. Подчеркнуть, что current practice changes fast; chapter should cite primary docs when using concrete names.
7. Сохранить мост к IX: permissions and sandbox are not this chapter’s subject, but process profile should imply them.
