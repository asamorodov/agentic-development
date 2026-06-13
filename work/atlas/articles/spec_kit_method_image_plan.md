# Image plan — Spec Kit article

Статус: P26 guarded final style. План отражает фактические inline-figures, external-real candidates and resolved/deferred visual ideas for the current article.

## Inline figures already in article

| Figure id | Type | Source / basis | Status | Rationale | Next action |
| --- | --- | --- | --- | --- | --- |
| `fig-spec-kit-home-positioning` | external real candidate | https://github.github.com/spec-kit/ | `inserted_inline_external_placeholder` | Shows product/source positioning: spec-driven, any agent, customization. | Asset-pass: download/localize, rights and quality check. |
| `fig-spec-kit-repo-layers` | synthetic figure | Dossier synthesis of docs, `.specify/`, specs, integrations. | `inserted_inline_synthetic_p01` | Explains three-layer repo mechanism better than prose alone. | Passed P13/P21 usefulness/language checks; keep unless final layout removes synthetic figures. |
| `fig-active-feature-resolution` | synthetic figure | `specify.md` + `common.sh` active feature resolution. | `inserted_inline_synthetic_p01` | Shows non-obvious fallback order: env override → feature.json → branch/catalog. | Passed P13 usefulness check; keep unless final layout removes synthetic figures. |
| `fig-full-sdd-cycle` | external real candidate | https://github.github.com/spec-kit/reference/workflows.html | `inserted_inline_external_placeholder` | Shows formal human checkpoints in workflow. | Asset-pass: download/localize, rights and quality check. |
| `fig-workflow-json-status` | external real candidate | https://github.github.com/spec-kit/reference/workflows.html | `inserted_inline_external_placeholder` | Shows machine-readable workflow state. | Asset-pass: download/localize, rights and quality check. |
| `fig-spec-kit-agents-context-hooks` | external real candidate | https://arxiv.org/abs/2604.05278 / PDF Figure 1 | `inserted_inline_external_placeholder_P12` | Shows research context-grounding layer around the Spec Kit phases, while caption explicitly says this is not baseline Spec Kit. | Asset-pass: localize only with CC BY 4.0 attribution and quality check. |
| `fig-fowler-sdd-overview-context` | local image asset | `content/assets/theory-images/fowler-sdd-overview.png` | `inserted_inline_local_asset_P11` | Gives SDD-context background only; caption says it is not a Spec Kit diagram. | Current local asset; keep as SDD-context unless final visual density requires removal. |

## Disposition for dossier image candidates

| Candidate from dossier | Disposition | Reason |
| --- | --- | --- |
| Spec Kit documentation first screen and blocks `Spec-driven by default`, `Use any coding agent`, `Make it your own` | `inserted_inline_external_placeholder` as `fig-spec-kit-home-positioning` | Directly supports article framing as portable SDD tooling. |
| GitHub repository tree with `integrations`, `templates`, `extensions`, `presets`, `workflows`, `src/specify_cli` | `deferred` | Deferred; current synthetic repo topology covers the need better than a volatile repo screenshot. |
| Workflows Mermaid/flowchart `Full SDD Cycle` | `inserted_inline_external_placeholder` as `fig-full-sdd-cycle` | Directly supports human checkpoints. |
| Workflow JSON status example (`run_id`, `workflow_id`, `status`, `current_step_id`) | `inserted_inline_external_placeholder` as `fig-workflow-json-status` | Supports machine-oriented orchestration. |
| `templates/commands/*.md` command template contract | `deferred` | Deferred; current state-transition table is more precise than another figure. |
| `templates/commands/constitution.md` semver and Sync Impact Report | `deferred` | Deferred; current prose is sufficient unless final layout requests a small callout. |
| `scripts/bash/common.sh` + `setup-plan.sh` + `setup-tasks.sh` active feature resolution | `inserted_inline_synthetic_p01` as `fig-active-feature-resolution` | Core mechanism for repo transition. |
| `scripts/powershell/common.ps1` active feature resolution Windows variant | `deferred` | Important for handbook/diagnostics; maybe too detailed for article. |
| `IntegrationBase` + `AGENTS.md` registry contract | `deferred` | Deferred; current prose and source note handle integration topology. |
| Integration lifecycle `install -> manifest -> use/switch -> upgrade` | `deferred` | Deferred; lifecycle prose is currently sufficient. |
| Upgrade two-layer update (`specify self upgrade` vs `specify init --here --force`) | `deferred` | Deferred; upgrade lifecycle is covered in prose, possible future source note. |
| `AGENTS.md` / `agent-context-config.yml` managed context | `deferred` | Deferred; article now has explicit agent-context prose. |
| Integration registry table `key -> command dir -> context file -> invocation` | `deferred` | Deferred to source note; too reference-heavy for concept article. |
| Supported integrations safety table (`slash`, `skill`, `recipe`, `wrapper`, `generic dir`) | `deferred` | Deferred to source note; too reference-heavy for concept article. |
| Presets stack resolution | `deferred` | Deferred; current article should not become a preset manual. |
| Fowler/Thoughtworks SDD overview local asset `content/assets/theory-images/fowler-sdd-overview.png` | `inserted_inline_local_asset_P11` as `fig-fowler-sdd-overview-context` | Relevant as SDD-context only; inserted with bounded caption and not used as replacement for official Spec Kit visuals. |
| arXiv Spec Kit Agents context-hooks figure | `inserted_inline_external_placeholder_P12` as `fig-spec-kit-agents-context-hooks` | Figure 1 exists in the PDF and directly supports the context-blindness caveat; caption marks it as research extension, not official Spec Kit baseline. |

