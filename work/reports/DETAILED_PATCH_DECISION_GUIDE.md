# Decision guide for detailed consolidated patch

Дата: 2026-06-07  
Статус: помогает принять решение по подробному patch.

## Что изменилось по сравнению с коротким patch

Короткий patch говорил: добавим SDLC artifacts first-class.

Подробный patch говорит точнее: артефакты должны быть сгруппированы в пять классов, чтобы не получить каталог.

Пять классов:

1. Артефакты намерения и решения.
2. Артефакты состояния задачи и проекта.
3. Артефакты среды исполнения и ограничений.
4. Артефакты свидетельства и проверки.
5. Артефакты завершения и хвоста lifecycle.

## Рекомендуемое решение

Принять patch в этом виде, но с ограничителями:

- не добавлять новые top-level части;
- не создавать новых deep anchors;
- не раздувать Part XII;
- создать 7–8 selected dossiers/notes, а не 20;
- после обновления plan перейти к skeleton.

## Если хочется ещё сузить

Минимальный безопасный вариант:

1. Внести правило отбора артефактов.
2. Внести пять классов артефактов.
3. Внести ADR/RFC.
4. Внести process/framework layer.
5. Внести evidence package taxonomy.
6. Внести controlled lifecycle tail.
7. Внести ownership/completion artifacts.

Остальное можно оставить как source-map support.

## Что точно не делать

- Не начинать drafting по старому approved plan.
- Не продолжать широкий source search.
- Не превращать Part XII в ops handbook.
- Не пересобирать SPDD/Gas Town из expanded quarry.

## Дополнение после Stage 0.12

Stage 0.12 добавляет два пункта, которые лучше принять вместе с основным patch:

1. **Архитектурные качества как проверяемые ограничения** — named subsection в Part X, с мостами в Part III, Part VIII and Part XII.
2. **Тестовые данные, тестовая среда и независимость оракула** — named subsection в Part X, с мостами в Part VIII and Part XII.

Оба пункта важнее short mention. Оба не требуют новой top-level части. Оба не должны конкурировать с SPDD or Gas Town.

Обновлённый минимальный безопасный вариант решения:

1. Принять пять классов артефактов.
2. Внести ADR/RFC and decision provenance.
3. Внести process/framework layer.
4. Внести evidence package taxonomy.
5. Внести controlled lifecycle tail.
6. Добавить architecture quality / fitness functions.
7. Добавить test data / test environments / oracle independence.
8. Не запускать новый широкий поиск источников.
