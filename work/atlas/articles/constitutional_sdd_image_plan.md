# constitutional_sdd — image plan

Статус: P26 guarded final style sync. Визуальные решения не менялись; обновлены только текущие названия разделов и подписи, где они связаны с текстом.

## Inline external placeholders

| Figure ID | Source candidate | Disposition | Article location | Rationale | Status |
|---|---|---|---|---|---|
| `fig-csdd-architecture` | Figure 1 from ar5iv full text | `inserted_inline_external_placeholder` | После вопроса читателя и короткой проверки CSDD | Показывает иерархию Constitution над артефактами и compliance traceability | `external-real-candidate`; rights/download/quality check required |
| `fig-csdd-compliance-matrix` | Table 1 from ar5iv full text | `inserted_inline_external_placeholder` | Compliance matrix section | Нужна для объяснения principle/CWE/file/lines/technique surface | `external-real-candidate`; rights/download/quality check required |
| `fig-csdd-three-phase-loop` | Figure 4 from repository `PAPER.md` | `inserted_inline_external_placeholder` | Workflow section | Показывает feedback loop from compliance verification to spec/generation | `external-real-candidate`; canonicality and rights check required |

## Dossier candidates disposition

| Candidate from dossier | Disposition | Reason |
|---|---|---|
| Figure 1 from ar5iv: architecture with Constitution on top | `inserted_inline_external_placeholder` | Core mechanism visual. |
| Table 1 from ar5iv: compliance traceability matrix | `inserted_inline_external_placeholder` | Core evidence-surface visual. |
| Figure 2 from ar5iv: CWE coverage by implementation effort | `external_queue_only` / `deferred` | Potentially useful for metrics section, but P01 keeps metrics cautious and does not over-center the 73% claim. |
| README diagrams from `banking-ms-by-constitution` | `external_queue_only` with rights hold | Useful for reference implementation / Fieldbook, but source license caveat says `Private - All rights reserved`; no inline placement before rights decision. |
| Figure 4 from `PAPER.md` | `inserted_inline_external_placeholder` | Useful workflow loop; marked non-canonical until PDF/arXiv comparison. |
| Reconstructed `.specify/memory/constitution.md -> spec.md -> plan.md -> tasks.md -> code -> CONSTITUTION_COMPLIANCE.md` diagram | `deferred` as `synthetic_figure` candidate | Strong candidate for later visual pass; P01 uses source Figure 1/Table 1 first and avoids replacing source visuals. |
| Reconstructed Mad Devs workflow | `deferred` as `editorial_visual_idea` / `synthetic_figure` | Could clarify threat model -> constitution -> agent instructions -> PR/CI gates, but needs visual pass. |
| Reconstructed DocGuard/Spec Kit loop | `deferred` as `editorial_visual_idea` / `synthetic_figure` | Could clarify guard/trace gates; avoid overloading CSDD article into DocGuard article. |
| Reconstructed Foundry flow | `deferred` as `editorial_visual_idea` / `synthetic_figure` | Useful for neighbor section only if Foundry remains substantial. |
| Reconstructed Foundry evidence gate | `deferred` as `editorial_visual_idea` / `synthetic_figure` | Useful for evidence comparison; may belong in a separate Foundry/neighbor article instead. |

## Proposed local paths for asset-pass

- `content/assets/atlas-images/constitutional-sdd/csdd-architecture-figure-1.png`
- `content/assets/atlas-images/constitutional-sdd/csdd-compliance-matrix-table-1.png`
- `content/assets/atlas-images/constitutional-sdd/csdd-three-phase-loop-paper-figure-4.png`
- `content/assets/atlas-images/constitutional-sdd/csdd-cwe-coverage-effort-figure-2.png`
- `content/assets/atlas-images/constitutional-sdd/banking-reference-readme-*`

## Visual cautions

- Do not replace ar5iv Figure 1 or Table 1 with a synthetic diagram unless rights/readability fail and the replacement is explicitly marked as original synthesis.
- Do not reuse README diagrams before rights/license decision.
- Do not let Foundry/DocGuard visuals make the article look like a Spec Kit extension article rather than CSDD.

## P05 visual sync note

P05 added an artifact map but did not add or remove image candidates. A later visual pass may decide whether this table should become an original synthetic diagram; for now no synthetic figure was created to avoid replacing source visuals prematurely.

## P06 visual sync note

