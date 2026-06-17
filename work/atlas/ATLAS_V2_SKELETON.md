# Atlas V2 Skeleton — technical layer map and article architecture

Status: working skeleton for Atlas V2.  
Date: 2026-06-17.  
Basis: ADR-0012 through ADR-0019, `ATLAS_V2_LAYER_ARTICLE_MAP.md`, legacy Atlas routing notes, and the second coverage check after the eTechLead/AgenticOps discussion.

## 0. What this skeleton is

This document is the Atlas-level counterpart to the Theory skeleton. It does not replace `work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md`. The difference is:

```text
ATLAS_V2_SKELETON.md
→ composition of the Atlas part, article roles, levels, boundaries, order and acceptance gates.

ATLAS_V2_LAYER_ARTICLE_MAP.md
→ operational planning map for building target-group plans and packages.
```

The Atlas is a peer major part of the corpus. It is not an appendix to Theory. Theory uses the lifecycle-of-change cut; Atlas uses the technical-layer cut.

## 1. Atlas thesis

Agentic development is not a single tool or a model feature. It is a system of technical layers around software change: project context, working surfaces, orchestration, tool access, execution environments, codebase retrieval, version-control substrate, checks, review, memory, security, UI feedback, model/provider routing, organizational metadata, program feedback, testing and production operation.

The Atlas should help a reader understand:

```text
what technical layers exist;
how each layer is built;
what tools, protocols, formats and artifacts appear in that layer;
how competing approaches differ;
when to choose one approach over another;
where the layer fails;
how the layer connects to neighboring layers.
```

The Atlas must not become:

- a theory of agentic development;
- a product ranking;
- a list of tools without architecture;
- a Handbook/Working Scenarios guide;
- a Fieldbook/Problem Catalog organized primarily by failures.

## 2. Article levels

### Level 1 — technical layer articles

A1–A19 are the main Atlas layer articles. They define the technical map.

### Level 2 — integrated product, method and platform profiles

These are not lower quality articles. They have a different role: they show how one method, product family or platform assembly crosses several layers. Examples:

- Kiro / Kiro Specs;
- Spec Kit;
- SPDD;
- Persistent Work Graph;
- ADR/MADR;
- TDAD;
- Constitutional SDD;
- BMAD / GSD / Open GSD;
- Gas Town / Beads;
- AgenticOps / agent-facing platform engineering;
- selected tool/platform profiles when they illuminate several Level 1 layers at once.

A Level 2 article must explicitly state which Level 1 layers it crosses. It should not pretend to replace the layer articles.

### Level 3 — case/source/profile nodes

These are shorter source-backed nodes or legacy articles that preserve important factual texture, source interpretation, or tool-specific detail. They can feed Level 1 and Level 2 articles and may remain discoverable from the Atlas.

## 3. Level 1 layer articles

Each Level 1 article must follow the same acceptance frame:

```text
layer problem;
classes of solutions;
concrete technologies/formats/protocols/work surfaces;
artifacts produced or changed by the layer;
technical operating logic;
selection criteria;
typical failures;
links to neighboring layers;
what belongs to Theory / Working Scenarios / Problem Catalog instead.
```

### A1. Context interface of the project for the agent

Russian working title: `Контекстный интерфейс проекта для агента`.

Role: explain where explicit project knowledge lives so the agent does not work from an empty prompt.

Must cover: `AGENTS.md`, `CLAUDE.md`, Cursor Rules, GitHub Copilot custom instructions, Codex/Amp instructions, Kiro steering, skills, hooks, subagents, project docs, specs, ADRs, local task packages, source manifests and rule-repair notes.

Main artifacts: instruction files, nested rules, steering docs, skill files, hook configs, subagent profiles, task packages, acceptance criteria, repair notes.

Boundary: A1 is about explicit project guidance. Codebase search/retrieval belongs to A10; memory of prior sessions belongs to A12; organizational catalog metadata belongs to A16.

### A2. Working surfaces of coding agents

Russian working title: `Рабочие поверхности coding agents`.

