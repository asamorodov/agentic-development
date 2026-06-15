# Post-Atlas global corpus routing — repo-level target-group plan

Статус: рабочий target-group plan / proposal for execution.  
Дата: 2026-06-13.  
Режим: **repo-snapshot-bound**. План рассчитан на запуск в корне развёрнутого репозитория, а не на self-contained package со всеми вложенными источниками.

## 0. Назначение

Этот план создаёт общий подготовительный слой перед написанием глав теории. Он не пишет главы и не создаёт планы конкретных глав. Его задача — разложить уже существующий корпус по будущим главам: какие фрагменты, статьи Атласа, досье, истории, внешние источники и визуальные кандидаты должны использоваться в каждом разделе.

Результаты этого плана станут входами для будущих per-chapter target plans. Поэтому план должен дать не красивый обзор, а рабочие карты, по которым можно собирать пакеты глав без повторного выбора источников с нуля.

## 1. Почему это repo-level план

Обычный writing package в этом проекте обычно self-contained: все read-only inputs перечислены в плане и упакованы внутрь исполнительного архива. Для общего routing layer это неудачный режим. Корпус слишком широк: Skeleton, `00_spine_map`, A/B/C-фрагменты, Атлас, companion-файлы Атласа, досье, истории, карты источников, отчёты, visual queues, протоколы и старые target plans.

Поэтому этот план должен исполняться иначе:

```text
исполнитель получает полный репозиторий отдельно
→ запускается в корне репозитория
→ читает источники из файловой системы репозитория
→ создаёт routing outputs внутри `work/theory-writing/reports/`
```

Если позже из этого target plan собирается executor package, такой пакет не должен включать весь корпус источников. Его `START.md` обязан прямо сказать: пакет запускается только рядом с развёрнутым репозиторием; без репозитория он не является самодостаточным.

## 2. Что этот план не делает

План не должен:

- писать главы;
- переписывать Skeleton V5;
- переписывать A/B/C-фрагменты;
- переписывать статьи Атласа;
- запускать полный внешний поиск по всем темам;
- скачивать внешние изображения;
- превращать routing maps в мини-теорию;
- создавать per-chapter target plans.

Он может фиксировать, что для некоторой главы нужен внешний поиск или asset-pass, но сам выполняет только подготовительную маршрутизацию.

## 3. Обрабатываемые файлы

Создать или обновить:

```text
work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md
work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md
work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md
work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_OPEN_QUESTIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_READINESS_REPORT.md
```

Обновить как сопутствующие файлы, если routing decisions меняют рабочее состояние:

```text
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/CHECKS.json
```

Не создавать отдельные пустые файлы для глав, если по главе нет реального решения. В `CHAPTER_PACKAGE_INPUT_MATRIX` достаточно отметить долг или отсутствие решения.

## 4. Источники для чтения

План работает по развёрнутому репозиторию. Поэтому ниже перечислены не вложения будущего package, а области файловой системы, которые исполнитель должен открыть или проиндексировать.

### 4.1. Управляющие документы

```text
START.md
work/discourse.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
```

Если какого-то из этих файлов нет, не угадывать его содержание. Зафиксировать отсутствие в `POST_ATLAS_GLOBAL_ROUTING_OPEN_QUESTIONS.md` и использовать ближайший действующий аналог только после явной отметки в readiness report.

### 4.2. Атлас

```text
work/atlas/articles/*.md
work/atlas/articles/*_theory_links.md
work/atlas/articles/*_source_usage.md
work/atlas/articles/*_image_plan.md
work/atlas/articles/*_external_image_queue.md
work/atlas/articles/*_open_questions.md
work/atlas/articles/*_degradation_and_duplication_audit.md
```

Главный источник по конкретным методам — сами статьи Атласа. Companion-файлы нужны для routing decisions, source gaps, visual candidates and known debts. Не переносить в карты всю фактуру из companion-файлов; фиксировать только то, что влияет на будущие главы.

