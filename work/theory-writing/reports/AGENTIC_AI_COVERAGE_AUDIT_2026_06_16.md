# Coverage audit: агентская экосистема вокруг теории agentic development

Дата: 2026-06-16.  
Статус: диагностический audit, не правка глав.  
Основание: текущая файловая база после правок глав VII–X, планов оставшихся частей и плана главы XI; внешний поиск по основным семействам LLM-agent literature/frameworks; локальный поиск по `work/theory-writing` и `content`.

## Короткий вывод

Основной акцент теории не был ошибочным. Мы действительно пишем не общий обзор LLM-агентов, а теорию агентской разработки программного обеспечения: как меняется жизненный цикл изменения от намерения до выполнения, проверки, принятия и сопровождения. Поэтому сильный фокус на `SPDD`, `PWG`, `GSD`, `BMAD`, `Gas Town`, `MCP`, hooks, worktrees, runtime rights, verification material и post-merge learning оправдан.

Но coverage по широкой агентской экосистеме был неравномерным. Мы хорошо прошли внутрь выбранного коридора — реальные developer workflows, doc-first/process approaches, coding-agent практики, MCP/hooks/skills/subagents, Gas Town/Beads. При этом почти не поставили на карту несколько базовых семейств: раннюю петлю reasoning/action, универсальные agent frameworks, stateful graph runtimes, multi-agent frameworks, agent-to-agent protocols, observability/evaluation/provenance и security/authorization слой агентских систем.

Это не требует переписывать всю теорию. Но перед финальной сборкой нужно добавить короткую “родословную” и несколько точных сравнительных вставок. Иначе читатель, знакомый с LLM agents, справедливо спросит, почему в тексте есть Gas Town и GSD, но почти нет ReAct, LangGraph, OpenAI Agents SDK, Google ADK, AutoGen, CrewAI и A2A.

## Почему поиск источников это пропустил

Первая причина — корпус был story-first и practice-first. Мы искали реальные истории разработчиков, практику Codex/Claude Code/CU, методологические досье, Атлас и doc-first workflow. Это дало хорошую практическую фактуру, но не обязано само вывести на классическую литературу по LLM-агентам.

Вторая причина — запросы были смещены в сторону `developer workflow`, `coding agent`, `doc-first`, `SDLC`, `process`, `MCP`, `hooks`, `skills`, `subagents`. Для ReAct/MRKL/Toolformer/LangGraph/AutoGen нужны другие запросы: `LLM agents`, `tool-using agents`, `agent orchestration`, `stateful agents`, `agent frameworks`, `multi-agent workflows`, `agent observability`, `agent interoperability`.

Третья причина — мы слишком рано приняли “agent loop” как понятный фон. Теория сразу стала строиться выше: трасса сессии, состояние работы, среда исполнения, проверочный материал, принятие результата. Но между “модель пишет текст” и “жизненный цикл изменения” есть промежуточный слой: reasoning/action loop, tool use, agent harness, graph runtime, multi-agent coordination и observability.

Четвёртая причина — не было отдельного coverage-audit по семействам источников. Мы проверяли полноту внутри выбранных тем, но не держали внешний список больших веток, которые должны быть хотя бы рассмотрены.

## Локальный сигнал покрытия

Простой поиск по текущим `work/theory-writing` и `content` показал асимметрию:

| Тема | Текущее покрытие |
|---|---|
| `ReAct`, `MRKL`, `Toolformer`, `Reflexion`, `Tree of Thoughts` | отсутствуют |
| `LangChain` | присутствует, но в основном через State of Agent Engineering / context engineering, а не как agent harness |
| `LangGraph` | часто встречается, но в основном как граница durable execution / PWG в Атласе и фрагментах; в основных главах роль не систематизирована |
| `LangSmith` | отсутствует как observability/evaluation слой |
| `OpenAI Agents SDK`, `Google ADK`, `Semantic Kernel`, `LlamaIndex`, `Haystack` | отсутствуют или почти отсутствуют |
| `AutoGen`, `CrewAI` | встречаются минимально, скорее как отложенные внешние сравнения |
| `A2A` / `Agent2Agent` | отсутствует |
| `SWE-agent`, `OpenHands`, `SWE-bench` | SWE-agent встречается в legacy/планах, но coding-agent research не встроен как отдельная ветка |
| `MCP`, hooks, skills, subagents | покрыты хорошо |

