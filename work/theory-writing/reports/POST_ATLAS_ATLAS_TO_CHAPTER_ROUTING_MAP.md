
# Post-Atlas Atlas-to-chapter routing map

Статус: рабочая карта доноров Атласа.  
Правило: `primary` означает концептуальную базу для главы; `secondary` — контраст или вспомогательное различение; `boundary-only` — защита границы; `avoid` — не тянуть материал, чтобы глава не стала каталогом методов.

## SPDD / OpenSPDD — `spdd_method.md`

| Роль | Главы |
| --- | --- |
| `primary` | IV; III в части structured intent; XI в части review/evidence по намерению |
| `secondary` | I, V, XIII, CONCLUSION |
| `boundary-only` | VI, VII, VIII |
| `avoid` | IX, X, XII, если речь не идёт о конкретном evidence/authority переходе |

Использовать как глубокий пример specification lifecycle: REASONS Canvas, review, `/spdd-reverse`, `prompt-update` and `sync`. Не повторять в каждой главе каталог команд OpenSPDD.

## Persistent Work Graph — `persistent_work_graph.md`

| Роль | Главы |
| --- | --- |
| `primary` | VII; VI в части граница проектного контекста и состояния |
| `secondary` | II, IX, X, XIII, CONCLUSION |
| `boundary-only` | VIII, XI, XII |
| `avoid` | III–V, кроме короткой границы между specification and work state |

Использовать как концептуальная база для work item, dependencies, ready/blocked, owner/claim, gate, evidence и prime. Не превращать PWG в issue tracker, transcript или runtime.

## Gas Town / Beads — `gas_town.md`

| Роль | Главы |
| --- | --- |
| `primary` | X |
| `secondary` | VII, VIII, IX, XIII, CONCLUSION |
| `boundary-only` | II, VI, XI, XII |
| `avoid` | III–V, кроме коротких граничные заметки |

Использовать как операционно-организационный deep anchor: Beads, two-tier coordination/execution, roles, backpressure, service agents, recovery. Не переносить словарь Gas Town во все главы.

## ADR — `adr_method.md`

| Роль | Главы |
| --- | --- |
| `primary` | III, XII |
| `secondary` | XI, XIII, CONCLUSION |
| `boundary-only` | I, IV, V, VII |
| `avoid` | IX, X, если не обсуждается authority/confirmation |

Использовать для decision memory: status, rationale, alternatives, consequences, replacement and `Confirmation`. Generated/reconstructed ADR остаётся candidate until human acceptance.

## Spec Kit — `spec_kit_method.md`

| Роль | Главы |
| --- | --- |
| `primary` | V; III в части specification → plan → tasks |
| `secondary` | I, VI, XI, XIII, CONCLUSION |
| `boundary-only` | IV, VIII, XII |
| `avoid` | X и большая часть IX, если глава не про контекст репозитория и проекта |

Использовать как переносимый specification toolkit и constitution-driven feature flow. Не делать список slash-команд.

## Kiro Specs — `kiro_specs.md`

| Роль | Главы |
| --- | --- |
| `primary` | V; VI в части product-native spec state and project rules |
| `secondary` | II, IX, XI, XIII, CONCLUSION |
| `boundary-only` | III, IV, VIII |
| `avoid` | X, если не нужен пример supervised execution в более широкой среде |

Использовать как пример спецификации внутри IDE/product surface: Feature Specs, Bugfix Specs, Quick Plan, requirements/design/tasks, hooks and supervised execution. Не превращать главу в обзор продукта.

## Constitutional SDD — `constitutional_sdd.md`

| Роль | Главы |
| --- | --- |
| `primary` | V; III в части higher-order specification; XI/XII в части traceability and human checkpoints |
| `secondary` | XIII, CONCLUSION |
| `boundary-only` | IV, VIII, IX |
| `avoid` | X and pure PWG discussion |

Использовать для constitution, traceability matrix, compliance/security constraints и human checkpoints. Не обобщать CSDD до всей governance.

## TDAD Comparative — `tdad_comparative.md`

| Роль | Главы |
| --- | --- |
| `primary` | V, XI |
| `secondary` | III, XIII, CONCLUSION |
| `boundary-only` | IV, VIII, IX |
| `avoid` | X и главы ADR/PWG, кроме коротких контрастов |

Использовать как различение: tests as agent definition vs tests as regression/risk route for code-agent work. Не сводить все evidence к тестам.

## GSD / Open GSD — `gsd_open_gsd.md`

| Роль | Главы |
| --- | --- |
| `primary` | VIII; IX в части граница process/runtime |
| `secondary` | VI, XI, XIII, CONCLUSION |
| `boundary-only` | VII, X, XII |
| `avoid` | III–V, если не обсуждается переход specification into process state |

Использовать как process-runtime profile: фазы, `.planning/`, model/security policy и recovery. Не смешивать с BMAD и Gas Town.

## BMAD Method — `bmad_method.md`

| Роль | Главы |
| --- | --- |
| `primary` | VIII |
| `secondary` | I, III, VI, IX, XI, XIII, CONCLUSION |
| `boundary-only` | V, VII, X, XII |
| `avoid` | IV, если речь не о contrast with SPDD |

Использовать как role/process profile: PRD, architecture, story, `sprint-status.yaml`, checkpoint preview, correct-course и retrospective. Не превращать в каталог ролей.

## Тезисы, которые нельзя повторять целиком в каждой главе

- «Атлас не заменяет теорию» — один раз во введении или appendix, дальше короткая ссылка.
- «Досье — quarry/gap-check, не public source» — в source contract и планах пакетов, не в каждой главе.
- «Внешний поиск модульный» — в матрице и per-chapter contract, без повторения полного обоснования.
- «Агент не получает право принять результат только потому, что выполнил работу» — полно раскрыть в XII, в других главах использовать как граничную заметку.
- «PWG не runtime» — полно раскрыть в VII/IX, в других местах коротко.
- «Gas Town не просто task graph» — полно раскрыть в X, в VII/VIII использовать как соседнюю границу.
