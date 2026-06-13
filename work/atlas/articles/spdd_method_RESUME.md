# spdd_method_RESUME

Статус: `resume_from_final_package`.

## Где продолжать

Основная статья: `work/atlas/articles/spdd_method.md`.

Companion-файлы уже синхронизированы с Final state. Начинать следующий проход лучше с:

1. `work/atlas/articles/spdd_method_readiness_report.md` — финальный статус и caveats;
2. `work/atlas/articles/spdd_method_image_plan.md` — визуальные решения и gate по synthetic/external figures;
3. `work/atlas/articles/spdd_method_external_image_queue.md` — очередь внешних ассетов;
4. `work/atlas/articles/spdd_method_open_questions.md` — публикационные blockers.

## Оставшиеся действия перед публикацией

- Выполнить asset-pass для трёх external-real candidates:
  - `fig-ext-openspdd-plan-vs-reasons-canvas`;
  - `fig-ext-openspdd-code-review-report`;
  - `fig-ext-openspdd-sync-bidirectional-flow`.
- После asset-pass заменить inline placeholders локальными `<figure><img ...></figure>` или удалить rejected candidates вместе с нижним разделом `Внешние изображения для asset-pass`.
- Проверить текущие OpenSPDD README/templates, особенно v0.4.9 template links, `/spdd-reverse` и Codex skills / `allow_implicit_invocation: false`.
- Выполнить внешнюю link-check перед публикацией.

## Что не делать без нового задания

- Не превращать статью в install manual OpenSPDD.
- Не расширять `/spdd-reverse` без template-level подтверждения.
- Не заменять готовые локальные изображения синтетическими таблицами.
- Не превращать final theory section в обзор TDAD, ADR, Spec Kit/Kiro или persistent work graph.
- Не сокращать source-level механику ради гладкого summary.

## Последний статус

`package_ready_with_publication_caveats`