Role: compare where the agent actually acts: chat, IDE, CLI, cloud task, PR-agent, local open-source harness, sandbox/worktree and hybrid surfaces.

Must cover: chat coding, IDE agents, CLI agents, cloud coding agents, PR/issue-to-PR agents, Aider, OpenHands, SWE-agent-like environments, sandbox/worktree work.

Main artifacts: transcript, local diff, patch, terminal log, worktree, cloud branch, agent-created PR, command output, run summary.

Boundary: A2 is about the work surface. Orchestration is A3; reproducible runtime is A9; browser/app feedback is A14.

### A3. Orchestration and agent execution frameworks

Russian working title: `Оркестрация и фреймворки агентского исполнения`.

Role: explain how agent work becomes a controlled process when one model in one surface is not enough.

Must cover: ReAct/tool-use loop as background, LangGraph, OpenAI Agents SDK, Google ADK, AutoGen, CrewAI, LlamaIndex Workflows, workflow runners, state machines, multi-agent roles, retries, interrupts, human gates and resumable workflows.

Main artifacts: graph/workflow definition, state object, tool-routing rule, retry policy, interrupt checkpoint, worker role, run trace, resume token.

Boundary: do not write a history of ReAct; do not rank frameworks. Compare orchestration needs and trade-offs.

### A4. Tools, protocols, access and authority

Russian working title: `Инструменты, протоколы, доступы и полномочия`.

Role: explain the difference between technical ability to act and legitimate permission to act.

Must cover: tool/function calling, MCP, A2A, connectors, sandbox permissions, approvals, scoped access, secret handling, audit logs, prompt injection surfaces, tool poisoning, role-scoped commands, agent-facing CLI/API design, `SKILL.md`-style tool guidance, discovery of commands, safe machine-readable outputs.

Main artifacts: tool schema, MCP server/tool, connector config, approval prompt, denied call, audit event, scoped credential, CLI command spec, skill/tool guide, discovery output.

Boundary: security controls overlap with A13; runtime environments are A9; organization-level catalog/actions are A16.

### A5. Observability, traces and evals

Russian working title: `Наблюдаемость, traces и evals`.

Role: show how agent work becomes visible, replayable, measurable and comparable.

Must cover: traces, spans, tool-call logs, replay/debug surfaces, LangSmith/Langfuse/Phoenix-like systems, eval harnesses, SWE-bench-like benchmarks, golden tasks, regression evals, automated graders, run comparison.

Main artifacts: trace, span, tool-call log, run comparison, eval report, benchmark result, failure cluster, cost/latency trace, replay view.

Boundary: A5 measures agent runs and systems. CI/review gates are A7; program diagnostics are A17; tests as artifacts are A18.

### A6. Git, worktree and PR/MR as change substrate

Russian working title: `Git, worktree и PR/MR как субстрат агентского изменения`.

Role: explain how an agent output becomes a change candidate: isolated, comparable, reviewable, mergeable and reversible.

Must cover: branch, worktree, index, commit, history, diff, patch, merge, squash, rebase, cherry-pick, conflicts, PR/MR, linked issue, review state, audit trail, revert, rollback, bisect, multi-agent branches/worktrees.

Main artifacts: branch, worktree, commit, diff, patch, PR/MR, merge commit, revert commit, conflict resolution, review state, provenance trail.

Boundary: A6 forms the candidate. A7 applies acceptance gates. A19 covers release and runtime consequences.

### A7. CI, status checks, review and acceptance gates

Russian working title: `CI, status checks, review и acceptance gates`.

Role: explain how a formed change candidate receives technical and human gates before it is accepted, rejected or sent back.

Must cover: CI, required status checks, protected branches, rulesets, merge queue, test reports, coverage, lint/typecheck/security scans, CODEOWNERS, review comments, approvals, requested changes, AI review tools, contract/API compatibility checks, deployment gates as handoff to A19.

Main artifacts: CI run, check suite, test report, coverage report, review comment, approval, requested-changes state, merge-queue item, compatibility report.

Boundary: do not repeat ex-A3 as theory. A7 is technical gate infrastructure, not general philosophy of acceptance.

