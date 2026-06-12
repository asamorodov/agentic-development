# Утверждённый проект верхней архитектуры v4

# «Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения»

Дата: 2026-06-07  
Статус: **утверждённая архитектурная версия v4: применён patch Stage 0.5–0.12; добавлен слой связанных артефактов; SPDD, спецификационная зона и Gas Town сохраняют прежний статус deep anchors.**

Этот документ заменяет v3 как рабочий архитектурный контракт для пересборки `Theoretical_synthesis_rebuilt.md`. Он не является финальным текстом теории. Его задача — задать структуру, роли источников, границы глубины и human gates перед созданием skeleton, dossiers и глав.

В v4 применены решения из:

- `work/reports/CONSOLIDATED_PLAN_PATCH_AFTER_STAGE_0_5_TO_0_9.md`;
- `work/reports/DETAILED_CONSOLIDATED_PLAN_PATCH_AFTER_FULL_REREAD.md`;
- `work/reports/TARGETED_SOURCE_EXPANSION_STAGE_0_12_REPORT.md`;
- `work/reports/PLAN_PATCH_RECOMMENDATIONS_STAGE_0_12.md`;
- `work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md`;
- `work/reports/PATCH_INTEGRATION_CHECKLIST_AFTER_STAGE_0_12.md`.

---

## 0. Зафиксированные решения v4

### 0.1. Главная рамка сохраняется

Финальная теоретическая часть пересобирается вокруг рамки:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения.**

Рамка понимается не как обычная корпоративная последовательность `requirements → design → coding → testing → deployment`, а как жизненный цикл программного изменения:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

Это петлевая модель. Поздние стадии возвращаются назад и меняют среду: инструкции, спецификации, тесты, hooks, skills, MCP, `AGENTS.md`, review policy, benches, workflow scripts, human gates.

### 0.2. “Карта течений” не возвращается как верхняя структура

Карта течений остаётся:

- source map;
- материалом для отбора кейсов;
- source-control layer;
- средством не потерять разнообразие практик;
- будущим материалом для Handbook / Fieldbook.

Финальная теория строится не как каталог течений, а как **синтез жизненного цикла программного изменения**.

### 0.3. Expanded-версия остаётся quarry

Expanded-версия после honest-pass cycles используется как material quarry. Её нельзя продолжать механически “полировать” как основной текст.

Из неё переносить:

- фактуру;
- источники;
- удачные формулировки;
- уже найденные связи;
- материалы для SPDD, Gas Town, specification zone, evidence, governance and lifecycle tail.

Не переносить:

- каталожную структуру;
- равноправные source-name headings;
- мелкие кейсы без механизма;
- “всё найденное”, если оно не работает на lifecycle line.

### 0.4. Старая теория остаётся композиционным baseline

`content/Theoretical_synthesis.md` остаётся главным композиционным ориентиром. Её ценность — не полнота новых источников, а сильное движение:

```text
от удачного запроса → к рабочей среде вокруг модели
```

При пересборке нужно сохранять старую дисциплину: часть несёт мысль, кейсы подчинены тезису, источники не становятся равноправными колоннами.

### 0.5. Спецификационная зона остаётся центральным узлом документа

Слой намерения / спецификации является одним из важнейших мест AI-driven SDLC. Поэтому v4 сохраняет специальную specification zone:

```text
III. Намерение: почему prompt слишком слаб как единица управления
IV. Deep case: SPDD как спецификационный lifecycle
V. Соседние спецификационные режимы: Spec Kit, Kiro, TDAD, Constitutional SDD
```

Эта зона должна показать, что AI-driven SDLC начинается не с “модель пишет код”, а с превращения намерения в управляемые, проверяемые и сопровождаемые артефакты.

### 0.6. SPDD остаётся отдельной частью

SPDD становится самостоятельной частью, а не deep block внутри Части III.

Причина: SPDD остаётся самым цельным методологическим источником в корпусе для слоя intent/specification lifecycle. Он соединяет:

- prompts as first-class delivery artifacts;
- REASONS Canvas;
- OpenSPDD command layer;
- end-to-end пример изменения billing engine;
- генерацию кода из Canvas;
- API-test;
- review/refactor;
- prompt update;
- sync-дисциплину;
- human learning / review trade-off;
- организационную рамку Thoughtworks internal IT.

Если SPDD оставить внутри общей части про намерение, есть риск повторить уже произошедшее с Gas Town: всё будет формально упомянуто, но методологическая сила кейса исчезнет.

### 0.7. Spec Kit, Kiro, TDAD и Constitutional SDD раскрываются глубоко

Spec Kit, Kiro, TDAD and Constitutional SDD не являются throwaway contrast cases. В v4 они сохраняют отдельную часть как разные формы спецификационного управления:

- **Spec Kit** — toolkit/ecosystem, где specification становится executable workflow с constitution/spec/plan/tasks/implement, templates, scripts, extensions/presets and agent integrations.
- **Kiro Specs** — productized spec workflow на `requirements.md`, `design.md`, `tasks.md`, task execution, `#spec` context, Sync Files и явные review gates.
- **TDAD** — два разных источника с одинаковым acronym:
  - `Test-Driven AI Agent Definition` — prompt/agent behavior as compiled artifact from behavioral specifications;
  - `Test-Driven Agentic Development` — graph-based code-test impact analysis as agent skill for regression reduction.
- **Constitutional SDD** — security/governance constraints as versioned machine-readable Constitution, with traceability from principles to code and security-by-construction.

### 0.8. Gas Town / Beads остаётся отдельной deep part

