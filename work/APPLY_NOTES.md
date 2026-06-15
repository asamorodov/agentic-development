# Инструкция по применению overlay

Базовый snapshot репозитория: полный `git.zip`, загруженный в текущем чате.

Этот overlay собран относительно последнего пользовательского snapshot, а не относительно предыдущего assistant-generated overlay. Поэтому он кумулятивно включает уже выполненные в этой цепочке изменения: лёгкое правило финального closeout, перестройку структуры главы VI вокруг `Маршруты действия`, расширение MCP-секции как внешнего интерфейса, расширение hooks-секции внешними источниками, правку раздела выбора маршрута и русскую перепись всей главы VI.

Текущий overlay дополнительно добавляет отчёт по внешним источникам и кандидатам на иллюстрации для главы VI. Сам текст главы VI в этом проходе не изменялся.

Применение: распаковать архив в корень репозитория. Архив собран в repository-root форме: внутри сразу лежат пути `protocols/...`, `work/...` и другие файлы без дополнительной папки-обёртки.

## Заменить или добавить файлы

Заменить:

```text
START.md
protocols/rules/chat-github-repo-work-protocol.md
protocols/skills/chat-github-repo-work.md
work/theory-writing/chapters/VI_context_working_state_interface.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Добавить:

```text
work/reports/CHAT_REPO_LIGHTWEIGHT_CLOSEOUT_PROTOCOL_UPDATE.md
work/theory-writing/reports/CHAPTER_VI_ROUTES_AND_MCP_INTERFACE_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_HOOKS_SOURCE_EXPANSION_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_ROUTE_SELECTION_AND_NATURAL_RU_PASS_REPORT.md
work/theory-writing/reports/CHAPTER_VI_EXTERNAL_IMAGE_CANDIDATES_REPORT.md
```

## Что добавлено в текущей правке

1. Собран список внешних источников, уже используемых в главе VI и отчётах по её последним правкам.
2. Прочитаны и проверены источники на наличие пригодных визуальных кандидатов: официальные MCP docs/spec, Claude Code hooks, Codex/Kiro/Gemini hooks, Anthropic Agent Skills, Claude Code Agent Teams, Anthropic multi-agent research, LangChain multi-agent patterns, Cognition anti-multi-agent article, Mark Erikson / Mae Capozzi practice reports, MCP examples and related arXiv papers.
3. Добавлен отчёт `work/theory-writing/reports/CHAPTER_VI_EXTERNAL_IMAGE_CANDIDATES_REPORT.md` с приоритизацией кандидатов и proposed local paths.
4. Текст главы VI не изменялся: это asset/source discovery, а не chapter patch.

## Что сохранено из предыдущих изменений этой цепочки

1. Раздел `Маршруты действия` остаётся вводным разделом, а `Skills`, `MCP-сервер`, `Subagents` и `Где инструкция становится вмешательством` остаются разделами уровня `##`.
2. MCP-секция сохраняет техническую фактуру из официальной спецификации: host/client/server, JSON-RPC, initialization handshake, capability negotiation, `stdio`, Streamable HTTP, `resources`, `prompts`, `tools`, discovery и tool/resource/prompt methods.
3. Hooks-секция сохраняет внешние ссылки на Claude Code, OpenAI Codex, Kiro и Gemini CLI и раскрывает hooks как слой жизненного цикла: добавление контекста, барьер политики, обратная связь после действия, финальный барьер, аудит и наблюдаемость.
4. Сохранена синтетическая фигура `fig-vi-mcp-server-interface`.
5. Сохранено лёгкое правило финального закрытия ChatGPT repo/archive задач без отдельного `STATE_CLOSEOUT.md`.

## Проверки

- Глава VI в текущем проходе не изменялась.
- Отчёт по image candidates добавлен в `work/theory-writing/reports/`.
- `work/discourse.md` обновлён, потому что изменилась рабочая позиция по визуальному pass-кандидату главы VI.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` обновлён, потому что добавлен новый отчёт, относящийся к главе VI.
- `work/APPLY_NOTES.md` обновлён под новый кумулятивный overlay.
- Overlay собран в repository-root форме.

- 2026-06-15 — CHAPTER VI FIGURE INTEGRATION: В `work/theory-writing/chapters/VI_context_working_state_interface.md` встроены шесть локальных иллюстраций. Добавлены asset-файлы в `content/assets/theory-images/`: `vi-project-interface-agent.png`, `vi-route-selection.png`, `vi-skills-procedure.png`, `vi-mcp-server-interface.png`, `vi-subagents-orchestration.png`, `vi-hooks-lifecycle.png`.
