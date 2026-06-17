# ADR-0018 — Harness Engineering as a cross-cutting frame in the Theory skeleton

Date: 2026-06-17

## Status

Accepted as a skeleton-level routing decision.

## Context

The corpus now separates one shared knowledge area into different public parts by organizing cut:

- Theory / possible future `Жизненный цикл программного изменения` — lifecycle-of-change cut;
- Atlas — technical-layer cut;
- Working Scenarios — practitioner-decision cut;
- Problem and Solution Catalog — failure-mode cut.

The Atlas now contains a growing technical layer map. This clarified that Theory does not need to contain full descriptions of technologies, but it still needs enough technical grounding to avoid becoming abstract methodology.

Recent external terminology around `Harness Engineering` gives a useful way to connect the Theory and Atlas without collapsing them into each other. The term is useful because it says that software-agent capability does not come from the model alone. It emerges from a model plus the surrounding harness/obвязка and environment: prompts, project context, filesystem, tools, MCP servers, sandboxes, browser/GUI feedback, orchestration, memory, traces, evals, permissions, review gates and recovery loops.

The user asked whether Harness Engineering should be reflected in the Theory skeleton.

## Decision

Reflect Harness Engineering in the Theory skeleton as a cross-cutting frame, not as a standalone Theory chapter and not as a replacement for existing corpus terms.

Working formulation:

```text
agentic development is not model use plus code generation;
it is a model-harness-environment system that moves a software change through context, action, feedback, verification, acceptance and recovery.
```

In Russian public prose, use natural phrasing such as:

```text
модель работает не сама по себе, а внутри рабочей обвязки: проектного контекста, инструментов, среды исполнения, проверок, прав, следов выполнения и правил принятия результата.
```

Keep `Harness Engineering` as the English term where useful, with `рабочая обвязка агента` / `системная обвязка агента` as explanatory Russian phrasing. Do not force a single Russian calque into every paragraph.

## Relation to existing internal concepts

Harness Engineering does not replace the user’s existing concepts.

- `Exoskeleton` remains the internal/public conceptual family for the protective process layer around agentic work.
- `Protected process profiles` remain the theory-side way to describe bounded, repeatable agentic work modes.
- `Persistent Work Graph` remains the durable-state/work-object idea.
- `Atlas technical layers` remain the place where individual harness components are described technically.

Harness Engineering should be used as an external-facing bridge and grounding term: it helps explain why model choice is only one part of the system and why the surrounding obвязка is the actual engineering object.

## Where it enters the Theory skeleton

Do not add a new top-level chapter. Add explicit harness framing in these places:

1. **Introduction / opening frame**
   - Introduce the move from `model capability` to `model + harness + environment`.
   - Explain why the book studies the lifecycle of change rather than only prompt quality or model quality.

2. **I. Unit of analysis**
   - Clarify that the unit is not a prompt, chat, run or model output, but a software change moving through a model-harness-project system.

3. **VI. Project as working support for change**
   - Connect repository rules, docs, specs and context files to harness design.

4. **IX. Environment, tools, permissions and runtime rights**
   - Treat tools, MCP, sandbox, browser, filesystem, command execution and permissions as harness components.

5. **XI. Verification material and boundaries of proof**
   - Treat traces, logs, tests, evals, diagnostics and self-correction loops as feedback/sensor parts of the harness.

6. **XII. Acceptance and authority**
   - Explain that the harness can produce evidence and route a change, but does not by itself confer the right to accept the change unless the social/organizational gate is part of the process.

7. **XIII. After merge**
   - Treat monitoring, rollback, cleanup, rule updates and memory updates as harness feedback back into the lifecycle.

8. **Conclusion**
   - Use Harness Engineering to summarize the practical thesis: progress comes from designing minimal sufficient working obвязка around capable models, not from waiting for the next model alone.

## Boundary with the Atlas

Theory may use Harness Engineering to name the system-level frame, but should not list all harness components in detail. The technical map of components belongs in the Atlas.

Atlas articles A1–A16 can be understood collectively as the technical decomposition of the harness around coding agents. This does not require adding a new Level 1 Atlas article called Harness Engineering. If needed, Harness Engineering may become an introduction/overview page for the Atlas, not a competing layer.

## Consequences

- Future chapter packages must include a `harness-frame check` alongside the existing `atlas-technical-grounding check`.
- The check should ask whether the chapter wrongly attributes success/failure to the model alone when the relevant issue is actually context, tools, permissions, environment, feedback, verification, memory, state or acceptance gates.
- The check should also prevent the opposite error: turning every chapter into a catalog of harness components.

## Follow-up documents

This decision is mirrored in:

```text
work/theory-writing/reports/HARNESS_ENGINEERING_THEORY_SKELETON_NOTE_2026_06_17.md
work/theory-writing/reports/THEORY_SKELETON_IMPLICATIONS_AFTER_ATLAS_CUTS_2026_06_17.md
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
work/multilingual/BILINGUAL_TERM_REGISTRY.md
```