P06 deepened the compliance-matrix explanation but did not add or move image candidates. The existing `fig-csdd-compliance-matrix` placeholder remains the correct external-real candidate for the matrix section. A later original visual could show matrix pressure on `plan.md`, `tasks.md`, PR/review and Constitution amendment, but it is deferred as a synthetic/editorial idea rather than added to the external image queue.

## P07 visual sync note

P07 added a textual layer table but did not add external image candidates. A later original synthetic diagram could show “Spec workflow” below “Constitution/policy layer” and “evidence/traceability” as a side rail. This is an editorial diagram idea, not an external asset queue item.

## P08 visual sync note

P08 added limits and false-confidence modes, but no new external image candidates. A later original sidebar could summarize “declaration / overconfidence / disconnected policy / missing evidence / human responsibility,” but no asset was added in this pass.

## P09 visual sync note

P09 added a textual `пакет конституционных ограничений` table. No external image candidates were added. A later original synthetic figure could show selection from full Constitution into a task-sized packet, but this is an editorial visual idea and not an external image queue item.

## P10 visual sync note

P10 added a transfer-endpoint walkthrough but no new external image candidates. A later original synthetic figure could show one feature moving through `spec.md -> plan.md -> tasks.md -> пакет конституционных ограничений -> code -> matrix -> repair loop`; this is an editorial visual idea and not an external asset candidate.

## P11 local asset pass

| Local asset | Disposition | Article location | Reason |
|---|---|---|---|
| `content/assets/theory-images/fowler-sdd-overview.png` | `inserted_inline_local_image_asset` | `Как CSDD ложится поверх спецификационного процесса` | Relevant only as generic SDD background: it shows agent-facing memory/spec surfaces before the article explains CSDD's higher Constitution/policy layer. Caption explicitly prevents treating it as CSDD evidence. |

Other local images listed in `LOCAL_ASSET_INDEX.md` were not inserted: they are about SPDD, harness engineering, multi-agent process, observability, worktrees, Codex UI, story screenshots or other atlas topics. They do not match the visual priorities for this CSDD article, where real Marri/repo figures and compliance/traceability tables remain primary.

## P12 external real image pass

P12 started from the CSDD dossier candidates and the shared external-image catalog. All dossier-listed visual candidates already had dispositions from P01; this pass normalized the public captions for the three inline placeholders and reaffirmed the queue decisions.

| Candidate | Disposition after P12 | Notes |
|---|---|---|
| ar5iv/PDF Figure 1 | `inline_external_real_candidate_caption_normalized` | Remains the priority source image for hierarchy/architecture. |
| ar5iv/PDF Table 1 | `inline_external_real_candidate_caption_normalized` | Remains the priority source table for traceability. Consider redrawing as local table only after rights/readability decision. |
| `PAPER.md` Figure 4 | `inline_external_real_candidate_caption_normalized` | Useful for repair loop, but still non-canonical until compared with arXiv/PDF. |
| ar5iv/PDF Figure 2 | `external_queue_only_deferred` | Not inserted because the article keeps metrics cautious and concept-first. |
| Reference README diagrams | `rights_hold_queue_only` | Not inserted because README license caveat says `Private - All rights reserved` in source slice. |
| Mad Devs workflow illustration | `synthetic_redraw_preferred_deferred` | Do not copy source graphic by default; if used, create an original diagram from sourced facts. |
| DocGuard/Spec Kit loop | `editorial_visual_idea_deferred` | Could be an original diagram later; not a source image for this article. |
| Foundry workflow/evidence gate | `editorial_visual_idea_deferred` | Could support neighbor section later; avoid over-expanding Foundry here. |

## P13 synthetic figure pass

No synthetic figure was inserted. The pass evaluated three possible original diagrams and deferred them:

| Synthetic candidate | Disposition | Reason |
|---|---|---|
| Constitution selection into a task-sized packet | `deferred_editorial_visual_idea` | Useful but not yet necessary; the P09 table explains the mechanism without replacing any real source image. |
| One-feature trace from transfer scenario through spec/plan/tasks/context/matrix/repair | `deferred_editorial_visual_idea` | Potentially valuable, but would overlap with the P10 walkthrough and the external `PAPER.md` Figure 4 candidate. |
| CSDD layer over generic SDD workflow | `not_inserted_due_to_existing_visual_and_table` | P11 already inserted `fowler-sdd-overview.png` and P07 has a layer table. |

The current visual priority remains: localize Marri Figure 1, Marri Table 1 and possibly `PAPER.md` Figure 4 before adding author-created diagrams.

