# Gas Town v4 patch report

Локальный patch применён к `work/atlas/articles/gas_town.md` без полного переписывания статьи.

## Что добавлено

1. Два external placeholders заменены локальными `source_excerpt_asset` SVG:
   - `fig-gastown-two-tier-beads-flow` → `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg`.
   - `fig-gastown-worker-roles` → `content/assets/atlas-images/gas-town/gastown-worker-roles.svg`.
2. В раздел «Наблюдаемость» добавлен компактный блок о словаре проблемных состояний и командах `bd blocked`, `bd dep tree`, `bd mail`.
3. `gas_town_image_plan.md` и `gas_town_external_image_queue.md` синхронизированы с новой картиной.

## Деградация: быстрые метрики

| Метрика | До patch | После patch |
|---|---:|---:|
| Слов | 6611 | 6856 |
| Строк | 245 | 251 |
| Заголовков | 20 | 20 |
| Figures | 7 | 7 |
| `<img>` refs | 5 | 7 |
| External placeholders | 3 | 0 |
| Local source excerpt assets | 0 | 2 |
| Inline-code delimiters | 270 | 304 |
| Средняя длина предложения | 14.0 | 13.9 |

## Проверка

- Все локальные `<img src=...>` разрешаются: yes.
- Пустые `external-real-candidate` placeholders: 0.
- Статья не получила новых больших разделов; добавлен один короткий смысловой блок и две локальные визуальные выдержки.

## Ограничение

Добавленные SVG — не копии оригинальных Medium-изображений. Это локальные source-derived diagrams по Figure 5 / Figure 6 из `Welcome to Gas Town`; если нужна именно публикация оригинальных картинок, потребуется отдельная проверка прав и качества.
