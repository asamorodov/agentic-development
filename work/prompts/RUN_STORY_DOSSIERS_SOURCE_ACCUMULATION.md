# Prompt: run story dossier source accumulation for six candidate stories

Ты работаешь в репозитории `agentic-development`.

Нужно запустить накопление досье для шести кандидатных историй через многопроходный документный процесс, но без `fresh`-режима. Ничего не обнуляй. Каждый native worker-subagent должен выполнять ровно один pass и завершаться: controller-thread запускает проходы волнами — pass 01 для всех активных историй, затем pass 02, и так далее до pass 20 или до `should_stop=yes` после pass 10.

Схема:

```text
controller prompt
→ round N
→ native worker-subagent per active story
→ one TS-loop invocation for exactly pass N
→ --backend sdk
→ child SDK-thread for that pass
→ pass artifacts
→ worker exits
→ controller checks should_stop and starts next round
```

Это не методологические досье. Не используй `METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md`. Используй только:

```text
work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
```

## Backend and access

Использовать:

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

Если SDK preflight не проходит, не запускать workers.

## Что прочитать в controller-thread

Прочитай, если файлы есть в репозитории:

```text
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/terminology-and-translation.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
work/automation/README.md
work/reports/RUN_SDK_SUBAGENTS_TEST_RESULT_STAGE_0_30.md
work/discourse.md
```

Не нужно читать первоисточники в controller-thread. Источники читают child SDK-thread проходы внутри каждого one-pass worker.

## Целевые документы

Используй этот mapping.

```text
Shopify Roast
→ work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
→ worker_id: SHOPIFY_ROAST_STORY_DOSSIER

Product Migration with Claude Code
→ work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
→ worker_id: PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER

Quix / Klaus Kode
→ work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
→ worker_id: QUIX_KLAUS_KODE_STORY_DOSSIER

Armin Ronacher
→ work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
→ worker_id: ARMIN_RONACHER_STORY_DOSSIER

Zig no-AI policy
→ work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
→ worker_id: ZIG_NO_AI_POLICY_STORY_DOSSIER

Stripe Minions
→ work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
→ worker_id: STRIPE_MINIONS_STORY_DOSSIER
```

Если в `work/discourse.md` или других project files явно указан другой canonical path для story dossiers, остановись и сообщи конфликт. Не переноси документы в `work/dossiers/`: этот каталог уже занят методологическими досье.

## No-fresh guard

В этом запуске **не использовать `fresh` вообще**.

Запрещено передавать:

```text
--mode fresh
--fresh-action stub
```

Все реальные проходы запускаются только через:

```text
--mode continue
```

Перед pass 01 проверь целевые файлы. Если какой-то файл отсутствует, создай минимальный stub обычной файловой операцией controller-thread, не через `fresh` и не перезаписывая существующие файлы:

```md
# <Story title> — story dossier

Working source-backed dossier for future story writing.

## Рабочая карта

## Эпизоды

## Источники и provenance

## Кандидаты на иллюстрации

## Открытые вопросы

## Синтез
```

Если целевой файл уже существует, не трогай его перед запуском. Если уже есть `passes/<worker_id>/`, определи последний pass по существующим artifacts и продолжай с `--start-pass <last_pass + 1>`. Не удаляй и не переносить pass artifacts.

Если не можешь уверенно определить last_pass, остановись и сообщи конфликт, а не запускай `fresh`.

## Параметры режима

Общая цель: 10–20 проходов.

Каждый worker-subagent запускается только на один pass:

```text
pass N invocation:
  --mode continue
  --start-pass N
  --min-pass N
  --max-pass N
```

Для pass 01 тоже использовать только `continue`:

```cmd
work\automation\run-story-dossier-loop.cmd ^
  --backend sdk ^
  --doc <doc> ^
  --topic "<topic>" ^
  --run-id <run_id> ^
  --worker-id <worker_id> ^
  --mode continue ^
  --start-pass 1 ^
  --min-pass 1 ^
  --max-pass 1
```

Для pass N, где N >= 2:

```cmd
work\automation\run-story-dossier-loop.cmd ^
  --backend sdk ^
  --doc <doc> ^
  --topic "<topic>" ^
  --run-id <run_id> ^
  --worker-id <worker_id> ^
  --mode continue ^
  --start-pass N ^
  --min-pass N ^
  --max-pass N
```

После pass 10 controller может перестать запускать worker, если latest `should_stop_NN.txt = yes`. До pass 10 игнорируй `should_stop=yes` как premature: minimum is 10 passes.