## Current visual blockers after P23

- Asset-pass remains for four external-real candidates: download/localize, check rights, check quality and preserve attribution.
- Final layout should review visual density: two synthetic figures, four external placeholders and one local contextual image.
- Deferred source/UI ideas remain out of the main article unless a future source note or package layout requires them.

## P02 image sync

No images were added, removed or moved in P02. Boundary additions did not require a new visual candidate. Later P11–P13 resolved the initial visual disposition debt.

## P04 image sync

No image was added, moved or removed in P04. The new `Почему одного spec.md недостаточно` subsection is explanatory prose rather than a new visual requirement. Later P11–P13 resolved the initial visual disposition debt.

## P05 image sync

No image was added, moved or removed in P05. The new command-as-state-transition material is represented as a textual table. A future P13 pass may decide whether this table should remain prose/table or become a synthetic diagram, but no new asset candidate is queued now.

## P06 image sync

No image was added, moved or removed in P06. Constitution/checklist constraints were strengthened in prose. Existing candidate for a future constitution Sync Impact Report diagram remains deferred; no new asset request is opened.

## P07 image sync

No image was added, moved or removed in P07. The existing deferred candidates about integration topology and `AGENTS.md`/agent-context remain useful for P13, but no new inline placeholder is introduced.

## P08 image sync

No image was added, moved or removed in P08. Issue/PR caveats were added as prose with source links, not as visual candidates.

## P09 image sync

No image was added, moved or removed in P09. The deferred candidate “двухслойное обновление” became more relevant after the lifecycle expansion, but it remains deferred until P13/visual usefulness review.

## P10 image sync

No image was added, moved or removed in P10. The new reader route might become a callout or synthetic flow in a later layout pass, but no asset candidate is added now.

## P11 local asset sync

| Asset | Disposition | Reason | Article placement |
| --- | --- | --- | --- |
| `content/assets/theory-images/fowler-sdd-overview.png` | `inserted_inline_local_asset` | Relevant as a general SDD workspace/context image; not Spec Kit-specific. | Section 16, after the risk about process heaviness and Fowler/Thoughtworks SDD modes. |

The caption explicitly says the image is background for SDD-context and not a diagram of Spec Kit. Official Spec Kit visual candidates remain in the external queue.

## P12 external visual disposition audit

