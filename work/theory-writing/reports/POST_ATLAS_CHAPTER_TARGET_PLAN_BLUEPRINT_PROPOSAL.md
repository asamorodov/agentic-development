# Post-Atlas blueprint для планов написания глав — предложение

Статус: superseded proposal / историческая версия.  
Дата: 2026-06-13.  
> Статус обновлён: этот proposal superseded. Его прежняя версия смешивала global corpus routing и per-chapter writing. Актуальное разделение зафиксировано в `POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md` и `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md`.

Основание: `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md`, `00_spine_map.md`, `CORE_NODES_WRITING_PLAN.md`, готовый Атлас из 10 статей, существующие A/B/C-фрагменты и target plans, досье, story corpus, принятый atlas blueprint и последние решения по стилю.

Этот документ не пишет главы и не заменяет существующие target plans. Его задача — предложить общий blueprint для будущих **chapter target-group plans** после Атласа.

## 1. Что показывает перечитывание Skeleton V5

Skeleton V5 в целом выглядит правильной post-atlas рамкой. Его не нужно переписывать снова. Он уже фиксирует главную ось: агентская разработка меняет не только генерацию кода, а жизненный цикл программного изменения — от намерения и границ задачи до устойчивого состояния работы, evidence, acceptance, recovery и handoff между сессиями, людьми и агентами.

Сильные стороны Skeleton V5:

- Атлас больше не описан как будущая задача, а используется как готовый concept-first baseline.
- У источников появилась нормальная иерархия: skeleton / A-B-C / Атлас / досье / внешние источники / истории.
- SPDD, PWG, Gas Town и ADR поставлены не как отдельные статьи, а как глубокие узлы общей теории.
- В Skeleton уже есть правильный риск: теория не должна стать каталогом методов.
- Внешние источники названы не только verification/assets layer, но и content discovery layer там, где тема недособрана.

Что нужно учесть в chapter-plan blueprint:

1. **Skeleton V5 задаёт композицию, но не должен механически диктовать одинаковую глубину каждой главе.** Некоторые главы почти готовы через A/B/C + Атлас, другие требуют внешнего discovery.
2. **A/B/C-фрагменты нельзя пропускать.** Они не просто старые черновики; это уже проделанный синтез, который должен быть инвентаризирован и либо использован, либо явно признан устаревшим.
3. **Атлас должен быть concept baseline, а не source dump.** Глава не пересказывает SPDD/PWG/Gas Town/ADR, а берёт из них точные понятия, границы и фактические опоры.
4. **Досье нужно читать после Атласа и фрагментов, а не вместо них.** Его роль — gap-check, восстановление деталей, failure modes, source queues.
5. **External discovery должен быть управляемым.** Не широкий поиск «по теме», а поиск по content gaps; при необходимости — двухшаговый: discovery → source unfolding → second-hop decision.
6. **Глава сложнее atlas article.** Atlas article работает по одному методу. Глава синтезирует несколько методов, несколько старых фрагментов, source layers и внешние источники. Поэтому chapter package должен быть не легче atlas package.

## 2. Главное отличие chapter package от atlas article package

Atlas article отвечает на вопрос: «что такое этот метод/механизм и как он работает?»

Chapter package отвечает на другой вопрос: «какой переход жизненного цикла изменения объясняет эта глава, и как разные методы, фрагменты, истории и источники помогают его доказать?»

Отсюда различия:

| Слой | Atlas article | Chapter package |
|---|---|---|
| Главный объект | один метод / механизм | один переход, напряжение или участок lifecycle |
| Главная опасность | конспект или технический appendix | каталог методов вместо аргумента |
| Основной источник | досье + первоисточники | Skeleton + A/B/C + Атлас, затем досье и внешние источники |
| Роль Атласа | результат | concept baseline / donor layer |
| Роль досье | основной quarry | gap-check / restoration layer |
| Внешние источники | уточнение/картинки/проверка | иногда полноценный content source |
| Визуальный слой | допустимо много source images | осторожно: только если помогает аргументу главы |
| Companion files | source/image/theory links по статье | donor maps, gap maps, discovery log, integration ledger |

## 3. Структура chapter target-group plan

Будущий target-group plan для главы должен сохранять формат, который уже хорошо работал в workflow:

1. **Обрабатываемые файлы** — основной chapter output и companion outputs.
2. **Файлы для чтения** — стандартные управляющие документы + chapter-specific inputs.
3. **Очередь prompt records** — gated records для execution package.
4. **Критерии готовности** — что Final должен проверить.

### 3.1. Типовые output-файлы

Минимальный набор:

```text
work/theory-writing/chapters/<chapter_id>.md
work/theory-writing/chapters/<chapter_id>_source_usage.md
work/theory-writing/chapters/<chapter_id>_source_register.md
work/theory-writing/chapters/<chapter_id>_atlas_donor_map.md
work/theory-writing/chapters/<chapter_id>_fragment_inventory.md
work/theory-writing/chapters/<chapter_id>_dossier_gap_map.md
work/theory-writing/chapters/<chapter_id>_content_gap_map.md
work/theory-writing/chapters/<chapter_id>_external_discovery_log.md
work/theory-writing/chapters/<chapter_id>_integration_decisions.md
work/theory-writing/chapters/<chapter_id>_story_anchor_map.md
work/theory-writing/chapters/<chapter_id>_figure_candidates.md
work/theory-writing/chapters/<chapter_id>_open_questions.md
work/theory-writing/chapters/<chapter_id>_degradation_and_duplication_audit.md
work/theory-writing/chapters/<chapter_id>_readiness_report.md
```

Если глава входит в linked target group, например две тесно связанные главы, plan может иметь несколько primary outputs. Но по умолчанию лучше один package — одна глава.

### 3.2. Стандартные read-only inputs

Каждый chapter package должен читать:

```text
START.md
work/discourse.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
```

Chapter-specific inputs добавляются явно:

- relevant A/B/C fragments;
- relevant old target plans, если они содержат useful source routing;
- primary and secondary Atlas articles;
- relevant dossiers;
- selected story files and story dossiers;
- external seed sources, если они уже известны;
- local assets / figure queues, если глава использует визуальный слой.

Нельзя писать `relevant files` без точных путей. Если путь пока неизвестен, это readiness debt для package-builder.

## 4. Source discovery profile

Чтобы external discovery не стал бесконтрольным расширением темы, каждый chapter contract должен выбрать уровень discovery.

### L0 — no new external discovery

Внутренних материалов достаточно. Внешние источники используются только через уже существующие ссылки в Атласе/досье и не открывают новую линию исследования.

### L1 — verification / primary-source restoration

Нужны первоисточники для уже известных утверждений, картинок, цитируемых документов, product docs или repos. Новое содержание почти не добавляется.

### L2 — content discovery

В главе есть содержательная лакуна. Нужно найти внешние источники, которые действительно могут добавить понятия, различения, диаграммы, failure taxonomies, research frames или practical evidence.

### L3 — two-hop discovery

Первое раскрытие источников может вывести на новые документы, авторов, термины, repos, papers или diagrams. Package должен иметь отдельный source unfolding pass и second-hop decision. Это не общий web-surfing: каждая новая ветка должна быть связана с content gap.

## 5. Базовая очередь: 35 рабочих проходов + Final

Это стартовая форма для тяжёлой главы. Она тяжелее atlas article, потому что глава синтезирует несколько source layers. При этом она не должна превращаться в coverage-бюрократию.

```text
P01 — context restore and chapter target confirmation
P02 — chapter contract: thesis, reader question, boundaries, source-discovery level
P03 — skeleton / 00 / neighboring-chapter alignment
P04 — existing-fragment inventory: A/B/C and old fragments
P05 — fragment salvage and anti-degradation baseline
P06 — Atlas donor map: primary, secondary, boundary-only, do-not-use
P07 — Atlas concept alignment: what must not be distorted
P08 — dossier gap map: internal material missing from Atlas/fragments
P09 — content gap map: what is still underdeveloped after internal sources
P10 — external discovery plan, if L1–L3
P11 — external source discovery pass 1, if L2–L3
P12 — source unfolding pass 1: open, read, follow important links
P13 — second-hop discovery/unfolding, if L3 or if P12 exposes a critical gap
P14 — integration decision: use now / source register / future debt / reject
P15 — story anchor map: sparse practical anchors, not story retelling
P16 — visual and asset candidate pass for the chapter argument
P17 — argument outline / reader path
P18 — first synthesis draft
P19 — existing-fragment integration pass
P20 — Atlas integration pass
P21 — dossier/source-detail integration pass
P22 — external-source integration pass, if any
P23 — story-anchor integration pass
P24 — anti-catalog pass: rebuild around argument, not methods
P25 — cross-chapter boundary and terminology pass
P26 — source/provenance pass
P27 — language pass 1
P28 — language pass 2
P29 — general editorial repair 1
P30 — general editorial repair 2
P31 — general editorial repair 3
P32 — chapter entry / public structure / sequence pass
P33 — companion sync: maps, registers, logs, open questions, figure candidates
P34 — style defect audit
P35 — selective natural rewrite
P36 — guarded final human technical style pass
P37 — final regression and readiness check
Final — package outputs, discourse/map update instructions, checks
```

Почему здесь 37, а не 20: текущий `POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md` правильно намечает слои, но слишком сжимает работу. Для главы, которая должна синтезировать Skeleton, A/B/C, Атлас, досье, истории и внешние источники, лучше развести inventory, gap mapping, discovery, integration and anti-catalog checks. Иначе package будет либо писать гладкую главу без содержательной досборки, либо снова провалится в каталог источников.

## 6. Обязательные смысловые guardrails

### 6.1. Не писать главу как пересказ Атласа

Плохая форма:

```text
SPDD делает ... Spec Kit делает ... Kiro делает ... ADR делает ... PWG делает ...
```

Хорошая форма:

```text
Глава объясняет один переход lifecycle, а методы появляются как evidence, contrast и boundary cases.
```

