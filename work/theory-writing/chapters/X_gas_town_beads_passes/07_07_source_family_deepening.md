# 07 — Добор фактуры по главным source families

## Назначение прохода

Этот проход собирает не новую рамку главы, а сырьё, которое легко потерять при слишком быстром синтезе: команды, статусы, артефакты, ограничения, переходы между фазами и практические детали. Материал ниже не является готовым текстом главы. Его задача — дать будущему черновику плотность и не оставить главу на уровне общих слов про «оркестрацию».

## 1. Gas Town / Beads: фактура для основного механизма главы

### 1.1. Общая рамка Gas Town

По README Gas Town полезно брать не маркетинговую фразу про «20–30 агентов», а более конкретный набор функций:

- multi-agent orchestration / workspace manager для Claude Code, GitHub Copilot, Codex, Gemini и других CLI/IDE agents;
- persistent work tracking;
- context persisted via git-backed hooks;
- mailboxes and handoffs вместо ручной координации;
- Beads ledger как место хранения work state;
- переход от хаотичных 4–10 агентов к 20–30 при наличии инфраструктуры.

В главе это нужно перевести так: проблема не в количестве агентских процессов, а в том, что у каждого процесса появляется адрес, состояние, канал связи, след и способ возврата результата.

### 1.2. Роли как сервисные функции, а не персонажи

Из Gas Town docs/repo нужно перенести роли не как список имён, а как распределение функций:

- **Mayor** — поверхность управления и принятия решений, dispatch, видимость problems/queues, связь с человеком.
- **Rig** — рабочая площадка вокруг проекта/repo, где живут локальные задачи, worktrees, agents и rig-level beads.
- **Polecat** — расходуемый исполнитель дискретной работы; важно: agent role не равен session, сессия может быть пересоздана.
- **Crew** — более долговечная исследовательская/контекстная работа; не сводить всех исполнителей к polecats.
- **Witness** — наблюдение за lifecycle и состояниями вроде stuck/orphan/merge-ready.
- **Refinery** — путь результата к merge, обработка merge-ready / merged / failed.
- **Deacon** — здоровье инфраструктуры, patrol, recovery, escalation.
- **Dogs** — сервисные помощники/инфраструктурные задачи.
- **Scheduler** — capacity/backpressure/deferred dispatch.
- **Convoy** — работа, которая должна идти через несколько rig или иметь cross-rig видимость.

В главе не надо объяснять каждую роль энциклопедически. Их стоит выводить из сбоя: claim завис → нужен Witness/Deacon; merge failed → нужен Refinery; много задач → нужен Scheduler; cross-rig работа → нужен convoy; человеку нужен не терминал каждого агента, а Mayor surface.

### 1.3. Два уровня Beads: town-level и rig-level

Из `architecture.md` важно перенести двухуровневость:

- **town-level beads**: Mayor mail/messages, convoy coordination, strategic issues/decisions, town-level agent beads, role-definition beads;
- **rig-level beads**: bugs/features/tasks, merge requests/code reviews, project molecules, rig-level agent beads.

Это помогает объяснить, почему Gas Town не дублирует PWG. PWG даёт долговечный объект работы; town-level слой организует связи между многими такими объектами и рабочими площадками. В главе можно использовать простую формулу: rig-level хранит локальную работу проекта, town-level хранит организацию потока между работами, ролями и решениями.

### 1.4. Команды и артефакты, которые стоит не потерять

Не обязательно все команды попадут в основной текст, но полезно держать список:

- `gt sling <bead-id> <rig>` — dispatch: spawned polecat / hook work / start session; хороший пример того, что поручение не остаётся сообщением в чате.
- `gt feed --problems` — проблемная поверхность для Mayor/человека; полезна для тезиса о защите человеческого внимания.
- `gt mail` — канал, через который сообщения переживают сбои процесса и сохраняют след; не делать главным механизмом, но оставить как инфраструктурный канал.
- `gt escalate -s <MEDIUM|HIGH|CRITICAL> ...` — structured escalation; проблема становится bead/comment/route, а не просьбой в чат.
- `gt escalate stale` — re-escalation stale/unacked escalations; хороший пример того, что даже сигнал человеку имеет lifecycle.
- `gt prime` — подача контекста роли/среды при старте; рядом с `bd prime`, но не смешивать.
- `bd prime` — AI-optimized Beads context; особенно важно для нового входа модели после compaction/session restart.
- `bd gate create` — блокировка work item до human/timer/GitHub condition; blocked issue не появляется в `bd ready`.
- `bd pin` / `bd hook` — назначение и явная привязка работы.
- `bd ready` — список работы, которую можно брать дальше; полезно для объяснения gates/dependencies.
- `bd pour` — создание molecule/formula instance; возможно упомянуть в разделе о повторяемых процессах.
- `bd wisp` — лёгкая ephemeral форма; использовать осторожно, без углубления.

### 1.5. Lifecycle и статусы

Самый ценный слой фактуры — не команды, а события:

- `POLECAT_DONE`;
- `MERGE_READY`;
- `MERGED`;
- `MERGE_FAILED`;
- `FIX_NEEDED`;
- `awaiting_verdict`;
- `RECOVERED_BEAD`;
- `GUPP_VIOLATION`;
- `ORPHANED_WORK`;
- Stalled / Zombie / Working / Idle как problem/status categories в feed.

Эти статусы стоит использовать как материал для описания сбоя. Они показывают, что среда не просто подписывает задачу «в работе», а превращает статусы в операционные реакции: вернуть, слить, чинить, будить, перераспределить, эскалировать.

### 1.6. GUPP и hook

GUPP важен не как забавный термин, а как пример рабочего контракта: если работа находится на hook, агент не должен ждать нового разрешения, он должен выполнять. В главе это можно использовать для различения:

- в обычном чате «агент ничего не делает» — это неопределённая ситуация;
- в системе с hook/GUPP это нарушение контракта или повод для lifecycle reaction.

Hook тоже нужно держать техническим: это не метафора «зацепки», а механизм привязки work item к исполнителю/площадке.

### 1.7. Scheduler / backpressure

Из scheduler docs стоит взять:

- `scheduler.max_polecats`;
- deferred dispatch;
- batch size;
- spawn delay;
- convoy integration;
- capacity/backpressure;
- safety properties: idempotency, pristine work bead, cross-rig guard, dispatch serialization, atomic scheduling, formula pre-cooking, fresh state on save.

Для главы достаточно показать: город не только запускает work, но и отказывается запускать её немедленно, если это разрушит управление. Это особенно важно против наивного тезиса «больше агентов = быстрее».

### 1.8. Escalation как признание предела автоматического обслуживания

Из escalation docs стоит перенести:

- escalation создаётся, когда automated resolution is not possible;
- маршрутизация по severity: medium/high/critical;
- route может включать bead, mail, email, SMS, Slack, log;
- поток: Agent → Deacon → Mayor → Overseer;
- chain tracked via bead comments;
- stale detection и max re-escalations;
- категории: decision, help, blocked, failed, emergency, gate_timeout, lifecycle;
- не нужно эскалировать normal workflow, recoverable errors, information queries.

Главная мысль: человеческая точка входа становится структурированной. Человек получает не весь шум работы, а случаи, где среда исчерпала автоматическое восстановление или упёрлась в решение.

### 1.9. Beads как durable control/work state

Из Beads docs нужно удержать современную фактуру:

- Dolt is the sole storage backend / source of truth;
- version-controlled SQL;
- branches/merge/diff/push/pull через Dolt-логику;
- server mode для multi-writer;
- recovery path and sync path;
- multi-clone race и ограничения local-first sync;
- limitations: large teams 10+, real-time collaboration, cross-repo limitations.

