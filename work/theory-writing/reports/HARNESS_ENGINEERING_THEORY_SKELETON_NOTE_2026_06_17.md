# Harness Engineering and the Theory skeleton

Дата: 2026-06-17.  
Статус: рабочая заметка для следующего обновления skeleton / chapter packages.  
Связанные решения: `ADR-0012`, `ADR-0014`, `ADR-0018`, `THEORY_CHAPTER_ATTACHMENT_MAP.md`, `ATLAS_V2_LAYER_ARTICLE_MAP.md`.

## Короткий вывод

Да, Harness Engineering нужно отразить в Теории, но не как новую главу и не как новый главный разрез. Это сквозная рамка, которая помогает сказать точнее:

```text
агентская разработка работает не потому, что модель «пишет код»,
а потому, что модель включена в рабочую обвязку:
контекст проекта, инструменты, среду исполнения, состояние, проверки,
права, следы выполнения, маршруты принятия и петли восстановления.
```

Верхний скелетон Теории остаётся построенным по жизненному циклу изменения. Harness Engineering даёт не структуру книги, а объяснительный слой внутри этой структуры.

## Почему это важно

После решений о разрезах корпуса стало ясно:

- Теория не должна становиться техническим Атласом;
- Атлас не должен быть приложением к Теории;
- технологии должны жить в Атласе как полноценные слои;
- Теория должна быть технологически заземлена, но не перегружена техническими каталогами.

Harness Engineering помогает держать этот баланс. Он связывает части Атласа в одну системную рамку и одновременно защищает Теорию от двух ошибок:

```text
ошибка 1: объяснять успех/сбой только качеством модели;
ошибка 2: превращать теоретическую главу в перечень инструментов.
```

## Рабочая терминология

В английском источниковом поле можно использовать `Harness Engineering`, `agent harness`, `model-harness-environment system`.

В русском тексте не нужно насильно переводить термин каждый раз. Рабочие варианты:

- `рабочая обвязка агента`;
- `системная обвязка агента`;
- `обвязка вокруг модели`;
- `модель + обвязка + среда`.

Нежелательно превращать это в тяжёлый термин вроде `харнесс-инжиниринг` в публичном русском тексте. Английский термин можно дать в скобках при первом введении.

## Как это входит в главы

### Introduction

Ввести главный поворот:

```text
важен не только выбор модели, а вся система, через которую модель получает контекст, действует, проверяет себя и передаёт результат в процесс принятия.
```

Это помогает объяснить, почему корпус изучает жизненный цикл изменения, а не «лучшие промпты» или «лучшую модель».

### I. Unit of analysis

Уточнить: единицей анализа является не prompt, не run, не diff и не модельный output, а изменение, проходящее через `model + harness + project environment`.

### VI. Project as working support

Показать, что репозиторий, документация, rules, specs, ADR, AGENTS/CLAUDE/Kiro steering и другие project-context артефакты — это не просто справка для модели, а часть рабочей обвязки.

### IX. Runtime, tools and permissions

Сделать Harness Engineering наиболее явным: tools, MCP, sandbox, filesystem, browser, command execution, approvals and permissions — это именно та среда, через которую модель получает способность действовать.

### XI. Verification material

Показать, что tests, traces, logs, static analysis, browser feedback, evals and diagnostics — это feedback/sensor layer. Они не просто «проверки после работы», а часть петли самокоррекции и доверия.

### XII. Acceptance and authority

Провести границу: harness может собрать материал, провести проверки и довести PR до review, но право признать изменение завершённым возникает только в социально-техническом контуре принятия.

### XIII. After merge

Показать, что post-merge monitoring, rollback, cleanup, обновление rules, memory and process artifacts — это обратная связь, которая меняет будущую обвязку.

### Conclusion

Свести практический вывод:

```text
прогресс в агентской разработке достигается не только ожиданием более сильной модели,
а проектированием минимально достаточной обвязки вокруг уже достаточно сильных моделей.
```

## Что не делать

1. Не добавлять отдельную главу «Harness Engineering».
2. Не переименовывать всю Теорию в книгу про harness.
3. Не заменять `экзоскелет`, `protected process profiles`, `Persistent Work Graph` и другие внутренние понятия новым модным термином.
4. Не делать в Теории список всех компонентов harness. Это задача Атласа.
5. Не использовать термин как декоративный англицизм. Он нужен только там, где помогает связать модель, среду и процесс.

## Новый gate для chapter packages

Добавить к будущим chapter packages короткий `harness-frame check`:

```text
1. Не объясняет ли глава успех/сбой только качеством модели, когда причина в обвязке?
2. Какие элементы обвязки реально участвуют в аргументе главы?
3. Какие детали нужно оставить Атласу?
4. Не превращается ли глава в каталог harness-компонентов?
5. Возвращается ли урок главы в изменение будущей обвязки: rules, tools, tests, memory, routing, permissions, review gates?
```

Этот check должен идти рядом с `atlas-technical-grounding check`.

## Relation to Atlas

Atlas A1–A16 можно читать как техническую декомпозицию рабочей обвязки coding-agent development. Но это не значит, что нужна отдельная статья A17 `Harness Engineering`. Сейчас лучше держать Harness Engineering как:

- введение/рамку к Атласу;
- сквозную рамку в Теории;
- контрольный вопрос в Рабочих сценариях;
- диагностическую ось в Каталоге проблем и решений.

Если позже появится потребность, можно сделать обзорную intro-страницу Атласа: `Что такое agent harness и как читать технические слои Атласа`. Но это не конкурирует с A1–A16.

## Source hints for future packages

External anchors to consult when rebuilding the relevant chapters:

- LangChain, `The Anatomy of an Agent Harness` — agent = model + harness; harness includes tools, state, execution environment, constraints and feedback loops.
- Martin Fowler / Thoughtworks, `Harness engineering for coding agent users` — coding-agent user harness, feedforward/feedback, guides and sensors, maintainability/architecture/behaviour harnesses.
- OpenAI, `Harness engineering: leveraging Codex in an agent-first world` — practical example: missing environment/tooling/legibility rather than missing model capability; app UI/logs/metrics made legible to Codex.
- Zhong & Zhu, `AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents` — model-harness-environment system, task specification, context selection, tool access, project memory, task state, observability, verification, permissions and intervention recording.
- O’Reilly Radar, `Agent Harness Engineering` — public synthesis of prompts/tools/MCP/sandboxes/orchestration/hooks/observability as harness components.

## Application to already written chapters

Рамка Harness Engineering должна применяться к уже написанным главам через живую карту приложений:

```text
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
```

Не заводить отдельный параллельный patch map для уже написанных глав: все такие решения должны согласовываться в одной карте вместе с Atlas layers, ex-A3, старыми фрагментами, story anchors and source gaps. Будущий patch package должен сначала показать точный список точечных правок к главам I–X and companion files, затем остановиться на human checkpoint.