## P14 visual sync note

P14 added a standalone vocabulary section and no new visual candidates. Existing source visuals remain sufficient for concept-first orientation.

## P15 visual sync note

P15 strengthened mechanism/failure-mode prose and removed the standalone failure catalog. No visual candidates were added, removed or moved. If a later visual is needed for this pass, it should be an original mechanism diagram showing “rule changes next action” across `spec.md`, `plan.md`, `tasks.md`, context and matrix; it should not replace Marri Figure 1/Table 1 or the existing workflow-loop candidate.

## P16 visual sync note

P16 changed theory-link framing and did not add visual candidates. No image plan changes are needed. If a future theory-backlink visual appears, it should live in the general theory/atlas navigation layer, not inside this CSDD article unless it directly clarifies Constitution-to-evidence mechanics.


## P17 языковая синхронизация изображений

- В основном тексте переведены подписи и пояснения вокруг визуальных кандидатов: `Figure/Table` в inline-подписях русифицированы как рисунок/таблица, а служебные статусы загрузки/прав/качества описаны по-русски.
- Решения по изображениям не изменились: один локальный SDD-контекст остаётся вставленным, три CSDD-кандидата остаются `external-real-candidate`, Figure 2 и README diagrams остаются в очереди/на паузе.
- Новых синтетических схем P17 не добавлял.

## P18 языковая синхронизация визуального плана

- Повторно проверены подписи inline-кандидатов и нижняя очередь внешних изображений.
- Точные указатели источников `Figure 1`, `Table 1`, `Figure 4`, `Figure 2` сохранены в поле источника, потому что они помогают найти нужный объект в исходном материале.
- Русские описания назначения, места в тексте, статуса и причин откладывания сохранены; визуальные решения P11–P13 не менялись.

## P19 редакторская синхронизация визуального плана

P19 добавил только текстовый критерий применения и раннюю диагностическую проверку. Новые изображения не нужны: эти фрагменты лучше работают как короткое объяснение, а не как дополнительная схема. Очередь реальных и отложенных визуальных кандидатов не изменилась.

## P20 редакторская синхронизация визуального плана

P20 не менял визуальную стратегию. Переименование раздела о матрице не меняет кандидата `fig-csdd-compliance-matrix`: источник и место в тексте остаются теми же.

## P21 редакторская синхронизация визуального плана

P21 переименовал несколько текстовых разделов, но не изменил места визуальных кандидатов. `fig-csdd-three-phase-loop` остаётся привязанным к рабочей цепочке, `fig-csdd-compliance-matrix` — к матрице, а нижняя очередь не меняется.

## P22 структурная синхронизация визуального плана

- `fig-csdd-architecture` перенесён ниже: теперь он стоит после reader question и короткой проверки CSDD, а не до них.
- Подписи Figure 1 и `PAPER.md` Figure 4 очищены от служебного редакторского тона.
- Нижний публичный раздел называется `Внешние изображения для asset-pass`; визуальные решения и статусы не изменились.


## P23 visual companion sync

- Место `fig-csdd-architecture` синхронизировано с текущей статьёй: после вопроса читателя и короткой проверки CSDD.
- Нижний публичный раздел согласован с названием `Внешние изображения для asset-pass`; новые изображения не добавлялись.
- Foundry/CodeGuard visual branch очищена: CodeGuard не является текущим blocker, а Foundry visuals остаются deferred neighbor-article ideas.

## P24 style-defect visual sync

- Визуальные кандидаты, статусы и места в статье не менялись.
- Caption `fig-csdd-three-phase-loop` очищен от псевдотермина «петля ремонта»; теперь он прямо говорит об обратной связи к спецификационным артефактам.
- Caption `fig-csdd-compliance-matrix` очищен от кальки «проверочная поверхность» и теперь говорит о месте в коде, которое можно проверить.

## P25 visual wording sync

- Визуальные кандидаты и места вставки не менялись.
- Подпись Figure 1 очищена от выражения `карта полномочий`; смысл сохранён: диаграмма показывает подчинение артефактов Constitution и след соответствия.
- Нижнее описание README diagrams в публичной статье теперь говорит о будущем практическом материале, а не использует Fieldbook-англицизм.

## P26 guarded final style sync

No image decision changed in P26. Figure placements, IDs, external-real-candidate statuses and local Fowler image remain the same. Only public caption language and current article section names were aligned with the final human technical style pass.
