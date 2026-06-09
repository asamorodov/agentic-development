# Prompt: run real methodology dossier source accumulation

Ты работаешь в репозитории `agentic-development` на ветке `work/theory-ai-sdlc-rebuild`.

Нужно запустить реальное пополнение методологических досье через уже проверенную схему:

```text
controller prompt
→ native worker-subagent per document
→ TS-loop
→ --backend sdk
→ child SDK-thread per pass
→ methodology dossier source accumulation prompt
→ pass artifacts
→ should_stop after min_pass
```

Это уже не debug-test. Но запуск всё равно должен быть аккуратным: без имитации проходов, без nested `codex exec`, без установки `node_modules` в репозиторий.

## Обязательный backend and access

Использовать только:

```text
--backend sdk
```

Запуск должен выполняться с network/escalated доступом.

Не использовать:

```text
--backend cli
codex exec
npm install inside work/automation
```

SDK backend already passed the debug subagents test only with escalated/network access. Если такой доступ недоступен, остановись и верни `FAIL`.

## Что прочитать перед запуском

Прочитай:

```text
project/repository-structure.md
project/source-precedence.md
protocols/rules/discourse-maintenance-rules.md
work/discourse.md
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
work/prompts/SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
work/automation/README.md
work/reports/RUN_SDK_SUBAGENTS_TEST_RESULT_STAGE_0_30.md
```

Не нужно читать все первоисточники в controller-thread. Источники должны читать child SDK-thread проходы внутри каждого worker.

## Целевые документы

Используй этот mapping как ожидаемый.

Если целевой файл отсутствует and режим запуска `fresh`, это нормально: worker должен создать его заново через TS-loop (`--mode fresh --fresh-action stub`). Не останавливай запуск только из-за отсутствия файла.

Остановись и спроси пользователя только если текущий discourse or project files явно говорят, что для темы есть другой canonical path, либо если mapping конфликтует с уже существующей структурой репозитория.

```text
Spec Kit
→ work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
→ worker_id: SPEC_KIT_METHOD_DOSSIER

Kiro Specs
→ work/dossiers/KIRO_SPECS_DOSSIER.md
→ worker_id: KIRO_SPECS_DOSSIER

Constitutional SDD
→ work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
→ worker_id: CONSTITUTIONAL_SDD_DOSSIER

TDAD comparative
→ work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
→ worker_id: TDAD_COMPARATIVE_DOSSIER

GSD / Open GSD
→ work/dossiers/GSD_METHOD_DOSSIER.md
→ worker_id: GSD_METHOD_DOSSIER

BMAD Method
→ work/dossiers/BMAD_METHOD_DOSSIER.md
→ worker_id: BMAD_METHOD_DOSSIER
```

Для `TDAD comparative` слово `comparative` относится к устройству этого конкретного досье: оно должно уточнять two TDAD variants. Не превращай этот запуск в общий сравнительный проход по всем методологиям.

## Параметры запуска

Для всех документов:

```text
prompt = work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
mode = fresh
fresh_action = stub
min_pass = 10
max_pass = 20
backend = sdk
```

`fresh` означает: TS-loop делает backup старого документа и pass-артефактов in its run-folder, затем пересоздаёт документ с нулевого stub and starts passes. Если документа ещё нет, TS-loop создаёт его. Не удаляй and не создавай целевые документы вручную in controller-thread.

## Preflight

Создай `run_id` вида:

```text
methodology-dossiers-source-accumulation-YYYY-MM-DD-HHMM
```

Сохрани trace запуска:

```text
work/automation/runs/<run_id>/resolved-targets.csv
```

CSV columns:

```text
worker_id,topic,doc,prompt,mode,min_pass,max_pass,fresh_action,backend
```

Затем выполни SDK preflight with network/escalated access:

```cmd
work\automation\sdk-probe.cmd --run-id <run_id>-preflight
```

Если preflight не проходит, не запускать worker-subagents.

## Dry-run sanity check

Перед настоящим запуском сделай dry-run для одного документа, например `SPEC_KIT_METHOD_DOSSIER`:

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md ^
  --doc work/dossiers/SPEC_KIT_METHOD_DOSSIER.md ^
  --topic "Spec Kit" ^
  --min-pass 10 ^
  --max-pass 20 ^
  --mode fresh ^
  --fresh-action stub ^
  --run-id <run_id> ^
  --worker-id SPEC_KIT_METHOD_DOSSIER ^
  --dry-run
```

Dry-run должен только собрать prompt files and verify parameters. Он не должен запускать SDK child-thread.

## Реальный запуск

Запусти native worker-subagents параллельно: один worker на один документ.

Если Codex subagent concurrency не позволяет запустить все шесть одновременно, запускай волнами, но всё равно через native worker-subagents, not through one controller-thread doing all work.

Каждый worker должен выполнить только свою команду:

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md ^
  --doc <doc> ^
  --topic "<topic>" ^
  --min-pass 10 ^
  --max-pass 20 ^
  --mode fresh ^
  --fresh-action stub ^
  --run-id <run_id> ^
  --worker-id <worker_id>
```

Worker не должен редактировать:

```text
work/discourse.md
work/CHECKS.json
work/APPLY_NOTES.md
общие отчёты
документы других тем
```

Все общие итоги пишет только controller after workers finish.

## Что проверить после каждого worker

Для каждого target должны появиться pass artifacts in root-level namespace:

```text
passes/<worker_id>/<worker_id>_after_pass_10.md
passes/<worker_id>/<worker_id>_delta_10.md
passes/<worker_id>/<worker_id>_should_stop_10.txt
```

Если `should_stop_10.txt = yes`, worker may stop at pass 10. Если `no`, loop continues until `yes` or pass 20.

If any worker creates artifacts under `work/automation/passes/`, this is FAIL.

If any worker produces no pass artifacts, this is FAIL.

If any worker uses `--backend cli`, this is FAIL.

## Финальный отчёт

Создай:

```text
work/reports/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION_RESULT.md
```

В отчёте должно быть:

```text
status: PASS / PARTIAL / FAIL
run_id
preflight result
dry-run result
per-worker status:
  worker_id
  topic
  doc
  first_pass
  last_pass
  stopped_by_should_stop
  status_file
  logs_dir
  backup_dir
failed workers
wrong-location artifacts check
node_modules/package-lock pollution check
real docs changed list
```

Обнови `work/discourse.md` короткой записью о результате: что запускали, какие темы прошли, где лежит итоговый report.

Не вставляй в discourse длинные логи.

## Что считать PASS

PASS только если:

- preflight прошёл;
- dry-run прошёл;
- все six worker-subagents completed or stopped by `should_stop`;
- each worker made at least pass 10;
- artifacts are in root-level `passes/<worker_id>/`;
- no artifacts are created under `work/automation/passes/`;
- `work/automation/node_modules/` is absent;
- `work/automation/package-lock.json` is absent unless already intentionally added by a separate decision;
- реальные досье updated only through their own worker-subagent;
- no real chapters, stories, source maps, or shared theory files were modified by workers.

If some workers pass and some fail, status is `PARTIAL`, not `PASS`.

## После завершения

Не коммить автоматически.

Верни короткий ответ пользователю:

```text
status
run_id
workers completed / partial / failed
where to inspect report
where to inspect logs
whether it is safe to proceed to human review
```
