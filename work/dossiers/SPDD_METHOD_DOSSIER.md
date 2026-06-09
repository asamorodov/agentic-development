# SPDD — системное методологическое досье

Статус: системно-интеграционная версия после прохода 11 с исправленным справочным хвостом. Верхний слой досье приведён к системной карте методологии; источники и кандидаты на иллюстрации восстановлены внутри этого досье в единых разделах. Фактура из предыдущих проходов не удалялась: подробные сведения сохранены в тематических разделах и в локальном source/image registry этого же файла.

Основание: `SPDD_METHOD_DOSSIER.md` из pass 11.

Граница досье: это рабочий source buffer для будущей теории, не финальная глава. Текст должен помогать модели и человеку видеть устройство метода, а не историю накопительных проходов.

## Устройство досье


- **Зачем существует SPDD:** intent gap, negative space, decision uncertainty и specification validation.

- **Главный артефакт:** REASONS Canvas как контракт намерения уровня фичи.

- **Рабочий процесс:** анализ → Canvas → генерация → проверяемые свидетельства → ревью → update/sync.

- **Проверка:** API tests, code review, intent drift, implicit decisions, asset integrity.

- **Жизнь артефакта:** prompt в git, плановое сопровождение, интеграции, коррекция и синхронизация.

- **Границы:** цена входа, риск stale Canvas, human judgement, ROI и сценарии сбоев.

## Системно-интеграционная карта SPDD

SPDD в этом досье следует читать как метод удержания намерения в управляемом артефакте, а не как набор удачных prompt-шаблонов. Метод начинается с проблемы: модель может построить правдоподобное решение, но не имеет права самостоятельно выбирать нагрузочные бизнес- и архитектурные развилки. Поэтому сначала создаётся REASONS Canvas — контракт намерения уровня фичи. Затем этот контракт проходит через команды анализа, генерации, проверки, обновления и синхронизации с кодом.

Рабочая карта метода в досье устроена так:

1. **Проблема и статус.** Здесь собраны intent gap, negative space, specification validation и место SPDD между свободным prompt-ингом и формальными спецификациями.
2. **Артефактный слой.** Здесь раскрыт REASONS Canvas: семь разделов, ingestion contract, `Safeguards`, `Operations`, asset integrity, repo-level rules и `/spdd-reverse` для подключения legacy-кода.
3. **Жизненный цикл и command surface.** Здесь собраны `spdd-analysis`, `spdd-reasons-canvas`, `spdd-generate`, optional commands, tool-adapter слой и разные поверхности запуска.
4. **Проверка и свидетельства.** Здесь находятся `/spdd-api-test`, `/spdd-code-review`, intent drift, implicit decisions, faithful implementation и API evidence.
5. **Обновление и синхронизация.** Здесь собраны `prompt-update`, `sync`, correction lanes, плановое сопровождение spec-корпуса и внешние примеры применения.
6. **Применимость и риски.** Здесь зафиксированы ROI, upfront cost, stale Canvas, неверный Canvas, человеческое суждение, process calcification и границы внедрения.
7. **Синтез и связи.** Здесь досье связывает SPDD с текущим корпусом и будущей теорией.

Ссылки на источники остаются рядом с фактами. Источники, поисковые формулировки и кандидаты на иллюстрации собраны в единых справочных разделах внутри этого досье, чтобы основной текст не распадался на следы накопительных проходов.

## Краткая рабочая карта

SPDD в этом досье нужно читать не как «метод написания prompt-ов», а как **уровня фичи intent contract**, который живёт рядом с кодом, задаёт границы генерации и должен поддерживаться синхронно с реализацией. Главный переносимый механизм: не заставить модель «лучше подумать», а сделать намерение, ограничения, операции и проверку отдельными ревьюируемыми артефактами. OpenSPDD адаптирует эту идею не только к Claude Code/Cursor, но и к Codex через skill-bundles; значит, SPDD лучше описывать как переносимую дисциплину командных шаблонов, а не как специфичный для Claude рабочий процесс.


## Проблема и статус SPDD в AI-driven SDLC

### SPDD как практический low/formal-middle слой intent formalization

Источник Lahiri полезен тем, что задаёт спектр intent formalization: tests, code contracts, logical contracts и DSLs. В этом спектре SPDD не является полноценным formal-methods методом и не должен так подаваться. Его рабочая зона — между structured informal intent artifact и lightweight executable evidence. REASONS Canvas остаётся mostly human-readable контракт дизайна, а `/spdd-api-test` и `/spdd-code-review` добавляют ближайший проверяемый слой: shell/cURL behavioral tests, expected-vs-actual tables, review report и prompt/code consistency checks.

Это уточняет статус SPDD для будущей теории: SPDD не закрывает intent gap полностью, но делает intent gap видимым, versioned и reviewable. Он не заменяет формальные спецификации, но может служить подготовительным уровнем: сначала человек и модель фиксируют negative space, operations, safeguards и expected behavior; затем часть этого намерения переводится в tests or contracts. В терминах Lahiri, SPDD находится ближе к cost-effective end of the formalization spectrum, где tests и proxy artifacts помогают ловить вероятные расхождения намерения, а не доказывают корректность всей системы.

### Specification validation: почему SPDD не может просто “доверять Canvas”

Сильное внешнее уточнение: главная проблема intent formalization — не только получить specification artifact, но и проверить, что specification itself выражает правильное намерение. Lahiri формулирует это как отсутствие oracle for specification correctness besides the user. Это напрямую усиливает уже имеющийся SPDD-risk: REASONS Canvas может быть аккуратным, полным и implementation-ready, но всё равно кодировать неверный business decision.

Отсюда важное следствие для SPDD-досье: human review должен быть направлен не только на generated code и API-test results, but first on Canvas correctness. Самый опасный сбой — не hallucinated code, а wrong but internally consistent Canvas. Для будущей теории это почти сильнее, чем обычный тезис “prompt is source asset”: prompt-source asset itself needs validation.

### Negative space как центральная причина существования SPDD

OpenSPDD design philosophy явно различает ambiguity that stronger AI can infer from codebase conventions и decision uncertainty that AI cannot infer: event-driven vs synchronous calls, one currency vs multiple currencies, what must not be touched. Этот раздел следует поднять в досье выше как один из главных аргументов. SPDD нужен не потому, что модель плохо пишет код, а потому что модель не имеет права сама выбирать load-bearing design trade-offs.

Практически это означает: `Safeguards` в REASONS Canvas — не декоративный раздел. Это storage for negative space. Если будущая глава будет писать о SPDD как о “структурированном prompt-е”, она недооценит его. Точнее: SPDD — это механизм удержания design authority у человека через versioned, executable, AI-readable declaration of both positive и negative intent.

### Intent-centric software engineering: SPDD как case, а не вся картина

Источник De La Cruz useful mainly as framing: GenAI снижает стоимость plausible code, но повышает значение intent specification, context curation, verification, security, provenance, governance и accountable human judgment. Для SPDD это подтверждающий, но не основной источник. Он помогает не раздувать SPDD до universal methodology: SPDD — один конкретный рабочий процесс в широкой перестройке, где разработчик всё меньше является isolated code author и more supervisor/validator/governor of human-agent-tool-evidence system.

В будущей теории SPDD стоит ставить рядом с Spec Kit, Kiro, BMAD, GSD и Gas Town как один тип intent artifact. Его уникальность — не в “requirements first” вообще, а в tight loop между structured prompt, code generation, API evidence, review и синхронизации prompt/code.

### SPDD как control layer, а не усилитель model capability

OpenSPDD design-philosophy формулирует важное различение: проблема сложной AI-разработки часто не в том, что модель “недостаточно умна”, а в том, что у неё слишком много допустимых вариантов и недостаточно выраженных human trade-off decisions. В тексте это разведено как **capability dimension** и **control dimension**: модель может лучше понимать требования и код, но выбор между несколькими “правильными” архитектурными решениями остаётся человеческим решением, которое нужно внешне зафиксировать. Поэтому SPDD надо описывать не как ещё один способ “писать prompts лучше”, а как слой управления design intent и границами исполнения: REASONS Canvas снижает свободу модели там, где свобода вредна. [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md)

Это уточнение полезно для будущей теории: SPDD не пытается компенсировать слабость модели в кодинге; он переносит человеческое суждение в structured artifact before execution. Поэтому strong model не отменяет SPDD автоматически: чем сильнее модель, тем выше цена незафиксированных boundaries, потому что модель правдоподобно реализует не тот вариант. [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md)

### SPDD between spec-anchored и spec-as-source

Для будущей теории полезно сравнить SPDD with broader spec-driven vocabulary. Paper-style framing “From Code to Contract…” distinguishes **spec-anchored** development, where spec и code evolve together и tests enforce alignment, from **spec-as-source**, where humans edit only the spec и generated code should not be manually changed. Источник: [From Code to Contract in the Age of AI Coding Assistants](https://arxiv.org/html/2602.00180). SPDD, по текущим источникам, ближе к гибридному режиму: REASONS Canvas is a контракт дизайна / источник истины for intent, but code review, prompt-update и sync allow controlled feedback from code и review back into the contract. Это сильнее, чем обычный “write a better prompt”, но мягче, чем pure generated-code regime.

### Уточнение статуса SPDD

SPDD нужно описывать как метод командной доставки, а не как набор хороших prompt-шаблонов. В источнике это прямо задаётся сдвигом от индивидуального ускорения к системному throughput: AI ускоряет отдельного разработчика, но системная скорость упирается в ambiguous requirements, review load, inconsistency, integration/testing issues и production risk. Поэтому SPDD формулируется как способ сделать AI-generated changes governable, reviewable и reusable, а не как способ «генерировать больше кода» ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)). Это подтверждает текущую теоретическую трактовку: SPDD — не prompt trick, а слой управления намерением в AI-driven SDLC.

