# C2 figure candidates

## Inline figures

| ID | Тип | Статус | Где стоит | Почему прошёл gate | Asset / rights notes |
| --- | --- | --- | --- | --- | --- |
| `fig-c2-process-output-pwg-state` | `synthetic_figure` | Вставлен inline в `C2_pwg_to_process_profiles.md` | После объяснения GSD как лёгкого профиля состояния и перед переходом к BMAD | Схема показывает нетривиальную границу: профиль производит ритм, роли, контрольные точки, сжатый контекст и recovery-сигналы, а PWG удерживает последствия для работы — готовность, владение, контрольный барьер, свидетельства, история и восстановление. Таблица связывает два слоя по типам рабочих последствий, была расширена после второго прохода строкой «Восстановление» и после третьего прохода стала поддерживать мост process-as-artifact → PWG. | Собственная схема, не заменяет внешний image asset. Правовые ограничения не требуются сверх обычной авторской схемы. |

## Deferred / rejected candidates

| ID | Тип | Источник / asset | Решение | Причина |
| --- | --- | --- | --- | --- |
| `fig-c2-gsd-phase-loop` | `synthetic_figure` | GSD phase loop sources | Отложено | Для C2 достаточно текстового фактического якоря. Отдельная фазовая схема увела бы фрагмент в обзор GSD и повторила бы A5. |
| `fig-c2-gsd-recovery-checkpoint` | `synthetic_figure` | `gsd-executor` + Auto Mode | Отложено | После второго прохода recovery-фактура добавлена в текст и inline-таблицу. Отдельная схема checkpoint/SQLite/recovery подходит скорее для GSD profile или technical atlas. |
| `fig-c2-bmad-workflow-map-real` | `external_real_image_candidate` | Official BMAD Workflow Map Diagram: `https://docs.bmad-method.org/workflow-map-diagram.html` | Отложено, не вставлено | В source/visual pass URL открыт и классифицирован как внешняя workflow-диаграмма/страница с artifact flow. Нужны rights-check, localization/asset-pass и решение, где она нужна. Подменять её текстовой схемой нельзя; C2 не требует полного визуального BMAD workflow. |
| `fig-c2-bmad-role-output-chain` | `synthetic_figure` | BMAD workflow map + agents + core tools | Отклонено для текущего фрагмента | Риск декоративного повторения: PRD → architecture → story уже объяснены в прозе, а полная схема лучше подходит для BMAD profile / technical atlas. |
| `fig-c2-bmad-recovery-correct-course-investigate` | `synthetic_figure` | BMAD correct-course + investigate | Отложено | Фактура добавлена в текст как пример role-output/recovery. Схема корректировки курса и расследования была бы полезна в BMAD article, но в C2 она отвела бы фокус от мостовой функции. |
| `fig-c2-gastown-architecture` | `local_image_asset` candidate | В A5 использован путь `../../../content/assets/theory-images/gastown-architecture.svg`; текущий C2-пакет не содержит локальный `content/` asset для проверки | Отложено, не вставлено | C2 упоминает Gas Town только как верхнюю границу. Повтор архитектурной схемы из A5 перегрузил бы bridge и потребовал бы asset verification в пакете, где самого asset-файла нет. |
| `fig-c2-gastown-role-lifecycle-boundary` | `synthetic_figure` | Welcome to Gas Town + Gas Town Docs + Gas Town GitHub | Отложено | Source/depth pass подтвердил полезность roles/lifecycle фактуры в прозе, но схема `Mayor/Crew/Polecats/Convoys/Refinery/Witness/Deacon/Dogs` отвела бы C2 от process-profile/PWG границы. Такой visual лучше подходит Gas Town/B3/atlas. |
| `fig-c2-process-theater-boundary` | `editorial_visual_idea` | Собственная идея | Отклонено | После process-theater pass различение усилено прозой. Вторая схема про role/phase/approval/ceremony как декор без state effect снизила бы плотность и стала бы антипримерным списком, а не самостоятельной фигурой. |
| `fig-c2-gsd-bmad-pwg-light-state` | `synthetic_figure` | Соседний A5-смысл о лёгких формах внешнего состояния | Отклонено | Дублирует A5 и ухудшает границу C2. Текущий inline-figure уже покрывает нужный bridge без повторения сравнительной таблицы GSD/BMAD. |

## Asset-pass notes

- В основной C2 вставлена только одна `synthetic_figure`, прошедшая usefulness/nontriviality gate; она покрывает также process-as-artifact bridge и consequence-pass без отдельной Gas Town-схемы.
- Настоящие внешние изображения не заменялись текстовыми схемами. BMAD workflow map открыта в source/visual pass и оставлена как `external_real_image_candidate` до проверки прав и локализации.
- Локальные image assets из соседних фрагментов не вставлялись: в текущем пакете не найден проверяемый `content/assets/...` путь, и C2 не требует повторного Gas Town visual anchor.
- Служебные asset-pass notes оставлены только в этом companion-файле; в основной фрагмент не попали статусы, причины отказа или редакторские комментарии.
- General editorial pass 1 визуальный слой не менял: единственная synthetic figure по-прежнему нужна для границы process output → PWG state consequence.

- General editorial pass 2 визуальный слой не менял: правка вступления, process-as-artifact формулы и Gas Town-абзаца не создала новых figure-кандидатов и не изменила asset-классификацию.
- General editorial pass 3 визуальный слой не менял: существенных visual/source/structure дефектов не найдено, новые кандидаты не добавлялись.
- Стилевой проход 2 визуальный слой не менял: inline остаётся только `fig-c2-process-output-pwg-state`, BMAD workflow map остаётся `external_real_image_candidate`, Gas Town-role lifecycle остаётся отложенной synthetic idea для profile/atlas.
