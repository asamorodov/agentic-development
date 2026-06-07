# Methodology dossier pass protocol

Дата: 2026-06-07  
Статус: обязательный task-local protocol для Codex Stage 0.19.  
Связанные решения:

- `work/decisions/ADR-0008-protected-methodology-profiles.md`
- `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`
- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`
- `work/approved-ai-sdlc-plan.md`

## 1. Назначение

Этот протокол задаёт, как Codex должен создавать dossiers для защищённых методологических профилей.

Главная цель: не допустить провала “mentioned but not understood”, когда важная методология вроде Spec Kit, Kiro, Constitutional SDD, GSD or BMAD формально упомянута в плане, но в финальном тексте остаётся мутным обзором на несколько страниц.

Protected methodology profile не обязан быть deep anchor уровня SPDD or Gas Town, но он обязан дать учебно полезное понимание методологии.

## 2. Protected methodology profiles

Codex должен создать dossiers для:

```text
Spec Kit
Kiro Specs
Constitutional SDD
TDAD: Test-Driven AI Agent Definition
TDAD: Test-Driven Agentic Development
GSD / Open GSD
BMAD Method
```

Выходные файлы:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/METHODOLOGY_DOSSIERS_QUALITY_AUDIT.md
```

## 3. Обязательные проходы для каждой методологии

Для каждой методологии Codex должен сделать не один “умный пересказ”, а несколько внешне видимых проходов.

Папки проходов:

```text
work/methodology-passes/spec-kit/
work/methodology-passes/kiro/
work/methodology-passes/constitutional-sdd/
work/methodology-passes/tdad/
work/methodology-passes/gsd/
work/methodology-passes/bmad/
```

В каждой папке:

```text
pass_01_source_inventory.md
pass_02_workflow_reconstruction.md
pass_03_artifact_and_gate_map.md
pass_04_missing_detail_pass.md
pass_05_comparative_pass.md
pass_06_anti_shallow_audit.md
```

### pass_01_source_inventory.md

Задача: найти и перечислить источники, которые реально использованы.

Обязательно разделить:

- primary / official sources;
- papers / research sources;
- existing internal notes;
- source-map references;
- sources not read or insufficient.

Не делать выводов без указания, на какой source family они опираются.

### pass_02_workflow_reconstruction.md

Задача: восстановить workflow методологии.

Для каждой методологии описать:

- вход;
- этапы;
- выходы;
- что создаёт человек;
- что делает агент;
- где возникает проверка;
- где workflow заканчивается or возвращается назад.

### pass_03_artifact_and_gate_map.md

Задача: составить карту артефактов and human gates.

Обязательно покрыть:

- artifacts created;
- context location;
- roles / agents;
- validation surfaces;
- lifecycle tail;
- human gates;
- what can be automated;
- what must remain human decision.

### pass_04_missing_detail_pass.md

Задача: перечитать источники and найти то, что не попало в первые проходы.

Формат:

```text
Detail found:
  source:
  why it matters:
  where to add:
  risk if omitted:
```

Если после прохода ничего не найдено, прямо написать why this is plausible, not just “nothing”.

### pass_05_comparative_pass.md

Задача: сравнить методологию с соседними.

Обязательные сравнения:

- Spec Kit ↔ SPDD ↔ Kiro;
- Constitutional SDD ↔ Spec Kit ↔ policy-as-code;
- TDAD A ↔ TDAD B;
- GSD ↔ BMAD ↔ Spec Kit ↔ Gas Town;
- GSD/BMAD ↔ current user's process in this repo, if relevant.

Не делать “кто лучше”. Сравнивать:

- central problem;
- central artifact;
- workflow shape;
- context model;
- human gate;
- validation;
- failure modes.

### pass_06_anti_shallow_audit.md

Задача: проверить, не стал ли dossier shallow overview.

Checklist:

- есть ли workflow;
- есть ли artifacts;
- есть ли human gates;
- есть ли validation;
- есть ли failure modes;
- есть ли lifecycle tail;
- есть ли contrast with neighbors;
- есть ли “what belongs in theory vs Handbook”;
- есть ли source-backed details, not just labels.

Вердикты:

```text
PASS
PASS WITH REPAIR
FAIL
```

При `FAIL` Codex должен repair dossier before moving on.

## 4. Финальный dossier для каждой методологии

Каждый dossier должен иметь структуру:

```text
# <Method> dossier

## Роль в AI-driven SDLC
## Проблема, которую решает
## Workflow
## Артефакты
## Где живёт контекст
## Роли / агенты / участники
## Human gates
## Проверка результата
## Lifecycle tail
## Сильные стороны
## Failure modes / overuse risks
## Отличие от соседних подходов
## Что должно попасть в теорию
## Что лучше уйдёт в Handbook / Fieldbook
## Open questions / human gates
```

## 5. Comparative synthesis reports

После individual dossiers Codex создаёт два synthesis files.

### SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md

Сравнить:

```text
SPDD
Spec Kit
Kiro Specs
TDAD A
TDAD B
Constitutional SDD
```

Главный вопрос:

```text
Каким способом намерение становится управляемым артефактом?
```

Формат не таблица first. Сначала — связный synthesis. Таблица допустима после.

### PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md

Сравнить:

```text
Spec Kit
GSD
BMAD
Reversa / OpenSpec / AgentSPEX
Gas Town
```

Главный вопрос:

```text
Когда процесс сам становится артефактом?
```

Особенно важно: GSD/BMAD не deep anchors, но protected profiles. Нужно объяснить, почему.

## 6. Что Codex не должен делать

Codex не должен:

- писать финальные главы;
- менять `work/approved-ai-sdlc-plan.md`;
- менять `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`, кроме отдельного proposed patch;
- демотировать protected methodology profile;
- решать, что dossier можно сжать;
- запускать широкий source search без human gate;
- переводить английские source names, если это ухудшает точность;
- писать объяснительный текст чрезмерно английским языком.

## 7. Языковые требования

Рабочие отчёты and dossiers пишутся по-русски.

Английским оставлять:

- точные названия источников;
- названия файлов;
- команды;
- имена инструментов;
- устойчивые названия методологий.

Не использовать английский как “клей”. Например:

- “слой рабочего процесса”, not `workflow layer`, если это не имя источника;
- “человеческое подтверждение”, not `human gate`, если gate is not used as project term;
- “глубина источника”, not `source depth`, если не таблица.

## 8. Quality gate before completion

Codex завершает Stage 0.19 только если существуют:

```text
work/methodology-passes/spec-kit/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
work/methodology-passes/kiro/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
work/methodology-passes/constitutional-sdd/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
work/methodology-passes/tdad/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
work/methodology-passes/gsd/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
work/methodology-passes/bmad/pass_01_source_inventory.md ... pass_06_anti_shallow_audit.md
```

and all final dossiers/synthesis reports/checks listed above.

If any part is incomplete, Codex must say so and not claim completion.
