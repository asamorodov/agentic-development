# P12. Визуальный слой главы IX

Статус: проход выполнен по черновику `10_10_full_draft.md`, добору `11_11_active_material_intake.md`, правилам `protocols/rules/visual-assets-and-figures.md`, реестрам A6/C4 и фактическому содержимому `content/assets`. Этот файл не означает, что все кандидаты нужно вставлять в главу. Он фиксирует визуальные решения перед следующей редакцией.

## 1. Главная визуальная задача главы

Глава IX легко может превратиться в экскурсию по интерфейсам Codex, Claude Code, Sandvault, Roast, Stripe Minions and HumanLayer. Это неправильное направление. Визуальный слой должен помогать читателю удержать не UI конкретных продуктов, а границу между:

1. поручением пользователю и местом, где агент реально действует;
2. sandbox, permission, approval, command rules и человеческим правом принять изменение;
3. инструментальной поверхностью (`shell`, files, browser, MCP, scripts, logs, services) и долговечным состоянием работы;
4. следом запуска и тем, что можно использовать как проверочный материал;
5. исполняемым workflow/runtime и Persistent Work Graph.

Поэтому визуальный слой главы должен быть строгим и небольшим: несколько объяснительных фигур, одна-две реальные локальные иллюстрации, если они действительно поддерживают аргумент, и отложенный список внешних/исторических кандидатов для asset-pass.

## 2. Проверка локальных ассетов

Фактически доступны в текущем архиве:

| Путь | Размер | Статус для главы IX |
|---|---:|---|
| `content/assets/story-images/07-humanlayer-harness-components.png` | 1280×1026 | `local_image_asset`; сильный кандидат для раздела про harness/tools, но в IX его нужно использовать осторожно, потому что A6 уже ставил HumanLayer как главный asset instrumental surface. |
| `content/assets/story-images/07-humanlayer-too-many-tools.png` | 1530×1380 | `local_image_asset`; сильный кандидат для раздела MCP/tools как визуальное предупреждение о разрастании tool surface. Лучше использовать не вместе с `harness-components`, а вместо него, если глава хочет показать именно цену инструментального расширения. |
| `content/assets/theory-images/humanlayer-too-many-mcp-tools.png` | 1530×1380 | `local_image_asset`; дубль / theory-local версия предыдущего кандидата, предпочтительнее для теоретической главы, если путь принят в сборке. |
| `content/assets/theory-images/humanlayer-context-firewall.png` | 1968×1720 | `local_image_asset`; кандидат не для IX как целого, а для соседних глав о контексте/subagents. В IX скорее отклонить, чтобы не увести текст в context management. |
| `content/assets/theory-images/fowler-harness-overview.png` | 1726×972 | `local_image_asset`; возможный source-backed anchor для `hooks/sensors`, но схема шире IX и легко уведёт к общей теории harness engineering. |
| `content/assets/theory-images/fowler-harness-continuous-feedback.png` | 1332×802 | `local_image_asset`; кандидат для `Hooks and sensors`: хорошо показывает sensors/feedback, но требует аккуратной подписи, что это не approval и не acceptance. |
| `content/assets/theory-images/openai-codex-permission-prompt.webp` | 2160×2160 | `local_image_asset`; сильный реальный кандидат для различения permission prompt и права принять изменение. Подходит лучше, чем общий dashboard screenshot. |
| `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | 1600×1562 | `local_image_asset`; кандидат для browser/devtools как проверочного канала. Не вставлять без подписи, что browser validation даёт наблюдение, а не саму приёмку. |
| `content/assets/theory-images/openai-codex-citations-evidence.webp` | 1920×1080 | `local_image_asset`; кандидат для финального раздела о следе запуска / citations / evidence, но может пересекаться с главой XI про проверку. |
| `content/assets/theory-images/openai-codex-dashboard-workflow.webp` | 3840×2160 | `local_image_asset`; скорее отклонить для IX: слишком общий UI-shot, риск UI-tour. |
| `content/assets/story-images/09-openai-codex-dashboard.webp` | 3840×2160 | `local_image_asset`; дубль dashboard-кандидата, для IX слабее permission prompt / DevTools / citations. |
| `content/assets/story-images/09-openai-codex-terminal-logs.webp` | 1920×1080 | `local_image_asset`; кандидат для следов запуска, но как самостоятельный screenshot может быть менее объяснительным, чем synthetic figure `run → trace → evidence package`. |
| `content/assets/story-images/09-openai-codex-citations.webp` | 1920×1080 | `local_image_asset`; кандидат для финального evidence-моста, но лучше держать для главы XI или использовать только если IX явно говорит о наблюдаемом следе. |
| `content/assets/theory-images/anthropic-coding-agent-flow.webp` | 2400×1666 | `local_image_asset`; внешний flow слишком общий; в IX лучше не использовать, потому что глава не должна объяснять весь coding-agent loop. |
| `content/assets/theory-images/anthropic-autonomous-agent.webp` | 2401×1000 | `local_image_asset`; отклонить для IX: общий маркетингово-архитектурный слой, слабая точность к правам запуска. |

Заявленные в `content/assets/story-images/MANIFEST.md`, но фактически отсутствующие в текущем архиве кандидаты:

- `content/assets/story-images/08-mike-sv-claude.png`, `08-mike-codex.png`, `08-mike-superset.png`, `08-mike-superset-prompt.png`, `08-mike-fork.png` — важны для Sandvault/worktrees, но в этой среде их нельзя вставлять как `<img>`.
- Stripe story 14 assets and Shopify story 15 assets не присутствуют в текущем архиве. Их можно держать только как `external_real_image_candidate` / future asset-pass, если источник и права будут проверены отдельно.

Общий `work/theory-writing/asset-catalog/` в текущем архиве отсутствует, поэтому синхронизация с каталогом не выполнялась. Решения ниже должны стать материалом для будущего chapter-level figure candidates file или общего каталога, если он будет создан.

## 3. Рекомендованный минимальный visual set для главы

Для следующей редакции я бы не вставлял больше четырёх inline-фигур. Оптимальный набор:

1. `fig-ix-runtime-rights-stack` — `source_backed_synthetic_figure` или `synthetic_figure` после usefulness gate. Ставить после вступления. Она должна показать не продукты, а путь действия: задача → рабочая копия/worktree/devbox → sandbox/permissions/approval → shell/files/browser/MCP/services → hooks/logs/tests → diff/trace → review/PWG. Это главная объяснительная фигура IX.
2. `fig-ix-codex-permission-prompt-boundary` — `local_image_asset`, путь `content/assets/theory-images/openai-codex-permission-prompt.webp`. Ставить в раздел `Sandbox, permission и approval — не одно и то же`, если финальная глава хочет иметь один реальный UI-anchor. Подпись должна прямо разводить permission prompt и право принять изменение.
3. `fig-ix-tool-surface-ladder` — `synthetic_figure`. Ставить в `Tools and MCP`. Нужна не таблица “типы tools”, а лестница риска: read-only docs → private read → локальная запись/тесты → external write → project/production/authority mutation. Она лучше объясняет, почему MCP/tool surface не равна “контексту”.
4. `fig-ix-run-trace-to-work-state` — `source_backed_synthetic_figure`, возможно объединённая с C4. Ставить ближе к финалу: run logs / browser screenshots / terminal output / citations / test result → evidence package → gate/review → PWG state update. Это мост к Persistent Work Graph.

Если место позволяет, можно добавить пятый визуальный элемент, но только один из пары:

- `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` для browser/devtools; или
- `content/assets/theory-images/fowler-harness-continuous-feedback.png` для hooks/sensors.

Не стоит вставлять оба: получится каталог каналов наблюдения вместо линии аргумента.

## 4. Figure candidates

| Candidate id | Тип | Где поставить | Решение | Причина / подпись |
|---|---|---|---|---|
| `fig-ix-runtime-rights-stack` | `source_backed_synthetic_figure` | После раздела `От поручения к месту действия` или в конце вступления | `recommended_inline_after_creation` | Главная схема главы: один запуск проходит через несколько границ — рабочее место, sandbox, разрешения, инструменты, наблюдения, след, review/PWG. Основана на материалах OpenAI Codex, Anthropic Claude Code, HumanLayer, Sandvault, Roast, Stripe and C4, но не воспроизводит одну внешнюю картинку. |
| `fig-ix-sandbox-permission-approval-authority` | `synthetic_figure` | `Sandbox, permission и approval — не одно и то же` | `merge_or_replace_with_runtime_stack` | Полезно разводит четыре понятия: sandbox ограничивает среду; permission задаёт режим; approval подтверждает конкретный ход; authority/acceptance остаётся у проекта/человека. Но отдельная схема может дублировать `fig-ix-runtime-rights-stack`; лучше встроить это различение в неё или использовать как текстовую мини-матрицу. |
| `fig-ix-codex-permission-prompt-boundary` | `local_image_asset` | `Sandbox, permission и approval — не одно и то же` | `recommended_inline_if_one_codex_asset_is_used` | Реальный UI prompt полезен именно как наблюдаемая фактура permission boundary. Подпись: “permission prompt останавливает конкретное действие и просит разрешение на запуск команды; он не делает результат правильным и не заменяет review.” Путь: `content/assets/theory-images/openai-codex-permission-prompt.webp`. |
| `fig-ix-sandvault-separate-user-worktree` | `external_real_image_candidate` в текущем архиве; потенциально `local_image_asset` в полном репозитории | `Sandbox` или `Worktrees and devboxes` | `defer_until_asset_available` | Sandvault — лучший реальный визуальный anchor для отдельного пользователя, wrapper and worktree, но ожидаемые `08-mike-*` файлы отсутствуют в текущем архиве. Не заменять синтетикой только потому, что картинка не передана: тезис уже можно раскрыть прозой. |
| `fig-ix-command-rules-decision-chain` | `synthetic_figure` | `Правила команд` | `defer_or_merge_into_text` | Возможная схема: argv/prefix rule → allow/prompt/forbid → most restrictive wins → shell/script обходные формы → смысловой предел правил. Нужна только если раздел останется тяжёлым. В текущем плане лучше прозой, чтобы не раздувать техническую механику. |
| `fig-ix-tool-surface-ladder` | `synthetic_figure` | `Tools and MCP: не контекст, а поверхность действия` | `recommended_inline_after_creation` | Нетривиальная объяснительная польза: показывает, что tools/MCP надо классифицировать по власти над миром, а не по названию “контекст”. Ступени: public docs/read-only → private repo/issues/logs → local write/test → external write → production/project authority. |
| `fig-ix-humanlayer-too-many-mcp-tools` | `local_image_asset` | `Tools and MCP` | `conditional_inline_or_queue` | Реальная HumanLayer иллюстрация наглядно показывает, что “more MCP tools” может стать проблемой контекста и выбора. Путь лучше брать из theory images: `content/assets/theory-images/humanlayer-too-many-mcp-tools.png`. Использовать только если синтетическая ladder не закрывает задачу; вместе их ставить не надо. |
| `fig-ix-humanlayer-harness-components` | `local_image_asset` | `Tools and MCP` или `Local harness` | `defer_for_ix` | Хорошая реальная схема модели внутри harness, но она уже важна для A6 и слишком широка для IX. В главе IX лучше сосредоточиться на правах/поверхностях действия, а не на общем harness anatomy. |
| `fig-ix-codex-browser-devtools-validation` | `local_image_asset` | `Browser/devtools` | `conditional_inline` | Реальный asset полезен, если следующая редакция хочет показать browser/devtools как канал наблюдения. Путь: `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`. Подпись должна сказать, что browser/devtools помогает увидеть поведение приложения, но не превращает проверку в принятие изменения. |
| `fig-ix-browser-as-action-surface` | `synthetic_figure` | `Browser/devtools` | `defer_or_merge_into_runtime_stack` | Возможная схема: browser может быть read/observe, form-fill/action, authenticated service access. Нужна только если раздел о браузере расширится. Иначе лучше не добавлять отдельную фигуру. |
| `fig-ix-hooks-sensors-feedback-loop` | `source_backed_synthetic_figure` or `local_image_asset` | `Hooks and sensors` | `conditional_inline` | Если использовать реальную картинку, лучший доступный путь — `content/assets/theory-images/fowler-harness-continuous-feedback.png`. Но для IX нужно переформулировать подпись: hooks/sensors создают ранний feedback and back-pressure; silence/green signal is not acceptance. |
| `fig-ix-local-harness-surface-map` | `synthetic_figure` | `Local harness` | `defer` | Можно показать `make dev`, `make tail-log`, Playwright/browser, DB scripts, logs, small tools. Но это рискует стать чеклистом. Лучше оставить как прозу, если нет явной композиционной перегрузки. |
| `fig-ix-worktree-devbox-ownership-boundary` | `source_backed_synthetic_figure` | `Worktrees and devboxes` | `defer_or_use_if_section_expands` | Полезная будущая схема: worktree/devbox изолирует diff and runtime state, но не решает ownership/merge/review. Если главе нужен один worktree visual, предпочтительнее реальный Sandvault asset после localization. |
| `fig-ix-roast-executable-workflow` | `external_real_image_candidate` / possible `source_backed_redraw` | `Workflow runtime` | `defer_to_asset_pass_or_technical_atlas` | Shopify Roast workflow лучше показывать реальным README/RubyDoc/tutorial asset или source-backed redraw после отдельного pass. В текущем архиве нет story 15 assets. Не рисовать суррогат ради количества. |
| `fig-ix-durable-execution-vs-durable-work` | `source_backed_synthetic_figure` | `Workflow runtime` | `merge_with_final_trace_figure_or_defer` | Отличие Temporal/LangGraph/DBOS/Restate-style durability от долговечной рабочей памяти важно, но уже покрыто C4. В IX можно не ставить отдельную фигуру, если финальная `run_trace_to_work_state` закрывает мост. |
| `fig-ix-platform-agent-review-bottleneck` | `source_backed_synthetic_figure` | `Platform agents and the review bottleneck` | `defer` | Возможная схема Stripe/enterprise platform: request → devbox → tests/benchmark → PR → review. Но глава и так опирается на Stripe прозой; визуально это лучше оставить для отдельного Stripe article/atlas. |
| `fig-ix-run-trace-to-work-state` | `source_backed_synthetic_figure` | Перед или внутри `След запуска ещё не доказательство` | `recommended_inline_after_creation` | Ключевой мост к C4/PWG: terminal logs, browser screenshots, test results, citations, diff and workflow status становятся usable evidence только после упаковки в claim/evidence/gate/review/state update. Это помогает не смешать “запуск прошёл” и “изменение принято”. |
| `fig-ix-codex-citations-evidence` | `local_image_asset` | `След запуска ещё не доказательство` | `conditional_or_defer_to_XI` | Реальный asset Codex citations/evidence полезен, но глава XI, вероятно, потребует его сильнее. Если IX уже ставит synthetic trace→evidence figure, этот screenshot лучше не вставлять. |
| `fig-ix-openai-codex-dashboard-workflow` | `local_image_asset` | Вступление или platform section | `reject_for_main_ix` | Слишком общий dashboard screenshot. Он показывает продуктовую поверхность, но слабее поддерживает различение прав и следа запуска. Риск UI-tour. |
| `fig-ix-openai-terminal-logs` | `local_image_asset` | `След запуска` или `Local harness` | `defer` | Терминальные логи реальны, но как изображение добавляют меньше, чем схема trace→evidence. Можно использовать только если нужен UI-anchor Codex logs instead of citations. |

## 5. Asset briefs для кандидатов, которые можно вставить после следующего редакторского решения

### `fig-ix-codex-permission-prompt-boundary`

- **Тип:** `local_image_asset`.
- **Путь:** `content/assets/theory-images/openai-codex-permission-prompt.webp`.
- **Размер:** 2160×2160.
- **Где:** после первого или второго абзаца раздела `Sandbox, permission и approval — не одно и то же`.
- **Задача:** показать, что permission prompt — это конкретная остановка перед запуском действия, а не доказательство корректности будущего результата.
- **Возможный alt:** `Codex permission prompt asking whether to allow a command to run in the workspace`.
- **Возможная подпись:** `Permission prompt делает границу действия видимой: агент может попросить разрешение на конкретную команду, но это разрешение не означает, что изменение уже проверено или принято проектом.`
- **Риск:** если рядом уже будет synthetic figure с четырьмя границами, скриншот может стать лишним. Тогда оставить его в кандидаты.

### `fig-ix-humanlayer-too-many-mcp-tools`

- **Тип:** `local_image_asset`.
- **Путь:** `content/assets/theory-images/humanlayer-too-many-mcp-tools.png`.
- **Размер:** 1530×1380.
- **Где:** в разделе `Tools and MCP` после разведения context/tool/action surface.
- **Задача:** показать, что добавление MCP tools не бесплатно: оно увеличивает поверхность выбора и может перегружать контекст/маршрутизацию агента.
- **Возможный alt:** `Diagram comparing a smaller MCP tool set with an overcrowded MCP tool set`.
- **Возможная подпись:** `HumanLayer показывает проблему не как нехватку tools, а как избыток поверхности: чем больше внешних инструментов получает агент, тем важнее описания, routing и ограничения действия.`
- **Риск:** изображение говорит о “too many tools”, но глава IX должна идти дальше и классифицировать tools по правам. Поэтому лучше не вставлять, если будет создана `fig-ix-tool-surface-ladder`.

### `fig-ix-codex-browser-devtools-validation`

- **Тип:** `local_image_asset`.
- **Путь:** `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`.
- **Размер:** 1600×1562.
- **Где:** в разделе `Browser/devtools`.
- **Задача:** показать browser/devtools as observation-and-action channel.
- **Возможный alt:** `Codex using Chrome DevTools MCP to interact with an application and observe validation results`.
- **Возможная подпись:** `Browser/devtools делает запуск ближе к пользовательскому поведению приложения: агент может наблюдать UI, консоль и результат действий. Но это всё ещё канал проверки, а не автоматическая приёмка изменения.`
- **Риск:** скриншот может создать впечатление, что глава рекламирует Codex DevTools. Удерживать подпись на концептуальной границе.

### `fig-ix-fowler-continuous-feedback-hooks`

- **Тип:** `local_image_asset`.
- **Путь:** `content/assets/theory-images/fowler-harness-continuous-feedback.png`.
- **Размер:** 1332×802.
- **Где:** в разделе `Hooks and sensors`.
- **Задача:** показать hooks/sensors как ранний feedback/back-pressure, а не final review.
- **Возможный alt:** `Diagram of continuous feedback sensors around a coding agent, codebase and runtime`.
- **Возможная подпись:** `Sensors and hooks сдвигают часть проверки внутрь среды исполнения: агент получает feedback до человеческого review. Но зелёный сигнал от sensor не равен праву менять рабочее состояние проекта.`
- **Риск:** Fowler figure шире IX и может увести в общую теорию harness engineering. Вставлять только если раздел hooks/sensors в следующем черновике станет центральным, а не проходным.

### `fig-ix-codex-citations-evidence`

- **Тип:** `local_image_asset`.
- **Путь:** `content/assets/theory-images/openai-codex-citations-evidence.webp`.
- **Размер:** 1920×1080.
- **Где:** в разделе `След запуска ещё не доказательство`.
- **Задача:** показать, что продуктовые агенты уже начинают собирать visible evidence/citations, но теоретически это только сырой материал для claim/evidence/gate.
- **Возможный alt:** `Codex interface showing citations and evidence attached to a proposed change`.
- **Возможная подпись:** `Citations and visible evidence make the trace more inspectable, but they still have to be tied to a claim, a work item and a review gate before becoming durable work state.`
- **Риск:** вероятно, это сильнее подходит главе XI про доказательства и проверку. В IX лучше оставить synthetic bridge unless the final draft lacks a real visual anchor near the end.

## 6. Отложенные реальные внешние кандидаты

| Candidate id | Источник / ожидаемый файл | Статус | Причина отложения |
|---|---|---|---|
| `fig-ix-mike-sandvault-sv-claude` | `content/assets/story-images/08-mike-sv-claude.png`; Mike McQuaid / Sandvault | `external_real_image_candidate_in_current_package` | Указан в manifest, но файла нет. Нужен asset-pass или полный репозиторный snapshot. Потенциально очень полезен для sandbox/worktree boundary. |
| `fig-ix-mike-sandvault-superset` | `content/assets/story-images/08-mike-superset.png` / `08-mike-superset-prompt.png` | `external_real_image_candidate_in_current_package` | Может показать worktree/session UI, но не должен превращать IX в историю Sandvault. |
| `fig-ix-shopify-roast-readme-workflow` | Story 15 / Shopify Roast README or docs image | `external_real_image_candidate` | Нужен для technical atlas или workflow runtime subsection, но в текущем архиве asset отсутствует. Не заменять суррогатом без source-backed redraw pass. |
| `fig-ix-shopify-roast-session-resume` | Story 15 / Roast docs/RubyDoc/tutorial | `external_real_image_candidate` | Полезно для session resume/forking, но слишком технически локально для основной IX. |
| `fig-ix-stripe-minions-devbox-or-blueprint` | Story 14 / Stripe Minions Part 2 assets | `external_real_image_candidate` | Полезно для platform-agent section, но потребует rights/source pass and likely belongs in Stripe atlas/story, not main theory chapter. |
| `fig-ix-stripe-integration-benchmark-evidence` | Stripe integration benchmark materials | `external_real_image_candidate` | Лучше для главы XI или отдельного evidence/testing atlas: IX может упомянуть benchmark прозой. |

## 7. Что не вставлять

1. Dashboard screenshots без точного утверждения. Они выглядят внушительно, но часто лишь показывают продуктовую страницу и уводят от теории прав исполнения.
2. Несколько Codex screenshots подряд. Для IX достаточно одного реального Codex anchor, иначе глава станет UI-tour.
3. Одновременно `HumanLayer harness-components` and `too-many-mcp-tools`. Первая объясняет harness anatomy, вторая — инструментальную перегрузку; вместе они распахивают соседнюю тему context/harness.
4. Stripe success/metric visuals без механики. Глава не оценивает производительность Stripe Minions, а различает platform agent substrate and review bottleneck.
5. Схему Roast, нарисованную “по памяти”, если рядом есть реальный README/RubyDoc/tutorial candidate. Нужно либо локализовать настоящий source image, либо сделать честный source-backed redraw после отдельного pass.
6. Скриншоты браузера с приватными данными, реальными аккаунтами или слишком конкретным authenticated service flow. Browser в IX — это граница наблюдения/действия, не демонстрация доступа к пользовательским сервисам.

## 8. Рекомендуемые места вставки в следующем черновике

### После вступления / перед `Sandbox, permission и approval`

Вставить `fig-ix-runtime-rights-stack` как authorial/source-backed synthetic figure. Она должна заменить часть объяснительной нагрузки вступления и подготовить все последующие разделы.

Публичная подпись может быть такой:

> Среда исполнения — это не один переключатель “можно/нельзя”. Один агентский запуск проходит через рабочее место, sandbox, permission policy, конкретные approvals, tool surface, наблюдения и следы запуска. Только после review/gate часть этого следа может стать состоянием работы.

### В разделе `Sandbox, permission и approval`

Вариант A: вставить `fig-ix-codex-permission-prompt-boundary` как реальный UI-anchor.

Вариант B: не вставлять screenshot и оставить только synthetic stack + улучшенную прозу. Этот вариант лучше, если глава и так получит четыре figures.

### В разделе `Tools and MCP`

Вставить `fig-ix-tool-surface-ladder`, если она будет оформлена как компактная публичная схема. Она должна работать лучше, чем просто иллюстрация “too many tools”, потому что держит главный тезис: разные tools несут разную власть, а не просто разный объём контекста.

### В разделе `Browser/devtools`

Не вставлять фигуру по умолчанию. Добавить `fig-ix-codex-browser-devtools-validation` только если после редакции раздел станет опорным, а не промежуточным.

### В разделе `Hooks and sensors`

Не вставлять фигуру по умолчанию. Если раздел будет расширен, использовать Fowler continuous feedback asset or a source-backed synthetic figure, но подпись должна прямо сказать: feedback before review, not acceptance.

### В разделе `След запуска ещё не доказательство`

Вставить `fig-ix-run-trace-to-work-state` как финальную bridge-схему. Она должна быть компактной и не повторять C4 дословно:

`run trace / test result / browser observation / citations / diff → claim + evidence package → review/gate → accepted/rejected/rework → PWG/work state`.

## 9. Возможная форма двух синтетических фигур

Эти формы не являются готовыми `<figure>` для основного текста; это briefs для следующего прохода.

### `fig-ix-runtime-rights-stack`

```text
Поручение пользователя
        ↓
