# constitutional_sdd — degradation and duplication audit

Статус: P26 guarded final style sync. Аудит отражает финальную охранную правку: псевдотермины и случайные тяжёлые формулы не возвращены.

## Degradation checks

| Check | Status | Notes |
|---|---|---|
| Article answers reader question | pass | The draft stays centered on Constitution/security-policy layer above feature spec and explains compliance matrix, context files and traceability. |
| No internal volume cap | pass | Draft was not compressed to a short summary. |
| Not a dossier summary | pass | Article is organized around mechanism, artifacts, gates, evidence, context and failures; it does not follow dossier order mechanically. |
| Technical anchors present | pass | Includes files, commands, matrix examples, context files, PR/CI gates, percentages with caveats, and concrete risks. |
| Source provenance near claims | partial_pass | Public links are embedded next to major facts. Later source-depth pass should verify exact details against live/PDF sources. |
| Evidence levels separated | pass | Marri is main source; Mad Devs, DocGuard and Foundry are marked as practical/neighbor sources rather than metric replication. |
| Visual candidates handled | pass | Dossier candidates received dispositions; three inline external placeholders added; queue created. |
| No source asset substitution | pass | Source visuals are placeholders; synthetic diagrams deferred rather than replacing them. |
| Russian technical style | partial_pass | Draft is Russian and avoids most model-summary tone; later language/style passes should remove remaining English-heavy labels where possible while preserving source-specific filenames/commands. |

## Duplication checks

| Potential duplication | Status | Mitigation |
|---|---|---|
| General theory of specification layer | controlled | Draft repeats only local minimum needed to understand CSDD. |
| Spec Kit article territory | controlled_risk | Spec Kit commands appear only where they explain CSDD's artifact chain and gates. Later pass should keep command detail bounded. |
| Secure coding article territory | controlled | The article uses secure coding examples only to explain Constitution and matrix traceability. |
| Foundry/neighbor article territory | controlled_risk | Foundry is a neighbor section; avoid expanding roles/evidence gates too far in this article. |
| Handbook/Fieldbook checklist territory | controlled | Practical checklist material is mostly in prose; companion files retain operational debt. |

## Known risks for next passes

1. P01 may still be too source-dense in some sections; later editor passes should improve sequence without removing technical anchors.
2. Metrics and numbers need exact source verification before final readiness.
3. `CONSTITUTION_COMPLIANCE.md` automation claim needs source-depth check.
4. Visual layer requires actual rights/download/quality pass.
5. The article should gain more concrete traceability examples only if they can be verified directly.

## P02 boundary audit

| Risk | Status after P02 | Evidence |
|---|---|---|
| Generic security manifesto | controlled | Added negative boundary: policy counts only if it changes action in spec/plan/tasks/code/review. |
| Paper/repo retelling | controlled | Contract section explicitly centers mechanism and boundaries before source detail. |
| Spec Kit duplicate | controlled | Boundary states Spec Kit is repo workflow; CSDD adds policy/Constitution layer. |
| SPDD duplicate | controlled | Boundary states SPDD manages structured prompt/intent; CSDD manages security/policy constraints above feature. |
| Kiro duplicate | controlled | Boundary states product spec surface is not automatically constitutional layer. |
| ADR duplicate | controlled | Boundary states ADR stores accepted decision; Constitution constrains recurring work. |
| TDAD/A7 evidence conflation | improved | Boundary states compliance matrix can support evidence but is not evidence by itself. |
| PWG drift | controlled | Boundary states PWG stores work state; CSDD defines constraints/gates. |
| C5/A10 boundary context | pass | C5/A10 are used only as read-only framing; concrete follow-ups are recorded separately. |

## P04 audit — paper framing vs repository workflow

