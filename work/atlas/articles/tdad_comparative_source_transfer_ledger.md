# TDAD Comparative — source transfer ledger

Статус: P01 ledger. Это журнал реальных переносов и сознательных отложений. Он не является coverage matrix и не доказывает полный обход досье.

| Материал / тезис | Источник | Решение P01 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| TDAD нельзя переносить как один метод: две линии используют одну аббревиатуру | TDAD comparative dossier → arXiv 2603.08806; arXiv 2603.17973 | Перенесено | Вводная развилка; сравнительная таблица | Центральная ось статьи |
| Первая линия компилирует `agent definition` из поведенческой спецификации и тестов | arXiv 2603.08806; HTML 2603.08806v1; tdad-paper-code | Перенесено | Раздел «Линия 1» | Раскрыто через `spec.yaml`, `TestSmith`, `PromptSmith`, `visible/hidden tests` |
| `PromptSmith` меняет не только prompt, но и описания инструментов | HTML 2603.08806v1 | Перенесено | Раздел «Линия 1» | Важно для тезиса, что `agent definition` шире system prompt |
| `respond` как структурированный контракт ответа | HTML 2603.08806v1 | Перенесено | Раздел «Линия 1» | Использовано как технический anchor детерминируемой проверки |
| Файловая структура первой линии (`specs`, `tests_visible`, `tests_hidden`, `mutation_packs`, `agent_artifacts`) | tdad-paper-code | Перенесено | Файловый блок в разделе «Линия 1» | Фигура repo-tree создана как external-real-candidate |
| Docker-тома и необходимость `build` / `init-volumes` после локальных изменений | raw README tdad-paper-code | Перенесено | Раздел «Линия 1» | Нужна будущая свежая проверка README |
| SpecSuite-Core как глубокий набор спецификаций, мутаций и результатов | HTML 2603.08806v1; HuggingFace SpecSuite-Core | Перенесено | Раздел «Линия 1» | Точные строки dataset пока не открывались в P01 |
| Заявленные числа первой линии | arXiv 2603.08806 | Перенесено осторожно | Раздел «Линия 1» | Явно помечены как заявленные результаты источника |
| Конфликт `ALWAYS_CREATE_TICKET` / `M_ALWAYS_TICKET` | raw README; GitHub README; HuggingFace dataset | Перенесено как warning | Раздел «Линия 1»; open questions | Не использовать как стабильный процент до проверки хэша/JSON |
| Вторая линия строит graph code-test impact и runtime `test_map.txt` | arXiv 2603.17973; HTML 2603.17973v2; tdad-skill | Перенесено | Раздел «Линия 2» | Центральный механизм второй линии |
| Графовые узлы/рёбра и AST/Test Linker pipeline | HTML 2603.17973v2 | Перенесено | Раздел «Линия 2» | Фигура pipeline создана как external-real-candidate |
| Runtime минимален: `test_map.txt` + `SKILL.md`, `grep` и `pytest` | HTML 2603.17973v2; tdad-skill SKILL.md | Перенесено | Раздел «Линия 2» | Связано с тезисом о маленьком рабочем контексте агента |
| CLI-команды `tdad index`, `tdad impact`, `tdad run-tests`, `tdad stats` | tdad-skill README | Перенесено частично | Раздел «Линия 2» | Уточнить актуальные команды на будущих проходах |
| Impact weights Direct/Coverage/Transitive/Imports | HTML 2603.17973v2; tdad-skill README | Перенесено | Раздел «Линия 2» | Использовано для объяснения эвристичности карты |
| Phase 1 / Phase 2 числа второй линии | HTML 2603.17973v2 | Перенесено осторожно | Раздел «Линия 2» | Рядом сохранены `resolution rate` и `generation rate` |
| `EXP-026` как отрицательный пример Neo4j skill | EXPERIMENTS.md TDAD | Перенесено | Раздел «Линия 2» и «Где граница ломается» | Важно для тезиса об упаковке рабочего сигнала |
| `EXP-028` как исправление через NetworkX и статический export | EXPERIMENTS.md TDAD | Перенесено | Раздел «Линия 2» | Нужны raw artifacts для углубления на source-depth pass |
| `EXP-021j/k/l` как provenance eval JSON | EXPERIMENTS.md TDAD | Перенесено | Раздел «Линия 2» | Точные файлы eval пока не открывались |
| `EXP-024` MLX/opencode tool_calls issue | EXPERIMENTS.md TDAD | Перенесено кратко | Раздел «Где граница ломается» через summary | Может быть расширено в P06 |
| TDD Prompting Paradox | arXiv 2603.17973; HTML 2603.17973v2 | Перенесено | Раздел «Линия 2» и failures | Важно для анти-лозунга «попросите агента делать TDD» |
| TDFlow как соседний тестовый workflow | TDFlow arXiv; HTML TDFlow | Перенесено как контраст | Раздел «Тест как спецификация, маршрут, задача» | Не использовать как факт о TDAD; визуал поставлен как optional contrast |
| Все кандидаты на изображения из досье | Dossier image candidates | Перенесено в image_plan / article placeholders | См. article bottom и image_plan | Права/качество/скачивание не выполнялись в P01 |
| run_benchmark.py telemetry fields | run_benchmark.py TDAD | Отложено | source_usage only | Добавить в P05/P06, если нужен слой телеметрии |
| Commit history второй линии | TDAD commit history | Отложено | open questions / source_usage context | P01 не использует коммиты в основной прозе, чтобы не перегружать draft |

