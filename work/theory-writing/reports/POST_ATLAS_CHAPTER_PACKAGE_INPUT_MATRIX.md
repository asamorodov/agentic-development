
# Post-Atlas chapter package input matrix

Статус: главный практический результат общего слоя маршрутизации.  
Назначение: будущий сборщик планов должен использовать эту матрицу, чтобы не инвентаризировать весь корпус заново.

| Глава | Обязательные управляющие и A/B/C-входы | Главные входы Атласа | Досье gap-check | Якоря историй | Профиль | Визуальная политика | Тип пакета |
| --- | --- | --- | --- | --- | --- | --- | --- |
| INTRO | 00, Skeleton V5, A1, A10, Cross-story | SPDD / Spec Kit / Kiro / BMAD как вторичные доноры | нет обязательных | Boris, Peter, Mark, Calvin | D0 | только уже существующая lifecycle-фигура, если нужна | normal_synthesis |
| I | 00, A1, A10 | SPDD, Spec Kit, Kiro, BMAD | методологические досье только если различения окажутся тонкими | Boris, Peter, Calvin, Mark, HumanLayer | D1 | одна figure про carrier/lifecycle по необходимости | normal_synthesis |
| II | A1, A6, A7, корпус историй | PWG, GSD, BMAD как вторичные доноры | story dossiers для Simon/Arvid/Jökull/Armin, если нужны точные факты | Simon, Arvid, Jökull, Armin, Peter | D2 | story/trace-изображения только под точный тезис | discovery_heavy |
| III | A2, A3, B1, C1 | ADR, SPDD, Spec Kit, CSDD | ADR/SPDD/Spec Kit/CSDD dossiers обязательны | Boris, HumanLayer, Matt, Mike | D2 | ADR/CSDD/SPDD figures только после asset-pass | discovery_heavy |
| IV | B1, C1, 00 | SPDD как основной донор | SPDD dossier обязателен | Boris, HumanLayer, Simon, Matt | D1 | отобранные локальные SPDD-assets | normal_synthesis |
| V | A3, C1 | Spec Kit, Kiro, CSDD, TDAD как основные доноры | четыре соответствующих method dossiers обязательны | Matt, Jökull, Mae, HumanLayer | D2 | внешние / official docs assets в очереди | discovery_heavy |
| VI | A6, C4, A4 | Kiro, GSD, BMAD, Spec Kit, PWG | Kiro/GSD/BMAD/PWG dossiers по разделам | Mark, Matt, Mae, Stripe, Armin | D2 | context/interface assets в очереди | discovery_heavy |
| VII | A4, B2, C2, C3, C4 | PWG основной; Gas Town вторичный | PWG dossier обязателен; Gas Town optional | Jökull, Mark, HumanLayer, Mae | D1 | Beads/PWG state visual вероятно inline | normal_synthesis |
| VIII | A5, B3, C2 | GSD и BMAD основные; Gas Town как граница | GSD/BMAD/Gas Town dossiers обязательны | Jesse, HumanLayer, Mae, Shopify, Matt | D2 | process visuals в очереди | composition_heavy |
| IX | A6, C4, истории | GSD, BMAD, PWG, Gas Town как вторичные доноры | GSD/BMAD/PWG/Gas Town + story dossiers для Armin/Stripe/Shopify | Arvid, HumanLayer, Mike, Armin, Stripe, Shopify | D3 | asset-heavy; не допустить UI-tour | discovery_heavy / asset_heavy |
| X | B3, C2, C4 | Gas Town основной; PWG вторичный | Gas Town dossier обязателен; PWG optional | Jökull, Stripe, Shopify, Mae | D1 | отобранные локальные Gas Town SVG | normal_synthesis |
| XI | A7, C3, A2 | SPDD, ADR, TDAD, CSDD, Kiro, GSD, BMAD | TDAD/ADR/CSDD and evidence-related dossiers обязательны | Simon, Arvid, Jökull, HumanLayer, Mike, Shopify | D3 | evidence visuals требуют сильной provenance | discovery_heavy |
| XII | A8, A2, C3 | ADR, CSDD, GSD, BMAD, PWG | ADR/CSDD/story policy dossiers обязательны | Mike, Jökull, Jesse, HumanLayer, Zig dossier | D3 | policy/authority visuals в очереди | discovery_heavy |
| XIII | A9, C1–C4 | SPDD, ADR, CSDD, Spec Kit, Kiro, GSD, BMAD, PWG | все релевантные method dossiers как gap-check, не как полное покрытие | Matt, Jesse, HumanLayer, Mark, Shopify | D2 | repair/update visuals в очереди | composition_heavy / discovery_heavy |
| CONCLUSION | A10, 00, все routing maps | весь Атлас по ссылке, не как пересказ | досье только для проверки, что не потерян deep node | Peter, Boris, HumanLayer, Mike, Matt | D0 | atlas-reference-only | composition_heavy |

## Риски по типам пакетов

- `normal_synthesis`: риск не в нехватке источников, а в повторении Атласа. Нужен anti-catalog pass.
- `discovery_heavy`: риск бесконтрольного расширения границ. Нужны content gaps, bounded discovery, раскрытие источников и явное решение о включении.
- `asset_heavy`: риск UI-tour. Нужны строгая визуальная политика и объяснение места каждой figure.
- `composition_heavy`: риск гладкой рамки без технических якорей. Нужны конкретные примеры и regression check against deep nodes.
- `repair_heavy`: включать только если основной фрагмент имеет явный defect; не превращать repair в переписывание ради стиля.

## Минимальные общие входы для каждого chapter package

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
релевантные строки из всех карт этого слоя маршрутизации
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/terminology-and-translation.md
protocols/rules/conceptual-translation-glossary.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
```

## Терминологическая оговорка для будущих глав

При языковых проходах словарь применяется ретроспективно: уже написанные `свидетельство`, `наблюдение`, `стенограмма`, `доказательный` и похожие слова нужно проверять как возможные следы прежнего неудачного перевода. Для `evidence` не использовать `наблюдение`; `наблюдение` оставлять для observation-layer, а материал для принятия изменения называть по функции: `результат проверки`, `проверочный материал`, `проверочное основание`, `основание для принятия изменения` или прямое описание проверки.
