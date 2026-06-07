# Plan patch recommendations after Stage 0.8

Дата: 2026-06-07  
Статус: дополняет Stage 0.5–0.7 recommendations; не меняет approved plan напрямую.

## Additional patch items

### 1. Traceability

Add to Part III/X/XII:

```text
Traceability links are lifecycle artifacts connecting requirements, specifications, implementation, evidence and maintenance. LLMs can help recover trace links, but the need for human-validated traceability becomes stronger, not weaker.
```

### 2. SBOM / dependency and license inventory

Add to Part XII and security/provenance cluster:

```text
SBOM/dependency/license inventories are lifecycle-tail artifacts. They support vulnerability management, license compliance and supply-chain transparency, but require quality, freshness and tooling discipline.
```

### 3. Secrets and sensitive context boundary

Add to Part VIII/XI/XII:

```text
Secret scanning, credential inventory and sensitive-context boundaries become explicit artifacts in agentic SDLC because agents interact with local credentials, tools, logs, stdout and MCP/skill configs.
```

### 4. Agent observability / trajectory evidence

Add to Part VIII/XII:

```text
Agent traces, GenAI spans, tool-call logs and trajectory-level signals form evidence artifacts. The goal is not only post-hoc debugging but online detection of loops, wasted computation, missing evidence and unsafe drift.
```

### 5. Human review capacity and supervisory engineering

Add to Introduction/Part I/X/XI:

```text
AI-driven SDLC must treat human review capacity and supervisory engineering as scarce resources. More generated code/activity can worsen cognitive load and review bottlenecks if evidence and ownership do not improve.
```

## Updated dossier/note recommendations

Add:

```text
work/dossiers/TRACEABILITY_AND_REQUIREMENTS_LINKS_NOTE.md
work/dossiers/SBOM_AND_DEPENDENCY_POLICY_NOTE.md
work/dossiers/SECRETS_AND_SENSITIVE_CONTEXT_BOUNDARY_NOTE.md
work/dossiers/AGENT_OBSERVABILITY_AND_TRACES_NOTE.md
work/dossiers/HUMAN_REVIEW_CAPACITY_AND_DEVEX_NOTE.md
```

## Do not do yet

- Do not add a new top-level part for traceability or SBOM.
- Do not let Part XII become larger than SPDD/Gas Town.
- Do not start drafting until the user approves which patch items enter `approved-ai-sdlc-plan.md`.
