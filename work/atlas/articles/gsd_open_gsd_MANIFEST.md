# MANIFEST — GSD / Open GSD article package

Статус пакета: `completed_with_publication_blockers`.

Пакет собран как overlay: пути внутри архива совпадают с путями, по которым файлы должны лечь в рабочее дерево.

## Target outputs

| Путь | Роль |
|---|---|
| `work/atlas/articles/gsd_open_gsd.md` | Основная самостоятельная concept-first статья. |
| `work/atlas/articles/gsd_open_gsd_source_usage.md` | Companion по использованным источникам и месту их применения. |
| `work/atlas/articles/gsd_open_gsd_source_transfer_ledger.md` | Ledger решений переноса фактуры, сознательных границ и source gaps. |
| `work/atlas/articles/gsd_open_gsd_image_plan.md` | План визуального слоя, disposition dossier candidates и локальных assets. |
| `work/atlas/articles/gsd_open_gsd_external_image_queue.md` | Очередь внешних real-image candidates для будущего asset-pass. |
| `work/atlas/articles/gsd_open_gsd_open_questions.md` | Консолидированные publication blockers и закрытые вопросы. |
| `work/atlas/articles/gsd_open_gsd_theory_links.md` | Смысловые связи статьи с C5/A10 и соседними концепциями. |
| `work/atlas/articles/gsd_open_gsd_degradation_and_duplication_audit.md` | Аудит деградации, дублирования и границ статьи. |
| `work/atlas/articles/gsd_open_gsd_readiness_report.md` | Отчёт готовности и история проходов. |

## Included asset

| Путь | Зачем включён |
|---|---|
| `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | Локальный image asset, на который ссылается `fig-gsd-browser-evidence-analogy` в основной статье. |

## Визуальный статус

В статье есть четыре synthetic figures и один local image asset. Внешние реальные изображения Open GSD не вставлены: ни один официальный rights-safe standalone screenshot/diagram не был выбран для inline placement. Поэтому в основной статье нет нижнего раздела `Внешние изображения для asset-pass`; внешний queue остаётся companion-файлом для будущей публикационной доработки.

## Оставшиеся publication blockers

- свежая проверка release/docs перед датированной публикацией;
- подтверждение lineage/reference paths для `artifact-types.md` и связанных source references;
- внешний real-image pass, если финальная площадка требует реальные Open GSD screenshots/diagrams;
- проверка site assembly для относительного пути локального image asset;
- будущие article-to-article links на соседние статьи атласа.

## File sizes at packaging

| Путь | Bytes |
|---|---:|
| `work/atlas/articles/gsd_open_gsd.md` | 128359 |
| `work/atlas/articles/gsd_open_gsd_source_usage.md` | 36730 |
| `work/atlas/articles/gsd_open_gsd_source_transfer_ledger.md` | 46129 |
| `work/atlas/articles/gsd_open_gsd_image_plan.md` | 22527 |
| `work/atlas/articles/gsd_open_gsd_external_image_queue.md` | 9344 |
| `work/atlas/articles/gsd_open_gsd_open_questions.md` | 5004 |
| `work/atlas/articles/gsd_open_gsd_theory_links.md` | 20940 |
| `work/atlas/articles/gsd_open_gsd_degradation_and_duplication_audit.md` | 23542 |
| `work/atlas/articles/gsd_open_gsd_readiness_report.md` | 27601 |
| `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | 175714 |
| `MANIFEST.md` | 3267 |
| `VERIFY.md` | 3773 |
| `RESUME.md` | 2262 |
| `READINESS_SUMMARY.md` | 1513 |
