# Degradation and duplication audit — Spec Kit article

Статус: P26 guarded final style. Audit records current risks plus relevant historical repairs; stale pass debts have been removed or superseded.

## Function of current article

The article is intended as a concept-first atlas entry for Spec Kit. It should answer how a feature intention becomes a repo-visible transition across specification, plan, tasks, implementation, constitution/checklists, and where human decisions stop the agent.

## P01 self-audit

| Risk | Current status | Evidence / action |
| --- | --- | --- |
| Article becomes dossier summary | Mostly avoided | Structure follows mechanism and reader question, not dossier order, though some source-rich sections may need later tightening. |
| Article becomes CLI manual | Partly controlled | Commands are explained as mechanism surfaces. P05/P09 must prevent flags/integration details from overwhelming concept. |
| Article becomes general SDD theory | Mostly avoided | Section 18 links to theory but does not rebuild full SDLC synthesis. Must re-check later. |
| Article duplicates SPDD/Kiro | Controlled in section 17 | Boundary stated; later passes should keep comparisons local. |
| Technical facts too thin | Not thin for P01 | Article includes files, commands, env variables, scripts, checks and integration mechanics. Requires source-depth verification. |
| Visual layer ignored | Not ignored | External placeholders and synthetic figures were later validated by P11–P13 and P22 public-caption pass; current blocker is asset-pass localization. |
| Human gate unclear | Mostly clear | Gating sections identify spec review, plan review, analyze no-write, implement checklist stop, workflow review, constitution/integration/upgrade decisions. |
| Companion files unsynchronized | Initial sync complete | Source usage, ledger, image plan, external queue, open questions, theory links, audit, readiness report created. |

## Potential degradation points for later passes

1. Source-depth passes may add too many implementation details. Keep technical detail only where it explains the mechanism or boundary.
2. Integration sections may become a table dump. Prefer a concise typology and a few important caveats.
3. Workflows/presets/extensions could turn article into product documentation. Use them to show process-as-repo-infrastructure, not every command.
4. Risks section could become a list of issues. Keep issue-level evidence as caveat, not headline.
5. Synthetic figures must survive usefulness gate; remove if they duplicate prose.

## Readiness for next pass

P01 is `ready_for_P02_with_known_debts`.

## P02 contract and boundary audit

| Check | Result |
| --- | --- |
| Reader question visible in article | Passed: `Контракт статьи` states the repo-workflow question directly. |
| Generic overview risk | Reduced: section-level test now requires every detail to explain agent action after artifact transition. |
| Product/tutorial reference risk | Reduced: installation and commands remain tied to mechanism; later passes must preserve this. |
| Theory repetition risk | Controlled: boundaries with A10/C5 kept as context, no generic blocker added. |
| SPDD duplication | Controlled: SPDD owns prompt/Canvas as intention artifact; Spec Kit owns repo workflow. |
| Kiro duplication | Controlled: Kiro owns productized spec surface; Spec Kit owns portable CLI/repo discipline. |
| Constitutional SDD duplication | Controlled: constitution is a Spec Kit workflow artifact, not the whole security-policy frame. |
| TDAD duplication | Controlled: TDAD owns test-driven control loop; Spec Kit owns artifact-quality gates. |
| ADR duplication | Controlled: ADR owns decision memory; `plan.md` does not replace ADR. |
| PWG duplication | Controlled: Spec Kit chain is lighter than durable graph with owner/dependencies/gates/prime. |

P02 status: `contract_strengthened_ready_for_P03`.

## P03 inventory audit

Inventory did not reveal a missing article-critical theme that requires immediate main-text insertion. Main risk for later passes is overcorrecting by importing too much diagnostic/script detail from the dossier. Keep source-depth additions tied to the reader question: how the next artifact changes permissible agent action.

## P04 source-depth audit

| Check | Result |
| --- | --- |
| Why not one specification file | Strengthened: new subsection explains different readiness criteria for spec, plan, tasks, analyze and implement. |
| Stop points for unresolved questions/constraints/decisions | Strengthened: behavior questions, planning unknowns, task coverage gaps, analyze findings and incomplete checklists are now separated. |
| CLI-manual drift | Controlled: no new flags or command reference table were added. |
| Source/provenance | Controlled: additions rely on already registered primary sources and include inline public links. |
| Visual bloat | Controlled: no new figure was added. |

P04 status: source-depth goal satisfied without expanding article scope.

## P05 source-depth audit

