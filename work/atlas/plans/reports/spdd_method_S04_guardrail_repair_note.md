# S04 guardrail repair note: `spdd_method`

Mode: `repair_existing`.

## Проверка

Plan был проверен против guardrails будущего article-writing package. Все read-only paths из плана существуют в текущем snapshot. Future outputs перечислены последовательно: основной article file, source usage, transfer ledger, image plan, external image queue, open questions, theory links, degradation audit and readiness report. Long/short companion filename mismatch не обнаружен. Internal length limits or `keep concise`-style instructions не обнаружены.

## Найденные дефекты

1. P12 говорил про inline placeholders and image queue, но не требовал нижний раздел `Внешние изображения для asset-pass` в самой статье. Это могло привести к потере external-real candidates при будущей сборке.
2. Final verification проверял результат слишком обобщённо; требовалось явно проверить существование and synchronization реальных output-файлов.
3. В плане оставалось немного английского клея в рабочих формулировках; он частично очищен, но source terms вроде `source usage`, `image plan`, `external-real candidate`, `readiness` сохранены как рабочие имена артефактов/статусов.

## Изменения

- P12 усилен: external-real candidates должны иметь inline placeholder, нижний раздел `Внешние изображения для asset-pass` and запись в external image queue / image plan.
- Final verification усилен: теперь он проверяет реальные файлы результата, заполненность source ledgers, provenance, local image figures, external image placeholders, companion synchronization and forbidden drift modes.
- Добавлен раздел `S04 integrated guardrails`, фиксирующий встроенные ограничения для будущего package.

No article text was written. No article-writing package was built.
