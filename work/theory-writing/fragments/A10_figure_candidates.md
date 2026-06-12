# A10 figure candidates

Статус: companion-файл к `A10_mode_selection_map.md` после второго стилевого прохода S02. Реестр различает inline synthetic figure, отложенные editorial visual ideas и внешние реальные image candidates. В текущем рабочем листе не найдено разрешённых локальных image assets для A10; внешние изображения не открывались и не локализовывались.

## Inline figures used

| ID | Классификация | Где стоит | Usefulness / nontriviality gate | Asset / rights notes | Решение |
|---|---|---|---|---|---|
| `fig-a10-mode-selection-map` | `synthetic_figure` | В начале `A10_mode_selection_map.md`, после постановки проблемы выбора режима. | Проходит gate: таблица удерживает нетривиальную связь между десятью слоями внешней структуры, условиями добавления, условиями неусложнения и ожидаемым остаточным артефактом. В прозе такую карту трудно использовать как рабочую памятку. | Авторская текстовая схема, не основана на реальном изображении или screenshot. Права: original draft content. | Вставлена inline рядом с основным аргументом. |

## Deferred / rejected candidates

| Candidate | Классификация | Asset-pass / rights notes | Причина отказа или переноса |
|---|---|---|---|
| “Risk radar” по осям `радиус / обратимость / свидетельства / владелец / параллельность / ремонт`. | `editorial_visual_idea` | Нет внешнего asset. | Отложено: может быть полезно в Handbook или Fieldbook как диагностический инструмент, но в A10 создало бы ложную точность баллов и дублировало бы таблицу. |
| “Review package checklist” для PR-передачи. | `editorial_visual_idea` или будущая `synthetic_figure` | Нет внешнего asset. | Перенести в Handbook / Fieldbook. Для A10 это слишком процедурная деталь; основной текст уже фиксирует completion/evidence criterion. |
| “PWG object schema” с полями `status`, `owner`, `gates`, `evidence`, `handoff`, `history`. | `editorial_visual_idea` | Нет внешнего asset. | Перенести в A4/B2 или concept-first technical atlas. В A10 нужна карта выбора режима, а не техническая структура PWG. |
| “Lifecycle repair feedback loop” после merge. | `editorial_visual_idea` | Нет внешнего asset. | Отложено в A9 / technical atlas: в A10 достаточно критерия, когда repair нужен; подробный цикл ремонта будет дублировать A9. |
| “A/B/C support matrix” с колонками `A1–A9 / B1–B3 / C1–C5 → строка карты`. | `editorial_visual_idea` | Нет внешнего asset; могла быть авторской схемой. | Отклонено для основного текста: такая схема быстро превращает A10 в таблицу оглавления и нарушает задачу “карта выбора режима, а не повтор плана”. Матрица перенесена в `A10_source_usage.md`, где она нужна как provenance-аудит, а не читательская figure. |
| “Refusal branch overlay” поверх карты выбора режима. | `editorial_visual_idea` | Нет внешнего asset. | Не вставлено inline: отказ описан отдельным абзацем как допустимый выход из любой строки карты. Визуальная развилка может пригодиться в Handbook / Fieldbook, но в A10 усложнила бы единственную synthetic figure. |
| “Edge-case mini-matrix” для small reversible task / migration / architecture decision / platform agent / policy-bound contribution. | `editorial_visual_idea` | Нет внешнего asset; могла быть авторской схемой. | Не вставлено inline: пять случаев добавлены коротким абзацем в основной текст. Отдельная таблица была бы полезна для Fieldbook worksheet, но в A10 дублировала бы карту и раздувала визуальный слой. |
| Скриншоты продуктовых поверхностей агентских платформ, workflow engines, Kiro Specs, GitHub Copilot cloud agent, Codex, Jules или похожих инструментов. | `external_real_image_candidate` | Свободный asset-pass не нашёл локального image asset; внешние изображения не открывались, права и качество не проверялись, локальные пути отсутствуют. | Не вставлять в A10. Такие изображения относятся к concept-first technical atlas или к главам про execution environment / product surfaces. Замена их текстовой схемой была бы деградацией реального визуального материала. |
| Диаграммы или графики из внешних DORA/Bain/A-SDLC/SLR источников. | `external_real_image_candidate` | Эти внешние визуальные источники не открывались и не локализовывались; rights/download/localization/quality-pass не выполнены. | Не использовать в A10 без отдельного source/asset pass. Если поздний source-pass добавит внешнюю рамку для заключения, кандидаты должны идти через отдельный asset-pass и registry. |

