# A2 figure candidates

## Inline figures after A2 repair

### `fig-a2-three-artifacts-and-substitutions`

- Тип: `synthetic_figure`.
- Решение: оставлена inline в основном A2.
- Причина: объединяет две прежние фигуры — “три артефакта” и “матрицу подмен” — и лучше выражает функцию узла: specification, проверочный контракт/оракул и ADR отвечают на разные вопросы, но опасны именно своими подменами.
- Asset status: внешнего изображения нет; это собственная нетривиальная схема.

### `fig-a2-intent-to-check`

- Тип: `synthetic_figure`.
- Решение: оставлена inline в основном A2.
- Причина: показывает переход от намерения к проверке и не даёт спецификации незаметно стать контрактом/оракулом.
- Изменение после repair: англоязычные labels заменены русскими формулировками, подпись стала публичной, без редакторского мета-текста.

### `fig-a2-status-origin-grid`

- Тип: `synthetic_figure`.
- Решение: оставлена inline в основном A2.
- Причина: фиксирует ключевое различение ADR-линии: происхождение записи (`origin`) не даёт ей статуса принятого решения (`status`).
- Изменение после repair: таблица частично русифицирована, но точные статусы `proposed`, `accepted`, `superseded`, `rejected` сохранены как технические имена.

### `fig-a2-operational-projection-card`

- Тип: `synthetic_figure`.
- Решение после повторного repair: снята с inline и переведена в `deferred_for_technical_atlas`.
- Причина: карточка полезна как практический пример ADR-projection, но в основном A2 она чрезмерно усиливала ADR-ветку и превращала теоретический узел в мини-fieldbook. В основном тексте оставлено правило: рабочая проекция ADR не получает новых полномочий и должна оставаться проверяемой производной от полной записи.

### `fig-a2-confirmation-bridge`

- Тип: `synthetic_figure`.
- Решение: оставлена inline в основном A2.
- Причина: нужна для финального синтеза: проверки подтверждают соблюдение решения, но не заменяют rationale/status ADR.
- Изменение после repair: подпись и схема очищены от английского связующего слоя.

## Кандидаты, снятые с inline после A2 repair

### Старый `fig-a2-three-artifacts`

- Тип: прежняя `synthetic_figure`.
- Решение: объединён с матрицей подмен в `fig-a2-three-artifacts-and-substitutions`.
- Причина: отдельная схема была слишком простой и повторяла соседний абзац.

### Старый `fig-a2-substitution-matrix`

- Тип: прежняя `synthetic_figure`.
- Решение: объединён с `fig-a2-three-artifacts`.
- Причина: как отдельная figure была полезной, но дублировала вводную схему; объединение сильнее держит композиционную задачу.

### Старый `fig-a2-test-oracle-boundary`

- Тип: `synthetic_figure`.
- Решение: снят с inline, оставлен как возможный материал для будущего evidence/oracle section или technical atlas.
- Причина: схема TDAD полезна, но в основном A2 она начинала уводить фрагмент в отдельный узел о проверках и test gaming.

### Старый `fig-a2-reconstructed-adr-lifecycle`

- Тип: `synthetic_figure`.
- Решение: снят с inline, оставлен для technical atlas ADR или будущего раздела про reconstructed ADR.
- Причина: основной A2 должен зафиксировать правило `origin ≠ status`, а не разворачивать полный lifecycle generated/reconstructed ADR.

### `Product Migration oracle gap`

- Тип: `synthetic_figure` / `editorial_visual_idea`.
- Решение: не вставлять inline в A2.
- Причина: Winder.AI уже работает как короткий негативный якорь в тексте; отдельная схема начала бы конкурировать с будущим migration/evidence разделом.

### `Specification correctness bottleneck`

- Тип: `synthetic_figure` / `editorial_visual_idea`.
- Решение: не вставлять inline в A2.
- Причина: тезис Lahiri уже встроен в раздел о спецификации; отдельная схема была бы почти пересказом абзаца.

## Source screenshots / external real image candidates

Source screenshots для A2 пока не нужны в основном теоретическом тексте.

Возможные реальные внешние кандидаты остаются отложенными:

- фрагмент MADR template около `Confirmation` и metadata;
- фрагмент Kiro specs с `requirements.md`, `design.md`, `tasks.md`;
- фрагмент Pact `can-i-deploy` / Pact Matrix;
- фрагмент ADR-шаблона Nygard/MADR около `Context`, `Decision`, `Status`, `Consequences`.

Статус: `external_real_image_candidate` / `asset-pass-required` / `deferred`.

Причина отсрочки: A2 сейчас выполняет теоретическую функцию через собственные схемы. Реальные screenshots могут быть полезны для technical atlas или сайта, но не должны подменяться текстовыми схемами и не должны перегружать A2 интерфейсными деталями.

## Regression note after A2 repair

После повторного repair в основном A2 осталось 4 inline-фигуры вместо прежних 8. Все оставшиеся inline-фигуры являются `synthetic_figure`, проходят usefulness/nontriviality gate и стоят рядом с соответствующим аргументом. Готовые внешние изображения или локальные ассеты не переписывались и не подменялись текстовыми схемами.
