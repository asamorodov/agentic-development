# adr_method — source usage

Статус: P27 final synchronized. Файл отражает фактические источники, которые вошли в основной текст статьи. Это не coverage matrix: источник перечислен только тогда, когда он поддерживает фактуру, уже перенесённую в статью.

## Принцип

В основной статье публичные фактические утверждения опираются на первичные или внешне читаемые источники. Внутренние фрагменты A2/A8/A10/C5 использованы как read-only контекст для границ статьи и не поставлены как публичные citation targets.

## Источники, использованные в основном тексте

### Классическая форма ADR и жизненный цикл

- Michael Nygard, “Documenting Architecture Decisions” — минимальная запись ADR, поля `Context / Decision / Status / Consequences`, последовательные номера, `superseded`, стиль разговора с будущим сопровождающим.
- Martin Fowler, “Architecture Decision Record” — короткая запись одного важного решения, дисциплина неизменяемого `accepted` ADR, замена новым ADR, размещение рядом с кодовой базой или в более видимом месте для внешних участников.
- MADR и MADR template — `Decision Drivers`, `Considered Options`, `Decision Outcome`, `Consequences`, `Confirmation`, front matter, категории и практическая посадка в `docs/decisions`.
- `adr-tools` — командная проекция жизненного цикла ADR, включая создание новой записи и замену через `adr new -s`.
- AWS Prescriptive Guidance ADR process — владелец ADR, review/rework/accept/reject, неизменяемость принятой записи, update/supersession и использование ADR в code review.
- WA Government `Decision Finder` — практическая проверка статуса, даты ревью и пригодности решения перед применением.

### Подтверждение решения

- ArchUnit User Guide — структурные проверки архитектуры, PlantUML rules и `FreezingArchRule` для baseline старых нарушений.
- NetArchTest, Import Linter, dependency-cruiser, Nx, Conftest и Open Policy Agent — примеры typed confirmation за пределами Java.
- GitHub CODEOWNERS docs — маршрутизация владельческого ревью и code-owner approval как частичное подтверждение области владения.
- oasdiff, Pact и Pact `can-i-deploy` — два горизонта совместимости API: diff спецификации и матрица consumer/provider.
- k6 thresholds, Google SRE Workbook SLO, Prometheus alerting rules / unit testing rules, Argo Rollouts Analysis, Flagger и OpenFeature — операционные сигналы для performance, SLO, progressive delivery и feature-flag решений.

### Агентская поверхность ADR

- Vercel `adr-skill` — agent-facing ADR process с `Phase 0: Scan the Codebase` и триггерами архитектурного порога.
- 7 ton shark ADR pattern for Claude — индекс ADR и `/adr`-команда вместо полного дампа журнала решений в активный контекст.
- Yotpo cADR — анализ staged/uncommitted changes и commit ranges для создания MADR-кандидатов по архитектурному diff.
- Angular Architects article — короткие правила в `AGENTS.md` / `architecture-boundaries.md`, производные от ADR и проверяемые hook/CI.
- Mneme ADR compiler — status-aware resolver: полные ADR в `docs/adr`, машинно читаемые constraints, компиляция в `project_memory.json`, остановка при конфликтующих accepted-решениях.
- GitHub `gh-aw` Design Decision Gate — PR/CI-точка контроля: детерминированный порог, сбор свидетельств, LLM-черновик и человеческое завершение перед merge.
- Gloaguen et al. 2026 и Zhang et al. 2026 — ограничения активного агентского контекста и различие между запретительными guardrails и общими советами.
- “Architecture Without Architects” — риск архитектурных решений, фактически принятых агентом через diff до явного ADR.

### исследования AI/ADR и реконструкция

- Dhar, Vaidhyanathan, Varma 2024/2025 — генерация Architectural Design Decisions с помощью LLM как черновой процесс, зависящий от контекста и проверки.
- Gupta et al. 2026 — выбор релевантного ADR-контекста для генерации, без полного исторического дампа.
- Nogueira, Silva, Conte 2026 — влияние шаблона ADR на результат записи.
- Su et al. 2026 — LLM-detection of ADR violations как triage-сигнал, а не автоматическое архитектурное решение.
- Fuchß et al. 2025/2026 — traceability и изменение архитектурных решений в LLM-assisted settings.
- AgenticAKM / sa4s-serc repository — pipeline для извлечения архитектурных знаний и generated ADR examples со `Status: Proposed`.
- Microsoft Learn ADR guidance и Belle et al. 2021 — brownfield/retroactive ADR, append-only journal и реконструкция недостающих архитектурных решений.

## Internal context used but not cited as public sources

- `A2_specification_adr_contract.md` — различение спецификации, проверочного контракта и ADR.
- `A8_authority_to_act_vs_complete.md` — граница между правом действовать и правом признать изменение принятым.
- `A10_mode_selection_map.md` — ADR как долговременная память при переходе от разговора/плана к спецификации, PWG и confirmation.
- `C5_theory_to_technical_atlas.md` — требование concept-first самостоятельной статьи.

## P23 sync note

Устаревшие долги source-depth удалены. Текстовая фактура перенесена в основную статью; незакрытым остаётся только asset-level долг по реальным внешним изображениям: права, качество, локализация, alt text и окончательные `<img>`-вставки.
