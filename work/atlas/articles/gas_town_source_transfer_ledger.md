# gas_town — source transfer ledger

Статус после Final: ledger отражает фактический перенос материала в статью. Это не coverage-отчёт по всем проходам.

## Что реально перенесено в основной текст

| Материал | Перенос в статью | Зачем он нужен |
|---|---|---|
| Gas Town как среда для управляемого флота кодовых агентов | H1, вступление, секции про один чат, pressure ladder, финальный вывод | Задаёт предмет статьи: организационная среда, а не «ещё один агент». |
| Early/chaotic/costly intended audience из Yegge | вступление | Защищает от generic multi-agent hype и универсальной рекомендации. |
| Beads/Dolt-backed durable work state | «Нижний слой», minimal frame, финальная theory map | Показывает нижний рабочий объект: identity, dependencies, claim, gates, memory, prime/recovery. |
| Town/Rig split и two-tier Beads | «Два уровня состояния» и external placeholder `fig-gastown-two-tier-beads-flow` | Разводит координацию и проектную реализацию. |
| Role functions: Mayor, Crew, Polecat, Witness, Refinery, Deacon/Dogs | «Роли как функции жизненного цикла» и external placeholder `fig-gastown-worker-roles` | Роли читаются как функции и цены жизненного цикла, а не как персонажи. |
| Convoy/sling/hook/mail protocol | «От поручения к доставке» | Показывает путь поручения от человека к исполнителю и обратно через состояние/почту. |
| MEOW, Formula, Molecule, Wisp, Gate, GUPP | «Декомпозиция работы» | Поддерживает тезис: декомпозиция нужна для адресуемых, назначаемых, проверяемых единиц работы. |
| Queue, scheduler, backpressure, statuses, Dashboard, OTEL | «Очередь и обратное давление», «Наблюдаемость» | Показывает, что масштабирование начинается с capacity control и human review capacity, а не с числа агентов. |
| Recovery through prime/hooks/handoff | «Восстановление» | Отделяет восстановление процесса от восстановления полного смысла ситуации. |
| Service work, diagnostics, backup/doctor/debug/sandbox/sync risks | «Сервисная работа», «Устойчивое состояние само становится инфраструктурой» | Показывает, что долговечное состояние само создаёт инфраструктурную цену. |
| Operation-log gap, HN perception signal, Beads local-first/team boundary | «Что остаётся нерешённым» | Сохраняет критическую границу: Gas Town показывает потребность, но не закрывает весь lifecycle. |
| PWG/process/runtime/evidence/authority/repair theory links | финальная таблица | Связывает Gas Town с общей теорией без повторного теоретического эссе. |

## Что сознательно не перенесено

| Материал | Решение | Причина |
|---|---|---|
| Полный Beads CLI/tutorial | Не переносить | Нарушит границу статьи и превратит её в справочник. |
| Полный каталог ролей/тематических фигур Gas Town | Не переносить | Усилит role glossary вместо механизма жизненного цикла. |
| Подробный UI-tour Dashboard/Problems View | Не переносить сейчас | Observability уже объяснена; готовых скриншотов не найдено/не решено. |
| Внешние queue-only изображения Yegge/Beads/DoltHub | Оставить в image/external queue | Они могут быть полезны позднее, но сейчас визуальная плотность уже высокая. |
| C5/A10 как внутренние ярлыки | Не оставлять в статье как pending labels | Их смысл уже переведён в публичные различения: concept-first entry, режим выбора, PWG/process/runtime/Gas Town boundary. |

## Текущие переносные долги

- Нет незакрытого `C5/A10 sync pending`.
- Нет долга «перенести больше фактуры» из досье: основные технические опоры уже в статье.
- Реальные долги относятся не к переносу, а к публикации: права/качество двух внешних изображений, свежесть version-sensitive источников и возможное сокращение плотных списков без потери якорей.
