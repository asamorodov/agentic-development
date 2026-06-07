# Rollback working change

```text
Примени skill `protocols/skills/rollback-working-change.md`.

Репозиторий: <owner/repo>
Ветка: <branch>
Что нужно откатить: <commit / файл / описание серии изменений>

Правила:
- если ветка — `main`, сначала явно подтверди, что пользователь разрешил запись в `main`;
- предпочитать новый revert/restore commit вместо переписывания истории;
- force-update ветки запрещён без явного подтверждения;
- если откат затрагивает `/content`, source precedence, baseline restore rules, deep anchor seeds или утверждённый план — остановиться у human gate;
- если откат меняет ход рабочей задачи и в ветке есть `/work/discourse.md`, обновить `work/discourse.md`.

В конце сообщи branch, commit SHA, какие файлы восстановлены или отменены и какие риски остались.
```
