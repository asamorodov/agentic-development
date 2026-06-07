# Historical handoff artifact manifest

Этот файл является исторической картой исходного handoff-пакета. Он не задаёт текущий порядок чтения для Codex.

Текущий главный файл задачи:

```text
work/discourse.md
```

Текущий порядок работы задают:

```text
AGENTS.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/chat-codex-transfer-protocol.md
project/source-precedence.md
work/discourse.md
```

## Как читать этот manifest

Имена ниже относятся к старой структуре handoff-архива. В v6 наиболее важные материалы уже перенесены в корень `/work` с плоскими именами: approved plan, source precedence, baseline restore rule, old-site baseline, expanded quarry, source map и seed-файлы.

Этот manifest можно использовать только как справочную карту происхождения материалов, если нужно понять, из какого handoff-документа произошёл тот или иной файл.

## Старые top-level handoff docs

- `00_START_HERE_HANDOFF.md` — старая стартовая точка handoff, заменена текущим `work/discourse.md`.
- `01_CONTEXT_BRIEF.md` — источник контекстного brief.
- `02_APPROVED_DECISIONS.md` — источник утверждённых решений.
- `03_DOCUMENT_ARCHITECTURE_APPROVED.md` — источник approved AI-driven SDLC architecture.
- `04_SOURCE_PRECEDENCE.md` — источник source precedence.
- `05_CODEX_HANDOFF.md` — источник правил использования Codex.
- `06_BASELINE_RESTORE_RULE.md` — источник hard rule for SPDD and Gas Town.

## Старые key inputs

Старые пути вида `inputs/...` больше не являются текущими путями репозитория. Их аналоги находятся в корне `/work`.
