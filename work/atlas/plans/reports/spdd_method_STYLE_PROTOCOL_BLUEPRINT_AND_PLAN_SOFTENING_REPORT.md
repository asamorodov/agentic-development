# SPDD style protocol / blueprint / target-plan softening report

Дата: 2026-06-13  
Основание: после сравнения двух Gas Town outputs пользователь указал, что предыдущая semantic-decompression правка сняла часть явных псевдотерминов, но местами ухудшила русский синтаксис. Проблема была диагностирована как эффект зарегулирования: модель получила слишком сильный сигнал «разворачивать смысл» и начала писать тяжёлые протокольные конструкции вместо нормальной русской технической прозы.

## Изменённые файлы

```text
protocols/rules/human-technical-style.md
protocols/rules/language-style-rules.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
START.md
work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/atlas/plans/reports/spdd_method_STYLE_PROTOCOL_BLUEPRINT_AND_PLAN_SOFTENING_REPORT.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

## Что изменено в стиле

`human-technical-style.md` больше не задаёт два обязательных decompression-pass-а внутри самого протокола. Протокол теперь описывает стиль и типы дефектов, а не число проходов.

Добавлен второй полюс дефекта:

- плохая смысловая свёртка / псевдотермин — когда мысль прячется в искусственное словосочетание;
- плохое механическое разворачивание — когда модель раскрывает мысль в длинную канцелярскую схему.

Новая формула: не «развернуть смысл любой ценой», а сказать мысль нормальным русским техническим текстом. Иногда для этого нужно раскрыть смысл; иногда — наоборот, сократить тяжёлую объяснительную конструкцию до естественной фразы или заголовка.

## Что изменено в blueprint

В `ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` старый хвост:

```text
P24 — style decompression 1
P25 — style decompression 2
P26 — guarded final human technical style pass
```

заменён на:

```text
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style pass
```

`P24` теперь должен сначала отметить реальные дефекты без массового переписывания.  
`P25` правит только выбранные места.  
`P26` отвечает за тон, ритм и связность, но не возвращает псевдотермины и не превращает прозу в протокольную инструкцию.

## Что изменено в SPDD target plan

`spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` приведён к текущей мягкой логике blueprint:

- hard `dossier-backed completeness / relevant but untransferred` gate заменён на main-text-first transfer map and section-local enrichment checks;
- P03 больше не строит тотальную coverage matrix;
- P04–P08 завершаются section-local enrichment check вместо `transfer-audit`;
- хвост плана теперь:

```text
P17 — language pass 1
P18 — language pass 2
P19 — general editorial pass 1
P20 — general editorial pass 2
P21 — general editorial pass 3
P22 — public/article structure and entry-sequence pass
P23 — companion sync / source ledger / image queue pass
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style pass
Final — final verification, package output, readiness status
```

Final check теперь проверяет не тотальное dossier coverage, а main-text fact integration: очевидно несущая для reader question фактура не должна оставаться только в ledger/досье без причины.

## Что не сделано

SPDD executor package `work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip` в этом шаге не пересобирался. После изменения target plan ранее собранный package устарел относительно плана.

Gas Town plan/package не менялись в этом шаге.

## Проверки

- `human-technical-style.md`: удалён блок про два обязательных decompression-pass-а внутри стилевого протокола.
- `ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`: очередь содержит `P24 — style defect audit`, `P25 — selective natural rewrite`, `P26 — guarded final human technical style pass`.
- `spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`: очередь содержит `P17`–`P26 + Final`; языковые проходы идут до repair; старые `transfer-audit` формулировки удалены; `P23` синхронизирует companion outputs.
- `work/discourse.md` и `WORKING_DOCUMENTS_MAP.md` обновлены.
