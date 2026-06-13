# Source transfer ledger — Spec Kit article

Статус: P26 guarded final style. Ledger keeps factual transfer decisions; current blockers live in open_questions/image_plan, not in pass-coverage debt.

## Что перенесено в основной текст

| Материал | Перенос | Источниковая опора | Решение |
| --- | --- | --- | --- |
| Spec Kit как `Spec -> Plan -> Tasks -> Implement` | Ввод и разделы 1/18. | Documentation, Quick Start, `spec-driven.md`. | Использовано как центральная ось статьи. |
| Неофициальные PyPI-пакеты | Раздел 3. | Installation Guide. | Перенесено, потому что это практический failure mode установки. |
| Non-interactive default integration | Раздел 3. | Installation Guide. | Перенесено как важный automation caveat. |
| `specify init` flags | Раздел 3. | Core Commands. | Перенесено, но требует P05 freshness check. |
| `.specify/memory/constitution.md` and Sync Impact Report | Раздел 4. | README, Quick Start, constitution template. | Перенесено как human governance gate. |
| `SPECIFY_FEATURE_DIRECTORY`, `.specify/feature.json`, branch fallback | Раздел 5 и synthetic figure. | `specify.md`, `common.sh`. | Перенесено как ключевой repo-transition mechanism. |
| `/speckit.clarify` one-question loop and writeback | Раздел 6. | `clarify.md`. | Перенесено как пример переноса из чата в файл. |
| `/speckit.checklist` as requirements-writing test | Раздел 6/15. | `checklist.md`, `spec-driven.md`. | Перенесено с осторожной формулировкой. |
| `/speckit.plan` supporting docs | Раздел 7. | `spec-driven.md`. | Перенесено как technical-decision layer. |
| `/speckit.tasks` task format and story grouping | Раздел 8. | `tasks.md`. | Перенесено как executable decomposition. |
| `/speckit.analyze` no-write audit | Раздел 9/14/15. | `analyze.md`. | Перенесено как clear human gate. |
| `/speckit.implement` checklist stop and task execution | Раздел 10/14. | `implement.md`. | Перенесено как most explicit agent stop point. |
| Workflows Full SDD Cycle and run state | Раздел 11 and image candidates. | Workflows Reference. | Перенесено как orchestration layer. |
| Agent integration heterogeneity | Раздел 12. | Integrations Reference and source-code links from dossier. | Перенесено as boundary of portability. |
| Integration manifest and upgrade behavior | Раздел 12 and 14. | Integrations Reference, manifest.py. | Перенесено as lifecycle/managed-file gate. |
| Presets/extensions/overrides | Раздел 13. | Extensions Reference, Presets Reference, command templates. | Перенесено as audit boundary. |
| Risks: documentation theater, context blindness, drift, overkill, hidden local state | Раздел 16. | Quick Start, Spec Kit Agents, issue #1063, Fowler/Thoughtworks, Core/Extensions/Presets/Integrations. | Перенесено as caveats. |
| Boundary with SPDD/Kiro/CSDD | Раздел 17. | C5 article map + dossier. | Перенесено as atlas boundary. |
| Theory links to A3/A5/A9/A10 | Раздел 18 and companion theory_links. | C5 and A10. | Перенесено as controlled backlink, not full theory recap. |

## Что сознательно отложено

| Материал | Почему отложено | Будущий проход |
| --- | --- | --- |
| Подробный разбор `create-new-feature.sh`, `setup-plan.sh`, `setup-tasks.sh` and PowerShell variants | P01 already explains active feature mechanism; detailed diagnostics risk turning article into handbook. | P05/P09 decide if diagnostic subsection is needed. |
| Full integration registry table | Too detailed for P01 and version-sensitive. | P05/P09 source-depth; maybe companion table or concise article table. |
| Community workflows/extensions/presets warnings in full detail | P01 mentions risk; full caution may overload article. | P06 limitations pass. |
| `taskstoissues` detailed remote verification | Mentioned only lightly; could support lifecycle tail. | P09 or P10. |
| Upgrade source-code details: symlink protection, `refresh_managed`, `force` modes | Useful but maybe too implementation-heavy for article. | P09/P10 if lifecycle section remains thin. |
| Spec Kit Agents full paper mechanics | P01 uses it only as research caveat. | P06 and possibly P10; avoid overclaiming as official behavior. |
| Fowler/Thoughtworks SDD typology figure | Candidate for image and boundary discussion; not inserted in main article. | P11/P12. |

