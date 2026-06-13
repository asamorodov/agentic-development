# Theory links — Spec Kit article

Статус: P26 guarded final style. Файл фиксирует фактические theory backlinks текущей статьи; generic C5/A10 sync debt отсутствует.

## Main backlinks

| Theory area | Link role in article | Where used in article | Boundary |
| --- | --- | --- | --- |
| A3 — specification methodologies | Spec Kit shows how specification becomes a sequence of repo artifacts rather than a single prompt. | Sections 1, 5–8, 18. | Do not retell all specification theory or SPDD. |
| A5 — process as artifact | Workflows, presets, extensions and command templates show process materialized as project infrastructure. | Sections 11–13, 18. | Do not turn article into general process taxonomy. |
| A9 — lifecycle repair | Drift after implementation, upgrade/project-file sync, constitution/template sync and stale agent context show repair obligations. | Sections 14, 16, 18. | Do not write full lifecycle repair chapter. |
| A10 — mode selection map | Spec Kit is a middle-weight external structure: heavier than chat/plan, lighter than PWG/Gas Town. | Section 18. | Do not turn article into mode selection guide. |
| C5 — concept-first atlas model | Article is self-contained concept-first entry with controlled repetition. | Whole structure. | Do not rebuild C1–C4 or full theory. |

## Dangerous adjacent routes

| Adjacent article | Boundary to keep |
| --- | --- |
| SPDD / OpenSPDD | Spec Kit = portable repo/process/tooling chain; SPDD = prompt/specification as reviewed lifecycle artifact. |
| Kiro Specs | Spec Kit = portable CLI/templates/integrations across agents; Kiro = integrated product/IDE/Web/CLI specification environment. |
| Constitutional SDD | Spec Kit has constitution as project governance artifact; CSDD article should own safety/governance-as-specification layer. |
| Persistent Work Graph / Beads | Spec Kit has spec/plan/tasks and workflows, but not a full durable graph of owners, dependencies, gates and handoffs. |
| Gas Town | Spec Kit can orchestrate phases but does not by itself create a multi-agent organizational environment with capacity control. |

## Controlled repetition status

P01 repeats only the local minimum needed for a standalone article:

- specification must survive the chat;
- plan is separate from product requirement;
- tasks become executable decomposition;
- checks/evidence and human gates matter before implementation;
- lifecycle repair remains after implementation.

Current status: section 18 is compact and functions as a return-to-theory bridge, not a mini-theory recap.

## P02 contract update

The article now names the local contract in the main text: each section must help answer how an artifact transition changes what the agent may do next.

Additional boundary links:

| Neighbor | P02 boundary |
| --- | --- |
| TDAD | Tests govern agent definition or code-change verification; Spec Kit uses checklists/analyze for artifact quality and consistency. |
| ADR | `plan.md` may surface an architectural choice, but ADR owns decision status, consequences and replacement. |
| Persistent Work Graph | Spec Kit workflow-state and tasks are not a durable graph of owners, dependencies, gates and recovery. |

## P04 theory-link update

P04 strengthens the A3/A5 link: Spec Kit is framed not as “specification first” alone, but as a sequence of typed handoffs. Each artifact changes the agent's allowed action: `spec.md` constrains product behavior, `plan.md` constrains technical decision, `tasks.md` constrains execution units, `analyze` constrains diagnosis versus action, and `implement` constrains code execution behind checklist state.

This also sharpens the boundary with TDAD and PWG: the stop points are artifact and workflow gates, not primarily test-as-controller and not a durable ownership/dependency graph.

## P05 theory-link update

P05 makes the process-as-artifact link explicit: each command is treated as a repository state transition rather than a UI action. This supports A5 because the process is materialized in files, scripts, templates, active-feature resolution and agent-context updates.

The A3 link is also sharper: specification is not only a document but the first state in a chain whose later states have different evidence requirements.

## P06 theory-link update

P06 strengthens the lifecycle/governance link: a policy artifact only matters when it changes downstream artifacts or a human gate. This supports A9 by showing a repair obligation: after changing constitution or finding checklist gaps, the workflow must propagate the change rather than merely record it.