## P06 visual decision

Адресный проход по критериям выбора режима не изменял визуальный слой. Новая диагностическая строка признаков добавлена прозой после уже существующей synthetic table; отдельная figure не нужна, потому что таблица `fig-a10-mode-selection-map` уже удерживает сравнительную структуру, а новая схема дублировала бы её.

## P07 visual decision

Адресный проход по переходам между режимами не создал новой схемы. Возможная `transition ladder` или `premature process noise` diagram отклонена как дублирование `fig-a10-mode-selection-map`: новая проза уточняет чтение существующей таблицы, а не требует второго визуального слоя.

## P08 visual decision

Адресный проход по практической применимости не добавил новой визуализации. Возможная `mode choice worksheet` оставлена как Handbook / Fieldbook material: в основном A10 новая проза достаточна, а ещё одна таблица превратила бы фрагмент в рабочий лист вместо теоретического заключения.

## P09 visual check

Общий редакторский проход P09 применил asset-classification gate и не выявил визуального дефекта. Единственная inline synthetic figure остаётся достаточной; разделение плотных абзацев не требует новой схемы, а `mode choice worksheet` остаётся Handbook / Fieldbook material.

## P10 visual check

Повторный общий редакторский проход P10 не выявил визуального дефекта. `fig-a10-mode-selection-map` остаётся единственной inline synthetic figure; новых local assets или external image candidates не появилось.

## P11 visual check

Третий общий редакторский проход не выявил визуальной проблемы. Новая figure не нужна: `fig-a10-mode-selection-map` остаётся единственной inline synthetic figure, а deferred candidates остаются в реестре/Handbook/Fieldbook/technical atlas queue.

## S02 visual classification check

Второй стилевой проход не добавил новых визуальных кандидатов и не изменил inline-решение. `fig-a10-mode-selection-map` остаётся `synthetic_figure`, потому что уже оформлена как публичная таблица и прошла usefulness/nontriviality gate. Все остальные элементы ниже остаются `editorial_visual_idea` или `external_real_image_candidate`; ни один внешний screenshot/source diagram не вставлялся без asset-pass.

## Asset-pass notes

- Локальный asset-check по архиву не нашёл файлов `png`, `jpg`, `jpeg`, `gif`, `webp` или `svg`, которые могли бы быть вставлены как разрешённый `local_image_asset` для A10.
- Внешние реальные изображения не открывались и не скачивались, потому что они не нужны для текущего критерия выбора режима; без rights/download/localization pass их нельзя превращать в текстовые схемы или inline figures.
- Единственная inline figure — авторская synthetic table. Она не заменяет готовый image asset и не маскирует отсутствие asset-pass.
- Во втором, третьем и edge/source-pass не добавлялись новые inline figures: A/B/C support matrix, refusal overlay и edge-case mini-matrix оставлены вне основного текста, потому что они полезнее как provenance/Handbook/Fieldbook material, а не как часть теоретического заключения.

## Readiness status

`ready_with_known_debts`: визуальный слой A10 пригоден для следующего прохода. После S02 inline figure считается устойчивой; новые схемы не требуются. Долги: при будущей сборке финальной главы нужно сверить, не появились ли разрешённые локальные assets из A1–A9/B/C, которые должны стоять рядом с соответствующими аргументами или уйти в technical atlas; также можно решить, нужна ли отдельная Handbook-версия диагностической карты и refusal-branch visualization или edge-case worksheet.

## Post-import visual repair decision

Во время post-import repair не добавлялись новые inline-figures. Недостающие target outputs `A10_mode_selection_matrix.md` и `A10_decision_stress_tests.md` созданы как supporting/diagnostic files, а не как дополнительные публичные схемы в основном фрагменте. Основной A10 сохраняет одну synthetic figure `fig-a10-mode-selection-map`; этого достаточно для публичного visual layer.
