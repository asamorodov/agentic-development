# 06 — сквозной пример для главы VIII

Это рабочее разворачивание примера, а не готовый фрагмент главы. Его задача — дать одну предметную линию, через которую можно провести различия между PWG, процессным профилем, средой исполнения и организационным слоем.

## 1. Исходная ситуация после главы VII

В проекте есть узел работы:

```text
PWG node: billing/API-compatibility
```

Проект переводит биллинг со старого REST API на новый внутренний service layer. Наружный контракт нельзя ломать: часть enterprise-клиентов использует старые endpoints, часть мобильных клиентов работает через старые SDK, часть webhooks завязана на старые payload names.

После предыдущей агентской сессии в PWG уже есть состояние:

- затронутые области: `BillingController`, `InvoiceService`, `PaymentWebhookHandler`, `legacy-contract-tests`, documentation snippets;
- зависимость от `auth-migration`, потому что новый service layer использует другой principal model;
- открытый вопрос по backward compatibility для `invoice.status` и `payment_state`;
- CI падает на двух legacy contract tests;
- code review оставил замечания по naming и error mapping;
- prime содержит краткое восстановление: что пробовали, какие решения уже отвергнуты, какие тесты надо запускать первыми;
- есть блокер: продуктовый владелец ещё не подтвердил, можно ли менять response shape в одном edge case;
- есть evidence: часть новых unit tests зелёная, но compatibility suite не зелёная;
- статус: implementation partially done, verification not passed.

Это хорошее состояние работы. По нему можно восстановить контекст. Но оно ещё не говорит, каким способом продолжать.

## 2. Неправильный вход: агент видит состояние и продолжает реализацию

Самый простой сбой выглядит так: следующая сессия открывает prime, видит failing tests и review comments, берёт роль обычного исполнителя и начинает исправлять код.

Поверхностно это выглядит разумно. Есть файлы, есть падающие тесты, есть замечания. Но именно здесь проявляется сбой главы VIII: агент вошёл в работу в режиме implementation, хотя состояние узла ещё не доказывает, что implementation сейчас допустима.

Что может пойти не так:

1. Агент исправит `invoice.status`, чтобы прошли тесты, но тем самым изменит поведение для enterprise-клиентов.
2. Агент «починит» mapping ошибок, не заметив, что old SDK ожидает старое имя поля.
3. Агент закроет review comments, но не снимет продуктовый блокер.
4. Агент напишет новые тесты под своё решение и объявит progress, хотя compatibility suite всё ещё не является evidence достаточного уровня.
5. Агент сделает локально хорошую правку, но продолжит план, который уже должен был быть пересобран.

PWG помог восстановить, где работа находится. Но без процессного профиля агент не понял, кем он должен быть в этой точке.

## 3. Возможный правильный вход №1: story execution

Если продуктовый блокер снят, compatibility decision есть, `sprint-status.yaml` показывает story в состоянии backlog или ready, story file уже собран, а acceptance criteria явно требуют сохранить старые response shapes, тогда правильный режим — story execution.

В этом режиме следующий агент должен:

- прочитать story file, architecture notes, relevant PRD section, `project-context.md`, previous summary;
- проверить, какие acceptance criteria относятся именно к совместимости;
- менять только файлы, входящие в радиус story;
- запускать заранее указанные unit tests и legacy contract tests;
- записать summary изменения;
- не менять requirement или acceptance criteria по собственной инициативе;
- остановиться, если обнаружено противоречие между story и реальным старым поведением.

Выход этого режима:

- working code;
- обновлённые тесты, если они действительно выражают старый контракт;
- summary implemented changes;
- evidence: какие проверки прошли;
- возможный статус story: implementation complete, review needed, blocked или needs course correction.

Здесь процессный профиль сужает действие. Агент не занимается общим исследованием биллинга, не переписывает API, не меняет план, не открывает продуктовую дискуссию без причины. Он исполняет уже подготовленную story.

## 4. Возможный правильный вход №2: story creation

Другая ситуация: в PWG есть узел `billing/API`, но story ещё не создана или создана плохо. Есть epic, есть архитектурные заметки, есть старые обсуждения, но нет компактного implementation-ready контейнера.

