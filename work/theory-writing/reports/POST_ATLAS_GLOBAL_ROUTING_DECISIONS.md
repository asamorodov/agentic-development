
# Post-Atlas global routing decisions

Статус: рабочие решения общего routing layer.  
Дата: 2026-06-13.  
Режим выполнения: `repo-snapshot-bound` поверх пользовательского baseline `git(11).zip`.

## Стартовые решения

- Работа идёт в режиме `repo-snapshot-bound`: источники читаются из развёрнутого репозитория, а не из вложенного source bundle.
- Этот пакет не пишет главы, не создаёт per-chapter target plans и не переписывает Skeleton V5, Атлас или A/B/C-фрагменты.
- Внешний поиск сейчас не запускается. Он только классифицируется по будущим главам через профили `D0`/`D1`/`D2`/`D3`.
- Выходы этого слоя становятся входом для будущего изготовления target plans глав.
- Досье используются как gap-check, source restoration и visual/source queues, а не как первый черновой слой глав.
- Атлас используется как concept-first baseline по конкретным методам, но не должен вытеснять уже сделанный A/B/C-синтез.

## Что реально найдено в repo snapshot

Найдены обязательные управляющие входы:

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/target-group-plans/POST_ATLAS_GLOBAL_CORPUS_ROUTING_TARGET_GROUP_PLAN.md
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
work/theory-writing/reports/POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
```

Найдены корпуса:

```text
work/atlas/articles/        # 10 canonical articles + companion files
work/theory-writing/fragments/
work/theory-writing/target-group-plans/
work/dossiers/
work/story_dossiers/
content/stories/
content/assets/
work/theory-writing/asset-catalog/
```

## Missing expected blueprint files

Executor package ожидал два файла, которых нет в текущем snapshot:

```text
work/theory-writing/reports/POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
```

Их содержание не угадывалось и не было создано как фиктивный источник. Для выполнения routing layer использованы ближайшие действующие аналоги:

- для общего слоя — `POST_ATLAS_GLOBAL_CORPUS_ROUTING_TARGET_GROUP_PLAN.md`, `POST_ATLAS_SOURCE_ROUTING_MAP.md`, `POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md`;
- для будущих chapter packages — `POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md`.

Это не блокирует создание карт, но остаётся open question: если пользователь хотел отдельные blueprint-документы с более строгим контрактом, их нужно восстановить или создать перед массовым изготовлением chapter target plans.

## Discovery profiles

- `D0` — внешний поиск не нужен; внутренних материалов достаточно.
- `D1` — нужен короткий source-restoration: восстановить первоисточники, ссылки, изображения или текущие official docs для уже известных claims.
- `D2` — нужен внешний поиск как содержательный материал: тема недособрана внутренним корпусом.
- `D3` — нужен двухшаговый discovery/unfolding: первичное чтение источников может открыть новые документы, авторов, термины, диаграммы или линии аргументации.

## Проверка перегруза и конфликтов

- Нет главы, куда нужно тянуть весь Атлас. Граница: каждая глава получает primary donors, secondary donors и boundary-only donors.
- Все 10 статей Атласа маршрутизированы.
- A/B/C-фрагменты не объявлены устаревшими автоматически: они классифицированы как `base text`, `partial salvage`, `distinction source`, `superseded by Atlas/Skeleton`, `historical only` или `needs repair before use`.
- Досье не используются как primary public source. Они нужны для gap-check и восстановления первичных источников.
- Якоря историй ограничены 3–7 на главу и используются как фактические опоры, а не второй пересказ корпуса историй.
- Visual candidates не превращаются в UI-tour. Большая часть внешних кандидатов остаётся `chapter-queue` до отдельного asset-pass.
- Главный конфликт старой A/B/C-логики и Skeleton V5: старые фрагменты местами организованы вокруг методик, а V5 организован вокруг lifecycle-of-change. Решение: будущий package читает фрагмент ради различения, но пересобирает главу вокруг перехода жизненного цикла.

## Как из этого routing layer делать планы глав

### Базовый вариант

Для главы с профилем `D0` или лёгким `D1` использовать `POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md` в укороченном режиме:

```text
section contract → fragment inventory → atlas donor map → dossier gap-check → synthesis draft → anti-catalog pass → source/provenance → language/style tail
```

Не вставлять пустой external discovery ради симметрии. Если источник нужен только для проверки ссылки, делать короткий source-restoration module.

### Discovery-heavy вариант

Для `D2` и особенно `D3` будущий per-chapter plan должен включать отдельные проходы:

```text
content gap map → bounded external discovery → раскрытия источников → integration decision → source register
```

Discovery не должен расширять scope главы молча. Новая линия получает одно из решений: `integrate now`, `source register only`, `future debt`, `separate appendix/Handbook/Fieldbook`.

### Asset-heavy вариант

Если visual policy главы содержит `inline-use` или сильный `chapter-queue`, план главы должен читать `visual-assets-and-figures.md`, local asset index, external image queues and relevant image plans. Реальные изображения нельзя заменять текстовыми схемами без отдельного решения.

### Repair-heavy вариант

Если основной A/B/C-фрагмент имеет статус `needs repair before use`, план главы сначала делает fragment diagnosis: функция фрагмента, дефекты, конфликт с V5, regression risk. Только после этого пишет синтез главы.

### Что нельзя вытеснить Атласом

- A1/A10 как рамку малого радиуса, единицы изменения и mode selection.
- A2/A3 как уже сделанный синтез specification / contract / ADR.
- A4/B2/C2/C3/C4 как предварительную работу по PWG, evidence и runtime boundary.
- A6/A7/A8/A9 как живые мосты между execution, observation, authority и lifecycle repair.

### Что нельзя тянуть из досье целиком

- Каталоги команд и template-полей.
- Длинные source notes без функции в главе.
- Визуальные очереди как украшение.
- Research survey material, если глава не ставит исследовательский вопрос.

### Где особенно осторожно

- Главы V, VIII, IX и XI легко становятся каталогом методов или инструментов.
- Главы XII и XIII легко уходят в общий governance/maintenance без агентского ядра.
- Введение и заключение легко становятся гладкими обобщениями без технических anchors.
- Gas Town и PWG нельзя смешивать: PWG — состояние продолжения работы; Gas Town — операционная организация вокруг многих работ и агентов.
