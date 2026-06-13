# Post-Atlas Skeleton Improvement Plan

Статус: план улучшения, без правки самого Skeleton.  
Дата: 2026-06-13.  
Основание: завершённый concept-first Atlas из 10 статей, текущий `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`, `00_spine_map`, A/B/C-фрагменты, CORE writing plan, досье, theory-link companion files и последние решения по стилю / technical anchoring.

## 1. Короткий вывод

Значимые улучшения нужны. Текущий Skeleton не плохой: его главная линия уже совпадает с новой рамкой — агентская разработка меняет не только генерацию кода, а жизненный цикл программного изменения. Но Skeleton был написан до завершения Атласа и до последних решений о стиле, источниках и chapter packages. Поэтому его нужно не переписать с нуля, а перевести в post-atlas состояние.

Главная правка должна быть такой:

```text
Старый режим: skeleton → досье → будущий атлас → главы.
Новый режим: skeleton/00 → A/B/C-фрагменты → готовый Atlas → досье gap-check → external source discovery where needed → heavy chapter packages.
```

То есть Skeleton должен стать не планом будущего Атласа и не каталогом методологий, а управляющей картой для написания глав после Атласа.

## 2. Что уже работает и не должно быть сломано

Текущий Skeleton нужно сохранить в следующих опорах:

1. **Единица анализа — программное изменение, а не prompt.** Это правильная верхняя смена масштаба.
2. **Две оси: жизненный цикл изменения и рабочие субстраты.** Они остаются несущими, но их нужно сформулировать естественнее и связать с завершённым Атласом.
3. **Три deep anchors:** SPDD, Persistent Work Graph, Gas Town / Beads. Это по-прежнему правильная глубинная триада.
4. **ADR как защищённый профиль внутри слоя решения.** Его не надо делать четвёртым deep anchor, но после ADR-атласа он заслуживает более точной роли.
5. **Разделение stories / theory / atlas.** Истории остаются фактическим корпусом, теория — поперечным синтезом, Атлас — concept-first слой конкретных методов.
6. **A/B/C-фрагменты как существующий синтез.** Их нельзя выбрасывать ради нового плана; они должны стать материалом для глав.

## 3. Главные post-atlas изменения

### 3.1. Обновить статус Skeleton

Сейчас Skeleton говорит о техническом Атласе как о будущем слое. Это устарело.

Нужно обновить статус:

- Атлас завершён как baseline из 10 статей.
- Внешние ассеты ещё требуют отдельного общего asset-pass, но это не блокирует написание глав.
- Atlas articles теперь являются concept baseline для конкретных методологий и механизмов.
- Досье остаются source-backed quarry, но не являются первым слоем написания главы.

### 3.2. Обновить источник власти для глав

В Skeleton и CORE plan нужно явно зафиксировать новую иерархию:

```text
1. Skeleton / 00_spine_map — композиция, терминологическая ось, границы.
2. A/B/C-фрагменты — уже написанный синтез.
3. Atlas articles — concept-first baseline по методам и механизмам.
4. Dossiers — полный quarry, gap-check, failure modes, source details.
5. External sources — не только verification, но и content discovery там, где тема недоразработана.
6. Stories — практические якоря, не пересказ.
```

Самая важная поправка: внешние источники нельзя описывать только как подтверждение готовых тезисов и картинки. Для некоторых глав они должны давать само содержание: новые различения, документы, авторов, diagrams, empirical frames, контраргументы, vocabulary и дополнительные линии аргументации.

### 3.3. Добавить source discovery loop для глав

Для heavy chapter packages нужен отдельный контур:

```text
content gap map
→ external source discovery
→ source unfolding
→ integration decision
→ provenance/style integration
```

- `content gap map`: где глава пока держится на внутренней рамке слишком слабо.
- `external source discovery`: первичный поиск по этим лакунам.
- `source unfolding`: чтение найденного, переход по ссылкам, авторам, связанным терминам, диаграммам и репозиториям.
- `integration decision`: что входит в главу, что уходит в source register, что становится future debt.

