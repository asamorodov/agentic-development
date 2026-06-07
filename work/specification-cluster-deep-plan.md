# Deep plan: specification zone

Дата: 2026-06-05  
Статус: рабочий план для глубокой проработки Частей III–V в новой структуре.

---

## 1. Почему specification zone стала центральной

В новой рамке AI-driven SDLC самый важный переход происходит не в моменте генерации кода, а раньше: когда неопределённое намерение превращается в внешний артефакт, который можно:

- прочитать;
- обсудить;
- версионировать;
- ревьюить;
- связать с кодом;
- проверять;
- обновлять;
- передавать агенту;
- использовать в следующем цикле.

Без этого agentic coding остаётся быстрой локальной сессией. С этим появляется lifecycle: намерение переживает чат и становится частью системы разработки.

---

## 2. Часть III: намерение до методологий

### Роль

Часть III должна объяснить, почему `prompt` слишком слаб как единица управления, но не должна подробно раскрывать SPDD/Spec Kit/Kiro/TDAD/Constitutional SDD. Она задаёт вопрос, на который отвечают Parts IV–V.

### Подразделы

1. **Prompt как одноразовый вход.**
   - живёт в моменте;
   - слабо версионируется;
   - плохо ревьюится;
   - теряет “почему” решения;
   - не связывает будущие изменения с исходным намерением.

2. **Intent debt.**
   - код остаётся, намерение исчезает;
   - агент ускоряет производство артефактов, но не гарантирует сохранность смысла;
   - review начинает проверять diff без карты причин.

3. **Intent artifact.**
   - должен быть durable;
   - должен быть пригоден и человеку, и агенту;
   - должен задавать границы действия;
   - должен быть связан с проверкой;
   - должен обновляться.

4. **Порог тяжёлого режима.**
   - не всякая задача требует SPDD/Spec Kit/Kiro;
   - важны риск, доменная чувствительность, повторное использование, compliance, команда, стоимость ошибки.

5. **Переход к deep cases.**
   - SPDD как самый цельный vertical slice;
   - соседние режимы как карта форм specification layer.

---

## 2A. Baseline rule for SPDD

Перед любым rewriting Части IV нужно взять SPDD-раздел из старого сайта целиком и без изменений. Последняя expanded/synthesis-версия не может быть seed для SPDD, потому что задача сейчас — не продолжить сжатый пересказ, а сохранить достигнутую глубину и только затем подчинить её новой AI-driven SDLC рамке.

Обязательные outputs:

```text
baseline_extracts/SPDD_FROM_SITE_BASELINE.md
drafts/part_iv_spdd_seed_unchanged.md
reports/SPDD_BASELINE_STRUCTURE_MAP.md
reports/SPDD_BASELINE_DETAIL_INVENTORY.md
reports/SPDD_ADAPTATION_PLAN.md
reports/SPDD_ANTI_DEGRADATION_CHECK.md
```

Адаптация разрешена только после seed stage. Дополнять можно; сжимать детали нельзя без явного human gate.

## 3. Часть IV: SPDD как deep anchor

### Роль

SPDD должен быть изложен не как “пример”, а как полноценный lifecycle intent artifact.

### Минимальная внутренняя структура

1. Зачем возник SPDD: проблема не в скорости кодинга, а в превращении AI assistance из личной эффективности в team/organization capability.
2. Prompt as first-class delivery artifact.
3. REASONS Canvas: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards.
4. OpenSPDD command workflow.
5. Billing-engine example reconstruction.
6. `/spdd-generate`: generation as downstream operation.
7. `/spdd-api-test`: functional evidence.
8. Iterative review: prompt/code consistency, architecture boundaries, hallucination/correctness checks.
9. `/spdd-prompt-update` and `/spdd-sync`: two-way closed loop.
10. Human review/learning: why fully automated review can miss business intent and weaken learning.
11. Trade-offs: overhead, false confidence, stale Canvas, over-specification.
12. Theory extraction: what SPDD teaches AI-driven SDLC.

### Обязательные вопросы к dossier

- Какие команды действительно core, какие optional?
- Где SPDD отличается от обычного SDD?
- Что именно делает REASONS Canvas сильнее task list?
- Какая часть billing-engine example обязательна для читателя?
- Какие навыки человека SPDD пытается сохранить?
- Где SPDD может быть вреден или чрезмерен?