### A8. Specifications, plans and executable process artifacts

Russian working title: `Спецификации, планы и исполняемые процессные артефакты`.

Role: explain how intent becomes controlled work before and around code.

Must cover: Spec Kit, Kiro specs, ADR, SPDD, BMAD/GSD/TDAD-like methods, Constitutional SDD, issue templates, task packages, acceptance criteria, executable specs, handoff docs.

Main artifacts: spec, ADR, plan, task package, acceptance criteria, handoff, decision record, process profile, package manifest.

Boundary: not a method catalog. Compare what each artifact controls: intent, boundaries, acceptance, sequence, state, recovery.

### A9. Reproducible execution environments and sandboxes

Russian working title: `Воспроизводимые среды исполнения и песочницы`.

Role: explain where the agent can safely run commands, tests, builds, migrations and applications.

Must cover: Docker/Compose, dev containers, Codespaces-like environments, ephemeral sandboxes, remote devboxes, Nix/reproducible environments where useful, local/remote CI-like runners, browser/VNC environments, dependency setup, secret boundaries, snapshots.

Main artifacts: devcontainer config, Dockerfile/Compose file, sandbox session, environment snapshot, dependency cache, setup log, isolated filesystem, allowed-command policy.

Boundary: A9 gives the place of execution. A14 gives browser/UI/app feedback. A17 gives program diagnostics. A7 turns some checks into gates.

### A10. Codebase indexing, search and context retrieval

Russian working title: `Индексация, поиск и извлечение контекста из кодовой базы`.

Role: explain how the agent finds relevant code, symbols, dependencies, call paths and project patterns in large codebases.

Must cover: grep/ripgrep and exact search, IDE/LSP indexes, symbol search, semantic search/embeddings, RAG over code, dependency/call graphs, code maps, Sourcegraph/Cody-like systems, multi-repo context, Shotgun / shotgun_code, context blast, stale index and retrieval errors.

Main artifacts: selected file list, search results, symbol references, code map, call graph, dependency graph, retrieval packet, context bundle, relevance note.

Boundary: A10 extracts current project structure. A1 gives explicit rules. A12 stores past experience and decisions.

### A11. Issue-to-agent tasks, queues, assignment and progress surfaces

Russian working title: `Issue-to-agent: задачи, очереди, assignment и progress surfaces`.

Role: explain how an issue/ticket becomes an agentic work unit with owner, scope, plan, progress and handoff.

Must cover: GitHub Issues, Jira/Linear-like trackers, labels, ownership, issue templates, task assignment to agent, background sessions, progress updates, plan comments, queueing, cancellation, retry, branch/PR linking.

Main artifacts: issue/ticket, assignment event, plan comment, progress update, queue entry, linked branch, draft PR, status comment, cancellation note.

Boundary: A11 is not just issue templates from A8 and not PR mechanics from A6. It is the work-management layer.

### A12. Long-lived project memory and reuse of experience

Russian working title: `Долгая память проекта и повторное использование опыта`.

Role: explain how prior sessions, decisions, failed attempts, fragile files and project habits become usable by future agent work.

Must cover: session memory, project memory, episodic/semantic/procedural memory, summaries, event logs, topic documents, decision records, failed attempts, known fragile files, chat-history retrieval, MCP memory servers, graph memory, consolidation, forgetting, contradiction handling, provenance.

Main artifacts: memory entry, topic doc, event log, decision note, failed-attempt record, retrieval packet, provenance link, contradiction note, stale-memory warning.

Boundary: public article must be neutral. Do not turn A12 into Noveia positioning.

### A13. Security of agentic development and supply-chain controls

Russian working title: `Безопасность агентской разработки и supply-chain controls`.

Role: explain how agentic development expands the risk surface and what technical controls reduce it.

Must cover: prompt injection in docs/issues/web pages, indirect injection, MCP/tool poisoning, malicious skills/instruction packages, secrets, unsafe dependencies, generated-code vulnerabilities, SAST/SCA/CodeQL-like scans, license/security policy gates, least privilege, generator/checker separation, audit logs, incident response.

