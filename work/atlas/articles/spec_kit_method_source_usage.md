# Source usage — Spec Kit article

Статус: P26 guarded final style. Файл фиксирует источники, которые фактически поддерживают текущую статью `spec_kit_method.md`, и только оставшиеся конкретные долги.

## Использованные первичные источники

| Источник | Где использован | Что поддерживает | Текущий статус / долг |
| --- | --- | --- | --- |
| https://github.github.com/spec-kit/ | Вводная рамка, базовая цепочка `Spec -> Plan -> Tasks -> Implement`, внешний image candidate `fig-spec-kit-home-positioning`. | Самоописание Spec Kit как SDD-инструментария и последовательности фаз. | Использовано в статье; image localization remains in image plan. |
| https://github.github.com/spec-kit/quickstart.html | Разделы о quickstart, constitution, clarify/checklist/analyze/implement. | Рекомендуемые цепочки команд и контрольные точки для неоднозначных фич. | Использовано в статье; no open article blocker. |
| https://github.github.com/spec-kit/installation.html | Раздел об инициализации и установке. | Предупреждение о неофициальных PyPI-пакетах, prerequisites, default integration в non-interactive init. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://github.github.com/spec-kit/reference/core.html | Раздел об инициализации, check/version, CLI-флагах. | `--script`, `--no-git`, `--branch-numbering`, `--preset`, `specify check`, `version --features --json`. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://github.github.com/spec-kit/reference/integrations.html | Разделы об интеграциях, манифестах, совместной установке и agent surfaces. | Разные форматы команд, skills/recipes/wrappers/generic, `integration list/use/switch/upgrade`, multi-install caveats. | Использовано в статье; integration drift remains a bounded risk, not a source blocker. |
| https://github.github.com/spec-kit/reference/workflows.html | Раздел о workflows и внешние image candidates `fig-full-sdd-cycle`, `fig-workflow-json-status`. | `Full SDD Cycle`, human checkpoints, `.specify/workflows/runs/<run_id>/`, `--json`, workflow catalog order. | Visual disposition checked; asset-pass download/rights/quality remains. |
| https://github.github.com/spec-kit/reference/extensions.html | Раздел о расширениях и hooks. | `.specify/extensions.yml`, hooks, extension catalog, lifecycle. | Использовано в статье; no open article blocker. |
| https://github.github.com/spec-kit/reference/presets.html | Раздел о presets. | Preset stack, `preset resolve`, overrides and priority. | Использовано в статье; no open article blocker. |
| https://github.github.com/spec-kit/upgrade.html | Разделы о lifecycle, upgrades and force. | Разделение CLI upgrade и project files, риск `.specify/memory/constitution.md`, safe zone `specs/`. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://github.com/github/spec-kit | Quickstart/README-related facts, `.specify/memory/constitution.md`, `taskstoissues`, install examples. | Репозиторий и README как primary source. | Использовано в статье; no open article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md | Problem statement, SDD relation, `spec.md`/`plan.md`/supporting artifacts. | Спецификация как управляющий артефакт; `WHAT/WHY` vs `HOW`; example artifacts. | Использовано в статье; no open article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md | Раздел constitution. | Semver, Sync Impact Report, template sync. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/specify.md | Раздел specify. | `before_specify`, feature directory, `.specify/feature.json`, requirements checklist, clarification caps. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/clarify.md | Раздел clarify. | Question taxonomy, one question at a time, `## Clarifications`, checklist recalculation. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/checklist.md | Раздел checklist. | Checklists as requirements-writing tests, `CHK###`, traceability markers. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md | Разделы plan/hooks. | Plan phase and extension hook handling. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/tasks.md | Раздел tasks. | Task format, `[P]`, `[US1]`, dependency graph, MVP-first. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md | Раздел analyze. | No-write audit, conflict severity, cap of 50 findings, separate permission for fixes. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/implement.md | Раздел implement. | Checklist gate, context files, ignore files, phased tasks, `[X]`. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/taskstoissues.md | Упоминание хвоста GitHub issues в досье; пока слабо в основном тексте. | GitHub remote verification before issue creation. | Deferred out of current article; possible source note, not blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/scripts/bash/common.sh | Раздел active feature resolution. | Root detection by `.specify`, `SPECIFY_FEATURE_DIRECTORY`, `.specify/feature.json`, branch prefix fallback. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/scripts/bash/create-new-feature.sh | Использовано через досье для context; пока не раскрыто подробно. | `--json`, `--dry-run`, branch/catalog/spec creation. | Deferred to source note/handbook; not article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/scripts/bash/setup-plan.sh | Использовано через досье для context; пока не раскрыто подробно. | Feature path setup for plan. | Использовано only as context; no open article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/scripts/bash/setup-tasks.sh | Использовано через досье для context; пока не раскрыто подробно. | Required files and tasks template resolution. | Использовано only as context; no open article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/scripts/powershell/common.ps1 | Упоминание Windows surface. | Case-insensitive comparisons, invoke separator, template resolution caveats. | Deferred to diagnostics/source note; not article blocker. |
| https://raw.githubusercontent.com/github/spec-kit/main/src/specify_cli/integrations/manifest.py | Раздел манифестов. | SHA-256 manifest and integration file provenance. | Использовано в статье; no open article blocker unless final freshness check is requested. |
| https://raw.githubusercontent.com/github/spec-kit/main/src/specify_cli/shared_infra.py | Риск upgrade/managed files использован через досье; пока не раскрыт сильно. | Refresh/force behavior, symlink protection. | Added lifecycle material; remaining operational detail deferred to source note. |
| https://raw.githubusercontent.com/github/spec-kit/main/AGENTS.md | Agent-context and integration architecture used through dossier. | Integration registry, managed agent context, `agent-context`. | Использовано в статье; no open article blocker. |
| https://arxiv.org/abs/2604.05278 | Раздел о context blindness and Spec Kit Agents. | Research caveat: context-grounded hooks and multi-agent SDD. | P12 verified figure/license context; bounded as research caveat. |
| https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | Раздел risks and boundaries. | SDD categories and warning about verification burden / semantic breadth. | Inserted as bounded SDD context; no open article blocker. |
| https://github.com/github/spec-kit/issues/1063 | Риск drift after implementation. | User-reported gap about post-implementation reconciliation. | Keep as issue-level evidence, not official roadmap. |