## Матрица семейств источников

### 1. Ранняя петля рассуждения и действия

**Ключевые источники:** ReAct, MRKL, Toolformer.  
**Текущий статус:** почти отсутствует.  
**Почему важно:** это минимальная предыстория агентской петли: модель не только отвечает, а чередует рассуждение, действие через инструмент/среду и наблюдение результата. MRKL добавляет системный взгляд на LLM + внешние источники/модули; Toolformer — идею, что модель может учиться выбирать API-вызовы, их аргументы и использовать результаты.

**Куда вставлять:**

- Введение: короткая историческая рамка.
- Глава II: ReAct как минимальная форма trace/action/observation, но наша сессия шире.
- Глава VI/IX: tool use как предыстория agent harness/runtime.

**Не делать:** отдельную большую главу. Это родословная, не центр труда.

**Основные источники:**

- ReAct: https://arxiv.org/abs/2210.03629
- MRKL: https://arxiv.org/abs/2205.00445
- Toolformer: https://arxiv.org/abs/2302.04761

### 2. Reflection, planning, search и память попыток

**Ключевые источники:** Reflexion, Tree of Thoughts, Self-Refine, memory surveys, planning critiques.  
**Текущий статус:** отсутствует или почти отсутствует.  
**Почему важно:** наша теория говорит о восстановлении, post-merge learning и долговечном состоянии работы. Нельзя делать вид, что reflection/memory/planning линия не существует. Но её надо использовать как фон, а не как замену PWG или пост-merge сопровождению.

**Куда вставлять:**

- Глава II: как усложняется session trace.
- Глава VII: различить память попыток и граф состояния работы.
- Глава XIII: reflection/memory как исторический фон обучения по результатам, но не как достаточный post-merge контур.

**Основные источники:**

- Reflexion: https://arxiv.org/abs/2303.11366
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- LLM-agent memory survey: https://arxiv.org/abs/2404.13501
- Survey on LLM-based autonomous agents: https://arxiv.org/abs/2308.11432
- Critical investigation of planning abilities: https://arxiv.org/abs/2302.06706

### 3. Agent harness и массовые framework-и

**Ключевые источники:** LangChain, OpenAI Agents SDK, Semantic Kernel.  
**Текущий статус:** LangChain присутствует частично; OpenAI Agents SDK и Semantic Kernel отсутствуют.  
**Почему важно:** глава VI уже описывает skills, MCP, hooks, subagents и маршруты действия. Но нужно показать, что этот слой существует не только в отдельных продуктах, а как широкая инженерная форма: model + tools + prompt + middleware + tracing/guardrails/session.

**Куда вставлять:**

- Введение: переход от prompt engineering к agent harness.
- Глава VI: agent harness как слой сборки модели, инструментов, контекста и middleware.
- Глава IX: SDK/runtime как место, где tool use превращается в управляемое выполнение.

**Основные источники:**

- LangChain overview: https://docs.langchain.com/oss/python/langchain/overview
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- Semantic Kernel overview: https://learn.microsoft.com/en-us/semantic-kernel/overview/

### 4. Stateful graph runtimes и долговечное выполнение

**Ключевые источники:** LangGraph, Google ADK, LlamaIndex Workflows/Agents, Temporal/DBOS/Restate as adjacent runtime family.  
**Текущий статус:** LangGraph присутствует, но в основном как контраст к PWG; ADK/LlamaIndex почти отсутствуют.  
**Почему важно:** LangGraph и ADK напрямую попадают в темы VII–IX: состояние, граф исполнения, interrupts, persistence, human-in-the-loop, memory, deployment, observability/evaluation. Их надо использовать как современный runtime-фон, но не позволять им забрать понятие PWG.

**Куда вставлять:**

- Глава VII: граф исполнения агента не равен графу состояния работы.
- Глава IX: durable execution, session/runtime, human-in-the-loop, restart/resume.
- Глава X: graph workflows и multi-agent workflows как сравнение с Gas Town/Beads.

**Основные источники:**

- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- Google ADK: https://adk.dev/
- LlamaIndex agents: https://developers.llamaindex.ai/python/framework/use_cases/agents/

### 5. Multi-agent orchestration