## P02 contract and boundary transfers

| Материал / тезис | Источник | Решение P02 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| TDAD ≠ A7: A7 про observation/evidence generally; TDAD про methods where tests/examples define agent work | P02 worksheet; C5/A10 context | Перенесено как article contract | `Контракт статьи` | A7 source file itself не был разрешён P02; формулировка держится на рабочем листе и C5/A10 context |
| TDAD ≠ Spec Kit / SPDD / Kiro / Constitutional SDD | Neighbor dossiers and external source links | Перенесено | `Контракт статьи` | Boundary added to prevent article duplication |
| TDAD ≠ CI/testing generally; benchmark pass ≠ acceptance | P02 worksheet; TDAD dossier | Перенесено | `Контракт статьи` | Reinforces central thesis and negative boundary |
| TDAD ≠ ADR / PWG | ADR dossier; PWG dossier; C5 map | Перенесено as negative boundary | `Контракт статьи` | No detailed ADR/PWG facts added beyond boundary statement |

## P03 dossier inventory — transfer state

P03 не добавлял новые факты в основной текст: явного article-critical пропуска после сверки с досье не найдено. Основной черновик уже держит две TDAD-линии, разные объекты управления, ключевые артефакты, границы тестового свидетельства и основные режимы сбоя. Ниже — рабочий inventory для следующих проходов; это не тотальная матрица покрытия.

### Уже перенесено достаточно для основного аргумента

| Материал / тезис | Источник в досье | Состояние в статье | Следующее действие |
| --- | --- | --- | --- |
| Аббревиатура `TDAD` закрывает две разные линии, а не один метод | Ввод и сравнительная развилка досье | Перенесено во ввод, развилку и итог | Сохранять как композиционный стержень |
| Первая линия: `agent definition` как компилируемый артефакт из `spec.yaml`, видимых/скрытых тестов, `TestSmith`, `PromptSmith`, `MutationSmith`, `respond` и файловой структуры репозитория | Разделы Line 1 / Artifacts | Перенесено; статья не сводит артефакт к одному `system prompt` | На source-depth pass сверить формулировки по первоисточникам и изображениям |
| Первая линия: SpecSuite-Core, домены, v1/v2, SURS/RPR, заявленные числа и осторожность к `mutation score` | Разделы о SpecSuite-Core, metrics, mutation conflict | Перенесено как осторожный source claim, без превращения чисел в общий вывод | Не усиливать без открытия точных dataset/run rows |
| Конфликт `ALWAYS_CREATE_TICKET` / `M_ALWAYS_TICKET` | Lines about raw/rendered README/HF conflict | Перенесено как provenance-warning, не как stable result | Требуется hash/JSON before stronger claim |
| Вторая линия: code-test graph, `AST Parser`, `Graph Builder`, `Test Linker`, `Impact Analyzer`, `.tdad/test_map.txt`, `SKILL.md`, `grep`, `pytest` | Line 2 workflow/artifacts | Перенесено в технический раздел и практическую форму различения | На source-depth pass добавить только если нужно больше телеметрии, не перегружать основной ход |
| Impact weights, Phase 1/Phase 2, TDD Prompting Paradox, статические ограничения графа | Detailed Line 2 sections | Перенесено с оговорками про модели, знаменатели и эвристики | Сохранять рядом с ограничениями, не выносить как slogan |
| `EXP-026`, `EXP-028`, stale eval JSON / `EXP-021j` | EXPERIMENTS.md-derived dossier blocks | Перенесено как failure/provenance anchors | Перед финалом проверить raw artifacts, если эти эпизоды останутся сильными опорами |
| TDFlow как соседний режим, где tests are the task | TDFlow contrast block | Перенесено как контраст, не как третья TDAD-линия | Следить, чтобы опциональная фигура не размывала фокус |
| Кандидаты на изображения | Dossier image candidates | Перенесены в image plan and article placeholders | Asset-pass: права, качество, локальные файлы, final placement |