Это не должно превращаться в бесконечный research loop. Но для глав IX, XI, XII, XIII и частично II/VI он, вероятно, обязателен.

### 3.4. Заменить “будущий технический атлас” на “Atlas baseline”

В Appendix/Technical Atlas section Skeleton сейчас ещё звучит как инструкция написать Атлас. Нужно заменить на:

- перечень 10 готовых atlas articles;
- правило, что теория не пересказывает их целиком;
- rule of use: atlas article is read before writing any chapter section that uses that concept;
- dossier gap-check after atlas read;
- asset-pass remains separate.

### 3.5. Закрепить актуальный стиль

В Skeleton / CORE plan нужно добавить post-atlas writing requirement:

```text
Все новые главы и вставки проходят текущий стиль-хвост:
language → repair/editorial → style defect audit → selective natural rewrite → guarded final human technical style.

Главный критерий — естественный русский технический текст. Не добавлять новые стилевые запреты без отдельной причины.
```

Важно не превратить это в новый чек-лист. Смысл: использовать принятый фильтр, но не зарегулировать текст.

## 4. Улучшения по частям Skeleton

### Введение

**Текущий статус:** верхний тезис правильный, но его нужно переписать в post-atlas формуле.

**Улучшение:** формулировать ось так:

```text
Агентская разработка меняет не только способ писать код. Она меняет жизненный цикл программного изменения: от формулировки намерения и границ задачи до устойчивого состояния работы, проверки результата, принятия решения, восстановления после сбоев и передачи контекста между сессиями, людьми и агентами.
```

**Что добавить:** короткое объяснение, что Атлас теперь даёт конкретные методы, а теория отвечает за поперечную ось.

### Часть I. Единица анализа: программное изменение, а не prompt

**Текущий статус:** сильная часть, но можно обновить язык 00/part I: убрать слишком сжатые выражения вроде `смысловая дельта`, если они звучат как псевдотермин.

**Улучшение:** говорить не “смысловая дельта”, а нормальной фразой: изменение, которое несёт намерение, ограничения, решение, проверку, ответственность и хвост сопровождения.

**Новые опоры из Атласа:** SPDD, Spec Kit, Kiro и BMAD хорошо показывают, что изменение начинается не с кода, а с состояния намерения / спецификации / story / задачи.

### Часть II. Реальная агентская сессия: трасса, вмешательство, выживание результата

**Текущий статус:** часть логически нужна, но после Атласа она должна сильнее готовить PWG, GSD/BMAD и evidence.

**Улучшение:** разделить:

- trace as observation;
- session as local execution context;
- durable state as separate requirement;
- what must survive compaction / handoff / interruption.

**External content discovery:** SWE-chat, Programming by Chat, How Coding Agents Fail, transcripts/agent traces should be treated as content sources, not just citations. Если эти источники дают классификации сбоев или форматы трасс, они должны войти в содержание главы.

### Часть III. Намерение, спецификация, контракт и архитектурное решение

**Текущий статус:** хороший каркас specification / contract / ADR. После ADR-атласа можно сделать его точнее.

**Улучшения:**

- сильнее развести ADR как memory of decision и contract/oracle как проверяемую границу поведения;
- встроить `Confirmation` как bridge к evidence, а не как второстепенную деталь MADR;
- добавить `Design Decision Gate` как пример: LLM может подготовить черновик/сигнал, но human completion сохраняет архитектурную власть;
- явно сказать, что generated/reconstructed ADR остаётся candidate evidence until accepted.

**Atlas donors:** `adr_method.md`, `spdd_method.md`, `spec_kit_method.md`, `constitutional_sdd.md`.

### Часть IV. SPDD как спецификационный жизненный цикл

**Текущий статус:** Skeleton уже содержит правильный набор тем, но post-atlas SPDD стал богаче и естественнее.

