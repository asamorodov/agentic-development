# TDAD Comparative — theory links

Статус: P01 theory links. Файл фиксирует смысловые обратные связи, а не простые навигационные ссылки.

| Theory area | What TDAD makes visible | Where article uses it | Boundary |
| --- | --- | --- | --- |
| A3 — спецификационные методологии | В первой линии поведенческая спецификация становится источником agent definition; тесты реализуют проверяемые срезы спецификации, но не заменяют её | Раздел «Линия 1» | Не превращать TDAD в общий SPDD/SDD-обзор |
| A7 — свидетельства / тестирование | Тестовый вывод становится свидетельством только при связи с обещанием изменения, происхождением и границами проверки | Раздел «Что считать свидетельством» | Не сводить свидетельства к «tests passed» |
| C3 — статус работы против пакета свидетельств | Во второй линии `completed` для патча требует не только diff, но impacted tests и понятный provenance eval/test signal | Разделы «Линия 2» и «Что считать свидетельством» | Не объявлять карту влияния полным статусом работы |
| A10 — карта выбора режима | TDAD нужен, когда проверочный контур должен появиться до агентского действия: компиляция agent definition, impacted tests, reproduction-test task | Раздел «Как TDAD связан с выбором режима работы» | A10 не превращать в decision matrix внутри статьи |
| C5 — concept-first atlas | Статья объясняет TDAD как самостоятельную методическую статью: reader question, mechanism, sources, technical surfaces, failures, theory return | Вся структура P01 | Не превращать статью в mini-theory or dossier summary |
| Теория полномочий / human gate | Passing score не снимает решения о выпуске агента или принятии патча | Ввод, failures, финал | Не подменять человеческое принятие benchmark-метрикой |
| Ремонт жизненного цикла | После изменения тестовый контур может устареть: spec, map, skill, hidden tests, eval scripts and artifacts need maintenance | В failures and A10 section | P01 только намечает; будущие passes могут усилить |

## Controlled repetition status

P01 осознанно повторяет из C5/A10 только локальный минимум: тест как управляющий контур, свидетельство против наблюдения, и необходимость human judgment. Статья не пересказывает весь SDLC-синтез. Техническая фактура сразу следует за повтором: `spec.yaml`, `visible/hidden tests`, `MutationSmith`, `.tdad/test_map.txt`, `grep`, impact weights, `EXP-026` / `EXP-028`, eval provenance.

## P02 boundary sync

| Boundary | Theory implication | Article control |
| --- | --- | --- |
| TDAD ≠ A7 | A7 remains the general observation/evidence chapter; TDAD is a method-family article about tests/examples as task-defining surfaces | Article now states this explicitly in contract section |
| TDAD ≠ Spec Kit/SPDD/Kiro/CSDD | Specification artifacts remain neighboring atlas articles; TDAD focuses on executable checks as specification-like surfaces | Boundary section cites external source links and avoids tutorial detail |
| TDAD ≠ CI/testing generally | General CI belongs to handbook/evidence layers; TDAD is about checks that shape agent work before/during action | Boundary section says benchmark pass does not equal acceptance |
| TDAD ≠ ADR/PWG | TDAD evidence may attach to ADR/PWG, but does not replace decision memory or durable work state | Negative boundary added without expanding ADR/PWG content |

## P04 theory sync — line 1

Line 1 now supports the atlas-level idea that an agent-facing specification becomes stronger when part of it is compiled into executable checks. The article should still not become a general specification article: `test_guidance` is included only because it explains how examples define expected agent behavior before `PromptSmith` optimizes the prompt/tool descriptions.

## P05 theory sync — line 2 practice

Line 2 now supports the theory link between evidence and working procedure: the benchmark result is not just a score, but a package of skill discovery, runtime context, selected tests, telemetry and provenance of eval files. This should connect to evidence/status chapters without duplicating Persistent Work Graph or handbook implementation material.

## P06 theory sync — scores and human framing

P06 strengthens the evidence theory connection: a score is a bounded observation until it is tied to source version, artifact path, selected tests, hidden/visible boundary and a human acceptance decision. This supports A7-style observation/evidence distinction without turning the TDAD article into an A7 rewrite.

## P07 theory sync — observation / evidence / acceptance

P07 makes the article's local evidence distinction explicit: observation is the raw test/benchmark signal, evidence is that signal bound to source/version/task, and acceptance is the human decision. This is a useful A7 connection, but later editing should keep the section TDAD-specific rather than making it a generic evidence chapter.

