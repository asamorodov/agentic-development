# BMAD Method — readiness report

Статус: Final verification завершён / package готов к передаче; обязательные output-файлы существуют, статья и companion-файлы упаковываются как completed archive.

## Created files

- `work/atlas/articles/bmad_method.md`
- `work/atlas/articles/bmad_method_source_usage.md`
- `work/atlas/articles/bmad_method_source_transfer_ledger.md`
- `work/atlas/articles/bmad_method_image_plan.md`
- `work/atlas/articles/bmad_method_external_image_queue.md`
- `work/atlas/articles/bmad_method_open_questions.md`
- `work/atlas/articles/bmad_method_theory_links.md`
- `work/atlas/articles/bmad_method_degradation_and_duplication_audit.md`
- `work/atlas/articles/bmad_method_readiness_report.md`

## P01 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Main article file exists | PASS | `bmad_method.md` created. |
| Article answers reader question | PASS | Central axis: artifact-first BMAD, context transfer through PRD/architecture/story/status/review/correct-course/brownfield docs. |
| No internal volume limit imposed | PASS | Draft length determined by concept/source needs. |
| Companion files created | PASS | All target outputs created with P01 status. |
| Source provenance started | PASS | Main article uses primary source links; source usage companion created. |
| Source transfer logged | PASS | Major transferred/deferred materials recorded. |
| Visual candidates handled | PASS with debts | Dossier candidates dispositioned; workflow map placeholder inserted; external queue created; two synthetic figures inserted. |
| Open questions recorded | PASS | Version, adoption, boundary and asset questions captured. |
| Theory links recorded | PASS | C5/A10/A5/C2/A9/A7/A8 links mapped. |
| Degradation audit recorded | PASS | Initial anti-duplication and readiness audit created. |
| External source refresh performed | NOT IN P01 | P01 used only allowed bundled inputs; future pass required. |
| External images downloaded/localized | NOT IN P01 | Queue only; rights/quality check required. |

## Current readiness

`ready_for_P02_article_contract_with_known_debts`.

The next pass should validate article contract: reader question, boundaries, article tier and relation to theory. It should not rewrite the article wholesale unless it finds a structural defect in the contract.


## P02 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Article contract added inside main article | PASS | New section «Контракт статьи: где проходит граница BMAD». |
| Reader question preserved | PASS | Intro unchanged and contract section operationalizes it. |
| Negative boundary added | PASS | Article says it must not become personas/commands/ecosystem overview/generic SDLC guide. |
| Lifecycle-function rule added | PASS | Detail inclusion must create next input, narrow context, record state, create human decision point, produce evidence or repair path. |
| BMAD/GSD boundary | PASS | GSD phase loop/runtime/process supervision separated from BMAD artifact-first SDLC profile. |
| BMAD/PWG boundary | PASS | `sprint-status.yaml` separated from durable work graph semantics. |
| BMAD/Gas Town boundary | PASS | Gas Town treated as operating environment / orchestration layer. |
| BMAD/Spec Kit/Kiro/SPDD/TDAD boundary | PASS with TDAD debt | Spec/prompt/test methods are adjacent; no TDAD-specific facts added because no TDAD dossier was allowed. |
| ADR boundary | PASS | ADR stores decisions, not the whole execution method. |
| C5/A10 handling | PASS | Read-only context only; no generic pending debt. |
| Companion sync | PASS | `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links`, audit/readiness all updated. |

## Current readiness after P02

`ready_for_P03_with_contract_boundaries_and_known_debts`.

Known P02 debts are concrete: source freshness for adjacent methods, future cross-article sync for PWG/Gas Town/GSD/specification-method articles, and TDAD-specific boundary source collection if a later pass introduces TDAD facts.


## P04 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Core artifact chain expanded as context handoff | PASS | Added handoff paragraph and table. |
| Role section not expanded into persona catalog | PASS | Roles tied to produced artifacts and reproducible traces. |
| New source facts tracked | PASS | Used existing BMAD sources; source usage updated. |
| Required companion sync | PASS | Source usage, transfer ledger, image plan, queue, open questions, theory links, audit and readiness updated. |
| Main article preserved | PASS | No wholesale rewrite; source-depth addition only. |

## Current readiness after P04

`ready_for_P05_with_documentary_handoff_strengthened`.


## P05 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| File mechanics expanded | PASS | `_bmad/`, `_bmad-output/`, manifest, planning artifacts, project context, sprint state and story files are explained as recovery surfaces. |
| Recovery and next-action function visible | PASS | New table maps each surface to recovery and next step. |
| Sprint state recovery added | PASS | `bmad-sprint-status` now explicitly framed as next-action recovery. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit and readiness updated. |
| No unauthorized external source | PASS | P05 used bundled dossier and existing tracked source links only. |

