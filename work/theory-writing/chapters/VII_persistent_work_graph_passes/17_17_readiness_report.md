# P17 — readiness report и regression note

## Проверенный основной файл

Основной файл главы после финальной редакции:

```text
work/theory-writing/chapters/VII_persistent_work_graph_passes/16_16_final_revision.md
```

Объём после финальной сборки — около 57 тыс. знаков. Скрытый потолок объёма не применялся: глава расширялась там, где это требовалось для сохранения фактуры по `ready`, `claim`, `gate`, проверочным сигналам, `source state`, `prime` / restoration packet, runtime-boundary и graph hygiene.

## Что глава теперь объясняет

Глава удерживает собственную ось: длительную агентскую работу нельзя безопасно продолжать из одного summary или transcript. После нескольких сессий, CI, review, дочерних исследований и человеческих решений работа должна жить как долговечное состояние графа.

Основной сбой показан через сквозной billing/API пример: локальное `done` может быть честным на уровне отдельного исполнителя, но ложным на уровне общего изменения, если остаются открытыми blockers, gates, проверочные сигналы, source-state обновления или человеческие решения.

Финальная версия проводит читателя через следующие вопросы:

1. почему «почти готово» не является состоянием работы;
2. почему summary и transcript не отвечают на вопрос, что можно делать сейчас;
3. что хранит Persistent Work Graph;
4. как связи превращаются в готовность и право действия;
5. почему `gate` — это объект работы, а не туманное «ждём»;
6. почему CI, review, Greptile/Codex comments, traces and subagent outputs должны сначала вернуться в граф как typed state;
7. почему выводы стареют вместе с источниками;
8. что должен делать restoration packet;
9. чем PWG отличается от issue tracker, task graph, durable runtime, worktree and Gas Town;
10. почему сам граф требует cleanup and recovery;
11. как глава передаёт управление главе VIII: PWG показывает, где находится работа, а process profile выбирает способ действия.

## Структура после регрессионной проверки

Финальная структура соответствует P14:

- `Когда «почти готово» перестаёт быть состоянием работы`;
- `Локальное done и завершение изменения`;
- `Почему хорошая сводка всё равно не спасает`;
- `Что хранит Persistent Work Graph`;
- `Связи, готовность и право действия`;
- ``Gate`: ожидание как объект работы`;
- `Проверочный сигнал должен вернуться в граф`;
- ``Source state`: выводы стареют`;
- `Пакет восстановления: не пересказ прошлого, а рабочая форма следующей сессии`;
- `Что PWG не заменяет`;
- `Граф тоже может лгать`;
- `Где заканчивается глава VII`.

Главная структурная регрессия P13 — каталог самостоятельных мини-разделов — устранена. `Связи`, `готовность` and `claim` собраны в один вопрос: что можно делать сейчас и кто имеет право это делать. Проверочные сигналы и `subagent output` собраны в один механизм: signal → triage → graph state. Runtime/worktrees/current practice собраны в boundary-section, чтобы глава не подменяла IX или X.

## Источники, реально использованные в главе

### Внутренние источники

Сопутствующий `source_register.md` согласован с финальной главой. Реально использованы:

- `A4_persistent_work_graph_boundary.md` — summary/transcript/local done не являются рабочим состоянием;
- `B2_pwg_contribution.md` — work item, dependencies, readiness, owner/claim, gates, acceptance/check basis, source state, recovery;
- `C2_pwg_to_process_profiles.md` — финальный мост к главе VIII;
- `C3_pwg_to_evidence.md` — проверочные основания только в узкой мере, без преждевременного разворота главы XI/XII;
- `C4_execution_runtime_to_pwg.md` — runtime creates trace, but does not decide closure;
- `work/atlas/articles/persistent_work_graph.md` — каноническая опора главы;
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` — расширенная фактура;
- `work/atlas/articles/gas_town.md` and `GAS_TOWN_METHOD_DOSSIER.md` — только boundary, без захвата главы X.

### Story anchors

Истории используются не как каталог кейсов, а как разные проявления одного механизма:

- Jökull Sólberg — `/babysit-pr`, Fix / Dismiss / Escalate, PR as work object, CI/Greptile/Codex signal triage;
- Mark Erikson — read-only reviewer, DiffLoupe, `cachebro` / OpenCode source-state mismatch, observability angle;
- HumanLayer — research can be wrong, insufficient, superseded or accepted; context should be purposeful and progressively disclosed;
- Mae Capozzi — PRs, Linear tickets, traces, spans and dependency-review comments become useful only after classification.

### Внешние источники

Финальная глава реально опирается на источники из `source_register.md`:

- Beads docs/repo/core/ready/dep/blocked/gate/prime/coordination/recovery/architecture/troubleshooting;
- GitHub Issues and GitHub CLI issue dependencies;
- Linear issue relations;
- Task Master task structure and clusters;
- Jökull `/babysit-pr` and Claude Code usage;
- HumanLayer “Skill Issue” and ACE FCA;
- Anthropic multi-agent research system;
- Mark Erikson blog/config/cachebro;
- Mae Capozzi workflow/dependency review/telemetry and Honeycomb Claude Code ROI;
- LangGraph persistence/interrupts, Temporal HITL, Pydantic AI durable execution integrations, DBOS;
- Git worktree, Claude Code worktree workflows, OpenAI Codex worktrees.

Источник Beads остаётся главным практическим якорем, но не превращается в предмет главы. GitHub/Linear/Task Master показывают нижний mainstream-слой. Durable runtime and worktrees используются только как boundary. Gas Town отложен до главы X.

## Визуальные решения

В финальной главе приняты три визуальных решения:

1. `fig-vii-summary-vs-work-graph` — синтетическая HTML table-figure, показывающая разницу между summary и состоянием графа.
2. `fig-vii-beads-task-graph-memory` — сохранённый локальный asset:

   ```text
   content/assets/theory-images/beads-task-graph-memory.svg
   ```

   Он сохранён именно как image asset, а не переписан в текстовую схему.
3. `fig-vii-signal-triage` — синтетическая HTML table-figure, показывающая signal → triage → graph state.

Реальные скриншоты HumanLayer/Mae/OpenAI/Gas Town осознанно отложены: они уводят в главы VI, IX, X or evidence chapters. Для VII достаточно одного source-backed visual anchor and two explanatory synthetic figures.

## Что осознанно отклонено или отложено

- Не раскрывать Beads как полный обзор CLI.
- Не превращать главу в runtime chapter: Temporal, LangGraph, Restate, DBOS and worktrees остаются boundary, не ядром.
- Не разворачивать Gas Town: это глава X.
- Не превращать проверочные сигналы в полноценную теорию evidence/authority: это later chapters.
- Не включать SKILL.nb, AEGIS, CodeCRDT, STORM: источники потенциально полезны, но расширяли бы главу в gates/security/shared-state research.
- Не заменять локальный SVG реальным текстовым рисунком.

## Согласованность с companion files

Проверены и оставлены согласованными:

```text
work/theory-writing/chapters/VII_persistent_work_graph_companion/source_register.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/fragment_usage.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/atlas_usage.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/dossier_gap_notes.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/external_discovery_log.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/story_anchors.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/figure_candidates.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/open_questions.md
work/theory-writing/chapters/VII_persistent_work_graph_companion/degradation_and_duplication_audit.md
```

Основная глава и companion files говорят об одной и той же композиции: Beads as anchor, Jökull/Mark/HumanLayer/Mae as signal/source-state examples, runtime/worktree as boundary, Gas Town deferred.

## Языковая и терминологическая проверка

После финальной сборки проведена дополнительная точечная проверка англо-русского клея. В основном тексте всё ещё оставлены source-native terms там, где их насильственный перевод ухудшил бы точность: `summary`, `transcript`, `issue tracker`, `work item`, `claim`, `gate`, `ready queue`, `source state`, `subagent`, `runtime`, `worktree`, `restoration packet`, `CI`, `PR`, `Fix / Dismiss / Escalate`.

Это не полностью «обрусенный» текст, но он соответствует инженерному стилю главы: русский ход мысли, английский — для точных технических имён, команд and source-native terms. Слово «свидетельство» не сделано центральным термином; предпочтены «проверочные сигналы», «проверочные основания», «основания закрытия», «состояние проверок».

## Оставшиеся вопросы

1. CSS сайта нужно проверить на двух table-figures: если таблицы плохо ведут себя на узкой ширине, их стоит заменить на list-card layout.
2. Путь к SVG нужно проверить после интеграции в реальную структуру сайта: сейчас он оставлен как относительный путь из chapter context.
3. В будущем glossary-pass должен решить, какие термины фиксировать как английские (`claim`, `gate`, `source state`, `restoration packet`), а какие сопровождать русскими пояснениями.
4. Если в следующих главах появится единая терминология для evidence/acceptance, можно точечно синхронизировать формулировки разделов о проверочных сигналах.

## Итоговая оценка готовности

Глава готова как финальный результат этого пакета. Она не выглядит как обзор Beads, не повторяет главу IX о runtime, не растворяется в Gas Town и не превращает evidence/authority в преждевременную центральную тему. Её собственная роль ясна: показать, где живёт работа между сессиями и почему `done` должно быть состоянием графа, а не последней фразой исполнителя.
