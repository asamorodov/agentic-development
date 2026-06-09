# Скелетон пересборки теоретического синтеза — v4.2 с ADR-профилем и границей технического атласа

Статус: рабочий скелетон перед написанием теоретической главы.  
Дата: 2026-06-09.  
Основание: `work/approved-ai-sdlc-plan.md` v4, ADR-0007, ADR-0008, `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`, текущие досье, сравнительные аудиты и обсуждение границы между историями, теорией и техническим атласом.

Этот скелетон заменяет v4.1 как рабочую структуру. Он сохраняет верхнюю AI-driven SDLC архитектуру и сравнительные главы v4.1, но добавляет четыре уточнения:

1. ADR получает статус защищённого профиля архитектурного решения внутри Части III.
2. Истории остаются первым разделом сайта и не пересказываются внутри теории.
3. Технический атлас становится приложением по тяжёлым методологическим досье, а не атласом концепций.
4. Блок `Required next dossiers before writing` заменён на правило готовности материала: теория пишется по скелетону, а при нехватке фактуры сначала проводится дополнительный проход по досье или источникам.

## Рабочий принцип

Верхняя рамка остаётся прежней:

```text
AI-driven SDLC = жизненный цикл программного изменения
```

Текст должен идти по жизненным напряжениям, а не по спискам артефактов. Ключевые методологии получают защищённую глубину, но теория не должна превращаться в каталог инструментов или второй корпус историй.

Истории уже находятся в первом разделе сайта. Теория может ссылаться на них как на фактические якоря, сравнивать их и извлекать из них механизмы, но не должна заново пересказывать сами истории.

## Методологический контракт

### Глубокие опорные случаи

```text
SPDD
Gas Town / Beads
```

SPDD и Gas Town / Beads остаются отдельными глубокими главами теории. Их нельзя демонтировать в обзорные разделы или выносить целиком в приложение.

### Защищённые методологические профили

```text
Spec Kit
Kiro Specs
Constitutional SDD
TDAD: Test-Driven AI Agent Definition
TDAD: Test-Driven Agentic Development
GSD / Open GSD
BMAD Method
```

Каждый защищённый методологический профиль должен раскрывать:

```text
проблема → рабочий процесс → артефакты → контекст → роли → человеческие подтверждения → проверка → хвост жизненного цикла → сильные стороны → сбои и риски → сравнение с соседними подходами → граница theory / Handbook / Fieldbook
```

### Защищённый профиль архитектурного решения

```text
ADR / Architecture Decision Records
```

ADR не становится третьим глубоким опорным случаем наравне с SPDD и Gas Town, но получает защищённую глубину внутри Части III. В теории нужно раскрыть Nygard, MADR, статусы ADR, reconstructed ADR, операционную проекцию ADR для агента и контуры подтверждения решения.

### Технический атлас

Технический атлас не объясняет концепты вместо теории. Он сохраняет техническую фактуру по тяжёлым досье:

```text
SPDD
Spec Kit
Kiro Specs
Constitutional SDD
TDAD
GSD / Open GSD
BMAD Method
Gas Town / Beads
ADR
```

В атласе должны жить источниковая база, файлы, команды, структуры, интерфейсы, проверочные контуры, ограничения источников, кандидаты на схемы и скриншоты, а также перенос в Handbook / Fieldbook. Теоретическая глава при этом остаётся самодостаточной по понятиям и аргументу.

---

## Введение. Почему речь не о генерации кода

### Задача части

Снять три ложных чтения:

1. это не “как лучше промптить”;
2. это не “обычный SDLC, где в каждую фазу вставили AI”;
3. это не “чем больше агент сгенерировал кода, тем лучше”.

### Ход

1. Код подешевел, но смысл, проверка и ответственность не подешевели автоматически.
2. Агент усиливает существующую систему, а не заменяет её целиком.
3. Объект анализа — жизненный цикл изменения.
4. Артефакт важен только тогда, когда переносит изменение через границу жизненного цикла.
5. Истории сайта уже дали фактический корпус; теория извлекает из них механизмы и не пересказывает их заново.
6. Переход: сначала нужно сменить единицу анализа.

---

## I. Единица анализа: программное изменение, а не prompt

### Управляющий тезис

Агентская разработка становится понятной только если смотреть на программное изменение как на контур: намерение, контекст, действие, свидетельства, ревью, право завершения и сопровождение.

