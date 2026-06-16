# P02 — Карта входного корпуса для главы IX

Статус: рабочая карта материала. Это не пересказ источников и не черновик главы.

## 1. Какие входы должны реально питать главу

Глава IX должна опираться на три слоя внутренних материалов.

Первый слой — **композиционный контроль**: `00_spine_map.md`, Skeleton V5, `POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md`, `POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md`, routing maps и P01-контракт. Они задают место главы в жизненном цикле: переход от рабочего состояния к исполнению. Из них в будущий основной текст нужно переносить не формулировки, а порядок вопросов: где агент действует, что ему доступно, чем ограничен ущерб, что можно наблюдать, что можно повторить и почему всё это ещё не равно принятию результата.

Второй слой — **готовый синтез по теме среды исполнения**: прежде всего `A6_execution_environment_distinctions.md` и companion-файлы A6. Это главный донор различений для главы: граница исполнения, инструментальная поверхность, движок рабочего процесса и платформенный агент. A6 уже собрал много фактуры по Sandvault, worktrees, HumanLayer, Ronacher, Roast, Quix/Klaus Kode и Stripe Minions. Его нельзя заново пересказывать как список кейсов; нужно взять структуру различений и переработать её под главу IX, где дополнительно нужно развести permission, approval, sandbox и authority.

Третий слой — **мост execution runtime → work state**: `C4_execution_runtime_to_pwg.md` и companion-файлы C4. C4 важен не как ещё один фрагмент о среде, а как защита границы: runtime может сохранить запуск, но не хранит состояние работы. В главе IX этот материал нужен ближе к середине и финалу: durable workflow, replay, checkpoint, run/session state, worktree/devbox/session log, а затем переход к вопросу, что из этого попадает в PWG, evidence и authority layers.

## 2. Роли основных внутренних фрагментов

| Вход | Роль для главы IX | Что брать | Чего избегать |
|---|---|---|---|
| `00_spine_map.md` | Верхняя ось жизненного цикла | Переход `работа → исполнение`; формулу, что среда исполнения ограничивает радиус действия, но не принимает результат | Не копировать carrier-таблицу как готовую композицию главы |
| Skeleton V5 | Скелет главы IX | Четыре слоя: boundary, tools/observation, durable runtime, platform agent | Не превращать скелетон в тезисный список подзаголовков без прозы |
| `A6_execution_environment_distinctions.md` | Главный содержательный донор | Различение слоёв среды; практические якоря Sandvault/worktrees/HumanLayer/Ronacher/Roast/Quix/Stripe | Не дублировать A6 целиком; не оставлять старую форму “среда агента — несколько слоёв” как название главы |
| `A6_source_usage.md` | Карта первичных ссылок | Точные внешние источники, к которым нужно возвращаться при переносе фактов | Не ссылаться на внутренний source usage вместо первоисточников |
| `A6_story_anchor_map.md` | Защита от пересказа историй | Как каждый кейс поддерживает конкретное различение | Не превращать Sandvault/Stripe/Roast в мини-истории внутри главы |
| `A6_open_questions.md` | Список нерешённых границ | Угрозы вокруг секретов, сети, MCP, browser artifacts; вопрос минимальной схемы для индивидуального разработчика | Не закрывать эти вопросы догадками без внешнего поиска |
| `C4_execution_runtime_to_pwg.md` | Мост к PWG | Различение состояния запуска и состояния работы; durable execution vs durable work state | Не расширять C4-фактуру так, чтобы глава IX стала повтором VII |
| `C4_open_questions.md` | Сборочные долги | Нужен source-pass по Claude/Codex worktrees; осторожность со Stripe transcript; asset-pass | Не выдавать курируемую стенограмму Stripe за полную официальную спецификацию |
| Atlas: GSD/BMAD/PWG/Gas Town | Boundary donors | Показывают соседние формы process profile, work graph, operational lifecycle | Не пересказывать методики; использовать только для границ и мостов |
| Story dossiers / stories | Практические якоря | Конкретные сцены действия: локальные логи, browser loop, harness, sandbox, devbox, workflow runner | Не заменять первичные ссылки внутренними историями |

## 3. Истории-якоря и их функция

### Arvid Kahl

Arvid Kahl нужен не как общий пример “хорошего агентского цикла”, а как сцена наблюдения: приложение, браузер, логи, небольшие безопасные итерации. В главе IX он может показать, что агенту нужен контакт с работающей системой, но browser/log loop остаётся наблюдением. Этот материал естественно ведёт к XI, где будет решаться, когда наблюдение становится достаточным проверочным материалом.

Риск дублирования: если раскрывать Arvid слишком подробно, глава IX начнёт повторять II или XI. Достаточно короткой сцены: агент видит поведение и логи, но принятие результата требует другого слоя.

### HumanLayer

