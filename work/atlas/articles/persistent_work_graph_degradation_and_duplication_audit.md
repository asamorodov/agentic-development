# Persistent Work Graph — degradation and duplication audit

Status: final package complete. Readiness blockers checked and passed.

## Boundary checks

| Boundary | Risk | P01 status |
| --- | --- | --- |
| Beads product overview | Article could become Beads documentation summary | Mitigated by framing Beads as anchor, but later source-depth passes must keep product detail selective. |
| Gas Town duplicate | Article could repeat organizational-operational Gas Town story | Provisional section exists; must be checked after reading Gas Town dossier and B3. |
| Durable execution duplicate | Article could treat LangGraph/Temporal/DBOS as PWG | Mitigated by explicit graph-of-work / graph-of-execution distinction. |
| Issue tracker reduction | Article could define PWG as ordinary task tracker | Mitigated by source state, gates, prime, evidence and recovery requirements. |
| Internal-process overfit | Article could become only about this writing workflow | Watch: current document-process section is useful but may need shortening or clearer generalization. |
| Theory repetition | Article could copy A4/B2/A10 too closely | P01 uses controlled repetition for self-contained article; later style/editorial passes should reduce echo. |

## Degradation check

P01 preserves the central mechanism from dossier: durable work state, dependency readiness, owner/handoff, gates, prime, recovery, source state, evidence, runtime boundary and failure modes.

## Duplication check

No full story retelling was added. Beads is not described as a standalone product tour. Gas Town is referenced only as boundary.


## P02 boundary audit

- Added explicit article contract table to stop scope drift.
- Gas Town boundary improved with roles/queues/mail/observability/human control surface; article still avoids retelling Gas Town.
- Process-profile boundary added: GSD/BMAD are not weak PWGs; they leave outputs that PWG may preserve as state.
- Durable execution and CRDT/shared editor boundaries remain explicit.


## P03 inventory audit

Selective inventory confirms that untransferred material is mostly product/implementation depth, not missing article-critical concept material. No total coverage matrix was created. The article should resist pressure to import full Beads troubleshooting, full Gas Town operations or TS-loop implementation details.


## P04 audit

Opening problem now has a concrete technical table rather than generic prose. This reduces risk that PWG reads as a vague memory metaphor.


## P05 audit

The minimal-property section now describes a state-transition mechanism, not a glossary. This reduces the risk that PWG reads as a list of nice-to-have fields.


## P06 audit

Beads section gained concrete commands and storage facts while preserving the boundary: the text says Beads is a mechanism check, not the article subject. Local asset inserted because it clarifies the mechanism and is already in repository assets.


## P07 audit

Adjacent layers now have concrete questions rather than taxonomy-only names. This reduces duplication risk with runtime, Gas Town and parallel-editing articles.


## P08 audit

Document-process section now serves as second proof of concept, not an implementation appendix. It has enough technical anchors but includes an explicit warning against reading it as a TS-loop specification.


## P09 audit

Added state schema as technical anchor. Risk: code block could feel implementation-heavy. Mitigation: surrounding prose says schema illustrates semantics, not storage or TypeScript implementation.

## P10 audit

The weakest conceptual seam was the cluster around work graph / execution graph / evidence / source state / shared editing. P10 added a five-layer table and linking rules. This should reduce false equivalence with durable execution and CRDT/shared-editing layers. Risk: the article now has two boundary tables; P19-P22 should remove repetition only if the separation remains clear.

## P11 audit

Local visual pass inserted two additional figures and kept one existing figure. Boundary risk is controlled in captions: Gas Town image is framed as an upper-layer boundary, not as article subject; Anthropic process diagram is framed as a parallel-worker/evidence flow reminder, not as a replacement for PWG. `gastown-basic-workflow.svg` and `anthropic-multi-agent-research-architecture.webp` were deliberately not inserted to avoid operational duplication.

## P12 audit

