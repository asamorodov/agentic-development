## 11. Артефакт намерения: prompt как delivery artifact {#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli}

[Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) стоит читать не как очередную технику “написать хороший запрос”, а как сильную форму управления намерением в агентской разработке. Его исходный ход простой: когда модель уже может быстро производить код, главная опасность — не медленная реализация, а быстро размноженное недопонимание. SPDD поэтому переносит центр процесса с одноразового чата на сопровождаемый артефакт намерения.

<figure class="source-figure" id="fig-fowler-spdd-overview">
  <img src="assets/theory-images/fowler-spdd-overview.svg" alt="Structured-Prompt-Driven Development: prompts as first-class delivery artifacts." loading="lazy" />
  <figcaption>SPDD начинает не с генерации кода, а с превращения prompt в первый класс delivery artifact: его можно версионировать, ревьюить, переиспользовать и синхронизировать с кодом. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-overview.svg</code>.</figcaption>
</figure>

В обычном агентском режиме запрос часто живёт слишком коротко. Он попадает в чат, помогает получить `diff`, а затем растворяется в истории, сжатии контекста, последующих правках и локальных объяснениях. Через две недели остаётся код, но теряется исходная модель решения: какие требования были поняты, какие границы приняты, какие варианты отклонены, какие нормы считались обязательными и какие предохранители нельзя было нарушать. SPDD отвечает на это превращением structured prompt в поддерживаемый файл, который лежит рядом с кодом и продолжает быть рабочим объектом после генерации.

