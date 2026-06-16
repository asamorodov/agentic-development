# VIII — story anchors

Статус: заполнено по текущему тексту главы.

## Сквозной synthetic anchor: `billing/API`

Функция: удерживает центральную проблему главы.

Состояние узла:

- миграция со старого REST API на новый internal service layer;
- старые clients/endpoints/mobile SDK/webhooks;
- affected files: `BillingController`, `InvoiceService`, `PaymentWebhookHandler`;
- compatibility tests;
- dependency on `auth-migration`;
- failing legacy contract checks;
- review comments on error mapping;
- unresolved product decision around response shape.

Как используется:

- ввод: состояние есть, но следующий вход может быть неверным;
- GSD: `STATE.md`, `PLAN.md`, `VERIFICATION.md`, blocker and UAT;
- BMAD: story creation, `correct-course`, brownfield/project-context, `bmad-investigate`;
- route table: один узел → несколько правильных профилей;
- reading/write boundary: широкий радиус чтения не равен праву менять production code.

Статус: synthetic explanatory example. Не источник фактов.

## Jesse Vincent

Использование: small process profiles / gates.

В текст вошло:

- separation of discussion, planning, architecture session, implementation session, spec review and code review;
- reviewer must receive spec/code/criteria, not the whole noisy session;
- removed-tests failure as example of model optimizing visible failure.

Функция в главе: показать, что protected process profile может быть маленьким gate/role boundary, not a full methodology.

## HumanLayer

Использование: transition protection and context boundaries.

В текст вошло:

- research → plan → implement;
- trajectory quality of context;
- subagents as context firewall;
- hooks/feedback loops as signals.

Функция в главе: связать процессные профили с контекстом и переходами, не уходя в execution harness.

## Matt Pocock

Использование: skills as tiny profiles.

В текст вошло:

- `/grill-me`;
- `/grill-with-docs`;
- `/to-prd`;
- `/to-issues`;
- `/triage`;
- `/tdd`;
- `/handoff`;
- `/diagnose`.

Функция в главе: показать, что маленький skill может остановить неправильный вход: преждевременное понимание, неправильное разбиение, отсутствие диагностики, загрязнение следующей сессии.

## Not used

| Story family | Почему не вошло |
|---|---|
| Mae Capozzi | Сильнее относится к orchestration/observability and chapter X/IX. В главе VIII не добавляет отдельный тип process profile. |
| Shopify Roast | Сильнее относится к executable workflow / business process harness. Для главы VIII был бы боковым расширением. |
