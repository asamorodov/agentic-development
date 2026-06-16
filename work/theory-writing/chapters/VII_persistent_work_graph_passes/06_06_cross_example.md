# P06 — сквозной пример для главы VII

## Назначение примера

Этот пример должен стать рабочей осью главы. Он не обязан попасть в финальный текст целиком, но в нём должны быть видны почти все различения главы: почему summary недостаточно, как локальное `done` становится ложным завершением, чем отличается work item от заметки, что такое blocker, gate, claim, source state, проверочное основание, stale state and restoration packet.

Ситуация выбрана намеренно обычная: изменение billing/API. Это не экзотический сценарий и не искусственная демонстрация инструмента. В такой форме проблема возникает почти в любой реальной разработке, где изменение проходит через код, тесты, совместимость, review, CI и несколько сессий агента.

## Короткая фабула

Команда меняет billing API. Нужно добавить поддержку нового поля `billingPlanId` в endpoint `POST /subscriptions/change-plan`, не сломав старых клиентов. Изменение кажется небольшим: обновить DTO, validation, mapping в billing service, несколько тестов и документацию.

Первый агент берёт задачу и делает реализацию. В конце сессии он пишет: «Готово, добавил поле, тесты проходят, осталось только review». Но к этому моменту в работе уже есть несколько ветвей состояния:

- найден edge case со старым mobile client, который отправляет payload без нового поля;
- один subagent проверил историю API контрактов и нашёл, что endpoint раньше явно обещал backward compatibility для старых клиентов;
- другой subagent посмотрел CI and tests: unit tests are green, но integration test падает на staging-like profile;
- review архитектурной границы не закрыт: есть риск, что billing DTO протекает в public API layer;
- human reviewer должен решить, допустим ли compatibility fallback or strict validation;
- target branch обновилась после начала работы;
- previous agent left a claim on implementation item, but the session ended.

Если продолжать из summary, следующая сессия видит «почти готово». Если продолжать из graph state, она видит совсем другое: часть работы действительно готова, часть заблокирована, часть ожидает решения, часть устарела, а часть можно безопасно продолжать прямо сейчас.

## Участники и объекты

### Люди и агенты

- **Агент A** — первая сессия, реализует основное изменение.
- **Subagent Contract** — короткое исследование истории API compatibility.
- **Subagent CI** — исследование тестов и CI-сигналов.
- **Reviewer** — человек или senior engineer, который должен принять compatibility decision and architecture boundary.
- **Агент B** — следующая сессия, которая должна продолжить работу после compaction or interruption.

### Источники состояния

- Branch: `feature/billing-plan-id`.
- Base commit: `main@8f31c2a` at the start of Agent A session.
- Target branch later advanced to `main@9c77b40`.
- PR: `#842 Add billingPlanId to subscription change endpoint`.
- Unit CI run: `ci/unit/18452`, success.
- Integration CI run: `ci/integration/18453`, failed on `LegacyMobilePayloadScenario`.
- API contract doc: `docs/api/subscriptions.md`, updated by another PR between sessions.
- Architecture note: `docs/architecture/public-api-boundary.md`.
- Review thread: `PR#842/thread#boundary-dto-leak`.

### Рабочие узлы

Условный graph snapshot после первой сессии:

```text
W-100  Change billing API: support billingPlanId in change-plan endpoint
  status: open
  claim: Agent A, last seen at 2026-06-15 12:10
  source: feature/billing-plan-id@b12d44f, base main@8f31c2a
  blocks: release/subscriptions-v2
  children:
    W-101 Implement DTO + validation
    W-102 Update billing service mapping
    W-103 Add unit tests
    W-104 Resolve legacy mobile payload compatibility
    W-105 Resolve architecture boundary review
    W-106 Fix or classify integration CI failure
    W-107 Update public API docs
  gates:
    G-201 Human decision: strict validation vs compatibility fallback
    G-202 Architecture review: DTO boundary
    G-203 Integration CI run: staging-like profile
```

Детали узлов:

```text
W-101 Implement DTO + validation
  status: closed locally
  source: feature/billing-plan-id@b12d44f
  check: unit tests passed in ci/unit/18452
  caveat: validation behavior depends on G-201

W-102 Update billing service mapping
  status: closed locally
  source: feature/billing-plan-id@b12d44f
  check: unit tests passed in ci/unit/18452

W-103 Add unit tests
  status: closed
  check: ci/unit/18452 success

W-104 Resolve legacy mobile payload compatibility
  status: open
  discovered-from: W-101
  blocks: W-100 done
  source: Subagent Contract report based on docs/api/subscriptions.md@main@8f31c2a
  gate: G-201

W-105 Resolve architecture boundary review
  status: open
  blocks: W-100 done
  source: PR#842/thread#boundary-dto-leak
  gate: G-202

W-106 Fix or classify integration CI failure
  status: open
  blocks: W-100 done
  source: ci/integration/18453 failed
  relation: may be caused by legacy payload compatibility

W-107 Update public API docs
  status: open
  blocked-by: G-201
  source: docs/api/subscriptions.md changed after branch start
```

Gates:

```text
G-201 Human decision: strict validation vs compatibility fallback
  type: human
  blocks: W-104, W-107, W-100 done
  state: pending
  owner: Reviewer
  question: Should missing billingPlanId be accepted for legacy clients?

G-202 Architecture review: DTO boundary
  type: human/review
  blocks: W-105, W-100 done
  state: pending
  owner: Reviewer
  source: PR#842/thread#boundary-dto-leak

G-203 Integration CI run
  type: ci
  blocks: W-106, W-100 done
  state: failed
  source: ci/integration/18453
  note: failing scenario overlaps with W-104
```

Это ещё не финальная модель данных. Для главы важна не точная схема, а видимость: работа уже не является одним линейным item, но и не должна превращаться в хаос заметок.

## Что сказал бы summary

После первой сессии summary мог бы выглядеть так:

```text
Добавил billingPlanId в change-plan endpoint. DTO, validation и mapping обновлены, unit tests проходят. Нашёл edge case со старым mobile client, надо решить compatibility. Integration CI падает на legacy payload scenario, возможно связано с edge case. Есть review comment по границе DTO. Следующей сессии надо поправить edge case, дождаться review и обновить docs.
```

Это summary неплохое. Оно не лжёт. Но оно не отвечает на практические вопросы продолжения:

- Можно ли агенту B прямо сейчас менять validation?
- Кто должен решить compatibility behavior?
- Падение integration CI уже classified or still unresolved?
- Unit tests зелёные на каком commit?
- Review по DTO boundary blocking or just related?
- Public API docs можно обновить сейчас или они зависят от human decision?
- Claim Agent A still active or stale?
- Что будет считаться closure для W-100?
- Изменился ли source после отчёта subagent?

Summary превращает состояние работы в рассказ. PWG должен превратить рассказ в набор действий, ожиданий и ограничений.

## Где появляется ложное `done`

Локальное `done` возникает не из злого умысла. Агент A действительно закончил некоторый кусок:

- DTO changed;
- mapping changed;
- unit tests added;
- unit CI passed;
- PR opened or updated.

Если система принимает это за done всего изменения, возникает ошибка. На самом деле закрыты только W-101, W-102, W-103. Общий W-100 остаётся open, потому что W-104, W-105 and W-106 still block it, and G-201/G-202/G-203 remain unresolved.

Правильная формулировка не «агент сказал неправду», а «локальный результат был принят не на том уровне». Локально patch может быть done; graph-level work item is not done.

Это различение нужно держать в главе постоянно. Иначе разговор о PWG превращается в очередной призыв «пишите лучшие summaries». Проблема не только в качестве summaries. Проблема в том, что завершение должно быть проверяемым состоянием графа.

## Work item vs note

Во время работы Agent A оставляет несколько записей:

```text
Note: legacy mobile client may not send billingPlanId.
Note: API contract doc says backward compatibility was promised in 2024.
Note: integration test fails in LegacyMobilePayloadScenario.
Note: public API DTO now imports BillingPlanId from internal billing namespace.
```

Если эти записи останутся notes, Agent B может их прочитать, а может пропустить. Они не управляют ready state. Поэтому часть notes должна быть повышена до graph objects:

- legacy client compatibility → W-104, потому что требуется решение and blocks done;
- integration test failure → W-106, потому что требуется action/classification and blocks done;
- public API DTO boundary → W-105, потому что требуется review and may block architecture acceptance;
- API contract promise → source/evidence attached to W-104, but not necessarily a separate work item.

