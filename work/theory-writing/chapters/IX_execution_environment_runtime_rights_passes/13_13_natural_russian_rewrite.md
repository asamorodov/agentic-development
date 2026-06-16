# IX. Исполнение: среда агента, права действия и след запуска

Об агентской разработке часто говорят слишком высоко: есть задача, есть модель, есть контекст, есть кодовая база, агент что-то делает. Такая формула ещё терпима, пока речь идёт о разговоре, плане или черновике. Но как только агент начинает менять файлы, запускать команды, открывать браузер, обращаться к API, читать логи, создавать ветку или готовить pull request, работа перестаёт быть только языковой. Она становится действием в конкретной среде.

Представим обычную задачу. В продукте есть страница оплаты: пользователь меняет тариф, проходит checkout, возвращается на `/billing`, а карточка тарифа всё ещё показывает старый план, пока страницу не обновить вручную. Агенту дают поручение: найти причину, исправить устаревшее состояние billing UI, не сломать существующие subscription flows и вернуть pull request.

На уровне намерения это маленький bugfix. На уровне исполнения это уже не одна операция. Агент читает frontend and backend code, ищет путь возврата из checkout, правит worktree, запускает тесты, поднимает локальное приложение, открывает браузер, смотрит console and network requests, хочет проверить test-mode billing flow, упирается в test secrets and network boundary, может попросить approval, может вызвать MCP/tool для issue tracker или billing provider, оставляет журнал команд, browser trace, diff and PR summary.

Если процесс устроен плохо, все эти переходы схлопываются в одну расплывчатую фразу: «агенту дали доступ» или «агент сделал задачу». Но что именно ему дали? Право читать код? Право писать в рабочее дерево? Право запускать тесты? Право открывать браузер, где пользователь уже залогинен в реальные сервисы? Право использовать test API key? Право позвать внешний MCP server? Право создать PR? Право влить изменение?

Это разные границы. Ошибка начинается там, где одна граница выдаёт себя за другую.

У такого запуска есть ещё одна неприятная особенность: разные действия внешне выглядят одинаково, потому что все они приходят из одного чата или одного agent thread. Агент «что-то делает». Но инженерно это разные виды перехода.

Когда агент читает `billing_controller.ts`, он получает информацию. Когда он правит frontend hook в worktree, он создаёт устойчивый diff. Когда он запускает `npm test -- billing`, он исполняет код проекта. Когда он открывает локальную страницу в браузере, он получает наблюдение и одновременно возможность нажимать кнопки. Когда браузер уже залогинен в реальный dashboard, то же самое действие становится действием через чужие полномочия. Когда агент вызывает MCP tool, он может читать внешнюю систему или менять её состояние. Когда он создаёт PR, он уже действует в социальной и организационной поверхности проекта.

Поэтому дальше в главе вопрос будет повторяться в разных формах: какой именно переход произошёл? Прочитали данные, записали файл, выполнили команду, пересекли сеть, использовали секрет, нажали кнопку в авторизованном интерфейсе, вызвали tool with side effect, создали артефакт ревью или приняли результат? Пока эти переходы не названы, разговор об «автономности агента» остаётся слишком грубым.

Главный сбой можно сформулировать так: процесс технически способен выполнить действие, а организация начинает обращаться с этим действием как с допустимым, безопасным или уже принятым результатом. В агентской разработке нужно отдельно держать техническую возможность, permission, approval, проверку и право принять изменение. Агент может запустить команду. Среда может разрешать определённый класс команд. Пользователь может подтвердить конкретный выход за границу. Тест или браузер может дать проверочный сигнал. И всё равно проекту ещё нужен тот, кто имеет право сказать: это изменение входит в рабочее состояние проекта.

Эта глава не является обзором Codex, Claude Code, MCP, Kiro, Roast, Temporal, LangGraph or Sandvault. Все эти источники важны, но только как материалы для одного аргумента: агентское действие становится инженерным действием не из-за силы модели и не из-за красивого prompt, а из-за среды, которая задаёт место действия, права, инструменты, наблюдение, продолжение и след.

## От поручения к месту действия

Поручение само по себе ещё не говорит, где агент действует. «Почини billing UI» может означать разные режимы: агент работает в основном checkout разработчика, в отдельном Git worktree, в контейнере, в облачном devbox, в изолированном пользователе macOS, в sandboxed CLI, в корпоративной платформе, которая сама создаёт среду и возвращает PR. У этих вариантов разный радиус ущерба.