### 4.3. A/B/C-фрагменты и старые планы теории

```text
work/theory-writing/fragments/*.md
work/theory-writing/target-group-plans/*.md
work/theory-writing/reports/*
```

A/B/C-фрагменты нужно классифицировать не как «черновики выбросить / оставить», а как уже сделанный синтез:

- использовать как основу;
- использовать после repair;
- использовать как source of distinctions;
- заменить Атласом;
- оставить как исторический след.

### 4.4. Досье

```text
work/dossiers/*.md
work/story_dossiers/*.md
work/atlas/dossiers/*.md        # если каталог существует
work/atlas/**/dossier*.md       # если фактическая структура отличается
```

Досье не являются основным first-draft source для глав. Их роль: gap-check, восстановление source-level деталей, failure modes, visual/source queues, проверка того, что Атлас не сжал важное различение. Если досье содержит важный источник, будущая глава должна ссылаться на первоисточник, а не на досье.

### 4.5. Истории

```text
content/stories/*.md
work/story_dossiers/*.md
content/Story_introduction.md
content/Cross_story_synthesis.md
```

Истории используются как sparse practical anchors. Routing layer должен указать, какие истории стоит использовать в каких главах и зачем. Он не должен превращать карту в пересказ 15 историй.

### 4.6. Протоколы

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Язык всех созданных карт должен быть русским. Английские названия методов, файлов, команд, моделей, источников и устойчивые source-native labels сохраняются.

## 5. Discovery profiles

Внешний поиск не включается автоматически в каждую будущую главу. Этот план назначает профиль:

```text
D0 — внешний поиск не нужен; внутренних материалов достаточно.
D1 — нужно восстановить первоисточники для уже известных утверждений, ссылок или изображений.
D2 — нужен внешний поиск как содержательный материал: тема в наших источниках недособрана.
D3 — нужен двухшаговый поиск: первичное чтение источников может открыть новые документы, авторов, термины, диаграммы или линии аргументации.
```

Если глава получает `D2` или `D3`, будущий per-chapter plan должен включить discovery/unfolding module. Если глава получает `D0`, в её plan не вставляются пустые подтверждающие discovery-pass'ы. Если глава получает `D1`, достаточно маленького source-restoration module, когда он действительно нужен.

## 6. Очередь проходов

### G01 — восстановление контекста и режима выполнения

Прочитать `START.md`, `work/discourse.md`, `WORKING_DOCUMENTS_MAP.md`, Skeleton V5, `00_spine_map`, `CORE_NODES_WRITING_PLAN` и два post-atlas blueprint-документа.

Подтвердить в `POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md`:

- работа идёт в repo-snapshot-bound режиме;
- все источники читаются из файловой системы репозитория;
- главы не пишутся;
- внешний поиск не запускается как массовый поиск, а только классифицируется по будущим главам;
- outputs этого package являются входом для будущих chapter target plans.

### G02 — список глав и границы scope

На основе Skeleton V5, `00_spine_map` и `CORE_NODES_WRITING_PLAN` создать `POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md`.

Для каждой будущей главы указать:

- рабочий идентификатор;
- русское название или временный заголовок;
- главный вопрос главы;
- роль в жизненном цикле изменения;
- соседние главы сверху/снизу;
- что глава не должна делать;
- предполагаемый уровень внешнего поиска: preliminary `D0`/`D1`/`D2`/`D3`, который будет уточнён позже.

Не превращать этот файл в новый Skeleton. Это карта scope, а не теория.

### G03 — маршрутизация Атласа по главам

Прочитать все 10 статей Атласа и их `*_theory_links.md`, `*_source_usage.md`, `*_open_questions.md`.

Создать `POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md`.

Для каждой статьи Атласа указать её роль в каждой релевантной главе:

```text
primary — глава должна опираться на статью как на один из главных concept-baseline источников;
secondary — статья даёт контраст, пример или вспомогательное различение;
boundary-only — статья нужна, чтобы не спутать соседние подходы;
avoid / do not import — материал не надо тянуть в главу, чтобы не превратить её в каталог методов.
```

