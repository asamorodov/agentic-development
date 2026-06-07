# Утверждённый проект верхней архитектуры v3

# «Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения»

Дата: 2026-06-05  
Статус: **утверждённая архитектурная версия v3: SPDD отдельной частью; Spec Kit/Kiro/TDAD/Constitutional SDD раскрываются глубоко; SPDD и Gas Town восстанавливаются из старого сайта целиком перед адаптацией.**

Этот документ заменяет прежний approved-draft в части структуры и места спецификационного блока. Он не является финальным текстом теории; это проект верхней архитектуры и рабочий контракт для пересборки `Theoretical_synthesis_rebuilt.md`.

Связанные документы:

- `AI_DRIVEN_SDLC_DOCUMENT_DESIGN_2026_06_05__APPROVED_DRAFT.md` — предыдущий approved draft;
- `SPDD_SEPARATE_PART_EXPERIMENT_2026_06_05.md` — эксперимент, подтвердивший целесообразность отдельной части для SPDD;
- `THEORY_SOURCE_MAP_AI_DRIVEN_SDLC_UPDATED_2026_06_05.md` — обновлённая карта первоисточников;
- `THEORY_STRUCTURAL_SYNTHESIS_PLAN_2026_06_04__REFERENCE.md` — прежний structural synthesis plan как guardrails;
- `SPECIFICATION_CLUSTER_DEEP_PLAN_2026_06_05.md` — детализация спецификационного блока;
- `ANCHOR_CASE_BASELINE_RESTORE_RULE_2026_06_05.md` — обязательное правило восстановления SPDD и Gas Town из старого сайта без начального сжатия.

---

## 0. Зафиксированные решения v3

### 0.1. Главная рамка сохраняется

Финальная теоретическая часть пересобирается вокруг рамки:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения.**

Рамка понимается не как обычная корпоративная последовательность `requirements → design → coding → testing → deployment`, а как lifecycle программного изменения:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

Это петлевая модель. Поздние стадии возвращаются назад и меняют среду: инструкции, спецификации, тесты, hooks, skills, MCP, `AGENTS.md`, review policy, benches, workflow scripts, human gates.

### 0.2. Спецификационная зона становится центральным узлом документа

Решение пользователя: слой намерения / спецификации является, вероятно, **важнейшим местом всего AI-driven SDLC**. Поэтому SPDD не должен быть сжат в подраздел, а соседние спецификационные подходы — GitHub Spec Kit, Kiro, TDAD и Constitutional SDD — не должны оставаться короткими контрастами.

В v3 документ сохраняет специальную **specification zone**:

```text
III. Намерение: почему prompt слишком слаб как единица управления
IV. Deep case: SPDD как спецификационный lifecycle
V. Соседние спецификационные режимы: Spec Kit, Kiro, TDAD, Constitutional SDD
```

Эта зона должна показать, что AI-driven SDLC начинается не с “модель пишет код”, а с превращения намерения в управляемые, проверяемые и сопровождаемые артефакты.

### 0.3. SPDD получает отдельную часть

SPDD становится самостоятельной частью, а не deep block внутри Части III.

Причина: SPDD сейчас является самым цельным методологическим источником в корпусе для слоя intent/specification lifecycle. Он соединяет:

- prompts as first-class delivery artifacts;
- REASONS Canvas;
- OpenSPDD command layer;
- end-to-end пример изменения billing engine;
- генерацию кода из Canvas;
- API-test;
- review/refactor;
- prompt update;
- двустороннюю sync-дисциплину;
- human learning / review trade-off;
- организационную рамку Thoughtworks internal IT.

Если SPDD оставить внутри общей части про намерение, есть риск повторить уже произошедшее с Gas Town: всё будет формально упомянуто, но методологическая сила кейса исчезнет.

### 0.4. Spec Kit, Kiro, TDAD и Constitutional SDD раскрываются глубоко

Решение пользователя: Spec Kit, Kiro, TDAD и Constitutional SDD должны быть раскрыты **глубоко**.

В v3 они сохраняют отдельную часть — не как “конкуренты SPDD”, а как разные формы спецификационного управления:

- **Spec Kit** — toolkit/ecosystem, где specification становится executable workflow с constitution/spec/plan/tasks/implement, templates, scripts, extensions/presets and agent integrations.
- **Kiro Specs** — productized spec workflow на `requirements.md`, `design.md`, `tasks.md`, task execution, `#spec` context, Sync Files и явные review gates.
- **TDAD** — нужно разнести два источника с одинаковым acronym:
  - `Test-Driven AI Agent Definition` — prompt/agent behavior as compiled artifact from behavioral specifications;
  - `Test-Driven Agentic Development` — graph-based code-test impact analysis as agent skill for regression reduction.
- **Constitutional SDD** — security/governance constraints как versioned machine-readable Constitution, с traceability от принципов к коду и security-by-construction.

### 0.5. SPDD не становится универсальным рецептом

Отдельная SPDD-часть не должна превратить текст в апологию SPDD.

Рабочая формула:

```text
SPDD — лучший известный нам deep case для intent/specification lifecycle.
Spec Kit / Kiro / TDAD / Constitutional SDD — соседние спецификационные режимы, раскрывающие другие стороны этого слоя.
Gas Town — другой deep case, уже про organizational/operational lifecycle.
```

### 0.6. «Карта течений» остаётся source/control layer

«Карта течений» не возвращается как верхняя структура. Она остаётся:

- source map;
- материалом для отбора кейсов;
- source-control layer;
- средством не потерять разнообразие практик;
- будущим материалом для Handbook / Fieldbook.

Финальная теория строится не как каталог течений, а как **lifecycle synthesis**.

### 0.7. Expanded-версия остаётся quarry

Expanded-версия после honest-pass cycles используется как material quarry. Её нельзя продолжать механически “полировать” как основной текст.

Из неё переносить:

- фактуру;
- источники;
- удачные формулировки;
- уже найденные связи;
- части SPDD/Gas Town/Spec Kit/Kiro/TDAD/Constitutional SDD, если они полезны.

Не переносить:

- каталожную структуру;
- равноправные source-name headings;
- мелкие кейсы без механизма;
- “всё найденное”, если оно не работает на lifecycle line.

### 0.8. Жёсткое правило для SPDD и Gas Town: сначала старый сайт целиком

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

Цель правила — не музейно сохранить старый текст, а защитить две главные deep-case опоры от повторной деградации. SPDD и Gas Town должны быть подчинены общей структуре, но не ценой потери фактуры, внутренних механизмов и уже достигнутой композиционной силы.

---

## 1. Обновлённая верхняя структура v2

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
X. Свидетельства, тесты, ревью и benchmark validity
XI. Завершение, governance и внешний контур
XII. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

### Почему не оставить 11 частей

Можно было бы объединить SPDD и соседние подходы в одну большую часть. Это опасно: SPDD снова начнёт конкурировать с Spec Kit/Kiro/TDAD/Constitutional SDD за место, и либо SPDD будет сжат, либо соседние подходы останутся поверхностными. Поэтому v2 разделяет:

- **Часть III** — теоретический вход в intent/specification layer;
- **Часть IV** — один центральный deep case: SPDD;
- **Часть V** — глубокая карта соседних спецификационных режимов.

Так спецификационная зона становится тяжёлой, но композиционно управляемой.

---

## 2. Логика документа по частям

## Введение. Почему речь не о генерации кода

### Управляющий тезис

AI-driven SDLC начинается там, где AI перестаёт быть ускорителем набора кода и начинает менять весь lifecycle программного изменения: намерение, контекст, среду исполнения, свидетельства, ревью, governance и сопровождение.

### Функция

Сразу защитить документ от двух неверных чтений:

1. “это про vibe coding / prompt engineering”;
2. “это обычная корпоративная схема SDLC с AI на каждой фазе”.

### Материалы

- DORA 2025 — AI как amplifier существующей организационной системы;
- Bain 2025 — ценность приходит от применения AI по lifecycle и redesign процессов;
- A-SDLC survey / Assistance-to-Autonomy SLR — внешняя проверка, что рамка SDLC является реальной линией обсуждения;
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
5. Переход к эмпирической поверхности реальной сессии.

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
5. Почему сессия требует внешних артефактов намерения.

---

## III. Намерение: почему prompt слишком слаб как единица управления

### Управляющий тезис

