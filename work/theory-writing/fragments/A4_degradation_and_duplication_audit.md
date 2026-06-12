# A4. Degradation and duplication audit

Цель прохода: проверить, что A4 показывает не только полезность PWG, но и давление сбоев, ради которых механизм нужен.

| Failure mode | Видимость в текущем A4 | PWG-control в тексте | Остаточный риск |
|---|---|---|---|
| Lost state after session break | Сильная: открывающая сцена и повтор в финале. | Prime, handoff, recovery, artifacts, history. | Нужно не перегрузить вводный абзац. |
| False completion | Усилена: done без evidence/gate назван как риск и как нарушение lifecycle. | Evidence before completed; gates before progress. | В финальной версии можно добавить маленькую figure. |
| Duplicated work/reading | Усилена: два агента читают один источник и расходятся в claim. | Owner/claim, source state, canonical write lock. | Нужна аккуратная связь с parallel source work. |
| Stale graph | Есть: риск graph theater/stale graph. | Graph должен читаться и обновляться инструментами. | Нужно решить, кто authoritative за stale detection. |
| Read-snapshot staleness | Есть через STORM boundary и новый failure pressure. | Read snapshot, source state, retry/reopen. | Не смешивать file snapshot и semantic source snapshot. |
| Wrong authority | Есть: agent не должен закрывать human/test gate. | Authority, gates, owner/claim, human decision. | Вопрос: отдельное поле authority или часть gate. |
| Unclosed gates | Есть: gate как durable wait, failure pressure и risk. | Pending/open/closed gate, timeout/escalation. | Нужна типизация gates в финальной схеме. |
| Unsynthesized утверждения с источниковой опорой | Добавлено: source note остаётся в карте без synthesis pass. | Source lifecycle, citation audit, canonical text write. | Нужно решить, является ли это отдельным статусом. |
| Cycle 05 contamination | Отдельно не использовался. | Source usage фиксирует: rejected cycle 05 не основание. | Можно оставить только в рабочей карте, не в главе. |

Вывод: failure-pressure виден достаточно для черновика. Самые сильные зоны — session break, false completion, gates, authority. Самые требующие доработки — stale graph ownership, semantic source snapshot и cleanup as completion criterion.

## Выравнивание несущего фрагмента 9a14858060

Основной фрагмент после выравнивания держит один ход: обрыв сессии → проблема продолжения → переносимое рабочее состояние → границы с соседними системами → жизненный цикл узла. Повторы про failure pressure, authority и соседние инструменты сжаты, но фактура и ссылки сохранены.

Материал, который лучше держать в technical atlas, а не расширять в основном A4:

- полный перечень source-state и переходов между `found/opened/read/used/rejected/needs_reopen`;
- typed evidence schema для тестов, diff, review, source audit, human decision and citation map;
- permission matrix: кто может менять readiness, закрывать gate, принимать evidence и выполнять cleanup;
- подробная lifecycle table для `discovered/scoped → cleaned/archived`;
- degradation matrix для graph theater, stale graph, false completion, wrong authority, semantic convergence trap and unsynthesized утверждения с источниковой опорой.

Риск после выравнивания: текст стал менее похож на список тем, но всё ещё содержит много терминов. В следующем проходе полезно проверить, где английский термин действительно нужен, а где его можно заменить русским объяснением без потери точности.

## Языковой проход 76db4e79ba

Основной фрагмент приведён к более русскому техническому языку без изменения аргумента. Переведён связующий слой: `source note` → заметка об источнике, `synthesis pass` → проход синтеза, `claim` в обычном объяснении → утверждение, `conflicting edits` → конфликтующие правки, `tokens of context` → токены контекста, `workflow context` → контекст рабочего процесса. Имена инструментов, команд, файлов, URL и устойчивые технические маркеры оставлены без русификации.

Остаточный риск: часть англоязычных терминов сохранена намеренно, потому что они являются именами команд, полей, статусов, источников или устойчивыми терминами в цитируемых системах. При публикационном проходе стоит отдельно решить судьбу `gate`, `prime`, `handoff`, `recovery`, `cleanup`, `authority`, `ready/blocked/done`.

