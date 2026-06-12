# A6. Использование источников

Статус: рабочий файл для фрагмента `A6_execution_environment_distinctions.md`. В основном тексте внутренние досье, планы, отчёты и файлы историй не использованы как публичные источники; они использованы только для композиции, проверки границ и поиска первичных / внешне читаемых источников.

## Управляющие материалы, прочитанные для композиции

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` — задал место фрагмента в Части IX: среда агента, обвязка, инструменты, права; связка с Persistent Work Graph.
- `work/theory-writing/CORE_NODES_WRITING_PLAN.md` — задал выходной файл, четыре различаемых слоя и проверку качества: не смешивать Roast, Stripe Minions, Quix, Armin, Sandvault и HumanLayer.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` — подтвердил роль историй-якорей и требование записать `source_usage` / `story_anchor_map`.
- `protocols/rules/*.md` и `protocols/rules/terminology-and-translation.md` — использованы для языка, происхождения, запрета ссылаться на внутренние досье вместо первоисточников и сохранения человеческого технического тона.

## Фактически использованные первичные / внешне читаемые источники

| Источник | Где использован | Поддерживаемое утверждение | Статус |
|---|---|---|---|
| HumanLayer, “Skill Issue: Harness Engineering for Coding Agents” — https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | Абзацы про инструментальную поверхность, harness и MCP | `coding agent = AI model(s) + harness`; обвязка включает контекстные файлы, MCP, skills, subagents, hooks, back-pressure; описания MCP-инструментов попадают в системный prompt, несут риск prompt injection и раздувают контекст | Основной источник для HumanLayer; использован под утверждения, не как обзор истории |
| Mike McQuaid, “Sandboxes and Worktrees” — https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/ | Абзац про границу исполнения | Sandvault/worktrees как слой ограничения прав и параллельной записи; проверка остаётся локальной и человеческой | Основной источник для Sandvault как истории-якоря |
| Sandvault repository — https://github.com/webcoyote/sandvault | Абзацы про sandbox, permissions, browser/iOS automation | Sandvault запускает агентов в отдельной macOS user account / `sandbox-exec`; модель безопасности: запрет доступа к home основного пользователя, system files, mounted drives; shared workspace `/Users/Shared/sv-$USER`; `--native-install`, `SANDVAULT_ARGS`; browser automation через `SV_BROWSER_ENDPOINT`, iOS bridge через `SV_IOS_SIMULATOR_ENDPOINT` | Второй проход расширил использование: не только запуск `sv claude`, но и конкретные permissions / browser факты |
| Claude Code worktrees — https://code.claude.com/docs/en/worktrees | Абзацы про worktrees и первичный запуск | `--worktree` создаёт рабочее дерево под `.claude/worktrees/<value>/` и ветку `worktree-<value>`; `.worktreeinclude`; очистка зависит от состояния изменений; `git worktree lock`; нужно инициализировать среду разработки в новом worktree | Второй проход усилил lifecycle worktree |
| Codex Worktrees — https://developers.openai.com/codex/app/worktrees | Абзацы про worktrees и Handoff | Worktree как фоновый контекст, Local как передний контекст; Handoff переносит поток работы и код через Git-операции; managed worktrees в `$CODEX_HOME/worktrees`; detached HEAD; скрипт настройки локальной среды | Второй проход усилил передний / фоновый контекст и различие Handoff |
| Git worktree documentation — https://git-scm.com/docs/git-worktree | Абзац про базовую семантику worktree | Отдельное рабочее дерево с собственной директорией и общей историей / метаданные репозитория | Использован как каноническое основание, без расширенной фактуры |
| Armin Ronacher, “Agentic Coding Recommendations” — https://lucumr.pocoo.org/2025/6/12/agentic-coding/ | Абзацы про инструментальную поверхность, логи, браузер, локальные скрипты и права | Инструментом может быть shell-скрипт, MCP-сервер, файл лога; `make dev` должен давать понятный сигнал; `make tail-log` и ссылка из отладочного письма в stdout помогают агенту; Playwright/browser как часть проверки; `claude --dangerously-skip-permissions` как локальный риск и решение о границе прав | Второй проход расширил конкретику по logs/browser/локальные скрипты |
| Armin Ronacher, “Your MCP Doesn’t Need 30 Tools: It Needs Code” — https://lucumr.pocoo.org/2025/8/18/code-mcps/ | Абзац про инструментальную поверхность | Код как программируемый интерфейс инструмента; критика больших MCP-каталогов; инструмент можно чинить как обычный код | Использован для различения инструментальной поверхности и свидетельств |
| Armin Ronacher, “Pi: The Minimal Agent Within OpenClaw” — https://lucumr.pocoo.org/2026/1/31/pi/ | Сравнительный абзац “почему нельзя одна категория” | Pi как минимальная изменяемая обвязка, маленькое ядро и расширения | Основной источник по Pi |
| Pi README — https://github.com/earendil-works/pi | Сравнительный абзац про Pi | `Read`/`Write`/`Edit`/`Bash`, self-extensible coding agent, границы безопасности | Использован как репозиторный источник |
| Pi compaction docs — https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md | Сравнительный абзац про Pi | Сессии как дерево, compaction, branch summaries и файловое состояние | Использован как технический якорь, без глубокого пересказа |
| Shopify Engineering, “Introducing Roast” — https://shopify.engineering/introducing-roast | Абзац про движок рабочего процесса | Roast как структурированные ИИ-рабочие процессы, где AI-шаги перемежаются с обычным кодом; `workflow.yml`, prompt-файлы, командные/Ruby/параллельные шаги, встроенный `CodingAgent`; Boba как детерминированная очистка / Sorbet autocorrect → CodingAgent → tests/typecheck | Главный источник по внутренней рамке Roast; третий проход использует его именно как источник про слой рабочего процесса |
| Shopify/roast README — https://github.com/Shopify/roast/blob/main/README.md | Абзац про Ruby DSL | Ruby DSL и cogs: `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call`; quick example `cmd(:recent_changes)` → `agent(:review)` → `chat(:summary)`; запуск `bin/roast execute`; `agent` cog запускает локальные agent CLI, default `:claude`, также `:pi` | Источник по текущей публичной форме Roast; поддерживает тезис, что агент — один cog/provider slot, а не весь процесс |
| Roast iterative workflows tutorial — https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md | Абзац про workflow control flow | `repeat`, `break!`, `next!`, `outputs`, передача результата итерации в следующую итерацию и лимиты повтора | Использован для утверждения о bounded repeat как workflow-механике |
| Quix blog, “Claude Code wouldn’t behave…” — https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it | Абзацы про Quix / Klaus Kode и MCP / раздувание контекста | Сбой управления только через prompt; описания MCP-инструментов занимали 34% контекста до начала работы; Claude Code вызывается через SDK для узкой задачи кодирования; загрузка кода/переменных/зависимостей в облачную песочницу, запуск и скачивание логов выполняются детерминированным кодом; разные шаги могут запускать свежие сессии Claude; Klaus Kode построен под конкретный сценарий применения и платформу | Второй проход расширил MCP тезис, третий проход усилил тезис про движок рабочего процесса, проход по глубине источников добавил ограничение по универсальности примера |
| Klaus Kode `workflow_factory.py` — https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py | Абзац про Quix | `WorkflowFactory` регистрирует Source, Sink, Diagnose, Deployment и Monitoring phases и связывает их с context/run_config/debug_mode | Использован как code-backed source |
| Klaus Kode `contexts.py` — https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py | Абзац про Quix | `WorkflowContext` состоит из workspace, technology, schema, code generation, deployment и credentials contexts; состояние сериализуется в JSON | Использован как code-backed source |
| Stripe Minions Part 1 — https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | Абзацы про платформенный агент | Minions как one-shot end-to-end coding agents, PR и человеческое ревью | Основной официальный источник Stripe |
| Stripe Minions Part 2 — https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 | Абзацы про платформенный агент | Devbox, blueprints, scoped context/tools, feedback, производство PR | Основной официальный источник для инфраструктурной части; веб-выдача страницы плохо раскрывает основной текст, поэтому точные devbox-числа не взяты отсюда |
| AI Engineer Singapore, курируемая стенограмма / заметки: Mark Doyle, Stripe — https://aie-sg-day1.vercel.app/ | Абзацы про Stripe devbox и цикл Minion | Репозиторий около 300M LoC / 90GB, удалённые среды разработки, готовый пул devbox, 64–128 GB RAM; анализатор собирает контекст Slack/тикета/PR; цикл prompt/context → coding agent → lint/test/typecheck → LLM-судья с prompt+diff → diagnose/create PR; Slack возвращает краткое резюме и ссылку на diff | Добавлен во втором проходе как внешний источник под devbox утверждения; третий проход использует его для механики платформенного слоя, с пометкой о статусе курируемой стенограммы |
| Stripe Sessions 2026 Developer Keynote — https://stripe.com/sessions/2026/developer-keynote | Абзац про полномочия / контроль человека | Официальный публичный слой про агентные инструменты для разработчика, предсказуемые и проверяемые действия, а также сохранение человеческого контроля | Использован осторожно; без слияния чисел в одну метрику |
| Stripe Selective Test Execution — https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo | После содержательной починки не используется как целевая публичная ссылка в основном тексте | Быстрая выборочная проверка может быть фоном для разговора о CI-субстрате, но не поддерживает утверждения о человеческом ревью, отбраковке PR, времени ревью или дефектах после слияния | Оставлен как кандидат для A7 / свидетельства или технической вставки про CI; убран из основного абзаца о метриках ревью Stripe |

