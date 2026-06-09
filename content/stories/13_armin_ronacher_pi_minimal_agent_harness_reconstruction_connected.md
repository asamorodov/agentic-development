# Armin Ronacher: маленький изменяемый harness, файловая память и человеческое владение агентской работой

История Armin Ronacher не сводится к тому, что сильный инженер начал много пользоваться Claude Code. Если читать её так, она быстро смешается с уже написанными историями про skills, hooks, MCP, worktrees и внешнюю память. В корпусе у неё другая роль: Ronacher показывает, как опытный автор инфраструктурных инструментов постепенно переносит агентскую работу из слоя “модель умеет писать код” в слой маленькой локальной среды, которую агент может читать, расширять, чинить и использовать как обычный код.

Эта история стоит рядом с Mark Erikson, Jesse Vincent, HumanLayer и Matt Pocock, но не повторяет их. У Mark важна файловая операционная среда вокруг сессий и внешней памяти. У Jesse — набор процедур, skills и проверочных шлюзов, которые дисциплинируют Claude Code. У HumanLayer — harness как место, где autonomy ограничивается контекстом, правами и обратным давлением. У Pocock — маленькие repairable skills для повторяемых сбоев. У Ronacher центральный ход другой: если агент всё равно умеет читать, писать и запускать код, то рабочая среда агента должна быть как можно ближе к коду. Не тридцать специально описанных инструментов, не огромный постоянный MCP-слой, не монолитная методология, а маленькое ядро, файловое состояние, shell, JSON, scripts, локальные расширения и человеческая ответственность за всё, что машина выносит наружу.

У этой истории есть и обратная сторона. В собственном окружении Ronacher может использовать агентов агрессивно: запускать Claude Code почти без разрешений, давать агенту читать логи, писать отладочные scripts, строить расширения для Pi, разбирать issues параллельно, закрывать работу через scripted wrap-up. Но в open source тот же объём машинно-сгенерированной работы превращается в чужой review debt. Поэтому история Ronacher не про “больше автоматизации всегда лучше”. Она про более точную границу: внутри контролируемого harness агентская работа становится мощной; снаружи, без владения, проверки и ответственности, она превращается в шум, который должен быть отфильтрован до того, как попадёт к maintainer.

## 1. Вход в агентский режим: не новый редактор, а новое распределение внимания

Весной 2025 года Ronacher уже не был человеком, которому нужно было объяснять, зачем нужны автоматизация, тесты, командная строка и маленькие рабочие инструменты. До агентского поворота у него уже была привычка превращать повторяемое действие в код: не терпеть ручную процедуру, если её можно выразить как script, CLI, локальный helper или маленький сервис. Поэтому его переход к coding agents важен не как sudden conversion, а как продолжение старого инженерного инстинкта: если в рабочем процессе появился новый повторяемый исполнитель, среду нужно перестроить так, чтобы этот исполнитель получал хороший сигнал.

