# Chapters I–V — external/source-backed illustration candidates

Date: 2026-06-15

## Scope

This is a visual-discovery pass for chapters I–V, performed after the Chapter VI figure integration and after the visual-layer blueprint update.

The pass used:

- current chapter texts for I–V;
- chapter companion files: `*_figure_candidates.md`, `*_source_register.md`, `*_external_discovery_log.md`, `*_story_anchors.md`, `*_atlas_usage.md`, `*_fragment_usage.md`, `*_dossier_gap_notes.md`, readiness reports and pass reports;
- fragment visual registers, especially `A1_figure_candidates.md`, `A2_figure_candidates.md`, `A3_figure_candidates.md`, `A4_figure_candidates.md`, `A5_figure_candidates.md`;
- asset catalog files under `work/theory-writing/asset-catalog/`;
- local assets under `content/assets/story-images/`, `content/assets/theory-images/`, and `content/assets/atlas-images/`;
- external sources referenced by the chapters and their reports, including source pages and PDF/ar5iv pages where figures are present.

The goal is not to insert images yet, but to identify candidates that help understand each chapter, classify their role, and mark whether they should be inserted as existing local assets, source-backed redraws, synthetic explanatory figures, or deferred external real image candidates.

## Visual decision vocabulary

- `local_image_asset` — already present in the repository and suitable for direct insertion after placement/caption review.
- `source_real_image_candidate` — a real image/table/screenshot exists in an external source; do not replace it automatically with a synthetic diagram. Needs rights/quality/localization/placement pass.
- `source_backed_redraw` — a source has a strong visual structure, but the chapter likely needs a localized/redrawn version in the site style.
- `source_backed_synthetic_figure` — the figure explains the chapter’s synthesis, but its parts are grounded in source material.
- `synthetic_explanatory_figure` — authorial figure based primarily on the chapter’s own argument.
- `defer` / `reject` — useful elsewhere, too decorative, too narrow, too catalog-like, or not worth the visual weight in this chapter.

## Cross-chapter findings

1. The existing chapter packages already contain good visual candidates, but they were treated as a late “figure decision.” The stronger visual layer should be treated as a reading pass over the chapter’s argument and source set.
2. Chapters I–III currently rely mostly on synthetic figures or no image. They can benefit from source-backed redraws, especially where the chapter makes distinctions between carriers, status, contract and decision memory.
3. Chapter IV already has the strongest current source-backed asset: `fowler-spdd-workflow.svg`. Additional SPDD images should be added only if they clarify the Canvas or review/sync loop without turning the chapter into a SPDD reference card.
4. Chapter V is the strongest candidate for a visual layer pass: it compares several protected specification profiles, but intentionally avoided a catalog-like matrix. The right visual form should help compare failure boundaries, not rank methods.
5. Several strong external images exist in papers and docs, but many are better as `source_backed_redraw` than direct screenshots: especially TDAD, Constitutional SDD, AWS ADR lifecycle and SWE-chat / Programming by Chat session diagrams.

---

# Chapter I — `I_unit_of_analysis.md`

## Current visual state

Chapter I contains one inline synthetic figure: `fig-i-partial-carriers-vs-software-change`. The package’s current figure-candidate file explicitly defers the broad lifecycle overview, Boris annotation-cycle asset, Codex evidence screenshot, Beads/PWG state image, seven-substrates table and A10 mode-selection map.

That decision was correct for the first canonical text: Chapter I needed to avoid becoming a map of the whole book. But after the stronger visual-layer pass, there are two useful upgrades.

## Recommended candidates

