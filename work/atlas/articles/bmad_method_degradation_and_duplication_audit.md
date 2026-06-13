# BMAD Method — degradation and duplication audit

Статус: P26 добавил guarded final style audit; фактура P01–P25 сохранена, публичная форма стабилизирована.

## Article function

Reader question: how BMAD distributes agentic development across roles, documents, gates, workflows and story context so work moves through readable, verifiable and repairable artifacts.

Central axis in P01: BMAD as an artifact-first SDLC profile. The draft is organized around artifact transfer, context narrowing, human gates, story context, sprint state, review, correct-course, brownfield documentation and lifecycle repair.

## Anti-degradation checks

| Risk | P01 assessment | Evidence in draft | Debt |
| --- | --- | --- | --- |
| Article becomes dossier summary | Stronger after P10. | New invariant section gives a reader path before details; sections follow mechanism rather than source order: installation surface, context cascade, roles, modes, story, status, gates, review, correct-course, brownfield, investigation, failures. | Later editorial passes should remove remaining source-enumeration rhythm and check intro overlap. |
| Article becomes second theory | Controlled with P15 watchpoint. | Failure-mode wording is now embedded in BMAD invariant and roles, not imported as a theory chapter. | P16 should check controlled repetition and reduce duplicated warnings. |
| Article becomes technical appendix | Avoided. | Commands/files are explained through context transfer and verification. | More source-depth may add details; guard against command list bloat. |
| BMAD absorbs TEA/Enterprise | Stronger after P15. | Invariant now says Enterprise/TEA should not become mandatory evidence layer where ordinary review/tests are enough. | Future pass should keep TEA proportion under control. |
| BMAD absorbs Gas Town/PWG | Controlled. | Draft says baseline BMAD is a process/status profile, not full PWG; Gas Town boundary kept high-level. | Needs later sync if Gas Town/PWG article exists. |
| BMAD absorbs GSD | Controlled by omission. | GSD comparison not detailed because GSD dossier not allowed in P01. | Later companion sync may add a safe boundary note from allowed sources. |
| Quick Flow underexplained | Stronger after P09. | Quick Flow section now includes input forms, short spec, tests, local commit, human diff review, revert path, escalation boundary, intent compression, `deferred-work.md` and layer-aware repair. | Future visual pass could add or reject Quick Flow figure; exact output names need source refresh. |
| Brownfield underexplained | Strong for P01. | Document Project, scan levels, generated docs, checklist, CSV, deep-dive included. | Ensure this does not turn into handbook. |
| Visual layer decorative | Controlled. | One external source placeholder plus two synthetic figures with clear conceptual work. | Later visual pass should verify both synthetic figures remain necessary. |
| Source provenance missing | Mostly controlled. | Main facts have primary links; companion source usage created. | P01 did not perform external source refresh. |
| English overuse | Mostly controlled. | English retained for commands/files/source labels and stable terms. | Later language passes should translate ordinary workflow prose where possible. |

## P01 readiness status

`ready_for_next_pass_with_known_debts`.

Known debts:

- Fresh source check required for current BMAD version, release status, command names and config paths.
- External workflow map asset requires rights/download/quality/attribution check.
- Article may still contain dense source-rich paragraphs that later editorial passes should smooth.
- Future source-depth passes should decide whether to expand exact story-file fields, readiness report structure, PRD validation rubric and Correct Course proposal anatomy.
- Future concept reinforcement should tighten the final theory return so it remains local and operational.


## P02 contract and boundary audit

| Check | P02 result | Evidence / action |
| --- | --- | --- |
| Reader question visible | PASS | Intro still states reader question; new contract section makes it operational. |
| Article is not generic overview | PASS with watchpoint | New negative boundary says details must support lifecycle function; future source-depth passes can still bloat. |
| Article is not product/tutorial reference | PASS | Commands and files remain tied to context transfer, status, gate, evidence or repair. |
| Article is not theory duplicate | PASS | C5/A10 remain read-only context; theory section is local and boundary-oriented. |
| BMAD ≠ GSD | PASS | New contract section explicitly separates artifact-first SDLC profile from GSD phase loop/runtime/process supervision. |
| BMAD ≠ PWG | PASS | `sprint-status.yaml` framed as minimal state machine, not durable graph. |
| BMAD ≠ Gas Town | PASS | Gas Town framed as operating environment/orchestration layer, not BMAD. |
| BMAD ≠ Spec Kit/Kiro/SPDD/TDAD | PASS with TDAD debt | Spec/prompt/test methods are explicitly adjacent; TDAD has only placeholder-level boundary because no TDAD dossier was allowed. |
| ADR boundary | PASS | ADR framed as decision memory inside architecture, not whole execution lifecycle. |
| Companion sync | PASS | Source usage, transfer ledger, open questions, theory links, image plan, image queue and readiness report updated. |