### Подглавы

1. Почему `prompt → code` слишком бедная модель.
2. Программное изменение как жизненный цикл.
3. Артефакт входит в теорию только если несёт функцию.
4. Пять классов артефактов как скрытая матрица:
   - намерение / спецификация;
   - решение / архитектурная память;
   - контекст / состояние работы;
   - среда исполнения;
   - свидетельства / завершение / сопровождение.
5. Переход к реальной агентской сессии.

---

## II. Реальная агентская сессия: трасса, вмешательство, выживание результата

### Управляющий тезис

Реальная агентская разработка видна в трассе, но трасса не удерживает всю инженерную работу. Часть смысла, решения и ответственности должна пережить сессию.

### Сравнительная подглава: SWE-chat / Programming by Chat / How Coding Agents Fail

- SWE-chat показывает трассу действий и вызовы инструментов.
- Programming by Chat показывает постепенную спецификацию и типы сессий.
- How Coding Agents Fail показывает рассогласования между намерением, действиями агента и результатом.

Синтез: трасса сессии необходима, но её недостаточно.

### Подглавы

1. Трасса как свидетельство, но не вся правда.
2. Progressive specification как нормальная форма работы.
3. Коррекция и сопротивление как сигнал качества.
4. Что исчезает после сессии.
5. Что должно выжить после сессии.
6. Почему нужна внешняя память.

---

## III. Намерение, спецификация, контракт и архитектурное решение

### Управляющий тезис

AI-driven SDLC начинается с превращения намерения, решений и ограничений во внешние артефакты, которые можно ревьюить, версионировать, связывать с кодом и возвращать в следующий цикл.

### Подглавы

1. Prompt как локальная инструкция.
2. Intent debt: что ломается, когда намерение остаётся только в чате.
3. Разные артефакты намерения и решения.

### Сравнительная подглава: specification / ADR / contract

#### Specification

Спецификация фиксирует ожидаемое изменение, границы и проверяемые требования. В сильном режиме она становится рабочей поверхностью агента.

#### Contract

Контракт задаёт проверяемое ожидание: поведение, API, ожидание потребителя, oracle или условие совместимости. Он помогает доказать, что изменение не разрушило договорённость, но сам по себе не объясняет, почему архитектурное решение было принято.

#### ADR

ADR хранит память архитектурного решения.

Обязательные элементы теоретического объяснения:

1. Nygard: ADR как короткая запись решения, контекста и последствий.
2. MADR: более структурированная форма ADR с шаблоном, статусами, связями и последствиями.
3. ADR не является задачей, спецификацией или комментарием к коду.
4. ADR фиксирует не только “что сделали”, но и почему это решение было разумным в данных обстоятельствах.

#### Статус и происхождение записи

Нужно развести статус решения и происхождение записи:

```text
proposed / accepted / deprecated / superseded
```

это статусы решения;

```text
generated / reconstructed
```

это происхождение записи, а не право считать решение принятым.

#### Reconstructed ADR

Reconstructed ADR — не автоматически accepted ADR, а гипотеза о решении:

```text
evidence
confidence
known gaps
review owner
confirmation plan
```

#### Операционная проекция ADR

Полный ADR не должен целиком превращаться в бесформенный контекст для агента. Для агента нужна короткая операционная проекция:

```text
scope
rule
status
backlink to full ADR
applicability check
```

#### Подтверждение ADR

Подтверждение ADR шире ревью владельца. Возможные контуры подтверждения:

```text
owner review
code structure
API compatibility
consumer contract
performance / SLO
rollout / runtime evidence
```

### Остальные подглавы

1. Quality attribute scenario и предположение о проверочном oracle.
2. Когда тяжёлый режим не нужен.
3. Переход к SPDD: когда намерение становится полноценным спецификационным жизненным циклом.

---

## IV. Deep case: SPDD как спецификационный жизненный цикл

### Управляющий тезис

SPDD показывает, как intent превращается в управляемый спецификационный жизненный цикл: prompt становится delivery artifact, связанным с анализом, генерацией, тестами, ревью, обновлением и синхронизацией.

### Baseline rule

До написания взять old-site SPDD seed unchanged. Адаптация допустима только после anti-degradation inventory.

### Подглавы