| Dossier candidate | P12 disposition | Source/right/quality note |
| --- | --- | --- |
| Spec Kit documentation first screen and positioning blocks | Kept inline as `fig-spec-kit-home-positioning`. | P12 web check confirmed the docs home still contains the positioning blocks. Screenshot/download still requires final asset-pass and attribution. |
| GitHub repository tree (`docs`, `extensions`, `integrations`, `presets`, `scripts`, `src/specify_cli`, `templates`, `workflows`) | Deferred as source/UI screenshot; superseded for now by `fig-spec-kit-repo-layers` synthetic figure and prose. | GitHub repository UI is volatile and the external catalog labels this a source-table/code-fragment candidate. Revisit only if final package needs a real repo-tree screenshot. |
| Workflows Mermaid/flowchart `Full SDD Cycle` | Kept inline as `fig-full-sdd-cycle`. | P12 web check confirmed the workflow YAML and Mermaid flowchart source are present. If the final renderer has a real diagram, localize it; otherwise treat as source code fragment or redraw with attribution. |
| Workflow JSON status example | Kept inline as `fig-workflow-json-status`. | P12 web check confirmed the JSON example with `run_id`, `workflow_id`, `status`, `current_step_id`, `current_step_index`. Candidate may be a screenshot of the docs block or a styled source excerpt. |
| `templates/commands/*.md` command template contract | Deferred / synthetic candidate only. | Not a real external image; a future P13 usefulness gate may decide whether command templates need a diagram. |
| `templates/commands/constitution.md` semver and Sync Impact Report | Deferred / synthetic candidate only. | Not a real external image; current prose is enough. |
| Bash setup/common scripts active feature resolution | Already represented by `fig-active-feature-resolution` synthetic figure. | Script mechanics are not an external screenshot candidate; P13 should review the synthetic figure. |
| PowerShell active feature resolution variant | Deferred. | Useful for diagnostics/source note, too detailed for the current article visual layer. |
| IntegrationBase + `AGENTS.md` registry/context contract | Deferred / possible synthetic figure. | P07 prose strengthened the handoff; no real external image localized in P12. |
| Integration lifecycle `install -> manifest -> use/switch -> upgrade` | Deferred / possible synthetic figure. | Relevant after P09, but no source image was identified; keep for P13 if visual density allows. |
| Upgrade two-layer update | Deferred / possible synthetic figure. | Relevant but not external real asset. |
| `AGENTS.md` / `agent-context-config.yml` managed context | Deferred / possible synthetic figure. | No real image needed yet. |
| Integration registry table | Deferred to companion/source note. | Better as a versioned table than as an inline image. |
| Supported integrations safety table | Deferred. | Version-sensitive; would need current source verification and likely belongs in source note. |
| Presets stack resolution | Deferred. | Could become a compact source-linked diagram later, not a P12 external image. |
| Fowler/Thoughtworks SDD overview local asset | Inserted inline as `fig-fowler-sdd-overview-context`. | Local file exists and is relevant as SDD-context; caption bounds its role. |
| arXiv Spec Kit Agents context-hooks figure | Inserted inline as `fig-spec-kit-agents-context-hooks`. | P12 inspected the PDF page with Figure 1 and noted arXiv page license link to CC BY 4.0; image not downloaded. |

## P13 synthetic figure gate

| Synthetic candidate | Decision | Reason |
| --- | --- | --- |
| `fig-spec-kit-repo-layers` | `keep` | Nontrivial: it compresses feature artifacts, `.specify/` process infrastructure and agent surface into one repo topology. It does not replace a real external asset; the repo-tree screenshot remains deferred separately. |
| `fig-active-feature-resolution` | `keep` | Nontrivial: it shows the fallback order for active feature resolution, which is difficult to hold in prose and is central to the article's “right artifact, right state” argument. |
| Command-as-state-transition diagram | `defer` | Current table is more precise and source-linked; a diagram would mostly duplicate it. |
| Constitution/checklist gate diagram | `defer` | Prose is sufficient after P06; no rare synthetic value yet. |
| Integration lifecycle / agent surface diagram | `defer` | Potentially useful, but P07/P09 prose already carries the point and a synthetic figure might blur version-sensitive details. |
| Two-layer upgrade diagram | `defer` | Useful for a practical source note, but the concept article does not need another inline schematic before final density review. |

No new synthetic figure was added in P13. Existing synthetic figures remain because they pass the nontriviality gate and are not substitutes for local/external real assets.

