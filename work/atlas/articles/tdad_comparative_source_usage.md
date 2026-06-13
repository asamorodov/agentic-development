# TDAD Comparative — source usage

Статус: companion-файл P01. Заполнен как рабочий журнал использования источников в первичном черновике. Источники перечислены не как полное покрытие досье, а как provenance для фактов, которые уже перенесены в основной текст.

| Источник | Роль в статье | Где использован | Почему нужен | Оговорки / долги |
| --- | --- | --- | --- | --- |
| [Test-Driven AI Agent Definition](https://arxiv.org/abs/2603.08806) | Первоисточник первой TDAD-линии | Вводная развилка; раздел о компиляции agent definition; заявленные метрики | Даёт центральную идею: поведенческая спецификация, видимые/скрытые тесты, мутации и эволюция спецификаций как контур сборки агента | На будущих проходах сверить полную версию, определения метрик и фигуры по PDF/HTML |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Детальная техническая база первой линии | YAML-спецификация, `TestSmith`, `PromptSmith`, `MutationSmith`, `respond`, `visible/hidden tests`, SURS/RPR, SpecSuite-Core | Нужна для технической плотности: поля спецификации, доступ к тестам, мутационные проверки, структурированный ответ | Нужно проверить права и качество фигур; часть конфликтов README/dataset остаётся open question |
| [f-labs-io/tdad-paper-code](https://github.com/f-labs-io/tdad-paper-code) | Референсный репозиторий первой линии | Файловая поверхность, README-команды, артефакты `specs`, `tests_visible`, `tests_hidden`, `mutation_packs`, `agent_artifacts` | Показывает, как метод воплощён в файлах и Docker-пайплайне | Нужна свежая проверка актуального README, коммитов и `results/` перед финальным текстом |
| [raw README tdad-paper-code](https://raw.githubusercontent.com/f-labs-io/tdad-paper-code/main/README.md) | Точный README-слой первой линии | Команды, Docker-тома, эволюция v1→v2, конфликт вокруг `M_ALWAYS_TICKET` | Нужен для source-specific ограничений среды и версии README | Есть конфликт между raw/отрендеренным/dataset-слоями; не использовать спорный процент без проверки хэша |
| [SpecSuite-Core](https://huggingface.co/datasets/f-labs-io/SpecSuite-Core) | Dataset-слой первой линии | `specs`, `mutations`, `results`, 8 спецификаций, 27 mutation intents, 24 запуска | Разделяет спецификацию, мутационные намерения и результаты пайплайна | Будущий проход должен открыть строки dataset, если нужны точные примеры |
| [Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973) | Первоисточник второй TDAD-линии | Вводная развилка; проблема регрессий; заявленный результат 70% снижения regression rate; TDD Prompting Paradox | Даёт центральную идею: code-test graph и impacted tests как рабочий контекст агента | Числа использовать только рядом с условиями эксперимента |
| [HTML-версия Test-Driven Agentic Development](https://arxiv.org/html/2603.17973v2) | Детальная техническая база второй линии | Граф, узлы/рёбра, AST Parser, Test Linker, веса impact analysis, Phase 1/2, ограничения | Нужна для технической плотности метода и границ применимости | Нужна проверка фигур и, возможно, кодовой реализации перед финалом |
| [pepealonso95/TDAD](https://github.com/pepealonso95/TDAD) | Репозиторий второй линии | Общий слой реализации, history/experiments context, NetworkX/Neo4j | Показывает эволюцию репозитория и упаковку метода | Не использовать как единственный источник чисел без `EXPERIMENTS.md` / eval paths |
| [EXPERIMENTS.md TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/EXPERIMENTS.md) | Журнал экспериментов второй линии | `EXP-021j/k/l`, `EXP-024`, `EXP-026`, `EXP-027`, `EXP-028` | Нужен для реальных сбоев: устаревший eval JSON, opencode/MLX, Neo4j failure, NetworkX repair | Будущий проход должен открыть конкретные `report.json`, `progress.log`, eval JSON, если они будут использоваться как доказательства отдельных запусков |
| [run_benchmark.py TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/claudecode_n_codex_swebench/run_benchmark.py) | Воспроизводимость и поля телеметрии второй линии | В P01 упомянут только косвенно через досье; пока не вынесен в основной текст как самостоятельная опора | Полезен для будущего P05/P06 по телеметрии `graph_guard`, `tdd_evidence_complete`, `progress.log` | В P01 не раскрыт подробно; оставить для source-depth проходов |
| [tdad-skill](https://github.com/pepealonso95/tdad-skill) | Рабочая упаковка второй линии | Команды `tdad index`, `tdad impact`, `tdad run-tests`, языковые плагины, NetworkX/Neo4j | Показывает, как research-method стал agent skill / CLI | Нужно отличать опубликованный skill от короткого runtime skill на уровне статьи |
| [tdad-skill SKILL.md](https://github.com/pepealonso95/tdad-skill/blob/main/SKILL.md) | Минимальная агентская инструкция второй линии | `.tdad/test_map.txt`, `grep`, обязательный новый тест, fallback при отсутствии записи | Показывает, какую задачу реально получает агент во время патча | Проверить актуальную форму SKILL.md перед финальным текстом |
| [TDFlow](https://arxiv.org/abs/2510.23761) | Соседний контрастный источник | Раздел о тесте как задаче для workflow | Помогает не расширять TDAD до всех test-driven workflows | Не использовать как подтверждение фактов о двух TDAD-линиях |
| [HTML-версия TDFlow](https://ar5iv.org/html/2510.23761v2) | Детали соседнего контраста | `reproduction tests`, `Explore Files`, `Revise Patch`, `Debug One`, test hacking, limits | Даёт проверочную линзу для test hacking и качества reproduction tests | Должен оставаться контрастом, а не третьей равноправной TDAD-линией |

## P02 boundary sources added

| Источник | Роль в статье | Где использован | Почему нужен | Оговорки / долги |
| --- | --- | --- | --- | --- |
| [Spec Kit](https://github.github.com/spec-kit/) | Соседняя спецификационная методология | `Контракт статьи` | Показывает границу: Markdown-цепочка `spec → plan → tasks → implement`, а не TDAD-тесты как surface задания | Не раскрывать Spec Kit подробно в TDAD article |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) and [OpenSPDD](https://github.com/gszhangwei/open-spdd) | Соседний SPDD / structured prompt method | `Контракт статьи` | Показывает границу с prompt/Canvas как артефактом намерения | TDAD не должен дублировать SPDD article |
| [Kiro Feature Specs](https://kiro.dev/docs/specs/feature-specs/) | Соседняя продуктовая спецификационная поверхность | `Контракт статьи` | Показывает границу с IDE/Web/CLI specs workflow | Не раскрывать Kiro UI/details здесь |
| [Constitutional SDD](https://arxiv.org/abs/2602.02584) | Соседний rule/constitution-driven specification layer | `Контракт статьи` | Показывает границу с Constitution and traceability as spec constraints | Не превращать TDAD в security/compliance SDD article |

## P03 dossier inventory update

P03 did not add new public sources and did not cite the internal dossier in the article. The inventory confirms that current article citations still point to public/readable sources rather than to the dossier itself. The dossier remains a transfer buffer, not a citation target.

| Source / source layer | P03 usage decision | Main-text status | Follow-up before final |
| --- | --- | --- | --- |
| TDAD comparative dossier | Used only as inventory input | Not cited in article | Keep as internal buffer; do not use as public provenance |
| `arXiv/html 2603.08806` + `tdad-paper-code` + `SpecSuite-Core` | Sufficient for current first-line mechanism | Already used for `agent definition`, `spec.yaml`, visible/hidden tests, mutation/evolution, dataset separation | Reopen primary source rows/assets before strengthening metrics or mutation examples |
| `arXiv/html 2603.17973` + `pepealonso95/TDAD` + `tdad-skill` | Sufficient for current second-line mechanism | Already used for graph, `test_map.txt`, skill, impact analysis, benchmark caveats | Reopen exact runtime/eval artifacts if `EXP-*` episodes remain major evidence anchors |
| `run_benchmark.py TDAD` | Confirmed as future technical support, not yet a full article source | Only indirect/provenance role in current text | Use only if adding concrete telemetry fields such as `graph_guard_passed` or `tdd_evidence_complete` |
| TDAD commit history | Keep as versioning/provenance context | Not needed in main article yet | Use only to disambiguate evaluated artifact vs later published skill/backend |
| GitHub Issues/PR absence | Keep as negative provenance note | Not needed in main article | Do not convert absence into a method claim |
| TDFlow HTML/PDF | Remains neighboring contrast | Already used only to distinguish test-as-task workflow | Keep optional; avoid making it a third equal TDAD line |
| Image-source candidates | Confirmed as candidates only | Inline placeholders and image plan | Asset-pass must verify rights, quality, exact figure identity and local paths |

P03 source posture: current article may proceed without a main-text expansion. The next useful source-depth work is not broad search; it is narrow artifact verification: dataset rows, run JSON/eval JSON, exact skill version, and figure assets.

## P04 source-depth update — first TDAD line

| Источник | P04 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Уточнение механизма, где примеры и `test_guidance` переводят неоднозначную политику в исполняемые проверки | Раздел «Линия 1», абзац про `test_guidance`; абзац про `MFT` / `INV` / `DIR` and `canary values` | Не превращать в implementation appendix; использовать только как support for concept-first claim |
| [tdad-paper-code](https://github.com/f-labs-io/tdad-paper-code) | Поддерживает файловую форму `spec.yaml` and generated tests already present | Context unchanged | No new repository claims in P04 |

P04 did not open or add external sources beyond the already recorded public/readable source layer. The added article material is sourced to the first-line HTML article and existing repository source where relevant.

## P05 source-depth update — second TDAD line

| Источник | P05 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [tdad-skill](https://github.com/pepealonso95/tdad-skill) and [SKILL.md](https://github.com/pepealonso95/tdad-skill/blob/main/SKILL.md) | Practical packaging of line 2 | Added distinction between paper-minimal runtime skill and published portable skill | Do not attach article benchmark numbers to later packaging without version evidence |
| [HTML-версия Test-Driven Agentic Development](https://arxiv.org/html/2603.17973v2) | Auto-improvement loop and benchmark-practice details | Added 15-iteration improvement loop, 4 kept changes, 11 reverts, static `test_map.txt` change | Treat as source-reported experiment; not independently verified |
| [EXPERIMENTS.md TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/EXPERIMENTS.md) | Engineering iteration from `EXP-026` to `EXP-028`; packaging failure and recovery | Already used, now tied more explicitly to practice | Raw artifacts still needed for instance-level claims |
| [run_benchmark.py TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/claudecode_n_codex_swebench/run_benchmark.py) | Telemetry source for benchmark practice beyond final `resolved` | Now used directly in main text for fields such as `graph_guard_passed` and `tdd_evidence_complete` | Reopen raw file before final if fields remain in article |

P05 did not add broad secondary sources. It promoted already recorded line-2 source layers into a tighter engineering-practice explanation.

## P06 source-depth update — score interpretation

| Источник | P06 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) and [SpecSuite-Core](https://huggingface.co/datasets/f-labs-io/SpecSuite-Core) | Metric interpretation for first line | New section `Как читать score` | Exact dataset rows still need final verification if examples become concrete |
| [tdad-paper-code](https://github.com/f-labs-io/tdad-paper-code) | Provenance warning around `mutation_score` conflict | New section `Как читать score` | Do not use disputed mutation example as stable result without commit/run evidence |
| [HTML-версия Test-Driven Agentic Development](https://arxiv.org/html/2603.17973v2) and [tdad-skill](https://github.com/pepealonso95/tdad-skill) | Defines how to read `resolution`, `regression`, `generation` together | New section `Как читать score` | Keep model/task/benchmark conditions attached to numbers |
| [EXPERIMENTS.md TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/EXPERIMENTS.md) and [run_benchmark.py TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/claudecode_n_codex_swebench/run_benchmark.py) | Eval provenance and telemetry interpretation | New section `Как читать score` | Raw artifacts remain a readiness debt |

P06 did not add new sources; it reinterpreted existing result sources through the article's human-acceptance boundary.

## P07 source-depth update — human decision boundary

| Источник | P07 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Human gates for first-line verification | `Где человек решает` | The section summarizes decision points; it should not become a process checklist |
| [tdad-skill SKILL.md](https://github.com/pepealonso95/tdad-skill/blob/main/SKILL.md) | Fallback and map-related human decision points | `Где человек решает` | Verify current SKILL.md before final if fallback wording remains exact |
| [EXPERIMENTS.md TDAD](https://raw.githubusercontent.com/pepealonso95/TDAD/main/EXPERIMENTS.md) | Eval provenance as human acceptance precondition | `Где человек решает` | Raw eval artifacts still pending |
| [HTML-версия TDFlow](https://ar5iv.org/html/2510.23761v2) | Contrast for tests-as-task and incorrect reproduction-test risk | `Где человек решает` | Keep as contrast only |

P07 did not add external sources; it clarified the verification boundary using already recorded sources.

## P08 source-depth update — failure anti-summary

| Источник | P08 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Supports wrong-specification and optimization-to-visible-check boundary | `Где граница ломается` anti-summary | Keep source-specific; do not universalize beyond described protocol |
| [Test-Driven Agentic Development](https://arxiv.org/abs/2603.17973) | Supports TDD Prompting Paradox as failure of procedure without target context | `Где граница ломается` anti-summary | Article should keep exact benchmark caveats nearby |
| [HTML-версия TDFlow](https://ar5iv.org/html/2510.23761v2) | Contrast for wrong reproduction tests and test hacking | `Где граница ломается` anti-summary | Contrast only; not evidence for two TDAD lines |

P08 did not add new sources; it condensed existing failure evidence into an anti-summary.


## P09 source update — SpecSuite domain specificity

| Источник | P09 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Доменные обязанности `SupportOps`, `DataInsights`, `IncidentRunbook`, `ExpenseGuard` | Раздел «Линия 1», после абзаца о SpecSuite-Core | Использовано как механизм статьи: что именно тест становится способен задавать агенту. Перед финалом стоит сверить отдельные формулировки с исходными спецификациями / generated tests, если они будут цитироваться подробнее |

P09 did not introduce a new source family. It made an already-used source more source-specific by showing that SpecSuite-Core is not just four labels, but four different kinds of agent obligation encoded into tests.

## P10 source update — reader path / article model

| Источник | P10 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| `C5_theory_to_technical_atlas.md` | Internal structural guide for concept-first atlas articles: pressure → mechanism → technical surfaces → evidence/limits → theory return | New section `Читательский маршрут: объект, поверхность, решение` | Used only as article-structure guidance, not as a public evidence source for TDAD claims |
| Existing TDAD and TDFlow sources | Reused factual anchors for the three surfaces: compiled behavior, impacted-test route, reproduction-test task | New reader-route section | No new factual claims beyond already-used source families |

P10 adds no new external TDAD source. It improves reader path by making the article's conceptual sequence explicit before the detailed comparison.

## P11 source update — local visual asset

| Источник | P11 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| `content/assets/theory-images/fowler-harness-types.png`, from Martin Fowler, `Harness engineering for coding agent users` as recorded in local asset manifest | Local visual boundary for tests as one sensor/regulatory surface inside a broader harness | Inserted as `fig-harness-types-verification-boundary` in `Что считать свидетельством, а что только наблюдением` | Used as conceptual boundary image, not as evidence for TDAD paper results. If source-specific TDAD figures are localized later, this image may become optional |
| Local asset catalog / manifest | Confirms local path, source and prior intended use of asset | Image plan and article figure | Publication still needs rights/licensing check for external-source images stored locally |

P11 adds a local image asset, not a new TDAD factual source. The image supports the article's evidence boundary: tests matter, but they are not the whole harness or whole acceptance decision.

## P12 source update — external real image candidates

| Источник | P12 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| [HTML-версия Test-Driven AI Agent Definition](https://arxiv.org/html/2603.08806v1) | Verified external figure candidates: TDAD overview and semantic mutation testing pipeline | Captions for `fig-tdad-definition-overview` and `fig-tdad-definition-mutation` rewritten as public captions | Figures remain not downloaded; rights/quality check pending |
| [tdad-paper-code](https://github.com/f-labs-io/tdad-paper-code) | External repo/source-tree visual candidate for first-line file separation | Caption for `fig-tdad-definition-repo-tree` rewritten | May become a screenshot of source tree or may be replaced by local code excerpt if no clean visual is suitable |
| [HTML-версия Test-Driven Agentic Development](https://arxiv.org/html/2603.17973v2) | Verified external figure candidates: workflow/pipeline and P2P failures | Captions for `fig-tdad-development-pipeline` and `fig-tdad-development-p2p-failures` rewritten | Figures remain not downloaded; choose between workflow fig 1 and pipeline fig 2 during actual asset localization |
| [tdad-skill](https://github.com/pepealonso95/tdad-skill) and [TDAD repo](https://github.com/pepealonso95/TDAD) | External source screenshot / source-fragment candidate for `.tdad/test_map.txt`, ASCII pipeline or CLI output | Caption for `fig-tdad-development-test-map` rewritten | Use only if actual source visual or screenshot is readable; otherwise keep code block and remove placeholder |
| [HTML-версия TDFlow](https://arxiv.org/html/2510.23761v1) | Verified contrast figure candidate for reproduction-test workflow | Caption for `fig-tdflow-reproduction-tests` rewritten | Contrast only; not evidence for TDAD lines |

P12 did not download images. It converted existing candidate placeholders into public-facing figure captions and recorded dispositions for all dossier image candidates.

## P13 source update — synthetic figures

P13 added no source and no synthetic figure. Existing source usage remains unchanged. The pass considered an authorial comparison diagram for `объект → поверхность → решение` and `test as specification / route / task`, but deferred it because the article already has an early comparison table, a reader-route section, multiple TDAD source-figure candidates and the local harness boundary image.

## P14 source update — standalone glossary

| Источник | P14 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| `C5_concept_atlas_article_map.md` and `C5_theory_to_technical_atlas.md` | Structural guidance for a standalone concept-first atlas article | New section `Минимальный словарь статьи` | Used as internal article-model guidance, not as public evidence for TDAD claims |
| Existing first-line TDAD sources | Local definitions of `agent definition`, `visible tests`, `hidden tests`, `mutation intent` | New glossary section before the quick split | No new factual source added; later source pass may verify exact English terms against the papers |
| Existing second-line TDAD sources | Local definition of `test map` as agent-facing working surface | New glossary section before the quick split | Keep distinction between paper-minimal map and published `tdad-skill` later in the article |

P14 adds no new external TDAD source. It uses C5 only to strengthen standalone readability and turns already-used TDAD terms into a local vocabulary for the article.

## P15 source update — mechanism and failure boundaries

| Источник | P15 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| Existing first-line TDAD sources | Support wrong-task, hidden/visible boundary, leakage/overfitting and benchmark-as-training-surface explanation | Replaced the old failure catalog with `Как управляющий тестовый контур даёт сбой` | No new source family; claims remain tied to already-cited paper/dataset layers |
| Existing second-line TDAD sources | Support narrow oracle, stale/partial map and packaging failure explanation | Same section | Keep exact static-analysis limitations and experiment labels source-bound |
| Existing TDFlow contrast source | Supports reproduction-test wrong-task risk and test-hacking lens | Same section | Contrast only; not evidence for the two TDAD lines |

P15 adds no new external source. It changes the function of the failure material: risks are now explained as failure modes of the same mechanism that makes TDAD useful, not as a generic testing-risk list.

## P16 source update — theory back-links

| Internal source | P16 role | Где добавлен / уточнён | Оговорка |
| --- | --- | --- | --- |
| `00_spine_map.md` | Lifecycle carrier and human responsibility frame | Theory-links semantic table; main section on general mode map | Internal theory source, not public TDAD evidence |
| `A3_specification_methodologies_synthesis.md` | Specification-layer question: what artifact governs before action | Theory-links semantic table; main section paragraph on first-line TDAD | Do not import SPDD/Spec Kit detail into article |
| `A5_process_methodologies_synthesis.md` | Process artifact vs ritual distinction | Theory-links semantic table; main section paragraph on second-line TDAD | Keep TDAD as concept article, not process handbook |
| `A7_observation_vs_evidence.md` | Observation/evidence/acceptance distinction | Theory-links semantic table | Existing TDAD sections already carry the local version |
| `A9_lifecycle_repair.md` | Repair of stale future guidance | Theory-links semantic table; main section paragraph on repair targets | Do not expand into general lifecycle repair chapter |
| `A10_mode_selection_map.md` | When to add external structure vs keep light mode | Theory-links semantic table; main section mode language | Avoid reproducing decision matrix |
| `C5_theory_to_technical_atlas.md` | Concept-first article/back-link model | Theory-links semantic table | Used as structural guidance only |

P16 adds internal semantic back-links, not new TDAD factual sources.

## P17 обновление источников — языковой проход 1

Новых фактических источников нет. Языковой проход нормализовал русскую прозу и сохранил английский только там, где он закреплён источником: в названиях статей, файлах, командах, метриках и идентификаторах артефактов. Основной текст теперь использует русские связки для бенчмарка, происхождения, свидетельств, рабочего процесса и принятия, не меняя точные source labels и команды.

## P18 обновление источников — языковой проход 2

Новых фактических источников нет. P18 вычитал заголовки, подписи, таблицу сравнения и нижний блок внешних изображений. Source-specific names, команды, пути, метрики и названия репозиториев сохранены; русская связность улучшена без изменения provenance.

## P19 обновление источников — редакторский проход 1

Новых источников нет. Редакторский проход не менял фактические утверждения, ссылки, метрики или provenance. Нижний инвентарный блок внешних изображений удалён из основного текста как publication-noise; его содержание уже сохранено в image_plan и external_image_queue.

## P20 обновление источников — редакторский проход 2

Новых источников нет. P20 не менял фактические утверждения, ссылки, метрики или происхождение материалов. Из основного текста удалены пустые внешние `<figure>`-заготовки без локального изображения; их содержание и статусы остаются в `image_plan` и `external_image_queue`.

## P21 обновление источников — визуальный provenance и редакторская согласованность

Новых источников нет. P21 не добавлял фактических утверждений и не менял ссылки TDAD. Изменение в статье касается только подписи локальной harness-фигуры: теперь она явно названа граничной иллюстрацией, а не источником фактов для двух TDAD-линий. P21 companion-only visual status was superseded by P22: четыре external TDAD-кандидата снова inline как `external-real-candidate`, остальные queue-only/optional.

## P22 обновление источников — public entry и visual protocol

Новых внешних фактических источников нет. P22 использовал внутреннее правило `protocols/rules/visual-assets-and-figures.md` как редакционный visual-governance input, а не как источник TDAD claims. Основной текст получил problem-first opening, но источниковые утверждения о двух TDAD-линиях не менялись. Четыре уже зарегистрированных external real image candidates возвращены inline как `external-real-candidate`; нижний раздел asset-pass восстановлен. Captions переписаны как публичные подписи без executor notes.

## P23 обновление источников — companion sync

Новых источников нет. P23 только синхронизировал companion state с текущей статьёй: P21 visual companion-only note marked as superseded by P22, active source blockers свернуты в open_questions. Source usage remains source-of-record for factual claims; no Generic theory sync item remains.

## P24 обновление источников — стилевой аудит

Новых источников нет. P24 менял только язык основного текста, подписи и нижнего asset-раздела: source-specific названия, ссылки, числа, команды, метрики, пути и figure IDs сохранены. Уточнения вроде замены `человеческого обрамления`, `runtime-инструкции`, `CLI-поверхности` и `leaderboard` не меняют provenance; они делают уже перенесённые claims читаемыми по-русски.

## P25 обновление источников — selective natural rewrite

Новых источников нет. P25 выборочно переписал неестественные русские связки и заголовки, найденные после P24: `Читательский вопрос` → главный вопрос, `методические семьи` → варианты практики, `поведенческая оболочка` → конкретные входы и проверки, `TDAD-контракт` → условия независимого свидетельства. Source-specific labels, citations, metrics, commands and artifact names preserved.

## P26 обновление источников — guarded final style

Новых источников нет. P26 выровнял русский тон и убрал оставшиеся англо-русские и служебные формулировки в пользовательской части, включая нижнюю таблицу визуальных кандидатов. Английский сохранён только там, где это название статьи, репозитория, команда, путь, метрика, поле, ID рисунка или устойчивая метка проекта. Ссылки, метрики, команды и provenance-утверждения не менялись.
