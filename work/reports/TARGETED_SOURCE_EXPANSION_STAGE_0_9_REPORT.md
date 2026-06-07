# Stage 0.9 source expansion report: единый замысел и управляющие поверхности

Дата: 2026-06-07  
Режим: кумулятивный архив-оверлей, продолжение Stage 0.5–0.8.  
Статус: источниковый добор для связности плана. Главы не переписывались; `work/approved-ai-sdlc-plan.md` не изменялся.

## Причина Stage 0.9

После Stage 0.5–0.8 в рабочем корпусе стало много правильных, но потенциально разрозненных артефактов: ADR, RFC, GSD, BMAD, контракты, трассируемость, SBOM, секреты, наблюдаемость, права владения, review capacity, feature flags, runbooks. Пользователь отдельно указал, что полнота важна, но всё это должно войти в единый замысел, а не выглядеть неоднородной коллекцией.

Stage 0.9 искал не ещё одну группу “важных вещей”, а источники, которые помогают связать найденные артефакты в цельную архитектуру.

## Темы

1. Поток ценности, платформа и каталог.
2. Воспроизводимая среда выполнения.
3. Политики как код и исполняемые ограничения.
4. Жизненный цикл запросов и контекста.
5. Граф артефактов и управляющие поверхности.

Каждая тема прошла три поисковых этапа с разными формулировками.

## 1. Поток ценности, платформа и каталог

### Что проверялось

Если новая теория собирает много артефактов, нужен вопрос, который сортирует их по роли. Value stream / DORA / Team Topologies / platform engineering дают такой вопрос: где этот артефакт помогает потоку изменения пройти дальше без потери смысла, качества, ответственности or recoverability?

### Источники

- DORA / Google Research and Bain остаются рамочными источниками для system-level view.
- Value stream and value-stream mapping give language for end-to-end flow from request to delivered value.
- Team Topologies gives a structure for fast flow of value, stream-aligned teams, platform teams, cognitive load and interaction modes.
- Platform engineering and internal developer platforms introduce self-service workflows and golden paths.
- Backstage Software Catalog gives a practical catalog of components, APIs, systems, owners and lifecycle metadata.

### Вывод

Для теории нужен не список артефактов, а вопрос:

```text
Как этот артефакт помогает изменить программную систему без потери намерения, контекста, проверки, прав завершения and learning?
```

Артефакт, который не отвечает на этот вопрос, уходит в source map or Handbook.

## 2. Воспроизводимая среда выполнения

### Что проверялось

Stage 0.8 уже говорил о SBOM, provenance and observability. Но агенту нужна ещё более ранняя вещь: воспроизводимая среда, где можно запускать проект, тесты and checks.

### Источники

- Dev Container Specification / GitHub Codespaces — development environment as repository-controlled artifact.
- Reproducible Builds — correspondence between source and binary, deterministic build, supply-chain integrity.
- Nix and Bazel/hermetic build ideas — reproducibility and isolated dependency resolution, with complexity limits.
- Attestable builds — source-to-binary correspondence using trusted execution environments and sandboxed build containers.

### Вывод

Part VIII should include “runnable/reproducible environment” as a concrete artifact. This is not just setup convenience. For agents it is the difference between reading code and being able to produce evidence.

## 3. Политики как код

### Что проверялось

Governance and security should not remain abstract. Some constraints can be expressed as executable policies.

### Источники

- Open Policy Agent — general-purpose policy engine; decouples decision-making from enforcement and works with structured data across Kubernetes, CI/CD, APIs and infrastructure.
- Conftest / Kyverno / InSpec — examples of policy/compliance checks over configs, Kubernetes and infrastructure.
- `Compliance as Code` empirical study — shows compliance rules as programmed checks and also shows mapping/coverage difficulties.
- ARPaCCino — agentic RAG for generating and validating Rego rules over infrastructure-as-code.
- `Policy as Code, Policy as Type` — theoretical caution: policies are constraints over allowed/disallowed actions, and weak policy languages can still leave safety gaps.

### Вывод

Policy-as-code belongs as a medium artifact connecting Constitutional SDD, harness/environment, evidence and governance. It should not replace human judgment: policies themselves require tests, review and maintenance.

## 4. Жизненный цикл запросов и контекста

### Что проверялось

У нас уже есть сильная SPDD линия. Но Stage 0.9 проверил более общий слой: как живут запросы, шаблоны запросов and context artifacts in software repositories.

### Источники

- `Prompts as Software Engineering Artifacts` — prompts need systematic development, documentation, maintenance, traceability and reuse.
- `Prompting in the Wild` — empirical prompt evolution across repositories; many changes are undocumented and can introduce inconsistencies.
- `Promptware Engineering` — prompt-enabled systems require their own lifecycle: requirements, design, testing, debugging, evolution, deployment and monitoring.
- ChainForge — prompt/model comparison and hypothesis testing.
- Context engineering sources — treat retrieved knowledge, instructions, tool definitions and metadata as managed context.

### Вывод

This supports SPDD, but also cautions against generic prompt management. Part III/VI/XII should treat prompt/context artifacts as maintainable and testable. SPDD remains the strong method; context files and prompt templates need quality discipline.

## 5. Граф артефактов и управляющие поверхности

### Что проверялось

Stage 0.5–0.8 produced many artifacts. Stage 0.9 checks whether they can be tied through a graph, not a list.

### Источники

- `SoK: Systematizing Software Artifacts Traceability...` — global artifact traceability graph of 22 artifact types and 23 associations; also notes research imbalance and adoption gap.
- Code property graph — merges syntax, control flow and data dependencies for program analysis.
- LLM-assisted architecture entity recognition — connects architecture documentation and code.
- Backstage Software Catalog — practical surface linking components, APIs, systems, owners and lifecycle metadata.

### Вывод

The final theory can use “artifact graph” as a mental model: not every artifact is a section; artifacts form links across lifecycle. This is the main defense against collection-like structure.

## Интеграционный вывод

Stage 0.9 suggests one stronger organizing line:

```text
AI-driven SDLC is a managed flow of software change through connected artifacts and control surfaces.
```

This should be written in Russian in the final theory, примерно так:

```text
Агентская разработка меняет не только исполнителя работы. Она требует связать намерение, контекст, решение, среду, проверку, владельца и сопровождение через артефакты, которые можно читать, проверять, обновлять и использовать в следующем цикле.
```

Это не новый верхний заголовок. Это способ вписать все найденные слабые зоны в уже утверждённую рамку AI-driven SDLC.

## Что добавить к plan patch

1. В Part I добавить правило отбора артефактов: артефакт нужен, если он переносит изменение дальше по lifecycle.
2. В Part VI добавить platform/catalog/golden-path layer как способ связать контекст, владельцев, среду and checks.
3. В Part VIII добавить runnable/reproducible environment and policy-as-code gates.
4. В Part X добавить prompt/context regression and policy evidence as evidence types.
5. В Part XI добавить catalog/ownership/policy gates as concrete completion-right surfaces.
6. В Part XII добавить artifact graph / lifecycle repair framing, чтобы tail не стал списком ops artifacts.

## Что не делать

- Не создавать отдельную часть “все артефакты”.
- Не превращать Backstage/platform engineering into deep case.
- Не превращать policy-as-code into governance panacea.
- Не размывать SPDD/Gas Town.
- Не превращать Part XII into dumping ground.
