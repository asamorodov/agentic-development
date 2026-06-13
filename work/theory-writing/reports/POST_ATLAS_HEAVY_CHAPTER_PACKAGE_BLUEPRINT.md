# Post-Atlas Heavy Chapter Package Blueprint

Статус: рабочий blueprint для будущих chapter packages.  
Назначение: заменить слишком лёгкую идею section-summary package на процесс, подходящий для синтеза глав после Атласа.

## Почему package тяжёлый

Глава теории сложнее atlas article. Atlas article обобщает один метод. Глава должна синтезировать несколько методов, готовые A/B/C-фрагменты, статьи Атласа, досье, истории и иногда новые внешние источники.

Поэтому chapter package не должен быть коротким summary-процессом. Он должен сначала собрать источник власти главы, затем написать текст, затем проверить, что текст не стал каталогом методов.

## Базовая очередь

```text
P01 — context restore
P02 — section contract
P03 — existing-fragment inventory
P04 — atlas donor map
P05 — dossier gap map
P06 — content gap map
P07 — external source discovery, если он нужен
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
Final — package outputs и обновление discourse/map
```

## Required output files

Каждый chapter package должен создавать:

```text
<chapter>.md
<chapter>_source_usage.md
<chapter>_source_register.md
<chapter>_atlas_donor_map.md
<chapter>_dossier_gap_map.md
<chapter>_external_discovery_log.md
<chapter>_open_questions.md
<chapter>_degradation_and_duplication_audit.md
<chapter>_readiness_report.md
```

Если external discovery не нужен, `external_discovery_log` должен объяснить почему, а не исчезнуть молча.

## P02 section contract

Контракт должен фиксировать:

- что глава должна доказать;
- чем она не должна стать;
- главного и вторичного читателя;
- boundaries with neighboring chapters;
- which Atlas articles are primary donors;
- где может понадобиться external discovery;
- что считается успехом.

## P05 / P06 gap distinction

`dossier gap map` спрашивает: что было во внутренних материалах, но не попало в Атлас или фрагменты?

`content gap map` спрашивает: что остаётся недоразработанным даже после внутренних материалов и требует внешних источников?

Не смешивать эти два слоя. Dossier gap-check — не то же самое, что внешнее исследование.

## P07 / P08 source discovery

Source discovery ограничен content gaps. Нельзя искать широко только потому, что тема интересная.

`source unfolding` должен открывать перспективные источники и идти по важным ссылкам: связанным документам, репозиториям, авторам, терминам, диаграммам, стандартам и конкурирующим рамкам. Именно здесь могут появиться новые источники.

## P11 anti-catalog pass

Главный риск теоретических глав — перечисление методов один за другим. Этот проход должен пересобрать главу вокруг её аргумента.

Bad shape:

```text
SPDD says ... Spec Kit says ... Kiro says ... ADR says ... PWG says ...
```

Good shape:

```text
Глава объясняет один переход или одно напряжение жизненного цикла, а методы использует как evidence и contrast.
```

## Style tail

Use the accepted post-atlas tail:

```text
language pass 1
language pass 2
style defect audit
selective natural rewrite
guarded final human technical style
```

Цель стиля — естественная русская техническая проза. Не добавлять новые стилевые запреты внутри пакетов без явного решения пользователя.

## Final regression check

Final должен проверить:

- no loss of critical distinctions;
- нет молчаливого конфликта со Skeleton V5 или 00;
- концепты Атласа не искажены;
- досье использовались для gap-check, а не для coverage-бюрократии;
- внешние источники встроены только там, где нужны;
- публикационные claims используют первичные источники, где это возможно;
- глава не превращается в summary Атласа;
- style remains natural.
