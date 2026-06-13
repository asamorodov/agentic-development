# BMAD Method — source usage

Статус: P26 завершил финальный guarded style pass; источники, фактура и visual queue не изменились. Текущие блокеры прежние: свежесть BMAD docs/releases и asset-pass для Workflow Map.

| Источник | Где использован в статье | Что поддерживает | Статус / оговорка |
| --- | --- | --- | --- |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/README.md | «Установка: где в репозитории живёт BMAD», «Роли как распределение суждения» | Позиционирование BMAD, prerequisites, `npx bmad-method install`, 12+ domain experts, modules/web bundles context. | Требует свежей проверки перед публикацией. |
| https://github.com/bmad-code-org/BMAD-METHOD | Косвенно через README/releases/source skill links | Primary repo surface, skill paths, releases. | Main branch mutable; final article should pin retrieval date/version. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md | Intro, «Инвариант BMAD», «Главная цепочка», PRD, UX, implementation workflows, readiness, Quick Flow framing. | Фазы, progressive context building, смена артефакта, задающего рамку работы, `bmad-prd`, workflow outputs, `bmad-check-implementation-readiness`, correct-course/status/investigate. | Core source for mechanism; version-sensitive names. |
| https://docs.bmad-method.org/workflow-map-diagram.html | Inline external image candidate, roles section, external image queue. | Visual map, personas Mary/John/Sally/Winston/Amelia, artifact flow, Quick Flow, Workflow Map V6 source page. | External real image candidate; before publication needs download, rights, quality, attribution and localization check. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md | Installation tree, phases, modes, fresh chats, story-count caveat. | `_bmad/`, `_bmad-output/`, Quick/BMad/Enterprise modes, fresh implementation chats. | Some docs may lag releases. |
| https://docs.bmad-method.org/how-to/install-bmad/ | Installation caveats. | `manifest.yaml`, `--pin`, channel reproducibility, GitHub API/token note. | Needs version/date in final. |
| https://github.com/bmad-code-org/BMAD-METHOD/releases | PRD skill name transition, v6.8 config and UX/spec changes. | v6.7 `bmad-prd` unification/shims; v6.8 `bmad-spec`, UX contract, config evolution. | Highly freshness-sensitive. |
| https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.7.0 | PRD shim note. | Readable release mirror for v6.7 PRD changes. | Secondary helper only; GitHub Releases remains preferred. |
| https://newreleases.io/project/github/bmad-code-org/BMAD-METHOD/release/v6.8.0 | UX/spec release framing. | Readable mirror for v6.8 UX/spec changes. | Secondary helper only. |
| https://docs.bmad-method.org/reference/core-tools/ | `bmad-spec` section. | `SPEC.md`, `Why`, `Capabilities`, `Constraints`, `Non-goals`, `Success signal`. | Needs freshness check. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md | `project-context.md` section, stale context risk. | Project context purpose, automatic loading, manual/generation paths, not generic best practices. | Stable conceptual function; path/version-sensitive. |
| https://docs.bmad-method.org/explanation/architecture/why-solutioning-matters/ | Full BMAD mode / architecture. | Why architecture precedes implementation. | Used with Preventing Agent Conflicts. |
| https://docs.bmad-method.org/explanation/preventing-agent-conflicts/ | Architecture section, risks. | Agent conflict examples, ADR fields, FR/NFR, implicit decisions, over-documentation, stale architecture. | Strong source for architecture boundary. |
| https://docs.bmad-method.org/how-to/quick-fixes/ | Quick Flow section, misuse risks, P09 scope boundary. | `bmad-quick-dev`, accepted inputs, short spec approval, tests, local commit, `git revert HEAD`, `deferred-work.md`, boundary to full BMAD. | Needs version/date before final. |
| https://docs.bmad-method.org/explanation/quick-dev/ | Quick Flow section, P09 mini-lifecycle and repair-layer paragraphs. | Intent compression into one consistent goal, minimal safe path, spec approval, human control points, diagnosis by intent/spec/implementation layer. | Needs version/date before final. |
| https://docs.bmad-method.org/how-to/established-projects/ | Brownfield and project-context sections. | Clean old artifacts, UX conditions, project-context generation, document-project suggestion. | Important brownfield source. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/core-skills/bmad-help/SKILL.md | Roles/navigation section. | `bmad-help` as state/navigation mechanism. | Raw skill path mutable. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md | Story section, gates, validation. | Story context loading, prevention failures, user intervention, story checklist, status update. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md | Story section. | Exact-order execution, allowed story-file fields, `baseline_commit`, review follow-ups. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-planning/SKILL.md | Sprint status section. | YAML state machine, key conversion, validation, epic/story/retro statuses. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md | Sprint status section. | Status reading, normalization, risks, next-action priority. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md | Review section. | Adversarial review, Blind Hunter, Edge Case Hunter, Acceptance Auditor, step-file architecture. | Key technical anchor. |
| https://docs.bmad-method.org/explanation/faq/implementation-faq/ | Gates/status/retrospective sections. | Manual story `review` → `done`, retrospective after each epic. | Used for manual joins. |
| https://docs.bmad-method.org/explanation/checkpoint-preview/ | Review section. | Checkpoint Preview purpose, inputs, concerns walkthrough, blast radius, no pass/fail. | Good example of human review interface. |
| https://docs.bmad-method.org/reference/testing/ | QA/TEA section. | Built-in QA scope and TEA overview/workflows. | Distinguish built-in QA from TEA. |
| https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/ | TEA overview. | `bmad-tea`, workflows/triggers, `GATE` helper boundary. | Extension source. |
| https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/ | Enterprise section, gates, risk. | Compliance/security/audit/NFR, evidence artifacts, approvers, release gate, retention. | Extension source; not base BMAD requirement. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md | Correct Course section. | Context loading, sprint-change proposal output, modes, approval, handoff. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md | Correct Course section, risks. | Change Navigation Checklist, impact analysis, direct adjustment / rollback / PRD MVP review. | Key technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md | Gates and retrospective section. | Partial retrospective, story/review/testing/debt/next epic inputs. | Implementation-side anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md | Investigation section. | Inputs, case files, diagnostic boundary, grades, confidence, routes after investigation. | Key technical anchor. |
| https://docs.bmad-method.org/explanation/forensic-investigation/ | Investigation section. | Conceptual role of forensic investigation. | Used with raw skill. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md | Brownfield section. | Router, scan state, resume/re-scan/deep-dive/archive/index behavior. | Key brownfield anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md | Brownfield section. | Scan levels, generated docs, write-as-you-go state, cleaning context. | Key brownfield anchor. |
| https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md | Brownfield section, risks. | Validation checklist, scan completeness, project-type flags, no placeholders/TODO. | Key brownfield validation source. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/documentation-requirements.csv | Brownfield section. | 12 project types and requirement flags such as API/data/state/UI scans. | Raw CSV technical anchor. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/deep-dive-instructions.md | Brownfield section. | Deep-dive full-file review, no sampling/guessing/tool-output-only. | Key boundary source. |
| https://www.bmadcode.com/ | Review/source caveat section. | Site-level PRD Coach / marketing signals from dossier. | Marketing surface; use cautiously. |