### Неперенесённое, но не критичное для текущего черновика

| Материал | Почему отложен | Куда может перейти |
| --- | --- | --- |
| Детальные доменные описания `SupportOps`, `DataInsights`, `IncidentRunbook`, `ExpenseGuard` | Основной текст уже использует домены как технический anchor; длинный список политик утяжелит статью | Source-depth appendix/footnote-like paragraph only if article needs more concreteness |
| Полный перечень телеметрических полей `run_benchmark.py`: `graph_guard_passed`, `indexed_search_success`, `impacted_selected_count`, `tdd_evidence_complete`, `f2p_runtime_strategy`, `p2p_runtime_unreliable_reason` | Главная статья уже показывает provenance eval-сигнала; полный список может стать handbook/debug материалом | Раздел о свидетельствах, если будущий pass потребует deeper evidence surface |
| Commit history второй линии (`EXP-001`, `EXP-028`, skill update, NetworkX backend) | Помогает не смешивать стадии метода, но в статье сейчас важнее механизм, а не chronology | Source usage / readiness; main text только при споре о версии skill/eval |
| GitHub issues/PR absence for обе repositories | Это отрицательный источник происхождения, но он не помогает читателю понять механизм TDAD | Open questions/readiness, не основной текст |
| TDFlow Bad Test Rate and generated-test-type figures | Полезно для будущей статьи о repair workflows, но TDAD Comparative должен держать две линии | External image queue only; не вставлять без решения о расширении контраста |
| Installation variants from `tdad-skill` marketplace / `npx skills add` | Практический adoption-detail, не central to concept-first argument | Handbook or implementation note |

### Требует открытия первоисточников перед усилением утверждений

| Утверждение / угол | Почему нельзя усиливать сейчас | Нужный первичный материал |
| --- | --- | --- |
| Точный статус `ALWAYS_CREATE_TICKET` / `M_ALWAYS_TICKET` as killed/survived mutant | Досье фиксирует конфликт rendered GitHub / raw README / HuggingFace naming | Commit hash, raw README at hash, `results/supportops_v1_*.json`, exact HF dataset row |
| Числа SpecSuite-Core beyond source-reported aggregate metrics | Агрегаты есть, но статья не должна создавать впечатление независимой верификации | PDF/HTML metric definitions, HF `specs`/`mutations`/`results` rows, run JSONs |
| Claims about eval reliability in `EXP-021j/k/l`, `EXP-026`, `EXP-028` | Main text uses them as examples from `EXPERIMENTS.md`; raw artifacts not opened | Concrete `report.json`, `progress.log`, `evaluations/*.eval.json`, prediction JSONL |
| Exact relation between short research `SKILL.md`, published `tdad-skill`, and evaluated skill | Dossier shows different stages; numbers must not be attached to wrong artifact | Paper text, repository history, evaluated prompt/skill artifact, commit/date evidence |
| Rights/quality of article figures and repository screenshots | Placeholders are source candidates, not local assets | PDF/HTML figure extraction, license/rights review, local asset metadata |

### Technical support gaps to watch

- Первая линия already has enough technical anchors for a concept-first article, but final source-depth should verify whether all source links still support: `spec.yaml` fields, `MFT/INV/DIR`, `respond`, SURS/RPR, `SpecSuite-Core` dataset structure and mutation claims.
- Вторая линия needs strongest future support around actual runtime artifacts: real `.tdad/test_map.txt`, exact CLI output or sample, and raw evaluation files behind the `EXPERIMENTS.md` summary.
- The article should not grow a universal testing taxonomy. Any additional fact must help the reader distinguish: tests compile agent behavior; tests route code-change verification; tests as repair task belong to a neighboring workflow.

