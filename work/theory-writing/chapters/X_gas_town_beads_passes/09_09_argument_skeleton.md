# 09 — Скелет аргумента главы

## Проверка общего замысла

Глава должна быть не каталогом Gas Town/Beads и не обзором multi-agent tools. Её аргумент строится вокруг одного практического сбоя: когда агентских рабочих потоков становится много, проект теряет управляемость, даже если каждый отдельный агент делает что-то разумное.

Отсюда центральное различение: **иметь состояние отдельной работы** и **обслуживать поток многих работ** — разные уровни. Beads/PWG дают первый уровень. Gas Town-like среда показывает второй уровень: маршруты, площадки, сервисные роли, наблюдение, recovery, backpressure, escalation и возврат результата в общее состояние.

## Предлагаемая последовательность главы

### 1. Начать не с Gas Town, а с узнаваемого сбоя

Открытие главы должно быть практическим. Не «Gas Town — это…», а ситуация:

- команда уже умеет запускать агентов;
- у неё есть worktrees/branches/PR/checks;
- задачи можно разложить на несколько частей;
- у части работ уже есть durable state;
- но при реальном параллелизме человек начинает видеть не проект, а шум.

Первый ход текста: больше агентов не создаёт автоматически больше управляемости. Оно создаёт больше мест, где работа может зависнуть, забыть вернуться в состояние, ожидать gate, сломаться на merge, запросить решение или продолжать работать по устаревшему контексту.

Здесь можно ввести сквозной пример с изменением payment webhook: backend, migration, frontend, docs, tests, final review. Важно: пример должен появиться до терминологии Gas Town, чтобы reader saw pain before mechanism.

### 2. Показать, что PWG/Beads решают только первый слой

После сбоя нужно признать: часть проблемы уже была решена предыдущими главами.

Work items становятся долговечными:

- `B-101` backend;
- `B-102` migration;
- `B-103` frontend;
- `B-104` docs;
- `B-105` tests;
- `B-106` final review.

У них есть dependencies, gates, status, comments, branch/PR/check links. Beads/PWG дают объект работы, а `bd prime` может вернуть agent session текущий контекст.

Но затем текст должен сразу показать недостаточность: durable graph сам по себе не решает, кто заметит orphaned work, кто поднимет merge failure, кто удержит очередь, кто не даст слишком многим agents стартовать одновременно, кто вернёт локальный вывод в состояние, кто поднимет решение человеку.

Ключевая формула раздела: PWG удерживает работу; глава X спрашивает, кто обслуживает движение многих работ.

### 3. Ввести центральное различение: work state vs flow service

Это первая теоретическая вершина главы. Её можно оформить как короткое различение:

- **work state** — где живёт отдельная работа: issue/bead, dependencies, gates, status, history, ownership, evidence links;
- **flow service** — что поддерживает движение множества работ: dispatch, queues, rigs, lifecycle observation, recovery, merge path, capacity, escalation, human surface.

Здесь важно не использовать «оркестрация» как самодостаточное слово. Если слово появится, нужно тут же расшифровать его механически: очередь, площадка, hook, gate, patrol, recovery, scheduler, escalation, return-to-state.

### 4. Ввести Beads как durable нижний слой

Beads должен появиться до Gas Town как основание:

- Dolt-backed source of truth;
- version-controlled work state;
- issues/dependencies/gates;
- `bd ready`;
- `bd pin` / `bd hook`;
- `bd prime`;
- routing/cross-repo dependencies;
- formulas/molecules as persistent workflow instances.

В тексте не надо делать отдельный справочник Beads. Нужно показать, что Beads делает work readable and actionable for agents. Без такого слоя Gas Town превратился бы в набор процессов и чатов.

Место источников: ссылку на Beads Architecture поставить рядом с Dolt/source-of-truth; `bd prime` — рядом с возвращением контекста в сессию; multi-agent coordination — рядом с pin/hook/handoff/fan-out; workflows/molecules — рядом с повторяемыми процессами.