| Priority | Candidate | Type | Suggested placement | Why it helps | Action |
|---:|---|---|---|---|---|
| 1 | `fig-i-change-as-unit-of-analysis` — software change as object, not prompt/session/diff | `synthetic_explanatory_figure` or polished local redraw of current inline figure | Replace or upgrade current `fig-i-partial-carriers-vs-software-change` | This is the chapter’s central distinction. The current inline table is conceptually right but can become a clearer visual: partial carriers orbit the project-level software change. | Produce local SVG/PNG or clean HTML figure; keep as authorial figure. |
| 2 | Lifecycle axis of change: intent → specification → decision → state → execution → evidence → acceptance → maintenance | `source_backed_synthetic_figure` | After “Изменение начинается раньше промпта” or before “Программное изменение как единица анализа” | Helps the reader see the chapter’s real object without dumping all later mechanisms into a table. Must remain a thin axis, not a complete book map. | Use only if caption says it is a minimal axis, not a full taxonomy. |
| 3 | Entry points before specification: chat request / issue / feedback / PR comment / support signal → one change object | `synthetic_explanatory_figure` | Near the section about change beginning before the prompt | Shows why “the prompt” is often a late visible entry point, not the beginning of work. | Optional; useful if the introduction feels too abstract. |
| 4 | `content/assets/story-images/01-boris-agentic-lifecycle.svg` | `local_image_asset`, but `defer` for current chapter | Could support Boris anchor if Chapter I expands story examples | It is a real local story asset showing a lifecycle from intent to agent/code/tests/deployment/ship. But current Chapter I uses stories only as short anchors; direct insertion may make the opening too story-specific. | Keep deferred unless Chapter I gets a richer story sidebar. |
| 5 | `content/assets/theory-images/openai-codex-citations-evidence.webp` | `local_image_asset`, `defer` | Later evidence/governance chapters | It helps evidence/authority, not the unit-of-analysis argument. | Do not insert in Chapter I now. |
| 6 | `content/assets/theory-images/beads-task-graph-memory.svg` | `local_image_asset`, `defer` | Later PWG/durable state chapter | It supports durable work state, not the opening unit-of-analysis. | Do not insert in Chapter I now. |

## External/source notes

- Boris Tane’s source is useful for the “work begins before implementation” anchor, but the existing Boris lifecycle asset is story-specific rather than chapter-level.
- Fowler/Thoughtworks SPDD and Spec Kit sources support the “change has carriers before code” claim, but their diagrams belong to Chapters IV/V or the atlas unless redrawn into a thin chapter-level axis.
- BMAD’s workflow map is a real source image candidate, but it would make Chapter I look like a process catalog.

## Chapter I decision

Best next action: **upgrade the existing central synthetic figure**, not add multiple external images. The figure should explain the unit of analysis and stay small.

---

# Chapter II — `II_agentic_session_trace.md`

## Current visual state

Chapter II currently contains one inline text/synthetic figure: `fig-ii-session-trace-to-state`. Earlier package notes checked but did not insert Simon Showboat/Rodney, browser-observation, PR/CI/review and harness visuals.

The stronger visual pass changes the decision: Chapter II has several high-value source-backed candidates because the external empirical sources themselves contain session diagrams and trace structures.

## Recommended candidates

| Priority | Candidate | Type | Suggested placement | Why it helps | Action |
|---:|---|---|---|---|---|
| 1 | Programming by Chat Figure 1 — annotated failure-driven debugging session | `source_real_image_candidate` or `source_backed_redraw` | Early, after “Зачем вообще смотреть на сессию” | Directly visualizes a real session as alternating user/assistant turns plus behavioral labels. It supports the idea that session trace is more than a prompt. | Prefer source-backed redraw/localization; direct screenshot needs rights/quality pass. |
| 2 | SWE-chat Figure 3 — structure of a coding agent session | `source_real_image_candidate` or `source_backed_redraw` | After “След сессии шире переписки” | Shows session as prompts, agent responses, tool calls, edits/commands and outputs. Very close to the chapter’s central point. | Strong candidate for source-backed redraw. |
| 3 | Existing `fig-ii-session-trace-to-state` upgraded to local image | `synthetic_explanatory_figure` | Keep current placement after “Наблюдение ещё не основание принять изменение” | The current schema is conceptually correct: trace → observations → interventions → external state. It should become a clean local figure, like Chapter VI images. | Convert from inline text to local image/SVG. |
| 4 | Cognition Agent Trace central image — code change linked to conversation / trajectory / line ranges | `source_real_image_candidate` or `source_backed_redraw` | Near “Что должно остаться после обрыва” | Strong for showing why trace must link to code and survive outside chat. Could also belong to PWG or evidence chapter. | Use cautiously; likely redraw as “trace → code ranges → retrievable context.” |
| 5 | `content/assets/story-images/03-simon-showboat-curl-demo.jpg` | `local_image_asset`, secondary | If the Showboat/Rodney example is expanded | Good real source image for “visible demo/evidence,” but it may pull Chapter II toward verification/evidence. | Better deferred to evidence chapter unless II gets a case sidebar. |
| 6 | SWE-chat Figure 2 — usage/failure mode summary | `source_real_image_candidate`, defer | Later evidence/quality chapter | Useful empirical summary, but too metric-heavy for the trace chapter. | Do not insert in Chapter II main text. |

