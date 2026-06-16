# P14 — структура и индивидуальность главы

## Диагноз после P13

Глава держит собственную ось: `summary` и transcript не дают состояния работы; локальное `done` может стать ложным завершением; нужен долговечный граф, где видны узлы, зависимости, `claims`, `gates`, проверочные сигналы, состояние источников и пакет восстановления для следующей сессии.

Но после активного добора и языковой переписи структура стала слишком дробной. В P13 почти каждый компонент PWG получил отдельный раздел: связи, готовность, `claim`, `gate`, сигнал, source state, prime, subagent output, runtime boundary, graph hygiene, current practice. Содержательно это верно, но возникает эффект каталога элементов. Читатель может почувствовать, что глава перечисляет свойства PWG, а не ведёт одну мысль.

Главная структурная правка: сгруппировать элементы не по названиям полей, а по вопросам продолжения работы.

- **Что вообще случилось с работой?** — вводный billing/API пример, локальное `done`, недостаточность summary/transcript.
- **Что нужно хранить, чтобы продолжать?** — work item, зависимости, готовность, `claim`, gate, проверочные сигналы, состояние источников.
- **Как это переносится в следующую сессию?** — `prime`, restoration packet, дочерние выводы, граница с runtime.
- **Почему и сам граф требует дисциплины?** — stale state, failed gates, stale claims, graph hygiene.
- **Куда это ведёт дальше?** — глава VIII выбирает способ действия, VII только показывает состояние.

## Что не должно захватить главу

### Beads

Beads остаётся главным практическим якорем, но не должен становиться предметом главы. В P13 Beads появляется в нескольких местах: граф задач, dependency types, `bd ready`, `bd blocked`, `bd gate`, `bd prime`, multi-agent coordination, recovery. Это допустимо, если каждый вход Beads отвечает на конкретный вопрос главы. Нельзя превращать эти места в обзор CLI.

Правило для финальной сборки: Beads упоминать как проверку формы — «такой механизм уже виден в текущей практике» — но не как нормативную реализацию PWG.

### Jökull / HumanLayer / Mark / Mae

Эти истории не должны стоять как четыре самостоятельных мини-кейса. Их лучше использовать в одном смысловом движении:

- Jökull показывает, что PR-сигналы нужно классифицировать, а не исполнять механически.
- Mark показывает, что review role and source/access state должны быть разделены и явны.
- HumanLayer показывает, что research output может быть неверным, недостаточным или superseded.
- Mae показывает, что artifact/traces/tickets/comments становятся полезны только после человеческой классификации.

Иными словами, все четыре истории работают на один тезис: внешний сигнал должен вернуться в граф как typed state.

### Runtime / worktrees

Граница с runtime нужна, но не должна стать маленькой главой IX внутри VII. В VII достаточно сказать: runtime может возобновить выполнение, worktree может изолировать записи, но только PWG отвечает, что это выполнение или эта ветка значит для работы.

## Новая рекомендуемая структура главы

### 1. Когда «почти готово» перестаёт быть состоянием работы

Оставить как в P13, но последнюю фразу сделать более резкой: «постоянный граф работы» нужен не как ещё одна память, а как форма текущего разрешённого состояния.

### 2. Локальное `done` и завершение изменения

Оставить отдельным разделом. Это центральный сбой главы, его нельзя растворять.

### 3. Почему хорошая сводка всё равно не спасает

Оставить. Вставить `fig-vii-summary-vs-work-graph`. После таблицы сократить отдельные абзацы про issue tracker and runtime до bridge-параграфов, чтобы не перегружать ранний ход главы. Детальный runtime boundary лучше оставить позже.

### 4. Что хранит Persistent Work Graph

Оставить. Включить Beads image. В конце раздела добавить не длинный перечень state transitions, а короткий смысловой вывод: поле в графе полезно только если меняет допустимое действие.

### 5. Связи, готовность и право действия

Слить три раздела P13:

- «Связь не всегда означает блокировку»;
- «Готовность как вычисляемое состояние»;
- «Claim: право продолжать и писать».