## P08 theory sync — anti-summary

P08 reinforces the theory boundary: external checks can discipline agent work, but they can also encode the wrong task, create score-chasing or become over-read as acceptance. This supports the atlas theme that evidence structures need owners and scope, not just automation.


## P09 theory sync — domain obligations

P09 strengthens the local theory link between executable checks and agent responsibility. The article now shows that the first TDAD line does not merely evaluate prompts on generic tasks: it encodes different operational obligations into testable branches. This helps the broader atlas theme that a specification becomes effective when it is bound to concrete evidence-producing surfaces, while staying inside the TDAD source material.

## P10 theory sync — article as atlas entry

P10 explicitly aligns the article with the C5 model for a concept-first technical atlas entry. The local reader path now starts from the controlled object, moves to the agent-facing surface, and ends at the human decision that the test signal can support. This strengthens the bridge back to theory without importing the full theory chapter into the article.

## P11 theory sync — visual evidence boundary

The inserted harness-types image makes the article's theory bridge visible: tests are a behavior-regulating surface, but evidence and acceptance also involve guides/specification, maintainability, architecture fitness and a human decision. This supports the A7-style evidence boundary while keeping the argument grounded in the TDAD article's local question.

## P12 theory sync — visual route through mechanisms

P12 clarifies which external figures serve the concept-first route: first-line figures show tests as a compilation and anti-gaming surface; second-line figures show tests as risk-routing through impact analysis; the TDFlow figure remains a contrast for tests as a repair task. The visual plan now mirrors the article's object → surface → decision path rather than adding images as a catalogue.

## P13 theory sync — no synthetic diagram

P13 keeps theory links in prose rather than adding an authorial diagram. This is intentional: the article's theoretical distinctions are already supported by the reader-route section, the evidence-boundary discussion and source-specific visual candidates. A synthetic scheme would be justified only if later pruning removes those supports.

## P14 theory sync — controlled repetition

The new glossary is controlled repetition in the C5 sense: it repeats only the minimal local vocabulary required for a reader to understand the TDAD comparison without assembling concepts from A7/C5 or neighboring atlas articles. It does not import a general theory framework into the article. The theory link remains: tests become useful evidence only when tied to provenance, version, task and human decision; TDAD is one concrete family where that evidence surface can also shape the agent's task.

## P15 theory sync — failure as mechanism, not generic testing

P15 strengthens the theory link by treating failure modes as reversals of the TDAD mechanism: the same executable surface that helps an agent act can encode the wrong task, narrow the oracle, leak into optimization, substitute benchmark score for understanding or produce passing examples without acceptance. This keeps the article inside concept-atlas scope. It does not become a general chapter on testing; the limits matter here because tests participate in the agent's task surface.

## P16 semantic back-links — what TDAD clarifies in the theory

| Theory fragment | Theoretical question clarified by TDAD | Article answer / backlink | Boundary control |
| --- | --- | --- | --- |
| `00_spine_map.md` | What lifecycle carrier preserves intent, checks and responsibility better than a chat session? | TDAD shows a case where tests move left from final verification into the carrier of agent work: they can shape an agent definition or route a patch before acceptance. | Do not claim tests replace decision memory, work state, environment or completion authority. |
| `A3_specification_methodologies_synthesis.md` | How can intent become manageable before an agent acts, and which artifact receives authority? | First-line TDAD is a specification-layer example where behavioral specs become executable examples, visible/hidden tests and mutation intents around an `agent definition`. | Keep SPDD/Spec Kit/Kiro as neighboring forms; TDAD's specificity is executable behavioral checking, not document workflow. |
| `A5_process_methodologies_synthesis.md` | When does a process artifact actually close a repeated gap rather than imitate process? | Second-line TDAD shows that “do TDD” is weak as ritual, while a concrete `code → tests` map can close the agent's missing context about regression risk. | Do not turn article into process handbook or universal testing procedure. |
| `A7_observation_vs_evidence.md` | When does a test/log/benchmark signal become evidence for human acceptance? | TDAD makes the distinction concrete: visible pass, hidden pass, mutation score, impacted-test output and eval JSON become evidence only with provenance, task link and uncovered-risk boundary. | Do not reduce A7 to test pass/fail; keep acceptance with a human owner. |
| `A9_lifecycle_repair.md` | What must be repaired after a successful change so the next agent does not inherit stale guidance? | TDAD adds repair targets: specs, visible/hidden tests, mutation packs, `.tdad/test_map.txt`, skills, benchmark runners and eval provenance. | Do not treat repair as a checklist; repair only the surface that became a future source of truth. |
| `A10_mode_selection_map.md` | When is extra external structure justified, and when is it overkill? | TDAD says: add a test-driven surface when the agent needs it before action—compiled behavior, impacted-test routing or reproduction-test task. For small visible reversible changes, ordinary tests and review may suffice. | Do not reproduce the A10 decision matrix inside the article. |
| `C5_theory_to_technical_atlas.md` | How should a concept-first atlas article return to theory without becoming a theory chapter? | The TDAD article returns via semantic questions—carrier, surface, evidence, repair, mode selection—while staying grounded in the two TDAD source lines. | Keep theory links as back-links; keep primary article driven by TDAD mechanisms and source artifacts. |