P02 readiness status: `ready_for_next_pass_with_contract_boundaries_and_known_debts`.


## P04 handoff audit

| Check | P04 result | Evidence / action |
| --- | --- | --- |
| Core chain reads as documentary handoff | PASS | Added handoff paragraph and table in «Главная цепочка». |
| Roles avoid persona catalog | PASS | Role paragraph now ties Mary/John/Sally/Winston/Amelia to artifact/output quality. |
| Source provenance preserved | PASS | New claims cite existing BMAD primary sources already tracked in source usage. |
| Visual/schema bloat controlled | PASS with watchpoint | Inline table overlaps with synthetic figure; logged for later visual/editorial decision. |
| Content preservation | PASS | Existing strong sections preserved; no broad rewrite. |

P04 readiness status: `ready_for_next_pass_with_documentary_handoff_strengthened`.


## P05 file mechanics audit

| Check | P05 result | Evidence / action |
| --- | --- | --- |
| `_bmad/` and `_bmad-output/` explained as recovery surfaces | PASS | Added recovery-surface table. |
| Manifest/pinning included without install tutorial drift | PASS with watchpoint | Manifest appears as reproducibility/recovery, not step-by-step setup. |
| Story files and sprint state tied to next action | PASS | Added table and sprint-status recovery paragraph. |
| PWG boundary preserved | PASS | Sprint state remains minimal state machine, not durable graph. |
| Source provenance | PASS | Used already tracked primary BMAD sources. |
| Density risk | WATCH | Two early tables may be heavy; logged in image plan/open questions. |

P05 readiness status: `ready_for_next_pass_with_file_recovery_surface_strengthened`.


## P06 brownfield audit

| Check | P06 result | Evidence / action |
| --- | --- | --- |
| Scan levels visible | PASS | Added Quick/Deep/Exhaustive/Deep Dive table. |
| Documentation requirements visible | PASS | Existing flags retained; P06 does not import full CSV matrix. |
| `project-scan-report.json` and generated docs/index visible | PASS | Added explicit state-of-knowledge and index/navigation paragraph. |
| Stale-doc risk visible | PASS | Added paragraph on old scan/index/PRD/stories as false current truth. |
| Handbook drift controlled | PASS with watchpoint | Details remain article-level; table density logged. |
| Source provenance | PASS | Used existing primary sources. |

P06 readiness status: `ready_for_next_pass_with_brownfield_knowledge_creation_strengthened`.


## P07 gates/review audit

| Check | P07 result | Evidence / action |
| --- | --- | --- |
| PRD validation/readiness surfaced | PASS | Human-gates table plus review section. |
| Checkpoint preview surfaced as human decision aid | PASS | Table and review section say it is not pass/fail. |
| Correct-course/investigation/retrospective surfaced as repair gates | PASS | Table ties each to human choice and next artifact. |
| Human authority preserved | PASS | Table and concluding paragraph separate agent preparation from human acceptance. |
| Source provenance | PASS | Existing primary sources tracked. |
| Density risk | WATCH | New table adds to table load; logged. |

P07 readiness status: `ready_for_next_pass_with_human_gates_and_repair_strengthened`.


## P08 evidence/release limits audit

| Check | P08 result | Evidence / action |
| --- | --- | --- |
| TEA/Enterprise bounded as extension | PASS | Review/testing section now names TEA as evidence/release boundary, not base BMAD. |
| Token cost included safely | PASS | Framed structurally from workflow behavior; no anecdotal reports used as evidence. |
| Overplanning/ceremony limits visible | PASS | Failure section includes Quick/full mismatch, Correct Course overhead and TEA coordination cost. |
| Stale artifacts visible | PASS | Existing failure/brownfield sections retained. |
| Module confusion visible | PASS | Failure section separates BMM, TEA, modules, web bundles and release-sensitive surfaces. |
| Source provenance | PASS | Used existing primary sources; no unvetted community evidence. |