| Check | Result |
| --- | --- |
| Commands as list risk | Reduced: added a state-transition table keyed by input state, repo mutation and handoff/stop. |
| Template/script details | Strengthened: `setup-plan.sh`, `setup-tasks.sh`, created files and active feature state now appear in main article. |
| CLI reference drift | Controlled: flags, PowerShell variants and `--json` diagnostics were deferred. |
| Duplication with P04 | Acceptable: P04 explains why multiple artifacts are needed; P05 explains the command transitions that produce them. |
| Site layout risk | New mild risk: the transition table is wide and may need P13/layout treatment. |

P05 status: source-depth goal satisfied without changing article boundary.

## P06 source-depth audit

| Check | Result |
| --- | --- |
| Constitution as mere artifact | Reduced: main text now says constitution matters only when it changes later artifacts or review. |
| Checklist as checkbox ritual | Reduced: main text now says checklist must route gaps back to artifacts or force a human decision. |
| Formality risk | Added explicitly in risks. |
| Boundary with Constitutional SDD | Controlled: constitution remains local workflow constraint, not full CSDD theory. |
| Visual bloat | Controlled: no new figure added. |

P06 status: source-depth goal satisfied.

## P07 source-depth audit

| Check | Result |
| --- | --- |
| Integrations as mere list | Reduced: main text now frames integrations as files and context the next agent reads. |
| AGENTS/context omitted | Fixed: `agent-context` and managed markers now appear in main article. |
| Presets/extensions as manual detail | Controlled: details are tied to handoff and process visibility, not a full reference. |
| Script layer | Strengthened: `.specify/scripts/` are framed as repo conventions for future agents. |
| Over-detail risk | Controlled for now: integration registry, PowerShell specifics and per-agent tables remain deferred. |

P07 status: source-depth goal satisfied.

## P08 source-depth audit

| Check | Result |
| --- | --- |
| “Intent to implementation” summary risk | Reduced: added active-feature, integration and local-source caveats. |
| Evidence boundaries | Strengthened: issue/PR facts are explicitly bounded as historical or integration-specific evidence. |
| Issue-list bloat | Controlled: only three issue/PR links added; deeper issue history deferred. |
| Troubleshooting-manual drift | Controlled: PowerShell and registry details remain out of main article. |
| Source provenance | Updated: source usage now records issue #975, PR #986 and issue #1926. |

P08 status: source-depth goal satisfied.

## P09 free-expansion audit

| Check | Result |
| --- | --- |
| Chosen underfill | Lifecycle of process infrastructure. |
| Static-method risk | Reduced: article now explains CLI/project-files/integration drift. |
| Operational-manual drift | Controlled: exact upgrade recipe and deep manifest handling deferred. |
| Source specificity | Strengthened with Upgrade Guide, shared infra, manifests and integration lifecycle. |
| Visual impact | No new visual; possible future synthetic upgrade diagram noted. |

P09 status: free expansion completed.

## P10 free-expansion audit

| Check | Result |
| --- | --- |
| Reader path | Strengthened: added a concrete route through one feature directory. |
| Tutorial drift | Controlled: route is framed as review, not step-by-step commands. |
| C5 model compliance | Improved: mechanism, artifacts, checks, limits and theory backlink are easier to follow. |
| Source specificity | Maintained: all route steps cite existing primary sources. |
| Visual impact | No new visual; possible callout/table later. |

P10 status: free expansion completed.

## P11/P12 visual audit

| Check | Result |
| --- | --- |
| Local asset not degraded into prose | Passed: `fowler-sdd-overview.png` inserted as `<img>` with bounded public caption. |
| External images not downloaded prematurely | Passed: P12 kept official docs and arXiv images as external-real placeholders. |
| Research figure overclaim | Controlled: `fig-spec-kit-agents-context-hooks` caption says research extension, not official baseline. |
| Spec Kit-specific visual debt | Still open: official docs/workflow candidates remain queued; Fowler image is not counted as replacement. |
| Decorative visual risk | Controlled for now: each figure supports positioning, workflow gate, machine state, context-blindness or SDD boundary. |

P12 status: visual candidates are mirrored in article, image plan and external queue without replacing real assets by synthetic figures.

## P13 synthetic visual audit

| Check | Result |
| --- | --- |
| Synthetic figure gate | Passed: no new synthetic figure was added. |
| Existing `fig-spec-kit-repo-layers` | Kept: nontrivial topology, not a decorative restatement. |
| Existing `fig-active-feature-resolution` | Kept: captures non-obvious active-feature fallback order. |
| External asset replacement risk | Controlled: no external/local real candidate was replaced by a new synthetic diagram. |
| Density risk | Moderate: final layout should check whether four external placeholders plus one local image plus two synthetic figures is too much. |

