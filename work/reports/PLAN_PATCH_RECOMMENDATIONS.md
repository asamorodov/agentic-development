# Plan patch recommendations after Stage 0.5 coverage audit

Дата: 2026-06-07  
Режим: ChatGPT / локальный snapshot archive → archive handoff overlay  
Ветка-источник: `work/theory-ai-sdlc-rebuild`  
Статус: рекомендации к `work/approved-ai-sdlc-plan.md`. Этот файл не меняет approved plan напрямую.

## Короткий вывод

Approved AI-driven SDLC plan остаётся правильной master architecture. Его не нужно откатывать и не нужно заменять новой рамкой.

Но перед drafting глав нужно внести patch-level уточнения:

1. Добавить first-class слой SDLC artifacts.
2. Добавить decision provenance layer: ADR / RFC / design proposal.
3. Добавить process/framework layer: GSD, BMAD and related frameworks.
4. Усилить lifecycle tail: release, rollback, migration, runbook, incident/postmortem, changelog/dependency/deprecation.
5. Явно артикулировать security/provenance artifacts: threat model, security review, audit log, provenance record.
6. Не переписывать главы до human approval этих patch recommendations.

## Что нужно добавить перед drafting

### 1. Artifact taxonomy as cross-cutting lens

В Part I or Part III добавить короткий taxonomy block:

```text
prompt ≠ plan ≠ specification ≠ ADR ≠ RFC/design proposal ≠ handoff ≠ evidence package
```

Задача блока: показать, что AI-driven SDLC держится не только на стадиях и кейсах, но и на артефактах, которые сохраняют разные типы смысла.

### 2. ADR / decision record

Добавить ADR как medium-deep cross-cutting artifact:

- Part III: ADR as decision-provenance artifact, not specification.
- Part VI: ADR as durable project memory for agents and humans.
- Part XII: stale ADR / decision debt / revisiting decisions.
- Process layer: proposed ADRs for architecture changes.

ADR не требует отдельной top-level part, но требует явного места. Иначе теория будет сильна в “что сделать” and weak in “почему это решение принято”.

### 3. RFC / design proposal

Добавить RFC/design proposal как social/technical review artifact. Он отличается от ADR:

- RFC/design proposal: proposal before decision.
- ADR: accepted decision and consequences.
- Spec: desired behavior / constraints.
- Plan: path of execution.

### 4. Process/framework layer

Добавить в Part VII or bridge between VI/VII subsection:

```text
Agentic development frameworks: process as installed artifact
```

Содержательно:

- GSD — context engineering and fresh-context execution loop.
- BMAD — role-based agile AI-driven methodology.
- Spec Kit — bridge back to executable specification toolkit.
- Reversa / OpenSpec / Spec Kitty — short contrasts or source-map candidates.

Default recommendation: не создавать отдельную top-level part прямо сейчас. Сначала добавить medium-deep layer and dossiers. Отдельная part требует human gate.

### 5. Lifecycle-tail artifact cluster

Part XII нужно усилить не только источниками про debt/security, но и artifacts:

- release plan;
- migration plan;
- rollback plan;
- runbook;
- incident report;
- postmortem;
- dependency policy;
- deprecation policy;
- changelog / release notes.

Не все должны быть глубокими. Но их отсутствие делает AI-driven SDLC похожим на “до merge/review”, а не на полный lifecycle.

### 6. Security/provenance artifact cluster

Добавить cross-cutting security/provenance artifacts:

- threat model;
- security review;
- audit log;
- provenance record / agent action trace;
- MCP/tool boundary record if relevant.

Связать с:

- Constitutional SDD in Part V;
- environment/harness in Part VIII;
- governance in Part XI;
- tail in Part XII.

### 7. Ownership artifacts

Part XI должен получить concrete ownership artifacts:

- CODEOWNERS;
- ownership map;
- review ownership;
- escalation path;
- completion authority.

Это переводит “right to completion” from concept to project interface.

## Что можно handled as short mentions

- dependency policy;
- deprecation policy;
- changelog / release notes;
- incident report/postmortem, если не появится rich source material;
- OpenSpec / Agent Spec;
- Spec Kitty until primary source is found;
- V-Bounce and vendor ADLC sources as cautionary framing.

## Что should go to source map only for now

- Spec Kitty, пока нет primary source.
- News/market posts.
- Vendor claims without concrete mechanics.
- Any framework named by taxonomy but not supported by primary-source detail.
- OpenSpec if no stronger source is read.

## Что требует human decision gate

1. Создание новой top-level части для agentic frameworks.
2. Promotion of GSD or BMAD to deep anchor.
3. Demotion of Spec Kit/Kiro/TDAD/Constitutional SDD from deep treatment.
4. Any compression of SPDD or Gas Town.
5. Any change to baseline restore rule.
6. Any direct update to `work/approved-ai-sdlc-plan.md`.
7. Any large new source-search cycle.
8. Any attempt to start drafting before applying or rejecting this patch.

## Proposed concrete patch to approved plan

Do not apply automatically. If approved, update `work/approved-ai-sdlc-plan.md` roughly as follows.

### Add to section 0: fixed decisions

Add new subsection:

```text
0.9. SDLC artifacts are first-class objects

The rebuilt theory must track not only stages and cases, but artifacts that carry intent, context, decisions, evidence, release state and ownership. ADR/RFC, release/rollback/runbook and audit/provenance artifacts must be explicitly placed before drafting.
```

### Amend Part III

Add:

```text
Prompt, plan, spec, ADR, RFC/design proposal and handoff preserve different kinds of information. The rebuilt theory must not collapse them into one “document layer”.
```

### Amend Part VI

Add `research.md`, `plan.md`, handoff, progress log, ADR and GSD as examples of project-as-agent-interface.

### Amend Part VII

Add subsection:

```text
Agentic development frameworks: when process becomes an installed artifact
```

Include GSD and BMAD as medium-deep cases.

### Amend Part XI

Add CODEOWNERS / ownership map / escalation path as concrete artifacts of completion right.

### Amend Part XII

Add lifecycle-tail artifact cluster: release plan, migration plan, rollback plan, runbook, incident report, postmortem, dependency/deprecation policy, changelog.

## Recommended next files before drafting

If user approves this patch, create dossiers/notes:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_DOSSIER.md
work/dossiers/BMAD_DOSSIER.md
work/dossiers/REVERSA_NOTE.md
work/dossiers/LIFECYCLE_TAIL_ARTIFACTS_NOTE.md
work/dossiers/SECURITY_PROVENANCE_ARTIFACTS_NOTE.md
```

Then update approved plan and discourse.
