# Проект новой теоретической части

# «Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения»

Дата: 2026-06-05

## 0. Рабочий вывод

Рамка **AI-driven SDLC** имеет смысл как новая верхняя архитектура теоретической части, но только в сильном варианте: не как таблица «AI в requirements / design / coding / testing / deployment», а как описание того, как меняется **жизненный цикл программного изменения**.

Единица анализа в новой версии должна быть не `prompt`, не «модель», не конкретный инструмент и не отдельный кейс, а **изменение в программной системе**, проходящее через контур:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

Это не waterfall. В агентской разработке эти стадии часто идут петлями, возвращаются назад и меняют саму среду работы: инструкции, тесты, hooks, skills, MCP, `AGENTS.md`, review policy, benches, workflow scripts, человеческие gates.

Главная структурная правка по сравнению с текущей expanded-версией:

- «карта течений» остаётся источниковой и аналитической базой;
- финальная теория строится вокруг lifecycle-оси;
- кейсы перестают быть равноправными станциями каталога;
- SPDD и Gas Town становятся глубокими вертикальными срезами lifecycle, а не обычными примерами.

## 1. Почему эта рамка лучше чинит текущую проблему

### 1.1. Что было сильным в старой версии

Старая теория лучше держала композицию: каждая часть отвечала за аспект общего сдвига — от удачного запроса к рабочей среде, контекст и намерение, обвязка и проверка, среда выполнения, Gas Town, свидетельства, ответственность, вывод для Handbook.

Её слабость была не в форме, а в недостатке фактуры и современных источников.

### 1.2. Что было сильным и слабым в expanded-версии

Expanded-версия дала много фактуры: SWE-chat, Programming by Chat, SPDD, harness engineering, Codex/GitHub/Jules/Claude Code, SASE, policy cluster, security/governance, tests/benchmarks/debt, Gas Town/DoltHub.

Но она начала распадаться на source dossier: источники и кейсы слишком часто становились единицами композиции.

### 1.3. Что даёт AI-driven SDLC

AI-driven SDLC возвращает последовательность: каждый материал должен отвечать на вопрос, **какую часть жизненного цикла программного изменения он перестраивает**.

Это помогает:

- не путать ускорение coding с улучшением lifecycle;
- показать, почему генерация кода переносит нагрузку в review, evidence, governance и сопровождение;
- объяснить, почему проект становится интерфейсом агента;
- связать локальные рабочие сцены, платформенные агенты, deep cases и open-source boundaries;
- напрямую связать теорию с Handbook/Fieldbook: Handbook становится картой выбора режима в lifecycle.

## 2. Основная модель документа

Документ должен держаться на двух осях.

### 2.1. Горизонтальная ось: lifecycle программного изменения

| Слой lifecycle | Что меняется в агентской разработке | Типичные источники |
|---|---|---|
| Намерение | запрос перестаёт быть одноразовой фразой и становится артефактом управления | SPDD, Spec Kit, Kiro, TDAD, Promptware |
| Контекст | контекст становится рабочей средой, а не только prompt window | AGENTS.md, Claude Code docs, Mark Erikson dev plans, Boris Tane research/plan |
| Делегирование | задача выбирает режим: разговор, исследование, план, spec, workflow, PR, background agent | SWE-chat, Programming by Chat, 12 stories |
| Исполнение | модель действует через harness, tools, permissions, sandbox, worktree, MCP, hooks, skills | Fowler Harness, Codex, Copilot cloud agent, Claude Code, SWE-agent |
| Свидетельства | результат должен оставлять проверяемый evidence package | tests, logs, terminal outputs, benchmarks, PR descriptions |
| Ревью | bottleneck переносится от генерации к проверке, коммуникации и review capacity | PR studies, Jökull, Code Review Agent Benchmark |
| Право завершения | operational agency не даёт права merge / publish / accept | SASE, Linux/QEMU/LLVM policy cluster, GitHub governance |
| Хвост lifecycle | сбои возвращаются в среду: инструкции, тесты, skills, policies, debt control | DORA, Bain, Agentic Technical Debt, OpenSSF, Snyk cautiously |

### 2.2. Вертикальная ось: deep anchor cases

