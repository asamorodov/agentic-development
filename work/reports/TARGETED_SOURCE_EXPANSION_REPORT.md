# Targeted source expansion report after Stage 0.5

Дата: 2026-06-07  
Режим: local snapshot → archive handoff overlay  
Статус: source expansion after Stage 0.5 coverage audit.

## Что было сделано

Для каждой выявленной слабой зоны выполнены три повторных поисковых этапа с разными формулировками:

1. Decision provenance / ADR / RFC / design rationale.
2. Agentic frameworks / GSD / BMAD / OpenSpec / Reversa.
3. Lifecycle tail / release / rollback / runbook / incident / changelog / deprecation.
4. Security provenance / threat model / audit log / SLSA / MCP.
5. Ownership / CODEOWNERS / ownership map / completion authority.

Файлы поисковых этапов лежат в:

```text
work/source-expansion/stage_0_6/
```

## Главные выводы

### Decision provenance

ADR/RFC/design rationale нужно добавить как cross-cutting layer. Это не часть specification zone в узком смысле. Specification говорит, что должно быть true; ADR фиксирует почему было принято решение and what trade-offs/consequences were accepted. LLM/ADR papers strengthen this because they show that decision records themselves can become agent-assisted artifacts and compliance/evidence targets.

### Agentic frameworks

Spec Kit already belongs to deep specification zone. GSD and BMAD are different: they are process/framework layer. They should receive medium-deep treatment after dossiers, but not automatically become deep anchors.

### Lifecycle tail

Part XII needs concrete artifacts: release plan, migration plan, rollback plan, runbook, incident report, postmortem, dependency/deprecation policy, changelog/release notes. Not all need depth, but their absence makes the lifecycle end too early.

### Security/provenance

Threat model, security review, audit log, provenance record and MCP/tool boundary should be explicit artifacts. They connect Part V (Constitutional SDD), Part VIII (environment/harness), Part XI (governance) and Part XII (maintenance/security tail).

### Ownership

CODEOWNERS/ownership map/review routing should concretize “right to completion”. Part XI should not leave completion right as abstract theory.

## Impact on previous Stage 0.5 reports

The previous Stage 0.5 reports remain valid. This source expansion strengthens them and adds search provenance. The plan patch recommendation should now be treated as more justified, not merely speculative.