## Внутренние входы, использованные как рабочие источники, но не как публичные citation targets

- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` — primary quarry for source facts, commands, risks, images and open questions.
- `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` — article model and controlled repetition boundary.
- `work/theory-writing/fragments/C5_concept_atlas_article_map.md` — Spec Kit article tier, reader question, theory backlinks and dangerous pairs.
- `work/theory-writing/fragments/A10_mode_selection_map.md` — mode-selection framing: choose the lightest external structure that covers risk.
- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` — output roles, visual layer, pass queue, no internal length cap.

## P01 source status

- Статья уже содержит public-facing markdown links to primary sources where source-supported facts appear.
- P04–P08 должны открыть и проверить наиболее critical sources directly, because Spec Kit is version-sensitive.
- Никакие утверждения из внутреннего досье не используются как публичные ссылки.

## P02 boundary inputs

P02 read adjacent dossiers as internal boundary context, not public citation targets:

- `SPDD_METHOD_DOSSIER.md` — boundary: prompt/REASONS Canvas as maintained intention artifact; not repo workflow.
- `KIRO_SPECS_DOSSIER.md` — boundary: productized IDE/Web/CLI specification surface; not portable Spec Kit CLI discipline.
- `CONSTITUTIONAL_SDD_DOSSIER.md` — boundary: security/policy/governance as top-layer specification; Spec Kit constitution is only one workflow artifact.
- `TDAD_COMPARATIVE_DOSSIER.md` — boundary: tests as control loop for agent definition or code change; Spec Kit checklists/analyze are artifact-quality gates.
- `ADR_METHOD_DOSSIER.md` — boundary: architecture decision memory with status/consequences; `plan.md` does not replace ADR.
- `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` — boundary: durable work graph with owners/dependencies/gates/prime/recovery; Spec Kit artifact chain is lighter.

No new public source was added in P02.

## P03 inventory update

No new public citation target was added in P03. Inventory confirms that the article already transfers the dossier's article-critical backbone and that remaining material requires source-depth verification before any main-text strengthening.

