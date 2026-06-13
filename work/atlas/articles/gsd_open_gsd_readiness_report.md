# GSD / Open GSD — readiness report

Статус: Final verification completed / package ready with explicit publication blockers.

## Созданные выходы

- `work/atlas/articles/gsd_open_gsd.md`
- `work/atlas/articles/gsd_open_gsd_source_usage.md`
- `work/atlas/articles/gsd_open_gsd_source_transfer_ledger.md`
- `work/atlas/articles/gsd_open_gsd_image_plan.md`
- `work/atlas/articles/gsd_open_gsd_external_image_queue.md`
- `work/atlas/articles/gsd_open_gsd_open_questions.md`
- `work/atlas/articles/gsd_open_gsd_theory_links.md`
- `work/atlas/articles/gsd_open_gsd_degradation_and_duplication_audit.md`
- `work/atlas/articles/gsd_open_gsd_readiness_report.md`

## Что сделал P01

- Создана большая самостоятельная concept-first статья по GSD / Open GSD.
- Центральная ось проведена как process-runtime profile: фазы, `.planning/`, `.gsd`, `STATE.md`, SQLite, tool policy, supervision, git isolation, verification and evidence.
- Разведена граница `gsd-core` / `gsd-pi` / `gsd-browser`.
- Раздел “Почему GSD ещё не PWG” создан как центральный boundary, а не как общая теория PWG.
- Созданы и синхронизированы companion-файлы.
- Dossier image candidates получили P01 disposition в image plan; external queue создана без выдуманных изображений.

## Сводный статус после P23

Текущий основной текст собран как самостоятельная concept-first статья: problem-first вход, рабочие опоры, границы с соседними концепциями, механика `gsd-core`, `gsd-pi`, evidence layer, политика среды выполнения, восстановление, проверка, ограничения и итоговая карта режимов.

Закрыто к P23:

- Контракт статьи и границы уточнены.
- Source-depth проходы перенесли нужную фактуру в основной текст без превращения статьи в справочник команд.
- Issue-driven ingress, artifact consumption, state recovery, verification, runtime policy и failure modes встроены в читательский маршрут.
- Visual layer синхронизирован: четыре synthetic figures и один local image asset; внешний rights-safe Open GSD image не вставлен.
- Языковые и редакторские проходы убрали большую часть внутреннего pass-facing тона, включая нижний asset backlog из основной статьи.
- Companion-файлы очищены от устаревших pass debts; оставлены только публикационные blockers, freshness concerns и будущие article-link вопросы.

Оставшиеся blockers вынесены в `gsd_open_gsd_open_questions.md` и касаются только freshness/release verification, lineage reference paths, external-real image asset policy, image path assembly, финальной русской унификации терминов и будущих ссылок на соседние статьи.

## Статус готовности

`ready_for_next_pass_after_P23_companion_sync`.


## P02 completion note

Статус: P02 completed / контракт статьи и границы усилены.

Что изменено:

- В основной статье добавлен раздел `Контракт статьи`.
- В статью добавлены границы с PWG, BMAD, Gas Town, Spec Kit, Kiro и SPDD.
- Уточнена отрицательная граница: статья не должна становиться учебником, инвентарём команд или справочником конфигурации.
- Companion-файлы обновлены: source usage, source transfer ledger, open questions, theory links, degradation/duplication audit.
- Image/external image queue не требует изменений по P02: новые факты не добавляют визуальных кандидатов.

Статус готовности: `ready_for_P03_with_known_debts`.


## P03 completion note

Статус: P03 completed / dossier inventory added.

Что сделано:

- В `source_transfer_ledger` добавлен inventory: что уже перенесено, что отложено, где нужны primary-source openings, где статье могут не хватать technical anchors.
- В `source_usage` добавлен source-status по группам источников.
- В `open_questions` добавлены конкретные долги: issue-driven orchestration, gate/checkpoint sources, verification ladder, current raw reference paths.
- Основной текст не изменялся: P03 не нашёл article-critical пропуска, который требовал бы немедленной вставки.

Статус готовности: `ready_for_P04_with_known_debts`.


## P04 completion note

Статус: P04 completed / `User Guide` углублён как фазовый lifecycle-control workflow.

Что изменено:

- В основной статье добавлен subsection `Фазы как регуляторы движения`.
- Workflow теперь явно отвечает на три вопроса P04: что двигает работу вперёд, что её останавливает, где появляется человеческий надзор.
- Companion-файлы синхронизированы: source usage, source transfer ledger, image plan, external image queue, open questions, theory links, degradation/duplication audit.
- Новые внешние изображения не добавлялись; P04 оставил возможную future synthetic figure как visual debt.

