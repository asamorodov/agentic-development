# A4. Кандидаты фигур и решения после repair

Этот файл теперь является не списком того, что нужно вставить в основной текст, а реестром визуальных решений. В A4 после repair оставлены только фигуры, которые действительно помогают удержать границу Persistent Work Graph: один локальный asset и три нетривиальные синтетические схемы/таблицы. Остальные кандидаты сняты с inline, чтобы фрагмент не превращался в набор служебных схем.

## Inline-фигуры в основном тексте

| ID | Статус | Тип | Решение | Обоснование |
|---|---|---|---|---|
| `fig-a4-pwg-minimal-node` | `inline` | `local_image_asset` | Использовать локальный asset `content/assets/theory-images/beads-task-graph-memory.svg`. | Beads остаётся ближайшим практическим якорем для PWG: работа живёт в графе задач, зависимостей, закреплений и памяти, а не только в отчёте агента. Подпись в основном тексте переписана как публичная, без рассказа о восстановлении asset. |
| `fig-a4-readiness-gate-owner` | `inline` | `synthetic_figure` | Оставить как таблицу готовности, ожиданий, владения и свидетельств. | Фигура проходит usefulness/nontriviality gate: она не повторяет соседний абзац, а показывает, почему готовность узла нельзя выводить из самоотчёта агента. |
| `fig-a4-source-state-machine` | `inline` | `synthetic_figure` | Оставить как таблицу состояния источника. | Для документной работы это отдельная специфика PWG: URL, прочитанный источник и источник, перенесённый в основной текст, имеют разные статусы. |
| `fig-a4-boundary-map` | `inline` | `synthetic_figure` | Оставить как boundary map в виде таблицы соседних слоёв. | Это центральная композиционная фигура A4: она удерживает границу PWG с issue tracker, Task Master, durable execution, CRDT/STORM и Gas Town. |

## Снятые с inline кандидаты

| ID | Новый статус | Причина |
|---|---|---|
| `fig-a4-session-break-failure` | `deferred_or_rejected` | Открывающий failure mode достаточно ясно работает в прозе. Отдельная схема была бы декоративным повтором. |
| `fig-a4-ready-blocked-queue` | `merged_into_fig-a4-readiness-gate-owner` | Идея готовности из графа сохранена, но объединена с владением и свидетельствами в более полезную таблицу. |
| `fig-a4-gates-durable-waits` | `deferred` | Gate-паттерн важен, но отдельная фигура в A4 перегружала текст. Можно вернуть в technical atlas или в будущую практическую схему PWG. |
| `fig-a4-prime-handoff-recovery` | `deferred` | Различение prime / передача работы / восстановление раскрыто в прозе. Отдельная схема может понадобиться позже, если появится technical atlas. |
| `fig-a4-parallel-source-work` | `deferred` | Anthropic-параграф оставлен как источник давления на проверяемые source packages; отдельная схема пока слишком быстро уводит фрагмент в multi-agent research workflow. |
| `fig-a4-runtime-vs-work-state` | `merged_into_fig-a4-boundary-map` | Различие между долговечным исполнением и состоянием работы включено в общую boundary map. |
| `fig-a4-crdt-storm-limit` | `merged_into_fig-a4-boundary-map` | Граница CodeCRDT/STORM с PWG включена в общую boundary map. |
| `fig-a4-tail-cleanup` | `rejected_for_main_text` | Сама формула про «хвост жизненного цикла» признана стилистически неудачной. Смысл сохранён в прозе как очистка/архивирование после выполнения. |
| `fig-a4-object-lifecycle` | `deferred` | Полная lifecycle-схема лучше подходит для technical atlas; в A4 достаточно короткой строки статусов. |
| `fig-a4-evidence-before-done` | `merged_into_fig-a4-readiness-gate-owner` | Проверяемое свидетельство включено в таблицу готовности/закрытия узла. |
| `fig-a4-authority-boundaries` | `merged_into_fig-a4-boundary-map` | Authority map объединена с boundary map, чтобы не плодить две похожие фигуры. |
| `fig-a4-pwg-layer-position` | `deferred` | Может пригодиться в общей карте слоёв, но в A4 дублирует boundary map. |
| `fig-a4-failure-pressure-chain` | `deferred_or_rejected` | Риск виден в открывающем и финальном абзацах; отдельная цепочка сейчас была бы слишком объяснительной. |
| `fig-a4-degradation-matrix` | `deferred` | Полезна для audit/technical atlas, но в основном A4 достаточно финального раздела о деградациях. |
| `fig-a4-prime-compact-refresh` | `deferred` | Источник Beads Claude Code integration сохранён в тексте, но отдельная схема prime-refresh пока перегружает фрагмент. |

## Asset note

В A4 не было восстановленных внешних real-image candidates помимо уже локального `beads-task-graph-memory.svg`. Остальные inline-фигуры являются авторскими синтетическими таблицами/схемами и не маскируют отсутствующие source screenshots. Если в будущем появится настоящий screenshot или source diagram по Beads/Gas Town/Task Master, его нужно занести в asset catalog и не подменять текстовой схемой.
