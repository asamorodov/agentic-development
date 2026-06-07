# Эксперимент: SPDD как отдельная часть

Дата: 2026-06-05

Рабочее название документа:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения**

Цель эксперимента: проверить, будет ли новая архитектура сильнее, если **SPDD вынести из Части III в отдельную часть**, а не держать его как deep block внутри главы про намерение.

---

## 1. Короткий вывод

Я считаю, что вариант с отдельной частью для SPDD **лучше текущего утверждённого варианта**, если мы действительно хотим построить не обзор течений, а сильную теорию AI-driven SDLC.

Причина не в том, что SPDD «интересный кейс». Причина в другом: SPDD сейчас является самым полным методологическим источником в нашем корпусе для слоя **intent/specification lifecycle**. Он показывает не отдельный приём, а почти полный контур:

```text
business intent → story → analysis context → REASONS Canvas → generation → API test → review/refactor → prompt update / sync → reusable governed asset
```

Если оставить SPDD как подраздел внутри Части III, есть высокий риск повторить уже случившуюся ошибку с Gas Town: формально всё будет упомянуто, но методологическая сила кейса будет сжата до резюме.

Поэтому экспериментальный вариант:

```text
Часть III. Намерение: почему prompt слишком слаб как единица управления
Часть IV. Deep case: SPDD как спецификационный lifecycle
```

а все последующие части сдвигаются дальше.

---

## 2. Поправка к исходной интуиции: SPDD действительно единственный такой?

Твоя формулировка в целом верна, но требует точной оговорки.

**SPDD не единственный spec-driven / AI-assisted methodology в абсолютном смысле.** В корпусе есть соседние сильные материалы:

- GitHub Spec Kit — зрелый toolkit для Spec-Driven Development, с процессом `Spec → Plan → Tasks → Implement`, Markdown-артефактами, интеграциями с агентами и расширяемой экосистемой.
- Kiro Specs — продуктовый workflow на `requirements.md`, `design.md`, `tasks.md`, с task execution, sync files, `#spec` context и выбором между Quick Plan и стандартным spec flow.
- Constitutional SDD — специальная методология для security-by-construction через машинно-читаемую Constitution.
- Spec Kit Agents — исследовательский workflow с context-grounding hooks и validation hooks.
- TDAD — важный подход, где тестируемым объектом становится поведение агента.

Но **SPDD сейчас единственный материал в корпусе, который одновременно имеет**:

1. качественную методологическую статью;
2. явный организационный контекст Thoughtworks internal IT;
3. named structure — REASONS Canvas;
4. end-to-end tutorial example на изменении billing engine;
5. командный слой OpenSPDD;
6. version-controlled prompt artifacts;
7. двусторонний lifecycle `requirements → prompt → code` и `code → prompt`;
8. встроенные review/test steps;
9. явное обсуждение человеческих навыков: alignment, abstraction-first, iterative review;
10. явное позиционирование как организация-level capability, а не личная привычка одного разработчика.

Именно поэтому SPDD можно считать не просто одним из кейсов, а **главным deep anchor для слоя намерения**.

Моя рабочая оценка:

| Источник / методология | Source depth | Structural fit для intent/spec layer | Может ли держать отдельную часть? | Комментарий |
|---|---:|---:|---|---|
| SPDD / OpenSPDD | 10.5–11 | 10 | Да | Самый цельный вертикальный срез intent lifecycle |
| GitHub Spec Kit | 8.5–9 | 8.5 | Скорее нет, но может держать крупный контраст | Сильный toolkit/ecosystem, но менее удобен как единый нарративный case |
| Kiro Specs | 7.5–8 | 8 | Нет | Хороший product workflow; лучше как medium contrast |
| Constitutional SDD | 7.5–8.5 | 7.5–8 | Нет в общей теории | Сильный, но узкий security-слой |
| Spec Kit Agents | 7.5–8 | 8 | Нет | Хороший bridge к context/harness, не центральный lifecycle case |
| TDAD | 7–7.5 | 7.5–8 | Нет | Лучше как bridge к verification / Part VIII |
| V-Bounce / AI-native SDLC | 5.5–6.5 | 5.5–6 | Нет | Полезен как осторожный контраст, не как опора |

---

## 3. Текущий утверждённый вариант

Текущий approved design:

```text
Введение. Почему речь не о генерации кода
I. Единица анализа: программное изменение, а не prompt
II. Реальная агентская сессия: трасса, вмешательство, выживание результата
III. Намерение: от запроса к артефакту управления
    - deep block: SPDD
IV. Контекст и рабочее состояние: проект как интерфейс агента
V. Делегирование: выбор режима работы, а не выбор инструмента
VI. Исполнение: среда агента, harness, tools, permissions
VII. Deep case: Gas Town / Beads как организационно-операционный lifecycle
VIII. Свидетельства, тесты, ревью и benchmark validity
IX. Завершение, governance и внешний контур
X. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

### Сильные стороны текущего варианта

1. Он компактнее: SPDD находится там, где по смыслу естественно возникает — в части про намерение.
2. Lifecycle быстрее движется дальше: intent → context → delegation → execution.
3. Меньше риск, что начало документа станет слишком тяжёлым.
4. Часть III может связать SPDD, Spec Kit, Kiro, TDAD и Constitutional SDD в одну карту intent-artifacts.

### Слабые стороны текущего варианта

1. SPDD может быть снова сжат как Gas Town в expanded-версии.
2. Часть III начинает выполнять сразу две разные функции: объяснить слой намерения и раскрыть полноценную методологию.
3. Secondary materials могут размыть SPDD, хотя должны быть контрастами.
4. В тексте появится асимметрия: Gas Town получает отдельную часть, а SPDD — только большой подраздел, хотя по силе источников SPDD не слабее.
5. Если SPDD будет раскрыт действительно подробно, Часть III может стать чрезмерно тяжёлой и композиционно неоднородной.

---

## 4. Экспериментальный вариант: SPDD как отдельная часть

```text
Введение. Почему речь не о генерации кода
I. Единица анализа: программное изменение, а не prompt
II. Реальная агентская сессия: трасса, вмешательство, выживание результата
III. Намерение: почему prompt слишком слаб как единица управления
IV. Deep case: SPDD как спецификационный lifecycle
V. Контекст и рабочее состояние: проект как интерфейс агента
VI. Делегирование: выбор режима работы, а не выбор инструмента
VII. Исполнение: среда агента, harness, tools, permissions
VIII. Deep case: Gas Town / Beads как организационно-операционный lifecycle
IX. Свидетельства, тесты, ревью и benchmark validity
X. Завершение, governance и внешний контур
XI. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

Главное отличие: **часть про намерение становится теоретическим входом**, а SPDD получает собственную часть как полный vertical slice.

---

## 5. Проект Части III в экспериментальном варианте

## Часть III. Намерение: почему prompt слишком слаб как единица управления

### Управляющий тезис

AI-driven SDLC начинается не тогда, когда разработчик пишет хороший prompt, а тогда, когда намерение становится внешним, проверяемым и сопровождаемым объектом: его можно пересматривать, связывать с кодом, проверять, обновлять и передавать между людьми, агентами и стадиями lifecycle.

### Функция части

Подготовить место для SPDD, не растворяя SPDD в общей теории. Часть III должна объяснить, почему raw prompt, chat history и даже хороший план недостаточны как единицы управления изменением.

### Внутренняя структура

1. **Почему prompt не выдерживает SDLC.**
   - prompt живёт в моменте;
   - плохо версионируется;
   - слабо ревьюится;
   - часто не сохраняет причины решений;
   - плохо связывает бизнес-намерение, domain model, code diff и future maintenance.

2. **Intent artifact как новая единица управления.**
   - должен переживать сессию;
   - должен быть читаем человеком и агентом;
   - должен задавать границы генерации;
   - должен быть связан с проверкой;
   - должен обновляться при изменении требований или кода.

3. **Спектр артефактов намерения.**
   - prompt;
   - plan.md;
   - research.md;
   - requirements/design/tasks;
   - constitution;
   - REASONS Canvas;
   - agent behavior tests.

4. **Почему не всякая задача требует тяжёлого спецификационного режима.**
   - быстрый локальный diff;
   - знакомая область;
   - низкая цена ошибки;
   - одноразовое исследование;
   - нефиксируемая exploratory работа.

5. **Переход к SPDD.**
   - если intent risk высок;
   - если изменение должно быть reusable/reviewable/governable;
   - если нужен накопительный актив;
   - если важно удержать связь business intent → code → future evolution.

### Anchor / contrast materials

- Коротко: GitHub Spec Kit, Kiro, Promptware papers.
- Не раскрывать глубоко: все они готовят поле для SPDD, но не замещают его.

---

## 6. Проект новой отдельной Части IV: SPDD

## Часть IV. Deep case: SPDD как спецификационный lifecycle

### Управляющий тезис

SPDD показывает, как AI-driven SDLC может превратить намерение в управляемый спецификационный контур: prompt перестаёт быть одноразовым входом модели и становится version-controlled delivery artifact, который задаёт границы генерации, поддерживает ревью, проверку, обновление и повторное использование.