## P02 boundary sources

P02 добавил в основной текст явный article contract и границы с соседними методами. Эти источники не переводят статью в comparative overview; они поддерживают только negative boundary.

| Источник | Где использован | Что поддерживает | Статус / оговорка |
| --- | --- | --- | --- |
| https://www.opengsd.net/ | «Контракт статьи», «Где BMAD помогает общей теории» | GSD/Open GSD как соседняя методология вокруг disciplined AI-agent development and context-management problem. | Source from allowed GSD dossier; needs freshness check before final. |
| https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | «Контракт статьи» | GSD phase loop and Verify boundary; supports BMAD ≠ GSD framing. | Main branch mutable. |
| https://www.opengsd.net/docs/v1/architecture | «Контракт статьи» | GSD command/workflow/agent/file architecture and thin orchestration boundary. | Versioned docs but still freshness-sensitive. |
| https://gastownhall.github.io/beads/ | «Контракт статьи» | Beads as adjacent work-graph/issue-tracking surface for PWG boundary. | Used only for boundary, not as BMAD source. |
| https://gastownhall.github.io/beads/architecture | «Контракт статьи» | Beads architecture as durable graph/state layer. | Needs final article version/date check. |
| https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md | «Контракт статьи» | Dependency semantics for PWG boundary. | Main branch mutable. |
| https://gastownhall.github.io/beads/recovery | «Контракт статьи» | Recovery surface for PWG boundary. | Needs final source check. |
| https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | «Контракт статьи» | Gas Town as operating environment, not BMAD process article. | External essay; use as boundary only. |
| https://github.com/gastownhall/gastown | «Контракт статьи» | Gas Town public repo surface. | Main branch mutable. |
| https://gastownhall.github.io/beads/multi-agent | «Контракт статьи» | Multi-agent Beads coordination boundary. | Adjacent-method source. |
| https://github.github.com/spec-kit/reference/workflows.html | «Контракт статьи» | Spec Kit workflow boundary. | Needs freshness check. |
| https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md | «Контракт статьи» | Spec-driven development framing and chain. | Main branch mutable. |
| https://kiro.dev/docs/specs/ | «Контракт статьи» | Kiro Specs as spec-state/product surface. | Current public docs should be refreshed later. |
| https://kiro.dev/docs/specs/feature-specs/ | «Контракт статьи» | Feature specs with requirements/design/tasks boundary. | Current public docs should be refreshed later. |
| https://martinfowler.com/articles/structured-prompt-driven/ | «Контракт статьи» | SPDD as structured prompt / intent-artifact method. | Stable article source. |
| https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md | «Контракт статьи» | open-spdd design philosophy boundary. | Main branch mutable. |
| https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | «Контракт статьи» | ADR as architecture decision record, not full execution process. | Stable primary source. |
| https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | «Контракт статьи» | ADR concept/status/consequences boundary. | Stable article source. |
| https://adr.github.io/madr/ | «Контракт статьи» | MADR template/status discipline. | Stable public template site. |

