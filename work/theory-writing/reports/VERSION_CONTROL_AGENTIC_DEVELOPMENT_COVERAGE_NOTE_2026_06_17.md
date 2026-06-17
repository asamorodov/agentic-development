# Контроль версий в агентской разработке: coverage gap и решение по Атласу

Дата: 2026-06-17.  
Статус: принятое решение после обсуждения разрезов Теории / Атласа / Handbook / Fieldbook.  
Связанное решение: `work/decisions/ADR-0013-git-version-control-agentic-change-substrate.md`.

## Короткий вывод

Контроль версий сейчас покрыт в репозитории как внутренний рабочий протокол проекта, но недостаточно покрыт как самостоятельный слой знания для agentic development.

Практический baseline для современной агентской разработки — Git и Git-совместимый workflow. Это не значит, что альтернативы концептуально невозможны. Но текущая экосистема coding agents, PR/MR review, CI/status checks, protected branches, worktrees, GitHub/GitLab-подобные поверхности и исследования agent-authored PR в основном предполагают Git-субстрат.

Поэтому формула должна быть аккуратной:

```text
Git — практическая база современного agentic development workflow.
Не потому, что других VCS в принципе не существует,
а потому что рабочие поверхности, агенты, PR/MR, CI и review tooling завязаны на Git-совместимую модель изменения.
```

Jujutsu, Sapling и другие варианты могут быть интересны как Git-compatible или Git-adjacent слои работы с изменениями. Но для Атласа и Handbook они должны рассматриваться через вопрос: как они взаимодействуют с Git/PR/CI/review контуром, а не как полная замена всей экосистемы.

## Решение

Git/version-control слой должен стать отдельной статьёй Атласа, а не обязательным разделом внутри статьи про CI/review/acceptance tooling.

Рабочее название:

```text
Git, worktree и PR/MR как субстрат агентского изменения
```

Главный вопрос статьи: как агентский результат получает форму change candidate, которую можно изолировать, сравнить, показать человеку, проверить, обсудить, принять, отклонить, откатить и использовать как provenance.

Статья про CI/status checks/review/acceptance gates должна быть соседней, а не поглощающей. Её предмет — какие технические и человеческие gates применяются к уже оформленному change candidate.

## Что уже есть в репозитории

Уже есть рабочие документы для собственного процесса проекта:

```text
project/branching-and-task-model.md
protocols/rules/git-branching-and-merge-protocol.md
```

Они описывают `main`, рабочие ветки, worktrees, `/work`, перенос устойчивых материалов из `/work` в постоянные папки, merge в `main`, rollback и human gate.

В теоретических главах Git/worktree/PR тоже уже появляется как часть среды исполнения и принятия результата, особенно вокруг worktree, sandbox, PR, CI, review и merge.

Но это пока не равно системному покрытию version-control слоя как отдельной темы agentic development.

## Чего не хватает

Нужен отдельный слой, который показывает Git/version-control не как обычную инфраструктуру разработки, а как рабочий субстрат агентского изменения.

Ключевые темы:

1. **Единица изменения.** Diff, patch, commit, branch, worktree, PR/MR, merge/revert как разные формы материала, который можно показать человеку, проверить, откатить или принять.

2. **Изоляция агентской работы.** Branch/worktree per task или per agent; отдельные рабочие деревья для параллельных агентов; граница между рабочей директорией, индексом, commit history и sandbox.

3. **Параллельная агентская работа.** Несколько агентов могут производить пересекающиеся изменения. Git даёт branches/worktrees/merge/rebase/cherry-pick/conflict surface, но не решает semantic conflict сам по себе.

4. **Коммит как checkpoint.** Частые маленькие commit-ы помогают сохранять состояние, сравнивать варианты, откатывать неудачные шаги и передавать работу следующему исполнителю. Но плохая commit history может наоборот маскировать агентские ошибки.

5. **PR/MR как change container.** Pull request / merge request соединяет diff, обсуждение, review comments, checks, approvals, linked issue, audit trail и решение о merge.

6. **Branch protection и status checks.** Required checks, protected branches, rulesets и merge queue превращают часть проверки в технический gate до merge. Это соседний слой с Git-substrate: он должен быть связан, но не должен поглощать саму тему version control.

7. **Откат и восстановление.** Revert, rollback через новый commit, file restore, bisect, сравнение веток, восстановление из известного commit. Reset/force push для агентской работы должен быть редким и требовать явного human gate.

8. **Provenance и accountability.** Git history, PR discussion, CI logs и review comments создают материал для последующего разбора: кто или что изменило код, какие проверки были выполнены, что было принято человеком, а что только предложено агентом.

9. **Что Git не решает.** Git не заменяет sandbox, permissions, secret handling, тесты, product acceptance, domain review, observability agent run и post-merge monitoring.

## Маршрутизация по публичным частям

- **Теория:** Git/PR/worktree используются как материал для жизненного цикла изменения: как рабочий след становится diff/branch/PR, как PR входит в контур проверки и принятия, как revert возвращает изменение в жизненный цикл.
- **Атлас:** Git/version-control — самостоятельный технический слой: конкретные объекты, команды, форматы, платформенные поверхности и критерии выбора branching/worktree/PR режима.
- **Handbook:** выбор режима: когда делать отдельную ветку, когда worktree, когда PR, когда squash, когда commit checkpoint, когда запретить force push, когда нужен reviewer gate.
- **Fieldbook:** сбои: агент испортил рабочую директорию, смешал задачи в одной ветке, потерял diff, сделал слишком большой PR, зелёный CI проверил не тот риск, rebase скрыл историю, force push уничтожил материал для разбора.

## Последствие для theory skeleton

Новая Git-статья не требует добавлять отдельную главу в Теорию. Теория остаётся построенной по жизненному циклу изменения. Git должен появляться как сквозной технический субстрат в главах VI, IX, XI, XII и XIII.

Отдельно зафиксировано в `work/theory-writing/reports/THEORY_SKELETON_IMPLICATIONS_AFTER_ATLAS_CUTS_2026_06_17.md`.
