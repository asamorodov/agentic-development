# 09 — скелет аргумента главы VIII

Это рабочий скелет будущей главы. Он нужен, чтобы глава не стала каталогом GSD/BMAD/Gas Town и не повторила A5/C2, а провела собственную линию: восстановленная работа может быть продолжена неправильным способом.

## 1. Начало главы: практический сбой, а не определение процесса

Начинать лучше не с термина «защищённые процессные профили», а с рабочей ситуации.

Сцена:

- проект восстановил состояние после прошлой сессии;
- есть узел `billing/API`;
- есть failing compatibility tests, review comments, product blocker, частичная реализация;
- prime and PWG state достаточно хороши, чтобы понять, где работа находится;
- новая сессия видит всё это и начинает править код.

Проблема: агент не «без контекста». Наоборот, контекста достаточно. Ошибка в другом: он вошёл как executor, хотя по состоянию работы ещё не ясно, что execution допустима.

Задача начального фрагмента — показать, что глава продолжает VII, но не повторяет её. После durable work state возникает новый вопрос: **как выбрать правильный режим продолжения?**

## 2. Первое различение: состояние работы и способ продолжения

После практического сбоя нужно ввести главное различение:

```text
PWG / durable work state: где находится работа, что известно, что заблокировано, чем подтверждена готовность.
Process profile: в какой роли, фазе и форме действия можно продолжать.
```

Здесь нужно сразу снять возможное смешение:

- PWG не обязан быть фазовой методологией;
- process profile не обязан быть долговечным графом работы;
- они встречаются через выходы: story, plan, verification, change proposal, investigation, decision request.

Важно сформулировать не сухо, а через действие:

> Один и тот же рабочий узел может требовать разных следующих ходов. Если выбрать неправильный ход, состояние не спасает работу.

## 3. Центральный сбой: wrong-entry failure

После различения можно назвать центральный сбой главы.

Рабочее название: неправильный вход в восстановленную работу.

Формы:

1. Implementation вместо research.
2. Implementation вместо story creation.
3. Continue old plan вместо correct-course.
4. Fix вместо diagnose/investigate.
5. Review как advice вместо gate.
6. Human tradeoff hidden inside agent choice.
7. Role as persona instead of role as allowed action.

Здесь можно дать короткую таблицу:

| Сигнал состояния | Неправильный вход | Нужный профиль |
|---|---|---|
| Старый API ведёт себя странно | поправить код | brownfield investigation |
| План противоречит найденному поведению | продолжить реализацию | correct-course |
| Story есть, но acceptance criteria неполны | dev-story | story creation / clarification |
| Code написан, evidence слабая | ship | verification / UAT |
| Решение меняет product contract | агент выбирает сам | human checkpoint |

Эта таблица должна помочь читателю почувствовать предмет главы до подробного разбора источников.

## 4. Определение protected process profile

После сбоя можно дать определение.

В рабочей форме:

> Защищённый процессный профиль — это форма продолжения работы, которая задаёт роль, фазу, обязательные входы, допустимые действия, ожидаемый выход, gate/stop/reroute conditions и способ вернуть результат в долговечное состояние.

Важно добавить критерий:

> Профиль работает только если его выход меняет следующий допустимый ход.

Эта часть должна включить interface model:

```text
state / signal
  → profile selection
  → role-specific read set
  → allowed action set
  → required output
  → gate / stop / reroute
  → durable state update
```

Здесь же ввести различие persona vs role profile:

- persona = how the model speaks;
- role profile = what it reads, may change, must produce, and where it must stop.

## 5. GSD как первый большой пример: фаза, файлы, свежий контекст, verification

GSD должен войти первым, потому что он хорошо продолжает тему VII: восстановление между сессиями and context rot.

Порядок фрагмента:

1. GSD отвечает на разрыв длинной агентской работы: решения теряются, контекст шумит, проверка становится словесной.
2. Фазовый цикл: Discuss → Plan → Execute → Verify → Ship. Ссылку поставить при первом конкретном упоминании current docs.
3. `.planning/` and files: `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `CONTEXT.md`, `PLAN-*.md`, `SUMMARY-*.md`, `VERIFICATION-*.md`, `UAT-*.md`.
4. Роли: planner, plan-checker, executor, verifier; fresh contexts and least privilege.
5. Главное для VIII: каждый файл and role changes allowed next action.
6. Пример `billing/API`: after failed compatibility suite, GSD-like profile should not move to ship; it needs verify fail or repair plan.
7. Ограничение: GSD не заменяет PWG and can become ceremony if files not consumed.

Нужно не уходить в GSD configuration, MCP, sandbox, model policies except as bridge to IX.

## 6. BMAD как второй большой пример: роль, фаза, artifact transfer, story cycle, correct-course

BMAD должен входить после GSD как другой профиль: не столько session recovery, сколько распределение суждений по фазам and workflows.

Порядок фрагмента:

1. BMAD строит контекст через analysis, planning, solutioning, implementation.
2. Документы одной фазы становятся входом следующей.
3. `bmad-help` as next-action guide — current practice, но не рекламно.
4. `bmad-spec` / PRD / architecture / epics-stories / implementation readiness.
5. `sprint-status.yaml` and story cycle.
6. `bmad-create-story`: story as context engine, not copy from epic.
7. `bmad-dev-story`: execution bounded by story.
8. `bmad-code-review`: gate.
9. `bmad-correct-course`: if implementation discovers contradiction, switch profile; produce Sprint Change Proposal.
10. `bmad-investigate`: diagnose before fixing; findings graded by evidence.
11. `project-context.md` and brownfield/document-project: established project cannot be treated as greenfield.
12. Ограничение: roles can be persona theater; docs can get stale; status can lie if not tied to evidence.

Сквозной `billing/API` должен вернуться здесь:

- if story missing → `bmad-create-story`;
- if old API behavior unknown → document-project / investigation;
- if plan wrong → `bmad-correct-course`;
- if tests unexplained → `bmad-investigate`;
- if story complete → code review / verification.

## 7. Small-scale profiles: skills, gates, harnesses

После больших методов нужно показать, что process profile не обязательно большой framework.

### Jesse Vincent

Использовать для:

- task discussion before implementation;
- architecture session vs implementation session;
- plan as portable context;
- spec review vs code review;
- gates as hard stops;
- skills under pressure;
- rule rationalization and deleted tests story;
- reviewers receiving too much context and overreaching.

Главный тезис: skill/gate matters when it changes behavior, not when agent can recite it.

### HumanLayer

Использовать для:

- research → plan → implement;
- subagents as context firewall;
- hooks and feedback as signal, not noise;
- human attention at high-leverage points.

Детали hooks/subagents оставить кратко, чтобы не уходить в IX.

### Matt Pocock

Использовать для:

- `/grill-me` as clarification before premature understanding;
- `/to-prd` and `/to-issues` as transformation artifacts;
- `/triage` as backlog readiness;
- `/tdd` as test-before-code profile;
- `/handoff` as context transfer;
- `/diagnose` as diagnose before fix.

Главный тезис: маленький skill может быть защищённым процессным профилем, если он устраняет конкретный wrong-entry failure.

## 8. Сквозной пример как связка, а не отдельная вставка

Пример `billing/API` лучше не ставить в один большой блок только в начале или конце. Его можно вводить в начале, затем возвращать после GSD and BMAD.

Распределение:

1. В начале: состояние есть, агент ошибочно продолжает кодить.
2. После определения: показать шесть возможных профилей.
3. В GSD-разделе: `STATE.md` / `PLAN.md` / `VERIFICATION.md` для billing/API.
4. В BMAD-разделе: story creation, correct-course, investigation, project-context.
5. В конце: итоговая таблица маршрутов для того же узла.

Финальная таблица:

| Situation in billing/API | Proper profile | Output back to state |
|---|---|---|
| acceptance criteria missing | story creation | story file, questions, not-ready/ready status |
| old behavior unknown | brownfield investigation | confirmed behavior, hypotheses, open evidence |
| plan broken by new fact | correct-course | Sprint Change Proposal, decision request |
| code done but evidence weak | verification | PASS/FAIL/CONCERNS, test evidence |
| product contract affected | human checkpoint | decision request, blocked state |
| story ready and scoped | execution | code, tests, summary, review needed |

## 9. Границы с соседями

### 9.1. Граница с VII

В конце главы нужно явно вернуть различие:

- PWG stores continuation state;
- process profile selects continuation mode;
- process outputs must be turned into PWG state to survive session breaks.

### 9.2. Граница с IX

Мост:

> Selected profile is still not safe execution. If profile says “execute story”, runtime must restrict files/tools; if profile says “investigate”, runtime may be read-only; if profile says “review”, runtime should not silently patch code.

Так глава передаёт тему прав, sandbox, hooks, MCP and execution surfaces в IX.

### 9.3. Граница с X

Мост:

> When many profiles and nodes run in parallel, the question changes from “what mode continues this work?” to “how is a multi-agent operation organized?” That is Gas Town / Beads / chapter X.

Gas Town in VIII only as boundary: work object, gates, prime, queues, town/rig.

## 10. Последовательность будущей главы

Предварительный порядок:

1. Практическая сцена: восстановленный `billing/API` node and wrong execution.
2. Почему состояние не выбирает режим.
3. Wrong-entry failure.
4. Protected process profile: definition and interface model.
5. Process as artifact: output changes next allowed action.
6. GSD: recovery profile for long agentic session.
7. BMAD: artifact/role/phase profile for context transfer and course changes.
8. Smaller profiles: Jesse/HumanLayer/Matt skills/gates/harnesses.
9. Return to billing/API table: one state, many correct continuation modes.
10. Boundaries with PWG, execution environment, organizational layer.
11. Final criterion: if a process artifact does not block, allow, reroute, verify or restore next action, it is not protecting the process.

## 11. Anti-catalog check

The chapter becomes a catalog if sections look like:

- “What is GSD?”
- “What is BMAD?”
- “What is Gas Town?”
- “What are skills?”

It stays an argument if each source answers one question:

- What wrong-entry failure does this mechanism prevent?
- Which role/phase/action does it authorize?
- What input must be read?
- What output must be produced?
- What gate/stop/reroute condition exists?
- What durable state receives the result?

So every source section should be rewritten around the failure and the next-action consequence, not around the tool’s own self-description.