P02 did not introduce public claims from C5 or A10 into the article body. C5/A10 remained read-only atlas context; no generic `C5/A10 pending` debt was created.


## P03 dossier inventory notes

P03 re-read the BMAD dossier as an inventory pass. No new article-critical fact was added to the main text. The following source classes are now explicitly tracked for future passes.

| Source class / examples | Current article status | Why not expanded in P03 |
| --- | --- | --- |
| Installation low-level details: `--set`, `GITHUB_TOKEN`, API-rate limits | Deferred | Useful for installation handbook, not for concept-first BMAD mechanism. |
| Quick Dev explanation (`/explanation/quick-dev/`) and `deferred-work.md` details | Promoted in P09 | Main article now explains Quick Dev as compressed lifecycle with intent compression, spec approval, deferred unrelated work and layer-aware repair. |
| Core Tools catalog beyond `bmad-help` and `bmad-spec` | Deferred | Party Mode, sharding/indexing and helper catalog would turn the article into product reference. |
| Exact `bmad-check-implementation-readiness` output/report anatomy | Candidate for future source-depth | Main text only needs readiness gate concept now. |
| Story template/checklist fields | Candidate for future source-depth | Current story section is strong but can be anchored further later. |
| Correct Course proposal anatomy | Candidate for future source-depth | Main text covers repair loop; detailed proposal structure could support a future figure or handbook note. |
| Investigation case-file / confidence structure | Candidate for future source-depth | Current article includes evidence ladder in prose; detailed field list is deferred. |
| Brownfield `documentation-requirements.csv` complete 12-type / 24-column schema | Deferred | Article uses the CSV to show data-driven scan completeness; full table belongs in source/handbook pass. |
| Enterprise/TEA detailed workflows beyond release gate and evidence package | Deferred | Prevents TEA from swallowing the base BMAD article. |
| Community/adoption friction sources: Ran the Builder, Reddit threads, GitHub issues #511/#813/#1629, Rovo thread | Not used as evidence | Dossier marks them as anecdotal/discussion artifacts; they require explicit source evaluation before public claims. |
| Search formulations | Not source material | Use only when a later working sheet explicitly permits web/source refresh. |

