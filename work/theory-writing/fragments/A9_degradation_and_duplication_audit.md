# A9 degradation and duplication audit

## Цель pass

Проверить, не превратился ли `A9_lifecycle_repair.md` в энциклопедию устаревших артефактов или механический checklist. Feedback-loop pass должен был связать каждый repair target с источником обратной связи: review, failed verification, release, runtime/rollout evidence, incident, support/user signal, migration discovery or failed agent execution.

## Repair target audit

| Repair target | Feedback signal, который теперь явно назван | Статус после pass |
|---|---|---|
| Specification / PRD | implementation drift, review discovery, support/user report, product decision | Связан с issue #212 and paragraph about PRD status after signal. |
| ADR | decision drift, code/review conflict, proactive agent trigger, accepted ADR contradiction | Связан с Nygard/Fowler/AWS and Vercel `adr-skill`. |
| Operational projection | ADR supersession or active rule drift | Связан с ADR lifecycle paragraph; не вынесен в отдельный checklist. |
| Rule / skill / hook | repeated failure, failed agent execution, review finding | Усилен: rule repair should record signal that created it. |
| Product migration oracle | migration discovery, schema/API mismatch, QA/review signal | Усилен through Subramanian field report and Claude best practices. |
| Work graph | graph drift, blocked/ready mismatch, unresolved dependency, gate/evidence mismatch | Усилен through Beads dependencies/gate/prime/recovery/architecture. |
| Workspace state | parallel worktree leftovers, non-interactive run leftovers, branch/temp state ambiguity | Добавлен as physical execution-state tail through Claude Code worktrees. |
| Incident action items | incident, support/user signal, postmortem review | Связан with Google SRE postmortem culture. |
| Release evidence | contract matrix, canary metric, deployment record, inconclusive rollout | Связан with Pact and Argo. |

## Degradation risks checked

1. **Checklist drift.** Риск: раздел начинает перечислять документы, которые нужно обновить после merge. Исправление: добавлен opening paragraph and conclusion that start from feedback signal and then choose repair target.

2. **Over-broad cleanup.** Риск: work graph cleanup читается как “удалить хвосты”. Исправление: добавлен Beads recovery/caution layer; cleanup now distinguishes abandoned artifact, valid dependency, compatibility layer and evidence.

3. **Migration triumphalism.** Риск: Product Migration field report could be read as independent proof of success. Исправление: main text states it is an author field report, not public forensic proof; source usage and open questions preserve the same caveat.

4. **Rule accumulation.** Риск: failed execution automatically becomes permanent rule. Исправление: text says rule must have precise trigger and source signal; stale rule is treated as a failure mode.

5. **Evidence self-reference.** Риск: agent summary becomes proof of completion. Исправление: text now uses oracle provenance and external surfaces: tests, build, fixture diff, screenshot, schemas, reference implementation, API docs, CI, quality gates, rollout metrics.

## Duplication audit

- ADR lifecycle and Vercel `adr-skill` overlap but serve different roles: Nygard/Fowler/AWS establish lifecycle discipline; Vercel shows agent-readable implementation and post-acceptance mechanics. Keep both.
- Subramanian appears twice but with different functions: memory/rule learning loop and migration oracle/evidence pattern. Keep both, but avoid expanding outcome metrics further.
- Beads appears in graph state and recovery/cleanup. This is intentional: first explains persistent work graph, second prevents cleanup from becoming destructive deletion.
- Pact/Argo and Claude best practices all discuss evidence, but at different scales: release gate, rollout gate and session-level runnable check. Keep concise.

## Remaining watchpoints

- Final chapter should probably choose one primary visual loop and avoid using every candidate figure.
- If a later pass adds more sources, source usage should preserve the distinction between primary sources and internal navigation dossiers.
- If adding a public migration/outage case, require PR/CI/release/postmortem artifacts before treating it as forensic proof.

## Composition alignment pass

После выравнивания `A9_lifecycle_repair.md` больше не устроен как последовательный обход источников. Основной ход теперь держится на трёх вопросах:

1. какой feedback signal изменил рабочую правду;
2. какая поверхность будущей работы теперь стала подозрительно старой;
3. какое evidence, решение или состояние должно вернуться в следующий цикл.

