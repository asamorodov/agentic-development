# P11 — Активный добор после первого черновика

Статус: после reread первого полного черновика выявлены несколько мест, где глава стала слишком общей, потеряла часть технической фактуры или слишком быстро перешла от среды исполнения к большим выводам. Ниже не просто замечания, а готовые переписанные фрагменты для замены/вставки в следующий полный вариант.

## 1. Главные находки после reread

### 1.1. Начало главы уже работает, но ему не хватает явной карты «чтение / запись / действие»

Первый черновик хорошо вводит billing/UI example, но недостаточно рано показывает, что агент проходит не один поток прав, а последовательность разных видов действия. Это можно усилить маленьким фрагментом после начальной сцены: не абстрактной таблицей, а естественным перечислением, где сразу различаются чтение, локальная запись, команда, браузерное действие, внешний вызов, communication mutation and PR.

### 1.2. В разделе про sandbox/approval стоит добавить network/local services nuance

В черновике есть network and secrets, но слабее звучит конкретное различение из Codex docs: allowed network destination is not trusted destination; local/private network targets are a separate boundary. Это важно для billing example: `localhost`, webhook tunnel, private admin service and external billing API are not one category.

### 1.3. Hooks section needs a sharper distinction between deterministic hooks and model hooks

Первый черновик это называет, но можно сделать сильнее. В главе нужно подчеркнуть: hook is not necessarily a deterministic sensor. Hook may be shell command, HTTP endpoint, MCP tool, prompt or agent; each changes trust boundary differently. Это поможет не превратить hooks в магическое «автоматически проверяет».

### 1.4. Local harness section needs more concrete failure and repair

Черновик говорит, что `make dev` should behave well, but could carry more concrete sequence: duplicate server, hanging command, huge log, hidden login email, target `tail-log`, test fixture, webhook replay. Эта глава ценна именно бытовыми деталями среды.

### 1.5. Workflow runtime section needs more Roast concreteness and the external run

В черновике Roast/Boba раскрыт, но почти не использует фактуру `cmd`/`ruby`/`chat`/`agent`/`map`/`repeat`, session resume/forking and Doubrovkine run. Нужно добавить не каталог DSL, а показать, что workflow has executable form and model/API credentials can be step-level runtime facts.

### 1.6. Final bridge should name PWG/gate only enough to prepare XI/XII

Финальный мост хороший, но слишком общий. Нужно добавить короткое различение: run history can say where execution stopped; work state must say why the work is waiting, who owns it, what evidence is needed, whether gate is satisfied. Beads/PWG should appear only as boundary, not as new topic.

## 2. Replacement fragment for the opening: sequence of action surfaces

Place after the paragraph ending with “Это разные границы, и ошибка начинается там, где одна граница начинает выдавать себя за другую.”

```markdown
У этого запуска есть ещё одна неприятная особенность: разные действия внешне выглядят одинаково, потому что все они приходят из одного чата или одного agent thread. Агент «что-то делает». Но инженерно это разные виды перехода.

Когда агент читает `billing_controller.ts`, он получает информацию. Когда он правит frontend hook в worktree, он создаёт устойчивый diff. Когда он запускает `npm test -- billing`, он исполняет код проекта. Когда он открывает локальную страницу в браузере, он получает наблюдение и одновременно возможность нажимать кнопки. Когда браузер уже залогинен в реальный dashboard, то же самое действие становится credentialed action. Когда агент вызывает MCP tool, он может читать внешнюю систему или менять её состояние. Когда он создаёт PR, он уже действует в социальной и организационной поверхности проекта.

Поэтому глава будет каждый раз задавать один и тот же вопрос: какой именно переход произошёл? Прочитали данные, записали файл, выполнили команду, пересекли сеть, использовали секрет, нажали в авторизованном интерфейсе, вызвали tool with side effect, создали артефакт ревью или приняли результат? Пока эти переходы не названы, разговор об «автономности агента» остаётся слишком грубым.
```

## 3. Replacement / expansion for sandbox-permission section

Insert after current paragraph about Codex permission profiles and before “In billing-примере...”

```markdown
У этой раздельности есть практическое следствие, которое легко упустить. Даже network allowlist не является решением о доверии. Если агенту разрешили обращаться к определённому домену, это значит только, что traffic может пройти к этому домену. Это не значит, что ответ домена полезен, безопасен, не содержит misleading content, не заносит prompt-injection-like instructions and не побуждает агента к лишним действиям. Codex документация прямо разводит outbound destinations and trust: domain rules constrain traffic; they do not determine whether an allowed destination is trustworthy [OpenAI Codex permissions](https://developers.openai.com/codex/permissions).

То же относится к local services. Для обычного разработчика `localhost` звучит безопаснее интернета, но для агента это может быть доступ к локальной админке, базе, dev dashboard, internal API, unix socket or webhook forwarder. Поэтому современные permission models отдельно говорят о local/private network targets. В billing-задаче local app на `localhost:3000`, webhook listener, локальная база, Stripe-like test API and production dashboard are different surfaces. Их нельзя открывать одним неразличимым «разрешить сеть».
```