P13 status: synthetic visual layer is intentionally sparse.

## P14 standalone audit

| Check | Result |
| --- | --- |
| Standalone readability | Improved: a local minimal model now appears before the command-heavy sections. |
| Theory duplication | Controlled: the subsection names only five terms needed to read Spec Kit. |
| CLI-reference drift | Controlled: no new flags or commands were added. |
| Visual bloat | Controlled: no new diagram was added. |
| Boundary with SPDD/Kiro | Preserved: the minimal model is about Spec Kit's repo workflow, not general SDD taxonomy. |

P14 status: standalone concept layer strengthened without expanding scope.

## P15 mechanism/failure-mode audit

| Check | Result |
| --- | --- |
| Failure catalog risk | Controlled: no separate error catalog was created; each failure mode appears inside the section where the mechanism can fail. |
| Feature/source overview drift | Controlled: added paragraphs explain transitions and boundaries, not additional feature inventory. |
| Spec/plan/tasks responsibility | Improved: the article now names polished specs, decorative plans and mechanical task lists as distinct state-transfer failures. |
| Evidence overclaim | Improved: verification section now separates checklist, analyze, environment and integration evidence. |
| Lightweight boundary | Improved: the limits section now says full Spec Kit is justified by ambiguity, risk and handoff need, not by document count. |
| Visual bloat | Controlled: no new diagram or external candidate was added. |

P15 status: mechanism and failure boundaries strengthened without changing source set or image set.

## P16 theory-link audit

| Check | Result |
| --- | --- |
| Theory rewrite risk | Controlled: main text received one compact paragraph, while the detailed map lives in `theory_links`. |
| Semantic-link requirement | Passed: links now state the question each theory node uses Spec Kit to illuminate. |
| Feature/source overview drift | Controlled: no new Spec Kit source facts or CLI flags were added. |
| Boundary with neighboring methods | Preserved: P16 reinforces Spec Kit as repo workflow, not SPDD, Kiro, Constitutional SDD, TDAD, ADR or PWG. |
| Visual bloat | Controlled: no visual change. |

P16 status: article now has explicit bidirectional theory routing without becoming a theory chapter.

## P17 language audit

| Check | Result |
| --- | --- |
| Russian prose mode | Improved: ordinary English glue in the article was translated or localized. |
| Fact preservation | Passed: no source fact, boundary or figure decision was removed. |
| Over-translation risk | Controlled: exact command names, files, paths, source titles, labels and stable tool surface terms were preserved. |
| Argument drift | Controlled: language edits did not change the article's mechanism. |

P17 status: first Russian-language cleanup complete; a later pass may still smooth remaining bilingual technical terms.

## P18 language audit

| Check | Result |
| --- | --- |
| Human technical style | Improved: opening, captions and asset section now read less like workflow metadata. |
| Content preservation | Passed: no command fact, source, boundary or image status was removed. |
| Caption clarity | Superseded by P22: inline captions now read as public article captions; asset status lives in attributes/queue. |
| Companion-facing text | Improved: bottom asset section uses Russian placement and rights/quality wording. |

P18 status: second language pass complete; remaining English is mainly exact names, commands, paths, labels or stable integration terms.

## P19 editorial audit

Problems identified before fixing:

| Problem | Risk to article | Result after fix |
| --- | --- | --- |
| Loose `analyze` references in prose | Weakened the state-transition/gate argument. | Normalized to `/speckit.analyze` where the command/gate is meant. |
| Duplicated or awkward wording around constitution conflicts and handoff grammar | Made source-grounded sections feel less trustworthy. | Corrected wording without altering claims or citations. |
| Bottom image-candidate block looked like production metadata | Could break standalone concept-first reading. | Temporarily contained as asset-preparation metadata; P22 later restored the required `Внешние изображения для asset-pass` heading and public captions. |
| Remaining bilingual terms | Checked: remaining English is mainly exact source titles, commands, fields, paths, labels or named neighboring methods. | Controlled; no over-translation applied. |

P19 status: editorial pass improved standalone readability while preserving source facts, boundaries, images and transfer ledger commitments.

## P20 editorial audit

Problems identified before fixing:

| Problem | Risk to article | Result after fix |
| --- | --- | --- |
| Dense neighbor-method boundary at the top | Could make the standalone article feel like taxonomy before mechanism. | Split into two paragraphs while keeping the same boundaries. |
| Awkward scope-exclusion wording before planning | Could obscure a real pre-plan review question. | Rephrased the scope check. |
| Shorthand evidence terms | Could blur which check proves which object. | Replaced with exact command surfaces in the evidence and theory-return sections. |
| Visual/editorial drift | Checked: no visual placement or status changed. | Controlled; image plan and external queue remain stable. |

