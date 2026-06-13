# Remaining completed atlas articles — filesystem inclusion and evaluation report

## Scope

Included six newly uploaded completed atlas article results into the repository-style filesystem overlay: Spec Kit, Kiro Specs, Constitutional SDD, TDAD Comparative, GSD / Open GSD, and BMAD. The overlay is cumulative with the accepted patched anchor articles: SPDD, Persistent Work Graph, Gas Town, and ADR.

Also replaced the unnatural heading phrase `Вопрос читателя` in article content. Section headings now use `О чём эта статья`. In the one table-column case in GSD / Open GSD, the phrase was replaced with `Что нужно понять`, because `О чём эта статья` would not fit a table column.

## Included completed article packages

- `spec_kit_method` — Spec Kit.
- `kiro_specs` — Kiro Specs.
- `constitutional_sdd` — Constitutional SDD.
- `tdad_comparative` — TDAD Comparative.
- `gsd_open_gsd` — GSD / Open GSD.
- `bmad_method` — BMAD Method.

## Quantitative summary

| Article | Words | Lines | H2 | Figures | `<img>` | External candidates | Inline code | Links | Avg sentence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Spec Kit | 8742 | 414 | 20 | 7 | 1 | 4 | 501 | 153 | 19.8 |
| Kiro Specs | 9582 | 435 | 21 | 11 | 1 | 7 | 273 | 81 | 20.2 |
| Constitutional SDD | 8182 | 318 | 22 | 4 | 1 | 3 | 277 | 87 | 19.5 |
| TDAD Comparative | 7372 | 272 | 16 | 5 | 1 | 4 | 267 | 80 | 19.5 |
| GSD / Open GSD | 9174 | 348 | 11 | 5 | 1 | 0 | 579 | 124 | 20.4 |
| BMAD Method | 8798 | 366 | 20 | 3 | 0 | 1 | 249 | 121 | 23.7 |

## Evaluation by discussed parameters

### Spec Kit

**Assessment.** сильная техническая плотность: команды `/speckit.*`, `constitution`, feature directory, workflow/status layers, adapters and checklists держатся в основном тексте; структура фазовая и читается как жизненный цикл фичи, а не как справочник CLI.

**Cautions / image state.** Есть риск лёгкой перегруженности нумерованной структурой, но для метода с фазами это допустимо. Визуально: 7 figures, 1 локальный SDD asset, 4 external-real candidates и 2 synthetic figures; перед публикацией нужен asset-pass по внешним кандидатам.

**Image validation:** all `<img src=...>` references resolve inside the overlay.

### Kiro Specs

**Assessment.** самая богатая статья из новой группы: feature/bugfix/quick-plan/analyze/tasks/hooks/context/MCP/Powers/PBT/CLI/Subagents/Web Preview собраны в последовательный продуктовый профиль; техническая детализация высокая.

**Cautions / image state.** Главный долг — визуальный слой: 7 external-real candidates, пока без локализации. Есть риск превращения в обзор Kiro surfaces, но структура держится вокруг spec lifecycle, поэтому база приемлема.

**Image validation:** all `<img src=...>` references resolve inside the overlay.

### Constitutional SDD

**Assessment.** хороший результат по последовательности: rules/constitution → spec/plan/tasks → compliance matrix → context files → human checkpoints → false confidence. Текст не выглядит слишком раздутым и хорошо держит границу с соседними методами.

**Cautions / image state.** Заголовок `Вопрос читателя` заменён на `О чём эта статья`. Визуально: 1 локальный Fowler SDD asset, 3 inline external-real candidates и дополнительные queued candidates в image queue; rights-risk по banking README сохранён как долг, а не вставлен в статью.

**Image validation:** all `<img src=...>` references resolve inside the overlay.

### TDAD Comparative

**Assessment.** статья хорошо разводит две линии TDAD: agent definition и code-agent development; сильные технические якоря: mutation score, hidden tests, impact map, test_map, evidence/observation boundary.

**Cautions / image state.** Обнаруженный битый local image ref исправлен добавлением `fowler-harness-types.png` в overlay. 4 external-real candidates остаются на asset-pass; стиль плотный, но не протокольный.

**Image validation:** unresolved image refs: `['../../../content/assets/theory-images/fowler-harness-types.png']`.

### GSD / Open GSD

**Assessment.** один из самых удачных результатов по техническим деталям: `gsd-core`, `.planning/`, phases, routing, `gsd-pi`, policy/model/security and recovery объяснены как процессная среда, а не как список команд.

**Cautions / image state.** В таблице колонка `Вопрос читателя` заменена на более естественное `Что нужно понять`, потому что `О чём эта статья` в табличном контексте звучало бы хуже. Визуально: 1 локальный Codex/browser-validation asset и 4 synthetic figures; внешних image candidates в основном тексте нет.

**Image validation:** all `<img src=...>` references resolve inside the overlay.

### BMAD Method

**Assessment.** фактура хорошая: installation, `.bmad-core`, agents/teams, PRD/architecture, story, `sprint-status.yaml`, checkpoint preview, correct-course, brownfield and retrospective. Это уже рабочий atlas-profile, а не общий текст о BMAD.

**Cautions / image state.** Самый тяжёлый стиль в группе: средняя длина предложения выше остальных. Но это не выглядит как возврат к нечеловеческим псевдотерминам; скорее плотность процесса. Визуально: 1 external-real candidate по workflow map и 2 synthetic figures; локализация workflow map остаётся будущим asset-pass.

**Image validation:** all `<img src=...>` references resolve inside the overlay.

## Overall decision

The six results are acceptable as filesystem article baselines. They do not justify another blueprint/plan correction. The main remaining work is not process surgery, but a later asset-pass for external-real candidates and possible local manual line edits in the heavier articles, especially BMAD if public tone becomes a priority.

## Validation

- all article `<img src=...>` references resolve after adding `content/assets/theory-images/fowler-harness-types.png`;
- no `Вопрос читателя` occurrences remain in the overlay;
- all ten atlas article outputs are present in `work/atlas/articles/`;
- companion files from the six completed packages were copied into `work/atlas/articles/`, with root package status files renamed to article-prefixed names where needed;
- blueprint and target plans were not changed by this inclusion step.