Если после pass 20 `should_stop=no`, зафиксируй worker как completed-max-pass-not-stopped, не запускай дальше.

## Preflight and trace

Создай `run_id` вида:

```text
story-dossiers-source-accumulation-YYYY-MM-DD-HHMM
```

Сохрани trace:

```text
work/automation/runs/<run_id>/resolved-targets.csv
```

CSV columns:

```text
worker_id,topic,doc,prompt,mode,min_pass,max_pass,fresh_action,backend,pass_strategy
```

Для mapping укажи:

```text
mode=continue
fresh_action=none
pass_strategy=one-subagent-per-pass-no-fresh
```

Затем выполни SDK preflight with network/escalated access:

```cmd
work\automation\sdk-probe.cmd --run-id <run_id>-preflight
```

## Dry-run sanity check

Перед настоящим запуском сделай dry-run в отдельном dry-run namespace, чтобы не загрязнить real worker status:

```cmd
work\automation\run-story-dossier-loop.cmd ^
  --backend sdk ^
  --doc work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md ^
  --topic "Shopify Roast" ^
  --run-id <run_id>-dry-run ^
  --worker-id DRY_RUN_SHOPIFY_ROAST_STORY_DOSSIER ^
  --mode continue ^
  --start-pass 1 ^
  --min-pass 1 ^
  --max-pass 1 ^
  --dry-run
```

Dry-run должен только собрать prompt file and verify parameters. Он не должен запускать SDK child-thread.

## Реальный запуск: one-pass rounds

Не запускай один worker на 10–20 проходов. Не выполняй все документы в controller-thread.

Для каждого pass number запускай native worker-subagents параллельно only for active workers.

Для любого pass N используй только command pattern с `--mode continue`:

```cmd
work\automation\run-story-dossier-loop.cmd ^
  --backend sdk ^
  --doc <doc> ^
  --topic "<topic>" ^
  --run-id <run_id> ^
  --worker-id <worker_id> ^
  --mode continue ^
  --start-pass N ^
  --min-pass N ^
  --max-pass N
```

Worker не должен редактировать:

```text
work/discourse.md
work/CHECKS.json
work/APPLY_NOTES.md
общие отчёты
документы других тем
```

Все общие итоги пишет только controller после завершения rounds.

## Проверки после каждого round

Для каждого active worker после pass N должны появиться:

```text
passes/<worker_id>/<worker_id>_after_pass_NN.md
passes/<worker_id>/<worker_id>_delta_NN.md
passes/<worker_id>/<worker_id>_should_stop_NN.txt
```

Если artifacts отсутствуют, worker failed for that round. Не запускай следующий pass для failed worker until причина понятна.

Если `N >= 10` and `should_stop_NN.txt = yes`, пометь worker как stopped_by_should_stop and не запускай его в следующих rounds.

If any worker creates artifacts under `work/automation/passes/`, this is FAIL.

If any worker uses `--backend cli`, this is FAIL.

If any command line contains `--mode fresh` or `--fresh-action`, this is FAIL.

## Финальный отчёт

Создай:

```text
work/reports/RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION_RESULT.md
```

В отчёте должно быть:

```text
status: PASS / PARTIAL / FAIL
run_id
preflight result
dry-run result
pass_strategy: one-subagent-per-pass-no-fresh
per-worker status:
  worker_id
  topic
  doc
  first_pass
  last_pass
  stopped_by_should_stop
  completed_max_pass_not_stopped
  failed_rounds
  status_file
  logs_dir
  backup_dir
failed workers
wrong-location artifacts check
node_modules/package-lock pollution check
real docs changed list
no-fresh guard notes
stub-created-if-missing notes
```

Обнови `work/discourse.md` короткой записью о результате: что запускали, какие темы прошли, где лежит итоговый report. Не вставляй в discourse длинные логи.

## Что считать PASS

PASS только если:

- preflight прошёл;
- dry-run прошёл;
- all six story dossiers reached at least pass 10;
- every worker either stopped by `should_stop=yes` after pass 10 or reached pass 20 without инфраструктурного сбоя;
- artifacts are in `passes/<worker_id>/`;
- no artifacts are created under `work/automation/passes/`;
- no real command used `--mode fresh` or `--fresh-action`;
- `work/automation/node_modules/` is absent;
- `work/automation/package-lock.json` is absent unless already intentionally added by a separate decision;
- real story dossiers were updated only through their own one-pass worker-subagents;
- no real chapters, theory files, old stories, shared dossiers, source maps or content files were modified by workers.

If some workers pass and some fail, status is `PARTIAL`, not `PASS`.
