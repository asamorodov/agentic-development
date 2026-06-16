# VII. Persistent Work Graph: состояние работы, которое переживает сессию

## Когда «почти готово» перестаёт быть состоянием работы

Представим обычное изменение в кодовой базе. Нужно добавить поле `billingPlanId` в endpoint смены подписки: обновить DTO, поправить валидацию, протянуть поле в billing service, добавить тесты и не сломать старых клиентов. Первая агентская сессия выглядит успешной. Поле добавлено, mapping написан, часть тестов проходит, PR открыт. В конце агент оставляет аккуратную сводку: реализация почти готова; остались совместимость старого клиента, integration CI и review.

Такой отчёт может быть честным. Но он ещё не является состоянием работы.

К моменту завершения сессии внутри изменения уже есть несколько разных линий. Старый mobile client может отправить payload без нового поля. Один `subagent` проверил историю API-контракта и нашёл прежнее обещание backward compatibility. Другой посмотрел проверки: unit run зелёный, а integration run падает на сценарии legacy payload. В PR открыт review thread: внутренний billing DTO, возможно, протекает в public API layer. Человек должен решить, будет ли strict validation или compatibility fallback. Target branch ушла вперёд. Ветка с изменением существует, но предыдущая сессия оставила `claim` на реализацию, и непонятно, жив он или завис после обрыва.

Если следующая сессия получит только summary, она увидит знакомую и опасную картину: «почти готово». Если она получит состояние работы, картина будет другой: одни узлы действительно закрыты, другие заблокированы, третьи ждут человеческого решения, четвёртые требуют повторного открытия источника, а один конкретный кусок можно безопасно взять прямо сейчас.

Именно здесь нужен слой, который нельзя заменить ни хорошим prompt, ни длинным transcript, ни обычным issue tracker, ни checkpoint’ом среды выполнения. Агентская работа живёт дольше одной сессии. Она проходит через CI, review, дочерние исследования, человеческие решения, смену веток, compaction, повторные запуски и частичную потерю контекста. Чтобы её можно было продолжить, проекту нужен не рассказ о прошлом, а долговечная форма текущего разрешённого состояния: где работа находится, что её блокирует, кто удерживает право действия, какие проверки относятся к актуальному источнику, чего ждём и что нужно показать следующей сессии.

Эту форму здесь удобно назвать **Persistent Work Graph**, или PWG: постоянный граф работы. Это не ещё одна память проекта. Это рабочая форма того, что теперь разрешено, запрещено, заблокировано, устарело, принято или требует восстановления.

## Локальное `done` и завершение изменения

Главный сбой, который делает этот слой необходимым, прост: локальное `done` начинает выглядеть как завершение всей работы.

Агент действительно мог закрыть локальный кусок. Он обновил DTO, добавил mapping, написал unit tests, получил зелёный unit run. Возможно, сделал commit и push. На уровне своей сессии он не обязательно ошибся. Проблема возникает тогда, когда система принимает локальный конец операции за конец изменения.

В примере с billing/API локально закрыты только несколько узлов:

```text
W-101  DTO and validation updated
W-102  billing service mapping updated
W-103  unit tests added and passed
```

Но общий work item ещё не закрыт:

```text
W-100  Add billingPlanId to change-plan endpoint
  blocked by W-104 legacy mobile compatibility
  blocked by W-105 architecture boundary review
  blocked by W-106 integration CI failure
  gated by G-201 human compatibility decision
  gated by G-202 review decision
  source state stale: target branch advanced
```

Это не педантизм. Если следующий агент закроет W-100 только потому, что patch выглядит готовым, проект получит ложное завершение. Документация может описать не то поведение, которое согласовал reviewer. Integration failure останется неразобранным. Комментарий по архитектурной границе потеряется. Вывод `subagent` может оказаться привязанным к старой версии документации. Человек, который должен принять compatibility decision, увидит уже «закрытое» изменение и будет вынужден заново восстанавливать, где именно случилась подмена.

Поэтому в агентской разработке `done` должно быть состоянием графа, а не самооценкой последнего исполнителя. Локальный результат может быть завершён. Общее изменение — нет.

## Почему хорошая сводка всё равно не спасает

Можно возразить: хорошая сводка ведь перечислит открытые вопросы. Например:

```text
Добавил billingPlanId в endpoint change-plan. DTO, validation и mapping обновлены, unit tests проходят. Нашёл edge case со старым mobile client; нужно решить compatibility. Integration CI падает на legacy payload scenario. Есть review comment по границе DTO. Следующей сессии надо разобраться с edge case, дождаться review и обновить docs.
```