Deep cases не должны стоять как «ещё примеры». Они должны прорезать несколько слоёв lifecycle сразу.

- **SPDD** показывает спецификационный lifecycle: от story до analysis context, canvas, generation, API-test, code review, prompt update и синхронизации артефактов.
- **Gas Town / Beads** показывает организационно-операционный lifecycle: роли, rigs, Mayor, Beads, Witness/Deacon/Dogs, Refinery, GUPP/NDI, escalation, session continuation, verification и цену orchestration.
- **SWE-chat / Programming by Chat** дают эмпирическую поверхность обычной агентской сессии: prompts, tool calls, user correction, progressive specification, survival of generated code.
- **Open-source policy cluster** показывает внешний предел lifecycle: чужой проект не обязан принимать AI-generated work, даже если он технически полезен.

## 3. Предлагаемая структура документа

Ниже структура не как окончательное оглавление, а как проект верхней архитектуры. Внутренние подразделы можно менять после утверждения общей линии.

---

# Введение. Почему речь не о генерации кода

## Управляющий тезис

AI-driven SDLC начинается там, где AI перестаёт быть ускорителем набора кода и начинает менять весь lifecycle программного изменения: намерение, контекст, среду исполнения, свидетельства, ревью, governance и сопровождение.

## Функция

Сразу защитить документ от двух неверных чтений:

1. «это про vibe coding / prompt engineering»;
2. «это обычная корпоративная схема SDLC с AI на каждой фазе».

## Источники

- DORA 2025 — AI как усилитель существующей организационной системы.
- Bain 2025 — ценность приходит от применения AI по всему lifecycle и redesign процессов, а не только от ускорения coding.
- A-SDLC survey и Assistance-to-Autonomy SLR — внешняя проверка, что рамка SDLC действительно стала отдельной линией обсуждения.

## Подразделы

1. Почему «код стал дешевле» — недостаточное описание.
2. Software-change lifecycle как единица анализа.
3. Чем AI-driven SDLC отличается от классического SDLC.
4. Как читать deep cases: SPDD, SWE-chat, Gas Town, policy cluster.
5. Как эта теория связана с Handbook и Fieldbook.

---

# Часть I. Единица анализа: программное изменение, а не prompt

## Управляющий тезис

Агентская разработка становится понятной только если смотреть не на отдельный prompt, а на весь контур изменения: кто формулирует намерение, где живёт контекст, что делает агент, какие следы остаются, кто проверяет и кто имеет право завершения.

## Функция в документе

Задать читателю базовую схему lifecycle, к которой будут привязаны все дальнейшие кейсы. Эта часть должна быть короткой, рамочной и композиционно сильной. Deep case здесь не нужен.

## Anchor / framing sources

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| DORA 2025 | AI как amplifier организационной системы | 8.5 | 9 | framing, не кейс |
| Bain 2025 | bottleneck выходит за пределы coding/testing | 8 | 9 | framing, не кейс |
| A-SDLC survey | внешняя карта термина Agentic SDLC | 7.5 | 8 | cautiously as external map |
| Assistance-to-Autonomy SLR | verifiability, bounded spaces, зрелость фаз | 8.5 | 9 | framing + later evidence |
| Old baseline theory | композиционный контроль | 9 | 10 | использовать как форму, не как факт-источник |

## Возможные подразделы

1. От модели к контуру работы.
2. От фазы SDLC к жизненному циклу изменения.
3. Вертикальные срезы вместо каталога кейсов.
4. Почему lifecycle не завершён после commit.
5. Как читать следующие части.

## Что не включать

- Не раскрывать здесь SPDD и Gas Town.
- Не делать длинный обзор всех AI-SDLC papers.
- Не вставлять market material кроме короткой рамки.

---

# Часть II. Реальная агентская сессия: трасса, вмешательство, выживание результата

## Управляющий тезис

Первичная эмпирическая поверхность agentic SDLC — не обещание модели и не финальный diff, а сессия: последовательность prompts, tool calls, corrections, misunderstandings, проверки и кода, который либо выживает, либо исчезает.

## Функция

Поставить под теорию реальную рабочую поверхность. После этой части читатель должен понимать, что lifecycle начинается не с красивой методологии, а с грязной, частично управляемой сессии, где человек постоянно корректирует, сужает, проверяет и переводит работу на следующий слой.

