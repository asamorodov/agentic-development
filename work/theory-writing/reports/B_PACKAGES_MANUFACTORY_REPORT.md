# B packages manufactury report

Baseline: исходный пользовательский `/mnt/data/git.zip`; рабочее состояние восстановлено через последний cumulative overlay перед сборкой B-пакетов.

Собраны self-contained Python-gated пакеты по принятым target-group plans. Prompt-очереди не редактировались; сборщик только материализовал планы в opaque record chain.

## Пакеты

- `work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip` — plan `work/theory-writing/target-group-plans/B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN.md`, records: 13 (12 prompt records + final), size: 1048183 bytes.
- `work/theory-writing/packages/B2_PWG_CONTRIBUTION.zip` — plan `work/theory-writing/target-group-plans/B2_PWG_CONTRIBUTION_TARGET_GROUP_PLAN.md`, records: 12 (11 prompt records + final), size: 1015774 bytes.
- `work/theory-writing/packages/B3_GAS_TOWN_BEYOND_PWG.zip` — plan `work/theory-writing/target-group-plans/B3_GAS_TOWN_BEYOND_PWG_TARGET_GROUP_PLAN.md`, records: 12 (11 prompt records + final), size: 1030599 bytes.

## Smoke-test

- `work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip`: PASS; unzip_t=True; first_run=True; second_transition=True; runner_opaque=True.
- `work/theory-writing/packages/B2_PWG_CONTRIBUTION.zip`: PASS; unzip_t=True; first_run=True; second_transition=True; runner_opaque=True.
- `work/theory-writing/packages/B3_GAS_TOWN_BEYOND_PWG.zip`: PASS; unzip_t=True; first_run=True; second_transition=True; runner_opaque=True.

## Проверенные инварианты

- Каждый пакет содержит только `START.md`, `q8v4m.py`, `z3k9p.dat`.
- Видимый runner generic: в нём нет имён B-фрагментов, списков документов, prompt-текстов или предметной логики.
- Первый запуск runner-а создаёт первый рабочий лист и разрешённые входы.
- После фиктивных required outputs второй запуск создаёт другой рабочий лист.
- Payload остаётся opaque record chain; instruction-файлы имеют непрозрачные имена.