P08 readiness status: `ready_for_next_pass_with_evidence_extension_and_limits_strengthened`.

## P09 Quick Dev audit

| Check | P09 result | Evidence / action |
| --- | --- | --- |
| Quick Flow no longer reads as “just faster coding” | PASS | Added mini-lifecycle paragraphs: intent compression, short spec/approval, deferred unrelated work, repair by failed layer. |
| Full BMAD boundary preserved | PASS | New text explicitly says multi-system, unclear or architecture-sensitive work should escalate to full BMAD. |
| Handbook drift controlled | PASS | Did not add step-by-step Quick Dev tutorial or command catalog. |
| Visual density controlled | PASS | No new figure/table; Quick Dev diagram remains deferred. |
| Source provenance | PASS | Used BMAD primary sources already in dossier/current source map. |

P09 readiness status: `ready_for_next_pass_with_quick_dev_lifecycle_strengthened`.

## P10 reader-path audit

| Check | P10 result | Evidence / action |
| --- | --- | --- |
| Article has concept-first reader path | PASS | Added «Инвариант BMAD» before installation/technical surfaces. |
| New material is not just style polish | PASS | Added a portable mechanism: artifact that frames the next step + four artifact properties. |
| C5 boundary respected | PASS | The section explains mechanism and route; it does not turn into a command catalog or theory chapter. |
| Source provenance controlled | PASS | Used Workflow Map as public anchor and C5 as internal editorial structure; no new external claim. |
| Duplication risk logged | WATCH | The invariant may overlap with intro, figure and practical-reading section; logged in open questions. |

P10 readiness status: `ready_for_next_pass_with_reader_path_strengthened`.

## P11 local visual asset audit

| Check | P11 result | Evidence / action |
| --- | --- | --- |
| Insert-or-explain applied to relevant local assets | PASS | Reviewed required Fowler harness images and recorded rejection reasons in image plan. |
| BMAD article not diluted by adjacent visuals | PASS | Harness engineering visuals rejected because they would blur article boundary. |
| Existing external candidate preserved | PASS | Official BMAD Workflow Map remains queued; no synthetic or local surrogate substituted. |
| No visual bloat | PASS | No new figure/table inserted. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P11 readiness status: `ready_for_next_pass_with_local_assets_dispositioned`.

## P12 external visual asset audit

| Check | P12 result | Evidence / action |
| --- | --- | --- |
| Dossier real candidates dispositioned | PASS | Official Workflow Map kept inline; project tree classified as source text/code; other candidates synthetic/deferred. |
| No external image downloaded prematurely | PASS | Candidate remains queued for rights/quality/attribution/localization. |
| No screenshot bloat | PASS | Did not turn project tree or source tables into screenshots. |
| Synthetic/external boundary preserved | PASS | Existing synthetic figures remain synthetic; no new synthetic surrogate created in external pass. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P12 readiness status: `ready_for_next_pass_with_external_visual_candidates_dispositioned`.

## P13 synthetic visual audit

| Check | P13 result | Evidence / action |
| --- | --- | --- |
| Synthetic figures added only when unusually useful | PASS | No new synthetic figure added. |
| Existing visuals not duplicated | PASS | Context cascade and sprint-state figures retained; Quick Dev and other diagrams deferred. |
| Article avoids visual bloat | PASS | Multiple tables/figures already exist; P13 chose restraint. |
| Boundary diagrams not premature | PASS | BMAD vs GSD/PWG/Gas Town visual deferred until cross-article sync. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P13 readiness status: `ready_for_next_pass_with_synthetic_visuals_controlled`.

## P14 standalone concept audit

| Check | P14 result | Evidence / action |
| --- | --- | --- |
| Concept-first reader can understand BMAD locally | PASS | Added minimal audit-report example showing one change through artifacts. |
| Controlled theory repeat, not copy-paste | PASS | Example concretizes process/context narrowing; no theory fragment copied. |
| No new official-source claim invented | PASS with watchpoint | Example is authorial; open questions record final copy caveat. |
| Article not converted into handbook | PASS | Example explains mechanism, not step-by-step procedure. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P14 readiness status: `ready_for_next_pass_with_standalone_concept_example_strengthened`.

## P15 mechanism/failure audit