Gas Town / Beads возвращается к статусу full deep case. Это deep anchor для organizational/operational lifecycle:

- roles;
- Mayor;
- Beads;
- durable task state;
- hooks / GUPP / molecules / wisps;
- service agents;
- work identities;
- cost of orchestration.

Он не должен снова стать одним обзорным подразделом.

### 0.9. Жёсткое правило для SPDD и Gas Town: сначала старый сайт целиком

Для **SPDD** и **Gas Town / Beads** действует отдельное правило восстановления baseline.

Нельзя начинать работу над этими разделами с последней expanded/synthesis-версии: она уже содержит следы сжатия, особенно по Gas Town. Начинать нужно с полного текста соответствующего раздела из **документа в сайте / старого baseline**.

Рабочий порядок:

```text
old site baseline first → unchanged seed → additive/adaptive rewrite → anti-degradation check
```

Обязательная процедура:

1. извлечь полный раздел SPDD / Gas Town из старого сайта;
2. сохранить его как baseline extract;
3. перенести в rebuilt-документ без изменений как seed;
4. только после этого адаптировать к новой AI-driven SDLC структуре;
5. добавлять новую фактуру из expanded-версии и первоисточников;
6. запрещено сжимать детали без explicit human gate;
7. перед завершением сделать baseline-vs-draft anti-degradation report.

### 0.10. Артефакты жизненного цикла становятся first-class objects

Новая теория должна отслеживать не только стадии AI-driven SDLC and deep cases, но и артефакты, которые переносят программное изменение между стадиями.

Артефакт получает место в основной теории только если он выполняет функцию в жизненном цикле изменения:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение
```

Формула v4:

> Агентская разработка меняет не только исполнителя работы. Она требует связать намерение, контекст, решение, среду, проверку, владельца и сопровождение через артефакты, которые можно читать, проверять, обновлять и использовать в следующем цикле.

Это не новая top-level part. Это скрытая организующая модель, которая не даёт новым материалам превратиться в неоднородную коллекцию.

### 0.11. Пять классов артефактов

Чтобы не получить каталог, новые материалы группируются по функции.

#### 0.11.1. Артефакты намерения и решения

- prompt;
- requirements / PRD;
- specification;
- acceptance criteria;
- ADR / decision record;
- RFC / design proposal;
- API/data contract;
- traceability link;
- quality attribute scenario;
- architecture constraint;
- tradeoff / risk record;
- test oracle assumption;
- data representativeness requirement.

Функция: удержать не только “что хотим”, но и почему, по каким альтернативам, с какими ограничениями and как это связано с кодом и проверкой.

#### 0.11.2. Артефакты состояния задачи и проекта

- `research.md`;
- `plan.md`;
- handoff;
- progress log;
- task graph;
- `AGENTS.md`;
- Cursor rules / Agent README;
- codebase readiness note;
- software catalog / ownership metadata.

Функция: сделать проект читаемым для агента и человека.

#### 0.11.3. Артефакты среды исполнения и ограничений

- dev container / reproducible environment;
- sandbox / permissions;
- worktree;
- tool/MCP boundary;
- policy-as-code;
- secret scanning;
- credential inventory;
- sensitive context boundary;
- agent workflow specification;
- architecture fitness function;
- architecture test;
- layer/dependency/cycle rule;
- controlled test environment;
- service virtualization;
- test dependencies as code;
- environment identity.

Функция: не просто дать агенту инструменты, а сделать его действие ограниченным, воспроизводимым and наблюдаемым.

#### 0.11.4. Артефакты свидетельства и проверки

- test outputs;
- CI evidence;
- benchmark results;
- contract tests;
- traceability matrix;
- review comments;
- PR description;
- agent trace / tool-call log;
- policy check results;
- security review;
- SBOM/provenance evidence;
- architecture fitness result;
- architecture test output;
- tradeoff review result;
- test data source;
- fixture / seed state;
- synthetic data note;
- masked production-like data note;
- oracle provenance;
- independent validation of generated tests.

Функция: дать результату право двигаться дальше.

#### 0.11.5. Артефакты завершения и хвоста lifecycle

- CODEOWNERS;
- ownership map;
- review routing;
- escalation path;
- release plan;
- migration plan;
- rollback plan;
- runbook;
- incident report;
- postmortem;
- changelog / release notes;
- dependency policy;
- deprecation policy;
- context cleanup;
- stale ADR / decision debt;
- architecture drift;
- stale fitness function;
- architecture-test maintenance;
- test data drift;
- stale fixtures;
- test environment drift;
- test data privacy cleanup.

Функция: показать, что AI-driven SDLC не заканчивается на merge.

### 0.12. Architecture quality and test data become named medium-high evidence/control layers

После Stage 0.12 два слоя получают явные named subsections:

1. **Архитектурные качества как проверяемые ограничения**.
2. **Тестовые данные, тестовая среда и независимость оракула**.

Они не становятся новыми top-level parts and not deep anchors. Но они сильнее короткого упоминания. Оба в первую очередь усиливают Part X, с мостами в Parts III, VIII and XII.

### 0.13. Process/framework layer добавляется, но не становится новой deep structure

GSD, BMAD, Reversa, OpenSpec / Agent Spec and AgentSPEX попадают в process/framework layer. Это отдельный класс от specification zone.

Пока их роль:

- medium-depth sections / dossiers;
- comparison by lifecycle function;
- no new deep anchor without human gate.

### 0.14. Part XII остаётся controlled tail

Part XII должна замкнуть lifecycle, но не стать эксплуатационным handbook. Новые хвостовые артефакты добавляются группами, а не как длинный список отдельных тем.

---

## 1. Обновлённая верхняя структура v4

```text
Введение. Почему речь не о генерации кода
I. Единица анализа: программное изменение, а не prompt
II. Реальная агентская сессия: трасса, вмешательство, выживание результата
III. Намерение: почему prompt слишком слаб как единица управления
IV. Deep case: SPDD как спецификационный lifecycle
V. Соседние спецификационные режимы: Spec Kit, Kiro, TDAD, Constitutional SDD
VI. Контекст и рабочее состояние: проект как интерфейс агента
VII. Делегирование: выбор режима работы, а не выбор инструмента
VIII. Исполнение: среда агента, harness, tools, permissions
IX. Deep case: Gas Town / Beads как организационно-операционный lifecycle
X. Свидетельства, тесты, ревью и качество доказательства
XI. Завершение, governance и внешний контур
XII. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