## Source gaps / checks

- Current Spec Kit CLI and docs may have changed; P04–P08 must verify official docs/source files directly.
- Need confirm exact current names and availability of all supported integrations.
- Need confirm current behavior of Git extension default in `v0.10.0` note before placing it in main article; P01 does not use this detail.
- Need decide whether issue #1063 and issues #975/#987/#1926 belong in main article or remain companion evidence.
- Need visual rights/pass for official docs screenshots, Workflows diagram, arXiv figure and local Fowler image.

## P02 transfer decisions

| Boundary / contract item | Article change | Companion impact |
| --- | --- | --- |
| Reader question made explicit as repo-workflow contract | Added `## Контракт статьи` near top of article. | Theory links and audit updated. |
| Spec Kit vs SPDD/OpenSPDD | Strengthened top contract and section 17. | Boundary now explicit in theory links/audit. |
| Spec Kit vs Kiro | Strengthened top contract and section 17. | Boundary now explicit in theory links/audit. |
| Spec Kit vs Constitutional SDD | Strengthened top contract and section 17. | Boundary now explicit in theory links/audit. |
| Spec Kit vs TDAD | Added to top contract and section 17. | Added to theory_links dangerous routes. |
| Spec Kit vs ADR | Added to top contract and section 17. | Added to theory_links dangerous routes. |
| Spec Kit vs PWG | Strengthened section 17 and contract. | Generic C5/A10 sync debt is closed; only concrete article blockers remain in open_questions. |
| Negative boundary against CLI reference / overview / theory duplicate | Added direct test: each section must explain how next artifact constrains agent action. | Readiness status updated to P02. |

## P03 dossier inventory

Inventory scope: `SPEC_KIT_METHOD_DOSSIER.md`, current article and current ledger/image plan. This is not a total coverage matrix; it records article-critical transfer state and future source-opening needs.

### Already transferred into the article

| Dossier area | Article location | Transfer status | Notes |
| --- | --- | --- | --- |
| Spec Kit as `specify → plan → tasks → implement` chain | Introduction, sections 1, 18 | `transferred` | Central article axis; public links already attached. |
| Problem of intention/document/code drift | Sections 1, 16 | `transferred` | Dossier's problem framing is present without turning article into general SDD overview. |
| Installation and initialization caveats | Section 3 | `transferred` | Official repo/PyPI warning, default integration, init flags included. |
| Agent integration heterogeneity | Sections 2, 12 | `transferred` | Slash commands vs skills/recipes/wrappers/global/generic surfaces included. |
| `.specify/` layers and feature artifacts | Sections 2, 5 | `transferred` | `specs/[feature]`, `.specify/memory`, templates, scripts, integration files included. |
| Constitution and `Sync Impact Report` | Section 4 and 14 | `transferred` | Treated as governance gate, not full CSDD article. |
| `/speckit.specify` mechanics | Section 5 | `transferred` | Branch/catalog/feature.json and requirements checklist included. |
| `/speckit.clarify` and `/speckit.checklist` | Section 6 and 15 | `transferred` | Answers written back to spec; checklists as requirements-quality tests. |
| `/speckit.plan` supporting outputs | Section 7 | `transferred` | Plan, research, data model, contracts, quickstart. |
| `/speckit.tasks` mechanics | Section 8 | `transferred` | User stories, task format, dependencies/MVP/parallelism. |
| `/speckit.analyze` no-write audit | Sections 9, 14, 15 | `transferred` | Important human gate. |
| `/speckit.implement` checklist stop | Sections 10, 14 | `transferred` | Most explicit stop before code. |
| Workflows and formal review checkpoints | Section 11 and image queue | `transferred` | `Full SDD Cycle`, run state, `--json`, catalog order. |
| Presets/extensions/overrides | Section 13 | `transferred` | Included as audit boundary; not expanded into reference. |
| Checks/version/integration list | Section 15 | `transferred` | Environment checks included. |
| Risks: documentation theater, context blindness, drift, overkill, local installation drift | Section 16 | `transferred` | Uses issue/research/Thoughtworks as caveated evidence. |
| Boundaries with SPDD/Kiro/CSDD/TDAD/ADR/PWG | Contract section and section 17 | `transferred after P02` | Boundary material strengthened. |
| Dossier image candidates | Article placeholders + image plan | `partly transferred` | Most important candidates inserted or deferred. |