Это неплохой текст. В нём нет явной лжи. Но он не отвечает на рабочие вопросы продолжения.

Можно ли следующей сессии прямо сейчас менять validation? Кто имеет право решить поведение для старых клиентов? Падение integration CI уже классифицировано или только замечено? Зелёный unit run относится к какому commit? Review по DTO boundary блокирует merge или это неблокирующее замечание? Public API docs можно обновлять сейчас или они зависят от человеческого решения? `Claim` предыдущей сессии ещё активен или его нужно восстанавливать? Что будет считаться закрытием W-100?

Summary хранит рассказ. Граф работы должен хранить продолжимость.

<figure class="synthetic-figure" id="fig-vii-summary-vs-work-graph">
  <figcaption>Одна и та же работа как summary и как состояние графа. Summary пересказывает прошлое; PWG показывает, что можно делать, что заблокировано и что нельзя закрывать.</figcaption>
  <table>
    <thead>
      <tr><th>Summary</th><th>Persistent Work Graph</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>«Реализация почти готова, остались compatibility, CI и review»</td>
        <td>W-100 открыт; W-101–W-103 закрыты локально; W-104/W-105/W-106 блокируют closure; G-201/G-202/G-203 открыты.</td>
      </tr>
      <tr>
        <td>«Unit tests проходят»</td>
        <td>`ci/unit/18452` success on `feature@b12d44f`; это не закрывает integration gate.</td>
      </tr>
      <tr>
        <td>«Нужно решить edge case»</td>
        <td>W-104 открыт; можно подготовить варианты; нельзя финализировать behavior до G-201.</td>
      </tr>
      <tr>
        <td>«Есть review comment»</td>
        <td>W-105 blocked by G-202; signal ещё не classified as fix/dismiss/escalate.</td>
      </tr>
      <tr>
        <td>«Следующей сессии продолжить»</td>
        <td>Agent A claim may be stale; recover branch/worktree before editing.</td>
      </tr>
    </tbody>
  </table>
</figure>

Transcript даёт больше материала, но не решает проблему. В стенограмме есть рассуждения, ложные старты, промежуточные идеи, команды, повторения, ошибочные гипотезы и устаревшие выводы. Чтобы продолжить работу из transcript, новая сессия сначала должна заново извлечь из прошлого актуальное состояние. В маленькой задаче это терпимо. В длинной агентской разработке это превращается в постоянный налог: новая сессия не продолжает работу, а сначала гадает, какие фразы из прошлого ещё являются обязательствами.