AI-driven SDLC начинается не с “лучшего prompt”, а с превращения намерения в внешний, проверяемый и сопровождаемый объект: его можно ревьюить, версионировать, связывать с кодом, обновлять, передавать между людьми и агентами и возвращать в будущий lifecycle.

### Функция

Подготовить спецификационную зону. Эта часть объясняет, почему raw prompt, chat history и даже хороший план недостаточны как единицы управления изменением.

### Подразделы

1. Prompt как ephemeral instruction: почему он не выдерживает SDLC.
2. Intent debt: что теряется, если код живёт дольше намерения.
3. Intent artifact: требования к артефакту намерения.
4. Спектр intent artifacts: prompt, plan, research, spec, constitution, behavior tests.
5. Когда тяжёлый спецификационный режим не нужен.
6. Переход: почему SPDD заслуживает отдельной части.

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
10. Стоимость и границы применимости SPDD.
11. Что SPDD даёт всей AI-driven SDLC рамке.

### Материалы

- Martin Fowler / Thoughtworks SPDD article;
- OpenSPDD repository / commands;
- SPDD iterative review page;
- SPDD Q&A / fragments;
- expanded theory quarry;
- previous SPDD work from current theory.

---

## V. Соседние спецификационные режимы: Spec Kit, Kiro, TDAD, Constitutional SDD

### Управляющий тезис

SPDD не исчерпывает intent/specification layer. Соседние подходы показывают, что спецификация в AI-driven SDLC может быть toolkit, IDE workflow, behavioral compiler, test-impact skill или security constitution. Их нужно раскрыть глубоко, потому что именно здесь видно, как “намерение” становится разными видами управляемой инфраструктуры.

### Функция

Не дать SPDD превратиться в единственный рецепт. Показать спектр спецификационных режимов и их разные trade-offs.

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
   - трехфазный workflow;
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
   - security-by-construction vs reactive security review;
   - banking microservices as case.

5. **Что эти подходы показывают вместе.**
   - specification может быть artifact, workflow, product surface, compiler target, test harness, security constraint layer;
   - глубина спецификации должна соответствовать риску intent drift;
   - тяжёлые режимы нужны не всегда;
   - выбор режима становится задачей Handbook.

---

## VI. Контекст и рабочее состояние: проект как интерфейс агента

### Управляющий тезис

Даже хорошая спецификация не работает в пустоте. Agentic SDLC требует, чтобы проект стал читаемым интерфейсом для агента: с рабочей памятью, инструкциями, context files, research notes, plans, rules, skills and repo conventions.

### Функция

Перейти от “что мы хотим изменить” к “в какой среде агент понимает изменение”.

### Материалы

- AGENTS.md;
- Codex docs;
- Claude Code docs;
- Cursor rules;
- Agentic Context Engineering;
- Boris Tane research/plan;
- HumanLayer research/plan/implement;
- Mark Erikson dev planning.

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
8. Когда нужно отказать агенту.

---

## VIII. Исполнение: среда агента, harness, tools, permissions

### Управляющий тезис

Агентская способность создаётся не только моделью, но и средой исполнения: tools, sandbox, permissions, worktrees, hooks, skills, MCP, subagents, logs, test runners, review surfaces.

### Функция

Показать техническую инфраструктуру AI-driven SDLC после выбора режима.

### Материалы

- Harness Engineering;
- ACI / SWE-agent;
- Codex / Copilot cloud agent / Jules / Claude Code;
- MCP, hooks, skills, subagents;
- configuration / context studies.

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

---

## X. Свидетельства, тесты, ревью и benchmark validity

### Управляющий тезис

Когда генерация дешевеет, центральным дефицитом становятся свидетельства: tests, logs, diffs, PR descriptions, benchmark validity, review capacity и способность процесса учиться на сбоях.

### Функция

Показать evidence layer: как lifecycle получает право двигаться дальше.

### Материалы

- UTBoost;
- over-mocked tests;
- Testing with AI agents;
- Saving SWE-Bench;
- SWE-PolyBench;
- PR / review studies;
- TDAD code-test impact analysis возвращается сюда как evidence bridge.

---

## XI. Завершение, governance и внешний контур

### Управляющий тезис

Operational agency не равна праву завершения. Агент может действовать, но merge, publish, release, accept или reject остаются социально-техническими правами внутри конкретного контура владения.