**Улучшения:**

- добавить три человеческих навыка SPDD: `Abstraction First`, `Alignment`, `Iterative Review`;
- оставить billing example с числами как technical anchor;
- добавить `/spdd-reverse` как обратный вход для legacy-кода, но с оговоркой: это candidate Canvas, not true original intent;
- подчеркнуть, что SPDD не просто “лучше промптить”, а управляет границами свободы модели;
- не переносить в теорию все команды OpenSPDD: детали остаются в Атласе.

### Часть V. Защищённые спецификационные профили

**Текущий статус:** Skeleton уже перечисляет Spec Kit, Kiro, TDAD, Constitutional SDD, но часть деталей предатласная.

**Улучшения:**

- заменить подробный каталог профилей на сравнительный синтез объектов управления:
  - Spec Kit — feature lifecycle through `specify/clarify/plan/tasks/analyze/implement` and constitution;
  - Kiro — IDE/product-native spec state: Feature Specs, Bugfix Specs, Quick Plan, Analyze Requirements, tasks and supervised execution;
  - TDAD — two different meanings of tests: behavior definition vs regression routing;
  - CSDD — Constitution as higher-authority specification layer, traceability matrix, human/security checkpoints.
- в каждом профиле оставить только то, что нужно для теории; все file/command details живут в Атласе.
- добавить warning: protected profile не означает equal depth in main theory chapter. Атлас уже держит подробность.

### Часть VI. Контекст и рабочее состояние: проект как интерфейс агента

**Текущий статус:** часть нужна как мост к PWG, но сейчас она может остаться слишком общей.

**Улучшения:**

- использовать Kiro, GSD, BMAD, Spec Kit as examples of project context becoming state-bearing surfaces;
- показать разницу между context file, skill, rule, steering, story, state file and work graph;
- добавить проблему provenance of behavior: если агент получает rule/skill/config/preset, нужно понимать, откуда взялось поведение.

**External source discovery:** Codex/Claude docs on AGENTS/skills/hooks/MCP/subagents and Kiro/BMAD/GSD docs may provide content, not just citations.

### Часть VII. Persistent Work Graph

**Текущий статус:** одна из самых сильных частей Skeleton. После patched PWG article нужны точечные усиления.

**Улучшения:**

- добавить `bd ready` / `bd blocked` as concrete but not dominating anchors;
- gate should have four minimal fields: blocked transition, unblocker, evidence after unblock, fallback on failure/timeout/manual override;
- `bd prime` / compact restart context should be included as a small anchor for rehydration;
- source-state transition should be aligned with patched article: `found → opened → read → used_in_main_text / used_in_source_register / candidate_image_only / rejected_with_reason / reopen_required`;
- подчеркнуть: this is not coverage bureaucracy; it is continuation state.

### Часть VIII. Защищённые процессные профили

**Текущий статус:** Skeleton describes GSD/BMAD at a high level; Atlas has made them much more concrete.

**Улучшения:**

- GSD should be described as process-runtime profile, not just lightweight context cycle: `.planning/`, `gsd-core`, `gsd-pi`, routing, tool/model/security policy, phase state, verification and recovery.
- BMAD should include real anchors: `story`, `sprint-status.yaml`, checkpoint preview, `bmad-correct-course`, brownfield mode, retrospective/investigation.
- Do not import full GSD/BMAD articles into the chapter. Use them to sharpen the comparison: process profile vs PWG vs Gas Town.
- Reversa/OpenSpec/AgentSPEX should be marked as optional/light neighbors unless new external discovery confirms they are needed.

### Часть IX. Исполнение: среда агента, harness, tools, permissions

**Текущий статус:** likely underdeveloped relative to future theory. Skeleton lists correct categories, but chapter will need content discovery.

**Улучшения:**