| Check | P15 result | Evidence / action |
| --- | --- | --- |
| Personas become theater | PASS | Invariant and role section now tie roles to artifact/gate/next-input changes. |
| Documents become dead archives | PASS | Invariant says a document must be read by the next workflow or support a human decision. |
| Stale artifacts integrated | PASS with watchpoint | Stale PRD/story/scan/project-context now appears as core mechanism failure; possible repetition logged. |
| Quick/Full/Enterprise confusion integrated | PASS | Mode errors are embedded in invariant rather than only listed later. |
| Evidence layer not mandatory core | PASS | TEA/Enterprise framed as optional upper boundary. |
| BMAD does not absorb PWG/GSD/Gas Town | PASS | P15 did not add graph/orchestration details. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P15 readiness status: `ready_for_next_pass_with_mechanism_failures_embedded`.

## P16 semantic-backlink audit

| Check | P16 result | Evidence / action |
| --- | --- | --- |
| Backlinks are semantic, not navigational | PASS | Added a matrix stating what each theory fragment asks and how BMAD answers that question. |
| Main article does not rewrite whole theory | PASS | Added only a short guard paragraph in «Где BMAD помогает общей теории». |
| BMAD remains standalone | PASS | Article still centers on artifact-first BMAD mechanics; theory details moved to companion. |
| No new public facts or visual assets | PASS | P16 used internal theory fragments only; no external images or source claims added. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P16 readiness status: `ready_for_next_pass_with_semantic_theory_backlinks`.

## P17 language-pass audit

| Check | P17 result | Evidence / action |
| --- | --- | --- |
| Russian mode improved in main article | PASS | Replaced many accidental English connectors and hybrid phrases in the public text. |
| Argument preserved | PASS | No source fact, boundary, image decision or theory claim was removed. |
| Source names / commands preserved | PASS with watchpoint | Official names, commands, paths and status values remain in English where exact form matters. |
| Mechanical replacement risks checked | PASS | URLs, key figure ids and `_bmad-output/*-artifacts/` paths were repaired after broad replacements. |
| Companion sync | PASS | Source usage, ledger, image plan, queue, open questions, theory links, audit/readiness updated. |

P17 readiness status: `ready_for_next_pass_with_first_language_cleanup`.

## P18 — аудит второго языкового прохода

| Проверка | Результат P18 | Действие / свидетельство |
| --- | --- | --- |
| Заголовки и нижний раздел про ассеты читаются по-русски | PASS | Нижний заголовок изменён на «Внешние изображения для прохода по ассетам»; описание Workflow Map сделано естественнее. |
| Подписи и таблицы проверены | PASS | Исправлено «текущее состояние спринта»; подпись placeholder для Workflow Map вычитана. |
| Точные имена из источников сохранены | PASS | Команды, пути, id фигур, source labels, статусы и имена артефактов BMAD сохранены там, где нужна точная форма. |
| Новые факты из источников не добавлены | PASS | P18 был только языковым проходом по подписям, таблицам и формулировкам. |
| Companion-файлы синхронизированы | PASS | Source usage, ledger, image plan, queue, open questions, theory links и readiness report обновлены. |

P18 readiness status: `ready_for_editorial_passes_after_second_language_cleanup`.

## P19 — аудит первого общего редакторского прохода

### Диагностика P19

| Проблема | Почему мешала standalone-статье | Исправление |
| --- | --- | --- |
| Контрактный раздел звучал преимущественно как граница с соседями | Читатель мог увидеть запретительную рамку раньше положительной функции BMAD | Заголовок изменён на «BMAD как профиль передачи работы через артефакты». |
| Формула «отрицательная граница» была абстрактной | Она работала как внутренний редакторский термин, а не как естественная инструкция читателю | Переписано как «ограничение включения деталей». |
| Практический раздел завершал статью общим советом, но не давал короткой проверки применения | Для standalone article нужен способ самому проверить, работает ли BMAD как механизм передачи следующего шага | Добавлен четырёхвопросный критерий: текущий артефакт, следующий рабочий процесс, человеческое решение, место возврата найденного факта. |

| Проверка | Результат P19 | Действие / свидетельство |
| --- | --- | --- |
| Standalone-функция усилена | PASS | Добавлен практический критерий применения BMAD без нового источникового слоя. |
| Удачные части не переписаны | PASS | P19 сделал точечные правки заголовка, одного абзаца и финального практического раздела. |
| Фактура сохранена | PASS | Источники, ссылки, технические детали, визуальные решения и границы не изменены. |
| Companion-файлы синхронизированы | PASS | Source usage, transfer ledger, image plan, queue, open questions, theory links и readiness report обновлены. |

