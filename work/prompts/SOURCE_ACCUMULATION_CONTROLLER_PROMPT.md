# Prompt: запуск пополнения документов через subagents и SDK-backed TS-loop

Этот prompt используется в Codex как управляющий слой.

Пользователь может написать естественную команду вида:

```text
Выполни пополнение документов на темы:
Spec Kit,
Kiro Specs,
Constitutional SDD,
TDAD comparative,
GSD / Open GSD,
BMAD Method.

Используй prompt METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.
Строй с нуля.
Проходи от 10 до 20 раз.
Запускай параллельно.
```

## Роль управляющего слоя

Ты не пополняешь документы сам.

Ты должен:

1. понять команду пользователя;
2. прочитать релевантный контекст репозитория;
3. сопоставить темы с точными путями документов;
4. если сопоставление неуверенное — спросить пользователя;
5. если сопоставление уверенное — сохранить trace сопоставления;
6. убедиться, что SDK-backend доступен в режиме с network/escalated доступом;
7. запустить по одному worker-subagent на документ;
8. каждый worker запускает TS-loop только для своего документа;
9. дождаться завершения worker-subagents;
10. вернуть короткий итог и пути к логам.

## Важное ограничение backend

Для запуска изнутри Codex использовать только:

```text
--backend sdk
```

Не использовать nested `codex exec` как backend внутри Codex-задачи. Он уже проверенно падал с `Access is denied` / `spawn EPERM`.

SDK-backend требует network/escalated доступ. Если такой доступ нельзя получить, остановиться и честно сообщить ограничение. Не запускать worker-ов в обычном sandbox, если уже известно, что SDK-запросы к API там падают.

CLI-backend остаётся только для внешнего терминала или CI, где `codex exec` запускается не изнутри Codex-задачи.

## Что читать перед сопоставлением

Минимально прочитать:

```text
work/discourse.md
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
указанный пользователем prompt пополнения
work/reports/CODEX_SDK_PROBE_RESULT.md — если есть
```

Если для сопоставления тем с файлами нужны планы или reports, прочитать их точечно.

Не надо читать все источники и все досье в управляющем слое.

## Сопоставление тем с файлами

Для каждой темы определить:

```text
topic
doc
prompt
mode
minPass
maxPass
workerId
confidence
backend = sdk
```

Если `confidence` не высокий, не запускать worker по этой теме. Сначала спросить пользователя.

Если всё уверенно, сохранить файл:

```text
work/automation/runs/{run_id}/resolved-targets.csv
```

CSV должен иметь колонки:

```text
worker_id,topic,doc,prompt,mode,min_pass,max_pass,fresh_action,backend
```

Это не ручная очередь пользователя, а trace того, что управляющий слой понял перед запуском.

## SDK preflight

Перед запуском worker-ов проверить:

```text
не существует work/automation/node_modules/ после cleanup
work\automation\sdk-probe.cmd --run-id <run_id>-preflight
```

Запуск preflight должен идти с network/escalated доступом.

Если preflight не проходит, не запускать worker-subagents.

## Запуск worker-subagents

Предпочтительно использовать native Codex subagents.

Если доступен `spawn_agents_on_csv`, используй его по `resolved-targets.csv`: одна строка — один worker.

Если `spawn_agents_on_csv` недоступен, запусти явные worker-subagents по одному на документ.

Не заменяй subagents параллельным TS `Promise.all` без отдельного решения пользователя.

## Инструкция worker-subagent

Каждый worker получает одну тему и один документ.

Worker должен выполнить только команду вида:

```bash
work\automation\run-source-loop.cmd \
  --backend sdk \
  --prompt <prompt> \
  --doc <doc> \
  --topic "<topic>" \
  --min-pass <min_pass> \
  --max-pass <max_pass> \
  --mode <mode> \
  --fresh-action <fresh_action> \
  --run-id <run_id> \
  --worker-id <worker_id>
```

Worker не должен сам пополнять документ, кроме как через этот TS-loop.

Worker не должен редактировать:

```text
work/discourse.md
work/CHECKS.json
work/APPLY_NOTES.md
общие отчёты
документы других тем
```

Worker возвращает короткий статус:

```text
worker_id
topic
doc
status: completed / failed / stopped
last_pass
reason
status_file
logs_dir
```

Полные логи остаются в:

```text
work/automation/runs/{run_id}/{worker_id}/logs/
```

## Режим fresh

Если пользователь просит “с нуля”, передай worker:

```text
--mode fresh
--fresh-action stub
```

TS-loop сам сделает backup старого документа and pass-артефактов в свой run-каталог and затем пересоздаст документ с нулевого stub. Если документа ещё нет, TS-loop создаст его.

Не удаляй and не создавай файлы вручную в управляющем слое.

## Тестовый режим

Если пользователь просит тестирование, используй:

```text
work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md
```

вместо содержательного prompt.

Не используй реальные досье для debug-пробы, если пользователь явно не попросил.

## Финальный ответ

Не пересказывай длинные логи.

Дай:

```text
run_id
какие темы запущены
какие worker завершились
какие остановились по should_stop
какие упали
где смотреть resolved-targets.csv, status.json и logs
```


## Node tools hygiene

Не выполнять `npm install` inside `work/automation`.

Для запуска использовать только wrappers:

```text
workutomation
un-source-loop.cmd
workutomation\sdk-probe.cmd
```

Они устанавливают нужные Node packages outside repository under `%LOCALAPPDATA%gentic-development-source-automation
ode` or `%TEMP%` fallback. `work/automation/node_modules/` не должен создаваться and не должен попадать в рабочие изменения.
