# VERIFY — C1_SPECIFICATION_TO_PWG

Статус проверки: `completed_with_known_publication_debts`.

## Проверки перед упаковкой

| Проверка | Результат |
| --- | --- |
| Основной файл существует | OK |
| Все companion-файлы существуют | OK |
| Источники и provenance вынесены в `C1_source_usage.md` | OK |
| Story anchors не превращены в пересказ; решение записано в `C1_story_anchor_map.md` | OK |
| Визуальные решения классифицированы в `C1_figure_candidates.md` | OK |
| Открытые вопросы вынесены в `C1_open_questions.md` | OK |
| Repair-аудит содержит regression audit и readiness status | OK |
| Баланс `<figure>` / `</figure>` в основном файле | OK |
| Баланс `<figcaption>` / `</figcaption>` в основном файле | OK |
| Локальные `img src` не вставлялись без asset-pass | OK |
| В основном тексте нет внутренних `work/` или `protocols/` ссылок | OK |
| В основном тексте нет служебных repair/executor markers | OK |

## Численные проверки основного файла

- Строк: 60.
- Ссылок Markdown: 35
- Inline `<figure>`: 1 synthetic figure.
- Inline `<img>`: 0.

## Известные долги

- Нужен source freshness check перед публикацией, потому что Spec Kit, Kiro и Beads — быстро меняющиеся документации.
- Нужен отдельный asset-pass только если редактор решит вставлять реальные внешние скриншоты/диаграммы или вторую схему.
- На уровне сборки главы может понадобиться единая терминологическая нормализация `gate`/контрольный барьер, `owner`/владелец, `handoff`/передача, `evidence`/свидетельство.

Блокирующих долгов для result archive нет.