Список частей почти не меняется. Изменение в v4 — внутри частей: добавлен слой связанных артефактов and updated evidence/control layers.

---

## 2. Логика документа по частям

## Введение. Почему речь не о генерации кода

### Управляющий тезис

AI-driven SDLC начинается там, где AI перестаёт быть ускорителем набора кода и начинает менять весь lifecycle программного изменения: намерение, контекст, среду исполнения, свидетельства, ревью, governance и сопровождение.

### Функция

Сразу защитить документ от трёх неверных чтений:

1. “это про vibe coding / prompt engineering”;
2. “это обычная корпоративная схема SDLC с AI на каждой фазе”;
3. “это про рост количества кода, PR or activity”.

### Что добавить в v4

Введение должно сказать: рост активности не равен росту ценности. AI-driven SDLC оценивается по способности процесса сохранить намерение, проверить изменение, распределить ответственность and вернуть опыт в среду.

### Материалы

- DORA 2025 — AI как amplifier существующей организационной системы;
- Bain 2025 — ценность приходит от применения AI по lifecycle and redesign процессов;
- SPACE / DevEx — activity is not productivity;
- supervisory engineering studies — AI shifts work toward verification and review capacity;
- Codex / Copilot / Jules / Claude Code docs — современные инструменты уже оформляют агентскую работу через task, repo, branch, PR, tests, logs, sandbox, instructions.

---

## I. Единица анализа: программное изменение, а не prompt

### Управляющий тезис

Агентская разработка становится понятной только если смотреть не на отдельный prompt, а на весь контур изменения: кто формулирует намерение, где живёт контекст, что делает агент, какие следы остаются, кто проверяет и кто имеет право завершения.

### Функция

Задать lifecycle-схему, к которой будут привязаны все дальнейшие материалы. Это рамочная часть без deep case.

### Подразделы

1. Почему “prompt → code” — слишком бедная модель.
2. Software-change lifecycle как единица анализа.
3. Контур работы: человек, агент, среда, инструменты, проверки, владелец завершения.
4. Почему AI усиливает систему, а не заменяет её.
5. Артефакт попадает в теорию только если выполняет функцию в lifecycle.
6. Переход к эмпирической поверхности реальной сессии.

### Что добавить в v4

Добавить правило отбора артефактов:

> Артефакт важен для этой теории только если он переносит изменение через границу жизненного цикла.

Не делать здесь полный каталог артефактов. Дать мысль and prepare later parts.

---

## II. Реальная агентская сессия: трасса, вмешательство, выживание результата

### Управляющий тезис

Реальная агентская разработка видна не в рекламной демонстрации, а в трассе: prompts, tool calls, исправления пользователя, pushback, выживание или исчезновение generated code, границы делегирования.

### Функция

Заземлить теорию до методологий. До SPDD и Spec Kit нужно показать, почему вообще требуется lifecycle-дисциплина: обычная агентская сессия уже является сложным контуром вмешательства, а не одноразовым запросом.

### Deep empirical anchor

- SWE-chat / Programming by Chat.

### Подразделы

1. Что видно в session trace.
2. Progressive specification как нормальная форма взаимодействия.
3. Pushback and correction как evidence, а не annoyance.
4. Survival of generated code: что живёт после агента.
5. Ограниченность session trace: что она не удерживает.
6. Почему сессия требует внешних артефактов намерения, решения and evidence.

### Что добавить в v4

Показать, что session trace не видит всего:

- ADR;
- ownership;
- release state;
- deployment/migration risk;
- SBOM;
- hidden contracts;
- test data provenance;
- architecture drift.

Это естественный переход к Part III.

---

## III. Намерение: почему prompt слишком слаб как единица управления

### Управляющий тезис

AI-driven SDLC начинается не с “лучшего prompt”, а с превращения намерения в внешний, проверяемый и сопровождаемый объект: его можно ревьюить, версионировать, связывать с кодом, обновлять, передавать между людьми и агентами и возвращать в будущий lifecycle.

### Функция

Подготовить specification zone and distinguish artifact types before SPDD.

### Подразделы

1. Prompt как ephemeral instruction: почему он не выдерживает SDLC.
2. Intent debt: что теряется, если код живёт дольше намерения.
3. Intent artifact: требования к артефакту намерения.
4. Разные артефакты намерения и решения.
5. Prompt, plan, spec, ADR, RFC, contract, traceability link — разные функции.
6. Quality attribute scenario and architecture constraint.
7. Acceptance criteria and test oracle assumptions.
8. Когда тяжёлый спецификационный режим не нужен.
9. Переход: почему SPDD заслуживает отдельной части.