## External/source notes

- `Programming by Chat` provides a source figure showing a representative conversational programming session annotated with behavioral intent labels; it directly supports progressive specification and user intervention.
- `SWE-chat` provides multiple figures: dataset overview, usage/failure summary and session structure. Figure 3 is most relevant to Chapter II.
- `Agent Trace` includes real images and mock UI concepts for attributing code changes to conversation/trajectory; most useful near the transition from trace to durable external state.
- Empirical failure papers contain heatmaps and distributions; these are better for later chapters on evidence, quality and acceptance.

## Chapter II decision

Best next action: **use two figures maximum**:

1. upgraded local `trace → observation → intervention → state` figure;
2. one source-backed redraw from either Programming by Chat Figure 1 or SWE-chat Figure 3.

This keeps Chapter II about the structure of session traces, not a survey of empirical charts.

---

# Chapter III — `III_intent_spec_contract_adr.md`

## Current visual state

Chapter III currently has no figure. Its figure-candidate file says a future figure would be useful, especially a diagram connecting full ADR record, ADR lifecycle and working projection for an agent.

The repository already contains strong local ADR visuals in `content/assets/atlas-images/adr/`:

- `adr-nygard-minimal-record.svg`;
- `adr-madr-template-confirmation.svg`;
- `adr-aws-lifecycle-process.svg`;
- `adr-design-decision-gate.svg`.

These are already source-backed redraws and are much better than creating fresh ad hoc diagrams from scratch.

## Recommended candidates

| Priority | Candidate | Type | Suggested placement | Why it helps | Action |
|---:|---|---|---|---|---|
| 1 | “Спецификация / контракт / ADR: три разных вопроса” | `synthetic_explanatory_figure` or `source_backed_synthetic_figure` | After section 4 or before ADR section | Chapter III’s main risk is substitution: spec, executable contract and decision record are not the same. A compact figure can make this boundary immediately visible. | Create authorial figure; use A2’s `three-artifacts-and-substitutions` as source material. |
| 2 | `content/assets/atlas-images/adr/adr-madr-template-confirmation.svg` | `local_image_asset`, source-backed redraw | Near section 8 about `Confirmation` | Directly supports the point that ADR can include a confirmation/validation bridge, but the confirmation does not replace the decision record. | Strong local candidate. |
| 3 | `content/assets/atlas-images/adr/adr-aws-lifecycle-process.svg` | `local_image_asset`, source-backed redraw | Near section 6 about status and supersession | Supports proposed/accepted/rejected/superseded lifecycle and immutability after acceptance. | Strong local candidate. |
| 4 | “Full record → lifecycle → agent projection” | `source_backed_synthetic_figure` | After section 9, where the chapter explains what to give the agent | This is the candidate already described by the chapter package. It would combine Nygard/MADR/AWS into the chapter’s exact thesis. | Best if only one ADR figure is allowed. |
| 5 | `content/assets/atlas-images/adr/adr-nygard-minimal-record.svg` | `local_image_asset`, secondary | Near first ADR explanation | Good minimal ADR record visual, but may duplicate prose if used with MADR/AWS. | Use only if Chapter III feels too abstract at ADR introduction. |
| 6 | AWS original ADR diagrams | `source_real_image_candidate`, probably redraw already sufficient | Same as AWS lifecycle | AWS page has diagrams for creation/adoption/update; local redraw already captures them better for Russian text and house style. | Prefer existing local redraw. |
| 7 | AgenticAKM Figure 1 | `source_real_image_candidate`, defer | Later technical atlas / architecture knowledge chapter | It shows ADR generators/retrievers/validators in a multi-agent AKM system, but Chapter III is about decision status, not AKM architecture. | Do not insert now. |