Main artifacts: injection finding, denied tool call, redacted log, scan result, dependency alert, license policy result, security review comment, audit event, incident note.

Boundary: A4 covers permission mechanics; A13 covers security and supply-chain risk across the agentic-development loop.

### A14. Browser, GUI and app feedback surfaces

Russian working title: `Browser/GUI/app feedback surfaces`.

Role: explain how the agent sees and checks the running application through rendered UI, browser automation, screenshots and app feedback.

Must cover: Playwright/browser automation, Playwright MCP, accessibility snapshots, screenshots, Computer Use, desktop/VNC sessions, devtools logs, network/console traces, visual diffs, appshots, UI comments, generated E2E steps, secrets/privacy risks.

Main artifacts: browser session, accessibility snapshot, screenshot, UI action, devtools log, console error, network trace, visual diff, appshot, E2E step, UI comment.

Boundary: A14 is feedback from the running app. A9 is the runtime environment; A18 is test-artifact generation and governance.

### A15. Model/provider layer, routing, cost and inference constraints

Russian working title: `Model/provider layer, routing, cost and inference constraints`.

Role: explain how model/provider/gateway choices shape the agentic process.

Must cover: model capability axes, provider APIs, tool support, context windows, multimodal support, OpenAI-compatible gateways, LiteLLM/Portkey/OpenRouter-like routing, retry/fallback, caching, rate limits, cost accounting, latency, data retention/residency, BYOK/BYOC/self-hosted options, model/process fit, local evals, real-work trials.

Main artifacts: model-selection note, routing config, gateway policy, cost report, latency report, eval comparison, model-change decision, fallback log.

Boundary: this is a fast-staleness article. It must not become an evergreen model ranking.

### A16. Organizational context, software catalog and developer portal

Russian working title: `Организационный контекст, software catalog и developer portal`.

Role: explain how the agent understands the organization’s engineering topology: services, ownership, dependencies, environments, runbooks, scorecards, portal actions and operational metadata.

Must cover: Backstage/Port-like catalogs, `catalog-info.yaml` and service descriptors, ownership, components/systems/APIs/resources, dependency maps, environments, runbooks, scorecards, maturity/security/compliance metadata, self-service actions, workflow automations, machine-readable app/service descriptors, topology, resource bindings, log/trace locations, deployment units and operational capabilities.

Main artifacts: catalog entity, service descriptor, ownership record, dependency link, system/domain map, API entity, runbook link, scorecard, environment record, self-service action, platform workflow.

Boundary: A16 is the current organizational topology and platform context. A12 is memory; A11 is task management; A1 is project-local explicit instruction.

### A17. Structured program feedback

Russian working title: `Структурированная обратная связь от программы`.

Role: explain how the agent receives and uses structured signals from code and runtime while working locally or in a sandbox.

Must cover: compiler errors, typechecker diagnostics, language server diagnostics, lints, static analysis warnings, debugger sessions, breakpoints, variable inspection, stack traces, runtime logs, profiler output, local reproduction loops, repair loops driven by these signals.

Main artifacts: compiler diagnostic, type error, LSP diagnostic, lint/static-analysis warning, stack trace, debugger transcript, breakpoint state, profiler output, runtime log, reproduction note, fix verification output.

Boundary: A17 is feedback from the program/toolchain during work. A5 is agent observability/evals; A7 is acceptance gates; A18 is test artifacts; A14 is browser/UI feedback.

### A18. Autonomous testing and QA artifacts

Russian working title: `Автономное тестирование и QA-артефакты`.

Role: explain how agents generate, repair, run, evaluate and govern tests and QA artifacts.

Must cover: unit/integration/E2E test generation, bug reproduction, regression tests, test repair, flaky-test handling, coverage-guided work, mutation testing, UI test generation, property/fuzz tests where relevant, test-data generation, test review, governance of AI-generated tests, limits of tests written by the same agent that wrote the code.

Main artifacts: generated test, reproduction test, regression test, test diff, coverage report, mutation score, flaky-test note, test-review comment, QA checklist, generated fixture, bug reproduction script.