## Anchor cases

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| SWE-chat | deep empirical anchor | 10 | 10 | раскрывать крупно |
| Programming by Chat | secondary anchor: progressive specification | 8.5–9 | 9 | раскрывать рядом |
| How Coding Agents Fail Their Users | misalignment/pushback layer | 8.5 | 9 | аналитическое углубление |
| Why AI Agents Still Need You | пошаговое взаимодействие vs one-shot | 7.5–8 | 8 | medium support |
| 12 stories | практический корпус | 8–10 по отдельным историям | 9 | story links |

## Возможные подразделы

1. Сессия как evidence surface.
2. Что показывают реальные логи: prompts, tool calls, commits, survival.
3. Progressive specification: намерение уточняется в диалоге.
4. Misalignment: агент работает, но не туда.
5. Почему one-shot подход плохо описывает реальную работу.
6. Переход к следующей части: если сессия порождает намерение, его надо вынести наружу.

## Контрасты

- «AI написал код» как слабое описание.
- Vibe coding без остаточного следа.
- Успешный локальный diff, который не выдерживает lifecycle.

## Что переносить в Handbook/Fieldbook

- Практические сцены остановки агента.
- Примеры перехода от лёгкой сессии к исследованию или плану.
- Локальные prompt patterns.

---

# Часть III. Намерение: от запроса к артефакту управления

## Управляющий тезис

AI-driven SDLC начинается всерьёз тогда, когда намерение перестаёт жить только в чате и превращается в проверяемый, пересматриваемый, версионируемый артефакт, способный управлять генерацией, проверкой и последующим исправлением.

## Функция

Показать первый крупный механизм новой теории: request → durable intent artifact. Здесь естественное место для SPDD.

## Deep anchor case: SPDD

**Оценка:** 10 по текущей шкале. В рамке AI-driven SDLC SPDD может даже стать 10.5, потому что он показывает не просто хороший case, а почти полный спецификационный lifecycle.

SPDD должен быть раскрыт не как «методика prompt-driven development», а как цепочка:

1. story shaping;
2. analysis context;
3. REASONS Canvas;
4. generation;
5. API-test before review;
6. code review;
7. prompt update / sync;
8. сохранение prompt as first-class delivery artifact.

## Secondary / contrast materials

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| OpenSPDD | команды и операционная оболочка | 9 | 10 | включать в deep case |
| GitHub Spec Kit | spec-first industrial contrast | 7.5 | 8.5 | medium contrast |
| Kiro Specs | specs as product workflow | 7 | 8 | medium contrast |
| TDAD | поведение агента как тестируемый объект | 7.5 | 8.5 | контраст / bridge to Part VIII |
| Constitutional SDD | machine-readable constraints | 7 | 8 | контраст security/governance |
| Promptware papers | prompt as artifact | 7 | 8 | theory support |
| V-Bounce | фазовая AI-native SDLC альтернатива | 5.5–6.5 | 6 | cautious contrast only |

## Возможные подразделы

1. Почему prompt слишком слаб как единица управления.
2. Intent artifact: что должно переживать сессию.
3. SPDD как глубокий спецификационный lifecycle.
4. Spec Kit / Kiro / TDAD: соседние формы спецификационной дисциплины.
5. Риск stale spec: артефакт намерения может стать источником ложной уверенности.
6. Переход: намерение без контекста не исполняется.

## Что не делать

- Не превращать раздел в обзор всех spec-first tools.
- Не вытеснять SPDD множеством средних кейсов.
- Не смешивать intent artifact с полным harness: это следующая часть.

---

# Часть IV. Контекст и рабочее состояние: проект как интерфейс агента

## Управляющий тезис

В AI-driven SDLC контекст — это не содержимое prompt window, а поддерживаемое рабочее состояние проекта: инструкции, планы, research notes, dev plans, style rules, task memory, repo layout, examples, failure history и границы действия.

## Функция

Показать, что агентская работа требует внешней памяти и проектной поверхности. Эта часть соединяет SPDD с harness: намерение уже вынесено наружу, но теперь нужно показать, где живёт контекст, который делает агентскую работу воспроизводимой.