### Partly transferred or intentionally deferred

| Dossier material | Current disposition | Why not fully transferred now | Future action |
| --- | --- | --- | --- |
| `create-new-feature.sh`, `setup-plan.sh`, `setup-tasks.sh` command options and JSON outputs | `partly_transferred` | Active feature mechanism is in article; full diagnostics would become handbook. | P05/P09 decide whether a compact diagnostic paragraph is needed. |
| PowerShell-specific behavior | `partly_transferred` in source_usage/ledger, not main article except high-level boundary | Too detailed for concept article unless Windows behavior explains mechanism. | P05/P09 evaluate if cross-platform detail is necessary. |
| Git extension default changing around `v0.10.0` | `deferred_source_check` | Version-sensitive and not central to reader question. | P04/P05 verify before adding, likely keep in source note. |
| `taskstoissues` remote/GitHub MCP safeguards | `deferred_or_light_tail` | Relevant lifecycle tail, but not central to feature-artifact transition. | P09 decide if lifecycle section needs one paragraph. |
| Integration source-code registry details (`IntegrationBase`, specific class metadata) | `partly_transferred` | Article needs typology, not exhaustive registry. | P05/P09 may add compact table if source-depth finds it article-critical. |
| Manifest internals and shared infra force/refresh/symlink behavior | `partly_transferred` | Useful for upgrade safety; too detailed for P01/P02 main text. | P09/P10 maybe add to lifecycle if article underexplains managed files. |
| Community extensions/presets/workflows warnings | `partly_transferred` | Article mentions risk but not full supply-chain warning. | P06 caveats pass. |
| Historical issues #975/#987/#1926 | `deferred` | Useful as weak evidence/case notes, but may clutter article. | P06 decide whether any issue belongs in main text. |
| Spec Kit Agents detailed PM/developer/state-machine model | `deferred` | Research caveat already used; full paper belongs in source note or context-grounding comparison. | P06/P10 only add if needed to explain context blindness. |
| Search formulations and open source-hunting notes | `not_transferred` | Operational notes, not article content. | Keep out of article. |
| Handbook/Fieldbook recipes | `not_transferred` | Article is concept-first, not manual. | Future Handbook/Fieldbook. |

### Material that requires opening primary sources before strengthening article

- Official docs: documentation landing, Quick Start, Installation, Core Commands, Integrations, Workflows, Extensions, Presets, Upgrade.
- Raw command templates: `constitution.md`, `specify.md`, `clarify.md`, `checklist.md`, `plan.md`, `tasks.md`, `analyze.md`, `implement.md`, `taskstoissues.md`.
- Raw scripts: `common.sh`, `create-new-feature.sh`, `setup-plan.sh`, `setup-tasks.sh`, PowerShell counterparts if article keeps cross-platform detail.
- Source-code integration files: registry/base/manifest/shared infra and selected integrations if article keeps typology.
- Spec Kit Agents paper: only for context-grounding caveat, not as official Spec Kit behavior.
- Fowler/Thoughtworks SDD article: only for boundary/overkill caveat.
- GitHub issues/PRs: weak evidence only; do not promote to product facts.
- Visual sources: official docs landing/workflows, arXiv figure, local Fowler asset.

### Potential weak spots in article technical supports

1. Plan section may be too short compared with specify/tasks/analyze. P04/P05 should check whether `setup-plan.sh`, plan template or plan command gives article-critical mechanics beyond `plan.md`/supporting files.
2. Lifecycle section may underuse `taskstoissues` and upgrade/project-file distinction; P09/P10 should decide whether to add a compact tail.
3. Integration section explains heterogeneity but not the exact relation between installed integration, default integration and shared templates as clearly as dossier does. P05 may strengthen if source confirms.
4. `agent-context` is mentioned indirectly; if later passes find it central to “what transfers from conversation to files,” add a focused paragraph.
5. Article currently avoids detailed issue history. Keep it that way unless an issue captures a still-current caveat better than official docs.

### P03 decision on main article

No P03 main-text edit was required. Current missing material is either future source-depth work, handbook material, or version-sensitive detail that must be verified before inclusion.