HumanLayer — сильный anchor для harness: модель сама по себе не является coding agent; результат зависит от обвязки вокруг неё: контекст, инструменты, MCP, skills, subagents, hooks, back-pressure. Для IX этот материал нужен в разделе про инструментальную поверхность и про цену расширения tools. Особенно важен риск: MCP и другие инструменты не просто “дают возможности”, они добавляют доверенную текстовую и командную поверхность, которую агент должен читать и использовать.

Риск дублирования: HumanLayer может перетянуть главу обратно в VI про context/harness. Поэтому в IX нужно удерживать именно действие: какие инструменты вызываются, что они открывают, где нужна граница вызова, что остаётся в следе выполнения.

### Mike McQuaid / Sandvault / worktrees

Это главный материал для нижней границы исполнения. Sandvault даёт отдельного пользователя macOS, `sandbox-exec`, ограничение доступа к home/system/mounted drives, shared workspace и мосты к browser/iOS endpoint. Git worktree даёт отдельный diff и параллельную запись. Вместе это удобно показывает, что разрешить агенту больше свободы можно только если заранее сузить радиус возможного вреда.

Риск дублирования: Sandvault/worktree нельзя подать как полноценный процесс или как гарантию качества. Они ограничивают место и права, но не знают обещание изменения, не выбирают тесты и не принимают diff.

### Armin Ronacher / Pi / local scripts

Ronacher нужен для минимальной программируемой среды: `make dev`, `make tail-log`, лог из приложения, отладочная ссылка в stdout, временный Playwright-скрипт, обычный код вместо тяжёлого каталога MCP-инструментов. Pi добавляет маленькую локальную обвязку с `Read`/`Write`/`Edit`/`Bash`, расширениями и состоянием сессий.

Риск дублирования: этот материал легко уйдёт в VI про project rules/skills или в handbook-рецепт локальной настройки. Для IX нужно оставить вопрос: какие сигналы и действия среда предоставляет агенту, и почему эта поверхность должна быть специально сделана для машинного исполнителя.

### Stripe Minions

Stripe — anchor платформенного агента: Slack/issue context, analyzer, devbox, scoped context/tools, checks, judge/diagnose loop, PR and review path. В IX он нужен как пример, где среда исполнения не локальная утилита, а часть internal developer platform. Сильное различение: devbox и checks делают выполнение управляемее, но результат всё равно идёт в PR/ревью, а не автоматически становится принятым изменением.

Риск дублирования и source debt: часть фактуры о devbox и цикле Minions опирается на курируемую публичную стенограмму/заметки AI Engineer Singapore, а не только на официальные blog posts Stripe. Нельзя усиливать точные числа и внутренние детали без повторного source check.

### Shopify Roast

Roast — главный anchor для workflow runtime: агент становится одним шагом исполняемого процесса рядом с shell/Ruby/chat/map/repeat/call. Этот материал помогает показать, что порядок шагов, повтор, ограничение итераций и replay лучше хранить вне модели. Boba даёт хороший пример “детерминированная подготовка → агентский шаг → проверки”.

Риск дублирования: Roast не должен стать началом главы X про операционные рабочие процессы и не должен выглядеть как authority layer. Исполняемый процесс может хорошо организовать действие, но он не присваивает себе право принять результат.

### Quix / Klaus Kode

Quix полезен как пример доменного workflow engine вокруг Claude Code: модель вызывается для узкой задачи, а загрузка в песочницу, запуск, скачивание логов, фазы Source/Sink/Diagnose и сериализованное состояние держатся во внешнем коде. Это хороший материал для мысли: проблема иногда не в том, что agent tool слабый, а в том, что процесс пытается держать в prompt то, что должно быть кодом и runtime.

Риск: Quix не должен выглядеть как универсально доказанная корпоративная архитектура. Его нужно использовать как содержательный частный пример.

## 4. Вторичные доноры: Атлас и досье

### GSD / Open GSD

GSD полезен как граница с process profile и как источник фактуры про runtime health, worktree strategy, browser-proof, auto mode, gates, model profiles, MCP context budget и восстановление. Для IX из GSD можно взять не методику целиком, а два осторожных различения: процессный профиль может включать среду исполнения, но не сводится к ней; browser artifacts and runtime checks полезны только если следующий шаг процесса действительно их потребляет.

Не переносить в главу каталог команд `/gsd ...`. Если понадобится факт, вернуться к первичным страницам GSD, а не к досье.

### BMAD

BMAD нужен в основном как граница с VIII: роль, story, sprint status, correct-course, checkpoint preview. Он меньше питает IX напрямую. Его функция — показать, что процессный профиль может задавать фазы и роли, но среда исполнения отвечает за действие внутри этих фаз.

Не расширять BMAD в IX, если только внешний поиск не выявит прямо релевантный механизм permissions/runtime.

### PWG / Beads

PWG — обязательная граница. Он нужен для финального различения: run/session state, worktree and logs can be referenced by work graph, но граф работы хранит то, что runtime сам не знает: owner, blocker, gate, evidence requirement, right to continue, cleanup. Beads/Gas Town лучше оставить мостом к X, а не материалом основного раздела IX.