## P04 transfer — line 1, tests/examples as behavior definition

| Материал / тезис | Источник | Решение P04 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| `test_guidance` и примеры уточняют неоднозначную политику до исполняемых тестов | HTML `2603.08806v1` через dossier inventory | Добавлено в основной текст | Раздел «Линия 1», сразу после `spec.yaml` / behavioral specification | Усиливает тезис: тесты реализуют ожидаемое поведение, а не только проверяют готовый prompt |
| Цепочка `specification → test guidance → executable tests → compiled agent definition` | Синтез из HTML `2603.08806v1` и dossier line-1 workflow | Добавлено как local explanatory formulation | Раздел «Линия 1» | Формулировка объяснительная; facts around fields and process remain sourced to HTML article |
| Риск конфликтующих тестов без уточняющих examples | HTML `2603.08806v1` | Добавлено | Раздел «Линия 1» | Keep concise; do not expand into TestSmith implementation appendix unless needed |
| Детерминированные фикстуры и `canary values` for PII/branch behavior | HTML `2603.08806v1` | Добавлено | Абзац про `MFT` / `INV` / `DIR` | Adds concrete mechanism for tests as behavior anchors |

P04 did not add new visual candidates. Existing `fig-tdad-definition-overview`, `fig-tdad-definition-repo-tree`, and `fig-tdad-definition-mutation` remain the line-1 visual set.

## P05 transfer — line 2 engineering practice

| Материал / тезис | Источник | Решение P05 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| Опубликованный `tdad-skill` шире минимального runtime skill in the paper | `tdad-skill` README / `SKILL.md`; HTML `2603.17973v2` | Добавлено | Раздел «Линия 2», после формата `.tdad/test_map.txt` | Prevents mixing research eval artifact with later practical packaging |
| Practical value depends on skill discovery, understanding and time budget | `EXPERIMENTS.md` around `EXP-026`; `tdad-skill` | Усилено | Раздел «Линия 2» | Connects skill packaging to negative benchmark result |
| Auto-improvement loop: 15 iterations, 4 kept, 11 reverted; `SKILL.md` shortened, static `test_map.txt`, directory proximity and import links | HTML `2603.17973v2`; dossier line 2 | Добавлено | Раздел «Линия 2», after Phase 2 results | Keep as engineering iteration, not as model self-learning |
| Old benchmark runner telemetry fields beyond `resolved` | `run_benchmark.py TDAD` | Перенесено into main text | Раздел «Линия 2», after eval provenance paragraph | Raw runner fields still need final source check if used as strong evidence |

P05 strengthens line 2 as practice: skill packaging, benchmark iteration, agent-assisted method improvement, and evidence telemetry. No new figure candidate added.

## P06 transfer — benchmark / dataset / result interpretation

| Материал / тезис | Источник | Решение P06 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| First-line metrics measure a bounded behavioral protocol, not general agent quality | HTML `2603.08806v1`; SpecSuite-Core | Added interpretation section | `Как читать score` | Keeps `vpr_percent`, `hpr_percent`, `mutation_score`, SURS/RPR within human framing |
| `mutation_score` misses mutation quality, non-activating mutant ambiguity and provenance conflicts | HTML `2603.08806v1`; tdad-paper-code; SpecSuite-Core | Added | `Как читать score` | Reinforces P01/P03 warning without adding new raw claims |
| Second-line metrics split `resolution rate`, `test-level regression rate`, `generation rate` | HTML `2603.17973v2`; tdad-skill | Added interpretation paragraph | `Как читать score` | Shows why lower regression can coexist with lower patch generation |
| Benchmark environment and eval provenance are part of what a score measures | EXPERIMENTS.md; run_benchmark.py | Added | `Как читать score` | Ties `EVAL_JSON_PATH` and telemetry fields to source provenance |
| Human framing starts where score ends | Synthesis of TDAD evidence sections | Added | `Как читать score` | No new external claim; article-level conclusion |

P06 did not add visual candidates. It clarified score interpretation and shifted result claims away from leaderboard reading.

## P07 transfer — human decision points and verification boundary