## Current readiness after P05

`ready_for_P06_with_file_recovery_surface_strengthened`.


## P06 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Scan levels shown | PASS | Added table for Quick/Deep/Exhaustive/Deep Dive knowledge depth. |
| Documentation requirements and scan report surfaced | PASS | Existing flags retained; `project-scan-report.json` framed as state of knowledge creation. |
| Generated docs/index explained | PASS | `index.md` now explicitly routes future agents to generated docs or missing-doc markers. |
| Stale-doc risk strengthened | PASS | Brownfield stale docs framed as false current truth risk. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

## Current readiness after P06

`ready_for_P07_with_brownfield_knowledge_creation_strengthened`.


## P07 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| PRD validation/readiness included | PASS | Added distributed human decision table. |
| Checkpoint preview located | PASS | Table connects it to human decision after autonomous work. |
| Investigation/correct-course/retrospective located | PASS | Repair and learning routes shown as human gates. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| No unauthorized external source | PASS | Used bundled/current tracked source links only. |

## Current readiness after P07

`ready_for_P08_with_human_gates_and_repair_strengthened`.


## P08 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| TEA/Enterprise bounded | PASS | Treated as evidence/release extension, not default BMAD. |
| Failure modes expanded | PASS | Token cost, ceremony, stale artifacts, overplanning and module confusion present. |
| Weak sources avoided | PASS | Community/adoption friction not used as evidence. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| No unauthorized external source | PASS | Used current tracked source links only. |

## Current readiness after P08

`ready_for_P09_with_evidence_extension_and_limits_strengthened`.

## P09 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Main deficiency selected editorially | PASS | Chose Quick Dev because the short mode was still too schematic compared with the dossier. |
| New material integrated into article | PASS | Added intent compression, short spec/approval, `deferred-work.md`, scope escalation and layer-aware failure diagnosis. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| No unauthorized external source | PASS | Used only current article outputs and BMAD dossier sources. |
| Over-expansion avoided | PASS | No new table/figure and no community/adoption claims. |

## Current readiness after P09

`ready_for_P10_with_quick_dev_lifecycle_strengthened`.

## P10 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Main deficiency selected editorially | PASS | Chose lack of a compact reader path connecting many technical details. |
| New material integrated into article | PASS | Added «Инвариант BMAD» section after the “why BMAD” pressure section. |
| C5 used appropriately | PASS | Used as article-structure constraint, not as public factual source. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| Visual/command bloat avoided | PASS | No new table, figure, command catalog or external image. |

## Current readiness after P10

`ready_for_P11_with_reader_path_strengthened`.

## P11 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Required local assets reviewed | PASS | Checked required catalogs and Fowler harness images. |
| Insert-or-explain satisfied | PASS | No local asset inserted; rejection reasons recorded in image plan. |
| BMAD visual priorities preserved | PASS | No non-BMAD harness image imported into BMAD article. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| No unauthorized source expansion | PASS | No web check and no unlisted markdown source used. |

## Current readiness after P11

`ready_for_P12_with_local_assets_dispositioned`.

## P12 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Dossier image candidates reviewed | PASS | Official Workflow Map, project tree and synthetic/editorial candidates dispositioned. |
| Relevant external candidate inline | PASS | `fig-bmad-workflow-map` already placed after the main chain and retained. |
| Bottom asset-pass section mirrored | PASS | Article bottom status updated; external queue updated. |
| No image downloaded | PASS | Required by pass; rights/quality/localization remain future work. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

## Current readiness after P12

`ready_for_P13_with_external_visual_candidates_dispositioned`.

## P13 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Rare synthetic-figure gate applied | PASS | No new figure added because existing visuals/tables already cover the mechanism. |
| Deferred candidates recorded | PASS | Quick Dev, SPEC, brownfield, Correct Course, investigation, TEA and boundary figures remain deferred. |
| No real image replaced | PASS | External Workflow Map candidate preserved. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| Article not bloated | PASS | No new table or figure inserted. |

## Current readiness after P13

`ready_for_P14_with_synthetic_visuals_controlled`.

## P14 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Standalone concept-first article strengthened | PASS | Added minimal example of a risky change through BMAD artifacts. |
| Controlled repetition allowed | PASS | Repeats only the local minimum: process passes context through documents/status/repair. |
| No new external source or asset | PASS | Example is illustrative prose; no image/source queue expansion. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |
| Boundary preserved | PASS | Example does not import GSD/PWG/Gas Town or general theory chapter. |

## Current readiness after P14

`ready_for_P15_with_standalone_concept_example_strengthened`.

