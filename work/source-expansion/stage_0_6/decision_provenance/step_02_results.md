# Search step 2 results — decision provenance / empirical and AI-specific angle

## Selected sources

- `Can LLMs Generate Architectural Design Decisions?` — exploratory empirical study on generating ADDs/ADRs from context. Role: AI-specific bridge; supports using LLMs to draft ADRs but not replacing human judgment.
- `DRAFT-ing Architectural Design Decisions using LLMs` — RAG/fine-tuning approach on ADR generation from a large ADR dataset. Role: evidence that ADR work itself can become agent-assisted workflow.
- `Evaluating Large Language Models for Detecting Architectural Decision Violations` — uses LLMs to identify ADR/code violations. Role: excellent bridge between decision records and evidence/audit.
- `One Size Fits All? An Empirical Comparison of ADR Templates...` — recent comparison of ADR templates, including Nygard/MADR. Role: supports not overdesigning ADR; template choice affects adoption/usability.
- `What rationales drive architectural decisions?` — empirical inquiry into decision rationales. Role: supports claim that rationale categories matter.

## Evaluation

This step upgrades ADR from “old architecture practice” to a relevant AI-driven SDLC artifact. LLMs can help draft and check decisions, but deployment/organizational decisions remain hard because code alone may not contain the needed context.

## Impact on theory

ADR should appear in:

- Part III as decision-provenance artifact.
- Part VI as durable project memory that agents can consult.
- Part VIII/XI as a compliance/evidence target: can the generated change violate known decisions?
- Part XII as decision debt / stale decision handling.