**Ключевые источники:** AutoGen, CrewAI, CAMEL, LangGraph multi-agent patterns, Google ADK multi-agent workflows.  
**Текущий статус:** почти отсутствует; X осознанно избегала широкого сравнения, чтобы не размыть Gas Town.  
**Почему важно:** глава X сейчас сильна как Gas Town/Beads-случай, но без сравнения с AutoGen/CrewAI/ADK может выглядеть так, будто мы приняли очень частный проект за общий ландшафт. Нужно не расширять главу до обзора всех фреймворков, а добавить короткую сравнительную рамку: чем Gas Town отличается от обычных multi-agent frameworks.

**Куда вставлять:**

- Глава X: короткий сравнительный раздел или подзаголовок.
- Атлас/appendix: отдельная краткая заметка по multi-agent orchestration family.

**Основные источники:**

- AutoGen AgentChat docs: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/agents.html
- CrewAI docs: https://docs.crewai.com/
- Google ADK multi-agent workflows: https://adk.dev/

### 6. Agent interoperability protocols

**Ключевые источники:** MCP, A2A, ACP, ANP, related protocol surveys.  
**Текущий статус:** MCP покрыт хорошо; A2A отсутствует.  
**Почему важно:** MCP отвечает на связь агента с инструментами/данными. A2A отвечает на другую границу: агент ↔ агент, capability discovery, task lifecycle, artifacts, remote agent delegation. Это важно для главы X и особенно XII, потому что агентская работа в разных системах усиливает вопрос ответственности.

**Куда вставлять:**

- Глава VI: MCP как tool/context protocol, A2A как отдельная линия agent-to-agent.
- Глава X: когда координация выходит за пределы локальной системы.
- Глава XII: кто отвечает, если задача делегирована другому агенту/организации.

**Основные источники:**

- Google A2A announcement: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- Survey of MCP/ACP/A2A/ANP: https://arxiv.org/abs/2505.02279
- A2A + MCP critical analysis: https://arxiv.org/abs/2505.03864

### 7. Observability, evaluation, provenance

**Ключевые источники:** LangSmith, ADK evaluation/observability, OpenTelemetry GenAI semantic conventions, AgentTrace, provenance/evidence tracing surveys.  
**Текущий статус:** OpenTelemetry и наблюдаемость частично есть; LangSmith/ADK/agent provenance almost absent.  
**Почему важно:** это особенно важно для главы XI. Проверочный материал в агентской разработке — не только тесты и ревью, но и trace, execution provenance, evidence links, runtime metrics, evaluation datasets, simulation и deployment monitoring.

**Куда вставлять:**

- Глава XI: проверочный материал включает трассы, provenance, evaluation/observability.
- Глава XII: trace/provenance как основание ответственности.
- Глава XIII: повторяющиеся проблемы и learning loop.

**Основные источники:**

- LangGraph/LangSmith overview: https://docs.langchain.com/oss/python/langgraph/overview
- ADK observability/evaluation sections: https://adk.dev/
- AgentTrace: https://arxiv.org/abs/2602.10133
- Evidence tracing and execution provenance survey: https://arxiv.org/abs/2606.04990

### 8. Security, permissions, guardrails, authorization

**Ключевые источники:** NeMo Guardrails, agent security surveys, prompt/tool/data/context boundaries, agentic workflow injection, MCP/A2A identity/delegation papers.  
**Текущий статус:** главы IX/XII уже имеют permissions/sandbox/approvals/MCP security направление, но broader agent security field почти не нанесён на карту.  
**Почему важно:** в agentic development права действия и ответственность — не абстракция. Агент читает untrusted content, запускает команды, пишет файлы, вызывает инструменты, делегирует задачи и может попадать в цепочки workflow injection.

**Куда вставлять:**

- Глава IX: sandbox/permissions/approvals плюс threat model agentic workflows.
- Глава XII: authorization, delegation, identity, policy и граница ответственности.

**Основные источники:**

- NeMo Guardrails: https://arxiv.org/abs/2310.10501
- Autonomy-induced security risks survey: https://arxiv.org/abs/2506.23844
- Agentic Workflow Injection in GitHub Actions: https://arxiv.org/abs/2605.07135
- Agent Identity Protocol across MCP/A2A: https://arxiv.org/abs/2603.24775

### 9. Coding-agent research and benchmarks