### Функция

Показать внешний предел AI-driven SDLC.

### Материалы

- SASE;
- Linux kernel coding assistants policy;
- QEMU AI-generated content policy;
- LLVM / Ghostty / Debian / Gentoo / scikit-learn / FastAPI policy cluster;
- GitHub Well-Architected governance.

---

## XII. Хвост lifecycle: сопровождение, долг и обучение среды

### Управляющий тезис

AI-driven SDLC не заканчивается merge. Сбой, drift, technical debt, intent debt, security risk, observability gaps and maintenance burden возвращаются назад и должны менять спецификации, tests, instructions, skills, policies and workflow gates.

### Функция

Замкнуть lifecycle и связать теорию с Handbook.

### Материалы

- DORA / Bain as system-level caution;
- Governing Technical Debt in Agentic AI Systems;
- maintenance papers;
- security/governance materials;
- OpenSSF / Snyk cautiously.

---

## Заключение. Не карта кейсов, а карта выбора режима

### Управляющий тезис

Финальный результат теории — не список “течений” и не методология одного типа, а карта выбора режима программного изменения: какой lifecycle-контур нужен в зависимости от риска намерения, контекста, проверяемости, прав завершения и хвоста сопровождения.

### Функция

Подготовить переход к Handbook / Fieldbook.

---

## 3. Deep / medium / contrast cases v2

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
| DORA / Bain / A-SDLC | Framing | Средняя | Рамочная проверка, не deep case |
| Honk / Roast / Quix | Medium structural cases | Средняя | Использовать только там, где несут механизм |

---

## 4. Обязательные guardrails

1. Не превращать спецификационную зону в каталог “SPDD, Spec Kit, Kiro, TDAD, Constitutional SDD”.
2. Каждая методология должна отвечать на один вопрос: **какую форму управляемого намерения она создаёт?**
3. SPDD раскрывать как lifecycle, а не как набор команд.
4. Spec Kit раскрывать как ecosystem/toolkit, а не просто “ещё SDD”.
5. Kiro раскрывать как productized IDE workflow и collaboration surface.
6. TDAD обязательно disambiguate: два разных TDAD с разными функциями.
7. Constitutional SDD раскрывать не как “security section”, а как security constraints at specification layer.
8. После Part V обязательно вернуться к lifecycle line: context → delegation → execution, иначе документ увязнет в specification zone.
9. Сохранять старую композиционную дисциплину: часть должна нести мысль, кейсы подчинены тезису.
10. Expanded quarry использовать выборочно, не переносить каталожную форму.

---

## 5. Следующее практическое действие

Теперь порядок работы меняется.

Раньше предлагался первый writing batch: `Введение + Части I–II`. После решения о глубокой спецификационной зоне лучше делать так:

```text
Stage A. Skeleton v2 всего документа.
Stage B. Specification zone dossiers:
  - SPDD_DOSSIER.md
  - SPEC_KIT_DOSSIER.md
  - KIRO_DOSSIER.md
  - TDAD_DISAMBIGUATION_AND_DOSSIER.md
  - CONSTITUTIONAL_SDD_DOSSIER.md
Stage C. Specification zone architecture review.
Stage D. Writing batch: Введение + Parts I–III.
Stage E. Writing batch: Part IV / SPDD.
Stage F. Writing batch: Part V / neighboring specification regimes.
Stage G. Anti-catalog audit of Parts III–V.
Stage H. Continue with Parts VI–IX, including Gas Town dossier and draft.
```

Причина: если сначала написать введение и I–II, а затем внезапно раздуть спецификационную зону, документ может получить неправильный ритм. Лучше сразу сконструировать skeleton v2 и dossiers, чтобы начало документа знало, что спецификационная зона будет центральной.

---

## 6. Короткая формула решения

```text
AI-driven SDLC — master architecture.
Specification zone — central explanatory knot.
SPDD — standalone deep anchor for intent/specification lifecycle.
Spec Kit, Kiro, TDAD, Constitutional SDD — deeply developed neighboring specification regimes.
Gas Town — standalone deep anchor for organizational/operational lifecycle.
Structural synthesis plan — guardrails against catalog structure.
Expanded theory — quarry, not form.
```
