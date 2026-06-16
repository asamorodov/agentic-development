# Theory Change Decision

Дата обзора: 2026-06-16  
Назначение: зафиксировать, что именно менять в теоретическом труде после обзора practical agentic development field map.

## 1. Общее решение

**Структурную ось труда не менять.**

Новые источники не требуют новой корневой части. Они усиливают текущую формулу: агентская разработка меняет жизненный цикл программного изменения. Главная недостача — не в оси, а в практической фактуре вокруг:

- early agent loop genealogy;
- repository-native instructions;
- runtime/orchestration layer;
- observability/evaluation/security;
- empirical PR/process evidence.

Рекомендуемый тип изменения: **локальные вставки + несколько расширений глав + отдельная очередь статей Атласа**.

---

## 2. Decisions by chapter

### Introduction

**Decision:** short insertion.

**What to add:** 2–4 абзаца о переходе от autocomplete/chat к agent loop. Упомянуть ReAct, MRKL, Toolformer, Reflexion, Tree of Thoughts как ранние формы: thought/action, tool routing, external modules, verbal self-correction, branching/search.

**Purpose:** дать историко-технический мост. Не углубляться в подробности papers.

**Possible insertion:**

> Агентская разработка выросла не просто из более сильного автодополнения. Уже ранние работы о ReAct, MRKL, Toolformer, Reflexion и Tree of Thoughts сдвинули центр тяжести от «модель сразу выдаёт ответ» к циклу: модель рассуждает, вызывает внешний инструмент или модуль, получает наблюдение, корректирует следующий шаг, иногда удерживает несколько вариантов и выбирает между ними. В разработке программ этот цикл стал особенно важен, потому что действие агента связано не с абстрактной задачей, а с файлами, командами, тестами, issue tracker, diff, branch, PR и правами доступа. Поэтому агентскую разработку нельзя сводить к генерации кода: она начинается там, где изменение становится исполнимой, проверяемой и восстанавливаемой сессией работы.

### Chapter I — Unit of Analysis

**Decision:** no major change.

**Optional insertion:** one sentence: the unit of analysis is not model call, tool call or agent framework, but the whole software change as it moves through intent, execution, trace, verification, acceptance and maintenance.

**Reason:** обзор подтверждает уже принятую главу I. Не надо ломать удачный no-stage result.

### Chapter II — Agentic Session Trace

**Decision:** short insertion.

**What to add:** distinction between:

- chat/dialogue record;
- agent run log;
- technical trace of tool calls/spans;
- verification material;
- acceptance record.

**Important wording:** trace helps reconstruct execution; it does not guarantee correctness.

**Possible insertion:**

> У агентской сессии есть несколько разных следов, и их нельзя склеивать в один термин. Один слой — обычный диалоговый след: что было запрошено и какие ответы были получены. Второй — журнал выполнения: какие файлы агент открыл, какие команды запустил, какие правки сделал, какие проверки прошли или не прошли. Третий — техническая трасса agent runtime: model calls, tool calls, handoffs, spans, guardrail events. Четвёртый — материал принятия: почему это изменение можно или нельзя внести в рабочее состояние проекта. Первые три слоя помогают восстановить ход работы, но только четвёртый отвечает на вопрос, можно ли принять результат.

### Chapter III — Intent / Spec / Contract / ADR

**Decision:** no required change; optional small cross-reference.

**What to add:** ADR/spec/contract can generate or update repository instructions when the pattern becomes recurring.

**Reason:** new material supports the chapter, but main concepts already stand.

### Chapter IV — SPDD / Specification Lifecycle

**Decision:** small optional insertion, probably after Kiro Atlas article.

**What to add:** Kiro as contemporary spec-driven IDE case: requirements/design/tasks, steering, hooks, powers. Use it as evidence that spec-driven agentic development is emerging in products, not only in theory.

**Risk:** do not turn SPDD chapter into Kiro article.

### Chapter V — Protected Specification Profiles

**Decision:** no immediate change.