**Ключевые источники:** SWE-agent, SWE-bench, OpenHands, OpenHands SDK, coding-agent adoption studies, Devin/Codex/Claude Code/Cursor practice reports.  
**Текущий статус:** практические истории и Claude/Codex слой сильны, но research/benchmark линия не систематизирована. SWE-agent встречается в legacy, OpenHands и SWE-bench практически не встроены.  
**Почему важно:** это прямой сосед нашей темы. SWE-agent формулирует agent-computer interface; OpenHands показывает sandboxed execution, CLI/browser/code interaction, multi-agent coordination and benchmarks; adoption studies показывают, что coding agents уже оставляют следы в реальных репозиториях.

**Куда вставлять:**

- Глава VI: agent-computer interface и surface design.
- Глава IX: sandbox, CLI/browser/code execution.
- Глава XI: benchmarks/evaluation and coding-agent evidence.
- Введение: coding agents как эмпирическая причина писать этот труд.

**Основные источники:**

- SWE-agent: https://arxiv.org/abs/2405.15793
- OpenHands platform: https://arxiv.org/abs/2407.16741
- OpenHands SDK: https://arxiv.org/abs/2511.03690
- Coding-agent adoption study: https://arxiv.org/abs/2601.18341

### 10. Declarative LM programs and optimization

**Ключевые источники:** DSPy, DSPy Assertions, GEPA/optimization family.  
**Текущий статус:** отсутствует.  
**Почему важно:** это не центральная линия агентской разработки как SDLC, но важный сосед: модельные pipeline-и можно не только prompt-ить вручную, но программно описывать, измерять и оптимизировать. Это может усилить главу XI и заключение, но не должно забирать центр.

**Куда вставлять:**

- Глава XI: evaluation-driven optimization как соседний подход к проверке/улучшению.
- Заключение: отдельный режим работы, когда объектом становится не код проекта, а сам LM-процесс.
- Атлас: краткая справка, если понадобится.

**Основные источники:**

- DSPy: https://arxiv.org/abs/2310.03714
- DSPy Assertions: https://arxiv.org/abs/2312.13382

## Что это говорит об акцентах

### Что было выбрано правильно

Наша главная ось — изменение программного обеспечения как жизненный цикл — остаётся сильной. Она даёт то, чего обычно нет в общих обзорах LLM agents: намерение, спецификация, состояние работы, среда исполнения, проверочный материал, принятие, сопровождение. В этом смысле `PWG`, `GSD`, `BMAD`, `Gas Town`, `MCP`, hooks и runtime rights — не случайные фетиши, а попытка описать именно software-change lifecycle.

### Где был перекос

Мы слишком много доверяли редким/локальным anchor cases как носителям общей теории. Gas Town, GSD и BMAD ценны, но это не общепринятые центры поля. Они должны оставаться anchor cases, через которые видны проблемы жизненного цикла, но вокруг них нужно дать карту более широкого поля: ReAct/tool-use lineage, LangGraph/ADK runtime, AutoGen/CrewAI orchestration, A2A interoperability, LangSmith/observability/evaluation.

Иначе текст может выглядеть так, будто он хорошо знает несколько необычных практик, но не видит стандартную agent ecosystem.

### Что делать с Gas Town

Не убирать и не сжимать. Gas Town остаётся сильным уникальным случаем: он показывает не просто multi-agent orchestration, а организацию множества работ, сервисные роли, очереди, человеческий интерфейс и возврат результатов в общее состояние. Но в главе X нужно добавить короткое позиционирование: AutoGen/CrewAI/ADK/LangGraph показывают более общие формы multi-agent orchestration, а Gas Town нужен как подробный рабочий пример организационной среды разработки.

### Что делать с GSD/BMAD

Не превращать их в “главные методологии агентской разработки”. Они должны быть примерами разных способов продолжать работу под контролем: GSD — фазовая дисциплина и проверочные остановки; BMAD — ролево-артефактная дисциплина вокруг stories/course correction. Их нужно уравновесить короткими ссылками на mainstream agent frameworks/runtime, чтобы глава VIII не выглядела как узкий методологический остров.

### Что делать с PWG

PWG не выглядит ошибочным акцентом. Напротив, на фоне LangGraph/ADK он становится яснее: LangGraph/ADK описывают граф/состояние выполнения агента, а PWG описывает состояние самой работы над изменением. Это различие нужно явно закрепить в главе VII и, возможно, во введении.

