# Source register — Chapter IV SPDD specification lifecycle

## Core sources actually used in the chapter

- `work/atlas/articles/spdd_method.md` — internal Atlas reference for the detailed SPDD/OpenSPDD treatment; the chapter links to it instead of reproducing it.
- Fowler/Thoughtworks, `Structured-Prompt-Driven Development` — основная рамка: промпт как артефакт поставки; пример биллинга; идея structured prompt как носителя намерения.
- OpenSPDD README — различение обычного плана и REASONS Canvas; общий цикл и роль структурированных промптов.
- OpenSPDD `/spdd-reasons-canvas` template — техническая опора для Canvas: полный ввод через `@`-файлы/папки, семь секций, запрет перехода к реализации без подтверждения.
- OpenSPDD `/spdd-generate` template — техническая опора для реализации по Canvas: идти по Operations, соблюдать Norms/Safeguards, не расширять область без возвращения проблемы в спецификацию.
- OpenSPDD `/spdd-api-test` and `/spdd-code-review` templates — ограниченно, только как примеры проверки, выведенной из Canvas; не превращены в самостоятельную главу о тестировании.
- OpenSPDD `/spdd-prompt-update` and `/spdd-sync` templates — обратные ходы после генерации: изменение намерения и синхронизация Canvas с принятым кодом.
- OpenSPDD `/spdd-reverse` template — отдельная линия восстановления рабочего спецификационного слоя по старому коду; в главе трактуется как описательный кандидатный Canvas, не как восстановление исходного намерения.
- OpenSPDD design philosophy — граница метода: Canvas на уровне фичи, repo-level conventions отдельно; structured prompt сужает интерпретацию, но не заменяет человеческое решение; риск stale Canvas.
- Fowler, `Understanding Spec-Driven-Development` — короткое финальное позиционирование SPDD как spec-anchored режима, не как spec-as-source для всей системы.

## Internal / story anchors

- Boris Tane story — минимальная дисциплина `research.md → plan.md → implement` как предшественник более строгого Canvas.
- HumanLayer story — предупреждение о цене плохой ранней карты задачи; связано с человеческим подтверждением Canvas до автономного выполнения.

## Anti-catalog decision

Команды SPDD оставлены только там, где они держат одну из двух опор главы:

1. полный цикл нового изменения: намерение → Canvas → генерация → проверка → обновление спецификации;
2. обратный вход для старого кода: существующая реализация → описательный кандидатный Canvas → дальнейшая работа через тот же цикл.

Неиспользованные или пограничные материалы не разворачивались в самостоятельные обзоры, чтобы глава не стала каталогом команд OpenSPDD.

## Visual material decision

The SPDD-cycle figure is now inserted in the main chapter:

- `content/assets/theory-images/fowler-spdd-workflow.svg`

The figure is placed after `## Полный рабочий цикл`. It is used to show lifecycle movement, not to turn the chapter into a command catalog. The full visual layer remains in the SPDD Atlas article.