P03 confirms that `bmad_method_source_usage.md` remains a source map, not a proof of total dossier coverage.


## P04 source-depth notes: documentary handoff

P04 strengthened the main article using already tracked BMAD primary sources. No new external source was introduced.

| Source | P04 use | Notes |
| --- | --- | --- |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md | Supports handoff chain and “documents inform next stage” framing. | Already in P01 source map; cited near the new handoff paragraph. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md | Supports phase/order/fresh-chat context for handoff reading. | Already in P01 source map; cited near the new handoff paragraph. |
| https://docs.bmad-method.org/workflow-map-diagram.html | Supports role/persona placement in workflow diagram. | Already in source map and image queue. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md | Supports role-to-story transfer and story as implementation context. | Already in source map. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md | Supports dev-story as reproducible execution trace. | Already in source map. |

P04 did not use community, issue, marketing or adjacent-method sources.


## P05 source-depth notes: file mechanics and recovery

P05 used existing tracked BMAD sources and added no new external source.

| Source | P05 use | Notes |
| --- | --- | --- |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/tutorials/getting-started.md | Supports `_bmad/`, `_bmad-output/`, planning/implementation artifacts and fresh-chat recovery framing. | Already tracked. |
| https://docs.bmad-method.org/how-to/install-bmad/ | Supports manifest/pinning/reproducibility warning. | Already tracked. |
| https://github.com/bmad-code-org/BMAD-METHOD/releases | Supports config evolution warning around TOML/fallback. | Already tracked; freshness-sensitive. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md | Supports next-action priority from `sprint-status.yaml`. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md | Supports story file as execution/recovery trace. | Already tracked. |

P05 deliberately did not add installer handbook details such as `--set`, API-rate limits or environment-specific troubleshooting.


## P06 source-depth notes: brownfield/document-project

P06 used already tracked BMAD primary sources; no new external source was introduced.

| Source | P06 use | Notes |
| --- | --- | --- |
| https://docs.bmad-method.org/how-to/established-projects/ | Supports stale-doc cleanup and `project-context.md`/document-project start for established projects. | Already tracked; cited in stale-doc paragraph. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/instructions.md | Supports router, `project-scan-report.json`, resume/re-scan/deep-dive/archive behavior. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md | Supports scan levels, generated docs, state updates and context cleanup after writing docs. | Already tracked. |
| https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/1-analysis/bmad-document-project/checklist.md | Supports validation checklist, scan completeness and project-type flags. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/documentation-requirements.csv | Supports documentation requirement flags for API/data/state/UI completeness. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/deep-dive-instructions.md | Supports Deep Dive as full-file-review mode for selected area. | Already tracked. |

P06 still does not import the full 12 project type / 24-column CSV schema into the article; that remains a deferred source-depth/handbook option.


## P07 source-depth notes: review, correct-course, human gates

P07 used already tracked BMAD primary sources; no new external source was introduced.

| Source | P07 use | Notes |
| --- | --- | --- |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md | Supports PRD intent/validation and readiness gate framing. | Already tracked. |
| https://github.com/bmad-code-org/BMAD-METHOD/releases | Supports version caveat around PRD validation pipeline. | Already tracked; freshness-sensitive. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md | Supports create-story start choices and status update. | Already tracked. |
| https://docs.bmad-method.org/explanation/checkpoint-preview/ | Supports checkpoint preview as human reading map, not pass/fail. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-code-review/SKILL.md | Supports code-review checkpoints and adversarial layers. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md | Supports correct-course modes, proposal and approval. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/checklist.md | Supports impact analysis and direct adjustment / rollback / PRD MVP review. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-investigate/SKILL.md | Supports diagnosis/route boundary. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md | Supports retrospective as post-epic learning/debt/preparation decision. | Already tracked. |

