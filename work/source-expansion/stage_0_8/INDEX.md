# Stage 0.8 targeted source expansion

Дата: 2026-06-07  
Режим: cumulative archive overlay, continuing from Stage 0.5 + Stage 0.6 + Stage 0.7.  
Статус: third source-expansion cycle after Stage 0.5 coverage audit. Главы не переписывались; `work/approved-ai-sdlc-plan.md` не изменялся.

Stage 0.8 проверяет следующие слабые зоны, которые стали видны после Stage 0.7:

1. `requirements_traceability/` — requirements traceability, trace links, traceability matrix, LLM-assisted trace recovery.
2. `supply_chain_sbom/` — SBOM, SPDX, CycloneDX, SSDF, dependency/license/supply-chain artifacts.
3. `secrets_and_sensitive_data/` — secrets, credentials, secret scanning, secret leakage in agent skills, shadow AI/data exposure.
4. `observability_and_agent_traces/` — OpenTelemetry GenAI conventions, AgentTrace, AgentSight, trajectory-state safety auditing.
5. `human_review_and_devex/` — review capacity, supervisory engineering, SPACE/DevEx, code review bottlenecks.

Каждая тема имеет три повторных честных поисковых этапа with different query formulations.
