# Chapter IV SPDD patch apply report

## Scope

Applied a manual content patch to Chapter IV, `SPDD как спецификационный жизненный цикл`, without rerunning the executor package.

The patch follows the SPDD/Atlas alignment review: the chapter should not become a second Atlas article. Its job is to explain, in the theory sequence, why SPDD is needed, what problem it solves, and how the mechanism works at the level an engineer can use.

## Main changes

- Strengthened the opening: SPDD is framed as a way to avoid hidden product/domain/architecture decisions by the agent, not as a technique for writing better prompts.
- Reworked `Почему обычного плана недостаточно`: a plan is useful, but it does not reliably preserve intent through generation, review and later changes.
- Expanded `Как устроен REASONS Canvas`: the seven REASONS areas are explained by function rather than listed as a template catalog.
- Strengthened the human-control layer: `Abstraction First`, `Alignment`, and `Iterative Review` now explain where the human checks intent before and after generation.
- Added a tighter engineering explanation of generation, verification, `prompt-update`, and `sync`.
- Renamed and rewrote the old-code section: `Старый код как обратный вход` became `Как работать со старым кодом без исходной спецификации`.
- Added an inline figure for the SPDD lifecycle: `content/assets/theory-images/fowler-spdd-workflow.svg`.
- Added a direct link to the Atlas article: `../../atlas/articles/spdd_method.md`.
- Updated companion files: atlas usage, figure candidates, source register, readiness report, manifest, verification and resume files.

## Explicit non-goals

The patch does not import the full OpenSPDD command catalog, all Atlas images, installation details, or a broad comparison with other specification-driven development methods. Those remain Atlas / Chapter V material.

## Result size

- Main chapter: about 25.7k characters / 44.2k UTF-8 bytes / 3262 words.
- The patch increases conceptual clarity and adds a figure without turning the chapter into a second Atlas article.

## Checks

- Markdown code fences are balanced.
- The chapter includes the Atlas link.
- The chapter includes the SPDD workflow figure and the local asset is present in the result archive.
- Problematic formulas checked: `свидетельство`, `стенограмма`, `выживание`, `расследование`, `обратный вход`, `diff`.
- Archive test: `unzip -t` passed.
