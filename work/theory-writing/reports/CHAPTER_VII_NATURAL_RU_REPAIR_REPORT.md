# Chapter VII natural-Russian repair — 2026-06-15

## Scope

Пользователь указал, что предыдущий natural-Russian pass по главе VII всё ещё оставил массу неестественных смысловых сцеплений. Главный пример: заголовок `Когда «почти готово» перестаёт быть состоянием работы`, где `готово` и `состояние` плохо соотносятся по-русски.

Выполнен более крупный редакторский проход по главе VII `VII_persistent_work_graph.md`. Это не добор источников и не перестройка главы. Цель прохода — переписать объяснительную прозу так, чтобы она читалась как нормальный русский технический текст, а не как калька с рабочих англоязычных ярлыков.

## Main changes

- Заголовок первого раздела заменён на `Почему «почти готово» не помогает продолжить работу`.
- Переписаны вводные абзацы: вместо искусственного противопоставления `почти готово` / `состояние работы` теперь говорится о том, что сводка не даёт безопасно продолжить изменение.
- Усилен русский связочный текст вокруг `summary`, `transcript`, `issue tracker`, `work item`, `gate`, `claim`, `source state`, `runtime`.
- Убраны или смягчены неестественные конструкции вроде `Summary хранит рассказ`, `Gate превращает ожидание...` в прежней механической форме, `состояние должно запрещать и разрешать действия` как плохо встроенная формула.
- Сохранены все ключевые фактические узлы главы: billing/API пример, Beads, GitHub/Linear, LangGraph/Temporal, Jökull Sólberg `/babysit-pr`, Mark Erikson, HumanLayer, Mae Capozzi, `source state`, `restoration packet`, границы с VI/VIII/IX/X.
- Ссылки, фигуры и кодовые блоки сохранены.

## Profile-term check

В основных файлах глав VII–X проверены вхождения `профайл`, `профиль`, `профили`, `профилей`, `profile`, `profiles`.

Результат: в основных текстах глав VII–X больше нет этих вхождений. В главе VIII оставшиеся объяснительные формулы `профиль восстановления длинной сессии`, `профиль фазовой передачи контекста` и `Если профиль выбран правильно` заменены на `способ восстановить длинную сессию`, `способ поэтапно передавать контекст` и `способ работы выбран правильно`. В главе IX техническая фраза про Codex `profiles` переписана через `встроенные режимы` и `permission-настройки`.

Это не означает, что слово `профиль` удалено из всех companion/pass-файлов старых глав V/III: там оно остаётся в исторических рабочих материалах. Проверка здесь относится к основным главам VII–X.

## Files changed

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/reports/CHAPTER_VII_NATURAL_RU_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

## Status

Chapter VII is now substantially more natural in Russian than after the previous broad pass. It still preserves source density and technical vocabulary where the vocabulary is a mechanism name, but the main explanatory argument no longer rests on the awkward formula that `готово` becomes or ceases to be a `state`.