### Gas Town

Gas Town нужен как следующая глава и как предупреждение против преждевременного расширения. Если в IX появятся roles/backpressure/service agents, глава начнёт уходить в X. В IX можно только сказать, что когда отдельные execution environments связываются в поток множества работ, появляется отдельный организационно-операционный слой.

## 5. Где источники пересекаются

1. **Sandvault, Claude/Codex worktrees, Stripe devbox и GSD worktree strategy** пересекаются на теме изоляции файловой записи и среды запуска. Их нужно развести по масштабу: локальный individual setup, productized coding surface, internal platform and process profile.

2. **HumanLayer, Ronacher, Pi, MCP and GSD context budget** пересекаются на инструментальной поверхности. Общий тезис: больше инструментов не всегда лучше; tools стоят токены, расширяют доверенную поверхность and demand clearer boundaries.

3. **Roast, Quix/Klaus Kode, GSD auto mode, LangGraph/Temporal/DBOS/Restate candidates** пересекаются на durable execution. Общий тезис: часть работы нужно вынести из model memory в явный процесс, code, workflow state, replay/checkpoint/retry. Но durable execution must not be confused with durable work state.

4. **Stripe Minions, GSD/BMAD, Gas Town** пересекаются на platform/process/organization boundary. IX должна использовать Stripe как platform agent, GSD/BMAD как process profiles, Gas Town as next operational layer. Нельзя смешать их в одну шкалу зрелости.

5. **Arvid browser loop, Ronacher Playwright/logs, GSD browser proof, Codex DevTools candidate and OpenAI/Fowler harness materials** пересекаются на browser/runtime observation. Это богатый материал, но его нужно держать до границы: observation and traces are produced here; evidence quality will be handled in XI.

## 6. Где нужен внешний добор

Профиль главы — D3, значит внешнего поиска недостаточно как “проверки ссылок”. Нужен discovery + unfolding: найденные источники могут открыть новые документы, diagrams, terms and restrictions.

Обязательные зоны добора:

1. **Codex / OpenAI current docs**: sandbox/approvals, worktrees, browser/DevTools validation, tools, hooks if available, AGENTS/project context as execution boundary. Нужны актуальные официальные документы, потому поведение продукта меняется.

2. **Claude Code current docs**: permissions, hooks, subagents, browser or MCP integration, worktrees, `allowedTools`/permission prompts, dangerous skip-permissions boundary. Нужны официальные документы и, возможно, docs pages around enterprise/security.

3. **MCP security / tool boundary**: нужно подтвердить, как tool descriptions, prompts, permissions and data access create trust boundary. Использовать не как security chapter, а как часть инструментальной поверхности.

4. **Workflow runtime / durable execution**: LangGraph, Temporal, DBOS, Restate. Их нельзя разворачивать как каталог orchestration tools; нужно получить язык различения: workflow state, durable execution, replay, determinism, timers, retries, human-in-the-loop, idempotency, side effects.

5. **Browser/devtools and runtime observation**: current Codex/Claude/OpenAI/Fowler materials, possibly screenshots/local assets. Нужно решить, что из этого supports IX and what is deferred to XI.

6. **Secrets/network/production-like boundary**: нужна точная формулировка о том, что sandbox/approval does not automatically make secret access safe. Это может потребовать official docs or security guidance, but should not become full threat-model chapter.

## 7. Визуальный материал

Для IX уже есть сильные кандидаты: HumanLayer harness components, Mike/Sandvault/worktree screenshots, OpenAI Codex dashboard/permissions/DevTools, Stripe Minions, Shopify Roast workflow. Риск очень высокий: глава может превратиться в UI-tour.

Рабочее решение для будущего visual pass:

- один центральный синтетический figure может показать четыре уровня среды и границы между permission/approval/sandbox/authority;
- один реальный asset допустим, если он помогает понять конкретный механизм лучше текста, например permission prompt or harness components;
- все реальные external assets требуют отдельной проверки прав, локализации и подписи;
- не подменять готовые локальные изображения текстовыми схемами, если они уже существуют and relevant.

## 8. Сборочный вывод

Основная глава должна быть написана не из последовательности источников, а из инженерского сбоя:

> агент может действовать шире, чем процесс понимает, а затем процесс принимает сам факт выполненного действия за разрешение, безопасность или принятие результата.

От этой ошибки выстраиваются входы:

1. A6 даёт слои среды.
2. C4 даёт границу runtime and work state.
3. Истории дают конкретные сцены действия.
4. Атлас и досье защищают соседние границы.
5. Внешний добор должен обновить текущие product/runtime/security details.

Если глава получится хорошей, читатель после неё должен перестать говорить “у агента есть доступ” как будто это одно свойство. Ему должно быть ясно, что доступ распадается на место действия, доступные инструменты, технические права, подтверждения, ограничение ущерба, журнал действий, состояние запуска, состояние работы и право принять результат.
