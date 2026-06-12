# LANGUAGE_STYLE_PROMPT_ONLY_PATCH_VALIDATION

## Проверено

- `work/automation/src/args.ts` не содержит `languageStyleControl`.
- `work/automation/src/run-source-loop.ts` не содержит special-case language-style stop logic.
- `work/automation/run-language-style-loop.cmd` вызывает обычный `run-source-loop.cmd`.
- Нижний prompt содержит условия `should_stop` and anti-degradation contract.
- Режим настроен на `min-pass 10` and `max-pass 20`.

## Проверка целостности

Этот patch не меняет универсальный loop engine. Он добавляет новый способ запуска через prompt/wrapper.