1. Почему SPDD возник.
2. Prompt as first-class delivery artifact.
3. Story shaping.
4. Analysis context.
5. REASONS Canvas.
6. OpenSPDD command layer.
7. Billing-engine example.
8. Generation as downstream operation.
9. API tests and functional evidence.
10. Iterative review.
11. Prompt update and sync.
12. Human learning and review boundaries.
13. Fit / ROI.
14. Что SPDD даёт AI-driven SDLC.

### Граница с техническим атласом

В теории остаётся механизм SPDD и его значение для жизненного цикла. В атлас уходят технические детали: команды, шаблоны, файлы, примеры, заметки по конкретным источникам и кандидаты на схемы.

---

## V. Защищённые specification methodology profiles

### Управляющий тезис

SPDD не исчерпывает specification layer. Соседние методологии показывают разные способы сделать намерение управляемым: через toolkit, IDE surface, тесты, constitution, governance или task decomposition.

### Правило глубины

Для каждой методологии раскрыть:

```text
проблема → рабочий процесс → артефакты → контекст → роли → человеческие подтверждения → проверка → хвост жизненного цикла → сильные стороны → сбои и риски → сравнение с соседними подходами → граница theory / Handbook / Fieldbook
```

### V.1. Spec Kit как переносимый specification toolkit

Обязательные элементы:

1. Проблема: превращение спецификаций в переносимый рабочий процесс агентной разработки.
2. Рабочий процесс: constitution → specify → plan → tasks → implement.
3. Артефакты: constitution, spec, plan, tasks, templates, scripts, `.specify`, extensions / presets.
4. Контекст: project memory and principles.
5. Человеческие подтверждения: constitution, plan review, task validation.
6. Проверка: analyze / checklist / hooks / extensions.
7. Хвост жизненного цикла: specs and constitution evolve.
8. Сильные стороны: переносимость, экосистема, организационная настройка.
9. Сбои и риски: ritual specification, template cargo cult, stale constitution.
10. Сравнение: SPDD closed loop vs Spec Kit toolkit.

### V.2. Kiro Specs как продуктовая поверхность specification workflow

Обязательные элементы:

1. Проблема: сделать specification workflow частью IDE / product surface.
2. Рабочий процесс: requirements / bug analysis → design → tasks → task execution.
3. Артефакты: `requirements.md` / `bugfix.md`, `design.md`, `tasks.md`, task status.
4. Контекст: `#spec`, Sync Files, repo scanning.
5. Человеческие подтверждения: review gates vs Quick Plan.
6. Проверка: task execution, sync, review checkpoints.
7. Хвост жизненного цикла: specs split, updated, synced with implementation.
8. Сильные стороны: productized collaboration surface.
9. Сбои и риски: shallow specs, Quick Plan overuse, spec drift.
10. Сравнение: Kiro IDE surface vs Spec Kit portable toolkit.

### V.3. TDAD comparative protected profile

#### TDAD A: Test-Driven AI Agent Definition

1. Проблема: specify behavior of tool-using agent.
2. Рабочий процесс: behavioral specs → tests → prompt compilation / refinement.
3. Артефакты: behavioral spec, visible / hidden tests, compiled prompt.
4. Проверка: semantic mutation testing, hidden tests.
5. Сбои и риски: test gaming, narrow behavior, overfit prompt.

#### TDAD B: Test-Driven Agentic Development

1. Проблема: reduce coding-agent regressions with targeted test context.
2. Рабочий процесс: code-test graph → impact analysis → agent skill → targeted tests.
3. Артефакты: graph, impact weights, skill file, test set.
4. Проверка: regression reduction.
5. Сбои и риски: graph staleness, false targeting, procedural TDD instructions without context.

### V.4. Constitutional SDD как governance внутри specification

Обязательные элементы:

1. Проблема: security / governance must shape generation before code exists.
2. Рабочий процесс: Constitution → constraints → generation → traceability → review.
3. Артефакты: machine-readable Constitution, constraint mappings, traceability reports.
4. Контекст: CWE / MITRE / regulatory frameworks.
5. Человеческие подтверждения: constitution approval, security review.
6. Проверка: security defect reduction claims, traceability.
7. Хвост жизненного цикла: Constitution evolves after incidents / regulatory change.
8. Сильные стороны: shifts security left into specification layer.
9. Сбои и риски: narrow empirical base, false security, overconstraint.
10. Сравнение: Constitutional SDD vs policy-as-code vs security review.

### V.5. Comparative synthesis: пять способов сделать намерение управляемым

Сравнить:

- SPDD — method / closed loop.
- Spec Kit — toolkit / ecosystem.
- Kiro — productized IDE surface.
- TDAD — tests as specification of behavior or regression guide.
- Constitutional SDD — governance / security as specification.

Вопрос: какой артефакт становится центральным и какое человеческое суждение остаётся необходимым?

---

## VI. Контекст и рабочее состояние: проект как интерфейс агента

### Управляющий тезис

Проект становится интерфейсом агента только тогда, когда состояние работы вынесено из головы и чата в поддерживаемые, проверяемые и ограниченные поверхности. Но больше контекста не значит лучше.

### Подглавы

1. Что агент должен знать, чтобы не действовать вслепую.
2. Где живёт состояние задачи.
3. Почему больше контекста не значит лучше.
4. Как кодовая база становится рабочей поверхностью.
5. Как проект показывает владельцев, правила и runnable path.
6. Persistent work graph как концепт:
   - task as durable object;
   - dependency;
   - owner;
   - wait condition;
   - lock / pin;
   - ready queue;
   - recovery after interrupted session.
7. Где контекст начинает устаревать.
8. Почему Gas Town будет отдельным deep case, а не просто примером в этой части.

---

## VII. Защищённые process methodology profiles

### Управляющий тезис

Иногда локальных документов и ручного выбора режима недостаточно. Тогда процесс сам становится артефактом: он задаёт роли, состояние, рабочий процесс, проверку и handoff.

### Правило глубины

GSD и BMAD должны быть реконструированы как защищённые методологические профили, а не как короткий обзор.

### VII.1. Когда достаточно разговора

Small reversible tasks. No methodology overkill.

### VII.2. Когда сначала нужен research or plan

Boris Tane / HumanLayer / Mark Erikson как практические якоря.

### VII.3. Когда нужен spec-first

Bridge to Parts III–V.

### VII.4. GSD / Open GSD как лёгкий контур внешнего состояния

Обязательные элементы:

1. Проблема: context rot and long task continuity.
2. Рабочий процесс: discuss → plan → execute → verify → ship.
3. Артефакты: state / context files, plans, verification notes.
4. Контекст: externalized state, fresh-context execution.
5. Роли: human, agent, possible subagents.
6. Человеческие подтверждения: plan approval, verify / ship decision.
7. Проверка: verify step, small checkable phases.
8. Хвост жизненного цикла: state cleanup, plan update, context repair.
9. Сильные стороны: lightweight process discipline.
10. Сбои и риски: stale state, false freshness, over-fragmentation.
11. Сравнение: GSD vs Spec Kit, BMAD, Gas Town.

### VII.5. BMAD как role-based guided process

Обязательные элементы:

1. Проблема: ideation / planning / architecture / implementation need role structure.
2. Рабочий процесс: analysis → planning → architecture → implementation, adapted by project scale.
3. Артефакты: role outputs, plans, architecture docs, implementation tasks.
4. Контекст: guided workflow and role-specific context.
5. Роли: specialized agents / domain experts.
6. Человеческие подтверждения: planning / architecture approval, task execution boundaries.
7. Проверка: workflow gates, review, implementation checks.
8. Хвост жизненного цикла: process state, handoff, role outputs.
9. Сильные стороны: role-based organization and guided flow.
10. Сбои и риски: role theater, overprocess, shallow expert simulation.
11. Сравнение: BMAD vs GSD, Spec Kit, Gas Town.

### VII.6. Reversa / OpenSpec / AgentSPEX как соседние формы

Короткое рассмотрение:

- Reversa: recovering operational specs from legacy.
- OpenSpec / AgentSPEX: agent workflow specification and portability.
- Роль: поддержать спектр process-as-artifact, но не становиться deep anchor.

### VII.7. Comparative synthesis: когда процесс становится артефактом

Сравнить:

- Spec Kit — specification toolkit.
- GSD — lightweight context / process loop.
- BMAD — role-based guided process.
- Reversa / OpenSpec / AgentSPEX — recovery or workflow specification.
- Gas Town — full organizational environment.

Вопрос: какой артефакт становится центральным и какой человеческий контроль остаётся необходимым?

### VII.8. Когда агенту надо отказать

Risk, irreversibility, missing context, weak evidence, unclear owner.

---

## VIII. Исполнение: среда агента, harness, tools, permissions

### Управляющий тезис

