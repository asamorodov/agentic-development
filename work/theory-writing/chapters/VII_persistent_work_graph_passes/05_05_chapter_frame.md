# P05 — собственная рамка главы VII

## Зачем нужна эта глава

Глава VII должна сделать самостоятельный шаг в общей логике книги. Предыдущие главы уже показали, что агентская разработка не сводится к одному запросу, одной сессии и одному ответу модели. Есть намерение, контракт изменения, спецификация, рабочая среда, правила доступа, интерфейсы проекта, skills, hooks, MCP, subagents and other routes of action. Но после этого остаётся отдельная проблема, которую нельзя закрыть ни хорошим prompt, ни хорошим summary, ни даже хорошим runtime.

Работа живёт дольше, чем одна агентская сессия.

Она переживает частичные реализации, неудачные проверки, ветки исследования, human review, CI, архитектурные сомнения, решения, которые ещё не приняты, найденные побочные задачи, временные claims, смену агента, потерю контекста, compaction, возврат через день и параллельные попытки. В такой ситуации нельзя честно продолжать работу из одного пересказа. Summary может быть полезным, но оно почти неизбежно превращает рабочее состояние в рассказ: «мы почти сделали», «остался edge case», «CI вроде падал», «надо проверить архитектурную границу». Рассказ похож на знание, но он не даёт строгого ответа на вопросы, от которых зависит продолжение:

- что сейчас является открытым work item;
- что действительно готово к взятию в работу;
- что заблокировано и чем именно;
- где нужно человеческое решение;
- какие проверки уже прошли, какие упали, какие ещё только ожидаются;
- кто или что уже claim-нуло узел;
- какая ветка, PR, тестовый сигнал, источник или вывод subagent является актуальным;
- что нужно показать следующей сессии, чтобы она не начинала с догадок;
- что надо убрать или пересобрать, потому что старое состояние стало ложным.

Эта глава вводит форму мышления: работа должна быть представлена не как линейная история и не как набор задач, а как постоянный граф продолжения. Он фиксирует не только «что есть», но и «что из этого можно продолжать, при каких условиях, кем, с каким основанием и после какого восстановления контекста».

## Центральная новая форма

Рабочее название формы — Persistent Work Graph, постоянный граф работы. В тексте лучше не навязывать английский как украшение. Английское имя можно оставить как устойчивое обозначение, но русская мысль должна быть простой: это граф, в котором состояние работы сохраняется за пределами текущей сессии и остаётся пригодным для продолжения.

Важное отличие от обычного issue tracker: issue tracker часто хранит карточки, статусы, assignees, подзадачи и зависимости. Это уже важная часть формы. Но для агентской разработки этого недостаточно, если карточки остаются в основном человеческим интерфейсом. Постоянный граф работы должен быть рабочей памятью для продолжения: агент или человек открывает его и понимает, какой узел можно взять, какой нельзя, что требуется для разблокировки, что уже проверено, чего мы ждём и как восстановить минимальный протокол работы.

Важное отличие от summary: summary пересказывает прошлое. Граф задаёт состояние продолжения. В summary можно написать «CI частично прошёл», но граф должен различить два сигнала: один успешный, один упавший, один ещё ожидающийся, один относящийся к старой ветке. В summary можно написать «нужен review», но граф должен представить это как gate, который блокирует ready state соответствующего узла. В summary можно написать «subagent нашёл проблему», но граф должен показать, превратился ли вывод subagent в work item, blocker, note, rejected hypothesis or source-state update.

Важное отличие от runtime checkpoint: runtime checkpoint сохраняет, где остановилось исполнение. Persistent Work Graph сохраняет, где находится работа. Runtime может восстановить конкретный процесс; PWG должен позволить другому процессу, другому агенту или человеку понять, что вообще стоит продолжать и почему.

## Центральный сбой

Главный сбой главы: локальное `done` начинает выглядеть как завершение работы, хотя фактическая работа ещё не завершена.

Это не мелкая ошибка статуса. В агентской разработке она становится системной. Модель завершила patch и пишет «done». Subagent вернул вывод и пишет «готово». CI один раз прошёл. Review comment закрыт. В сессии возникло ощущение завершения. Но если посмотреть на рабочий граф, видно другое:

- implementation node закрыт, но architecture boundary gate открыт;
- один CI run зелёный, другой красный или относится к другой ветке;
- edge case найден, но не превращён в отдельный узел;
- human decision обещан, но не записан как gate;
- claim остался висеть после оборванной сессии;
- source branch изменилась, но старый вывод subagent всё ещё выглядит актуальным;
- acceptance basis не доведена до проверки;
- cleanup не выполнен, поэтому граф начинает показывать ложное состояние.