P03 source-opening priorities:

1. Official docs and raw command templates for phase mechanics.
2. Raw scripts for active-feature and setup mechanics.
3. Integrations/manifest source files for portability and managed-file claims.
4. Workflows documentation for formal human checkpoint and machine-state claims.
5. Spec Kit Agents and Fowler/Thoughtworks only as caveated external context.
6. Visual sources for asset-pass, not prose substitution.

## P04 source-depth update

No new public source target was introduced in P04. The main article now uses already registered primary sources more explicitly to explain why Spec Kit needs multiple artifacts rather than one `spec.md`:

- `spec-driven.md`, `specify.md`, `clarify.md` and `checklist.md` now support the strengthened explanation of the first gate: `WHAT/WHY`, `[NEEDS CLARIFICATION]`, writeback to `spec.md` and checklist issues.
- `plan.md` now supports the strengthened explanation that Phase 0 unknowns should become decisions/research/alternatives before tasks.
- `tasks.md` now supports the strengthened explanation that executable tasks require story/file/dependency traceability before implementation.
- `analyze.md` and `implement.md` now support the strengthened pre-code stops: no-write consistency audit and incomplete-checklist confirmation.

P04 did not open new external sources and did not add internal dossier citations to the public text.

## P05 source-depth update

P05 added a command-as-state-transition table and strengthened the `plan`/`tasks` sections. No new public source target was introduced; all cited targets were already registered.

Additional usage now visible in the main article:

- `constitution.md` — transition from project principles to `.specify/memory/constitution.md`, semver and `Sync Impact Report`.
- `specify.md` + `common.sh` — transition from feature intention to active `FEATURE_DIR`, `spec.md`, `checklists/requirements.md` and `.specify/feature.json`.
- `clarify.md` + `checklist.md` — transitions that write uncertainty and quality checks back into repo files.
- `plan.md` + `setup-plan.sh` — transition from clear spec to technical plan and supporting artifacts.
- `tasks.md` + `setup-tasks.sh` — transition from plan to executable task backlog with stricter required inputs.
- `analyze.md` + `implement.md` — transitions from consistency diagnosis to confirmed implementation.

## P06 source-depth update

P06 added no new public source targets. It changed the role of already cited constitution/checklist sources in the article:

- `constitution.md` is now used to distinguish a real governance constraint from a formal constitution file: semver, Sync Impact Report and dependent template/command sync must affect later workflow.
- `plan.md`, `analyze.md` and `implement.md` now support the claim that constitution matters only when it changes planning, consistency review or implementation context.
- `checklist.md` and `implement.md` now support the claim that checklists matter only when they route gaps/ambiguities/conflicts back to artifacts or force an explicit pre-implementation decision.

## P07 source-depth update

P07 added no new public source target outside the already registered source map, but made the AGENTS/context and integration-manifest sources visible in the main article:

- `AGENTS.md` is now cited for `agent-context`, `context_file` and managed marker sections such as `SPECKIT START` / `SPECKIT END`.
- `manifest.py` and `shared_infra.py` are now used to frame integration manifests and shared infrastructure manifests as provenance for files the next agent reads.
- Integrations, Presets, Extensions, `common.sh`, `setup-plan.sh` and `setup-tasks.sh` now support the concept of an agent-readable repository surface, not only command execution.

## P08 source-depth update

P08 added issue/PR evidence boundaries from the dossier's public source map:

| Source | Where added | What it supports | Boundary |
| --- | --- | --- | --- |
| https://github.com/github/spec-kit/issues/975 | Section 5 active-feature caveat. | Historical PowerShell numbering/active-feature risk: old behavior could repeat `001-*` when only current-branch `specs/` were considered. | Issue-level historical evidence; not current baseline without direct recheck. |
| https://github.com/github/spec-kit/pull/986 | Section 5 active-feature caveat. | Fix context for issue #975: counting branches/remote refs in PowerShell path. | PR-level historical evidence; not a claim of present behavior beyond the cited fix context. |
| https://github.com/github/spec-kit/issues/1926 | Section 12 integration caveat. | Kiro CLI dynamic-argument/fallback-instruction caveat as one integration-specific limitation. | Issue-level evidence; not general behavior of all integrations. |

