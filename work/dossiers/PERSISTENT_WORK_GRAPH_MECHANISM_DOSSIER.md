# Persistent Work Graph — досье механизма

Статус: отдельное досье механизма, расширенное проходом 2026-06-09. Это не отдельная история и не замена Gas Town. В слое историй Beads остаётся частью Gas Town. В теоретическом слое Beads становится сильным текущим примером более общего механизма: Persistent Work Graph, то есть устойчивого графа работы, который переживает сессию агента.

Граница досье: здесь описывается переносимый механизм, а не весь продукт Beads и не весь набор ролей Gas Town. Материал нужен для будущих разделов про внешнее состояние агентной работы, оркестрацию, gates, handoff, восстановление после обрыва и возможный дизайн нашего многопроходного документного процесса. В теории этот материал должен работать как механизм. В техническом атласе он должен дать фактуру по Beads / Gas Town и многопроходному документному процессу.

## Краткая рабочая карта

Persistent Work Graph — это внешний устойчивый граф работы, где агентная деятельность хранится не только в запросе, стенограмме сессии или окне контекста, а в долговечных объектах, которые могут читать и человек, и агент:

- задача / issue / bead;
- зависимость;
- владелец, закрепление, блокировка;
- gate или условие ожидания;
- handoff-заметка;
- очередь готовой работы;
- статус восстановления;
- комментарии и история;
- связь между репозиториями или рабочими потоками;
- компактная поверхность восстановления контекста.

Главный переносимый тезис: зрелая агентная разработка требует не только более удачных запросов, но и устойчивого рабочего субстрата. Сессия агента может оборваться, сжаться, забыть контекст, пойти по другой ветке, столкнуться с параллельной сессией или быть заменена другим агентом. Работа должна переживать эти события как граф, который можно посмотреть, продолжить, проверить и восстановить.

Минимальный уровень уже виден в обычных трекерах задач: GitHub Issues поддерживает sub-issues и отношения blocking / blocked, а Linear поддерживает отношения blocked / blocking и историю issues. Но для агентной разработки этого мало: нужен не только список связанных задач, а машинно-удобное состояние, очередь готовой работы, правила владения, восстановление контекста и проверяемые ожидания. Beads важен именно тем, что пытается собрать эти элементы в локальный CLI/MCP-доступный граф для coding agents.

## Что именно считается графом работы

Граф работы не обязан быть реализован как отдельная графовая база. Важна не технология хранения, а свойства состояния.

Рабочий элемент должен иметь устойчивую идентичность. Если задача существует только как строка в запросе или как пункт временного плана, агент не может надёжно продолжить её после сжатия контекста или нового запуска. У Beads это issue/bead с hash-based ID; у Taskmaster — запись в `tasks.json` и отдельный task file; у GitHub Issues или Linear — issue с историей, статусом, владельцем и отношениями.

Зависимости должны влиять на готовность работы. Если task B зависит от task A, система должна уметь показать, что B пока нельзя брать, а после закрытия A — что B стал доступен. В Beads это выражено через `bd ready`, `bd blocked`, типы зависимостей и проверки циклов. В Taskmaster то же направление видно в `tm next`, `tm list --ready`, `tm list --blocking` и `tm validate-dependencies`.

Граф должен различать состояние работы и текст объяснения. Комментарий или handoff-заметка полезны, но они не заменяют поля статуса, владельца, зависимости и gates. Агенту нужно не только прочитать, что “это потом”, а получить машинно-видимый ответ: задача готова, заблокирована, ждёт человека, закреплена за другим агентом, требует проверки или может быть продолжена.

## Якорный пример: Beads