### Важное различение v4

Не смешивать:

- `prompt` — локальная инструкция;
- `requirements / PRD` — исходная потребность;
- `specification` — целевое поведение and constraints;
- `plan` — путь выполнения;
- `ADR` — принятое решение, причины, альтернативы, последствия;
- `RFC/design proposal` — поверхность обсуждения до решения;
- `contract` — граница поведения для других систем или данных;
- `traceability link` — связь между intent, implementation and evidence;
- `quality attribute scenario` — качество, которое архитектура должна сохранять;
- `test oracle assumption` — предположение о том, что считать правильным результатом.

### Важное ограничение

Не раскрывать здесь SPDD подробно. Часть III должна создать вопрос, на который отвечает Часть IV.

---

## IV. Deep case: SPDD как спецификационный lifecycle

### Управляющий тезис

SPDD показывает, как intent layer превращается в управляемый спецификационный lifecycle: prompt перестаёт быть одноразовым входом модели и становится version-controlled delivery artifact, который задаёт границы генерации, поддерживает ревью, проверку, обновление, синхронизацию и повторное использование.

### Функция

Дать первый большой deep anchor всей теории. SPDD должен стать benchmark-глубиной для изложения методологий в документе.

### Подразделы

1. Почему SPDD возник: от personal productivity к organization-level capability.
2. Prompt as first-class delivery artifact.
3. REASONS Canvas: requirements, entities, approach, structure, operations, norms, safeguards.
4. OpenSPDD command layer.
5. End-to-end пример billing engine.
6. Генерация как downstream operation, а не центр метода.
7. API tests / functional validation / iterative review.
8. Prompt update и sync: замкнутый lifecycle вместо handoff.
9. Human learning и границы автоматического review.
10. Asset integrity: prompt version must correspond to code commit.
11. Стоимость и границы применимости SPDD.
12. Что SPDD даёт всей AI-driven SDLC рамке.

### Материалы

- Martin Fowler / Thoughtworks SPDD article;
- OpenSPDD repository / commands;
- SPDD iterative review page;
- SPDD Q&A / fragments;
- old site SPDD seed;
- expanded theory quarry.

### Правило

Сначала old-site SPDD seed unchanged, затем adaptation. No compression without human gate.

---

## V. Соседние спецификационные режимы: Spec Kit, Kiro, TDAD, Constitutional SDD

### Управляющий тезис

SPDD не исчерпывает intent/specification layer. Соседние подходы показывают, что спецификация в AI-driven SDLC может быть toolkit, IDE workflow, behavioral compiler, test-impact skill или security constitution. Их нужно раскрыть глубоко, потому что именно здесь видно, как “намерение” становится разными видами управляемой инфраструктуры.

### Функция

Не дать SPDD превратиться в единственный рецепт. Показать спектр спецификационных режимов и их trade-offs.

### Подразделы

1. **Spec Kit: specification as executable workflow toolkit.**
   - constitution;
   - specify;
   - plan;
   - tasks;
   - implement;
   - templates/scripts;
   - extensions/presets;
   - agent integrations;
   - enterprise/compliance customization.

2. **Kiro Specs: productized spec workflow inside IDE.**
   - `requirements.md` / `bugfix.md`;
   - `design.md`;
   - `tasks.md`;
   - task execution interface;
   - `#spec` context;
   - Sync Files;
   - review gates vs Quick Plan;
   - spec splitting and collaboration.

3. **TDAD: два разных подхода под одним acronym.**
   - `Test-Driven AI Agent Definition`: поведение агента как compiled prompt artifact from behavioral specs;
   - visible/hidden tests, semantic mutation testing, spec evolution;
   - `Test-Driven Agentic Development`: code-test graph impact analysis, target tests as agent skill, regression reduction;
   - почему один TDAD ближе к specification layer, а другой к evidence/harness layer.

4. **Constitutional SDD: security and governance as specification.**
   - Constitution as versioned machine-readable artifact;
   - constraints from CWE/MITRE/regulatory frameworks;
   - traceability from principles to code locations;
   - security-by-construction vs reactive review.

5. **Соседние boundary artifacts.**
   - API/data contracts;
   - traceability links;
   - contract tests;
   - policy-as-code connection.

### Ограничение v4

GSD and BMAD не добавлять сюда как “ещё два спецификационных режима”. Их место — process/framework layer in Part VII.

---

## VI. Контекст и рабочее состояние: проект как интерфейс агента

### Управляющий тезис

Даже хорошая спецификация не работает в пустоте. Agentic SDLC требует, чтобы проект стал читаемым интерфейсом для агента: с рабочей памятью, инструкциями, context files, research notes, plans, rules, skills, environments, ownership and repo conventions.

### Функция

Перейти от “что мы хотим изменить” к “в какой среде агент понимает изменение”.

### Подразделы

1. Project as agent-readable surface.
2. `research.md`, `plan.md`, handoff and progress log.
3. ADR as durable project memory.
4. Context files: `AGENTS.md`, Cursor rules, Agent READMEs.
5. Codebase readiness: tests, CI, instructions, metrics, feedback loops.
6. Context file quality/debt: more context is not automatically better.
7. Reproducible setup and runnable project state.
8. Software catalog / ownership metadata as navigation surface.
9. Переход к выбору режима делегирования.

### Материалы

- AGENTS.md;
- Codex docs;
- Claude Code docs;
- Cursor rules studies;
- Agent READMEs;
- Evaluating AGENTS.md;
- Agentic Context Engineering;
- Boris Tane research/plan;
- HumanLayer research/plan/implement;
- Mark Erikson dev planning;
- Team Topologies / platform engineering / catalog sources as light support.

