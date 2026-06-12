> Current status after C/00 result integration: `00` and `C1`–`C4` have now been imported and repaired. The previously generated `A10_MODE_SELECTION_MAP.zip` remains premature/superseded, but a **new** A10 package may now be manufactured from the updated 17-pass A10 plan using imported `C1`–`C4` as read-only inputs.

# Future-ready packages manufactury report

> Current correction: the A10 row in this historical report is superseded. `A10_MODE_SELECTION_MAP.zip` must not be used; A10 now depends on completed C1–C4 and has a refined 17-pass plan. Active packages from this report are `00_SPINE_MAP.zip` and `C1`–`C4`.

Baseline: исходный пользовательский `git.zip` из текущего чата. Рабочее состояние восстановлено через cumulative overlay до `future target reinforcement passes`, включая concept-first atlas decision и последние ремонты A/B-фрагментов.

## Задача

Пользователь попросил собрать пакеты для планов, фрагменты которых ещё не построены, но которые не зависят от ещё не построенных фрагментов. Отдельно пользователь предположил, что это, вероятно, `C1–C4`, но не был уверен насчёт `00`.

## Dependency check

Ещё не построены:

- `00_spine_map.md`;
- `A10_mode_selection_map.md`;
- `C1_specification_to_pwg.md`;
- `C2_pwg_to_process_profiles.md`;
- `C3_pwg_to_evidence.md`;
- `C4_execution_runtime_to_pwg.md`;
- `C5_theory_to_technical_atlas.md`.

Пакеты, которые можно собирать сейчас:

- `00_SPINE_MAP`: не зависит от ещё не написанных фрагментов; работает как терминологический контракт по скелетону, плану, досье, отчётам и историям.
- `A10_MODE_SELECTION_MAP`: superseded correction — не запускать; A10 требует результатов C1–C4 и должен быть пересобран позже по обновлённому 17-pass плану.
- `C1_SPECIFICATION_TO_PWG`: требует A2/A3/A4/B2; все эти фрагменты уже есть.
- `C2_PWG_TO_PROCESS_PROFILES`: требует A4/A5/B2; все эти фрагменты уже есть.
- `C3_PWG_TO_EVIDENCE`: требует A4/A7/B2; все эти фрагменты уже есть.
- `C4_EXECUTION_RUNTIME_TO_PWG`: требует A6/A4/B2; все эти фрагменты уже есть.

Пакет, который не собран:

- `C5_THEORY_TO_TECHNICAL_ATLAS`: пока не собирать. После интеграции `00` и `C1–C4` главный оставшийся блокер — новый A10-фрагмент; C5 должен идти после A10.

## Plan consistency repair before packaging

Перед сборкой обнаружена механическая ошибка в будущих target-group plans: в `A10` и `C1–C4` адресные проходы местами ссылались на companion-файлы с длинным префиксом основного фрагмента, например:

```text
work/theory-writing/fragments/C1_specification_to_pwg_source_usage.md
```

при том что целевые companion-файлы в секции `Обрабатываемые файлы` называются:

```text
work/theory-writing/fragments/C1_source_usage.md
```

Такая несогласованность остановила бы runner в середине пакета: первые проходы создали бы короткие companion-файлы, а последующие адресные проходы стали бы ждать длинные имена.

Исправлено в планах:

- `A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md`;
- `C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md`;
- `C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md`;
- `C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md`;
- `C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md`.

`00_SPINE_MAP_TARGET_GROUP_PLAN.md` был консистентен. `C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md` не менялся.

## Собранные пакеты

Все пакеты self-contained, Python-gated, opaque record chain. Каждый содержит только:

```text
START.md
q8v4m.py
z3k9p.dat
```

| Пакет | План | Records |
|---|---|---:|
| `00_SPINE_MAP.zip` | `00_SPINE_MAP_TARGET_GROUP_PLAN.md` | 16 |
| `A10_MODE_SELECTION_MAP.zip` | `A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md` | 16 |
| `C1_SPECIFICATION_TO_PWG.zip` | `C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md` | 16 |
| `C2_PWG_TO_PROCESS_PROFILES.zip` | `C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md` | 16 |
| `C3_PWG_TO_EVIDENCE.zip` | `C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md` | 16 |
| `C4_EXECUTION_RUNTIME_TO_PWG.zip` | `C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md` | 16 |

В каждом пакете: 15 prompt records + final packaging record.

## Smoke-test

Проверки:

- `unzip -t` / `ZipFile.testzip()`;
- в архиве только `START.md`, `q8v4m.py`, `z3k9p.dat`;
- runner не содержит предметных имён фрагментов, target-group plans, prompt-текстов или списков документов;
- первый запуск runner-а создаёт первый рабочий лист;
- после фиктивных required outputs второй запуск создаёт следующий рабочий лист;
- payload остаётся opaque record chain.

Результат:

| Пакет | unzip | first run | second transition | runner opaque |
|---|---|---|---|---|
| `00_SPINE_MAP.zip` | PASS | PASS | PASS | PASS |
| `A10_MODE_SELECTION_MAP.zip` | PASS | PASS | PASS | PASS |
| `C1_SPECIFICATION_TO_PWG.zip` | PASS | PASS | PASS | PASS |
| `C2_PWG_TO_PROCESS_PROFILES.zip` | PASS | PASS | PASS | PASS |
| `C3_PWG_TO_EVIDENCE.zip` | PASS | PASS | PASS | PASS |
| `C4_EXECUTION_RUNTIME_TO_PWG.zip` | PASS | PASS | PASS | PASS |

## Result

Пакеты положены в:

```text
work/theory-writing/packages/00_SPINE_MAP.zip
work/theory-writing/packages/C1_SPECIFICATION_TO_PWG.zip
work/theory-writing/packages/C2_PWG_TO_PROCESS_PROFILES.zip
work/theory-writing/packages/C3_PWG_TO_EVIDENCE.zip
work/theory-writing/packages/C4_EXECUTION_RUNTIME_TO_PWG.zip
```

`C5` не собран и должен обсуждаться отдельно.


## 2026-06-11 correction: A10 package superseded

Повторная проверка зависимостей показала, что `A10_MODE_SELECTION_MAP` должен идти после `C1–C4`, потому что финальная карта выбора режимов должна учитывать переходные мосты между specification, PWG, process, evidence and runtime. Ранее собранный `A10_MODE_SELECTION_MAP.zip` считать premature/superseded и не запускать. После интеграции результатов C-фрагментов эти executor packages уже не являются активным следующим шагом. Следующий package-candidate — новый `A10_MODE_SELECTION_MAP.zip`, пересобранный по обновлённому плану и с `C1–C4` как read-only inputs.

## 2026-06-12 update: new A10 package built after C results

After importing and repairing `00` and `C1`–`C4`, the blocker for A10 was removed. A new `work/theory-writing/packages/A10_MODE_SELECTION_MAP.zip` has been built from the updated 17-pass A10 plan and supersedes the earlier premature package.

Correction: `C5_THEORY_TO_TECHNICAL_ATLAS.zip` is no longer blocked by missing A10. After `00` and `C1`–`C4` are imported/repaired, C5 may be packaged; missing A10 should be recorded as `A10 sync pending` for later synchronization.

Historical blocker report: `work/theory-writing/reports/A10_PACKAGE_MANUFACTORY_AND_C5_BLOCKER_REPORT.md`; corrected package report: `work/theory-writing/reports/C5_PACKAGE_MANUFACTORY_AFTER_DEPENDENCY_CORRECTION_REPORT.md`.