### 5. Ввести Gas Town как город вокруг Beads/PWG

Gas Town следует вводить как слой поверх множества work items:

- town-level vs rig-level beads;
- Mayor as human/control surface;
- rigs as work sites;
- polecats/crew as agents with different durability;
- convoys for cross-rig work;
- Witness/Refinery/Deacon/Dogs as service roles;
- Scheduler/backpressure;
- Escalation.

Не делать глоссарий ролей. Каждая роль должна появляться по необходимости в примере:

- work dispatched → Mayor / `gt sling` / rig;
- work active → polecat / hook;
- work stalled → Witness / Deacon;
- merge path → Refinery;
- too much work → Scheduler;
- decision needed → escalation to Mayor/human.

Место источников: Gas Town README для общей рамки; Architecture docs для town/rig layers; polecat-lifecycle-patrol для statuses/recovery; scheduler docs для backpressure; escalation docs для human route; public docs/reference для команд/roles.

### 6. Развернуть сбой в сквозном примере

После введения слоёв нужно вернуться к payment webhook example и провести его через сбои.

#### 6.1. Claim завис

Backend work на hook, polecat не продвигает lifecycle. В обычной системе это висит в чате/терминале; в Gas Town-like системе становится `GUPP_VIOLATION` / stalled / orphaned signal. Witness/Deacon должны вернуть work в контур.

Тезис: зависание перестаёт быть ощущением человека и становится событием в системе.

#### 6.2. Полезный вывод остался в локальном отчёте

Docs-agent понял важность replayed payloads, но не обновил Beads/PWG. Сервисная среда должна вернуть этот вывод в work state: comment, dependency, linked issue, test update.

Тезис: главный риск не только «агент не сделал код», но и «агент сделал смысловой вывод, который не стал частью проекта».

#### 6.3. Gate удерживает premature ready

Regression checks выглядят зелёными, но CI/human gate ещё не resolved. Work item не должен попасть в ready queue. Это переход к gates, но не к полноценной evidence-главе.

Тезис: поток должен уметь не продвигать работу, если условие готовности ещё не выполнено.

#### 6.4. Merge failed

Refinery пытается merge, получает `MERGE_FAILED`, создаёт fix-needed / status / re-dispatch. Результат не исчезает и не начинается заново без памяти.

Тезис: merge failure — не конец разговора, а управляемое состояние.

#### 6.5. Capacity exceeded

Maintainer хочет запустить ещё agents, но scheduler/backpressure deferred dispatch. Часть работы ждёт, потому что необузданный параллелизм ухудшит управляемость.

Тезис: зрелая многопоточность умеет говорить «не сейчас».

#### 6.6. Decision cannot be automated

Два архитектурных/product решения вокруг webhook compatibility. Agent не должен выбирать сам. Escalation route создаёт structured human intervention.

Тезис: автоматизация не отменяет человека, а меняет форму его входа.

### 7. Обобщить механизм: обслуживаемая рабочая среда

После примера нужно сделать вторую теоретическую вершину:

В агентской разработке появляется слой, который можно назвать обслуживаемой рабочей средой. Он состоит из:

1. durable work state;
2. routing and assignment;
3. work sites;
4. lifecycle observation;
5. recovery;
6. queues/backpressure;
7. merge/review path;
8. structured escalation;
9. human control surface.

Это не один инструмент и не обязательно Gas Town буквально. Но Gas Town/Beads позволяют увидеть класс механизмов в собранном виде.

### 8. Вставить параллели из историй, но не размыть центр

После основного механизма можно дать короткий раздел-подтверждение: Gas Town не единственное место, где видна эта проблема.