---

## 4. Часть V: соседние спецификационные режимы

### Роль

Показать, что SPDD — не единственный путь. Но соседние подходы должны быть раскрыты не как список, а как разные архитектурные ответы на вопрос: как сделать намерение управляемым в AI-driven SDLC?

---

## 4.1. GitHub Spec Kit

### Управляющий вопрос

Что происходит, когда specification layer оформляется как open-source toolkit/ecosystem, а не как конкретная методология одного workflow?

### Что раскрывать глубоко

- SDD philosophy: specifications become executable, not discarded scaffolding.
- `/speckit.constitution`: governing principles as project memory.
- `/speckit.specify`: what/why before how.
- `/speckit.plan`: technical plan.
- `/speckit.tasks`: task breakdown.
- `/speckit.implement`: task execution.
- Optional commands: clarify, analyze, checklist.
- Templates/scripts: `.specify`, `specs/`, `plan-template.md`, `spec-template.md`, `tasks-template.md`.
- Extensions and presets: domain/compliance customization.
- Agent integrations, including Codex/Copilot/Claude/others.
- Enterprise constraints and compliance as natural extension.

### Как использовать в теории

Spec Kit — не “хуже SPDD” и не “лучше SPDD”. Он показывает другую форму: specification as portable toolkit and ecosystem. Если SPDD силён как методологический closed loop, Spec Kit силён как generalized scaffolding for agentic SDD.

### Возможная оценка

- Source depth: 8.5–9.
- Structural fit for Part V: 9.
- Может держать крупный раздел: да.
- Не должен становиться отдельной частью: пока нет, если не появится ещё более богатый живой кейс.

---

## 4.2. Kiro Specs

### Управляющий вопрос

Что происходит, когда specification layer становится продуктовой поверхностью IDE?

### Что раскрывать глубоко

- Three key files: `requirements.md` / `bugfix.md`, `design.md`, `tasks.md`.
- Three-phase workflow: requirements/bug analysis → design → tasks.
- Task execution interface with status updates.
- Review gates vs Quick Plan.
- `#spec` context provider.
- Sync Files and scanning already implemented tasks.
- Spec splitting / multiple specs per repo.
- Collaboration surface between product and engineering.

### Как использовать в теории

Kiro важен тем, что показывает не research-methodology и не open-source toolkit, а productized SDLC surface: спецификация становится частью IDE workflow, task execution и context injection.

### Возможная оценка

- Source depth: 8.
- Structural fit for Part V: 8.5.
- Может держать крупный раздел: да.
- Слабость: часть источников продуктовые docs, меньше independent critical evaluation.

---

## 4.3. TDAD: disambiguation

В корпусе есть минимум два разных источника с acronym TDAD. Их нельзя смешивать.

### A. Test-Driven AI Agent Definition

#### Управляющий вопрос

Что происходит, когда объектом спецификации становится не feature code, а поведение tool-using agent?

#### Что раскрывать

- Agent prompts as compiled artifacts.
- Behavioral specifications.
- Coding agent converts specs into executable tests.
- Second coding agent iteratively refines prompt until tests pass.
- Visible/hidden tests to reduce specification gaming.
- Semantic mutation testing.
- Spec evolution scenarios.
- SpecSuite-Core and compliance/grounded analytics/runbook/deterministic enforcement agents.
- Results and limits.

#### Роль

Это ближе к specification layer: поведение агента становится artifact + tests + compiled prompt.

### B. Test-Driven Agentic Development

#### Управляющий вопрос

Что происходит, когда агенту нужно не “делать TDD”, а знать, какие тесты действительно связаны с изменением?

#### Что раскрывать

- Regression risk in coding agents.
- Code-test graph construction.
- Weighted impact analysis.
- Agent skill as static text file queried at runtime.
- Reduction of regressions in SWE-bench Verified setting.
- Surprising result: procedural TDD instructions alone can worsen regressions if they do not provide targeted context.

#### Роль

Это bridge между specification zone и evidence/harness zone. В Part V он показывает, что tests могут стать спецификационным интерфейсом для агента; в Part X он возвращается как evidence/benchmark material.

### Возможная оценка