## P15 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Mechanism strengthened | PASS | Invariant now explains why roles/documents fail when they do not feed next steps. |
| Boundaries strengthened | PASS | Mode confusion and TEA-as-core risk integrated. |
| Failure modes embedded, not cataloged | PASS | Added prose in invariant and role sections, not a new error list. |
| No feature/source overview drift | PASS | No new source catalog or command list added. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

## Current readiness after P15

`ready_for_P16_with_mechanism_failures_embedded`.

## P16 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Semantic backlinks added | PASS | `bmad_method_theory_links.md` now states which theory question each fragment helps BMAD clarify. |
| Main text checked against theory scope | PASS | Added one guard paragraph; no wholesale theory rewrite. |
| C5 standalone-article boundary preserved | PASS | Full theory exposition remains in companion links, not in the public article body. |
| No new source facts introduced | PASS | P16 used internal theory fragments and existing article outputs only. |
| Visual queue unaffected | PASS | No new image, table or external candidate. |
| Companion sync | PASS | All required companions updated. |

## Current readiness after P16

`ready_for_next_pass_with_semantic_theory_backlinks`.

## P17 acceptance checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Main article language pass performed | PASS | Accidental English glue and hybrid explanatory phrases were reduced. |
| Factual argument preserved | PASS | P17 did not add/remove source facts or article sections. |
| Exact names preserved | PASS | Commands, file paths, source labels, status values and established BMAD terms remain where exact form matters. |
| Replacement damage checked | PASS | URLs and main figure/path identifiers checked after cleanup. |
| Companion sync | PASS | All required companions updated. |

## Current readiness after P17

`ready_for_next_pass_with_first_language_cleanup`.

## P18 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Второй языковой проход выполнен | PASS | Проверены заголовки, подписи, таблицы и нижний раздел для прохода по ассетам. |
| Основной аргумент сохранён | PASS | P18 не добавлял и не удалял факты из источников, разделы или визуальные решения. |
| Точные имена сохранены | PASS | Команды, пути, source labels, id фигур и устойчивые термины BMAD оставлены там, где нужна точная форма. |
| Раздел для прохода по ассетам синхронизирован | PASS | Кандидат Workflow Map сохраняет статус `external-real-candidate`; долги по правам, скачиванию, качеству и атрибуции явно указаны. |
| Companion-файлы синхронизированы | PASS | Все обязательные companion-файлы обновлены для P18. |

## Текущая готовность после P18

`ready_for_editorial_passes_after_second_language_cleanup`.

## P19 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Проблемы сначала сформулированы | PASS | Диагностика P19 записана в degradation/duplication audit. |
| Standalone-ценность усилена | PASS | Практический раздел получил короткий четырёхвопросный критерий применения BMAD. |
| Фактура не сглажена | PASS | Технические детали, ссылки, source-specific names и визуальные решения сохранены. |
| Изменения точечные | PASS | Исправлены заголовок контрактного раздела, формулировка ограничения деталей и финальная практическая проверка. |
| Companion-файлы синхронизированы | PASS | Все обязательные companion-файлы обновлены для P19. |

## Текущая готовность после P19

`ready_for_second_editorial_pass_with_practical_criterion_added`.

## P20 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Проблемы сначала сформулированы | PASS | Диагностика P20 записана в degradation/duplication audit. |
| Standalone-вход усилен | PASS | Контрактный раздел переставлен после минимального примера. |
| Boundary-функция сохранена | PASS | Содержимое границ BMAD не удалено и не сглажено. |
| Фактура и визуальные решения сохранены | PASS | Источники, ссылки, фигуры и очередь внешних изображений не менялись. |
| Companion-файлы синхронизированы | PASS | Все обязательные companion-файлы обновлены для P20. |

## Текущая готовность после P20

`ready_for_third_editorial_pass_with_boundary_section_repositioned`.

## P21 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Проблемы сначала сформулированы | PASS | Диагностика P21 записана в degradation/duplication audit. |
| Переход после контракта улучшен | PASS | Добавлен мост от сравнительных границ к устройству метода. |
| Заголовки уточнены | PASS | Разделы про ревью, brownfield и расследование стали точнее. |
| Фактура сохранена | PASS | Технические детали, источники, visual queue и figure decisions не изменены. |
| Companion-файлы синхронизированы | PASS | Все обязательные companion-файлы обновлены для P21. |

## Текущая готовность после P21

`ready_for_structure_pass_with_editorial_sequence_stabilized`.

## P22 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Первый экран problem-first | PASS | Статья начинается с объекта, reader question, short answer and context-loss problem; boundary не стоит первым. |
| Порядок разделов сохранён | PASS | P20/P21 sequence оставлена: проблема → инвариант → пример → контракт → устройство метода. |
| Служебные captions убраны | PASS | `fig-bmad-workflow-map` получил публичную подпись. |
| Bottom asset-pass section проверен | PASS | Секция названа «Внешние изображения для asset-pass»; P12 executor-note удалён. |
| Companion-файлы синхронизированы | PASS | Все обязательные companion-файлы обновлены для P22. |