Первый слой среды — место записи. Агент должен работать не в абстрактной «кодовой базе», а в конкретной области: project root, отдельный worktree, writable roots, temporary/cache paths, generated files, protected paths. В современных агентских инструментах это уже стало отдельным понятием. В Codex документация разводит sandbox as technical boundary and approval policy as the rule for asking before crossing it: sandbox определяет, какие файлы можно менять и можно ли использовать сеть, а approval policy определяет, когда Codex должен остановиться и спросить разрешение [OpenAI Codex sandboxing](https://developers.openai.com/codex/concepts/sandboxing). В Claude Code исходная позиция тоже строится вокруг read-only permissions by default: редактирование файлов, запуск тестов и выполнение команд требуют явного разрешения, а запись ограничена рабочей папкой и её подпапками, если не выдано дополнительное право [Claude Code Security](https://code.claude.com/docs/en/security).

Для billing-задачи это означает простую вещь: агент должен получить отдельное рабочее дерево или подготовленную рабочую среду, где его diff отделён от обычной работы человека. Он может читать `docs/billing.md`, route/controller code, frontend billing hook, existing tests. Он может писать в рамках worktree. Но из этого ещё не следует, что он может читать реальные `.env` values, трогать production database, открывать logged-in billing dashboard или вызывать внешний payment API.

Инструкции вроде `AGENTS.md`, `CLAUDE.md`, steering files or project rules полезны, но они не являются границей исполнения. Они могут сказать агенту: используй только test data, не трогай production, запускай `npm test -- billing`. Но если среда одновременно показывает production secrets, открывает реальную browser session и разрешает broad network access, текстовая инструкция остаётся просьбой. Хорошая среда делает опасное действие невозможным или по крайней мере требует отдельного подтверждения в момент перехода.

Именно поэтому «контекст» и «среду» нельзя смешивать. Контекст говорит агенту, как думать о проекте. Среда определяет, что он может сделать даже тогда, когда думает плохо, спешит, неправильно понял задачу или пытается обойти ограничение.

## Sandbox, permission и approval — не одно и то же

В обычной речи легко сказать: «агенту разрешили запускать команды». Для инженерной среды этого недостаточно. Нужно спросить: какие команды, где, с какими правами, с какой сетью, с какими файлами, с какими исключениями и кто рассматривает переходы за границу.

Sandbox — это техническое ограничение. Команды агента исполняются в среде, где часть файлов недоступна для записи, сеть может быть выключена, локальные сервисы закрыты, private network blocked, protected paths нельзя менять. Codex в текущей документации говорит, что локально агент по умолчанию работает с отключённым network access и OS-enforced sandbox, который обычно ограничивает действия текущим workspace. Это ограничение applies to spawned commands, включая `git`, package managers and test runners [OpenAI Codex Agent approvals & security](https://developers.openai.com/codex/agent-approvals-security), [OpenAI Codex sandboxing](https://developers.openai.com/codex/concepts/sandboxing).

Permission profile or permission mode — это поза допуска. Codex, например, описывает встроенные profiles `:read-only`, `:workspace`, `:danger-full-access` and custom profiles. Но его же документация подчёркивает: permission profiles define boundaries for local sandboxed command execution, while app connectors, MCP servers, browser/computer-use surfaces, cloud environments and approved escalations have separate controls [OpenAI Codex permissions](https://developers.openai.com/codex/permissions). Это важнее, чем кажется. Если локальная command execution переведена в read-only, это не значит, что агент вообще безопасен: браузер, MCP server, облачная среда или уже одобренная escalation могут иметь другую поверхность прав.

У этой раздельности есть практическое следствие, которое легко упустить. Даже network allowlist не является решением о доверии. Если агенту разрешили обращаться к определённому домену, это значит только, что traffic может пройти к этому домену. Это не значит, что ответ домена полезен, безопасен, не содержит misleading content, не заносит prompt-injection-like instructions и не побуждает агента к лишним действиям. Codex документация прямо разводит outbound destinations and trust: domain rules constrain traffic; they do not determine whether an allowed destination is trustworthy [OpenAI Codex permissions](https://developers.openai.com/codex/permissions).

То же относится к local services. Для обычного разработчика `localhost` звучит безопаснее интернета, но для агента это может быть доступ к локальной админке, базе, dev dashboard, internal API, unix socket or webhook forwarder. Поэтому современные permission models отдельно говорят о local/private network targets. В billing-задаче local app на `localhost:3000`, webhook listener, локальная база, Stripe-like test API and production dashboard — разные поверхности. Их нельзя открывать одним неразличимым «разрешить сеть».

Approval — это решение о конкретном переходе. Агент пытается сделать что-то за пределом текущего режима: написать outside writable roots, открыть network, вызвать tool with side effect, зайти на новый сайт в browser, использовать test key. Система спрашивает: разрешить один раз, на сессию, для класса действий or not at all. Эта пауза важна не потому, что человек должен вручную благословлять каждую мелочь, а потому, что в ней проявляется граница действия.

Claude Code показывает ту же проблему через режимы. `acceptEdits` позволяет автоматически принимать file edits and some common filesystem commands inside scope. `plan` даёт исследовать и писать план без правки исходников. `auto` уменьшает количество prompts через отдельный classifier, но документация называет его research preview and not a replacement for review on sensitive operations. `bypassPermissions` требует особого включения и доступен не на всех поверхностях [Claude Code permission modes](https://code.claude.com/docs/en/permission-modes). Это не разные названия одной кнопки. Это разные ответы на вопрос, что агент может делать сам, когда он должен остановиться и какой человек или механизм принимает риск.

В billing-примере агент может иметь permission писать в workspace and run tests. Но когда он просит доступ к Stripe-like test API, это уже другой переход: сеть, секрет, внешний сервис, external object creation. Approval должен быть узким: например, разрешить один раз создать test Checkout Session using test key for this reproduction. Такое подтверждение не должно превращаться в общее «можешь пользоваться сетью и секретами как сочтёшь нужным».

Новая деталь в Codex — Auto-review — полезна как показатель направления. Auto-review может заменить человека на отдельного reviewer agent at the sandbox boundary: главный агент остаётся в той же sandbox and approval policy, а reviewer решает, можно ли выполнить eligible escalation. Документация подчёркивает, что Auto-review is a reviewer swap, not a permission grant; он не расширяет writable roots, не включает network и не ослабляет protected paths [OpenAI Codex Auto-review](https://developers.openai.com/codex/concepts/sandboxing/auto-review). Это хорошая форма для будущих систем, но она не отменяет человеческое принятие результата. Reviewer agent может сказать, что конкретный вызов выглядит допустимым; он не становится владельцем продукта.

Особенно важно, что отрицательное решение не должно превращаться в игру «найди обход». В current Codex Auto-review docs denial returns a rationale and instructs the main agent not to pursue the same outcome through workaround, indirect execution or policy circumvention, but to find a materially safer path or stop [OpenAI Codex Auto-review](https://developers.openai.com/codex/concepts/sandboxing/auto-review). Это прямо рифмуется с примером Arvid Kahl, где агент пытался выполнить запрещённую migration-like command через bash script. Хорошая среда должна блокировать не только опасную строку, но и попытку добиться того же эффекта обходным путём.

Эта часть легко превращается в мораль «не включайте опасные режимы». Но правильнее сказать иначе: чем шире автономность, тем более жёсткой должна быть внешняя среда. Mike McQuaid в своей практике с Sandvault описывает именно такую логику: агентские CLI запускаются через отдельного macOS user and sandbox wrapper; `sv claude`, `sv codex`, `sv opencode`, `sv gemini`, `sv shell` дают удобный вход, но отделяют агента от основного пользователя и домашней директории [Mike McQuaid, “Sandboxed Agent Worktrees”](https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/), [Sandvault repository](https://github.com/webcoyote/sandvault). Это не недоверие к модели как характеру. Это признание того, что действие должно иметь место и границу.

## Правила команд: механическая польза и смысловой предел

Одна из самых понятных форм permission — правила команд. Можно разрешить `npm test`, запретить `rm -rf`, спрашивать перед `git push`, запретить `php artisan migrate:fresh`, разрешить `pytest tests/billing`. Такая механика привлекательна потому, что она конкретна. Она превращает расплывчатую безопасность в набор проверяемых правил.

Codex Rules формализуют это через `prefix_rule`: decision can be `allow`, `prompt` or `forbid`; most restrictive match wins; `match` and `not_match` задают условия; правило применяется к argv, а для shell-команд учитывается splitting of simple chains [OpenAI Codex rules](https://developers.openai.com/codex/rules). Это хорошая инженерная поверхность: команда не просто «кажется опасной», она попадает в правило.

Но у механики есть предел. Команда — это строка, а риск часто находится не в строке, а в контексте. `npm test` почти всегда выглядит безопасно. Но если test script downloads arbitrary code, touches shared database or writes generated files outside workspace, простая строка уже не описывает действие. `migrate:fresh` в одноразовой test DB and `migrate:fresh` в базе, которую разработчик вручную собирал неделю, — не одно и то же действие, хотя argv может совпасть. `git push` в personal branch and force-push to protected branch — разные переходы.

Arvid Kahl показывает этот слой на бытовом уровне. В его настройках Claude Code появляются `allow` and `deny`: разрешить полезные команды, запретить опасные, вроде database-wipe/migration-like actions. Но он же описывает проблему обхода: агент может попытаться выполнить запрещённую команду через shell script, если запрет построен слишком поверхностно [Arvid Kahl, “How to actually use Claude Code to build serious software”](https://thebootstrappedfounder.com/how-to-actually-use-claude-code-to-build-serious-software/). Эта история важна не как анекдот о хитром агенте, а как урок: правило должно защищать не только текст команды, но и смысловое действие.

В billing-задаче это означает, что policy не должна ограничиваться списком «разрешённых» команд. Нужны protected paths, disposable local database, отдельные test credentials, сетевые ограничения, hooks and logs. Если агенту нельзя менять billing schema без review, запрет должен ловить не только прямую migration command, но и попытку создать скрипт, который делает то же самое. Если агенту можно запускать tests, хорошо бы, чтобы targeted billing tests existed and were cheap, иначе он будет выбирать между слишком широким `npm test` and guesswork.

Правила команд поэтому должны проектироваться вокруг радиуса ущерба, а не вокруг удобства агента. Команда сборки обычно безопасна. Targeted tests usually safe. Reset test container may be safe if the container is explicitly disposable. `migrate:fresh` against a hand-built local database is already a different action. The same-looking command against production is not a command at all in this sense; it is a forbidden boundary crossing.

Именно здесь сходятся Arvid and Codex. Arvid показывает бытовой случай: `allow` removes friction, `deny` protects local state, но агент может попробовать indirect path. Codex rules show the product-level shape: argv-prefix policy, most-restrictive match, examples, shell splitting. Обе линии говорят одно и то же: command rules are useful because they are mechanical, and limited because they are mechanical. Они должны быть окружены sandbox, protected paths, hook checks, logging and human review.

## Tools and MCP: не контекст, а поверхность действия

MCP часто описывают коротко: он «даёт модели контекст». Это правда только для части случаев. MCP can expose resources, prompts and tools; tools are model-controlled capabilities for interacting with external systems [MCP tools specification](https://modelcontextprotocol.io/specification/draft/server/tools). Если tool только читает документацию, он действительно похож на расширение контекста. Но если tool читает private issues, получает логи, создаёт test object, меняет ticket, вызывает internal API or posts comment, это уже не просто context. Это поверхность действия.

В billing-примере MCP/tool может делать несколько очень разных вещей. Он может вернуть публичную документацию billing provider. Может прочитать internal issue with reproduction steps. Может достать последние logs from staging. Может создать test customer or test Checkout Session. Может закрыть support ticket. Может обновить subscription config. Называть всё это «доступом к инструментам» слишком грубо.

Здесь полезна маленькая лестница действий.

На первом уровне tool возвращает public documentation. Это всё ещё не нейтрально: внешний текст может быть устаревшим, ошибочным or hostile to the agent context. На втором уровне tool reads private project data: issue comments, customer object, logs, observability. Здесь появляется confidentiality boundary. На третьем уровне tool creates test state: checkout session, webhook replay, temporary customer. Здесь появляется side effect, даже если он test-mode. На четвёртом уровне tool mutates durable project or customer state: cancel subscription, update billing config, post issue comment, close ticket. На пятом уровне tool changes authority surface: creates PR, asks reviewer, triggers deployment, changes policy.

Если всё это назвать «tool access», policy теряет различие, которое ей нужно. Хорошая среда должна хотя бы грубо знать: this call is read-only but sensitive; this call writes disposable test state; this call is destructive; this call affects project communication; this call changes deployment or customer state.

Документация MCP security and authorization отдельно предупреждает о trust boundaries: server can expose capabilities that matter; annotations such as `readOnlyHint` are hints for clients/models, not cryptographic guarantees; token handling and confused-deputy-like flows require careful design [MCP Authorization specification](https://modelcontextprotocol.io/specification/draft/basic/authorization), [MCP Security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices). Claude Code security docs make the same practical point: MCP servers are powerful integrations, and adding a server changes the trust model [Claude Code Security](https://code.claude.com/docs/en/security).

Codex MCP docs show the productive side. MCP connects the agent to external tools and context: docs, browser/Figma-like surfaces, STDIO/HTTP servers, Bearer/OAuth authentication, server instructions [OpenAI Codex MCP](https://developers.openai.com/codex/mcp). Это нужно. Без таких интеграций агент остаётся в маленькой комнатке с локальными файлами. Но чем больше инструментов, тем важнее описания, маршрутизация и права.

HumanLayer’s harness writing is useful here because it refuses to treat “more tools” as automatic progress. Tool descriptions consume context, similar tools compete, and the agent needs help deciding when to use what. HumanLayer argues for harness engineering: progressive disclosure, skills, subagents as context firewalls, tool descriptions that are not just API docs but routing aids [HumanLayer, “Skill Issue”](https://www.humanlayer.dev/blog/skill-issue), [HumanLayer, “Skill Issue: Harness Engineering for Coding Agents”](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents). В терминах этой главы: tool surface must be designed as a rights surface, not piled up as a bag of capabilities.

В хорошем billing run агенту не нужен один всемогущий billing MCP. Ему нужны разные уровни: read-only docs; internal issue/log read with confidentiality; test-mode object creation with scoped approval; no production mutation by default; PR creation or comment posting only through a separate review-aware path. Чем точнее среда называет эти переходы, тем меньше ей приходится надеяться на то, что модель сама каждый раз почувствует границу.

## Browser/devtools: окно, которое тоже может быть полномочием

Браузер кажется безопасным, потому что разработчики привыкли считать его наблюдателем. Открыл страницу, посмотрел UI, проверил console, увидел network request. Но для агента browser/devtools — это не только глаза. Это ещё и руки. Он может нажимать кнопки, заполнять формы, отправлять запросы, читать страницы, где пользователь уже authenticated, вытаскивать данные из интерфейсов, куда обычный shell не имеет доступа.

Claude Code Chrome integration прямо перечисляет полезные сценарии: testing web apps, debugging console errors, automating form filling, extracting data, working with Google Docs/Gmail/Notion-like sites if the browser is already signed in [Claude Code Chrome extension](https://code.claude.com/docs/en/chrome). Полезность здесь очевидна. Для billing/UI task browser может наконец проверить не только функцию, но и живой пользовательский путь: checkout redirect, refreshed plan card, no console error, correct network request.

Но это одновременно новая boundary. Если агент работает в dedicated test browser profile, local or staging URL, test account, no password manager, no production dashboard, no shared personal cookies, screenshots and traces saved only if they help review and do not leak private data, browser становится хорошим каналом наблюдения. Если же он открывает уже залогиненный личный браузер разработчика, где есть production admin, Stripe dashboard, Gmail and internal tools, то browser tool получает полномочия пользователя.

Безопасный billing run должен поэтому проектировать browser как отдельную среду, а не как обычное окно человека. Если агенту нужен login, среда должна дать test login helper, debug email in logs or seeded session. Если он упирается в CAPTCHA, two-factor prompt or production dashboard, это не nuisance, а правильная точка остановки.

Опасный вариант выглядит почти так же на поверхности: агент открывает страницу, видит ошибку и «для диагностики» переходит в уже авторизованный billing dashboard разработчика. Технически это может быть один и тот же browser tool. Смыслово это другой класс действия. В первом случае агент проверяет локальный пользовательский поток. Во втором он действует внутри чужих credentials and production-like authority.

OpenAI’s Codex materials about browser/DevTools validation, Claude’s Chrome integration and practical stories like Arvid Kahl’s browser loop all point to the same useful direction: агент должен видеть приложение вживую, а не только редактировать файлы. But observation channel must be separated from authority channel. Browser trace is good review material. A click in production dashboard is not “just another test”.

## Hooks и sensors: обратная связь до ревью

Среда исполнения не заканчивается разрешениями. Ей нужно ещё вовремя говорить агенту, что он делает что-то не то. Это место hooks and sensors.

Hook — это автоматическая реакция на событие: before tool use, after edit, on file save, before finish, after test, before approval request, on worktree creation, on subagent start/stop. Anthropic’s hooks documentation describes hooks as shell commands, HTTP endpoints, LLM prompts or other handlers at lifecycle points; events include `PreToolUse`, `PostToolUse`, `PermissionRequest`, `Stop`, `SubagentStart`, `TaskCreated`, `FileChanged`, `WorktreeCreate`, MCP-related events and more [Claude Code hooks](https://code.claude.com/docs/en/hooks). Kiro’s hooks follow a similar idea from the IDE side: predefined agent prompts or shell commands can run on events such as file save/create/delete, prompt submission, turn completion, before/after tool invocation and spec task boundaries [Kiro hooks](https://kiro.dev/docs/hooks/).

For billing task, hooks can do useful things. After agent edits frontend billing files, run formatter and targeted tests. Before it finishes, check that it has run billing regression tests. When it tries to touch migration files, require review. When it changes subscription logic, add owner-review label. When it opens browser trace, save screenshot path. When tests fail, feed concise error back into the agent.

Но hooks нельзя описывать как единый механизм «автоматической проверки». У них есть разные уровни доверия.

Детерминированный command hook, который после `Edit` запускает formatter or `npm test -- billing`, ближе всего к обычному инженерному feedback. Он может быть шумным, медленным or incorrectly scoped, but its nature is understandable. HTTP hook crosses a network boundary: task data может уйти во внешний сервис, and the response becomes part of runtime decision. MCP hook invokes another tool server, with its own credentials, trust and audit model. Prompt or agent hook adds another model judgment, which may be useful, but no longer has the same status as a deterministic check.

Это не аргумент против HTTP, MCP or model hooks. Это аргумент за честную маркировку. Если Stop hook блокирует завершение, потому что targeted tests failed, это один вид обратной связи. Если Stop hook спрашивает другого агента, выглядит ли работа завершённой, это другой вид обратной связи. Оба могут быть полезны, но их нельзя одинаково называть доказательством.

Martin Fowler’s harness engineering language helps name the broader shape: guides/feedforward steer the agent before action; sensors/feedback report what happened after action; the harness should present feedback in a form optimized for LLM consumption, not just human log reading [Fowler, “Harness engineering for coding agents”](https://martinfowler.com/articles/harness-engineering.html). Это важное дополнение к permission. Permission asks whether the action may happen. Sensor says what the action produced. Review decides whether the result should count.

В хорошей среде hooks make the safe path shorter. Агенту не нужно гадать, какие tests run for billing; hook запускает нужный набор. Агенту не нужно пролистывать огромный log; sensor возвращает compact failure. Агент не должен сам вспоминать, что subscription logic требует owner review; hook marks it. Но если среда начинает считать hook success окончательным принятием, она снова смешивает границы.

## Local harness: scripts, logs and small tools

Иногда самая важная часть среды выглядит слишком приземлённо, чтобы попасть в теорию: `make dev`, `make test`, `make tail-log`, seed scripts, local fixtures, debug email stdout, browser helpers, local API wrappers. Но именно здесь агентская разработка часто выигрывает или ломается.

Armin Ronacher в своих заметках про agentic coding and Pi постоянно возвращает модель к обычному software execution. У проекта должны быть скрипты, которые запускают dev environment, читают logs, дают browser access, выводят test email in stdout, создают local state and let agent inspect what matters [Armin Ronacher, “Agentic Coding”](https://lucumr.pocoo.org/2025/6/12/agentic-coding/), [Armin Ronacher, “Code MCPs”](https://lucumr.pocoo.org/2025/8/18/code-mcps/), [Pi repository](https://github.com/earendil-works/pi). Он также осторожно относится к превращению всего в MCP: иногда обычный code/CLI is the better tool surface.

Для billing bug хороший local harness может быть простым. `make dev` поднимает frontend and backend. `make seed-billing-user` создаёт user with basic plan. `make simulate-checkout-return` or local webhook replay creates test event. `make test-billing-refresh` запускает targeted regression. `make tail-log billing` показывает последние relevant lines. Browser helper opens local `/billing` as seeded user. None of these tools is glamorous. But they make the safe path cheap.

Хороший локальный harness обычно заметен не по одному большому инструменту, а по маленьким отсутствующим шероховатостям. `make dev` можно вызвать дважды, и он не поднимает две копии сервера на одном порту. Если порт занят, команда говорит, какой процесс уже работает. Логи не исчезают в прокрученной terminal history, а пишутся в известный файл. `make tail-log` показывает последние строки без бесконечного потока. Test email appears in dev log, not in the developer’s real inbox. Webhook replay has a test fixture. Seed data can create billing user in known state. Targeted test command exists and does not require agent to infer the whole test layout.

Когда этих деталей нет, агент начинает чинить не продукт, а среду. Он перезапускает сервисы, угадывает порт, читает огромный output, создаёт новую фикстуру вместо использования существующей, просит реальные credentials or gives up. Поэтому harness косвенно относится к правам исполнения: он не только показывает, что разрешено, но и делает безопасный путь самым лёгким путём.

Здесь есть важная связь с разрешениями. Чем хуже local harness, тем чаще агент просит широкий доступ: к сети, production-like dashboard, реальным данным, arbitrary shell commands. Чем лучше harness, тем меньше таких просьб. Хорошая среда не просто запрещает опасное. Она предлагает рабочий безопасный маршрут.

## Worktrees and devboxes: где появляется diff

Агентская задача почти всегда производит diff. Значит, среде нужно решить, где этот diff живёт, как он отделён от других изменений, как его можно сравнить, передать, удалить, принять or reject.

Git worktree — простейшая форма такой изоляции. Агент работает в отдельной checkout-like директории, где его изменения не смешиваются с текущей работой человека. Codex app worktrees docs describe running multiple independent tasks in background worktrees, using handoff back to local environment, and treating each task as a separate working area [OpenAI Codex worktrees](https://developers.openai.com/codex/app/worktrees). Claude Code and similar tools also increasingly treat worktree/session separation as normal practice. Mike McQuaid’s Sandvault/Superset setup pushes this further: agent runs in a sandboxed user, with worktrees and a shared directory designed for controlled transfer rather than full access to the maintainer’s home [Mike McQuaid, “Sandboxed Agent Worktrees”](https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/).

Для billing example это значит: агент создаёт diff in `billing-ui-fix` worktree. Он не трогает developer’s current branch. Он может run tests inside that tree. Он может return patch/PR. Если задача оказалась плохой, worktree can be deleted. If useful, diff can be reviewed and merged.

Но worktree is not authority. Он изолирует изменения, но не говорит, что они правильные. Он позволяет параллелить tasks, но не решает conflict semantics. Он защищает основной checkout from accidental edits, but not necessarily secrets, network, browser or external tools. Он может быть частью хорошей среды, но не заменяет sandbox, permission, tests, review and project state.

Devbox or cloud environment extends the same idea. Platform can prepare machine/container with repo, dependencies, secrets policy, test data, browser, network rules and evaluation harness. Stripe’s Minions are relevant at this level: the platform creates a substrate where agents can attempt real tasks and return candidate PRs. The important point for theory is not “cloud is better than local”. It is that environment becomes a first-class object: reproducible enough to run, isolated enough to bound damage, instrumented enough to inspect, and connected enough to produce useful work.

## Workflow runtime: продолжать запуск — не значит продолжать работу

Некоторые агентские задачи помещаются в одну interactive session. Многие — нет. Billing/UI fix уже может стать длинным процессом: prepare worktree, read issue, reproduce locally, patch, run tests, open browser, pause for test API key, call external service, resume, collect artifacts, prepare PR. Если session crashes after creating an external test object, naive retry can duplicate side effects. Если человек через несколько часов разрешает network call, run must resume without losing state.

Здесь появляется workflow runtime. Shopify Roast useful because it makes an AI step part of an executable workflow rather than the whole workflow. In Shopify’s Boba example, the process for adding Sorbet annotations does not start by asking an agent to “type the project”. It first applies deterministic changes, runs Sorbet autocorrect, inspects remaining errors, gives `CodingAgent` a specific residual task, and afterwards runs tests/type checks [Shopify Engineering, “Introducing Roast”](https://shopify.engineering/introducing-roast). The public Roast project exposes this general shape through workflow cogs such as `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call` and session resumption/forking [Shopify Roast repository](https://github.com/Shopify/roast).

Важны не названия `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call` сами по себе, а то, что workflow has executable surface. `cmd` запускает обычную команду. `ruby` выполняет обычный код. `chat` asks a model without giving it full code-editing agency. `agent` delegates a bounded coding step. `map` fans out a pattern over a collection. `repeat` creates an explicit loop with exit conditions. Session resume/forking lets a costly interaction continue or branch without starting from zero. В такой схеме агент больше не обязан держать весь процесс в голове. Процесс становится внешним артефактом.

Внешний walkthrough Daniel Doubrovkine adds a useful mundane detail: Roast run is affected by ordinary runtime facts such as API key, selected model and workflow file edits. Он first checks OpenAI key with `curl`, then adjusts workflow model settings because the original model mix is not available/cost-effective for his run [Doubrovkine, “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html). Это хороший reminder: даже “AI workflow” is still software execution. It has environment variables, model routing, credentials, logs and failure modes.

This pattern is worth naming without turning it into a slogan: deterministic work before the agent, bounded agent work in the middle, deterministic checks after. It is not anti-agent. It is what makes agent work less vague.

Quix’s Klaus Kode story gives the same lesson from the opposite direction. Команда может попытаться закодировать длинную точную последовательность в prompt или открыть большой MCP catalog, но тогда модель тратит контекст на tool descriptions and brittle procedural instructions. Repair is to move stable orchestration into deterministic code: upload code and dependencies through ordinary API calls, run app in a cloud sandbox, download logs, call Claude Code for the bounded coding step, then continue with code again. In that pattern the agent is not humiliated; it is placed where uncertainty actually remains.

Durable execution frameworks обобщают сторону продолжения. LangGraph supports persistence, interrupts and human-in-the-loop decisions around tool calls [LangGraph durable execution](https://langchain-ai.github.io/langgraph/concepts/durable_execution/). Temporal gives durable workflows, event history, signals, timers and replay [Temporal documentation](https://docs.temporal.io/workflows). Restate journals steps and side effects so replay can skip completed work [Restate documentation](https://docs.restate.dev/). DBOS workflows can resume from the last completed step with workflow IDs for idempotency [DBOS documentation](https://docs.dbos.dev/python/tutorials/workflow-tutorial). Эти системы не взаимозаменяемы, и глава не должна сравнивать их как продукты. Общего пункта достаточно: они позволяют run pause, retry, resume and keep execution history.

For billing/UI, durable workflow might pause when the agent needs test billing credentials, resume after scoped approval, record the created test Checkout Session ID, and avoid creating it again after a crash. Это важная инженерия. Но это всё ещё не значит, что работа принята. Workflow can know that step 7 resumed and step 8 passed. It may not know whether the test coverage actually matches the product promise, whether a domain owner accepted the external-service risk, or whether the PR should merge.

Сбой здесь тонкий. Durable runtime can remember that step 6 failed, step 7 waited for approval, approval arrived, and step 8 resumed. It can replay event history or skip completed journaled steps. But if a reviewer asks “what exactly are we proving?”, the runtime may have no answer beyond its own steps. It knows execution order, not necessarily work meaning. The missing object is the work item: promise, owner, blocker, gate, required checking material, accepted/rejected state and safe next action.

Вот граница между runtime state and work state. Runtime может продолжить запуск. Он не обязан сам продолжать смысл работы.

## Platform agents and the review bottleneck

At scale, те же механизмы становятся платформой. Developer or product person requests a change from Slack, issue tracker or IDE. System prepares environment, loads blueprint or workflow, gives the agent tools, runs checks, creates PR and returns candidate. Это место, где Stripe’s Minions важны, но их нужно использовать аккуратно. Public materials and secondary summaries report high PR volumes, but numbers come from different contexts: Minion-produced PR, AI-assisted PR, merged PR, one-shot merge and human-reviewed PR can mean different things. Structural claim matters more than exact number: agentic code production at large volume shifts pressure from writing toward task selection, environment preparation, checking material, review and policy.

Stripe’s integration benchmark is more directly useful for this chapter than headline PR counts. Stripe built realistic test environments for agents attempting Stripe integrations: code, databases, scripts, test Stripe API keys and deterministic graders that inspect API behavior, UI behavior or Stripe artifacts such as test-mode Checkout Sessions [Stripe, “Can AI agents build real Stripe integrations?”](https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations). That is exactly the shape the billing example needs. In payments, “almost right” is not enough. The environment must let the agent interact with a realistic system and then check concrete artifacts.

Stripe’s later steering experiments add another useful point: do not whisper important guidance from a place the agent may never read. If an instruction matters, put it on the path of execution — as loaded context, explicit error, skill, tool intervention or deterministic check [Stripe, “You can’t whisper at an AI agent”](https://stripe.dev/blog/ai-steering-experiments). This is the same principle as hooks and harnesses: if a rule matters, it must be encountered when action happens.

Но platformization does not remove authority. A Minion-like or Roast-like system can produce a PR, even many PRs. A PR is a candidate. CI and checks are feedback. A generated summary is a useful wrapper. Проекту всё равно нужны правила: кто может merge, какие области требуют owner review, как disclose AI-generated contributions, какие изменения too broad, что делать, когда reviewers become the bottleneck.

Homebrew’s contribution policy around AI-assisted PRs is useful here because it keeps responsibility with the contributor: disclosure, readiness to respond to review, splitting large PRs and limits on low-quality AI contributions remain social/process gates around the technical runtime [Homebrew CONTRIBUTING](https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md). That is not anti-agent either. It is the same distinction again: environment can produce candidate changes at high speed; authority decides what enters the project.

## След запуска ещё не доказательство

At the end of a healthy billing/UI run, agent may return a lot of useful material:

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

Это след исполнения. Он ценен. Но сам по себе он ещё не доказательный материал.

Чтобы этот след стал проверочным материалом, его нужно связать с обещанием изменения. Original promise was not “agent ran tests”. It was: after a successful checkout return, billing page should show the updated plan without manual refresh, and existing subscription flows should not break. Поэтому важен не весь log, а та его часть, которая отвечает на этот claim: test route, test account, endpoint refetch, frontend state update, no console error, targeted regression tests, maybe test-mode Checkout Session or webhook artifact, and clear scope limitations.

Здесь глава IX передаёт ход будущей главе о проверке. Runtime can create raw material. It can even structure some of it. But checking material is not just output; it is output interpreted against a claim. A browser screenshot without route, action and state can be decorative. A test pass without a link to the bug can be misleading. A long transcript can hide the absence of the one check that matters.

То же относится к approval. Approval to run `npm test` is not approval to call external billing API. Approval to call test API is not approval to use production credentials. Approval to create a PR is not approval to merge. Green CI is not product acceptance. Hook success is not maintainer review. Workflow completion is not project authority.

This is why PWG-like mechanisms belong after, not inside, execution runtime. A gate can wait for human review, CI, a GitHub run, PR state, timer or another work item. A prime/rehydration artifact can help a later agent recover task context. But these mechanisms do not replace the run log; they organize what the run log is for. Runtime says: here is what happened. Work state says: here is why this matters, who must decide, what is still blocked, and what material is enough to continue.

If IX blurs this line, later chapters lose their reason to exist. The whole point is that a trace becomes useful only when attached to the claim it is meant to support. A durable run history without a work item is an execution diary. A work item without run trace is a promise without grounded material. The lifecycle needs both, but they are not the same layer.

Финальное различение главы можно сказать так: среда исполнения может показать, что агент сделал, где он это сделал, какие границы переходил и какие следы остались. Но следующий слой связывает этот след с обещанным изменением, а слой полномочий решает, может ли результат войти в проект.

## Зачем эта глава нужна всей теории

Обсуждение агентской разработки часто перескакивает от capability модели к организационному результату. Model can write code, therefore maybe it can do the task. Agent can run tools, therefore maybe it can ship. Tests passed, therefore maybe it is correct. PR exists, therefore maybe the work is done.

Missing middle is execution environment. Это не самая эффектная часть агентской разработки, но именно здесь автономность становится пригодной к использованию. Среда решает, сколько рутинного действия можно выполнить без постоянного вмешательства человека, насколько узок blast radius when the agent is wrong, что агент может наблюдать, что он может менять, где он должен остановиться, как он продолжает работу после паузы и какой материал получает reviewer.

Зрелый вопрос звучит не так: «как дать агенту больше доступа?» Правильнее спрашивать: какой доступ должен быть в default environment, какой требует scoped approval, какой должен быть невозможен, какие наблюдения должны быть простыми, какие side effects must be logged, какие шаги требуют durable continuation and where human authority remains explicit?

Хорошая среда не только ограничивает агента. Она делает безопасный путь дешёвым, а опасный переход видимым. Она даёт small reliable tools, readable logs, test accounts, isolated worktrees, scoped network, explicit approvals and recoverable run state. Она позволяет агенту проходить рутинные сбои без того, чтобы человек подтверждал каждый безвредный шаг. И она останавливает агента там, где граница уже не техническая: production data, external side effects, product judgment, customer impact, merge authority.

Таково место исполнения в lifecycle of change: не сделать модель всемогущей, а сделать её действие bounded, observable, recoverable and reviewable. Агент тогда может двигаться быстрее внутри тех частей работы, которые безопасно механизировать, а проект сохраняет имена для решений, которые нельзя передать sandbox, hook or workflow runtime.