Ссылки и фактура сохранены, но локальные подробности сведены к функциям в repair loop. Текст теперь лучше соответствует скелетону Части XIII: release feedback, incident feedback, stale specification, stale ADR, stale operational projection, stale rules/skills, stale work graph, work graph cleanup, migration tail and return-to-start представлены не как оглавление будущей главы, а как разные поверхности одного замыкания цикла.

## Что лучше держать в техническом атласе

- Детальные таблицы Claude Code hook events, exact schemas, event cadences and edge cases вроде nondeterministic `updatedInput` order.
- Полные Beads recovery sequences, конкретные команды диагностики и разрушительные режимы auto-fix.
- Расширенную матрицу migration oracle provenance: source, independence, scope, failure mode, retention.
- Tool-by-tool release engineering comparison beyond Pact/Argo; в теории достаточно contract matrix / rollout metric / deployment record как типов evidence.
- Source catalogue and screenshot candidates; основной фрагмент должен объяснять repair loop, а не превращаться в справочник tooling.

## Проверка после выравнивания

- **Checklist drift:** снижен. Финальный абзац возвращает все repair targets к feedback loop, а не к списку “что обновить после merge”.
- **Story retelling:** снижен. Product Migration, Matt Pocock skills, GSD/BMAD, Beads and release tooling используются как якоря механизма, без пересказа историй.
- **Source catalogue drift:** снижен, но watchpoint остаётся из-за высокой плотности ссылок. Если финальная глава будет длиннее, часть технических ссылок можно оставить в атласе, а в теории держать только representative anchors.
- **Atlas boundary:** усилена. Hook schemas, Beads runbooks, release tooling variants and oracle provenance tables отмечены как atlas material.

## Language protocol pass

В `A9_lifecycle_repair.md` убран английский связующий слой после композиционного прохода. Сохранены точные имена файлов, команд, источников, URL, инструментов и технических механизмов: `AGENT-BRIEF.md`, `/handoff`, `triage/SKILL.md`, `PreToolUse`, `PostToolUse`, `bd gate`, `bd prime`, `can-i-deploy`, `AnalysisTemplate`, `AnalysisRun` и аналогичные имена. Русифицированы связки вроде “repair target”, “feedback signal”, “source/depth pass”, “context goes to...”, “must decide whether...” и другие объяснительные фразы.

URL sanity check выполнен: 30 URL в основном фрагменте, кириллицы или не-ASCII символов в URL не найдено.

Оставшийся watchpoint: текст всё ещё сознательно оставляет ряд английских технических терминов (`skill`, `hook`, `gate`, `worktree`, `field report`, `oracle`, `evidence`, `drift`, `cutover`, `rollback`, exact role names), потому что они являются именами механизмов, команд, ролей или устоявшимися терминами источников. На финальном языковом проходе можно решить, какие из них перевести в общей терминологической карте.

## Second language precision pass

Повторная языковая проверка исправила гибриды, появившиеся после первого русифицирующего прохода:

- исправлены грамматические сбои после замен (`документация ... говорит`, `сторона хвоста миграции`, duplicate `решения решения`);
- переведены объяснительные связки вокруг ADR skill, triage, `write-a-skill`, Claude Code memory/hooks, migration oracle, Beads cleanup, GSD/BMAD and incident/release feedback;
- сохранено различие между рекомендательным контекстом (`CLAUDE.md`, auto memory, rules), повторяемой процедурой (`skill`) and принудительным контролем (`hook`, permission, test, external gate);
- точные имена команд, файлов, ролей, статусов и источников оставлены без русификации.

Повторная URL sanity check: 30 URL, кириллицы или не-ASCII символов в URL не найдено. Остаточные англоязычные термины считаются допустимыми техническими именами или source terms, но их можно централизованно проверить на финальном terminology pass.

## First style pass

Первый стилевой проход по `A9_lifecycle_repair.md` оставил прежнюю фактуру и ссылки, но снял часть интонации рабочего summary. Заголовок переведён на русский, opening и closing теперь звучат как связанный технический аргумент: merge меняет дерево, но будущая работа берёт контекст из спецификаций, ADR, правил, skills, hooks, graph state, gates и evidence.

Основные правки:

- ослаблены формулы вида “источник показывает X” там, где они звучали как пересказ каталога источников;
- заменены несколько декоративных или слишком резких образов (`активный закон`, `старый маршрут`, `мягкий хвост`) на более прямые инженерные формулировки;
- уточнены русские связки вокруг PRD status, ADR projection, memory/hook boundary, migration oracle, worktree cleanup, postmortem and release gates;
- сохранены source-specific детали: ADR statuses, `PreToolUse`/`PostToolUse`, `bd status`/`bd doctor`/`bd blocked`, `bd prime`, `can-i-deploy`, `AnalysisTemplate`, `AnalysisRun`, `manage-mr`, CI/SonarQube/fix-push-recheck, GSD/BMAD артефакты.

Проверка ссылок: 30 URL в основном фрагменте, не-ASCII символов в URL не найдено.

Остаточные watchpoints:

- В тексте сознательно оставлены английские имена механизмов и source terms (`skill`, `hook`, `gate`, `worktree`, `oracle`, `evidence`, `rollout`, `cutover`, `rollback`, `verification results`, `deployment records`). На финальном terminology pass можно решить, что переводить централизованно, а что оставить как имя механизма.
- Заключительный абзац всё ещё сжимает несколько feedback-paths в плотную связку. Это лучше прежнего checklist-формата, но при расширении главы его можно разнести на два абзаца.

## Second style pass

Второй стилевой проход проверил `A9_lifecycle_repair.md` как самостоятельный теоретический узел, а не как досье источников. Основной фрагмент получил дополнительные переходы между поверхностями ремонта: от PRD status к передаче состояния, от повторяющихся действий к правилам/skills/hooks, от миграционного хвоста к рабочему графу, от графа к процессу и от релизного сигнала к будущим условиям работы.

Истории оставлены как якоря. Product Migration не расширен до истории успешной миграции; в основном тексте он поддерживает только learning loop среды и migration oracle/evidence. Matt Pocock skills не развёрнуты в обзор репозитория; они работают как пример передачи состояния между PRD, brief, handoff and triage. Google SRE, Pact, Argo, GSD, BMAD, Beads and Claude Code worktrees удержаны как механизмы замыкания repair loop.

`A9_story_anchor_map.md` обновлён: добавлен блок ограничений второго стилевого прохода и уточнена роль Subramanian, Matt Pocock skills and incident/release/process anchors. `A9_figure_candidates.md` обновлён: Figure 1 зафиксирована как главный визуальный ход, Figure 3/4/6 — как боковые или authoring-варианты, Figure 5 — только для расширенного migration-tail разворота, Figure 7 — как точечная диаграмма для memory/skill/hook/gate boundary.

Проверка ссылок: в основном фрагменте 30 URL, в story anchor map 29 URL; не-ASCII символов в URL не найдено.

Остаточный риск: высокая плотность source-specific терминов всё ещё может создавать ощущение каталога. Сейчас это компенсировано переходами, но при финальной интеграции часть tool-specific деталей можно перенести в technical atlas или sidebars.

## Content repair pass

### Короткий план содержательной починки

1. Проверить, нет ли в `A9_lifecycle_repair.md` ссылок на внутренние досье, планы, отчёты или рабочие карты вместо публичных первоисточников.
2. Найти утверждения, которые звучат сильнее своих источников. Главный кандидат — Product Migration field report: он может поддерживать схему evidence/oracle, но не независимое доказательство результата миграции.
3. Проверить, не распадается ли фрагмент на пересказ источников после двух стилевых проходов. Исправлять только реальные провалы переходов, без расширения объёма.
4. Сверить source usage, story anchor map, figure candidates and open questions с текущей формой основного текста, чтобы рабочие файлы не закрепляли старые формулировки.
5. Не добавлять новые внешние источники без конкретного неподдержанного утверждения.

### Применённые изменения

- В основном фрагменте ослаблено утверждение о Subramanian Product Migration: источник теперь назван пригодным для схемы evidence/oracle surfaces, но не для независимого доказательства результата.
- Уточнена формулировка про Pact `can-i-deploy`: речь идёт о кодах завершения для решения deploy/no-deploy, а не о самостоятельных “deploy/no-deploy exit codes” как отдельном механизме.
- В `A9_source_usage.md` обновлены устаревшие формулировки про stale ADR, Subramanian field report, BMAD retrospective and Pact.
- В `A9_story_anchor_map.md` добавлена заметка, что истории остаются якорями и не расширяются в самостоятельные кейсы; Product Migration не используется как proof case.
- В `A9_figure_candidates.md` добавлена проверка поддержки фигур: неподдержанных фигур не найдено, но Figure 3/4/6 отмечены как потенциально возвращающие checklist/router-интонацию.
- В `A9_open_questions.md` добавлен статус content repair pass.

