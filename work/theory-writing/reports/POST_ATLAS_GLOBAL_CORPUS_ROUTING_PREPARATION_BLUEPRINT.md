# Post-Atlas global corpus routing / preparation blueprint

Статус: proposal / подготовительный blueprint.  
Дата: 2026-06-13.  
Основание: завершённый Атлас из 10 статей, `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md`, `00_spine_map.md`, `CORE_NODES_WRITING_PLAN.md`, существующие A/B/C-фрагменты, досье, истории, текущие правила языка и стиля.

Этот blueprint описывает **общий подготовительный слой** перед созданием планов отдельных глав. Он не пишет главы и не заменяет per-chapter blueprint. Его задача — один раз разложить корпус материалов по будущим главам, чтобы каждый chapter target plan не начинал заново с вопроса «какие источники вообще относятся к этой главе?».

## 1. Зачем нужен отдельный общий слой

Общий слой нужен не как часть каждого chapter package, а как подготовка для самих планов глав. Он создаёт рабочие карты, по которым потом будет собираться каждый конкретный target-group plan.

Если этот слой не сделать, каждый план главы будет заново решать одни и те же вопросы:

- какие статьи Атласа являются primary/secondary/boundary-only для главы;
- какие A/B/C-фрагменты уже содержат синтез по теме;
- какие досье нужно читать как gap-check;
- какие истории дают практические anchors;
- где нужны внешние источники как content discovery, а где только как provenance/assets;
- какие visual candidates не должны засорять главу.

Это создаст повтор, случайность и риск расползания scope. Поэтому общий слой лучше выполнить отдельным target-group package или отдельным рабочим чатом, а не как обычную ad hoc задачу в текущем чате. Он foundational: его outputs будут входами для нескольких будущих планов.

При этом общий слой не должен превращаться в тяжёлую статью или новый Атлас. Его outputs — карты, матрицы, decisions and preparation docs, а не публичные главы.

## 2. Рекомендуемый режим выполнения

Лучший режим:

```text
создать отдельный GLOBAL_CORPUS_ROUTING target-group plan
→ собрать executor package
→ выполнить в отдельном чате / рабочем запуске
→ получить карты для будущих chapter target plans
```

Почему не просто выполнить в текущем чате:

- нужно поднять все важные рабочие документы, Атлас, A/B/C-фрагменты, досье и истории;
- результат должен быть воспроизводимым и включённым в файловую систему;
- ошибки маршрутизации затем будут повторяться во всех главах;
- нужен clear audit trail: что было прочитано, что отнесено к какой главе, что осталось долгом.

Можно сделать маленький ручной набросок в чате, но финальный routing layer лучше делать как package-backed artifact.

## 3. Outputs общего слоя

Рекомендуемые файлы:

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
```

При необходимости `CHAPTER_PACKAGE_INPUT_MATRIX` может стать главным machine-readable-ish документом для будущей manufactury: на одну строку/секцию — одна глава, её mandatory inputs, optional inputs, discovery profile, visual policy and known risks.

## 4. Read-only inputs

Общий package должен читать:

```text
START.md
work/discourse.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
work/atlas/articles/*.md
work/theory-writing/fragments/*.md
work/theory-writing/target-group-plans/*.md
relevant dossiers under work/atlas/dossiers or equivalent paths
relevant story files and story navigation documents
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
```

Если фактический путь к dossier/story corpus отличается, plan должен перечислить точные пути. Нельзя оставлять `relevant files` как placeholder.

## 5. Рабочая очередь общего package

Это не blueprint для написания главы. Поэтому очередь должна быть короче и суше, чем chapter package.

```text
G01 — restore context and confirm active post-atlas baseline
G02 — read Skeleton V5, 00_spine_map, CORE plan and existing source-routing reports
G03 — build/update chapter list and scope map
G04 — map Atlas articles to chapters: primary / secondary / boundary-only / avoid
G05 — inventory A/B/C fragments and route them to chapters
G06 — map dossiers to chapters: mandatory gap-check / optional / visual-source-only / not needed
G07 — route story anchors: sparse practical evidence, not retelling
G08 — identify external discovery profiles by chapter: none / provenance / content discovery / two-hop discovery
G09 — route visual candidates: use in chapter / atlas-reference-only / queue-only / reject-for-chapter
G10 — build chapter package input matrix
G11 — global routing contradiction audit: overloaded chapters, missing inputs, duplicated roles
G12 — language/style clean-up for the generated maps
G13 — final synchronization: discourse, WORKING_DOCUMENTS_MAP, checks
Final — package outputs and readiness status
```

Здесь `G12` использует обычные языко-стилевые правила, но не должен превращать карты в публичные эссе. Цель — ясный, естественный русский и отсутствие машинных словосочетаний; фактические routing decisions должны быть сохранены.

## 6. Discovery profile в общем слое

Общий слой **не выполняет весь внешний поиск для каждой главы**. Он определяет, где discovery нужен и какого типа.

- `D0 — no discovery`: внутренних материалов достаточно.
- `D1 — provenance/restoration`: нужны первоисточники для уже известных claims, figures, docs or repos.
- `D2 — content discovery`: глава имеет содержательную лакуну; внешние источники нужны для самой разработки темы.
- `D3 — two-hop discovery`: первое чтение источников может обнаружить важные новые документы, термины, авторов, diagrams or research lines.

Если глава получает `D2` или `D3`, её конкретный chapter target plan должен включить discovery/unfolding module. Если получает `D0` or `D1`, per-chapter plan не должен держать пустые discovery-проходы «для порядка».

## 7. Как общий слой используется дальше

После выполнения общего routing package будущий chapter target plan должен брать из него:

- список mandatory inputs;
- donor priority;
- какие фрагменты salvaged / superseded / need repair;
- какие досье читать как gap-check;
- external discovery level;
- story anchors;
- visual policy;
- known duplication/degradation risks.

То есть общий слой не является частью per-chapter blueprint. Он является **input-preparation layer** для планов конкретных глав.

## 8. Критерии готовности общего слоя

Final должен проверить:

- все будущие главы имеют scope entry;
- все 10 atlas articles routed хотя бы как primary/secondary/boundary/avoid;
- A/B/C fragments не потеряны без решения;
- dossiers mapped as gap-check, not as first-draft source;
- story anchors sparse and factual;
- external discovery profiles assigned without forcing discovery everywhere;
- visual candidates routed without turning chapters into tool tours;
- chapter input matrix usable for target-plan manufacture;
- outputs written in clear Russian and not in protocol-like prose;
- discourse and working documents map updated.