## External/source notes

- Michael Nygard’s ADR article supports minimal fields `Context / Decision / Status / Consequences`.
- MADR adds richer metadata and `Confirmation`, which is directly relevant to the chapter’s section 8.
- AWS ADR process documentation contains three diagrams: creation/ownership/adoption, using ADRs in code review, and update/supersession. The existing local redraw is the cleanest publication candidate.
- GitHub CODEOWNERS / branch protection sources are better reserved for governance/authority chapters.

## Chapter III decision

Best next action: **insert one combined ADR figure or two small local ADR figures**:

- minimal option: one synthetic/source-backed figure “full ADR record → lifecycle → agent projection”;
- richer option: `adr-aws-lifecycle-process.svg` plus `adr-madr-template-confirmation.svg`.

Avoid adding raw external ADR screenshots unless there is a specific need to show source UI or original source layout.

---

# Chapter IV — `IV_spdd_specification_lifecycle.md`

## Current visual state

Chapter IV already contains `fig-fowler-spdd-workflow` using local asset `content/assets/theory-images/fowler-spdd-workflow.svg`. The package’s figure-candidate file explicitly says this is the best figure because the chapter needs SPDD as a cycle, not a Canvas catalog.

The visual pass confirms that decision.

## Recommended candidates

| Priority | Candidate | Type | Suggested placement | Why it helps | Action |
|---:|---|---|---|---|---|
| 1 | Existing `content/assets/theory-images/fowler-spdd-workflow.svg` | `local_image_asset` | Keep after “Полный рабочий цикл” | This remains the best central image: it shows SPDD as lifecycle/loop, not as command list. | Keep. |
| 2 | `content/assets/theory-images/fowler-spdd-reasons-canvas.svg` | `local_image_asset`, secondary | After “Как устроен REASONS Canvas” | Could help readers remember the seven parts of the Canvas if the prose feels dense. | Optional; use only if the chapter needs one more explanatory visual. |
| 3 | `content/assets/theory-images/fowler-spdd-overview.svg` | `local_image_asset`, secondary | Near introduction or before workflow figure | Useful if the opening needs an overview of prompt-as-artifact / workflow. May duplicate current workflow. | Usually defer. |
| 4 | `content/assets/theory-images/fowler-spdd-code-review.svg` | `local_image_asset`, defer | Future review/evidence chapter or SPDD technical atlas | Helps explain review/change classification, but can pull Chapter IV too far into verification details. | Defer unless review loop is expanded. |
| 5 | `content/assets/theory-images/fowler-spdd-api-test-script.png` and `fowler-spdd-api-test-results.png` | `local_image_asset`, defer | Evidence/testing chapter or SPDD atlas | Real artifacts from the SPDD example. Useful factual texture, but too detailed for Chapter IV’s theoretical role. | Defer. |
| 6 | OpenSPDD command-template snippets | `source_table_or_code_fragment`, defer | Technical atlas | The command templates are useful for mechanics, not for the main chapter. | Do not insert in Chapter IV main text. |

## External/source notes

- Fowler/Thoughtworks SPDD article contains multiple images: first-class prompts, REASONS Canvas, workflow, API test script/results, code review/change response, prompt-update and regression outputs.
- The current local asset set already preserves the most useful images as SVG/PNG under `content/assets/theory-images/`.
- Direct external images are not needed unless the local assets are stale or missing.

## Chapter IV decision

Best next action: **keep the existing workflow figure**. If one more figure is added, use `fowler-spdd-reasons-canvas.svg`; do not add API test/code-review screenshots to the main theoretical chapter.

---

# Chapter V — `V_protected_specification_profiles.md`

## Current visual state

Chapter V currently has no figure. Its figure-candidate file says a synthetic comparison matrix is the best visual candidate, but the earlier package rejected insertion because the chapter had been carefully kept from becoming a catalog.