Главное правило примера: не всё важное становится задачей, но всё, что блокирует продолжение или acceptance, должно быть видно графу.

## Dependency types: почему не всякая связь блокирует

В примере есть разные связи:

```text
W-104 discovered-from W-101
W-104 blocks W-100 done
W-106 related-to W-104
W-107 blocked-by G-201
W-105 blocks W-100 done
W-101 parent-child W-100
```

Если система трактует все эти связи как blockers, ready queue может опустеть без причины. Например, W-106 related-to W-104, but it may still be investigated before human decision. Можно открыть failing integration test and classify it even while compatibility decision is pending. Но W-107 public API docs действительно blocked by G-201, потому что final documented behavior depends on the human decision.

Если система, наоборот, не различает hard blockers, Agent B может начать обновлять docs before compatibility is decided, or close W-100 while architecture boundary still unresolved.

В главе этот момент можно объяснить через простой конфликт: graph relation is not automatically readiness relation. Семантика связи важнее самого факта ребра.

## Ready queue в примере

После первой сессии граф может вычислить ready set.

Примерно так:

```text
Ready now:
  W-106 Fix or classify integration CI failure
    reason: open; blocks W-100; no human decision required to inspect failing run

Possibly ready after stale claim cleanup:
  W-104 Resolve legacy mobile payload compatibility
    reason: open; but final behavior gated by G-201
    allowed action: prepare options, inspect code paths, do not finalize validation semantics

Not ready:
  W-107 Update public API docs
    blocked by G-201

Not ready:
  W-105 Resolve architecture boundary review
    blocked by G-202 / reviewer response

Not ready:
  W-100 Change billing API
    blocked by W-104, W-105, W-106 and gates G-201/G-202/G-203
```

Здесь есть тонкость: W-104 одновременно open and gated. Это не значит, что с ним нельзя делать вообще ничего. Нельзя закрыть final compatibility decision before G-201. Но можно подготовить варианты, посмотреть код, написать failing test for legacy payload, собрать consequences. Поэтому глава VIII потом должна говорить о process profiles: для gated узла может быть профиль «prepare options / investigation without finalizing decision». Глава VII фиксирует только состояние: final closure blocked by human decision.

## Claim failure

Agent A оставил claim on W-100 or W-101. Если claim слишком слабый, Agent B может взять тот же узел и перезаписать работу. Если claim слишком сильный, работа останется невидимой because previous session died.

Пример stale claim:

```text
claim:
  owner: Agent A
  scope: W-100 implementation
  worktree: /tmp/agent-a-feature-billing-plan-id
  last_seen: 2026-06-15 12:10
  state: no heartbeat after session end
```

Agent B должен не просто игнорировать claim. Он должен провести небольшой recovery step:

- проверить, существует ли worktree or branch;
- проверить, есть ли uncommitted changes;
- понять, был ли claim на весь W-100 or only W-101/W-102;
- release or renew claim with note;
- не начинать independent rewrite if existing branch contains valid work.

В summary это почти всегда исчезает. Summary может сказать «работал агент A». Graph state должен сказать, удерживает ли эта работа узел сейчас.

## Gates в примере

### G-201: human compatibility decision

Решение: что делать, если старый client отправляет payload without `billingPlanId`?

Варианты:

1. Reject request as invalid.
2. Accept request and infer current plan.
3. Accept only for legacy client versions.
4. Add deprecation warning and keep compatibility for one release.

Пока это не решено, несколько действий можно делать только частично. Агент может подготовить варианты, написать tests for options, оценить risk. Но он не должен закрывать API docs and final validation behavior.

Gate должен хранить не только «ждём человека», а сам вопрос, affected nodes, owner and resolution condition.

### G-202: architecture boundary review

Риск: internal billing DTO or domain object попал в public API layer. Это может быть не runtime bug, а design boundary violation.

Пока review open, W-105 blocks W-100 done. Но это не значит, что implementation work all stops. Можно локализовать import, предложить public DTO, подготовить patch. Финальное закрытие depends on reviewer acceptance.

### G-203: integration CI failure

CI gate отличается от human gate. У него есть machine signal. Но и здесь нужна семантика:

- failed run belongs to commit `b12d44f`;
- failing scenario overlaps with legacy payload;
- rerun after rebase may produce different result;
- success of unit tests does not close integration gate;
- canceled/failed/pending states should not be compressed into «CI была».

В summary фраза «CI падает» слишком груба. Graph state needs exact signal and its relation to work item.

## Проверочные основания в примере

Для закрытия W-100 могут быть нужны такие основания:

```text
Acceptance basis for W-100:
  - unit tests: ci/unit/18452 success on feature/billing-plan-id@b12d44f
  - integration tests: pending or failed until ci/integration rerun passes
  - compatibility behavior: decided by Reviewer in G-201
  - architecture boundary: accepted in PR#842/thread#boundary-dto-leak or fixed
  - public docs: updated after compatibility decision
  - source freshness: branch rebased on current main
```

Это не финальная теория evidence. Здесь важно только, что граф не должен позволить закрыть W-100 based only on local self-report. Он должен видеть, какие проверочные основания уже есть, какие относятся к старому source state, какие отсутствуют, какие являются pending gates.

Если использовать слово `evidence`, лучше делать это в техническом месте: `evidence state` or `acceptance basis`. В русском тексте естественнее говорить «состояние проверок», «основания принятия», «сигналы проверки». Для этой главы не надо застревать на терминологии, но нельзя оставлять слово «свидетельства» как главный термин.

## Source state в примере

После первой сессии target branch продвинулся:

```text
start base: main@8f31c2a
current main: main@9c77b40
feature branch: feature/billing-plan-id@b12d44f
api docs changed at main@9c77b40
```

Это меняет состояние нескольких выводов:

- Subagent Contract based its conclusion on old `docs/api/subscriptions.md@8f31c2a`.
- Current docs now include a new note from another team.
- Unit CI success belongs to `b12d44f`, not rebased branch.
- Integration failure may disappear or change after rebase.
- Architecture review may refer to code before refactoring from `main@9c77b40`.

Если PWG не хранит source state, Agent B может принять устаревший вывод как текущий. Он может, например, обновить docs based on a version already changed by another PR. Или решить, что compatibility promise exists, while current docs narrowed it. Или наоборот потерять важное старое обязательство.

Для главы важно: source state не должен превращать PWG в полный database of everything. Нужны минимальные ссылки на состояние источников там, где от них зависит работа.

## Subagent output: как он возвращается в граф

Subagent Contract возвращает такой вывод:

```text
Legacy behavior: In 2024 docs, change-plan endpoint allowed missing plan metadata for existing subscriptions. Mobile clients before v5.8 may still send partial payload. Recommendation: do not require billingPlanId without compatibility fallback.
```

Этот вывод сам по себе не закрывает вопрос. Он должен быть triaged:

- accepted as source evidence for W-104;
- linked to source doc version;
- converted into G-201 question for human reviewer;
- maybe converted into test task: add legacy mobile payload test;
- not treated as final product decision unless reviewer has authority.

Subagent CI возвращает другой вывод:

```text
Unit suite is green. Integration suite fails in LegacyMobilePayloadScenario. Failure likely caused by validation rejecting missing billingPlanId.
```

Этот вывод тоже должен быть triaged:

- attach CI run IDs;
- create/keep W-106;
- link W-106 to W-104 as related or possibly caused-by;
- do not close W-100;
- maybe mark W-106 ready for investigation.

Главная мысль: subagent output should not land only as prose in transcript. It must return into the work graph with type and consequences.

## Возврат результата в следующую сессию

Agent B starts after compaction or next day. Bad restoration packet:

```text
We implemented billingPlanId. Some compatibility and CI issues remain. Continue from there.
```

Better restoration packet:

```text
Current work: W-100 billing/API change.
Branch: feature/billing-plan-id@b12d44f; base main@8f31c2a; current main@9c77b40, rebase needed before final CI.
Closed locally: W-101 DTO/validation, W-102 mapping, W-103 unit tests.
Do not close W-100 yet.
Blocking:
  - W-104 legacy mobile payload compatibility; final behavior gated by G-201.
  - W-105 architecture boundary review; gated by G-202.
  - W-106 integration CI failure; ci/integration/18453 failed on LegacyMobilePayloadScenario.
Ready now:
  - Investigate W-106 failure and prepare compatibility options for W-104.
  - Check whether Agent A claim is stale; recover branch/worktree before editing.
Not ready:
  - W-107 public API docs until G-201 resolved.
Reviewer questions:
  - G-201: strict validation or compatibility fallback?
  - G-202: public API DTO boundary accepted or must be refactored?
Cautions:
  - Subagent Contract report was based on docs at main@8f31c2a; docs changed at main@9c77b40.
  - Unit CI success does not close integration gate.
```