| Материал / тезис | Источник | Решение P07 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| Разделение наблюдение / свидетельство / принятие | Article synthesis from TDAD sources and P06 score work | Added standalone section | `Где человек решает` | Supports evidence boundary without citing internal theory docs |
| Human decision points in line 1: specification, `test_guidance`, hidden/visible promotion, non-activating mutants, RPR thresholds | HTML `2603.08806v1` | Added | `Где человек решает` | Keeps first-line tests from becoming automatic acceptance |
| Human decision points in line 2: map freshness, empty map entry, impacted tests vs full CI, eval provenance | `tdad-skill SKILL.md`; `EXPERIMENTS.md` | Added | `Где человек решает` | Connects runtime surface to engineering judgment |
| TDFlow contrast: correctness of reproduction tests and test-hacking boundary | HTML TDFlow | Added as contrast | `Где человек решает` | Still not treated as a TDAD line |

P07 added no new source family or visual candidate. It made explicit where a test can answer a narrow check but not the full engineering question.

## P08 transfer — failures and anti-summary

| Материал / тезис | Источник | Решение P08 | Где в статье | Примечание / долг |
| --- | --- | --- | --- | --- |
| Wrong task encoded: tests can faithfully optimize the wrong specification/task | HTML `2603.08806v1`; TDFlow HTML contrast | Added anti-summary paragraph | `Где граница ломается` | Keeps TDAD from sounding like tests create understanding automatically |
| Benchmark as substitute for understanding is invalid | Existing score/provenance sources | Added | `Где граница ломается` | Connected to version/spec/map/eval/model context |
| Agent optimized to check rather than engineering intent | HTML `2603.08806v1`; `2603.17973`; TDFlow HTML | Added | `Где граница ломается` | Connects hidden tests, mutation testing, TDD Prompting Paradox and test hacking |
| Passing examples are not sufficient evidence by themselves | Article synthesis from P06/P07 and source caveats | Added | `Где граница ломается` | No new external source; article-level anti-summary |

P08 added no new source family or visual candidate. It adds a compact anti-summary to stop over-smooth readings of TDAD.


## P09 transfer — free expansion 1 / SpecSuite domain mechanisms

| Недобор, выбранный редакторски | Источник | Добавлено в основной текст | Где | Что осталось долгом |
| --- | --- | --- | --- | --- |
| Первая линия называла четыре домена SpecSuite-Core, но почти не показывала, какую работу тесты реально задают агенту | HTML `2603.08806v1` | Краткая доменная расшифровка: `SupportOps` как авторизация/PII/эскалация, `DataInsights` как SQL grounding/числа/неоднозначность/стоимость, `IncidentRunbook` как evidence-first/severity/runbook, `ExpenseGuard` как лимиты/FX/чеки/approval | Раздел «Линия 1», сразу после абзаца о SpecSuite-Core | Перед публикацией проверить exact examples in primary specs/generated tests, если статья будет расширять этот абзац до конкретных кейсов |

P09 strengthens line 1 without adding a new theory layer: tests are shown as behavior branches for distinct operational duties, not merely as benchmark items.

## P10 transfer — free expansion 2 / reader path

| Недобор, выбранный редакторски | Источник / материал | Добавлено в основной текст | Где | Что осталось долгом |
| --- | --- | --- | --- | --- |
| Статья уже имела факты и границы, но читатель мог идти дальше как по двум независимым TDAD-конспектам | `C5_theory_to_technical_atlas.md` article-model guidance plus current article structure | Added a reader-route section with three questions: object under control, agent-facing test surface, human decision supported by evidence | After `Контракт статьи`, before the quick TDAD split | Later structure pass should check whether this duplicates the opening/table or whether it improves navigation enough to keep |
| TDFlow contrast risked appearing late and incidental | Existing TDFlow contrast already used in article | Moved its role into early reader path as the third test-driven mode: reproduction tests define a repair task, not a TDAD line | Same new section | Keep wording cautious so TDFlow remains neighbor/contrast only |

P10 strengthens coherence rather than source breadth. The core article route is now: object → surface → decision.

## P11 transfer — local visual asset pass