The new visual-layer rule changes the decision slightly: a figure is useful if it does not become a scorecard. It should show **where each profile protects the change and where it needs external support**, not rank methods.

## Recommended candidates

| Priority | Candidate | Type | Suggested placement | Why it helps | Action |
|---:|---|---|---|---|---|
| 1 | “Protected specification profiles” comparison matrix | `source_backed_synthetic_figure` | After section 8 “Способ работы выбирают по тому, где изменение может сломаться” | This is the chapter’s strongest visual: Spec Kit, Kiro Specs, TDAD and Constitutional SDD protect different failure points. The matrix can clarify that comparison without turning into a method catalog if written as failure-boundary map. | Produce a local figure/table with careful caption. |
| 2 | Four profile cards: Spec Kit / Kiro / TDAD / Constitutional SDD | `source_backed_synthetic_figure` | After the four method sections, before human-decision section | More readable than one large matrix if the matrix feels too dense. Each card: protects what, strong where, needs support where, poor fit where. | Alternative to Candidate 1. |
| 3 | Spec Kit workflow mini-line: constitution → spec → clarify/checklist → plan → tasks → analyze → implement | `source_backed_redraw` | Near Spec Kit section | Spec Kit docs give a command sequence and workflow logic but not a single strong source image. Redraw is better than screenshot. | Use only if the Spec Kit section needs visual support. |
| 4 | Kiro Specs surface: requirements.md / design.md / tasks.md | `source_backed_redraw` | Near Kiro section | Helps show Kiro as a feature-state surface, not just “another spec.” | Optional; likely better in technical atlas. |
| 5 | TDAD Figure 2 — AST Parser → Graph Builder → Test Linker → Impact Analyzer → `test_map.txt` → AI Coding Agent / SKILL.md | `source_real_image_candidate` or `source_backed_redraw` | Near TDAD section | Very strong diagram for “protected specification via test impact.” Best as source-backed redraw/localized schematic. | High-priority if TDAD section is expanded or gets a sidebar. |
| 6 | TDAD Figure 1 — compilation pipeline / TestSmith / PromptSmith / Compiled Agent / MutationSmith | `source_real_image_candidate` or `source_backed_redraw` | Only if Chapter V talks about behavioral agent specifications, not just code regression | Good figure, but may confuse the two TDAD meanings already distinguished in the text. | Secondary/defer. |
| 7 | Constitutional SDD Figure 1 — Constitution → specification layer → AI generation → implementation → traceability | `source_real_image_candidate` or `source_backed_redraw` | Near Constitutional SDD section | Strong source diagram for upper constraints and traceability. Best as localized redraw if inserted. | Strong secondary candidate. |
| 8 | Constitutional SDD Table 1 — compliance traceability matrix | `source_table_or_code_fragment` / `source_backed_redraw` | Near Constitutional SDD section or evidence chapter | Useful if the chapter needs to show what “traceability” concretely means. But a full table may be too detailed. | Defer or summarize as a small redraw. |
| 9 | `content/assets/theory-images/fowler-sdd-overview.png` | `local_image_asset`, defer | Could support broad SDD framing | Useful but likely too generic compared with the actual four-profile comparison. | Defer. |

## External/source notes

- Spec Kit docs explicitly describe `Spec → Plan → Tasks → Implement` and the richer quality-gate path with constitution, clarify, checklist and analyze; this is better redrawn than screenshotted.
- Kiro docs describe specs through `requirements.md`, `design.md`, and `tasks.md`, including feature and bugfix modes; a small redraw can show the spec surface.
- TDAD papers contain strong diagrams. The graph-based TDAD pipeline is the best match for Chapter V because it shows the agent receiving a static `test_map.txt` and `SKILL.md` rather than a generic instruction.
- Constitutional SDD has a clear hierarchy figure and a compliance traceability matrix; use only if the chapter needs to make constitutional constraints concrete.

## Chapter V decision

Best next action: **add one synthetic/source-backed matrix after section 8**, not four unrelated source screenshots. The figure should compare failure boundaries:

- Spec Kit — ambiguity before plan/tasks;
- Kiro Specs — feature-state surface inside IDE/workflow;
- TDAD — executable behavioral/test impact protection;
- Constitutional SDD — upper constraints and compliance traceability.

