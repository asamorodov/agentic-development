# External image queue — Spec Kit article

Статус: P26 guarded final style. Очередь содержит только external-real image candidates that still need asset-pass localization/rights/quality work.

## Inline candidates

### fig-spec-kit-home-positioning
- Источник: https://github.github.com/spec-kit/
- Что взять: первый экран документации и блоки позиционирования.
- Зачем нужна: показывает самоописание Spec Kit как переносимого SDD-инструментария.
- Предлагаемый локальный путь: `content/assets/atlas-images/spec-kit/spec-kit-home-positioning.png`
- Текущее место в статье: after reader question.
- Статус: `external-real-candidate`; требуется download/localization, rights and quality check.

### fig-full-sdd-cycle
- Источник: https://github.github.com/spec-kit/reference/workflows.html
- Что взять: схема `Full SDD Cycle` / Mermaid diagram.
- Зачем нужна: показывает `review-spec` и `review-plan` как формальные человеческие гейты.
- Предлагаемый локальный путь: `content/assets/atlas-images/spec-kit/full-sdd-cycle.png`
- Текущее место в статье: Workflows section.
- Статус: `external-real-candidate`; требуется download/localization, rights and quality check.

### fig-workflow-json-status
- Источник: https://github.github.com/spec-kit/reference/workflows.html
- Что взять: пример JSON-статуса запуска или возобновления рабочего процесса.
- Зачем нужна: показывает машинно-читаемое состояние рабочего процесса.
- Предлагаемый локальный путь: `content/assets/atlas-images/spec-kit/workflow-json-status.png`
- Текущее место в статье: Workflows section.
- Статус: `external-real-candidate`; требуется download/localization, rights and quality check.

### fig-spec-kit-agents-context-hooks
- Источник: https://arxiv.org/abs/2604.05278 и PDF https://arxiv.org/pdf/2604.05278
- Что взять: Figure 1 с обзором рабочего процесса Spec Kit Agents, PM/developer agents, discovery hooks, validation hooks and repository tools.
- Зачем нужна: отличает базовый Spec Kit от исследовательского слоя, который привязывает фазы к контексту репозитория.
- Предлагаемый локальный путь: `content/assets/atlas-images/spec-kit/spec-kit-agents-context-hooks.png`
- Текущее место в статье: Risks section after context-blindness caveat.
- Статус: `inserted_inline_external_placeholder_P12`; PDF figure was inspected, arXiv page links to CC BY 4.0; not downloaded.

## Queue-only / future candidates and resolved local assets

### fig-fowler-sdd-overview
- Источник: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html and local asset `content/assets/theory-images/fowler-sdd-overview.png` noted in dossier.
- Что взять: existing local asset as SDD-context only.
- Зачем нужна: contextualize `spec-first`, `spec-anchored`, `spec-as-source` boundary without replacing Spec Kit-specific visuals.
- Proposed local path if reused: existing local path.
- Статус: `resolved_local_asset_inserted_P11` as `fig-fowler-sdd-overview-context`; no external download needed.

## P02 queue sync

No external image candidates were added, removed or moved in P02.

## P04 queue sync

No external image candidate was added, removed or moved in P04. The strengthened multi-artifact explanation does not require a new screenshot or third-party image at this stage.

## P05 queue sync

No external image candidate was added, removed or moved in P05. The state-transition table is not an external asset request.

## P06 queue sync

No external image candidate was added, removed or moved in P06.

## P07 queue sync

No external image candidate was added, removed or moved in P07. Integration/context surface material is currently prose-only.

## P08 queue sync

No external image candidate was added, removed or moved in P08.

## P09 queue sync

No external image candidate was added, removed or moved in P09.

## P10 queue sync

No external image candidate was added, removed or moved in P10.

## P12 queue sync

- `fig-spec-kit-home-positioning`, `fig-full-sdd-cycle` and `fig-workflow-json-status` remain inline `external-real-candidate` placeholders. P12 verified the relevant source content on the Spec Kit docs pages, but did not download images.
- `fig-spec-kit-agents-context-hooks` moved from queue-only to inline placeholder because Figure 1 directly supports the context-blindness risk. The caption marks it as research extension, not official Spec Kit.
- `fig-fowler-sdd-overview` is no longer external queue debt: the local file was inserted as `fig-fowler-sdd-overview-context` and bounded as SDD background.
- Repository tree, integration lifecycle, upgrade lifecycle, presets and command-template candidates remain deferred/synthetic-candidate items; P12 did not create new external downloads.

## P13 queue sync

No external image was added, removed or replaced in P13. The pass only reviewed synthetic-figure candidates. External-real candidates from P12 remain unchanged, and deferred source/UI candidates are not replaced by new synthetic diagrams.

## P14 queue sync

No external image candidate changed in P14. The new standalone entry subsection does not create an asset need.

## P15 external queue sync

No external image candidate was added, removed or reprioritized in P15. The official docs/workflow candidates and the arXiv Spec Kit Agents candidate remain in the same asset-pass queue; the new failure-mode text does not require additional external verification or screenshot capture.

## P16 external queue sync

No queue change in P16. Theory back-links do not introduce new external image candidates and do not alter the status of existing official-doc/workflow/arXiv candidates.

## P17 external queue sync

No external image was added, removed or reprioritized in P17. Queue entries keep their exact source URLs, proposed local paths and `external-real-candidate` labels; surrounding Russian wording was normalized in the article.

## P18 external queue sync

No external queue change. The queue remains the same; P18 only improved the article's Russian wording around image candidates, rights/quality checks and placement notes.

## P19 external-image queue sync

Queue contents did not change. P19 temporarily contained the bottom list as future image-preparation metadata; P22 later restored the required `Внешние изображения для asset-pass` heading. No candidate was promoted, rejected, downloaded or substituted by a synthetic figure.

## P20 external-image queue sync

No queue change. P20 made editorial command-surface and readability fixes only; all external-real candidates remain in the same status and placement.

## P21 external-image queue sync

No external-image queue change. P21 touched only Russian terminology and the existing synthetic figure label; no external candidate was promoted, rejected, moved or downloaded.

## P22 external-image queue sync

Queue contents did not change. Public captions were rewritten in the article, but all four external-real candidates keep the same source URLs, proposed local paths and statuses. The article bottom section is again titled `Внешние изображения для asset-pass`, matching the queue purpose.

## P23 external-image queue sync

P23 updated the queue status and wording to match the current article. Queue contents remain unchanged: four inline external-real candidates require asset-pass work; the Fowler item is resolved as a local asset; no queue-only candidate is a current article blocker.

## P24 external-image queue sync

External-real queue unchanged. The `fig-full-sdd-cycle` inline caption was tightened stylistically, but source URL, proposed local path, status and asset-pass obligations remain the same.

## P25 external-image queue sync

Queue contents unchanged. The opening Spec Kit homepage caption was made more natural, but the homepage candidate remains `external-real-candidate` with the same source URL, path and rights/quality obligations.

## P26 external-image queue sync

No queue change. P26 did not move, promote, reject, localize or rewrite external-image candidates.