## P04 source-depth transfer — why one `spec.md` is insufficient

| Material | Main-text action | Source basis | Status |
| --- | --- | --- | --- |
| Multi-artifact handoff rather than a single specification document | Added a subsection `Почему одного spec.md недостаточно` under the problem section. | `spec-driven.md`, Quick Start chain already in article, command templates. | `transferred_P04` |
| First stop: unresolved behavior/constraint must be clarified or surfaced in checklist | Strengthened explanation of `[NEEDS CLARIFICATION]`, `/speckit.clarify` and requirements checklists as a gate before planning. | `specify.md`, `clarify.md`, `checklist.md`. | `transferred_P04` |
| Second stop: planning unknowns become research/decision/alternatives before tasks | Added a stronger paragraph in `/speckit.plan` section about Phase 0 and unfinished technical decisions. | `plan.md`. | `transferred_P04` |
| Third stop: tasks must be traceable to stories/files/dependencies before implementation | Added a stronger paragraph in `/speckit.tasks` section. | `tasks.md`. | `transferred_P04` |
| Pre-code stops | Reframed `/speckit.analyze` and `/speckit.implement` as separate diagnostic and checklist-confirmation gates in the new subsection. | `analyze.md`, `implement.md`. | `transferred_P04` |

No material was rejected in P04. No image candidate was added. The main debt remaining is direct freshness verification of the linked primary sources in later source-depth passes.

## P05 transfer — commands as repo workflow state transitions

| Transition | Transferred detail | Main-text location | Status |
| --- | --- | --- | --- |
| `/speckit.constitution` | Constitution versioning, dates, Sync Impact Report and dependent template statuses are a project-state transition. | New table under section 2. | `transferred_P05` |
| `/speckit.specify` | Feature intention becomes `FEATURE_DIR`, `spec.md`, `checklists/requirements.md`, `.specify/feature.json`; active feature is resolved by files/env/script logic. | New table and existing specify section. | `transferred_P05` |
| `/speckit.clarify` | Clarification answers are written to `## Clarifications`, integrated into `spec.md`, and checklist state is recalculated. | New table and clarify/checklist section. | `transferred_P05` |
| `/speckit.checklist` | `FEATURE_DIR/checklists/*.md`, `CHK###`, traceability and issue markers create a requirements-quality state. | New table and checklist section. | `transferred_P05` |
| `/speckit.plan` | `setup-plan` and command template create/prepare `plan.md`, Phase 0/1 outputs, Constitution Check and agent-context update. | New table plus plan section. | `transferred_P05` |
| `/speckit.tasks` | `setup-tasks` requires `spec.md` and `plan.md`, lists supporting docs, resolves `tasks-template` and yields `tasks.md`. | New table plus tasks section. | `transferred_P05` |
| `/speckit.analyze` | No-write consistency audit is a diagnostic state before edits. | New table and analyze section. | `transferred_P05` |
| `/speckit.implement` | Checklist scan, context read, ignore-file prep, phased task execution and `[X]` task updates are implementation-state transition. | New table and implement section. | `transferred_P05` |

Rejected/deferred in P05: PowerShell variants, `--json` diagnostics and `taskstoissues` stayed out of the main table to avoid turning the article into a command reference. They remain available for later diagnostic/source-note passes.

## P06 transfer — Constitution Check and checklist as working constraints

| Material | Main-text action | Source basis | Status |
| --- | --- | --- | --- |
| Constitution is not useful by mere existence | Added paragraphs in section 4: it must affect plan, templates, tasks, implementation or human review. | `constitution.md`, `plan.md`, `analyze.md`, `implement.md`. | `transferred_P06` |
| Sync Impact Report as anti-formality mechanism | Strengthened section 4: unresolved template/command sync means governance has not propagated. | `constitution.md`. | `transferred_P06` |
| Checklist is not useful by mere checkbox | Added paragraphs in section 6: checklist markers must route back to `spec.md`, `plan.md`, `tasks.md` or a human decision. | `checklist.md`, `implement.md`. | `transferred_P06` |
| Formality risk | Added risk paragraph: constitution/checklist can become decorative discipline if they do not change downstream action. | Command templates already in source usage. | `transferred_P06` |

No image candidate or new external source was added. No boundary comparison was changed.

## P07 transfer — agent-readable repository surface