| Risk | Status after P04 | Notes |
|---|---|---|
| Treating academic metrics as workflow gates | controlled | Article states figures/Table 3/73% are explanatory/evaluative, not executable gates. |
| Treating demo repository as the whole method | controlled | Article states repo is a workflow surface, not the definition of all CSDD. |
| Over-abstract paper summary | improved | Article now names concrete files that agent/package can inspect. |
| Tooling overclaim | improved | `CONSTITUTION_COMPLIANCE.md` remains useful but automation claim is still open. |

## P05 audit — concrete artifacts

| Risk | Status after P05 | Notes |
|---|---|---|
| Article remains too conceptual | improved | Artifact table names concrete files, state and expected outputs. |
| Article becomes product/tutorial reference | controlled | Table avoids installation or CLI walkthrough; it focuses on CSDD roles. |
| Unsupported repo claims | controlled | Table distinguishes expected surfaces from confirmed reference repo files. |
| Context files over-authorized | controlled | Table states context files should backlink to authoritative artifacts and not outrank Constitution/spec/plan. |

## P06 audit — matrix and traceability depth

| Risk | Status after P06 | Notes |
|---|---|---|
| Matrix treated as audit paperwork | improved | New section defines when matrix constrains plan/tasks/review and when it is only formal. |
| Evidence/matrix conflation | controlled | Section preserves three levels: intention, implementation and verification. |
| Overclaiming automation | controlled | `CONSTITUTION_COMPLIANCE.md` generator remains an open question; article does not treat it as proven CI enforcement. |
| Turning article into tool tutorial | controlled | DocGuard and Spec Kit issue material are used only for traceability mechanics and failure modes. |
| Repetition with existing matrix section | acceptable | P06 adds process pressure; existing section still explains source examples and compliance surface. |

## P07 audit — boundaries with workflow and documentation

| Risk | Status after P07 | Notes |
|---|---|---|
| CSDD collapses into Spec Kit | improved | New layer table says Spec Kit is a workflow baseline, not CSDD by itself. |
| CSDD collapses into generic security docs | improved | Text requires action influence: context, gates, traceability, review or evidence. |
| ADR confusion | controlled | ADR is framed as decision memory that can support a principle, not replace Constitution. |
| New duplicate material | controlled | Section deepens boundaries already introduced in P02 without expanding command tutorials. |

## P08 audit — caveats and anti-summary

| Risk | Status after P08 | Notes |
|---|---|---|
| Article sounds like “CSDD guarantees security” | improved | Added explicit false-confidence section. |
| Constitution treated as sufficient | controlled | Section requires concrete principles, ownership and enforcement path. |
| Matrix treated as proof | controlled | Section distinguishes green status from reproducible evidence. |
| Human responsibility lost | improved | Section says security ownership, exceptions and residual risk remain human-governed. |
| Duplicate with typical failures | acceptable | Existing failure section gives examples; P08 table gives limit categories and anti-summary frame. |

## P09 audit — free expansion on context selection

| Risk | Status after P09 | Notes |
|---|---|---|
| Context files remain abstract | improved | Added task-sized `пакет конституционных ограничений` fields. |
| New invented mechanism overclaims source | controlled | Framed as an operational synthesis from Marri context-selection data and existing matrix fields, not as a named source artifact. |
| English-heavy terminology | resolved | Public terminology now uses `пакет конституционных ограничений`; old hybrid packet wording is kept out of current companion debts. |
| Article becomes Handbook checklist | controlled | Section stays short and tied to reader question. |

## P10 audit — reader path and cohesion

| Risk | Status after P10 | Notes |
|---|---|---|
| Article reads as a pile of artifacts | improved | Added one feature-level walkthrough. |
| Example overclaims exact repository state | controlled | Uses sourced qualitative example and repo artifacts; final exact-file verification remains open. |
| Duplicates workflow section | acceptable | The new section gives concrete reader path, not another abstract workflow list. |
| C5 atlas contract | improved | Section explains mechanism through a local change rather than turning article into command reference. |

## P11 audit — local visual asset