Документация Beads определяет Beads как трекер задач на Dolt для coding workflows под надзором AI. Она прямо перечисляет AI-native workflows, hash-based IDs, Dolt-backed storage, dependency-aware execution, formulas и multi-agent coordination как причины, по которым Beads отличается от обычного списка задач ([Beads Documentation](https://gastownhall.github.io/beads/)). README репозитория формулирует близкую идею ещё резче: Beads — распределённый графовый issue tracker для AI agents и устойчивая структурированная память для coding agents ([Beads GitHub repository](https://github.com/gastownhall/beads)).

Для Gas Town Beads не аксессуар. Это data/control plane, который позволяет нескольким сессиям и ролям координироваться без одной гигантской контекстной сессии. Для теории это делает Beads главным текущим якорем Persistent Work Graph.

Важная оговорка: переносимый механизм не равен требованию “использовать Beads”. В Beads есть конкретные технологические ставки: Dolt, CLI/MCP, локальная база, explicit sync, Git-like semantics. Теория должна извлечь не продуктовый рецепт, а свойства, которые нужны агентной работе: структурированное состояние, зависимости, готовность, gates, ownership, восстановление, компактная подача контекста и диагностируемость сбоев.

## Почему markdown-памяти и стенограммы недостаточно

Markdown-планы, стенограммы сессий и ad-hoc TODO полезны на раннем этапе. Они плохо выдерживают давление многосессионной и многоагентной работы:

- нет устойчивой семантики владельца;
- нет dependency-aware очереди готовой работы;
- слабая защита от параллельных правок;
- нет версионированного структурированного состояния;
- тяжело восстановиться после compaction, crash или неправильного `cwd`;
- плохо различаются состояния “известно заблокировано”, “готово”, “в работе”, “передано”, “ждёт человека”, “ждёт CI”.

DoltHub / Beads-материалы ставят проблему именно как проблему устойчивости состояния и координации: агентная работа нуждается в общем состоянии, а полудоверенные параллельные записи требуют структурированного хранилища с версионностью, а не только markdown или JSON-файлов. Для нашего многопроходного документного процесса это прямой урок: pass-артефакты и логи недостаточны, если система должна продолжать работу после сбоя, распределять проходы, не запускаться заново случайно и объяснять, почему следующий шаг именно такой.

## Структурированное состояние на Dolt

Beads Architecture описывает Dolt как единственный storage backend и source of truth. Каждая запись автоматически попадает в историю Dolt; база даёт семантику branch / merge / diff / push / pull на уровне SQL; server mode нужен для сценариев с несколькими авторами записи, а embedded mode подходит для CI, контейнеров и одноразовых сценариев ([Beads Architecture](https://gastownhall.github.io/beads/architecture)).

Из этого не следует, что многопроходному документному процессу обязательно нужен Dolt. Переносимый принцип другой: состояние агентной работы должно быть структурированным, запрашиваемым, версионированным и восстанавливаемым. Если система хранит только логи проходов, человек может восстановить ход вручную, но агенту трудно механически понять, какой pass был успешным, какой документ является текущим target, какой gate не пройден и какой исполнитель имеет право заменить канонический файл.

Dolt-решение также показывает неудобную сторону подхода. Beads Architecture прямо ограничивает область применения: для больших команд, real-time collaboration, неразработческих рабочих процессов, rich media attachments и cross-repository tracking документация советует рассматривать GitHub Issues, Linear или Jira ([Beads Architecture](https://gastownhall.github.io/beads/architecture)). В troubleshooting-документах есть практические сбои: wrong server / shadow database, port conflicts, journal corruption и осторожность вокруг repair-команд ([Beads Troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md)). Для теории это важнее гладкой product story: долговечное состояние само становится объектом сопровождения.

## Модель зависимостей и очередь готовой работы

Beads Dependencies даёт более точную механику, чем первоначальная формула “есть зависимости”. В Beads есть blocking dependency types, которые влияют на `bd ready`: `blocks`, `parent-child`, `conditional-blocks`, `waits-for`. Есть и non-blocking annotations: `related`, `tracks`, `discovered-from`, `caused-by`, `validates`, `supersedes`. Команда `bd ready` показывает работу без открытых blocking dependencies; `bd blocked` показывает, что именно держит задачу; `bd dep cycles` ищет циклы, а `bd graph` может выводить граф в compact / box / dot / html formats ([Beads Dependencies](https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md)).

Здесь особенно важна разница между relation и scheduling relation. Обычный трекер может дать related issue, но агентному исполнителю нужен ответ “можно ли брать задачу сейчас?”. Если в графе нет такого ответа, агент будет либо спрашивать человека, либо делать неготовую работу.

Для многопроходного документного процесса аналогичный primitive должен быть не “списком проходов”, а очередью готовой работы по проходам и документам:

- нормализация источников должна завершиться до прохода переноса в теорию;
- раскрытие источников должно быть выполнено до синтезирующего прохода;
- языковая вычитка должна идти после переноса фактуры, а не вместо него;
- замена канонического файла должна ждать отчёта о различиях и человеческого review gate;
- упавший проход должен иметь recovery state, а не запускать fresh reset.

Taskmaster показывает более лёгкую версию того же механизма. В его документации task хранится в `tasks.json` с полями `id`, `status`, `dependencies`, `priority`, `details`, `testStrategy`, `subtasks` и optional metadata; `tm next` выбирает pending / in-progress task, у которого выполнены зависимости, а `tm list --ready`, `tm list --blocking`, `tm validate-dependencies` и `tm fix-dependencies` поддерживают зависимостный порядок работы ([Taskmaster Task Structure](https://tryhamster.com/docs/taskmaster/capabilities/task-structure), [Taskmaster Dependencies](https://tryhamster.com/docs/taskmaster/task-workflow/dependencies)). Это не так богато, как Beads/Dolt, но полезно как промежуточная модель: file-based task graph, который можно положить рядом с кодом и дать агенту через CLI/MCP.

## Владение, закрепление и передача работы

Beads Multi-Agent Coordination описывает pinning work to an agent, проверку закреплённой работы через `bd hook`, последовательный handoff, параллельную работу, fan-out/fan-in, file reservations и issue locking ([Beads Multi-Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination)). Это не декоративная функция. Без ownership несколько агентов могут одновременно думать, что один и тот же кусок “свободен”, а после сбоя человек не понимает, кто должен продолжать.

Последовательный handoff в Beads выражается не только текстом “передаю тебе”. Агент A закрывает или обновляет issue, закрепляет его за agent B; agent B затем смотрит `bd hook` и принимает work. Для многопроходного документного процесса это означает, что worker/job должен знать:

- какой документ он ведёт;
- какой pass продолжает;
- какие файлы может менять;
- какой snapshot является входом;
- что он должен вернуть как delta;
- какой gate должен пройти перед записью канонического файла.

Handoff-заметка остаётся нужна, но она должна жить рядом с формальным состоянием. Иначе следующий агент читает объяснение, но не видит права на действие.

## Gates как долговечные асинхронные ожидания

`bd gate` моделирует асинхронные условия ожидания, которые блокируют шаги рабочего процесса. Gate types включают human, timer, GitHub run, GitHub PR и bead. `bd gate check` может проверять gates; GitHub gates используют `gh` CLI для запроса состояния run или PR; gate может разрешиться или перейти в escalation depending on result ([`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate)).

Это важное обобщение human gate. Gate — не просто фраза в prompt вроде “спроси пользователя”. Это долговечный объект ожидания в рабочем графе. В AI-driven SDLC человеческое ревью, CI, PR approval, timer, внешняя зависимость и завершение upstream-работы тоже ведут себя как gate-like objects.

Temporal cookbook даёт соседний durable-execution пример: AI-agent workflow может остановиться на рискованном действии и ждать человеческого подтверждения через Temporal Signal; документ подчёркивает экономное ожидание ресурсов, signal-based approval, durable timers и audit trail ([Temporal Human-in-the-Loop AI Agent](https://docs.temporal.io/ai-cookbook/human-in-the-loop-python)). Это не work graph в смысле Beads, но хорошо показывает, что “ждать человека” можно реализовывать как долговечное состояние процесса, а не как открытую вкладку с чатом.

Для многопроходного документного процесса durable gates могли бы представлять:

- не продолжать source accumulation, пока человек не принял source map;
- не заменять каноническое досье, пока не создан delta report;
- не начинать следующий pass, пока не прошла проверка языка;
- не считать проход завершённым, пока нет source links и image candidates;
- не выполнять destructive change без явного human gate.

## Prime и восстановление компактного контекста

`bd prime` — важная часть механизма, потому что сам по себе граф работы ещё не решает проблему контекстного окна. CLI reference описывает `bd prime` как AI-optimized markdown context: `--mcp` даёт compact brief, а CLI output обычно занимает около 1–2k tokens; команда предназначена для Claude Code, Gemini CLI и Codex SessionStart после compaction ([`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime)).

Это практичный урок. Не нужно каждый раз заставлять модель читать огромные директории, логи и все pass-файлы. Система должна собирать короткий prime: текущая работа, последний успешный pass, целевой файл, ограничения, открытые вопросы, допустимые файлы, следующий шаг и gates. Это не заменяет чтение источников, но экономит контекст и снижает вероятность случайного fresh reset.

LangGraph persistence показывает соседнюю реализацию на уровне execution graph. Checkpointer сохраняет состояние графа как checkpoints, организованные в threads; persistence используется для human-in-the-loop, memory, time travel и fault tolerance. Документация также описывает `thread_id` как primary key и pending writes recovery: успешные node writes внутри super-step долговечны, и их не нужно повторять, если другой node падает ([LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)). Это не issue graph, но полезная аналогия: агентный рабочий процесс должен иметь thread/job ID, checkpoints, точку продолжения и долговечные частичные записи.

## Маршрутизация и подтягивание связанных задач

Beads Routing поддерживает автоматическую маршрутизацию issues между репозиториями: `.beads/routes.jsonl` сопоставляет patterns с целевыми репозиториями; patterns могут матчить title, labels или явный префикс пути; есть команды проверки маршрутов; cross-repo dependencies можно выражать через `external:backend-repo/bd-100`, а `bd hydrate` подтягивает связанные issues из других репозиториев ([Beads Routing](https://gastownhall.github.io/beads/multi-agent/routing)).

Для Noveia и dev plugin это прямой дизайн-сигнал. Изменение процесса часто начинается в одном документе, но требует связанных правок в theory, Handbook, site, prompts, protocols и automation. Routing/hydration primitives позволяют представить это как связанный набор work items, а не как один неограниченный запрос “поправь всё”.

В таком процессе пока можно не строить полноценный cross-repo graph. Но уже в POC нужно избежать ошибки “всё в одном job”. Если проход по досье требует обновить source register, pass-артефакты, каноническое досье и discourse, эти действия должны быть связаны одним job ID, но различаться как sub-items с gates.

## Восстановление и операционная гигиена

Beads recovery docs дают единый формат runbook: симптомы, диагностика, решение и профилактика. Быстрая диагностика начинается с `bd status`, `bd doctor`, `bd blocked` ([Beads Recovery Overview](https://gastownhall.github.io/beads/recovery)). Architecture docs добавляют универсальную последовательность восстановления с `bd dolt stop`, `git worktree prune`, `bd dolt pull`, `bd dolt start`, а также предупреждают, что `bd doctor --fix` нужно использовать только после backup и dry run: автоматическое исправление может удалить зависимости, ошибочно признанные циклическими ([Beads Architecture](https://gastownhall.github.io/beads/architecture)).

Это важный corrective к гладкому тезису “сделаем устойчивое состояние”. Долговечное состояние не устраняет сбои; оно делает сбой диагностируемым. Для многопроходного документного процесса соответствующая модель должна включать:

- явный job status;
- last successful pass;
- last failed pass;
- команду продолжения;
- запрет на fresh reset без explicit force;
- короткий отчёт о сбое;
- audit trail для canonical-file replacements;
- проверку wrong-location artifacts, как уже случилось у нас с SDK child thread, который писал under `work/automation` вместо repo root.

## Обычные issue-графы как baseline, но не достаточное решение

GitHub Issues и Linear полезны как baseline: они показывают, что иерархия задач, отношения blocking / blocked и видимость bottlenecks уже стали нормальной частью рабочих систем. GitHub Docs описывает issue dependencies как отношения, где issues могут блокировать другую работу или сами быть заблокированы; blocked issues отмечаются в project boards или на issue pages. GitHub sub-issues допускают до 100 подзадач на parent issue и до восьми уровней вложенности, а прогресс parent issue виден в projects ([GitHub issue dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies), [GitHub sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)). Linear поддерживает related, blocked, blocking и duplicate issue relations; changelog отмечает появление записей в истории issue, когда blocking issue закрывается или открывается заново ([Linear issue relations](https://linear.app/docs/issue-relations), [Linear issue relations changelog](https://linear.app/changelog/2020-03-11-issue-relations)).

Для агентной разработки этого baseline недостаточно по трём причинам. Во-первых, эти системы обычно ориентированы на людей и project management surface, а не на compact context injection для агента. Во-вторых, readiness часто визуальна или workflow-driven, но не обязательно является CLI/MCP-first primitive. В-третьих, они не решают проблему compaction/resume на уровне агентной сессии.

Но baseline важен, чтобы не романтизировать Beads. Persistent Work Graph не начинается с AI. Он наследует давно известные свойства issue tracking: иерархия, зависимости, владелец, история, статус, блокировка. Новизна для агентной разработки в том, что эти свойства становятся исполняемым интерфейсом агента.

## Taskmaster как более лёгкий граф задач для AI-разработки

Taskmaster заслуживает отдельной пометки как более лёгкая модель. Он строит задачи из PRD, хранит их в `tasks.json`, генерирует отдельные task files и использует dependencies, priority, details и testStrategy. `tm next` выбирает самую приоритетную незаблокированную задачу, `tm clusters` группирует уровни зависимостей для параллельного выполнения, tags разделяют независимые рабочие потоки на отдельные task files, а `tm loop` может повторно выбирать следующую задачу, собирать prompt с полным контекстом задачи, запускать Claude Code, ждать structured completion markers, обновлять статус и продолжать работу после interruption ([Taskmaster Task Structure](https://tryhamster.com/docs/taskmaster/capabilities/task-structure), [Taskmaster Dependencies](https://tryhamster.com/docs/taskmaster/task-workflow/dependencies), [Taskmaster Tags](https://tryhamster.com/docs/taskmaster/task-workflow/tags), [Taskmaster Loop](https://tryhamster.com/docs/taskmaster/automation/loop)).

Для нашего досье Taskmaster важен не как конкурент Beads, а как другая точка в пространстве решений. Beads сильнее как распределённый графовый issue tracker с версионированным SQL-состоянием. Taskmaster ближе к файловому субстрату проектных задач: проще, понятнее, ближе к PRD/task workflow, но потенциально слабее под multi-writer merge, recovery и диагностику графа. Для многопроходного документного процесса это хорошее напоминание: первый POC не обязан начинаться с Beads-like storage. Можно начать с хорошо дисциплинированных JSON/status files, если они имеют job ID, dependencies, gates, pass-артефакты и recovery command. Но тогда нужно честно признать, где такой вариант слабее.

## Граф выполнения и граф работы

LangGraph, Temporal и Pydantic AI durable execution не являются прямыми источниками Persistent Work Graph. Они описывают другой слой: состояние выполнения agent/workflow, checkpoints, interrupts, timers, signals, resume и fault tolerance. Но этот слой полезен для досье, потому что Persistent Work Graph почти всегда соприкасается с durable execution.

LangGraph interrupts останавливают выполнение графа и сохраняют состояние до возобновления; вызывающий код продолжает выполнение через command, а `thread_id` указывает checkpointer на сохранённое состояние ([LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)). Pydantic AI описывает durable agents как agents, которые сохраняют progress при API failures, application errors и restarts; документация прямо называет long-running, asynchronous и human-in-the-loop workflows, а также перечисляет Temporal, DBOS, Prefect и Restate как supported durable execution integrations ([Pydantic AI Durable Execution](https://pydantic.dev/docs/ai/integrations/durable_execution/overview/)).

Разведение важно для теории:

- work graph отвечает на вопрос: какая работа существует, кто её ведёт, что готово, что заблокировано, что ждёт человека;
- execution graph отвечает на вопрос: где остановился конкретный workflow run и как его продолжить;
- context rehydration отвечает на вопрос: какую компактную рабочую правду дать следующей модели;
- evidence layer отвечает на вопрос: почему можно считать результат прохода или изменения достаточным.

Если эти слои смешать, получится опасная путаница. Можно иметь durable execution без нормальной рабочей очереди; можно иметь issue graph без durable execution; можно иметь markdown-memory без формальной готовности. Для многопроходного документного процесса нужны как минимум work graph + compact prime + pass-артефакты + recovery state. Durable execution можно добавлять позже, если TS-loop среда начнёт реально управлять long-running workers.


## Минимальная схема многопроходного документного процесса: job / pass / gate / prime / recovery

Для многопроходного документного процесса Persistent Work Graph нужен не как абстрактная архитектурная схема, а как практический слой, который исправляет уже видимые сбои: проход может стартовать из неправильного каталога, артефакты могут создаться не там, модель может объявить завершение без внешних следов, следующий запуск может нечаянно начать заново вместо продолжения. Поэтому минимальная схема должна начинаться не с Dolt/SQL, а с небольшого долговечного состояния, которое читается человеком, проверяется скриптом и достаточно строго направляет модель.

Минимальный объект `job`:

```json
{
  "job_id": "pwg-dossier-2026-06-09",
  "target_doc": "work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md",
  "base_snapshot": "git(5).zip",
  "state": "ready|running|blocked|waiting_human|recovering|done|failed",
  "owner": "assistant-run",
  "allowed_paths": [
    "work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md",
    "work/dossier-passes/persistent-work-graph/**",
    "work/discourse.md"
  ],
  "current_pass": 3,
  "next_action": "continue_from_last_successful_pass",
  "gates": [],
  "recovery": {}
}
```

Минимальный объект `pass`:

```json
{
  "pass_id": "cycle_03_parallel_shared_state",
  "pass_no": 3,
  "status": "planned|running|artifact_check|language_check|done|failed",
  "prompt_file": "cycle_03_prompt_parallel_shared_state.md",
  "source_queries": [],
  "opened_sources": [],
  "used_sources": [],
  "image_candidates": [],
  "artifacts": [],
  "checks": [],
  "next_hint": "narrow_followup_only"
}
```

Минимальный `gate`:

```json
{
  "gate_id": "inline-source-links",
  "blocks": "canonical_dossier_replacement",
  "resolver": "script_or_human_review",
  "evidence_required": [
    "new_source_links_are_inline",
    "source_register_updated",
    "image_candidates_updated"
  ],
  "status": "open|passed|failed|waived"
}
```

`prime` должен быть не пересказом всего досье, а компактной рабочей правдой для следующего вызова модели: целевой файл, последний успешный pass, незакрытые источники, обязательные языковые правила, запрет на fresh reset, требуемые артефакты, список открытых вопросов и точные границы правки. Это близко к `bd prime` в Beads, где команда предназначена для восстановления компактного контекста после сжатия. В многопроходном документном процессе `prime` должен дополнительно нести обязательства по источникам, языковые правила и список ожидаемых артефактов ([bd prime](https://gastownhall.github.io/beads/cli-reference/prime)).

`recovery` должен быть механическим. После сбоя система не должна спрашивать модель “что, кажется, делать дальше”. Она должна иметь last successful pass, failed operation, expected files, проверку `cwd`, команду повтора, запрет fresh reset и escalation note. Durable execution средаs показывают соседний слой: DBOS workflows checkpoint state, persist steps and outputs, а также позволяют query/restart failed workflows; Restate описывает durable execution через journal, timers, signals и resume ([DBOS Transact TypeScript](https://github.com/dbos-inc/dbos-transact-ts), [Restate durable execution](https://docs.restate.dev/concepts/durable_execution)). Но этот слой не заменяет job/pass/gate state: DBOS или Restate могут возобновить workflow run, а Persistent Work Graph должен сказать, какую работу вообще можно продолжать, какие источники уже использованы и какое человеческое решение ещё ждёт.

Пороговая рекомендация для многопроходного документного процесса: начать с файлового состояния и append-only ledgers, а не с полноценной базы. JSON/Markdown достаточно, если есть строгие checks. SQLite или Dolt-like хранилище становится оправданным только когда появляются настоящие параллельные writers, конфликтующие gates, query-heavy status views или необходимость сравнивать ветки состояния. Иначе storage layer начнёт съедать внимание раньше, чем появится реальная боль.

## Состояние источников и промежуточные артефакты

Для source-accumulation work graph должен хранить не просто список ссылок. У источника есть состояние:

```text
found → opened → read → used_in_main_text → used_in_source_register
                       ↘ candidate_image_only
                       ↘ rejected_with_reason
```

Это важно потому, что source register без inline transfer не доказывает, что источник реально вошёл в досье. В наших правилах источник должен появляться рядом с фактом в основном тексте, а не только в списке источников. Поэтому gate на проход должен проверять три вещи: ссылка внесена в основной текст; источник добавлен в register; если источник содержит полезную картинку или схему, кандидат внесён в раздел иллюстраций.

Свежая работа про durable intermediate artifacts полезна как теоретический сосед: она утверждает, что многошаговые агентные системы должны сохранять inspectable intermediate artifacts — typed, structured, addressable, versioned, dependency-aware и пригодными для downstream computation; при этом такие артефакты не являются private chain-of-thought, а являются maintained work products вроде evidence maps, criteria, assumptions, plans и unresolved tensions ([Intermediate Artifacts as First-Class Citizens](https://arxiv.org/abs/2605.12087)). Для многопроходного документного процесса это почти прямое описание статуса pass-файлов, source ledgers, delta reports, unresolved queues и image candidates. Они не должны быть скрытой “мыслью модели”; они должны быть внешними рабочими продуктами.

SKILL.nb добавляет полезную аналогию для gates: reusable workflows хранятся как auditable versioned notebooks, где natural-language guidance, executable cells, validation gates, fallback paths и multimodal evidence; runtime gate-conditioned execution решает, выполнять код или делать локальный fallback, если drift invalidates executable realization ([SKILL.nb](https://arxiv.org/abs/2606.08049)). Для многопроходного документного процесса это поддерживает идею: gate не обязан быть только человеческим approval. Gate может быть проверкой наличия артефактов, проверкой языка, проверкой ссылок, проверкой правки в правильном каталоге или проверкой, что stale source не используется без открытия заново.

AEGIS полезен как граница permissions: pre-execution firewall может перехватывать tool calls, удерживать high-risk calls for human approval и записывать решения в tamper-evident audit trail ([AEGIS](https://arxiv.org/abs/2603.12621)). Для Persistent Work Graph это не отдельная очередь задач, а слой исполнения gate: mutating canonical writes, network calls, deletion, secret-bearing operations и archive publication должны отличаться от read-only status queries.

## Параллельная работа агентов: общая среда, конфликты и пределы ускорения

Второе направление расширения — parallel-agent coordination. Здесь важно не сделать простую ошибку: “если есть общий граф работы, можно просто запускать больше агентов”. Общий граф работы решает readiness, ownership и handoff. Он не гарантирует, что параллельные правки кода, источников или досье будут семантически совместимы.

CodeCRDT предлагает coordination through shared convergent state: агенты наблюдают общую структуру работы и координируются через состояние, а не только через сообщения. В работе сформулированы требования к substrate: observable updates, deterministic convergence и monotonic progress; реализация строится на CRDT-структурах и TODO-claim protocol, где агенты утверждают ownership над TODO и проверяют claim before writing ([CodeCRDT](https://arxiv.org/abs/2510.18893)). Результаты важны как предупреждение, а не как реклама: в 600 trial evaluations эффект варьирует от 21.1% speedup до 39.4% slowdown в зависимости от типа задачи; character-level convergence не устраняет semantic conflicts, и 5–10% задач всё ещё имеют semantic conflicts. Авторы прямо отмечают quality/performance tradeoff, code length inflation и bounded scalability around 3–5 agents.

STORM атакует соседнюю проблему: worktree isolation даёт агентам независимость, но откладывает конфликт до merge. STORM делает write-time validation: агент читает локальный snapshot, а при записи система проверяет target file и read dependencies; если файл или зависимость устарели, запись отклоняется, а система возвращает current content, diff и stale dependency list. Дополнительно STORM поддерживает reservations и intent annotations, чтобы другие агенты видели, что участок работы уже занят или каков замысел изменения ([STORM paper](https://arxiv.org/html/2604.09003v1), [STORM GitHub repository](https://github.com/haipham2306/STORM-CodeAgent)). Но и здесь границы существенны: STORM не координирует shell commands, terminal bypass remains a limitation, file-level granularity can create false positives, а оставшиеся failures включают semantic, task-boundary и budget issues.

MAST полезен как отрицательная проверка. В статье о failure modes multi-agent LLM systems failures often arise from organizational design and agent coordination, not only individual model limitations; communication protocols can be insufficient, agents reset, make wrong assumptions or withhold information ([Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)). Для Persistent Work Graph это означает: мало дать агентам общий список задач. Нужно задавать ownership, dependency readiness, evidence gates, verification path и escalation points.

Для многопроходного документного процесса это даёт строгие правила параллельности:

1. Параллелить можно независимые source shards или разные target documents, а не два writer на одно каноническое досье.
2. У каждого worker должен быть read snapshot: версия target doc, source register, discourse и pass folder.
3. Запись в канонический файл допускается только через владельца или merge pass.
4. Если source register или `work/discourse.md` изменились после read snapshot, worker должен re-prime или перейти в recovery.
5. Gates должны блокировать не только human approval, но и stale read, wrong cwd, duplicate source transfer, missing image candidates и unverified external facts.
6. Semantic conflicts cannot be solved by CRDT convergence alone: нужен отдельный synthesis pass, который проверяет, не противоречат ли друг другу независимые вставки.

Итоговая граница:

```text
Persistent Work Graph ≠ CRDT editor
Persistent Work Graph ≠ STORM-like file mediator
Persistent Work Graph ≠ durable execution runtime
```

Persistent Work Graph должен задавать durable work state. CRDT/shared-state coordination может помочь с concurrent editing. STORM-like mediation может защитить write-time consistency. Durable execution может возобновлять runs. Но качество досье всё равно зависит от источников, синтезирующего прохода, human gate и language/style repair.

## Протокол безопасной параллельной работы с источниками

Для source discovery и source opening параллелизм обычно полезнее, чем для записи в канонический текст. Источники можно искать по независимым направлениям, открывать в отдельных контекстах и возвращать сжатые findings. Но перенос фактуры в досье требует другого режима: один синтезирующий проход должен увидеть все возвращённые фрагменты, проверить дубликаты, противоречия, качество источников, кандидаты на иллюстрации и соответствие языковым правилам. Иначе параллельная работа ускорит сбор сырья, но ухудшит основной документ.

Ближайший сильный источник для такого режима — Anthropic Research. В их multi-agent research system ведущий агент планирует работу, создаёт subagents с отдельными аспектами поиска, собирает результаты и передаёт итог citation agent, который привязывает утверждения к источникам. В статье отдельно названы ошибки раннего режима: subagents дублировали поиск, расходились по темам или продолжали работу после достаточного результата; решение состояло не в свободном запуске большего числа агентов, а в явных objectives, output format, source/tool guidance и task boundaries для каждого subagent ([Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)). Там же важна оценочная рамка: factual accuracy, citation accuracy, completeness, source quality и tool efficiency. Для наших досье это почти прямой список gate-проверок перед заменой канонического файла.

Anthropic также показывает границы параллелизма. Multi-agent research хорошо работает для широких исследовательских задач с независимыми направлениями, но хуже подходит для доменов, где всем агентам нужен один и тот же контекст или много зависимостей между действиями. Они отдельно отмечают, что coding tasks часто имеют меньше реально независимых частей, чем research tasks, а асинхронное выполнение добавляет проблемы согласования результатов, согласованности состояния и распространения ошибок. Для работы с источниками вывод такой: параллелить можно поиск и раскрытие источников, но перенос в канонический текст и финальный синтез должны оставаться последовательными или проходить через явный gate слияния.

Документация Claude Code даёт второй практический слой. Subagents запускаются в отдельном контексте и возвращают итоговое резюме; agent teams предназначены для нескольких независимых сессий с общими задачами и обменом сообщениями между участниками; worktrees изолируют параллельные правки файлов, а не решают сами задачу координации ([Claude Code extensions](https://code.claude.com/docs/en/features-overview), [Claude Code worktrees](https://code.claude.com/docs/en/worktrees)). Codex Worktrees описывает близкую модель для Codex: отдельные worktrees позволяют запускать независимые задачи в одном проекте, а Handoff безопасно переносит работу между Local и Worktree через Git-операции ([OpenAI Codex Worktrees](https://developers.openai.com/codex/app/worktrees)). Базовый Git `worktree` остаётся техническим основанием: это несколько рабочих деревьев одного репозитория с отдельными checkout, метаданными веток и командами cleanup/repair ([Git worktree documentation](https://git-scm.com/docs/git-worktree)).

Из этих источников получается проект протокола безопасной параллельной работы с источниками.

1. **Координатор создаёт исследовательский план.** План содержит целевой документ, base snapshot, список независимых направлений поиска, границы файлов, критерии качества источников, обязательный формат возврата и запрет на запись в каноническое досье для workers, которые занимаются источниками.

2. **Направление поиска должно быть независимым.** Хорошее направление ищет отдельный класс источников: официальную документацию, статьи, репозитории, issues, визуальные кандидаты, отчёты о сбоях или baseline tools. Плохое направление звучит как “поищи ещё про тему”: оно почти гарантирует дублирование и пересечение с другими workers.

3. **Каждый worker получает read snapshot.** Минимальный snapshot: версия целевого досье, версия source register, версия pass-folder, хвост discourse и список уже использованных источников. Worker обязан вернуть snapshot id в результате. Если за время работы изменился source register или целевое досье, результат нельзя сразу переносить в канонический файл.

4. **Source claim защищает от дублирования.** Перед глубоким раскрытием источника worker записывает claim: URL, source type, shard id, intended use и статус. Если другой worker уже раскрыл тот же источник, новый worker либо дополняет недостающий угол, либо помечает источник как duplicate-support, но не переносит те же факты вторично.

5. **Worker возвращает не прозу для вставки, а пакет свидетельств.** Пакет должен содержать: opened sources, точные факты, возможные цитируемые места, ограничения источника, rejected leads, image candidates, предложенные inline links и нерешённые напряжения. Это снижает риск, что канонический текст станет суммой несогласованных фрагментов.

6. **Проверка источников и ссылок отделена от синтеза.** Перед переносом в досье отдельная проверка смотрит, есть ли источник рядом с фактом, не перепутан ли первичный источник с пересказом, не остались ли кандидаты на картинки только в рабочем файле, нет ли устаревшего источника, который нужно переоткрыть.

7. **Каноническую запись делает один владелец.** Параллельные workers не правят основной файл. Их результаты входят в merge/synthesis pass, где один владелец выбирает порядок материала, устраняет дублирование, фиксирует противоречия и проводит языковой проход. STORM-like write-time validation может быть полезна, но даже она не заменяет смысловой merge: согласованность на уровне файла не доказывает, что итоговый досье-раздел стал цельным.

8. **Кандидаты на иллюстрации имеют отдельный gate.** Кандидат на картинку должен иметь source, intended use, тип изображения, будущий целевой раздел и rights/check status. Если источник содержит полезную схему, но она не попала в image candidates, source pass считается неполным.

9. **После параллельной фазы нужен synthesis pass.** Он проверяет coverage по направлениям поиска, противоречия между источниками, duplicate facts, missing source links, перенос image candidates и языковой сдвиг. Только после этого можно заменять каноническое досье и обновлять discourse.

Минимальная структура записи для такого процесса:

```json
{
  "source_work_item_id": "pwg-c04-anthropic-research-system",
  "shard": "multi_agent_research_architecture",
  "worker": "source-worker-2",
  "read_snapshot": {
    "target_doc_hash": "...",
    "source_register_hash": "...",
    "discourse_hash": "..."
  },
  "claimed_sources": [
    {
      "url": "https://www.anthropic.com/engineering/multi-agent-research-system",
      "status": "opened",
      "intended_use": "protocol design and image candidate"
    }
  ],
  "return_package": {
    "facts": [],
    "inline_link_suggestions": [],
    "image_candidates": [],
    "rejected_leads": [],
    "open_questions": []
  },
  "write_permission": "no_canonical_write"
}
```

Такой протокол не требует сразу строить сложную базу. Его можно поддержать файлами `source_claims.jsonl`, `source_worker_returns/*.md`, `synthesis_plan.md` и gate-проверкой перед канонической записью. Persistent Work Graph здесь нужен как слой, который делает параллельную работу с источниками видимой: кто какой источник взял, на каком snapshot он работал, что вернул, какие факты попали в основной текст, какие картинки потеряны, и почему следующий проход должен быть merge/synthesis, а не очередным независимым поиском.

## Сравнительные якоря

| Механизм | Долговечный объект работы | Gate / блокировка | Восстановление | Главный риск |
| --- | --- | --- | --- | --- |
| Beads / Gas Town | bead / issue / molecule / wisp | `bd gate`, dependencies, pinned work, очередь готовой работы | Dolt history, `bd status`, `bd doctor`, runbooks, hooks | сложность, Dolt/server failure modes, local-first sync limits, product lock-in |
| GitHub Issues | issue, sub-issue, project item | blocked / blocking relations, project views | issue history, project state, GitHub APIs | human-facing surface, слабая rehydration для агента, external SaaS dependency |
| Linear | issue, sub-issue, relation, project | blocked / blocking flags, issue history | workspace history и workflow statuses | человеческий/team workflow, сам по себе не substrate для coding agent |
| Taskmaster | `tasks.json`, task files, tags | dependencies, `tm next`, ready/blocking filters, clusters | task files, loop progress, manual/CLI resume | JSON conflict risk, weaker structured recovery, task plan drift |
| LangGraph | thread, checkpoint, state snapshot | interrupts, graph control flow | checkpointer, pending writes, resume по `thread_id` | слой execution state, а не ownership / work allocation |
| DBOS / Restate | workflow instance, step journal, queue item | durable queues, rate/concurrency limits, signals/timers | checkpoint/journal, query/restart failed workflow | execution graph can be mistaken for work graph |
| Pydantic AI durable agents | agent run with durable backend | durable integrations, human-in-the-loop workflow support | сохраняет progress при failures/restarts | интеграционный слой, не определяет work ownership |
| CodeCRDT | shared CRDT document / TODO skeleton / claim | TODO claim protocol, shared observation | deterministic convergence and visible updates | semantic conflicts, task coupling, speedup only on suitable tasks |
| STORM | shared workspace file with read snapshot | write-time validation, reservations, intent annotations | rejected write returns current content, diff and stale dependency list | terminal bypass, no command coordination, file-level false positives |
| Intermediate artifacts | typed/versioned evidence map, plan, criteria, unresolved tension | artifact lineage and supersession semantics | maintained artifacts across revisions | can become artifact bureaucracy without quality gate |
| AEGIS | intercepted tool call and audit record | pre-execution firewall, policy validation, human escalation | tamper-evident audit trail | protects tool boundary, not work allocation |
| Spec Kit | `tasks.md`, specs, workflows | task boundaries, workflow gates | manual resume / workflow state | too much product surface, spec drift |
| BMAD | story files, project context, checkpoints | phase gates, QA/review steps | continue/fresh discipline, checkpoints | ceremony и token overhead |
| GSD | state/trace/gates/heartbeats | validation gates, context budget | checkpoints, watchdog/heartbeat | orchestrator complexity |
| Многопроходный документный процесс | job/pass-артефакты, status, ledgers | artifact gates, source gates, language gates, human review | continue/start-pass, recovery report, exact artifact check | token blow-up, accidental fresh reset, wrong cwd/path, false completion |

## Проектные примитивы для многопроходного документного процесса

1. **Job как долговечный объект.** Запуск многопроходного документного процесса не должен быть только процессом. Ему нужны ID, owner, target document, base snapshot, state, allowed files, read snapshot и next action.
2. **Pass как рабочий элемент.** У каждого pass должны быть input source set, output delta, status, token usage при наличии, использованные source links, image candidates, artifacts, checks и continuation pointer.
3. **Очередь готовой работы.** Система должна знать, какой pass готов, а какой заблокирован source map, человеческим ревью, token budget, previous failure, stale snapshot или missing artifacts.
4. **Владение и locks.** Worker должен владеть ровно одним target file/shard и не должен делать fresh reset без explicit force. Для параллельной работы нужен lock per target doc, а не общий оптимизм “агенты договорятся”.
5. **Read snapshot.** Pass должен знать версии target doc, source register, discourse и pass folder at start. Если они изменились, следующий worker делает re-prime или отдельный merge/synthesis pass.
6. **Gates.** Human approval, budget threshold, no-glossary-violations, source coverage, artifact presence, image-candidate transfer, no-degradation checks и stale-read checks должны быть gates, а не прозаическими напоминаниями.
7. **Prime.** Каждый вызов модели должен получать compact job prime: current target, last pass, source obligations, language/style constraints, open questions, expected artifacts, forbidden shortcuts, stale warnings и write boundary.
8. **Source state.** Source register должен знать состояние источника: `found`, `opened`, `read`, `used_in_main_text`, `candidate_image_only`, `rejected_with_reason`.
9. **Image state.** У image candidates должны быть source, role, rights/check status, target future section и признак: source screenshot или synthetic diagram.
10. **Recovery runbook.** После interruption следующий шаг должен выводиться механически: продолжить с pass N, повторить failed source, восстановить missing artifact, re-prime after stale read или передать на escalation.
11. **Версионированная запись канонического файла.** Замена канонического досье должна создавать snapshot, delta report и human-readable apply notes.
12. **Проверка wrong-location artifacts.** Среда должна проверять, что pass-артефакты созданы от repository root и в ожидаемой pass folder, а не в tool cwd.
13. **Pre-execution permission gate.** Read-only graph operations, mutating job-state operations, canonical writes, network fetches и archive publication должны быть разными классами действий.
14. **Synthesis pass для параллельных результатов.** После независимых workers нужен отдельный pass, который проверяет semantic conflicts, duplicate source transfer, противоречия в терминологии и style drift.
15. **Граница графа и текста.** Граф должен направлять выполнение, но текст досье остаётся читаемым человеком. Рабочее состояние не должно стать скрытой базой данных, которую будущие writers не могут проверить.

## Режимы сбоя и риски чрезмерного применения

**Graph theater.** Команда может создать граф задач и всё равно оставить настоящие решения в чате. Если зависимости не влияют на очередь готовой работы, gates не блокируют действие, а ownership не меняет поведение, граф остаётся декорацией.

**Stale graph.** Устойчивое состояние может быть опаснее эфемерного, если агенты доверяют ему после того, как изменились код, source map или решение человека. Persistent Work Graph требует правил stale detection и cleanup.

**False completion.** Агент отмечает задачу выполненной, потому что произвёл текст, а не потому что существуют нужные артефакты. Для многопроходного документного процесса это значит: after/delta/should_stop files, inline source links, image candidates и language repair должны проверяться механически.

**Wrong authority.** Агент может обновить статус задачи, но не может принять архитектурное или редакционное решение, которое этот статус представляет. Human gates и tool gates должны оставаться разными контурами.

**Storage complexity.** Beads/Dolt-style state даёт версионированную структуру, но добавляет server modes, sync, repair и corruption runbooks. Для одиночной локальной среды более простой JSON/SQLite-слой может быть лучше до момента, когда concurrency реально начнёт болеть.

**Auto-approval collapse.** Beads plugin docs отмечают, что approval в Claude Code MCP сейчас грубый: manual approval безопасен, но прерывает workflow; server-level auto-approval удобен, но одобряет любую beads operation; per-tool approval granularity в такой настройке нет ([Beads plugin docs](https://github.com/gastownhall/beads/blob/main/docs/PLUGIN.md)). Для нашего многопроходного документного процесса это напрямую ложится на дизайн permissions: read-only graph operations и mutating canonical writes не должны жить под одним недифференцированным approval.

**Metadata leaks.** Taskmaster metadata docs предупреждают, что secrets и sensitive credentials нельзя хранить в task metadata: task data может попадать в logs, exports или передаваться AI providers ([Taskmaster Task Structure](https://tryhamster.com/docs/taskmaster/capabilities/task-structure)). Многопроходный документный процесс тоже должен считать job state видимым для tools и, возможно, model providers; secrets не должны попадать в job metadata.

**Semantic convergence trap.** CRDT/shared-state coordination может дать deterministic convergence, не сняв semantic conflict. CodeCRDT reports zero character-level convergence failures, но всё равно оставляет 5–10% semantic conflicts; это значит, что “текст сошёлся” не равно “решение согласовано” ([CodeCRDT](https://arxiv.org/abs/2510.18893)).

**Read-snapshot staleness.** STORM показывает, что агент может писать из устаревшей картины мира. Если target file не изменился, но read dependency изменилась, итоговая правка всё равно может быть неправильной. Для многопроходного документного процесса это относится к source register, discourse, skeleton и snapshot канонического досье ([STORM paper](https://arxiv.org/html/2604.09003v1)).

**Command side-effect gap.** STORM прямо ограничен тем, что terminal commands can bypass workspace mediation. Для многопроходного документного процесса похожий риск возникает, если script changes files outside expected path или updates archive without passing gates. Поэтому graph state должен быть связан с filesystem checks.

**Coordination overconfidence.** MAST показывает, что failures in multi-agent systems часто связаны с organizational design и coordination, а не только с individual model weakness. Больше агентов без ownership, gates и verification может ухудшить, а не ускорить работу ([MAST](https://arxiv.org/abs/2503.13657)).

## Что должно попасть в теорию

В теории Persistent Work Graph должен появиться не как “ещё один инструмент”, а как переносимый механизм между context files и Gas Town:

- сессия агента не является достаточным носителем работы;
- задача должна стать долговечным объектом;
- зависимости должны влиять на готовность работы;
- owner / pin / lock нужны для многоагентной работы и восстановления;
- gates должны быть долговечными объектами ожидания;
- compact prime возвращает агенту рабочую правду без полного перечитывания всего проекта;
- source state и intermediate artifacts превращают поиск, перенос фактуры и unresolved tensions в inspectable maintained work products;
- parallel execution требует read snapshots, locks, write-time validation или merge/synthesis pass;
- durable execution остаётся соседним, но недостаточным слоем: он возобновляет runs, а work graph управляет существованием работы, readiness и authority;
- Gas Town / Beads остаётся deep case, где механизм показан в наиболее сильной форме.

Важно не превратить теоретический раздел в пересказ Beads docs, CodeCRDT или STORM. Достаточно объяснить механизм, показать его границы и дать Gas Town как глубокий пример. Технические подробности Beads, Taskmaster, LangGraph, DBOS, Restate, CodeCRDT, STORM и GitHub/Linear лучше держать в технический атлас или в этом досье.

## Что лучше уйдёт в Handbook / Fieldbook

В Handbook полезно перенести практические правила:

- как понять, что проекту уже недостаточно markdown-плана;
- какие поля нужны минимальному job object;
- какие поля нужны pass object;
- как хранить source state и image candidate state;
- когда достаточно `tasks.json`/JSON-status, а когда нужен полноценный issue graph;
- когда можно начать с JSON/Markdown, когда переходить к SQLite, когда рассматривать Dolt-like хранилище;
- как писать handoff так, чтобы он был связан со status/dependencies/gates;
- как задавать очередь готовой работы и blocked work для агента;
- как не хранить секреты и личные данные в task metadata;
- как проверять, что agent run не создал artifacts in wrong cwd;
- как задавать read snapshot и stale-read gate;
- как безопасно параллелить source shards, но не записи в каноническое досье;
- как разделять read-only graph commands, mutating graph commands и canonical publication.

В Fieldbook можно вынести маленькие сценарии:

- source pass одного досье с durable job state;
- recovery упавшего прохода;
- human review gate перед заменой канонического файла;
- расширение источников двумя workers с lock per target file;
- context prime after compaction;
- stale source register recovery;
- merge/synthesis pass after parallel source shards;
- permission gate before archive publication;
- minimal TS-loop job/pass/gate JSON schema.

## Источники

- Beads Documentation: [https://gastownhall.github.io/beads/](https://gastownhall.github.io/beads/) — основной источник по Beads как трекеру задач на Dolt для coding workflows под надзором AI; важен для AI-native workflows, hash-based IDs, Dolt-backed storage, dependency-aware execution, formulas, gates, molecules и multi-agent coordination.
- Beads GitHub repository: [https://github.com/gastownhall/beads](https://github.com/gastownhall/beads) — README формулирует Beads как distributed graph issue tracker for AI agents и persistent structured memory for coding agents; формулировка важна как самоназвание проекта.
- Beads Architecture: [https://gastownhall.github.io/beads/architecture](https://gastownhall.github.io/beads/architecture) — Dolt как source of truth, auto-commits, server/embedded modes, multi-clone risks, recovery model и границы применимости Beads.
- Beads Dependencies: [https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md](https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md) — dependency types, `bd ready`, `bd blocked`, graph formats, cycle detection; важнейший источник для очереди готовой работы.
- Beads Multi-Agent Coordination: [https://gastownhall.github.io/beads/multi-agent/coordination](https://gastownhall.github.io/beads/multi-agent/coordination) — pinning, hooks, handoff, fan-out/fan-in, file reservations, locking, comments и labels.
- Beads Codex Integration: [https://gastownhall.github.io/beads/integrations/codex](https://gastownhall.github.io/beads/integrations/codex) — Codex hooks и `bd prime` context injection; использовать вместе со страницей `bd prime`.
- `bd prime`: [https://gastownhall.github.io/beads/cli-reference/prime](https://gastownhall.github.io/beads/cli-reference/prime) — AI-optimized context rehydration after compaction; сильный источник для compact prime idea.
- `bd gate`: [https://gastownhall.github.io/beads/cli-reference/gate](https://gastownhall.github.io/beads/cli-reference/gate) — durable async gates: human, timer, GitHub run, GitHub PR, bead; полезно для понимания gates как долговечных ожиданий.
- Beads Recovery Overview: [https://gastownhall.github.io/beads/recovery](https://gastownhall.github.io/beads/recovery) — формат recovery runbook и быстрые diagnostic commands.
- Beads Troubleshooting: [https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md) — practical failure modes: wrong database/server, port conflicts, corruption, repair caution.
- Beads Routing: [https://gastownhall.github.io/beads/multi-agent/routing](https://gastownhall.github.io/beads/multi-agent/routing) — routing rules, cross-repo dependencies и hydration.
- Beads plugin docs: [https://github.com/gastownhall/beads/blob/main/docs/PLUGIN.md](https://github.com/gastownhall/beads/blob/main/docs/PLUGIN.md) — workflow commands, dependency types, Claude Code MCP approval trade-offs и task-agent loop.
- DoltHub — A Day in Gas Town: [https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/) — полевое объяснение Beads/Gas Town persistence; полезно для Gas Town deep case, но не раскрывалось заново в этом проходе.
- DoltHub — Multi-Agent Coordination with Dolt and Beads: [https://www.dolthub.com/blog/2026-04-22-multi-agent-dolt-beads/](https://www.dolthub.com/blog/2026-04-22-multi-agent-dolt-beads/) — structured/versioned shared state for agent tasks; полезно для Gas Town deep case, но не раскрывалось заново в этом проходе.
- GitHub issue dependencies: [https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies) — mainstream baseline для blocked / blocking relationships.
- GitHub sub-issues: [https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues) — mainstream hierarchy baseline; полезный контраст с AI-native graph.
- Linear issue relations: [https://linear.app/docs/issue-relations](https://linear.app/docs/issue-relations) — human/team issue relation baseline, including blocked / blocking / duplicate.
- Linear issue relations changelog: [https://linear.app/changelog/2020-03-11-issue-relations](https://linear.app/changelog/2020-03-11-issue-relations) — показывает history entries для blocking/resolution events; полезно для history-as-state.
- Taskmaster GitHub repository: [https://github.com/eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) — AI-powered task-management system for AI-driven development; полезен как более лёгкий file/CLI-based graph.
- Taskmaster Task Structure: [https://tryhamster.com/docs/taskmaster/capabilities/task-structure](https://tryhamster.com/docs/taskmaster/capabilities/task-structure) — `tasks.json`, metadata, testStrategy, complexity reports, `next`, metadata caveats.
- Taskmaster Dependencies: [https://tryhamster.com/docs/taskmaster/task-workflow/dependencies](https://tryhamster.com/docs/taskmaster/task-workflow/dependencies) — `tm next`, `tm list --ready`, `tm list --blocking`, `tm clusters`, validation и dependency rules.
- Taskmaster Tags: [https://tryhamster.com/docs/taskmaster/task-workflow/tags](https://tryhamster.com/docs/taskmaster/task-workflow/tags) — workstreams как separate task files, tag movement, conflict suggestions.
- Taskmaster Loop: [https://tryhamster.com/docs/taskmaster/automation/loop](https://tryhamster.com/docs/taskmaster/automation/loop) — automated loop: выбор следующей задачи, сбор контекста, запуск Claude Code, ожидание completion marker, обновление статуса, resume.
- LangGraph Persistence: [https://docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — checkpoints, threads, memory, time travel, fault tolerance и pending writes; соседний источник по execution state.
- LangGraph Interrupts: [https://docs.langchain.com/oss/python/langgraph/interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — dynamic interrupts, saved graph state, resume via command; соседний источник по долговечным человеческим ожиданиям.
- Temporal Human-in-the-Loop AI Agent: [https://docs.temporal.io/ai-cookbook/human-in-the-loop-python](https://docs.temporal.io/ai-cookbook/human-in-the-loop-python) — human approval via Signals, durable timers и audit trail; соседний источник по durable execution.
- Pydantic AI Durable Execution: [https://pydantic.dev/docs/ai/integrations/durable_execution/overview/](https://pydantic.dev/docs/ai/integrations/durable_execution/overview/) — durable agents, сохраняющие progress при failures и restarts; supported integrations Temporal / DBOS / Prefect / Restate.
- DBOS Transact TypeScript: [https://github.com/dbos-inc/dbos-transact-ts](https://github.com/dbos-inc/dbos-transact-ts) — durable workflows on Postgres, checkpointed workflow steps, durable queues, querying и restarting failed workflows; использовать как соседний слой durable execution, не как work graph.
- Restate durable execution: [https://docs.restate.dev/concepts/durable_execution](https://docs.restate.dev/concepts/durable_execution) — journaled steps, timers, signals и resumability; полезно для recovery model and human approvals.
- Intermediate Artifacts as First-Class Citizens: [https://arxiv.org/abs/2605.12087](https://arxiv.org/abs/2605.12087) — typed, structured, addressable, versioned, dependency-aware intermediate artifacts; важный источник для source/pass ledgers as maintained work products.
- SKILL.nb: [https://arxiv.org/abs/2606.08049](https://arxiv.org/abs/2606.08049) — auditable versioned notebooks, validation gates, fallback paths и multimodal evidence; полезно для gate-conditioned execution and drift handling.
- AEGIS: [https://arxiv.org/abs/2603.12621](https://arxiv.org/abs/2603.12621) — pre-execution firewall, human escalation and tamper-evident audit trail for tool calls; полезно для permission gates.
- CodeCRDT: [https://arxiv.org/abs/2510.18893](https://arxiv.org/abs/2510.18893) — observation-driven coordination through shared convergent state, TODO claim protocol, speedup/slowdown results и semantic conflict limits; использован для parallel-agent coordination boundary.
- STORM: [https://arxiv.org/html/2604.09003v1](https://arxiv.org/html/2604.09003v1) — state-oriented management with read snapshots, write-time validation, stale dependency rejection, reservations и intent annotations; важен как соседний механизм для concurrent file writes.
- STORM GitHub repository: [https://github.com/haipham2306/STORM-CodeAgent](https://github.com/haipham2306/STORM-CodeAgent) — experiment runner, outputs, reports и implementation surface; полезен для технический атлас and illustration candidates.
- Why Do Multi-Agent LLM Systems Fail?: [https://arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657) — MAST taxonomy and failure analysis; источник для тезиса, что multi-agent failures часто связаны с organizational design и coordination.
- Multi-Agent Collaboration Mechanisms survey: [https://arxiv.org/abs/2501.06322](https://arxiv.org/abs/2501.06322) — широкий обзор mechanisms for multi-agent collaboration; source pool для следующего возможного pass.

## Cycle 04 — safe parallel source-work protocol sources

- Anthropic multi-agent research system: [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) — lead agent, subagents, citation agent, task boundaries, duplicate-work failures, source/citation quality criteria and limits of multi-agent parallelism.
- Claude Code extensions: [https://code.claude.com/docs/en/features-overview](https://code.claude.com/docs/en/features-overview) — subagents, agent teams, hooks, MCP and isolated contexts as practical source-work surfaces.
- Claude Code worktrees: [https://code.claude.com/docs/en/worktrees](https://code.claude.com/docs/en/worktrees) — separate worktrees for parallel sessions, cleanup and worktree locks.
- OpenAI Codex Worktrees: [https://developers.openai.com/codex/app/worktrees](https://developers.openai.com/codex/app/worktrees) — independent Codex tasks, worktree handoff and Git-backed isolation.
- Git worktree documentation: [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) — canonical Git semantics for multiple working trees, cleanup and repair.
- LangChain multi-agent docs: [https://docs.langchain.com/oss/python/langchain/multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent) — subagents, handoffs, router and custom workflow patterns; useful as general pattern vocabulary, not as source-specific evidence for our repository process.

## Поисковые формулировки

Уже использованные:

- `Beads persistent work graph AI coding agents Dolt`
- `Beads multi-agent coordination pin handoff fan-out fan-in`
- `bd prime Codex hooks compaction recovery`
- `bd gate durable async human CI wait condition`
- `agentic work graph durable state versioned SQL Dolt`
- `AI coding agents persistent issue graph task dependencies recovery`

Добавлены в проходе 2026-06-09:

- `Beads bd blocked очередь готовой работы dependencies docs`
- `Beads CLI reference blocked status doctor recovery docs`
- `GitHub Issues sub-issues dependencies blockers official docs`
- `Linear issue relations blocking blocked official docs`
- `Task Master AI Claude Code task dependencies tasks.json GitHub`
- `Taskmaster tm next ready blocking validate dependencies loop docs`
- `LangGraph durable execution persistence interrupts human in the loop checkpoints official docs`
- `Temporal durable execution AI agents human in the loop workflow official docs`
- `Pydantic AI durable agents Temporal DBOS Prefect Restate docs`
- `multi-agent LLM code generation shared state coordination CRDT`

Добавлены в проходах 2026-06-09 по многопроходному документному процессу и parallel-agent coordination:

- `DBOS durable workflow TypeScript agent queue recovery`
- `Restate durable execution journaled steps timers signals AI agents`
- `durable intermediate artifacts agentic systems versioned dependency-aware`
- `SKILL.nb gated execution durable workflows versioned notebooks evidence screenshots`
- `AEGIS pre-execution firewall audit layer AI agents tool calls human approval`
- `CodeCRDT observation-driven coordination CRDT LLM agents semantic conflicts`
- `STORM state-oriented management multi-agent collaboration worktree isolation conflict write-time validation`
- `multi-agent LLM systems fail MAST inter-agent misalignment verification`
- `parallel AI coding agents shared state conflicts semantic collisions`


Добавлены в проходе 2026-06-09 по safe parallel source-work protocol:

- `Anthropic multi-agent research system lead agent subagents citation agent source quality`
- `Claude Code subagents isolated context agent teams official docs`
- `Claude Code worktrees parallel sessions official docs`
- `OpenAI Codex Worktrees independent tasks handoff official docs`
- `Git worktree multiple working trees official documentation`
- `LangChain multi-agent subagents router handoffs shared state official docs`
- `safe parallel source discovery citation audit multi-agent research`

## Кандидаты на иллюстрации

| ID | Источник | Что изображать | Зачем использовать | Статус |
| --- | --- | --- | --- | --- |
| `fig-persistent-work-graph-core` | это досье + Beads docs | Рабочий элемент с dependency, owner, gate, handoff, history и prime | Главная схема механизма для теории | Синтетическая схема, можно рисовать самостоятельно |
| `fig-beads-dolt-stack` | Beads Architecture | Agent sessions → Beads CLI/MCP/hooks → Dolt DB/version history → remote sync | Показывает structured/versioned substrate | Кандидат; права/перерисовку проверить |
| `fig-beads-ready-queue` | Beads Dependencies | Dependency DAG: слой 0 — ready work, слой 1 — blocked work, `bd ready` / `bd blocked` | Лучше всего объясняет очередь готовой работы | Синтетическая схема на основе команд; безопаснее перерисовать |
| `fig-bd-prime-rehydration` | `bd prime` + Codex integration | SessionStart/PostCompact → `bd prime` → compact context restored | Связывает граф с экономией контекста | Синтетическая схема, можно делать локально |
| `fig-gates-as-durable-waits` | `bd gate` + Temporal HITL | Issue/workflow заблокирован до human approval, timer, GitHub run, PR или dependency resolution | Поддерживает тему gates/human-in-loop | Синтетическая схема; источник фактуры Beads + Temporal |
| `fig-routing-hydration` | Beads Routing | Issue создан в main repo, routed to backend/frontend/docs repo, затем hydrated back как cross-repo dependency | Показать, как work graph выходит за один файл/репозиторий | Синтетическая схема |
| `fig-taskmaster-tasks-json` | Taskmaster Task Structure | `tasks.json` fields: status, dependencies, priority, testStrategy, metadata | Показать лёгкий file-based AI task graph | Можно сделать собственный sanitized snippet, не скриншот |
| `fig-taskmaster-loop` | Taskmaster Loop | `tm loop`: choose next task → build context → launch Claude Code → completion marker → update status | Показать более лёгкий автоматический work loop | Синтетическая схема |
| `fig-langgraph-checkpoint-thread` | LangGraph Persistence | `thread_id` → checkpoints → resume / time travel / pending writes | Развести work graph и execution graph | Кандидат; лучше перерисовать по документации |
| `fig-github-subissues-baseline` | GitHub sub-issues docs | Parent issue с nested sub-issues и project progress | Baseline for non-AI issue hierarchy | В источнике есть screenshot in docs; права проверить |
| `fig-linear-blocked-flag-baseline` | Linear issue relations docs | Blocked / blocking issue flags | Baseline for human team dependency relation | возможен screenshot/diagram; права проверить |
| `fig-multi-pass-document-workflow-future-state` | это досье + дизайн многопроходного документного процесса | Модель `job/pass/status/gate/prime/recovery` для многопроходного документного процесса | Проектная схема для собственной среды | Синтетическая схема, не source image |
| `fig-multi-pass-document-workflow-job-pass-state-machine` | это досье + дизайн многопроходного документного процесса | Состояния `job`: ready → running → artifact_check → language_check → waiting_human / done / recovering | Показать минимальный work graph для многопроходного документного процесса | Синтетическая схема |
| `fig-multi-pass-document-workflow-source-state-flow` | это досье + Intermediate Artifacts | Source state: found → opened → read → used_in_main_text / candidate_image_only / rejected | Показать, что источники имеют состояние, а не только URL | Синтетическая схема |
| `fig-aegis-permission-gate` | AEGIS | Tool call → risk scan → policy validation → allow / block / human approval → audit trail | Показать permission gate before side effect | Лучше перерисовать по paper abstract / figures; права проверить |
| `fig-skillnb-gated-workflow` | SKILL.nb | Notebook step with natural guidance, executable cell, validation gate, fallback path, screenshot/error trace | Показать gate-conditioned workflow и drift fallback | Кандидат на синтетическую схему; source figures rights check |
| `fig-codecrdt-observation-driven-coordination` | CodeCRDT | Shared CRDT TODO skeleton, agents claim TODOs, observe updates, write code after claim | Показать отличие shared-state coordination from message-only coordination | Синтетическая схема на основе paper |
| `fig-codecrdt-speedup-tradeoff` | CodeCRDT | Диапазон результата: 21.1% speedup → 39.4% slowdown, плюс 5–10% semantic conflicts | Показать пределы “просто запустить больше агентов” | Синтетический mini-chart / table |
| `fig-storm-write-time-validation` | STORM | Agent read snapshot → stale dependency → rejected write → current content + diff + stale dependency list | Показать write-time conflict mediation | Синтетическая схема; можно свериться с repo/docs |
| `fig-mast-failure-distribution` | MAST paper | Failure taxonomy / distribution figure | Показать, что сбои multi-agent systems системные, а не только model-level | Кандидат на screenshot/перерисовку; права проверить |
| `fig-parallel-loop-read-snapshot` | это досье + STORM/CodeCRDT | Two source workers with read snapshots, one merge/synthesis pass, canonical write lock | Проектная схема для параллельного выполнения многопроходного документного процесса | Синтетическая схема |

| `fig-anthropic-multi-agent-research-process` | Anthropic multi-agent research system | LeadResearcher → Subagents → Memory → CitationAgent → final sourced report | Показать production-grade pattern для параллельного source discovery и отдельного citation pass | В источнике есть официальная диаграмма; права/условия использования проверить, безопаснее перерисовать |
| `fig-safe-parallel-source-protocol` | это досье + Anthropic/STORM/CodeCRDT | Coordinator → source shards → source claims → worker returns → citation audit → synthesis pass → canonical write | Главная схема проекта протокола безопасной параллельной работы с источниками | Синтетическая схема |
| `fig-source-claim-lifecycle` | это досье | `candidate → claimed → opened → extracted → audited → used / rejected / image_candidate_only` | Показать, что у источника есть состояние и владелец, а не только URL | Синтетическая схема |
| `fig-worktree-isolated-source-workers` | Claude Code Worktrees + Codex Worktrees + Git worktree docs | Несколько workers в отдельных worktrees/read snapshots; canonical write только через owner | Развести filesystem isolation и смысловой merge | Синтетическая схема на основе official docs |
| `fig-citation-audit-gate` | Anthropic multi-agent research system + правила provenance | Claim → source link → exact fact → citation/source audit → allow transfer | Показать gate между source opening и переносом в основной текст | Синтетическая схема |
| `fig-synthesis-pass-conflict-matrix` | это досье + STORM/CodeCRDT | Таблица конфликтов: duplicate source, stale snapshot, semantic conflict, missing image candidate, style drift | Показать, что synthesis pass проверяет больше, чем merge текста | Синтетическая схема |

## Открытые вопросы

- Достаточно ли многопроходному документному процессу JSON/status files plus disciplined TypeScript tooling, или нужен SQLite/Dolt-like structured store?
- Где точная граница перехода от JSON/Markdown к SQLite: число workers, query complexity, конфликтующие writes или human dashboard?
- Какие gates должны быть human-visible, а какие internal automation-only?
- Какой минимальный read snapshot нужен pass worker: target doc, source register, discourse, skeleton, previous pass folder?
- Нужен ли STORM-like write-time validation для markdown/dossier work, или достаточно lock per target file plus merge pass?
- Можно ли безопасно параллелить source discovery/opening без параллельной записи в каноническое досье? Текущий проект протокола отвечает: да, если workers возвращают пакеты свидетельств, а каноническую запись делает отдельный владелец или synthesis pass.
- Нужна ли многопроходному документному процессу поддержка branching/merge of work items, или single-user sequential work достаточно для POC?
- Как совместить cheap prime с source integrity, чтобы модель не теряла факты из источников?
- Где граница между Persistent Work Graph и чрезмерным project-management substrate?
- Нужен ли отдельный execution graph, или TypeScript-оркестрация + pass-артефакты пока достаточно?
- Как хранить source state: found/opened/read/used/rejected/image-candidate, чтобы будущий pass не повторял поиск?
- Как не допустить, чтобы агент изменял граф работы для оправдания уже сделанного результата?
- Как не спутать CRDT/file-level convergence и semantic correctness?

## Следующий возможный проход

`should_stop = no` для всего Persistent Work Graph-досье, но направление safe parallel source-work protocol закрыто достаточно для теории и технического атласа. Следующий полезный узкий проход — только implementation sketch: перевести `job/pass/gate/prime/recovery`, `source_claim`, `worker_return`, `citation_audit` и `synthesis_pass` в минимальную JSON/file layout, пригодную для TypeScript-оркестрации схему без начала кодирования.

Перед написанием теории отдельный новый search pass уже не обязателен: для теоретического слоя достаточно текущего материала, если не писать раздел технического атласа.