- make four layers explicit:
  - execution boundary / sandbox / worktree / permissions;
  - tool and observation surface;
  - workflow runtime / durable execution;
  - platform agent / internal developer platform.
- strengthen link to PWG: runtime can execute a step; PWG stores work existence, gates and right to continue.
- use external source discovery for LangGraph/Temporal/DBOS/Restate/HumanLayer/Sandvault/Codex/Claude docs where current internal material is insufficient.

This chapter should not be written as a list of tools. Its real question: what makes agent action bounded, replayable, observable, resumable and accountable?

### Часть X. Gas Town / Beads

**Текущий статус:** Skeleton is good but should import post-atlas clarity.

**Улучшения:**

- roles as lifecycle functions, not funny names;
- two-tier Beads: coordination/town vs execution/rig;
- problem-state vocabulary: `Working`, `Stalled`, `Zombie`, `GUPP Violation`, `FIX_NEEDED`, `MERGE_FAILED`, `ORPHANED_WORK`;
- service agents as maintenance loops around parallel agents: Witness, Refinery, Deacon/Dogs;
- Gas Town gives organization, visibility and backpressure beyond PWG.

Avoid turning Part X into a tour of Gas Town UI/commands; that remains Atlas / Fieldbook.

### Часть XI. Свидетельства, тесты, ревью и качество доказательства

**Текущий статус:** structurally right, but should become more central and source-rich.

**Улучшения:**

- organize by promise type rather than by test-tool list:
  - behavior evidence;
  - boundary/contract evidence;
  - architectural confirmation;
  - security/governance traceability;
  - runtime/rollout evidence;
  - human/maintainer acceptance.
- use Atlas donors:
  - SPDD: `/spdd-api-test`, `/spdd-code-review`;
  - ADR: `Confirmation`, Pact/can-i-deploy, OAS diff, SLO/rollout signals;
  - TDAD: test as behavior spec vs regression route;
  - CSDD: traceability matrix and false confidence;
  - Kiro: property-based testing / requirements analysis;
  - GSD/BMAD: verify/checkpoint/review evidence.
- external source discovery needed for contract testing, architecture fitness, rollout, SLO/error-budget and replay/trace sources.

### Часть XII. Завершение, ответственность и внешний контур

**Текущий статус:** correct but probably needs external content.

**Улучшения:**

- make authority distinction central: right to act vs right to complete;
- integrate ADR status, CODEOWNERS, maintainer policies, open-source AI policies, platform-agent PR completion and human gates;
- avoid turning this into ethics chapter; keep it engineering/governance of acceptance.

**External source discovery:** SASE/open-source policies, CODEOWNERS, no-AI/limited-AI contribution policies, maintainer trust cost, security/sandbox policies.

### Часть XIII. Хвост жизненного цикла

**Текущий статус:** conceptually right but likely underdeveloped.

**Улучшения:**

- align with A9 and Atlas details:
  - SPDD `prompt-update/sync`;
  - ADR supersession / operational projection staleness;
  - CSDD Constitution update after incidents/regulatory changes;
  - Spec Kit/Kiro specs and tasks update after implementation;
  - GSD/BMAD state cleanup, retrospective and correct-course;
  - PWG cleanup: stale deps, obsolete gates, orphaned claims;
  - skills/rules/hooks/AGENTS updates.
- add external discovery for incident feedback, supply-chain/dependency inventory, SBOM, rules/skills update practices if the chapter needs content beyond internal sources.

### Заключение / Mode selection

**Текущий статус:** A10 is a strong fragment; Skeleton conclusion should use it more directly.

**Улучшения:**

- mode selection must not rank methods by sophistication;
- choose the minimum external structure that preserves intent, state, evidence, authority and repair;
- include signals that lighter mode is no longer enough;
- distinguish failure of under-structure from failure of over-process.

## 5. Proposed heavy chapter package model

The next chapter packages should not be lighter than Atlas packages. They are more complex because they synthesize multiple finished artifacts and may need new external content discovery.

