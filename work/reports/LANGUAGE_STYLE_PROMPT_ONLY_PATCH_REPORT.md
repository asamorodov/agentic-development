# LANGUAGE_STYLE_PROMPT_ONLY_PATCH_REPORT

## Итог

Патч исправляет прежнее архитектурное усложнение языко-стилевого режима.

Вместо отдельного TS-флага `--language-style-control` используется исходная схема многопроходного документного процесса:

```text
тот же run-source-loop
+ другой нижний prompt
+ простой wrapper
+ min-pass 10
+ max-pass 20
+ should_stop по решению worker-а
```

## Что добавлено

```text
work/automation/run-language-style-loop.cmd
work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md
work/prompts/RUN_DOSSIERS_LANGUAGE_STYLE_NORMALIZATION.md
```

В `work/automation/README.md` добавлен раздел о языко-стилевой нормализации.

## Что намеренно не добавляется

В TS-ядро не добавляются:

```text
--language-style-control
--language-style-threshold
language-style-control.ts
watchlist/allowlist config
```

Остановка остаётся общей: `pass >= min-pass` and `should_stop=yes`.

## Если предыдущий hardcoded patch уже был применён

Удалить:

```text
work/automation/src/language-style-control.ts
work/automation/config/language-style-watchlist.txt
work/automation/config/language-style-allowlist.txt
```

Восстановить `work/automation/src/args.ts` and `work/automation/src/run-source-loop.ts` к обычной версии без language-style специальных флагов. В delta-архив включены обычные версии этих файлов для безопасного отката предыдущего патча.