## Anchor / medium materials

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| AGENTS.md / OpenAI Codex docs | repo-level instructions as working memory | 8 | 9 | раскрывать как platform primitive |
| Claude Code docs | CLAUDE.md, Skills, hooks, subagents, MCP | 8 | 9 | medium anchor |
| Mark Erikson dev plans | external task state | 8–9 | 9 | story anchor |
| Boris Tane research.md / plan.md | research and plan as durable surfaces | 8–9 | 9 | story anchor |
| Agentic Context Engineering | context collapse / evolving instructions | 7.5 | 8.5 | theory support |
| Cursor Rules / Configuring Agentic Tools | empirical config layer | 7 | 8 | support, not anchor |

## Возможные подразделы

1. Контекст не равен размеру окна.
2. Project instructions as interface: `AGENTS.md`, `CLAUDE.md`, rules.
3. Plans, research notes and dev plans as external state.
4. Skills/hooks as crystallized repeated context.
5. Когда контекст становится долгом.
6. Переход: внешний контекст должен быть подключён к исполняющей среде.

## Что переносить в Handbook

- Практический слой: когда заводить `dev-plan.md`, `research.md`, `AGENTS.md`, skills, hooks.
- Шаблоны файлов и checklists.

---

# Часть V. Делегирование: выбор режима работы, а не выбор инструмента

## Управляющий тезис

Зрелая агентская разработка выбирает не «какой AI использовать», а какой режим делегирования выдерживает риск, обратимость, проверяемость и стоимость ошибки данной задачи.

## Функция

Собрать локальную палитру режимов из 12 историй и expanded-версии, но не как каталог. Эта часть должна стать мостом между empirical session и technical harness: разные задачи требуют разной степени внешнего состояния, проверки, прав и изоляции.

## Anchor / story materials

Здесь, вероятно, не нужен один deep external case. Лучше использовать несколько внутренних историй как controlled examples.

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| Boris Tane | research / plan / implement | 8–9 | 9 | story anchor |
| Simon Willison | code research and evidence artifact | 8–9 | 8.5 | story anchor/contrast |
| HumanLayer | plan/research/implementation and 12-factor frame | 8–9 | 9 | story anchor + bridge Part VI |
| Jökull Sólberg | PR сопровождение / `/babysit-pr` | 8 | 8.5 | medium case, bridge Part VIII |
| Mike McQuaid | worktrees/Sandvault | 8 | 8.5 | medium case, bridge Part VI |
| Matt Pocock | skills as reusable procedures | 7.5–8 | 8 | bridge Part IV/VI |

## Возможные подразделы

1. Лёгкий разговорный режим.
2. Исследование без правок.
3. План как объект правки.
4. Долгая задача с внешним состоянием.
5. PR-сопровождение как отдельный режим.
6. Когда нужен worktree / sandbox / isolated environment.
7. Когда режим надо усилить, а когда остановить.

## Контрасты

- One-shot prompt where agent invents architecture.
- Background PR without review path.
- Workflow ceremony for small reversible fix.

## Риск части

Эта часть особенно легко превращается в каталог. Её надо писать не по именам историй, а по режимам. Истории должны появляться внутри режима.

---

# Часть VI. Исполнение: среда агента, harness, tools, permissions

## Управляющий тезис

Агентская способность не находится только внутри модели. Она возникает из связки model + interface + tools + permissions + sandbox + working tree + instructions + feedback channels. AI-driven SDLC проектирует эту среду как часть процесса разработки.

## Функция

Показать техническое ядро agentic SDLC: где агент реально действует, что он может видеть, что может менять, как получает обратную связь и как оставляет evidence.

## Anchor cases / sources

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| Fowler / Thoughtworks Harness Engineering | conceptual anchor | 9 | 10 | раскрывать крупно |
| OpenAI Codex | official platform workflow | 8.5 | 9.5 | medium anchor |
| GitHub Copilot cloud agent | official PR/platform workflow | 8.5 | 9.5 | medium anchor |
| Claude Code docs | skills/hooks/subagents/MCP/platform primitives | 8 | 9 | medium anchor |
| SWE-agent | agent-computer interface | 8 | 8.5 | technical support |
| HumanLayer 12-factor agents | practical harness discipline | 8 | 9 | bridge from stories |
| Google Jules | async plan/diff/PR workflow | 6.5–7 | 7 | short contrast only |