| Material | Main-text action | Source basis | Status |
| --- | --- | --- | --- |
| Integrations as different readable surfaces | Strengthened section 12: agents read concrete command files, skills, recipes, wrappers and context files, not abstract Spec Kit. | Integrations reference. | `transferred_P07` |
| `AGENTS.md` / `agent-context` | Added section 12 paragraph about `context_file`, managed marker sections and stale/disabled context risk. | `AGENTS.md`. | `transferred_P07` |
| Integration manifests as provenance | Added section 12 paragraph about `.specify/integrations/<key>.manifest.json` and `speckit.manifest.json`. | `manifest.py`, `shared_infra.py`. | `transferred_P07` |
| Presets/extensions as process visible to the next agent | Strengthened section 13: presets and extensions can change templates, commands, hooks, workflows, constitution and context. | Presets/Extensions references, `AGENTS.md`. | `transferred_P07` |
| Scripts and repo conventions as lower surface | Added section 13 paragraph connecting `.specify/scripts/`, feature resolution and setup scripts to handoff correctness. | `common.sh`, `setup-plan.sh`, `setup-tasks.sh`. | `transferred_P07` |

Deferred in P07: detailed table of every integration key, PowerShell-specific context behavior, and source-code registry internals. These remain candidates for a source note or later visual/schematic pass.

## P08 transfer — failures, caveats and anti-summary

| Material | Main-text action | Source basis | Status |
| --- | --- | --- | --- |
| Active feature / numbering failure mode | Added section 5 caveat with issue #975 and PR #986 to show scripts determine real state. | Dossier issue/PR notes and public links. | `transferred_P08_with_evidence_boundary` |
| Kiro CLI integration caveat | Added section 12 paragraph with issue #1926 as integration-specific caveat. | Dossier issue note and public link. | `transferred_P08_with_evidence_boundary` |
| Public baseline vs local project files | Added risk paragraph: docs/templates are baseline, local `.specify/`, manifests, overrides and agent context determine actual behavior. | Integrations/Upgrade docs already in source usage. | `transferred_P08` |
| Anti-summary framing | The article now contains more places where “intent to implementation” is broken down into scripts, paths, manifests and local state. | P04–P08 accumulated source-depth. | `transferred_P08` |

Rejected/deferred in P08: deeper PowerShell diagnostics, broad issue history and integration-key registry details. They would shift the article toward a troubleshooting manual.

## P09 free expansion — lifecycle of process infrastructure

Chosen underfill: the article had strong artifact transitions, but still made Spec Kit look too static after installation. The dossier showed that lifecycle/upgrade behavior is central: CLI, project files, integrations, manifests and local customizations can drift independently.

| Added material | Main-text location | Source basis | Remaining debt |
| --- | --- | --- | --- |
| Two-layer upgrade: CLI vs project `.specify/` files | Section 13 after repo-conventions paragraph. | Upgrade Guide. | Direct freshness check if later external source opening is allowed. |
| Safe zone vs risk zone: `specs/`/source code vs `.specify/memory/constitution.md`, `.specify/scripts/`, `.specify/templates/` | Section 13. | Upgrade Guide. | Later decide if this deserves a small diagram. |
| Managed-file mechanism: manifests, hashes, preserved/skipped files | Section 13. | `shared_infra.py`, `manifest.py`. | Keep details at concept level; source note can go deeper. |
| Integration lifecycle and `uvx` temporary-copy caveat | Section 13. | Integrations Reference. | Later verify exact wording/current behavior. |

Deferred: step-by-step upgrade recipe, `specify self upgrade --dry-run`, timeout env vars, duplicate IDE slash-command cleanup and symlink handling. These are better for a practical source note unless a later pass asks for operational details.

## P10 free expansion — reader path through one feature

Chosen underfill: after P04–P09 the article had strong technical density, but a reader path was still too implicit. P10 added a concrete review route through one feature directory so the concept is easier to follow without becoming a command tutorial.

| Added material | Main-text location | Source basis | Remaining debt |
| --- | --- | --- | --- |
| Active feature first | New subsection `Как читать одну фичу Spec Kit` under section 15. | `specify.md`, `common.sh`. | Later layout pass may turn route into a small callout. |
| Review sequence `spec.md` → `plan.md` → `tasks.md` → execution surface | Same subsection. | Command templates and existing docs. | Ensure it does not become a procedural checklist in final polish. |
| Conceptual closing sentence: Spec Kit lets humans verify transfer of meaning between files | Same subsection. | C5 article model + accumulated source-depth. | Keep as local concept statement, not full theory recap. |