Recommended package stages:

```text
P01 — read current discourse, WORKING_DOCUMENTS_MAP, Skeleton V4, 00_spine_map, CORE plan
P02 — section contract: what this chapter must prove and what it must not become
P03 — existing-fragment inventory: A/B/C fragments and current chapter-related fragments
P04 — atlas donor map: which Atlas articles are primary/secondary/control sources
P05 — dossier gap map: what important material exists in dossiers but not Atlas/fragments
P06 — content gap map: what the chapter lacks even after internal sources
P07 — external source discovery pass, if gaps exist
P08 — source unfolding pass: read found sources and follow important references/diagrams/repos
P09 — integration decision: what enters chapter, what stays in source register, what is future debt
P10 — first synthesis draft from skeleton/fragments/atlas/dossiers/sources
P11 — anti-catalog pass: remove method-by-method listing and rebuild around chapter argument
P12 — cross-article consistency pass against Atlas and 00_spine_map
P13 — source/provenance pass: primary sources for publication claims
P14 — chapter repair: structure, transitions, boundaries with neighbor chapters
P15 — language pass 1
P16 — language pass 2
P17 — style defect audit
P18 — selective natural rewrite
P19 — guarded final human technical style
P20 — regression check: no loss of critical distinctions, technical anchors, source obligations
Final — package article/fragment, companion files, source register, open questions, discourse/map updates
```

This is only a starting shape. Chapters with heavy external discovery may need more source passes; chapters mostly covered by Atlas/A/B/C may use fewer.

## 6. Files to update in the next real package

Do not edit Skeleton ad hoc. Build a dedicated package:

```text
POST_ATLAS_SPINE_AND_SKELETON_UPDATE
```

Target files:

```text
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
```

Possible companion files:

```text
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
work/theory-writing/reports/POST_ATLAS_SKELETON_ANTI_DEGRADATION_AUDIT.md
work/theory-writing/reports/POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md
```

V4 should remain as historical baseline. V5 should be created as a new file unless the user explicitly chooses in-place replacement.

## 7. Anti-degradation checks for Skeleton V5

Before accepting V5, check:

1. Does it keep the lifecycle-of-change axis?
2. Does it avoid becoming an Atlas table of contents?
3. Does it use Atlas as concept baseline without copying every article?
4. Does it keep A/B/C fragments as existing synthesis, not discard them?
5. Does it include dossier gap-check without restoring hard coverage bureaucracy?
6. Does it include external source discovery for underdeveloped chapters?
7. Does it preserve deep anchors: SPDD, PWG, Gas Town?
8. Does it preserve ADR as protected decision-memory profile?
9. Does it keep natural Russian style and avoid pseudo-term compression?
10. Does it make chapter packages heavy enough for synthesis rather than lightweight summary?

## 8. What not to do

- Do not start writing chapters before the post-atlas skeleton/spine reconciliation.
- Do not reopen Atlas article plans or style protocol now.
- Do not make dossiers the main direct drafting source; use them for gap-check and source restoration.
- Do not reduce chapter packages to 12-pass lightweight summaries.
- Do not make external sources merely citation/asset confirmation; some chapters need content discovery.
- Do not let source discovery become unbounded research. It must be tied to explicit content gaps.
- Do not remove the distinction between theory, Atlas, Handbook and Fieldbook.

## 9. Recommended next action

Build and execute a dedicated `POST_ATLAS_SPINE_AND_SKELETON_UPDATE` package. Its result should not be a full theory chapter. It should produce:

1. updated `00_spine_map`;
2. new `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md`;
3. updated `CORE_NODES_WRITING_PLAN.md`;
4. updated `WORKING_DOCUMENTS_MAP.md`;
5. source routing map for future chapters;
6. external discovery needs map;
7. heavy chapter package blueprint.

After that, start chapter packages from the updated Skeleton V5, not from the old V4.3-PWG Skeleton.