P07 did not add TEA detail beyond already tracked release gate and approval notes.


## P08 source-depth notes: evidence/release extensions and failure modes

P08 used already tracked BMAD primary sources; no new external source was introduced.

| Source | P08 use | Notes |
| --- | --- | --- |
| https://docs.bmad-method.org/reference/modules/ | Supports BMM/core/module boundary and TEA as separate module. | Already tracked. |
| https://docs.bmad-method.org/reference/testing/ | Supports built-in QA vs TEA boundary. | Already tracked. |
| https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/ | Supports TEA module overview. | Already tracked. |
| https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/how-to/brownfield/use-tea-for-enterprise/ | Supports Enterprise evidence, compliance, approvers, release gate and retention. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md | Supports structural token/context cost from large context loading. | Already tracked. |
| https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/1-analysis/bmad-document-project/workflows/full-scan-instructions.md | Supports context cleanup after writing docs during full scan. | Already tracked. |
| https://github.com/bmad-code-org/BMAD-METHOD/releases | Supports module/surface churn and release-sensitive commands/config. | Already tracked; freshness-sensitive. |

P08 did not use Reddit, community reports or GitHub issues as evidence for token cost. The article frames token cost as a structural mechanism supported by BMAD workflow behavior, not a measured adoption statistic.

## P09 source notes: Quick Dev mini-lifecycle

P09 chose Quick Dev as the main remaining technical under-specification. Before P09, the article described Quick Flow through input forms, short spec approval, tests, local commit and revert path, but did not make the inner lifecycle explicit.

Material added to the main article:

- Quick Dev as a small lifecycle rather than process absence: raw intent is compressed into one consistent goal, then the workflow chooses a minimal safe path.
- Human control points in short mode: intent clarification, short spec/plan approval when the change is not trivial, and final result review.
- Scope boundary through `deferred-work.md`: unrelated or pre-existing work is recorded/deferred instead of silently entering the diff.
- Failure diagnosis by layer: intent, short specification, or implementation; repair should return to the failed layer instead of blindly patching the diff.

Primary sources used: Quick Fixes and Quick Dev explanation pages already present in the BMAD dossier. Remaining debt: exact current file names, generated spec trace and `deferred-work.md` behavior require a fresh source/version check before publication.

## P10 source notes: reader-path invariant

P10 added a connective section, not a new public-source factual block. The deficiency selected: the article had strong details but lacked a compact reader path for understanding why all surfaces belong to one mechanism.

Source use:

- BMAD Workflow Map remains the public factual anchor for progressive context building and documents informing the next stage.
- C5 was used as an internal editorial/theory constraint: an atlas article must be independently readable from a concept-first entry and should expose pressure, mechanism, technical surfaces, failures and return links without becoming a command catalog.
- No new external public source was added.

Material added: the “artifact that frames the next step” invariant and four properties of a useful BMAD artifact: narrow enough for fresh context, explicit enough for human correction, source-linked enough to resist agent fantasy, and alive enough to receive review/status/lessons/correct-course feedback.

## P11 source/asset notes: local visual asset pass

P11 added no source facts to the main article. It checked the local asset catalog and the explicitly listed Fowler harness images as visual candidates only.

Decision: no local image was inserted. The reviewed Fowler harness images are real local assets, but they support Fowler’s harness-engineering article, not BMAD-specific workflow maps, BMAD role/artifact diagrams, `_bmad/` file trees, sprint-status state, brownfield document-project flows, checkpoint/correct-course surfaces or TEA/release-gate visuals.

Consequence for source usage: Fowler harness sources remain external theory/background assets, not BMAD article sources. The BMAD article continues to rely on BMAD primary sources and the existing external-real BMAD workflow-map candidate.