- TDAD Agent Definition source depth: 7.5–8.5.
- TDAD Agentic Development source depth: 7.5–8.5.
- Structural fit Part V: 8.
- Structural fit Part X: 8.5.

---

## 4.4. Constitutional SDD

### Управляющий вопрос

Что происходит, когда specification layer несёт не только feature intent, но и non-negotiable security/governance constraints?

### Что раскрывать глубоко

- Constitution as versioned, machine-readable artifact.
- Constraints derived from CWE/MITRE Top 25 and regulatory frameworks.
- Security-by-construction vs security-after-generation.
- Banking microservices case: customer management, accounts, transaction processing.
- Traceability from principles to code locations.
- Reported 10 critical CWE vulnerabilities addressed by constitutional constraints.
- Reported 73% reduction in security defects vs unconstrained AI generation.
- Limits: narrow empirical setting, security-specific scope, source status as arXiv/preprint.

### Как использовать в теории

Constitutional SDD показывает, что specification layer может стать governance/security layer. Это не просто “безопасность” в конце SDLC; это перенос security policy в момент формулирования намерения и ограничения генерации.

### Возможная оценка

- Source depth: 8.
- Structural fit Part V: 9.
- Может держать крупный раздел: да.
- Не должен заменять broader governance cluster in Part XI.

---

## 5. Anti-catalog structure for Part V

Part V должна быть глубокой, но не каталожной. Рекомендуемая композиция:

```text
V. Соседние спецификационные режимы
  1. Почему SPDD не исчерпывает specification layer
  2. Spec Kit: specification как переносимый workflow toolkit
  3. Kiro: specification как productized IDE surface
  4. TDAD: specification как behavioral/test contract
  5. Constitutional SDD: specification как security/governance constitution
  6. Сравнение режимов: какой объект они делают управляемым
  7. Вывод для Handbook: как выбирать тяжесть спецификационного режима
```

Объединяющая таблица в конце Part V:

| Подход | Что становится артефактом | Где живёт | Что проверяется | Главный риск |
|---|---|---|---|---|
| SPDD | structured prompt / REASONS Canvas | repo + OpenSPDD workflow | intent/code alignment | overhead, stale canvas |
| Spec Kit | spec/plan/tasks/constitution | `.specify`, `specs/`, agent commands | coverage, consistency, task execution | generic process without domain judgment |
| Kiro | requirements/design/tasks | IDE specs | task progress, spec context | product workflow may hide judgment costs |
| TDAD Agent Definition | behavior spec + compiled prompt + tests | benchmark/harness | behavioral compliance | test gaming, narrow scenarios |
| TDAD Agentic Development | code-test impact graph | agent skill/runtime context | targeted regression tests | incomplete dependency map |
| Constitutional SDD | Constitution/security constraints | versioned machine-readable spec | security traceability | false confidence, narrow domain evidence |

---

## 6. Dossier requirements before writing Parts IV–V

До написания SPDD и Part V нужно создать:

```text
cases/SPDD_DOSSIER.md
cases/SPEC_KIT_DOSSIER.md
cases/KIRO_DOSSIER.md
cases/TDAD_DISAMBIGUATION_AND_DOSSIER.md
cases/CONSTITUTIONAL_SDD_DOSSIER.md
reports/SPECIFICATION_CLUSTER_COMPARISON_MATRIX.md
reports/SPECIFICATION_CLUSTER_SOURCE_GAPS.md
```

Каждый dossier должен иметь:

- source inventory;
- reconstructed workflow;
- artifact model;
- lifecycle role;
- evidence / claims / limits;
- comparison with SPDD;
- what to use in main text;
- what to keep in source map;
- doubts and weak points.

---

## 7. Главное решение для утверждения

Решение уже принято в текущем диалоге:

> SPDD — отдельная часть. Spec Kit, Kiro, TDAD и Constitutional SDD раскрываются глубоко в следующей части как соседние спецификационные режимы.

Оставшееся открытое решение не архитектурное, а процессное:

- писать Parts III–V подряд после dossiers;
- или сначала написать Introduction + Parts I–II, затем вернуться к specification zone.

Моя рекомендация: сначала skeleton v2 + specification dossiers, затем writing batch для Introduction + Parts I–III, затем SPDD, затем Part V.
