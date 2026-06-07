# Theory image assets

Локальные копии и локально отрисованные схемы для теоретической части сайта.

Изображения хранятся рядом с Markdown: `Doc/assets/theory-images/`.
Для готового сайта они продублированы в `assets/theory-images/`, чтобы относительные пути из HTML работали локально.

В Markdown используется HTML-блок `<figure>`: он сохраняет локальный путь к картинке, подпись, источник и имя файла. Обычный Markdown `![alt](path)` здесь слабее, потому что не даёт стандартной подписи и плохо фиксирует, зачем именно картинка вставлена в это место.

## Список ассетов

| Файл | Источник | Где используется | Зачем стоит в тексте |
| --- | --- | --- | --- |
| `anthropic-autonomous-agent.webp` | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Раздел 3, агент как петля | Показывает автономного агента как цикл: действие, инструмент, среда, обратная связь. |
| `fowler-harness-overview.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 4, модель + обвязка | Показывает, что агентская работа управляется направляющими, датчиками, проверками и человеком, а не только моделью. |
| `humanlayer-context-building.png` | [12 Factor Agents](https://github.com/humanlayer/12-factor-agents) | Раздел 4, инструменты и контекст | Показывает, что приложение может собирать контекст для следующего шага агента как часть обвязки. |
| `fowler-sdd-overview.png` | [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Раздел 5.1, инструментальные поверхности | Разделяет постоянную память проекта, агента и спецификации конкретных изменений. |
| `anthropic-context-vs-prompt-engineering.webp` | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Раздел 6, контекст как рабочее состояние | Показывает различие между одним запросом и проектированием динамической системы контекста. |
| `fowler-coding-context-overview.png` | [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) | Раздел 6, контекст | Разделяет system prompt, context interfaces, активные инструкции и историю разговора. |
| `openai-limits-of-agent-knowledge.webp` | [Harness engineering](https://openai.com/index/harness-engineering/) | Раздел 8, кодовая база как контекстный интерфейс | Показывает ограничения знания агента о среде выполнения и внешних состояниях приложения. |
| `fowler-spdd-reasons-canvas.svg` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 12, REASONS Canvas | Показывает REASONS Canvas как структуру для требований, домена, подхода, норм и предохранителей. |
| `fowler-spdd-workflow.svg` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 13, SPDD workflow | Показывает workflow, где prompt assets, code, validation и повторное использование связаны в цикл. |
| `fowler-harness-change-lifecycle.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 13, качество левее | Размещает feedforward и feedback по жизненному циклу изменения. |
| `fowler-harness-types.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 14, типы проверки | Различает поддерживаемость, архитектурную пригодность и поведение как разные объекты регулирования. |
| `openai-layered-domain-architecture.webp` | [Harness engineering](https://openai.com/index/harness-engineering/) | Раздел 15, пригодность проекта к обвязке | Показывает важность явных доменных слоёв и пересекающих границ для agent-readable архитектуры. |
| `fowler-harness-templates.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 17, шаблоны и топологии | Показывает, как шаблон приложения может нести не только структуру и стек, но и harness template. |
| `anthropic-multi-agent-research-architecture.webp` | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Раздел 18, подагенты | Показывает подагентов как архитектурную изоляцию работы, а не как декоративные роли. |
| `anthropic-coding-agent-flow.webp` | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Раздел 19, среда выполнения | Показывает высокоуровневый поток coding agent: задача, модель, инструменты, среда, результат. |
| `beads-task-graph-memory.svg` | [Beads](https://github.com/gastownhall/beads) | Раздел 24, граф задач | Локально отрисованная схема: задачи, зависимости, claim-состояние, память и `bd prime` как вход в работу. |
| `gastown-architecture.svg` | [Gas Town](https://github.com/gastownhall/gastown) | Раздел 25, Gas Town | Локально отрисованная схема по mermaid-архитектуре README: Mayor, town workspace, rigs, crew, hooks, polecats. |
| `gastown-basic-workflow.svg` | [Gas Town](https://github.com/gastownhall/gastown) | Раздел 30, GUPP / hooks / molecules | Локально отрисованная схема workflow: пользователь, Mayor, Convoy, Agent, Hook и возврат состояния. |
| `openai-codex-chrome-devtools-validation.webp` | [Harness engineering](https://openai.com/index/harness-engineering/) | Раздел 35, UI-свидетельства | Показывает проверку приложения через Chrome DevTools MCP и рабочую среду, а не только чтение файлов. |
| `fowler-harness-continuous-feedback.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 37, наблюдаемость | Показывает постоянные датчики дрейфа кодовой базы и среды выполнения. |
| `fowler-humans-on-loop.png` | [Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) | Раздел 41, human on the loop | Показывает роль человека как управляющего рабочей петлёй, а не ручного проверяющего каждой строки. |

## Примечание по локально отрисованным схемам

`beads-task-graph-memory.svg`, `gastown-architecture.svg` и `gastown-basic-workflow.svg` не являются скачанными скриншотами. Они отрисованы локально по README/mermaid-схемам первоисточников, чтобы сайт не зависел от внешнего рендера и чтобы можно было точно подписать переносимый смысл схемы.

## Публикационная оговорка

Для внутреннего рабочего сайта ассеты хранятся локально, чтобы материал был автономным. Если сайт будет публиковаться наружу, нужно отдельно проверить лицензии и условия переиспользования изображений каждого источника или заменить спорные изображения собственными схемами с указанием источника идеи.

## Дополнение: реальные изображения из первоисточников, добавленные вторым проходом

| Файл | Источник | Где используется | Зачем стоит в тексте |
| --- | --- | --- | --- |
| `fowler-harness-bounded-contexts.png` | [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) | Раздел 4, модель + обвязка | Уточняет, что `harness` имеет разный смысл в границах модели, агентской системы и пользовательской обвязки coding agent. |
| `humanlayer-intentional-compaction.png` | [Advanced Context Engineering for Coding Agents](https://www.humanlayer.dev/blog/advanced-context-engineering) | Раздел 6, контекст как рабочее состояние | Показывает intentional compaction как управляемое восстановление рабочего состояния, а не просто аварийное сжатие окна. |
| `fowler-claude-code-context.png` | [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) | Раздел 7, контекстные интерфейсы | Делает видимым состав загруженного контекста и поддерживает идею контекста как управляемого интерфейса. |
| `openai-codex-permission-prompt.webp` | [Unlocking the Codex harness](https://openai.com/index/unlocking-the-codex-harness/) | Раздел 21, подтверждение как граница ответственности | Показывает permission prompt как часть протокола ответственности, а не как абстрактное “разрешить/запретить”. |
| `anthropic-multi-agent-process-diagram.webp` | [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Раздел 22, восстановление долгоживущей задачи | Показывает долгую работу как процесс с ролями, подзадачами, памятью и финальной сборкой результата. |
| `gastown-mayor-hub.webp` | [Gas Town Docs](https://docs.gastownhall.ai/) | Раздел 27, Mayor | Поддерживает мысль о Mayor как поверхности управляемой видимости для человека, а не как ещё одном потоке логов. |
| `fowler-spdd-code-review.svg` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 47, review signals | Показывает, что review comment может вести к обновлению prompt artifact, а не к механической правке кода. |
| `fowler-spdd-api-test-script.png` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 16, SPDD validation | Показывает human-reviewable test-case overview как пример свидетельства, пригодного для ревью и передачи состояния. |

## Дополнительный 10-проходный real-source pass
Добавлены только реальные изображения из первоисточников / source screenshots, без новых сконструированных диаграмм.
| Local file | Source | Figure id | Why it is included |
| --- | --- | --- | --- |
| `openai-codex-dashboard-workflow.webp` | https://openai.com/index/introducing-codex/ | `fig-openai-codex-dashboard-workflow` | Поток работы как объект: задача, репозиторий, ветка, статус и список задач. |
| `humanlayer-context-firewall.png` | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | `fig-humanlayer-context-firewall` | Подагенты как изоляция контекстного шума и возврат сжатого результата. |
| `humanlayer-backwards-harness.png` | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | `fig-humanlayer-backwards-harness` | Что именно добавляет harness поверх модели. |
| `mae-honeycomb-trace-observability.png` | https://maecapozzi.com/blog/building-a-multi-agent-orchestrator | `fig-mae-honeycomb-trace-observability` | Трасса агентской работы как наблюдаемость процесса. |
| `openai-codex-citations-evidence.webp` | https://openai.com/index/introducing-codex/ | `fig-openai-codex-citations-evidence` | Связь summary, testing evidence, files and cited code lines. |
| `mike-superset-worktrees.png` | https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/ | `fig-mike-superset-worktrees` | Практическая поверхность для нескольких worktrees и агентов. |
| `humanlayer-too-many-mcp-tools.png` | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | `fig-humanlayer-too-many-mcp-tools` | MCP/tool overload как контекстный и trust-boundary риск. |

## Дополнение: SPDD deepening pass

| Файл | Источник | Где используется | Зачем стоит в тексте |
| --- | --- | --- | --- |
| `fowler-spdd-overview.svg` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 11, prompt как delivery artifact | Показывает исходный тезис SPDD: prompt становится first-class delivery artifact, а не одноразовым сообщением. |
| `fowler-spdd-analysis-review.png` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 14, billing engine example | Показывает analysis review: edge cases и technical risks видны до генерации кода. |
| `fowler-spdd-prompt-update.png` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 15, prompt-update vs sync | Показывает случай, где изменение бизнес-правила требует сначала обновить structured prompt. |
| `fowler-spdd-api-test-results.png` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Раздел 16, поведенческая проверка | Показывает expected/actual/result как вторую половину проверяемого свидетельства после test-case overview. |