Add after Auto-review paragraph:

```markdown
Особенно важно, что отрицательное решение не должно превращаться в игру «найди обход». В current Codex Auto-review docs denial returns a rationale and instructs the main agent not to pursue the same outcome through workaround, indirect execution or policy circumvention, but to find a materially safer path or stop [OpenAI Codex Auto-review](https://developers.openai.com/codex/concepts/sandboxing/auto-review). Это прямо рифмуется с примером Arvid, где агент пытался выполнить запрещённую migration-like command через bash script. Хорошая среда должна блокировать не только опасную строку, но и попытку добиться того же эффекта обходным путём.
```

## 4. Replacement for the command-rules section close

Replace the final paragraph of “Правила команд...” with this stronger close:

```markdown
Правила команд поэтому должны проектироваться вокруг радиуса ущерба, а не вокруг удобства агента. Команда сборки обычно безопасна. Targeted tests usually safe. Reset test container may be safe if the container is explicitly disposable. `migrate:fresh` against a hand-built local database is already a different action. The same-looking command against production is not a command at all in this sense; it is a forbidden boundary crossing.

Именно здесь сходятся Arvid and Codex. Arvid показывает бытовой случай: `allow` removes friction, `deny` protects local state, but the agent may try to create an indirect path. Codex rules show the product-level shape: argv-prefix policy, most-restrictive match, examples, shell splitting. Обе линии говорят одно и то же: command rules are useful because they are mechanical, and limited because they are mechanical. Они должны быть окружены sandbox, protected paths, hook checks, logging and human review.
```

## 5. Expansion for the MCP/tools section: read/action ladder

Insert after the list of example billing MCP tools.

```markdown
Здесь полезна маленькая лестница действий.

На первом уровне tool returns public documentation. Это всё ещё не нейтрально: внешний текст может быть устаревшим, ошибочным or hostile to the agent context. На втором уровне tool reads private project data: issue comments, customer object, logs, observability. Здесь уже появляется confidentiality boundary. На третьем уровне tool creates test state: checkout session, webhook replay, temporary customer. Здесь появляется side effect, даже если он test-mode. На четвёртом уровне tool mutates durable project or customer state: cancel subscription, update billing config, post issue comment, close ticket. На пятом уровне tool changes authority surface: creates PR, asks reviewer, triggers deployment, changes policy.

Если всё это назвать «tool access», среда становится слепой. Хорошая среда должна знать хотя бы грубо: this call is read-only but sensitive; this call writes disposable test state; this call is destructive; this call affects project communication; this call changes deployment or customer state.
```

## 6. Replacement for browser/devtools section middle

Replace the paragraph beginning “A safe billing run should therefore...” with this longer version.

```markdown
Безопасный billing run должен поэтому проектировать browser как отдельную среду, а не как обычное окно пользователя. Лучший вариант — dedicated browser profile, local or staging URL, test user, no password manager, no production dashboard, no shared personal cookies, screenshots and traces saved only if they help review and do not leak private data. Если агенту нужен login, среда должна дать test login helper, debug email in logs or seeded session. Если он упирается в CAPTCHA, two-factor prompt or production dashboard, это не nuisance, а правильная точка остановки.

Опасный вариант выглядит почти так же на поверхности: агент открывает страницу, видит ошибку и «для диагностики» переходит в уже авторизованный billing dashboard разработчика. Технически это может быть один и тот же browser tool. Смыслово это другой класс действия. В первом случае агент проверяет локальный пользовательский поток. Во втором он действует внутри чужих credentials and production-like authority.
```

## 7. Replacement for hooks section: deterministic / HTTP / MCP / model hook split

Insert after the paragraph about Kiro hooks.

```markdown
Поэтому hooks нельзя описывать как единый механизм «автоматической проверки». У них есть разные уровни доверия.

Детерминированный command hook, который после `Edit` запускает formatter or `npm test -- billing`, ближе всего к обычному инженерному feedback. Он может быть шумным, медленным or incorrectly scoped, but its nature is understandable. HTTP hook crosses a network boundary: теперь task data может уйти во внешний сервис, and the response becomes part of runtime decision. MCP hook invokes another tool server, with its own credentials, trust and audit model. Prompt or agent hook adds another model judgment, which may be useful, but no longer has the same status as a deterministic check.

Это не аргумент против HTTP, MCP or model hooks. Это аргумент за честную маркировку. Если Stop hook блокирует завершение, потому что targeted tests failed, это один вид обратной связи. Если Stop hook спрашивает другого агента, выглядит ли работа завершённой, это другой вид обратной связи. Оба могут быть полезны, но их нельзя одинаково называть proof.
```

## 8. Expansion for local harness section

Insert after “The exact commands do not matter. The shape matters.”