### Функция части

Дать первый большой deep anchor всей теории. Это не «пример spec-first», а развёрнутый случай, на котором читатель должен понять, что значит lifecycle-мышление в AI-assisted development.

### Внутренняя структура

1. **Зачем SPDD возник.**
   - проблема personal productivity vs organization-level capability;
   - generated code ускоряет misunderstanding, если intent не управляется;
   - review bottleneck растёт вместе с объёмом изменений;
   - production risk становится труднее рассуждать, если изменение не привязано к явному намерению.

2. **Prompt as first-class delivery artifact.**
   - prompt хранится с кодом;
   - версионируется;
   - ревьюится;
   - переиспользуется;
   - улучшается;
   - связывает business needs и implementation boundary.

3. **REASONS Canvas как форма intent → design → execution → governance.**
   - Requirements;
   - Entities;
   - Approach;
   - Structure;
   - Operations;
   - Norms;
   - Safeguards.

4. **Командный слой OpenSPDD.**
   - `/spdd-story`;
   - `/spdd-analysis`;
   - `/spdd-reasons-canvas`;
   - `/spdd-generate`;
   - `/spdd-api-test`;
   - `/spdd-prompt-update`;
   - `/spdd-sync`;
   - возможно `/spdd-code-review`, если решим включать Q&A/roadmap материал.

5. **End-to-end пример billing engine.**
   - current system;
   - enhancement: model-aware pricing / multi-plan billing;
   - story generation;
   - clarification and shared alignment;
   - analysis context через relevant-code scan;
   - REASONS Canvas как executable blueprint;
   - generation task by task;
   - API test script;
   - code review and cleanup;
   - regression test;
   - prompt update when requirements change;
   - sync when code changes.

6. **Двусторонняя синхронизация как главное отличие от обычной спецификации.**
   - requirements → prompt → code;
   - code → prompt;
   - спецификация не становится историческим снимком;
   - следующий цикл начинает не с пустого чата, а с накопленного актива.

7. **Human-in-the-loop в SPDD.**
   - alignment;
   - abstraction-first;
   - iterative review;
   - agent can check alignment mechanically, but human must still validate business intent;
   - review is also a learning surface.

8. **SPDD как semi-automated harness.**
   - commands encode repeatable thinking strategies;
   - artifacts become stable enough for review/governance;
   - automation ratio can grow only after each step proves reliable.

9. **Границы применимости.**
   - SPDD тяжёлый;
   - не нужен для каждой локальной задачи;
   - лучше подходит для intent-heavy, domain-sensitive, reusable, compliance-sensitive, multi-person changes;
   - может породить false confidence, если Canvas устарел или плохо проверен.

10. **SPDD среди соседних подходов.**
    - Spec Kit — более широкий toolkit/ecosystem;
    - Kiro — product workflow на `requirements/design/tasks`;
    - Constitutional SDD — безопасность как constraint layer;
    - TDAD — поведение агента как тестируемый объект;
    - Promptware papers — теоретическое обоснование prompt-as-artifact.

11. **Что SPDD даёт всей теории.**
    - намерение как durable asset;
    - specification as executable boundary;
    - code generation as downstream operation;
    - review before and after code;
    - evidence and prompt/code alignment;
    - intent debt как реальный риск;
    - bridge к следующей части: даже лучшая спецификация нуждается в контексте проекта.

---

## 7. Сравнение: текущий вариант vs SPDD отдельной частью

| Критерий | SPDD внутри Части III | SPDD отдельной Частью IV | Оценка |
|---|---|---|---|
| Сохранение глубины SPDD | Среднее: можно, но велик риск сжатия | Высокое: часть сама требует глубины | Преимущество отдельной части |
| Плавность lifecycle | Выше: intent сразу переходит к context | Чуть ниже: появляется большая остановка на case | Преимущество текущего, но не решающее |
| Композиционная ясность | Часть III перегружена двумя функциями | Теория intent и deep case разведены | Преимущество отдельной части |
| Риск каталога кейсов | Средний: SPDD конкурирует с Spec Kit/Kiro/TDAD | Ниже: secondary materials подчинены SPDD | Преимущество отдельной части |
| Симметрия с Gas Town | Слабая: Gas Town отдельная часть, SPDD нет | Сильная: два deep vertical slices | Преимущество отдельной части |
| Риск whitepaper-структуры | Низкий | Низкий/средний | Не критично |
| Риск “SPDD как универсальный рецепт” | Средний | Средний/высокий, если плохо написать | Требуется оговорка о границах применимости |
| Удобство для Handbook | Хорошее | Очень хорошее: отдельный mode/case extraction | Преимущество отдельной части |
| Читательский темп | Быстрее | Тяжелее, но содержательнее | Зависит от исполнения |
| Защита от повторения ошибки с Gas Town | Недостаточная | Сильная | Преимущество отдельной части |