Deferred: full walkthrough with sample feature contents. That would be useful for a handbook, but too large for this concept article.

## P11/P12 visual transfer

| Material | Main-text action | Source basis | Status |
| --- | --- | --- | --- |
| Fowler/Thoughtworks SDD overview local image | Inserted as `fig-fowler-sdd-overview-context` in risks section after the SDD-heaviness paragraph. | Existing local asset `content/assets/theory-images/fowler-sdd-overview.png` and Fowler/Thoughtworks SDD article already in source usage. | `transferred_P11_as_context_only` |
| Spec Kit docs home first screen | Existing placeholder caption was rewritten as a public external-real candidate with source URL and proposed local path. | P12 web check of docs home. | `queued_inline_P12` |
| Workflows Full SDD Cycle | Existing placeholder caption was rewritten as a public external-real candidate. | P12 web check of Workflows reference. | `queued_inline_P12` |
| Workflow JSON status example | Existing placeholder caption was rewritten as a public external-real candidate. | P12 web check of Workflows reference. | `queued_inline_P12` |
| Spec Kit Agents Figure 1 | Added inline external-real candidate after context-blindness caveat and mirrored in bottom asset-pass section. | arXiv abstract page, PDF page 1/Figure 1 screenshot inspection, CC BY 4.0 license link. | `queued_inline_P12_research_boundary` |

Deferred visual transfers remain deliberate: repository tree, integration lifecycle, upgrade lifecycle, presets stack and command-template contract are better handled as synthetic/source-note candidates unless a later visual pass asks for more inline images.

## P13 synthetic visual transfer

| Candidate | Decision | Transfer status |
| --- | --- | --- |
| `fig-spec-kit-repo-layers` | Kept as rare useful synthetic topology. | `kept_P13` |
| `fig-active-feature-resolution` | Kept as rare useful state-resolution schematic. | `kept_P13` |
| New command/constitution/integration/upgrade diagrams | Not added. | `deferred_P13` |

P13 deliberately did not add synthetic figures for visual variety. The article already has enough visual anchors, and the remaining candidates are better kept as deferred plan items unless a layout/final-polish pass proves a specific need.

## P14 transfer — standalone concept layer

| Added material | Main-text location | Source basis | Status |
| --- | --- | --- | --- |
| Minimal standalone model: intent, artifact, transition, gate, agent surface | New subsection under `Контракт статьи`. | C5 standalone-article model plus accumulated Spec Kit sources. | `transferred_P14` |
| Clarification that Spec Kit does not promise code from a good prompt, but makes work pass through visible states | Same subsection. | Existing article mechanism and C5 concept-first framing. | `transferred_P14` |

P14 did not add new command details or external facts. It strengthened the reader's entry point so the article can be read without assembling the whole theory first.

## P15 transfer — mechanism and failure boundaries

| Added material | Main-text location | Source basis | Status |
| --- | --- | --- | --- |
| Polished spec without executable path | Requirements/specification section after the checklist-return paragraph. | `specify.md`, `clarify.md`, `checklist.md`, dossier risk on document imitation. | `transferred_P15` |
| Decorative plan as false technical certainty | Planning section after `plan.md` bridge explanation. | `plan.md`, constitution checks, `spec-driven.md`. | `transferred_P15` |
| Mechanical tasks without responsibility | Tasks section after traceability explanation. | `tasks.md`, `analyze.md`, task dependency/order model. | `transferred_P15` |
| Evidence/checklist overclaim boundary | Verification section after the list of check types. | `checklist.md`, `implement.md`, Core Commands, Integrations docs. | `transferred_P15` |
| Lightweight-plan boundary for small reversible changes | Limits/positioning section after SDD-context image. | Fowler/Thoughtworks SDD context plus existing article risk framing. | `transferred_P15` |

P15 did not add a standalone failure catalog. The material was embedded where each mechanism is explained, so the reader sees the failure mode at the exact transition it can corrupt.

## P16 transfer — semantic theory back-links