Статус готовности: `ready_for_P05_with_known_debts`.


## P05 completion note

Статус: P05 completed / commands, configuration, architecture, tool policy, git isolation и browser evidence собраны как runtime discipline.

Что изменено:

- В основной статье добавлен subsection `Команды и конфигурация как runtime-дисциплина`.
- Добавлена таблица, которая связывает командную маршрутизацию, `config.json`, tool policy, git-изоляцию, наблюдаемость/восстановление и браузерные свидетельства с центральной осью статьи.
- Уточнена граница для будущих case studies: оценка GSD без конфигурации, модели, режима git isolation, tool policy, audit/MCP/evidence/recovery-path неполна.
- Companion-файлы синхронизированы; внешние реальные изображения не добавлялись.

Статус готовности: `ready_for_P06_with_known_debts`.


## P06 completion note

Статус: P06 completed / `.planning/`, `STATE.md`, handoff and recovery linked to continuation boundary.

Что изменено:

- В основной статье добавлен subsection `Продолжение и восстановление: что дают файлы состояния`.
- Показано, как `STATE.md`, фазовые документы, `HANDOFF.json`, `.continue-here.md`, side context, SQLite/`.gsd` projections and diagnostics help continuation after context loss or interruption.
- Уточнена граница с PWG: state files and local recovery can feed a future work graph, but they do not by themselves provide durable dependency/readiness/ownership/evidence semantics.
- Companion-файлы синхронизированы; новые внешние изображения не добавлялись.

Статус готовности: `ready_for_P07_with_known_debts`.


## P07 completion note

Статус: P07 completed / `gsd-pi`, SQLite, tool policy and verification surfaces reframed as one unit lifecycle.

Что изменено:

- В основной статье добавлен subsection `Единица работы как контур среды выполнения`.
- Runtime/state details explained as lifecycle functions: choosing a unit from SQLite, constructing focused context, applying `ToolsPolicy`, executing through `gsd_exec`, verifying through commands/verdicts, persisting results and pausing/recovering when unsafe.
- Companion-файлы синхронизированы; новая external image не добавлялась.

Статус готовности: `ready_for_P08_with_known_debts`.


## P08 completion note

Статус: P08 completed / failure modes, over-ceremony and anti-summary limits strengthened.

Что изменено:

- В раздел `Типичные сбои и чрезмерное применение` добавлено anti-summary framing: phase tutorial without freshness, gates, checkpoints, tool policy and state consumption is only an illusion of process.
- Strengthened limits: stale state files, stale `PLAN.md`, supervised autonomy illusion, no full graph state, ceremony heavier than task, DB/projection confusion and local SQLite/WAL boundary.
- Companion-файлы синхронизированы; новых изображений нет.

Статус готовности: `ready_for_P09_with_known_debts`.


## P09 completion note

Статус: P09 completed / free expansion added issue-driven ingress and GitHub sync boundary.

Что изменено:

- В основной статье добавлены paragraphs on GitHub issue ingress: import into `.planning/issues/`, classification, human review before phase inclusion, binding/closing after ship.
- Added `gsd-pi` GitHub sync boundary: mapping to Issues/PRs/Milestones in `.gsd/.github-sync.json`, with sync as mirror/channel rather than source of runtime authority.
- Companion-файлы синхронизированы; внешние изображения не добавлялись.

Статус готовности: `ready_for_P10_with_known_debts`.


## P10 completion note

Статус: P10 completed / second free expansion added end-to-end reader path.

Что изменено:

- В основной статье добавлен subsection `Сквозной пример: от входящего issue до поставки`.
- The example connects issue ingress, Discuss, Plan, plan-checker revision, Execute checkpoint, Verify/UAT/browser evidence, Ship/issue close and lifecycle repair.
- Companion-файлы синхронизированы; внешние изображения не добавлялись.

Статус готовности: `ready_for_P11_with_known_debts`.


## P11 completion note

Статус: P11 completed / local visual asset pass.

Что изменено:

- В основной статье вставлен local image asset `openai-codex-chrome-devtools-validation.webp` as `fig-gsd-browser-evidence-analogy` near the Verify/`gsd-browser` evidence paragraph.
- `openai-codex-dashboard-workflow.webp` and `fowler-harness-continuous-feedback.png` were reviewed and not inserted, with reasons recorded in the image plan.
- Companion-файлы синхронизированы; external image queue remains for P12.

Статус готовности: `ready_for_P12_with_known_debts`.

## P12 completion note

Статус: P12 completed / external-real visual candidates checked and not inserted.

