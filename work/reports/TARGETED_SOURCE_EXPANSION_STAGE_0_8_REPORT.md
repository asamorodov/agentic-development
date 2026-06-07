# Stage 0.8 source expansion report

Дата: 2026-06-07  
Режим: cumulative archive overlay, continuing from Stage 0.5 + Stage 0.6 + Stage 0.7.  
Статус: third targeted source-expansion cycle. Главы не переписывались; `work/approved-ai-sdlc-plan.md` не изменялся.

## Почему понадобился Stage 0.8

Stage 0.7 добавил second-order gaps: codebase readiness, contracts, workflow specs, delivery safety and decision enforcement. Stage 0.8 проверяет ещё один слой: какие artifacts нужны, чтобы AI-driven SDLC был не только lifecycle of intent/execution/review, but also traceable, supply-chain-aware, secret-safe, observable and compatible with human review capacity.

Темы Stage 0.8:

1. Requirements traceability.
2. Supply chain / SBOM.
3. Secrets and sensitive data.
4. Observability and agent traces.
5. Human review and developer experience.

Каждая тема прошла три повторных search steps with different formulations.

## 1. Requirements traceability

Sources considered:

- Requirements traceability / traceability matrix baseline sources.
- `TraceLLM`.
- `Enhancing Requirement Traceability through Data Augmentation Using LLMs`.
- VERIFAI / Formalising Software Requirements using LLMs.

Findings:

- Traceability is a missing cross-cutting artifact.
- It is not the same as specification or test plan.
- It links requirement → design/spec → implementation → test/evidence → release/use.
- LLMs can help recover trace links, but this strengthens the case for explicit trace artifacts rather than replacing them.

Impact:

- Add traceability link / traceability matrix to artifact taxonomy.
- Part III introduces it as intent-to-evidence link.
- Part X uses it to judge evidence completeness.
- Part XII uses it for change impact and maintenance.

## 2. Supply chain / SBOM

Sources considered:

- CISA/NTIA SBOM minimum elements.
- SPDX.
- CycloneDX.
- NIST SSDF.
- SBOM tool ecosystem analyses and SLRs.

Findings:

- SBOM is a first-class lifecycle artifact for dependency, vulnerability, license and supply-chain transparency.
- SBOM is not a solved artifact: tool inconsistency, metadata issues, license accuracy, hidden packages, false positives, privacy and sharing barriers are real.
- AI agents can add or update dependencies quickly, so dependency policy + SBOM quality matter more, not less.

Impact:

- Add SBOM / dependency inventory / license inventory to Part XII.
- Connect SBOM to security/provenance cluster.
- Add SBOM quality/freshness/trustworthiness caveat.

## 3. Secrets and sensitive data

Sources considered:

- GitHub secret scanning / push protection.
- SecretBench.
- `Credential Leakage in LLM Agent Skills`.
- OWASP GenAI/LLM security materials.
- AI-related secret leakage reports.

Findings:

- Secrets are not just a generic security issue. Agent skills, stdout/logging, prompt injection, MCP configs and local credentials create agent-specific leakage paths.
- Debug logs/stdout can expose secrets to LLM contexts.
- Secret scanning and credential inventory are SDLC gates/artifacts.

Impact:

- Add secret scanning / credential inventory / sensitive context boundary to Part VIII/XI/XII.
- Treat secrets as environment/harness and governance artifacts, not only code review issue.

## 4. Observability and agent traces

Sources considered:

- OpenTelemetry GenAI semantic conventions.
- `AgentTrace`.
- `AgentSight`.
- `Early Diagnosis of Wasted Computation...`
- `TRACES`.

Findings:

- Agent observability is more than logs.
- Need structured traces across prompts, tool calls, state changes, environment effects, evidence availability, loops and budget pressure.
- Observability can support both post-hoc accountability and online failure/risk detection.

Impact:

- Add `agent trace / GenAI span / tool-call log` as evidence/provenance artifact.
- Strengthen Part VIII and Part XII around observability debt and trajectory-level evidence.
- Connect to audit log / provenance record from Stage 0.6.

## 5. Human review and DevEx

Sources considered:

- SPACE framework.
- DevEx framework.
- DORA 2025.
- `Human-AI Synergy in Agentic Code Review`.
- `Rethinking Code Review in the Age of AI`.
- `The Impact of AI Coding Assistants on Software Engineering`.
- METR productivity RCT.

Findings:

- Human review capacity is a lifecycle bottleneck.
- AI shifts work from creation to verification/supervisory engineering.
- More code activity is not equal to more value.
- Review is also knowledge transfer and contextual judgment, not only defect screening.

Impact:

- Add review capacity / supervisory engineering / human cognitive load as explicit constraint.
- Use in Part I, Part X, Part XI and conclusion.
- Do not create a new deep case unless later architecture requires an organizational chapter.

## New patch items

Stage 0.8 adds these items to Stage 0.5–0.7 patch recommendations:

1. Traceability link / traceability matrix.
2. SBOM / dependency inventory / license inventory.
3. Secret scanning / credential inventory / sensitive context boundary.
4. Agent trace / GenAI span / tool-call log / trajectory-level evidence.
5. Review capacity / supervisory engineering / DevEx constraints.

## Human gates

Human approval required before:

- adding a new top-level traceability/provenance part;
- making Part XII overly large;
- treating SBOM/traceability/observability as deep cases;
- demoting SPDD/Gas Town/specification zone;
- modifying `work/approved-ai-sdlc-plan.md`.