Среда исполнения должна не только дать агенту способность действовать, но и сделать действие ограниченным, воспроизводимым, наблюдаемым и обратимым.

### Подглавы

1. Возможность действовать.
2. Граница действия.
3. Сравнительная подглава: Harness / Sandvault / platform agents.
4. Workflow runner / workflow engine:
   - structured run;
   - replay;
   - observability;
   - failure recovery.
5. Истории как короткие якоря, не встроенные кейсы:
   - Shopify Roast;
   - Quix / Klaus Kode;
   - Stripe Minions;
   - Armin Ronacher.
6. Воспроизводимость действия.
7. Исполняемые ограничения.
8. След действия.
9. Где environment itself becomes debt.

---

## IX. Deep case: Gas Town / Beads как организационно-операционный жизненный цикл

### Управляющий тезис

Gas Town показывает, как агентская разработка становится организационной средой: роли, память задачи, управляющие поверхности, сервисные агенты, handoff и стоимость оркестрации.

### Baseline rule

Start from old-site Gas Town seed unchanged.

### Подглавы

1. Почему Gas Town нельзя оставлять одним обзорным разделом.
2. Roles: organizational functions.
3. Mayor: visibility and control.
4. Agent is not session.
5. Beads as data / control / why layer.
6. Persistent work graph на живом материале.
7. GUPP, hooks, molecules, wisps.
8. Refinery, Witness, Deacon.
9. Session continuation and handoff.
10. DoltHub contrast.
11. Cost: throughput vs understanding.
12. What Gas Town gives AI-driven SDLC.

### Bridge

Contrast GSD / BMAD / Gas Town only to explain why Gas Town is deeper, not to reduce Gas Town.

### Граница с техническим атласом

В теории остаётся смысл и механизм Gas Town. В атлас уходят технические детали Beads / GUPP / hooks / molecules / wisps / service agents / diagrams / заметки по конкретным источникам.

---

## X. Свидетельства, тесты, ревью и качество доказательства

### Управляющий тезис

Когда генерация дешевеет, главным дефицитом становится право считать изменение доказанным. Свидетельство зависит от типа изменения.

### Подглавы

1. Почему summary агента не является свидетельством.
2. Почему один тип свидетельства не подходит всем изменениям.
3. Поведенческая правильность.
4. Граничная правильность.
5. Сравнительная подглава: architecture fitness / contract tests / test data.
6. Архитектурная сохранность.
7. API compatibility:
   - breaking changes;
   - consumer contracts;
   - deployability.
8. Performance / SLO / error budget.
9. Rollout / runtime confirmation.
10. Надёжность доказательства: данные, среда, oracle.
11. Социальная проверка:
   - owner review;
   - CODEOWNERS;
   - maintainer acceptance.
12. Трасса выполнения.
13. Evidence package as decision support.
14. Связь с ADR Confirmation.

---

## XI. Завершение, governance и внешний контур

### Управляющий тезис

Право действовать и право завершать изменение принадлежат разным контурам. Агент может выполнить работу, но не владеть её принятием.

### Подглавы

1. Агент может исполнить, но не владеть завершением.
2. Кто обязан смотреть.
3. Кто может принять.
4. Кто отвечает за выпуск.
5. Сравнительная подглава: SASE / open-source policies / CODEOWNERS.
6. Внешний контур и AI-generated contributions.
7. No-AI / limited-AI policies as governance signal.
8. Zig как короткий якорь, не встроенная история.
9. Восстановимость завершения.

---

## XII. Хвост жизненного цикла: сопровождение, долг и обучение среды

### Управляющий тезис

Merge не завершает жизненный цикл. Настоящий хвост изменения — момент, когда его последствия возвращаются в спецификации, тесты, политики, ADR, контекстные файлы, skills и workflow gates.

### Подглавы

1. Release feedback.
2. Incident feedback.
3. Drift feedback.
4. Сравнительная подглава: incident / stale ADR / context cleanup.
5. Stale specification.
6. Stale ADR.
7. Stale `AGENTS.md` / rules / skills.
8. Work graph cleanup.
9. Migration tail.
10. Supply / security feedback.
11. User-facing memory.
12. Возврат в начало.

---

## Заключение. Не карта кейсов, а карта выбора режима

### Управляющий тезис

Финальная теория должна дать карту выбора режима изменения: сколько внешней структуры нужно в зависимости от риска, обратимости, проверяемости, владельца и хвоста сопровождения.

