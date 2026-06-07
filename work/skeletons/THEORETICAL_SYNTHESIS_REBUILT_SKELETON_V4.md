# Theoretical synthesis rebuilt — skeleton v4.1 with methodology depth contract

Статус: рабочий skeleton перед writing.  
Дата: 2026-06-07.  
Основание: `work/approved-ai-sdlc-plan.md` v4, ADR-0007, ADR-0008, `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`, selected dossiers and comparative audit.

Этот skeleton заменяет предыдущий skeleton v4 как рабочую структуру. Он сохраняет верхнюю AI-driven SDLC архитектуру, но добавляет methodology depth lock: ключевые методологии не могут быть сжаты до обзорных подглав.

## Рабочий принцип

Верхняя рамка остаётся прежней:

```text
AI-driven SDLC = жизненный цикл программного изменения
```

Текст должен идти по жизненным напряжениям, а не по спискам артефактов. Но внутри этого движения ключевые методологии получают защищённую глубину.

## Методологический контракт

### Deep anchors

```text
SPDD
Gas Town / Beads
```

### Protected methodology profiles

```text
Spec Kit
Kiro Specs
Constitutional SDD
TDAD: Test-Driven AI Agent Definition
TDAD: Test-Driven Agentic Development
GSD / Open GSD
BMAD Method
```

Protected profile must cover: problem, workflow, artifacts, context, roles, human gates, validation, lifecycle tail, strengths, failure modes, contrasts, theory/Handbook split.

---

## Введение. Почему речь не о генерации кода

### Задача части

Снять три ложных чтения:

1. это не “как лучше промптить”;
2. это не “обычный SDLC, где в каждую фазу вставили AI”;
3. это не “чем больше агент сгенерировал кода, тем лучше”.

### Ход

1. Код подешевел, но смысл, проверка and ответственность не подешевели автоматически.
2. Агент усиливает существующую систему.
3. Объект анализа — lifecycle изменения.
4. Артефакты нужны только если они переносят изменение через границу lifecycle.
5. Переход: сначала сменить единицу анализа.

---

## I. Единица анализа: программное изменение, а не prompt

### Управляющий тезис

Агентская разработка становится понятной только если смотреть на программное изменение как на контур: намерение, контекст, действие, свидетельства, ревью, право завершения, сопровождение.

### Подглавы

1. Почему `prompt → code` слишком бедная модель.
2. Программное изменение как lifecycle.
3. Артефакт входит в теорию только если несёт функцию.
4. Пять классов артефактов как скрытая матрица.
5. Переход к реальной сессии.

---

## II. Реальная агентская сессия: трасса, вмешательство, выживание результата

### Управляющий тезис

Реальная агентская разработка видна в трассе, но трасса не удерживает всю инженерную работу.

### Сравнительная подглава: SWE-chat / Programming by Chat / How Coding Agents Fail

- SWE-chat показывает трассу действий and tool calls.
- Programming by Chat показывает постепенную спецификацию and session archetypes.
- How Coding Agents Fail показывает рассогласования.

Синтез: session trace is necessary but insufficient.

### Подглавы

1. Трасса как свидетельство, но не вся правда.
2. Progressive specification как нормальная форма.
3. Pushback and correction as signal.
4. Что выживает после сессии.
5. Почему нужна внешняя память.

---

## III. Намерение: почему prompt слишком слаб как единица управления

### Управляющий тезис

AI-driven SDLC начинается с превращения намерения, решения and ограничений во внешние артефакты, которые можно ревьюить, версионировать, связывать с кодом and возвращать в следующий цикл.

### Подглавы

1. Prompt как локальная инструкция.
2. Intent debt.
3. Разные артефакты намерения и решения.
4. Сравнительная подглава: specification, ADR, contract.
5. Quality attribute scenario and test oracle assumption.
6. Когда тяжёлый режим не нужен.
7. Переход к SPDD.

---

## IV. Deep case: SPDD как спецификационный lifecycle

### Управляющий тезис

SPDD показывает, как intent превращается в управляемый спецификационный lifecycle: prompt становится delivery artifact, связанный с generation, tests, review, prompt update and sync.

### Baseline rule

До writing: взять old-site SPDD seed unchanged. Адаптация только после anti-degradation inventory.

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
13. Fit/ROI.
14. What SPDD gives AI-driven SDLC.

---

## V. Protected specification methodology profiles

### Управляющий тезис

SPDD не исчерпывает specification layer. Чтобы получить учебную ценность, соседние методологии нельзя сжимать до краткого обзора. Каждая должна быть реконструирована как protected methodology profile.

### Methodology depth rule

Для каждой методологии раскрыть:

```text
problem → workflow → artifacts → context → roles → human gates → validation → lifecycle tail → strengths → failure modes → contrasts → theory/Handbook split
```

### V.1. Spec Kit как переносимый specification toolkit

Обязательные элементы:

1. Какую проблему решает: превращение спецификаций в переносимый workflow for agentic development.
2. Workflow: constitution → specify → plan → tasks → implement.
3. Артефакты: constitution, spec, plan, tasks, templates, scripts, `.specify`, extensions/presets.
4. Контекст: project memory and principles.
5. Human gates: constitution, plan review, task validation.
6. Validation: analyze/checklist/hooks/extensions.
7. Lifecycle tail: specs and constitution evolve.
8. Сильные стороны: portability, ecosystem, organizational customization.
9. Failure modes: ritual specification, template cargo cult, stale constitution.
10. Contrast: SPDD closed loop vs Spec Kit toolkit.

### V.2. Kiro Specs как продуктовая поверхность specification workflow

Обязательные элементы:

1. Проблема: сделать specification workflow part of IDE/product surface.
2. Workflow: requirements/bug analysis → design → tasks → task execution.
3. Артефакты: `requirements.md` / `bugfix.md`, `design.md`, `tasks.md`, task status.
4. Context: `#spec`, Sync Files, repo scanning.
5. Human gates: review gates vs Quick Plan.
6. Validation: task execution, sync, review checkpoints.
7. Lifecycle tail: specs split, updated, synced with implementation.
8. Strength: productized collaboration surface.
9. Failure modes: shallow specs, Quick Plan overuse, spec drift.
10. Contrast: Kiro IDE surface vs Spec Kit portable toolkit.

### V.3. TDAD comparative protected profile

#### TDAD A: Test-Driven AI Agent Definition

1. Problem: specify behavior of tool-using agent.
2. Workflow: behavioral specs → tests → prompt compilation/refinement.
3. Artifacts: behavioral spec, visible/hidden tests, compiled prompt.
4. Validation: semantic mutation testing, hidden tests.
5. Failure modes: test gaming, narrow behavior, overfit prompt.

#### TDAD B: Test-Driven Agentic Development

1. Problem: reduce coding-agent regressions with targeted test context.
2. Workflow: code-test graph → impact analysis → agent skill → targeted tests.
3. Artifacts: graph, impact weights, skill file, test set.
4. Validation: regression reduction.
5. Failure modes: graph staleness, false targeting, procedural TDD instructions without context.

### V.4. Constitutional SDD как governance inside specification

Обязательные элементы:

1. Problem: security/governance must shape generation before code exists.
2. Workflow: Constitution → constraints → generation → traceability → review.
3. Artifacts: machine-readable Constitution, constraint mappings, traceability reports.
4. Context: CWE/MITRE/regulatory frameworks.
5. Human gates: constitution approval, security review.
6. Validation: security defect reduction claims, traceability.
7. Lifecycle tail: Constitution evolves after incidents/regulatory change.
8. Strength: shifts security left into specification layer.
9. Failure modes: narrow empirical base, false security, overconstraint.
10. Contrast: Constitutional SDD vs policy-as-code vs security review.

### V.5. Comparative synthesis: пять способов сделать намерение управляемым

Сравнить:

- SPDD — method/closed loop.
- Spec Kit — toolkit/ecosystem.
- Kiro — productized IDE surface.
- TDAD — tests as specification of behavior or regression guide.
- Constitutional SDD — governance/security as specification.

Вопрос: which artifact becomes central and what human judgment remains?

---

## VI. Контекст и рабочее состояние: проект как интерфейс агента

### Управляющий тезис

Проект становится интерфейсом агента только тогда, когда состояние работы вынесено из головы и чата в поддерживаемые, проверяемые and ограниченные поверхности. Но больше контекста не значит лучше.

### Подглавы

1. Что агент должен знать, чтобы не действовать вслепую.
2. Где живёт состояние задачи.
3. Почему больше контекста не значит лучше.
4. Как кодовая база становится рабочей поверхностью.
5. Как проект показывает владельцев, правила and runnable path.
6. Где контекст начинает устаревать.

---

## VII. Protected process methodology profiles

### Управляющий тезис

Иногда локальных документов и ручного выбора режима недостаточно. Тогда процесс сам становится артефактом: он задаёт роли, состояние, workflow, проверку and handoff.

### Methodology depth rule

GSD and BMAD must be reconstructed as protected methodology profiles, not shallow contrasts.

### VII.1. Когда достаточно разговора

Small reversible tasks. No methodology overkill.

### VII.2. Когда сначала нужен research or plan

Boris Tane / HumanLayer / Mark Erikson as practice anchors.

### VII.3. Когда нужен spec-first

Bridge to Parts III–V.

### VII.4. GSD / Open GSD как лёгкий контур внешнего состояния

Обязательные элементы:

1. Problem: context rot and long task continuity.
2. Workflow: discuss → plan → execute → verify → ship.
3. Artifacts: state/context files, plans, verification notes.
4. Context: externalized state, fresh-context execution.
5. Roles: human, agent, possible subagents.
6. Human gates: plan approval, verify/ship decision.
7. Validation: verify step, small checkable phases.
8. Lifecycle tail: state cleanup, plan update, context repair.
9. Strength: lightweight process discipline.
10. Failure modes: stale state, false freshness, over-fragmentation.
11. Contrast: GSD vs Spec Kit, BMAD, Gas Town.

