# GSD / Open GSD — image plan

Статус: Final verification / visual layer complete for current package. В статье остались четыре синтетические фигуры и один локальный image asset; внешние реальные изображения не вставлены, потому что официальный rights-safe standalone asset не был выбран.

## Фигуры, вставленные в статью

| Figure id | Тип | Основание | Статус |
|---|---|---|---|
| `fig-gsd-process-runtime-profile` | synthetic_figure | Сводит центральную ось статьи: фазы + `.planning/.gsd` + policy/git/evidence | inserted_inline_synthetic_figure |
| `fig-gsd-artifact-consumption` | synthetic_figure | Показывает потребление артефактов, без которого `.planning/` становится инертным | inserted_inline_synthetic_figure |
| `fig-gsd-core-vs-pi-state` | synthetic_figure | Различает `.planning/STATE.md` как навигацию и SQLite как authority в `gsd-pi` | inserted_inline_synthetic_figure |
| `fig-gsd-not-pwg-boundary` | synthetic_figure | Фиксирует главную boundary: process-runtime profile vs Persistent Work Graph | inserted_inline_synthetic_figure |
| `fig-gsd-browser-evidence-analogy` | local_image_asset | Показывает browser evidence contour через локальную аналогию OpenAI Codex: UI action, snapshots, runtime events, повторная проверка | inserted_inline_local_image_asset (P11) |

## Disposition кандидатов из досье

| Кандидат из досье | Disposition P01 | Причина |
|---|---|---|
| Фазовый цикл `gsd-core`: `Discuss -> (UI design) -> Plan -> Execute -> Verify -> Ship` | inserted_as_synthetic_component | Вошёл в `fig-gsd-process-runtime-profile`; отдельная чистая схема может понадобиться после structure pass |
| Поток артефактов `.planning/` | inserted_as_synthetic_component | Вошёл в `fig-gsd-artifact-consumption` |
| Машина состояний автоматического режима `gsd-pi` | deferred | Текст раскрывает цикл; отдельная схема может быть нужна после source-depth pass по `gsd-pi` |
| Авторитетность состояния `gsd-pi`: SQLite -> `.gsd/` projections -> dispatch -> DB | inserted_as_synthetic_component | Вошла в `fig-gsd-core-vs-pi-state` |
| Миграция/восстановление legacy `.planning/` -> `.gsd` | deferred | В P01 раскрыто в failure mode; отдельная схема скорее Handbook |
| Слои архитектуры `gsd-core`: command -> workflows -> agents -> tools -> `.planning/` | deferred | Механизм раскрыт прозой; может стать visual в P11/P13 |
| Multi-repo workspace for `gsd-pi` | deferred | Упомянуто косвенно через configuration; не центральная ось P01 |
| Git isolation `none/worktree/branch` | deferred | Сильный кандидат для Fieldbook-схемы; в P01 раскрыто в тексте |
| Карта поверхностей Open GSD | deferred | Нужна проверка актуальности roadmap и, возможно, реальный screenshot/карта |
| Полномочия агентов `planner/checker/executor` | deferred | Сильно полезный кандидат для P13; в P01 раскрыт в тексте |
| Матрица аудита покрытия | deferred | Скорее Handbook visual; не вставлено в primary article |
| Схема безопасности волн | deferred | Может усилить Plan/Execute после source-depth pass |
| Карточка продолжения после checkpoint | deferred | Скорее Fieldbook companion |
| Стек наблюдаемости | deferred | Нужен после source-depth pass по diagnostics/audit |
| Граница безопасности config/audit/secrets | deferred | Сильный кандидат для визуального pass, но нужен careful privacy framing |
| Surface routing namespace | deferred | Может заменить часть prose после structure pass |
| Предварительная проверка пригодности: plan-status -> Nyquist -> artifacts | deferred | Сильный Handbook/atlas candidate после P04–P08 |
| Карта зрелости контекста: backlog -> seed -> thread -> roadmap/requirement/decision -> phase | deferred | Может усилить theory link; P01 упомянул side channels |
| Workstream vs wave | deferred | Важный boundary; P01 оставил в prose |
| Таксономия контрольных остановок | deferred | Требует чтения/проверки gates/checkpoints как source-depth |
| Экономика checkpoint | deferred | Требует отдельного source-depth/fieldbook framing |
| Цикл браузерных свидетельств | deferred | Требуется visual asset pass по `gsd-browser`; внешний candidate possible |
| Карта бюджета контекста | deferred | В P01 раскрыто текстом; возможно synthetic visual later |
| Лестница проверки existence/substance/wiring/behavior | deferred | Требует source-depth pass по `verification-patterns.md` before inline |
| Граф потребления артефактов | inserted_as_synthetic_component | Вошёл в `fig-gsd-artifact-consumption` |
| Матрица маршрутизации моделей | deferred | Скорее Fieldbook; требует аккуратной актуализации моделей |
| Стек политики конфигурации | deferred | Сильный candidate after source-depth pass |
| Слой ingest/graphify/surface | deferred | Скорее Handbook; P01 раскрыл prose |
| Схема безопасности worktree | deferred | Скорее Fieldbook; может быть merged with Git isolation visual |

