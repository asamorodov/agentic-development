# A6. Кандидаты на фигуры и визуальные решения

Статус: обновлено после composition / visual / style repair A6. Этот файл не является инструкцией «вставить всё inline». Он фиксирует решения по визуальному слою: что оставлено в основном фрагменте, что отложено в technical atlas, что объединено или отклонено.

## Inline в основном A6

### `fig-a6-agent-environment-four-layers`

- **Класс:** `synthetic_figure`.
- **Решение:** оставить inline.
- **Причина:** это главная композиционная схема A6. Она не дублирует один абзац, а удерживает различение четырёх обязанностей: граница исполнения, инструментальная поверхность, движок рабочего процесса, платформенный агент.

### `fig-a6-sandvault-separate-user-worktrees`

- **Класс:** `local_image_asset`.
- **Локальный путь:** `content/assets/story-images/08-mike-sv-claude.png`.
- **Решение:** оставить inline как `<img>`.
- **Причина:** Sandvault — самый наглядный anchor для границы исполнения: отдельный macOS user, sandbox and wrapper показывают, что права и место действия задаются до вопроса качества результата.
- **Подпись:** публичная, без служебных формул про recovery/source/local file.

### `fig-a6-humanlayer-harness-components`

- **Класс:** `local_image_asset`.
- **Локальный путь:** `content/assets/story-images/07-humanlayer-harness-components.png`.
- **Решение:** оставить inline как `<img>`.
- **Причина:** HumanLayer asset поддерживает различение модели и harness как инструментальной среды работы агента. Он лучше текстового суррогата и не должен перерисовываться.
- **Подпись:** публичная, с явной границей: harness помогает работе агента, но не доказывает завершение изменения.

### `fig-a6-agent-as-node-not-system`

- **Класс:** `synthetic_figure`.
- **Решение:** оставить inline.
- **Причина:** схема держит нетривиальную границу между агентским шагом и более широкой машиной работы в Roast, Quix/Klaus Kode и Stripe Minions. Она заменяет три более узкие схемы `fig-a6-roast-dsl-pipeline`, `fig-a6-quix-klaus-kode-deterministic-corridor` and `fig-a6-devbox-platform-agent-substrate`.

### `fig-a6-same-story-different-layer-matrix`

- **Класс:** `synthetic_figure`.
- **Решение:** оставить inline.
- **Причина:** это ключевая проверка A6: одна история не равна одной категории. Матрица помогает не превращать Stripe, Sandvault, Ronacher/Pi and Roast в отдельные bucket-истории.

### `fig-a6-runtime-vs-pwg-boundary`

- **Класс:** `synthetic_figure`.
- **Решение:** оставить inline.
- **Причина:** нужна как мост к Persistent Work Graph и будущему C4. Она удерживает различие между выполнением шага и долговечным состоянием работы.

## Снято с inline после repair

### `fig-a6-sandbox-permission-boundary`

- **Класс:** `synthetic_figure`.
- **Решение:** `deferred_to_technical_atlas`.
- **Причина:** полезная схема для sandbox/permissions, но в основном A6 её функцию уже выполняет реальный Sandvault asset плюс текст. Inline-дублирование перегружало блок границы исполнения.

### `fig-a6-worktree-lifecycle-and-handoff`

- **Класс:** `synthetic_figure`.
- **Решение:** `deferred_to_technical_atlas`.
- **Причина:** содержит документационные детали Claude/Codex worktrees (`.claude/worktrees/<name>/`, branch naming, `.worktreeinclude`, `$CODEX_HOME/worktrees`). Это полезно для technical atlas, но слишком механично для теоретического A6.

### `fig-a6-claude-codex-worktree-isolation`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_text` / `deferred_to_technical_atlas`.
- **Причина:** тезис “parallel worktrees reduce workspace conflict; acceptance still goes through review” сохранён в прозе. Отдельная схема была банальным повтором соседнего абзаца.

### `fig-a6-logs-browser-local-scripts-as-sensors`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_text`.
- **Причина:** перечень `make dev`, `make tail-log`, Playwright, endpoints, local scripts and database CLI уже работает в прозе. Как фигура он не проходил usefulness/nontriviality gate.

### `fig-a6-ronacher-logs-local-scripts`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_text`.
- **Причина:** дублировал предыдущую схему и абзац про Ronacher. В A6 оставлен текстовый anchor; отдельная схема лучше подходит fieldbook/atlas.

### `fig-a6-mcp-context-cost-vs-deterministic-code`

- **Класс:** `local_image_asset`.
- **Локальный путь:** `content/assets/theory-images/humanlayer-too-many-mcp-tools.png`.
- **Решение:** `deferred_to_A7_or_technical_atlas`.
- **Причина:** реальный asset не переписан в схему и не потерян, но в A6 он создавал лишнюю visual branch внутри блока инструментальной поверхности. Тезис про цену MCP-инструментов сохранён в прозе; изображение лучше рассмотреть для A7/evidence/tool-cost section или technical atlas.

### `fig-a6-pi-minimal-harness-extension-surface`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_text` / `deferred_to_technical_atlas`.
- **Причина:** полезная детализация Pi, но A6 не должен становиться каталогом локальных harness-форм. Pi сохранён как anchor в прозе и матрице.

### `fig-a6-roast-dsl-pipeline`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_fig-a6-agent-as-node-not-system`.
- **Причина:** как отдельная фигура слишком близко к technical atlas / README-пересказу Roast. Нужная мысль сохранена в объединённой фигуре про агента как узел внутри процесса.

### `fig-a6-quix-klaus-kode-deterministic-corridor`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_fig-a6-agent-as-node-not-system`.
- **Причина:** детерминированный коридор Quix важен, но отдельная схема утяжеляла раздел workflow. В основном тексте достаточно прозы и объединённой схемы.

### `fig-a6-devbox-platform-agent-substrate`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_fig-a6-agent-as-node-not-system` / `deferred_to_technical_atlas`.
- **Причина:** платформа Stripe хорошо раскрыта в прозе; отдельная схема была слишком близка к technical atlas.

### `fig-a6-stripe-minion-platform-path`

- **Класс:** `synthetic_figure`.
- **Решение:** `merged_into_text` / `deferred_to_technical_atlas`.
- **Причина:** дублировала `fig-a6-devbox-platform-agent-substrate` и прозу про Stripe. Снята, чтобы Stripe не заняла весь A6.

### `fig-a6-stripe-selective-test-execution-substrate`

- **Класс:** `synthetic_figure`.
- **Решение:** `rejected_for_main_A6`; possible `technical_atlas` only after separate source check.
- **Причина:** уводила A6 в CI/Selective Test Execution. Этот материал может поддерживать отдельный atlas/evidence section, но не нужен для различения среды исполнения.

## Кандидаты, которые не использовать без отдельного pass

- Картинки только с числом Stripe PR/week без механики: риск превратить A6 в оценку успешности Stripe вместо различения платформенного слоя.
- Общие MCP-картинки без конкретного утверждения: риск снова смешать инструментальную поверхность со всей средой агента.
- Скриншоты браузера без подписи о статусе наблюдения: риск внушить, что browser automation сама закрывает приёмку.
- Внутренние досье как источник для фигуры: досье остаются навигацией, не публичной целью ссылки.

## Статус после A6 repair

Основной A6 содержит 6 inline-фигур: 2 реальные локальные иллюстрации и 4 нетривиальные синтетические фигуры. Остальные кандидаты не удалены как идеи, но сняты с inline, потому что дублировали прозу, относились к technical atlas или не проходили usefulness/nontriviality gate для основного теоретического фрагмента.