### VII.5. BMAD как role-based guided process

Обязательные элементы:

1. Problem: ideation/planning/architecture/implementation need role structure.
2. Workflow: analysis → planning → architecture → implementation, adapted by project scale.
3. Artifacts: role outputs, plans, architecture docs, implementation tasks.
4. Context: guided workflow and role-specific context.
5. Roles: specialized agents / domain experts.
6. Human gates: planning/architecture approval, task execution boundaries.
7. Validation: workflow gates, review, implementation checks.
8. Lifecycle tail: process state, handoff, role outputs.
9. Strength: role-based organization and guided flow.
10. Failure modes: role theater, overprocess, shallow expert simulation.
11. Contrast: BMAD vs GSD, Spec Kit, Gas Town.

### VII.6. Reversa / OpenSpec / AgentSPEX as adjacent forms

Shorter protected-adjacent treatment:

- Reversa: recovering operational specs from legacy.
- OpenSpec / AgentSPEX: agent workflow specification and portability.
- Role: support process-as-artifact spectrum, not deep anchor.

### VII.7. Comparative synthesis: когда процесс становится артефактом

Compare:

- Spec Kit — specification toolkit.
- GSD — lightweight context/process loop.
- BMAD — role-based guided process.
- Reversa/OpenSpec/AgentSPEX — recovery or workflow specification.
- Gas Town — full organizational environment.

Question: what is the central artifact and what human control remains?

### VII.8. Когда агенту надо отказать

Risk, irreversibility, missing context, weak evidence, unclear owner.

---

## VIII. Исполнение: среда агента, harness, tools, permissions

### Управляющий тезис

Среда исполнения должна не только дать агенту способность действовать, но и сделать действие ограниченным, воспроизводимым, наблюдаемым and обратимым.

### Подглавы

1. Возможность действовать.
2. Граница действия.
3. Сравнительная подглава: Harness / Sandvault / platform agents.
4. Воспроизводимость действия.
5. Исполняемые ограничения.
6. След действия.
7. Где environment itself becomes debt.

---

## IX. Deep case: Gas Town / Beads как организационно-операционный lifecycle

### Управляющий тезис

Gas Town показывает, как агентская разработка становится организационной средой: роли, память задачи, управляющие поверхности, сервисные агенты, handoff and orchestration cost.

### Baseline rule

Start from old-site Gas Town seed unchanged.

### Подглавы

1. Почему Gas Town нельзя оставлять одним обзорным разделом.
2. Roles: organizational functions.
3. Mayor: visibility and control.
4. Agent is not session.
5. Beads as data/control/why layer.
6. GUPP, hooks, molecules, wisps.
7. Refinery, Witness, Deacon.
8. Session continuation and handoff.
9. DoltHub contrast.
10. Cost: throughput vs understanding.
11. What Gas Town gives AI-driven SDLC.

### Bridge

Contrast GSD/BMAD/Gas Town only to explain why Gas Town is deeper, not to reduce Gas Town.

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
7. Надёжность доказательства: данные, среда, oracle.
8. Социальная проверка.
9. Трасса выполнения.
10. Evidence package as decision support.

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
6. Внешний контур and AI-generated contributions.
7. Восстановимость завершения.

---

## XII. Хвост lifecycle: сопровождение, долг и обучение среды

### Управляющий тезис

Merge не завершает lifecycle. Настоящий хвост изменения — момент, когда его последствия возвращаются в спецификации, тесты, политики, контекстные файлы, skills and workflow gates.

### Подглавы

1. Release feedback.
2. Incident feedback.
3. Drift feedback.
4. Сравнительная подглава: incident / stale ADR / context cleanup.
5. Supply/security feedback.
6. User-facing memory.
7. Возврат в начало.

---

## Заключение. Не карта кейсов, а карта выбора режима

### Управляющий тезис

Финальная теория должна дать карту выбора режима изменения: сколько внешней структуры нужно в зависимости от риска, обратимости, проверяемости, владельца and хвоста сопровождения.

### Финальная сравнительная рамка

```text
conversation → research/plan → spec → methodology/framework → controlled environment → evidence → completion → lifecycle repair
```

---

## Required next dossiers before writing

Before writing Part V and VII:

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

Before writing Part IV and IX:

```text
work/dossiers/SPDD_BASELINE_DOSSIER.md
work/dossiers/GAS_TOWN_BASELINE_DOSSIER.md
```

Before writing final prose:

```text
language pass
anti-catalog audit
SPDD/Gas Town anti-degradation check
```

## Skeleton quality gates

For every methodology section:

1. Does it satisfy protected methodology profile checklist?
2. Does it compare against neighboring methods?
3. Does it preserve lifecycle line?
4. Does it avoid shallow summary?
5. Does it say what goes to Handbook/Fieldbook?
