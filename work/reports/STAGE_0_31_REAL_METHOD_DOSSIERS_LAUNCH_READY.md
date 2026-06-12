# Stage 0.31 — real methodology dossier source accumulation launch

Дата: 2026-06-09  
Статус: подготовлен prompt для первого реального запуска.

## Почему запуск теперь допустим

Debug test после Stage 0.30 завершился `PASS`:

```text
controller prompt
→ native worker-subagent per debug document
→ TS-loop
→ --backend sdk
→ child SDK-thread per pass
→ debug prompt
→ pass artifacts
→ should_stop after min_pass
```

Проверено:

- dry-run прошёл;
- SDK preflight прошёл;
- два native worker-subagent завершились параллельно;
- `DEBUG_ALPHA` and `DEBUG_BETA` создали pass 01 and pass 02 in root-level `passes/*`;
- оба остановились after pass 02 because `DEBUG_STOP_NOW` wrote `should_stop=yes`;
- pass 03 не создан;
- `work/automation/node_modules/`, `package-lock.json`, `work/automation/passes` and `work/automation/work` отсутствуют;
- logs show `cwdForChild` as repo root.

## Новый prompt

```text
work/prompts/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION.md
```

Он запускает реальные методологические досье:

```text
Spec Kit → work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
Kiro Specs → work/dossiers/KIRO_SPECS_DOSSIER.md
Constitutional SDD → work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
TDAD comparative → work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
GSD / Open GSD → work/dossiers/GSD_METHOD_DOSSIER.md
BMAD Method → work/dossiers/BMAD_METHOD_DOSSIER.md
```

Общие параметры:

```text
prompt = work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
mode = fresh
fresh_action = stub
min_pass = 10
max_pass = 20
backend = sdk
parallel = native subagents
network/escalated access required
```

## Защитные условия

- Не использовать nested `codex exec`.
- Не использовать `--backend cli` inside Codex.
- Не устанавливать `node_modules` inside `work/automation`.
- Не запускать worker-ов без SDK preflight.
- Не считать запуск успешным без root-level pass artifacts.
- Не модифицировать общие файлы внутри worker-subagents.
- Общий report and discourse update делает only controller after workers finish.

## Ожидаемый отчёт после запуска

```text
work/reports/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION_RESULT.md
```
