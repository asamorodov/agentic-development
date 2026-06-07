# Approved document architecture: AI-driven SDLC v3

Working title:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения**

## Top-level structure

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

## Intended movement

The document should move from a single software change to the systems that govern it:

1. The unit is a software change, not a prompt.
2. Actual agentic work is traceable as session/activity, not reducible to a model answer.
3. Intent must become governable.
4. Specification can become a lifecycle artifact, not only a preliminary document.
5. Context and task state become external working infrastructure.
6. Delegation is a choice of work mode, not a tool preference.
7. Execution depends on harness/environment/tool boundaries.
8. Organizational agentic work needs durable roles and memory.
9. Verification must produce evidence, not just confidence.
10. Completion rights remain social/organizational/legal, not model-internal.
11. Maintenance, debt and process learning are part of the lifecycle, not an appendix.

## Deep anchors

- Part II: SWE-chat / Programming by Chat.
- Part IV: SPDD.
- Part V: Spec Kit / Kiro / TDAD / Constitutional SDD.
- Part IX: Gas Town / Beads.
- Part XI: Open-source governance/policy cluster.

## Guardrail

A part must not become a list of sources. Each part needs:

- governing thesis;
- lifecycle function;
- anchor/contrast/drop roles for cases;
- clear transition to adjacent lifecycle stages.