## Текущая готовность после P22

`ready_for_companion_sync_pass_with_public_structure_checked`.

## P23 — проверки приёмки

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Source usage синхронизирован | PASS | Строка Workflow Map соответствует текущей статье. |
| Image plan и external queue синхронизированы | PASS | Текущий статус `fig-bmad-workflow-map`: inline external placeholder с публичной подписью и незакрытым asset-pass. |
| Open questions очищены | PASS | Текущие живые блокеры вынесены наверх; устаревшие редакторские вопросы P19–P22 закрыты или понижены до истории. |
| Нет generic C5/A10 pending | PASS | Остались только конкретные проверки согласованности между статьями. |
| Синхронизация companion-файлов завершена | PASS | Все обязательные companion-файлы обновлены для P23. |

## Текущая готовность после P23

`ready_for_style_defect_audit_with_companions_synced`.

## P24 readiness checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Selective style audit completed | PASS | Исправлены реальные стилевые дефекты без тотального переписывания. |
| Content preservation | PASS | Фактура, источники, границы, figure IDs и asset queue не изменены. |
| Source labels preserved | PASS | Имена файлов, команд, BMAD labels и URLs сохранены. |
| Public-service notes absent | PASS | Повторная проверка не нашла `Здесь нужна`, `P12`, `executor` или `repair-note` в статье. |
| Required anchors preserved | PASS | `_bmad-output/planning-artifacts/`, `_bmad-output/implementation-artifacts/`, `{planning_artifacts}`, `{implementation_artifacts}`, `fig-bmad-workflow-map`, `fig-bmad-context-cascade`, `fig-bmad-sprint-state-machine` сохранены. |

## P25 readiness checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Selective natural rewrite completed | PASS | Исправлены только участки с реальными стилевыми дефектами. |
| Content preservation | PASS | Источники, фактические утверждения, границы, figure IDs и asset queue сохранены. |
| Calques reduced | PASS | `working source of truth`, «рабочая файловая рамка», «поверхности восстановления» и часть ритма `не X, а Y` заменены на естественные русские формулировки. |
| Source labels preserved | PASS | `story`, `Quick Flow`, `Workflow Map`, `project-context.md`, `sprint-status.yaml`, skill names, paths and URLs сохранены. |
| Required anchors preserved | PASS | `_bmad-output/planning-artifacts/`, `_bmad-output/implementation-artifacts/`, `{planning_artifacts}`, `{implementation_artifacts}`, `fig-bmad-workflow-map`, `fig-bmad-context-cascade`, `fig-bmad-sprint-state-machine` сохранены. |

## P26 readiness checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| Guarded final style completed | PASS | Тон, ритм и переходы выровнены без тотального rewrite. |
| Content preservation | PASS | Факты, ссылки, команды, числа, ограничения, границы и companion decisions сохранены. |
| Russian technical style | PASS | Убраны последние явные кальки и неестественные обороты; source labels сохранены по правилам. |
| Visual stability | PASS | Figure IDs, asset queue and bottom asset-pass section не менялись. |
| Required anchors preserved | PASS | `_bmad-output/planning-artifacts/`, `_bmad-output/implementation-artifacts/`, `{planning_artifacts}`, `{implementation_artifacts}`, `fig-bmad-workflow-map`, `fig-bmad-context-cascade`, `fig-bmad-sprint-state-machine` сохранены. |

## Final verification readiness checks

| Проверка | Статус | Заметки |
| --- | --- | --- |
| All target outputs exist | PASS | 9 target files present under `work/atlas/articles/`. |
| Main article is not a short overview | PASS | Article keeps source-specific commands, files, statuses, release caveats, failure modes, figures and asset-pass section. |
| Companion files support but do not replace article | PASS | `source_usage`, `source_transfer_ledger`, image companions, open questions, theory links and audit remain supporting files. |
| No hard coverage blocker | PASS | Real remaining debts are concrete: source freshness, Workflow Map asset-pass, bottom asset-pass section decision, table/figure density and cross-article consistency. |
| Visual asset handling | PASS | `fig-bmad-workflow-map` is inline as `external-real-candidate`, mirrored in bottom asset-pass section and external queue; synthetic figures do not replace it. |
| C5/A10 sync | PASS | Represented as concrete theory links/debts, not generic pending. |
| Public captions | PASS | No executor notes, local-file restoration text or service captions in article captions. |
| Style preservation | PASS | P24–P26 removed main pseudo-terms/calks while preserving technical detail. |
| Archive status | PASS | Completed archive can be produced. |

Final package status: `completed`.