- **Jökull Sólberg**: `/babysit-pr` показывает малый цикл обслуживания PR после `push`: CI wait, Greptile, `codex review --base main`, Fix/Dismiss/Escalate, max three iterations, merge-ready. Это не город, но это та же логика «человек не должен быть живым таймером».
- **Stripe Minions**: Slack emoji запускает routed devbox/branch/tools/tests/PR path. Снаружи Slack → PR, внутри platform pipeline. Это поддерживает тезис: автономный агент требует инженерной платформы вокруг.
- **Shopify Roast**: workflow as code, named outputs, session resumption/forking, `map`/`parallel`, formatter events. Это показывает превращение AI steps в исполняемую процедуру, но не заменяет city-level servicing.
- **Mae Capozzi**: worktrees/traces/timeouts/observability; видимость lifecycle and limits вместо доверия одному отчёту.

Этот раздел должен быть коротким. Его задача — подтвердить переносимость класса проблем, а не открыть четыре новых кейса.

### 9. Чётко провести границы с соседними главами

Границы можно вставлять не отдельным «мета-разделом», а как короткие предупреждения в нужных местах. Но рабочий скелет должен держать их явно.

- С VII: «мы уже знаем, зачем нужен persistent work graph; теперь спрашиваем, как обслуживать много таких графовых узлов».
- С VIII: «процесс говорит, каким маршрутом идти; flow service замечает, что маршрут реально движется или уже сломался».
- С IX: «runtime задаёт права и среду исполнения; X организует множество таких сред и результатов».
- С XI: «X возвращает работу в управляемый поток; XI проверяет, достаточно ли материал доказывает результат».
- С XII/XIII: «человек получает структурированные точки вмешательства, но финальная ответственность и поддержка результата — отдельная тема».

### 10. Закрытие главы: мост к evidence

Финал должен быть не восторженным, а переходным.

После Gas Town/Beads-like среды проект может видеть:

- что создано;
- что назначено;
- что зависло;
- что осиротело;
- что вернулось в очередь;
- что не прошло gate;
- что не смержилось;
- что требует решения человека;
- где результат вернулся в state.

Но это ещё не отвечает на вопрос: правильно ли изменение, достаточно ли tests, можно ли доверять review, не сломана ли система, пригоден ли результат к дальнейшему сопровождению. Поэтому следующая глава должна перейти к проверочному материалу/evidence.

## Возможная структура с рабочими заголовками

1. **Когда параллелизм перестаёт быть прогрессом**
   - opening failure;
   - payment webhook example begins;
   - local progress vs project progress.

2. **Почему persistent work graph уже недостаточен**
   - Beads/PWG solves durable item;
   - many items need servicing;
   - central distinction work state / flow service.

3. **Beads: рабочая память, которую может читать и менять агент**
   - Dolt-backed source of truth;
   - dependencies/gates/ready;
   - pin/hook/prime/routing/molecules.

4. **Gas Town: город вокруг рабочих объектов**
   - town/rig;
   - Mayor/rig/polecat/crew;
   - convoy;
   - service roles.

5. **Что происходит при сбое**
   - stalled/GUPP/orphaned;
   - local insight not returned;
   - gate not resolved;
   - merge failed;
   - capacity/backpressure;
   - escalation.

6. **Не только Gas Town: те же функции в других историях**
   - Jökull PR babysitting;
   - Stripe platform routing/devbox;
   - Roast executable workflow/named outputs;
   - Mae traces/worktrees/timeouts.

7. **Что даёт обслуживаемая среда и чего она не даёт**
   - gives flow visibility and recovery;
   - does not prove result quality;
   - bridge to XI.

## Проверка: почему это не каталог методов

Аргумент держится не на перечне источников, а на переходе:

1. Параллелизм создаёт новый сбой.
2. Durable state решает только часть сбоя.
3. Нужен слой обслуживания потока.
4. Gas Town/Beads дают видимый прототип этого слоя.
5. Другие истории подтверждают ту же потребность в меньших или соседних формах.
6. Этот слой возвращает работу в управляемое состояние, но не закрывает вопрос доверия к результату.

Если будущий черновик начнёт перечислять Gas Town роли подряд, нужно вернуться к этому скелету и снова вести текст через сбой и поток.