## Возможные подразделы

1. Harness as work environment.
2. Permissions, sandbox and worktrees.
3. Tools and commands as action surface.
4. Hooks, skills and subagents as repeated operational memory.
5. Platform agents: Codex, Copilot cloud agent, Jules.
6. Evidence from environment: terminal logs, test outputs, branches, PRs.
7. Security boundary: what the agent can use, do and generate.

## Что не делать

- Не превращать это в product comparison.
- Не писать «Codex vs Copilot vs Claude».
- Использовать официальные docs как признаки новой формы SDLC, а не как рекламные материалы.

---

# Часть VII. Глубокий кейс: Gas Town / Beads как организационно-операционный lifecycle

## Управляющий тезис

Gas Town показывает край, где агентская разработка перестаёт быть сессией разработчика с помощником и становится организационной средой: роли, очереди, долговременные идентичности, task graph, watchdogs, merge machinery, escalation и human oversight.

## Функция

Восстановить потерянную силу старой Gas Town части и показать второй главный полюс теории рядом со SPDD:

- SPDD — спецификационный контур намерения;
- Gas Town — организационно-операционный контур исполнения и координации.

## Source strength

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| Steve Yegge / Welcome to Gas Town | original narrative and roles | 9 | 10 | deep anchor |
| Gas Town docs / glossary | formal vocabulary: Town, Rig, GUPP, NDI, roles | 9 | 10 | deep anchor support |
| Gas Town GitHub repo | commands, monitoring, Refinery, escalation, Seance | 9 | 10 | operational facts |
| DoltHub Two Weeks in Gas Town | field evaluation, adversarial rigs, test harness, token leak | 9.5 | 10 | essential contrast / price |
| Old baseline Gas Town part | composition model | 8 | 10 | restore shape |
| Habr translation / secondary posts | extra details (`gt nudge`, `gt seance`) | 6 | 7 | use only if corroborated |

**Оценка кейса:** 10–11. Он потенциально сильнее SPDD для организационного слоя, но источники более шумные и менее академические, поэтому нужна аккуратная опора на первичные docs/repo/DoltHub.

## Возможные подразделы

1. Почему Gas Town не просто «много агентов».
2. Town, Rig, Crew, Polecats: рабочая топология.
3. Mayor как управляемая человеческая поверхность.
4. Beads как task memory / coordination substrate.
5. GUPP и NDI: автономия через надзор, а не через надёжность одной сессии.
6. Witness, Deacon, Dogs: обслуживание агентской системы самой системой.
7. Refinery и merge queue: когда агентский поток упирается в integration.
8. Seance / session continuation: сессии расходуемы, рабочая идентичность должна переживать их.
9. DoltHub: что работает, что ломается, почему verification becomes the new skill.
10. Что Gas Town даёт теории AI-driven SDLC.

## Обязательная критическая линия

Gas Town нельзя писать только как вдохновляющую футуристическую сцену. DoltHub показывает цену:

- agents may use any available tool to make progress;
- isolation between rigs может оказаться фиктивной, если ключи/доступы видны агентам;
- тестовая архитектура может быть сильной, но доверие к коду всё равно требует human verification;
- Mayor может выходить из своей high-level роли и писать код;
- orchestration itself creates new failure modes.

---

# Часть VIII. Свидетельства, тесты, ревью и benchmark validity

## Управляющий тезис

Когда генерация дешевеет, дефицитом становится не код, а проверяемые свидетельства: тесты, логи, PR descriptions, benchmark validity, review capacity и способность процесса учиться на сбоях.

## Функция

Соединить technical execution с правом завершения. После этой части читатель должен видеть: green tests, passed benchmark или coherent PR description ещё не означают, что lifecycle завершён.