Отдельно отметить повторяющиеся тезисы, которые можно использовать только один раз в теории, а в других главах давать через короткую ссылку или boundary note.

### G04 — маршрутизация A/B/C-фрагментов

Прочитать существующие A/B/C-фрагменты и связанные target plans/reports, если они помогают понять статус фрагмента.

Создать `POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md`.

Для каждого фрагмента указать:

- к каким будущим главам он относится;
- его статус: `base text`, `partial salvage`, `distinction source`, `superseded by Atlas/Skeleton`, `historical only`, `needs repair before use`;
- какие мысли нельзя потерять;
- какие формулировки или английский клей требуют будущего language/style pass;
- где фрагмент конфликтует с post-atlas Skeleton V5.

Не переписывать фрагменты в этом package.

### G05 — карта досье как gap-check

Прочитать методологические досье, story-dossiers и dossier-like документы, которые относятся к Атласу и будущим главам.

Создать `POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md`.

Для каждого досье указать:

- какие главы должны читать его обязательно как gap-check;
- какие главы могут использовать его optional;
- где досье нужно только для visual/source queues;
- какие важные различения или failure modes могли не попасть в Атлас;
- какие первоисточники из досье стоит восстановить в будущей главе.

Не требовать полного покрытия досье. Главный вопрос: что может понадобиться главе и отсутствует или сжато в Атласе/фрагментах.

### G06 — маршрутизация историй

Прочитать `content/stories/*.md`, story introduction, cross-story synthesis и story dossiers по необходимости.

Создать `POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md`.

Для каждой будущей главы указать 3–7 практических anchors максимум, если они есть:

- история;
- какой реальный рабочий паттерн она показывает;
- где она может быть использована в главе;
- почему это не пересказ истории, а короткая фактическая опора.

Если глава не нуждается в stories, зафиксировать это. Не подтягивать истории ради симметрии.

### G07 — внешние source-discovery profiles

На основе Skeleton V5, Атласа, досье, фрагментов и уже существующего `POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md` создать `POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md`.

Для каждой главы указать:

- профиль `D0`/`D1`/`D2`/`D3`;
- почему выбран этот профиль;
- какие темы недособраны внутренними материалами;
- какие seed terms, authors, repos, papers, docs or diagrams могут быть начальной точкой;
- какой риск будет, если внешний поиск не делать;
- какие внешние источники уже известны и требуют только восстановления.

Не выполнять полный внешний поиск в этом package. Если при чтении внутренних материалов уже явно названы источники, их можно записать как seed sources.

### G08 — визуальные кандидаты

Прочитать image plans, external image queues, visual candidates in dossiers, existing local assets and visual reports.

Создать `POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md`.

Для каждой главы классифицировать кандидаты:

```text
inline-use — вероятно стоит вставить в главу после asset-pass;
chapter-queue — хороший кандидат, но требует отдельной проверки;
atlas-reference-only — лучше оставить в Атласе и ссылаться на статью Атласа;
boundary/appendix-only — не для основного текста главы;
reject-for-chapter — уводит в обзор инструментов, UI-tour или чужую тему.
```

Не скачивать изображения. Не создавать synthetic figures без отдельного решения.

### G09 — матрица входов для будущих chapter packages

Создать `POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md`.

Для каждой главы указать:

- обязательные управляющие входы;
- обязательные A/B/C-фрагменты;
- обязательные статьи Атласа;
- обязательные досье для gap-check;
- optional досье и источники;
- story anchors;
- external discovery profile;
- visual policy;
- known risks;
- предполагаемый тип будущего package: normal synthesis, discovery-heavy, asset-heavy, repair-heavy, or composition-heavy.

Эта матрица должна быть самым практичным output всего общего слоя. Её будущий plan-builder должен использовать без повторной инвентаризации всего корпуса.