### Важное ограничение

Не превращать Part VI в энциклопедию documentation practices. Её задача — показать, как проект становится интерфейсом агента.

---

## VII. Делегирование: выбор режима работы, а не выбор инструмента

### Управляющий тезис

В агентской разработке главный выбор — не “какой инструмент использовать”, а какой режим делегирования соответствует риску, обратимости, неопределённости, проверяемости и цене ошибки.

### Функция

Вернуть разнообразие “карты течений”, но подчинить его lifecycle line.

### Подразделы

1. Лёгкий разговорный режим.
2. Research-first режим.
3. Plan-first режим.
4. Spec-first режим.
5. Bugfix/diagnose-first режим.
6. PR сопровождение.
7. Background/parallel agent mode.
8. Process as installed artifact: GSD, BMAD, Reversa, OpenSpec / AgentSPEX.
9. Когда нужно отказать агенту.

### Новый process/framework layer v4

GSD / Open GSD:

- externalized state;
- context engineering;
- small checkable plans;
- fresh-context execution;
- verify step.

BMAD:

- role-based methodology;
- specialized agents;
- guided workflows;
- planning/architecture/implementation loop.

Reversa:

- recovering operational specifications from legacy systems;
- possible bridge to migration/tail.

OpenSpec / Agent Spec / AgentSPEX:

- workflow specification;
- portability;
- explicit control flow / state / verification.

### Ограничение

Medium-depth only unless dossiers justify promotion. No new deep anchor without human gate.

---

## VIII. Исполнение: среда агента, harness, tools, permissions

### Управляющий тезис

Агентская способность создаётся не только моделью, но и средой исполнения: tools, sandbox, permissions, worktrees, hooks, skills, MCP, subagents, logs, test runners, reproducible environments, policies and traces.

### Функция

Показать техническую инфраструктуру AI-driven SDLC после выбора режима.

### Подразделы

1. Tools, sandbox, permissions.
2. Worktrees and isolation.
3. Hooks, skills, subagents, MCP.
4. Reproducible/runnable environment: dev container, setup, build/test commands.
5. Policy-as-code as executable constraint.
6. Secret scanning, credential inventory, sensitive context boundary.
7. Architecture fitness functions and architecture tests as execution constraints.
8. Controlled test environment, service virtualization, test dependencies as code.
9. Agent trace / tool-call log / trajectory evidence.
10. Переход к Gas Town as organizational environment.

### Материалы

- Harness Engineering;
- ACI / SWE-agent;
- Codex / Copilot cloud agent / Jules / Claude Code;
- MCP, hooks, skills, subagents;
- configuration / context studies;
- Dev Containers / reproducible build / attestable build sources;
- OPA / policy-as-code sources;
- secret leakage in agent skills;
- AgentTrace / AgentSight / OpenTelemetry GenAI conventions;
- Testcontainers / service virtualization.

### Ограничение

Part VIII should not become tool catalog. Every item must answer: what does it make controlled, reproducible, observable or bounded?

---

## IX. Deep case: Gas Town / Beads как организационно-операционный lifecycle

### Управляющий тезис

Gas Town показывает другой глубокий слой AI-driven SDLC: агентская разработка может стать организационной средой с ролями, памятью задачи, рабочими идентичностями, управляющими поверхностями, обслуживающими агентами и ценой orchestration.

### Функция

Второй большой vertical slice после SPDD. Если SPDD показывает intent/specification lifecycle, Gas Town показывает organizational/operational lifecycle.

### Подразделы

1. Почему Gas Town нельзя оставлять одним обзорным разделом.
2. Roles, rigs and agent identities.
3. Mayor как управляемая поверхность видимости.
4. Beads как память задачи и контур долговременного состояния.
5. Witness / Deacon / Dogs / Refinery.
6. GUPP / NDI / hooks / molecules / wisps.
7. Session continuation and handoff.
8. DoltHub contrast: orchestration, isolation, trust, verification.
9. Цена: complexity, coordination overhead, verification burden.
10. Что Gas Town даёт AI-driven SDLC.

### Связь с v4 artifact layer

Gas Town может быть объяснён как organizational artifact graph:

- Beads — task memory and control layer;
- Mayor — visibility/control surface;
- roles — organizational functions;
- hooks/molecules/wisps — workflow continuity;
- service agents — maintenance of the agentic environment.

### Правило

Start from old-site Gas Town seed unchanged. Add new details only after baseline preservation.

---

## X. Свидетельства, тесты, ревью и качество доказательства

### Управляющий тезис

Когда генерация дешевеет, центральным дефицитом становятся свидетельства: tests, logs, diffs, PR descriptions, benchmark validity, review capacity, contract evidence, architecture fitness, test data quality and agent traces.

### Функция

Показать evidence layer: как lifecycle получает право двигаться дальше.

### Подразделы

1. Why “agent says done” is not evidence.
2. Evidence package depends on change type.
3. Tests and CI evidence.
4. Benchmarks and benchmark validity.
5. Contract tests and traceability links.
6. **Архитектурные качества как проверяемые ограничения.**
7. **Тестовые данные, тестовая среда и независимость оракула.**
8. PR description and review comments.
9. Agent trace / tool-call log / trajectory evidence.
10. Policy check results and security review outputs.
11. Review capacity and supervisory engineering.
12. Переход к completion rights.

### Evidence package taxonomy

Evidence package may include:

- unit/integration/API tests;
- contract tests;
- CI logs;
- benchmark results;
- traceability links;
- PR description;
- review comments;
- agent trace/tool-call log;
- policy check results;
- security review outputs;
- SBOM/provenance evidence;
- reproducible build evidence;
- architecture fitness results;
- test data source;
- fixture / seed state;
- environment identity;
- oracle provenance.

### Subsection: Архитектурные качества как проверяемые ограничения

Must cover:

- quality attribute scenarios;
- tradeoffs and sensitivity points;
- architecture constraints;
- architecture fitness functions;
- architecture tests;
- layer/dependency/cycle rules;
- architecture drift;
- limits of automation;
- human architectural judgment.

### Subsection: Тестовые данные, тестовая среда и независимость оракула

Must cover:

- test data management;
- fixtures, seeds and datasets;
- masked production-like data;
- synthetic data and verification;
- service virtualization;
- Testcontainers-style dependencies as code;
- generated tests and generated test data;
- oracle independence;
- environment identity.

### Материалы

- UTBoost;
- over-mocked tests;
- Testing with AI agents;
- Saving SWE-Bench;
- SWE-PolyBench;
- PR / review studies;
- TDAD code-test impact analysis;
- architecture quality / ATAM / fitness function sources;
- ArchUnit / architecture tests;
- test data management;
- Testcontainers;
- service virtualization;
- LLM unit testing SLR and HardTests.

### Ограничение

Part X should be rigorous but not encyclopedic. The principle: different change types require different proof packages.

---

## XI. Завершение, governance и внешний контур

### Управляющий тезис

Operational agency не равна праву завершения. Агент может действовать, но merge, publish, release, accept или reject остаются социально-техническими правами внутри конкретного контура владения.

### Функция

Показать внешний предел AI-driven SDLC.

### Подразделы

1. Operational agency vs completion right.
2. Open-source policy cluster.
3. CODEOWNERS / ownership map / review routing.
4. Protected branches / required review / escalation path.
5. Release authority vs merge authority.
6. Disclosure and provenance for agent-generated contributions.
7. Audit/provenance record.
8. Governance boundaries for tools, models and data.
9. Переход к lifecycle tail.

### Главная формула

```text
право исполнять ≠ обязанность ревьюить ≠ право сливать ≠ право выпускать
```

### Материалы

- SASE;
- Linux kernel coding assistants policy;
- QEMU AI-generated content policy;
- LLVM / Ghostty / Debian / Gentoo / scikit-learn / FastAPI policy cluster;
- GitHub Well-Architected governance;
- CODEOWNERS / ownership research;
- review capacity studies.

---

## XII. Хвост lifecycle: сопровождение, долг и обучение среды

### Управляющий тезис

AI-driven SDLC не заканчивается merge. Сбой, drift, technical debt, intent debt, security risk, observability gaps, stale context files, architecture drift and maintenance burden возвращаются назад и должны менять спецификации, tests, instructions, skills, policies and workflow gates.

### Функция

Замкнуть lifecycle и связать теорию с Handbook.

### Controlled tail clusters

#### 1. Release and operational control

- release plan;
- feature flags;
- canary rollout;
- migration plan;
- rollback plan;
- runbook.

#### 2. Learning and repair

- incident report;
- postmortem;
- stale ADR;
- context file cleanup;
- prompt/context regression;
- observability debt.

#### 3. Architecture and test evidence tail

- architecture drift;
- stale fitness functions;
- architecture-test maintenance;
- test data drift;
- stale fixtures;
- test environment drift;
- test data privacy cleanup.

#### 4. Supply-chain and security tail

- SBOM;
- dependency/license inventory;
- secret rotation;
- credential follow-up;
- provenance record.

#### 5. Communication and external memory

- changelog;
- release notes;
- traceability to PR/issues/contracts.

### Материалы

- DORA / Bain as system-level caution;
- Governing Technical Debt in Agentic AI Systems;
- maintenance papers;
- security/governance materials;
- OpenSSF / Snyk cautiously;
- SBOM / SPDX / CycloneDX / SSDF;
- runbooks / postmortems / release notes;
- architecture drift and test-data drift sources.

### Ограничение

Part XII must remain a controlled tail, not operational handbook. It closes the lifecycle and prepares Handbook / Fieldbook.

---

## Заключение. Не карта кейсов, а карта выбора режима

### Управляющий тезис

Финальный результат теории — не список “течений” и не методология одного типа, а карта выбора режима программного изменения: какой lifecycle-контур нужен в зависимости от риска намерения, контекста, проверяемости, прав завершения and хвоста сопровождения.

### Функция

Подготовить переход к Handbook / Fieldbook.

### Финальная формула

AI-driven SDLC is not “AI does every phase.” It is a way to decide how much structure a software change needs:

- light conversation;
- research/plan;
- specification;
- process framework;
- controlled execution;
- evidence package;
- governance boundary;
- lifecycle repair.

---

## 3. Deep / medium / short roles v4