Boundary: A18 creates and maintains test/QA artifacts. A7 uses test results as gates; A17 provides diagnostic signals; A14 may generate UI/E2E steps.

### A19. Release, deployment, production monitoring and incident/remediation agents

Russian working title: `Release, deployment, production monitoring and incident/remediation agents`.

Role: explain the post-merge operational layer: releasing, deploying, observing production, rolling back, remediating incidents and feeding lessons back into future work.

Must cover: release pipelines, deployment approvals, feature flags, canaries, progressive delivery, environment promotion, production monitoring, alerts, Sentry/Datadog/Grafana/PagerDuty-like signals, runbook automation, rollback/revert decisions, incident triage, remediation PRs, postmortems, learning back into docs/rules/tests/memory.

Main artifacts: release plan, deployment run, environment promotion, feature flag, canary result, alert, incident ticket, runbook action, rollback, remediation PR, postmortem, production metric, monitoring dashboard note.

Boundary: A7 accepts/rejects the engineering change candidate. A19 handles release and runtime survival. It should now be treated as core, not a candidate.

## 4. Additional Atlas articles beyond A1–A19

A1–A19 are not the whole Atlas. They are the Level 1 technical layer backbone.

Additional Atlas articles should be routed as Level 2/3 profiles, method articles or case nodes. They must name which A-layers they cross.

### Kiro / Kiro Specs profile

Role: integrated product/method profile showing how specs, steering, hooks, IDE work surface and MCP/tooling can be packaged together.

Likely links: A1, A2, A4, A8, A11, A14.

### AgenticOps / agent-facing platform engineering profile

Role: integrated platform profile showing how an agent-facing platform can combine CLI/API tools, discoverable commands, IaC/CaC, self-hosted components, deployment, monitoring, LiteLLM/model gateway, observability and role-scoped agent operations.

Likely links: A4, A6, A7, A9, A15, A16, A19.

This should not become A20 because it is an assembly of layers, not a separate layer.

### SPDD profile

Role: method profile for specification-driven programming/development and the specification-to-change lifecycle.

Likely links: A8, A1, A6, A7, A18.

### Persistent Work Graph profile

Role: concept/method profile around durable work state, relations, recovery, context carryover and project memory.

Likely links: A8, A12, A1, A6, A5.

### ADR/MADR profile

Role: decision-record profile around architectural decisions, decision provenance, review and later reuse.

Likely links: A8, A1, A6, A7, A12.

### Spec Kit / TDAD / Constitutional SDD / BMAD / GSD profiles

Role: method/tool profiles that show competing ways of making intention, plan, constraints, checks and process state explicit for agents.

Likely links: A1, A3, A8, A11, A18.

### Gas Town / Beads profile

Role: dense organizational/operational case showing roles, work units, queues, orchestration, backpressure, continuation, local histories and responsibility boundaries.

Likely links: A3, A8, A11, A12, A16, A19.

## 5. Cross-corpus notes

`Dark matter of software` should be routed primarily to Cross-story synthesis, not to Atlas Level 1. It is a pattern about invisible or undercounted AI-assisted software: internal utilities, personal tools, one-off automations, reports and workflow scripts that may never become public products. It can support the site entry argument and Working Scenarios, but it is not a technical layer by itself.

## 6. Acceptance gates for Atlas packages

Every Atlas package must state:

```text
article level: Level 1 layer / Level 2 profile / Level 3 source node;
required technical payload;
source/fact card plan;
technology matrix;
artifact inventory;
selection criteria;
boundary with Theory, Working Scenarios and Problem Catalog;
human checkpoint before final synthesis.
```

For Level 1 articles, mini-dossiers should not be standalone essays. Prefer source/fact cards, technology matrices, artifact-level extraction and section-slice drafts.

## 7. Synchronization

When this skeleton changes, update:

```text
work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md
work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/APPLY_NOTES.md
```

The Atlas skeleton controls composition. The layer article map controls package construction. The Theory attachment map controls how Atlas material is attached to Theory chapters.
