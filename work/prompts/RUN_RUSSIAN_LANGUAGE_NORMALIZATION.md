# Prompt: запуск отдельного языкового прохода по активным досье и трём новым историям

Ты работаешь в репозитории сайта. Нужно запустить многопроходную языковую нормализацию уже существующих документов.

Это не source accumulation, не writing, не rewriting, не стилевой проход, не теоретическая переработка и не поиск новых источников. Нужно только привести обычный авторский текст к русскому языку по языковому протоколу и проверить, что не потеряны детали.

## 0. Прочитай controller-level context

Сначала прочитай:

```text
AGENTS.md
project/repository-structure.md
project/source-precedence.md
work/discourse.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/discourse-maintenance-rules.md
protocols/rules/russian-language.md
work/automation/README.md
work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md
```

Не проектируй новый процесс. Не переписывай нижний prompt без явной причины. Нижний prompt уже подготовлен как `work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md`.

Важно: child-pass prompt должен читать только корректируемый документ и `protocols/rules/russian-language.md`. Controller-level чтение выше нужно только для запуска и отчётности.

## 1. Scope

Обработай только активные досье из `work/dossiers/` и три новые опубликованные истории из `content/stories/`.

Не обрабатывай:

```text
work/story_dossiers/
content/stories/01_*.md … content/stories/12_*.md
work/reports/
work/dossier-passes/
passes/
work/discourse.md
content/Theoretical_synthesis.md
content/Cross_story_synthesis.md
content/Handbook.md
content/Fieldbook.md
```

Активные досье:

```text
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
```

Не включай:

```text
work/dossiers/BMAD_METHOD_DOSSIER_COMPARISON_SNAPSHOT_2026_06_08.md
```

Три новые истории:

```text
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

Если файла нет в текущем рабочем дереве, не создавай его заново. Зафиксируй статус `missing` в итоговом отчёте и продолжай по остальным документам.

## 2. Важная техническая деталь про 5–20 проходов

`work/automation/run-source-loop.cmd` принимает `--min-pass` и `--max-pass` как абсолютные номера проходов, а не как количество новых проходов текущего запуска.

Поэтому для каждого документа перед запуском вычисли:

```text
last_pass = максимальный существующий номер в passes/<safeDocName>/*_after_pass_NN.md, если каталог существует; иначе 0
start_pass = last_pass + 1
min_pass = last_pass + 5
max_pass = last_pass + 20
```

Запускай worker с:

```text
--start-pass <start_pass>
--min-pass <min_pass>
--max-pass <max_pass>
```

Так каждый документ получает 5–20 новых языковых проходов, даже если для него уже есть старые pass-артефакты.

Не используй `fresh`. Используй только `--mode continue`.

## 3. Preflight

Создай `run_id` вида:

```text
russian-language-normalization-YYYY-MM-DD-HHMM
```

Создай таблицу целей:

```text
work/automation/runs/<run_id>/resolved-targets.csv
```

CSV columns:

```text
worker_id,topic,doc,prompt,mode,last_pass,start_pass,min_pass,max_pass,backend,status
```

Для всех существующих целей:

```text
prompt=work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md
mode=continue
backend=sdk
status=planned
```

Выполни SDK preflight:

```cmd
work\automation\sdk-probe.cmd --run-id <run_id>-preflight
```

Если preflight не проходит, не запускай worker-ы. Создай итоговый отчёт со статусом `preflight-failed`.

## 4. Dry-run

Перед настоящим запуском сделай dry-run для одного досье и одной новой истории.

Досье:

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md ^
  --doc work/dossiers/SPEC_KIT_METHOD_DOSSIER.md ^
  --topic "Spec Kit language normalization" ^
  --start-pass <start_pass_for_spec_kit> ^
  --min-pass <min_pass_for_spec_kit> ^
  --max-pass <max_pass_for_spec_kit> ^
  --mode continue ^
  --run-id <run_id>-dry-run ^
  --worker-id DRY_RUN_SPEC_KIT_LANGUAGE ^
  --dry-run
```

История:

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md ^
  --doc content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md ^
  --topic "Armin Ronacher story language normalization" ^
  --start-pass <start_pass_for_armin_story> ^
  --min-pass <min_pass_for_armin_story> ^
  --max-pass <max_pass_for_armin_story> ^
  --mode continue ^
  --run-id <run_id>-dry-run ^
  --worker-id DRY_RUN_ARMIN_STORY_LANGUAGE ^
  --dry-run
```

Dry-run должен только собрать prompt-файлы и проверить параметры. Он не должен запускать SDK child-thread.

## 5. Реальный запуск

Запускай worker-ы волнами по 2–3 документа.

Один worker работает только с одним документом.

Шаблон команды:

```cmd
work\automation\run-source-loop.cmd ^
  --backend sdk ^
  --prompt work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md ^
  --doc <doc> ^
  --topic "<topic>" ^
  --start-pass <start_pass> ^
  --min-pass <min_pass> ^
  --max-pass <max_pass> ^
  --mode continue ^
  --run-id <run_id> ^
  --worker-id <worker_id>
```

Worker не должен редактировать:

```text
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
общие отчёты
документы других тем
```

Все общие итоги пишет только controller после завершения worker-ов.

## 6. Worker id и topic

Используй такие `worker_id`:

```text
ADR_METHOD_DOSSIER_LANGUAGE
BMAD_METHOD_DOSSIER_LANGUAGE
CONSTITUTIONAL_SDD_DOSSIER_LANGUAGE
GAS_TOWN_METHOD_DOSSIER_LANGUAGE
GSD_METHOD_DOSSIER_LANGUAGE
KIRO_SPECS_DOSSIER_LANGUAGE
PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER_LANGUAGE
SPDD_METHOD_DOSSIER_LANGUAGE
SPEC_KIT_METHOD_DOSSIER_LANGUAGE
TDAD_COMPARATIVE_DOSSIER_LANGUAGE
ARMIN_RONACHER_STORY_LANGUAGE
STRIPE_MINIONS_STORY_LANGUAGE
SHOPIFY_ROAST_STORY_LANGUAGE
```

Темы:

```text
ADR Method dossier language normalization
BMAD Method dossier language normalization
Constitutional SDD dossier language normalization
Gas Town Method dossier language normalization
GSD / Open GSD dossier language normalization
Kiro Specs dossier language normalization
Persistent Work Graph dossier language normalization
SPDD Method dossier language normalization
Spec Kit Method dossier language normalization
TDAD Comparative dossier language normalization
Armin Ronacher story language normalization
Stripe Minions story language normalization
Shopify Roast story language normalization
```

## 7. Проверки после каждого worker-а

Для каждого документа проверь:

1. выполнено ли не меньше 5 новых проходов относительно `last_pass`;
2. где остановился документ: `should_stop=yes` или достигнут `max_pass`;
3. создан ли последний `*_after_pass_NN.md`;
4. создан ли последний `*_delta_NN.md`;
5. создан ли последний `*_should_stop_NN.txt`;
6. нет ли явной потери ссылок, URL, команд, имён файлов, источников, кандидатов на иллюстрации, технических деталей и открытых вопросов;
7. не были ли созданы служебные разделы внутри основного документа;
8. не была ли проведена стилевая или теоретическая переработка вместо языковой нормализации;
9. не были ли добавлены новые источники или внешние факты.

Если worker испортил документ или потерял детали, не скрывай это в отчёте. Зафиксируй документ как `manual-review-needed`.

## 8. Итоговый отчёт

После завершения всех worker-ов создай:

```text
work/reports/RUSSIAN_LANGUAGE_NORMALIZATION_RUN_REPORT.md
```

В отчёте укажи по каждому документу:

```text
doc
worker_id
last_pass_before_run
start_pass
last_pass_after_run
new_pass_count
should_stop
status
manual_review_needed
notes
```

Статусы:

```text
completed-stopped
completed-max-pass-not-stopped
failed
missing
manual-review-needed
preflight-failed
```

Отдельно перечисли:

- документы, где остался допустимый английский только как имена, команды, пути, URL, названия источников или устойчивые технические имена;
- документы, где остался спорный английский;
- документы, где есть риск потери деталей;
- документы, которые лучше перечитать вручную перед использованием в теории.

## 9. Обновление служебных файлов

После отчёта controller обновляет:

```text
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

В `work/discourse.md` зафиксируй только смысловой поворот:

- запущен отдельный языковой проход, не стилевой;
- нижний prompt читает только корректируемый документ и `protocols/rules/russian-language.md`;
- обработаны активные досье и три новые истории;
- стиль оставлен для отдельного будущего прохода;
- детали и ссылки должны сохраняться;
- если какой-то документ ушёл в `manual-review-needed`, назови его прямо.

В `work/checks.json` добавь сведения о запуске, количестве документов, статусах и проверке валидности отчёта.

Проверь:

```cmd
python -m json.tool work/checks.json
```

## 10. Финальное сообщение

В финальном ответе напиши:

- какие документы обработаны;
- сколько новых проходов по каждому;
- где `should_stop=yes`;
- где нужен ручной review;
- какие файлы созданы/обновлены;
- что это был только языковой проход, без стилевой переработки и без source accumulation.