External image pass avoided screenshot accumulation. GitHub/Linear baselines, MAST failure distribution, AEGIS/SKILL.nb visuals and Taskmaster/route diagrams were not inserted because they would dilute the article or duplicate textual boundaries. The strongest external process candidate is already available as a local asset from P11.

## P13 audit

Only one synthetic figure was created. This avoids visual inflation while addressing the article's hardest boundary: PWG as a coordination hub between runtime, source state, shared editing and evidence. No job/pass diagram was added because the document-process section already has a table and Anthropic process image.

## P14 audit

Added controlled theory repetition for standalone readability. The new lifecycle section is deliberately short and scoped to PWG; it does not import the full theory chapter or story corpus.

## P15 audit

PWG-specific risks are now explicit in the main article. This reduces the risk of a too-smooth mechanism story. New editorial risk: the failure section is longer; later passes may compress phrasing while preserving each distinct failure mode.

## P16 audit

Theory-link section now uses semantic questions rather than file-name references or a duplicate theory chapter. This preserves article independence while making its place in the broader theory explicit.

## P17 language audit note

The first language pass reduced unnecessary English in explanatory prose while preserving product names, commands, file paths, status literals and source-specific terms. It also repaired accidental formatting damage in JSON-like examples and tables so the mechanism remains readable rather than degraded by translation artifacts.

## P18 language audit note

The second language pass removed English connective phrases and accidental bilingual glue from the main text. Exact commands, product names, field names, status literals and URLs were preserved. No source claims, boundaries or images were changed.

## P19 editorial assessment and fixes

Problems found:

- The mechanism was present, but the article needed a sharper behavioral test so PWG could not be mistaken for a decorated task list.
- The Beads section was correctly bounded, but the table still risked reading as a feature tour rather than a mechanism check.
- A few language repairs left small consistency defects in labels and grammar.

Fixes applied:

- Added a practical control test: every PWG field should change permitted behavior, recovery, evidence or transition logic.
- Added an editorial guard before the Beads table: rows are mechanism checks, not product recommendations.
- Corrected consistency defects around companion-file wording, recovery field naming and the theory-link authority row.

No new external source was added. The changes synthesize existing article claims.

## P20 editorial assessment and fixes

Problems found after P19:

- The new behavioral control test improved the mechanism, but the document-process section still risked reading as an internal process report rather than a transferable proof case.
- The image plan remained coherent: Beads anchors the mechanism, Gas Town marks an upper boundary, Anthropic illustrates safe parallel returns, and the synthetic hub separates work state from neighboring state layers. Removing any one of these would weaken a distinct boundary; adding more would overproduce visuals.
- No key factual transfer appeared to be lost after P19.

Fix applied:

- Added a short orientation sentence at the start of the document-process section explaining that the example demonstrates transferability outside a conventional bug tracker, not the project's internal pipeline.

## P21 adversarial boundary audit

Problems checked:

- Beads product overview: still bounded. The Beads material remains a mechanism check, not a recommendation or feature list.
- Gas Town repetition: the article had a concise boundary, but B3 makes the distinction sharper: PWG is durability of a work unit; Gas Town is durability of the organization around many work units.
- Generic task-tracker essay: mitigated by behavioral control test, source-state lifecycle, evidence transitions and recovery requirements.
- Survey drift: adjacent systems remain boundary examples rather than the article's subject.
- Concrete implementation overfit: document-process material is framed as portability proof, not TS-loop specification.

Fixes applied:

- Added the explicit Gas Town/PWG boundary formula: PWG gives durability to individual work; Gas Town adds durability to the organization around many works.
- Added a stop-line that keeps roles, patrols, merge queues, mail routing and Mayor surface in the Gas Town article unless they explain the state of one work unit.

## P22 structure audit

Checked headings, first screen, figure order and captions. The article still opens with the core problem before Beads, explains why transcript/TODO/ordinary issues are insufficient, and places figures in a functional order: layer separation, Beads anchor, Gas Town boundary, parallel-source process. Added the required bottom section for external image disposition without changing the article's main argument.

## P23 companion-sync audit

