# Первая задача для Codex

Этот prompt рассчитан на рабочую ветку, где уже есть `/work/discourse.md`. Для чистого `main` без `/work` уберите из списка чтения `work/discourse.md` и вопросы про `/work`.

```text
Осмотри репозиторий без правок.

Прочитай:

- README.md
- AGENTS.md
- project/repository-structure.md
- project/source-precedence.md
- site-spec/README.md
- protocols/README.md
- protocols/rules/codex-task-work-protocol.md
- work/discourse.md

Затем дай короткий отчёт:

1. Как ты понимаешь назначение папок /content, /site, /site-spec, /protocols, /project и /work.
2. Какую роль играет work/discourse.md и почему в нём должны сохраняться точные имена значимых файлов/артефактов.
3. Какие документы ты прочитал бы перед правкой сайта.
4. Какие документы ты прочитал бы перед задачей по перестройке теории.
5. Какие действия ты считаешь рискованными и требующими planning-only pass.

Никаких файлов не меняй.
```


Перед выполнением задачи также проверьте, есть ли подходящий reusable skill в `protocols/skills/`, и если есть — прочитайте его перед правками.
