# Атлас V2 — подробная карта статей технического слоя

Статус: рабочая карта для пересборки target-group plans.  
Дата: 2026-06-17.  
Основание: ADR-0012, ADR-0013, ADR-0014 и жанровая диагностика ex-A3.

## Назначение

Этот документ — не статья Атласа и не финальная навигация сайта. Это рабочая карта, из которой должны строиться новые планы статей Атласа. Она фиксирует, что именно нужно собрать в досье и какие разделы должна закрыть каждая статья.

Главное правило: статья Атласа строится по техническому слою, а не по жизненному циклу изменения. Она должна показывать реальные технологии, форматы, протоколы, рабочие поверхности, артефакты, ограничения и критерии выбора. Хорошая концептуальная статья без этого payload не считается принятой статьёй Атласа.

## Общая форма статьи

Каждая крупная статья уровня A должна пройти одну и ту же рамку:

```text
слой и его задача
→ классы решений
→ конкретные технологии, протоколы, форматы и рабочие поверхности
→ артефакты, которые они создают или меняют
→ техническая логика работы
→ отличия конкурирующих подходов
→ критерии выбора
→ типовые сбои
→ связи с соседними слоями
```

Перед финальной сшивкой нужен technological payload gate. Мини-досье должны предъявить достаточно фактуры, чтобы читатель после статьи понимал не только смысл слоя, но и то, чем люди реально пользуются.

## Быстрая карта A1–A8

| ID | Рабочее название | Слой | Главный риск подмены |
| --- | --- | --- | --- |
| A1 | Контекстный интерфейс проекта для агента | Где живут правила, знания и процедуры проекта для агента | Свести к списку файлов инструкций |
| A2 | Рабочие поверхности coding agents | Где агент действует над кодом и проектом | Смешать чат, IDE, CLI, облако и PR-agent в один обзор продуктов |
| A3 | Оркестрация и фреймворки агентского исполнения | Как строится управляемый агентский процесс | Написать историю ReAct или каталог фреймворков |
| A4 | Инструменты, протоколы, доступы и полномочия | Как агент получает возможность и право действовать | Уйти в общую философию ответственности или security-обзор |
| A5 | Наблюдаемость, traces и evals | Как видеть, воспроизводить и измерять агентскую работу | Свести к фразе «нужны логи и бенчмарки» |
| A6 | Git, worktree и PR/MR как субстрат агентского изменения | Как результат получает форму change candidate | Спрятать Git внутри CI/review |
| A7 | CI, status checks, review и acceptance gates | Как candidate проходит проверки и решение о статусе | Повторить ex-A3 как теорию принятия |
| A8 | Спецификации, планы и исполняемые процессные артефакты | Как намерение превращается в управляемую работу | Смешать методологии без технического сравнения |

## A1. Контекстный интерфейс проекта для агента

**Назначение слоя.** Показать, как проект становится читаемой и исполнимой средой для агента. Агент должен получать не только текст задачи, но и правила проекта, ограничения, процедуры, стиль, источники правды, точки остановки и способы восстановления.

**Обязательные темы.** `AGENTS.md`; `CLAUDE.md`; Cursor Rules; GitHub Copilot custom instructions; Codex/Amp instructions; Kiro steering; skills; hooks; subagents; project docs; specs; ADR; task package / local working sheet; source manifest; старение и ремонт инструкций после неудачного прогона.

**Мини-досье для пакета.**

1. Инструкционные файлы и область действия: корневые, вложенные, tool-specific и task-specific правила.
2. Steering / project knowledge: постоянные проектные правила, документы как рабочее знание, конфликт и устаревание.
3. Skills/hooks/subagents: что является инструкцией, что процедурой, что автоматическим датчиком, что делегированием.
4. Task-local interface: START.md, рабочий лист, acceptance criteria, source manifest, package contract.
5. Failure and repair: устаревшие правила, over-instruction, missing context, conflict of instructions, recovery update.

**Артефакты слоя.** `AGENTS.md`, nested rules, instruction file, skill file, hook config, subagent profile, steering file, task package, source manifest, local acceptance criteria, rule update note.

**Критерии выбора.** Одноразовая задача или повторяемый процесс; один инструмент или несколько агентов; насколько важно наследование правил; сколько контекста держать в инструкции, а что вынести в документы; где будет repair после ошибки.

