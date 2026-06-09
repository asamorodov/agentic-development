# Prompt: run SDK backend + subagents test

Ты работаешь в репозитории `agentic-development` на ветке `work/theory-ai-sdlc-rebuild`.

Нужно проверить не рабочее пополнение досье, а тестовую связку:

```text
Codex controller
→ native subagent per debug document
→ TS loop
→ --backend sdk
→ child SDK-thread per pass
→ debug prompt
→ pass artifacts
→ should_stop
```

Не запускай реальные методологические досье, истории, главы теории or source maps.

## Обязательное условие

Этот тест должен выполняться с network/escalated доступом.

SDK probe уже показал:

```text
без escalation: FAIL на API request
с escalation: PASS
```

Поэтому не начинай обычный non-escalated run. Если network/escalated доступ недоступен, остановись and верни `FAIL`.

## Что прочитать

Сначала прочитай:

```text
work/discourse.md
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/prompts/DEBUG_SOURCE_ACCUMULATION_PROMPT.md
work/prompts/SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
work/automation/README.md
work/reports/CODEX_SDK_PROBE_RESULT.md
```

Если `work/reports/CODEX_SDK_PROBE_RESULT.md` отсутствует, прочитай последние SDK-probe artifacts under:

```text
work/automation/runs/
```

## Что выполнить

Выполни тестовый сценарий из:

```text
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
```

Особенно важно:

1. сделать dry-run для `DEBUG_ALPHA`;
2. выполнить SDK preflight with escalation;
3. запустить два native worker-subagent параллельно:
   - `DEBUG_ALPHA`
   - `DEBUG_BETA`
4. каждый worker должен запускать только TS-loop:
   ```bash
   npx tsx work/automation/src/run-source-loop.ts ...
   ```
   с параметром:
   ```text
   --backend sdk
   ```
5. каждый worker должен работать только со своим debug-документом and своим namespace.

## Что нельзя делать

- Не использовать nested `codex exec`.
- Не использовать `--backend cli` inside Codex.
- Не заменять native subagents на ручной последовательный запуск, если subagents доступны.
- Не редактировать реальные досье.
- Не редактировать реальные главы/истории.
- Не обновлять общий theory plan.
- Не имитировать pass artifacts.
- Не считать тест успешным, если pass artifacts не созданы дочерними SDK-thread проходами.

## Что проверить

Для каждого debug-документа должны быть созданы:

```text
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_01.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_01.txt
passes/DEBUG_ALPHA/DEBUG_ALPHA_after_pass_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_delta_02.md
passes/DEBUG_ALPHA/DEBUG_ALPHA_should_stop_02.txt
```

и аналогично для `DEBUG_BETA`.

Так как темы содержат `DEBUG_STOP_NOW`, после обязательного второго прохода loop должен остановиться. Pass 03 не должен быть создан.

Также проверить:

```text
work/automation/runs/<run_id>/DEBUG_ALPHA/status.json
work/automation/runs/<run_id>/DEBUG_BETA/status.json
work/automation/runs/<run_id>/DEBUG_ALPHA/logs/
work/automation/runs/<run_id>/DEBUG_BETA/logs/
```

## Отчёт

В конце дай короткий отчёт:

```text
status: PASS / FAIL / INCONCLUSIVE
run_id:
dry-run:
sdk preflight:
subagents:
DEBUG_ALPHA:
  passes:
  should_stop:
  logs:
DEBUG_BETA:
  passes:
  should_stop:
  logs:
errors:
```

Если subagents недоступны as native Codex mechanism, не подменяй тест последовательным запуском. Верни `INCONCLUSIVE` or `FAIL` and explain exact limitation.

Если SDK backend fails without or despite escalation, верни `FAIL` and include exact stderr/stdout/status path.


## Stage 0.30 repair expectations

Этот повторный тест должен проверять repair после предыдущего FAIL:

```text
DEBUG_BETA previously wrote artifacts under work/automation/passes instead of root passes.
```

Теперь worker должен использовать updated TS-loop:

- repo root определяется automatically or passed by wrapper;
- process cwd is set to repo root before SDK child thread;
- prompt contains both repo-relative and absolute artifact paths;
- wrappers install Node tools outside repository, not under work/automation/node_modules.

Перед запуском удали старые wrong-location artifacts if present:

```text
work/automation/passes/
work/automation/work/
```

И не выполняй `npm install` inside `work/automation`.