| Материал | Новая роль | Глубина в финальном тексте | Причина |
|---|---|---:|---|
| SPDD / OpenSPDD | Deep anchor Part IV | Очень высокая | Самый цельный case для intent/spec lifecycle |
| Spec Kit | Deep neighboring methodology Part V | Высокая | Toolkit/ecosystem: spec as executable workflow |
| Kiro Specs | Deep neighboring methodology Part V | Высокая | Productized spec workflow inside IDE |
| TDAD: AI Agent Definition | Deep/spec-evidence bridge Part V | Средне-высокая | Prompt/agent behavior as compiled artifact |
| TDAD: Agentic Development | Deep/evidence bridge Parts V/X | Средне-высокая | Test-impact graph as agent skill; regression reduction |
| Constitutional SDD | Deep security/governance spec Part V | Высокая | Security constraints embedded into spec layer |
| SWE-chat / Programming by Chat | Empirical anchor Part II | Высокая | Реальная поверхность сессии |
| Gas Town / Beads | Deep anchor Part IX | Очень высокая | Organizational/operational lifecycle |
| Open-source policy cluster | Boundary anchor Part XI | Высокая | Право завершения и внешний контур |
| GSD / Open GSD | Medium process-framework case Part VII | Средняя | Context/process continuity |
| BMAD | Medium process-framework case Part VII | Средняя | Role-based AI development workflow |
| Reversa | Medium/short Part VII/XII | Средняя-низкая | Recovery of operational specs from legacy |
| Architecture quality / fitness functions | Medium-high Part X | Средне-высокая | Checks qualities normal tests may miss |
| Test data / test environments | Medium-high Part X | Средне-высокая | Evidence quality depends on data/environment/oracle |
| SBOM / dependency inventory | Short-medium Part XII | Средняя-низкая | Supply-chain tail artifact |
| Agent observability/traces | Medium Part VIII/X | Средняя | Evidence/provenance of trajectory |
| Policy-as-code | Medium-short Part VIII/XI | Средняя-низкая | Executable governance |
| DORA / Bain / A-SDLC | Framing | Средняя | Рамочная проверка, не deep case |

---

## 4. Обязательные guardrails v4

1. Не превращать документ в каталог SDLC artifacts.
2. Каждый артефакт должен отвечать на вопрос: какую границу жизненного цикла он помогает пройти?
3. Не превращать Part XII в эксплуатационный handbook.
4. Не создавать новых top-level parts without human gate.
5. Не создавать новых deep anchors without dossiers and human gate.
6. Не демотировать SPDD, Gas Town or deep specification cluster.
7. SPDD и Gas Town восстанавливать из старого сайта целиком.
8. Specification zone не размывать GSD/BMAD.
9. Evidence package не сводить к tests.
10. Architecture quality and test data must be visible but controlled.
11. Контекстные файлы не романтизировать: more context is not automatically better.
12. Policies and fitness functions must themselves be reviewed and maintained.
13. Все основные пользовательские объяснения писать по-русски; английский оставлять для точных имён и устойчивых терминов.

---

## 5. Selected dossiers / notes before drafting

Перед writing нужны не все возможные dossiers, а selected files:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_AND_TRACEABILITY_NOTE.md
work/dossiers/EXECUTION_CONTROL_SURFACES_NOTE.md
work/dossiers/ARCHITECTURE_QUALITY_AND_FITNESS_FUNCTIONS_NOTE.md
work/dossiers/TEST_DATA_ENVIRONMENTS_AND_ORACLES_NOTE.md
work/dossiers/EVIDENCE_PACKAGE_TAXONOMY_NOTE.md
work/dossiers/LIFECYCLE_TAIL_ARTIFACTS_NOTE.md
work/dossiers/OWNERSHIP_AND_COMPLETION_ARTIFACTS_NOTE.md
```

SPDD and Gas Town dossiers are separate and governed by baseline restore rule.

---

## 6. Следующее практическое действие

После утверждения v4 порядок работы:

```text
Stage A. Create / update selected dossiers and notes.
Stage B. Skeleton v4 of whole document.
Stage C. Specification zone dossiers and baseline restore.
Stage D. Gas Town baseline restore dossier.
Stage E. Evidence package / architecture quality / test data notes.
Stage F. First writing batch: Introduction + Parts I–II.
Stage G. Writing Parts III–V with SPDD/specification depth.
Stage H. Writing Parts VI–IX, including Gas Town.
Stage I. Writing Parts X–XII.
Stage J. Anti-catalog audit.
Stage K. Anti-degradation checks for SPDD and Gas Town.
```

No drafting before at least the selected dossiers/notes that directly affect the relevant part.

---

## 7. Короткая формула v4

```text
AI-driven SDLC — master architecture.
Specification zone — central explanatory knot.
SPDD — standalone deep anchor for intent/specification lifecycle.
Spec Kit, Kiro, TDAD, Constitutional SDD — deeply developed neighboring specification regimes.
Gas Town — standalone deep anchor for organizational/operational lifecycle.
Artifacts — connective tissue across lifecycle stages.
Evidence package — broader than tests.
Completion right — broader than merge.
Lifecycle tail — controlled feedback into specs, tests, policies, context and environment.
Structural synthesis plan — guardrails against catalog structure.
Expanded theory — quarry, not form.
```

---

## 8. Methodology depth contract addendum

Дата: 2026-06-07  
Статус: accepted update after ADR-0008.

### 8.1. Новая ось глубины

С этого момента план различает:

```text
роль в архитектуре теории ≠ глубина изложения
```

Материал может не быть deep anchor, но всё равно требовать protected depth.

### 8.2. Protected methodology profiles

Статус protected methodology profile получают:

```text
Spec Kit
Kiro Specs
Constitutional SDD
TDAD: Test-Driven AI Agent Definition
TDAD: Test-Driven Agentic Development
GSD / Open GSD
BMAD Method
```

SPDD remains deep anchor + full methodology profile.  
Gas Town remains deep anchor as organizational/operational environment case.

### 8.3. Protection rule

Protected methodology profile cannot be reduced to a vague overview. It must reconstruct:

- problem solved;
- workflow;
- artifacts;
- context location;
- roles/agents;
- human gates;
- validation;
- lifecycle tail;
- strengths;
- failure modes;
- contrast with neighboring methods;
- theory vs Handbook/Fieldbook role.

### 8.4. Mandatory comparative syntheses

The final theory must include comparative syntheses:

1. Specification methods: SPDD / Spec Kit / Kiro / TDAD / Constitutional SDD.
2. Process methods: Spec Kit / GSD / BMAD / Reversa / OpenSpec / AgentSPEX / Gas Town.
3. Evidence methods: TDAD / contract tests / architecture fitness / test data / agent traces.
4. Completion/governance: SASE / open-source policies / CODEOWNERS / audit-provenance.

### 8.5. Готовность материала перед написанием Частей V и VII

Части V и VII пишутся по скелетону, а не как сборка заранее готовых будущих документов. Досье и сравнительные отчёты служат материалом готовности: они дают фактуру, источники, технические детали, ограничения и проверочные вопросы, но сами не являются черновыми главами сайта.

Перед написанием Части V или Части VII нужно проверить, хватает ли материала в текущих досье и сравнительных отчётах:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
```