---

## 8. Главный риск отдельной SPDD-части

Риск не в том, что документ станет длиннее. Риск в том, что SPDD начнёт выглядеть как **главная авторская методология**, а всё остальное — как приложения к ней.

Этого нельзя допустить.

Правильная формулировка:

```text
SPDD — не универсальный рецепт агентской разработки.
SPDD — лучший известный нам deep case для одного слоя AI-driven SDLC: превращения намерения в управляемый спецификационный контур.
```

Так же Gas Town — не универсальный рецепт организации. Это лучший deep case для другого слоя: организационно-операционной агентской среды.

Их надо держать как два полюса:

```text
SPDD → intent/specification lifecycle
Gas Town → organizational/operational lifecycle
```

---

## 9. Рекомендуемое решение

Я рекомендую принять вариант с **SPDD как отдельной частью**.

Не потому, что нужно увеличивать документ, а потому что это решает сразу четыре проблемы:

1. защищает единственный действительно глубокий методологический case от сжатия;
2. делает структуру симметричной: SPDD и Gas Town как два deep anchors;
3. разгружает Часть III, оставляя ей чистую функцию — объяснить слой намерения;
4. переводит secondary spec-driven materials в правильную роль: не конкуренты SPDD, а контрасты и расширения.

Обновлённая рекомендуемая архитектура:

```text
Введение. Почему речь не о генерации кода
I. Единица анализа: программное изменение, а не prompt
II. Реальная агентская сессия: трасса, вмешательство, выживание результата
III. Намерение: почему prompt слишком слаб как единица управления
IV. Deep case: SPDD как спецификационный lifecycle
V. Контекст и рабочее состояние: проект как интерфейс агента
VI. Делегирование: выбор режима работы, а не выбор инструмента
VII. Исполнение: среда агента, harness, tools, permissions
VIII. Deep case: Gas Town / Beads как организационно-операционный lifecycle
IX. Свидетельства, тесты, ревью и benchmark validity
X. Завершение, governance и внешний контур
XI. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

---

## 10. Практическое следствие для следующей работы

Если это решение утверждается, следующий порядок должен измениться.

Вместо:

```text
Введение + Части I–II
Часть III + SPDD deep block
```

лучше:

```text
Batch A: Введение + Части I–III
Batch B: SPDD dossier
Batch C: Часть IV / SPDD standalone draft
Batch D: Parts V–VII
Batch E: Gas Town dossier + Part VIII
Batch F: Parts IX–XI + conclusion
```

При этом Batch B должен быть не “собери краткое описание SPDD”, а полноценный dossier:

```text
cases/SPDD_DOSSIER.md
- source inventory
- workflow reconstruction
- REASONS Canvas breakdown
- command matrix
- billing-engine example reconstruction
- prompt/code sync mechanics
- human review / skill layer
- fitness/tradeoff assessment
- theory extraction
- source gaps / weak points
```

---

## 11. Что надо поправить в approved design

Если принимаем этот эксперимент, то в `AI_DRIVEN_SDLC_DOCUMENT_DESIGN_2026_06_05__APPROVED_DRAFT.md` надо изменить:

1. Раздел `0.5. Deep anchor cases`: SPDD получает explicit standalone part status.
2. Раздел `2. Предлагаемая верхняя структура`: заменить 10 частей на 11 частей.
3. Раздел `6. Часть III`: убрать SPDD из deep block, оставить переход к нему.
4. Добавить новый раздел `Часть IV. Deep case: SPDD как спецификационный lifecycle`.
5. Перенумеровать последующие части.
6. В `17. Оставшиеся открытые решения` заменить вопрос `Part III deep block vs separate Part IIIA` на принятое решение, если пользователь его утверждает.

---

## 12. Итог

Да: опасение по поводу ужима SPDD оправдано.

Да: среди текущих источников SPDD — самый сильный и самый цельный методологический case уровня SPDD=10, возможно 10.5–11 в новой AI-SDLC рамке.

Нет: SPDD не единственный spec-driven approach вообще; Spec Kit, Kiro, Constitutional SDD, TDAD и Spec Kit Agents важны. Но они не дают такого же сочетания narrative depth, workflow detail, commands, artifact lifecycle, prompt/code synchronization и organizational framing.

Мой выбор после эксперимента: **делать SPDD отдельной частью**.