**Граница.** Не превращать статью в учебник по каждому инструменту. A1 говорит, где агент получает правила и знания; A2 говорит, где он действует.

## A2. Рабочие поверхности coding agents

**Назначение слоя.** Показать, где агент реально работает: в чате, IDE, CLI, облачной задаче, песочнице, локальном open-source окружении или PR-контуре. Это выбор прав, видимости, воспроизводимости, проверки и стоимости контроля.

**Обязательные темы.** Chat-based coding; IDE agents; CLI agents; cloud coding agents; PR-agent / issue-to-PR mode; sandbox/worktree/devbox; Aider; OpenHands; SWE-agent-подобные среды; Computer Use / browser-use forms для разработки через UI или devtools.

**Мини-досье для пакета.**

1. Chat-based coding: какие артефакты остаются и где границы.
2. IDE agents: локальная навигация, diff, review, редакторская поверхность.
3. CLI agents: shell, commands, repo-wide edits, local checks, approvals.
4. Cloud coding agents and PR agents: remote branch, issue-to-PR, agent-created PR.
5. Open-source execution environments: OpenHands, SWE-agent, Aider-like surfaces.
6. Sandbox/worktree/devbox: изоляция, запуск проверок, воспроизводимость.

**Артефакты слоя.** Chat transcript, local diff, patch, command log, terminal output, worktree, sandbox snapshot, cloud branch, agent-created PR, task run log.

**Критерии выбора.** Нужен ли агенту полный репозиторий; можно ли запускать проверки; кто видит diff и когда; как ограничивается радиус ущерба; можно ли воспроизвести run; насколько удобно передавать результат в review.

**Граница.** Не сравнивать продукты напрямую как `лучший/хуже`. Сравнивать классы рабочих поверхностей. Оркестрационные фреймворки относятся к A3, Git/PR substrate — к A6.

## A3. Оркестрация и фреймворки агентского исполнения

**Назначение слоя.** Показать, как строится управляемый агентский процесс, когда одного агента в одной рабочей поверхности недостаточно: графы, маршрутизация, состояние, роли, повторные попытки, human gates и возобновление процесса.

**Обязательные темы.** ReAct / tool-use loop как базовая форма; LangGraph; OpenAI Agents SDK; Google ADK; AutoGen; CrewAI; LlamaIndex Workflows; самописные workflow runners; state machines; multi-agent orchestration; human-in-the-loop stops; resumable workflows.

**Мини-досье для пакета.**

1. Базовый цикл: reason/act/observe, tool calling, observation, repair.
2. Graph/state frameworks: LangGraph и state-machine подход.
3. Agents SDK / ADK class: agents, tools, handoffs, guardrails, traces.
4. Multi-agent frameworks: AutoGen, CrewAI and role/task orchestration.
5. Workflow/data frameworks: LlamaIndex Workflows and event/workflow models.
6. Self-built orchestration: runner, queue, state file, explicit gates.
7. Human gates and resumability: interrupts, checkpoints, approvals, retries.

**Артефакты слоя.** Graph node, edge, state object, tool call, handoff, run id, checkpoint, interrupt, retry record, workflow event, agent role, route decision, trace link.

**Критерии выбора.** Нужен ли persistent state; есть ли ветвление и параллельные ветки; нужны ли разные роли/агенты; сколько human gates; нужна ли наблюдаемость и replay; сколько стоит поддержка фреймворка; проще ли явный runner, чем общий framework.

**Граница.** Не делать историческую статью про papers. Не делать каталог LangGraph/AutoGen/CrewAI. Главное — какие orchestration patterns они воплощают и когда слой нужен.

## A4. Инструменты, протоколы, доступы и полномочия

**Назначение слоя.** Показать разницу между техническим вызовом инструмента, доступом к данным, полномочием действовать и правом признать результат завершённым.

**Обязательные темы.** Tool/function calling; MCP; A2A; connectors; sandbox permissions; approvals; secret handling; scoped access; audit logs; prompt injection; tool poisoning; data boundaries; organizational policy.

**Мини-досье для пакета.**

1. Tool/function calling: схема вызова, результат, ошибки.
2. MCP connectors and resources: что даёт протокол и какие риски вводит.
3. A2A / agent-to-agent boundaries: где начинается межагентское действие.
4. Approval and permission profiles: allow/ask/deny, scoped actions, human confirmation.
5. Secrets and data boundaries: токены, redaction, минимизация доступа.
6. Prompt injection / tool poisoning: типовые атаки и защитные patterns.
7. Audit and organizational control: logs, policy, revocation, accountability.

