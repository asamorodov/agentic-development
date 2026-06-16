# 11 — Активный добор после первого черновика

## Статус после перечитывания

Первый полный черновик держит основную ось: много локально разумных агентских действий не образуют управляемый поток; Beads/PWG дают durable work state; Gas Town-like слой обслуживает множество работ; следующий мост ведёт к проверочному материалу. Но после повторного открытия источников и сопутствующих файлов видны несколько недоборов.

1. **Слишком слабо проявлен interface layer Gas Town.** В черновике есть роли и lifecycle, но почти нет `gt feed --problems`, `gt mail`, `gt prime`, convoy и различия между чтением состояния и действием над состоянием. Из-за этого середина местами звучит как концептуальное описание, а не как current-practice surface.
2. **Поддерживающие истории ссылаются только на corpus-файлы.** Для сайта это допустимо, но правило provenance требует не терять внешние источники там, где вводится source-specific факт. Нужно рядом с Jökull, Stripe, Roast и Mae поставить внешние ссылки хотя бы на основные публичные источники.
3. **Недостаточно явно сказано, что visibility без action не решает проблему.** Черновик говорит о видимости и состоянии, но можно сильнее показать различие: dashboard сам по себе не обслуживает поток, если из него нельзя re-sling, defer, close gate, escalate, recover.
4. **Мало честной оговорки о границах Beads/Gas Town.** В финале есть антирекламный тон, но стоит добавить конкретнее: Beads docs сами называют ограничения large teams, real-time collaboration и cross-repo limits; Yegge описывает Gas Town как frontier/hands-on/expensive. Это важно, чтобы не звучало как зрелый стандарт.
5. **Сквозной пример хорошо введён, но исчезает в разделе «Что именно даёт обслуживаемая среда».** Там нужно коротко вернуть `B-101`…`B-106`, чтобы вывод не стал абстрактным.

Ниже — не заметки к будущей правке, а переписанные фрагменты, которые нужно интегрировать в следующий draft pass.

## Переписанный фрагмент 1: расширить раздел «Gas Town как город вокруг рабочих объектов»

### Gas Town как город вокруг рабочих объектов

Gas Town добавляет к Beads/PWG не ещё одно поле задачи, а организационную среду вокруг многих работ. В architecture docs прямо различаются town-level и rig-level beads: town-level слой держит Mayor mail/messages, convoy coordination, strategic issues/decisions, town-level agent beads и role-definition beads; rig-level слой держит bugs/features/tasks, merge requests/code reviews, project molecules и rig-level agent beads ([Gas Town Architecture](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md)). Это почти готовая схема различения между локальной работой проекта и городским обслуживанием потока.

`Rig` можно понимать как рабочую площадку вокруг конкретного репозитория или проекта. В сквозном примере backend, frontend, docs и tests могут быть разными rig или разными рабочими площадками внутри larger rig. Важно не буквальное соответствие, а принцип: работа живёт не в абстрактном пространстве, а в месте, где есть репозиторий, ветка, проверки, исполнители и локальное состояние.