| Визуальный материал | Статус P11 | Где в статье | Решение / причина | Долг |
| --- | --- | --- | --- | --- |
| `content/assets/theory-images/fowler-harness-types.png` | `local_image_asset / inserted_inline` | Section `Что считать свидетельством, а что только наблюдением` | Inserted because it visually separates test suite/behavior from broader guides, sensors, maintainability and architecture fitness. This supports the article's boundary against reading TDAD as “tests replace engineering judgment” | If TDAD-native source figures are later localized, decide whether this cross-source harness image still earns space |
| Other local assets listed in `LOCAL_ASSET_INDEX.md` | `not_inserted` | — | They belong mainly to neighboring atlas articles: SPDD, Kiro/SDD, PWG/Beads, Gas Town, Codex/harness or story cases. P11 keeps TDAD visual priority on TDAD papers/repos and uses only the one local asset that directly supports the test-as-evidence boundary | Reconsider only if a later structure pass needs a broader harness/evidence bridge |

P11 does not replace any external-real TDAD candidate. It inserts one relevant local asset and leaves TDAD paper/repo diagrams in the external asset queue.

## P12 transfer — external visual candidates

| Candidate from dossier | P12 disposition | Article figure id | Placement / reason | Remaining debt |
| --- | --- | --- | --- | --- |
| `2603.08806` figure 1 TDAD overview | `inline_external_real_candidate_confirmed` | `fig-tdad-definition-overview` | After visible/hidden test explanation in line 1 | Download/localize, rights and quality check |
| `2603.08806` figure 2 semantic mutation testing pipeline | `inline_external_real_candidate_confirmed` | `fig-tdad-definition-mutation` | After mutation testing explanation | Download/localize, rights and quality check |
| `tdad-paper-code` repo/source tree | `inline_external_real_candidate_confirmed_as_source_screenshot_or_tree` | `fig-tdad-definition-repo-tree` | After first-line file-surface block | Verify whether a clean source tree screenshot is better than removing the figure |
| `2603.17973` figure 1 agentic workflow | `merged/deferred` | `fig-tdad-development-pipeline` | Current figure slot prioritizes fig 2 pipeline; figure 1 can replace or supplement only if needed | Choose one during asset localization to avoid duplicate workflow visuals |
| `2603.17973` figure 2 TDAD pipeline | `inline_external_real_candidate_confirmed` | `fig-tdad-development-pipeline` | After second-line graph/test_map explanation | Download/localize, rights and quality check |
| `2603.17973` figure 3 P2P failures | `inline_external_real_candidate_confirmed_but_optional` | `fig-tdad-development-p2p-failures` | Metrics discussion | Keep only if metrics section survives structure compression |
| `pepealonso95/TDAD` / `tdad-skill` `.tdad/test_map.txt`, CLI or ASCII pipeline | `inline_external_real_candidate_confirmed_as_source_fragment` | `fig-tdad-development-test-map` | Runtime surface of second line | Verify source fragment is readable and rights-safe; remove if not |
| TDFlow figure 1 workflow | `inline_external_real_candidate_confirmed_contrast_only` | `fig-tdflow-reproduction-tests` | Section `Тест как спецификация, тест как маршрут, тест как задача` | Keep only if TDFlow remains in article as contrast |
| TDFlow Bad Test Rate / generated-test figures | `queue_only` | — | Not inserted; would over-expand reproduction-test quality discussion | Revisit only if article adds a stronger TDFlow failure subsection |

P12 moved no facts into the article. It improved the public quality and disposition of the visual layer.

## P13 transfer — synthetic figure decision

| Synthetic idea | P13 disposition | Reason | Future condition |
| --- | --- | --- | --- |
| `Объект → поверхность → решение` comparison across first TDAD, second TDAD and TDFlow | `deferred_editorial_visual_idea` | Useful but currently redundant with the reader-route prose and quick comparison table; would add visual load before real source figures are localized | Reconsider only if structure pass removes the table or readers still need a one-screen conceptual map |
| `Тест как спецификация / маршрут / задача` three-column diagram | `deferred_editorial_visual_idea` | Already explained by a full section and supported by external source candidates; not enough added value as a synthetic figure now | Reconsider if TDFlow is pruned and the distinction needs a compact replacement |
| Evidence ladder `наблюдение → свидетельство → принятие` | `rejected_for_now` | P11 already inserted a local harness image for the broader evidence boundary; another synthetic ladder would duplicate theory material | Reopen only if P11 image is removed and the later evidence sections stay separate |

P13 preserves the source-image priority and avoids creating a decorative authorial diagram.

## P14 transfer — standalone concept minimum