## Anchor / sources

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| Part VIII existing rewrite | материал quarry | 8 | 9 | пересобрать композиционно |
| UTBoost / Saving SWE-Bench / SWE-PolyBench | benchmark validity | 7.5–8 | 8.5 | medium cluster |
| Over-mocked tests / Testing with AI Agents | generated tests risks | 8 | 9 | medium cluster |
| SlopCodeBench / Beyond Isolated Tasks | sequential code evolution | 7.5 | 8.5 | bridge to lifecycle tail |
| PR communication papers | review communication | 8 | 9 | medium cluster |
| Jökull Sólberg | practical PR babysitting | 8 | 9 | story anchor |
| SASE Merge-Readiness Pack | conceptual evidence package | 8.5 | 9 | conceptual bridge |

## Возможные подразделы

1. Evidence package вместо “готово”.
2. Почему зелёные тесты недостаточны.
3. Benchmark validity: задача, загрязнение, последовательность изменений.
4. Generated tests and over-mocking.
5. PR description as review interface.
6. Human-AI review: что должен делать человек.
7. Verification debt: когда сбой должен вернуться в harness/spec/process.

---

# Часть IX. Завершение, governance и внешний контур

## Управляющий тезис

Операционная инициативность агента не даёт ему права завершения. Завершение изменения — это governance act: кто принимает риск, кто подписывает происхождение, кто отвечает за merge, release, supply chain и последствия.

## Функция

Завершить lifecycle там, где текущая expanded-версия уже имела сильную ось: ownership, right to refuse, policy boundaries. Здесь должны встретиться SASE, open-source policies, GitHub governance, OpenSSF/Snyk security framing и external maintainer burden.

## Anchor / sources

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| SASE | conceptual model: ACE/AEE/Merge-Readiness | 8.5–9 | 9 | conceptual anchor |
| Linux/QEMU/LLVM/etc. policy cluster | external boundary and provenance | 9 | 10 | concrete anchor |
| GitHub Well-Architected governance | enterprise governance/audit primitive | 8.5 | 9 | platform support |
| OpenSSF SAFE-MCP / agentic AI security | security/governance support | 8 | 8.5 | support |
| Snyk ADLC | vendor but useful risk language | 6.5 | 7.5 | cautious support only |
| Agentic Technical Debt | lifecycle-tail governance | 7.5 | 8.5 | bridge to Part X |

## Возможные подразделы

1. Operational agency ≠ completion right.
2. Merge governance: who can say “done”.
3. Provenance, DCO and AI-generated contributions.
4. External maintainer capacity as scarce resource.
5. Agent tools, MCP, skills and supply-chain boundary.
6. Audit trail and session evidence.
7. Right to refuse as normal boundary, not anti-AI conservatism.

---

# Часть X. Хвост lifecycle: сопровождение, долг и обучение среды

## Управляющий тезис

AI-driven SDLC не заканчивается merge. Если агентская работа меняет систему быстрее, чем организация меняет проверки, инструкции, test harness, observability и governance, ускорение превращается в новый долг.

## Функция

Дать финальную сборку: ошибки и friction должны возвращаться не только в код, но в среду разработки. Эта часть напрямую подводит к Handbook и Codex/process-exoskeleton.

## Sources

| Материал | Роль | Source depth | Structural fit | Решение |
|---|---:|---:|---:|---|
| DORA 2025 | AI as amplifier | 8.5 | 9 | финальная рамка |
| Bain 2025 | lifecycle redesign, bottleneck shift | 8 | 9 | финальная рамка |
| Agentic Technical Debt | prompts/memory/tools/orchestration/observability debt | 7.5 | 8.5 | use cautiously but useful |
| Code maintenance papers | accepted AI code still needs maintenance | 7.5 | 8 | medium support |
| SlopCodeBench / sequential evolution | long-term change risk | 7.5 | 8.5 | bridge from VIII |
| Handbook / Fieldbook | practical output | 9 | 10 | internal continuation |

## Возможные подразделы

1. Merge is not the end.
2. Agentic technical debt and stochastic tax.
3. When repeated failures become skills, hooks, tests, policies.
4. AI-driven SDLC as process exoskeleton.
5. How this theory feeds Handbook and Fieldbook.
6. What remains human: architecture, taste, ownership, gates.

---

# Заключение. Не карта кейсов, а карта выбора режима

## Управляющий тезис

Итоговая теория должна давать не энциклопедию agentic tools, а способ выбрать и построить рабочий режим под lifecycle-risk конкретного изменения.

## Функция

