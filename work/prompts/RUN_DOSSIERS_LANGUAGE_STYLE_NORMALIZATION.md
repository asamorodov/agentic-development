# Prompt: запуск языко-стилевой нормализации досье

Запусти языко-стилевую нормализацию досье через существующий многопроходный документный процесс.

Это не source accumulation и не theory writing. Нужно только привести уже накопленные досье к русскому языку и стилю по протоколам, сохранив детали.

## Обязательное чтение controller-а

Перед запуском перечитай:

```text
work/automation/README.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/english-source-handling.md
protocols/rules/terminology-and-translation.md
protocols/rules/human-technical-style.md
protocols/rules/content-preservation.md
protocols/rules/source-and-provenance.md
work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md
```

## Важная архитектурная граница

Не меняй TS-код многопроходного документного процесса.

Режим задаётся только другим нижним prompt-ом и wrapper-ом:

```text
work/automation/run-language-style-loop.cmd
```

TS-loop по-прежнему останавливается по обычному контракту:

```text
pass >= min-pass
should_stop=yes
```

Жёсткость остановки задаёт нижний prompt: worker не должен писать `should_stop=yes`, пока в досье остаётся заметный английский связующий язык, который по протоколам должен быть русским.

## Параметры

Используй:

```text
--min-pass 10
--max-pass 20
--mode continue
```

Не запускай `fresh`.

Если у документа уже есть pass-артефакты, продолжай обычным `continue`. Не очищай существующие досье и pass-артефакты.

## Какие документы обрабатывать

Найди актуальные досье в:

```text
work/dossiers/
```

Обрабатывай рабочие досье методологий и механизмов. Не обрабатывай:

- pass snapshots;
- reports;
- временные файлы;
- общие журналы;
- `work/discourse.md`;
- `content/`.

Если есть сомнение, включать ли файл, ориентируйся на смысл: это должно быть досье, которое позже будет источником для теории/сайта.

## Запуск

Для одного досье используй форму:

```cmd
work\automation\run-language-style-loop.cmd ^
  --backend sdk ^
  --doc work/dossiers/<DOSSIER>.md ^
  --topic "<TOPIC>" ^
  --run-id dossier-language-style-<DATE> ^
  --worker-id <DOSSIER_ID>
```

Запускай волнами по 2–3 worker-а, чтобы не повторить проблему с лимитами и внешними timeout-ами.

## Что проверять после worker-ов

После завершения каждого worker-а проверь:

- достигнут ли минимум 10 проходов;
- остановился ли worker по `should_stop=yes` или дошёл до pass 20;
- созданы ли `after_pass`, `delta`, `should_stop` для последнего прохода;
- нет ли очевидной потери источников, URL, команд, имён файлов, списков иллюстраций и открытых вопросов;
- не появились ли дублирующиеся служебные разделы.

## Итоговый отчёт

Создай короткий отчёт в `work/reports/`:

```text
LANGUAGE_STYLE_NORMALIZATION_RUN_REPORT.md
```

В отчёте укажи по каждому досье:

- последний проход;
- `should_stop`;
- осталось ли что-то на ручную проверку;
- были ли обнаружены признаки деградации;
- какие документы лучше перечитать человеком перед использованием в теории.