## Приоритеты исправления

### Срочно перед финальной сборкой

1. Введение: добавить короткую генеалогию от ReAct/MRKL/Toolformer к agent harness/runtime и далее к жизненному циклу изменения.
2. Глава II: добавить ReAct как минимальную форму действия/наблюдения, от которой наша session trace уходит дальше.
3. Глава VI: добавить LangChain/OpenAI Agents SDK/Semantic Kernel как общий agent harness фон; LangGraph/ADK как runtime/graph фон.
4. Глава VII: явнее развести LangGraph/ADK graph execution и PWG как граф состояния работы.
5. Глава IX: добавить OpenAI Agents SDK, LangGraph, ADK, OpenHands как современный runtime/sandbox/human-in-the-loop фон.
6. Глава X: добавить короткое сравнение Gas Town с AutoGen/CrewAI/ADK/LangGraph/A2A.
7. Глава XI: добавить LangSmith/ADK evaluation/provenance/evidence tracing как часть проверочного материала.
8. Глава XII: добавить A2A, authorization/delegation/security как материал для ответственности.

### Желательно, но не как большая новая ветка

- Reflexion/Tree of Thoughts/Self-Refine — компактно во II/VII/XIII.
- DSPy — как соседний режим evaluation-driven LM pipeline, скорее в XI/заключении.
- LlamaIndex/Haystack/Semantic Kernel — как контрольные представители framework/RAG/agent ecosystem, без раздувания.
- Agent security surveys — как support для IX/XII, не как отдельная глава.

### Не включать глубоко

- Полные обзоры agentic commerce, роботических VLA-agents, социальные simulation agents, broad enterprise automation, если они не помогают software-change lifecycle.
- Слишком свежие single-paper protocols без зрелой практической роли; их можно отметить как “watch list”, но не строить на них аргумент.

## Конкретная карта вставок

| Часть | Что добавить | Объём |
|---|---|---|
| Введение | ReAct/MRKL/Toolformer → LangChain/LangGraph/OpenAI Agents SDK/ADK → software-change lifecycle | 4–8 абзацев |
| II | ReAct как минимальный trace/action/observation; Reflexion как память попыток | 2–4 абзаца |
| VI | Agent harness/framework background: LangChain, OpenAI Agents SDK, Semantic Kernel; graph/runtime background: LangGraph/ADK | 4–8 абзацев |
| VII | LangGraph/ADK не равны PWG: graph of execution vs graph of work | 2–4 абзаца |
| VIII | GSD/BMAD как частные process approaches; короткое уравновешивание mainstream frameworks | 1–3 абзаца |
| IX | OpenAI Agents SDK, LangGraph, ADK, OpenHands как runtime/sandbox/session/human-in-the-loop примеры | 4–8 абзацев |
| X | AutoGen/CrewAI/ADK/A2A как фон multi-agent coordination; Gas Town как deep anchor, а не весь рынок | 3–6 абзацев |
| XI | LangSmith/ADK observability/evaluation/provenance, AgentTrace/evidence tracing | 4–8 абзацев |
| XII | A2A, authorization/delegation, prompt/tool/data/context boundaries, workflow injection | 4–8 абзацев |
| XIII | Reflexion/memory surveys как фон learning loop; отличить от post-merge maintenance | 2–4 абзаца |
| Заключение | Добавить выбор между agent harness, runtime graph, work-state graph, multi-agent orchestration, verification/evaluation layer | 2–4 абзаца |

## Итоговое решение

Акцент теории не нужно менять радикально. Главная идея — агентская разработка как изменение жизненного цикла программного изменения — остаётся правильной и более ценной, чем очередной обзор LLM-agent frameworks.

Но нужно добавить внешний слой ориентирования. Сейчас текст рискует выглядеть так, будто он движется от внутренних кейсов сразу к собственной теории, пропуская общепринятую родословную и современную инфраструктуру LLM-агентов. Это исправляется не новой большой частью, а серией компактных вставок и, возможно, одной короткой atlas/appendix-статьёй: “Agent loop, harness, graph runtime, multi-agent orchestration: где наша теория находится относительно общего поля”.

После этого Gas Town, GSD, BMAD и PWG будут восприниматься не как случайно выбранные странные опоры, а как специализированные ответы на software-development проблемы внутри более широкой карты агентской экосистемы.
