# kiro_specs — image plan

Статус: `P26_guarded_final_style_current`. План отражает фактический визуальный слой текущей статьи `kiro_specs.md`: один локальный общий SDD-asset, три синтетические схемы и семь inline external-real candidates, зеркалированные в нижнем блоке `Внешние изображения для asset-pass`.

## Inline figures currently in article

| Figure id | Type / status | Source or basis | Purpose | Current disposition |
| --- | --- | --- | --- | --- |
| `fig-general-sdd-context` | `local_image_asset` | `content/assets/theory-images/fowler-sdd-overview.png`; source caption links Martin Fowler `Exploring Generative AI`. | Give broad SDD context: agent, memory bank, specs. | Inserted as general context only; not Kiro UI evidence. |
| `fig-kiro-productized-spec-environment` | `synthetic_figure` | Article synthesis from Kiro Specs docs + context/execution/governance sources. | Show spec at the center of files, context, execution, integrations and organization. | Retained; explanatory, not decorative. |
| `fig-kiro-feature-spec-lifecycle` | `synthetic_figure` | Feature Specs, Requirements-First/Design-First, task execution, Sync Files. | Show requirements/design/tasks approvals, execution and feedback/sync. | Retained; central lifecycle figure. |
| `fig-kiro-quick-plan-candidate` | `external-real-candidate` | Quick Plan docs and `Specs just got faster (and smarter)`. | Show compressed route from idea to tasks. | Inline placeholder; asset-pass required. |
| `fig-kiro-deep-spec-analysis-candidate` | `external-real-candidate` | `Deep Spec Analysis` blog. | Show requirement refinement/formal analysis/questions. | Inline placeholder; asset-pass required. |
| `fig-kiro-task-status-ui-candidate` | `external-real-candidate` | Kiro home-page task transcript/screenshot candidate. | Show task as visible delegation unit: status, changes, execution trace. | Inline placeholder; asset-pass required. |
| `fig-kiro-parallel-task-waves-candidate` | `external-real-candidate` | `Specs just got faster (and smarter)` parallel execution material. | Show dependency waves / parallel task execution. | Inline placeholder; asset-pass required. |
| `fig-kiro-context-layers` | `synthetic_figure` | Steering, chat/context, hooks, MCP/Powers, Sync Files. | Show where Kiro stores and activates context around spec. | Retained; explanatory, not decorative. |
| `fig-kiro-pbt-candidate` | `external-real-candidate` | Correctness/PBT docs. | Show natural-language/EARS requirement → executable property → generated cases/failure. | Inline placeholder; asset-pass required. |
| `fig-kiro-subagents-boundary-candidate` | `external-real-candidate`; possible synthetic fallback | Subagents docs. | Show boundary: IDE subagents do not get Specs and Hooks do not trigger. | Placeholder retained; verify whether official visual exists. |
| `fig-kiro-web-boundary-candidate` | `external-real-candidate`; freshness-sensitive | Kiro Web docs/blog. | Distinguish IDE Specs from Web Preview / autonomous PR-cycle / roadmap. | Placeholder retained; fresh Web Specs check required. |

## External candidates mirrored in article bottom block

| Candidate | Proposed local path | Article location |
| --- | --- | --- |
| `fig-kiro-quick-plan-candidate` | `content/assets/atlas-images/kiro/quick-plan-workflow.png` | After `Quick Plan: когда полный цикл был бы лишним`. |
| `fig-kiro-deep-spec-analysis-candidate` | `content/assets/atlas-images/kiro/deep-spec-analysis-pipeline.png` | After `Analyze Requirements: проверка требований до того, как они станут кодом`. |
| `fig-kiro-task-status-ui-candidate` | `content/assets/atlas-images/kiro/task-status-ui.png` | In `Задачи как единица агентского исполнения`. |
| `fig-kiro-parallel-task-waves-candidate` | `content/assets/atlas-images/kiro/parallel-task-waves.png` | In `Задачи как единица агентского исполнения`. |
| `fig-kiro-pbt-candidate` | `content/assets/atlas-images/kiro/property-based-testing-workflow.png` | After PBT section. |
| `fig-kiro-subagents-boundary-candidate` | `content/assets/atlas-images/kiro/subagents-specs-boundary.png` | After Subagents section. |
| `fig-kiro-web-boundary-candidate` | `content/assets/atlas-images/kiro/web-preview-vs-ide-specs.png` | After Web Preview section. |

## Deferred / rejected visual ideas

| Idea | Current disposition | Reason |
| --- | --- | --- |
| Feature Spec vs Bugfix branching | Deferred | Current prose/table handles the distinction; another synthetic figure would duplicate the lifecycle figure. |
| CLI context bridge | Deferred to Handbook/Fieldbook or later visual pass | Article keeps CLI as neighboring surface; no need for a separate main-article figure yet. |
| Run all Tasks protective stack | Deferred | Facts are in prose; visual density is already high. |
| Checkpoint coverage / Autopilot-Supervised control schema | Deferred | Useful operational material, but closer to Handbook/Fieldbook. |
| MCP/governance/monitoring diagrams | Deferred | Tables communicate policy-vs-evidence boundary more cleanly. |
| Vibe vs Spec mode-choice figure | Deferred | Practical criterion section is readable without another mode-selection diagram. |
| Powers dynamic context figure | Deferred | Context-layer synthetic figure already covers this enough for concept article. |

## Visual risks and blockers

- External placeholders must not be published as final assets without download, rights, quality and freshness checks.
- Web and product UI screenshots are freshness-sensitive.
- Subagents/Web candidates may need to be marked `not_found_in_source` if no official real visual exists; only then consider synthetic fallback.
- Synthetic figures are currently retained because they explain mechanism; they should be removed only if later layout/asset pass proves they duplicate prose.

## P23 sync note

- The first table now includes `fig-general-sdd-context`, which was missing from the original inline-figure inventory.
- The old generic synthetic-figure review debt is closed: P13 already retained current synthetic figures. Remaining visual blockers are concrete asset-pass checks.
## P24 image-plan note

No image was added, removed or reclassified. Heading references were synchronized after style edits: PBT now appears under `Тестирование на основе свойств: как требования становятся проверяемыми свойствами`, and Subagents under `Subagents: соседние исполнители вне полного Specs-процесса`.
## P25 image-plan note

No visual changes. Figure IDs, statuses, local path and external candidate paths remain unchanged.

## P26 image-plan note

No visual changes. Figure IDs, statuses, local path, external candidate paths and asset-pass blockers remain unchanged after the guarded final style pass.
