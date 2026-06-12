# A10 mode-selection plan refinement report

Baseline: исходный пользовательский `git.zip` из текущего чата. Текущее состояние восстановлено через последний cumulative overlay с C5 concept-atlas refinement.

## Причина правки

После обсуждения A10 стало ясно, что прежний план всё ещё мог породить не финальную карту выбора режима, а пересказ A1–A9 или классификацию режимов. Кроме того, ранний package A10 уже был признан преждевременным: A10 должен учитывать C1–C4.

## Что изменено

`work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md` переписан как поздний 17-pass план:

1. `Dependency gate`: не писать и не пакетировать A10 до C1–C4.
2. Добавлены target outputs:
   - `A10_mode_selection_matrix.md`;
   - `A10_decision_stress_tests.md`.
3. A10 определён как карта выбора минимально достаточного режима работы, а не `summary`, `maturity model` or static classification.
4. В план добавлены обязательные upstream inputs B1–B3 and C1–C4.
5. Добавлены адресные проходы:
   - критерии выбора режима;
   - переходы, эскалация and деэскалация;
   - сочетания режимов and минимально достаточная структура;
   - сценарный stress-test.
6. После общей редакторской тройки добавлен `public decision-map / visual-artifact pass`.
7. Финальная проверка вынесена отдельно и не считается рабочим проходом.

## Активный маршрут

До результатов C1–C4 активны только:

- `00_SPINE_MAP.zip`;
- `C1_SPECIFICATION_TO_PWG.zip`;
- `C2_PWG_TO_PROCESS_PROFILES.zip`;
- `C3_PWG_TO_EVIDENCE.zip`;
- `C4_EXECUTION_RUNTIME_TO_PWG.zip`.

`A10_MODE_SELECTION_MAP.zip` остаётся `premature/superseded` and must be rebuilt after C1–C4.

## Verification

- A10 target outputs include matrix and stress-tests.
- A10 plan has 17 working prompt sections.
- A10 plan has separate final verification.
- A10 dependency gate mentions C1–C4.
- Current cumulative overlay does not include `work/theory-writing/packages/A10_MODE_SELECTION_MAP.zip`.
