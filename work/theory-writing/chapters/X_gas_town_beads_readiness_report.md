# 17 — Readiness report и regression note

## Main chapter status

Основной итоговый текст текущего пакета: `16_16_final_revision.md`.

Размер: около 58 тыс. знаков. Скрытый потолок объёма не применялся. Текст не содержит внутренних комментариев рабочего процесса; figure blocks встроены как обычная часть главы.

## Что глава объясняет

Глава объясняет переход от долговечного состояния отдельной работы к обслуживаемому потоку многих агентских действий. Центральная формула удержана:

- persistent work graph / Beads дают durable work state;
- при множестве рабочих потоков этого недостаточно;
- проекту нужны маршруты, рабочие площадки, очереди, наблюдение lifecycle, recovery, backpressure, escalation и возвращение результатов в общее состояние;
- Gas Town/Beads дают видимый прототип такого слоя, но не являются зрелым универсальным стандартом;
- организация потока не доказывает качество результата, поэтому финал ведёт к главе XI о проверочном материале.

Сквозной пример `B-101`…`B-106` проходит через основные сбои главы:

- зависший claim;
- полезный вывод, не возвращённый в состояние;
- gate против преждевременной ready-готовности;
- `MERGE_FAILED` как управляемое состояние;
- backpressure;
- escalation к человеку.

## Реально использованные источники

### Gas Town / Beads

В основном тексте используются и inline-ссылаются:

- Gas Town README: общая рамка, `gt feed`, `gt feed --problems`, problem states;
- Beads Architecture: Dolt-backed storage/source of truth and limitations;
- Beads gate docs: human/timer/GitHub gates and `bd ready` blocking;
- Beads multi-agent coordination: `bd pin`, `bd hook`, handoff, fan-out/fan-in;
- `bd prime` docs;
- Beads routing docs;
- Beads Codex integration docs;
- Beads workflows/molecules docs;
- Gas Town architecture docs;
- Gas Town public docs;
- Mayor role template;
- Steve Yegge “Welcome to Gas Town”;
- Gas Town polecat lifecycle patrol;
- Gas Town glossary;
- Gas Town scheduler docs;
- Gas Town escalation docs.

Companion `source_register.md` согласован с этим набором.

### Supporting stories

В основном тексте используются direct external links:

- Jökull Sólberg — “Babysitting PRs With Claude Code” and “How I Use Claude Code”;
- Stripe Minions / ChatPRD article and workflow page;
- Shopify “Introducing Roast” and `Shopify/roast` README;
- Mae Capozzi article.

Story anchors reflected in `story_anchors.md`. Supporting stories are intentionally short and do not become second centers of the chapter.

## Визуальные решения

В `16_16_final_revision.md` включены две фигуры:

1. `fig-x-pressure-mechanism-stack` → `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg`.
2. `fig-x-two-tier-beads-flow` → `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg`.

Deferred/rejected:

- `gastown-basic-workflow.svg` — optional, not inserted;
- `gastown-worker-roles.svg` — deferred to avoid glossary feel;
- `beads-task-graph-memory.svg` — deferred to avoid duplicating Chapter VII;
- Mae/Honeycomb images — deferred/rejected for X because Mae is supporting parallel, not visual center.

Caveat remains: final repository integration must verify `../assets/...` relative paths.

## Осознанно отклонено

- Broad market overview of multi-agent orchestration tools.
- HN/Reddit reception threads.
- Full Gas Town command/reference tour.
- Full Beads technical/admin deep dive.
- `MAIL_PROTOCOL` as central mechanism; lifecycle/patrol/escalation are stronger for this chapter.
- Long expansions of Jökull/Stripe/Roast/Mae.
- Third visual figure by default.

## Checks against neighboring chapters

### Against Chapter VII / PWG

Глава не повторяет PWG. Beads/PWG appear as lower layer; central topic is the next layer: servicing many work items.

### Against Chapter VIII / process profiles

Formulas/molecules/gates are mentioned, but not expanded into process-profile theory.

### Against Chapter IX / runtime

Hooks/Codex lifecycle are mentioned only as context-return mechanism; runtime/sandbox/tool rights are not retold.

### Against Chapter XI / evidence

The text explicitly distinguishes gates/flow state from proof of quality. It closes by saying Chapter XI must handle verification material.

## Language and style regression

- P13/P16 removed most protocol language from the main chapter.
- Remaining English terms are mostly tool/source-native: `bd prime`, `gt sling`, `hook`, `ready`, `merge`, `gate`, `rig`, `convoy`, `session`, `work item`.
- The phrase “flow service” was replaced in prose with “обслуживание потока”; English version remains only in companion/report context.
- No artificial “state_delta” or plan markers are present in the main text.
- The final text avoids presenting Gas Town as mature product; limitations and frontier caveat are included.

## Companion files consistency

All required companion files exist:

- `source_register.md`
- `fragment_usage.md`
- `atlas_usage.md`
- `dossier_gap_notes.md`
- `external_discovery_log.md`
- `story_anchors.md`
- `figure_candidates.md`
- `open_questions.md`
- `degradation_and_duplication_audit.md`

They reflect the actual P16 text plus remaining integration caveats.

## Remaining questions

1. Verify final figure paths once the chapter is moved to its repository location.
2. Decide whether the final canonical output should be `16_16_final_revision.md` directly or copied to a chapter path in `work/result/` / repository overlay by the package’s final pass.
3. If a future editor expands `gt mail` or `gt prime`, add direct source links at the exact expansion point.
4. If a future editor adds the optional basic workflow figure, re-check visual load.

## Regression note

No major degradation detected after P16. The strongest remaining risk is density in the Gas Town section: it contains many source-native terms. P14’s lifecycle framing was integrated, so the section no longer reads as a pure glossary, but future edits should avoid adding more role/command detail unless tied to the `B-101`…`B-106` example.