## Что было добавлено во втором проходе

- Конкретизация жизненного цикла worktree: путь `.claude/worktrees/<value>/`, ветка `worktree-<value>`, `.worktreeinclude`, cleanup, lock, Local/Worktree foreground/background, Handoff и detached HEAD.
- Конкретизация sandbox/permissions: Sandvault модель безопасности, shared workspace, native install и browser/iOS endpoints.
- Конкретизация инструментальной поверхности: `make dev`, `make tail-log`, ссылка из отладочного письма в stdout, Playwright/browser, логи как сенсор, локальные скрипты как программируемые инструменты.
- Конкретизация MCP: HumanLayer prompt-injection / тезис о стоимости контекста плюс Quix число 34% контекста, занятые описаниями MCP-инструментов.
- Конкретизация devbox: Mark Doyle transcript по масштабу удалённых сред разработки Stripe и циклу Minion на devbox.


## Что было добавлено в третьем проходе

- **Roast как слой рабочего процесса:** уточнено различие между ранней формой из статьи (`workflow.yml`, prompt-файлы, командные/Ruby/параллельные шаги, `CodingAgent`, Boba) и текущей Ruby DSL-формой из README (`cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call`). Основной тезис: `agent` — один исполняемый узел процесса, а не весь процесс.
- **Quix / Klaus Kode как детерминированный коридор:** добавлены детали про Claude Code SDK, детерминированные шаги upload/run/download-logs, свежие сессии Claude по фазам и кодовую структуру Source/Sink/Diagnose/Deployment/Monitoring и сериализованные контексты.
- **Stripe как платформенный слой:** усилено отличие платформенного агента от движка рабочего процесса: анализатор Slack/context → devbox → цикл кодирования → lint/test/typecheck → LLM-судья → диагностический цикл / PR → краткое резюме и ссылка на diff в Slack. Добавлено, что результат — пакет для ревью, а не ответ в чате.



