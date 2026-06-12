# Skill: chat-github-repo-work

## Когда применять

Применяйте этот skill, когда ChatGPT работает с Git-репозиторием из чата:

- через GitHub-интеграцию;
- через snapshot/archive overlay;
- через подготовку файлов для последующего ручного commit or Codex application.

Этот skill не предназначен для Codex task/worktree execution. Для Codex используйте `protocols/skills/codex-task-work.md`.

## Что прочитать

Перед содержательным ответом or записью в репозиторий прочитайте:

```text
AGENTS.md
project/repository-structure.md
protocols/rules/chat-github-repo-work-protocol.md
```

Если задача относится к текущей рабочей ветке or `/work`, обязательно прочитайте:

```text
work/discourse.md
```

Затем оцените файлы в корне `/work` and прочитайте нужные. Если неясно, какие документы нужны, прочитайте все релевантные текстовые документы из `/work`, а не угадывайте по названиям.

## Как работать

Работайте по:

```text
protocols/rules/chat-github-repo-work-protocol.md
```

Для многофайловых задач default mode — **archive overlay**, not direct commit.

Direct commit mode используется только по явной просьбе пользователя:

```text
закоммить в <branch-name-or-description>
```

Для archive overlay:

- если пользователь дал full snapshot, работайте с файлами локально;
- перед сборкой архива назовите baseline: последний полный repo snapshot пользователя или явную commit/apply-точку;
- не считайте assistant-generated overlay новым baseline без явного указания пользователя;
- для длинных файлов используйте full-file replacement in overlay;
- если нужен итог всей текущей chat-work chain, делайте overlay кумулятивным относительно того же baseline, а не поверх предыдущего overlay;
- если делаете узкую некумулятивную дельту, прямо скажите, какие прежние uncommitted overlays она не включает;
- включайте `work/APPLY_NOTES.md`, `work/COMMIT_MESSAGE.txt`, `work/CHECKS.json`;
- давайте подробный отчёт в чате.

Новые рабочие документы создавайте в `/work` inside overlay or repository. Persistent protocol/project changes go to `/protocols`, `/project`, `/site-spec` or `/content` only after human gate.

Если работа меняет ход задачи, обновите `work/discourse.md` по `protocols/rules/discourse-maintenance-rules.md`.

## Итог

В финальном ответе укажите:

- режим: archive overlay or direct commit;
- ветку or snapshot base;
- ссылку на архив or commit SHA;
- список изменённых файлов;
- suggested commit anchor;
- как обновлён discourse;
- что делать дальше.

Если запись/архив не выполнялись, явно скажите, что изменений нет.