## Статус внешних реальных изображений

- В P01 не найдено и не вставлено внешних реальных изображений.
- Необходим P12: проверить product pages / docs на screenshots, diagrams, UI images, command screenshots, browser proof examples и roadmap graphics.
- Любой внешний реальный asset должен получить `external-real-candidate` placeholder в статье, запись в `gsd_open_gsd_external_image_queue.md` и проверку download/rights/quality.


## P04 visual note

P04 добавил текстовую lifecycle-control matrix, но не вставлял новую figure и не добавлял внешние изображения. Возможный будущий synthetic candidate: `fig-gsd-lifecycle-control-gates`, если structure/visual pass решит превратить таблицу “двигает / останавливает / надзор” в схему. Сейчас таблица оставлена в тексте, чтобы не плодить визуальный слой до source-depth по gates/checkpoints.


## P05 visual note

P05 добавил таблицу runtime discipline, но не вставил новую figure. Возможный synthetic candidate для P13: `fig-gsd-runtime-discipline-stack` — слои commands/config/tool policy/git/evidence/diagnostics. Пока кандидат отложен, потому что `fig-gsd-process-runtime-profile` уже частично покрывает эту ось, а новая схема может продублировать текст.


## P06 visual note: continuation/recovery boundary

P06 добавил табличный слой про `STATE.md`, фазовые документы, handoff, side context, SQLite projections and recovery commands. Новая external image не требуется.

Potential synthetic figure candidate for later visual pass:

- `fig-gsd-continuation-recovery-boundary`: left side `.planning/STATE.md`, phase docs and handoff; middle side SQLite/`.gsd` projections and recovery commands; right side PWG boundary with nodes/deps/owners/readiness/evidence. Candidate only; не вставлен в P06, чтобы не перегружать уже существующую artifact-consumption figure.


## P07 visual note: unit lifecycle contour

P07 added a lifecycle table for one `gsd-pi` unit. A synthetic figure could be useful later but was not inserted now.

Candidate:

- `fig-gsd-pi-unit-runtime-contour`: SQLite state -> focused session -> UnitContextManifest/ToolsPolicy -> `gsd_exec` evidence -> verification verdict -> DB/projection update -> pause/recovery. This may overlap with `fig-gsd-core-vs-pi-state`, so final visual pass should decide whether to merge or omit.


## P08 visual note: failure limits

P08 does not require a new figure. The failure-mode section is prose/table-like enough, and adding a risk matrix now could duplicate the article's existing synthetic figures.

Potential later option:

- `fig-gsd-failure-modes`: ceremony too heavy, stale state, no graph state, autonomy illusion, DB/projection confusion. Defer to final visual pass.


## P09 visual note: issue ingress

P09 does not add a figure. Possible later synthetic option: `fig-gsd-issue-ingress-boundary` showing GitHub issue -> `.planning/issues/` -> classification -> human review -> phase/roadmap -> ship/close. This is a candidate only; current article can carry it in prose.


## P10 visual note: issue-to-ship path

P10 added an end-to-end prose example. A synthetic diagram may be useful later:

- `fig-gsd-issue-to-ship-reader-path`: issue candidate -> review -> Discuss -> Plan -> Execute -> Verify -> Ship -> repair/update state. This overlaps with artifact-consumption figure, so visual pass should decide whether to merge them.


## P11 local asset pass