Issue tracker тоже не равен PWG, хотя современные трекеры уже приблизились к нужной форме. GitHub Issues поддерживает sub-issues и issue dependencies, а GitHub CLI вынес issue types, parent/sub-issue relationships и dependencies в terminal/JSON-поверхность, полезную для скриптов и coding agents ([GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues), [GitHub CLI changelog](https://github.blog/changelog/2026-06-10-github-cli-projects-issue-types-sub-issues-and-issue-dependencies/)). Linear поддерживает relations вроде blocking, related и duplicate и визуально показывает blocked/blocking issues ([Linear issue relations](https://linear.app/docs/issue-relations)). Это важная основа. Но обычная issue-карточка часто не знает, какой `source state` использовал `subagent`, какой CI run относится к текущему commit, какой review signal был отклонён, какой `claim` устарел после оборванной сессии и какой компактный restoration packet нужно дать следующему агенту.

Runtime checkpoint решает соседнюю, но другую задачу. LangGraph сохраняет состояние graph execution через checkpointers и stores и может останавливать выполнение через interrupts ([LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)). Temporal показывает durable human-in-the-loop flow, где workflow может ждать решения человека и затем продолжить выполнение ([Temporal human-in-the-loop](https://docs.temporal.io/ai-cookbook/human-in-the-loop-python)). Это важно для главы IX, но не заменяет PWG. Runtime может знать, что workflow ждёт approval. PWG должен знать, какой work item заблокирован этим approval, что нельзя закрывать до решения, какие варианты можно подготовить и какие проверочные основания должны пережить исполнителя.

## Что хранит Persistent Work Graph

PWG не обязан быть одним продуктом или одной базой данных. Это скорее контракт формы: какую долговечную рабочую информацию проект обязан хранить так, чтобы её могли читать люди, агенты, маршруты, hooks, review-процедуры и восстановительные сессии.

Минимальный узел PWG — это не строка «сделать X». Это объект работы с границей, статусом, зависимостями и основаниями продолжения:

```text
work item:
  id: W-100
  title: Add billingPlanId to change-plan endpoint
  boundary: DTO, validation, billing service mapping, tests, docs
  parent/child links: W-101..W-107
  blockers: W-104, W-105, W-106
  gates: G-201, G-202, G-203
  claim: Agent A / stale / recover before editing
  source state:
    base: main@8f31c2a
    branch: feature/billing-plan-id@b12d44f
    target: main@9c77b40 now ahead
    contract report: docs/api/subscriptions.md@8f31c2a
  check state:
    unit: success on feature@b12d44f
    integration: failed on feature@b12d44f
    review: boundary thread open
  restoration packet: available / refresh after rebase
```

У такого объекта есть история, но главное — не история. Главное — текущие допустимые переходы. Можно ли взять узел? Можно ли писать в файлы? Можно ли закрывать parent? Нужно ли ждать человека? Нужно ли перечитать источник? Нужно ли восстановить stale claim? Нужно ли превратить проверочный сигнал в новый work item?

Beads даёт самый близкий текущий якорь для этой формы. Документация описывает Beads как Dolt-powered issue tracker for AI-supervised coding workflows, где есть dependency-aware execution, multi-agent coordination, gates и команды, пригодные для агентов ([Beads documentation](https://gastownhall.github.io/beads/), [Beads GitHub repository](https://github.com/gastownhall/beads)). Визуально это хорошо видно в локальном рисунке из атласа: задача уже не один пункт TODO, а узел с зависимостями, памятью и состоянием.

<figure class="source-figure" id="fig-vii-beads-task-graph-memory">
  <img src="../../assets/theory-images/beads-task-graph-memory.svg" alt="Beads-style task graph with dependencies, local memory and agent-facing work state" />
  <figcaption>Практический образ PWG: задача становится частью долговечного графа с зависимостями, состоянием и памятью, из которой агент может восстановить рабочую картину. Рисунок сохранён как локальный asset, а не заменён текстовой схемой.</figcaption>
</figure>

Важный сдвиг здесь не в том, что «задач стало больше». Сдвиг в том, что состояние должно запрещать и разрешать действия. Поле полезно только тогда, когда оно меняет поведение следующего исполнителя. `Gate` запрещает closure. `Claim` запрещает чужую запись без передачи или восстановления. `Source state` требует перепроверки после rebase. Открытый review signal запрещает merge до классификации. Закрытый child work item не закрывает parent, если у parent остались блокирующие ребра.

Поэтому у PWG должны быть и запрещённые переходы. Нельзя перейти из `claimed` сразу в `accepted`, если gate-условия и проверочные основания не закрыты. Нельзя сделать blocked node `ready`, если блокирующая зависимость всё ещё открыта. Нельзя заменить `claim` другого исполнителя без передачи или события восстановления. Нельзя закрыть работу с источниками, если source state остался `found` или `read`, но не перешёл в `used`, `rejected_with_reason`, `stale` или другой явный статус.

Граф работы нужен не для красоты структуры. Он нужен, чтобы следующее действие было ограничено действительным состоянием проекта, а не уверенностью последней сессии.

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

Именно поэтому готовность должна вычисляться из семантики связей, а не из самого факта ребра. Узел готов, если он открыт, не удерживается чужим действующим `claim`, не заблокирован hard blockers, не ждёт gate, не опирается на явно устаревший source state и не отложен сознательно.

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

Beads снова полезен как проверка формы, а не как обязательная реализация. `bd ready` показывает открытые issues без активных blockers, исключает состояния вроде `in_progress`, `blocked`, `deferred`, `hooked` и может атомарно взять первый ready issue через `--claim` ([`bd ready`](https://gastownhall.github.io/beads/cli-reference/ready)). `bd dep` показывает, почему семантика связей важна: dependency links могут выражать разные отношения, включая блокирующие и неблокирующие ([`bd dep`](https://gastownhall.github.io/beads/cli-reference/dep)). `bd blocked` и recovery diagnostics важны для отрицательного случая: пустая ready queue может быть правильным результатом, но может означать и неправильные блокировки, зависшие зависимости или повреждённую рабочую картину ([`bd blocked`](https://gastownhall.github.io/beads/cli-reference/blocked), [Beads Recovery Overview](https://gastownhall.github.io/beads/recovery)).

Но ready queue — только половина дела. Если узел готов, кто имеет право его брать?

Без `claim` два агента могут увидеть W-106 как ready, оба начать расследование, получить два несовместимых вывода и оба оставить «готово». С `claim` появляется другая опасность: stale claim. Сессия оборвалась, worktree удалён, агент ушёл, а узел всё ещё выглядит занятым. Поэтому `claim` должен быть не только флажком владельца, но и восстанавливаемым состоянием: owner, scope, branch/worktree/session reference, last seen, heartbeat or expiry, release/transfer procedure.

В billing/API примере следующая сессия должна увидеть не просто «Agent A работал над W-100», а более точное состояние:

```text
claim:
  owner: Agent A
  scope: W-100 implementation
  branch: feature/billing-plan-id@b12d44f
  worktree: /tmp/agent-a-feature-billing-plan-id
  last_seen: 2026-06-15 12:10
  state: probably stale; recover before editing
```

Правильное продолжение начинается с восстановления: проверить branch, worktree, uncommitted changes, scope of claim, затем release or renew claim. Это не хозяйственная мелочь. Без этого работа либо дублируется, либо исчезает из ready set.

Beads multi-agent coordination даёт полезную практическую фактуру. В этой модели work can be pinned to a specific agent; `bd hook` показывает, что находится на hook конкретного агента; sequential handoff закрывает/прикрепляет работу к следующему агенту; fan-out/fan-in разбивает части и затем блокирует merge до завершения всех частей; conflict prevention включает file reservations и issue locking ([Beads Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination)). Для главы VII это важно не как набор команд, а как смысл: владение — часть состояния работы. Оно определяет, кто имеет право писать, кто должен передать, какие файлы нельзя трогать параллельно и как восстановить зависшее действие.

`Claim` поэтому лучше понимать как право продолжать, а не как имя исполнителя. Передача работы переносит не настроение агента и не общий рассказ, а ограниченное право действия: входной снимок, уже созданные артефакты, открытые gate-условия, риски, последний валидный шаг и следующий допустимый ход.

## `Gate`: ожидание как объект работы

Многие длинные задачи не готовы не потому, что никто не знает следующий шаг, а потому что они ждут внешнего события или решения. В summary это обычно записывается словами: «ждём review», «подождать CI», «надо спросить человека». В PWG это должно становиться gate.

`Gate` — это долговечное условие ожидания, которое влияет на готовность и закрытие work item.

В billing/API примере есть как минимум три gate:

```text
G-201 Human decision: strict validation or compatibility fallback
  type: human
  owner: Reviewer
  blocks: W-104, W-107, W-100 final closure

G-202 Architecture boundary review
  type: review
  source: PR#842/thread#boundary-dto-leak
  blocks: W-105, W-100 final closure

G-203 Integration CI run
  type: ci
  source: ci/integration/18453
  state: failed
  blocks: W-106, W-100 final closure
```

Эти gate-условия имеют разные последствия. Human decision нельзя закрыть implementation-agent’ом без явного полномочия. CI gate может пройти, упасть, быть отменённым или устареть после rebase. Review gate может завершиться принятием, отказом или превращением в новую работу. Если всё это хранится как «ждём», следующая сессия снова будет угадывать.

Beads `bd gate` описывает этот объект в полезной форме: gates — это асинхронные условия ожидания, блокирующие шаги workflow; среди типов есть `human`, `timer`, `gh:run`, `gh:pr` и `bead`; проверки могут закрывать gates, когда GitHub run succeeds, PR is merged, timer expires or target bead closes, а failures могут escalated ([`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate)). Важна именно последняя часть: gate resolution не всегда означает успех. Failed CI может создать W-106. Closed PR не равен merged PR. Timer expiry может означать timeout, а не approval. Human gate может завершиться strict validation, compatibility fallback или architectural redesign.

Temporal и LangGraph показывают runtime-сторону того же давления: workflow может остановиться на approval, прервать graph execution и затем продолжиться. Но gate в PWG отвечает на другой вопрос: какой work item заблокирован, какое условие его разблокирует, кто владеет решением, какие проверочные основания нужны и какие state transitions произойдут после решения.

В хорошо устроенном PWG gate не просто «лежит». Он должен иметь owner, source, blocked nodes, permitted preparatory work, expiry/escalation rule и closure semantics. Пока G-201 открыт, можно готовить compatibility options. Нельзя финализировать public docs. Пока G-203 failed, можно расследовать failure. Нельзя закрывать W-100. Если G-203 после rebase пройдёт, граф должен обновить не только сам gate, но и ready/blocked state узлов, которые от него зависели.

Gate превращает ожидание из туманной паузы в часть работы.

## Проверочный сигнал должен вернуться в граф

Как только граф начинает хранить CI, review, `subagent` outputs и traces, появляется новый риск: система начинает механически выполнять каждый сигнал. Reviewer написал comment — агент чинит. Codex нашёл concern — агент меняет code. Greptile поднял observation — задача разрастается. `Subagent` предложил hypothesis — summary превращает её в truth.

У Jökull Sólberg этот риск хорошо виден в `/babysit-pr`, Claude Code skill for escorting a PR through CI, Greptile and Codex review ([“Babysitting PRs With Claude Code”](https://www.solberg.is/babysit-pr), [“How I Use Claude Code”](https://www.solberg.is/how-i-use-claude-code)). Процедура определяет current PR через `gh pr view`, ждёт CI и Greptile, обрабатывает тот источник, который завершился первым, запускает `codex review --base main`, классифицирует feedback как Fix / Dismiss / Escalate, чинит действительные items, запускает lint, commits, pushes и повторяет цикл до clean state или iteration limit. Критерий выхода — не «агент внёс правки», а CI green, no untriaged issues и PR ready to merge. Есть и ограничитель: максимум три итерации, после чего задачу, вероятно, должен посмотреть человек.

Маленькая классификация здесь важнее всей автоматизации:

- **Fix** — сигнал действителен, локальное исправление понятно, scope позволяет его сделать;
- **Dismiss** — сигнал неверен, основан на неправильной предпосылке или не относится к текущему изменению;
- **Escalate** — нужен человек: продуктовая граница, архитектурный выбор, риск за пределами scope.

В одном из его примеров CI был зелёным, Greptile дал observation про operational behavior, который был dismissed, а Codex нашёл две реальные смысловые проблемы: текст интерфейса больше не соответствовал поведению, а lifecycle `unpublish→republish` оставлял tour в неправильном состоянии. После исправлений second pass был clean, а auto-merge был поставлен в очередь. Вывод не в том, что один reviewer лучше другого. Вывод в том, что signal должен пройти triage до того, как станет действием или основанием закрытия.

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

Mark Erikson показывает тот же принцип со стороны reviewer role. В его OpenCode configuration есть DiffLoupe workflow for intent alignment и read-only reviewer agent, который анализирует changed code, но не редактирует его; reviewer различает must fix / should fix / consider и явно лишён edit permissions ([Mark Erikson, AI workflow setup](https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/), [`markerikson/opencode-config-example`](https://github.com/markerikson/opencode-config-example)). Для PWG это важная граница: review output сначала становится typed graph state. Только затем process profile решает, исправлять, отклонять, передавать человеку или закрывать.

`Subagent` output принадлежит к той же семье. Anthropic в описании своего multi-agent research system подчёркивает, что каждому subagent нужны objective, output format, guidance on tools and sources и ясные task boundaries; иначе агенты дублируют работу, оставляют gaps или не находят necessary information ([Anthropic, “How we built our multi-agent research system”](https://www.anthropic.com/engineering/multi-agent-research-system)). Для главы VII это не аргумент за большее число subagents. Это аргумент за typed returns. Результат дочернего агента должен сказать, что он смотрел, чего не смотрел, что утверждает, что осталось неопределённым и какой work item должен измениться.

Примеры HumanLayer с BAML и parquet/Hadoop уточняют этот же тезис. В случае BAML первый research pass ошибочно решил, что codebase already correct; этот проход отбросили и повторили с лучшим steering. В случае parquet/Hadoop research не прошёл достаточно глубоко по dependency tree, поэтому правдоподобный план сломался на более глубоких зависимостях ([HumanLayer, “Skill Issue”](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)). Значит, у research тоже есть состояние: accepted, rejected, stale, insufficient, blocking, superseded или converted into work.

Mae Capozzi’s platform work gives the artifact version of the same rule. Agent runs produce PRs, Linear tickets, traces, spans, test branches, GitHub Action comments or dependency-review summaries; then a human classifies diff, type errors, Honeycomb UI state, `/review` output or dependency recommendations before merge ([Mae Capozzi, “My AI Coding Workflow”](https://maecapozzi.com/blog/my-ai-coding-workflow), [“AI-Assisted Dependency Review”](https://maecapozzi.com/blog/using-conductor-for-dependabot-reviews)). Artifact is necessary because the human needs something inspectable. But artifact does not automatically mean acceptance.

PWG therefore needs not just `check passed/failed`, but signal state: untriaged, accepted, dismissed, escalated, stale, converted to work item, converted to gate. Проверочный сигнал — вход в состояние работы, а не приказ к немедленному действию.

## `Source state`: выводы стареют

В длинной работе почти всякий вывод привязан к источнику. Агент прочитал файл на одном commit. CI run относится к одной ветке. Review comment написан к одному diff. `Subagent` report основан на старой версии документации. Trace captures one execution. Если источник меняется, вывод может стать устаревшим, даже если в момент получения был верным.

В billing/API примере это происходит сразу:

```text
start base: main@8f31c2a
feature branch: feature/billing-plan-id@b12d44f
current main after one day: main@9c77b40
Subagent Contract report: docs/api/subscriptions.md@8f31c2a
unit CI: success on feature@b12d44f
integration CI: failed on feature@b12d44f
api docs: changed on current main
```

Следующая сессия не должна принимать `subagent report` как timeless truth. Она должна видеть: report был основан на старой версии docs; docs изменились; перед финальным решением нужен refresh. Unit CI success реален, но относится к старому состоянию ветки. Integration failure может всё ещё иметь значение, но его нужно перепроверить после rebase. Review comment может относиться к коду до последнего refactor.

В документной работе source state виден ещё грубее. Ссылка могла быть найдена, но не открыта. Источник мог быть прочитан, но не перенесён. Факт мог попасть в текст, но без ссылки в месте введения. Иллюстрация могла быть настоящим asset candidate, и её нельзя заменить текстовой схемой. Всё это должно быть состоянием работы, если от этого зависит продолжение.

Mark Erikson’s `cachebro` / OpenCode mismatch gives a precise technical example: a file read through `cachebro` MCP was known to that external tool, but OpenCode’s internal edit-safety logic did not know the file had been read, so Erikson had to build a bridge for file access state ([`cachebro`](https://github.com/glommer/cachebro), [`opencode-config-example`](https://github.com/markerikson/opencode-config-example)). Это не мелкая интеграционная ошибка. Это разрыв source state между слоями системы. Один слой считает источник увиденным, другой — нет. В PWG такой разрыв должен становиться видимым, иначе система либо запрещает безопасное действие, либо разрешает небезопасное.

С observability artifacts происходит то же самое. Работа Erikson с Replay MCP показывает, что agent debugging сильно меняется, когда агент видит recording overview, screenshots, React renders, Redux actions или console errors, а не только файлы и failing tests. Работа Mae с Honeycomb показывает traces, spans и Claude Code telemetry events вроде `InstructionsLoaded`, `SessionStart`, `UserPromptSubmit`, `ToolUse` и `SessionEnd` как operational signals вокруг agent work ([Mae, “AI agents removed the friction from writing telemetry”](https://maecapozzi.com/blog/ai-removes-observability-friction), [Honeycomb, “Measuring Claude Code ROI and Adoption”](https://www.honeycomb.io/blog/measuring-claude-code-roi-adoption-honeycomb)). Эти traces сами по себе не являются PWG. Но они могут стать source artifacts, прикреплёнными к work items: этот run упал здесь; это tool decision было отклонено; этот instruction file был загружен; эта session produced this span.

PWG не должен хранить весь мир. Он должен хранить те source-state markers, которые меняют смысл продолжения или закрытия работы.

## Пакет восстановления: не пересказ прошлого, а рабочая форма следующей сессии

Даже хороший граф бесполезен, если следующая сессия не знает, как к нему подступиться. Поэтому рядом с PWG нужен restoration packet: компактная рабочая картина для следующего actor.

Это не то же самое, что summary. Summary пересказывает, что произошло. Restoration packet говорит, как безопасно продолжить.

Для billing/API он мог бы выглядеть так:

```text
Current work: W-100 billing/API change.
Branch: feature/billing-plan-id@b12d44f; base main@8f31c2a; current main@9c77b40.
Closed locally: W-101 DTO/validation, W-102 mapping, W-103 unit tests.
Do not close W-100 yet.
Blocking:
  - W-104 legacy mobile compatibility; final behavior gated by G-201.
  - W-105 architecture boundary review; gated by G-202.
  - W-106 integration CI failure; ci/integration/18453 failed.
Ready now:
  - Investigate W-106 failure.
  - Prepare compatibility options for W-104 without finalizing behavior.
Not ready:
  - W-107 public docs until G-201 resolved.
Cautions:
  - Subagent Contract report was based on old docs.
  - Unit CI success does not close integration gate.
  - Agent A claim may be stale; recover before editing.
```

Такой packet не пытается быть полным transcript. Он восстанавливает рабочую форму: что ready, что blocked, что gated, что stale и что запрещено.

Beads `bd prime` даёт полезный конкретный якорь. Он выводит essential workflow context in AI-optimized Markdown, adapts between MCP and CLI modes, поддерживает `.beads/PRIME.md` и designed for agent startup and post-compaction recovery ([`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime)). Codex integration использует skill, managed `AGENTS.md` и lifecycle hooks: SessionStart может inject full `bd prime`; after compaction система может refresh context through the next user-prompt lifecycle ([Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex)).

Но `prime` / restoration packet должен быть не только коротким, но и структурно верным. Материалы HumanLayer по harness engineering предупреждают против dumping the whole encyclopedia into `CLAUDE.md` / `AGENTS.md`; startup instructions должны быть small, purposeful и progressively disclose what matters ([HumanLayer, “Skill Issue: Harness Engineering for Coding Agents”](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents), [Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)). Неудачная оптимизация `rtk grep` у Mark Erikson добавляет другую сторону: overcompressed output может настолько запутать агента, что он начнёт ходить по кругу. Одной компактности недостаточно. Restoration must preserve the distinctions the next actor needs: ready vs blocked, signal vs command, gate vs decision, source current vs stale, claim active vs recoverable.

Это место связывает главы VI и VII. Hooks, skills и MCP относятся к проектному интерфейсу. Они доставляют контекст. Но содержание, которое здесь важно, приходит из PWG: ready queue, gates, claims, source state и recovery notes.

## Что PWG не заменяет

PWG не существует в пустоте. Вокруг него уже есть трекеры задач, task graphs, worktrees, durable runtimes, telemetry и более крупные multi-agent environments. Ошибка начинается тогда, когда один из этих слоёв принимают за весь граф работы.

Обычный issue tracker хорошо показывает, что обсуждается, кто назначен, какие issues связаны и какие из них blocked or blocking. GitHub и Linear уже делают hierarchy and blocking relationships частью обычной практики. Но tracker часто не знает, какой source state использовал `subagent`, какой CI run относится к текущему commit, какой review signal был dismissed, какой `claim` устарел после оборванной сессии и какой restoration packet нужно показать следующему actor.

Task Master и похожие task graphs приближают структуру к agentic execution: tasks могут содержать dependencies, details, test strategy и execution clusters ([Task Master task structure](https://docs.task-master.dev/capabilities/task-structure), [Task Master clusters](https://tryhamster.com/docs/taskmaster/capabilities/clusters)). Но task graph без gate-условий, проверочного состояния, source state, recovery и ownership остаётся планом, а не полным состоянием работы.

Durable runtime решает другую проблему. Temporal, Restate и DBOS показывают, как сохранять execution progress, avoid duplicated side effects и resume after failures ([Pydantic AI Temporal integration](https://pydantic.dev/docs/ai/integrations/durable_execution/temporal/), [Pydantic AI Restate integration](https://pydantic.dev/docs/ai/integrations/durable_execution/restate/), [DBOS Pydantic AI integration](https://docs.dbos.dev/integrations/pydantic-ai)). Runtime может сказать: workflow is waiting for approval. PWG должен сказать: W-104 заблокирован G-201, final docs пока нельзя писать, W-100 нельзя закрывать, а Agent B может prepare options, но не decide.

Worktree изолирует file writes и делает parallel diffs reviewable. Но сам worktree не знает, является ли он experiment, candidate patch, discarded approach, blocked branch, stale claim или accepted path ([Git worktree](https://git-scm.com/docs/git-worktree), [Claude Code common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows), [OpenAI Codex worktrees](https://developers.openai.com/codex/app/worktrees)). Это semantic state находится выше filesystem.

Gas Town — более широкое организационное направление: more agents, roles, rigs, routing and visible coordination. Глава X может развернуть его отдельно. Здесь тезис уже: даже внутри большого town кто-то должен знать, что именно разрешает конкретный кусок работы. Это слой PWG.

Поэтому концепт главы не придуман в изоляции. Beads — ближайший отдельный якорь: Dolt-powered issue tracker for AI-supervised coding workflows, with dependency-aware execution, multi-agent coordination, gates and agent-readable commands ([Beads documentation](https://gastownhall.github.io/beads/), [Beads GitHub repository](https://github.com/gastownhall/beads)). GitHub и Linear показывают mainstream issue relations. Task Master показывает AI-facing task topology. Durable execution systems показывают persistent runtime state. Jökull, HumanLayer, Mark и Mae показывают, как checks, research, review and artifacts возвращаются в human/agent work.

Эти практики не сводятся к одной продуктовой категории. Они указывают на одно давление: когда agents работают across sessions and systems, состояние нужно вынести наружу в форме, которую могут инспектировать и люди, и агенты.

## Граф тоже может лгать

Persistent Work Graph — не магическое решение. Он сам может стать новым источником ложной уверенности.

Самый простой сбой — неправильная dependency semantics. Если каждое отношение превращается в `blocks`, ready queue пустеет, и агенты перестают видеть допустимую работу. Если blockers представлены как loose relations, агенты действуют слишком рано. Beads troubleshooting прямо предупреждает: если `bd ready` не показывает issues, это может означать open blockers; только blocking dependencies должны влиять на ready work; сложные dependency structures могут confuse agents and may need simplification or labels for loose relationships ([Beads troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md)).

Stale claims — другой сбой. Мёртвая сессия может держать узел недоступным. Отсутствующий claim может позволить двум агентам перезаписать друг друга. Слишком широкий claim может заморозить несвязанную работу.

Gates могут протухать. CI gate мог быть resolved, но не closed. Human decision могло быть принято в PR comment, но не propagated. Failed gate может требовать escalation, а не silent retry. Closed PR не равен merged PR. Timer expiry может быть timeout, а не success.

Source state может лгать умолчанием. Subagent report, основанный на старых docs, может выглядеть current. Green CI run на старом commit может выглядеть как acceptance. Trace из одного environment могут ошибочно принять за production truth. Review comment на старом diff может неправильно блокировать новый code.

Даже сама PWG-инфраструктура может отказать. Beads architecture описывает Dolt as source of truth, auto-committed writes, embedded/server modes, recovery through pull or backup restore, а также ограничения around multi-machine sync, real-time collaboration and larger teams ([Beads architecture](https://gastownhall.github.io/beads/architecture)). Beads recovery documentation starts from diagnostics such as `bd status`, `bd doctor` and `bd blocked`; это полезное напоминание: граф — инфраструктура, а инфраструктуре нужны recovery, migration discipline и cleanup ([Beads Recovery Overview](https://gastownhall.github.io/beads/recovery)).

Cleanup therefore belongs to the work graph. Not all cleanup, not the whole theory of technical debt, but graph-truth cleanup:

- stale claims must be released or renewed;
- resolved gates must be closed;
- failed gates must create work or escalation;
- old source notes must be marked stale;
- duplicate work items must be merged;
- abandoned worktrees must not be deleted before artifacts are accepted or rejected;
- subagent outputs must be accepted, rejected, superseded or archived;
- restoration packet must be regenerated after meaningful state change.

Без этого PWG становится summary, которому придали более убедительную форму. Это хуже обычной сводки, потому что ложное состояние начинает выглядеть как структура.

## Где заканчивается глава VII

PWG не выбирает способ действия. Он показывает, где находится работа.

Если граф говорит, что W-106 готов к работе, следующая глава может спросить: какой process profile нужен — investigation, repair, test reproduction, CI triage или escalation? Если W-104 gated by human compatibility decision, следующая глава может спросить: агент должен prepare options, собрать source evidence, draft a decision memo или ждать? Если W-107 blocked by G-201, следующая глава может спросить, какой profile applies after the gate resolves. Если W-100 не done, потому что integration CI failed, review открыт и source state stale, следующая глава может спросить, как перейти от этого graph state к дисциплинированному action path.

Такова граница.

Глава VI объяснила проект как интерфейс: skills, hooks, MCP, rules и routes. Глава VII объясняет, где живёт работа, оставленная этими routes. Глава IX глубже уйдёт в runtime, rights, sandbox и execution environment. Глава X развернёт более широкий Gas Town / organizational layer. Более поздние главы подробнее разберут acceptance, authority, evidence и cleanup. Здесь центральный тезис уже и острее:

Долгое агентское изменение нельзя безопасно продолжать из красивого summary. Ему нужен persistent work graph: долговечное состояние work items, dependencies, claims, gates, source states, classified signals и restoration packets. Без этого слоя `done` становится тем, что последняя сессия имела достаточно контекста назвать завершением. С этим слоем следующая сессия видит не только, что произошло, но и что теперь разрешает сама работа.
