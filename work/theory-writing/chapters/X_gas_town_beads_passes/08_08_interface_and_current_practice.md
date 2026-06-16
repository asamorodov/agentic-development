# 08 — Техническая фактура и текущая практика: внешняя форма механизма

## Задача прохода

Этот проход описывает не философию главы, а внешнюю форму механизма: кто участвует, какие объекты входят в систему, какие операции меняют состояние, какие сигналы только читают состояние, где работа считается готовой, где она блокируется, где система должна вернуть управление человеку. Материал нужен, чтобы будущая глава не свелась к абстрактному слову «оркестрация».

## 1. Участники и роли

### Человек / maintainer / overseer

Человек остаётся источником суждения и final authority. Но его роль меняется. Он не должен читать каждый терминал и babysit каждую агентскую сессию. Его интерфейс — это:

- видимость очередей, problem feed и work state;
- решения, которые система не должна принимать сама;
- human gates;
- escalation beads / routed escalations;
- review/acceptance на выходе.

В хорошем тексте главы важно подчеркнуть: человек не исчезает, но перестаёт быть ручным диспетчером всех таймеров, вкладок, CI-ожиданий и потерянных промежуточных выводов.

### Mayor

Mayor — не просто «главный агент». Это поверхность управления городом:

- принимает или оформляет work;
- dispatches через `gt sling`;
- видит problem feed;
- принимает escalations;
- связывает town-level и rig-level состояние;
- может решать, reroute/re-sling/hold/defer/escalate.

В главе Mayor лучше описывать как interface role между человеком и множеством рабочих потоков.

### Rig

Rig — рабочая площадка вокруг конкретного проекта, репозитория или области. Rig должен иметь:

- локальное рабочее состояние;
- rig-level beads;
- worktrees/branches;
- исполнителей;
- путь к merge/review;
- локальные проверки и ограничения.

Rig важен для примера со связанными работами: backend rig, frontend rig, docs rig, test rig.

### Polecat / Crew

Polecat — расходуемый исполнитель дискретной задачи. Важно не путать polecat с долговечной ответственностью: сессия может умереть, но работа должна остаться на hook/bead/rig.

Crew — более долговечный или контекстно богатый исполнитель. В главе можно упомянуть различие, но не нужно разворачивать его подробно, если основной пример держится на polecats.

### Witness / Refinery / Deacon / Dogs

Это сервисные роли, через которые можно объяснить обслуживание потока:

- Witness наблюдает lifecycle и сообщает о состояниях;
- Refinery проводит работу через merge-ready / merged / merge-failed;
- Deacon смотрит на здоровье среды, recovery и escalation;
- Dogs выполняют инфраструктурные сервисные задачи.

Главная мысль: в многопоточной агентской работе появляются роли, которые не делают основную фичу, но делают возможным сам поток фич.

### Scheduler

Scheduler — роль/механизм capacity. Он не нужен для красивой архитектуры, но нужен для реального масштаба:

- deferred dispatch;
- capacity / `scheduler.max_polecats`;
- batch size;
- spawn delay;
- convoy integration;
- safety around dispatch.

В главе этот слой должен защищать от наивной идеи, что задача масштабирования решается запуском ещё большего числа агентов.

## 2. Входы механизма

### Work item / bead / issue

Первичный вход — не сообщение в чате, а work item. В Beads/Gas Town это может быть bead/issue/molecule step:

- title / body;
- labels;
- dependencies;
- gates;
- status;
- owner/pin/hook;
- comments/history;
- links to branch/PR/checks;
- routing metadata.

В будущем тексте полезно показать переход: человек может начать с обычного намерения, но чтобы работа стала управляемой, она должна получить форму в durable state.

### Convoy / cross-rig work

Когда работа затрагивает несколько rig, входом становится не один issue, а convoy/cross-rig coordination. Для главы это важно в примере с backend/frontend/docs/tests:

- общая цель одна;
- локальные задачи разные;
- зависимости пересекаются;
- финальный review зависит от нескольких веток;
- часть событий должна быть видна на town-level.

### Formula / molecule

Если работа повторяемая, входом может быть formula, из которой создаётся molecule:

- formula задаёт шаблон;
- molecule создаёт persistent instance;
- steps становятся issues;
- dependencies управляют ready queue;
- hooks/pinning назначают исполнителей.

Это полезно для связи с process profiles: процесс не только написан в документе, но может стать исполняемым рабочим графом.

### Wisp

Wisp можно оставить как лёгкий вспомогательный вход: черновая или эпизодическая запись, которая не обязана сразу становиться большим durable item. В главе не стоит делать из wisps отдельную тему.

### Внешние сигналы

Входами также становятся:

- CI results;
- GitHub PR checks;
- review comments;
- merge failure;
- timeout/staleness;
- Codex/Claude session lifecycle events;
- user prompt / SessionStart / PreCompact / PostCompact hooks;
- human decision.

Это важно: агентская среда читает не только сообщения агентов, но и сигналы из инженерной инфраструктуры.

## 3. Выходы механизма

### Изменённое durable state

Главный выход — не текстовый отчёт. Главный выход — обновлённое состояние:

- work item получил новый статус;
- dependency закрыта или появилась новая;
- gate resolved/unresolved;
- новая работа создана;
- result/comment вернулся из локальной сессии в Beads/PWG;
- branch/PR/check связаны с work item;
- merge failed записан как состояние, а не потерян в терминале.

### Dispatch / re-dispatch / defer

Система может:

- отправить work в rig;
- `sling` work на polecat;
- оставить work в deferred queue;
- перераспределить orphaned/stalled work;
- не запускать новую сессию из-за capacity.

### Structured signal to human

Выходом может быть не сделанная работа, а структурированный сигнал:

- escalation bead;
- severity route;
- problem feed item;
- human gate awaiting decision;
- stale escalation;
- summary of attempted automatic recovery.

Такой сигнал отличается от обычной просьбы агента в чате: он привязан к work item, имеет историю, маршрут, статус и последствия для очереди.

### Merge / review path

Для работ, которые меняют код, выходом может быть:

- merge-ready;
- merged;
- merge-failed;
- fix-needed;
- awaiting-verdict;
- PR ready to review;
- checks green but human gate unresolved.

Эти состояния нужно использовать, чтобы показать границу с главой XI: X ведёт работу до review/merge path, но вопрос достаточности результата выходит дальше.

## 4. Состояния и переходы

### Состояния work item

Минимальный набор состояний для будущей главы:

- created / open;
- ready;
- blocked by dependency;
- blocked by gate;
- pinned / assigned;
- hooked / active;
- deferred;
- stalled;
- orphaned;
- merge-ready;
- merged;
- merge-failed;
- fix-needed;
- escalated;
- closed.

Не нужно утверждать, что все эти статусы буквально являются одной enum в Gas Town/Beads. Для текста главы это рабочие типы состояния, подтверждённые разными источниками.

### Переходы

Нужно описать переходы как операции, а не как «агент что-то сделал»:

1. Human intent → work item/bead.
2. Work item → routed target / rig.
3. Ready work → pinned/hooked executor.
4. Hooked work → active session/worktree.
5. Active work → partial result / comment / branch / PR / check.
6. Partial result → durable state update.
7. Ready for merge → Refinery attempt.
8. Merge failed → status + fix-needed / re-dispatch / escalation.
9. Gate unresolved → not ready.
10. Stalled/orphaned → recovery or re-sling.
11. Automatic recovery fails → escalation.
12. Human decision → updated work state / unblock / reroute.

Эта цепочка может стать основой одной центральной схемы главы.

## 5. Различие чтения и действия

В главе важно не смешать наблюдение и изменение состояния.

### Чтение

Читающие операции:

- посмотреть problem feed;
- открыть work item;
- получить `bd prime` / `gt prime` контекст;
- посмотреть dependencies/gates/status;
- прочитать PR checks;
- посмотреть agent session / logs / trace;
- inspect merge failure;
- list ready work.

Чтение создаёт видимость, но само по себе не обслуживает поток. Если среда только показывает dashboard, человек остаётся диспетчером.

### Действие

Изменяющие операции:

- создать bead/issue;
- добавить dependency;
- создать/разрешить gate;
- pin/hook work;
- sling work в rig;
- defer dispatch;
- создать escalation;
- acknowledge/close/re-escalate escalation;
- update status/comment;
- create branch/PR;
- merge/retry/fix-needed;
- reassign/recover orphaned work;
- close work item.

Для главы полезно подчеркнуть: реальная среда начинается там, где видимость соединена с допустимым действием. Dashboard без действий — это наблюдение хаоса; action без durable state — это хаотичное вмешательство.

## 6. Текущая практика Gas Town/Beads как рабочий прототип

На момент внешней проверки источников Gas Town/Beads выглядят не как зрелый массовый стандарт, а как живой, быстро меняющийся набор практик:

- README и docs говорят о множестве поддерживаемых agent surfaces, но механика остаётся frontier/hands-on;
- Beads documentation обновлена 13–14 июня 2026 и уже фиксирует Dolt-backed source of truth;
- Codex integration docs говорят о конкретных lifecycle hooks, включая SessionStart, PreCompact, PostCompact, UserPromptSubmit;
- Gas Town design docs включают scheduler/backpressure, escalation, polecat lifecycle patrol;
- публичная авторская статья одновременно объясняет роли и предупреждает о дороговизне/сырости подхода;
- часть деталей в docs/repo может быть ближе к текущей реализации, чем статья;
- старые формулировки про JSON-backed state не нужно переносить как актуальные без проверки.

В главе это следует подать честно: не «все будут использовать Gas Town», а «Gas Town/Beads уже показывают внешний контур класса механизмов, который понадобится, если агентская разработка действительно станет многопоточной».

## 7. Практическая форма интерфейса в сквозном примере

Для примера с webhook change интерфейс можно разложить так.

### Вход

- Человек создаёт цель: изменить payment webhook handling.
- Цель раскладывается на work items `B-101`…`B-106`.
- У items появляются dependencies and gates.
- Часть work is routed to backend/frontend/docs/tests rigs.
- Backend and docs work are pinned/hooked to agents.

### Исполнение

- Backend polecat работает в branch/worktree.
- Docs-agent обновляет API docs.
- Test-agent готовит regression checks.
- `bd prime` / `gt prime` дают новым сессиям актуальную картину.
- Scheduler удерживает лишние jobs, если capacity exceeded.

### Сбои

- Backend claim stalls → Witness/Deacon detects lifecycle problem.
- Docs-agent produces useful replayed payload insight but does not return it to durable state → сервисная роль или human review добавляет linked work/update.
- Test work claims green before CI gate resolved → gate keeps it out of ready.
- Merge attempt fails → Refinery writes merge-failed/fix-needed state.
- Architectural decision cannot be automated → escalation to Mayor/human.

### Выход

- Work items updated.
- New dependency for replayed payload tests created.
- Gate remains blocking until CI/human approval.
- Merge failure becomes fix-needed work, not lost terminal output.
- Human decision updates backend contract and unblocks downstream work.
- Final review receives structured state, not scattered chat logs.

## 8. Где механизм заканчивается

Глава X не должна делать вид, что обслуживаемый поток равен правильному результату. Механизм заканчивается там, где работа:

- возвращена в durable state;
- не потеряла dependencies/gates/history;
- дошла до review/merge path;
- передала человеку структурированные решения;
- сохранила failures and recoveries.

Дальше начинается вопрос главы XI: какие проверки, артефакты и evidence делают результат достаточным. Например, `B-105` может пройти CI gate, но это ещё не доказывает, что тесты покрывают все важные replayed payload cases. Это уже не обслуживание потока, а качество проверочного материала.

## 9. Формулировка для будущего черновика

Внешняя форма такого механизма выглядит как соединение трёх слоёв. Первый слой — durable work state: beads/issues/molecules, dependencies, gates, status, comments, `bd prime`, pin/hook. Второй слой — рабочая география: rigs, worktrees, branches, PRs, checks, convoys. Третий слой — обслуживание потока: Mayor, Witness, Refinery, Deacon, Dogs, scheduler, escalation. Только вместе они создают среду, в которой много агентских действий перестают быть набором чатов и становятся потоком, с которым проект может работать.
