# Story dossier loop patch validation

Статус: prompt-only patch проверен после anti-anchoring correction.

## Проверено

- TS-ядро многопроходного документного процесса не меняется.
- Специальных hardcoded story controls не добавлено.
- `run-story-dossier-loop.cmd` использует обычный `run-source-loop.cmd`.
- Нижний prompt не раскладывает материал по theory / Handbook / Fieldbook.
- Добавлено явное правило: не фиксировать главный смысл истории слишком рано.
- Добавлено требование держать несколько конкурирующих углов и сохранять counterfacts.
- `should_stop=yes` зависит не только от количества фактуры, но и от проверки конкурирующих рамок истории.

## Параметры режима

```text
min_pass = 10
max_pass = 20
mode = fresh
fresh_action = stub
backend = sdk
```