Глава должна показать, что `done` в агентской разработке не может быть только локальным self-report модели. Завершение должно быть привязано к графу: закрыты ли blockers, разрешены ли gates, актуальны ли источники, есть ли проверочное основание для acceptance, нет ли stale claims, не осталось ли discovered work, которое делает общий результат незавершённым.

Здесь важно не уйти в главу про evidence/acceptance целиком. Глава VII не должна становиться главой XI/XII. Её вопрос уже: не «что такое доказательство качества», а «как состояние проверок, ожиданий и оснований влияет на возможность продолжать работу».

## Сквозной пример

Рабочий пример главы: billing/API изменение, которое пережило несколько ветвей.

Минимальная сцена:

Команда или агент меняет billing API. В первой сессии сделана почти готовая реализация. Во время работы найден edge case: старый клиент может отправить неполный payload; не ясно, надо ли поддерживать старое поведение или ломать compatibility. Один subagent проверил историю контрактов и сказал, что compatibility важна. Другой subagent проверил текущие tests and CI и нашёл, что часть тестов зелёная, но integration test падает на другом окружении. CI даёт два сигнала: unit tests passed; integration run failed or pending. Review architecture boundary ещё не закрыт: изменение может протечь из billing в public API layer. Human reviewer должен решить, считать ли это допустимым breaking change. Ветка существует, но за день target branch изменился. Следующая сессия должна продолжить не из фразы «почти готово», а из компактной рабочей картины:

- основной work item: billing/API change;
- подузел: compatibility edge case;
- подузел: integration failure;
- gate: human/API compatibility decision;
- gate: architecture boundary review;
- gate or signal: CI integration run;
- source state: branch X based on commit Y; target branch advanced; subagent result based on old contract doc or current code;
- claim: implementation node was claimed by previous agent; stale claim must be released or renewed;
- ready queue: what can be worked now without waiting;
- restoration packet: what the next session must know before touching code.

Этот пример хорош тем, что в нём все ключевые элементы не выглядят искусственными. Любой опытный разработчик видел «почти готовую» работу, которая на самом деле не может быть merged because one gate, one failing signal, one review decision and one stale assumption remain unresolved. Глава должна превратить это знакомое ощущение в формальный объект.

## Что именно должно попасть в рамку PWG

### Work items

Базовый узел графа — не «заметка», а work item: единица работы, которую можно показать, взять, заблокировать, связать, проверить, закрыть или оставить на будущее. Это может быть реализация, исследование, проверка, review issue, cleanup, migration risk, найденный edge case, task spawned by subagent.

Не каждый текстовый фрагмент должен становиться work item. Граф распухнет, если превращать каждую мысль в задачу. В рамке главы нужно сразу держать различие:

- work item — требует действия или решения;
- note/memory — помогает понять контекст;
- blocker — делает другой item неготовым;
- gate — ожидает внешнего события/решения;
- relation — связывает работу, но не обязательно блокирует;
- source-state mark — говорит, на каком состоянии кода/документа/ветки основан вывод.

### Dependencies and relation types

Глава должна объяснить, что «связано» и «заблокировано» — разные вещи. Обычный граф ломается, если все связи начинают трактоваться как blockers. И наоборот, граф бесполезен, если hard blocker записан как soft relation.

Полезные типы отношений:

- `blocks`: пока один узел не разрешён, другой не должен появляться как ready;
- `parent-child`: иерархия разбиения работы;
- `discovered-from`: работа возникла во время другой работы;
- `related`: связь для понимания, но не запрет на продолжение;
- `duplicates` or equivalent: одно и то же обнаружено дважды;
- `depends-on-source-state`: вывод или задача актуальны только относительно конкретного состояния источника.

Главная мысль: PWG — это не просто graph-shaped todo list. Это граф с семантикой отношений. Готовность зависит только от тех связей, которые действительно блокируют продолжение.

### Ready state

`Ready` в этой главе надо подавать как вычисляемое состояние, а не как декоративный статус. Узел готов к работе, если он открыт, не закрыт, не в чужом действующем claim, не заблокирован hard blockers, не удерживается gate, не зависит от устаревшего source state, не находится в excluded state вроде deferred/hooked unless explicitly resumed.