| Local asset | Status | Placement / reason |
|---|---|---|
| `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | inserted_inline_local_image_asset | Inserted as `fig-gsd-browser-evidence-analogy` after the Verify/`gsd-browser` paragraph. Caption says it is an OpenAI Codex analogy, not a GSD screenshot. |
| `content/assets/theory-images/openai-codex-dashboard-workflow.webp` | not_inserted_explained | Relevant only at the broad “agent task dashboard” level. It does not show GSD phases, `.planning/`, `STATE.md`, config surface, SQLite or browser evidence, so inline use would be decorative and could confuse source boundaries. |
| `content/assets/theory-images/fowler-harness-continuous-feedback.png` | not_inserted_explained | Relevant to the broader harness/continuous feedback theme, but not source-specific to GSD. The article already explains verification and diagnostics with GSD-specific sources; this image is better reserved for harness-engineering material. |

Updated inserted figure list: add `fig-gsd-browser-evidence-analogy` as `local_image_asset`.

## P12 external-real visual pass and dossier dispositions

P12 treated the dossier's image-candidate section as the required starting point. The candidates are editorial/synthetic visualization ideas rather than already identified external screenshots or diagrams. Official Open GSD product/docs/roadmap pages were checked for real visual candidates, but no standalone external image was inserted.

| Dossier candidate | P12 disposition | Reason |
|---|---|---|
| Фазовый цикл Discuss -> Plan -> Execute -> Verify -> Ship | covered_by_existing_synthetic | `fig-gsd-process-runtime-profile` already captures the phase cycle and control surfaces. |
| Поток артефактов `.planning/` | covered_by_existing_synthetic | `fig-gsd-artifact-consumption` covers producer/consumer movement. |
| State machine `gsd-pi` | deferred_synthetic_candidate | Could be useful later, but current `gsd-pi` section and state-authority figure are sufficient. |
| SQLite authority vs markdown projections | covered_by_existing_synthetic | `fig-gsd-core-vs-pi-state` covers DB/projection boundary. |
| Migration/recovery path | deferred_fieldbook_candidate | Better for operational fieldbook; not inserted in concept article. |
| GSD Core architecture layers | deferred_synthetic_candidate | Could become a layer diagram, but would duplicate runtime-discipline table. |
| Multi-repo workspace for `gsd-pi` | deferred_fieldbook_candidate | Not central to primary concept axis. |
| Git isolation `none/worktree/branch` | deferred_fieldbook_candidate | Important operational visual; left in prose to avoid process overload. |
| Карта поверхностей Open GSD | external_checked_deferred | Roadmap/product pages checked; no standalone official visual selected. |
| Полномочия агентов `planner/checker/executor` | deferred_synthetic_candidate | Useful but not rare enough after lifecycle-control text. |
| Матрица аудита покрытия | deferred_handbook_candidate | Better suited to verification handbook. |
| Схема безопасности волн | deferred_handbook_candidate | Could support planning, but not required for article argument. |
| Карточка продолжения после checkpoint | deferred_fieldbook_candidate | Operational artifact; current continuation section covers the boundary. |
| Стек наблюдаемости | deferred_handbook_candidate | Needs separate diagnostics framing. |
| Граница безопасности config/audit/secrets | deferred_safety_candidate | Privacy/security-sensitive; not inserted without deeper safety pass. |
| Surface routing namespace | deferred_synthetic_candidate | Could explain command routing but prose/table suffice. |
| Plan-status -> Nyquist -> artifacts | deferred_handbook_candidate | Useful gate taxonomy, but outside P13 rarity threshold. |
| Context maturity map: backlog -> seed -> thread -> roadmap/requirement/decision -> phase | deferred_theory_candidate | Potentially useful in broader context-state article. |
| Workstream vs wave | deferred_boundary_candidate | Important boundary; kept in prose. |
| Таксономия контрольных остановок | deferred_handbook_candidate | Requires deeper gate/checkpoint treatment. |
| Экономика checkpoint | deferred_handbook_candidate | Better for operations/economics note. |
| Цикл браузерных свидетельств | partly_covered_by_local_asset | P11 inserted Codex browser-evidence analogy; official GSD external visual not found in P12. |
| Карта бюджета контекста | deferred_theory_candidate | Text already explains budget heuristics. |
| Лестница проверки existence/substance/wiring/behavior | deferred_handbook_candidate | Useful for verification guide, not inserted here. |
| Граф потребления артефактов | covered_by_existing_synthetic | `fig-gsd-artifact-consumption` inserted earlier. |
| Матрица маршрутизации моделей | deferred_fieldbook_candidate | Would require freshness of model/provider details. |
| Стек политики конфигурации | deferred_synthetic_candidate | Runtime-discipline table covers the concept. |
| Слой ingest/graphify/surface | deferred_synthetic_candidate | P09/P10 prose covers ingress; no real external visual found. |
| Схема безопасности worktree | deferred_fieldbook_candidate | Could merge with Git isolation visual in fieldbook. |

External-real status after P12: no new `<figure data-asset-status="external-real-candidate">` was added. The article keeps its existing synthetic figures plus the P11 local image asset `fig-gsd-browser-evidence-analogy`.

## P13 rare synthetic figure pass

No new synthetic figure inserted in P13.

Deferred P13 candidates:

| Candidate | Status | Reason |
|---|---|---|
| `fig-gsd-issue-to-ship-reader-path` | deferred | Would clarify the P10 example, but overlaps with `fig-gsd-artifact-consumption` and the adjacent prose. |
| `fig-gsd-runtime-discipline-stack` | deferred | The runtime-discipline table already gives the comparison; a stack diagram would be decorative. |
| `fig-gsd-failure-modes` | deferred | Failure modes are clearer as prose because each risk has different source/mitigation structure. |
| `fig-gsd-continuation-recovery-boundary` | deferred | Strong candidate for a fieldbook, not necessary for this concept article. |

Decision rule: after P11 and P12, P13 should not create synthetic substitutes for missing external screenshots. The existing visual layer is sufficient for the primary article.

## P14 visual note: standalone framing

P14 added a conceptual table, not a figure. It does not create a new visual asset candidate because the table is part of the reading contract and does not need independent image treatment. No external or local image queue changes.

## P15 visual note: negative mechanism test

P15 added prose, not a figure. A failure-mode visual remains deferred because the new subsection intentionally integrates limits into the mechanism instead of creating a separate error catalogue.

## P16 visual note: theory back-links

No image changes. Semantic back-links are companion navigation, not visual content.


## P17 image-plan language note

P17 не менял визуальный состав статьи. Идентификаторы фигур, class labels и asset paths сохранены как технические поля. Подписи и пояснения вокруг изображений переведены в более русский режим там, где это было пользовательским текстом; локальная Codex-картинка по-прежнему обозначена как аналогия к браузерным свидетельствам, а не как скриншот Open GSD.

## P18 image-plan language note

P18 не менял изображения и не добавлял новые figure candidates. Подпись локального Codex-изображения стала более прямой: она объясняет повторяемый ход UI-проверки и сохраняет явную оговорку, что это аналогия, а не скриншот GSD. Нижний раздел основного текста теперь говорит о будущем проходе по ассетам без внутренней ссылки на P12.

## P19 image-plan editorial note

Основной текст больше не содержит отдельный нижний раздел про будущие внешние ассеты. Это редакционное решение: статус изображений должен жить в `image_plan` и `external_image_queue`, а не завершать пользовательскую статью. Визуальный состав статьи не изменился: четыре synthetic figures остаются на местах, локальное Codex-изображение остаётся аналогией для браузерных свидетельств, внешние реальные изображения Open GSD по-прежнему не вставлены.

## P20 image-plan editorial note

P20 не менял визуальный план. Правка входного раздела не затронула figures, captions, asset paths или статусы внешних изображений.

## P21 image-plan editorial note

P21 не менял визуальный план и не затрагивал figures/captions. Правка касалась только локальной читательской рамки в начале статьи.

## P22 image-plan note

No visual asset was added, removed or reclassified. The first inline synthetic figure now appears after a stronger problem-first setup: the reader first sees the failure that GSD answers, then the process/runtime profile diagram. The public article still contains no bottom `Внешние изображения для asset-pass` section because no external-real candidate has been selected, rights-checked and localized for insertion. Existing visual balance remains four synthetic figures plus one local image asset.

## P23 image-plan sync

Image plan matches the current article. Inline figures are: `fig-gsd-process-runtime-profile`, `fig-gsd-browser-evidence-analogy`, `fig-gsd-artifact-consumption`, `fig-gsd-core-vs-pi-state` and `fig-gsd-not-pwg-boundary`. The first, third, fourth and fifth are synthetic figures; `fig-gsd-browser-evidence-analogy` is a local image asset and remains explicitly an analogy, not a GSD screenshot. No stale bottom asset backlog remains in the article.

## P24 image-plan note

No image, figure, caption, path or visual status changed. P24 was a style audit of prose and headings only.

## P25 image-plan note

No visual changes. The selective rewrite did not move figures, change captions, or alter local/external asset status.

## P26 image-plan note

No visual changes. Figures remain in the same order and with the same ids/classes/paths.

## Final verification image note

Визуальный слой проверен для упаковки. В статье есть четыре synthetic figures и один local image asset `fig-gsd-browser-evidence-analogy`. Локальный файл `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` должен быть включён в result archive, чтобы относительный путь статьи мог резолвиться после overlay. Внешние реальные изображения не вставлены и не зеркалятся в нижнем разделе статьи, потому что ни один rights-safe standalone Open GSD screenshot/diagram не был выбран для inline placement.