It also keeps the boundary with Constitutional SDD: Spec Kit has a constitution mechanism, but this article treats it locally as a workflow constraint, not as the full policy/security theory.

## P07 theory-link update

P07 strengthens the handoff theory: the next agent inherits not only `spec.md`, `plan.md` and `tasks.md`, but also the readable process surface around them: installed commands, skills, scripts, context files, manifests, presets and extensions. This supports A5/process-as-artifact and A9/lifecycle repair because stale context or changed managed files can alter agent behavior without changing the feature spec.

## P08 theory-link update

P08 sharpens the anti-summary link: a method cannot be evaluated only by its narrative arc from intent to implementation. The concrete state carriers — scripts, branch/catalog resolution, generated files, manifests, local overrides and issue-level caveats — are part of the method's epistemic boundary.

This reinforces A9 lifecycle repair: a future agent can inherit stale local machinery even when the public method description is correct.

## P09 theory-link update

P09 strengthens A9/lifecycle repair: the Spec Kit process itself is maintained infrastructure. Updating a CLI, refreshing project files, switching integrations and preserving customized managed files are part of the method, not external housekeeping.

## P10 theory-link update

P10 applies the C5 atlas model directly: the article now gives a concrete route from local artifact to mechanism to evidence boundary. The new reader path helps the concept article stand on its own while still pointing back to the theory question: how meaning survives across SDLC artifacts and agent handoffs.

## P11/P12 visual-theory update

P11/P12 strengthened the visual link to A3/A5/A9 without changing the article boundary. The Fowler image anchors the general SDD workspace pattern, while the arXiv Spec Kit Agents candidate anchors the context-blindness caveat. Both are explicitly bounded: Fowler is background context, and Spec Kit Agents is research extension, not the official Spec Kit baseline.

The official docs candidates still serve the article contract: home positioning frames portable SDD, Workflows shows human gates as process state, and JSON status shows machine-readable workflow state.

## P13 synthetic-figure theory update

P13 kept only the two existing synthetic figures because they support theory links rather than decoration. `fig-spec-kit-repo-layers` supports A5/process-as-artifact; `fig-active-feature-resolution` supports A9/lifecycle and handoff correctness by showing how local state chooses the active feature. No new synthetic visual layer was added.

## P14 standalone-concept update

P14 applied the C5 standalone-article contract directly. The article now gives a small local model before the technical sections: intent, artifact, transition, gate and agent surface. This is controlled repetition of the specification/process theory, but it is bounded to Spec Kit and does not recreate the full A/B/C theory path.

## P15 mechanism-boundary theory update

P15 strengthens the article's A3/A5/A9/A10 links without adding a new theory layer. A3 is sharper because a specification is not “good” until it can feed a plan without inventing hidden meaning. A5 is sharper because `plan.md` and `tasks.md` are treated as state transitions with responsibility, not as decorative documents. A9 is sharper because each evidence object has a limited repair obligation. A10/mode-selection is sharper because Spec Kit is positioned as a heavier coordination mode for ambiguity, risk and handoff, not the default answer to every small change.

## P16 semantic back-links to the general theory

