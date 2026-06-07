# Comparative deep case candidates

Дата: 2026-06-07  
Статус: рабочий аудит сравнительных пар/троек перед skeleton v4.

## Почему этот файл нужен

Пользователь предложил важную мысль: возможно, некоторые большие кейсы лучше раскрывать не по одному, а через сравнение или противопоставление. Это может быть сильнее и нешаблоннее, чем “один кейс — одна глава”. Этот документ проверяет, какие пары/тройки у нас есть и какие из них подходят для deep comparative treatment.

## Критерии

Сравнительная глава/подглава возможна, если:

1. Cases answer the same lifecycle problem in different ways.
2. У каждого есть достаточно primary-source texture.
3. Сравнение раскрывает механизм, а не просто делает таблицу.
4. It reduces catalog risk.
5. It does not demote SPDD/Gas Town or break approved structure.

## Candidate 1: SPDD / Spec Kit / Kiro

### Lifecycle problem

Как намерение становится управляемым спецификационным контуром.

### Contrast

- **SPDD** — методологический closed loop: story → analysis → REASONS Canvas → generate → API test → review → prompt update → sync.
- **Spec Kit** — portable/executable toolkit: constitution, specify, plan, tasks, implement, templates, scripts, integrations.
- **Kiro** — productized IDE surface: requirements/design/tasks, task execution, `#spec`, Sync Files, review gates.

### Strength

Very strong. This is already Part IV–V. The comparison should be present, but not as one merged chapter, because SPDD needs standalone depth.

### Recommendation

Use as Part V framing after SPDD. Not a new separate deep comparison.

## Candidate 2: Two TDADs

### Lifecycle problem

Когда tests become a way to specify or guide agent behavior.

### Contrast

- **Test-Driven AI Agent Definition** — behavior of the agent itself becomes tested/compiled prompt artifact.
- **Test-Driven Agentic Development** — code-test impact graph becomes agent skill for reducing regressions.

### Strength

Strong and necessary. This is a perfect small comparative subsection.

### Recommendation

Use inside Part V and return briefly in Part X.

## Candidate 3: GSD / BMAD / Spec Kit / Reversa

### Lifecycle problem

Когда процесс становится устанавливаемым артефактом.

### Contrast

- **GSD** — lightweight context/process continuity: externalized state, fresh context, verify step.
- **BMAD** — role-based guided process: specialized agents, planning/architecture/implementation.
- **Spec Kit** — specification toolkit that touches process but remains specification-centered.
- **Reversa** — reverse direction: recover operational specs from legacy.

### Strength

Promising but not SPDD/Gas Town-level yet. Source depth for GSD/BMAD is enough for medium comparative section, not standalone deep anchor.

### Recommendation

Use as a medium-deep comparative section in Part VII:

```text
Когда процесс становится артефактом
```

Do not create a separate top-level part unless later dossiers show much richer primary-source detail.

## Candidate 4: Gas Town / GSD / BMAD

### Lifecycle problem

Как long-running agentic work becomes organized beyond one chat session.

### Contrast

- **GSD** — lightweight file/process discipline.
- **BMAD** — explicit roles and guided workflows.
- **Gas Town** — full organizational environment with roles, Beads, Mayor, service agents and orchestration cost.

### Strength

Very useful as a short bridge into Gas Town. It helps explain why Gas Town is deeper and more radical.

### Recommendation

Use before or inside Part IX introduction. Do not let GSD/BMAD steal Gas Town's role.

## Candidate 5: Harness Engineering / Sandvault / Codex-Copilot-Claude-Jules

### Lifecycle problem

How autonomy is bounded by environment.

### Contrast

- **Harness Engineering** — custom environment and feedback loops.
- **Sandvault / worktrees / sandbox** — bounded autonomy through isolation.
- **Codex/Copilot/Claude/Jules** — productized cloud/branch/PR/task environments.

### Strength

Good for Part VIII. This comparison can prevent tool catalog.

### Recommendation

Use as Part VIII internal structure:

```text
способность → граница → воспроизводимость → след
```

## Candidate 6: SWE-chat / Programming by Chat / How Coding Agents Fail

### Lifecycle problem

What real sessions reveal that demos hide.

### Contrast

- **SWE-chat** — trace of real coding-agent interactions.
- **Programming by Chat** — session archetypes and progressive specification.
- **How Coding Agents Fail** — misalignment forms.

### Strength

Strong empirical anchor for Part II.

### Recommendation

Use Part II as empirical triangulation, not three separate case sections.

## Candidate 7: Architecture fitness / contract tests / test data

### Lifecycle problem

Why tests passing is not enough.

### Contrast

- **Architecture fitness** — preserves architectural qualities.
- **Contract tests** — preserve boundaries and compatibility.
- **Test data / oracle independence** — preserve proof quality.

### Strength

Very strong for Part X. This may be the best comparative subchapter after SPDD/Gas Town.

### Recommendation

Use as core of Part X, under governing question:

```text
Что именно должно быть доказано?
```

## Candidate 8: SASE / open-source policy cluster / CODEOWNERS

### Lifecycle problem

Who has right to complete the change.

### Contrast

- **SASE** — role/artifact map for agentic software engineering.
- **Open-source AI policy cluster** — external boundary and review burden.
- **CODEOWNERS / ownership map** — concrete ownership routing.

### Strength

Good for Part XI.

### Recommendation

Use as one coherent chapter line: operational agency vs completion right.

## Candidate 9: SBOM / provenance / agent trace / audit log

### Lifecycle problem

How to reconstruct what happened and why it is safe.

### Contrast

- **SBOM** — components/dependencies/licenses.
- **Provenance** — how artifact was produced.
- **Agent trace** — what the agent did.
- **Audit log** — governance record.

### Strength

Medium. Useful but should not become separate chapter.

### Recommendation

Use as support in Parts VIII/X/XII.

## Candidate 10: Incident/postmortem / stale ADR / context cleanup

### Lifecycle problem

How the tail teaches the environment.

### Contrast

- **Incident/postmortem** — failure teaches operations and process.
- **Stale ADR** — decision memory must be revisited.
- **Context cleanup** — agent instructions must be repaired.
- **Test data/architecture drift** — evidence infrastructure also decays.

### Strength

Good for Part XII.

### Recommendation

Use as lifecycle feedback, not ops handbook.

## Overall answer on GSD/BMAD

GSD/BMAD should **not** become standalone deep anchors now.

They should become a **medium-deep comparative section** in Part VII, probably under:

```text
Когда процесс становится устанавливаемым артефактом
```

They can be compared with Spec Kit and Gas Town:

```text
Spec Kit: specification toolkit
GSD: lightweight context/process loop
BMAD: role-based guided process
Gas Town: full organizational environment
```

This comparison is valuable and non-template, but only if it remains tied to the lifecycle question. It should not become a survey of methodologies.

## Best comparative structures to use in skeleton

1. Part V: SPDD → Spec Kit/Kiro/TDAD/Constitutional SDD.
2. Part VII: GSD/BMAD/Spec Kit/Reversa as process-artifact spectrum.
3. Part VIII: Harness/Sandvault/platform tools as bounded autonomy spectrum.
4. Part X: architecture fitness / contract tests / test data as evidence-beyond-tests.
5. Part XI: SASE / policies / CODEOWNERS as completion-right spectrum.
6. Part XII: incident / stale ADR / context cleanup as feedback spectrum.