Рабочее место: repo snapshot / worktree / devbox / sandboxed user
        ↓
Политика среды: read-only / workspace / network / secrets / allowed roots
        ↓
Конкретное действие: shell / file edit / browser / MCP tool / external service
        ↓
Контрольные точки: command rules / approval prompt / hook / sensor / test
        ↓
След запуска: diff / logs / screenshots / citations / workflow status
        ↓
Право принять: review / gate / merge / PWG state update
```

Статус: `source_backed_synthetic_figure`. Источниковая база: Codex sandbox/permissions/rules/hooks/MCP/worktrees docs, Claude Code permissions/hooks/browser docs, Sandvault, HumanLayer, C4.

### `fig-ix-tool-surface-ladder`

```text
Read-only knowledge
  public docs, local docs, source search
        ↓
Private observation
  repo, issues, logs, CI, tickets, dashboards
        ↓
Local controlled action
  edit worktree, run tests, seed DB, local browser
        ↓
External project action
  create issue, comment, update branch, call internal API
        ↓
Production / authority action
  deploy, mutate billing/customer data, change policy, merge accepted work
```

Статус: `synthetic_figure`. Источниковая база: MCP spec/security, Codex MCP/permissions, Claude MCP trust caveat, HumanLayer tool-surface critique, Stripe/Ronacher/Arvid практики.

### `fig-ix-run-trace-to-work-state`

```text
Что оставляет запуск:
  logs · terminal output · screenshots · citations · diff · test result · workflow status
        ↓