Если агент войдёт как исполнитель, он сам начнёт реконструировать задачу из разбросанных материалов и почти неизбежно потеряет важные ограничения. Правильный режим здесь — подготовка story.

В этом режиме следующий агент должен:

- прочитать PRD, architecture, epics, старые решения, notes из PWG, relevant old code, compatibility tests;
- собрать, какие части контекста должен получить future dev agent;
- выделить acceptance criteria: какие response shapes нельзя менять, какие старые ошибки надо сохранить, какие новые случаи можно изменить;
- добавить source hints: какие файлы старого кода и какие тесты читать;
- перенести known risks: old SDK, webhooks, enterprise clients, auth migration;
- записать вопросы отдельно, а не прятать их внутри расплывчатых задач;
- остановиться, если нет ключевого решения по product contract.

Выход этого режима:

- story file;
- список unresolved questions;
- связь со sprint status;
- возможно, recommendation: не начинать implementation до решения по compatibility.

Состояние PWG здесь остаётся важным, но оно не заменяет story profile. Работа должна не «продолжиться», а быть подготовлена к безопасному продолжению.

## 5. Возможный правильный вход №3: brownfield-анализ

Третий вариант: в old billing API нет надёжной документации. В тестах видно, что `payment_state=settled` иногда соответствует `invoice.status=paid`, но для частичных возвратов старый API выдавал комбинацию, которой нет в новой модели. Никто в текущей команде уже не помнит, почему так сделано.

Если агент войдёт как исполнитель, он может «нормализовать» странность старого API. Для новой модели это будет красиво, но для реальных клиентов — breaking change.

Правильный режим здесь — brownfield-навигация или investigation of existing behavior.

В этом режиме агент должен:

- читать старый код как источник фактического поведения, а не как материал для немедленной замены;
- найти contract tests, production logs, SDK usage, документацию клиентов, old tickets;
- различать confirmed facts, deduced behavior and hypotheses;
- не переписывать API до фиксации поведения;
- создать карту старых семантических случаев;
- выявить, какие странности являются случайными багами, а какие стали внешним контрактом;
- оформить результаты так, чтобы product/architecture могли принять решение.

Выход этого режима:

- investigation report или brownfield notes;
- таблица старых cases and observed behavior;
- перечень confirmed compatibility requirements;
- перечень open questions;
- рекомендация: какие части можно менять, какие нельзя, где нужен human decision.

Здесь процессный профиль расширяет действие: агент больше не ограничен конкретной story implementation, но и не получает право переписывать систему. Он исследователь старого поведения.

## 6. Возможный правильный вход №4: correct-course

Четвёртый вариант: во время исполнения обнаружено, что исходный план неверен. Например, architecture предполагала, что `invoice.status` можно напрямую вывести из нового service layer, но old API фактически кодирует несколько бизнес-смыслов в одном поле. Простая миграция нарушит старые клиенты.

Если агент просто продолжит реализацию, он будет углублять неверный план. Нужен профиль course correction.

В этом режиме агент должен:

- зафиксировать trigger: какое новое обнаружение ломает исходный план;
- загрузить PRD, epics, architecture, UX/API documentation, existing story, PWG state;
- проверить impact: какие stories, requirements, architecture decisions and tests затронуты;
- предложить варианты: direct adjustment, rollback, MVP scope review, separate compatibility layer;
- показать old → new changes для affected stories/requirements;
- не применять правки молча, если они меняют scope или acceptance criteria;
- вывести работу к человеческому решению или к новому утверждённому плану.

Выход этого режима:

- Sprint Change Proposal или аналогичный change package;
- список affected artifacts;
- recommended path;
- explicit edits;
- decision log entry;
- обновлённое состояние PWG: implementation blocked until course decision или ready after approved plan.

Это ключевой пример для главы: правильное продолжение — не продолжение. Правильное продолжение — смена режима.

## 7. Возможный правильный вход №5: verification / review

Пятый вариант: код уже написан, product blocker снят, story acceptance criteria выполнены, но нет доказательств. CI зелёный только частично, legacy suite запускали локально, UAT не сделан, review comments не закрыты.