P20 status: second editorial pass improved readability and command precision without changing source facts or article scope.

## P21 editorial audit

Problems identified before fixing:

| Problem | Risk to article | Result after fix |
| --- | --- | --- |
| Bare English integration terms in explanatory prose | Could make the standalone article feel like a source inventory rather than Russian concept prose. | Added Russian glosses for `skills`, `recipes`, `wrappers`, `skill`, `recipe` and `wrapper` where useful. |
| Synthetic figure language drift | Diagram labels mixed Russian structure with English-only surface terms. | Localized the label while preserving exact command and integration terms. |
| Ordinary `prompt` wording | Some non-source-title prose remained unnecessarily English. | Localized ordinary prompt wording without changing SPDD/OpenSPDD boundary. |
| Over-translation risk | Exact file paths, commands, labels and integration identifiers could be harmed by translation. | Controlled: exact identifiers remain in code style or source-title form. |

P21 status: third editorial pass improved terminology consistency without changing claims, sources, boundaries or image queue.

## P22 public-structure audit

Problems identified before fixing:

| Problem | Risk to article | Result after fix |
| --- | --- | --- |
| Entry sequence exposed contract/taxonomy too early | First screen could feel like atlas governance rather than a public article. | Problem statement, reader question and first visual source frame now come before the contract section. |
| Service wording in inline figure captions | Captions could look like executor notes instead of article material. | Rewrote captions as public explanations; asset status remains in attributes and queue. |
| Bottom image section name drift | P19/P20 temporary wording no longer matched visual-rule expectations. | Restored `Внешние изображения для asset-pass` and kept metadata out of the main argument. |
| Visual degradation risk | External candidates could have been removed or replaced by prose. | Controlled: all external candidates remain inline placeholders plus queue metadata; no synthetic replacement added. |

P22 status: public entry structure and visual captions now match the concept-atlas visual rules.

## P23 companion-sync audit

Problems identified before fixing:

| Problem | Risk | Result after fix |
| --- | --- | --- |
| Stale pass-specific debts in source/image/open-question files | Companions could imply unfinished work that the article has already resolved. | Removed or superseded stale P04–P13 verification/debt wording in current-status areas. |
| Open questions had become a pass-history archive | Real blockers were diluted by old consolidation reminders. | Rewrote `open_questions` around asset-pass, freshness, layout and package guardrails only. |
| Image plan and queue had mixed current status with earlier draft labels | Visual state could be misread as still awaiting P11–P13 rather than asset-pass. | Updated statuses to P23 and kept only real visual blockers. |
| Generic C5/A10 debt-language | Could suggest unresolved theory sync. | Closed it explicitly and kept only concrete theory backlinks/guardrails. |

P23 status: companions now reflect the actual article state; current blockers are specific and actionable.

## P24 style-defect audit

| Defect class checked | Result |
| --- | --- |
| Pseudo-technical metaphors | Replaced “садится в репозиторий”, “техническая посадка”, “высаживается в файлы” and “ремонт жизненного цикла” with plainer technical wording. |
| Heavy noun chains | Tightened “проектная методологическая инфраструктура”, manifest/provenance wording, task-link wording and section-18 bridge prose. |
| Overused contrast formula | Reduced several “не X, а Y” constructions where sequential explanation was clearer; retained contrasts only where they mark a real boundary. |
| Content preservation | No factual source, image candidate or theory boundary was removed; edits stayed local and stylistic. |

## P25 selective natural rewrite audit

| Area | Result |
| --- | --- |
| Core title/question | Reworded into a natural “passes through repo artifacts” formulation while preserving the transition thesis. |
| English/calque cleanup | Replaced ordinary “промпт” in non-source prose, “файлы промптов”, “репозиторный diff”, and “плотное соседство” with more natural Russian. |
| Neighbor boundary preservation | Kept exact prompt/Canvas and product/method names where they are boundary terms rather than ordinary prose. |
| Content preservation | No source fact, figure, boundary or article structure was removed. |

## P26 guarded final style audit

| Area | Result |
| --- | --- |
| Tone and rhythm | Opening, problem section and theory bridge now use direct technical explanation instead of abstract control-language. |
| Subheadings and transitions | Existing structure preserved; wording around initialization, layers and route review is more natural. |
| Specificity | Commands, files, issue/PR examples, figure statuses and source boundaries stayed intact. |
| New risks | No new source, image or theory debt introduced. |