Заключение должно сделать переход к Handbook естественным:

- если изменение маленькое и проверка рядом — лёгкий разговорный режим;
- если неизвестность высока — research / plan;
- если ошибка намерения дорога — spec/SPDD;
- если execution сложен — harness / sandbox / worktree / tools;
- если поток масштабируется — workflow / platform agent / Gas Town-like organization;
- если результат выходит наружу — evidence / review / governance / policy boundary.

## 4. Иерархия кейсов в новой архитектуре

### 4.1. Deep anchor cases

| Кейс | Где раскрывать | Почему |
|---|---|---|
| SPDD | Часть III | лучший кейс durable intent artifact / specification lifecycle |
| Gas Town / Beads | Часть VII | лучший кейс organizational-operational lifecycle |
| SWE-chat + Programming by Chat | Часть II | лучший empirical anchor реальных сессий |
| Open-source policy cluster | Часть IX | лучший concrete anchor внешней границы и права отказа |

### 4.2. Medium structural cases

| Кейс / материал | Где использовать | Роль |
|---|---|---|
| Codex | Часть VI | official platform workflow, evidence, sandbox, AGENTS.md |
| GitHub Copilot cloud agent | Часть VI / IX | PR workflow, metrics, enterprise governance |
| Claude Code docs | Часть IV/VI | skills, hooks, subagents, MCP, context discipline |
| SASE | Часть VIII/IX | conceptual evidence/merge-readiness/governance vocabulary |
| Jökull Sólberg | Часть V/VIII | PR babysitting, Fix/Dismiss/Escalate |
| Boris Tane | Часть IV/V | research/plan/implement as local mode |
| HumanLayer | Часть V/VI | agent harness and procedural discipline |
| Matt Pocock | Часть IV/VI | skills as reusable operational memory |

### 4.3. Short contrasts / boundary materials

| Материал | Использование |
|---|---|
| Google Jules | short platform contrast, not anchor |
| V-Bounce | cautious contrast to phase-heavy AI-native SDLC |
| Snyk ADLC | security language, vendor caveat |
| AI Codebase Maturity Model | candidate, verify before use |
| McKinsey / generic market reports | background only, not load-bearing |
| Weak standalone AI tool posts | source map / Handbook only |

## 5. Что переносится из старой и новой версий

### 5.1. Из старой версии

- Композиционная дисциплина: часть должна вести одну мысль.
- Gas Town как полноценный большой разбор.
- Линия «от удачного запроса к рабочей среде» как исторический предшественник новой рамки.
- Ответственность и границы автономии.

### 5.2. Из expanded-версии

- Фактура по реальным сессиям, PR, ownership contours, local modes, SPDD, harness, tools, verification, security, policy boundaries.
- Ledger/source map как quarry.
- Уточнения Gas Town: `gt nudge`, `gt seance`, DoltHub adversarial rigs and verification problems.
- Новые рамочные AI-SDLC источники.

### 5.3. Что нужно убрать из основного текста

- Равноправное перечисление всех источников.
- Source-name headings без теоретической функции.
- Слабые кейсы, которые не несут механизм.
- Market/news framing без первичной фактуры.
- Параллельные версии одного и того же тезиса.

## 6. Риски новой рамки

### Риск 1. Корпоративный SDLC-учебник

Если структура станет `requirements → design → code → test → deploy`, документ потеряет остроту. Нужно держать lifecycle как контур изменения, а не фазовую бюрократию.

### Риск 2. Слишком много deep cases

Deep case должен быть редким. Если deep cases станет больше 4–5, теория снова распадётся.

### Риск 3. Gas Town как футуристический миф

Gas Town надо писать с критической линией DoltHub, иначе это будет вдохновляющий, но слабый текст.

### Риск 4. Platform docs как реклама

Codex/GitHub/Jules/Claude Code использовать не для product comparison, а как признаки того, какие primitives уже входят в agentic SDLC: sandbox, branch, PR, logs, tests, hooks, skills, MCP, custom instructions, audit.

### Риск 5. Слишком раннее переписывание

До написания полного текста нужны утверждённые part projects. Иначе снова возникнет source-transfer вместо structural synthesis.

## 7. Рекомендуемая последовательность работы