## P14 image sync

No image was added, moved or removed in P14. The new minimal-model subsection is conceptual prose and does not require a new figure; converting it into a diagram would risk duplicating `fig-spec-kit-repo-layers` and the command state-transition table.

## P15 image-plan sync

P15 added no new image, screenshot or synthetic figure. Existing visual placement remains valid: the failure-mode reinforcement is textual and belongs beside the relevant mechanism sections, not in a separate warning diagram. Later layout may turn one or two checks into callouts, but no visual asset is currently required.

## P16 image-plan sync

P16 added theory back-links only. No figure, screenshot, external visual candidate or synthetic diagram was added or moved. Visual density and asset queue remain unchanged.

## P17 image-plan sync

P17 changed language only. Figure set, placement and image statuses did not change. Captions were lightly normalized where they contained ordinary English glue; exact source titles and asset-status labels remain unchanged.

## P18 image-plan sync

P18 did not change the image set or placement. It normalized captions and the bottom asset-preparation wording so they read as Russian user-facing text. All asset IDs, source URLs, proposed paths and `external-real-candidate` statuses remain unchanged.

## P19 image-plan sync

No image was added, removed, moved or downloaded in P19. The editorial pass found that the bottom image-candidate block could distract from standalone reading if it looked like normal article argument. The block was therefore temporarily contained as asset-preparation metadata; P22 later restored the required `Внешние изображения для asset-pass` heading and made inline captions public.

All image IDs, source URLs, proposed local paths, placements and `external-real-candidate` statuses remain unchanged.

## P20 image-plan sync

No image was added, moved, removed or downloaded in P20. The split boundary paragraph and command-surface clarifications do not require a new visual. Existing external candidates and synthetic figures remain unchanged.

## P21 image-plan sync

No image was added, moved, removed or downloaded in P21. The only visual-related change was inside the existing synthetic `fig-spec-kit-repo-layers`: one label was localized so the diagram reads in the same language as the article while preserving exact integration terms. Image status and placement remain unchanged.

## P22 image-plan sync

P22 changed public visual framing but did not add, remove, download or replace any image.

| Item | Change | Status |
| --- | --- | --- |
| `fig-spec-kit-home-positioning` | Now appears immediately after the reader question, before section 1, so the entry sequence remains problem-first while still giving a visual source frame. | `same_candidate_public_caption_P22` |
| Inline external-real candidates | Captions no longer say “service asset-preparation wording”; they now describe the image's argumentative role. | `captions_publicized_P22` |
| Bottom external-image section | Heading restored to `Внешние изображения для asset-pass`; candidate metadata remains there and in the external queue. | `asset_pass_metadata_preserved_P22` |
| Local Fowler image and synthetic figures | No placement or status change. | `unchanged_P22` |

This pass follows the visual rule: external real candidates remain inline placeholders plus bottom/queue metadata, without being degraded into synthetic substitutes.

## P23 image-plan sync

P23 removed stale visual-debt wording from earlier pass notes and converted the current plan into concrete blockers:

- four external-real candidates need asset-pass localization/rights/quality work;
- two synthetic figures remain accepted after P13/P21 unless final layout removes them;
- the local Fowler image remains inserted as SDD context only;
- deferred repository/integration/upgrade/preset visuals are not current article blockers and belong to a possible source note if needed.

## P24 image-plan sync

P24 changed only caption prose. `fig-spec-kit-repo-layers` now says “инфраструктура метода в проекте” instead of a heavier noun chain; `fig-full-sdd-cycle` now explains that the workflow gate is stronger than a textual manual-review request. No image candidate, source, proposed path or asset-pass blocker changed.

## P25 image-plan sync

P25 changed only caption language for `fig-spec-kit-home-positioning`: the caption now says the first screen shows how Spec Kit describes itself, rather than calling it a “visual frame of self-description”. Candidate status, source URL, proposed path and asset-pass requirements did not change.

## P26 image-plan sync

P26 did not change figures, captions, source URLs, proposed local paths or visual status. The image plan remains the same: four external-real candidates need asset-pass work; two synthetic figures and the local Fowler context image remain as currently placed.