## P12 source/asset notes: external real images

P12 started from the BMAD dossier image-candidate list and the external-real candidate catalog. It then inspected the official BMAD Workflow Map surfaces. Decision: the existing inline placeholder for `fig-bmad-workflow-map` remains the only external-real image candidate for the BMAD article.

Disposition of dossier candidates:

- Official Workflow Map Diagram: kept inline and mirrored in the bottom asset-pass section and external image queue.
- Getting Started project tree: source table/code fragment; current article uses a text tree, no screenshot needed.
- Sprint-status state machine and context-flow diagrams: already represented as synthetic figures.
- Quick Dev, SPEC compression, QA/TEA, brownfield, Document Project validation, Correct Course, investigation ladder, TEA release-gate, cost/depth, BMAD vs Gas Town: synthetic/editorial candidates only; no external real image added in P12.

No image was downloaded. Remaining debt: rights, quality, attribution and localization/capture for the Workflow Map diagram before publication.

## P13 source/asset notes: synthetic figure restraint

P13 added no new source facts and no new synthetic figure. Existing source-supported visuals are sufficient for the current article structure:

- `fig-bmad-context-cascade` already explains artifact handoff.
- `fig-bmad-sprint-state-machine` already explains minimal state lifecycle.
- `fig-bmad-workflow-map` remains the real external candidate for the official workflow map.

Deferred candidates such as Quick Dev boundary, SPEC compression, brownfield flow and TEA release gate remain design ideas, not source changes.

## P14 source notes: standalone concept example

P14 added an illustrative audit-report example to strengthen standalone concept-first readability. It does not add a BMAD source fact or claim that BMAD documentation uses that example.

Source basis:

- Existing BMAD sources already support the flow used in the example: PRD, UX, architecture/ADR, epics/stories, sprint status, create-story, dev-story, review, retrospective and correct-course.
- C5 and the concept-atlas article map were used as internal editorial constraints: a BMAD reader should understand the concept locally without assembling it from theory chapters.

Remaining source debt: none for the example as an example; later fact-check should ensure no phrasing makes it sound like an official BMAD case study.

## P15 source notes: mechanism, boundaries, failure modes

P15 added interpretive mechanism/failure wording, not new source facts. The added text uses existing BMAD source anchors already present in the article:

- Workflow Map / progressive context building for documents as next-step inputs.
- Role/workflow skill sources for roles producing/checking artifacts rather than acting as decorative personas.
- Existing Quick Flow / Enterprise / TEA sources for mode-confusion and evidence-layer boundaries.
- Existing brownfield/project-context/story/status sources for stale artifact risk.

No new public source was introduced in P15.

## P16 semantic-backlink source sync

| Input | P16 use | Article effect | Source debt |
| --- | --- | --- | --- |
| `00_spine_map.md` | Internal theory frame for software-change lifecycle and carriers | Reflected in `theory_links` as a semantic backlink, not cited as public BMAD fact. | None for article publication; internal theory cross-link only. |
| `A3_specification_methodologies_synthesis.md` | Specification-layer question: when intent artifact gets authority before action | Strengthened theory_links boundary: BMAD uses specs but is wider than spec-only lifecycle. | No new public source facts. |
| `A5_process_methodologies_synthesis.md` | Process-profile question: process vs ceremony | Strengthened theory_links and main theory paragraph. | No new public source facts. |
| `A7_observation_vs_evidence.md` | Observation/evidence distinction | Strengthened theory_links around review, investigation and TEA. | No new public source facts. |
| `A9_lifecycle_repair.md` | Repair surface selection after result/failure | Strengthened theory_links around correct-course, retrospective, stale artifacts. | No new public source facts. |
| `A10_mode_selection_map.md` | Mode-depth selection by risk | Strengthened theory_links around Quick/Full/Enterprise. | No new public source facts. |
| `C5_theory_to_technical_atlas.md` | Standalone article / backlink contract | Added one guard sentence in main article and detailed theory_links matrix. | None. |