## Проход по глубине источников

Новых целевых публичных ссылок в основной текст не добавлено. Полезная глубина найдена в уже учтённых источниках:

- **Shopify/roast README:** добавлена деталь, что `agent` cog запускает локальные agent CLI, по умолчанию `:claude`, но также поддерживает `:pi`. Это усиливает тезис “агент как слот провайдера внутри рабочего процесса”, а не “агент как вся система”.
- **Quix blog:** добавлено ограничение, что Klaus Kode рассчитан на конкретный сценарий применения и платформу, где запускается код. Это предотвращает чтение Quix как корпоративный платформенный слой и оставляет его в слое движка рабочего процесса.
- **Официальные страницы Stripe:** страницы Part 1/2 и Selective Test Execution повторно открыты, но текстовое извлечение отдало в основном метаданные / related cards; новые утверждения из них не добавлялись. Для механики Stripe по-прежнему используется осторожная атрибуция AI Engineer transcript, а уже зафиксированные официальные ссылки остаются фоном.

## Проход “та же история / разные слои”

Новых внешних источников в этом проходе не добавлено. Повторно использованы уже открытые первичные / внешне читаемые источники, чтобы проверить, что один пример не превращается в цельный пересказ:

- **Stripe Minions:** devbox используется дважды, но с разной функцией: сначала как граница исполнения / удалённая рабочая машина, затем как часть платформенного слоя вместе с analyzer, validation, judge, диагностический цикл, PR и путь к ревью.
- **Sandvault:** модель безопасности и `sandbox-exec` относятся к границе исполнения; browser/iOS endpoints относятся к инструментальной / сенсорной поверхности. Это одна история-якорь, но разные вопросы.
- **Ronacher / Pi:** logs, Playwright и локальные scripts относятся к наблюдательной поверхности; Pi относится к минимальной обвязке / локальному агентскому субстрату, а не к корпоративной платформе.
- **Shopify Roast:** `repeat`, повторное воспроизведение сессии, Boba и `CodingAgent` используются как механика рабочего процесса; текст явно запрещает читать их как полномочие или слой ревью.