| Need / source pressure | Article action | Status / debt |
| --- | --- | --- |
| Reader must understand core terms before detailed source mechanics | Added `Минимальный словарь статьи` after the reader-route section | Done |
| `agent definition` can be misread as model or prompt only | Defined it as prompt + tool descriptions + response contract + fixtures + testable behavior | Done |
| `visible` / `hidden` split can be misread as importance hierarchy | Defined it by access and optimization boundary | Done |
| `mutation intent` can be misread as random corruption | Defined it as plausible wrong agent behavior | Done |
| `test map` can be misread as a full graph or ordinary test list | Defined it as the second-line agent-facing working surface | Done |
| `свидетельство` can be misread as any green output | Defined it through provenance, version, task link and uncovered-risk boundary | Done |
| Duplication with later split table and evidence sections | Keep for now; later structure pass should compress if repetitive | Watchpoint |

P14 transfers no new primary fact. It makes the existing fact pattern legible earlier so the article can stand alone as a concept-first atlas entry.

## P15 transfer — mechanism-bound limitations

| Pressure / gap | Article action | Status / debt |
| --- | --- | --- |
| Old failure section risked becoming a numbered catalog | Replaced it with a mechanism-oriented section: `Как управляющий тестовый контур даёт сбой` | Done |
| Required risk: test defines wrong task | Integrated into the opening mechanism paragraph with first-line TDAD and TDFlow contrast | Done |
| Required risk: benchmark as surrogate understanding | Integrated into leakage/overfitting and passing-examples paragraphs | Done |
| Required risk: passing examples treated as acceptance | Integrated into final paragraph of the mechanism section and later evidence/acceptance continuity | Done |
| Required risk: data leakage / overfitting to benchmark | Added explicit explanation of hidden/eval/benchmark leakage into the optimizer loop | Done |
| Required risk: test oracle too narrow | Added explicit oracle paragraph covering mutation score, hidden pass rate, resolution rate and pytest output | Done |
| Required risk: article becomes generic testing chapter | Added explicit boundary: these limits matter only where the same signal guides agent action | Done |
| Later structure | New section may overlap with score/evidence sections; later editor should tighten repeated benchmark/provenance wording | Watchpoint |

P15 transfers no new primary facts; it relocates and rewrites already-supported risk material into the conceptual mechanism.

## P16 transfer — semantic theory back-links

| Theory pressure | Article / companion action | Status / debt |
| --- | --- | --- |
| Back-links must answer theory questions, not just name A3/A5/A7/A9/A10/C5 | Added P16 semantic back-link table in `theory_links` | Done |
| Main text risked a narrow A10-only link | Rewrote mode section into `Как TDAD возвращается в общую карту режима` | Done |
| Avoid rewriting the theory chapter inside the article | Main section kept to four local links: specification, process, evidence, repair | Done |
| Preserve TDAD source focus | No new TDAD facts added; source-specific sections untouched | Done |
| Future duplication | Final summary now partly overlaps with new theory-return section | Watchpoint |

P16 transfers theory framing into back-links and a compact article section. It does not add new external claims or visual assets.

## P17 перенос — языковая нормализация

Случайные английские связки заменены русскими эквивалентами: benchmark→бенчмарк, executable example→исполняемый пример, examples→примеры, evidence→свидетельства, workflow→рабочий процесс, score→показатель, oracle→оракул проверки, leakage→утечка, impacted tests→затронутые тесты, acceptance→принятие, runtime signal→сигнал времени выполнения, eval file→файл оценки. Точные названия источников и артефактов сохранены: названия статей, метрики, команды, пути, имена полей и figure IDs.

Долг: P18 или будущий языковой проход должен проверить оставшиеся английские метрики и source-specific labels.

## P18 перенос — связность и подписи

P18 не переносил новую фактуру. Изменения касались только формы: уточнены русские заголовки, подписи к рисункам, `alt` локального изображения, нижний блок внешних кандидатов, формулировки про `eval`/файл оценки и несколько тяжёлых калькированных оборотов. Технические source labels и числовые утверждения сохранены.

## P19 перенос — редакторское сокращение без потери фактуры

Сначала выявлены три реальные проблемы: основной текст заканчивался служебным asset-инвентарём; слово `контур` повторялось чаще, чем нужно для аргумента; readiness-долг P18 про companion-only слой оказался настоящим. Исправления: нижний блок внешних изображений перенесён из основного текста в companion-слой, несколько повторов `контур` заменены на `проверочный слой`, `механизм`, `связка`, `система проверок`. Фактура, ссылки, числа и технические артефакты сохранены.