В источнике также явно сказано, что SPDD относится к spec-anchored подходам: prompt/spec сохраняется как живой якорь рядом с кодом, но не превращается в единственный источник истины. Это важно для будущей теории: SPDD не отменяет код, тесты и runtime evidence; он делает намерение inspectable и reusable до, во время и после генерации ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/), [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

### Роль в AI-driven SDLC

SPDD полезен прежде всего как team-level метод, а не как личный prompt trick. В текущей теории подчёркнуто ограничение индивидуального AI-ускорения: один разработчик может быстрее набрасывать и менять код, но системная скорость упирается в ambiguous requirements, рост review load, inconsistency, integration/testing issues и production risk. SPDD отвечает не на вопрос «как сгенерировать больше кода», а на вопрос «как сделать AI-generated changes governable, reviewable и reusable». Источник в корпусе: [§11](../../content/Theoretical_synthesis.md#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli), внешний источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

В отношении к обычному spec-driven development SPDD занимает промежуточную позицию. Он начинается в той же точке, что и [spec-driven development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html): сначала формулируется спецификация, затем модель помогает получить код. Но существенная часть SPDD не в факте `spec before code`, а в способе производства, проверки и сопровождения спецификации. Корпусный раздел [«Что SPDD добавляет к SDD и почему это не просто spec-first»](../../content/Theoretical_synthesis.md#spdd-adds-to-sdd) связывает это с Thoughtworks-классификацией **spec-first**, **spec-anchored** и **spec-as-source** из [Understanding Spec-Driven-Development: Kiro, spec-kit, и Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).

Текущая теория помещает SPDD ближе всего к **spec-anchored**: prompt/spec сохраняется после первой реализации и становится якорем дальнейшей эволюции, но не объявляется единственным источником правды. Это важное различение для всего сайта: doc-first не должен превращаться в «документ вместо системы». Хороший intent artifact связан с кодом, тестами, runtime evidence и человеческим решением, но не заменяет их. Корпусный фрагмент: [§12](../../content/Theoretical_synthesis.md#spdd-adds-to-sdd).

### Проблема, которую решает SPDD

Основная проблема — не медленная генерация кода, а потеря и дрейф намерения после генерации. Когда agent-produced code появляется быстро, review и maintenance начинают страдать не только от ошибок кода, но и от того, что человеку приходится заново восстанавливать смысл результата из `diff`. Текущая теория связывает SPDD с историями [Boris Tane](../../content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md), [Jesse Vincent](../../content/stories/06_jesse_vincent_agentic_рабочий процесс_reconstruction_connected.md) и [Mark Erikson](../../content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md): `research.md`, `plan.md`, переносимый план и внешняя рабочая память делают понимание видимым до кода. SPDD идёт дальше: если артефакт намерения действительно важен, его нужно сопровождать после кода. Корпусный фрагмент: [§11](../../content/Theoretical_synthesis.md#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli).

Вторая проблема — человеческая нагрузка на подтверждение. В SPDD рабочий процесс шагов шесть не ради ceremony. В Q&A, как это пересказано в текущей теории, авторы объясняют: если подтверждать intent одним большим review после plan generation, cognitive load слишком высока; люди skim, откладывают, одобряют по умолчанию, и drift становится почти неизбежным даже в аккуратно выглядящем документе. SPDD дробит подтверждение намерения на маленькие решения, которые человек ещё способен реально прочитать. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс), внешний источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

Третья проблема — отсутствие целостной traceability между business intent, prompt/spec, code, review evidence и tests. SPDD требует asset integrity: код, попадающий в commit, должен cleanly map to the exact prompt version. Иначе future maintainer видит prompt и code, но не знает, какая версия намерения породила какую реализацию и где начался drift. Корпусный фрагмент: [§22](../../content/Theoretical_synthesis.md#spdd-asset-integrity), внешний источник для core skill: [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html).

### Что SPDD добавляет к обычному SDD

В текущей теории выделены четыре добавления SPDD к обычному SDD. Их важно сохранить как структуру, потому что они объясняют, почему SPDD не сводится к «spec-first».

1. **Maintained artifact.** Structured prompt не создаётся один раз и не выбрасывается после генерации. Он проходит рабочий процесс, живёт в version control, может ревьюиться, переиспользоваться и улучшаться. Корпусный фрагмент: [§12](../../content/Theoretical_synthesis.md#spdd-adds-to-sdd), основной источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).
2. **Переход от requirements к engineering spec.** [REASONS Canvas](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance) фиксирует не только то, что система должна делать, но и chosen approach, system structure, engineering norms и safeguards. Модель получает implementation boundary, а не только цель. Корпусный фрагмент: [§12](../../content/Theoretical_synthesis.md#spdd-adds-to-sdd).
3. **Sync, not handoff.** Prompt и code не должны расходиться молча. Если меняется business rule, сначала меняется prompt. Если код меняется без изменения поведения, prompt синхронизируется обратно. Следующая итерация стартует от актуального intent asset, а не от исторического документа. Корпусный фрагмент: [§20](../../content/Theoretical_synthesis.md#spdd-prompt-update-sync).
4. **Repeatable team control.** Цель не в том, чтобы каждый раз писать более длинную спецификацию, а в том, чтобы команда могла повторяемо управлять AI output: смотреть на один и тот же тип артефакта, проверять похожие места, переносить доменное знание между итерациями и снижать variance между разработчиками. Корпусный фрагмент: [§12](../../content/Theoretical_synthesis.md#spdd-adds-to-sdd).


## Артефактный слой: REASONS Canvas и контракты намерения

### `/spdd-prompt-update`: минимальный patch к контракту, а не перегенерация всего Canvas

Шаблон `/spdd-prompt-update` полезен как operational guardrail. Он требует путь к prompt-файлу и update instructions, читает весь existing prompt, определяет затронутые REASONS-секции, но дальше действует по minimal-change principle: не переписывать всё, не трогать unaffected sections, не ломать cross-section consistency, не оставлять placeholders, не переименовывать файл. Особенно важна граница “specification vs implementation”: prompt-файл описывает contracts, behaviors и constraints, но не должен содержать implementation code blocks. [OpenSPDD `/spdd-prompt-update`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md)

Для теории это важное уточнение: SPDD не просто “сначала spec, потом code”. Он вводит **small controlled update protocol** для живого контракт дизайна. Это снижает риск, что каждое изменение требований запускает полный redesign документа. Но одновременно появляется новая дисциплина: человек должен уметь различать behavioral change, architectural change, constraint update, bug fix in specification и pure refactor.

### REASONS Canvas как contract of ingestion, а не только форма результата

В предыдущих версиях досье REASONS Canvas уже был описан как intent/design/execution artifact. Четвёртый проход добавляет более низкий и важный слой: `/spdd-reasons-canvas` — это ещё и **контракт на поглощение исходного контекста**. Шаблон команды допускает ввод как plain text, так и `@file` / `@folder` references; если есть `@`-ссылки, агент должен прочитать все указанные файлы полностью, для папок — все релевантные `.md`, `.txt`, `.yaml`, `.json` и similar files, объединить все источники в единый business context, сохранить полную информацию и explicitly avoid summarization/truncation before building the Canvas ([`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md)).

Это меняет интерпретацию SPDD. Canvas не просто «лучше сформулированный prompt». Он начинается раньше: с требования, чтобы агент **не перескочил через входной материал**. Это важная защитная механика против типичного AI failure mode: модель быстро строит правдоподобный дизайн на неполном чтении требования. В терминах нашей теории SPDD создаёт не только intent artifact, но и context-ingestion gate.

Однако этот же слой создаёт риск для стоимости. Если `@folder` читается буквально, SPDD может легко столкнуться с тем же, с чем столкнулась наш многопроходный документный процесс: формально правильное чтение “всего релевантного” превращается в token blow-up. Поэтому для будущей теории нужна двойная формулировка: SPDD требует высокого context integrity, но без slicing/indexing стратегия чтения может стать слишком дорогой.

### `/spdd-generate`: Operations как designed execution order

Шаблон `/spdd-generate` усиливает отличия SPDD от обычного plan-driven generation. Он требует прочитать structured prompt целиком, извлечь все семь секций REASONS и treat `Operations` as the concrete sequence of implementation tasks. Команда отдельно задаёт, что code generation must follow the Operations sequence и coding norms from the prompt; before generation it should identify the project’s stack, locate similar patterns, package structure, base classes и utilities, и align generated code with existing conventions ([`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md)).

Эта деталь делает SPDD более жёстким, чем “model follows spec”. `Operations` — не список пожеланий, а designed execution order. Это защищает от agent improvisation, but also creates a new failure mode: если Operations were poorly decomposed, the model is now intentionally constrained by a bad sequence. Значит, сильный SPDD-process должен вкладывать серьёзное внимание не только в Requirements/Approach, но и в Operations as dependency-ordered work plan.

### SPDD vs repo-level instruction files

Design philosophy уточняет важную границу, которую нельзя потерять: structured prompts are not a fixed format, и OpenSPDD does not claim to replace all other instruction artifacts. Документ прямо сравнивает Kiro requirements/design/tasks, Claude `CLAUDE.md`, Codex `AGENTS.md` и ADR-like practices as addressing the same broad problem from different angles ([OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md)).

Ключевое различение: `CLAUDE.md` / `AGENTS.md` usually carry уровня репозитория conventions — how this project does things; REASONS Canvas is уровня фичи — how this specific feature is designed. Это нужно перенести в будущую теорию: SPDD не конкурирует напрямую с AGENTS.md. Он закрывает более узкий и более дорогой слой: уровня фичи intent, decisions, operations и safeguards.

### REASONS Canvas: семь частей и уровень детализации

Раскрытие источников уточняет, что REASONS Canvas в статье делится на три смысловых слоя: intent/design, execution и governance. Семь частей: `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards`. Важная деталь: `Operations` — не просто список задач, а переход от strategy к concrete, testable implementation steps; `Norms` и `Safeguards` формируют не общий стиль, а governance-слой с повторяемыми стандартами и non-negotiable boundaries ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)).

Репозиторий OpenSPDD подтверждает это операционно: `/spdd-reasons-canvas` должен сгенерировать implementation-ready structured prompt с секциями `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards` и сохранить его в `spdd/prompt/<file-name>.md` ([spdd-reasons-canvas.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md)). Это усиливает мысль досье: Canvas — не пояснительный документ после решения, а исполняемый контракт для следующего шага.

### REASONS Canvas: intent, design, execution, governance

REASONS Canvas — центральный structured prompt artifact. В текущей теории он описан не как длинный документ ради документа, а как структура, которая удерживает intent, design, execution и governance до генерации кода. Источник в корпусе: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance), внешний источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/), команда: [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md).

- **Requirements** фиксируют проблему, Definition of Done, acceptance criteria и scope. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Entities** вытаскивают доменные сущности, связи и ключевой vocabulary. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Approach** описывает стратегию решения, trade-offs и выбранные паттерны. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Structure** указывает, где изменение должно лечь в систему: components, dependencies, layers, responsibilities, integration points. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Operations** переводят абстракцию в исполнимые шаги. В SPDD это не TODO-list: Operations должны быть concrete, testable, atomic и acceptance-ready. В Q&A, как пересказано в теории, авторы говорят, что Operations может доходить до method signatures и execution order, чтобы reviewers проверили шаги до генерации кода. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Norms** фиксируют повторяемые инженерные нормы: naming, observability, defensive coding, error handling, layering, logging, team conventions. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).
- **Safeguards** задают non-negotiable boundaries: инварианты, performance limits, security rules, compatibility constraints, запреты на изменение внешнего поведения. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).

Сила Canvas в том, что он делает намерение обозримым до `diff`. Человек может проверить не только «что модель собирается сделать», но и «на каком уровне абстракции она поняла задачу». Если `Requirements` выражают не тот продуктовый смысл, если `Entities` пропускают важный доменный объект, если `Approach` выбирает плохую архитектурную линию, если `Operations` разрезают работу по слоям вместо проверяемых вертикальных срезов, это нужно увидеть до генерации кода. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).

Canvas при этом не является внешним оракулом истины. Хороший Canvas требует человека, который понимает домен, архитектуру и цену ошибки. Иначе structured prompt может быть просто длинным и уверенным документом, красиво формализующим неверное намерение. Корпусный фрагмент: [§16](../../content/Theoretical_synthesis.md#spdd-reasons-canvas-intent-design-execution-governance).

### Asset integrity

Asset integrity — отдельный пункт из [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html), который текущая теория считает легко недооценить. Код, попадающий в commit, должен cleanly map to the exact prompt version. Иначе теряется traceability: future maintainer видит prompt, видит code, но не знает, какая версия намерения породила какую версию реализации и где начался drift. Корпусный фрагмент: [§22](../../content/Theoretical_synthesis.md#spdd-asset-integrity).

Asset integrity превращает SPDD из «хорошо написанной спецификации» в governance mechanism. Если prompt изменился, но код не обновлён, artifact врёт. Если код refactored, но prompt не synced, artifact превращается в historical record. Если code review принял business correction без prompt-update, future evolution стартует от устаревшего intent. Поэтому SPDD требует, чтобы prompt, code, review evidence и tests сохраняли связность во времени. Корпусный фрагмент: [§22](../../content/Theoretical_synthesis.md#spdd-asset-integrity).

Практические требования asset integrity в текущей теории:

- Prompt assets должны лежать в version control рядом с codebase, а не в chat history.
- Изменения бизнес-логики должны попадать в prompt before code.
- Refactoring без изменения поведения должен возвращаться в prompt через [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md).
- Code review должен проверять not only code quality, but also prompt/code consistency.
- Следующая итерация должна начинаться от accumulated prompt assets: domain model, decisions, norms, safeguards, accepted patterns.

Корпусный фрагмент: [§22](../../content/Theoretical_synthesis.md#spdd-asset-integrity).



### `/spdd-reverse`: подключение legacy-кода к SPDD

`/spdd-reverse` в предыдущей версии досье был упомянут слишком осторожно и слишком кратко. Шаблон команды показывает, что это не просто “обратное документирование”, а отдельный вход в жизненный цикл SPDD для кода, который уже существует без REASONS Canvas. Команда принимает ссылки на файлы или папки через `@`, текстовое описание области или смешанный ввод; если область не задана, она должна остановиться и спросить пользователя, какой код нужно кодифицировать. Для папок команда требует прочитать исходные файлы, а при слишком большой области — примерно больше пятнадцати файлов — показать список и попросить сузить или подтвердить охват. Это важная граница: SPDD не должен самовольно превращать весь репозиторий в “спецификацию”, если пользователь не подтвердил масштаб. [OpenSPDD `/spdd-reverse`](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md)

Внутри `/spdd-reverse` есть полный набор операций обратной кодификации: структурный анализ файлов, извлечение сущностей, описание поведения, карта зависимостей, обнаружение конвенций и ограничений. Затем команда собирает REASONS Canvas: `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards`. Принципиальная оговорка источника — описывать код как он есть, включая неудачные паттерны и расхождения, а не подменять обратную спецификацию скрытым рефакторингом. Operations должны быть достаточно подробными, чтобы `/spdd-generate` мог воспроизвести текущее поведение, но без вставки реализационного кода в Canvas. [OpenSPDD `/spdd-reverse`](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md)

Для будущей теории это добавляет отдельную ветку SPDD: методология работает не только в направлении “новое намерение → код”, но и в направлении “существующий код → артефакт намерения”. Это полезно для brownfield-проектов, где нельзя начать с чистой спецификации. Но эта ветка несёт отдельный риск: если команда неверно прочитает legacy-код, она создаст убедительный Canvas, который будет выглядеть как намерение системы, хотя на самом деле является реконструкцией поведения и частичной интерпретацией. Поэтому `/spdd-reverse` должен оставаться подконтрольным человеческому шлюзу: пользователь подтверждает область, а затем проверяет, что Canvas не идеализирует и не переписывает фактическое поведение.

## Жизненный цикл и командная поверхность OpenSPDD

### Optional commands как показатель зрелости метода, но не как core requirement

README OpenSPDD фиксирует optional beta commands: `spdd-story`, `spdd-code-review`, `spdd-api-test`, `spdd-reverse`. Это расширяет рамку метода: SPDD постепенно покрывает не только forward generation, но также декомпозицию историй, ревью, поведенческие свидетельства API и подключение legacy-кода. Но важно не сделать из этого перегруз: optional commands не установлены по умолчанию и должны использоваться выборочно. [OpenSPDD README](https://github.com/gszhangwei/open-spdd)

`spdd-reverse` особенно важен как возможный путь в brownfield: существующий код можно обратить в REASONS Canvas. Но пока это только необязательная beta-команда в README, поэтому в теории лучше упоминать его осторожно: перспективный путь подключения старого кода, а не уже доказанная зрелая опора. [OpenSPDD README](https://github.com/gszhangwei/open-spdd)

### Implementation-ready output как человеческий шлюз

Команда `/spdd-reasons-canvas` не должна возвращать framework metadata, timestamps, placeholders or TODOs; она должна выдать только полностью заполненный structured content, with all seven REASONS sections и clear executable Operations. После этого файл сохраняется в `spdd/prompt/<derived-name>.md` и предлагается подтвердить, переходить ли к implementation phase ([`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md)).

Это важно для рамки качества. SPDD не должен быть описан как “генерируем красивую спецификацию и сразу кодим”. Core move другой: создаётся **reviewable artifact before implementation**. Human gate встроен не обязательно как формальная кнопка approval, но как структурный момент: сначала появляется файл, который можно прочитать, отредактировать, закоммитить, сравнить, сослаться на него; затем уже можно запускать генерацию.

### Tool-adapter слой: SPDD уже не только `.claude/commands/`

Текущая версия OpenSPDD важна для досье тем, что явно показывает переносимость метода между поверхностями инструментов. README перечисляет разные целевые среды: Cursor, Claude Code, Antigravity, GitHub Copilot, OpenCode и Codex; для GitHub Copilot команды кладутся в `.github/copilot-prompts/`, а для Codex генерируются не плоские command files, а project-scoped skill bundles under `.agents/skills/<id>/SKILL.md` ([OpenSPDD README](https://github.com/gszhangwei/open-spdd/blob/main/README.md)). Это меняет формулировку для теории: SPDD — не «набор slash-команд Claude», а portable discipline, которая проецируется на разные агентские surfaces.

Особенно важна Codex-деталь: README говорит, что generated skills for Codex are configured for explicit-only invocation by default, with `allow_implicit_invocation: false`, и notes trust-model issues where skills from untrusted projects may be ignored until the project is trusted/restarted ([OpenSPDD README](https://github.com/gszhangwei/open-spdd/blob/main/README.md)). Для нашей теории это полезный маленький факт: intent-artifacts недостаточно положить в репозиторий; инструментальная поверхность, граница доверия и политика вызова решают whether the agent will actually see/use them.

### Optional commands шире, чем прошлое досье фиксировало

Предыдущие проходы уже раскрыли `/spdd-story`, `/spdd-api-test` и `/spdd-code-review`. Третий проход добавляет, что OpenSPDD README также перечисляет optional `/spdd-reverse`: reverse-engineer existing code into a REASONS-Canvas prompt for подключение legacy-кода ([OpenSPDD README](https://github.com/gszhangwei/open-spdd/blob/main/README.md)). Это важно не как новый центральный рабочий процесс, а как сигнал: SPDD может идти не только requirement → code, но и кодовая база → артефакт намерения. Для теории это мост к brownfield / подключению legacy-кода и практикам обратной спецификации.

Практический WebReactiva-разбор подтверждает installation path и expected file layout: `openspdd init`, `openspdd generate --all`, затем появляются `requirements/`, `spdd/analysis/`, `spdd/prompt/`, `scripts/test-api.sh` и `src/`; optional commands are installed explicitly (`spdd-story`, `spdd-api-test`, `spdd-code-review`) ([WebReactiva](https://www.webreactiva.com/blog/spdd)). Это secondary source, но он хорошо показывает, как метод выглядит для обычного пользователя, не только для автора статьи.

### Команды OpenSPDD как рабочий процесс, а не просто CLI

OpenSPDD README даёт компактную последовательность: `openspdd init`, `openspdd generate --all`, затем `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-sync`; для простых features можно пропустить `/spdd-analysis` и передать требования прямо в `/spdd-reasons-canvas` ([OpenSPDD](https://github.com/gszhangwei/open-spdd)). Это уточняет, что шесть стадий из статьи и четыре-шаговый quick-start в CLI не противоречат друг другу: статья раскрывает полный метод, README показывает минимальный operational path.

Команда `/spdd-analysis` особенно важна для нашего corpus, потому что она запрещает наивное «прочитай весь codebase». В шаблоне требуется concept-driven exploration: сначала lightweight project fingerprint, затем извлечение domain nouns/action verbs/API surfaces/technical hints из требования, потом scoped schema/code exploration и one-hop expansion. Это почти прямой аналог будущего принципа «модель читает не всё, а релевантную область» для нашего многопроходного документного процесса ([spdd-analysis.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md)).

`/spdd-generate` требует прочитать весь prompt-файл и извлечь все секции REASONS Canvas; затем перед генерацией проверить tech stack, похожие паттерны, package structure и reusable utilities. Эта деталь важна: кодогенерация не должна идти только от Canvas, оторванного от проекта; Canvas задаёт намерение, но реализация должна align with existing project conventions ([spdd-generate.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md)).

`/spdd-prompt-update` и `/spdd-sync` образуют две стороны синхронизации. Первый обновляет prompt при новых требованиях или архитектурных изменениях, сохраняя структуру REASONS Canvas; второй закрывает reverse flow — code → design — через анализ изменений, comparison, plan updates и prompt update ([spdd-prompt-update.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md), [spdd-sync.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md)). Поэтому в теории лучше говорить не просто «prompt и code синхронизируются», а «SPDD вводит два разных канала синхронизации: requirements/architecture → prompt → code и code/refactoring → prompt».

### Рабочий процесс: шесть стадий распределённого подтверждения

Полная последовательность SPDD в текущей теории дана как шесть стадий. Эта структура должна быть сохранена без упрощения, потому что именно она показывает distributed confirmation of intent. Корпусный раздел: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс), основной источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/), command templates: [OpenSPDD](https://github.com/gszhangwei/open-spdd).

1. **Create initial requirements.** Raw idea или enhancement превращается в user story. Опциональная команда [`/spdd-story`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) разбивает крупное требование на INVEST-like stories размером примерно 1–5 дней и добавляет business-language acceptance criteria. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).
2. **Review и clarify the story.** Человек подтверждает, что story действительно выражает нужный business intent. В walkthrough две generated stories объединяются в simplified story с `Background`, `Business Value`, `Scope In`, `Scope Out` и `Acceptance Criteria`. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).
3. **Generate analysis context.** [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) извлекает domain keywords, сканирует релевантную часть codebase, выделяет existing/new concepts, business rules, strategic approach, risks и gaps. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).
4. **Generate и review REASONS Canvas.** [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) превращает analysis context в structured prompt: `Requirements`, `Entities`, `Approach`, `Structure`, `Operations`, `Norms`, `Safeguards`. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).
5. **Generate code, validate behavior и review.** [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) строит код по `Operations`; затем [`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) проверяет system boundary; review делит изменения на logic corrections и refactorings. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).
6. **Generate unit tests.** После стабилизации реализации создаётся отдельный testing prompt, сценарии дедуплицируются против существующего test suite, затем генерируются unit tests как regression safety net. Корпусный фрагмент: [§13](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).

Смысл последовательности не в церемонии. Каждый шаг сужает вопрос для человека: на story-уровне проверяется правильная business problem; на analysis-уровне — domain understanding и risks; на Canvas-уровне — design, boundaries и executable operations; на code-generation/validation уровне — соответствие поведения intended business behavior; на review уровне — architecture, maintainability и prompt/code consistency; на unit-test уровне — future regression protection. Корпусный фрагмент: [§13–22](../../content/Theoretical_synthesis.md#spdd-six-step-рабочий процесс).

### Три core skills: Abstraction First, Alignment, Iterative Review

Текущая теория подчёркивает, что три core skills SPDD — не side notes, а модель того, куда смещается ценность разработчика в AI-assisted delivery. Корпусный фрагмент: [§17](../../content/Theoretical_synthesis.md#spdd-three-core-skills), внешние источники: [Abstraction First](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html), [Alignment](https://martinfowler.com/articles/structured-prompt-driven/alignment.html), [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html).

**Abstraction First** означает design before generation. До кода нужно понять, какие objects существуют, как они взаимодействуют, где проходят boundaries, какие interface responsibilities фиксируются contract-first, какой уровень granularity допустим. В операционных принципах skill есть четыре ключа: design before generation, contract first, control granularity, diagram early. Смысл не в любви к диаграммам, а в том, что narrative requirements слишком легко допускают разные интерпретации; lightweight diagrams, ER diagrams, sequence diagrams или flow charts помогают быстро зафиксировать logic model. Корпусный фрагмент: [§17](../../content/Theoretical_synthesis.md#spdd-three-core-skills), источник: [Abstraction First](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html).

**Alignment** означает lock intent before code. Здесь проверяется domain language, scope, acceptance criteria, dependencies и hidden constraints. Уточняются термины вроде `customer`, `order`, `asset`; устраняются случаи `same word, different meaning` и `same meaning, different words`; happy path, edge cases и Definition of Done становятся testable. Главный operating principle: analysis doc → structured prompt → code. Если ранний артефакт не aligned, нельзя продвигаться дальше. Корпусный фрагмент: [§17](../../content/Theoretical_synthesis.md#spdd-three-core-skills), источник: [Alignment](https://martinfowler.com/articles/structured-prompt-driven/alignment.html).

**Iterative Review** означает turn output into a controlled loop. Агентская работа не должна быть one-shot draft и не должна превращаться в бесконечные patch requests, где решение постепенно drifts. Review loop проверяет prompt/code consistency, architecture и responsibility boundaries, hallucination и correctness. Здесь появляются признаки зрелого процесса: prompt debugging, functional validation, deep code review и asset integrity. Корпусный фрагмент: [§17](../../content/Theoretical_synthesis.md#spdd-three-core-skills), источник: [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html).

Эти skills важны как сопротивление поверхностному «AI пишет код». SPDD требует от разработчика больше работы на уровне абстракции: моделировать домен, принимать architectural trade-offs, проектировать atomic tasks, задавать testable acceptance criteria, различать business mismatch и code smell. Корпусный фрагмент: [§17](../../content/Theoretical_synthesis.md#spdd-three-core-skills).

### Generate code: реализация locked intent

Только после story, analysis и Canvas SPDD переходит к [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md). Команда читает REASONS Canvas и генерирует код task by task, следуя порядку `Operations`; она должна придерживаться `Norms` и `Safeguards`: no improvisation, no features beyond the spec. В источнике это сформулировано как соответствие один-к-одному: prompt captures the intent, code implements that intent. Корпусный фрагмент: [§18](../../content/Theoretical_synthesis.md#spdd-generate-locked-intent).

Это меняет роль генерации. Модель не должна заново решать, что строить. Она должна выполнить уже согласованный blueprint. Если она обнаруживает contradiction, missing dependency или невозможность выполнить Operations, правильный ход — вернуться к артефакту намерения, а не тихо выдумать обход. Корпусный фрагмент: [§18](../../content/Theoretical_synthesis.md#spdd-generate-locked-intent).

В billing example generated code включает product code, tests и reviews. Но review после генерации уже не должен начинаться с полного восстановления смысла из `diff`: смысл был вытащен раньше. Code review получает фокус: проверить, правильно ли реализация перевела locked intent в код, не нарушила ли responsibilities, не добавила ли лишнюю сложность, не галлюцинировала ли imports/dependencies/API. Корпусный фрагмент: [§18](../../content/Theoretical_synthesis.md#spdd-generate-locked-intent).


## Проверка, свидетельства и ревью соответствия намерению

### SPDD как планируемая фоновая проверка спецификаций

Файл `daily-spdd-spec-planner.md` в `github/gh-aw` показывает неожиданный режим использования SPDD. Он не просто говорит агенту “сделай фичу по Canvas”. Сначала рабочий процесс разрешает текущий `OPENSPDD_REF`, скачивает четыре OpenSPDD-команды в `.github/copilot-prompts`, затем запускает ежедневного planner-а, который должен идти по стадиям `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-sync`. Область проверки задана файлово: `specs/**/*.md`, `docs/src/content/docs/reference/*specification*.md`, `scratchpad/*specification*.md`. Для равномерности используется `rotation cache`, проход ограничен пятью файлами спецификаций, а перед записью рабочий процесс обязан выполнить `write preflight` и не переинициализировать повреждённое состояние rotation cache.[^spdd-gh-aw]

Это важное расширение досье. SPDD может быть не только интерактивным порядком работы над одной фичей, но и периодическим сопровождением корпуса спецификаций. В таком режиме REASONS Canvas и команды OpenSPDD становятся материалом для планировщика, который ищет слабые места спецификаций и создаёт issue с конкретными действиями. Для будущей теории это полезно: SPDD начинает пересекаться с темой агентного сопровождения документации, а не только с генерацией кода.

[^spdd-gh-aw]: GitHub `gh-aw`, [`daily-spdd-spec-planner.md`](https://github.com/github/gh-aw/blob/main/.github/workflows/daily-spdd-spec-planner.md), особенно блоки загрузки команд OpenSPDD, стадий planner-а, области `specs/**/*.md` и rotation cache.


### Результат daily planner как проверяемый артефакт, а не только определение процесса

`github/gh-aw` даёт не только файл рабочего процесса, но и пример результата такого рабочего процесса. Issue `[spdd] Daily spec work plan - 2026-05-07` показывает, как ежедневный SPDD-планировщик проходит по пяти спецификационным файлам, фиксирует `rotation index`, группирует проблемы в очередь P0/P1/P2 и раскладывает рабочие пункты по категориям SPDD: Analysis, Norms, Safeguards, Sync. Это важно для досье, потому что источник показывает не абстрактное обещание, а форму артефакта, которую получает человек: список конкретных правок к спецификациям, привязанный к файлам и условия готовности.[^spdd-gh-aw-issue]

Для будущей теории это полезнее, чем ещё один пересказ схемы `analysis → Canvas → generate → sync`. Здесь видно, как SPDD может работать как плановый аудит корпуса документов: агент не пишет код, а проверяет слабые места спецификаций, предлагает следующую очередь работы и оставляет человеку задачу для ревью. Это также уточняет границу метода. Если результатом становится issue, то качество SPDD зависит от того, насколько хорошо issue сохраняет источник рассуждения: какие файлы были прочитаны, какие разделы признаны слабым местом, какие условия готовности проверяемы, и не потерялась ли связь с исходным Canvas.

[^spdd-gh-aw-issue]: GitHub issue `github/gh-aw#30864`, [`[spdd] Daily spec work plan - 2026-05-07`](https://github.com/github/gh-aw/issues/30864), показывает reviewed files, rotation index, priority work queue и SPDD checklist по Analysis / Norms / Safeguards / Sync.

### `/spdd-api-test`: поведенческое свидетельство как артефакт для ревью

`/spdd-api-test` оказался важнее, чем просто “сгенерировать curl script”. Его template определяет отдельный **удобный для человеческой проверки evidence artifact**: self-contained `scripts/test-api.sh`, structured test-case tables at script top, result tables after execution, direct `curl` calls, no `eval` wrapper, explicit timeout и expected-vs-actual status recording. Input может быть `@file`, `@folder`, acceptance criteria, API specification or direct text; при `@` references template требует читать referenced API files completely, extract endpoints, schemas, acceptance criteria, validation rules, error scenarios и seed data. Это делает API-test layer не только smoke-test, а проверяемым мостом between REASONS Canvas / acceptance criteria и runtime behavior. Источник: [OpenSPDD `/spdd-api-test` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md); same artifact is also summarized in the Fowler/Thoughtworks article as extracting endpoint information и generating a cURL-based script with normal, boundary и error scenarios plus expected-vs-actual output: [Fowler SPDD article](https://martinfowler.com/articles/structured-prompt-driven/).

Практический смысл для теории: SPDD не должен описываться как “structured prompt before coding” only. В сильной версии он создает цепочку **intent artifact → generated code → поведенческое свидетельство artifact → review/sync decision**. Именно этот слой отличает SPDD от простого upfront prompt-writing: после генерации остается внешнее свидетельство, которое человек может быстро проверять.

### `/spdd-code-review`: проверка faithful implementation, а не обычный lint-review

Команда `/spdd-code-review` описана не как generic code review, а как review AI-generated code against REASONS Canvas: detect intent drift, safeguard violations и scope creep before merge ([`/spdd-code-review`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-code-review.md)). Она поддерживает несколько режимов входа: review structured prompt + changed files/folders, review git diff against structured prompt, и prompt-only review when implementation files are not available.

Главная деталь для нашей теории: команда требует читать all referenced files fully, including the structured prompt и code files. Если кодовая область не указана, agent должен infer scope из Operations section; если контекст неполный, он обязан запросить недостающие файлы before proceeding. Это делает review не “комментариями по стилю”, а попыткой построить explicit traceability между Canvas и implementation.

Шаблон review разворачивает REASONS по секциям:

- **Requirement** — implemented behavior must match user needs и acceptance conditions, without introducing unrelated features.
- **Effect** — user-visible outcomes и side effects must correspond to the intended result.
- **Architecture** — implementation should preserve the architectural direction chosen in Canvas.
- **Safeguards** — validation, error handling, auth, limits и protected flows should be checked against stated safeguards.
- **Operations** — the implementation should follow the planned operation sequence, not silently skip or invent steps.
- **Norms** — naming, structure, testing conventions и coding norms should follow the prompt и project conventions.
- **Scope** — implementation must avoid unrelated expansion.

Это важный переносимый механизм: review report становится **semantic diff**, not just a code diff. Он отвечает на вопрос: “код соответствует намерению, которое мы перед этим сделали ревьюируемым?”

### Intent drift: положительный, отрицательный и directional drift

В шаблоне `/spdd-code-review` отдельно выделен intent drift. Это полезно не только для SPDD, но и для общей теории агентной разработки: агент может не просто ошибиться в коде, а сместить meaning of the change. Drift делится как минимум на три типа:

- **positive drift** — код добавляет полезное поведение, но это поведение не было явно согласовано в Canvas;
- **negative drift** — код теряет or weakens часть intent artifact;
- **directional drift** — код уходит в другой product/architecture direction while still looking locally reasonable.

Поэтому SPDD-review нельзя свести к “tests passed”. Tests may pass while intent has drifted. Этот слой особенно важен для будущей главы о verification/harness: harness проверяет not only executable behavior, but also alignment between artifacts.

### Implicit decisions и scope boundary

`/spdd-code-review` требует искать implicit decisions: choices that were made in code but not captured in the prompt. Это ключевой момент. Агентная разработка часто производит незаметные локальные решения: naming, data shape, API behavior, default values, error semantics, retry behavior, permission boundary. Каждое такое решение может быть harmless, but collectively they move the design center.

SPDD решает это не запретом на локальные решения, а **making implicit decisions reviewable**. Если решение полезно, оно должно вернуться в prompt through `/spdd-prompt-update` or `/spdd-sync`; если решение случайно, его нужно откатить or align with the Canvas.

### `/spdd-api-test`: удобный для человеческой проверки behavioral evidence

Команда `/spdd-api-test` добавляет другой тип свидетельства. Она генерирует self-contained shell script, usually `scripts/test-api.sh`, with cURL commands for manual or automated endpoint testing; also produces structured test case tables with endpoint, method, input, expected output и failure cases ([`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-api-test.md)).

Шаблон требует читать all referenced API specs, controllers, routes, DTOs, validation rules и README/test files; then identify endpoints, HTTP methods, auth requirements, request/response schemas, business rules, validation и error cases. Это делает API tests промежуточным артефактом между full automated test suite и manual QA. Пользователь может открыть таблицу и generated script и understand what behavior is being checked.

Это важно для SPDD как глубокий якорь: SPDD does not rely only on prose conformance. It produces artifacts that can be run, inspected и adjusted. Даже если API-test script is not final production test suite, он даёт cheap поведенческое свидетельство и creates a review surface for “does the implementation behave as the prompt promised?”

### Конкретные examples: token billing scenario

Fowler/Thoughtworks walkthrough даёт конкретный пример на token billing: when adding billing support, missing `modelId`, unknown customer, negative token counts, Standard plan quota/overage, Premium plan split prompt/completion rates и response format become test scenarios. These examples are useful because they show what SPDD looks like below abstract method level: the Canvas produces concrete billing rules; `/spdd-generate` implements them; generated API tests exercise normal и edge behavior; review checks whether implementation drifts from the billing intent ([Fowler/Thoughtworks SPDD](https://martinfowler.com/articles/structured-prompt-driven/)).

Для будущей теории это лучше, чем общий тезис “SPDD improves alignment”. Нужно показывать, как intent becomes executable evidence: billing rules → code paths → API test table/script → review report.

### Проверка faithful implementation: не “работает ли код”, а “соответствует ли intent artifact”

В статье Fowler/Thoughtworks core command table `/spdd-generate` описан как command that reads the Canvas и generates code task by task, strictly following operations, norms и safeguards; в разделе о review фокус формулируется как strict adherence to expected architecture, alignment with initial intent и avoidance of unrelated scope creep ([Fowler/Thoughtworks SPDD](https://martinfowler.com/articles/structured-prompt-driven/)). Для нашей теории это нужно вынести явно: SPDD меняет критерий проверки. Код недостаточно запустить; нужно спросить, **соответствует ли он intent artifact one-to-one**.

Отсюда прямой мост к будущей главе о verification/harness: SPDD’s verification target is not only tests, but traceability between R/E/A/S/O/N/S и resulting code. API tests и code review are downstream checks; the first check is semantic conformance to the Canvas.

### Практический пример: billing engine

Статья Fowler/Thoughtworks раскрывает пример не как toy prompt, а как end-to-end enhancement существующей системы billing engine. Изменение включает добавление `modelId` в `POST /api/usage`, переход от single global rate к model-aware pricing, поддержку Standard и Premium plan с разными правилами quota / split prompt-completion billing, а также стратегию расширяемой архитектуры через Strategy/Factory-like separation ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)).

Этот пример полезен тем, что показывает правильный размер SPDD-задачи: это не микробаг и не огромная cross-domain программа, а feature/change с бизнес-правилами, архитектурной формой, тестируемыми acceptance criteria и future extensibility. Его стоит сохранить как anchor example для будущей главы.

### Проверяемые свидетельства: API tests до глубокого code review

Один из самых важных ходов SPDD для текущего сайта — порядок проверки. В Q&A авторы обсуждают, почему [`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) идёт до глубокого code review, а unit tests — позже. Логика отличается от TDD: generated code дешёв; нет смысла глубоко ревьюить код, который ещё не доказал соответствие intended business behavior. Поэтому first gate — поведение на system boundary. Корпусный фрагмент: [§19](../../content/Theoretical_synthesis.md#spdd-validation-review-evidence), внешний источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

[`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) извлекает API endpoint information из implementation или acceptance criteria и генерирует cURL-based test script. Скрипт содержит test-case table по normal scenarios, boundary conditions и error scenarios. При выполнении он выводит expected-vs-actual comparison results. Важна двойная форма свидетельства: сначала человек может прочитать `TEST CASE OVERVIEW`, затем увидеть фактический результат выполнения. Корпусный фрагмент: [§19](../../content/Theoretical_synthesis.md#spdd-validation-review-evidence).

После API validation code review фокусируется на том, что только человек или сильный review-agent может оценить: architecture, trade-offs, non-functional concerns, maintainability, layering, exception handling, encapsulation, magic numbers, long methods, imports/dependencies, syntax/compilation, hallucinated APIs, adherence to `Norms` и `Safeguards`. Базовое «what» должно быть уже проверено на boundary, иначе reviewer тратит внимание на код, который может не решать задачу. Корпусный фрагмент: [§19](../../content/Theoretical_synthesis.md#spdd-validation-review-evidence).

Текущая теория связывает это с общей темой проверяемых свидетельств: «готово» не является свидетельством. Свидетельство должно быть пригодно для следующего шага: test overview пригоден для human review, expected/actual results пригодны для acceptance decision, code review пригоден для maintainability judgement, unit tests пригодны для будущей regression protection. Корпусный фрагмент: [§19](../../content/Theoretical_synthesis.md#spdd-validation-review-evidence).

### Unit tests: последний safety net

Unit tests в SPDD не исчезают, но появляются после стабилизации implementation через structured prompt, API validation и review. Причина практическая: если unit tests написать слишком рано, их придётся переписывать после крупных review-driven changes. SPDD использует API tests для быстрого behavior gate, code review для architecture и maintainability, а unit tests — как final regression safety net for core logic. Корпусный фрагмент: [§21](../../content/Theoretical_synthesis.md#spdd-unit-tests-after-stabilization).

В walkthrough dedicated testing commands ещё не finalized. Поэтому используется interim template-driven approach. Сначала implementation details prompt комбинируется с testing template вроде [`TEST-SCENARIOS-TEMPLATE.md`](https://github.com/gszhangwei/token-billing/blob/after-enhancement/spdd/template/TEST-SCENARIOS-TEMPLATE.md), чтобы создать baseline test prompt. Затем AI-generated scenarios дедуплицируются и уточняются: агент должен сверить предложенные сценарии с existing test suite, убрать повторы и оставить genuinely new coverage. Только после этого генерируется unit-test code. Корпусный фрагмент: [§21](../../content/Theoretical_synthesis.md#spdd-unit-tests-after-stabilization).

Этот порядок не является анти-TDD. В Q&A авторы говорят, что SPDD сохраняет цели TDD — clarify behavior, protect regressions, shape design — но распределяет их иначе: behavior уточняется раньше через story, Canvas и API tests; design shape возникает через Abstraction First и Operations; regression protection закрепляется unit tests после стабилизации implementation. Корпусный фрагмент: [§21](../../content/Theoretical_synthesis.md#spdd-unit-tests-after-stabilization).


## Обновление, синхронизация и внешнее применение


### Трение context ingestion: вопрос о `reasons-context`

Issue `gszhangwei/open-spdd#9` даёт маленький, но важный сигнал о том, где метод начинает требовать более явного контракта источников. Пользователь спрашивает, почему команда `spdd-reasons-canvas` не читает предыдущий Canvas из папки `spdd` по умолчанию и выглядит так, будто читает только кодовую базу. Сам issue открыт с меткой `question / Further information is requested`, поэтому его нельзя использовать как доказательство поведения инструмента. Но как сигнал трения он полезен: если REASONS Canvas является design contract, пользователю нужно понимать, какие источники входят в новый Canvas — текущая формулировка требования, предыдущий Canvas, результаты анализа, кодовая база или их комбинация.[^spdd-issue-9]

Для досье это уточняет уже описанный риск stale Canvas. Проблема не только в том, что Canvas может устареть. Проблема ещё и в том, что на каждом обновлении нужно явно задавать source precedence. Если команда silently строит новый Canvas на неполном наборе источников, она может выглядеть формальной, но потерять часть намерения. Поэтому SPDD в рабочем процессе должен иметь маленький проверяемый preflight: какие входные файлы прочитаны, какой предыдущий prompt artifact учитывался, что взято из кода, а что остаётся предположением.

[^spdd-issue-9]: Issue `gszhangwei/open-spdd#9`, [How to capture all reasons-context via command `spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/issues/9), фиксирует вопрос о том, должен ли `spdd-reasons-canvas` читать предыдущий Canvas/context из `spdd` folder, а не только кодовую базу.

### Давление переносимости: Codex и OpenCode как запросы на adapter layer

Два открытых issue в OpenSPDD показывают не новую методологическую деталь, а направление практического давления. В issue `#6` пользователь просит добавить поддержку Codex, а в issue `#5` — поддержку OpenCode. Оба запроса короткие, поэтому их нельзя переоценивать. Но вместе с уже раскрытым `рабочий процесс `gh-aw` они подтверждают, что OpenSPDD постепенно читается не как набор команд для одной среды, а как переносимый слой: один и тот же порядок работы должен жить в Claude Code, Cursor, Codex, OpenCode, GitHub Copilot и других поверхностях.[^spdd-issue-6][^spdd-issue-5]

Для теории это усиливает различие между методом и adapter layer. Метод задаёт форму намерения и проверки: analysis, Canvas, generate, test, review, sync. Adapter layer отвечает за то, как эти команды попадают в конкретный агент: slash-команды, каталог prompts, Codex skill, Copilot prompt, локальная CLI-команда, workflow. Если смешать эти уровни, SPDD будет выглядеть более хрупким, чем он есть: смена инструмента тогда кажется сменой метода. Если разделить уровни, становится видно, что главный вопрос — не “поддерживает ли инструмент X slash-команды”, а “может ли инструмент X надёжно читать, обновлять и проверять intent artifacts”.

[^spdd-issue-6]: Issue `gszhangwei/open-spdd#6`, [OpenAi Codex support](https://github.com/gszhangwei/open-spdd/issues/6), открыт 8 May 2026 и просит добавить поддержку Codex.
[^spdd-issue-5]: Issue `gszhangwei/open-spdd#5`, [feat: OpenCode support](https://github.com/gszhangwei/open-spdd/issues/5), открыт 7 May 2026 и просит поддержку OpenCode.

### SPDD как возможность, которую хотят встроить в другие инструменты

Issue CodeMie полезен как маленький, но показательный сигнал. Автор просит интегрировать OpenSPDD в CLI, потому что хочет для крупных задач иметь контракт дизайна, трассируемость требований, автоматическую связь между дизайном и кодом и синхронизацию. Это не полноценный кейс внедрения и не доказательство качества метода. Но это показывает, какой именно слой люди распознают в SPDD как переносимый: не “хороший prompt”, а инструментальную дисциплину, которая связывает дизайн, код и обратную синхронизацию.[^spdd-codemie]

Для досье это добавляет осторожную формулировку: SPDD становится кандидатом на интеграционный примитив. Если инструментальная среда умеет скачивать и обновлять команды, хранить Canvas в репозитории, связывать его с задачами и проверками, то метод можно встроить в существующий рабочий процесс без ручного копирования шаблонов. Но это одновременно создаёт риск: если интеграция прячет Canvas от человека или превращает `/spdd-sync` в автоматическую процедуру, метод теряет главный защитный пункт — ревью намерения до генерации.

[^spdd-codemie]: CodeMie issue [#274](https://github.com/codemie-ai/codemie-code/issues/274) формулирует пользовательский сценарий через контракт дизайна, трассируемость требований и синхронизацию дизайна и кода.

### Внешний практический разбор: два маршрута исправления и граница применимости

WebReactiva не является первичным источником SPDD, но полезен как внешний практический пересказ. Он особенно хорошо фиксирует две вещи. Первая: prompt живёт в `git` и должен сопровождать код в течение жизни изменения. Вторая: исправления после генерации делятся на два маршрута. Если меняется наблюдаемое поведение, сначала обновляется prompt через `/spdd-prompt-update`, затем заново применяется генерация или локальная правка. Если это чистый рефакторинг без изменения поведения, код меняется первым, а затем синхронизируется обратно через `/spdd-sync`. Там же сформулирована прагматичная граница: применять SPDD к фичам с деловой логикой, которые проживут достаточно долго; не тратить его на срочное исправление, исследовательский spike или одноразовый скрипт.[^spdd-webreactiva]

Этот внешний пересказ подтверждает уже найденную в досье линию correction lanes, но делает её проще для будущей главы: читатель быстрее поймёт SPDD через вопрос “изменилось ли наблюдаемое поведение?”. Если да, меняется намерение; если нет, меняется реализация и потом подтягивается Canvas.

[^spdd-webreactiva]: WebReactiva, [“SPDD vs SDD y por qué importan los prompts estructurados”](https://www.webreactiva.com/blog/spdd), разделы о prompt в `git`, рабочем процессе, `/spdd-prompt-update`, `/spdd-sync`, настройке и случаях, где SPDD не стоит применять.

### Практический adoption path: команды, структура папок и “prompt lives in git”

WebReactiva даёт полезный practitioner-layer, которого не хватало в досье: SPDD описан как метод, где structured prompt lives in repository и travels with code in commits; tool setup is not abstract — `openspdd init`, `openspdd generate --all`, five core commands in `.claude/commands/`, optional commands, и a conventional folder layout: `requirements/`, `spdd/analysis/`, `spdd/prompt/`, `scripts/test-api.sh`, `src/`. [WebReactiva SPDD guide](https://www.webreactiva.com/blog/spdd)

Это важно не из-за самой папочной схемы, а из-за статуса артефактов. SPDD превращает prompt из ephemeral chat input в repo artifact. Если `spdd/prompt/` не меняется месяцами, а код меняется, метод фактически сломан: Canvas начинает врать. WebReactiva прямо подчёркивает ошибку “не коммитить prompt и code together” и правило: если меняется observable behavior, сначала обновляется prompt через `/spdd-prompt-update`; если это чистый refactor, код синхронизируется обратно через `/spdd-sync`. [WebReactiva SPDD guide](https://www.webreactiva.com/blog/spdd)

### `/spdd-sync`: reverse sync как дорогой, но необходимый контроль drift

Шаблон `/spdd-sync` подтверждает, что reverse sync — не магическая “обнови документ” команда. Он просит указать affected components or analyze recent git changes, читает current implementation, сравнивает class names, package paths, method signatures, attributes, annotations, business logic steps, validation rules и error messages с REASONS Canvas, затем генерирует Prompt Sync Plan и presents it for review before applying. Самый критичный раздел для обновления — Operations: именно там спецификация обычно содержит implementation-specific detail. [OpenSPDD `/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md)

Это уточняет одну из главных слабостей SPDD: reverse sync сам по себе является mini-review task. Его нельзя рассматривать как дешёвый housekeeping. Он требует знания того, какие компоненты изменились, и несёт риск ложной синхронизации: Canvas может стать аккуратно оформленным, но всё равно неверным, если сравнение было поверхностным.

### Correction lanes: prompt-update vs sync vs code fix

Шестой проход уточняет, что SPDD различает несколько correction lanes. `/spdd-prompt-update` содержит mapping of change types to affected REASONS sections: new functional requirement affects Requirements/Entities/Approach/Structure/Operations и possibly Norms/Safeguards; architectural change affects Approach/Structure/Operations/Norms; new safeguard affects Safeguards и possibly Operations; specification bug fix can target a section only. Источник: [OpenSPDD `/spdd-prompt-update` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md). `/spdd-sync` is explicitly about synchronizing implementation details from refactored or updated code back to the structured prompt so the prompt remains accurate источник истины: [OpenSPDD `/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md).

Это помогает убрать потенциальное недоразумение: SPDD не всегда означает “код нельзя трогать руками”. Более точная формула: observable/business change should update the intent artifact first or immediately after discovery; behavior-preserving refactoring can be code-first but must be synced back if it changes design-relevant structure. Внешний разбор mgks.dev формулирует тот же смысл: bug/business-logic fixes update the prompt и regenerate, while refactoring without behavior change can update code и sync back; this is external commentary, not core source. Источник: [mgks.dev SPDD commentary](https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/).

### Sync loop: обратная связь от кода к намерению

Третий проход уже фиксировал `/spdd-sync`, но четвёртый уточняет его место в петле. OpenSPDD README прямо противопоставляет typical plan documents и REASONS Canvas: плановые документы не обладают traceability, whereas `/spdd-sync` enables reverse sync; validation is not vague “done when complete”, but explicit status codes, error messages и safeguards ([OpenSPDD README](https://github.com/gszhangwei/open-spdd)). Это означает, что SPDD claims не только prompt-first, но и **bidirectional artifact maintenance**.

Слабое место остаётся тем же: синхронизация не происходит магически. Если команда забывает запускать sync после refactor/implementation drift, Canvas становится устаревшим и начинает вредить. Поэтому в будущем разделе SPDD нужно формулировать как **discipline with repair loop**, not as self-healing artifact system.

### Logic correction, prompt-update и sync

В SPDD важно различать два направления синхронизации. [`/spdd-prompt-update`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) работает, когда изменилось намерение: business rule, constraint, architectural adjustment, accepted behavior. [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) работает, когда изменился код без изменения намерения: refactoring, cleanup, decomposition, new component, implementation detail. В обоих случаях цель одна: Canvas не должен стать historical snapshot. Корпусный фрагмент: [§20](../../content/Theoretical_synthesis.md#spdd-prompt-update-sync).

В billing example logic correction появляется вокруг `modelId`. Первоначальная реализация допускает nullable field ради backward compatibility with historical data. После business confirmation команда решает, что для historical bills default value должен быть `fast-model`. Это не cosmetic refactoring, а изменение observable business behavior. Поэтому сначала выполняется [`/spdd-prompt-update`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md): structured prompt уточняет required field, default value и соответствующие части REASONS Canvas. Только после этого обновляется код. Корпусный фрагмент: [§20](../../content/Theoretical_synthesis.md#spdd-prompt-update-sync).

Напротив, если code review находит magic numbers в `calculateRemainingQuota`, это ordinary refactoring. Observable behavior не меняется. Агент делает small incremental refactor, затем [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) сравнивает current code against Canvas и записывает implementation updates обратно в REASONS sections. В источнике это называется golden rule: keep the structured prompt synchronized with your latest codebase. Корпусный фрагмент: [§20](../../content/Theoretical_synthesis.md#spdd-prompt-update-sync).

Это различение полезно за пределами SPDD: если bugfix меняет business meaning, но человек правит только код, intent asset начинает врать. Если refactoring заставляют проходить через полноценный business prompt update, процесс становится тяжелее задачи. SPDD даёт язык для разведения двух направлений: requirement → prompt → code и code → prompt нельзя смешивать. Корпусный фрагмент: [§20](../../content/Theoretical_synthesis.md#spdd-prompt-update-sync).

### Hotfixes и production signal

Fit table помечает firefighting hotfixes как слабый fit для SPDD. Текущая теория уточняет: это не значит, что production bugs, edge cases и сценарии сбоев проходят мимо methodology. Во время live incident system recovery comes first; писать Canvas в момент `stop the bleeding` — неправильный выбор. Но governance не отменяется, а переносится на следующий шаг. Корпусный фрагмент: [§24](../../content/Theoretical_synthesis.md#spdd-hotfix-production-signal).

Есть два сценария:

- **Scenario A — context exists.** Если bug falls inside область, уже покрытую structured prompt, команда может использовать AI для анализа failure и root cause, затем применить compressed SPDD loop: update prompt first, then update code. Fix становится частью governed asset, а не локальным emergency patch. Корпусный фрагмент: [§24](../../content/Theoretical_synthesis.md#spdd-hotfix-production-signal).
- **Scenario B — legacy or no prior context.** Если код не был brought under SPDD, прагматический ход — позволить AI проанализировать logs и исправить issue напрямую. Но closing step должен быть deliberate post-mortem: синтезировать fix, failure mode и relevant context в новые documented assets. Так SPDD coverage органически растёт по codebase. Корпусный фрагмент: [§24](../../content/Theoretical_synthesis.md#spdd-hotfix-production-signal).

Если production signal не возвращается в intent layer после инцидента, возникает spec/code delta. Код знает о failure mode, а артефакт намерения — нет. Следующая итерация снова начнётся без памяти о реальном сбое. Корпусный фрагмент: [§24](../../content/Theoretical_synthesis.md#spdd-hotfix-production-signal).

### Roadmap: от expert craft к organization-level asset system

Авторы, как это пересказано в текущей теории, честно признают: в нынешнем виде SPDD может выглядеть как метод для senior architects, потому что требует strong abstraction, modelling, systematic analysis и deep business understanding. Их целевое направление другое: framework должен постепенно переносить часть веса в organization-level asset system, а не зависеть полностью от personal craftsmanship. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory), внешний источник: [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

Roadmap в текущей теории состоит из четырёх направлений:

1. **Recurring workflows as commands.** Паттерн [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md), [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md), [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md), [`/spdd-sync`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) не закончен. По мере появления повторяемых ситуаций successful рабочий процесс извлекается в command, а не остаётся знанием отдельных людей. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory).
2. **Automated verification at the asset layer.** Проверять нужно не только code level. Будущий слой должен проверять analysis, Canvas и prompt artifacts: gaps, inconsistencies, under-specification, routine calls, structural completeness vs substantive adequacy. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory).
3. **Raising the automation ratio.** SPDD уже является harness, но semi-automated. Автоматизация должна расти постепенно, только там, где AI надёжно справляется с конкретным type of task. Это не «убрать человека», а пошагово переносить hand-holding в проверяемые commands и asset checks. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory).
4. **Decision memory.** Past canvases, trade-offs, accepted patterns и historical decisions должны стать persistent context, который agent может извлекать в новой ситуации. В текущей теории это прямо связывается с Noveia и active memory: ценность не только в сохранении документа, но в возможности поднимать правильное предыдущее reasoning именно тогда, когда оно нужно. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory).

Текущая теория делает важный вывод: SPDD сам движется от методики к экзоскелету. Сначала skilled practitioners вручную строят хорошие artifacts. Потом recurring thinking strategies становятся commands. Затем asset-layer verification и decision memory должны сделать качество менее зависимым от отдельного человека. Это ещё не решённый механизм, но направление важно. Корпусный фрагмент: [§25](../../content/Theoretical_synthesis.md#spdd-roadmap-decision-memory).



### Внешние сигналы трения: захват контекста и поддержка Codex

Список открытых issues в OpenSPDD полезен не как доказательство зрелости или незрелости проекта, а как маленькая карта реальных точек трения. На момент этого прохода там видны вопросы про `Pi Support`, захват полного `reasons-context`, поддержку OpenAI Codex, поддержку OpenCode и сбой `go install` из-за расхождения module path. Для досье важны не сами тикеты как источник фактов о методологии, а то, что пользователи упираются именно в границы инструментальной поверхности: как захватить весь контекст для Canvas, как перенести метод на Codex/OpenCode, как корректно поставить инструмент. [OpenSPDD issues](https://github.com/gszhangwei/open-spdd/issues)

Это уточняет риск SPDD: слабое место не только в качестве REASONS Canvas. Даже если Canvas хорош, рабочий процесс может сорваться на установке команд, политике доверия инструментов, неполном захвате `@`-контекста или несовпадении формата skills/commands между агентскими средами. Поэтому в будущей теории SPDD нужно описывать как связку артефакта намерения и инструментальной доставки этого артефакта в конкретный агент, а не как чистую методологическую форму.

## Применимость, стоимость, roadmap, риски и сценарии сбоев

### Риски и ограничения

* **Автоматизация без ревью намерения.** Если SPDD встроить в инструмент так, что пользователь видит только созданную issue или список задач, а не сам Canvas, метод может потерять своё главное свойство: явное согласование намерения до реализации.
* **Drift сопровождения спецификаций.** Ежедневный planner может исправно создавать задачи по устаревшим файлам спецификаций. Это полезно только при живом состоянии rotation cache, `write preflight` и человеческом ревью созданных issue.
* **Ритуальная установка команд.** Внешние guides упрощают вход, но могут превратить SPDD в установку slash-команд без дисциплины синхронизации prompt/code.
* **Расхождение инструментальных поверхностей.** Команды OpenSPDD могут копироваться в разные каталоги и адаптеры; без обновления и сверки с upstream шаблонами возникает расхождение поведения между Claude Code, Cursor, Codex, Copilot и локальными копиями.

### Риски и ограничения

* **False formalization risk** — structured Canvas can look precise without being correct.
* **Specification-oracle risk** — no independent oracle verifies whether Canvas matches business intent; human review remains load-bearing.
* **Evidence insufficiency** — generated API tests check selected behaviors, not full semantic correctness.
* **Overclaim risk** — SPDD should not be presented as formal methods; it is a pragmatic intent-control рабочий процесс.
* **Decision laundering** — AI may appear to “infer” design decisions that are actually unmade human trade-offs.

### Риски и ограничения

* **Stale Canvas is worse than no Canvas.** Если Canvas перестал соответствовать коду, он начинает не сохранять intent, а выдавать false alignment.
* **Sync is expensive.** `/spdd-sync` требует чтения кода, сравнения implementation details и human review of update plan; это не бесплатный автоматический ритуал.
* **Minimal-patch discipline can fail.** Если модель переписывает весь Canvas вместо targeted update, теряется auditability.
* **Хрупкость установки и доверия к инструменту.** README notes that some Codex versions may silently ignore skills from untrusted projects; для реального рабочий процесс это означает ещё один сценарий сбоя настройки. [OpenSPDD README](https://github.com/gszhangwei/open-spdd)
* **SPDD overuse.** Design philosophy и practitioner guidance both warn that rapid prototypes, one-off scripts и short-lived tasks may not justify structured-prompt overhead. [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md)

### `/spdd-code-review`: triage report вместо неограниченного human diff reading

`/spdd-code-review` задаёт очень конкретный формат review. Он принимает prompt file plus code files/folder/diff, проверяет все 7 REASONS dimensions, ищет safeguard violations, scope-boundary issues, implicit decisions и three forms of intent drift: positive drift (unauthorized additions), negative drift (omissions) и direction drift (different implementation direction). Output должен быть review report in `spdd/review/<file-name>.md` with summary table, traffic-light indicators, priority-ranked findings, overall merge-readiness verdict и recommendations. Важно, что command is read-only: it must not modify code or prompt, must read the complete REASONS Canvas, must read all referenced code files completely и must preserve objectivity: “what the code does vs what the prompt says,” not what reviewer personally prefers. Источник: [OpenSPDD `/spdd-code-review` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md).

Это уточняет место review в SPDD: review не является общей оценкой качества кода. Его load-bearing задача — снизить cognitive load человеческого reviewer-а, указав, где именно implementation crossed the intent contract. Conventional code review still matters, but SPDD review answers a narrower и more dangerous question: **did the AI implement the agreed intent, or did it add/omit/redirect meaning?**

### Риски и ограничения

- **False confidence from generated tests**: `/spdd-api-test` improves поведенческое свидетельство but its expected values are still AI-generated и must be reviewed; otherwise it can verify the model’s misunderstanding rather than the business rule.
- **Review report as another artifact to trust blindly**: `/spdd-code-review` reduces reviewer load, but if the model reads files partially or misses references, the report can become a false gate. The template’s insistence on complete `@` reading is therefore not decorative but load-bearing.
- **Prompt-as-source ambiguity**: SPDD may be misunderstood either as “only prompt matters” or as “just sync docs after code”. The useful position is stricter: behavior/design changes must travel through REASONS, while local refactors can be synced back when they affect design-relevant facts.

### Риски и ограничения

- **Narrow поведенческое свидетельство.** Generated API scripts are useful, but they mostly cover externally visible API behavior. They do not automatically prove UI behavior, data migrations, concurrency, security or performance.
- **Review report overconfidence.** A REASONS alignment report can look authoritative, even when the reviewer model missed a code path or misread an invariant.
- **Full-read cost.** Both review и API-test commands prefer full reading of references; this improves fidelity but can become expensive in large repositories.
- **Spec fidelity preserves bad design.** If the Canvas is wrong, strong conformance mechanisms faithfully implement the wrong design.
- **Optional command maturity.** Some OpenSPDD commands are optional/beta/specialized; the theory should not imply that every SPDD practice in the wild has the same maturity or adoption.

### Риски и ограничения

- **Token-heavy context integrity.** Требование читать все `@`-refs полностью хорошо защищает от hallucinated design, но без indexing/chunking может резко увеличить стоимость.
- **Bad Operations freeze.** Если Operations плохо разбиты, `/spdd-generate` может честно выполнить плохую последовательность; это лучше, чем бесконтрольная импровизация, но не гарантирует хороший дизайн.
- **False traceability.** Canvas может выглядеть связанным с кодом, но фактически устареть после refactor; sync становится обязательной hygiene, а не optional polish.
- **Prompt-first inversion trap.** Принцип “if reality diverges, fix prompt first” полезен, пока prompt действительно выражает intent. Но при архитектурной переоценке код может показать, что сам intent artifact нуждается в пересборке, а не в механическом patch.

### Два review lanes и fitness boundary

WebReactiva даёт полезную внешнюю формулировку двух review lanes: если меняется observable behavior, update prompt first with `/spdd-prompt-update` и regenerate affected code; if it is a pure refactor, change code и then use `/spdd-sync` to reflect structural changes back into the Canvas ([WebReactiva](https://www.webreactiva.com/blog/spdd)). Это вторичный источник, но формулировка хорошо подходит для будущего Handbook/Fieldbook: главный diagnostic question is “did observable behavior change?”

Там же полезно сжато сформулирована fitness rule: SPDD окупается, если feature has non-trivial business logic, lives longer than a few months, will be modified by someone else, or errors have real impact; for hotfixes, spikes и disposable scripts, upfront cost can dominate ([WebReactiva](https://www.webreactiva.com/blog/spdd)). Это не заменяет official fitness assessment, но усиливает практический край: SPDD is not a universal default.

### Риск process calcification

Наконец, сторонняя заметка [Treating Prompts Like Code](https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/) называет риск process calcification: team may generate REASONS Canvas because “that is what the process says,” not because it clarifies design. Этот источник слабее первичных, но полезен как warning label. В теории его лучше использовать не как авторитет, а как точную формулировку опасности: SPDD может стать cargo-cult ceremony, если Canvas не является местом настоящего решения.


### Внешнее чтение SPDD как “среднего слоя” между свободным prompt и formal spec

Внешний разбор Shahzad Bhatti полезен не как первичный источник SPDD, а как сравнительная рамка. Автор ставит OpenSPDD и REASONS Canvas между двумя крайностями: с одной стороны — свободная естественно-языковая просьба, где модель вынуждена угадывать edge cases; с другой — формальная спецификация вроде TLA+, где фиксируются state transitions, invariants и concurrency scenarios. В этой рамке REASONS Canvas работает как практический средний уровень: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards делают intent достаточно явным для ежедневной работы, но не требуют полноценные формальные методы.[^spdd-bhatti]

Эта рамка помогает точнее описать статус SPDD. Метод не должен обещать свойства формальной спецификации. Он снижает пространство произвольной интерпретации и делает ограничения ревьюируемыми, но корректность Canvas всё равно зависит от качества человеческого анализа. Поэтому SPDD лучше подавать как lightweight intent-control discipline: он даёт больше управления, чем обычный prompt или план, но остаётся ниже формального proof/specification layer.

[^spdd-bhatti]: Shahzad Bhatti, [AI Writes Code. You Own the Design. Here's How to Keep It That Way](https://weblog.plexobject.com/archives/7644), разделы про TLA+, REASONS Canvas, Operations sequencing, Norms/Safeguards и bidirectional sync.

### Где SPDD окупается и где нет

В источнике есть fitness assessment, который нужно перенести в будущую теорию почти без сглаживания. SPDD высоко оценивается для scaled standardized delivery, high compliance/hard constraints, team collaboration/auditability и cross-cutting consistency work. Слабо подходит для firefighting hotfixes, exploratory spikes, one-off scripts и context black holes — случаев, где стоимость governance выше полезности или problem boundary слишком плохой, чтобы задать meaningful Canvas ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)).

Это важный анти-универсалистский вывод: SPDD не должен становиться общей рекомендацией «всё писать через Canvas». Он является дорогим intent-governance инструментом и требует задачи, где сохранение и проверка намерения реально окупает overhead.

### Честные ограничения: variance и человеческое суждение

Самое важное уточнение из Q&A: SPDD снижает variance по сравнению с free-form prompting, но не устраняет её. Разные разработчики могут написать разные Canvas по одному требованию; у framework пока нет полностью объективного стандарта “good Canvas”. Источник прямо говорит, что структура, granularity, level of abstraction и task breakdown зашиты в команды как baseline criteria, но human judgement remains load-bearing. Следующий слой развития — automated verification at asset layer: проверки analysis, Canvas и prompt artifacts, а не только кода ([Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/)).

Это нужно обязательно сохранить в теории, чтобы SPDD не выглядел как магическое решение проблемы спецификаций. Его сила — не в автоматической правильности, а в том, что он делает намерение отдельным проверяемым объектом.

### Где SPDD окупается

Сильная зона SPDD — logic-heavy и rules-heavy изменения: billing, taxes, reporting, compliance, access rights, pricing, business workflows, cross-cutting consistency, migration-sensitive work. В таких задачах ошибка часто дорогая, а intent artifact окупается: снижает hallucination, делает traceability видимой, помогает ревью, удерживает границы и позволяет следующей итерации стартовать с накопленного контекста. Корпусный фрагмент: [§23](../../content/Theoretical_synthesis.md#spdd-fit-and-roi).

Fit assessment задаёт экономическую модель. Сильный fit: scaled, standardized delivery; high compliance и hard constraints; team collaboration и auditability; cross-cutting consistency work. Слабый fit: firefighting hotfixes, exploratory spikes, one-off scripts, context black holes, pure creative / visual work. Это вопрос отношения стоимости артефакта к стоимости ошибки и будущей эволюции. Корпусный фрагмент: [§23](../../content/Theoretical_synthesis.md#spdd-fit-and-roi).

### ROI

| Выгода | Что покупается процессом |
| --- | --- |
| Determinism | Логика кодируется в precise spec, поэтому модель меньше «творит» там, где нужна предсказуемость. |
| Traceability | Meaningful change можно проследить к structured prompt, closing the audit loop. |
| Faster reviews | Code приходит ближе к team standards; review меньше тратится на cleanup и больше — на logic/design. |
| Explainability | Intent и behavior видны на natural-language level; maintenance дешевле. |
| Safer evolution | Boundaries и stepwise implementation снижают риск targeted changes. |

Корпусный фрагмент: [§23](../../content/Theoretical_synthesis.md#spdd-fit-and-roi).

### Upfront cost

| Барьер | Что требуется |
| --- | --- |
| Mindset shift | Команде нужно привыкнуть к design-first вместо code-first. |
| Senior expertise up front | Нужны люди, способные переводить business rules в clean abstractions и constraints. |
| Automation tooling | Без CLI/рабочий процесс automation SPDD упирается в throughput ceiling и consistency problems. |

Корпусный фрагмент: [§23](../../content/Theoretical_synthesis.md#spdd-fit-and-roi).

Практический критерий: SPDD окупается, когда цена неверного намерения выше цены поддержки артефакта. Если задача маленькая, обратимая и близко проверяется браузером или одним тестом, SPDD может стать тяжёлым ритуалом. Если задача проходит через данные, API, business rules, compliance, архитектурные границы или командную передачу знания, отсутствие maintained intent asset может быть дороже. Корпусный фрагмент: [§23](../../content/Theoretical_synthesis.md#spdd-fit-and-roi).

### Ограничения, сопротивление и сценарии сбоев

Критика SPDD в текущей теории встроена в сам раздел, чтобы метод не стал слишком гладкой догмой. Корпусный раздел: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).

1. **Variance переносится на уровень Canvas.** SPDD не устраняет variance полностью. Два разработчика могут написать разные Canvas по одному требованию, а один и тот же человек может в разные дни сделать более сильный или более тонкий artifact. Команды OpenSPDD поднимают нижнюю границу, задавая structure, granularity, abstraction level и task breakdown, но не дают объективного стандарта «хорошего Canvas». Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source), источник команд: [OpenSPDD](https://github.com/gszhangwei/open-spdd).
2. **SPDD остаётся human-led.** Это сила и ограничение. Человек проверяет business intent, abstraction, boundaries, trade-offs и пригодность Canvas к реальной задаче. Если человек слаб в домене или поверхностно ревьюит документ, SPDD может не защитить. Он создаёт место для правильного решения, но не гарантирует, что решение будет принято. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).
3. **Relation to spec-as-source.** SPDD ближе к spec-anchored, но из этого не следует, что спецификация должна стать единственным источником правды. Spec-as-source наследует проблемы model-driven development: overhead, ограничения выразительности, трудность синхронизации, опасность того, что формально красивый документ хуже отражает реальную систему, чем код, тесты и эксплуатационные сигналы. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source), сравнительный источник: [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
4. **Model и configuration drift.** SPDD intended as model-agnostic, но raw capability имеет значение, особенно для analysis и REASONS Canvas. После фиксации intent менее сильная модель может быть приемлемым executor, но risk of intent drift остаётся. В некоторых средах реальным артефактом становится не только prompt-as-spec, а prompt + model configuration + command semantics + review protocol. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).
5. **Ceiling на стороне задачи.** Если область слишком широкая, multi-project, multi-discipline, multi-domain, плохо ограниченная или требует portfolio-scale decisions, модельная сила не спасает. Нужны decomposition, накопленные decision assets и человеческий шлюзs. В context black holes, где business rules unclear и boundaries weak, stronger AI just fails more confidently. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).
6. **Риск ухудшения человеческой компетенции при полном agent-driven review.** [`/spdd-code-review`](https://github.com/gszhangwei/open-spdd) уже может читать Canvas и code diff together и flag drift, но авторы считают, что человек нужен для catching intent drift, когда сам Canvas уже не соответствует real business intent, и для learning from AI choices. Если review полностью отдать агенту, можно ускорить процесс, но потерять long-term skill growth. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).

Итоговая позиция текущей теории: SPDD — один из лучших примеров того, как agentic/doc-first разработка может сделать намерение сопровождаемым инженерным объектом. Но его нельзя превращать в универсальную норму. Он полезен там, где нужно удерживать сложное, проверяемое, дорогое намерение; вреден там, где задача мала, плохо определена или требует быстрой разведки без тяжёлого governance. Корпусный фрагмент: [§26](../../content/Theoretical_synthesis.md#spdd-resistance-boundaries-and-spec-as-source).


## Синтез и связи с текущим корпусом

### Сводный синтез

SPDD в этом досье следует описывать не как «хороший prompt template» и не как лёгкую разновидность SDD, а как **практический контур управления намерением**. Его исходная проблема проста: модель способна построить правдоподобное решение, но не может самостоятельно нести ответственность за бизнес-смысл, архитектурные развилки, отрицательное пространство и границы изменения. Поэтому SPDD выносит намерение в сопровождаемый артефакт — REASONS Canvas — и заставляет реализацию проходить через файл, который можно читать, ревьюить, версионировать, обновлять и синхронизировать с кодом. Основной источник этой рамки — Fowler/Thoughtworks о Structured Prompt-Driven Development и OpenSPDD как командная реализация метода ([Fowler / Thoughtworks](https://martinfowler.com/articles/structured-prompt-driven/), [OpenSPDD](https://github.com/gszhangwei/open-spdd)).

Собранная фактура показывает, что зрелая форма SPDD держится не на одном Canvas, а на нескольких связанных контрактах:

1. **Контракт поглощения контекста.** Команды вроде `/spdd-analysis`, `/spdd-reasons-canvas` и `/spdd-reverse` требуют раскрывать переданные `@file` / `@folder`, читать предыдущий Canvas, кодовую базу и исходные требования до построения нового артефакта. Поэтому важен не только результат Canvas, но и явный source-precedence: что считалось исходным контекстом, что было проигнорировано и где модель сделала реконструкцию, а не получила факт напрямую ([`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md), [`/spdd-reverse`](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md)).
2. **Контракт решения.** REASONS Canvas фиксирует не только требования, но и сущности, подход, операции, нормы и safeguards. Это важнее обычного плана: Canvas должен удерживать именно те решения, которые нельзя надёжно вывести из кода или тестов после факта.
3. **Контракт исполнения.** `/spdd-generate` должен исполнять `Operations`, `Norms` и `Safeguards`, а не заново планировать задачу как свободный агент. В сильной версии SPDD модель становится исполнителем уже принятого намерения, а не скрытым автором новой архитектуры.
4. **Контракт свидетельств и ревью.** `/spdd-api-test` создаёт удобные для человека поведенческие свидетельства: shell/cURL script, таблицы expected/actual, edge/error cases. `/spdd-code-review` проверяет implementation against REASONS Canvas: intent drift, safeguard violations, implicit decisions, scope boundary и merge readiness ([`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md), [`/spdd-code-review`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md)).
5. **Контракт обновления.** `/spdd-prompt-update` и `/spdd-sync` различают изменение намерения, чистый рефакторинг и обратную синхронизацию кода с Canvas. Без этого SPDD быстро деградирует в красивую историческую спецификацию, которая уже не управляет будущей работой.

Итоговый жизненный цикл выглядит так: analysis → REASONS Canvas → generation → behavioral evidence → REASONS-aware review → prompt update / sync → при необходимости reverse onboarding legacy-кода. Эта петля может работать в трёх режимах: интерактивная фича, плановое сопровождение корпуса спецификаций и встраиваемый слой других инструментов. Пример `github/gh-aw` показывает, что SPDD-команды можно использовать не только в IDE-чате, но и как scheduled workflow, который обходит spec-файлы, формирует issue, выставляет P0/P1/P2 и оставляет проверяемый план работы ([daily SPDD planner workflow](https://github.com/github/gh-aw/blob/main/.github/workflows/daily-spdd-spec-planner.md)).

При этом SPDD не следует подавать как формальный метод и не нужно делать вид, что Canvas решает intent gap. Более точная формулировка: SPDD **превращает разрыв между намерением и реализацией в управляемый артефактный контур**. Canvas сам остаётся предметом проверки; если человек зафиксировал неверное намерение, модель может аккуратно реализовать именно неверный замысел. Поэтому SPDD остаётся human-led: человек принимает load-bearing решения, проверяет Canvas, смотрит evidence, решает, изменился ли смысл фичи, и несёт ответственность за границы. Внешняя рамка intent formalization полезна именно как ограничитель: проверяемые спецификации лежат на спектре от tests/contracts до logical specs/DSLs, а SPDD занимает практический средний слой, где формализация ещё не строгая, но уже достаточно явная для ревью ([Intent-Centric Software Engineering](https://ar5iv.org/html/2603.17150v1)).

Практическая ценность SPDD максимальна там, где цена неверного намерения выше цены поддержки артефакта: сложные фичи, неоднозначные бизнес-правила, дорогие интеграции, API-visible behavior, долгоживущие продукты, legacy-onboarding и командная работа. Он хуже подходит для маленьких обратимых задач, горячих production-fixes, разведки без ясных границ и случаев, где документ становится тяжелее самой работы. Для будущей теории это делает SPDD глубоким якорем: он показывает, как prompt/design artifact может стать сопровождаемым инженерным объектом с ingestion, execution, evidence, review и repair, но одновременно показывает цену такой дисциплины.

### Связи в текущем корпусе

`Cross_story_synthesis.md` использует SPDD как более жёсткую форму той же механики, которая у историй проявляется через внешние артефакты. В cross-story разделе сказано, что structured prompt превращается в maintained delivery artifact, REASONS Canvas держит intent, design, execution и governance, а рабочий процесс требует синхронизировать prompt и code, а не выбрасывать спецификацию после генерации. Корпусный фрагмент: [Cross-story, раннее упоминание SPDD](../../content/Cross_story_synthesis.md).

В другом месте `Cross_story_synthesis.md` связывает SPDD с линией Tane, Vincent, Mark Erikson и Matt Pocock: документ полезен не только как план до кода, но и как поддерживаемый intent asset, который должен оставаться синхронизированным с реализацией. Одновременно HumanLayer, Steinberger и Pocock предупреждают против огромного постоянного контекста: документ полезен, если хранит решение, состояние, доменный язык, проверку или синхронизируемое намерение; документ вреден, если становится энциклопедией, которую агент игнорирует или использует как шум. Корпусный фрагмент: [Cross-story, раздел о внешних артефактах](../../content/Cross_story_synthesis.md).

Ещё одно cross-story различение: если документ помогает агенту продолжать, но не помогает человеку принять ответственность, он неполон; если документ помогает человеку, но агент его игнорирует, нужно менять форму загрузки контекста, а не просто писать больше. SPDD здесь полезен как крайний пример: артефакт намерения должен быть связан с проверяемым поведением, code review и обратной синхронизацией, иначе он быстро становится красивым историческим снимком. Корпусный фрагмент: [Cross-story, раздел о документах и ответственности](../../content/Cross_story_synthesis.md).

`Handbook.md` упоминает Thoughtworks / Martin Fowler о context engineering, structured prompt-driven development и роли людей в петлях разработки с агентами как источник для практического слоя. Это не добавляет отдельной фактуры SPDD, но показывает, что SPDD должен позже войти в Handbook не как догма, а как верхняя ступень усложнения процесса. Корпусный фрагмент: [Handbook](../../content/Handbook.md).


## Источникный контекст и сохранённые поисковые заметки

### review/test artifacts и external spec-alignment contrast

Поисковый угол этого прохода отличался от предыдущих: не очередной обзор SPDD и не новые команды ради списка, а **как SPDD делает намерение проверяемым после генерации** и где его место относительно более широкой spec-driven линии. Поэтому были раскрыты: optional command templates `/spdd-api-test` и `/spdd-code-review`, core templates `/spdd-prompt-update` и `/spdd-sync`, внешний разбор “prompts like code” и a broader paper-style framing of spec-anchored vs spec-as-source development.

### verification layer — `/spdd-code-review`, `/spdd-api-test` и concrete examples

Этот проход сделан не как ещё один общий поиск по SPDD, а как добор **verification layer**, которого не хватало deep-anchor досье. После раскрытия этих источников SPDD уже был хорошо раскрыт как intent/execution/sync loop, но оставался риск описать его слишком односторонне: Canvas → generation → sync. Пятый проход раскрывает, что в OpenSPDD есть отдельный слой проверяемого свидетельства: code review against REASONS Canvas и API test generation. Основные источники: [`/spdd-code-review`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-code-review.md), [`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-api-test.md), [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) и practical examples from [Fowler/Thoughtworks SPDD](https://martinfowler.com/articles/structured-prompt-driven/) и the [WebReactiva SPDD walkthrough](https://www.webreactiva.com/blog/desarrollo-spdd/).

### anchor-depth слой — execution fidelity, ingestion contract и traceability loop

Этот проход был сделан потому, что SPDD в нашей теории является **глубокий якорь**, а не обычным примером. Поэтому поиск был намеренно смещён от обзорных статей к нижнему operational layer: какие именно обязательства OpenSPDD command templates накладывают на агента до генерации, во время генерации и после изменения кода. Основные источники прохода: командный шаблон [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md), [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md), основной [OpenSPDD README](https://github.com/gszhangwei/open-spdd), а также таблица core commands в статье [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

### tool adapters, downstream practice и сценарии сбоев

Этот проход искал не новые пересказы статьи Fowler/Thoughtworks, а другой слой: как OpenSPDD раскладывает метод по разным AI-инструментам, как внешние практические статьи объясняют setup/fitness/review lanes, и какие риски появляются при превращении Canvas в обязательную церемонию. Основные дополнительные источники: текущий [OpenSPDD README](https://github.com/gszhangwei/open-spdd/blob/main/README.md), [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md), практический разбор [WebReactiva: SPDD vs SDD](https://www.webreactiva.com/blog/spdd), заметка [Treating Prompts Like Code](https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/) и официальная статья [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) для сверки optional commands.

### что добавлено после раскрытия источников

Этот раздел фиксирует фактуру, добавленную уже не из `/content`, а после открытия внешних источников. Он не заменяет материал ниже, а уточняет его и добавляет проверенные опорные детали. Основные источники прохода: статья Thoughtworks/Fowler [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/), страницы навыков [Abstraction first](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html), [Alignment](https://martinfowler.com/articles/structured-prompt-driven/alignment.html), [Iterative Review](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html), обзор SDD-инструментов [Kiro, spec-kit, и Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) и репозиторий [OpenSPDD](https://github.com/gszhangwei/open-spdd).


## Дополнительные сохранённые заметки

### Две линии исправления: code-first correction vs prompt-first correction

Практические SPDD walkthroughs emphasize an important distinction: when implementation diverges from intended behavior, update the prompt first и regenerate or correct from the prompt; when implementation changes are behavior-preserving refactors, code can change first и then `/spdd-sync` keeps the Canvas aligned ([WebReactiva SPDD walkthrough](https://www.webreactiva.com/blog/desarrollo-spdd/)).

Это различие полезно для нашей теории because it prevents caricature. SPDD is not “never edit code manually”. It is closer to:

1. if behavior/architecture/intent changed, update the intent artifact;
2. if code changed without changing intent, sync evidence back;
3. if code reveals that the original prompt was wrong, revise the prompt as source of design truth;
4. if generated code merely violates the prompt, fix code or regenerate against the existing prompt.

### Синхронизация как нерешённый engineering challenge

Design philosophy содержит честное предупреждение: structured prompt can become outdated too. Если код меняется, а Canvas не обновляется, он превращается из design guide into misleading outdated documentation; bidirectional synchronization between design specs и code is explicitly named as one of the biggest engineering challenges, not solved completely. Current OpenSPDD practice is manual `/spdd-sync` after each feature iteration, with future automation as direction ([OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md)).

Эта оговорка должна быть в теории рядом с SPDD обязательно. Иначе SPDD будет выглядеть слишком гладко: будто достаточно завести Canvas, и drift исчезнет. Реальная позиция сильнее и честнее: SPDD делает drift видимым и repairable, but does not remove the discipline requirement.

### Code review на уровне REASONS

Раскрытие источников добавляет ещё один важный слой: optional `/spdd-code-review` проверяет соответствие code diff не общим ожиданиям, а каждой части REASONS Canvas. В шаблоне есть отдельные блоки `Requirements Alignment`, `Entities Alignment`, `Approach Alignment`, `Structure Alignment`, `Operations Alignment`, `Norms Alignment`, `Safeguards Alignment`; особенно сильна часть про safeguards как negative space — границы, которые нельзя пересекать ([spdd-code-review.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md)).

Это полезно для будущей теории: SPDD превращает review из чтения диффа в проверку соответствия диффа intent artifact. Но это не значит, что человек перестаёт проверять код. Скорее, кодовое ревью получает дополнительную структуру: не только «правильно ли написано», но и «не ушло ли решение от того, что было зафиксировано в Canvas».

### Заметки для будущей проверки источников

- Проверить, есть ли в текущих локальных assets уже сохранённые изображения SPDD; если нет — скачать только Canvas/рабочий процесс/first-class-artifact images, а не все картинки статьи.
- Возможно, стоит сделать отдельную короткую таблицу `SPDD commands → artifact → человеческий шлюз → sync direction`, потому что она полезнее для будущей главы, чем длинный пересказ команд.
- Не переносить fitness assessment в виде абстрактной оценки; лучше сохранить пары “high payoff / low payoff”, чтобы theory не стала универсализировать SPDD.
- В будущем chapter drafting не использовать OpenSPDD templates как «истину о методе» сильнее, чем статью: templates показывают operationalization, статья задаёт method framing.


Structured-Prompt-Driven Development нужно читать не как технику «написать хороший запрос», а как сильную форму управления намерением в агентской разработке: когда модель уже быстро производит код, главная опасность смещается к быстро размноженному недопониманию. SPDD отвечает на это превращением prompt в поддерживаемый delivery artifact: его можно версионировать, ревьюить, переиспользовать и синхронизировать с кодом. Основной источник в текущем корпусе — раздел [«Артефакт намерения: prompt как delivery artifact»](../../content/Theoretical_synthesis.md#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli) со ссылкой на [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/).

Ключевая формула текущей теории: SPDD переносит центр процесса с одноразового чата на сопровождаемый артефакт намерения. В обычном агентском режиме запрос помогает получить `diff`, но затем растворяется в истории чата, сжатии контекста, последующих правках и локальных объяснениях. Через две недели остаётся код, но теряется исходная модель решения: какие требования были поняты, какие границы приняты, какие варианты отклонены, какие нормы считались обязательными и какие предохранители нельзя было нарушать. SPDD сохраняет эту модель решения в structured prompt, который лежит рядом с кодом и продолжает быть рабочим объектом после генерации. Корпусный фрагмент: [§11](../../content/Theoretical_synthesis.md#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli).

Важно не подменить SPDD лозунгом «документы важнее кода». В текущей теории прямо зафиксировано: код, тесты, runtime-проверки и человеческие решения остаются отдельными слоями истины. Отличие SPDD в том, что намерение перестаёт быть расходуемым сообщением и становится версионируемым, ревьюируемым, повторно используемым объектом, который должен эволюционировать вместе с реализацией. Корпусный фрагмент: [§11](../../content/Theoretical_synthesis.md#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli).

## Источники и provenance

Этот раздел восстановлен внутрь досье `SPDD_METHOD_DOSSIER.md` после ошибочного выноса в общий реестр. Хронология проходов здесь снята: источники сгруппированы по функции в методологии, а не по моменту добавления. Inline-ссылки в основном тексте сохранены рядом с конкретными утверждениями; этот раздел нужен для проверки покрытия и подготовки дальнейших проходов.

### Основные методологические и корпусные источники

- Martin Fowler / Thoughtworks, [Structured Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — повторно использован для сверки sequence API tests → code review → unit tests и human review boundaries.
- Martin Fowler / Thoughtworks — [Structured Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — использован для concrete token-billing examples и relation between generated code, API tests, и review.
- `content/Theoretical_synthesis.md`, разделы 11–26 — основной корпусный источник: структура SPDD, рабочий процесс, REASONS Canvas, core skills, validation, sync, unit tests, asset integrity, ROI, hotfix handling, roadmap, limitations.
- Martin Fowler / Thoughtworks — Structured-Prompt-Driven Development: [https://martinfowler.com/articles/structured-prompt-driven/](https://martinfowler.com/articles/structured-prompt-driven/) — основной внешний источник по методологии, рабочий процесс, Q&A, examples, API validation, prompt update/sync и review logic.
- Martin Fowler / Thoughtworks — SPDD / Abstraction First: [https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html](https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html) — источник по design before generation, contract first, granularity и diagrams.
- Martin Fowler / Thoughtworks — SPDD / Alignment: [https://martinfowler.com/articles/structured-prompt-driven/alignment.html](https://martinfowler.com/articles/structured-prompt-driven/alignment.html) — источник по lock intent before code, domain language, scope, acceptance criteria и hidden constraints.
- Martin Fowler / Thoughtworks — SPDD / Iterative Review: [https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html](https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html) — источник по review loop, prompt/code consistency, asset integrity, hallucination и correctness.
- Martin Fowler / Thoughtworks — Understanding Spec-Driven-Development: Kiro, spec-kit, и Tessl: [https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — источник различения spec-first, spec-anchored, spec-as-source и контекст для позиционирования SPDD относительно SDD.
- Martin Fowler fragments / SPDD Q&A pointer: [https://martinfowler.com/fragments/](https://martinfowler.com/fragments/) — источник по human-review trade-off: agent can check alignment, but humans remain necessary for real business intent и learning.
- Martin Fowler / Thoughtworks — Structured-Prompt-Driven Development: [https://martinfowler.com/articles/structured-prompt-driven/](https://martinfowler.com/articles/structured-prompt-driven/) — повторно раскрыт точечно для optional `/spdd-api-test`, `/spdd-story`, examples и revision notes, без дублирования основного прохода.
- `content/Cross_story_synthesis.md` — использует SPDD как крайний пример maintained intent artifact и синхронизации prompt/code; связывает SPDD с Tane, Vincent, Mark Erikson, Matt Pocock и HumanLayer.
- `content/Handbook.md` — упоминает structured prompt-driven development как источник для практического слоя, но не добавляет новой фактуры к SPDD.
- [Fowler/Thoughtworks: Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — core command table, `/spdd-generate` semantics и review focus.
- Martin Fowler / Thoughtworks SPDD article — feature verification и `/spdd-api-test` explanation: https://martinfowler.com/articles/structured-prompt-driven/

### OpenSPDD: команды, шаблоны, adapter-layer и реализация процесса

- OpenSPDD command template [`/spdd-reverse`](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md) — основной новый источник прохода: подключение legacy-кода, reverse-engineering existing code into REASONS Canvas, подтверждение области, полное чтение файлов, извлечение структуры, сущностей, поведения, зависимостей, конвенций и ограничений, `[Codify]` file naming и ограничители против идеализации кода.
- OpenSPDD [`README`](https://github.com/gszhangwei/open-spdd) — повторно использован для проверки supported environments, Codex skills, explicit invocation, список необязательных команд и пример Plan vs REASONS.
- GitHub `gh-aw` — [`daily-spdd-spec-planner.md`](https://github.com/github/gh-aw/blob/main/.github/workflows/daily-spdd-spec-planner.md) — источник по scheduled SPDD planning: download OpenSPDD command templates, planner stages, spec-file scope, rotation cache и write preflight.
- [`/spdd-code-review` command template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-code-review.md) — основной источник по REASONS alignment review, режимы ввода, full-read requirement, intent drift, implicit decisions, safeguard/scope checks и review report shape.
- [`/spdd-api-test` command template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-api-test.md) — основной источник по generated `scripts/test-api.sh`, cURL-based endpoint tests, structured test-case tables, expected/failure results и удобный для человеческой проверки поведенческое свидетельство.
- [`/spdd-generate` command template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) — повторно использован для связи verification layer with Operations/Norms/Safeguards execution.
- OpenSPDD — command templates и CLI: [https://github.com/gszhangwei/open-spdd](https://github.com/gszhangwei/open-spdd) — источник по командам `/spdd-story`, `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-api-test`, `/spdd-prompt-update`, `/spdd-sync` и связанным шаблонам.
- OpenSPDD command template `/spdd-story`: [https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) — источник по story decomposition, INVEST evaluation, business-language acceptance criteria, no technical-layer split и required full reading of `@` references.
- OpenSPDD command template `/spdd-analysis`: [https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) — источник по concept-driven codebase exploration, lightweight project fingerprint, domain nouns/action verbs/API surfaces, targeted reading и one-hop expansion.
- OpenSPDD command template `/spdd-reasons-canvas`: [https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) — источник по built-in REASONS framework и implementation-ready structured prompt.
- OpenSPDD command template `/spdd-sync`: [https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) — источник по reverse flow Code → Design: analyze changes, compare, plan updates, update prompt.
- OpenSPDD command template `/spdd-code-review`: [https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md) — источник по REASONS alignment, intent drift, safeguards, implicit decisions, scope boundary и review report.
- OpenSPDD design philosophy: [https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) — источник по distinction between model capability и process/control; открыт как дополнительный background, но использован ограниченно.
- OpenSPDD README: [https://github.com/gszhangwei/open-spdd/blob/main/README.md](https://github.com/gszhangwei/open-spdd/blob/main/README.md) — использован для tool-adapter layer, supported environments, Codex skill-bundles under `.agents/skills/<id>/SKILL.md`, explicit-only invocation by default, optional `/spdd-reverse`, command list и Plan vs REASONS Canvas example.
- OpenSPDD design philosophy: [https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) — использован для границы SPDD vs `CLAUDE.md`/`AGENTS.md`, уровня фичи vs уровня репозитория artifacts, warning about stale Canvas и unsolved bidirectional-sync problem.
- [OpenSPDD `/spdd-reasons-canvas` command template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) — context-ingestion contract, `@file` / `@folder` handling, no truncation, implementation-ready output, no placeholders.
- [OpenSPDD `/spdd-generate` command template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) — Operations sequence, whole-prompt reading, project context scan, strict application of Norms и Safeguards.
- [OpenSPDD README](https://github.com/gszhangwei/open-spdd) — plan-vs-REASONS comparison, traceability claim, `/spdd-sync` as reverse sync, validation differences.
- OpenSPDD `/spdd-api-test` template — detailed optional command template for generating self-contained cURL API test scripts with удобный для человеческой проверки test tables и result tables: https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md
- OpenSPDD `/spdd-code-review` template — optional command template for reviewing implementation against REASONS Canvas, intent drift, implicit decisions, safeguard violations и scope boundary: https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md
- OpenSPDD `/spdd-prompt-update` template — core command template for updating REASONS sections based on change type: https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md
- OpenSPDD `/spdd-sync` template — core command template for syncing implementation details back into structured prompt: https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md
* [OpenSPDD design philosophy — AI Isn't Lacking Intelligence — It Has Too Many "Ideas"](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) — источник для capability/control distinction, overuse warning, stale Canvas risk и future automation direction.
* [OpenSPDD README](https://github.com/gszhangwei/open-spdd) — command inventory, optional beta commands, plan-vs-Canvas example, usage recommendations и trust-model note for Codex skills.
* [OpenSPDD `/spdd-prompt-update` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) — minimal patch discipline, no-code-block rules, affected-section update logic.
* [OpenSPDD `/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) — reverse sync protocol: implementation reading, discrepancy categories, update plan и consistency validation.
- OpenSPDD [design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) — повторно раскрыт через угол negative space, decision uncertainty, stale design intent и control dimension.
- OpenSPDD [README](https://github.com/gszhangwei/open-spdd) — повторно использован для supported command surface, Codex skill bundles и Plan vs REASONS Canvas comparison.

### Внешнее применение, walkthrough и интеграционные сигналы

- GitHub issue `github/gh-aw#30864`, [`[spdd] Daily spec work plan - 2026-05-07`](https://github.com/github/gh-aw/issues/30864) — конкретный результат daily SPDD planner: reviewed files, rotation index, priority queue и SPDD checklist.
- Shahzad Bhatti, [`AI Writes Code. You Own the Design. Here's How to Keep It That Way`](https://weblog.plexobject.com/archives/7644) — внешний сравнительный разбор REASONS Canvas как средний слой между свободным prompt и формальной спецификацией.
- WebReactiva — [SPDD vs SDD y por qué importan los prompts estructurados](https://www.webreactiva.com/blog/spdd) — внешний practitioner guide по prompt-in-git, correction lanes, setup, folder layout и when not to use SPDD.
- WebReactiva — [SPDD walkthrough](https://www.webreactiva.com/blog/desarrollo-spdd/) — secondary practice source for prompt-update / sync distinction и behavior-changing vs behavior-preserving correction lanes.
- WebReactiva — SPDD vs SDD y por qué importan los prompts estructurados: [https://www.webreactiva.com/blog/spdd](https://www.webreactiva.com/blog/spdd) — вторичный практический источник по установке, структуре файлов, необязательным командам, двум линиям ревью и правилу “когда не использовать”.
* [WebReactiva: SPDD vs SDD y por qué importan los prompts estructurados](https://www.webreactiva.com/blog/spdd) — practitioner guide: setup path, folder layout, correction lanes, common mistakes и when not to use SPDD.

### Слабые сигналы внедрения и переносимости

- GitHub issue `gszhangwei/open-spdd#9`, [`How to capture all reasons-context via command spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/issues/9) — слабый, но важный сигнал трения вокруг source precedence и захват предыдущего Canvas.
- GitHub issue `gszhangwei/open-spdd#6`, [`OpenAi Codex support`](https://github.com/gszhangwei/open-spdd/issues/6) — короткий запрос поддержки Codex; использовать только как сигнал давление переносимости.
- GitHub issue `gszhangwei/open-spdd#5`, [`feat: OpenCode support`](https://github.com/gszhangwei/open-spdd/issues/5) — короткий запрос поддержки OpenCode; использовать только как сигнал adapter-layer pressure.
- OpenSPDD [`Issues`](https://github.com/gszhangwei/open-spdd/issues) — слабый, но полезный источник по adoption friction: вопросы о захвате полного context для `reasons-context`, поддержке Codex/OpenCode, установке и module path. Использован только как сигнал трения, не как источник внутренней методологической механики.
- CodeMie issue [#274: Integrate OpenSPDD to enable design-spec driven development](https://github.com/codemie-ai/codemie-code/issues/274) — слабый, но полезный источник по external integration demand: контракт дизайна, requirements traceability и синхронизацию дизайна и кода.

### Внешние рамки, критика и сравнительный фон

- Treating Prompts Like Code: [https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/](https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/) — вторичный критический источник по риску окостенения процесса и cargo-cult использования.
- From Code-Centric to Intent-Centric Software Engineering: [https://arxiv.org/abs/2605.11027](https://arxiv.org/abs/2605.11027) — указан в карте источников теории рядом с SPDD/intent-centric framing; в данном досье не использован содержательно, потому что текущая теория не переносит из него SPDD-specific детали.
- Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents: [https://arxiv.org/abs/2603.17150](https://arxiv.org/abs/2603.17150) — указан в карте источников теории рядом с темой intent formalization; в данном досье не использован содержательно.
- mgks.dev commentary — external interpretation of prompt-as-code, review semantics и prompt/code correction lanes: https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/
- “From Code to Contract in the Age of AI Coding Assistants” — external conceptual frame distinguishing spec-anchored и spec-as-source development: https://arxiv.org/html/2602.00180
- Shuvendu K. Lahiri — [Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents](https://ar5iv.labs.arxiv.org/html/2603.17150v1) — источник по intent gap, spectrum of specifications/tests/contracts/DSLs, validation bottleneck, no oracle for specification correctness и lightweight tests as proxy artifacts.
- Elyson De La Cruz — [From Code-Centric to Intent-Centric Software Engineering](https://arxiv.org/abs/2605.11027) — рамочный источник по переходу от изолированного авторства к надзору, проверке и управлению системами “человек — агент — инструмент — свидетельства”.

## Поисковые формулировки и углы будущих проверок

Этот раздел сохранён как рабочая память поисковых направлений. Хронология проходов снята: формулировки сгруппированы как единый набор проверочных углов, чтобы они не задавали отдельную структуру досье.

- `open-spdd issues reasons-context previous canvas spdd-reasons-canvas`
- `open-spdd Codex support OpenCode support adapter layer`
- `github gh-aw daily SPDD planner issue output SPDD checklist`
- `OpenSPDD REASONS Canvas формальная спецификация TLA+ comparison`
- `OpenSPDD spdd-reverse подключение legacy-кода REASONS Canvas`
- `OpenSPDD issues reasons-context Codex support OpenCode support`
- `SPDD reverse existing code into REASONS Canvas guardrails`
- `SPDD Plan vs REASONS Canvas example поддерживаемые среды Codex skills`
* `intent formalization AI agents code generation specification validation`
* `intent gap AI generated code plausible not correct`
* `From code-centric to intent-centric software engineering agentic systems accountability`
* `SPDD negative space design decisions AI cannot infer`
* `OpenSPDD design philosophy negative space stale Canvas`
* `REASONS Canvas формальная спецификация tests contracts DSL comparison`
* `OpenSPDD adoption GitHub рабочий процесс daily SPDD planner`
* `OpenSPDD integration issue design code traceability sync`
* `SPDD practitioner guide prompt lives in git prompt update sync`
* `SPDD when not to use hotfix spike disposable script`
* `SPDD scheduled spec maintenance GitHub Actions Copilot prompts`
- business input → `/spdd-story` превращает расплывчатое требование в независимые stories;
- `/spdd-analysis` делает targeted context extraction instead of broad context hoarding;
- `/spdd-reasons-canvas` фиксирует intent/design/execution/governance;
- `/spdd-generate` выполняет instruction-following внутри Canvas;
- `/spdd-code-review` ищет intent drift и safeguard violations;
- `/spdd-sync` возвращает code-side changes обратно в prompt asset.
- `OpenSPDD Codex skills .agents/skills allow_implicit_invocation`
- `OpenSPDD supported tools Claude Code Cursor Codex GitHub Copilot spdd-reverse`
- `OpenSPDD design philosophy AGENTS.md CLAUDE.md REASONS Canvas уровня фичи уровня репозитория`
- `SPDD when not to use hotfix spike disposable scripts feature lives longer than 3 months`
- `SPDD prompt as code process calcification cargo cult REASONS Canvas`
- `OpenSPDD command templates spdd-analysis spdd-code-review spdd-sync`
- `SPDD code review intent drift safeguards implicit decisions`
- `Structured Prompt-Driven Development Q&A human review learning intent drift`
- `OpenSPDD design philosophy capability control AI coding`
- `SPDD concept-driven codebase exploration domain nouns action verbs API surfaces`
- `Structured-Prompt-Driven Development Fowler REASONS Canvas prompt update sync`
- `OpenSPDD spdd-analysis spdd-reasons-canvas spdd-generate spdd-sync templates`
- `SPDD Abstraction First Alignment Iterative Review Fowler Thoughtworks`
- `SPDD API test expected actual TEST CASE OVERVIEW cURL script`
- `SPDD asset integrity prompt version code commit`
- `SPDD spec-anchored spec-as-source spec-driven development`
- `SPDD model drift configuration drift command semantics review protocol`
- `SPDD hotfix production signal prompt update postmortem`
- `OpenSPDD spdd-reasons-canvas command template @file read all referenced files no truncate`
- `OpenSPDD spdd-generate Operations sequence Norms Safeguards structured prompt`
- `Structured Prompt Driven Development generate sync traceability REASONS Canvas`
- `SPDD prompt first sync code drift operations safeguards`
- `OpenSPDD spdd-code-review intent drift implicit decisions`
- `OpenSPDD spdd-api-test scripts/test-api.sh curl generated tests`
- `SPDD API tests token billing example modelId negative tokens`
- `SPDD prompt update sync behavior preserving refactor`
- `REASONS Canvas code review safeguard violations scope creep`
- `OpenSPDD spdd-api-test generated artifact test case table expected actual`
- `OpenSPDD spdd-code-review intent drift implicit decisions scope boundary`
- `SPDD prompt update sync code first prompt first correction lanes`
- `spec anchored spec as source AI coding assistants prompt as code`
* `OpenSPDD design philosophy control problem AI coding too many ideas`
* `SPDD practitioner guide openspdd init generate all folder layout`
* `spdd-prompt-update minimal change preserve REASONS Canvas no code blocks`
* `spdd-sync Operations section update plan prompt code drift`
* `OpenSPDD optional commands spdd-reverse spdd-story beta`

## Кандидаты на иллюстрации

Кандидаты возвращены внутрь `SPDD_METHOD_DOSSIER.md` и сгруппированы по смыслу. Это не финальный asset manifest: перед вставкой на сайт изображения нужно отдельно проверить, сохранить локально и привязать к конкретным местам текста.

### Основные схемы SPDD: prompt as artifact, REASONS Canvas и intent loop

* Diagram: `informal intent → REASONS Canvas → code → API evidence/review → prompt update/sync`, with feedback arrows.
* Comparison table: “Plan”, “REASONS Canvas”, “формальная спецификация”, “test oracle”.
* Failure diagram: wrong Canvas → correct generation → wrong product behavior.
* Screenshot / code block from OpenSPDD README: “Plan vs REASONS Canvas” example for user registration.
- Diagram: `REASONS Canvas → /spdd-generate → code → /spdd-api-test → /spdd-code-review → prompt-update/sync`.
- `fig-spdd-verification-loop` — `/spdd-code-review`, `/spdd-api-test`, `/spdd-sync` — Canvas → code → API script/table → review report → prompt-update/sync — Показывает SPDD as evidence-and-repair loop, not just prompt-first generation.
- `fig-spdd-four-layer-loop` — [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md), [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md), OpenSPDD README — Context ingestion → REASONS Canvas → Generate by Operations → Sync/review back to Canvas. — Центральная схема для глубокий якорь: показывает SPDD как artifact loop, а не template.
- `fig-spdd-context-ingestion-gate` — [`/spdd-reasons-canvas`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) — `@requirements.md`, `@api-spec.yaml`, `@folder` → full read / no truncation → consolidated business context. — Показывает новый слой, которого раньше почти не было: reading discipline before design.
- `fig-spdd-traceability-risk` — OpenSPDD README + design philosophy — Canvas ↔ code sync; drift path if sync forgotten. — Нужна как warning illustration, чтобы не идеализировать SPDD.
- `fig-spdd-reasons-canvas` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Схема/картинка REASONS Canvas. — Центральная иллюстрация досье: seven-part structure intent/design/execution/governance. — Кандидат на локальное сохранение.
- `fig-spdd-final-adjustments` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Изображение около code review & final adjustments. — Полезно для объяснения двух путей: logic correction через prompt update и refactoring через sync. — Кандидат, но менее приоритетен, чем Canvas/рабочий процесс.
- `fig-fowler-spdd-overview` / `assets/theory-images/fowler-spdd-overview.svg` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Prompt как first-class delivery artifact. — Показывает главный сдвиг: prompt не исчезает после генерации, а становится версионируемым и ревьюируемым артефактом. — В начале раздела SPDD или рядом с объяснением intent artifact. — Уже локально вставлено в текущую теорию; можно переиспользовать.
- `fig-fowler-spdd-рабочий процесс` / `assets/theory-images/fowler-spdd-рабочий процесс.svg` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Рабочий процесс: business input → analysis → structured prompt → generation → validation/review → sync. — Поддерживает шесть стадий и идею распределённого подтверждения намерения. — В разделе рабочий процесс. — Уже локально вставлено.
- `fig-fowler-reasons-canvas` / `assets/theory-images/fowler-reasons-canvas.svg` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — REASONS Canvas. — Нужна для раскрытия Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards. — В разделе Canvas. — Уже локально вставлено.
- `fig-fowler-spdd-api-test-script` / `assets/theory-images/fowler-spdd-api-test-script.png` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Human-reviewable test-case overview для API test script. — Показывает, что evidence должен быть человекочитаемым до запуска. — В разделе API validation. — Уже локально вставлено.
- `fig-fowler-spdd-api-test-results` / `assets/theory-images/fowler-spdd-api-test-results.png` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Summary expected/actual/pass-fail результатов API tests. — Показывает вторую половину свидетельства: не слова агента, а проверяемый результат. — В разделе validation/evidence. — Уже локально вставлено.
- `fig-fowler-spdd-code-review` / `assets/theory-images/fowler-spdd-code-review.svg` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Два варианта реакции на review comment: менять код напрямую или сначала обновлять prompt. — Нужна для различения logic correction и refactoring. — В разделе prompt-update/sync. — Уже локально вставлено.
- `fig-fowler-spdd-prompt-update` / `assets/theory-images/fowler-spdd-prompt-update.png` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Пример prompt update перед изменением кода. — Хорошо показывает, что business-rule correction не должен растворяться в локальном патче. — В разделе prompt-update / billing example. — Уже локально вставлено.
- `fig-openspdd-repo-vs-feature-artifacts` / candidate — [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) — `AGENTS.md`/`CLAUDE.md` как уровня репозитория conventions vs REASONS Canvas как уровня фичи contract. — Помогает не смешивать project constitution и feature intent artifact. — В сравнении SPDD с context engineering / project instructions. — Кандидат для собственной схемы.
- `fig-spdd-prompt-code-evidence-sync` — combined OpenSPDD commands — Canvas / code / tests / review / sync loop — Главная иллюстрация для SPDD deep-anchor section.
* OpenSPDD README “Plan vs REASONS Canvas” example for user registration as a compact before/after illustration.
* Spectrum: informal prompt → REASONS Canvas → tests/contracts → formal specs/DSL.
* Feedback loop: Canvas → generate → API evidence → code review → prompt update/sync.
* Wrong-Canvas failure path: precise artifact, faithful code, wrong business behavior.
- Диаграмма source-precedence для Canvas: текущая задача → предыдущий Canvas → analysis context → кодовая база → новый REASONS Canvas; рядом показать failure mode, когда один из источников silently выпадает.
- Спектр формализации: свободным prompt → structured requirements → REASONS Canvas → формальная спецификация; SPDD отмечен как daily-use средний слой.
- `fig-spdd-reverse-lifecycle` — [`/spdd-reverse` template](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md) — Схема подключение legacy-кода: existing code → analyze → reverse-engineer REASONS Canvas → normal SPDD cycle. — Показать SPDD как двунаправленную петлю, а не только forward-flow от требований к коду.
- `fig-spdd-daily-planner-loop` — `github/gh-aw` daily planner рабочий процесс — Spec files → rotation cache → `/spdd-analysis` → `/spdd-reasons-canvas` → `/spdd-generate` → `/spdd-sync` → daily issue. — Показать SPDD как периодическое сопровождение spec-корпуса, а не только интерактивную фичу.
- `fig-spdd-integration-surface` — CodeMie issue + OpenSPDD templates — Tool shell вокруг Canvas: commands, traceability, sync, issue/task output. — Показать SPDD как capability, которую можно встроить в другие агентные инструменты.

### Проверка и свидетельства: API tests, code review, correction lanes

* Spectrum graphic: tests / code contracts / logical contracts / DSLs, with SPDD positioned as practical structured-intent + lightweight evidence layer.
* Small flowchart: behavior change → `/spdd-prompt-update`; pure refactor → `/spdd-sync`; verification issue → `/spdd-code-review` / `/spdd-api-test`.
- Screenshot / excerpt of `/spdd-api-test` template showing structured test-case overview и result table.
- Screenshot / excerpt of `/spdd-code-review` output schema: traffic-light summary, intent drift table, implicit decisions и overall merge-readiness verdict.
- `fig-spdd-code-review-report` — [`/spdd-code-review`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-code-review.md) — Report structure: REASONS alignment, drift, safeguards, implicit decisions, scope — Хорошая иллюстрация semantic review surface.
- `fig-spdd-api-test-artifact` — [`/spdd-api-test`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-api-test.md) — Generated shell script + test-case table — Показывает поведенческое свидетельство artifact.
- `fig-openspdd-code-review-drift` / candidate — [`/spdd-code-review`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md) — REASONS alignment + intent drift + safeguards + scope boundary. — Хорошо показывает, что review проверяет не «код красивый», а соответствие intent artifact. — Раздел verification / review / evidence. — Кандидат для собственной схемы.
- `fig-spdd-two-review-lanes` / candidate — [WebReactiva SPDD vs SDD](https://www.webreactiva.com/blog/spdd) + primary SPDD prompt-update/sync sources — Два carriles: behavior change → update prompt first; pure refactor → sync after code. — Очень сильная практическая схема для Handbook/Fieldbook. — Раздел review / sync / drift. — Кандидат; лучше перерисовать по первичным и secondary sources.
- `fig-spdd-review-table` — `/spdd-code-review` output shape — Схема отчёта review: section alignment, drift, safeguards, implicit decisions — Удобно вставлять в verification/review главу.
- `fig-spdd-api-test-shell` — `/spdd-api-test` generated script — Пример shell script + cURL test cases — Показывает, что evidence layer is concrete и runnable.

### Синхронизация, drift и repair-loop

* Lifecycle diagram: `requirements/` → `spdd/analysis/` → `spdd/prompt/` → generated code → `/spdd-prompt-update` or `/spdd-sync` → commit prompt + code together.
- `fig-spdd-two-correction-lanes` — WebReactiva walkthrough + `/spdd-prompt-update` / `/spdd-sync` — Behavior-changing correction vs behavior-preserving code change — Объясняет, почему SPDD is not “never edit code”.
* `/spdd-sync` Prompt Sync Plan checklist: Entities / Structure / Operations / Norms / Safeguards updates.
- `fig-spdd-correction-lanes-simple` — WebReactiva guide + OpenSPDD command templates — Behavior change → `/spdd-prompt-update`; pure refactor → `/spdd-sync`. — Дать читателю простой decision gate for correction lanes.

### Сравнительные и риск-схемы

* Диаграмма “capability vs control”: модельная способность растёт, но human design trade-offs need explicit boundary artifacts.
- Comparative diagram: spec-anchored vs SPDD hybrid vs spec-as-source.
- `fig-spdd-operations-as-execution-order` — [`/spdd-generate`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) — Operations as ordered task graph with Norms/Safeguards applied to every generated code step. — Полезно для сравнения с Spec Kit `tasks.md`, BMAD story context и GSD execution gates.
- `fig-sdd-three-tools-overview` — [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — Обзорные схемы spec-driven development tools. — Использовать осторожно как сравнительный фон для spec-first/spec-anchored/spec-as-source, не как SPDD-specific source. — Вторичный кандидат.
- `fig-fowler-sdd-overview` / `assets/theory-images/fowler-sdd-overview.png` — [Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — Общая схема spec-driven workspace: memory bank, agent, specs. — Полезна для сравнения SPDD с более общей SDD-рамкой. — В вводном сравнении SPDD / SDD, если нужна карта соседнего пространства. — Уже локально вставлено в ранней части теории; использовать осторожно, чтобы не смешать SPDD и общий SDD.
- Скриншот/схема daily SPDD planner issue: список прочитанных spec files → P0/P1/P2 queue → SPDD checklist.

### Уже локально сохранённые assets / кандидаты к переиспользованию

- `fig-spdd-prompts-first-class-artifacts` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Изображение рядом с блоком `Prompts as First-Class Delivery Artifacts`. — Хорошо подходит для открытия SPDD-раздела: prompt становится delivery artifact. — Кандидат на локальное сохранение, если в текущих assets его ещё нет.
- `fig-spdd-рабочий процесс` — [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) — Рабочий процесс image около SPDD рабочий процесс. — Показывает closed loop и prompt/code co-evolution. — Кандидат на локальное сохранение.

### Дополнительные визуальные кандидаты SPDD

* Negative-space card: examples of things AI must not infer: architecture style, currency scope, touched boundaries, retry strategy.
- `fig-openspdd-story-template` / candidate — [`/spdd-story`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) — Command-template header / steps for story decomposition и INVEST evaluation. — Показывает, что SPDD начинается до engineering design: business input is converted into scoped stories before code analysis. — Раздел о входной стадии SPDD or context/story preparation. — Кандидат; если использовать, лучше не скриншот GitHub, а локальная diagram/table reconstructed from source.
- `fig-openspdd-analysis-concept-exploration` / candidate — [`/spdd-analysis`](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) — Concept-driven codebase exploration: fingerprint → domain nouns/action verbs/API surfaces → targeted files → one-hop expansion. — Очень полезно для theory chapter on context engineering: модель не читает всё, а строит bounded source map. — Раздел о context extraction / analysis phase. — Кандидат для собственной схемы; права проще, если перерисовать.
- `fig-openspdd-tool-adapter-map` / candidate — [OpenSPDD README](https://github.com/gszhangwei/open-spdd/blob/main/README.md) — Карта: Claude/Cursor/GitHub Copilot/OpenCode/Codex → разные места установки команд/skills. — Показывает SPDD как переносимая дисциплина командных шаблонов, а не специфичный для Claude рабочий процесс. — В разделе об инструментальных поверхностях и переносимых артефактах намерения. — Кандидат для собственной схемы; лучше перерисовать, не скриншот README.
* Capability/control diagram from OpenSPDD design philosophy: useful as a simple conceptual figure for why stronger models still need intent boundaries.
* Practitioner folder tree from WebReactiva (`requirements/`, `spdd/analysis/`, `spdd/prompt/`, `scripts/test-api.sh`, `src/`).
* Negative-space checklist: “не трогать”, “не выбирать самому”, “не расширять scope”, “не менять architecture style”.
- Схема portability layer: один SPDD lifecycle → несколько adapter surfaces: Claude Code, Cursor, Codex, OpenCode, Copilot prompts, GitHub workflow.
- `fig-spdd-reverse-scope-gate` — [`/spdd-reverse` template](https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md) — Scope confirmation при большой области: список файлов → подтверждение/сужение. — Объяснить human gate при кодификации legacy-кода.
- `fig-openspdd-adoption-friction-map` — [OpenSPDD issues](https://github.com/gszhangwei/open-spdd/issues) — Маленькая карта трений: context capture, Codex/OpenCode support, install/module path. — Показать, что методология зависит от инструментальной доставки команд и контекста.

## Открытые вопросы и следующий возможный проход

Открытые вопросы сведены в единый список без привязки к номерам проходов.

- Нужно ли теперь разделить SPDD-досье на два слоя: Thoughtworks/Fowler methodology и OpenSPDD command-template mechanics? Сейчас они связаны, но не идентичны.
- Нужно ли для теории отдельно раскрыть `/spdd-code-review` как мост между SPDD и verification harness, а не держать его в хвосте SPDD?
- Нужно ли оценить token/process cost OpenSPDD commands на реальных задачах: command templates require full reference reading и structured outputs, что может быть дорого.
- Нужно ли в будущем досье открывать внешние источники заново и переносить детали, которые в текущей теории уже были сжаты? Сейчас досье сохраняет только уже перенесённую фактуру.
- Насколько сильно нужно привязывать SPDD к OpenSPDD command templates? Текущая теория использует команды как рабочую конкретику, но не раскрывает полный CLI/install/setup слой.
- Нужно ли отдельно проверять фактическое состояние testing commands: в текущей теории отмечено, что dedicated testing commands на момент статьи ещё не finalized, но это может измениться.
- Нужно ли выделять SPDD как центральную отдельную часть теории или оставить как сильный узел внутри раздела об intent artifacts?
- Нужно ли добавить отдельный comparative pass против Spec Kit, Kiro, BMAD, GSD и Constitutional SDD, чтобы не перегрузить SPDD ролью универсальной методологии?
- Как строго переводить устойчивые английские термины: `intent asset`, `delivery artifact`, `asset integrity`, `sync`, `prompt/code consistency`? В текущем досье часть терминов оставлена английскими, потому что это термины источников и корпуса.
- Нужно ли в будущем выделить `/spdd-reverse` как отдельный brownfield / legacy-onboarding механизм, а не оставлять его в хвосте optional commands?
- Нужно ли в теории явно развести `AGENTS.md`/`CLAUDE.md` как уровня репозитория instructions и REASONS Canvas as уровня фичи контракт дизайна?
- Нужно ли добавить warning box: stale Canvas can be worse than no Canvas, если `/spdd-sync` не становится реальной дисциплиной?
- Нужно ли в Handbook формализовать вопрос “does observable behavior change?” как routing gate между `/spdd-prompt-update` и `/spdd-sync`?
- Нужен ли отдельный mini-dossier по `/spdd-code-review` как verification-harness, или достаточно включить его в общую главу о проверке?
- Как в будущей теории отделить сильное требование context integrity from impractical “read everything” token explosion?
- Стоит ли прямо сравнить `Operations` из REASONS Canvas with Spec Kit `tasks.md`, BMAD story context и Gas Town/Beads граф работы?
- Нужен ли visual/source audit по примерам реальных generated Canvas files in token-billing repository?
- Нужно ли выделить `/spdd-api-test` в отдельный subsection будущей главы о verification artifacts, или оставить его внутри SPDD anchor case?
- Насколько SPDD в нашем тексте следует позиционировать как spec-anchored hybrid, а не как spec-as-source regime?
- Нужно ли отдельно сравнить `/spdd-code-review` with other review/harness cases: Willison evidence artifacts, Sandvault policy, babysit-pr triage, GSD validation gates?
* Насколько `/spdd-sync` реально устойчив в большом legacy-codebase, где фактическая реализация уже давно не соответствует исходному Canvas?
* Нужно ли в теории отдельно выделить “minimal patch discipline” как самостоятельный механизм SPDD, наряду с REASONS Canvas?
* Стоит ли использовать `spdd-reverse` как отдельный brownfield-onboarding пример или оставить его как осторожно упомянутый optional beta lane?
* Где провести границу между SPDD и broader spec-driven tools: prompt-as-contract vs spec-as-project-plan vs task graph?
* Нужно ли в будущей теории явно связать SPDD with Lahiri-style intent formalization, or это перегрузит главу академическим слоем?
* Где провести границу между pragmatic REASONS Canvas и formal/checkable specifications?
* Должен ли future SPDD рабочий процесс require `/spdd-api-test` by default for high-risk features, or optional evidence layer достаточно?
* Как проверять correctness самого Canvas, если only human user is the real oracle?
* Нужно ли в будущей теории выделить плановое сопровождение спецификаций режим SPDD отдельно от feature-loop режима?
* Стоит ли использовать `gh-aw` daily planner как полноценный пример или только как короткий signal of adoption, учитывая что это рабочий процесс-файл, а не статья с ретроспективой?
* Где граница между полезной интеграцией OpenSPDD в IDE/CLI и скрытием Canvas от человека, которое разрушает intent review?
* Нужно ли для нашего многопроходного документного процесса заимствовать SPDD-like rotation cache и write-preflight дисциплину для обхода документов?

## Языко-стилевые и редакционные замечания
### Языко-стилевые замечания

В добавленном материале обычные английские слова переведены: `рабочий процесс` передан как “рабочий процесс” или оставлен только там, где речь о точном имени файла GitHub Actions; `review` — как “проверка” или “ревью”, когда речь о процедуре; `source` — как “источник”; `evidence` — как “свидетельство” или “проверяемый артефакт”. Латиницей оставлены только имена команд, файлов, проектов и точные термины вроде `OPENSPDD_REF`, `.github/copilot-prompts`, `/spdd-sync`, `rotation cache`.