P16 main-text sync: the former `Как TDAD связан с выбором режима работы` section was rewritten as `Как TDAD возвращается в общую карту режима`. It now links TDAD to specification, process, evidence and repair questions without re-writing the full theory.

## P17 синхронизация теории — русская терминология

Языковая нормализация не меняет смысловые обратные связи. Она делает теоретическое возвращение статьи менее зависимым от английских связок: evidence→свидетельство, score→показатель, workflow→рабочий процесс, oracle→оракул проверки, eval file→файл оценки.

## P18 синхронизация теории — стиль

P18 не менял смысловые связи с A3/A5/A7/A9/A10/C5. Стилевые правки сделали теоретический возврат более прямым: вместо кальки про shift-left теперь используется формулировка о более раннем появлении проверочного контура в жизненном цикле.

## P19 синхронизация теории — редакторская структура

Смысловые back-links не изменились. Удаление нижнего asset-инвентаря делает основной текст более похожим на standalone concept-first article: теория теперь возвращается в финале статьи, а служебные визуальные решения остаются в companion-файлах.

## P20 синхронизация теории — визуальный шум убран

Смысловые back-links не изменились. Удаление пустых external placeholder-фигур усиливает concept-first чтение: теория и TDAD-механизмы теперь идут без служебных asset-разрывов. Локальный harness visual остаётся как поддержка границы свидетельства.

## P21 синхронизация теории — boundary visual clarified

Смысловые back-links не изменились. Подпись локальной harness-фигуры уточнена: она поддерживает общий theoretical boundary между тестовым сигналом и свидетельством, но не является source diagram для TDAD. Это снижает риск, что читатель примет соседний harness-visual за доказательство механики двух TDAD-линий.

## P22 синхронизация теории — entry before taxonomy

Смысловые back-links не изменились. P22 усилил порядок публичного чтения: сначала проблема теста как рабочей поверхности агента, затем reader question, затем taxonomy двух TDAD-линий. Это лучше соответствует concept-first связи с A3/A5/A7/A10: теория возвращается после механизма, а не открывает статью как boundary catalog.

## P23 синхронизация теории — no generic pending sync

C5/A10/A3/A7 links are already concrete in the article and companion table: intent carrier, mode selection, evidence boundary, repair target and concept-first return. P23 removes the need for any generic theory-sync debt. Future theory work must name the specific article problem it solves.

## P24 синхронизация теории — style without semantic change

Смысловые back-links не изменились. P24 убрал несколько модельных словосочетаний из основного текста, чтобы связь с теорией читалась через конкретные решения: что получает агент, какие проверки выбраны, какой след поддерживает принятие и где нужен контроль человека. Теоретические роли TDAD — носитель намерения, выбор режима, свидетельство, repair target — сохранены.

## P25 синхронизация теории — headings naturalized

Смысловые back-links не изменились. Основной теоретический раздел теперь называется `Что TDAD добавляет к общей карте режимов`, что точнее описывает его функцию: TDAD не пересказывает карту режима, а добавляет к ней конкретные случаи, где внешний проверочный артефакт оправдан. P25 also made the process-layer wording less abstract by saying directly that extra artifacts are useful only where intent, needed checks or completion authority would otherwise be lost.

## P26 синхронизация теории — final style guard

Смысловые back-links не изменились. P26 снизил долю метафорического словаря в словаре статьи и theory-return section, но сохранил теоретические тезисы: TDAD проясняет, когда исполняемая тестовая поверхность становится носителем намерения, когда оправдана дополнительная внешняя структура и когда тестовый результат становится свидетельством только вместе с provenance и человеческим принятием.