Причина: все три отвечают на один вопрос — «кто и что может делать сейчас?» Если держать их отдельными разделами, структура становится механическим списком полей. В слитом разделе движение будет естественным:

1. не всякая связь блокирует;
2. поэтому ready queue должна вычисляться из семантики связей;
3. если узел готов, право действия фиксируется через `claim`;
4. если `claim` завис, нужна передача или восстановление.

### 6. Gate: ожидание как объект работы

Оставить отдельным разделом. Gate — не просто одно из полей; это другой тип времени: работа может быть понятна, но заблокирована внешним событием или решением. Раздел важен как самостоятельный hinge.

### 7. Проверочные сигналы и дочерние выводы

Слить P13:

- «Проверочный сигнал не является приказом»;
- «Вывод subagent должен вернуться в граф».

Причина: subagent output — частный случай проверочного/исследовательского сигнала. Если делать отдельный раздел, глава начинает выглядеть как каталог источников: PR-review, subagents, runtime, telemetry. Лучше показать один механизм: signal → triage → graph state.

Внутри слитого раздела использовать Jökull as main story anchor, затем коротко Mark/HumanLayer/Mae as variations.

### 8. `Source state`: выводы стареют

Оставить отдельным разделом. Это не просто разновидность сигнала: source state отвечает на вопрос, актуален ли вообще источник, на котором строится вывод. Здесь особенно важен Erikson `cachebro` / OpenCode mismatch.

### 9. `Prime` и пакет восстановления

Оставить отдельным разделом, но переименовать в более русскую форму:

**Пакет восстановления: не пересказ прошлого, а рабочая форма следующей сессии**

`bd prime` оставить внутри как практический якорь.

### 10. Что PWG не заменяет

Слить boundary and current practice:

- issue trackers;
- Task Master / task graphs;
- runtime durable execution;
- worktrees;
- Gas Town as broader organizational layer.

Так этот материал перестанет выглядеть как отдельный каталог «как это видно в практике» и станет boundary-section: PWG рядом с этими слоями, но не равен им.

### 11. Граф тоже может лгать

Оставить отдельным разделом. Это сильный late-section: после объяснения механизма нужно показать, что структура не магична. Здесь хорошо держатся stale claims, rotten gates, wrong dependency semantics, stale source state and cleanup.

### 12. Где заканчивается глава VII

Оставить финальный мост к VIII. Он должен быть коротким и ясным: VII показывает, где находится работа; VIII выбирает способ действия.

## Переписанный структурный узел: связи + готовность + claim

Ниже готовая замена для трёх разделов P13. Её задача — убрать каталог полей и собрать один раздел вокруг вопроса «что можно делать сейчас?».

---

## Связи, готовность и право действия

Когда работа превращается в граф, первым соблазном становится связать всё со всем. Но связь сама по себе ещё не говорит, можно ли работать.

В billing/API примере есть несколько отношений:

```text
W-104 discovered-from W-101
W-104 blocks W-100 final closure
W-106 related-to W-104
W-107 blocked-by G-201
W-105 blocks W-100 final closure
W-101 parent-child W-100
```

Если система трактует все эти отношения как blockers, ready queue может опустеть без причины. W-106 связан с compatibility question, но его можно исследовать до человеческого решения: открыть failing scenario, посмотреть логи, проверить инфраструктурный сбой, воспроизвести test locally. А W-107 public API docs действительно заблокирован G-201, потому что финальное описание зависит от решения о поведении для старых клиентов.

Если система, наоборот, не различает жёсткие блокировки, агент может начать обновлять docs до принятого compatibility behavior или закрыть W-100 при открытом architecture boundary review.

Именно поэтому готовность должна вычисляться из семантики связей, а не из самого факта ребра. Узел готов, если он открыт, не удерживается чужим действующим `claim`, не заблокирован hard blockers, не ждёт gate, не опирается на явно устаревший source state and is not intentionally deferred.

В нашем примере рабочая поверхность может выглядеть так:

```text
Ready now:
  W-106 Fix or classify integration CI failure
    reason: open; blocks W-100; no human decision required to inspect failure

Partially actionable, not closable:
  W-104 Resolve legacy mobile payload compatibility
    allowed: prepare options, inspect code paths, add exploratory tests
    forbidden: finalize behavior before G-201

Not ready:
  W-107 Update public API docs
    blocked by G-201 compatibility decision

Not done:
  W-100 Add billingPlanId
    blocked by W-104, W-105, W-106 and gates G-201/G-202/G-203
```

Это уже не summary. Это ответ на вопрос: что можно делать сейчас, а что нельзя закрывать.

Beads даёт здесь хороший текущий якорь, но не потому, что все проекты должны использовать Beads. В документации Beads описан как Dolt-powered issue tracker for AI-supervised coding workflows; среди его базовых свойств названы dependency-aware execution, `bd ready`, multi-agent coordination and gates ([Beads documentation](https://gastownhall.github.io/beads/)). `bd ready` shows open issues with no active blockers, excludes states such as `in_progress`, `blocked`, `deferred`, `hooked`, and can atomically claim the first ready issue with `--claim` ([`bd ready`](https://gastownhall.github.io/beads/cli-reference/ready)). `bd dep` shows why relation semantics matter: dependency links can express more than one kind of relationship, including blocking and non-blocking relations ([`bd dep`](https://gastownhall.github.io/beads/cli-reference/dep)).

Но ready queue — только половина дела. Если узел готов, кто имеет право его брать?

Без `claim` два агента могут увидеть W-106 as ready, оба начать расследование, получить два несовместимых вывода и оба оставить «готово». С `claim` появляется другая опасность: stale claim. Сессия оборвалась, worktree удалён, агент ушёл, а узел всё ещё выглядит занятым. Поэтому `claim` должен быть восстанавливаемым состоянием, а не просто именем исполнителя:

```text
claim:
  owner: Agent A
  scope: W-100 implementation
  branch: feature/billing-plan-id@b12d44f
  worktree: /tmp/agent-a-feature-billing-plan-id
  last_seen: 2026-06-15 12:10
  state: probably stale; recover before editing
```

Beads multi-agent coordination показывает практические формы такого владения: work can be pinned to a specific agent, `bd hook` shows what is on an agent’s hook, sequential handoff closes/pins work for the next agent, fan-out/fan-in splits parts and then blocks merge on all parts, and conflict prevention includes file reservations and issue locking ([Beads Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination)). Для главы VII это важно не как набор команд, а как смысл: владение — часть состояния работы. Оно определяет, кто имеет право писать, кто должен передать, какие файлы нельзя трогать параллельно and how to recover a stuck action.

Передача работы переносит не настроение агента и не общий рассказ, а ограниченное право действия: входной снимок, созданные артефакты, открытые gate-условия, риски, последний валидный шаг и следующий допустимый ход.

---

## Переписанный структурный узел: сигналы + subagents

Ниже замена для двух разделов P13. Она удерживает истории Jökull, Mark, HumanLayer и Mae как разные проявления одного механизма.

---

## Проверочный сигнал должен вернуться в граф

Как только граф начинает хранить CI, review, subagent outputs and traces, появляется новый риск: система начинает механически выполнять каждый сигнал. Reviewer написал comment — агент чинит. Codex нашёл concern — агент меняет code. Greptile поднял observation — задача разрастается. Subagent предложил hypothesis — summary превращает её в truth.

У Jökull Sólberg этот риск хорошо виден в `/babysit-pr`, Claude Code skill for escorting a PR through CI, Greptile and Codex review ([“Babysitting PRs With Claude Code”](https://www.solberg.is/babysit-pr), [“How I Use Claude Code”](https://www.solberg.is/how-i-use-claude-code)). Процедура определяет current PR through `gh pr view`, waits for CI and Greptile, processes whichever source finishes first, runs `codex review --base main`, classifies feedback as Fix / Dismiss / Escalate, fixes valid items, runs lint, commits, pushes and repeats until a clean state or iteration limit. Критерий выхода — не «агент внёс правки», а CI green, no untriaged issues and PR ready to merge.

Маленькая классификация здесь важнее всей автоматизации:

- **Fix** — сигнал действителен, локальное исправление понятно, scope позволяет его сделать;
- **Dismiss** — сигнал неверен, основан на неправильной предпосылке или не относится к текущему изменению;
- **Escalate** — нужен человек: продуктовая граница, архитектурный выбор, риск за пределами scope.

В одном из примеров Jökull CI был зелёным, Greptile дал observation про operational behavior, который был dismissed, а Codex нашёл две реальные смысловые проблемы: текст интерфейса больше не соответствовал поведению, and unpublish→republish lifecycle left a tour in wrong state. После исправлений second pass был clean and auto-merge queued. Вывод не в том, что один reviewer лучше другого. Вывод в том, что signal must be triaged before it becomes action or closure.

<figure class="synthetic-figure" id="fig-vii-signal-triage">
  <figcaption>Проверочный сигнал сначала классифицируется, и только потом меняет граф работы.</figcaption>
  <table>
    <thead><tr><th>Сигнал</th><th>Возможное состояние в PWG</th><th>Что нельзя делать автоматически</th></tr></thead>
    <tbody>
      <tr><td>CI failed</td><td>blocker / flaky signal / infrastructure issue / new work item</td><td>закрывать общий work item</td></tr>
      <tr><td>Reviewer comment</td><td>fix / dismiss / escalate / gate</td><td>чинить как приказ без triage</td></tr>
      <tr><td>Subagent report</td><td>accepted / stale / insufficient / superseded</td><td>переносить как timeless truth</td></tr>
      <tr><td>Trace or screenshot</td><td>source artifact attached to node</td><td>считать наблюдение полным acceptance</td></tr>
    </tbody>
  </table>
</figure>

Mark Erikson’s setup gives the same principle from the reviewer side. Его OpenCode configuration includes DiffLoupe workflow for intent alignment and a read-only reviewer agent whose role is to analyze changed code, not edit it; the reviewer distinguishes must fix / should fix / consider and is explicitly denied edit permissions ([Mark Erikson, AI workflow setup](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/), [`markerikson/opencode-config-example`](https://github.com/markerikson/opencode-config-example)). Review output should first become typed graph state. Only then a process profile decides whether to fix, dismiss, escalate or close.

Subagent output belongs to the same family. Anthropic’s description of its multi-agent research system notes that each subagent needs objective, output format, guidance on tools and sources, and clear task boundaries; otherwise agents duplicate work, leave gaps or fail to find necessary information ([Anthropic, “How we built our multi-agent research system”](https://www.anthropic.com/engineering/multi-agent-research-system)). For chapter VII this is not an argument for more subagents. It is an argument for typed returns. A subagent’s result must say what it looked at, what it did not look at, what it claims, what remains uncertain and which work item should change.

HumanLayer’s BAML and parquet/Hadoop examples sharpen this point. In the BAML case, an initial research pass wrongly concluded that the codebase was correct; the pass was discarded and rerun with better steering. In the parquet/Hadoop failure, research did not go deep enough through dependency tree, so a plausible plan broke on deeper dependencies ([HumanLayer, “Skill Issue”](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)). Research therefore has state: accepted, rejected, stale, insufficient, blocking, superseded or converted into work.

Mae Capozzi’s platform work gives the artifact version of the same rule. Agent runs produce PRs, Linear tickets, traces, spans, test branches, GitHub Action comments or dependency-review summaries; then a human classifies diff, type errors, Honeycomb UI state, `/review` output or dependency recommendations before merge ([Mae Capozzi, “My AI Coding Workflow”](https://maecapozzi.com/blog/my-ai-coding-workflow), [“AI-Assisted Dependency Review”](https://maecapozzi.com/blog/using-conductor-for-dependabot-reviews)). Artifact is necessary because the human needs something inspectable. But artifact does not automatically mean acceptance.

PWG therefore needs not just `check passed/failed`, but signal state: untriaged, accepted, dismissed, escalated, stale, converted to work item, converted to gate. Проверочный сигнал — вход в состояние работы, а не приказ к немедленному действию.

---

## Переписанный boundary-section: что PWG не заменяет

В P13 разделы про runtime and current practice стоят отдельно. Лучше собрать их в один boundary-section, чтобы глава не превращалась в список соседних инструментов.

---

## Что PWG не заменяет

PWG не существует в пустоте. Вокруг него уже есть трекеры задач, task graphs, worktrees, durable runtimes, telemetry and larger multi-agent environments. Ошибка начинается тогда, когда один из этих слоёв принимают за весь граф работы.

Обычный issue tracker хорошо показывает, что обсуждается, кто назначен and which issues are blocked or related. GitHub and Linear already make hierarchy and blocking relationships mainstream. Но tracker часто не знает, какой source state использовал subagent, какой CI run относится к текущему commit, какой review signal был dismissed, какой `claim` устарел после оборванной сессии and which restoration packet should be shown to the next actor.

Task Master and similar task graphs bring the structure closer to agentic execution. Tasks can carry dependencies, details, test strategy and execution clusters ([Task Master task structure](https://docs.task-master.dev/capabilities/task-structure), [Task Master clusters](https://tryhamster.com/docs/taskmaster/capabilities/clusters)). Но task graph без gate-условий, проверочного состояния, source state, recovery and ownership still remains a plan, not full work state.

Durable runtime решает другую проблему. Temporal, Restate and DBOS show how to preserve execution progress, avoid duplicated side effects and resume after failures ([Pydantic AI Temporal integration](https://pydantic.dev/docs/ai/integrations/durable_execution/temporal/), [Pydantic AI Restate integration](https://pydantic.dev/docs/ai/integrations/durable_execution/restate/), [DBOS Pydantic AI integration](https://docs.dbos.dev/integrations/pydantic-ai)). Runtime can say: workflow is waiting for approval. PWG must say: W-104 is blocked by G-201, final docs cannot be written yet, W-100 cannot close, and Agent B may prepare options but not decide.

Worktree isolates file writes and makes parallel diffs reviewable. But worktree does not know whether it is an experiment, a candidate patch, a discarded approach, a blocked branch, a stale claim or the accepted path ([Git worktree](https://git-scm.com/docs/git-worktree), [Claude Code common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows), [OpenAI Codex worktrees](https://developers.openai.com/codex/app/worktrees)). That semantic state belongs above the filesystem.

Gas Town is the larger organizational direction: more agents, roles, rigs, routing and visible coordination. Chapter X can expand it. Here the point is narrower: even inside a larger town, someone must know what a particular piece of work now permits. That is the PWG layer.

The chapter’s concept is therefore not invented in isolation. Beads is the closest single anchor: a Dolt-powered issue tracker designed for AI-supervised coding workflows, with dependency-aware execution, multi-agent coordination, gates and agent-readable commands ([Beads documentation](https://gastownhall.github.io/beads/), [Beads GitHub repository](https://github.com/gastownhall/beads)). GitHub and Linear show mainstream issue relations. Task Master shows AI-facing task topology. Durable execution systems show persistent runtime state. Jökull, HumanLayer, Mark and Mae show how checks, research, review and artifacts return to human/agent work.

These practices do not collapse into one product category. They point to one pressure: once agents work across sessions and systems, state must be externalized in a form that both humans and agents can inspect.

---

## Финальная индивидуальность главы

После этой структурной правки глава VII должна ощущаться не как «глава про Beads», не как «глава про durable execution» и не как «каталог текущих AI coding practices». Её собственная индивидуальность такая:

> Агентская работа перестаёт быть сессией и становится долгоживущим состоянием. Чтобы продолжать её честно, нужно знать не только что произошло, а что теперь разрешено, что запрещено, что ждёт решения, кто удерживает действие, какие сигналы уже классифицированы, какие источники устарели и какую рабочую картину получит следующая сессия.

Эту фразу стоит держать как внутренний критерий финальной сборки. Если какой-то источник, пример или подзаголовок не помогает этой мысли, его нужно либо сократить, либо перенести в соседнюю главу.
