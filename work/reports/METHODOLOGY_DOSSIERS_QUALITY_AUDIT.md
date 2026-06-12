# Methodology dossiers quality audit

Дата: 2026-06-08
Статус: repaired audit after re-running Stage 0.19 with dossier-as-source-consolidation understanding.

Verdict: PASS WITH RESIDUAL EXTRACTION QUEUE.

## Что проверялось

Этот audit не засчитывает простое наличие headings. Проверялись три вещи:

1. Является ли dossier большим рабочим source consolidation buffer, а не кратким profile.
2. Сохранены ли детали из external primary / official / research sources в объёме, полезном для future site writing.
3. Видны ли residual queues, где требуется ещё более глубокое file/table/example extraction before final prose.

## Таблица

| Methodology | Large consolidation buffer | Source-backed detail breadth | Source register repaired | Cycle transfer repaired | Image candidates retained | Verdict |
|---|---|---|---|---|---|---|
| Spec Kit | yes | good | yes | yes | yes | PASS WITH QUEUE |
| Kiro Specs | yes | good | yes | yes | yes | PASS WITH QUEUE |
| Constitutional SDD | yes | good for paper-level profile | yes | yes | yes | PASS WITH QUEUE |
| TDAD comparative | yes | good for paper-level contrast | yes | yes | yes | PASS WITH QUEUE |
| GSD / Open GSD | yes | good | yes | yes | yes | PASS WITH QUEUE |
| BMAD Method | yes | good | yes | yes | yes | PASS WITH QUEUE |

## Почему не plain PASS

Plain PASS would imply no meaningful residual extraction remains. That is too strong. The repaired dossiers are now useful source notebooks for drafting orientation and comparative sections, but several areas still deserve deeper extraction if the final chapter uses implementation-level details:

- Spec Kit: exact template files, example specs, command docs.
- Kiro: Bugfix Specs, Sync Files, hooks details, concrete EARS examples.
- Constitutional SDD: paper PDF tables/figures and exact evaluation setup before using detailed numbers.
- TDAD: repository examples, exact benchmark tables, graph construction details.
- GSD: individual command docs and configuration schema examples.
- BMAD: exact agent responsibilities and readiness-check wording.

## Corrected completion claim

The earlier Stage 0.19 completion claim was invalid because dossiers were short profiles. This repair changes the status: current dossiers are now source-consolidation notebooks with residual queues. Parts V and VII are ready for first drafting of protected-methodology sections, but final prose should still reopen residual queues when it needs exact implementation examples, tables or image assets.

## Gates that remain

- Visual pass: rights/stability check for image candidates.
- Research-number pass: exact PDF/table check before using quantitative claims from papers.
- No promotion of GSD/BMAD to deep anchors without human gate.
- No changes to approved plan or skeleton made in this repair.