Если агент войдёт как executor, он может продолжить polishing. Но узел уже нуждается не в реализации, а в проверке.

В режиме verification/review агент должен:

- прочитать story, acceptance criteria, previous summary, changed files, test plan;
- запустить или запросить нужные проверки;
- отличить unit success от compatibility evidence;
- проверить, что review comments закрыты не формально, а по смыслу;
- записать PASS/FAIL/CONCERNS;
- не объявлять завершение без evidence;
- вернуть работу в implementation только с конкретными defect items.

Выход:

- verification report;
- review decision;
- список fix items или PASS;
- обновление статуса story;
- evidence, достаточная или недостаточная для ship.

Здесь процессный профиль задаёт gate. Без него состояние «код вроде готов» слишком легко превращается в ложное завершение.

## 8. Возможный правильный вход №6: human checkpoint

Шестой вариант: технически агент может предложить compatibility layer, но это меняет сроки, scope и поддержку старых клиентов. Это уже не только инженерное решение.

Правильный профиль здесь — остановка до human checkpoint.

Агент должен:

- собрать варианты в форме, пригодной для решения;
- явно отделить факты от гипотез;
- показать последствия для старых клиентов, сроков, тестов и поддержки;
- не выбирать product tradeoff сам;
- записать, какое решение требуется и кто может его принять;
- обновить состояние так, чтобы следующая сессия не начала implementation до решения.

Выход:

- decision request;
- короткий briefing;
- список вариантов и последствий;
- состояние blocked-awaiting-human-decision;
- запрет на следующий implementation step до ответа.

Это важная граница: protected process profile иногда нужен не для запуска агента, а для остановки агента.

## 9. Как результат возвращается в рабочее состояние

Процессный профиль не заменяет PWG. После каждого режима он должен вернуть результат в рабочее состояние.

Если был story execution, PWG должен получить implemented files, tests run, evidence, remaining blockers, review needed.

Если был story creation, PWG должен получить story file, unresolved questions, ready/not-ready status.

Если был brownfield investigation, PWG должен получить confirmed behavior, open hypotheses, affected contracts, recommended next profile.

Если был correct-course, PWG должен получить change proposal, decision status, affected nodes, blocked/ready state.

Если был review, PWG должен получить PASS/FAIL/CONCERNS, fix items, evidence.

Если был human checkpoint, PWG должен получить decision request and blocked state.

Так пример связывает главы VII и VIII: PWG хранит продолжимость работы, а процессные профили создают обновления, которые меняют её состояние и следующий допустимый ход.

## 10. Граница со средой исполнения

Даже когда профиль выбран, остаётся вопрос главы IX: где агент действует и какие права имеет.

Например, story execution может быть правильным режимом, но executor должен работать в отдельном worktree, с ограниченным радиусом файлов, с доступом к тестам и без права менять PRD. Correct-course может требовать чтения planning artifacts, но не права сразу переписывать весь код. Investigation может требовать read-only доступа к старому коду и логам. Verification может требовать запуск tests, но не право исправлять их по пути.

В VIII это можно только обозначить. Главная мысль: профиль выбирает способ действия; среда исполнения должна ограничить реальные действия под этот способ.

## 11. Граница с организационным слоем

Если таких узлов много — `billing/API`, `auth-migration`, `webhook-contracts`, `customer-export`, `legacy-SDK` — один процессный профиль уже недостаточен. Нужно распределять потоки, выбирать владельцев, держать очереди, prime, gates, service work, backpressure. Это уже материал для Gas Town / Beads / главы X.

В VIII достаточно показать: пока речь идёт об одном рабочем узле, вопрос — «каким режимом его продолжать?». Когда таких узлов много и они требуют отдельной организации среды, вопрос меняется на «как управлять множеством потоков и ролей?». Это следующий слой, не предмет текущей главы.

## 12. Рабочая формула примера

Для последующего черновика можно держать компактную формулу:

> Один и тот же `billing/API` node может требовать story execution, story creation, brownfield investigation, correct-course, verification or human checkpoint. PWG показывает состояние узла; protected process profile выбирает допустимый способ следующего хода; execution environment ограничивает реальные права действия; organizational layer управляет множеством таких узлов.
