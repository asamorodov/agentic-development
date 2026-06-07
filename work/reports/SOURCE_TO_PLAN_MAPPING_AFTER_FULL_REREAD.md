# Source-to-plan mapping after full reread

Дата: 2026-06-07  
Статус: карта связи между перечитанными источниками и предлагаемым patch.

Этот файл не является source map. Он показывает, какие группы источников реально работают на какие части будущей теории.

## 1. Старый `content/Theoretical_synthesis.md`

### Что даёт

- Композиционный baseline.
- Сильную линию “запрос → рабочая среда”.
- Развёрнутый SPDD.
- Развёрнутый Gas Town.
- Базовую теорию свидетельств, ответственности and автономии.

### Что сохранить

- Движение по слоям, а не каталог.
- SPDD and Gas Town detail density.
- Русский инженерный стиль.
- Связи с Handbook.

### Где используется

- Все части как композиционный benchmark.
- Parts III–V for SPDD/specification.
- Part IX for Gas Town.
- Parts X–XI for evidence/responsibility.
- Part XII for feedback into environment.

## 2. `work/expanded-quarry-theoretical-synthesis.md`

### Что даёт

- Современные источники и эмпирический слой.
- Реальные сессии / PR / misalignment.
- SASE and open-source policy cluster.
- Расширенный evidence/review/security set.
- Предупреждение о каталожной форме.

### Что не брать

- Верхнюю структуру “карты течений”.
- Равноправные source-name headings.
- Сжатую Gas Town форму.
- Слишком частое добавление новых кейсов без deep role.

## 3. `content/Cross_story_synthesis.md`

### Что даёт

- Практические оси: plan before code, research, evidence, sandbox, worktrees, external memory, review package.
- Конфликты: скорость vs смысл, автономия vs review burden, documents vs noise, skills vs methodology.
- Переход к Handbook: режимы работы, а не универсальная методология.

### Как использовать

- Part I and conclusion: map of regime choice.
- Part VI/VII: context, plan, external memory, process repair.
- Part X/XI: review package and human attention.

## 4. Истории

### Boris Tane

Role: research/plan/implement and document surface before code.  
Use: Part VI/VII, `research.md`, `plan.md`, intent/context boundary.

### Peter Steinberger

Role: fast conversational expert mode and limited radius.  
Use: Part VII as contrast: not every task needs heavy artifact stack.

### Simon Willison

Role: research as artifact, Showboat/benchmarks/transcripts, evidence through experiments.  
Use: Part II, Part X, evidence package.

### Arvid Kahl

Role: browser/runtime verification and SaaS responsibility.  
Use: Part VIII/X, runtime evidence and user-facing checks.

### Jökull Sólberg

Role: PR triage, Fix/Dismiss/Escalate, review comments as signals.  
Use: Part X/XI, review package and human gate.

### Jesse Vincent

Role: Superpowers, gates, hooks, session drivers.  
Use: Part VIII, policy/gates/hooks/process repair.

### HumanLayer

Role: harness, context budget, MCP, skills, subagents, back-pressure.  
Use: Part VI/VIII, project/interface and environment.

### Mike McQuaid

Role: Sandvault, worktrees, sandbox, maintainer policy.  
Use: Part VIII/XI, controlled autonomy and maintainer boundary.

### Calvin French-Owen

Role: practical agentic workflow reconstruction.  
Use: Part VII/VIII, local modes and process discipline.

### Mark Erikson

Role: code appears faster than meaning can be recovered.  
Use: Part I/VI/X, intent/context and meaning preservation.

### Mae Capozzi

Role: workflow/trace/process examples.  
Use: Part VIII/X, trace and validation surfaces.

### Matt Pocock / skills

Role: skills, ADR-like memory, handoff, reusable procedures.  
Use: Part VI/VIII/XII, skills as process repair and reusable context.

## 5. New Stage 0.5–0.9 sources

### ADR / decision provenance

Use: Part III/VI/X/XI/XII.  
Depth: medium-deep.  
Function: preserve why, alternatives, consequences and decision compliance.

### GSD / BMAD / process frameworks

Use: Part VII, supported by Part VI.  
Depth: medium unless dossiers prove more.  
Function: installed process layer, not specification layer.

### Contracts / traceability

Use: Part III/V/X/XII.  
Depth: medium.  
Function: connect intent, boundary behavior, implementation and evidence.

### Codebase readiness / context files

Use: Part VI/XII.  
Depth: medium.  
Function: explain why project state, tests, context files and feedback loops determine agent reliability.

### Reproducible environment / policy-as-code / secrets

Use: Part VIII/XI/XII.  
Depth: medium-short.  
Function: execution control surface.

### Observability / agent traces

Use: Part VIII/X.  
Depth: medium.  
Function: evidence and trajectory-level accountability.

### SBOM / supply chain

Use: Part XII/security-provenance.  
Depth: short-medium.  
Function: lifecycle tail and dependency/provenance.

### Human review / DevEx

Use: Introduction/I/X/XI.  
Depth: medium.  
Function: prevent activity-centric productivity story.

### Artifact graph / catalog / platform

Use: hidden organizing model; light mentions in Part VI/XI.  
Depth: short.  
Function: integration, not new theme.