**Optional:** mention that protected profiles can be materialized through repository instructions, directory-scoped rules, allowed tools, hooks and CI gates.

### Chapter VI — Context / Working State / Interface

**Decision:** chapter expansion.

**Why:** this is the largest gap. Current material on skills/hooks/MCP/subagents should become part of a wider concept: repository configuration and agent-facing interface.

**Add subsections:**

1. **Repository as an agent-facing surface.**  
   `AGENTS.md`, `CLAUDE.md`, Cursor rules, GitHub custom instructions, Kiro steering, Replit workspace instructions.

2. **Instructions-as-Code.**  
   Instructions are not prose decoration; they are operational project assets. They require scope, versioning, review, repair, deletion and tests.

3. **Static instructions vs executable hooks.**  
   Static instructions shape agent behavior; hooks enforce or intercept actions; skills package reusable procedures; subagents isolate roles and context.

4. **Scope and conflict.**  
   Global/user/team/repository/directory/task instructions can conflict. More instructions are not always better.

5. **From failure to instruction repair.**  
   Every serious failed agent run should ask: was the task badly framed, the verification bar missing, the tool permission wrong, or the repo instruction stale?

**External material:** AGENTS.md, Claude Code hooks/skills/subagents, Kiro steering/specs/hooks/powers, GitHub Copilot instructions, Amp manual, Replit customization, Configuring Agentic AI Coding Tools, Toward Instructions-as-Code.

### Chapter VII — Persistent Work Graph

**Decision:** short defensive insertion.

**What to add:** distinguish Persistent Work Graph from runtime graph/state.

**Possible insertion:**

> Agent runtimes often speak about graph state, sessions, memory or durable execution. This is useful, but it is not the same object as persistent project working state. Runtime state belongs to a particular execution system and describes how the agent run proceeds. Project working state belongs to the project and records accepted decisions, live documents, unresolved debts, provenance, handoff conditions and repair obligations. A LangGraph-style graph can help execute an agent workflow; it does not by itself answer what the project now knows or what the next session is allowed to assume.

### Chapter VIII — Protected Process Profiles

**Decision:** no major change.

**Optional:** connect protected process profiles with agent mode selection: local agent, cloud PR, app-builder, harness, spec-driven mode.

### Chapter IX — Execution Environment / Runtime Rights

**Decision:** chapter expansion.

**Why:** MCP/A2A/security/authorization material is too important to remain implicit.

**Add subsections:**

1. **Protocol is not permission.** MCP/A2A define communication/action channels; authorization must be separate.
2. **Tool surface and data boundary.** Tools/resources/prompts, secrets, local files, cloud APIs, admin actions, databases.
3. **Identity and delegation.** Who is acting: user, agent, service account, tool server, delegated identity?
4. **Consent and approval.** Human approval must be tied to action class, not to generic trust.
5. **Prompt injection and tool poisoning.** Tool descriptions and external resources can become attack surfaces.
6. **Sandbox and blast radius.** Worktree/container/cloud sandbox per agent task; no production data by default.

**External material:** MCP intro/authorization/security specs, A2A docs, protocol comparison, AIP, Authenticated Workflows, MCP security papers.

### Chapter X — Gas Town / Beads / Parallel Work

**Decision:** short-to-medium insertion.

**What to add:** connect beads/parallelism with subagents/cloud tasks and PR evidence.

**Possible subsection:** “Parallel agents multiply acceptance work.”

**Core point:** subagents and parallel cloud tasks are not free acceleration. They increase branches, partial results, coordination debt and review burden. The useful unit of parallelism is not “more agents,” but “separable change bead with clear acceptance material.”

### Chapter XI — Verification / Evaluation / Acceptance Evidence

**Decision:** write with expanded source base from the beginning.

**Required distinctions:**

- trace;
- run log;
- eval;
- benchmark;
- project test;
- code review;
- state-diff contract;
- static verification;
- acceptance decision;
- provenance.

