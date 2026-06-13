# План написания теоретической главы после Атласа

Статус: post-atlas working plan.  
Дата обновления: 2026-06-13.  
Основание: завершённый concept-first Atlas из 10 статей, `00_spine_map`, `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md`, готовые A/B/C-фрагменты, досье, истории и последние решения по стилю.

## Назначение

Этот документ задаёт порядок перехода от Атласа к написанию глав теории. Он не отменяет A/B/C-фрагменты и не превращает Атлас в единственный источник. Его задача — удержать порядок работы: сначала актуализированная ось и skeleton, затем тяжёлые chapter packages.

## Текущая позиция

Атлас завершён как concept-first baseline. Внешние ассеты ещё требуют общего asset-pass, но это не блокирует написание глав. Для теории важно другое: не возвращаться к досье как первому черновому слою и не писать главы как пересказ десяти статей.

## Источниковая иерархия

```text
00_spine_map / Skeleton V5 / CORE plan — композиция и термины
A/B/C-фрагменты — существующий синтез
Atlas articles — concept baseline
Dossiers — gap-check, source restoration, failure modes, visual/source queues
External sources — content discovery там, где внутренних материалов недостаточно, плюс provenance/assets
Stories — адресные практические якоря
```

Внешние источники не сводятся к проверке готовых claims. Для отдельных глав они должны приносить содержание: новые различения, документы, авторов, диаграммы, исследовательские рамки, контраргументы и словарь.

## Общая последовательность

```text
Фаза 0. Post-atlas spine/skeleton reconciliation. [выполняется этим обновлением]
Фаза 1. Проверка готовых A/B/C-фрагментов относительно Skeleton V5 и Атласа.
Фаза 2. Heavy chapter packages по Skeleton V5.
Фаза 3. Composition pass по всей теории.
Фаза 4. Language/style pass по собранной теории.
Фаза 5. Handbook/Fieldbook routing: что остаётся в теории, что уходит в практические материалы.
```

Старые фазы A/B/C не выбрасываются. Они уже дали материал, который должен быть прочитан в каждом релевантном chapter package.

# Фаза 0. Post-atlas reconciliation

Целевые файлы:

```text
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
```

Выход этой фазы:

- новая главная ось: lifecycle of software change;
- Atlas как готовый baseline, а не будущая задача;
- source routing for chapters;
- heavy chapter package blueprint;
- external discovery needs map.

# Фаза 1. Проверка A/B/C-фрагментов

Перед написанием глав не надо переписывать все фрагменты. Но каждый chapter package должен читать связанные A/B/C-фрагменты и фиксировать их роль:

- **primary synthesis input** — фрагмент является непосредственным материалом главы;
- **boundary/control input** — фрагмент нужен для границы с соседней главой;
- **superseded by Atlas / V5** — фрагмент полезен исторически, но конкретный тезис уже уточнён Атласом;
- **needs repair before chapter use** — фрагмент слишком сырой или стилистически устаревший.

Особые группы:

- `A1`, `00`, `A10` — верхняя ось и mode selection.
- `A2`, `A3`, `B1`, `C1` — specification / SPDD / ADR / protected spec profiles.
- `A4`, `B2`, `C2`, `C3`, `C4` — PWG / process / evidence / runtime boundaries.
- `A5`, `B3` — process profiles and Gas Town.
- `A6`, `A7`, `A8`, `A9` — execution, evidence, authority, lifecycle repair.

# Фаза 2. Heavy chapter packages

Каждая глава получает отдельный package. Базовая форма:

```text
P01 — прочитать discourse, map, 00, Skeleton V5, CORE plan
P02 — section contract
P03 — existing-fragment inventory
P04 — atlas donor map
P05 — dossier gap map
P06 — content gap map
P07 — external source discovery, если нужны внешние содержательные источники
P08 — source unfolding
P09 — integration decision
P10 — first synthesis draft
P11 — anti-catalog pass
P12 — cross-article consistency pass
P13 — source/provenance pass
P14 — chapter repair
P15 — language pass 1
P16 — language pass 2
P17 — style defect audit
P18 — selective natural rewrite
P19 — guarded final human technical style
P20 — regression check
Final — chapter + companion files + discourse/map updates
```

Это стартовая форма, не жёсткая клетка. Если глава почти полностью покрыта A/B/C и Атласом, source discovery может быть короче. Если глава IX, XI, XII или XIII требует внешних материалов, source discovery / unfolding может занять больше проходов.

# Фаза 3. Composition pass

После первых глав нужен отдельный composition pass по всей теории:

- не повторяются ли Atlas summaries;
- не спорят ли термины между главами;
- не выпал ли lifecycle tail;
- не превращается ли теория в каталог методов;
- не потеряна ли связь с историями как практическими якорями;
- не попали ли Handbook/Fieldbook instructions в теоретический слой.

# Фаза 4. Язык и стиль

Новые главы и вставки проходят текущий стиль-хвост:

```text
language pass
→ repair/editorial
→ style defect audit
→ selective natural rewrite
→ guarded final human technical style
```

Критерий: естественный русский технический текст. Не добавлять новые стилевые правила без отдельного решения. Не превращать хорошие примеры в абстрактные пояснительные хвосты.

# Фаза 5. Routing to Handbook / Fieldbook

После composition pass нужно решить, какие материалы не должны оставаться в теории:

- operational checklists → Handbook / Fieldbook;
- tool-specific command recipes → Atlas / Fieldbook;
- decision heuristics → Handbook;
- implementation rituals/package templates → process docs;
- high-level conceptual distinctions → theory.

# Active next step

Следующий рабочий шаг после этого обновления: выбрать первую главу или группу глав и построить для неё heavy chapter package from Skeleton V5. Не начинать главу напрямую из досье или Атласа без package contract.