**Артефакты слоя.** Tool schema, connector config, MCP server/resource/tool, approval prompt, permission profile, audit log, secret reference, redaction rule, policy file, deny/allow list.

**Критерии выбора.** Насколько опасно действие; какие данные видит агент; можно ли действие отменить; нужен ли человек до вызова или после; как отозвать доступ; что должно логироваться; как ограничить prompt injection через tools.

**Граница.** Не писать общую статью о безопасности ИИ. A4 говорит о праве вызвать действие и границах доступа, а не о праве признать изменение завершённым.

## A5. Наблюдаемость, traces и evals

**Назначение слоя.** Показать, как агентскую работу можно видеть, воспроизводить, сравнивать и измерять.

**Обязательные темы.** Trace; span; tool-call log; run tree; replay/debug surfaces; LangSmith-подобные системы; Langfuse/Phoenix-подобный класс; OpenTelemetry-like vocabulary там, где полезно; eval harnesses; regression evals; golden tasks; automated graders; SWE-bench и близкие coding-agent benchmarks; run comparison.

**Мини-досье для пакета.**

1. Trace model: run, span, tool call, observation, error.
2. Observability platforms: LangSmith/Langfuse/Phoenix classes and what they store.
3. Eval harnesses: local tasks, golden tasks, regression evals, graders.
4. Coding-agent benchmarks: SWE-bench and benchmark-based trust limits.
5. Debug and replay: how traces are used to repair agents/workflows.
6. Metrics and comparison: model/toolchain/prompt/orchestration comparisons.

**Артефакты слоя.** Trace, span, run id, tool-call record, eval dataset, golden task, grader output, benchmark score, regression report, prompt/version comparison, replay link.

**Критерии выбора.** Нужен debug или usage logging; есть ли repeated workflow; нужно ли сравнивать версии; можно ли определить success criteria; кто читает trace; что не покрывает eval.

**Граница.** A5 показывает, как увидеть и измерить run; A7 показывает, как candidate проходит gates; Теория XI объясняет достаточность проверочного материала.

## A6. Git, worktree и PR/MR как субстрат агентского изменения

**Назначение слоя.** Показать, почему version control в агентской разработке становится не фоном, а несущей поверхностью изменения. Агент должен оставлять не только текстовый отчёт, но и изолируемый, сравнимый, ревьюируемый и откатываемый материал.

**Обязательные темы.** Git as baseline; working tree; index; commit; history; diff; patch; branch per task; worktree per agent; commit as checkpoint; PR/MR as change candidate; linked issue; review state; audit trail; merge; squash; rebase; cherry-pick; revert; rollback; bisect; file restore; conflict surface; Git-compatible варианты вроде Jujutsu/Sapling через вопрос совместимости с Git/PR/CI/review контуром.

**Мини-досье для пакета.**

1. Git objects and working states for agentic change.
2. Branch/worktree strategies for agents and parallel tasks.
3. Diff/patch/commit as reviewable and recoverable material.
4. PR/MR as candidate container and provenance surface.
5. Merge/rebase/squash/cherry-pick/revert/bisect as lifecycle operations.
6. Multi-agent conflict patterns: mixed tasks, hidden conflicts, semantic conflicts.
7. Git-compatible alternatives: what they change and what remains Git/PR-compatible.

**Артефакты слоя.** Working tree, index, branch, worktree, commit, diff, patch, PR/MR, linked issue, review state, merge commit, squash commit, rebase history, revert commit, conflict marker, bisect result.

**Критерии выбора.** Одна задача или параллельные agent tasks; нужен ли отдельный worktree; как часто делать commit checkpoints; когда branch должен стать PR; как сохранять readable history; когда squash/rebase/merge commit; как не потерять материал разбора при force push или rebase; как Git слой связан с CI/review gates.

**Граница.** Не превращать статью в учебник Git. Git/PR/MR оформляют candidate; CI/status checks/review/merge rules применяют gates.

## A7. CI, status checks, review и acceptance gates

**Назначение слоя.** Показать, как уже оформленный change candidate проходит проверочные и человеческие контуры перед принятием, отклонением, доработкой или отложенным статусом. Эта статья должна заново пересобрать тему ex-A3, но в техническом разрезе.