P19 readiness status: `ready_for_second_editorial_pass_with_practical_criterion_added`.

## P20 — аудит второго общего редакторского прохода

### Диагностика P20

| Проблема | Почему мешала standalone-статье | Исправление |
| --- | --- | --- |
| Контрактный раздел стоял сразу после вступления | Сравнение с GSD, PWG, Gas Town и другими соседями появлялось до того, как читатель увидел практический пример BMAD | Раздел переставлен после «Минимальный пример: одно изменение через BMAD». |
| Абзац маршрута читателя устаревал после перестановки | Он не называл минимальный пример и контракт как отдельные опорные узлы | Абзац после инварианта обновлён. |
| Риск структурного дрейфа | Перестановка могла затронуть визуальные и источниковые решения | Визуальные места, ссылки и фактические утверждения оставлены без изменений. |

| Проверка | Результат P20 | Действие / свидетельство |
| --- | --- | --- |
| Standalone-вход улучшен | PASS | Читатель сначала получает проблему, инвариант и пример, затем границы. |
| Границы не ослаблены | PASS | Boundary-блок сохранён полностью и остаётся перед установкой и источниковой детализацией. |
| Фактура сохранена | PASS | Источники, ссылки, технические детали и visual queue не изменены. |
| Companion-файлы синхронизированы | PASS | Source usage, ledger, image plan, queue, open questions, theory links и readiness report обновлены. |

P20 readiness status: `ready_for_third_editorial_pass_with_boundary_section_repositioned`.

## P21 — аудит третьего общего редакторского прохода

### Диагностика P21

| Проблема | Почему мешала standalone-статье | Исправление |
| --- | --- | --- |
| После перестановки P20 переход от boundary-блока к установке был резким | Читатель переходил от сравнительных границ сразу к `npx bmad-method install` | Добавлен мост: от сравнения к устройству метода — где создаются артефакты, как они передаются, кто принимает решения и где чинится контекст. |
| Несколько заголовков оставались менее точными, чем содержание разделов | Они смешивали обычные английские слова и source-specific names | Уточнены заголовки про `bmad-checkpoint-preview`, brownfield-проект и расследование. |
| Риск чрезмерной перестройки | Третий редакторский проход мог начать переписывать удачные source-rich sections | Правки ограничены переходом и заголовками; фактура не сглажена. |

| Проверка | Результат P21 | Действие / свидетельство |
| --- | --- | --- |
| Переход после контрактного раздела улучшен | PASS | Добавлен один связующий абзац перед установкой. |
| Навигационные заголовки стали точнее | PASS | Заголовки соответствуют официальным рабочим процессам и функции разделов. |
| Фактура сохранена | PASS | Источники, ссылки, таблицы, фигуры и visual queue не изменены. |
| Companion-файлы синхронизированы | PASS | Source usage, ledger, image plan, queue, open questions, theory links и readiness report обновлены. |

P21 readiness status: `ready_for_structure_pass_with_editorial_sequence_stabilized`.

## P22 — аудит public/article structure and entry sequence

### Диагностика P22

| Проблема | Почему мешала публичной статье | Исправление |
| --- | --- | --- |
| Inline caption Workflow Map был служебным | Фразы «здесь нужна» и «должна пройти проверку» звучали как executor note, а не как публичная подпись | Caption переписан как описание официальной Workflow Map BMAD. |
| Нижний статус внешнего изображения ссылался на P12 | P12 — рабочий проход, а не читательская информация | Убрана ссылка на P12; оставлен статус `external-real-candidate` и будущие проверки. |
| Название bottom section разошлось с asset-pass label из рабочего протокола | Для будущей обработки важно явно видеть asset-pass секцию | Заголовок возвращён к «Внешние изображения для asset-pass». |
| Первый экран мог деградировать после редакторских перестановок | Нужно проверить, что статья не начинается с taxonomy/boundary | Проверено: начало problem-first, boundary идёт после минимального примера. |

| Проверка | Результат P22 | Действие / свидетельство |
| --- | --- | --- |
| Первый экран problem-first | PASS | Вступление вводит объект, reader question and context-loss risk before taxonomy. |
| Служебные captions убраны | PASS | Workflow Map caption больше не содержит executor note. |
| Фигуры не раздувают статью | PASS | Новые фигуры не добавлены; существующие визуальные элементы оставлены по смысловым узлам. |
| Companion-файлы синхронизированы | PASS | Source usage, ledger, image plan, queue, open questions, theory links и readiness report обновлены. |