## Источники, просмотренные через досье, но не использованные в основном тексте как целевые публичные ссылки

- `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md`, `SHOPIFY_ROAST_STORY_DOSSIER.md`, `ARMIN_RONACHER_STORY_DOSSIER.md`, `QUIX_KLAUS_KODE_STORY_DOSSIER.md` — использованы для навигации по фактуре и поиска первичных ссылок.
- `content/stories/07_*`, `08_*`, `13_*`, `14_*`, `15_*` — использованы как уже написанный слой историй и для проверки роли историй-якорей; в основном тексте прямые ссылки поставлены на внешние источники.
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` — использован только для связи runtime исполнения / состояния работы и проверки ссылок на Claude/Codex worktrees; целевая публичная ссылка в основном тексте не ставилась.

## Осознанные ограничения источникового прохода

- Stripe: не использованы сильные утверждения о полной автономности, дефектах, времени ревью или доле отбраковки, потому что публичные источники не дают достаточно репрезентативных данных.
- AI Engineer Singapore transcript: источник полезен и публичен, но не равен официальной документации Stripe; точные числа devbox использованы как свидетельство курируемой страницы доклада, а не как верифицированная спецификация платформы.
- Quix: история использована как доменный якорь движка рабочего процесса и пример раздувания контекста из-за MCP, а не как доказательство зрелого продукта или широкого внедрения.
- Roast: внутренние сценарии Shopify использованы только в той мере, в какой они раскрыты в статье; открытый README/tutorial использован для текущей формы DSL.
- Pi: безопасность описана как внешняя граница доверия; Pi не представлен как универсально безопасный runtime.
- Worktrees: использованы как механизм изоляции параллельной записи и handoff, не как workflow / граф состояния / механизм полномочий.

## Содержательная починка после проверки источников

- В основном фрагменте статья Stripe Selective Test Execution убрана из ссылки при утверждении о метриках ревью / дефектах. Она не доказывает наличие или отсутствие таких метрик; её место — фон про CI-субстрат или будущий фрагмент про свидетельства.
- Формулировка про доклад Mark Doyle уточнена как “курируемая публичная стенограмма”, чтобы не делать из неё официальную спецификацию Stripe.
- Внутренние досье и файлы историй остаются навигацией. Для публичных утверждений в основном тексте используются внешние страницы, документация, репозитории и курируемая публичная стенограмма.

## 2026-06-11 — source/asset note after A6 repair

Composition / visual / style repair did not add new external sources. It changed only placement and treatment of existing figures:

- Sandvault screenshot remains a `local_image_asset` and is used under the execution-boundary argument, supported by Mike McQuaid post and Sandvault repository.
- HumanLayer harness components remains a `local_image_asset` and is used under the tool/sensor surface argument, supported by HumanLayer “Skill Issue”.
- HumanLayer `too many MCP tools` image remains a known local asset but is no longer inline in A6; the underlying claim about MCP context cost remains in prose, supported by HumanLayer and Quix.
- Worktree/sandbox/Roast/Quix/Stripe synthetic figures removed from inline do not remove their source facts; those facts remain in prose and in the source table above.