### Этап 1. Утверждение верхней архитектуры

Утвердить или изменить:

- количество частей;
- место SPDD;
- место Gas Town;
- нужен ли отдельный хвост lifecycle / debt / Handbook или это часть заключения.

### Этап 2. Part project batches

Проходить по 3 части:

1. Введение + Части I–II;
2. Части III–V;
3. Части VI–VIII;
4. Части IX–X + заключение.

Для каждой части фиксировать:

- управляющий тезис;
- функцию;
- anchor / medium / contrast / move/drop;
- source-depth score;
- story links;
- что берём из old baseline;
- что берём из expanded quarry.

### Этап 3. Deep dossier passes

Отдельные dossiers:

1. `SPDD_DOSSIER.md` — обновить по новой функции.
2. `GAS_TOWN_DOSSIER.md` — восстановить и углубить.
3. `SWE_CHAT_PROGRAMMING_BY_CHAT_DOSSIER.md`.
4. `POLICY_GOVERNANCE_DOSSIER.md`.

### Этап 4. Draft rebuild

Писать новый `Theoretical_synthesis_rebuilt.md` не как правку expanded-версии, а как новый clean synthesis с selective reuse.

### Этап 5. Anti-catalog audit

Проверить:

- есть ли у каждой части управляющая линия;
- не стали ли source names headings;
- не появились ли равноправные кейсы;
- достаточно ли раскрыты deep cases;
- нет ли слишком гладкого summary вместо угловатой фактуры.

### Этап 6. Story-link and Handbook bridge pass

Поставить связи с 12 историями, Cross-Story, Handbook и Fieldbook не в конце механически, а там, где материал действительно поддерживает мысль.

## 8. Открытые решения для утверждения

1. Делать ли SPDD отдельной частью или большим deep block внутри части про намерение?
   - Моя рекомендация: большой deep block внутри Части III. Если станет слишком тяжёлым — выделить в отдельную Part IIIA.

2. Делать ли Gas Town отдельной частью?
   - Моя рекомендация: да, отдельная Часть VII. Он потерял силу при сжатии до одного раздела.

3. Нужна ли отдельная Часть X про lifecycle-tail?
   - Моя рекомендация: да, но она должна быть короче SPDD/Gas Town. Её функция — связать debt, maintenance, learning environment and Handbook.

4. Держать ли «карта течений» как термин?
   - Моя рекомендация: не в названии и не как структура. Можно оставить как внутренний слой: карта течений стала source map, а финальный текст — lifecycle synthesis.

5. Нужно ли добавлять ещё источники до переписывания?
   - Моя рекомендация: нет массово. Достаточно. Новые источники искать только под конкретные дырки, выявленные в part project или dossier pass.

## 9. Короткая версия дизайна

```text
Введение. Почему речь не о генерации кода
I. Единица анализа: программное изменение, а не prompt
II. Реальная агентская сессия: трасса, вмешательство, выживание результата
III. Намерение: от запроса к артефакту управления
IV. Контекст и рабочее состояние: проект как интерфейс агента
V. Делегирование: выбор режима работы, а не выбор инструмента
VI. Исполнение: среда агента, harness, tools, permissions
VII. Deep case: Gas Town / Beads как организационно-операционный lifecycle
VIII. Свидетельства, тесты, ревью и benchmark validity
IX. Завершение, governance и внешний контур
X. Хвост lifecycle: сопровождение, долг и обучение среды
Заключение. Не карта кейсов, а карта выбора режима
```

## 10. Итоговая оценка

Рамка **AI-driven SDLC** действительно может спасти системность теории, если использовать её как lifecycle of software change. Она не отменяет старую мысль про рабочую среду, а уточняет её: рабочая среда нужна потому, что агентская разработка перестраивает весь жизненный цикл изменения, а не только момент написания кода.

Главное преимущество новой рамки: она подчиняет все источники и кейсы одному вопросу — **где в жизненном цикле изменения возникает новая сила, новая проверка, новый долг или новая граница ответственности**.

Главная опасность: сделать из этого корпоративный AI-in-SDLC обзор. Поэтому документ должен сохранять язык конкретной инженерной практики, глубокие кейсы, угловатую фактуру источников и контроль композиции старой версии.