Это полезно для честности: Beads мощнее простого issue tracker, но имеет реальные ограничения и инженерную цену.

### 1.10. Beads coordination, routing, gates

Из multi-agent docs:

- `bd pin` закрепляет work за agent/person;
- `bd hook` связывает работу с активным исполнением;
- sequential handoff: один agent закрывает/передаёт, другой подхватывает;
- fan-out/fan-in: большая работа делится на части, затем merge/review зависит от нескольких веток;
- cross-repo dependencies and hydration;
- routing через patterns: title/labels/path prefix;
- auto-routing может направлять issue в target repo;
- gates: human, timer, GitHub run, GitHub PR;
- blocked issue не должен попадать в ready queue.

Эта группа нужна для объяснения нижнего уровня в примере: work items вокруг webhook change не просто написаны списком, а имеют dependencies, gates, hooks, routing.

### 1.11. Beads workflows: formulas, molecules, wisps

Для главы X особенно полезны molecules:

- formula/TOML задаёт шаблон повторяемой работы;
- molecule создаёт persistent instance of formula;
- steps map to issues;
- dependencies управляют `bd ready`;
- molecule state syncs through `.beads`;
- lifecycle включает создание, выполнение шагов, закрытие, возможно повторное использование;
- hooks/pinning связывают шаги с исполнителями.

Wisp лучше оставить как вторичную деталь: лёгкая ephemeral форма (`.beads-wisp`) для черновых/малых шагов. Не разворачивать, чтобы не перегрузить главу.

### 1.12. Beads/Codex integration

Из Codex integration:

- SessionStart injects full `bd prime`;
- PreCompact checks `bd prime --memories-only` and warns;
- PostCompact marks need for refresh;
- UserPromptSubmit injects full `bd prime`;
- PreCompact alone is not enough because of Codex stdout behavior.

Это хорошая связка с главой VI: hooks не просто «расширяют модель», а возвращают durable work context в новую или сжатую сессию. В главе X этот материал должен служить тезису о потоке: следующая сессия получает не память из воздуха, а текущую картину работы.

## 2. PWG / Beads / Gas Town: что именно добавляет X сверх VII

Из B3 и PWG-досье нужно перенести различение:

- PWG удерживает work item: цель, зависимости, владельца, условия остановки, ход, проверочный материал, handoff/resume.
- Gas Town удерживает среду вокруг множества work items: dispatch, rigs, service roles, feed, recovery, queue, merge, health.

Хорошая таблица для будущей главы может идти не по «свойствам инструментов», а по вопросам:

| Вопрос | PWG / Beads | Gas Town |
|---|---|---|
| Где живёт работа? | bead/issue/molecule, dependencies, gates | town/rig context вокруг множества beads |
| Кто её взял? | pin/hook/claim | polecat/crew/role identity, Mayor visibility |
| Что её блокирует? | dependency/gate/status | scheduler, convoy state, problem feed |
| Что случилось при сбое? | comment/status/history | Witness/Refinery/Deacon/Dogs превращают сбой в действие |
| Где человек вмешивается? | human gate/comment/review | escalation route / Mayor surface / structured problem |

Этот материал поможет не повторять главу VII: глава X не доказывает, что work state нужен; она показывает, как work state начинает требовать городского обслуживания.

## 3. Jökull Sólberg: маленький родственник Gas Town-проблемы

История Jökull нужна как компактная форма той же боли, но вокруг PR.

Фактура, которую можно перенести:

- `/babysit-pr` — Claude Code skill около 170 строк;
- процедура определяет current PR через `gh pr view`;
- ждёт CI через `gh pr checks --watch`;
- обрабатывает Greptile comments;
- запускает `codex review --base main`;
- классифицирует замечания как Fix / Dismiss / Escalate;
- имеет выход: CI green, no unresolved issues, PR ready to merge;
- имеет лимит: максимум три итерации;
- пример: два прохода, CI green, затем Greptile и Codex нашли два реальных пункта, после исправлений auto-merge поставлен в очередь; весь путь занял около десяти минут, большую часть занял CI.

