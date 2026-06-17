# Кумулятивная дельта с начала чата — 2026-06-17

Статус: overlay для применения к исходному `git.zip`, загруженному в начале чата.

## Что входит

Дельта объединяет рабочие изменения этой ветки обсуждения:

1. Разные разрезы одного корпуса знаний:
   - Теория — жизненный цикл изменения;
   - Атлас — технические слои;
   - Рабочие сценарии — решения практика;
   - Каталог проблем и решений — типовые сбои, диагностика и восстановление.
2. Атлас зафиксирован как равноправная часть корпуса, не приложение к Теории.
3. Добавлена и уточнена карта Атласа: Level 1 A1–A19 плюс дополнительные Level 2/3 статьи и профили.
4. Добавлены решения по Git/version-control, A9–A19, Kiro/AgenticOps, legacy Atlas routing и reader-oriented entrypoint review.
5. Добавлена многоязычная архитектура корпуса для будущего английского перевода.
6. Harness Engineering внесён как сквозная рамка Скелетона Теории и синхронизирован через `THEORY_CHAPTER_ATTACHMENT_MAP.md`.
7. Скелетон Атласа и связанные документы переписаны более естественным русским языком.
8. Добавлен ADR-0020 и исправлен протокол staged packages: checkpoint archive и continuation package теперь различаются, checkpoint должен упаковываться только после сохранения stop-state и проверяться распаковкой.

## Что не входит

Дельта не включает standalone executor packages, которые выдавались отдельно как рабочие архивы для A1/A2 continuation. Это не изменения репозитория, а отдельные исполняемые артефакты.

Дельта также не меняет публичную навигацию сайта и не переписывает уже написанные главы или статьи. Она обновляет управляющие документы, карты, протоколы и решения.

## Главные новые/изменённые документы

```text
work/atlas/ATLAS_V2_SKELETON.md
work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
work/theory-writing/reports/ATLAS_LEGACY_ARTICLE_ROUTING_NOTE_2026_06_17.md
work/theory-writing/reports/SITE_ENTRYPOINT_AND_READING_ORDER_REVIEW_NOTE_2026_06_17.md
work/theory-writing/reports/HARNESS_ENGINEERING_THEORY_SKELETON_NOTE_2026_06_17.md
work/theory-writing/reports/MULTILINGUAL_READINESS_NOTE_2026_06_17.md
work/multilingual/MULTILINGUAL_CORPUS_PROTOCOL.md
work/multilingual/BILINGUAL_TERM_REGISTRY.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md
```

## Новые ADR

```text
ADR-0012 — Единый корпус знаний и разные разрезы частей
ADR-0013 — Git/version-control как отдельный слой Атласа
ADR-0014 — Атлас как равноправная часть и русские названия
ADR-0015 — Расширение Атласа до A15
ADR-0016 — A16, старые статьи Атласа и вход на сайт
ADR-0017 — Многоязычная архитектура корпуса
ADR-0018 — Harness Engineering в Скелетоне Теории
ADR-0019 — Скелетон Атласа, A17–A19 и дополнительные статьи
ADR-0020 — Корректность checkpoint-архивов и continuation packages
```

## Проверка формы overlay

Архив должен накладываться на корень репозитория. Файлы лежат сразу по путям репозитория, без дополнительной верхней папки.