`Convoy` нужен там, где работа проходит через несколько таких площадок. В публичной документации Gas Town convoys описаны как cross-rig tracking, auto-notification и historical record ([Gas Town docs](https://docs.gastownhall.ai/)). Это полезное отличие от обычной зависимости между задачами. Dependency говорит, что одна работа логически ждёт другую; convoy помогает вести движение через несколько rig так, чтобы город видел связанный маршрут, а не отдельные локальные задачи.

`Mayor` — не просто «главный агент». Это поверхность управления. Mayor видит работу, dispatches её, принимает problem feed, получает escalations и соединяет человека с городом. Ролевой шаблон Mayor описывает `gt sling <bead-id> <rig>` как команду work dispatch: spawn polecat, hook work, start session ([Mayor role template](https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl)). Эту команду не обязательно разбирать как CLI-справочник, но она хорошо показывает сдвиг: поручение не остаётся приватным сообщением в чате; оно становится операцией над work item, rig и executor.

Вторая важная поверхность Mayor — не запуск, а чтение проблем. B3 уже фиксировал `gt feed --problems` как характерный образ: агенты группируются по состояниям вроде GUPP Violation, Stalled, Zombie, Working и Idle. Эта деталь нужна в главе, потому что она показывает защиту человеческого внимания. Человек не должен читать все терминалы, чтобы понять, где город горит. Но сама сводка ещё недостаточна: из неё должны следовать действия — re-sling, defer, close gate, escalate, recover, merge, mark fix-needed.

`gt prime` и `bd prime` дают ещё одну грань интерфейса. `bd prime` подаёт агенту Beads work context, а `gt prime` подаёт роль и городскую рамку. Это не «память в голове модели», а повторная загрузка рабочего положения из внешнего состояния. Поэтому continuation в такой среде не равна просьбе «вспомни, что мы делали»; она строится через durable state и role-specific context.

`Polecat` и `Crew` обозначают разные типы исполнителей. Polecat — расходуемый исполнитель дискретной работы; Crew — более долговечная или контекстная форма. Здесь важна фраза из авторского объяснения Steve Yegge: agent is not session; agent role и текущая сессия не одно и то же, потому что сессия может умереть, а работа и роль должны сохраняться ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)). Продолжимость возникает не из магической памяти модели, а из внешних ролей, hooks, beads, mail, history и рабочих площадок.

`gt mail` нужно упомянуть не как главный механизм главы, а как пример канала, который переживает процессные сбои и оставляет след. Если агент просто написал сообщение в терминале, оно легко теряется вместе с сессией. Если сообщение становится частью mail/handoff/state, оно может быть прочитано сервисной ролью, Mayor или следующим исполнителем.

