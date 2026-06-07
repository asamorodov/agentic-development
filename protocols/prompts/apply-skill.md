# Apply skill

Используйте этот prompt, когда нужно явно вызвать один из skill-файлов.

```text
Примени skill `<skill-file>` из `protocols/skills/`.

Сначала прочитай:
- AGENTS.md
- protocols/skills/<skill-file>
- protocols/rules, указанные внутри skill
- work/discourse.md, если задача относится к текущей активной работе

Задача:
<описание задачи>

Ограничения:
<что не менять / где остановиться / какой branch использовать>

В конце дай отчёт: какие файлы прочитаны, какие файлы изменены, какие проверки выполнены, как обновлён work/discourse.md, где нужен human gate.
```