## Повторный языковой проход 84062c23f3

Повторно проверены гибриды после русификации. Исправлены места, где английский связующий слой оставался не как имя источника или поле: `Runtime` заменён на «среда исполнения», `compaction` в объяснении — на «уплотнение контекста», `remote/backup` — на «удалённое хранилище» и «резервная копия», `write lock` — на «блокировка записи», `authority` в обычной прозе — на «полномочия», `prompt/session/output` — на «промпт, сессия и выходной результат», `durable work state` — на «долговечное рабочее состояние».

Термины `gate`, `handoff`, `prime`, `recovery`, `cleanup`, `ready`, `blocked`, `done`, `claimed`, `evidence` оставлены там, где они работают как технические маркеры или статусы lifecycle. Это сохраняет различие между близкими понятиями: gate не сводится к обычной зависимости, handoff не сводится к prime, recovery не сводится к handoff, evidence не сводится к произвольному артефакту.

## Первый стилевой проход 3b77731348

Стилевой проход не менял фактические claims и ссылки. Основная правка — убрать ощущение отчётной карточки: объектная форма узла описана через вопросы продолжения, Beads введён как близкий инструментальный случай, различение handoff/prime/recovery раскрыто через моменты работы, boundary section переведён в язык полномочий, а риски PWG собраны в один технический абзац о деградации.

Сохранены конфликтные ограничения: PWG не сводится к task tracker, execution graph, редактору совместной работы или Gas Town; `done` без свидетельства и gate остаётся недействительным; prime не заменяет граф; handoff не равен recovery; источник не считается использованным, пока утверждение не перенесено в канонический текст.

## Второй стилевой проход a792e977b2

Второй стилевой проход проверил, что A4 читается как самостоятельный узел теории, а не как досье по инструментам. Добавлены мягкие переходы: от привычных трекеров задач к Beads, от source-state к границе с долговечным исполнением, от нижнего слоя CRDT/STORM к общей границе полномочий. Смысловые ограничения не ослаблены: инструменты остаются boundary anchors, а не героями самостоятельных историй.

Фигуры уточнены под текущий текст: parallel source work теперь поддерживает проверяемый пакет источников, а prime/compact-refresh показывает пересборку prime из графа на границе `SessionStart` и уплотнения контекста. Story map дополнен guard: будущие истории можно использовать только как короткие проверки конкретных переходов PWG.

## Содержательный provenance pass eec2b912df

План починки:
- Проверить, не стал ли A4 досье или оглавлением: дефектов уровня полной перестройки не найдено; инструменты работают как boundary anchors.
- Проверить source gaps: найден один реальный gap по Gas Town, где текст опирался на внутренние досье для описания верхнего организационного слоя.
- Проверить истории: основной текст не пересказывает Jökull/HumanLayer/Matt Pocock/Shopify Roast; Beads и Gas Town используются как технические anchors.
- Проверить фигуры: `fig-a4-authority-boundaries` требовала обновления источниковой опоры для Gas Town.

Применённые изменения:
- Открыт публичный `gastown/docs/glossary.md`.
- Основной A4 получил ссылку на Gas Town glossary в boundary-параграфе.
- `A4_source_usage.md` обновлён: Gas Town glossary стал публичным citation target, внутренние досье оставлены только как рабочие карты.
- Story map и figure candidates обновлены, чтобы Gas Town не разрастался в A4 до самостоятельной истории.

Остаточный риск: glossary достаточен для узкого boundary-тезиса, но не заменяет отдельный source pass для будущей глубокой главы Gas Town.

## Остаточная починка 6e7b58388e

План остаточной починки:
- Проверить повторы и оглавительный тон после provenance pass.
- Проверить, не осталась ли устаревшая source usage запись про Gas Town как незакрытый gap.
- Проверить длинный boundary-абзац, который мог выглядеть как сухое перечисление систем.
- Проверить figure candidates: поддержаны ли они текущим текстом после правок.