This is not just a longer summary. It is a different object: a restoration packet derived from graph state. It separates ready, blocked, gated, stale, source-bound and cautionary information. It gives Agent B an action surface without forcing it to reread the whole transcript.

## Как пример проходит через основные различения главы

### Summary vs graph

Summary says “almost done.” Graph says which nodes are closed, which are blocked, and what must happen before done.

### Issue list vs PWG

A plain issue list might show W-100, W-104, W-105, W-106. PWG adds relation semantics, ready computation, claims, gates, source state, acceptance basis and restoration packet.

### Runtime checkpoint vs PWG

A runtime checkpoint might resume Agent A’s process. But Agent B may not be the same process; the old process may be gone; human reviewer may decide later; CI may finish while no agent is running. PWG must make work state durable outside any one run.

### Local done vs graph done

Agent A’s local implementation can be done. W-100 graph-level work is not done. Это основная драматургия.

### Human decision as gate

Compatibility is not merely a todo. It is a decision gate that changes which code and docs are correct.

### CI as gate / signal

One green signal does not close the work. Multiple CI signals must be attached to source state and interpreted.

### Subagent output as graph update

Subagent findings are not automatically truth. They need triage, source state, relation to work items and authority boundaries.

### Source state

Branch, docs, CI runs and review comments age at different speeds. PWG must mark freshness where it affects continuation.

### Cleanup

Before Agent B continues, stale claim and possibly stale subagent result must be cleaned or refreshed. Otherwise graph itself becomes misleading.

## Возможная сцена для финального текста

Финальная глава может использовать этот пример не как таблицу, а как narrative sequence:

1. Первая сессия закрывает локальную реализацию.
2. Агент пишет confident summary.
3. На следующий день другой агент пытается продолжить and sees a deceptively simple state.
4. Then the chapter reveals hidden graph: compatibility gate, CI gate, architecture review, stale base, subagent output, claim.
5. From there define PWG.

Такой порядок лучше, чем начинать с определения, потому что читатель сначала почувствует, почему summary fails.

## Минимальный фрагмент примера, который можно вставить почти напрямую

Черновая формулировка, не финальный текст:

> Представим, что агент меняет billing API: добавляет `billingPlanId` в endpoint смены подписки. К концу сессии DTO обновлён, mapping написан, unit tests зелёные, PR открыт. В summary это выглядит как почти законченная работа. Но внутри изменения уже есть другой контур: старый mobile client может отправить payload без нового поля; integration CI падает именно на legacy scenario; reviewer ещё не решил, допустим ли compatibility fallback; в PR открыт комментарий о протекании internal billing DTO в public API layer; target branch ушла вперёд; вывод subagent по API контракту был сделан по старой версии docs. Если следующая сессия получит только summary, она увидит «почти готово». Если она получит граф работы, она увидит открытые узлы, blockers, gates, stale source marks and ready work. Это разные картины реальности.

Этот фрагмент можно будет переписать естественнее в основном draft, но он удерживает нужную интонацию.

## Чего не делать с примером

Не превращать пример в спецификацию вымышленной issue-системы. Команды и поля можно показывать как иллюстрацию, но глава не должна зависеть от конкретной схемы.

Не перегружать пример слишком многими названиями инструментов. Beads, GitHub, CI, Codex hooks могут появиться позже как внешние опоры. В самом примере достаточно billing/API, PR, CI, reviewer, subagent, branch.

Не делать из него главу про API compatibility. Compatibility здесь нужна только потому, что хорошо показывает human decision gate.

Не уходить в подробную теорию verification. Проверочные основания нужны только для различения local done and graph done.

Не делать Agent A виноватым. Иначе мысль станет банальной: «модели ошибаются». Суть сильнее: даже честный локальный результат не равен завершению изменения, если система не хранит состояние работы на правильном уровне.
