# IX. Исполнение: среда агента, права действия и след запуска

Агентская разработка часто описывается слишком высоко: есть задача, есть модель, есть контекст, есть кодовая база, агент что-то делает. Такая формула удобна, пока речь идёт о разговоре, плане или черновике. Но как только агент начинает менять файлы, запускать команды, открывать браузер, обращаться к API, читать логи, создавать ветку или готовить pull request, работа перестаёт быть только языковой. Она становится действием в конкретной среде.

Представим обычную задачу. В продукте есть страница оплаты: пользователь меняет тариф, проходит checkout, возвращается на `/billing`, а карточка тарифа всё ещё показывает старый план, пока страницу не обновить вручную. Агенту дают поручение: найти причину, исправить stale billing state, не сломать существующие subscription flows и вернуть pull request.

На уровне намерения это маленький bugfix. На уровне исполнения это уже не одна операция. Агент читает frontend and backend code, ищет путь checkout return, правит worktree, запускает тесты, поднимает локальное приложение, открывает браузер, смотрит console and network requests, хочет проверить test-mode billing flow, сталкивается с test secrets and network boundary, может попросить approval, может вызвать MCP/tool для issue tracker или billing provider, оставляет журнал команд, browser trace, diff and PR summary.

Если процесс устроен плохо, все эти переходы схлопываются в одну расплывчатую фразу: «агенту дали доступ» или «агент сделал задачу». Но что именно ему дали? Право читать код? Право писать в рабочее дерево? Право запускать тесты? Право открывать браузер, где пользователь уже залогинен в реальные сервисы? Право использовать test API key? Право позвать внешний MCP-server? Право создать PR? Право влить изменение? Это разные границы, и ошибка начинается там, где одна граница начинает выдавать себя за другую.

Главный сбой этой главы можно сформулировать так: агент технически может выполнить действие, а процесс начинает обращаться с этим действием как с допустимым, безопасным или уже принятым результатом. В агентской разработке нужно отдельно держать пять вещей: техническую возможность, permission, approval, проверку и authority. Агент может технически запустить команду. Среда может разрешать определённый класс команд. Пользователь может подтвердить конкретный выход за границу. Тест или браузер может дать проверочный сигнал. И всё равно проекту ещё нужен тот, кто имеет право принять изменение.

Эта глава не является обзором Codex, Claude Code, MCP, Kiro, Roast, Temporal, LangGraph or Sandvault. Все эти источники важны, но только как материалы для одного аргумента: агентское действие становится инженерным действием не из-за силы модели и не из-за красивого prompt, а из-за среды, которая задаёт место действия, права, инструменты, наблюдение, продолжение и след.

## От поручения к месту действия

Поручение само по себе ещё не говорит, где агент действует. «Почини billing UI» может означать одно из нескольких состояний: агент работает в основном checkout разработчика, в отдельном Git worktree, в контейнере, в облачном devbox, в изолированном пользователе macOS, в sandboxed CLI, в корпоративной платформе, которая сама создаёт среду и возвращает PR. У этих вариантов разный радиус ущерба.