Для главы X это важно не как «PR automation», а как малая версия обслуживания потока после генерации кода. После `push` работа не закончилась: CI, review comments, локальная проверка, повторные правки и критерий готовности должны быть проведены до merge-ready. Человек иначе становится живым таймером и диспетчером.

Граница: Jökull хорошо поддерживает идею servicing loop, но не даёт полноценного city-level слоя. Не надо приравнивать `/babysit-pr` к Gas Town.

## 4. Stripe Minions: platform-level routing и среда перед агентом

История Stripe нужна как корпоративная параллель: agentic work становится возможной благодаря уже существующей платформе разработки.

Фактура:

- публичная рамка легко сводится к «1300+ / 3000 PRs», но это не главный факт;
- внешне запуск может выглядеть как Slack message → emoji reaction → PR;
- внутри есть route signal в emoji suffix, например `:create-minion-payserver:`;
- система поднимает isolated cloud dev environment / devbox;
- checkout новой git branch;
- setup database/tools/VS Code server;
- agent ищет по кодовой базе, правит, запускает tests, commits, возвращает PR;
- вокруг one-shot есть devbox, warmed repo, scope rules, Toolshed/MCP, blueprint, analyzer, coding loop, linters, tests, type checks, LLM judge, diagnostic feedback, CI, PR template, human review.

Для главы X Stripe поддерживает тезис: чем автономнее агент, тем больше обычной инженерной инфраструктуры вокруг него. Здесь нет Gas Town-ролей, но есть тот же переход: вход из коммуникационного места получает routing, workspace, checks и возвращается как reviewable artifact.

Граница: Stripe ближе к enterprise platform and runtime substrate. Использовать как supporting parallel, не как центр главы.

## 5. Shopify Roast: executable workflow и named outputs

Roast нужен, чтобы показать соседний, но отличающийся слой: не город вокруг многих agents, а workflow as code for AI steps.

Фактура:

- текущая форма — Ruby DSL: `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call`;
- ранняя форма была YAML workflow с steps, command steps, inline prompts, agent prompts, `each`, `repeat`, `case/when/else`, `json`, `params`, `coerce_to`, `exit_on_error: false`;
- README miniature: `cmd(:recent_changes)` → `agent(:review)` → `chat(:summary)`;
- tutorial security review: `agent(:review_security)` через Claude, `chat(:prioritize)` и `chat(:summarize_for_executive)` через OpenAI, `ruby(:display_report)`;
- named outputs: `cmd!(:recent_changes).lines`, `agent!(:review).response`, `agent!(:review_security).text`, `chat(...).session`, iteration outputs;
- session resumption/forking: можно продолжить session или ответвиться от более раннего состояния;
- `map`/`collect`/`reduce`, `parallel(3)` / `parallel!` with ordered outputs;
- formatter stack and block events: prompts, responses, stats, session ids, action boundaries должны быть видимы, иначе workflow трудно проверить.

Для главы X Roast полезен как контраст: он показывает, как процедура превращается в исполняемый объект, где выводы становятся именованными outputs. Но Gas Town/Beads добавляют другой уровень — обслуживание множества work items, roles, queues, recovery и escalation.

Граница: не писать в X полноценное объяснение Roast. Достаточно одного абзаца о том, что executable workflow решает одну часть проблемы, но городская среда нужна, когда таких workflow/agents/work items много и они начинают конфликтовать, зависать и требовать service roles.

## 6. Mae Capozzi: worktrees, traces, timeout и платформа сопровождения

История Mae нужна как близкая параллель к visible state/observability.

Из уже собранных материалов для X пригодны следующие элементы:

- worktrees/branches как форма параллельной работы, которую нужно делать управляемой;
- traces / `TRACEPARENT` как способ видеть путь выполнения, а не только финальный ответ;
- timeout как явная граница ожидания;
- CI/observability/dependencies как ограничения скорости агентского PR-потока;
- платформа нужна не только для генерации кода, но и для того, чтобы много агентских действий не превратились в неразборчивый поток артефактов.

Связь с X: Gas Town uses roles/status/patrol, Mae показывает более традиционный engineering-platform язык для сходной боли: если работа распределена по веткам, проверкам, traces и timeouts, нужно видеть жизненный цикл, а не доверять отчёту агента.

## 7. Внутренние активы/иллюстрации

Найденные локальные активы, которые могут помочь главе:

- `content/assets/theory-images/gastown-architecture.svg` — вероятно использовать для архитектуры Gas Town, если тексту нужна карта ролей.
- `content/assets/theory-images/gastown-basic-workflow.svg` — возможно лучше для основной главы, если он показывает путь работы, а не статичную архитектуру.
- `content/assets/theory-images/gastown-mayor-hub.webp` — полезно для человеческой поверхности Mayor, но проверить, не слишком ли UI-specific.
- `content/assets/theory-images/beads-task-graph-memory.svg` — полезно для Beads/PWG слоя, но есть риск дублировать главу VII.
- `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg` — возможно лучший синтетический рисунок для X: давление масштаба → механизмы.
- `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg` — полезно для town-level / rig-level distinction.
- `content/assets/atlas-images/gas-town/gastown-worker-roles.svg` — использовать только если глава всё же перечисляет роли.
- `content/assets/story-images/11-mae-honeycomb-trace.png` и `content/assets/theory-images/mae-honeycomb-trace-observability.png` — supporting visual для traces/observability, но не главный кандидат.

Предварительное решение: в главу лучше всего подходят две иллюстрации: `gastown-pressure-to-mechanism-stack.svg` и `gastown-two-tier-beads-flow.svg`. Остальные — кандидаты на вспомогательные места или на отказ, чтобы не перегрузить главу картинками.

## 8. Фактура, которую не стоит переносить полностью

1. Полный список команд Gas Town/Beads. В главе нужны несколько точных команд как доказательство механизма, не справочник.
2. Подробности Dolt-администрирования. Достаточно сказать, что Beads current docs используют Dolt-backed source of truth и имеют multi-writer/server/recovery concerns.
3. Все роли Gas Town. Их надо показывать через сбои, иначе текст станет глоссарием.
4. Все PR-детали Shopify Roast. Для X нужен workflow/named outputs/observability, а не история провайдеров и formatter PR stack во всей полноте.
5. PR/CI детали Jökull beyond babysit loop. Ценность — в цикле ожидание → проверка → Fix/Dismiss/Escalate → ограничение итераций → merge-ready.
6. Цифры Stripe как самостоятельный аргумент. Без инфраструктурной трассы они превращают историю в рекламный пример.

## 9. Сжатая карта переноса в будущий черновик

- **Открытие главы:** несколько агентов работают, но проект не понимает, где реальный progress.
- **Beads/PWG слой:** work items, dependencies, gates, `bd prime`, pin/hook, routing, molecules.
- **Gas Town слой:** Mayor, rigs, polecats/crew, convoys, Witness/Refinery/Deacon/Dogs, scheduler, escalation.
- **Сбой:** `GUPP_VIOLATION`, `ORPHANED_WORK`, `MERGE_FAILED`, gate not resolved, stale escalation.
- **Человек:** Mayor surface / escalation route; человек вмешивается по структурированному сигналу.
- **Параллели:** Jökull — маленький PR-servicing loop; Stripe — platform routing/devbox/checks; Roast — executable workflow/named outputs; Mae — traces/worktrees/timeouts.
- **Граница с XI:** всё это возвращает работу в управляемый поток, но не доказывает достаточность результата.