`Witness`, `Refinery`, `Deacon` и `Dogs` показывают, что в многопоточной агентской среде появляются сервисные роли. Они не обязательно создают основную фичу. Они смотрят, возвращают, чинят, сливают, эскалируют, проверяют здоровье среды. В публичной документации Gas Town infrastructure roles включают Mayor, Deacon, Witness и Refinery ([Gas Town docs](https://docs.gastownhall.ai/)). Это не декоративная терминология. Это ответ на тот факт, что параллельность сама себя не обслуживает.

Особенно важен документ о polecat lifecycle patrol. Там появляются операционные события: `RECOVERED_BEAD`, `GUPP_VIOLATION`, `ORPHANED_WORK`, сообщения Witness → Refinery вроде `MERGE_READY`, а также Refinery → Witness вроде `MERGED` и `MERGE_FAILED` ([Gas Town polecat lifecycle patrol](https://github.com/gastownhall/gastown/blob/main/docs/design/polecat-lifecycle-patrol.md)). Эти названия ценны не сами по себе, а потому что показывают форму зрелого состояния. Работа не просто «вроде зависла». Она становится событием, которое может вызвать recovery, re-dispatch, merge handling или escalation.

Gas Town тем самым делает видимым второй этаж. Beads держит работу; Gas Town пытается обслуживать жизнь этой работы в городе.

## Переписанный фрагмент 2: добавить различие visibility / action после раздела «Что именно даёт обслуживаемая среда»

### Видимость без действия ещё не обслуживает поток

У обслуживаемой среды есть два разных режима: читать состояние и менять состояние. Их нельзя смешивать.

Чтение даёт человеку и агентам обзор: problem feed, список ready work, открытый bead, dependencies, gates, PR checks, trace, session log, merge failure, current role context через `gt prime` или work context через `bd prime`. Это защищает от слепоты. Но если среда только показывает dashboard, человек всё равно остаётся диспетчером: он должен вручную решить, кого будить, что перезапускать, что закрывать, что считать ready, что эскалировать.

Действие меняет поток: создать work item, добавить dependency, открыть или закрыть gate, `pin`/`hook` work, `sling` задачу в rig, defer dispatch, re-sling orphaned work, записать `MERGE_FAILED`, создать fix-needed work, acknowledge escalation, re-escalate stale item, закрыть работу. В агентской среде эти операции должны быть привязаны к durable state. Иначе действие снова превращается в свободное вмешательство в чат: агент что-то сделал, но проект не знает, что изменилось.

Поэтому правильная формула не «нужен dashboard» и не «нужен автономный агент». Нужна связка: видимость состояния плюс допустимое действие над этим состоянием. Dashboard без действия — наблюдение хаоса; action без состояния — хаотичная автоматика. Flow service начинается там, где они соединены.

## Переписанный фрагмент 3: усилить вывод через возвращение к сквозному примеру

### Что именно даёт обслуживаемая среда

После прохождения такого цикла проект получает не просто набор ответов агентов. Он получает рабочую картину.

В примере с payment webhook это означает, что `B-101` не просто «где-то делался backend-agent’ом», а имеет состояние: hooked, stalled, recovered, merge-ready или merge-failed. `B-104` не просто содержит черновик документации, а возвращает вывод о replayed payloads в общий граф. `B-105` не становится ready, пока не прошёл CI gate и пока тесты не учли новый риск. `B-103` не идёт в merge до стабилизации backend contract. `B-106` видит не обрывки отчётов, а путь связанных работ: что было сделано, что блокировалось, где была неудача merge, где потребовалось человеческое решение.

Такой проект знает:

- какие work items созданы;
- какие зависимости закрыты;
- что находится на hook;
- что зависло;
- что осиротело;
- где merge failed;
- какие gates ещё блокируют ready;
- где нужен human decision;
- какие полезные выводы вернулись из локальных сессий в Beads/PWG;
- какие ветки можно продолжать;
- что не надо запускать сейчас из-за capacity.

Это и есть предмет главы. В агентской разработке появляется новая инфраструктурная потребность: обслуживать движение рабочих объектов через множество исполнителей и площадок. Если такой среды нет, даже хороший persistent work graph превращается в базу, которую человек вручную сопровождает. Если такая среда есть, человек видит не все подробности всех агентов, а рабочую картину проекта: где поток движется, где стоит, где сломался, где требует решения.

## Переписанный фрагмент 4: заменить supporting stories paragraph прямыми внешними ссылками

### Не только Gas Town: те же функции в других историях

Gas Town даёт самый собранный язык для этой главы, но потребность в обслуживании потока видна не только там.

У Jökull Sólberg маленькая версия той же проблемы появляется вокруг PR. После `push` работа не заканчивается: нужно дождаться CI, разобрать Greptile comments, запустить `codex review --base main`, решить, что исправить, что отклонить, что эскалировать, повторить проверки и дойти до состояния ready to merge. В “Babysitting PRs With Claude Code” он описывает `/babysit-pr` как процедуру сопровождения PR, а в “How I Use Claude Code” — более широкий режим нескольких рабочих потоков, GitHub issues, worktrees, context management and specialized agents ([Babysitting PRs With Claude Code](https://www.solberg.is/babysit-pr); [How I Use Claude Code](https://www.solberg.is/how-i-use-claude-code)). Это не Gas Town, но это тот же сдвиг: человек не должен быть живым таймером между CI, review comments и повторными исправлениями.

У Stripe Minions похожая логика видна на корпоративном уровне. Снаружи запуск может выглядеть как Slack message и emoji reaction; внутри есть route signal, isolated devbox, branch, tools, анализ кода, tests, commit, PR и human review. В ChatPRD-разборе Stripe Minions эта сцена показана как переход от Slack-сообщения к PR через эмодзи-реакцию и подготовленную dev environment, а связанная workflow page раскладывает steps: Slack idea, emoji trigger, isolated cloud environment, agent loop, PR review ([How Stripe’s AI Minions Ship 1,300 PRs Weekly from a Slack Emoji](https://www.chatprd.ai/how-i-ai/stripes-ai-minions-ship-1300-prs-weekly-from-a-slack-emoji); [workflow page](https://www.chatprd.ai/how-i-ai/workflows/how-to-automate-code-generation-from-a-slack-message-into-a-pull-request)). Для главы X отсюда важен не масштаб PR, а платформа вокруг агента: чем автономнее запуск, тем больше обычной инженерной инфраструктуры должно его удерживать.

Shopify Roast показывает соседнюю форму: workflow as code для AI steps. В статье Shopify Engineering Roast представлен как structured AI workflow framework; открытый README показывает Ruby DSL с `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, named outputs and providers; tutorial examples показывают chaining cogs, session resumption, collections and iterative workflows ([Introducing Roast](https://shopify.engineering/introducing-roast); [Shopify/roast README](https://github.com/Shopify/roast/blob/main/README.md)). Roast не заменяет city-level service, но помогает увидеть другой важный принцип: агентская процедура должна быть исполняемым объектом, а не цепочкой устных пожеланий модели.

У Mae Capozzi похожая потребность выражена через worktrees, traces, timeouts, CI, observability and platform constraints. В “How I Use Claude Code to Reduce Toil as a Platform Engineer” она описывает использование Claude Code для рутинной платформенной работы, CI/test PRs, dependency reviews, instrumentation before deploy and cleanup/deletion work ([Mae Capozzi](https://maecapozzi.com/blog/ai-powered-toil-reduction-platform-engineering)). Когда агентских PR и веток становится много, мало получить финальный ответ. Нужно видеть жизненный цикл, время ожидания, зависимые проверки, путь выполнения и место, где работа застряла.

Эти истории не нужно превращать в четыре дополнительных кейса внутри главы. Они подтверждают переносимость проблемы. Gas Town/Beads дают наиболее яркую форму, но за ними стоит более общий сдвиг: агентская разработка переходит от одиночной сессии к обслуживаемой рабочей среде.

## Переписанный фрагмент 5: честнее закрыть ограничения

### Чего такая среда не даёт

Важно закрыть главу не рекламой Gas Town и не обещанием, что городская среда решит все проблемы. Даже если Beads/PWG удерживает work state, Gas Town-like слой обслуживает flow, scheduler не даёт перегрузить систему, escalation возвращает решения человеку, а merge failures не теряются, остаётся следующий вопрос: можно ли доверять результату?

Кроме того, сами текущие источники не позволяют писать о Gas Town/Beads как о зрелом стандарте. Beads docs прямо фиксируют ограничения: large teams, real-time collaboration и cross-repo use требуют осторожности; multi-clone races and sync/recovery concerns остаются инженерной реальностью ([Beads Architecture](https://gastownhall.github.io/beads/architecture)). Авторская статья Steve Yegge описывает Gas Town как frontier/hands-on/expensive режим, а не как спокойную готовую платформу для любой команды ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)). Поэтому ценность Gas Town/Beads для этой главы не в том, что «все будут использовать именно это», а в том, что они называют и собирают правильный класс механизмов.

`B-105` мог пройти CI gate, но это ещё не доказывает, что тесты действительно покрывают replayed webhook payloads. `B-104` мог пройти human gate, но это ещё не значит, что документация не содержит двусмысленности. `B-101` мог быть merged, но это ещё не доказывает, что backward compatibility сохранена. `B-106` может собрать итоговый review, но итоговый review должен опираться на проверочный материал, а не только на статусы потока.

Это граница с главой XI. Глава X показывает, как работа доходит до review/merge path в управляемом состоянии: не потеряв зависимости, gates, failures, partial results, escalations и human decisions. Но сама организация потока не доказывает достаточность результата. Следующий вопрос — какие проверки, артефакты, логи, диффы, тесты, review decisions и другие материалы делают результат заслуживающим доверия и пригодным для передачи дальше.

## Решение для следующего прохода

Следующий draft pass должен не просто добавить эти фрагменты в конец, а встроить их в полный текст:

1. Расширить Gas Town-раздел за счёт convoy, `gt feed --problems`, `gt mail`, `gt prime` и visibility/action distinction.
2. В разделе «Что именно даёт обслуживаемая среда» вернуть пример `B-101`…`B-106`, чтобы вывод не стал абстрактным.
3. Supporting stories переписать с прямыми внешними ссылками и оставить corpus-подробности только как внутреннюю опору.
4. В финале добавить честную оговорку о зрелости/ограничениях Beads/Gas Town.
5. Проверить, что после этих добавлений текст не превращается в справочник команд: каждая техническая деталь должна работать на центральный сбой потока.
