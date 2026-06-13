# GSD / Open GSD — external image queue

Статус: Final verification / queue open but non-blocking for current package.

В P01 внешние реальные изображения не добавлялись. Причина: рабочий лист не требовал и не разрешал отдельный внешний visual-search/download pass, а досье содержит главным образом кандидаты на авторские схемы.

## Очередь для P12 visual asset pass

| Candidate id | Источник для проверки | Что искать | Зачем статье | Статус |
|---|---|---|---|---|
| `ext-gsd-core-product-ui-or-diagram` | https://opengsd.net/products/gsd-core; https://www.opengsd.net/docs/v1/user-guide | Product diagram, workflow screenshot, command surface visual | Помочь читателю увидеть `gsd-core` как поверхность процесса | pending_search |
| `ext-gsd-pi-status-or-report` | https://www.opengsd.net/docs/v2/commands; https://www.opengsd.net/docs/v2/auto-mode | TUI/status/report/headless query screenshot or example visual | Показать `gsd-pi` как runtime, а не только текстовый цикл | pending_search |
| `ext-gsd-browser-proof` | https://opengsd.net/products/gsd-browser; https://opengsd.net/docs/v5/commands | Screenshot/assertion/trace/HAR/live viewer visual | Поддержать раздел про свидетельства UI/UAT | pending_search |
| `ext-open-gsd-roadmap-surfaces` | https://opengsd.net/roadmap | Roadmap visual or ecosystem diagram, if rights permit | Показать границы `gsd-core` / `gsd-pi` / `gsd-browser` / future surfaces | pending_search |

Пока ни один candidate не вставлен в основной текст как `<figure data-asset-status="external-real-candidate">`.


## P04 queue status

Новых external-real candidates нет. P04 добавил только текстовую lifecycle-control matrix; visual asset pass по реальным screenshots/diagrams остаётся отложенным.


## P05 queue status

Новых external-real candidates нет. Browser evidence упомянут как класс runtime artifacts, но реальные screenshots/trace visuals остаются задачей P12 visual asset pass.


## P06 external image queue

P06 не добавляет внешних реальных изображений. Если позже понадобится visual asset, он должен быть synthetic diagram, not a downloaded screenshot, because the pass explains process semantics rather than a public UI artifact.


## P07 external image queue

No external real image added. The new material is a process contour and should remain synthetic if visualized.


## P08 external image queue

No external image candidate added. Failure limits should not be represented with real screenshots unless a later visual pass finds an official, rights-safe diagnostic UI image.


## P09 external image queue

No external image added. GitHub issue screenshots would be generic and rights/PII-sensitive; use a synthetic diagram if needed.


## P10 external image queue

No external image added. The issue-to-ship path is synthetic and should not use real tracker screenshots without rights/PII review.


## P11 local asset pass queue status

P11 inserted one local image asset and did not add external-real placeholders. Existing P12 queue remains: find real Open GSD / `gsd-browser` / `gsd-pi` visuals if available and rights-safe.

## P12 external-real search result

P12 checked the existing queue against public Open GSD product/docs/roadmap surfaces. No inline external-real placeholder was added to the article.

| Candidate id | P12 status | Disposition |
|---|---|---|
| `ext-gsd-core-product-ui-or-diagram` | checked_no_external_real_image_inserted | Product/docs surfaces remained useful as text sources; no standalone diagram/screenshot selected. |
| `ext-gsd-pi-status-or-report` | checked_no_external_real_image_inserted | No TUI/status/report/headless image was inserted; keep deferred. |
| `ext-gsd-browser-proof` | checked_no_external_real_image_inserted | Evidence surface remains text-described; P11 local Codex analogy is the current inline visual substitute, explicitly not a GSD screenshot. |
| `ext-open-gsd-roadmap-surfaces` | checked_no_external_real_image_inserted | Roadmap stayed a source link, not an image asset. |

Queue remains open for a future asset localization pass if official screenshots, diagrams or downloadable media appear.

## P13 external queue status

P13 added no synthetic replacement for these external candidates and no new external-real candidate.

## P14 external image queue status

P14 added no image candidate. The standalone-reading subsection is conceptual framing and should not be represented by a generic illustration.

## P15 external image queue status

No new external image candidate. Failure-mode reinforcement is conceptual and source-text based.

## P16 external image queue status

No change. Theory backlinking does not create external image candidates.


## P17 external image queue note

P17 не добавлял внешние изображения и не менял статусы кандидатов. Нижний раздел основного текста только языково выровнен: внешние реальные изображения Open GSD остаются не вставленными, а будущий asset-pass всё ещё должен проверять права, качество, актуальность и пригодность standalone screenshot/diagram перед вставкой.

## P18 external image queue note

Очередь внешних изображений не изменилась. P18 только очистил пользовательский текст: отсутствие внешнего реального ассета объясняется через проверку официальных страниц и документов, а не через внутренний номер прохода. Все кандидаты остаются в статусе deferred/needs rights and quality check.

## P19 external image queue note

Пользовательская статья больше не содержит нижний asset-backlog section. Очередь внешних изображений остаётся здесь: официальные Open GSD страницы и документы уже проверялись, standalone rights-safe screenshot/diagram не выбран, будущий проход должен продолжать отсюда.

## P20 external image queue note

Очередь внешних изображений не изменилась. P20 был редакторским проходом по вступительной рамке статьи.

## P21 external image queue note

Очередь внешних изображений не изменилась. P21 не был visual pass.

## P22 external image queue note

Очередь внешних изображений не изменилась. P22 проверял публичную структуру статьи и оставил asset backlog в companion-слое: в основной статье нет нижнего раздела `Внешние изображения для asset-pass`, потому что внешний реальный ассет Open GSD не был выбран и локализован.

## P23 external image queue sync

Queue status after companion sync: open but non-blocking for the current article. No external-real candidate is inserted inline, and no bottom backlog section exists in `gsd_open_gsd.md`. Future work should resume here only if official Open GSD screenshots/diagrams become available and rights-safe.

## P24 external image queue note

Очередь внешних изображений не изменилась. Стилевой проход не добавлял real-image candidates и не возвращал bottom asset backlog в основной текст.

## P25 external image queue note

Очередь внешних изображений не изменилась. P25 не был asset-pass.

## P26 external image queue note

Очередь внешних изображений не изменилась. Финальный стилевой проход не добавлял external-real placeholders and did not alter asset status.

## Final verification queue note

Очередь остаётся открытой только для будущего asset-pass. В текущем пакете нет inline `<figure data-asset-status="external-real-candidate">` и нет нижнего раздела `Внешние изображения для asset-pass`, потому что проверенный внешний реальный asset не был выбран. Это не blocker текущей статьи, но остаётся публикационным условием, если финальная площадка требует реальные Open GSD screenshots/diagrams.
