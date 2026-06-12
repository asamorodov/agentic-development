# B3: кандидаты фигур

## Inline-решение

| ID | Type | Статус | Решение | Причина |
|---|---|---|---|---|
| `fig-b3-gas-town-organizational-loop` | `synthetic_figure` | вставлена inline в `B3_gas_town_beyond_pwg.md` | Сохранить в draft. | Фигура проходит usefulness/nontriviality gate: она не украшает текст и не заменяет внешний screenshot, а сжимает главный boundary-аргумент B3 — PWG как долговечная единица работы, Gas Town как организационно-операционный lifecycle. После repair-pass таблица русифицирована и очищена от лишнего английского клея. |

## Локальные image assets

| ID | Type | Локальный путь | Статус | Решение |
|---|---|---|---|---|
| `fig-gastown-architecture` | `local_image_asset` | `content/assets/theory-images/gastown-architecture.svg` | файл найден | Не вставлять в B3 сейчас. Asset уже используется в A5 как якорь организационного слоя; повтор в B3 возможен только при финальном composition-pass, если B3 будет читаться отдельно от A5. |
| `fig-gastown-basic-workflow` | `local_image_asset` | `content/assets/theory-images/gastown-basic-workflow.svg` | файл найден | Отложить в technical atlas / walkthrough. Для B3 он слишком процедурный: показывает базовую петлю Gas Town, но слабее поддерживает границу Gas Town/PWG, чем текущая таблица. |
| `fig-gastown-mayor-hub` | `local_image_asset` | `content/assets/theory-images/gastown-mayor-hub.webp` | файл найден | Не вставлять в B3. Иллюстрация скорее декоративная/брендовая; для теоретического аргумента о жизненном цикле она слабее архитектурной схемы и таблицы. |
| `fig-beads-task-graph-memory` | `local_image_asset` | `content/assets/theory-images/beads-task-graph-memory.svg` | файл найден | Не повторять в B3, чтобы не сворачивать Gas Town обратно к Beads/PWG. Подходит для A4/B2 или технического атласа. |

## Кандидаты внешних реальных изображений

| ID | Type | Внешний источник | Статус | Решение |
|---|---|---|---|---|
| `fig-gastown-two-tier-beads-flow` | `external_real_image_candidate` | `Welcome to Gas Town`, Figure 6, two-tier Beads flow. | Реальное внешнее изображение. Нужны asset-pass, проверка прав/статуса и политика локального захвата перед inline-вставкой. | Отложить. Сильный кандидат для будущего visual pass, потому что прямо поддерживает различие town-level и rig-level. |
| `fig-gastown-worker-roles` | `external_real_image_candidate` | `Welcome to Gas Town`, Figure 5, worker roles. | Реальное внешнее изображение. Нужны asset-pass и проверка прав/статуса. | Отложить. Может поддержать раздел о ролях, но не вставлять без локального файла и разрешённого статуса. |
| `fig-gastown-readme-architecture-mermaid` | `external_real_image_candidate` | Gas Town README Mermaid architecture / system diagrams. | Source diagrams из внешнего repo, а не повод рисовать похожую текстовую схему. Нужны проверка лицензии репозитория и решение о rendering. | Отложить. B3 уже имеет boundary table; README-diagram лучше подходит technical atlas или implementation appendix. |
| `fig-gastown-readme-basic-workflow-mermaid` | `external_real_image_candidate` | Gas Town README basic workflow diagram: You → Mayor → Convoy → Agent → Hook → completion summary. | Реальный external/source diagram; нужна проверка лицензии/прав и решение, можно ли render-ить Mermaid from source в publication pipeline. | Отложить. Не пересоздавать как synthetic chart в этом pass. |

## Отложенные редакторские визуальные идеи

| ID | Type | Идея | Решение |
|---|---|---|---|
| `fig-gastown-service-agents-loop` | `editorial_visual_idea` | Показать Refinery/Witness/Deacon/Dogs как maintenance loops вокруг параллельных агентов. | Отложить. Может стать synthetic figure, если будущей главе нужно подробно объяснить сервисных агентов и если реального asset не хватает. |
| `fig-gastown-handoff-mail-flow` | `editorial_visual_idea` | Показать передачу работы через bead, hook, mail и сервисных агентов: Polecat → Witness/Refinery → Mayor. | Отложить. B3 уже объясняет это прозой; будущая фигура должна использовать имена из текущего `polecat-lifecycle-patrol` source. |
| `fig-gastown-escalation-path` | `editorial_visual_idea` | Показать Agent → Deacon → Mayor → Overseer как управляемый путь blocker-а. | Отложить. В основном тексте достаточно одной фразы; отдельная figure рискует сделать B3 слишком process-heavy. |
| `fig-gastown-orchestration-cost-curve` | `editorial_visual_idea` | Показать throughput vs review/merge/attention/coordination cost. | Отложить. Есть риск overclaiming без измерений; лучше оставить как концептуальную заметку, пока не появятся данные. |
| `fig-gastown-harness-pwg-org-stack` | `editorial_visual_idea` | Stack: harness → PWG → Gas Town organizational lifecycle. | Отложить. B3 уже формулирует relation прозой; такая фигура может быть полезнее в overview синтеза. |

## Примечание по visual decision

Ни одно внешнее реальное изображение не было превращено в текстовую замену. Единственная inline-фигура в B3 — оригинальная синтетическая boundary table; она сохранена, потому что удерживает центральное сравнение, а не дублирует соседний абзац. Локальные Gas Town assets теперь корректно признаны существующими, но не вставлены автоматически: часть уже используется в A5, часть лучше подходит technical atlas, а часть слишком декоративна для B3.

Readiness по визуальному слою: основной B3 usable; дополнительные image decisions отложены до отдельного composition/asset-pass.