Secondary option: add two small source-backed redraws, TDAD pipeline and Constitutional SDD hierarchy, if the profile sections feel under-visualized.

---

# Prioritized insertion plan for I–V

## Minimal visual upgrade

1. Chapter I — polish/replace existing synthetic unit-of-analysis figure.
2. Chapter II — convert `fig-ii-session-trace-to-state` to a local image and optionally add one source-backed session-trace redraw.
3. Chapter III — add one ADR figure: either combined record/lifecycle/projection, or reuse `adr-aws-lifecycle-process.svg` + `adr-madr-template-confirmation.svg`.
4. Chapter IV — keep `fowler-spdd-workflow.svg`; no urgent extra figure.
5. Chapter V — add one protected-profile comparison figure after section 8.

## Strong visual-layer upgrade

- Chapter I: 1–2 figures.
- Chapter II: 2 figures.
- Chapter III: 1–2 figures.
- Chapter IV: 1 existing + optional Canvas figure.
- Chapter V: 1 matrix + optional TDAD/CSDD source-backed redraws.

This would give I–V a balanced visual layer without turning the text into a catalog.

## Candidates to avoid in the main chapters for now

- Broad process maps like BMAD workflow map in Chapter I: too catalog-like.
- Full empirical metric charts in Chapter II: better for evidence/quality chapters.
- Raw ADR screenshots in Chapter III when local source-backed redraws already exist.
- SPDD API test screenshots in Chapter IV: useful for technical atlas/evidence layer, not the main SPDD theory chapter.
- Four separate product screenshots in Chapter V: would make the chapter look like a tool comparison rather than a theory of protected specification profiles.

# Source-read inventory

The pass inspected current repo files and the following external source families:

- SPDD / Fowler / Thoughtworks: `https://martinfowler.com/articles/structured-prompt-driven/` and local SPDD assets.
- Harness Engineering: `https://martinfowler.com/articles/harness-engineering.html`.
- Spec Kit docs and repo: `https://github.github.com/spec-kit/`, `https://github.github.com/spec-kit/quickstart.html`, `https://github.github.com/spec-kit/reference/workflows.html`, `https://github.com/github/spec-kit`.
- Kiro Specs docs: `https://kiro.dev/docs/specs/`, `https://kiro.dev/docs/specs/feature-specs/`, `https://kiro.dev/docs/specs/analyze-requirements/`.
- AWS ADR process/best practices: `https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html`, `https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/best-practices.html`.
- MADR template and Nygard ADR: `https://adr.github.io/madr/decisions/adr-template.html`, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`.
- Programming/session-trace sources: `https://arxiv.org/abs/2604.00436`, `https://arxiv.org/pdf/2604.00436`, `https://arxiv.org/abs/2604.20779`, `https://ar5iv.org/html/2604.20779v1`, `https://www.swe-chat.com/`, `https://arxiv.org/abs/2605.29442`, `https://arxiv.org/pdf/2605.29442`, `https://cognition.ai/blog/agent-trace`.
- Practical story sources: Boris Tane, Peter Steinberger, Mark Erikson, Calvin French-Owen, Simon Willison, Armin Ronacher, HumanLayer.
- TDAD / CSDD / AKM papers: `https://arxiv.org/pdf/2603.08806`, `https://arxiv.org/pdf/2603.17973`, `https://arxiv.org/pdf/2602.02584`, `https://arxiv.org/pdf/2602.04445`.

For PDF sources with candidate figures, screenshots were inspected for the relevant pages before classifying them as visual candidates.

# Next recommended package step

Do not immediately generate all images. First decide the desired visual density per chapter:

- I: central explanatory figure only, maybe one lifecycle axis.
- II: one source-backed session figure + one trace-to-state figure.
- III: one combined ADR figure or two local ADR assets.
- IV: keep one figure unless Canvas comprehension is weak.
- V: one protected-profile matrix; optional TDAD/CSDD redraws only if the sections need anchors.

After this decision, run a dedicated **visual integration pass** that creates/localizes assets and inserts them with captions/alt text.
