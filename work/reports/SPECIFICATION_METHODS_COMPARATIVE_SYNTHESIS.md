# Specification methods comparative synthesis

Дата: 2026-06-08
Статус: repaired synthesis after source-consolidation dossier pass.

Главный вопрос: каким способом намерение становится управляемым артефактом?

## Основной вывод

Specification methods differ not by “how much documentation they create”, but by what they choose as the object of control before an agent acts.

SPDD remains the deep theoretical anchor: specification governs delegation and meaning. Spec Kit turns that into portable command/template workflow: constitution, spec, plan, tasks and implementation (https://github.github.com/spec-kit/, https://github.com/github/spec-kit). Kiro turns similar movement into IDE-native files and execution: `requirements.md`, `design.md`, `tasks.md`, steering and task tracking (https://kiro.dev/docs/specs/, https://kiro.dev/docs/steering/). Constitutional SDD narrows the object to non-negotiable security constraints encoded in a machine-readable Constitution (https://arxiv.org/abs/2602.02584). TDAD A moves specification to the agent definition itself: prompt as compiled artifact from behavioral specs (https://arxiv.org/abs/2603.08806). TDAD B moves testing/specification to regression evidence for code changes through graph-based impact analysis (https://arxiv.org/abs/2603.17973).

## Object of control

| Method | Controlled object | Main artifacts | What becomes explicit | Main human gate |
|---|---|---|---|---|
| SPDD | delegation meaning and intent | specification model | what the agent is allowed to infer | approval of meaning |
| Spec Kit | feature intent to implementation chain | constitution, spec, plan, tasks | behavior, technical plan, implementation units | clarify/analyze before implement |
| Kiro Specs | IDE-local feature/bugfix work | requirements/bugfix, design, tasks, steering | requirements, design, tasks, persistent workspace knowledge | requirements/design/task approval |
| Constitutional SDD | security constraints for generation | Constitution, traceability | non-negotiable security rules before code | security constraint approval |
| TDAD A | tool-using agent behavior | behavioral specs, tests, compiled prompt | expected agent behavior and regressions | hidden-test/spec approval |
| TDAD B | code-change regression surface | code-test graph, impacted tests | which tests matter for a change | graph/test coverage approval |

## What the future Part V should do

Part V should not list methodologies. It should ask: before an agent acts, what must be made explicit?

Suggested sequence:

1. Start with SPDD as the conceptual anchor.
2. Use Spec Kit to show tool-shaped spec-to-code chain.
3. Use Kiro to show IDE-native requirements/design/tasks and steering.
4. Use Constitutional SDD to show constraints that are not negotiable preferences.
5. Use TDAD A/B to show that sometimes the object of specification is not the product feature but the agent behavior or regression evidence.

## Important contrasts

Spec Kit vs Kiro:

- Spec Kit is portable and command/template based.
- Kiro is IDE-native and connects specs to task execution and steering.

Constitutional SDD vs Spec Kit:

- Both can use constitution-like artifacts.
- Spec Kit constitution is broad project/workflow governance.
- Constitutional SDD Constitution is security-constraint governance.

TDAD A vs TDAD B:

- TDAD A compiles agent definition from behavioral specifications.
- TDAD B selects impacted tests for AI coding-agent changes.
- The shared word “test-driven” hides different objects of testing.

## Failure modes to carry into final writing

- Specification rituals can become theater if humans do not review.
- Quick gate compression, like Kiro Quick Plan, is useful only when ambiguity is low.
- Constitutional artifacts can overclaim safety if constraints are shallow.
- Hidden tests can be unrepresentative.
- Graph-based test selection can miss dynamic dependencies.
- Paper claims must stay source-attributed.

## Handbook / Fieldbook split

Theory should explain object-of-control differences and why they matter.

Handbook should contain:

- Spec Kit command walkthrough.
- Kiro spec file examples and EARS examples.
- Constitution schema and review checklist.
- TDAD harness design and mutation-test examples.
- Graph/test impact integration examples.