### Проверка источников

`A9_lifecycle_repair.md` не содержит ссылок на `work/`, `content/`, `dossiers/` или `reports/`. Все 30 URL в основном тексте ведут на публичные источники или официальную документацию; не-ASCII символов в URL не найдено. Новые внешние источники не добавлялись.

### Оставшиеся риски

- Высокая плотность tool-specific фактуры всё ещё может потребовать технического атласа или sidebar.
- Supply/security feedback остаётся открытым вопросом: без отдельного источникового прохода его лучше не добавлять в A9.
- Для incident/release chain всё ещё нет отдельного public case с PR/CI/release/postmortem цепочкой; текущий фрагмент опирается на структурные sources, а не на один forensic case.

## Residual repair pass

### План остаточной починки

1. Проверить повторяющиеся переходы вокруг specification → handoff, migration → oracle, oracle → work graph and release feedback.
2. Убрать мелкие языковые шероховатости, которые остались после content repair pass: `brief-формы`, слишком сухую связку “для хвоста миграции”, устаревшее phrasing в source/story/figure notes.
3. Не менять сильные различения: advisory memory vs enforceable hook/gate, field report vs forensic proof, logical graph cleanup vs physical workspace cleanup.
4. Проверить, не появились ли новые сомнительные ссылки или внутренние citation targets.
5. Не добавлять новые источники и не расширять фрагмент без фактической необходимости.

### Применённые изменения

- В `A9_lifecycle_repair.md` сглажена связка про Matt Pocock skills: вместо обещания “двух способов” теперь говорится о нескольких связанных практиках — `AGENT-BRIEF.md`, `/handoff` and `triage`.
- Миграционный переход стал менее оглавительным: “У миграции есть ещё один хвост...” вместо сухой отсылки к “другой детали того же отчёта”.
- Формулировка про Subramanian уточнена ещё раз: в A9 он полезен как источник схемы свидетельств, не как proof case.
- PWG-переход уточнён: системе нужна запрашиваемая запись состояния, а не просто текстовый отчёт.
- Release paragraph получил более ясный финал: oracle нужен, чтобы следующий цикл увидел причину признания изменения действительным или опасным.
- В `A9_source_usage.md`, `A9_story_anchor_map.md`, `A9_figure_candidates.md` and `A9_open_questions.md` обновлены остаточные notes после этой правки.

### Оставлено без изменения

- Высокая плотность точных source terms оставлена, потому что она сохраняет проверяемость claims and command/tool semantics.
- Figure 3/4/6 не удалены: они помечены как side/authoring candidates, а не как обязательные фигуры.
- Supply/security feedback не добавлен без отдельного source pass.
- Отдельный forensic incident/release case не добавлен без публичной цепочки PR/CI/release/postmortem.

### Проверка

В основном фрагменте осталось 30 URL, не-ASCII символов в URL не найдено. Ссылок на `work/`, `content/`, `dossiers/` или `reports/` в основном фрагменте нет.

## Composition / visual / style repair 2026-06-11

A9 was rechecked after the newer visual/style guardrails used for A3/A4/A6/A7/A8. The main defects were not source gaps but presentation regressions:

- seven inline figures made the fragment look like a router/checklist catalogue;
- the real Fowler/Thoughtworks image carried a service caption about asset recovery and local file path;
- several synthetic figures duplicated the same signal-to-repair routing logic;
- wording around “tail / checklist / stale map” made the text less human than the surrounding repaired fragments.

Applied actions:

- inline figures reduced from 7 to 4;
- `fig-a9-post-merge-repair-loop` kept as the only local image asset and given a public caption;
- `fig-a9-artifact-freshness-matrix`, `fig-a9-feedback-signal-router` and `fig-a9-repair-target-selected-by-signal` removed from inline and documented in `A9_figure_candidates.md` as deferred/merged/sidebar material;
- main text now uses direct Russian formulations for stale context, future work, cleanup and verification, while preserving source terms where they are names of mechanisms.

Regression check: A9 still performs its assigned role — repair loop after merge/release/incident/migration — and does not become a general cleanup handbook. It remains `ready_with_known_debts`: publication pass still needs final terminology and atlas/sidebar decisions.