Эту мысль можно выразить без формулы, но сама логика должна быть строгой. Следующая сессия не должна гадать, что делать. Она должна иметь возможность открыть граф и увидеть: вот работа, которую можно брать сейчас; вот работа, которую нельзя брать, пока не придёт human decision; вот работа, которую нельзя закрывать, потому что CI signal contradicts local completion.

### Claims

Claim — это не просто assignee. В агентской среде claim отвечает на вопрос: кто сейчас удерживает право действия над узлом, чтобы два агента не меняли одно и то же независимо и не создавали конфликт.

В тексте важно показать две проблемы:

1. Без claim параллельность превращается в дублирование и конфликт.
2. Со stale claim работа может исчезнуть из practical ready set, хотя фактически её уже никто не делает.

Поэтому PWG должен поддерживать не только claim, но и claim cleanup / renewal. Сессия оборвалась; agent failed; worktree deleted; claim must not remain sacred forever. Но автоматическое снятие claim тоже опасно, если работа действительно продолжается в другой среде. Здесь нужен аккуратный механизм: срок, owner, source/worktree reference, last heartbeat, human override or recovery procedure.

### Gates

Gate — центральное понятие для главы. Gate — это формализованное ожидание, которое блокирует продолжение или acceptance. Оно может быть человеческим, временным, CI-related, PR-related, source-related, dependent-work-related.

Важно объяснить, почему gate не должен жить только в голове человека или в тексте summary. Если gate не является объектом graph state, следующая сессия легко сделает ложный шаг:

- продолжит до решения, которое ещё не принято;
- закроет работу, пока CI ещё pending;
- забудет, что PR должен быть merged, а не просто opened;
- примет зеленый сигнал не того run;
- перепутает elapsed time with resolved condition.

Gate переводит ожидание из «пометки» в проверяемое состояние работы.

### Проверочные основания / evidence state

В рабочем листе исходно стоит слово «свидетельства». Для финального текста лучше не закреплять его механически. Пользователь уже отмечал, что слово звучит неудачно. В рамках главы можно использовать более естественные формулировки: «проверочные основания», «основания принятия», «состояние проверок», «следы проверки», «сигналы проверки». Английское `evidence` можно оставить в техническом месте, но не строить русский текст вокруг кальки.

Для главы VII не нужно полностью решать терминологию evidence. Нужно лишь показать, что узел не может считаться завершённым, если граф не знает, на чём основана acceptance claim:

- тесты прошли или только были запущены;
- reviewer accepted or requested changes;
- subagent output was accepted, rejected or not yet triaged;
- CI signal belongs to current source state;
- manual check performed, pending or obsolete;
- known edge case intentionally deferred or unresolved.

Эта часть должна быть строго ограничена: глава VII не доказывает, что результат качественный; она хранит состояние того, что позволяет или не позволяет считать работу готовой к продолжению/закрытию.

### Source state

Source state — один из самых важных элементов, который легко теряется в summary. Любой вывод агента зависит от состояния источников: commit, branch, PR, CI run, документа, issue, API spec, migration version, dependency version.

Глава должна показать несколько типичных провалов:

- subagent сделал правильный вывод, но по старому commit;
- тест был зелёным до rebase;
- review comment закрыт, но target branch changed;
- документация обновилась, а рабочий item ссылается на старую версию;
- branch exists, но worktree removed or diverged;
- generated patch no longer applies.

PWG должен хранить не весь мир, а достаточные markers of source state, чтобы не принимать stale facts as current.

### Prime / restoration packet

Здесь глава должна сделать важное движение: продолжение работы требует не только данных, но и восстановления рабочей формы. Агенту нужно знать не всё, а правильный minimum:

- какие команды/протоколы использовать;
- какой граф открыть;
- какие узлы ready;
- что blocked and why;
- какие gates pending;
- какие claims active/stale;
- какие sources are current;
- какие cleanup actions required;
- где не надо начинать заново.

`Prime` или restoration packet — это мост от постоянного графа к следующей сессии. Это не summary of the whole project. Это подготовка агента к корректному действию в текущей форме работы. Для границы с VI: hooks/MCP/skills may deliver it. Для VII: graph state supplies what must be delivered.

### Cleanup and stale state

Постоянный граф работы может деградировать. Это важно признать внутри самой главы, иначе PWG будет выглядеть как очередной «серебряный» механизм. Деградации:

- stale claims;
- stale blockers;
- resolved gates that remain open;
- open gates that were resolved outside the graph;
- duplicate work items;
- issue hierarchy used as blocker hierarchy;
- loose relation wrongly blocking ready work;
- source-state marks not updated after rebase/merge;
- old subagent conclusions treated as current;
- abandoned work items hiding real next step;
- over-detailed graph that agents stop reading.

Cleanup — не хозяйственная мелочь. It is graph hygiene that preserves the possibility of continuation. Но глава VII должна не уходить в будущую главу XIII; здесь cleanup нужен только как условие правдивого work graph.

## Отличие от соседних глав

### От главы VI

Глава VI говорит о проекте как об интерфейсе работы: где правила, skills, hooks, MCP, subagents, command surfaces, project context and route selection. Она отвечает на вопрос: через какие поверхности проект направляет агента и какие рабочие возможности ему даёт.

Глава VII отвечает на другой вопрос: когда маршрут уже был выбран и работа началась, где сохраняется её состояние так, чтобы её можно было честно продолжить.

Простая граница:

- VI: как проект говорит агенту, каким способом работать.
- VII: как проект хранит, где работа находится.

Эту границу можно показать на `bd prime` / Codex hooks. Hook может доставить prime at SessionStart or after compaction. Но сам prime имеет смысл только потому, что есть долговечный рабочий граф и протокол работы с ним. Delivery belongs to VI; work-state meaning belongs to VII.

### От главы VIII

Глава VIII должна говорить о process profiles: каким способом действовать с узлом — исследовать, исправлять, проверять, стабилизировать, переписывать, изолировать риск, делать repair loop, escalate to human, fork subagent, etc.

Глава VII не выбирает стиль действия. Она показывает состояние узла: ready, blocked, gated, claimed, stale, needs review, has conflicting signals, can be picked up, should be cleaned.

Простая граница:

- VII: где работа и что с ней известно.
- VIII: какой режим работы применить дальше.

Финальный мост главы VII должен прямо вести в VIII: когда граф показывает, что узел готов или заблокирован определённым образом, следующий вопрос — не «что случилось раньше», а «какой рабочий профиль нужен теперь».

### От главы IX

Глава IX — execution environment, runtime rights, sandbox, harnesses, worktrees, durable execution, tool permissions. Она отвечает на вопрос: в какой среде действие реально исполняется and what rights/resources/checks it has.

PWG не является runtime. Он может ссылаться на worktree, CI run, sandbox state, durable workflow, but it is not reducible to them. Runtime может checkpoint execution; PWG must record work-state semantics.

Простая граница:

- IX: как действие выполняется и восстанавливается технически.
- VII: что именно должно быть продолжено и почему это состояние правдиво.

Durable execution examples must be used as contrast, not as replacement.

### От главы X

Глава X, судя по корпусу, будет про Gas Town / Beads / broader organization. Там можно говорить о городе агентов, ролях, gas stations, организационной форме.

Глава VII должна быть уже и строже: не вся Gas Town organization, а минимальная переносимая форма work-state graph. Beads может быть главным внешним примером, но не надо разворачивать полный Gas Town narrative.

Простая граница:

- VII: work graph as continuation state.
- X: broader agent-work organization/ecosystem.

### От глав XI/XII

Главы XI/XII, по текущей карте, будут глубже говорить о evidence, authority, acceptance, verification and probably how results become legitimate. Глава VII не должна заранее съесть эту тему.

В VII достаточно сказать: acceptance claim must be graph-visible enough to affect ready/done. Какие именно проверки считаются достаточными, кто имеет право принять, как устроен evidence contract — это позже.

### От главы XIII

Глава XIII, вероятно, про cleanup/debt/stabilization. В VII cleanup появляется только как maintenance of graph truth. Не надо превращать главу в общую теорию технического долга.

## Внутренняя композиция главы

Это не финальный план, но рабочая рамка для будущего draft.

### 1. Начать с невозможности продолжать из summary

Лучшее начало — не абстрактное определение PWG. Начать с ситуации: сессия закончилась, есть «почти готово», но следующий агент не знает, что из этого реально можно делать. Summary сообщает историю, но не отделяет ready work from blocked work.

Сразу показать billing/API example in compressed form.

### 2. Сформулировать сбой локального `done`

Показать, что `done` на уровне сессии, patch, subagent output or one CI signal не равен завершению работы. Это центральная драматургия главы.

Важно не морализировать про «модель обманула». Модель может честно завершить локальную операцию. Ошибка в том, что система принимает локальный конец за конец изменения.