### G10 — аудит противоречий и перегруза

Создать или заполнить раздел в `POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md`.

Проверить:

- нет ли главы, в которую routed почти весь Атлас;
- не потеряна ли какая-то статья Атласа;
- не потеряны ли A/B/C-фрагменты без решения;
- не используется ли одно и то же досье как primary source в слишком многих главах;
- не превращаются ли stories в второй пересказ корпуса;
- не становятся ли visual candidates UI-tour;
- нет ли conflict между Skeleton V5 and старой A/B/C логикой;
- где нужна ручная decision by user.

Если конфликт нельзя решить уверенно, не прятать его. Записать в `POST_ATLAS_GLOBAL_ROUTING_OPEN_QUESTIONS.md`.

### G11 — плановые указания для будущих chapter target plans

В `POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md` добавить раздел `How to manufacture per-chapter plans from this routing layer`.

Для каждого типа главы указать:

- какой per-chapter blueprint variant выбрать;
- нужно ли включать discovery module;
- нужно ли включать source-restoration module;
- какие материалы нельзя вытеснить Атласом;
- какие материалы нельзя тянуть из досье в полном объёме;
- где будущий plan должен быть особенно осторожен со стилем, каталогизацией или визуальными кандидатами.

Не писать сами per-chapter target plans.

### G12 — языко-стилевая проверка карт

Прочитать созданные карты и отчёты.

Исправить:

- английский клей в русском тексте;
- нечеловеческие словосочетания;
- механическое разворачивание смысла в тяжёлую канцелярскую конструкцию;
- повторяющиеся служебные фразы;
- заголовки, которые звучат как машинные labels.

Не превращать карты в публичные статьи. Их стиль должен быть рабочим и естественным: короткие объяснения, ясные решения, точные списки.

### G13 — финальная синхронизация рабочих документов

Обновить:

```text
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/CHECKS.json
```

В `WORKING_DOCUMENTS_MAP.md` добавить новый routing layer как активный источник для будущих chapter target plans.

В `work/discourse.md` кратко зафиксировать:

- что создан repo-level global corpus routing plan/output;
- что он не является chapter-writing package;
- что per-chapter plans должны использовать его карты;
- что discovery remains modular.

В `CHECKS.json` зафиксировать созданные файлы и результат readiness check.

### Final — readiness report

Создать `POST_ATLAS_GLOBAL_ROUTING_READINESS_REPORT.md`.

Проверить:

- все будущие главы имеют entry в chapter list/scope map;
- все 10 статей Атласа routed;
- A/B/C-фрагменты classified;
- досье classified as gap-check/source/visual/optional;
- stories routed only where useful;
- external discovery profiles assigned without forcing discovery everywhere;
- visual candidates classified;
- `CHAPTER_PACKAGE_INPUT_MATRIX` usable for future target-plan manufacture;
- no placeholder `relevant files` remains in final outputs;
- maps use normal Russian and do not contain English half-sentences except source-native names;
- discourse and working documents map updated.

Readiness statuses:

```text
ready_for_chapter_plan_manufacture
ready_with_open_questions
blocked_missing_repo_sources
blocked_scope_conflict
```

## 7. Критерии качества

Хороший результат общего слоя:

- помогает строить планы глав, а не сам становится главой;
- различает composition sources, concept baseline, gap-check, story anchors and external discovery;
- не заставляет каждую главу снова читать всё;
- не прячет нерешённые вопросы;
- не превращает главы в каталог методов;
- оставляет внешний поиск модульным;
- написан обычным русским рабочим языком.

Плохой результат:

- пытается написать мини-теорию;
- переносит в карты слишком много фактуры из Атласа или досье;
- делает пустые discovery decisions ради симметрии;
- считает досье главным источником глав;
- перечисляет истории без функции;
- создаёт visual queue, которая превращает будущие главы в обзор инструментов;
- содержит английские служебные labels там, где нужен русский текст.