**Обязательные темы.** CI systems as class: GitHub Actions, GitLab CI, Azure Pipelines, Buildkite, CircleCI как примеры; required status checks; branch protection; rulesets; test reports; coverage; lint; typecheck; security scans; contract/API compatibility checks; OpenAPI diff; schema compatibility; protobuf breaking checks; consumer-driven contract tests; snapshot/API checks; CODEOWNERS; review comments; approvals; requested changes; AI review tools and bots; merge queue; deployment gates; feature flags; canary; monitoring after merge; accepted/rejected/needs changes/superseded/stale/unknown status vocabulary.

**Мини-досье для пакета.**

1. CI/status check layer: systems, check suites, required checks.
2. Test/report layer: unit/integration/e2e/coverage/lint/type/security scan.
3. Contract/API compatibility layer: OpenAPI/schema/protobuf/consumer contracts/snapshot checks.
4. PR review mechanics: comments, approvals, requested changes, CODEOWNERS.
5. Review automation and AI review: bots, AI review tools, false positives, triage.
6. Merge queue and protected integration: branch protection/rulesets/merge queue.
7. Deployment/rollout signals: feature flags, canary, monitoring, incident/revert feedback.
8. Agent-authored PR statuses: why merged/closed/stale/superseded cannot be read naively.

**Артефакты слоя.** CI run, check suite, status check, test report, coverage report, scan result, contract diff, review comment, approval, requested changes, CODEOWNERS match, merge queue entry, deployment status, rollback/revert signal.

**Критерии выбора.** Какой риск несёт изменение; какие проверки покрывают этот риск; что должно быть required check; где нужен CODEOWNERS/human review; когда AI review помогает, а когда создаёт шум; как защищать главную ветку; когда нужна merge queue; что делать с зелёным CI, который не проверяет главный риск.

**Граница.** Не повторять ex-A3 как теорию статуса. Центральная идея `agent run не равен accepted change` остаётся skeleton, но статья должна быть технической картой gates.

## A8. Спецификации, планы и исполняемые процессные артефакты

**Назначение слоя.** Показать, как намерение становится управляемой работой до кода, вокруг кода и после кода. Этот слой связывает методологический Атлас с новыми техническими статьями: спецификация, ADR, task package, acceptance criteria и handoff становятся не prose, а рабочими артефактами процесса.

**Обязательные темы.** Spec Kit; Kiro specs; SPDD; ADR; BMAD/GSD/TDAD/Constitutional SDD-подобные режимы; issue templates; task packages; START.md; local working sheet; source manifest; acceptance criteria; definition of done; handoff docs; process artifacts as versioned, reviewable, repairable material.

**Мини-досье для пакета.**

1. Specs as process artifacts: Spec Kit, Kiro specs, SPDD.
2. Decision artifacts: ADR, status, supersession, operational projection.
3. Task packages and local execution sheets: START.md, source manifests, acceptance criteria.
4. Methodology profiles: BMAD, GSD/Open GSD, TDAD, Constitutional SDD as protected process forms.
5. Handoff and continuation artifacts: resume files, state notes, checkpoint records.
6. Executable/checkable criteria: tests, confirmation, contract, validation scripts as linked boundaries.
7. Repair loop: how process artifacts are updated after failures or accepted changes.

**Артефакты слоя.** Spec, feature spec, steering file, ADR, task package, START.md, working sheet, source manifest, acceptance criteria, confirmation note, handoff/resume note, supersession record, process profile.

**Критерии выбора.** Насколько изменение дорогое или опасное; нужно ли ревью намерения до кода; нужна ли память решения; должен ли процесс пережить одну сессию; какие критерии можно проверить автоматически; когда достаточно issue template, а когда нужен полноценный package; когда артефакт становится долгом и требует cleanup.

**Граница.** Не повторять старые статьи SPDD/ADR/Spec Kit целиком. Эта статья сравнивает классы process artifacts как технический слой.

## Синхронизация с Теорией

Эта карта является источником для `work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md`. Когда меняется состав A1–A8, нужно обновлять attachment map, чтобы будущие главы Теории знали, какие слои Атласа их заземляют.

Правило: Атлас раскрывает слой технически; Теория берёт из слоя только тот срез, который нужен для жизненного цикла изменения. Если chapter package начинает пересказывать статью Атласа, это ошибка. Если chapter package вообще не привязывает теоретический тезис к техническим слоям, это тоже ошибка.
