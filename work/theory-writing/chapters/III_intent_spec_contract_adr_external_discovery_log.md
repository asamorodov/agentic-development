# III. External discovery log

Внешняя проверка использовалась точечно. Задача — не расширить список источников, а закрыть места, где глава без внешней опоры была бы слишком быстрой или неточной.

## Проверенные направления

| Направление | Проверенные источники | Вывод для главы |
| --- | --- | --- |
| Минимальная форма ADR | Michael Nygard, “Documenting Architecture Decisions”: <https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions>; Martin Fowler, “Architecture Decision Record”: <https://martinfowler.com/bliki/ArchitectureDecisionRecord.html> | Источники нужны для объяснения ADR как короткой записи решения, а не как тяжёлой архитектурной документации. |
| ADR lifecycle | AWS Prescriptive Guidance ADR process: <https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html>; AWS best practices: <https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/best-practices.html> | Источник достаточен для статусов, ревью, неизменяемости accepted ADR и замещения через новую ADR. |
| `Confirmation` в ADR | MADR template: <https://adr.github.io/madr/decisions/adr-template.html> | Источник достаточен. Он явно описывает `Confirmation` как место, где команда фиксирует, как будет подтверждаться реализация или соблюдение ADR. |
| `CODEOWNERS` и branch protection | GitHub docs: <https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>; <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule> | Источники достаточны для узкого тезиса: review routing может быть автоматическим, а branch protection может требовать ревью code owner. |
| Generated ADR / LLM-assisted ADD | Dhar et al. 2024: <https://arxiv.org/abs/2403.01709> | Достаточно для главы. Источник поддерживает мысль, что модель может помогать в генерации архитектурного решения, но это не равно человеческому уровню и не даёт статуса принятия. |
| Восстановление архитектурной памяти агентом | AgenticAKM: <https://arxiv.org/html/2602.04445v1> | Источник встроен только для узкой линии: восстановленная запись полезна, но она не становится исторически принятой ADR без проверки и статуса. |
| Более новые AI/ADR работы | DRAFT-ing Architectural Design Decisions using LLMs: <https://arxiv.org/abs/2504.08207>; Using LLMs in Generating Design Rationale: <https://arxiv.org/abs/2504.20781> | Оставить в резерве. Они усиливают тему AI-assisted ADR, но в III добавили бы отдельный исследовательский обзор. |
| CODEOWNERS empirical work | Automated Code Review Assignments, 2025: <https://arxiv.org/abs/2512.05551> | Оставить в резерве для XII. Для III достаточно официальной документации GitHub. |

## Решение после ручной ADR-правки

В основной текст входят: Nygard, Fowler, AWS ADR process, MADR, Evolutionary Architecture, GitHub CODEOWNERS/branch protection, Dhar et al. 2024 и AgenticAKM.

Не входят в основной текст: DRAFT 2025, design rationale 2025, CODEOWNERS empirical study 2025, Mneme/cADR/violation-detection papers, подробные инструментальные источники проверки.

Общее правило сохраняется: источник входит в III только тогда, когда помогает различить форму намерения, проверяемое обещание, память решения, статус принятия или рабочую проекцию ADR для агента. Всё остальное остаётся для XI, XII, XIII, Атласа или Handbook.