Что изменено:

- В нижнем разделе основного текста уточнён статус внешних изображений: официальные Open GSD product/docs/roadmap surfaces не дали проверенного standalone screenshot/diagram для inline `external-real-candidate`.
- `image_plan` получил явные dispositions для candidates из dossier image section.
- `external_image_queue` обновлён: все четыре P12-направления checked/no external-real image inserted.
- Companion-файлы синхронизированы; новых inline images нет.

Статус готовности: `ready_for_P13_with_known_debts`.

## P13 completion note

Статус: P13 completed / rare synthetic visual pass kept conservative.

Что изменено:

- Новые synthetic figures не вставлены: existing visual layer already covers nontrivial lifecycle/state/evidence/PWG boundaries.
- Deferred candidates recorded in image plan and transfer ledger: issue-to-ship path, runtime-discipline stack, failure modes and continuation/recovery boundary.
- Companion-файлы синхронизированы; external image queue unchanged except for P13 status note.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P14 completion note

Статус: P14 completed / standalone concept framing strengthened.

Что изменено:

- В основной статье добавлен subsection `Минимум рамки для самостоятельного чтения`.
- Читателю дан локальный набор различений: намерение, рабочее состояние, полномочие, свидетельство и ремонт жизненного цикла.
- Повтор теории ограничен: каждое понятие привязано к GSD-поверхностям, а не к общей главе.
- Companion-файлы синхронизированы; новые изображения не добавлялись.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P15 completion note

Статус: P15 completed / mechanism limits and failure boundaries reinforced.

Что изменено:

- В основной статье добавлен subsection `Негативный тест механизма` после process-runtime figure.
- Усилены границы: phase tutorial, inert persistent files, hidden supervision, weak verification, pseudo-PWG and over-ceremony.
- Failure material embedded into mechanism rather than expanded into a separate error catalogue.
- Companion-файлы синхронизированы; новые изображения не добавлялись.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P16 completion note

Статус: P16 completed / semantic theory back-links added.

Что изменено:

- `theory_links` получил semantic back-link table для `00`, `A3`, `A5`, `A7`, `A9`, `A10` и `C5`.
- Основной текст не расширялся: статья уже связана с общей рамкой через локальный frame and negative mechanism test, а новый теоретический индекс утяжелил бы чтение.
- Companion-файлы синхронизированы; новых изображений нет.

Статус готовности: `ready_for_next_pass_with_known_debts`.


## P17 completion note

Статус: P17 completed / first Russian-language pass applied.

Что изменено:

- Основной текст выровнен в русский пользовательский режим: убрана часть случайной английской связки и машинных гибридов.
- Точные имена команд, путей, файлов, конфигурационных ключей, source labels и устойчивых технических терминов сохранены.
- Отдельно проверены места, где широкие замены могли повредить `workflow-map.md`, `/gsd-workflow`, `workflow.*` и `checkpoint:human-verify`.
- Companion-файлы синхронизированы; новых фактов и изображений нет.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P18 completion note

Статус: P18 completed / second Russian-language pass applied.

Что изменено:

- Уточнены заголовки, подписи фигур, таблицы и нижний раздел про будущие ассеты.
- `process-runtime profile` закреплён в основном тексте как `профиль работы в среде выполнения`.
- Обычный `prompt` в объяснительном тексте заменён на `запрос`, кроме source-specific названий.
- Из пользовательского нижнего раздела убрана внутренняя ссылка на P12; статус внешних изображений описан как редакционная проверка ассетов.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P19 completion note

Статус: P19 completed / editorial pass 1 applied.

Сначала выявленные проблемы:

- Основная статья после языковых проходов всё ещё заканчивалась служебным разделом про будущий проход по ассетам.
- Этот раздел был полезен для редакционного учёта, но ослаблял standalone concept-first финал: читатель выходил из статьи не с главным различением GSD, а с внутренним статусом картинок.

Что изменено:

- Нижний asset-pass section удалён из `gsd_open_gsd.md`.
- Статус внешних изображений сохранён в `image_plan` и `external_image_queue`.
- Основной текст теперь заканчивается концептуальным разделом `Как читать GSD в атласе`.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_editorial_pass_with_known_debts`.

## P20 completion note

Статус: P20 completed / editorial pass 2 applied.

Сначала выявленные проблемы:

- Вступительный раздел `Контракт статьи` звучал слишком редакционно и напоминал внутренний бриф.
- Формула `успешное чтение даёт четыре результата` удерживала meta-слой вместо прямого объяснения, что в GSD важно увидеть.

Что изменено:

- Раздел переименован в `Что важно удержать`.
- Первые абзацы раздела переписаны как практическая модель чтения GSD.
- Границы статьи сформулированы через реальные риски: справочник команд, редукция к `.planning/`, универсальная замена соседним режимам.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_editorial_pass_with_known_debts`.