Это роднит SPDD с [Boris Tane](#story-01-boris-tane--4-stadiya-planirovaniya-plan-kak-otdelnyy-markdown-dokument), где `research.md` и `plan.md` делают первое понимание агента видимым до кода, с [Jesse Vincent](#story-06-jesse-vincent--5-plan-kak-perenosimyy-nositel-konteksta), где план становится входом для следующей сессии, и с [Mark Erikson](#story-10-mark-erikson--11-dev-plans-vneshnyaya-rabochaya-pamyat-otdelennaya-ot-repozitoriya-koda), где внешняя память защищает ментальную модель человека. Но SPDD идёт дальше минимального plan-first. Он говорит: если артефакт намерения действительно важен, его нужно не только написать до кода, но и сопровождать после кода.

SPDD полезен именно как team-level метод. Fowler / Thoughtworks начинают статью с ограничения индивидуального AI-ускорения: один разработчик может быстрее набрасывать и менять код, но системная скорость упирается в ambiguous requirements, рост review load, inconsistency, integration/testing issues и production risk. SPDD отвечает не на вопрос “как сгенерировать больше кода”, а на вопрос “как сделать AI-generated changes governable, reviewable and reusable”. Поэтому его нельзя свести к улучшенной формулировке prompt. Это попытка перенести prompt в ту же дисциплину, где уже живут код, тесты, review и commit history.

Важно не подменить эту мысль лозунгом “документы важнее кода”. В SPDD код, тесты, runtime-проверки и человеческие решения остаются отдельными слоями истины. Отличие в том, что намерение перестаёт быть расходуемым сообщением. Оно становится версионируемым, ревьюируемым и повторно используемым объектом, который должен эволюционировать вместе с реализацией.

## 12. Что SPDD добавляет к SDD и почему это не просто spec-first {#spdd-adds-to-sdd}

SPDD начинается в той же точке, что и [spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html): сначала формулируется спецификация, затем модель помогает получить код. Но важная часть SPDD не в факте “spec before code”, а в способе производства, проверки и сопровождения этой спецификации. Thoughtworks в отдельном [обзоре SDD](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) различает **spec-first**, **spec-anchored** и **spec-as-source**. SPDD находится ближе всего к spec-anchored: prompt/spec сохраняется после первой реализации и становится якорем дальнейшей эволюции, но не объявляется единственным источником правды.

У SPDD есть четыре добавления к обычному SDD.

Первое — **maintained artifact**. Structured prompt не создаётся один раз и не выбрасывается после генерации. Он проходит workflow, живёт в version control, может ревьюиться, переиспользоваться и улучшаться.

Второе — **переход от требований к engineering spec**. [REASONS Canvas](#theoretical-synthesis--spdd-reasons-canvas-intent-design-execution-governance) не только говорит, что система должна делать. Он фиксирует chosen approach, system structure, engineering norms и safeguards. Модель получает не только цель, но и implementation boundary.

Третье — **[sync, not handoff](#theoretical-synthesis--spdd-prompt-update-sync)**. Prompt и code не расходятся молча. Если меняется business rule, сначала меняется prompt. Если код меняется без изменения поведения, prompt синхронизируется обратно. Следующая итерация стартует от актуального intent asset, а не от исторического документа.

Четвёртое — **repeatable team control**. Цель не в том, чтобы каждый раз писать более длинную спецификацию. Цель в том, чтобы команда могла повторяемо управлять AI output: смотреть на один и тот же тип артефакта, проверять похожие места, переносить доменное знание между итерациями и снижать variance между разработчиками.

Поэтому SPDD занимает промежуточную позицию. Он сильнее обычного [`plan.md`](#story-01-boris-tane--4-stadiya-planirovaniya-plan-kak-otdelnyy-markdown-dokument), потому что план должен быть синхронизируемым delivery artifact. Но он осторожнее spec-as-source, потому что не требует, чтобы человек перестал трогать код. Для этого сайта это важный баланс: doc-first не должен превращаться в “документ вместо системы”. Хороший intent artifact должен быть связан с кодом, тестами, runtime evidence и человеческим решением, а не заменять их.

## 13. Шесть стадий SPDD: распределённое подтверждение намерения {#spdd-six-step-workflow}

SPDD workflow устроен не как один большой “сначала план, потом код”. В Q&A авторы специально объясняют, почему шагов шесть: если подтвердить intent одним большим review после plan generation, когнитивная нагрузка слишком велика. Люди начинают skim, откладывать, одобрять по умолчанию, и drift становится неизбежным даже в аккуратно выглядящем документе. SPDD дробит подтверждение намерения на маленькие решения, которые человек ещё способен реально прочитать.

<figure class="source-figure" id="fig-fowler-spdd-workflow">
  <img src="assets/theory-images/fowler-spdd-workflow.svg" alt="SPDD workflow: бизнес-ввод, анализ, структурированный запрос, генерация, проверка и синхронизация." loading="lazy" />
  <figcaption>SPDD workflow показывает закрытый цикл: бизнес-ввод превращается в анализ, REASONS Canvas, генерацию, проверку, ревью и обратную синхронизацию prompt/code. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-workflow.svg</code>.</figcaption>
</figure>

Полная последовательность выглядит так.

1. **Create initial requirements**: raw idea или enhancement превращается в user story. Опциональная команда [`/spdd-story`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) разбивает крупное требование на INVEST-like stories размером примерно 1–5 дней, с business-language acceptance criteria.
2. **Review and clarify the story**: человек подтверждает, что story действительно выражает нужный business intent. В walkthrough две generated stories объединяются в simplified story с Background, Business Value, Scope In, Scope Out и Acceptance Criteria.
3. **Generate analysis context**: [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) извлекает domain keywords, сканирует релевантную часть codebase, выделяет existing/new concepts, business rules, strategic approach, risks и gaps.
4. **Generate and review REASONS Canvas**: [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) превращает analysis context в structured prompt: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards.
5. **Generate code, validate behavior and review**: [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) строит код по Operations, затем [`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) проверяет system boundary, а review делит изменения на logic corrections и refactorings.
6. **Generate unit tests**: после стабилизации реализации создаётся отдельный testing prompt, сценарии дедуплицируются против существующего test suite, затем генерируются unit tests как regression safety net.

Смысл последовательности не в ceremony. Каждый шаг сужает вопрос для человека. На [story уровне](#theoretical-synthesis--spdd-story-shaping) проверяется правильная business problem. На [analysis уровне](#theoretical-synthesis--spdd-analysis-context) — domain understanding и risks. На [Canvas уровне](#theoretical-synthesis--spdd-reasons-canvas-intent-design-execution-governance) — design, boundaries и executable operations. На code level — behavior, structure, maintainability. На unit-test level — долговременная regression protection. К моменту code review требования, доменная модель и design уже должны быть подтверждены, поэтому человеческое внимание тратится на решения, которые действительно относятся к коду.

Это уточняет обычный [plan-first](#handbook--plan-first). У [Boris Tane](#story-01-boris-tane--4-stadiya-planirovaniya-plan-kak-otdelnyy-markdown-dokument) человек видит план до реализации. В SPDD человек видит не один план, а несколько слоёв намерения, каждый из которых должен быть достаточно малым, чтобы его можно было прочитать без иллюзии контроля.

## 14. Story shaping: сырое требование ещё не является входом для Canvas {#spdd-story-shaping}

Сильная деталь SPDD часто теряется при кратком пересказе: workflow начинается не с REASONS Canvas. До [Canvas](#theoretical-synthesis--spdd-reasons-canvas-intent-design-execution-governance) есть story shaping. Команда [`/spdd-story`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) опциональна, но сама стадия принципиальна: raw enhancement нужно превратить в управляемую user story, иначе analysis и Canvas будут уточнять не ту задачу.

В walkthrough исходное enhancement касается billing engine для LLM API platform: существующая система должна поддержать Standard и Premium планы, model-aware pricing, prompt/completion split-rate billing, quota/overage logic и extensible design для будущих pricing models. `/spdd-story` сначала разбивает требование на две deliverable stories: Standard Plan / model-aware pricing и Premium Plan / split-rate billing. Затем авторы для walkthrough сознательно консолидируют их в одну [simplified story](https://martinfowler.com/articles/structured-prompt-driven/#combined-user-story-simplified), чтобы пример был self-contained.

Эта consolidated story сохраняет только пять разделов: **Background**, **Business Value**, **Scope In**, **Scope Out**, **Acceptance Criteria**. Implementation detail сознательно убирается: на story level нужно описать, что система должна делать, а не как. Acceptance Criteria формулируются через Given/When/Then и concrete numeric examples. Например, Standard Plan должен показывать quota-covered tokens, overage и charge в зависимости от `modelId`; Premium Plan должен считать prompt/completion tokens по разным ставкам; response format должен возвращать bill id, customer id, token counts, timestamp, `modelId` и plan-appropriate charge breakdown.

Эта стадия важна для всего метода. Если raw idea плохо сформулирована, REASONS Canvas может сделать её более убедительной, но не более правильной. SPDD поэтому сначала требует согласования business language: что входит в scope, что явно out-of-scope, какие acceptance criteria проверяют реальное поведение, какой Definition of Done будет считаться победой. Только после этого имеет смысл строить analysis context.

В этом месте SPDD близок к [Matt Pocock `/grill-me`](#story-12-matt-pocock-skills--5-grill-me-ostanovit-prezhdevremennoe-ponimanie), но работает в более формализованной delivery-среде. У Pocock skill задаёт вопросы, пока намерение не станет рабочим. В SPDD story shaping делает то же самое, но результат сразу становится входом для следующих команд и будущего versioned artifact.

## 15. Analysis context: strategic clarity до implementation detail {#spdd-analysis-context}

После [story shaping](#theoretical-synthesis--spdd-story-shaping) SPDD не прыгает к Canvas и тем более к коду. [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) получает business requirements, извлекает domain keywords и сканирует только релевантные части кодовой базы. Это важное ограничение: агент не должен “читать всё” как шумный ритуал, но и не должен строить решение из головы. Он ищет domain concepts, business rules, existing concepts, new concepts, strategic direction, risks, gaps и acceptance-criteria coverage.

<figure class="source-figure" id="fig-fowler-spdd-analysis-review">
  <img src="assets/theory-images/fowler-spdd-analysis-review.png" alt="Фрагмент SPDD analysis review: таблицы edge cases и technical risks." loading="lazy" />
  <figcaption>Фрагмент analysis review показывает, зачем SPDD отделяет стратегический анализ от кода: edge cases и technical risks становятся видимыми до генерации. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-analysis-review.png</code>.</figcaption>
</figure>

Analysis context отвечает на “what” и “why”, а не на granular implementation. В billing example он должен распознать существующую billing model, quota logic, plan differentiation, model-aware rate selection, validation behavior, response contract и риски изменения. На этом этапе появляются edge cases и technical risks: отрицательные tokens, unknown customer, missing `modelId`, backward compatibility с historical bills, различие quota/overage и premium split-rate rules.

Review analysis context выполняет две функции. Во-первых, человек проверяет, совпадает ли его понимание требований с интерпретацией AI. Во-вторых, AI может поднять boundary scenarios, которые человек не назвал. Это не “модель знает бизнес лучше”. Это способ дешево расширить список вопросов до того, как они превратились в code paths.

Здесь SPDD особенно хорошо ложится на тезис [HumanLayer](#story-07-humanlayer--4-chelovecheskoe-vnimanie-dolzhno-stoyat-blizhe-k-mestu-gde-rozhdaetsya-delta): человеческое внимание нужно ставить ближе к месту, где рождается delta. Плохая строка в [analysis context](#theoretical-synthesis--spdd-analysis-context) может породить плохой Canvas; плохой Canvas — сотни правдоподобных строк кода. Поэтому analysis review — не подготовительная формальность, а один из самых высокорычажных human gates.

## 16. REASONS Canvas: intent, design, execution, governance {#spdd-reasons-canvas-intent-design-execution-governance}

Центральный инструмент SPDD — [REASONS Canvas](https://martinfowler.com/articles/structured-prompt-driven/#the-reasons-canvas). Он полезен именно тем, что не сводит спецификацию к списку требований или задач. Canvas заставляет удерживать семь измерений: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards. Эта форма ведёт задачу от intent и design к execution и governance.

<figure class="source-figure" id="fig-fowler-spdd-reasons-canvas">
  <img src="assets/theory-images/fowler-spdd-reasons-canvas.svg" alt="REASONS Canvas: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards." loading="lazy" />
  <figcaption>REASONS Canvas показывает, что структурированный запрос удерживает требования, доменную модель, подход, структуру, операции, нормы и предохранители в одном проверяемом артефакте. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-reasons-canvas.svg</code>.</figcaption>
</figure>

Первые четыре элемента работают на уровне абстракции. **Requirements** фиксируют проблему, DoD, acceptance criteria и scope. **Entities** вытаскивают доменные сущности, связи и ключевой vocabulary. **Approach** описывает стратегию решения, trade-offs и выбранные паттерны. **Structure** указывает, где изменение должно лечь в систему: components, dependencies, layers, responsibilities, integration points.

**Operations** переводит абстракцию в исполнимые шаги. В SPDD это не просто TODO-list. Operations должны быть concrete, testable, atomic и acceptance-ready. В Q&A авторы отдельно говорят, что Operations может доходить до method signatures и execution order: reviewers проверяют эти шаги до генерации кода, чтобы generation стала faithful translation of agreed plan, а не импровизацией модели.

Последние два элемента — **Norms** и **Safeguards** — особенно важны для агентской разработки. Norms фиксируют повторяемые инженерные нормы: naming, observability, defensive coding, error handling, layering, logging, team conventions. Safeguards задают non-negotiable boundaries: инварианты, performance limits, security rules, compatibility constraints, запреты на изменение внешнего поведения. Это сближает SPDD с [HumanLayer](#story-07-humanlayer--1-glavnaya-ramka-inzhenerit-nuzhno-ne-tolko-model-no-i-ee-sredu): качество результата задаётся не только моделью, но и тем, какие направляющие, границы и сигналы получает агент.

Сила Canvas в том, что он делает намерение обозримым до `diff`. Человек может проверить не только “что модель собирается сделать”, но и “на каком уровне абстракции она поняла задачу”. Если Requirements выражают не тот продуктовый смысл, если Entities пропускают важный доменный объект, если Approach выбирает плохую архитектурную линию, если Operations разрезают работу по слоям вместо проверяемых [вертикальных срезов](#story-12-matt-pocock-skills--9-to-issues-vertikalnye-zadachi-vmesto-gorizontalnogo-raspila), это нужно увидеть до генерации кода.

Но Canvas не является внешним оракулом истины. Хороший Canvas требует человека, который понимает домен, архитектуру и цену ошибки. Иначе structured prompt может быть просто длинным и уверенным документом, который красиво формализует неверное намерение.

## 17. Три core skills SPDD: Abstraction First, Alignment, Iterative Review {#spdd-three-core-skills}

В статье SPDD отдельно выделены три core skills. Это не side notes, а фактическая модель того, куда смещается ценность разработчика в AI-assisted delivery.

**[Abstraction First](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html)** означает design before generation. До кода нужно понять, какие objects существуют, как они взаимодействуют, где проходят boundaries, какие interface responsibilities фиксируются contract-first, какой уровень granularity допустим. В операционных принципах этого skill есть четыре ключа: design before generation, contract first, control granularity, diagram early. Смысл не в любви к диаграммам, а в том, что narrative requirements слишком легко допускают разные интерпретации; lightweight diagrams, ER diagrams, sequence diagrams или flow charts помогают быстро зафиксировать logic model.

**[Alignment](https://martinfowler.com/articles/structured-prompt-driven/alignment.html)** означает lock intent before code. Здесь проверяется domain language, scope, acceptance criteria, dependencies и hidden constraints. Уточняются термины вроде “customer”, “order”, “asset”; устраняются случаи “same word, different meaning” и “same meaning, different words”; happy path, edge cases и Definition of Done становятся testable. Главный operating principle: analysis doc → structured prompt → code. Если ранний артефакт не aligned, нельзя продвигаться дальше.

**[Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html)** означает turn output into a controlled loop. Агентская работа не должна быть one-shot draft и не должна превращаться в бесконечные patch requests, где решение постепенно drifts. Review loop проверяет prompt/code consistency, architecture and responsibility boundaries, hallucination and correctness. Здесь появляются признаки зрелого процесса: prompt debugging, functional validation, deep code review и asset integrity.

Эти skills важны как сопротивление поверхностному “AI пишет код”. SPDD требует от разработчика не меньше, а больше работы на уровне абстракции. Нужно уметь моделировать домен, принимать архитектурные trade-offs, проектировать atomic tasks, задавать testable acceptance criteria, различать business mismatch и code smell. В этом смысле SPDD не отменяет senior judgement. Он делает места применения этого judgement более явными.

## 18. Generate code: модель реализует locked intent, а не ищет решение заново {#spdd-generate-locked-intent}

Только после [story](#theoretical-synthesis--spdd-story-shaping), [analysis](#theoretical-synthesis--spdd-analysis-context) и [Canvas](#theoretical-synthesis--spdd-reasons-canvas-intent-design-execution-governance) SPDD переходит к [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md). Эта команда читает REASONS Canvas и генерирует код task by task, следуя порядку [Operations](#theoretical-synthesis--spdd-reasons-canvas-intent-design-execution-governance). Она должна придерживаться Norms и Safeguards: no improvisation, no features beyond the spec. В источнике это сформулировано как соответствие один-к-одному: prompt captures the intent, code implements that intent.

Это меняет роль генерации. Модель на этом шаге не должна заново решать, что строить. Она должна выполнить уже согласованный blueprint. Если она обнаруживает contradiction, missing dependency или невозможность выполнить Operations, правильный ход — вернуться к [артефакту намерения](#theoretical-synthesis--10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli), а не тихо выдумать обход.

Для billing example generated code включает product code, tests and reviews. Но review после генерации уже не должен начинаться с полного восстановления смысла из `diff`: смысл был вытащен раньше. Благодаря предыдущим rounds of logical deduction code review получает ясный фокус: проверить, правильно ли реализация перевела locked intent в код, не нарушила ли responsibilities, не добавила ли лишнюю сложность, не галлюцинировала ли imports/dependencies/API.

Здесь SPDD резко отличается от режима, где agent сначала пишет код, а человек потом пытается понять, что произошло. Он ближе к [Mark Erikson](#story-10-mark-erikson--1-ishodnaya-problema-kod-poyavlyaetsya-bystree-chem-vosstanavlivaetsya-smysl): агентская скорость допустима только тогда, когда человек может восстановить смысл результата. SPDD переносит часть восстановления смысла до генерации, чтобы code review не начинался с нуля.

## 19. Проверяемые свидетельства: API tests до глубокого code review {#spdd-validation-review-evidence}

Один из самых полезных для этого сайта ходов SPDD — порядок проверки. В Q&A авторы прямо обсуждают, почему `/spdd-api-test` идёт до глубокого code review, а unit tests — позже. Логика сознательно отличается от TDD. Generated code дешёв; нет смысла глубоко ревьюить код, который ещё не доказал соответствие intended business behavior. Поэтому first gate — поведение на system boundary.

<figure class="source-figure" id="fig-fowler-spdd-api-test-script">
  <img src="assets/theory-images/fowler-spdd-api-test-script.png" alt="SPDD API test script: human-reviewable test-case overview." loading="lazy" />
  <figcaption>Human-reviewable test-case overview показывает, что свидетельство в SPDD должно быть пригодно для чтения человеком: normal, boundary и error scenarios видны до запуска скрипта. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-api-test-script.png</code>.</figcaption>
</figure>

[`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) извлекает API endpoint information из implementation или acceptance criteria и генерирует cURL-based test script. Скрипт содержит test-case table по normal scenarios, boundary conditions и error scenarios. При выполнении он выводит expected-vs-actual comparison results. Важна именно двойная форма: сначала человек может прочитать TEST CASE OVERVIEW, затем увидеть фактический результат выполнения.

<figure class="source-figure" id="fig-fowler-spdd-api-test-results">
  <img src="assets/theory-images/fowler-spdd-api-test-results.png" alt="SPDD API test results summary: expected, actual, pass/fail." loading="lazy" />
  <figcaption>API test results показывают вторую половину свидетельства: expected, actual и result превращают “модель говорит, что работает” в проверяемый сигнал. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-api-test-results.png</code>.</figcaption>
</figure>

После API validation code review фокусируется на том, что только человек или сильный review-agent может оценить: architecture, trade-offs, non-functional concerns, maintainability, layering, exception handling, encapsulation, magic numbers, long methods, imports/dependencies, syntax/compilation, hallucinated APIs, adherence to Norms and Safeguards. Базовое “what” должно быть уже проверено на boundary, иначе reviewer тратит внимание на код, который может не решать задачу.

Такой порядок хорошо связывает SPDD с разделом о [проверяемых свидетельствах](#theoretical-synthesis--39-svidetelstva-dolzhny-byt-prigodny-dlya-sleduyuschego-shaga). “Готово” не является свидетельством. Свидетельство должно быть пригодно для следующего шага: test overview пригоден для human review, expected/actual results пригодны для acceptance decision, code review пригоден для maintainability judgement, unit tests пригодны для будущей regression protection.

## 20. Logic correction, prompt-update и sync: два направления обратной связи {#spdd-prompt-update-sync}

В SPDD важно различать два направления синхронизации. [`/spdd-prompt-update`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) работает, когда изменилось намерение: business rule, constraint, architectural adjustment, accepted behavior. [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) работает, когда изменился код без изменения намерения: refactoring, cleanup, decomposition, new component, implementation detail. В обоих случаях цель одна — Canvas не должен стать historical snapshot.

<figure class="source-figure" id="fig-fowler-spdd-code-review">
  <img src="assets/theory-images/fowler-spdd-code-review.svg" alt="Схема SPDD: два варианта реакции на review comment — менять код напрямую или сначала обновлять prompt." loading="lazy" />
  <figcaption>Схема из SPDD показывает развилку review: если замечание меняет observable behavior, сначала обновляется structured prompt; если это refactoring без изменения поведения, код меняется и синхронизируется обратно. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-code-review.svg</code>.</figcaption>
</figure>

В billing example logic correction появляется вокруг `modelId`. Первоначальная реализация допускает nullable field ради backward compatibility с historical data. После business confirmation команда решает, что для historical bills default value должен быть `fast-model`. Это уже не cosmetic refactoring. Это изменение observable business behavior. Поэтому сначала выполняется [`/spdd-prompt-update`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md): structured prompt уточняет required field, default value и соответствующие части REASONS Canvas. Только после этого обновляется код.

<figure class="source-figure" id="fig-fowler-spdd-prompt-update">
  <img src="assets/theory-images/fowler-spdd-prompt-update.png" alt="SPDD prompt update: пример изменения structured prompt перед обновлением кода." loading="lazy" />
  <figcaption>Prompt update показывает, что business-rule correction не должен растворяться в локальном кодовом патче: сначала фиксируется новое намерение, затем реализация приводится к нему. Источник: <a href="https://martinfowler.com/articles/structured-prompt-driven/">Structured-Prompt-Driven Development</a>. Локальный файл: <code>assets/theory-images/fowler-spdd-prompt-update.png</code>.</figcaption>
</figure>

Напротив, если code review находит magic numbers в `calculateRemainingQuota`, это может быть ordinary refactoring. Observable behavior не меняется. Агент делает small incremental refactor, затем [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) сравнивает current code against Canvas и записывает соответствующие implementation updates обратно в REASONS sections. В источнике это называется golden rule: keep the structured prompt synchronized with your latest codebase.

Это различение полезно за пределами SPDD. В обычном agentic workflow легко смешать logic correction и refactoring. Если bugfix меняет business meaning, но человек правит только код, intent asset начинает врать. Если refactoring заставляют проходить через полноценный business prompt update, процесс становится тяжелее задачи. SPDD даёт язык для этого разведения: requirement → prompt → code и code → prompt — разные направления, и их нельзя путать.

## 21. Unit tests: последний safety net, а не первый источник смысла {#spdd-unit-tests-after-stabilization}

Unit tests в SPDD не исчезают и не становятся второстепенными. Но они появляются после того, как implementation стабилизирована через structured prompt, API validation и review. Причина практическая: если unit tests написать слишком рано, их придётся переписывать после крупных review-driven changes. SPDD поэтому использует API tests для быстрого behavior gate, code review для архитектуры и maintainability, а unit tests — как final regression safety net для core logic.

В walkthrough dedicated testing commands ещё не finalized. Поэтому используется interim template-driven approach. Сначала implementation details prompt комбинируется с testing template вроде [`TEST-SCENARIOS-TEMPLATE.md`](https://github.com/gszhangwei/token-billing/blob/after-enhancement/spdd/template/TEST-SCENARIOS-TEMPLATE.md), чтобы создать baseline test prompt. Затем AI-generated scenarios дедуплицируются и уточняются: агент должен сверить предложенные сценарии с existing test suite, убрать повторы и оставить genuinely new coverage. Только после этого генерируется unit-test code.

Это важная деталь, потому что она удерживает SPDD от слишком гладкого образа “всё автоматизировано командами”. На момент статьи testing stage ещё частично ручной и template-driven. Он показывает не завершённую платформу, а зрелую инженерную осторожность: если команда ещё не имеет dedicated testing command, она всё равно не перескакивает через test design. Она делает test prompt отдельным артефактом, проверяет coverage и только потом генерирует тесты.

Такой порядок не является анти-TDD. В Q&A авторы прямо говорят, что SPDD сохраняет цели TDD — clarify behavior, protect regressions, shape design — но распределяет их иначе. Behavior уточняется раньше через story, Canvas и API tests; design shape возникает через Abstraction First и Operations; regression protection закрепляется unit tests после стабилизации implementation. Это спорный, но осмысленный порядок для AI-generated code, где initial implementation дешёв, а человеческое review attention дорого.

## 22. Asset integrity: prompt version должен соответствовать code commit {#spdd-asset-integrity}

В [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html) есть отдельный пункт, который легко недооценить: **asset integrity**. Код, который попадает в commit, должен cleanly map to the exact prompt version. Иначе теряется traceability: future maintainer видит prompt, видит code, но не знает, какая версия намерения породила какую версию реализации и где начался drift.

Asset integrity превращает SPDD из “хорошо написанной спецификации” в governance mechanism. Если prompt изменился, но код не обновлён, artifact врёт. Если код refactored, но prompt не synced, artifact превращается в historical record. Если code review принял business correction без prompt-update, future evolution стартует от устаревшего intent. Поэтому SPDD требует, чтобы prompt, code, review evidence и tests сохраняли связность во времени.

Практически это означает несколько вещей.

- Prompt assets должны лежать в version control рядом с codebase, а не в chat history.
- Изменения бизнес-логики должны попадать в prompt before code.
- Refactoring без изменения поведения должен возвращаться в prompt через `/spdd-sync`.
- Code review должен проверять not only code quality, but also prompt/code consistency.
- Следующая итерация должна начинаться от accumulated prompt assets: domain model, decisions, norms, safeguards, accepted patterns.

Это сильный мост к теме [внешней рабочей памяти](#cross-story-synthesis--3-8-vneshnyaya-pamyat-kak-zaschita-ne-tolko-agenta-no-i-cheloveka). SPDD делает память не только удобной для агента, но и проверяемой для человека. Не “мы где-то это обсуждали”, а “вот artifact, commit history, review trail и behavior evidence”.

## 23. Где SPDD окупается: ROI, upfront cost и fit table {#spdd-fit-and-roi}

SPDD хорошо подходит не для любой задачи. Его сильная зона — logic-heavy и rules-heavy изменения: биллинг, налоги, отчётность, compliance, права доступа, pricing, business workflows, cross-cutting consistency, migration-sensitive work. Там ошибка часто дорогая, а intent artifact действительно окупается: он снижает hallucination, делает traceability видимой, помогает ревью, удерживает границы и позволяет следующей итерации стартовать с накопленного контекста.

В источнике fit assessment фактически задаёт экономическую модель. На верхнем уровне — scaled, standardized delivery; high compliance and hard constraints; team collaboration and auditability; cross-cutting consistency work. На нижнем уровне — firefighting hotfixes, exploratory spikes, one-off scripts, context black holes, pure creative / visual work. Это не вкусовая классификация. Это вопрос отношения стоимости артефакта к стоимости ошибки и будущей эволюции.

ROI SPDD складывается из нескольких выгод.

| Выгода | Что реально покупается процессом |
| --- | --- |
| Determinism | Логика кодируется в precise spec, поэтому модель меньше “творит” там, где нужна предсказуемость. |
| Traceability | Meaningful change можно проследить к structured prompt, closing the audit loop. |
| Faster reviews | Code приходит ближе к team standards; review меньше тратится на cleanup и больше — на logic/design. |
| Explainability | Intent and behavior видны на natural-language level; maintenance дешевле. |
| Safer evolution | Boundaries and stepwise implementation снижают риск targeted changes. |

Но upfront investment тоже реален.

| Барьер | Что требуется |
| --- | --- |
| Mindset shift | Команде нужно привыкнуть к design-first вместо code-first. |
| Senior expertise up front | Нужны люди, способные переводить business rules в clean abstractions and constraints. |
| Automation tooling | Без CLI/workflow automation SPDD упирается в throughput ceiling и consistency problems. |

Практический критерий такой: SPDD окупается, когда цена неверного намерения выше цены поддержки артефакта. Если задача маленькая, обратимая и близко проверяется браузером или одним тестом, SPDD может стать тяжёлым ритуалом. Если задача проходит через данные, API, business rules, compliance, архитектурные границы или командную передачу знания, отсутствие maintained intent asset может быть дороже.

Это уточняет [лестницу усложнения Handbook](#handbook--choice-map). SPDD не должен стать default-режимом. Он должен стать одной из верхних ступеней: когда обычного `plan.md`, issue, handoff или PRD уже недостаточно, потому что намерение должно сопровождаться вместе с кодом.

## 24. Hotfixes и production signal: governance можно отложить, но нельзя выбросить {#spdd-hotfix-production-signal}

Fit table помечает firefighting hotfixes как слабый fit для SPDD. Это легко понять неверно: будто production bugs, edge cases и failure modes проходят мимо methodology. Q&A уточняет: во время live incident system recovery comes first. Писать Canvas в момент “stop the bleeding” — неправильный выбор. Но governance не отменяется, а переносится на следующий шаг.

Есть два сценария.

**Scenario A — context exists.** Если bug falls inside [область](#theoretical-synthesis--spdd-fit-and-roi), уже покрытую structured prompt, команда может использовать AI для анализа failure, root cause и затем применить compressed SPDD loop: update prompt first, then update code. Так fix становится постоянной частью governed asset, а не локальным emergency patch.

**Scenario B — legacy or no prior context.** Если код не был brought under SPDD, прагматический ход — позволить AI проанализировать logs и исправить issue напрямую. Но closing step должен быть deliberate post-mortem: синтезировать fix, failure mode и relevant context в новые documented assets. Так SPDD coverage органически растёт по codebase.

Это важный пример умеренности. SPDD не должен мешать восстановлению production. Но если production signal не возвращается в intent layer после инцидента, возникает spec/code delta. Код знает о failure mode, а артефакт намерения — нет. Следующая итерация снова начнётся без памяти о реальном сбое.

## 25. Roadmap SPDD: от expert craft к organization-level asset system {#spdd-roadmap-decision-memory}

Авторы честно признают: в нынешнем виде SPDD может выглядеть как метод для senior architects, потому что требует strong abstraction, modelling, systematic analysis и deep business understanding. Их целевое направление другое: framework должен не зависеть полностью от personal craftsmanship, а постепенно переносить часть веса в organization-level asset system.

Roadmap состоит из четырёх направлений.

Первое — **recurring workflows as commands**. Паттерн [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md), [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md), [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md), [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) не закончен. По мере появления повторяемых ситуаций successful workflow извлекается в command, а не остаётся знанием отдельных людей.

Второе — **automated verification at the asset layer**. Проверять нужно не только code level. Будущий слой должен проверять analysis, Canvas и prompt artifacts: gaps, inconsistencies, under-specification, routine calls, structural completeness vs substantive adequacy.

Третье — **raising the automation ratio**. SPDD уже является harness, но semi-automated. Автоматизация должна расти постепенно, только там, где AI надёжно справляется с конкретным type of task. Это не “убрать человека”, а пошагово переносить hand-holding в проверяемые commands and asset checks.

Четвёртое — **decision memory**. Past canvases, trade-offs, accepted patterns and historical decisions должны стать persistent context, который agent может извлекать в новой ситуации. Это особенно близко к теме Noveia и active memory: ценность не только в сохранении документа, но в возможности поднимать правильное предыдущее reasoning именно тогда, когда оно нужно.

В этом смысле SPDD сам движется от методики к экзоскелету. Сначала skilled practitioners вручную строят хорошие artifacts. Потом recurring thinking strategies становятся commands. Затем asset-layer verification и decision memory должны сделать качество менее зависимым от отдельного человека. Это ещё не решённый механизм, но направление важно: SPDD понимает свою текущую слабость и пытается вынести её в инфраструктуру.

## 26. Сопротивление SPDD: variance, model drift, spec-as-source и предел человеческого суждения {#spdd-resistance-boundaries-and-spec-as-source}

Критика SPDD должна быть встроена в сам раздел, иначе метод легко станет слишком гладким. Первая проблема: SPDD не устраняет variance, а частично переносит его на уровень Canvas. В Q&A авторы честно признают, что два разработчика могут написать разные Canvas по одному требованию, а один и тот же человек может в разные дни сделать более сильный или более тонкий artifact. Команды OpenSPDD поднимают нижнюю границу, задавая structure, granularity, abstraction level и task breakdown, но не дают полностью объективного стандарта “хорошего Canvas”.

Вторая проблема: SPDD остаётся human-led. Это сила и ограничение одновременно. Человек проверяет business intent, abstraction, boundaries, trade-offs и пригодность Canvas к реальной задаче. Если человек слаб в домене или поверхностно ревьюит документ, SPDD может не защитить. Он создаёт место для правильного решения, но не гарантирует, что решение будет принято.

Третья проблема — relation to spec-as-source. Thoughtworks различает spec-first, spec-anchored и spec-as-source. SPDD ближе к spec-anchored: spec/prompt сохраняется и сопровождает дальнейшую эволюцию. Но из этого не следует, что спецификация должна стать единственным источником правды. Spec-as-source наследует старые проблемы model-driven development: overhead, ограничения выразительности, трудность синхронизации, опасность того, что формально красивый документ хуже отражает реальную систему, чем код, тесты и эксплуатационные сигналы.

Четвёртая проблема — model and configuration drift. SPDD intended as model-agnostic, но raw capability имеет значение, особенно для analysis и REASONS Canvas. После того как intent зафиксирован, менее сильная модель может быть приемлемым executor, но risk of intent drift остаётся. В некоторых средах реальным артефактом становится не только prompt-as-spec, а prompt + model configuration + command semantics + review protocol. Стратегический выбор зависит от cost, compute and compliance constraints.

Пятая проблема — ceiling на стороне самой задачи. Если область слишком широкая, multi-project, multi-discipline, multi-domain, плохо ограниченная или требует portfolio-scale decisions, модельная сила не спасает. Нужна decomposition, накопленные decision assets и human gates. В context black holes, где business rules unclear и boundaries weak, stronger AI just fails more confidently.

Шестая проблема — риск ухудшения человеческой компетенции при полном agent-driven review. `/spdd-code-review` уже может читать Canvas and code diff together and flag drift. Но авторы считают, что человек всё ещё нужен для двух вещей: catching intent drift, когда сам Canvas уже не соответствует real business intent, и learning from AI choices. Если review полностью отдать агенту, можно ускорить процесс, но потерять long-term skill growth, ради которого SPDD и строит human-led loop.

Итоговая позиция поэтому должна быть двойной. SPDD — один из лучших примеров того, как agentic/doc-first разработка может сделать намерение сопровождаемым инженерным объектом. Но его нельзя превращать в универсальную норму. Он полезен там, где нужно удерживать сложное, проверяемое, дорогое намерение; вреден там, где задача мала, плохо определена или требует быстрой разведки без тяжёлого governance. Для этого сайта SPDD важен именно как сильная форма артефакта намерения и управляемого delivery loop, а не как новая догма.


---