| Risk | Status after P11 | Notes |
|---|---|---|
| Local asset omitted without explanation | pass | `fowler-sdd-overview.png` inserted; other local assets rejected in image plan. |
| Generic SDD visual confuses CSDD boundary | controlled | Caption states the image is only SDD background and not CSDD evidence. |
| Visual priority drift | controlled | CSDD-specific Marri/repo figures remain queued and prioritized. |
| Asset path risk | open | Final site build may need path rewriting from repo-relative Markdown path. |

## P12 audit — external visuals

| Risk | Status after P12 | Notes |
|---|---|---|
| Inline placeholders contain service captions | improved | Captions now describe the source visual's meaning rather than saying “здесь нужна”. |
| Source visuals replaced by text diagrams | controlled | Figure/Table candidates remain external-real candidates. |
| Metrics visual overemphasis | controlled | Figure 2 remains queue-only. |
| Rights-unclear README diagrams inserted | pass | README diagrams remain rights-hold queue items. |
| Synthetic visual creep | controlled | Mad Devs/DocGuard/Foundry ideas remain deferred synthetic/editorial ideas. |

## P13 audit — synthetic visual restraint

| Risk | Status after P13 | Notes |
|---|---|---|
| Synthetic diagram replaces source visual | pass | No synthetic figure inserted; real source candidates remain primary. |
| Visual clutter | pass | Deferred diagrams that would duplicate existing tables/prose. |
| Missing visual decision record | pass | Image plan records evaluated synthetic ideas and reasons. |

## P14 audit — standalone concept-first article

| Risk | Status after P14 | Notes |
|---|---|---|
| Reader needs prior theory to understand terms | improved | Added minimal vocabulary. |
| Article becomes generic theory recap | controlled | Section is short and tied to CSDD artifacts. |
| Repetition with existing sections | acceptable | Definitions prepare reader; later sections still provide mechanism and source detail. |
| Source provenance | pass | Public links point to Marri, reference Constitution and compliance report. |

## P15 audit — mechanism, boundaries and embedded failures

| Risk | Status after P15 | Notes |
|---|---|---|
| Standalone failure catalog makes article feel like checklist | improved | Removed `Типовые сбои` as a separate section and distributed its material into mechanism sections. |
| Constitution becomes declaration | improved | Constitution section now ties enforceability to origin, scope and next affected artifact, not just principle wording. |
| Matrix looks stronger than it is | improved | Matrix section now names traceability without evidence and client/runtime blind spots as coverage boundaries. |
| Policy disconnected from next action | improved | Workflow section now asks what action changed at each handoff. |
| Model optimizes checklist wording | improved | `spec/plan/tasks` and caveat table now treat `PASS`/`MUST`/`SEC-*` wording without behavior change as mechanism failure. |
| Article becomes governance rhetoric | controlled | New text explicitly says governance language is insufficient unless lower artifacts act differently. |
| Duplication with P08 caveats | controlled | P08 table remains a compact anti-summary; detailed examples are now embedded where they explain the mechanism. |

## P16 audit — theory connection without theory rewrite

| Risk | Status after P16 | Notes |
|---|---|---|
| Article disconnected from general SDLC theory | improved | Final section now ties CSDD to software-change lifecycle, specification layer, process vs imitation, evidence, lifecycle repair and mode selection. |
| Article rewrites whole theory | controlled | Added concise theoretical framing only; detailed semantic links live in `theory_links`. |
| `theory_links` contains only vague references | improved | Added semantic back-link table with one question per theory fragment and a local CSDD answer. |
| Duplicates A3/A5/A7/A9/A10 | controlled | Companion boundaries explicitly keep comparisons, process theory, evidence theory and mode map out of main article. |


## P17 audit — language pass 1