P22 readiness status: `ready_for_companion_sync_pass_with_public_structure_checked`.

## P23 — аудит синхронизации companion-файлов

| Проверка | Результат P23 | Действие / свидетельство |
| --- | --- | --- |
| Source usage соответствует статье | PASS | Строка Workflow Map обновлена; новые источники не добавлены. |
| Image plan и external queue синхронизированы | PASS | Текущий статус Workflow Map обновлён без устаревшей P12-формулировки. |
| Open questions очищены | PASS | Живые блокеры вынесены наверх; устаревшие редакторские вопросы P19–P22 закрыты или понижены до истории. |
| Нет generic C5/A10 pending | PASS | В open questions нет generic pending; остались только конкретные будущие cross-article проверки. |
| Ledger не раздут в coverage-бюрократию | PASS | P23 добавил только короткую таблицу синхронизации; тотальная coverage-матрица не добавлялась. |

P23 readiness status: `ready_for_style_defect_audit_with_companions_synced`.

## P24 — style defect audit

P24 проверял не полноту источников, а качество русской технической формы. Проход был selective: хорошие компактные формулы сохранены, source labels не русифицировались, а правились только реальные дефекты.

| Дефект | Почему исправлялся | Результат |
| --- | --- | --- |
| Псевдотермин «первичность артефактов» | Скрывал простую мысль за абстрактной конструкцией. | Заменено на прямое «артефакты имеют приоритет». |
| Театральные и машинные метафоры | Делали сбои BMAD звучащими как образ, а не как проверяемый механизм. | «театр», «красивая машина» и близкие обороты заменены на функциональные формулировки. |
| Неясное «контур» там, где речь о следующем этапе или участнике | Термин мог казаться отдельной методической сущностью. | Заменено на «этап», «участник процесса» или «следующий шаг» по месту. |
| Кальки и тяжёлые словосочетания | Увеличивали плотность без новой информации. | Исправлены точечно: «цена в токенах», «ложное ощущение полноты», «интерфейсы automator/UI». |
| Риск механического разворачивания | Тотальная правка могла бы ухудшить компактные технические места. | Сохранены имена файлов, команд, режимов и официальных BMAD labels. |

P24 readiness status: `ready_for_selective_natural_rewrite_with_style_defects_reduced`.

## P25 — selective natural rewrite audit

P25 продолжил P24, но не стал общим переписыванием статьи. Основные исправления:

| Участок | Правка | Зачем |
| --- | --- | --- |
| Инвариант BMAD | `working source of truth` заменён на «артефакт задаёт рамку работы» и «ведущий артефакт». | Убрать кальку без потери механизма смены артефактов. |
| Установка и восстановление | Заголовок установки стал конкретнее; таблица говорит «Файл или место». | Убрать искусственную «поверхность» там, где речь о файлах, каталогах и manifest. |
| Роли | Снят повторяющийся ритм `не X, а Y`; роли описаны через создаваемый артефакт или след работы. | Сделать раздел менее презентационным и более инженерным. |
| Enterprise/ревью/brownfield | Несколько фраз перестроены в прямой русский технический текст. | Сохранить различения без лозунговых противопоставлений. |
| Failure modes | «Инструментальная поверхность» заменена на «инструменты вокруг BMAD». | Уточнить, что быстро меняются команды, UI, bundles и конфигурация, а не абстрактная поверхность. |

P25 readiness status: `ready_for_next_pass_after_selective_natural_rewrite`.

## P26 — guarded final style audit

P26 был последним осторожным языковым проходом, а не переписыванием статьи. Он проверил ритм, переходы и русскую техническую фразу после P24–P25.

| Проверка | Результат |
| --- | --- |
| Псевдотермины не возвращены | PASS |
| Конкретика источников сохранена | PASS |
| Английские source labels сохранены только там, где они являются именами команд, файлов, статусов или источников | PASS |
| Переходы и заголовки стали естественнее без перестановки фактуры | PASS |
| Фигуры, таблицы, ссылки и boundary-блок не изменены по смыслу | PASS |

P26 readiness status: `ready_for_next_working_sheet_after_guarded_final_style`.