| Added material | Main-text / companion location | Source basis | Status |
| --- | --- | --- | --- |
| Compact explanation of which theory questions Spec Kit clarifies | Section `Что Spec Kit помогает понять в общей теории`. | `00_spine_map`, A3, A5, A7, A9, C5, A10. | `transferred_P16_main_text` |
| Detailed semantic back-link table | `spec_kit_method_theory_links.md`. | Same allowed theory fragments. | `transferred_P16_companion` |

P16 intentionally did not add more command facts. The transfer is conceptual routing: each theory link now says what problem the Spec Kit article illuminates and what boundary it does not cross.

## P17 transfer — language normalization

| Changed surface | Action | Status |
| --- | --- | --- |
| English glue in main prose | Replaced with Russian equivalents where the words were ordinary explanation rather than exact names: workflow → рабочий процесс, checklist → чек-лист, implementation → реализация, evidence → свидетельство, governance/checklist ritual → ритуал управления и чек-листов. | `language_normalized_P17` |
| Exact technical names | Preserved commands, files, paths, source titles, fields, labels and stable integration terms such as `Full SDD Cycle`, `Sync Impact Report`, `Phase 0 research`, `skills`, `recipes`, `wrappers`, `MCP`. | `preserved_P17` |

P17 changed wording only; no factual transfer was added or removed.

## P18 transfer — second language pass

| Surface | P18 action | Status |
| --- | --- | --- |
| Opening and standalone model | Smoothed explanatory prose while preserving the article contract. | `language_smoothed_P18` |
| Captions and bottom asset section | Rephrased ordinary English/glue and fixed Russian grammar around asset preparation. | `captions_smoothed_P18` |
| Integration table/prose | Localized ordinary terms such as wrappers/agents/timestamp while preserving exact fields and names. | `terminology_smoothed_P18` |

P18 was a wording pass only. It did not add or remove factual material.

## P19 editorial transfer — problems and fixes

Problems identified before editing:

| Problem | Why it hurt standalone reading | Fix applied | Transfer status |
| --- | --- | --- | --- |
| Some command references had drifted into loose prose (`analyze` instead of `/speckit.analyze`). | The article's core contract is about state transitions, so a loose noun weakened the gate semantics. | Normalized key references to `/speckit.analyze` in the minimal model and theory-return section. | `fixed_P19_no_source_change` |
| A table sentence duplicated conflict wording around constitution. | It made the `/speckit.analyze` row look mechanically assembled instead of precise. | Rewrote it as conflicts plus constitution violations. | `fixed_P19_no_source_change` |
| A few Russian grammar issues interrupted the argument near integration handoff, boundary conclusion and human authority. | These were small but visible failures in a concept-first article. | Corrected agreement and case without changing source facts. | `fixed_P19_no_source_change` |
| The bottom visual-candidate block still read like production metadata inside the article body. | It could make the article feel like an asset worksheet rather than a standalone article. | Temporarily contained it as non-methodological metadata; P22 later restored the required `Внешние изображения для asset-pass` heading and public inline captions. | `contained_P19` |

No source fact was added, moved or rejected. The pass tightened how already transferred material is presented.

## P20 editorial transfer — problems and fixes

Problems identified before editing:

| Problem | Why it hurt standalone reading | Fix applied | Transfer status |
| --- | --- | --- | --- |
| Neighbor-method boundary was factually useful but too dense near the top. | A standalone reader could hit a taxonomy wall before the local Spec Kit model. | Split the paragraph into two bounded blocks while preserving all distinctions. | `readability_fixed_P20` |
| The pre-plan review sentence said “what the feature must not touch” awkwardly. | The scope-exclusion check is important and should not sound incomplete. | Rephrased as “чего фича не должна затрагивать”. | `precision_fixed_P20` |
| Evidence checks later used shorthand names (`checklist`, `analyze`, `check`). | Shorthand blurred the article's core distinction between requirement, consistency, CLI and integration evidence. | Replaced with explicit command surfaces in section 15 and section 18. | `command_surface_fixed_P20` |

No new material was transferred; P20 clarified already transferred claims.

## P21 editorial transfer — problems and fixes

Problems identified before editing:

| Problem | Why it hurt standalone reading | Fix applied | Transfer status |
| --- | --- | --- | --- |
| Integration-surface terms appeared as bare English (`skills`, `recipes`, `wrappers`) in explanatory prose. | The article is Russian and concept-first; bare terms made the integration layer feel like an unprocessed source dump. | Added Russian glosses while preserving exact English terms in code-style parentheses. | `terminology_fixed_P21` |
| The synthetic repo-layers figure still contained English-only surface labels. | A figure should support the argument without requiring the reader to translate source vocabulary mentally. | Localized the figure line to commands, навыки, рецепты and обёртки while preserving `/speckit.*`, `$speckit-*`, `skills`, `recipes`, `wrappers`. | `figure_label_fixed_P21` |
| Ordinary `prompt` wording remained outside fixed method labels. | It was not a source title and therefore did not need to remain English. | Localized to `промпт` / `промпт-артефакт` where appropriate. | `language_fixed_P21` |

No source fact was added, moved or rejected.

## P22 public-structure transfer — problems and fixes

Problems identified before editing:

| Problem | Why it hurt public/article structure | Fix applied | Transfer status |
| --- | --- | --- | --- |
| The entry sequence put contract/taxonomy material before the first problem section. | The first screen should start from the reader's problem and question, not atlas-boundary bookkeeping. | Moved `Контракт статьи` and the minimal model after section 1, before the technical layers. | `structure_fixed_P22` |
| Inline external-image captions contained service asset-preparation wording. | Public captions should explain the image's role, while asset status belongs in attributes/queue. | Rewrote inline captions as normal article captions; kept asset metadata in attributes and bottom section. | `caption_publicized_P22` |
| The bottom image note used a temporary P19 label rather than the required asset-pass section name. | The visual rules expect external-real candidates to be mirrored in `Внешние изображения для asset-pass`. | Restored the bottom heading and kept a short boundary sentence separating asset localization from the main argument. | `asset_pass_section_restored_P22` |

No factual source transfer changed; P22 rearranged and publicized existing material.

## P23 companion sync transfer

P23 did not transfer new facts into the main article. It synchronized companions with the current article state:

| Companion area | Cleanup | Current blocker kept |
| --- | --- | --- |
| Source usage | Removed stale P04–P13 “verify later” debt language from current source statuses. | Optional final freshness pass for version-sensitive Spec Kit sources. |
| Open questions | Rewrote the file to keep only actual blockers and package-time guardrails. | Asset-pass, final layout, source freshness if publishing with a date claim. |
| Image plan / external queue | Updated status wording to match P22 public captions and required asset-pass section. | Four external-real candidates still need localization/rights/quality work. |
| Theory links | Closed generic C5/A10 debt explicitly; kept concrete theory backlinks. | None beyond package-time guardrails. |

Ledger remains a transfer log, not a coverage checklist.

## P24 style-defect transfer

| Material | Transfer | Source support | Decision |
| --- | --- | --- | --- |
| Style cleanup without new facts | Rephrased existing article claims about initialization, command transitions, constitution gates, active-feature examples, tasks, manifests and the theory bridge. | Same sources already listed in source_usage; no new source introduced. | `style_only_no_new_factual_transfer` |
| Caption wording cleanup | Tightened the repository-layers caption and the `Full SDD Cycle` caption without changing image candidates. | Existing image/source entries. | `caption_style_sync_only` |

## P25 selective natural rewrite transfer

| Material | Transfer | Source support | Decision |
| --- | --- | --- | --- |
| Natural title and reader question | Rephrased “becomes transition” into “passes through repo artifacts” / “conducts intention through spec, plan, tasks, implementation, constitution and checklists”. | Existing central Spec Kit sources. | `style_only_core_thesis_preserved` |
| Plain Russian for remaining source phrases | Replaced ordinary “prompt” in non-source prose with “запрос” / “файлы инструкций для агента”; kept exact prompt/Canvas where it names SPDD/OpenSPDD boundary. | Existing article text; no new source. | `language_cleanup_no_fact_change` |

## P26 guarded final style transfer

| Material | Transfer | Source support | Decision |
| --- | --- | --- | --- |
| Final human-style opening and bridge | Rephrased existing central claims so they read as technical explanation rather than protocol wording. | Same central Spec Kit sources already cited in the article. | `style_only_no_source_change` |
| Content preservation check | Kept commands, paths, figures, issue/PR caveats, source boundaries and theory boundaries intact. | Current article and companion state. | `preserved` |