### 6.2. Не возвращать досье как первый черновик

Досье используется после A/B/C and Atlas. Если начать с досье, глава снова станет накоплением фактуры.

### 6.3. Не превращать external discovery в расширение scope

Новый источник может быть важным. Но каждый найденный источник получает решение:

```text
integrate_now
source_register_only
future_debt
visual_asset_queue
reject_with_reason
```

Если source unfolding открывает новую крупную линию, package должен поставить её в debt/separate appendix, а не молча расширять главу.

### 6.4. Не терять старые фрагменты

Если A/B/C fragment имеет сильную формулировку или уже проделанный синтез, глава должна либо использовать его, либо объяснить, почему он superseded by Atlas / Skeleton V5 / current chapter contract.

### 6.5. Не писать Handbook внутри теории

Operational checklists, tool recipes, step-by-step rituals and package-execution instructions должны уходить в Handbook / Fieldbook / process docs. Теория оставляет conceptual distinctions, lifecycle transitions, evidence and boundaries.

## 7. Языко-стилевой хвост

Сохраняется хвост, который сработал для последних статей Атласа:

```text
language pass 1
language pass 2
general editorial repair 1
general editorial repair 2
general editorial repair 3
chapter entry / public structure / sequence pass
companion sync
style defect audit
selective natural rewrite
guarded final human technical style pass
```

Языковые проходы идут до repair/editorial. Они приводят текст к русскому режиму, убирают английский клей и оставляют английский только для имён, команд, путей, source labels and устойчивых терминов. Repair после этого работает уже с русским текстом.

Стилевой блок не должен добавлять новые правила. Приоритет: естественный русский технический текст. Не надо снова расширять протокол стиля ради каждого нового наблюдения. Если пользовательская правка показывает новую устойчивую закономерность, её лучше сначала копить как calibration note, а не превращать в новый gate.

## 8. Визуальный слой для глав

Для глав визуальный слой осторожнее, чем в Атласе. Главе нужны не все source screenshots, а только те изображения, которые поддерживают аргумент главы.

Типы решений:

- `local_image_asset` — готовый asset можно использовать, если он прямо помогает главе.
- `external_real_image_candidate` — обычно queue-only до общего asset-pass, если картинка не является центральной для главы.
- `synthetic_figure` — допустима, если схема объясняет lifecycle transition или boundary, который сложно удержать прозой.
- `atlas_reference_only` — картинка остаётся в статье Атласа; глава только ссылается на концепт.
- `reject_for_chapter` — картинка полезна для tool overview, но ломает главу.

Chapter package не должен превращать теоретическую главу в visual tour по инструментам.

## 9. Companion files: зачем они нужны

Companion files не являются бюрократией. Они нужны, чтобы удержать сложный synthesis process без засорения главы.

- `atlas_donor_map` — какие статьи Атласа использованы и как.
- `fragment_inventory` — какие старые фрагменты использованы, superseded or need repair.
- `dossier_gap_map` — что внутренний quarry добавляет сверх Атласа.
- `content_gap_map` — что не покрыто внутренними материалами.
- `external_discovery_log` — что искали, что нашли, что отклонили, что требует unfolding.
- `integration_decisions` — почему материал вошёл или не вошёл в главу.
- `story_anchor_map` — где истории работают как короткие практические anchors.
- `source_register` — publication-grade sources and unresolved source debts.
- `figure_candidates` — визуальные решения без захламления текста.

## 10. Final regression check

Final должен проверить:

- chapter output exists and matches contract;
- глава не стала summary Атласа;
- глава не стала catalog of methods;
- Skeleton V5 and `00_spine_map` не искажены;
- A/B/C-фрагменты не потеряны без решения;
- Atlas concepts used accurately;
- dossier gaps processed without coverage bureaucracy;
- external discovery level respected;
- no uncontrolled scope expansion from source unfolding;
- story anchors sparse and factual;
- publication claims have primary sources where possible;
- visual candidates classified, no broken image refs;
- Handbook/Fieldbook material routed out;
- language/style tail completed;
- текст звучит естественно по-русски;
- companion files synchronized;
- readiness status set.

## 11. Как использовать этот blueprint дальше

Следующий практический шаг — не писать главу напрямую, а сделать `CHAPTER_TARGET_PLAN_MANUFACTORY` или первый manual target plan для одной главы.

Я бы начал с одного пилотного plan, а не со всех глав сразу. Хорошие кандидаты:

1. **VII. Persistent Work Graph как устойчивый граф работы** — центральный механизм, хорошо проверяет Atlas/PWG/Gas Town/BMAD/GSD synthesis.
2. **III. Намерение, спецификация, контракт и архитектурное решение** — хорошо проверяет SPDD/Spec Kit/ADR/Constitutional SDD synthesis.
3. **XI. Свидетельства, тесты, ревью и качество доказательства** — требует external content discovery и поэтому хорошо проверяет discovery loop.

Пилот должен показать, не слишком ли тяжёлый blueprint, не хватает ли external discovery depth and не портит ли хвост естественность языка.
