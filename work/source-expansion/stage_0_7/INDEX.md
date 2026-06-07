# Stage 0.7 second-order targeted source expansion

Дата: 2026-06-07  
Режим: cumulative archive overlay; previous Stage 0.5 and Stage 0.6 files preserved.  
Основание: пользователь зафиксировал, что все `work`-архивы должны быть кумулятивными, пока не будет предоставлен новый полный snapshot or explicit commit.

Stage 0.6 подтвердил слабые зоны: decision provenance, process/framework layer, lifecycle tail, security/provenance and ownership artifacts. Stage 0.7 проверяет second-order gaps, которые стали видны после анализа источников:

1. `codebase_readiness/` — codebase readiness, context files, AGENTS.md, AI Codebase Maturity.
2. `contracts_and_interfaces/` — API contracts, data contracts, contract tests, schema evolution, contract-adherence.
3. `workflow_specification/` — Agent Spec, AgentSPEX, declarative workflow languages, framework portability.
4. `delivery_safety/` — feature flags, progressive delivery, migration/rollback, AI-augmented CI/CD.
5. `decision_enforcement/` — ADR generation, decision rationale, ADR violation detection, decision compliance.

Каждая тема имеет три повторных честных поисковых этапа: `step_01`, `step_02`, `step_03`, с разными формулировками и разными источниковыми углами.