P23 checked that source, ledger, image, external-queue, open-question and theory-link files describe the same current article.

Resolved duplication risks:

- Beads remains an anchor and mechanism check, not a product overview.
- Gas Town remains an upper-boundary comparison, not a retelling of roles, convoys, town/rig operations, queues or mail routing.
- Durable execution remains adjacent: run state and checkpoints do not replace work acceptance state.
- Evidence remains adjacent: evidence justifies transitions; it is not itself the PWG or the acceptance authority.
- The document-process section now reads as a portability proof, not a memoir of the article-production pipeline.
- Visual use is bounded: four figures, four different functions, no screenshot accumulation.

Remaining final checks are local: preserve semantics during style edits, verify asset paths in the final package and decide whether the bottom external-image appendix stays in the public bundle.

## P24 style defect audit

P24 used only the article and the human technical style / content preservation rules. It made selective style repairs, not a total rewrite.

Actual defects fixed:

- replaced pseudo-technical abstractions such as “external substrate”, “surface of thinking”, “surface of recovery”, “product surface” and “link contour” with plain technical wording;
- removed a few decorative or translated metaphors: “distant edge of the space”, “working truth”, “closing the loop”, “managed delta”;
- softened heavy or unnatural nouns where a normal Russian technical phrase was clearer: “human management surface”, “false distribution of responsibility”, “instrumental surface”;
- preserved source-specific names, commands, status literals, figure ids, URLs and the necessary boundary distinctions.

No factual claim, source, figure or boundary was added or removed. The article still retains deliberate “not X / but Y” distinctions where they carry a real boundary: PWG versus Beads, Gas Town, durable execution, evidence, shared editing and process profiles.

## P25 selective natural rewrite

P25 rewrote only places already surfaced by the style audit and a few adjacent sentences with the same defect pattern. The pass improved readability without changing source facts or technical anchors.

Edits made:

- normalised several headings and first sentences: `операционная гигиена` became `эксплуатационная дисциплина`; `Эта статья держит узкий контракт` became a plain statement;
- replaced a few model-like abstractions with direct phrases: manual transcript archaeology, source doing work for text, instrumental form, link closure and theory insertion;
- kept compact terms where they are doing real boundary work: `claim`, `gate`, `prime`, `ready`, evidence package, durable execution, Gas Town, Beads and PWG.

No article section, source link, figure, code block, schema field or boundary table was removed.

## P26 guarded final style pass

P26 made a final guarded style pass over the article using the human technical style, Russian-language and content-preservation rules.

Changes stayed formal rather than factual:

- translated ordinary English in several link labels and image alt text where exact source names did not require English wording;
- split the longest mechanism paragraph so the claim/gate/prime/recovery sequence reads as a normal explanation rather than a compressed protocol block;
- kept exact product names, commands, paths, status literals and source titles where translation would reduce precision;
- preserved all figures, schemas, source links, boundary tables and technical anchors.

No companion source/image/theory sync was needed beyond this audit note because no claim, source, figure or boundary changed.

## Final readiness audit

Blocking checks from the final worksheet:

| Blocking risk | Result |
| --- | --- |
| Product review Beads | passed — Beads remains a mechanism anchor and bounded section. |
| Gas Town duplicate | passed — Gas Town remains an upper-boundary comparison. |
| Survey-paper drift | passed — CodeCRDT/STORM/MAST/durable execution examples are boundary supports, not the article subject. |
| Generic task-tracker essay | passed — article includes gate/prime/recovery/source-state/evidence/control-condition mechanics. |
| Work graph / execution graph / evidence confusion | passed — five-layer separation and synthetic state-hub figure remain. |
| Missing document-process transfer | passed — document-process section remains and is framed as portability proof. |
| Visual candidate disposition missing | passed — image plan and external queue record dispositions; no public external placeholder remains. |
| Local asset missing or unexplained | passed — three local assets are inline and packaged. |
| Companion sync missing | passed — companions updated to final status. |

Final package status: `completed`.