```markdown
Хороший локальный harness обычно заметен не по одному большому инструменту, а по маленьким отсутствующим шероховатостям. `make dev` можно вызвать дважды, и он не поднимает две копии сервера на одном порту. Если порт занят, команда говорит, какой процесс уже работает. Логи не исчезают в прокрученной terminal history, а пишутся в известный файл. `make tail-log` показывает последние строки без бесконечного потока. Test email appears in dev log, not in the developer’s real inbox. Webhook replay has a test fixture. Seed data can create billing user in known state. Targeted test command exists and does not require agent to infer the whole test layout.

Когда этих деталей нет, агент начинает чинить не продукт, а среду. Он перезапускает сервисы, угадывает порт, читает огромный output, создаёт новую фикстуру вместо использования существующей, просит реальные credentials or gives up. Поэтому harness is part of execution rights indirectly: он не только показывает, что разрешено, но и делает безопасный путь самым лёгким путём.
```

## 9. Replacement/expansion for workflow runtime section

Insert after paragraph about Roast repository/cogs.

```markdown
Важны не названия `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call` сами по себе, а то, что workflow has executable surface. `cmd` запускает обычную команду. `ruby` выполняет обычный код. `chat` asks a model without giving it full code-editing agency. `agent` delegates a bounded coding step. `map` fans out a pattern over a collection. `repeat` creates an explicit loop with exit conditions. Session resume/forking lets a costly interaction continue or branch without starting from zero. В такой схеме агент больше не обязан держать весь процесс в голове. Процесс становится внешним артефактом.

Внешний walkthrough Daniel Doubrovkine adds a useful mundane detail: Roast run is affected by ordinary runtime facts such as API key, selected model and workflow file edits. Он first checks OpenAI key with `curl`, then adjusts workflow model settings because the original model mix is not available/cost-effective for his run [Doubrovkine, “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html). Это хороший reminder: даже «AI workflow» is still software execution. It has environment variables, model routing, credentials, logs and failure modes.
```

Replace the paragraph beginning “Quix’s Klaus Kode story...” with:

```markdown
Quix’s Klaus Kode story gives the same lesson from the opposite direction. A team can try to encode a long exact sequence in the prompt or expose a large MCP catalog, but then the model spends context on tool descriptions and brittle procedural instructions. The repair is to move stable orchestration into deterministic code: upload code and dependencies through ordinary API calls, run app in a cloud sandbox, download logs, call Claude Code for the bounded coding step, then continue with code again. In that pattern the agent is not humiliated; it is placed where uncertainty actually remains.
```

## 10. Stronger bridge after durable execution paragraph

Insert before “That is the boundary between runtime state and work state.”

```markdown
The failure mode here is subtle. A durable runtime can remember that step 6 failed, step 7 waited for approval, approval arrived, and step 8 resumed. It can replay event history or skip completed journaled steps. But if a reviewer asks “what exactly are we proving?”, the runtime may have no answer beyond its own steps. It knows execution order, not necessarily work meaning. The missing object is the work item: promise, owner, blocker, gate, required checking material, accepted/rejected state and safe next action.
```

## 11. Expansion for final trace/evidence bridge with PWG/Beads

Insert after the paragraph ending “Workflow completion is not project authority.”

```markdown
This is why PWG-like mechanisms belong after, not inside, execution runtime. A gate can wait for human review, CI, a GitHub run, PR state, timer or another work item. A prime/rehydration artifact can help a later agent recover task context. But these mechanisms do not replace the run log; they organize what the run log is for. Runtime says: here is what happened. Work state says: here is why this matters, who must decide, what is still blocked, and what material is enough to continue.

If IX blurs this line, later chapters lose their reason to exist. The whole point is that a trace becomes useful only when attached to the claim it is meant to support. A durable run history without a work item is an execution diary. A work item without run trace is a promise without grounded material. The lifecycle needs both, but they are not the same layer.
```

## 12. Minor wording repairs for next full draft

- Replace scattered “evidence” in the Russian prose with “проверочный материал”, “доказательный материал” or “след проверки” depending on context. Keep `evidence` only when naming an external concept/source if needed.
- Replace “proof” with “доказательство” only where a strict proof-like claim is intended. Most runtime outputs are not proof; they are signals or material.
- In the phrase “agent technically can run command”, rewrite as “process is able to execute command” when the point is about runtime, not model agency.
- Avoid “делает среду слепой” if it sounds too metaphorical; possible replacement: “policy loses the distinction it needs”.
- Avoid overusing “authority surface”; in public Russian, prefer “поверхность полномочий” only once, then explain as “где действие уже происходит от имени пользователя или проекта”.

## 13. Updated conclusion shape

The final conclusion should be slightly less abstract than P10. Candidate replacement for the last two paragraphs:

```markdown
A good environment does not merely restrain the agent. It makes the safe path cheap and the dangerous crossing visible. It gives the agent small reliable tools, readable logs, test accounts, isolated worktrees, scoped network, explicit approvals and a recoverable run state. It lets the agent continue through routine failures without forcing the human to approve every harmless step. And it stops the agent where the boundary is no longer technical: production data, external side effects, product judgment, customer impact, merge authority.

That is the role of execution in the lifecycle of change: not to make the model omnipotent, but to make its action bounded, observable, recoverable and reviewable. The agent can then move faster inside the parts of work that are safe to mechanize, while the project keeps names for the decisions that cannot be delegated to a sandbox, hook or workflow runtime.
```