### 3. Ввести PWG как состояние продолжения

Затем дать определение: PWG — это долговечный граф work items, relations, readiness, claims, gates, source state and restoration context, который позволяет следующей сессии продолжить работу без догадки.

Здесь же отличить от summary, issue list and runtime checkpoint.

### 4. Разобрать элементы графа

Отдельными подглавами или компактными секциями:

- work item;
- relation types;
- ready queue;
- claims;
- gates;
- checking/acceptance state;
- source state;
- prime/restoration packet;
- cleanup of stale state.

Каждая секция должна держать пример billing/API, а не превращаться в словарик.

### 5. Внешний якорь Beads

После собственной рамки можно ввести Beads как current-practice example. Не раньше, чтобы читатель не подумал, что глава просто объясняет инструмент.

Использовать:

- `bd ready` for computed readiness;
- `bd gate` for durable wait;
- `bd prime` for restoration;
- Dolt source-of-truth and dependency-aware graph;
- GitHub/Linear/Task Master as broader baseline.

### 6. Граница с durable execution

Отдельная секция или контрастный блок: runtime can pause/resume execution; PWG keeps work intelligible across sessions and actors. Use LangGraph/Temporal/Pydantic AI as short external references.

### 7. Как граф портится

Показать negative side: stale claims, wrong dependencies, stale source state, open gates, overgrown graph. Это нужно, чтобы глава не выглядела как простое добавление ещё одного инструмента.

### 8. Финальный мост к process profiles

Закончить тем, что граф не говорит сам по себе, как действовать дальше. Он говорит, где работа находится and what constraints apply. Следующая глава должна показать, какие профили действия применяются к этим состояниям.

## Тон главы

Глава должна быть инженерной, но не сухой. Здесь есть понятная человеческая боль: «всё почти готово, но никто не может безопасно продолжить». Нужно писать не языком управления задачами, а языком восстановления рабочей правды после распада сессии.

Опасные стилистические ловушки:

- «граф становится источником истины» — можно использовать, но не слишком часто и не как магическую формулу;
- «свидетельства» — избегать как основного русского термина;
- «персистентный» — лучше «постоянный», «долговечный», «сохраняемый за пределами сессии»;
- «оркестрация» — осторожно, это скорее VIII/IX/X;
- «карта работы» — возможно хорошо, но нельзя заменить граф карты только метафорой;
- «агентская память» — слишком широко; PWG is not all memory;
- «handoff» — не сводить к передаче между людьми; here it is continuation state.

Желательный стиль:

- сначала конкретная ситуация;
- затем точное различение;
- затем механизм;
- затем внешний пример;
- затем границы и деградации.

## Фактические внешние опоры, которые должны поддержать рамку

Главная внешняя опора — Beads:

- `bd ready` shows open issues with no active blockers and can atomically claim a ready issue;
- `bd gate` turns human/timer/CI/PR/bead waits into blocking work-state objects;
- `bd prime` provides AI-optimized workflow context after session start or compaction;
- architecture positions Dolt as source of truth and warns about sync/recovery limits.

Baseline sources:

- GitHub Issues now supports sub-issues and issue dependencies; GitHub CLI changelog 2026-06-10 makes this available through `gh`, including JSON fields useful for scripts and coding agents.
- Linear has blocked/blocking/related/duplicate semantics.
- Task Master tasks carry dependencies, status, details, test strategy and subtasks; clusters show dependency topology and parallel execution possibilities.

Boundary sources:

- LangGraph persistence/interrupts: graph state checkpoints and human-in-the-loop pause/resume.
- Temporal: durable human approval waits and audit trail.
- Pydantic AI / DBOS / Restate / Temporal integrations: durable execution that preserves progress across failures, replays journals or workflows, persists model calls and steps.

These sources should not dictate the chapter’s conceptual frame. They should confirm that the frame is not invented in the air.

## Что эта глава должна оставить читателю

После главы читатель должен перестать думать о продолжении агентской работы как о пересказе истории. Он должен увидеть, что нужна отдельная рабочая форма: не просто «память», не просто «issue tracker», не просто «checkpoint», а граф, где продолжение вычисляется и проверяется.

Хорошая итоговая мысль:

Если проект не хранит work state as graph, каждая новая сессия вынуждена либо доверять красивому summary, либо заново раскапывать историю. В простых задачах это терпимо. В долгой агентской разработке это превращает `done` в иллюзию: работа кажется законченной там, где она всего лишь вышла из видимого контекста.