## P20 перенос — удаление пустых figure-заготовок

Сначала выявлена реальная проблема P20: после P19 статья уже заканчивалась чисто, но внутри текста оставались пустые `<figure>`-блоки с `external-real-candidate`. Они выглядели как незавершённые asset-заготовки и мешали standalone reading. Исправление: все внешние placeholder-фигуры удалены из основного текста. Локальная фигура `fig-harness-types-verification-boundary` сохранена, потому что у неё есть реальный `img` и она поддерживает границу свидетельства. Визуальные кандидаты не потеряны: они остаются в `image_plan` и `external_image_queue`.

## P21 перенос — согласование визуального слоя после удаления placeholders

Сначала выявлена проблема: после P20 основной текст уже не содержал пустых внешних фигур, но верхние строки image_plan и P12/P19-заметки всё ещё могли читаться так, будто inline placeholders остаются текущим состоянием статьи. Исправления: текущий статус image_plan переписан под реальное состояние, external queue уточнена как companion-only, а подпись локальной `fig-harness-types-verification-boundary` в статье прямо говорит, что это не TDAD-source diagram, а граничная иллюстрация harness. Фактическая TDAD-аргументация не менялась.

## P22 перенос — entry-sequence и visual protocol

Сначала выявлены две проблемы публичной формы. Первая: первый экран всё ещё начинался с taxonomy двух TDAD-линий, хотя статья должна problem-first вводить объект — тест как поверхность постановки задачи агента. Исправление: opening переписан в последовательность `problem → reader question → two TDAD lines`.

Вторая: P20/P21 сделали статью визуально чистой, но слишком жёстко отступили от правила для concept-atlas articles: external_real_image_candidate должен иметь inline slot или явный queue-only disposition, а нижний asset-pass раздел должен зеркалить решения. Исправление: четыре ключевых внешних кандидата возвращены inline как `external-real-candidate` с публичными подписями; repo-tree, P2P chart and TDFlow workflow оставлены queue-only/optional. Фактическая аргументация не менялась.

## P23 перенос — companion cleanup, not new coverage

P23 не переносил новую фактуру в основной текст. Задача прохода — удалить устаревшие companion-долги и не превращать ledger в coverage-бюрократию. Active debts now live in `tdad_comparative_open_questions.md`: source/provenance blockers, asset localization blockers, structure watchpoints and theory-link watchpoints. Ledger remains historical transfer record plus this sync note; future passes should add to it only when фактура реально переносится, отклоняется или меняет статус.

## P24 transfer note — style defects only

| Область | Что исправлено | Что сохранено |
| --- | --- | --- |
| Main text terminology | Убраны псевдотехнические свёртки вроде `человеческого обрамления`, `фронта проверки`, `контрольного шлюза`, `поверхности сбоя` | Фактическая структура двух TDAD-линий и source-bound термины сохранены |
| Boundary and theory prose | Несколько абстрактных формул заменены на прямые решения человека, проверяемые артефакты и наборы проверок | Связь с A3/A5/A7/A10 остаётся прежней |
| Visual captions / asset table | Публичные подписи и роли изображений русифицированы без изменения `Figure ID`, статуса и proposed local path | Четыре inline external candidates, один local harness asset и queue-only candidates сохранены |

P24 does not transfer new facts from sources. It records a style-preservation pass: factual density remains, model-like phrasing is reduced.

## P25 transfer note — natural rewrite without new fact transfer

P25 transferred no new source material. The pass changed article surface language only: section `Читательский маршрут` became `Как читать статью`, failure heading became `Где тестовое управление даёт сбой`, and theory-return heading became `Что TDAD добавляет к общей карте режимов`. These are readability changes; article boundaries, figure dispositions and claims remain unchanged.

## P26 transfer note — final guarded style

P26 не переносил новых фактов и не удалял source-bound детали. Главные изменения: определения в словаре стали прямее, подпись локальной harness-фигуры меньше похожа на meta-note, а финальная таблица внешних изображений получила русские заголовки и описания при сохранённых figure IDs, статусах и proposed paths. Это проход сохранения стиля и provenance, а не расширение содержания.