В статье [“AI Changes Everything”](https://lucumr.pocoo.org/2025/6/4/changes/) Ronacher описывает состояние после нескольких месяцев интенсивной работы с Claude Code не как “я иногда прошу модель написать функцию”, а как почти новый режим разработки. Он пишет, что теперь большую часть времени использует Claude Code в hands-off режиме: даёт системе задачу, переключается на другую работу, возвращается к результату, review, затем задаёт следующий шаг. Он оценивает выигрыш не как десятикратное ускорение, а примерно как увеличение продуктивного времени: если раньше день был ограничен человеческим вниманием, то теперь часть работы может идти, пока он читает, проверяет или думает о другом.

Это принципиальная разница с ранним chat-assisted coding. Агентская работа становится не “ответом модели в окне”, а циклом распределения внимания. Человек больше не обязательно сидит внутри каждой строки. Он задаёт направление, получает промежуточные артефакты, проверяет, отбраковывает и снова запускает. Но чтобы такой цикл не развалился, агенту нужна среда, где он может безопасно и быстро получать обратную связь: запускать тесты, читать logs, видеть состояние, менять files, использовать shell, а не только продолжать текстовый диалог.

В [интервью Syntax](https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript) Ronacher описывает более личную точку входа. После ухода из Sentry у него появилось много свободного времени, и в мае 2025 он провёл ночной эксперимент с Peter Steinberger и Mario Zechner: они делали “crazy stuff” с Claude, пробовали агентные подходы и быстро попали в режим, где модель не просто отвечает, а действует через tools. Важна не романтика all-nighter, а то, что после него Ronacher начал смотреть на agent harness как на программируемую рабочую поверхность. Если агент может читать, писать, запускать команды и расширять инструменты, значит, вопрос уже не только в prompts. Вопрос в том, какой environment дать этому агенту.

Здесь начинается отличие от многих историй корпуса. Boris Tane показывает, как документ становится поверхностью решения перед кодом. Peter Steinberger показывает быстрый разговорный режим для небольшого радиуса. Simon Willison показывает research spikes и проверяемые артефакты. Ronacher же движется к другой точке: рабочая среда сама должна стать частью программы, которую агент может изменять.

## 2. Июньский Claude Code режим: shell, logs, tests и почти полный доступ

Через несколько недель после этого входа Ronacher публикует [“Agentic Coding Recommendations”](https://lucumr.pocoo.org/2025/6/12/agentic-coding/). Это не обзор инструмента, а практическая инструкция по тому, какие свойства кодовой базы и окружения делают агентскую работу более устойчивой.

Тон статьи сразу снимает иллюзию, что всё решается prompt engineering. Ronacher говорит не “напишите лучший запрос”, а “подготовьте систему так, чтобы агент мог действовать”. Он использует Claude Code Max, предпочитает Sonnet из-за скорости и token efficiency, редко прерывает агента и почти не полагается на IDE как центральную поверхность. IDE остаётся для финального polish, но основная работа идёт через terminal/harness. Агент читает файлы, запускает команды, проверяет гипотезы и видит ошибки.

Показательно, что Ronacher запускает Claude Code в режиме, который сам называет опасным, но продуктивным: с `--dangerously-skip-permissions`. У него есть alias вроде `claude-yolo`. Это не рекомендация для любого окружения; это показатель того, насколько сильно он смещает работу внутрь локальной trust boundary. Если репозиторий и машина контролируются, а задача требует много мелких операций, постоянные разрешения становятся трением. Он предпочитает дать агенту широкий локальный доступ, а риск контролировать архитектурой окружения, тестами, Git и собственным review.

Минимальный operational pattern выглядит примерно так:

```bash
claude --dangerously-skip-permissions
```

или через alias:

```bash
claude-yolo
```

Сама команда не является “методом”. Метод начинается вокруг неё: проект должен иметь понятные команды запуска, быстрые tests, читаемые logs, простой способ поднять dev environment и минимальное количество скрытого знания. Если агенту нужно постоянно спрашивать, как запустить сервис, где лежит log, почему тесты падают от уже запущенного процесса или как достать последние события из Sentry, harness не работает.

В этой статье появляются несколько принципов, которые потом перейдут в Pi.

Первый принцип: агентам нравится explicit context. Ronacher отдельно выделяет Go как язык, который хорошо ложится на агентскую работу: явные типы, простой control flow, быстрые тесты, мало магии. Python для него в этом режиме сложнее не потому, что плох как язык вообще, а потому что часто несёт скрытые механики: fixture injection в pytest, event loop, startup cost процесса, более неявное runtime-поведение. Агент может работать и там, но ему труднее предсказать, что именно произойдёт при запуске.

Второй принцип: проект должен иметь commands, которые агент может запускать без человеческого перевода. Ronacher приводит pattern с `Makefile`: `make dev`, `make test`, `make tail-log`, отдельные команды для background services и logs. Если `make dev` падает потому, что services уже запущены, это плохая команда для agent harness. Агент не должен угадывать, означает ли ошибка real failure или “всё уже работает”. Если debugging email уходит в browser или external service, агент его не увидит; если email пишется в stdout/log, агент может его прочитать.

Третий принцип: permissions should be local. Если проверка прав размазана по framework, middleware, remote service и implicit state, агенту труднее понимать последствия изменения. Если permission check — локальная функция рядом с кодом, которую можно прочитать, вызвать и покрыть тестом, агент может работать с ней почти как человек.

Четвёртый принцип: plain SQL лучше скрытой магии ORM там, где агенту нужно увидеть реальную shape of data. Это не идеологический запрет на ORM. Это практический критерий: чем больше важной логики находится в неочевидных conventions, тем больше агент будет hallucinate или пропускать constraints.

Все эти пункты сходятся в одну формулу: agent-friendly codebase — это не кодовая база “для ИИ”. Это кодовая база с хорошими seams, быстрым feedback, читаемой runtime surface и малым количеством скрытой магии. Агент просто делает цену плохой инженерной среды видимой быстрее.

## 3. Быстрый feedback как часть harness, а не как “потом проверим”

У Ronacher обратная связь должна быть встроена в саму работу агента. Это хорошо видно в его практических рекомендациях: тесты должны запускаться быстро; logs должны быть доступны через shell; dev server не должен вести себя как загадочный singleton; email, Sentry events и другие external signals нужно уметь превратить в локальные файлы или stdout.

Такой подход отличается от простого “пусть агент напишет код, а человек потом проверит”. Если агент не видит результатов запуска, он работает как autocomplete с большим контекстом. Если видит, он может построить цикл: изменить, запустить, прочитать ошибку, сузить гипотезу, снова изменить. Для человека это выглядит как более самостоятельная работа, но самостоятельность появляется не из доверия к модели. Она появляется из плотности signals.

Ronacher особенно ценит тот тип сигналов, который агент может обработать программно. Текстовый stack trace лучше расплывчатого описания сбоя в UI. JSON лучше скриншота, если задачу нужно фильтровать и сопоставлять. Log tail лучше ручного описания “там что-то упало”. CLI лучше закрытого dashboard, если у dashboard нет scriptable доступа. Всё это потом станет частью его аргумента против чрезмерного MCP tool explosion: не каждую внешнюю систему нужно заворачивать в 30 специальных tools. Иногда агенту достаточно shell, auth и права написать маленький script.

Здесь есть важная связка с историей Simon Willison. Willison делает проверяемые research artifacts: transcripts, Showboat documents, benchmarks, reproductions. Ronacher делает похожий перенос на runtime loop: если агент может производить и читать проверочные артефакты в filesystem, часть reasoning перестаёт быть чисто текстовой. Она становится observable work.

## 4. Что не прижилось: slash commands, hooks, print mode и subagents как шум

Ronacher не романтизирует любые новые функции agent tools. В [“Agentic Coding Things That Didn’t Work”](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/) он описывает неудачные попытки автоматизации. Это важный слой истории, потому что Pi позже выглядит не как “ещё один framework”, а как результат удаления того, что не окупилось.

Его правило простое: автоматизировать стоит только то, что повторяется. Если command, hook или helper не используется, он должен быть удалён. Иначе среда агента превращается в кладбище instructions. Для человека лишний command — просто лишний пункт в списке. Для агента это ещё и потенциальный источник неверного выбора: модель видит команду, не понимает её статус, применяет не туда или начинает пытаться чинить процесс, который давно устарел.

Slash commands казались естественным местом для локальных процедур, но на практике оказались грубыми. У них были ограничения discoverability и composition; им не хватало autocomplete по файлам; они часто превращались в длинные prompts, которые приходилось объяснять заново. Один из работавших примеров — command для grammar cleanup: он начинался с `git status`, требовал работать с pending/untracked files, делать backup `.bak`, чистить existing backup и применять правки к указанным файлам. Но даже здесь видно, что slash command работает как текстовая оболочка над shell/Git дисциплиной, а не как настоящий программный интерфейс.

Более характерны failed commands. Ronacher перечисляет попытки вроде `/fix-bug`, `/commit`, `/add-tests`, `/fix-nits`, `/next-todo`. Они выглядят заманчиво, потому что соответствуют частым задачам, но именно поэтому слишком широки. `/fix-bug` не знает, какая diagnosis уже выполнена. `/commit` легко нарушает Git hygiene. `/add-tests` не понимает test strategy. `/next-todo` начинает управлять вниманием вместо человека. В итоге такие команды не сокращают работу, а добавляют слой ложной определённости.

Hooks тоже не стали универсальным решением. Ronacher работал в yolo mode, где Claude Code почти всё разрешено, и хотел использовать hooks как способ подправлять поведение. Но hooks в Claude Code тогда были в основном механизмом deny/observe, а не полноценным programmable policy layer. Попытка заставить агента использовать `uv` через hook оказалась слабой. Более надёжным оказался старый Unix-приём: подложить в `PATH` перехватчик, который срабатывает, когда агент вызывает неправильный executable.

Условный sketch такого interceptor выглядит так:

```bash
#!/bin/sh
echo "This project uses uv, please use 'uv run python' instead."
exit 1
```

А запуск harness меняет `PATH` так, чтобы `.claude/interceptors` шёл первым:

```bash
PATH="$(pwd)/.claude/interceptors:${PATH}" claude --dangerously-skip-permissions
```

Смысл не в конкретном `uv`. Смысл в том, что надёжная steering-поверхность иногда проще и грубее, чем официальный hook API. Агент думает, что запускает обычную команду, но локальная файловая среда возвращает ему понятный сигнал. Это ближе к operating-system trick, чем к prompt engineering.

`--print` mode тоже не стал базовым инструментом. На бумаге он хорошо подходит для workflows, где 90% задачи deterministic, а 10% требует inference. Но Ronacher обнаружил, что такие runs трудно debug, они медленные, а failure surface плохо видна. Subagents полезны для investigations и context isolation, но смешение read/write задач между несколькими агентами быстро создаёт хаос. В таких случаях он часто предпочитает fresh sessions, markdown notes, отдельные context chunks или вообще другой инструмент.

Этот отрицательный материал задаёт практическую границу. У Pocock skills становятся устойчивой библиотекой малых процедур. У Ronacher похожая логика проходит через более жёсткий фильтр: если локальная автоматизация не стала регулярным рабочим движением, её нужно удалить. Хороший agent harness не обязан быть богатым. Он должен быть живым и ремонтопригодным.

## 5. От MCP к code-as-tool-interface

Следующий поворот Ronacher формулирует в [“Your MCP Doesn’t Need 30 Tools: It Needs Code”](https://lucumr.pocoo.org/2025/8/18/code-mcps/). Его претензия к чрезмерно богатым MCP-серверам не в том, что MCP бесполезен. Проблема в том, что длинный список специальных tools часто хуже, чем одна программируемая поверхность.

Командная строка сильна не отдельными командами, а композиционностью. Агент может вызвать command, сохранить output, отфильтровать через `jq`, написать Python script, повторить с другими arguments, объединить файлы, добавить logging, удалить временный helper. Если tool API заранее описывает 30 отдельных операций, агент получает интерфейс, который выглядит structured, но плохо изменяется в моменте. Если нужной операции нет, он снова упирается в человека или начинает злоупотреблять похожей.

Ronacher предлагает думать о MCP иначе: иногда достаточно одного “ubertool”, который принимает code. В статье он приводит идею Python interpreter with retained state, например через `pexpect`: модель не получает отдельный tool для каждого действия, а пишет маленький Python fragment, который управляет process, читает output и сохраняет state между вызовами. Это небезопасно по умолчанию, но методологически важно. Для coding agent код уже является естественным интерфейсом. Если агент умеет писать код, не всегда нужно скрывать внешнюю систему за большим набором заранее названных кнопок.

В Syntax-интервью он даёт более бытовой пример на Sentry. Вместо того чтобы ждать официальный Sentry MCP, он просит coding agent построить маленький skill под его auth flow: скачать нужные события, положить JSON в filesystem, показать несколько элементов в context, остальные оставить в файле. Агент может сначала увидеть три события, потом понять, что нужно больше, открыть JSON, прогнать `jq`, написать маленький shell script, повторить запрос с другим фильтром. Важная деталь: данные не обязаны целиком проходить через LLM context. Они могут лежать в файлах, а модель берёт оттуда только то, что нужно для текущего reasoning.

Ещё более показательный эпизод из той же линии — его разбор conversion workflow в [“Tools: Code Is All You Need”](https://lucumr.pocoo.org/2025/8/18/code-mcps/). Ronacher переносил blog posts из reStructuredText в Markdown не через один большой prompt “перепиши текст”, а через AST и scripts: агент писал transformation code, запускал его, сравнивал HTML output before/after и кормил diffs обратно в цикл. Это заняло около получаса machine work, но доверие появилось не потому, что модель “красиво переписала”, а потому что процесс был mechanical and reviewable. Текст не должен был исчезнуть в чёрном ящике модели; он проходил через проверяемую программу.

Там же он приводит второй типичный ход: когда нужно управлять browser или debugger, агент часто лучше работает не через большой catalog of fixed buttons, а через маленький script на Playwright, `tmux`, `pexpect` or Python. Он сначала пишет одноразовый инструмент, затем использует его повторно. Если инструмент оказался полезным, его можно оставить; если нет — удалить. Это и есть практический смысл code-as-tool-interface: не “всё решает shell”, а “интерфейс должен быть тем, что агент может сочинить, прочитать, исправить и повторить”.

Декабрьская статья [“Skills vs Dynamic MCP Loadouts”](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/) уточняет тот же ход после нескольких месяцев практики. Ronacher пишет, что переносит remaining MCPs into skills: skill is not a new tool definition in context, а short summary and file/manual that teaches the agent how to use the ordinary tools it already has. Sentry MCP для него стал показательной границей: eager loading cost around 8k tokens, dynamic CLI wrapping через `mcporter` did not remove the need for manual summaries, and Sentry’s own tool surface could change. Agent-maintained skill оказался менее официальным, но more repairable: если ломается auth, query syntax or browser flow, agent can change the skill itself.

Это напрямую ведёт к Pi. Если агенту нужен новый инструмент, Ronacher предпочитает дать ему возможность написать расширение, а не заранее строить гигантский tool catalog. Если browser skill ломается из-за cookie banner, агент может изменить свой skill. Если review UI неудобен, агент может построить UI component. Если нужно другое представление файлов, extension state можно писать на disk. Стабильным остаётся маленькое ядро; всё остальное должно быть изменяемым.

## 6. Pi: маленькое ядро вместо большого agent framework

В январе 2026 Ronacher публикует [“Pi: The Minimal Agent Within OpenClaw”](https://lucumr.pocoo.org/2026/1/31/pi/). Здесь его накопленные решения становятся самостоятельным инструментом. Pi — это не продуктовый assistant и не попытка заменить Claude Code богатой IDE. Это маленький agent harness внутри OpenClaw, который Ronacher начинает использовать почти исключительно для собственной coding work.

Ключевая архитектурная деталь предельно проста: Pi имеет маленькое ядро и четыре базовых tools — `Read`, `Write`, `Edit`, `Bash`. Всё остальное должно строиться как extension. Ronacher прямо противопоставляет это MCP-heavy подходу. Он не хочет заранее держать огромный список внешних tools. Он хочет, чтобы агент мог расширить сам себя: найти пример extension, написать новый вариант, сохранить state, reload, попробовать, исправить.

На уровне репозитория Pi описан как монорепозиторий с несколькими пакетами: `@earendil-works/pi-coding-agent`, `@earendil-works/pi-agent-core`, `@earendil-works/pi-ai`, `@earendil-works/pi-tui`. В [README](https://github.com/earendil-works/pi) проект называется agent harness и self-extensible coding agent; эти английские формулы важны как самоназвание проекта, но по сути речь идёт о маленькой обвязке для кодового агента. Pi не притворяется “интеллектом”. Он задаёт форму взаимодействия между моделью, файлами, инструментами, расширениями, сессиями и пользователем.

В Syntax-интервью Ronacher описывает Pi почти как `while` loop: взять messages, вызвать model, дать ей tools, получить tool calls, выполнить, добавить results, повторить. Снаружи такие harnesses похожи. Но отличие Pi в том, что он не пытается быть большим снаружи. Он оставляет внешнюю поверхность маленькой, а изменчивость переносит внутрь файлов и extensions.

<figure class="source-figure" id="fig-story-13-armin-pi-extension-surface">
  <img src="../assets/story-images/13-armin-pi-extension-surface.webp" alt="Скриншот Pi или страницы Pi: минимальное ядро и расширения как рабочая поверхность агента." loading="lazy" />
  <figcaption>Иллюстрация нужна не как портрет инструмента, а как визуальная привязка центрального сдвига: Pi не строится вокруг большого каталога tools; расширяемая поверхность живёт в локальных extensions и session state. Источник: <a href="https://lucumr.pocoo.org/2026/1/31/pi/">Pi: The Minimal Agent Within OpenClaw</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-extension-surface.webp</code>.</figcaption>
</figure>

Здесь есть сильная связь с идеей “code as tool interface”. Если extension — обычный code/file, агент может его прочитать. Если он может прочитать, он может изменить. Если может изменить, то tool surface становится частью рабочей памяти проекта, а не внешним API, который должен поддерживать человек. Такой подход не отменяет необходимости review, но меняет место ремонта: слабый tool можно чинить тем же агентом, который его использует.

## 7. Сессия как дерево, а не как один умирающий контекст

Pi важен не только tools. Ronacher отдельно выделяет session architecture. В Pi sessions являются trees: можно ответвиться, выполнить review в fresh context, вернуться назад с summary, сохранить custom messages и extension state. Это не декоративная feature. Это ответ на одну из главных проблем long-running agent work: контекст одновременно нужен и вреден.

Если агент долго работает в одной сессии, он накапливает history, tool results, старые решения, неудачные гипотезы и случайные детали. В какой-то момент context становится тяжёлым, и модель начинает хуже различать, что актуально. Но если каждый раз начинать с нуля, теряются decisions, open tasks и local state. Pi пытается удержать середину: sessions можно ветвить, summarization переносит важное между ветками, extension state живёт на disk, а не только в model context.

В документации по [compaction](https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/compaction.md) это устроено довольно конкретно. Есть два механизма: compaction и branch summarization. Auto-compaction срабатывает, когда использованные context tokens приближаются к размеру окна с заданным запасом. В документации фигурируют defaults вроде `reserveTokens=16384` и `keepRecentTokens=20000`: Pi оставляет свежий хвост сессии, идёт назад от newest message, ищет безопасную точку разреза и не режет tool results отдельно от соответствующих calls. Старый фрагмент превращается в `CompactionEntry` с `summary`, `firstKeptEntryId`, token counts, списком read/modified files and other details. При загрузке сессии модель получает summary плюс свежие messages, а не весь старый шум.

Branch summarization решает другой случай. Если пользователь уходит в боковую ветку, например просит review или investigation, Pi находит common ancestor, собирает entries этой ветки, делает summary и добавляет `BranchSummaryEntry` при возвращении. Формат summary не произвольный: goal, constraints and preferences, progress, key decisions, next steps, critical context. Большие tool outputs при serialization могут обрезаться до короткого представления, чтобы старый stdout не съедал контекст. Это уже не просто “сжать чат”. Это попытка сделать переходы между рабочими ветками управляемой частью harness.

<figure class="source-figure" id="fig-story-13-armin-pi-compaction-docs">
  <img src="../assets/story-images/13-armin-pi-compaction-docs.webp" alt="Фрагмент документации Pi о compaction и branch summarization." loading="lazy" />
  <figcaption>Картинка должна показать невидимую механику истории: Pi хранит не только prompt и ответ, а деревья сессий, summaries, token thresholds и branch return. Источник: <a href="https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md">Pi compaction docs</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-compaction-docs.webp</code>.</figcaption>
</figure>

Это роднит Ronacher с Mark Erikson, но точка другая. Erikson показывает external memory как помощь агенту между sessions: scripts, prompts, scratchpads, repo-specific files. Ronacher в Pi делает session tree частью самого harness. Память здесь не только “документ рядом с кодом”; это runtime object, который можно compact, branch, summarize and reload.

## 8. Extensions: рабочие поверхности, которые агент может построить себе сам

В статье о Pi Ronacher перечисляет extensions вроде `/answer`, `/todos`, `/review`, `/files`. Они выглядят как обычные commands, но принципиально отличаются от failed slash commands из Claude Code-периода. Это не просто prompts, которые живут в меню. Extension может иметь persistent state, UI, own files, integration with session tree. Агент может открыть пример, изменить его, создать новый variant и immediately use it.

`/answer` вынимает вопросы агента в отдельную input surface: вместо того чтобы оставлять user buried inside the stream, Pi собирает вопросы и позволяет ответить на них как на отдельный рабочий объект. `/todos` держит задачи в markdown files under `.pi/todos`; sessions могут claim tasks, то есть todo state становится файловым состоянием harness, а не только скрытой модельной памятью. `/review` branch-ится в fresh context, смотрит изменения и приносит fixes back; Ronacher описывает review surface, где можно выбирать uncommitted changes, single commit or main branch, а не каждый раз руками просить агента “посмотри diff”. `/files` показывает files changed or referenced by session.

В Syntax-интервью эта архитектура становится совсем практичной. Ronacher говорит, что перестроил аналог Claude Code todo tool как Pi extension за evening: Pi читал собственные markdown examples and API descriptions, писал extension и сразу мог её использовать. Это важнее самого todo-интерфейса. Если tool surface лежит в документации и коде, агенту не нужно ждать, пока vendor добавит feature; он может построить локальную версию, а человек потом решает, достойна ли она остаться.

Здесь скрыт важный критерий хорошей agent extension: она должна быть не только полезной, но и читаемой для агента. Если инструмент существует как black box service, модель может только вызвать его или не вызвать. Если extension лежит в репозитории, модель может понять contract, изменить behavior, добавить state или написать соседний extension. Это превращает tool-building из отдельной инженерной задачи в часть обычной агентской работы.

Но такой подход одновременно требует доверия к локальному окружению. Если агент может менять свои инструменты, он может испортить свои инструменты. Если extension state живёт на disk, он может быть stale, inconsistent или unsafe. Поэтому Ronacher не продаёт Pi как универсально безопасную систему. Он строит инструмент для controlled local work, где человек владеет средой и может review.

## 9. Security boundary: “just runs code” полезно ровно там, где оно ограничено

Ronacher не скрывает опасность своего подхода. В README Pi прямо сказано, что у Pi нет built-in permission system: он запускается с теми правами, которые есть у process/user. Если нужна изоляция, нужно sandbox/containerize whole process or route tool execution. Документация по [containerization](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md) описывает несколько patterns: OpenShell как policy sandbox, Gondolin extension, который оставляет Pi/auth на host, но выполняет tools в local Linux micro-VM, и Docker, где весь Pi запускается в container.

Это важный момент для правильного понимания истории. Ronacher не доказывает, что permission prompts не нужны. Он работает в режиме, где широкая локальная автономия окупается, потому что окружение его, repo его, review его, последствия его. Если перенести этот режим в чужой production system, shared workstation или open-source intake, он станет безответственным.

В этом смысле Pi — не противоположность Sandvault у Mike McQuaid. Sandvault делает bounded autonomy через macOS sandbox, worktrees, limited filesystem access and policy. Pi делает другой trade-off: маленькое изменяемое ядро и локальное доверие, но с явным признанием, что sandbox должен быть внешним слоем, если trust boundary меняется. Обе истории сходятся в одном: безопасность нельзя решить просьбой к модели “будь осторожна”. Она должна быть свойством среды.

Prompt injection здесь тоже не исчезает. Если агент читает issue, web page, log или external JSON, он может получить malicious instructions. Ronacher скорее принимает этот риск как часть мира, где agent runs code, и ограничивает его локальной trust boundary. Поэтому его later open-source gate так важен: внешний machine-generated input не должен автоматически получать такой же trust, как локальная работа владельца репозитория.

## 10. MiniJinja Go port: большая задача за пределами Pi

Прежде чем история уйдёт в issue tracker Pi, полезно увидеть, что harness Ronacher не ограничен маленькими локальными fixes. В январе 2026 он публикует разбор [“Porting MiniJinja to Go With an Agent”](https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/) и открывает [MiniJinja PR `#854`](https://github.com/mitsuhiko/minijinja/pull/854), “Minijinja Go Port”. Это боковой кейс, но он системно важен: минимальный harness проверяется не только на собственном agent product, а на большой задаче переноса с проверкой поведенческого соответствия.

Сценарий не был “перепиши библиотеку на Go”. Ronacher начал с вопроса, как вообще валидировать такой port. Рабочая форма получилась test-driven: переиспользовать существующие Rust snapshot tests и переносить систему по фазам — сначала lexer, затем parser, затем runtime. Агент построил Go-side tooling, которое читало Rust test input files with JSON settings headers, парсило reference `insta` `.snap` snapshots, сравнивало output и вело skip-list для временно падающих тестов. Поэтому агент получил не только цель, а плотную проверочную поверхность: каждое недостающее поведение давало один или несколько падающих snapshots.

Дальше Pi branch architecture стала частью работы. Ronacher rewound earlier parts of the session, branched off phases and let Pi inject a summary of prior work when switching branches. Это не абстрактная “длинная память”; это тот же механизм, который выше появился как session tree and branch summaries, но применён к реальному porting task. Агент быстро ушёл от literal porting к behavioral porting: например, runtime side used a tree-walking interpreter and Go reflection instead of copying Rust’s bytecode-ish shape. Ronacher разрешал это там, где тесты сохраняли поведение, но pushback всё равно был нужен: модель пыталась отказаться от “must fail” tests, потому что точные сообщения об ошибках были трудны, и Ronacher направил её к fuzzy matching; она также хотела откатить точную семантику HTML escaping и поведение `range`.

По собственным session stats: Ronacher spent about 45 minutes of active human time; the agent worked roughly 3 hours supervised and then about 7 hours unattended. Session had 2,698 messages, 34 human prompts, 1,386 tool calls, about 2.2 million tokens and roughly $60 raw API cost, with prompting by voice in Pi, начав с Opus 4.5 и перейдя к GPT-5.2 Codex на длинном хвосте исправления тестов. Эти numbers не нужны как реклама скорости. Они показывают форму работы: успешный port был не single magic completion, а hours-long harnessed run with tests, branches, compaction, human interventions and final cleanup.

<figure class="source-figure" id="fig-story-13-armin-minijinja-pr-854">
  <img src="../assets/story-images/13-armin-minijinja-pr-854.webp" alt="Скриншот GitHub PR #854 Minijinja Go Port." loading="lazy" />
  <figcaption>PR нужен как отдельная визуальная опора: MiniJinja Go port показывает Pi/harness вне собственного репозитория, на задаче behavioral translation с tests, commits, CI и session trace. Источник: <a href="https://github.com/mitsuhiko/minijinja/pull/854">MiniJinja PR #854</a>. Локальный файл: <code>../assets/story-images/13-armin-minijinja-pr-854.webp</code>.</figcaption>
</figure>

PR `#854` сам фиксирует public artifact layer: 21 commits, session trace, CI/release/process work and a note that the fate of the automated port still needed to be decided. Поэтому MiniJinja не подменяет главную историю Pi, но удерживает её от слишком узкого чтения. Minimal harness Ronacher работает не потому, что репозиторий Pi особенный, а потому, что некоторые задачи можно превратить в плотный контур артефактов, тестов, branches и human steering.

[Session trace dataset](https://huggingface.co/datasets/badlogicgames/pi-mono) по Pi/OpenClaw work добавляет ту же мысль с другой стороны. Даже если отдельный viewer недостаточно надёжен для восстановления каждого reasoning path, сам факт shared traces важен: agent sessions treated as inspectable work artifacts, not invisible private conversations. Это сближает Ronacher с transcript-oriented research у Simon Willison, но уже в context coding-agent harness.

## 11. Building Pi with Pi: issue tracker как вход для prompt

В мае 2026 Ronacher публикует [“Building Pi With Pi”](https://lucumr.pocoo.org/2026/5/24/pi-oss/). Это лучший центральный эпизод истории: Pi уже не просто инструмент, а среда, с помощью которой Ronacher чинит сам Pi.

Рабочий цикл начинается с GitHub issue. Но issue не воспринимается как готовая истина. Ronacher прямо пишет, что issue tracker стал входным материалом для агента: понять проблему, воспроизвести, посмотреть код и предложить исправление. При этом плохие AI-expanded issues хуже, чем отсутствие diagnosis. Если reporter принёс длинное машинное объяснение root cause, Pi не должен ему верить. Неверная diagnosis становится не подсказкой, а материалом для проверки, который часто нужно отбросить.

Именно поэтому у Pi появляется локальный prompt `/is`. Он не говорит агенту “исправь issue”. Он задаёт расследовательский режим. Агент должен открыть issue через `gh`, посмотреть title, body, comments, labels, assignees, state, URL, author, timestamps and closed PR references. Потом он должен не доверять анализу в issue. Для bug report — игнорировать proposed root cause, читать relevant files полностью, trace code path, reproduce behavior if possible, propose fix. Для feature request — проверить proposal, impacted files, trade-offs. И главное: не implement unless explicitly asked.

Сильно сокращённый смысл `/is` можно выразить так:

```text
Analyze issue $ARGUMENTS.
Do not trust the issue's own diagnosis.
For bugs, reproduce or trace the behavior from code.
Do not implement unless explicitly asked.
```

Полная ценность здесь не в тексте prompt. Ценность в рабочем разделении. Issue becomes input; `/is` turns it into investigation; implementation remains a separate decision. Это защищает от одного из типичных agent failures: модель слишком рано принимает формулировку задачи, особенно если она уже написана уверенным AI-языком.

## 12. Хороший issue как рабочий материал для агента

В “Building Pi With Pi” Ronacher описывает, какой issue действительно помогает. Хороший issue contains command, expected behavior, actual behavior, exact error or log. Такой report можно проверить. Его можно запустить, сравнить, локализовать. Он не обязан объяснять внутреннюю причину; иногда лучше, если не объясняет.

Плохой AI-expanded issue делает противоположное: добавляет гладкое, уверенное, но неверное объяснение. Ronacher приводит характерный pattern: malformed session log crashes reader; модель предлагает tolerant reader, fallback, migration, debug logging. Но правильный fix может быть не в том, чтобы терпеть corrupted state, а в том, чтобы сохранить invariant and make bad state impossible. Если agent начинает с ложного “разумного” explanation, он строит вокруг него лишнюю архитектуру.

Эта сцена важна не только как open-source etiquette. Она показывает конкретный механизм деградации: машинный текст может повысить surface plausibility issue, но ухудшить diagnostic value. Для agentic workflow это опасно вдвойне, потому что следующий агент тоже склонен доверять длинному structured explanation. Slop begets slop.

Ronacher решает это не моральным запретом, а процедурой: `/is` заставляет Pi не доверять issue, читать код, trace behavior and separate diagnosis from input. Это почти forensic hygiene for agents.

<figure class="source-figure" id="fig-story-13-armin-pi-prompt-is-md">
  <img src="../assets/story-images/13-armin-pi-prompt-is-md.webp" alt="Фрагмент prompt-файла .pi/prompts/is.md с правилами issue investigation." loading="lazy" />
  <figcaption>Этот фрагмент полезен потому, что показывает `/is` как реальную процедурную границу, а не как риторический совет: сначала получить issue через <code>gh</code>, не доверять его диагнозу, читать код и не переходить к реализации без отдельного запроса. Источник: <a href="https://github.com/earendil-works/pi/blob/main/.pi/prompts/is.md">.pi/prompts/is.md</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-prompt-is-md.webp</code>.</figcaption>
</figure>

## 13. Параллельные расследования: несколько Pi окон вместо одного героического агента

Когда issue формализован как prompt input, появляется следующая возможность: несколько investigations можно вести параллельно. В [“Building Pi With Pi”](https://lucumr.pocoo.org/2026/5/24/pi-oss/) Ronacher описывает локальную `.pi` папку с prompts and helpers. Там есть `/is`, `prompt-url-widget` and `/wr`. `prompt-url-widget` watches prompt text, распознаёт GitHub issue/PR URL, через `gh` забирает title and author, renders widget in the UI, renames session и rebuilds state when session starts or switches. Поэтому несколько Pi windows могут нести identity своего issue визуально, а не только в model context.

<figure class="source-figure" id="fig-story-13-armin-pi-prompt-url-widget">
  <img src="../assets/story-images/13-armin-pi-prompt-url-widget.webp" alt="Скриншот Pi terminal session with GitHub issue widget from Building Pi With Pi." loading="lazy" />
  <figcaption>Эта картинка полезнее generic UI screenshot: она показывает, как GitHub issue становится видимым session object в Pi, а не просто URL внутри prompt. Источник: <a href="https://lucumr.pocoo.org/2026/5/24/pi-oss/">Building Pi With Pi</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-prompt-url-widget.webp</code>.</figcaption>
</figure>

Это не совсем то же самое, что “запустить много агентов”. Важна не численность, а containment. Каждое окно получает конкретный issue, prompt, local state, branch/session identity. Человек может переключаться между investigations, видеть, где что происходит, и закрывать работу через отдельный wrap-up ritual. Если просто попросить один большой агент “разбери все open issues”, он смешает contexts, перепутает root causes and generate summaries too early.

Параллельность у Ronacher ближе к batch of bounded investigations. Она родственна Calvin French-Owen, где несколько agents создают новые bottlenecks for human attention, и Jökull Sólberg, где PR triage превращается в structured review queue. Но Ronacher переносит это в open-source maintainer workflow: issue становится маленьким container for investigation, а не item in a generic backlog.

## 14. `/wr`: closure as a scripted ritual

Если `/is` отвечает за начало расследования, то `/wr` отвечает за завершение. В репозитории Pi [`/wr` prompt](https://raw.githubusercontent.com/earendil-works/pi/main/.pi/prompts/wr.md) формализует wrap-up: определить контекст from conversation, обновить changelog under `## [Unreleased]`, подготовить final issue/PR comment, commit only files changed in session, добавить `closes #` only when exactly one issue is in scope, проверить branch `main`, never stage unrelated files, never `git add .`, run checks if code changed, no PR unless asked.

Особенно важна строка AI disclosure: final comment должен заканчиваться точной фразой:

```text
This comment is AI-generated by /wr
```

Это маленькая деталь, но она хорошо показывает этику harness. Ronacher не пытается спрятать машину за человеческим голосом. Если final comment генерируется через Pi, это должно быть видно. Если commit связывается с issue, связь должна быть точной. Если изменены unrelated files, они не должны быть случайно staged. Если code changed, checks должны быть запущены.

У многих agent workflows завершение задачи остаётся самым слабым местом. Агент может хорошо сделать fix, но плохо завершить работу: забыть changelog, закрыть wrong issue, добавить чужой файл, написать overly cheerful comment, не указать AI involvement. `/wr` превращает конец работы в отдельную процедуру. Это близко к Matt Pocock’s handoff and git guardrails, но у Ronacher closure привязан к issue-driven open-source loop.

<figure class="source-figure" id="fig-story-13-armin-pi-prompt-wr-md">
  <img src="../assets/story-images/13-armin-pi-prompt-wr-md.webp" alt="Фрагмент prompt-файла .pi/prompts/wr.md с правилами wrap-up и AI disclosure." loading="lazy" />
  <figcaption>Здесь важен не весь prompt, а сам факт его существования: завершение работы формализовано отдельным файлом с правилами changelog, final comment, точного <code>closes #</code>, staging discipline и AI disclosure. Источник: <a href="https://github.com/earendil-works/pi/blob/main/.pi/prompts/wr.md">.pi/prompts/wr.md</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-prompt-wr-md.webp</code>.</figcaption>
</figure>

## 15. Внешний поток: slop, объём и исполняемый фильтр

Теперь социальная граница возникает не как отдельный essay, а как прямое следствие harness. Если issue tracker стал prompt input, то качество внешнего issue становится важным для агента. В “Building Pi With Pi” Ronacher показывает два разных сбоя. Первый — semantic: человек видит один симптом, пропускает его через модель, получает confident diagnosis and expanded scope, а потом другой agent may treat that diagnosis as evidence. Второй — объёмный: Pi/OpenClaw tracker receives far more external issues and PRs than maintainers can review.

Цифры в статье жёсткие. За 90 дней в Pi/OpenClaw-поле пришло 3,145 external issues/PRs; 2,504 were auto-closed; roughly 17% reopened; if references to commits/merged PRs are counted, useful/acted-on share rises to 26%; PRs merged were 60 of 714, about 8%. Эти числа не надо превращать в универсальную статистику open source. Они нужны как причина архитектурного решения: open-source boundary становится частью самого agent workflow.

В Pi repository новые issues и PRs auto-close by default. README отправляет к `CONTRIBUTING.md`; [`CONTRIBUTING.md`](https://github.com/earendil-works/pi/blob/main/CONTRIBUTING.md) фиксирует ownership-first позицию: AI-written code допустим, но автор должен понимать код; AI-generated slop без понимания не принимается. Reporter должен писать коротко, своим голосом and clearly explain why it matters. PR должен проходить checks; core должен оставаться minimal; feature often should be extension.

Технически gate реализуется через GitHub Actions. [`issue-gate.yml`](https://raw.githubusercontent.com/earendil-works/pi/main/.github/workflows/issue-gate.yml) reacts to opened issues, проверяет permission and `.github/APPROVED_CONTRIBUTORS`, пропускает bots/collaborators and approved capability `issue`, иначе закрывает с комментарием. [`pr-gate.yml`](https://raw.githubusercontent.com/earendil-works/pi/main/.github/workflows/pr-gate.yml) делает то же для PRs, но требует capability `pr`. [`APPROVED_CONTRIBUTORS`](https://raw.githubusercontent.com/earendil-works/pi/main/.github/APPROVED_CONTRIBUTORS) stores usernames and capabilities. Это не philosophy in README, а executable review-budget policy.

<figure class="source-figure" id="fig-story-13-armin-pi-issue-gate-workflow">
  <img src="../assets/story-images/13-armin-pi-issue-gate-workflow.webp" alt="Фрагмент GitHub Actions workflow issue-gate.yml и списка APPROVED_CONTRIBUTORS в репозитории Pi." loading="lazy" />
  <figcaption>Этот скриншот нужен, чтобы социальная граница не оставалась абстрактной. В Pi review-budget policy выражена в исполняемом workflow: GitHub Action проверяет capability и автоматически закрывает вход, который не должен превращаться в чужую бесплатную review-работу. Источник: <a href="https://github.com/earendil-works/pi/tree/main/.github/workflows">Pi GitHub workflows</a> и <a href="https://raw.githubusercontent.com/earendil-works/pi/main/.github/APPROVED_CONTRIBUTORS">APPROVED_CONTRIBUTORS</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-issue-gate-workflow.webp</code>.</figcaption>
</figure>

У OpenClaw gate есть отдельная важная деталь: workflow может добавить label `possibly-openclaw-clanker`, если автор уже проявлял активность в `openclaw/openclaw`. Это triage heuristic, а не доказательство, что конкретный report был machine-generated. В истории `#4945` therefore label нельзя читать as forensic conclusion; it shows suspicion/source context, not a substitute for reading the issue.

<figure class="source-figure" id="fig-story-13-armin-pi-external-volume">
  <img src="../assets/story-images/13-armin-pi-external-volume.webp" alt="График weekly external volume and acceptance rate of Pi issues and pull requests from Building Pi With Pi." loading="lazy" />
  <figcaption>График нужен как визуальная причина gate: вопрос не в абстрактной неприязни к AI, а в резком увеличении внешнего issue/PR volume, который не сопровождается таким же ростом maintainer capacity. Источник: <a href="https://lucumr.pocoo.org/2026/5/24/pi-oss/">Building Pi With Pi</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-external-volume.webp</code>.</figcaption>
</figure>

В этой части Ronacher’s position is more precise than a refusal policy. Он интенсивно использует agents; he uses Pi to build Pi; he accepts that AI-assisted code can be valid. Но он refuses cost transfer. If a machine helps you understand a bug, you still own the report. If a machine writes code, you still own the code. If your machine creates issue-tracker noise, you создали этот шум с помощью машины.

## 16. Конкретная цепочка: `#4945` → `#4979` → неясность после merge

Хорошая проверка этой системы — конкретные issues. Один из самых информативных examples: [issue `#4945`](https://github.com/earendil-works/pi/issues/4945), “openai-codex can hang on Working... with zero-usage aborted turns”. Пользователь `liushuaiiu` opened bug report on 24 May 2026. Issue had label `inprogress`, was assigned to `mitsuhiko`, and also carried `possibly-openclaw-clanker`. Последний label нужно читать осторожно: as gate heuristic from OpenClaw-side activity, not proof about this particular report.

Report был необычно конкретным. Он описывал зависание TUI on `Working...`: no text, no tool call, no visible error; Escape records aborted turn. Environment included Pi 0.75.5, Node v22.22.1, provider/model `openai-codex`/`gpt-5.5`, thinking `xhigh`, default tools/extensions. Saved session entry had assistant turn with `stopReason: aborted`, empty content and usage counters all zero. Reporter suggested that `getTransport()` returns `auto`, docs default `sse`, auto tries WebSocket, retry timeout not applied, event loop waits with no idle timer. Workaround: set transport to `sse` and `httpIdleTimeoutMs`.

Это почти идеальный example of issue as working material for an agent: reproducible behavior, exact state, environment, session JSON, possible code path and workaround. Но даже здесь Ronacher does not simply accept diagnosis. [PR `#4979`](https://github.com/earendil-works/pi/pull/4979), “fix(codex): timeouts for websockets”, was merged on 27 May 2026. Its description had a caveat: “This is not going to fix #4945 but…” — PR aligns timeout behavior for Codex WebSocket path, adds inactivity timeout even with keepalive and 15-second connect timeout. It was merged from branch `fix/codex-websocket-idle-timeout`, included 4 commits and passed checks.

<figure class="source-figure" id="fig-story-13-armin-pi-pr-4979">
  <img src="../assets/story-images/13-armin-pi-pr-4979.webp" alt="Скриншот GitHub PR #4979 fix(codex): timeouts for websockets." loading="lazy" />
  <figcaption>PR полезен как иллюстрация неидеального, но реального issue-driven agent workflow: хороший bug report, частичный fix, caveat в описании and ambiguity around auto-closing issue. Источник: <a href="https://github.com/earendil-works/pi/pull/4979">PR #4979</a>. Локальный файл: <code>../assets/story-images/13-armin-pi-pr-4979.webp</code>.</figcaption>
</figure>

После merge появилась характерная неясность: another participant asked whether `#4945` should be reopened, because issue auto-closed even though PR itself said it was not a full fix. Later release `v0.76.0` still carried this chain into a release artifact: changelog mentions fixes around `httpIdleTimeoutMs`, `websocketConnectTimeoutMs` and a 10-second SSE response-header timeout. Therefore the episode is not a false alarm. It shows a finer point: good external report can lead to release-level change, but issue lifecycle and fix semantics still need human care.

Это маленький, но важный failure case. Even good issue, useful PR and scripted closure can produce wrong lifecycle state. `closes #` helps close concrete work, but if fix is partial, automation can over-close reality. In Ronacher’s story this does not undermine the harness; it shows its limit. Issue/PR automation useful, but closure semantics remain human responsibility.

## 17. Другие issues: где report полезен, где запрос остаётся feature noise

На соседних examples видно, как Ronacher’s issue process различает material for the agent from material that should not immediately become code.

[Issue `#4984`](https://github.com/earendil-works/pi/issues/4984) describes crash in interactive mode on transient terminal `EPIPE`. Report points to `Error: write EPIPE` after diff preview. It gives size context: file 1,667 lines, 63,753 bytes. In session JSONL assistant had `edit` call without `toolResult`. Debug extensions disabled diff preview and added EPIPE guard, confirming preview rendered but tool call wasn’t triggered. Это useful material: concrete error, moment of failure, file size, session artifact, attempted isolation.

[Issue `#5028`](https://github.com/earendil-works/pi/issues/5028) describes startup crash on MSYS2 `ucrt64` Node because `@mariozechner/clipboard` native addon does not load. Report includes Rust/N-API clue, package install command, environment, expected fallback to `clip`. Здесь агент может inspect dependency, platform assumptions, fallback logic and release packaging. Это не “AI wrote a bug”; это structured platform report.

[Issue `#5027`](https://github.com/earendil-works/pi/issues/5027) is a feature request for `$RAW_ARGUMENTS`, preserving newlines/spaces in prompt templates. Он был closed. The request sounds reasonable, but core minimality matters. Feature may belong in an extension, a different quoting convention, or no change. Агент не должен превращать каждый правдоподобный feature request в код.

[Issue `#1871`](https://github.com/earendil-works/pi/issues/1871) даёт другой тип concrete repro: misleading `No API key found for openai-codex` during parallel startup lock contention. Reporter used shell parallelism:

```bash
seq 1 4 | xargs -P4 -I{} sh -c 'pi --mode json -p --models openai-codex/gpt-5.3-codex "ping {}" > /tmp/pi-{}.log 2>&1'
```

Suspected issue was in shared settings/auth lock, and desired behavior was lock-specific error instead of misleading missing-key message. Это хорошая agent task, потому что command, concurrency condition and expected diagnostic are explicit.

[Issue `#4877`](https://github.com/earendil-works/pi/issues/4877) reports session folder collision: paths like `/a/b/c/d` and `/a-b/c-d` map to same session folder name. The repro uses two directories and simple `pi -p` calls. Это ещё один mechanical issue, где агент может trace path normalization and storage layout.

В совокупности эти examples show that Ronacher’s gate is not anti-user. Он хочет, чтобы external input входил в harness in a form that preserves diagnostic value: command, environment, expected/actual, exact error, artifacts. Если input — generated explanation без ownership, он вреден. Если input — воспроизводимый material, Pi может его использовать.

## 18. Локальные правила: `AGENTS.md`, `CONTRIBUTING.md`, тесты и supply chain

В репозитории Pi есть не только source code and workflows, но и документы, которые направляют работу людей и агентов. [`AGENTS.md`](https://github.com/earendil-works/pi/blob/main/AGENTS.md) короткий и операционный: писать кратко, читать файлы целиком перед правкой, не использовать `any`, запускать project commands вроде `npm run check`, `./test.sh` и targeted vitest, не выполнять destructive git commands, помнить о нескольких Pi sessions в одном working directory, stage только явные пути and never `git add .`. Там же заданы правила для PR inspection через `gh pr view`, `gh pr diff`, `gh api`, and comments через temp files with AI disclaimer.

Это не философия, а operating manual for agents in repo. Особенно важна строка про несколько Pi sessions: Ronacher действительно запускает несколько Pi windows. Generic instruction “be careful with git” здесь слабее, чем конкретное правило: несколько sessions могут касаться одного working directory, therefore stage only explicit paths.

`CONTRIBUTING.md` обращён уже к людям, которые используют агентов. Его правило — ownership-first: human must understand code; AI-written code is allowed, AI-generated slop without understanding is not. Issue should fit roughly on one screen, be written in own voice and explain why it matters. For review the file distinguishes `lgtmi` and `lgtm`; PR must pass `npm run check` and `./test.sh`; changelog in PR is not needed. Core remains minimal; feature often should be extension. New issues/PRs auto-close to protect review budget.

Pi README добавляет скучный, но несущий слой: development commands like `npm install --ignore-scripts`, `npm run build`, `npm run check`, `./test.sh`, `./pi-test.sh`; pinned direct dependencies; `.npmrc` with exact saves and minimum release age; lockfile as ground truth; pre-commit guard around lockfile and release smoke tests; scripts disabled in install path.

Эти детали защищают историю от романтического чтения. Если агент может редактировать extensions and tools, package environment всё равно требует жёстких правил. Dependency drift, lifecycle scripts, lockfile mutations and release packaging are not solved by “model is smart”. Они контролируются обычными инженерными ограничениями. Чем автономнее агент, тем важнее скучная инфраструктура: package policy, commands, tests, filesystem layout, CI, sandboxing and review semantics.

## 19. Социальная граница: машина, владелец и отказ от племени отказа

Две поздние социальные статьи Ronacher не должны висеть в конце как отдельный моральный довесок. Они закрывают ту же причинную дугу, что и Pi: если агентская работа становится мощнее, нужно точнее говорить, кто действует, кто отвечает and where the boundary sits.

Ранняя статья [“GenAI Criticism and Moral Quandaries”](https://lucumr.pocoo.org/2025/6/10/genai-criticism/) уже задаёт эту двойную позицию. Ronacher не пишет из отказа от AI: он описывает собственное использование как уже очевидно полезное, говорит о grassroots adoption and treats code generation as utilitarian work where review and steering still matter. Но он не отбрасывает критику целиком: utility does not erase cost, pressure, education problems or maintainer burden. Поэтому поздний `clanker` language возникает не из anti-AI identity, а из тяжёлого ежедневного использования инструментов.

В [“Clanker: A Word For The Machine”](https://lucumr.pocoo.org/2026/5/26/clankers/) главное — язык ответственности. Ronacher не любит слово “agent”, потому что в обычном языке agent sounds like someone with delegated authority and responsibility. Для current LLM tool loops он предпочитает более холодную формулу: model + harness + prompt + tools + context + loop. Если coding tool открывает PR, PR открыл человек. Если машина spammed issue tracker, человек заспамил tracker с помощью машины. Это напрямую возвращает к `/wr` disclosure and contribution gate: machine output может существовать, но human ownership не должен исчезать в формулировках.

Та же статья добавляет caution about the word itself. Ronacher acknowledges that `clanker` can be polluted by people using robot imagery to replay human racism under a science-fiction mask; if the word stops doing the work of de-anthropomorphizing machines, another word will be needed. Эта оговорка важна: цель не в том, чтобы импортировать резкий slogan, а в том, чтобы сохранить boundary. Машина — не coworker, не friend и не moral subject текущего workflow; ответственность остаётся у человека и организации.

[“Communities of Not”](https://lucumr.pocoo.org/2026/6/6/communities-of-not/) даёт другой guardrail. Ronacher warns against communities that build identity around abstinence or rejection: in AI-skeptical developer spaces, отказ может съехать от legitimate criticism к policing и коллективному наказанию людей, которые пробуют LLMs. Это завершает social position. Он не хочет boosterism, который прячет machine output за человекоподобным языком; но он не хочет и anti-AI identity, которая трактует само использование как betrayal.

Поэтому конец истории должен быть здесь. Ronacher’s answer is neither “ban agents” nor “let agents act as social participants”. Его формула: агрессивно использовать agents там, где ты владеешь harness, context, repository and consequences; фильтровать external machine-shaped volume до того, как он станет чужой unpaid review work; держать язык достаточно холодным, чтобы responsibility оставалась у humans; не строить community identity вокруг refusal. Это та же структура, что и в технической истории, только at social scale.

## 20. Что эта история добавляет к корпусу

Эта история добавляет к корпусу не ещё один пример “опытный разработчик хорошо использует Claude Code”. Такой сюжет уже был бы слабым повтором. Её отдельный объект — переход от использования внешнего coding agent к созданию маленькой изменяемой среды, где агент работает с кодом, файлами, состоянием сессии, prompts, extensions и issue tracker как с единым рабочим пространством.

По отношению к Matt Pocock и Jesse Vincent здесь важна не только процедурная память. У Matt skills дисциплинируют повторяемые действия; у Jesse gates and hooks собирают session-driver вокруг агента. У Ronacher процедура становится ближе к живому инструменту: у Pi есть prompts, extensions, session tree, compaction, branch summaries, issue widgets и wrap-up scripts, и эти элементы могут развиваться внутри той же среды, которая их использует. Поэтому история показывает не “пиши лучшие инструкции”, а более сильный сдвиг: собери ремонтопригодный agent harness, поверхность которого достаточно мала, чтобы её понимать, и достаточно изменяема, чтобы её расширять.

По отношению к Mark Erikson эта история уточняет роль внешнего состояния. У Mark важны файлы, logs, session tools и повторяемый контекст вне chat. У Ronacher это превращается в архитектурный принцип: контекст не только вспоминается, но и оформляется как файлы, сессии, ветви, summaries и explicit prompts. В результате агентская работа становится меньше похожа на один длинный разговор и больше похожа на последовательность ограниченных расследований, привязанных к файловой системе.

По отношению к Shopify и Stripe история задаёт нижний масштаб той же проблемы. Shopify показывает workflow-as-code; Stripe показывает enterprise developer platform как основание для агентов. Ronacher показывает минимальную версию: один maintainer всё ещё может построить маленький harness, где commands, prompts, sessions, review rules и social boundaries заданы явно. Это важно для корпуса, потому что не все читатели могут повторить Stripe, а Roast может оказаться слишком framework-shaped for their problem. Pi показывает промежуточный путь: не просто chat with tools, но и не корпоративная платформа.

Наконец, история добавляет open-source boundary. Агентская работа здесь не заканчивается на локальной продуктивности. Если issue tracker становится входом для prompt, то качество внешних issues, contribution policy, disclosure, ownership и review budget становятся частью harness. Поэтому финальная социальная часть не является отдельной моральной вставкой. Она показывает тот же принцип на другом уровне: machine output полезен только тогда, когда человек или организация владеет границей вокруг него.

## 21. Ограничения источников и открытые края

История необычно богата публичными источниками, но типы источников разные.

Blog posts Ronacher и Syntax transcript — primary testimony автора и пользователя инструмента. Они сильны для реконструкции reasoning and working preferences, но не раскрывают every private session, branch, failed run or cost accounting. Pi repository files, workflows, prompts and documentation сильнее для concrete mechanics: мы видим `CONTRIBUTING.md`, `AGENTS.md`, `issue-gate.yml`, `pr-gate.yml`, compaction docs and prompts like `/is` and `/wr`.

GitHub issues and PRs — самый сильный forensic layer для specific public events. `#4945`, `#4979`, `#4984`, `#5028`, `#1871` and `#4877` показывают actual reports, labels, comments, merge state or closure. Но они всё равно не доказывают exactly how much of each investigation was done by Pi versus human reading, если linked session trace не прочитан и не связан с этим событием.

Pi session traces and the MiniJinja automated port дают третий слой: public artifacts of agent runs. Они ценны as evidence that sessions are treated as shareable work objects, but each trace still requires separate reading before it can prove a particular reasoning path.

Главный открытый край совпадает с главной мыслью истории: minimal mutable harnesses are powerful but sharp. Если environment is local, trusted and reviewed by its owner, code-as-tool-interface продуктивен. If boundary expands to shared systems, unknown inputs or external contributors, the same pattern requires sandboxing, policy and gates. Pi shows one strong answer, not a universal safe default.

## 22. Карта источников

- [“AI Changes Everything”](https://lucumr.pocoo.org/2025/6/4/changes/) — источник по ранней публичной рамке Ronacher: hands-off Claude Code usage, новый pattern распределения внимания и умеренный, но реальный productivity gain.
- [“GenAI Criticism and Moral Quandaries”](https://lucumr.pocoo.org/2025/6/10/genai-criticism/) — источник по ранней социальной позиции Ronacher: strong positive utility for code/text work, grassroots adoption, review/steering as control, and refusal to dismiss criticism wholesale.
- [“Agentic Coding Recommendations”](https://lucumr.pocoo.org/2025/6/12/agentic-coding/) — источник по практическим рекомендациям июня 2025: Claude Code Max/Sonnet, `--dangerously-skip-permissions`, preference for Go, Makefile/log/test design, simple code, plain SQL and local permission checks.
- [“Agentic Coding Things That Didn’t Work”](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/) — источник по failed automation: slash commands, hooks, print mode, subagents, deletion rule and `uv` interceptor approach.
- [“Your MCP Doesn’t Need 30 Tools: It Needs Code”](https://lucumr.pocoo.org/2025/8/18/code-mcps/) — источник по code-as-tool-interface argument, CLI composability, single-tool MCP/`pexpect` idea and critique of fixed tool catalogs.
- [“Skills vs Dynamic MCP Loadouts”](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/) — источник по migration from MCPs to skills, Sentry/Playwright skill examples, token/context cost and why agent-maintained local skills can be easier to repair than fixed tool loadouts.
- [Syntax transcript: “Pi: The AI Harness That Powers OpenClaw”](https://syntax.fm/show/976/pi-the-ai-harness-that-powers-openclaw-w-armin-ronacher-and-mario-zechner/transcript) — источник по May all-nighter with Peter Steinberger and Mario Zechner, Pi as a small loop with four tools, Sentry/code-as-tool-interface examples and extension-building details.
- [“Pi: The Minimal Agent Within OpenClaw”](https://lucumr.pocoo.org/2026/1/31/pi/) — источник по Pi architecture: tiny system prompt, `Read`/`Write`/`Edit`/`Bash`, extension system, sessions as trees, branch summaries, local state and extensions like `/answer`, `/todos`, `/review`, `/files`.
- [Pi repository README](https://github.com/earendil-works/pi) — источник по package layout, self-extensible coding agent framing, development commands, auto-close notice, session sharing, security warning and supply-chain hardening.
- [Pi compaction documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md) — источник по compaction and branch summarization mechanics: thresholds, token reserve, `CompactionEntry`, `BranchSummaryEntry`, summary format and serialization/truncation rules.
- [Pi containerization documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md) — источник по security boundary: Pi runs with process/user permissions, OpenShell, Gondolin extension and Docker isolation patterns.
- [`.pi/prompts/is.md`](https://github.com/earendil-works/pi/blob/main/.pi/prompts/is.md) — источник по issue-investigation prompt: fetch issue through `gh`, distrust issue diagnosis, read code, trace behavior, do not implement unless asked.
- [`.pi/prompts/wr.md`](https://github.com/earendil-works/pi/blob/main/.pi/prompts/wr.md) — источник по wrap-up ritual: changelog, final comment, AI disclosure, explicit staging, checks, branch constraints and issue closure rules.
- [“Building Pi With Pi”](https://lucumr.pocoo.org/2026/5/24/pi-oss/) — источник по issue tracker as prompt input, bad AI-expanded issues, 90-day external issue/PR numbers, `prompt-url-widget`, parallel Pi windows, `/wr` closure practice and hard-problem/upstream-maintenance framing.
- [Pi `CONTRIBUTING.md`](https://github.com/earendil-works/pi/blob/main/CONTRIBUTING.md) — источник по human ownership rule, AI-written code allowed with understanding, AI slop rejected, issue/PR auto-close and minimal-core contribution expectations.
- [Pi `AGENTS.md`](https://github.com/earendil-works/pi/blob/main/AGENTS.md) — источник по local agent rules: concise style, full-file reading, checks, no destructive Git commands, multiple sessions in one working directory, explicit staging and PR/comment conventions.
- [`issue-gate.yml`](https://github.com/earendil-works/pi/blob/main/.github/workflows/issue-gate.yml), [`pr-gate.yml`](https://github.com/earendil-works/pi/blob/main/.github/workflows/pr-gate.yml), [`APPROVED_CONTRIBUTORS`](https://github.com/earendil-works/pi/blob/main/.github/APPROVED_CONTRIBUTORS) — источники по executable external contribution gate based on repo permissions and approved capabilities.
- [`openclaw-gate.yml`](https://github.com/earendil-works/pi/blob/main/.github/workflows/openclaw-gate.yml) — источник по `possibly-openclaw-clanker` как heuristic label based on prior OpenClaw activity, not proof about a specific issue.
- [Issue `#4945`](https://github.com/earendil-works/pi/issues/4945), [PR `#4979`](https://github.com/earendil-works/pi/pull/4979) and [release `v0.76.0`](https://github.com/earendil-works/pi/releases/tag/v0.76.0) — связка источников по Codex WebSocket/timeout issue, concrete environment/session details, partial fix, release follow-through and post-merge closure ambiguity.
- [Issue `#4984`](https://github.com/earendil-works/pi/issues/4984) — источник по terminal `EPIPE` crash report with session artifact and diff preview isolation.
- [Issue `#5028`](https://github.com/earendil-works/pi/issues/5028) — источник по MSYS2 `ucrt64` native addon startup crash and fallback expectation.
- [Issue `#5027`](https://github.com/earendil-works/pi/issues/5027) — источник по `$RAW_ARGUMENTS` feature request and an example of plausible request not automatically becoming core work.
- [Issue `#1871`](https://github.com/earendil-works/pi/issues/1871) — источник по parallel startup lock contention and misleading “No API key found for openai-codex” diagnostic.
- [Issue `#4877`](https://github.com/earendil-works/pi/issues/4877) — источник по session folder collision repro.
- [“Porting MiniJinja to Go With an Agent”](https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/) and [MiniJinja PR `#854`](https://github.com/mitsuhiko/minijinja/pull/854) — источники по test-driven Go port: snapshot-test harness, branch phases, active human time, tool-call/token stats, CI and public PR artifact.
- [Pi session trace dataset on Hugging Face](https://huggingface.co/datasets/badlogicgames/pi-mono) — источник по public session-sharing surface; useful as artifact layer, но сам по себе не доказывает качество конкретной trace.
- [“Clanker: A Word For The Machine”](https://lucumr.pocoo.org/2026/5/26/clankers/) — источник по responsibility language: machine is not coworker/friend; agency stays with human/organization; term caveat if it becomes polluted by dehumanizing usage.
- [“Communities of Not”](https://lucumr.pocoo.org/2026/6/6/communities-of-not/) — источник по broader warning against building identity around rejection; used as social guardrail paired with `clanker`, not as separate anti-AI politics.

## Временный список ассетов для скачивания

- `../assets/story-images/13-armin-pi-extension-surface.webp` — source URL: `https://lucumr.pocoo.org/2026/1/31/pi/`. Нужен для визуальной привязки Pi как minimal extensible harness; лучше взять `/answer` or `/review` screenshot, где видна extension/session surface, а не общий портрет инструмента. Статус: не скачано.
- `../assets/story-images/13-armin-pi-compaction-docs.webp` — source URL: `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md`. Нужен для объяснения session trees, compaction and branch summaries; это невидимая механика, и скриншот документации помогает не оставить её абстрактной. Статус: не скачано.
- `../assets/story-images/13-armin-minijinja-pr-854.webp` — source URL: `https://github.com/mitsuhiko/minijinja/pull/854`. Нужен для MiniJinja side case: concrete PR artifact, commits/checks/session trace, and the fact that Pi/harness was used outside its own repository. Статус: не скачано.
- `../assets/story-images/13-armin-pi-prompt-url-widget.webp` — source URL: `https://lucumr.pocoo.org/2026/5/24/pi-oss/`. Нужен для сцены с `prompt-url-widget`: GitHub issue becomes visible session object, а не просто URL в prompt. Статус: не скачано.
- `../assets/story-images/13-armin-pi-prompt-is-md.webp` — source URL: `https://github.com/earendil-works/pi/blob/main/.pi/prompts/is.md`. Нужен как прямое доказательство того, что issue triage formalized in a prompt file: `gh issue view`, недоверие к diagnosis, чтение кода и запрет на немедленную реализацию. Статус: не скачано.
- `../assets/story-images/13-armin-pi-prompt-wr-md.webp` — source URL: `https://github.com/earendil-works/pi/blob/main/.pi/prompts/wr.md`. Нужен для wrap-up ritual: changelog, final comment, precise `closes #`, staging discipline и AI disclosure. Статус: не скачано.
- `../assets/story-images/13-armin-pi-external-volume.webp` — source URL: `https://lucumr.pocoo.org/2026/5/24/pi-oss/`. Нужен для объяснения gate через volume/acceptance-rate graph; предпочтительнее generic workflow screenshot. Статус: не скачано.
- `../assets/story-images/13-armin-pi-issue-gate-workflow.webp` — source URL: `https://github.com/earendil-works/pi/tree/main/.github/workflows` и `https://raw.githubusercontent.com/earendil-works/pi/main/.github/APPROVED_CONTRIBUTORS`. Нужен для показа executable review-budget policy: capability-based auto-close and approved contributor gate. Статус: не скачано.
- `../assets/story-images/13-armin-pi-pr-4979.webp` — source URL: `https://github.com/earendil-works/pi/pull/4979`. Нужен как concrete artifact of issue-driven work: partial fix, merge, checks, release follow-through and closure ambiguity. Статус: не скачано.
- `../assets/story-images/13-armin-pi-dev-desktop-ui.webp` — source URL: `https://pi.dev/`. Не обязательно вставлять в основной текст, но полезно иметь кандидатом: показывает Pi как desktop UI with sidebar/session surface, если при финальной сборке захочется сделать историю менее terminal-only. Статус: не скачано.