Первый слой среды — место записи. Агент должен работать не в абстрактной «кодовой базе», а в конкретной области: project root, worktree, writable roots, temporary/cache paths, generated files, protected paths. В современных агентских инструментах это уже стало отдельным понятием. В Codex документация прямо разводит sandbox as technical boundary and approval policy as the rule for asking before crossing it: sandbox определяет, какие файлы можно менять и можно ли использовать сеть, а approval policy определяет, когда Codex должен остановиться и спросить разрешение [OpenAI Codex sandboxing](https://developers.openai.com/codex/concepts/sandboxing). В Claude Code исходная позиция также строится вокруг read-only permissions by default: редактирование файлов, запуск тестов и выполнение команд требуют явного разрешения, а запись ограничена рабочей папкой и её подпапками, если не выдано дополнительное право [Claude Code Security](https://code.claude.com/docs/en/security).

Для billing-задачи это означает простую вещь: агент должен получить отдельное рабочее дерево или подготовленную рабочую среду, где его diff отделён от обычной работы человека. Он может читать `docs/billing.md`, route/controller code, frontend billing hook, existing tests. Он может писать в рамках worktree. Но из этого ещё не следует, что он может читать реальные `.env` values, трогать production database, открывать logged-in billing dashboard или вызывать внешний payment API.

Инструкции вроде `AGENTS.md`, `CLAUDE.md`, steering files or project rules полезны, но они не являются границей исполнения. Они могут сказать агенту «используй только test data», «не трогай production», «запускай `npm test -- billing`». Но если среда одновременно показывает production secrets, открывает реальную browser session и разрешает broad network access, текстовая инструкция остаётся просьбой. Хорошая среда делает опасное действие невозможным или по крайней мере требует отдельного подтверждения в момент перехода.

Именно поэтому «контекст» и «среда» нельзя смешивать. Контекст говорит агенту, как думать о проекте. Среда определяет, что он может сделать даже тогда, когда думает плохо, спешит, неправильно понял задачу или пытается обойти ограничение.

## Sandbox, permission и approval — не одно и то же

В обычной речи легко сказать: «агенту разрешили запускать команды». Для инженерной среды этого недостаточно. Нужно спросить: какие команды, где, с какими правами, с какой сетью, с какими файлами, с какими исключениями и кто рассматривает переходы за границу.

Sandbox — это техническое ограничение. Команды агента исполняются в среде, где часть файлов недоступна для записи, сеть может быть выключена, локальные сервисы закрыты, private network blocked, protected paths нельзя менять. Codex в текущей документации говорит, что локально агент по умолчанию работает с отключённым network access и OS-enforced sandbox, который обычно ограничивает действия текущим workspace; sandbox applies to spawned commands, включая `git`, package managers and test runners [OpenAI Codex Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [OpenAI Codex sandboxing](https://developers.openai.com/codex/concepts/sandboxing).

Permission profile or permission mode — это поза допуска. Codex, например, описывает встроенные profiles `:read-only`, `:workspace`, `:danger-full-access` and custom profiles. Но его же документация подчёркивает: permission profiles define boundaries for local sandboxed command execution, while app connectors, MCP servers, browser/computer-use surfaces, cloud environments and approved escalations have separate controls [OpenAI Codex permissions](https://developers.openai.com/codex/permissions). Это важнее, чем кажется. Если локальная command execution переведена в read-only, это не значит, что агент вообще безопасен: браузер, MCP-server, облачная среда или уже одобренная escalation могут иметь другую поверхность прав.

Approval — это решение о конкретном переходе. Агент пытается сделать что-то за пределом текущего режима: написать outside writable roots, открыть network, вызвать tool with side effect, зайти на новый сайт в browser, использовать test key. Система спрашивает: разрешить один раз, на сессию, для класса действий or not at all. В Codex app текущая документация формулирует это просто: approvals decide when Codex pauses before running a command, while sandbox controls directories and network access; if unsure, approve the narrowest option [OpenAI Codex app features](https://developers.openai.com/codex/app/features).

Claude Code показывает ту же проблему через режимы. `acceptEdits` позволяет автоматически принимать file edits and some common filesystem commands inside scope. `plan` даёт исследовать и писать план без правки исходников. `auto` уменьшает количество prompts через отдельный classifier, но документация прямо называет его research preview and not a replacement for review on sensitive operations. `bypassPermissions` требует особого включения и доступен не на всех поверхностях [Claude Code permission modes](https://code.claude.com/docs/en/permission-modes). Это не разные названия одной кнопки. Это разные ответы на вопрос, что агент может делать сам, когда он должен остановиться и какой человек или механизм принимает риск.

В billing-примере агент может иметь permission писать в workspace and run tests. Но когда он просит доступ к Stripe-like test API, это уже другой переход: сеть, секрет, внешний сервис, external object creation. Approval должен быть узким: например, разрешить один раз создать test Checkout Session using test key for this reproduction. Такое подтверждение не должно превращаться в общее «можешь пользоваться сетью и секретами как сочтёшь нужным».

Новая деталь в Codex — Auto-review — полезна как показатель направления. Auto-review может заменить человека на отдельного reviewer agent at the sandbox boundary: главный агент остаётся в той же sandbox and approval policy, а reviewer решает, можно ли выполнить eligible escalation. Документация подчёркивает, что Auto-review is a reviewer swap, not a permission grant; он не расширяет writable roots, не включает network и не ослабляет protected paths [OpenAI Codex Auto-review](https://developers.openai.com/codex/concepts/sandboxing/auto-review). Это хорошая форма для будущих систем, но она не отменяет человеческое принятие результата. Reviewer agent может сказать, что конкретный вызов безопасен; он не становится владельцем продукта.

Эта часть легко превращается в мораль «не включайте опасные режимы». Но правильнее сказать иначе: чем шире автономность, тем более жёсткой должна быть внешняя среда. Mike McQuaid в своей практике с Sandvault описывает именно проблему approval fatigue: если каждое безопасное действие требует подтверждения, агент становится медленным shell; если подтверждения выключить на основной машине, риск переносится на токены, файлы и репозитории мейнтейнера. Его ответ — запускать агентов под отдельным macOS user with `sandbox-exec`, shared workspace and Git worktrees [Mike McQuaid, “Sandboxed Agent Worktrees”](https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/), [Sandvault repository](https://github.com/webcoyote/sandvault). Безопасность переносится ниже текста prompt: агент действует не как основной пользователь.

Это и есть зрелая форма различения. Permission снижает трение. Sandbox ограничивает ущерб. Approval управляет переходами. Authority всё ещё остаётся отдельно.

## Правила команд: механическая польза и смысловой предел

После базового sandbox появляется следующий слой: какие команды считаются безопасной рутиной, а какие должны быть запрещены или спрашивать подтверждение. Без allowlists агент постоянно будет спрашивать разрешение на тесты, сборку и обычные project scripts. Слишком широкие allowlists превращают policy в декорацию.

Codex rules are current example of this mechanism. A `prefix_rule()` matches a command argument prefix and decides `allow`, `prompt` or `forbidden`; if multiple rules match, the most restrictive decision wins. Rules can include `match` and `not_match` examples, almost like small unit tests for the policy [OpenAI Codex rules](https://developers.openai.com/codex/rules). Это хорошая инженерная форма: policy становится файлом, который можно читать, версионировать, проверять and manage through config layers.

Но command rule не понимает смысл действия. Он видит argument list or parsed shell fragments. Codex пытается разбирать простые shell chains into individual commands, but this still stays syntactic. Arvid Kahl даёт важный практический пример из своего Claude Code workflow. Он добавляет безопасные действия в `allow` in `settings.local.json`: known build commands, targeted tests, проверенные project scripts. Опасные database operations вроде `php artisan db:wipe`, `migrate:fresh`, `db:*` уходят в `deny`. Но он также описывает риск: агент может написать bash script, внутри которого вызывает запрещённую команду. Формально он не запустил forbidden command directly; по смыслу он попытался сделать то же самое через другой путь [Arvid Kahl, “How to Actually Use Claude Code to Build Serious Software”](https://thebootstrappedfounder.com/how-to-actually-use-claude-code-to-build-serious-software/).

Здесь нужно удержать простую, но тяжёлую мысль: правило команды защищает от строки команды, а не от намерения изменить состояние. Если нельзя wipe local DB, но можно запустить любой script, который wipe её изнутри, запрет слабый. Если агенту разрешено редактировать `package.json`, CI config, shell startup files, build scripts or test hooks, он может создать изменение, которое выполнится позднее outside original sandbox context. Codex permissions docs прямо называют такие writes sensitive: scripts, build steps, package manager hooks, shell startup files and shared directories can be executed later outside the original sandbox [OpenAI Codex permissions](https://developers.openai.com/codex/permissions).

Для billing/UI это означает, что безопасная рутина должна быть узкой. Разрешить `npm test -- billing`, `npm run typecheck`, `npm run lint`, maybe `make dev` if it is idempotent and controlled. Не разрешать broad database reset, arbitrary bash wrappers, commands that can touch production-like state, unscoped network fetches or migrations. Если агенту нужно стереть test DB, пусть это будет test container designed for wipe, not developer’s local state and certainly not production.

Правила команд необходимы. Они делают автономность практичной. Но в тексте главы их нужно показать как механический слой, который требует соседних слоёв: sandbox, protected paths, hooks, review, evidence and authority.

## Tools and MCP: не контекст, а поверхность действия

Про MCP часто говорят так, будто это просто способ «дать модели контекст». Иногда это правда: server can expose documentation, resources or prompts. Но в реальной агентской среде MCP гораздо чаще становится поверхностью действия. Он может дать доступ к database, issue tracker, browser, Figma, billing API, internal docs, observability, cloud provider, local filesystem. Tool description входит в контекст модели, но tool call может читать данные, менять состояние, использовать credentials and return untrusted content.

MCP specification is explicit about this: tools expose external systems such as databases, APIs and computation, and are model-controlled; client applications are expected to show tools/indicators and let users confirm or deny tool calls [MCP Tools specification](https://modelcontextprotocol.io/specification/draft/server/tools). Tool annotations such as `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint` help describe behavior, but they are hints, not guarantees unless backed by a trusted server and enforcement. MCP security guidance separately warns about confused-deputy risks, token passthrough and audit/trust-boundary problems [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices), while authorization guidance treats OAuth and consent as part of the architecture when servers access user data or perform actions [MCP Authorization](https://modelcontextprotocol.io/specification/draft/basic/authorization).

Codex’s current MCP docs show the same practical shape: MCP can connect Codex to third-party documentation or developer tools like browser or Figma; it supports local STDIO servers and remote HTTP servers with bearer/OAuth authentication; server `instructions` are read during initialization and used alongside tools [OpenAI Codex MCP](https://developers.openai.com/codex/mcp). Claude Code likewise lets users configure MCP servers, but Anthropic’s security docs caution that MCP servers should be trusted and that Anthropic does not security-audit or manage every MCP server [Claude Code Security](https://code.claude.com/docs/en/security).

In billing example, this is not theoretical. Suppose an MCP server exposes:

```text
get_customer
list_subscription_events
create_test_checkout_session
replay_webhook
cancel_subscription
update_issue_comment
```

These are not equivalent. `get_customer` may be read-only, but can expose sensitive user data. `create_test_checkout_session` mutates external test environment. `cancel_subscription` is destructive. `update_issue_comment` mutates project communication and can create social/organizational effects. `search_docs` may look harmless, but external docs can carry irrelevant or malicious text into context. Tool names and annotations are useful, but they cannot be the whole boundary.

HumanLayer’s harness material makes the same point from the other side. It warns that adding too many MCP tools can pollute the context and lower agent quality; broad tool catalogs consume attention and make it harder for the agent to choose. HumanLayer’s practical answer is often to use narrower CLIs, skills and controlled hooks rather than wiring every possible service into the agent [HumanLayer, “Skill Issue: Harness Engineering for Coding Agents”](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents). Armin Ronacher pushes a similar idea from his tool philosophy: many tasks are better exposed through composable code/CLI surfaces than through a large fixed MCP catalog [Ronacher, “Your MCP Doesn’t Need 30 Tools: It Needs Code”](https://lucumr.pocoo.org/2025/8/18/code-mcps/).

The final chapter should therefore replace the weak sentence «MCP даёт контекст» with a stricter one: MCP can provide context, but in agentic development it also defines operational rights. Once a tool can act on behalf of the user, it belongs to the runtime rights model.

## Browser/devtools: окно, которое может быть полномочием

For UI work, browser access is often the missing feedback channel. Unit tests can pass while the layout is broken, a stale cache remains visible, an action silently fails, or a console error appears only after a real click. Arvid Kahl’s workflow around Claude Code and Chrome integration is valuable exactly because it makes browser check structured: route, user action, screenshot, DOM clue, console error, network request, then minimal change and recheck [Arvid Kahl, “How to Actually Use Claude Code to Build Serious Software”](https://thebootstrappedfounder.com/how-to-actually-use-claude-code-to-build-serious-software/).

For billing/UI, this matters directly. The agent should open local app, log in as a test user, return to `/billing?checkout_success=true`, watch whether subscription summary endpoint refetches, inspect console errors and confirm that the plan card updates without manual refresh. That is much stronger than “tests passed” when the bug lives in frontend state after a real route transition.

But browser is not a passive viewport. Claude Code’s current Chrome docs say the integration can test web apps, debug console logs, automate form filling and extract data; it opens tabs and shares browser login state, so it can access sites the user is already signed into, including authenticated web apps like Gmail, Notion or Google Docs [Claude Code with Chrome](https://code.claude.com/docs/en/chrome). This is one of the sharpest facts for the chapter. A browser with user session is an authority surface. If the agent can click in a logged-in dashboard, it is not merely “observing the UI”. It can act.

A safe billing run should therefore use a dedicated browser profile, local/staging URL, test user, no password manager, no production admin session, and clear separation between test provider and production provider. If screenshots or browser traces are saved, they should be scoped and reviewed for sensitive data. If the agent needs to complete a CAPTCHA or login, it should stop and ask; not improvise around credentials.

Sandvault’s browser and iOS bridges add another important nuance. Sandvault cannot simply run GUI apps inside its sandbox user, so browser automation is exposed through a host-side headless browser and endpoint such as `SV_BROWSER_ENDPOINT`; iOS Simulator is similarly bridged through `SV_IOS_SIMULATOR_ENDPOINT` [Sandvault repository](https://github.com/webcoyote/sandvault). This shows how execution boundaries often contain designed holes. A bridge through sandbox is not bad; it is often necessary. But it needs its own command set, credentials policy, path restrictions and logging. Otherwise the phrase «sandboxed agent» hides the fact that some actions leave the sandbox through a controlled — or uncontrolled — channel.

## Hooks and sensors: feedback before review

Hooks are where the execution environment begins to answer the agent back. A hook can run a formatter after file edits, block a dangerous command before it runs, scan a prompt, add local context, run tests on stop, notify the user, route an approval, or keep the agent from ending a task too early. They are not review, but they can reduce the amount of low-level review humans must do.

Claude Code’s hooks reference gives the current shape of this mechanism. Hooks can be shell commands, HTTP endpoints or LLM prompts that fire at lifecycle points; they receive JSON context and may return decisions. Events include `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SubagentStart`, `TaskCreated`, `Stop`, `FileChanged`, `WorktreeCreate`, `PreCompact`, `PostCompact`, `SessionEnd` and MCP elicitation events [Claude Code hooks](https://code.claude.com/docs/en/hooks). The docs show a concrete `PreToolUse` hook that matches `Bash`, checks for `rm -rf`, and returns `permissionDecision: "deny"` with a reason. If the script exits silently, normal permission flow continues; silence is not approval.

Codex’s current hook docs add a trust model around hooks themselves: non-managed command hooks must be reviewed and trusted by exact definition/hash; changed hooks are skipped until trusted; `/hooks` lets users inspect, trust or disable them; managed hooks from system, MDM, cloud or requirements sources are trusted by policy and cannot be disabled from the user hook browser [OpenAI Codex hooks](https://developers.openai.com/codex/hooks). This matters because a hook is executable policy. If a repo can smuggle an untrusted hook into the agent environment, the hook becomes part of the threat surface.

Kiro shows the same idea moving into mainstream IDE form. Its agent hooks run predefined agent prompts or shell commands on events such as save/create/delete file, prompt submission, agent turn completion, before/after tool invocation, before/after spec task and manual trigger [Kiro hooks](https://kiro.dev/docs/hooks/), [Kiro hook actions](https://kiro.dev/docs/hooks/actions/). This is not merely convenience automation. It is the environment becoming eventful.

Arvid’s Ralph Wiggum loop is a vivid process example. A stop hook prevents the agent from ending when a checkable promise is not yet met. If the task is “make this page load without console errors” or “fix this failing test”, the hook can push the agent back into the loop until the criterion is satisfied. But this works only when the criterion is narrow and cheap enough to check. For vague goals like “improve architecture” or “make UI nicer”, a stop loop becomes an expensive generator of churn.

Fowler’s harness engineering vocabulary helps separate two families of controls: guides or feedforward controls steer the agent before it acts; sensors or feedback controls observe after it acts and help it self-correct. Some sensors are computational — tests, typecheckers, linters, dependency checks. Some are inferential — another model or evaluator making a judgment [Fowler, “Harness engineering for coding agent users”](https://martinfowler.com/articles/harness-engineering.html). This distinction is useful because a deterministic hook that runs `npm test -- billing` has a different status from a prompt hook that asks another model if the code looks good.

For billing/UI, a reasonable environment might run targeted tests after edits, typecheck the project, run a browser smoke scenario on stop and show failures back to the agent. If the hook fails, the agent continues. If it passes, the result is still not automatically accepted. Hook feedback is part of the execution environment. Review and acceptance remain separate.

## Local harness: scripts, logs and small tools

A chapter about runtime rights can become too defensive: sandbox, approvals, network, secrets. But a useful agent environment is not only a fence. It is also a set of affordances that make the system observable and steerable.

Armin Ronacher’s agentic coding recommendations are useful here because they treat ordinary development scripts as agent-facing tools. A command like `make dev` should not just be convenient for a human who can interpret messy output. It should behave well when called by an agent: be idempotent if possible, fail clearly, avoid spawning duplicate services, write logs to predictable files and expose a cheap `make tail-log` or equivalent [Ronacher, “Agentic Coding Recommendations”](https://lucumr.pocoo.org/2025/6/12/agentic-coding/). Logs are not incidental; they are the agent’s sensory surface.

The same applies to test logins, seed data, local email, webhook replay and observability. Ronacher has described the practical value of making debug email available through stdout/logs: the agent can sign into a test flow without being given a real inbox. This is the right pattern. Do not give the agent a broad credentialed surface when a narrow test affordance solves the problem.

Bad harnesses make agents look worse than they are. If `make dev` hangs forever, prints thousands of lines, starts duplicate services and gives no way to inspect recent logs, the agent wastes context and starts guessing. If a test command fails with a vague message, the model may patch around symptoms. If browser checks require a human-only login path, the agent cannot close the loop. A good harness gives fast errors, clear state and narrow tools.

HumanLayer frames the same problem as model plus harness, not model alone. Its materials list AGENTS/CLAUDE files, MCP, skills, subagents, hooks, back-pressure, context budget and verification as parts of the agent environment [HumanLayer, “Skill Issue”](https://www.humanlayer.dev/blog/skill-issue). The important point for this chapter is narrower: if you want an agent to act safely and productively, you have to build surfaces it can use. A script, log file or CLI can be a better tool than a broad, opaque integration.

For billing/UI, this means a project should ideally have:

```text
make dev
make tail-log
npm test -- billing
npm run typecheck
seed test user
generate test checkout state
replay test webhook
open local billing route with test login
```

The exact commands do not matter. The shape matters. The agent should not need to invent environment control. The project should expose it.

## Worktrees and devboxes: где появляется diff

Once an agent can write, the next question is where its diff lives. A worktree is not a security model by itself, but it is a very good way to isolate parallel writes. Codex app docs describe worktrees as a way to let Codex run multiple independent tasks in the same project without interfering with current local setup; a Git worktree is a second checkout with its own files while sharing repository metadata, and Handoff can move a thread between Local and Worktree [OpenAI Codex app worktrees](https://developers.openai.com/codex/app/worktrees).

Mike McQuaid’s setup shows the interaction of two layers. Sandvault lowers machine/user permissions. Superset/worktrees separate parallel agent tasks. He configures agent commands so Superset launches agents through Sandvault — `sv claude --`, `sv codex --`, `sv gemini --`, `sv opencode --` — and places worktrees under the shared Sandvault path. A `script/bootstrap` prepares a fresh worktree so the agent does not spend the first part of the run fighting missing dependencies [Mike McQuaid, “Sandboxed Agent Worktrees”](https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/).

The practical lesson is simple: worktree is a place for a candidate change. It protects the developer’s current checkout and makes review easier. It does not protect the entire machine, does not automatically hide secrets, does not control network, does not know whether browser session is safe, and does not decide whether the change is correct.

This distinction will matter increasingly in platform-agent environments. A task may start in Slack or an issue tracker; the platform creates devbox/worktree, loads context, runs tools, produces PR and sends it back. Stripe’s public Minions materials point in this direction, although exact architecture and metrics need cautious sourcing because public numbers and article access can differ by context [Stripe Minions Part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents), [Stripe Minions Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2). The safe claim is not “platform agents solve development”. The safe claim is that agent execution is moving into prepared environments where code, tools, tests, PRs and human review are orchestrated together.

Worktree and devbox should therefore sit in the middle of the chapter, not at the end. They are not authority. They are the physical and Git-level place where an attempt becomes a reviewable artifact.

## Workflow runtime: продолжать запуск — не значит продолжать работу

Some agent tasks fit in one interactive session. Many will not. Billing/UI can already become multi-step: prepare worktree, read issue, reproduce locally, patch, run tests, open browser, pause for test API key, call external service, resume, collect artifacts, prepare PR. If the session crashes after creating an external test object, a naive retry can duplicate side effects. If the human approves a network call hours later, the run must resume without losing state.

This is where workflow runtime matters. Shopify Roast is a useful example because it makes an AI step part of an executable workflow rather than the whole workflow. In Shopify’s Boba example, the process for adding Sorbet annotations does not start by asking an agent to “type the project”. It first applies deterministic changes, runs Sorbet autocorrect, inspects remaining errors, then gives `CodingAgent` a specific residual task, and afterwards runs tests/type checks [Shopify Engineering, “Introducing Roast”](https://shopify.engineering/introducing-roast). The public Roast project exposes this general shape through workflow cogs such as `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call` and session resumption/forking [Shopify Roast repository](https://github.com/Shopify/roast).

This pattern is worth naming without turning it into a slogan: deterministic work before the agent, bounded agent work in the middle, deterministic checks after. It is not anti-agent. It is what makes agent work less vague.

Quix’s Klaus Kode story, from the source discovery pass, supports the same direction from a different practice. The team found that exact long sequences in prompts were brittle and that large MCP/tool descriptions could consume a damaging share of context. They moved orchestration into deterministic Python/API calls and used Claude Code for discrete coding steps. The model did not need to own setup, upload, API plumbing and log retrieval when ordinary code could do those things more reliably.

Durable execution frameworks generalize the continuation side. LangGraph supports persistence, interrupts and human-in-the-loop decisions around tool calls. Temporal gives durable workflows, event history, signals, timers and replay. Restate journals steps and side effects so replay can skip completed work. DBOS workflows can resume from the last completed step with workflow IDs for idempotency. These systems are not interchangeable, and this chapter should not compare them. Their common point is enough: they let a run pause, retry, resume and keep execution history.

For billing/UI, a durable workflow might pause when the agent needs test billing credentials, resume after scoped approval, record the created test Checkout Session ID, and avoid creating it again after a crash. This is crucial engineering. But it still does not mean the work is accepted. The workflow can know that step 7 resumed and step 8 passed. It may not know whether the test coverage actually matches the product promise, whether a domain owner accepted the external-service risk, or whether the PR should merge.

That is the boundary between runtime state and work state. Runtime can continue the run. It does not by itself continue the meaning of the work.

## Platform agents and the review bottleneck

At scale, the same mechanisms reappear as a platform. A developer or product person requests a change from Slack, issue tracker or IDE. The system prepares an environment, loads a blueprint or workflow, gives the agent tools, runs checks, creates PR and returns a candidate. This is where Stripe’s Minions are relevant, but they must be used carefully. Public materials and secondary summaries report high PR volumes, but the numbers come from different contexts: Minion-produced PR, AI-assisted PR, merged PR, one-shot merge and human-reviewed PR can mean different things. The important structural claim is not the exact number; it is that agentic code production at large volume shifts pressure from writing toward task selection, environment preparation, evidence, review and policy.

Stripe’s integration benchmark is more directly useful for this chapter than headline PR counts. Stripe built realistic test environments for agents attempting Stripe integrations: code, databases, scripts, test Stripe API keys and deterministic graders that inspect API behavior, UI behavior or Stripe artifacts such as test-mode Checkout Sessions [Stripe, “Can AI agents build real Stripe integrations?”](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations). That is exactly the shape the billing example needs. In payments, “almost right” is not enough. The environment must let the agent interact with a realistic system and then check concrete artifacts.

Stripe’s later steering experiments add another useful point: do not whisper important guidance from a place the agent may never read. If an instruction matters, put it on the path of execution — as loaded context, explicit error, skill, tool intervention or deterministic check [Stripe, “You can’t whisper at an AI agent”](https://stripe.dev/blog/ai-steering-experiments). This is the same principle as hooks and harnesses: if a rule matters, it must be encountered when action happens.

But platformization does not remove authority. A Minion-like or Roast-like system can produce a PR, even many PRs. A PR is a candidate. CI and checks are feedback. A generated summary is a useful wrapper. The project still needs rules about who may merge, which domains require owner review, how AI-generated contributions are disclosed, which changes are too broad, and how to respond when reviewers become the bottleneck. Homebrew’s contribution policy around AI-assisted PRs is useful here because it keeps responsibility with the contributor: disclosure, readiness to respond to review, splitting large PRs and limits on low-quality AI contributions remain social/process gates around the technical runtime [Homebrew CONTRIBUTING](https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md).

The point is not to distrust every agentic PR. The point is to keep the grammar right. The environment can produce candidate changes at high speed. Authority decides what enters the project.

## След запуска ещё не доказательство

At the end of a healthy billing/UI run, the agent may return a lot of useful material:

```text
diff in the worktree
changed files list
command log
test/typecheck/lint output
browser route and screenshot
console/network observations
external test object IDs
approval records
MCP/tool call log
workflow event history
PR summary
known limitations
```

This is a trace of execution. It is valuable. It is not automatically evidence.

For it to become проверочный материал, it must be tied to the promise of the change. The original promise was not «agent ran tests». It was: after a successful checkout return, billing page should show the updated plan without manual refresh, and existing subscription flows should not break. Therefore the relevant material is not all logs, but the subset that answers that claim: test route, test account, endpoint refetch, frontend state update, no console error, targeted regression tests, maybe test-mode Checkout Session or webhook artifact, and clear scope limitations.

This is where chapter IX must hand off to the later chapter about evidence/verification. Runtime can create raw material. It can even structure some of it. But evidence is not just output; it is output interpreted against a claim. A browser screenshot without route, action and state can be decorative. A test pass without a link to the bug can be misleading. A long transcript can hide the absence of the one check that matters.

The same applies to approval. Approval to run `npm test` is not approval to call external billing API. Approval to call test API is not approval to use production credentials. Approval to create a PR is not approval to merge. Green CI is not product acceptance. Hook success is not maintainer review. Workflow completion is not project authority.

This is the final distinction of the chapter: среда исполнения может показать, что агент сделал, где он это сделал, какие границы переходил and what traces remained. But only the next layer links that trace to the promised change, and only the authority layer decides whether the result may enter the project.

## Зачем эта глава нужна всей теории

Agentic development often fails in discussion because people jump from model capability to organizational outcome. The model can write code, therefore maybe it can do the task. The agent can run tools, therefore maybe it can ship. Tests passed, therefore maybe it is correct. A PR exists, therefore maybe the work is done.

The missing middle is execution environment. It is not glamorous, but it is where autonomy becomes usable. It decides how much routine action can proceed without exhausting the human, how narrow the blast radius is when the agent is wrong, what the agent can observe, what it can mutate, where it must ask, how it resumes after interruption and what material a reviewer receives.

The mature question is not «how do we give the agent more access?» It is: which access belongs in the default environment, which access should require scoped approval, which access should be impossible, which observations should be easy, which side effects must be logged, which steps need durable continuation, and where does human authority remain explicit?

A good environment lets the agent move quickly inside known low-risk boundaries. It makes dangerous crossings visible. It exposes the right logs, tests, browser state and tools. It records enough of the run to inspect later. It supports continuation when the run is long. And it does not pretend that any of this replaces evidence or acceptance.

That is the role of execution in the lifecycle of change: not to make the model omnipotent, but to make its action bounded, observable, recoverable and reviewable.