| Theory node | Question this Spec Kit article helps answer | Local answer contributed by the article | Boundary kept |
| --- | --- | --- | --- |
| `00_spine_map` | What carrier lets a software change survive the transition from intention to execution? | Spec Kit shows the carrier as a chain of repository artifacts, not a single prompt: `spec.md` → `plan.md` → `tasks.md` → implementation/evidence surfaces. | It does not claim this chain covers ownership, release acceptance or every post-merge repair surface. |
| `A3_specification_methodologies_synthesis` | Which object becomes governable before the agent acts? | The governable object is the handoff between artifacts: requirement clarity, technical decision, task coverage and implementation permission. | Spec Kit is not SPDD's single Canvas, Kiro's product state or Constitutional SDD's whole policy layer. |
| `A5_process_methodologies_synthesis` | When does process become an artifact instead of a ritual? | Process becomes real when each Spec Kit file is consumed by the next command/workflow step and can block or redirect the agent. | It remains below PWG: workflow-state and checklists are not the same as durable ownership/dependency/gate graph. |
| `A7_observation_vs_evidence` | How should evidence be scoped to the promise it verifies? | The article separates requirement-quality evidence, artifact-consistency evidence, CLI/environment evidence and agent-surface evidence; none proves the others. | It does not treat successful checklists or installed integrations as proof that code works. |
| `A9_lifecycle_repair` | What can become stale after a change is accepted? | Spec Kit exposes repair surfaces: `specs/`, `tasks.md`, constitution, templates, scripts, managed integration files, context markers, workflow runs and manifests. | It does not solve post-implementation reconciliation completely; it names the repair debt and current issue-level gap. |
| `A10_mode_selection_map` | When is Spec Kit the right amount of structure? | It fits when ambiguity/risk/handoff justify file-based phases; it is too heavy for reversible local changes and too light for durable multi-owner work needing PWG/organizational environment. | Mode selection remains diagnostic, not a claim that Spec Kit is a universal default. |
| `C5_theory_to_technical_atlas` | How should a technical atlas article repeat theory without becoming theory again? | The article repeats only a local model—intent, artifact, transition, gate, agent surface—and then grounds it in commands, files, scripts, images and boundaries. | The general theory remains in the A/B/C fragments; this article stays anchored in Spec Kit's repo workflow. |

P16 also added a compact section-18 paragraph in the main article so the reader sees these links as questions Spec Kit clarifies, not as a second theory chapter.

## P17 language-theory sync

P17 did not alter the semantic theory back-links. It only made the article's local theory-return paragraph more Russian in explanatory wording, especially around evidence/svidetelstvo, workflow/rabochiy protsess and checklist/chek-list. The A3/A5/A7/A9/A10 mapping remains unchanged.

## P18 language-theory sync

P18 did not alter theory routing. The main article's theory-return section still maps Spec Kit to the same A3/A5/A7/A9/A10 questions; wording was only smoothed so it reads as article prose rather than companion metadata.

## P19 theory-link sync

P19 did not change the semantic theory mapping. It strengthened the standalone article contract by making `/speckit.analyze` references more explicit and by keeping the image-preparation material outside the methodological argument. The A3/A5/A7/A9/A10/C5 links remain the same.

## P20 theory-link sync

P20 did not change theory routing. It made the evidence-layer link more precise by naming exact command surfaces (`/speckit.checklist`, `/speckit.analyze`, `specify check`) instead of shorthand labels. The A7 evidence-boundary link is therefore clearer, but not semantically different.

## P21 theory-link sync

P21 did not change theory routing. The local model's “agent surface” term is clearer because `skills` and `recipes` now have Russian glosses, but the A5/A9/A10 meaning is unchanged.

## P22 theory-link sync

P22 did not change theory routing. Moving the article contract after the problem section improves the C5 standalone-article requirement: readers encounter the problem and reader question before atlas-boundary material. The local theory model and A3/A5/A7/A9/A10 links remain unchanged.

## P23 theory-link sync

P23 removed generic debt-language from the theory companion. Current theory state: the article has concrete A3/A5/A7/A9/A10/C5 backlinks, section 18 is compact, and there is no unresolved generic C5/A10 synchronization blocker.

## P24 theory-link sync

P24 made the theory bridge less abstract without changing its backlinks: “последующий ремонт жизненного цикла” was rewritten as “сопровождение жизненного цикла после реализации”, and the section-18 bridge now names the same theory roles in plainer prose. A3/A5/A9/A10/C5 mapping remains unchanged.

## P25 theory-link sync

P25 softened the title and section-18 prose but kept the same theory routing. The article still maps Spec Kit to A3 specification methodology, A5 process-as-artifact, A9 post-implementation lifecycle maintenance, A10 mode selection and C5 standalone concept-first writing.

## P26 theory-link sync

P26 kept section 18 as the return-to-theory bridge and made it read more naturally. The theory mapping remains A3/A5/A9/A10/C5; no adjacent-method boundary changed.