P08 also added a source-boundary paragraph in risks: public docs/raw templates describe baseline Spec Kit, but concrete projects must be audited through local `.specify/`, manifests and agent context.

## P09 free expansion update

Editorial underfill chosen for P09: lifecycle of Spec Kit project infrastructure. No new public source target was introduced; the article now uses already registered sources more strongly:

- Upgrade Guide now supports the two-layer update distinction: CLI capabilities vs project `.specify/` files, with `specs/` and source code outside template packages.
- Upgrade Guide now supports the risk that `.specify/memory/constitution.md`, `.specify/scripts/` and `.specify/templates/` can be overwritten during project-file refresh.
- `shared_infra.py` and `manifest.py` now support the mechanism for managed-file preservation/skipping and `speckit.manifest.json` as shared infrastructure state.
- Integrations Reference now supports the separate integration lifecycle and the `uvx` temporary-copy caveat.

## P10 free expansion update

P10 added no new public source targets. It added a reader-path subsection that reuses already registered sources to show how to review one concrete Spec Kit feature directory:

- `specify.md` and `common.sh` — active feature resolution before reading artifacts.
- `specify.md`, `clarify.md`, `checklist.md` — `spec.md`, Clarifications and requirements checklist as first review layer.
- `plan.md` — technical decision and supporting artifacts as second review layer.
- `tasks.md` — story/task/dependency review as third review layer.
- `analyze.md`, `implement.md`, Workflows and Integrations docs — execution surface before code and handoff.

## P11/P12 visual source update

| Source | Visual/source action | Boundary |
| --- | --- | --- |
| https://github.github.com/spec-kit/ | P12 kept `fig-spec-kit-home-positioning` inline as an external-real candidate after checking that the docs home still contains the positioning blocks. | Screenshot/localization still requires asset-pass; do not treat docs marketing blocks as proof of method efficacy. |
| https://github.github.com/spec-kit/reference/workflows.html | P12 kept `fig-full-sdd-cycle` and `fig-workflow-json-status`; source contains the built-in Full SDD Cycle workflow, Mermaid flowchart source and JSON status example. | The flowchart may be localized as screenshot only after rights/quality check, or redrawn from source if that is safer. |
| https://arxiv.org/abs/2604.05278 and https://arxiv.org/pdf/2604.05278 | P12 inserted `fig-spec-kit-agents-context-hooks` as external-real candidate after inspecting Figure 1 in the PDF and noting the arXiv license link to CC BY 4.0. | Research caveat only; not official Spec Kit baseline. Any localized image must attribute authors and license. |
| https://creativecommons.org/licenses/by/4.0/ | Used only to record the license condition for the arXiv figure candidate. | License note, not a methodological source for the article. |
| https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html / `content/assets/theory-images/fowler-sdd-overview.png` | P11 inserted the existing local asset as `fig-fowler-sdd-overview-context`. | SDD-context only; does not replace Spec Kit-specific official/source visuals. |

No additional public methodological claim was added solely from visual inspection. Visual source notes are recorded to guide later asset localization and attribution.

## P13 source update

No new public source was added in P13. The pass reviewed synthetic figures against already used source bases: repository topology, command templates, workflow docs, scripts and companion visual rules.

## P14 standalone concept update

No new public source was added in P14. The new “minimal model” subsection is a concept-first synthesis from the article's existing source base and C5 article model: intent, artifact, transition, gate and agent surface are framing terms for the current Spec Kit material, not new claims requiring external citations.

## P15 mechanism/failure-mode source update

No new public source was added in P15. The pass reuses already registered primary sources and dossier material to tighten failure boundaries inside the concept explanation rather than creating a separate error catalog:

- `specify.md`, `clarify.md` and `checklist.md` support the boundary that a polished `spec.md` still fails if success criteria, scope, assumptions and open questions are not testable enough to feed planning.
- `plan.md` and constitution material support the boundary that `plan.md` must justify technical decisions from `spec.md` and project rules, not merely list stack/layers/tests.
- `tasks.md` and `analyze.md` support the boundary that tasks need traceable responsibility to requirements, files, dependencies and checks.
- `checklist.md`, `implement.md`, `Core Commands` and Integrations docs support the evidence-boundary paragraph: each check proves only its own narrow object.
- Fowler/Thoughtworks SDD context and the existing risks section support the lightweight-plan boundary: full Spec Kit is justified by ambiguity, risk and handoff need, not by document count.