Если профиль не проходит правило защищённого методологического профиля, следующий шаг — дополнительный проход по досье или источникам. Нельзя закрывать слабое место гладкой теоретической прозой поверх недостаточной фактуры. При этом не нужно создавать отдельные “документы будущей теории” до начала письма: теория, технический атлас, Handbook и Fieldbook будут написаны по скелетону и на основе материала, накопленного в `/work`.

### 8.6. Патч скелетона v4.2

Скелетон v4.2 сохраняет архитектуру v4.1 и сравнительные главы, но уточняет четыре границы:

1. ADR получает статус защищённого профиля архитектурного решения внутри Части III. Он не становится третьим deep anchor, но требует раскрытия Nygard, MADR, статусов, reconstructed ADR, operational projection и confirmation.
2. Истории остаются первым разделом сайта. Теория использует их как фактические якоря и не пересказывает сами истории.
3. Технический атлас теперь уточнён поздним решением 2026-06-11 как концептуально-технический атлас, а не узкое техническое приложение. Он по-прежнему опирается на тяжёлые методологические досье — SPDD, Spec Kit, Kiro Specs, Constitutional SDD, TDAD, GSD / Open GSD, BMAD Method, Persistent Work Graph, Gas Town / Beads и ADR, — но его разделы должны быть самостоятельными связными концептуально-техническими статьями. Теория сохраняет поперечный SDLC-синтез; атлас допускает контролируемое повторение теоретических тезисов, если это нужно для самостоятельного понимания конкретной концепции.
4. Готовность к письму формулируется как проверка достаточности материала. Если фактуры мало, сначала проводится проход по источникам или досье; если материала достаточно, пишется глава по скелетону.

---

## Addendum 2026-06-10: Persistent Work Graph как глубокий опорный механизм

После расширения `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` рабочий скелетон обновляется до `v4.3-PWG`.

Решение: `Persistent Work Graph` больше не рассматривается как короткий подпункт части о контексте. Он становится отдельным глубоким опорным механизмом жизненного цикла рабочего состояния.

Обновлённая триада глубоких опорных узлов:

```text
SPDD — глубокий опорный случай спецификационного жизненного цикла.
Persistent Work Graph — глубокий опорный механизм жизненного цикла рабочего состояния.
Gas Town / Beads — глубокий опорный случай организационно-операционного жизненного цикла.
```

При этом `Gas Town / Beads` не сводится к PWG и остаётся отдельной глубокой частью. PWG объясняет переносимый механизм долговечного рабочего состояния; Gas Town показывает, как этот механизм становится частью организационно-операционной среды с ролями, Mayor, service agents, handoff и стоимостью оркестрации.

Технический атлас получает отдельную главу `Persistent Work Graph`. Эта глава должна быть чтение от конкретной концепции статьёй: связно объяснять PWG как концепцию и затем давать объектные модели, source-state схемы, safe parallel source-work protocol, Beads/Taskmaster/LangGraph/STORM/CodeCRDT notes и кандидаты на иллюстрации. Такие детали не должны перегружать теоретическую главу, но в атласе они должны быть встроены в самостоятельное объяснение, а не лежать как несвязанный справочник.


### Addendum 2026-06-11: технический атлас как концептуально-технический атлас

После обсуждения границы theory / atlas принято уточнение: жёсткая формула «теория хранит смысл, атлас хранит технические детали» слишком обедняет атлас и делает его неудобным для читателя, который пришёл за конкретной концепцией, а не за всем поперечным синтезом.

Новая рамка: теория остаётся поперечный объяснением AI-driven SDLC и связей между слоями жизненного цикла изменения; технический атлас становится концептуально-техническим слоем. Его разделы должны быть самостоятельными статьями с опорой на источники по отдельным концепциям, методологиям и инструментальным формам. В таких статьях допустимо контролируемое повторение тезисов из теории, если оно нужно для самостоятельного понимания SPDD, PWG, Gas Town / Beads, TDAD, Spec Kit, Kiro, BMAD, GSD, ADR и соседних концепций.

Атлас не должен становиться ни копией общей теории, ни складом команд, скриншотов и источниковые заметки без связного объяснения. Его ценность — путь чтения от конкретной концепции: читатель может открыть конкретный раздел и получить цельное представление о концепции, её источниках, механике, ограничениях, визуальных материалах и связи с общей SDLC-рамкой.