| Risk | Status after P17 | Notes |
|---|---|---|
| Random English glue weakens Russian article voice | improved | Removed hybrid phrases around AI-assisted generation, endpoint, prompt, runtime, evidence, traceability, compliance pass, audit table and image statuses. |
| Broad replacement introduces broken Russian | improved | Fixed visible artifacts such as `контекстный файлs`, wrong cases around merge/commit/audit log, and mixed table cells. |
| Stable technical names accidentally translated | controlled | Product names, commands, files, paths, exact source labels, status tokens and quoted Foundry principles remain intact where exact form matters. |
| P09 terminology becomes pseudo-term | improved | Replaced the old hybrid packet term in public prose with `пакет конституционных ограничений`. |

## P18 audit — второй языковой проход

| Риск | Статус после P18 | Заметки |
|---|---|---|
| Английские подписи ссылок выглядят как случайный шум | improved | Переведены непредметные подписи ссылок: reference Constitution/repository/README, Spec Kit documentation, analyze command. |
| Точные указатели источников случайно теряются | controlled | `Figure 1`, `Table 1`, `Figure 4`, `Figure 2` сохранены в нижней очереди как точные указатели на источники. |
| Таблицы звучат как машинное резюме | improved | Внесены точечные правки падежей и обычных технических слов без перестройки структуры. |
| Визуальная очередь превращается в служебный жаргон визуального прохода | improved | Нижний раздел остаётся русским и объясняет, что нужно взять, зачем и почему статус ещё не закрыт. |

## P19 audit — общий редакторский проход 1

| Проблема, найденная перед правкой | Исправление | Статус после P19 |
|---|---|---|
| Читатель получал детали CSDD раньше, чем простой тест «это действительно CSDD или просто документация безопасности». | Добавлена ранняя проверка: одно правило должно пройти от Constitution до спецификации, плана, задачи, кода и свидетельства. | improved |
| Практический критерий выбора CSDD был слишком поздно и слишком теоретически сформулирован. | Добавлен раздел `Когда CSDD оправдан` с границей между долговечной политики для нескольких фич и локальными правками, где достаточно SDD/тестов/ревью. | improved |
| Новый раздел мог бы создать дублирование с финальной теорией. | Раздел сделан практическим и коротким; финальная теория остаётся общей связью с SDLC. | controlled |
| Добавление могло сдвинуть визуальную очередь или источник доказательности. | Изображения и источники не менялись; изменения являются редакторским синтезом. | controlled |

## P20 audit — общий редакторский проход 2

| Проблема, найденная перед правкой | Исправление | Статус после P20 |
|---|---|---|
| Заголовок матричного раздела мог переобещать силу матрицы. | `где намерение становится свидетельством` заменено на `где намерение связывается со свидетельством`. | improved |
| В публичном тексте оставалась служебная фраза про первый черновик. | Формулировка заменена на нейтральное описание практического слабого места. | improved |
| Финальная теория повторяла свежий раздел о применимости. | Последний теоретический абзац сфокусирован на последующем ремонте после слияния; критерий выбора режима оставлен в практическом разделе. | controlled |
| Фактура могла сгладиться при редакторской правке. | Числа 78/96/91%, матричные примеры и источники сохранены. | controlled |

## P21 audit — общий редакторский проход 3

| Проблема, найденная перед правкой | Исправление | Статус после P21 |
|---|---|---|
| Заголовки `перевод средств как не только конечная точка`, `Человеческие гейты` и `Что должно жить после слияния` были менее человеческими, чем сами разделы. | Заголовки заменены на `перевод средств как цепочка артефактов`, `Человеческие контрольные точки` и `Что должно обновляться после слияния`. | improved |
| Внутренние companion-ссылки могли устареть после переименования. | Обновлены внутренние ссылки на новый раздел о синхронизации после слияния. | controlled |
| Риск случайного содержательного сдвига при переименовании. | Текст разделов, источники и визуальные кандидаты не менялись. | controlled |

## P22 audit — entry sequence and public structure