Что нужно добавить:
  claim · scope · work item · reproduction path · known limits · owner
        ↓
Gate:
  human review · automated check · dependency gate · acceptance/rejection
        ↓
Долговечное состояние работы:
  accepted change · rejected attempt · rework task · recovery note · PWG update
```

Статус: `source_backed_synthetic_figure`. Источниковая база: C4, Beads/PWG, Codex citations/logs, Roast/Temporal/LangGraph/DBOS/Restate distinctions.

## 10. Итоговое решение прохода

- Inline `<img>` в текущий черновик на этом проходе не вставлялись: P12 является визуальным реестром, а не редакцией главы.
- Готовые реальные локальные картинки не пересказывались текстовыми суррогатами. Для каждого сильного local candidate указан статус и риск.
- Главная рекомендация: в следующем черновике добавить две собственные/основанные на источниках схемы (`runtime-rights-stack`, `run-trace-to-work-state`) и максимум один real UI-anchor (`permission prompt` или `browser/devtools`, но не оба без необходимости).
- Sandvault, Roast and Stripe реальные визуалы отложены: часть файлов упомянута в manifest, но отсутствует в текущем архиве; для них нужен отдельный asset-pass или полный snapshot.
- Если следующая редакция добавляет только один visual layer, лучше выбрать `fig-ix-runtime-rights-stack`. Если два — добавить `fig-ix-run-trace-to-work-state`. Если три — добавить `fig-ix-codex-permission-prompt-boundary` как реальный asset.