## P17 language-pass source sync

P17 edited the main article for Russian technical style: translated accidental English glue (`gates`, generic `workflow`, `evidence layer`, `module confusion`, mixed `artifact-first` phrasing) while preserving official names, commands, file paths, source labels and stable BMAD terms. No factual claim, citation, source boundary or source priority changed.

## P18 — синхронизация источников после языкового прохода

P18 повторно проверил русский текст после P17: заголовки, подписи, таблицы и нижний раздел для прохода по ассетам. Исправлены формулировки вроде «текущее состояние спринта», placeholder Workflow Map и asset-pass section переведены в более естественный русский, а source-specific labels сохранены там, где важна точная форма. Проход не добавлял, не удалял и не менял приоритет фактов, ссылок или границ.

## P19 — синхронизация источников после редакторского прохода

P19 не был источниковым проходом и не менял набор ссылок. В статье добавлен редакторский критерий проверки BMAD перед передачей работы дальше: назвать текущий артефакт, задающий рамку работы, следующий рабочий процесс, человеческое решение и место возврата найденного факта. Это синтез уже раскрытой логики статьи, а не новая внешняя фактура.

## P20 — синхронизация источников после второго редакторского прохода

P20 не менял источники, ссылки или фактические утверждения. Контрактный раздел с границами BMAD переставлен после минимального примера, чтобы читатель сначала увидел практическую механику метода, а уже затем сравнительные границы с GSD, PWG, Gas Town, Spec Kit, Kiro, SPDD, TDAD и ADR.

## P21 — синхронизация источников после третьего редакторского прохода

P21 не менял источники и ссылки. Правки касались редакторской навигации: добавлен переход от контрактного раздела к устройству метода, уточнены заголовки про `bmad-checkpoint-preview`, brownfield-проект и расследование. Source-specific names сохранены там, где они являются точными именами BMAD-артефактов или рабочих процессов.

## P22 — синхронизация источников после structure / entry-sequence pass

P22 не добавлял источники. Inline-placeholder для официальной Workflow Map переписан как публичная подпись, а не как executor note. Нижний раздел возвращён к явному workflow label «Внешние изображения для asset-pass», потому что это служебная секция будущего asset-pass, а не обычный объяснительный раздел статьи.

## P23 — companion source sync

P23 сверил source usage с текущей статьёй. Публичный текст после P22 не добавил источников: изменения касались порядка разделов, заголовков, публичной подписи Workflow Map и companion-формулировок. Строка Workflow Map обновлена: это текущий inline external image candidate и элемент очереди, а не P12-only note. Generic `C5/A10 sync pending` отсутствует; C5/A10 остаются read-only context.

## P24 — style-only source sync

P24 не добавлял и не удалял источники. Все правки были языковыми: убраны псевдотермины и тяжёлые обороты вроде «первичность артефактов» в пользу более прямого «артефакты имеют приоритет», а также смягчены метафоры про роли и устаревший контекст.

Источникная карта остаётся прежней. Изменена только ссылка на переименованный раздел ролей: теперь это «Роли как распределение суждения, а не каталог персон».

## P25 — selective rewrite source sync

P25 не добавлял и не удалял источники. Правки убрали оставшиеся кальки и тяжёлые фразы: `working source of truth` заменён на русскую формулу «артефакт задаёт рамку работы», heading установки стал «Установка: где в репозитории живёт BMAD», а таблица восстановления теперь говорит «Файл или место», а не «Поверхность».

Источникная логика прежняя: Workflow Map поддерживает смену ведущего артефакта между фазами, Getting Started / Install BMad поддерживают файловую рамку, а skill-файлы поддерживают story/status/review/repair mechanics.

## P26 — guarded style source sync

P26 не менял набор источников и не добавлял фактических утверждений. Правки затронули только человеческую техническую фразу: «слеш-команды», «основной носитель контекста», «функция восстановления», более прямое описание TEA/Enterprise и theory-раздела.

Источникные привязки и version-sensitive долги остаются прежними.