| Проблема, найденная перед правкой | Исправление | Статус после P22 |
|---|---|---|
| Первый экран показывал внешний placeholder до явного reader question. | `fig-csdd-architecture` перенесён ниже, после reader question и короткой проверки CSDD. | improved |
| Подписи визуальных кандидатов содержали редакторский тон. | Figure 1 и Figure 4 captions переписаны как публичные объяснения. | improved |
| Нижний раздел визуальной очереди не совпадал с названием, ожидаемым структурным pass. | Заголовок заменён на `Внешние изображения для asset-pass`. | improved |
| Риск подменить изображения текстовыми схемами. | Новые synthetic figures не создавались; real candidates сохранены как inline placeholders + queue. | controlled |


## P23 audit — companion synchronization

| Проблема, найденная перед правкой | Исправление | Статус после P23 |
|---|---|---|
| Companion-файлы ещё содержали устаревшие места, псевдотермины и общие sync-долги. | Синхронизированы image plan, queue, open questions, source usage, ledger, theory links and readiness. | improved |
| Ledger мог снова стать coverage bureaucracy. | P23 закрепил его как журнал решений и сохранил только конкретные нерешённые проверки. | controlled |
| CodeGuard мог выглядеть blocker для статьи без публичного цитирования. | CodeGuard оставлен как deferred neighbor context; текущие blockers связаны с Foundry/Marri/repo freshness, visual rights and evidence provenance. | resolved |
| C5/A10 могли остаться общим sync-label. | Оставлены только конкретные boundary follow-ups и theory-mode framing. | resolved |

## P24 audit — style-defect pass

| Проблема, найденная перед правкой | Исправление | Статус после P24 |
|---|---|---|
| Несколько формулировок звучали как псевдотермины: «петля ремонта», «проверочная поверхность», «карта намерения/реализации/проверки». | Заменены на прямые русские формулировки про обратную связь, проверяемое место в коде и состояния строки матрицы. | improved |
| Заголовок `Артефактная карта` был менее естественным, чем содержание раздела. | Заголовок заменён на `Карта артефактов...`. | improved |
| Заголовок матричного раздела сохранял механическое противопоставление. | Заголовок заменён на `Как матрица ограничивает работу до слияния`. | improved |
| Риск потерять техническую фактуру при стилевой чистке. | Числа, источники, артефакты, visual candidates and caveats сохранены; новых источников не добавлено. | controlled |

## P25 audit — selective natural rewrite

| Проблема, найденная перед правкой | Исправление | Статус после P25 |
|---|---|---|
| После P24 в тексте ещё оставались искусственные или слишком книжные формулы: `карта полномочий`, `путь принудительного исполнения`, `трасса соответствия`, Fieldbook-англицизм в публичном bottom-note. | Формулировки заменены на обычный русский технический текст без потери смысла. | improved |
| Риск сгладить сильные технические места при естественной правке. | Таблицы, численные данные, source links, file names, commands and caveats сохранены. | controlled |
| Финальная теория могла звучать слишком академично. | Один абзац переформулирован как прямое объяснение роли CSDD в спецификационном слое. | improved |

## P26 audit — guarded final human technical style

| Проблема, проверенная перед финалом | Исправление | Статус после P26 |
|---|---|---|
| Запрещённая тяжёлая формула `путь принудительного исполнения` вернулась в публичный текст. | Формулировка заменена на обычное объяснение: файл памяти агента участвует в том, как правило влияет на работу агента. | improved |
| Несколько заголовков оставались точными, но звучали как служебные labels. | Заголовки про контракт, CSDD поверх спецификационного процесса, матрицу, пакет для агента, ограничения, Foundry и финальную теорию стали более естественными. | improved |
| Риск потери фактуры при финальной гладкой правке. | Источники, числа, таблицы, визуальные кандидаты, caveats and known debts сохранены. | controlled |
| Риск возвращения псевдотерминов P24/P25. | Публичный текст проверен на `путь принудительного`, `карта полномочий`, `трасса`, `петля`, `смыслов*`, `проверочная поверхность`, `Fieldbook`. | controlled |
