# Updated plan quality audit

Дата: 2026-06-07  
Проверяемый файл: `work/approved-ai-sdlc-plan.md` v4  
Статус: аудит после применения consolidated patch Stage 0.5–0.12.

## Verdict

**PASS WITH WATCHPOINTS.**

План v4 стал существенно сильнее и полнее, но требует аккуратного исполнения. Главный риск теперь не в пропуске источников, а в том, что при написании Parts VI–XII они могут распухнуть and снова создать ощущение каталога. В самом плане это осознано: добавлены guardrails, five artifact classes, controlled Part XII and selected dossiers.

## 1. Проверка верхней архитектуры

### Критерий

План должен сохранять AI-driven SDLC как master architecture and not revert to “map of currents”.

### Result

Pass.

План v4 сохраняет lifecycle:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

Новые артефакты не становятся верхней структурой. Они встроены как connective tissue across lifecycle stages.

### Watchpoint

При writing Part I must explicitly say why artifacts are included. If not, readers may still see list inflation.

## 2. Проверка deep anchors

### Критерий

SPDD and Gas Town must remain protected.

### Result

Pass.

SPDD remains Part IV. Gas Town remains Part IX. Baseline restore rule remains explicit.

### Watchpoint

New artifact layer must not be inserted into SPDD/Gas Town in a way that dilutes their internal mechanisms. SPDD should not become a general artifact taxonomy. Gas Town should not become platform-engineering example only.

## 3. Проверка specification zone

### Критерий

Spec Kit / Kiro / TDAD / Constitutional SDD must stay deep, not short contrasts.

### Result

Pass.

Part V remains deep. The plan explicitly prevents GSD/BMAD from being inserted into specification zone.

### Watchpoint

Part V is already heavy. Dossiers must help select the strongest details; otherwise it may become catalog-like inside one part.

## 4. Проверка artifact layer coherence

### Критерий

New artifacts must be grouped by function, not listed randomly.

### Result

Pass.

The five classes are coherent:

1. intent/decision;
2. task/project state;
3. execution constraints;
4. evidence/review;
5. completion/tail.

This is the main improvement over earlier patch.

### Watchpoint

The classes are still long. In prose, avoid tables unless needed. Use them as hidden structure, not reader-facing checklist everywhere.

## 5. Проверка Part X

### Критерий

Evidence layer must become richer than tests without becoming unbounded.

### Result

Pass with watchpoint.

Part X now has clear evidence package taxonomy and two named medium-high subsections:

- architecture quality as verifiable constraints;
- test data, test environment and oracle independence.

These are justified by sources and likely important.

### Watchpoint

Part X could become too large. Writing should use “change type determines evidence type” as governing thesis.

## 6. Проверка Part XII

### Критерий

Lifecycle tail must be concrete but controlled.

### Result

Pass with risk.

Part XII now has clusters rather than loose list: release/control, learning/repair, architecture/test tail, supply-chain/security, communication.

### Risk

This remains the highest overload risk. It must not become ops handbook. Most items should be short or linked to Handbook/Fieldbook.

## 7. Проверка process/framework layer

### Критерий

GSD/BMAD/Reversa/OpenSpec/AgentSPEX need place but not automatic deep status.

### Result

Pass.

Part VII includes them as medium process/framework layer and keeps human gate for promotion.

### Watchpoint

GSD/BMAD dossiers are important before writing Part VII. Without dossiers, the section may be shallow.

## 8. Проверка language/style

### Критерий

User-facing plan should not overuse English glue.

### Result

Pass with reservations.

Plan v4 is much more Russian than earlier Stage 0.5–0.8 reports, but still uses English terms for source/tool names and established workflow concepts. That is acceptable for plan, but final prose should be more consistently Russian.

### Watchpoint

Before final text, run language pass using `protocols/rules/language-style-rules.md`.

## 9. Проверка source grounding

### Критерий

Plan should reflect internal and external sources.

### Result

Pass.

The plan reflects:

- old site baseline;
- expanded quarry;
- cross-story synthesis;
- 12 stories;
- Stage 0.5–0.12 source expansion;
- accepted ADR-0007.

### Watchpoint

`work/theory-source-map-ai-driven-sdlc.md` has not yet been consolidated with all Stage 0.6–0.12 sources. Source expansion files contain the material, but the central source map is now behind.

Recommended later task:

```text
work/reports/SOURCE_MAP_CONSOLIDATION_PLAN.md
```

or directly update source map after dossiers.

## 10. Проверка next-step readiness

### Критерий

Plan should give actionable next step.

### Result

Pass.

Plan recommends selected dossiers/notes before skeleton/drafting.

### Recommended immediate next step

Create dossiers/notes:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_AND_TRACEABILITY_NOTE.md
work/dossiers/EXECUTION_CONTROL_SURFACES_NOTE.md
work/dossiers/ARCHITECTURE_QUALITY_AND_FITNESS_FUNCTIONS_NOTE.md
work/dossiers/TEST_DATA_ENVIRONMENTS_AND_ORACLES_NOTE.md
work/dossiers/EVIDENCE_PACKAGE_TAXONOMY_NOTE.md
work/dossiers/LIFECYCLE_TAIL_ARTIFACTS_NOTE.md
work/dossiers/OWNERSHIP_AND_COMPLETION_ARTIFACTS_NOTE.md
```

## Main residual risks

1. **Overload risk in Parts VI–XII.**  
   Mitigation: use governing thesis and artifact function, not exhaustive treatment.

2. **Part X may become too technical.**  
   Mitigation: organize by evidence need per change type.

3. **Part XII may become ops handbook.**  
   Mitigation: keep tail as lifecycle feedback, move practical recipes to Handbook.

4. **Source map lag.**  
   Mitigation: consolidate source map after dossiers, before final drafting.

5. **Language drift.**  
   Mitigation: run Russian language pass on any drafted prose.

## Final judgment

Plan v4 is suitable as active architecture for the next stage. It should not be broadened further before dossiers. The correct next step is not more broad source search, but selected dossiers/notes and skeleton v4.