### Финальная сравнительная рамка

```text
conversation
→ research / plan
→ specification
→ decision memory
→ methodology / framework
→ controlled environment
→ evidence
→ completion
→ lifecycle repair
```

### Финальные вопросы

1. Когда достаточно разговора?
2. Когда нужен research / plan?
3. Когда нужна спецификация?
4. Когда нужен ADR?
5. Когда нужна методология или процессная рамка?
6. Когда нужен persistent work graph?
7. Когда нужна организационная среда уровня Gas Town?
8. Когда агенту надо отказать?

---

## Приложение. Технический атлас методологических досье

### Назначение

Технический атлас не объясняет концепты вместо теории. Он сохраняет техническую фактуру по тяжёлым досье, чтобы теория не превращалась в каталог файлов, команд, шаблонов, инструментов и деталей конкретных источников.

### Разделы

```text
A1. SPDD
A2. Spec Kit
A3. Kiro Specs
A4. Constitutional SDD
A5. TDAD
A6. GSD / Open GSD
A7. BMAD Method
A8. Gas Town / Beads
A9. ADR
```

### Структура каждого раздела

1. Где это используется в теории.
2. Источниковая база.
3. Рабочий процесс / жизненный цикл.
4. Артефакты, файлы, команды, интерфейсы.
5. Роли и человеческие подтверждения.
6. Проверка / подтверждение.
7. Хвост жизненного цикла.
8. Ограничения источников.
9. Кандидаты на схемы, скриншоты, иллюстрации.
10. Перенос в Handbook / Fieldbook.

---

## Порядок написания и готовность материала

Этот раздел не требует заранее создать новые “документы будущей теории”. Теоретическая глава и технический атлас ещё будут написаны по скелетону. Досье, карты источников, старые версии разделов и отчёты являются материалом для письма, а не готовыми частями будущего сайта.

Перед написанием каждой части нужно проверить, что для неё достаточно фактуры в уже собранных историях, досье, картах источников и рабочих заметках. Если материала не хватает, сначала проводится дополнительный проход по досье или источникам. Нельзя закрывать слабую часть гладкой теоретической прозой поверх недостаточной фактуры.

### Для Части IV: SPDD

Писать по уже собранному SPDD-материалу, сохраняя old-site seed и проводя anti-degradation check.

### Для Части V: specification methodology profiles

Писать профили Spec Kit, Kiro Specs, Constitutional SDD и TDAD по существующим или дополнительно расширенным досье. Если профиль не проходит правило глубины защищённого методологического профиля, сначала расширять досье, а не писать поверхностный раздел.

### Для Части VII: process methodology profiles

Писать GSD / Open GSD и BMAD как защищённые методологические профили. Если материала недостаточно, сначала проводить проход по источникам.

### Для Части IX: Gas Town / Beads

Писать как глубокий случай по собранному Gas Town-материалу, сохраняя old-site seed и проводя anti-degradation check.

### Для ADR-блока в Части III

Писать по ADR-досье. ADR остаётся защищённым профилем архитектурного решения внутри теории, а не отдельной большой главой.

### Для технического атласа

Создавать разделы атласа после или вместе с написанием соответствующих теоретических частей. Атлас не должен начать диктовать концептуальную структуру теории.

---

## Проверки качества скелетона

### Для каждой методологической секции

1. Раскрыта ли структура защищённого методологического профиля?
2. Есть ли сравнение с соседними методами?
3. Сохраняется ли линия жизненного цикла изменения?
4. Не превращается ли раздел в поверхностный обзор?
5. Понятно ли, что идёт в теорию, а что в Handbook / Fieldbook?

### Для ADR

1. Объяснены ли Nygard и MADR внутри теории?
2. Разведены ли статус решения и происхождение записи?
3. Разведены ли полный ADR и операционная проекция ADR для агента?
4. Есть ли подтверждение шире ревью владельца?
5. Не превращается ли ADR в задачу, спецификацию или бесформенный контекст?

### Для историй

1. Ссылается ли теория на истории как на якоря?
2. Не пересказывает ли теория истории заново?
3. Сохраняется ли первый раздел сайта как фактический корпус историй?

### Для технического атласа

1. Ограничен ли он выбранными тяжёлыми досье?
2. Не стал ли он дублёром концептуальной главы?
3. Сохраняет ли он технические детали, которые перегрузили бы теорию?