## P16 theory-source update

No new public Spec Kit source was added in P16. The pass used only the allowed theory fragments (`00_spine_map`, A3, A5, A7, A9, C5 and A10) plus the current article to add semantic back-links. These fragments are not new external factual sources for Spec Kit; they define the atlas/theory questions that the article should answer without rewriting the theory.

## P17 language update

No new source was added in P17. The pass normalized Russian-language prose in the main article while preserving source labels, command names, file names, paths, exact fields and figure/source titles. Source meaning and citations were not changed.

## P18 language update

No source changed in P18. The pass improved headings, captions, table wording and the bottom asset-preparation section. Exact source titles, URLs, command names, file paths and asset-status labels were preserved.

## P19 editorial source update

No new source was added in P19. The pass assessed the article as a standalone concept-first text and made only editorial/source-boundary preserving changes:

- normalized `/speckit.analyze` references so the audit gate is named consistently as a command rather than as a loose noun;
- corrected prose around constitution conflicts, handoff grammar, lifecycle wording and post-implementation repair traces;
- contained the bottom image material as non-methodological metadata; P22 restored the required `Внешние изображения для asset-pass` heading and public inline captions.

Source claims, URLs, image statuses and boundaries remain unchanged.

## P20 editorial source update

No new source was added in P20. The pass made presentation-only changes that preserve the registered source base:

- split the dense neighboring-method boundary paragraph for readability without changing the SPDD/Kiro/Constitutional SDD/TDAD/ADR/PWG distinctions;
- corrected the scope-review wording before planning;
- expanded shorthand evidence checks into exact command surfaces: `/speckit.checklist`, `/speckit.analyze`, `specify check`, `specify version --features --json` and `specify integration list`.

The edits strengthen source traceability by making the cited command surface explicit.

## P21 editorial source update

No new source was added in P21. The pass localized ordinary explanatory terms around integration surfaces while preserving exact source labels and command/path names:

- `skills`, `recipes` and `wrappers` are now introduced with Russian glosses where they function as ordinary explanatory terms;
- exact integration terms and paths such as `.agents/skills`, `$speckit-<command>`, `generic`, `Hermes`, `RovoDev`, `Goose`, `Pi` and MCP remain unchanged;
- ordinary `prompt` wording outside fixed method labels was localized as `промпт`.

The change is terminological, not factual.

## P22 structure/source update

No new source was added in P22. The pass changed public article structure and visual framing only:

- moved the article contract and atlas-boundary material after the problem section, so the entry sequence remains problem-first;
- kept the first external visual candidate after the reader question, now with a public caption rather than asset-preparation wording;
- changed inline external-candidate captions to describe the source image's argumentative role instead of saying “service asset-preparation wording”.

Source URLs, claims and evidence boundaries remain unchanged.

## P23 companion sync update

P23 removed stale pass-specific source debts from the current source table and converted them into concrete current statuses. Remaining source follow-ups are now limited to:

- final freshness pass only if the article is published with a current-date claim;
- asset-pass localization/rights/quality checks for external visual sources;
- issue/PR examples staying bounded as issue-level evidence.

No public source was added or removed.

## P24 style-defect audit sync

P24 did not add or remove factual sources. The article now states several already-supported points in plainer Russian: initialization is described as installation into the repository rather than “technical landing”; manifest evidence is described as provenance of files read by the agent; task quality is described through links to stories/files/checks rather than pseudo-terms. Source coverage and remaining freshness/asset blockers are unchanged.

## P25 selective natural rewrite sync

P25 again changed only wording. The title, reader question, opening image caption, Workflows wording, issue phrasing and theory bridge were made more natural, but the same sources support the same claims. No source was added, removed or promoted; existing freshness and asset-pass notes remain unchanged.

## P26 guarded final style sync

P26 changed tone and transitions only. It removed remaining abstractions such as “единица управления”, clarified the opening path from chat to repository files, and made the theory bridge less list-like. Source set, citations, command facts, numbers and remaining freshness/asset blockers are unchanged.