**External material:** LangSmith, OpenAI tracing, Agentproof, Agent-Diff, SWE-MERA, SWE-smith, RepoForge, ADK Arena, Where Do AI Coding Agents Fail?.

**Core thesis:** Verification in agentic development is layered evidence. Agent trace shows what happened; tests show some properties; benchmarks show comparative capability; review checks project fit; acceptance records that the project state may now change.

### Chapter XII — Acceptance / Merge Governance / Responsibility

**Decision:** chapter expansion.

**What to add:** empirical PR studies.

**Core thesis:** PR is a socio-technical acceptance object. Agent may produce code, docs and tests, but human maintainers still govern merge. Failures often involve stale task state, duplicate work, reviewer non-engagement, missing rationale, unwanted feature shape or process mismatch.

**Recommended subsection:** “The agent-authored PR as the boundary between execution and project acceptance.”

### Chapter XIII — Maintenance / Learning / Handoff

**Decision:** chapter expansion.

**What to add:** instruction repair and documentation maintenance.

**Core thesis:** Agentic development only matures if failures update durable project artifacts: tests, instructions, package templates, ADRs, checklists, runbooks. Otherwise each session repeats the same mistake with a different model.

**External material:** Instructions-as-Code, documentation PR studies, agentic refactoring, adoption studies.

### Conclusion

**Decision:** short insertion.

**What to add:** practical mode selection table. Choose agent surface by task type/risk:

- local terminal agent for isolated repo work;
- IDE agent for exploratory multi-file edits;
- cloud PR agent for docs/CI/dependency/build maintenance;
- spec-driven IDE for feature work needing requirements/design/tasks;
- open harness for experiments and benchmarks;
- app-builder only for prototypes unless environment isolation is strict.

---

## 3. Cross-cutting terminology

| English term | Recommended Russian use | Note |
|---|---|---|
| trace | след выполнения / техническая трасса | “трасса” for technical spans/tool calls; “след” for broader session reconstruction |
| transcript | диалоговый след / запись диалога | Avoid heavy “стенограмма” unless literal verbatim transcript matters |
| evidence | проверочный материал / материал принятия / основание для принятия | Avoid flattening to “наблюдение” |
| run log | журнал выполнения | Good for commands/files/results |
| runtime state | состояние выполнения | Not project working state |
| project state | рабочее состояние проекта | Accepted, durable, project-owned |
| instruction file | файл инструкций / агентская инструкция репозитория | If conceptual: Instructions-as-Code |
| guardrail | ограничитель / защитное правило / проверочный барьер | Pick by context |
| handoff | передача работы / передача контекста | Avoid unnecessary English glue |

---

## 4. Immediate edits vs later work

### Immediate edits worth doing soon

1. Add ReAct/MRKL/Toolformer/Reflexion/ToT block to introduction.
2. Add trace/log/verification/acceptance distinction to chapter II.
3. Expand chapter VI around Instructions-as-Code.
4. Add runtime graph vs project state defensive paragraph to chapter VII.
5. Expand chapter IX around MCP/A2A/security.

### Better handled while writing pending chapters

1. Chapter XI: verification/eval/tracing/state-diff/static verification.
2. Chapter XII: PR acceptance and merge governance.
3. Chapter XIII: instruction repair, documentation, maintenance, learning loops.
4. Conclusion: mode selection.

### Better handled in Atlas first

1. ReAct → Toolformer → Reflexion genealogy.
2. Instructions-as-Code.
3. LangGraph/ADK/OpenAI Agents SDK runtime comparison.
4. MCP/A2A security and authorization.
5. AI-authored PRs in the wild.

---

## 5. Anti-degradation warning

Do not convert strong chapters into a survey. The purpose is to add factual and conceptual supports, not to turn the theory into “what exists in the field”. The theory should remain written from the author’s axis:

- What is the unit of work?
- What makes a change continuable?
- What must be visible to the next human/agent?
- What can be accepted into project state?
- What must be repaired after failure?