## P21 completion note

Статус: P21 completed / editorial pass 3 applied.

Сначала выявленные проблемы:

- Раздел `Минимум рамки для самостоятельного чтения` звучал как внутренняя теоретическая карточка.
- Термин `местные различения` был точным для редакции, но менее удобным для standalone-читателя.

Что изменено:

- Раздел переименован в `Пять опор для чтения GSD`.
- Табличный заголовок `Местное различение` заменён на `Рабочая опора`.
- Заключение блока переформулировано как локальная оптика чтения GSD.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_editorial_pass_with_known_debts`.

## P22 completion note

Статус: P22 completed / entry-sequence structure pass applied.

Сначала выявленные проблемы:

- Первый экран слишком быстро переходил от объекта статьи к продуктовой поверхности и рамке чтения; конкретная боль длинной агентной работы появлялась позже.
- Для standalone-читателя было полезнее раньше увидеть `context rot`, преждевременную готовность и потерю состояния, а уже затем читать рабочие опоры и границы.

Что изменено:

- Раздел `Что ломается без внешнего процесса` перенесён сразу после вводных абзацев.
- Раздел `Что важно удержать` теперь следует после конкретных failure cases и звучит как ответ на уже показанную проблему.
- Основная статья по-прежнему не содержит служебного asset-pass backlog section.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_pass_with_known_debts`.

## P23 completion note

Статус: P23 completed / companion sync applied.

Что изменено:

- `open_questions` переписан как текущий список blockers, а не хронологический журнал закрытых долгов.
- Верхний `readiness_report` заменил устаревший P01 debt roadmap на сводный статус после P23.
- `source_transfer_ledger` больше не говорит, что P11–P12 visual passes только предстоят; их результат сведен к текущему status: внешнего rights-safe Open GSD image нет.
- Source usage, image plan, external image queue, theory links, audit and readiness синхронизированы с фактической статьёй.
- Основной текст не менялся; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_next_pass_after_companion_sync`.

## P24 completion note

Статус: P24 completed / style defect audit applied.

Что изменено:

- Исправлены реальные стилевые дефекты без тотального переписывания статьи.
- Вступление и несколько заголовков стали естественнее по-русски.
- Убраны или смягчены кальки и псевдотермины: `публичная поверхность`, `анти-резюме`, `процессная машина`, `исполняемая дисциплина`, `coverage решений`.
- В читательском блоке `Ремонт жизненного цикла` заменён на более прямое `Обновление после поставки`; theory bridge сохранён в companion-файле.
- Факты, источники, визуальные элементы, команды, пути и конфигурационные ключи не менялись.

Статус готовности: `ready_for_next_style_or_final_pass`.

## P25 completion note

Статус: P25 completed / selective natural rewrite applied.

Что изменено:

- Выборочно выправлены оставшиеся неестественные русские обороты после P24.
- Улучшены boundary paragraphs, command-routing prose, issue-to-ship example, runtime policy section and several table cells.
- Конкретные source labels, команды, пути, config keys, факты, фигуры и структура статьи сохранены.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_final_style_or_package_pass`.

## P26 completion note

Статус: P26 completed / guarded final human technical style pass applied.

Что изменено:

- Финально выровнены тон, ритм, переходы и несколько подзаголовочных/связующих фраз.
- Обычные английские слова в технических объяснениях переведены там, где русский вариант естественнее; source-specific labels сохранены.
- Сохранены факты, источники, команды, числовые ограничения, границы, figures and image paths.
- Companion-файлы синхронизированы; новых источников, фактов и изображений нет.

Статус готовности: `ready_for_package_or_final_readiness_pass`.

## Final verification completion note

Статус: `completed_with_publication_blockers`.

Финальная проверка подтвердила наличие всех target outputs, самостоятельность основной статьи, заполненность companion-файлов, конкретность технических anchors и честное описание оставшихся рисков. В статье нет нижнего редакционного asset backlog, нет inline external-real placeholders без выбранного источника, нет служебных captions и нет generic `relevant but untransferred` blocker.

Оставшиеся blockers являются публикационными, а не блокерами сборки пакета: свежая проверка release/docs перед датированной публикацией, подтверждение lineage/reference paths, возможный внешний real-image pass при требовании площадки, проверка site assembly для относительного пути локального asset и будущие links на соседние статьи атласа.