Применённые изменения:
- Boundary-абзац разделён на две части: сначала issue/task/runtime полномочия, затем CRDT/STORM/Gas Town.
- Переход `source-state` заменён на русскую формулировку «линия состояния источников».
- В source usage ранний Gas Town gap помечен как исторический и закрытый проходом eec2b912df.
- В open questions вопрос 11 обновлён: glossary восстановлен для A4, но не закрывает будущую глубокую главу Gas Town.
- Story map и figure candidates получили короткие остаточные заметки; новых историй и фигур не добавлялось.

Оставлено без изменения: основной тезис, source facts, ссылки, lifecycle statuses и приоритетные фигуры. Их правка ради гладкости ослабила бы уже зафиксированные различения.

## Repair 2026-06-11 — A4 composition / visual / language pass

Повторная оценка A4 против target-plan показала, что фрагмент уже выполнял главную функцию: отделял Persistent Work Graph от issue tracker, durable execution, CRDT/shared-state layer, Task Master и Gas Town. Главный дефект был не в оси аргумента, а в старом рабочем слое до новых правил по фигурам и стилю.

Диагностика дефектов:

| Тип дефекта | Где проявлялся | Исправление |
|---|---|---|
| Визуальный | 10 inline-фигур, почти все как `figure-candidate`, часть с пустой схемой и служебной подписью. | В основном тексте оставлены 4 фигуры: один local image asset и три нетривиальные synthetic figures. Остальные кандидаты переведены в deferred/merged/rejected в `A4_figure_candidates.md`. |
| Мета-текст | Подпись к локальному Beads asset рассказывала о восстановлении картинки и локальном файле. | Подпись переписана как публичная: что показывает Beads и зачем это важно для PWG. |
| Языковой | Английский связующий слой: `graph theater`, `false completion`, `wrong authority`, `handoff/recovery/evidence packages`, а также неудачная формула про «хвост жизненного цикла». | Основная проза переведена на русский технический язык: имитация графа, ложное завершение, ошибка полномочий, передача работы, восстановление, проверяемый пакет. Формула про «хвост» удалена. |
| Композиционный | Фигуры начинали превращать A4 в technical atlas по PWG. | Подробные lifecycle/gate/prime/source-work схемы оставлены в companion-файле для будущего atlas/pass, а основной фрагмент удерживает теоретическую границу. |
| Интеграционный | A4 мог частично дублировать B2, если слишком глубоко разворачивать Beads/PWG object model. | Beads оставлен как practical anchor, но основной текст не расширен до Beads-главы; вклад PWG как deep anchor остаётся за B2. |

Regression audit: источники и ссылки сохранены; локальный Beads asset не деградировал в текстовую схему; служебные captions удалены; баланс `<figure>` корректен; старые плохие формулы вроде «хвост жизненного цикла» и `graph theater` убраны из основного A4. Статус после repair: `ready_with_known_debts`. Долги: финально решить, сколько английских lifecycle-статусов (`ready/blocked/done`, `waiting gate`, `completed with evidence`) оставлять в публикационной версии, и вынести подробные lifecycle/gate/prime схемы в technical atlas, если он будет собираться.


## Повторный repair 2026-06-11 — weak-fragment pass

A4 был выбран как один из двух самых слабых фрагментов по repair-отчётам. Диагностика показала, что главный оставшийся дефект — остаточный lifecycle/status language: “Ложное завершение”, англоязычная status-chain и несколько связующих терминов, которые уже не нужны в основном русском тексте.

Повторный repair заменил “Ложное завершение” на “преждевременное закрытие”, перевёл lifecycle-цепочку в русскую прозу, оставил `gates` только как точный Beads term при первом объяснении контрольных барьеров и убрал `organizational OS` / `STORM-like mediator` / `provenance` из основного связующего языка.

Регрессии не обнаружены: PWG-boundary с issue trackers, durable execution, CRDT/STORM, Task Master and Gas Town сохранён; Beads asset сохранён как `<img>`; 4 inline-фигуры остались сбалансированными.
