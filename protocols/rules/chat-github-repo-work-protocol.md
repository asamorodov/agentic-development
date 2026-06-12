# Протокол работы ChatGPT с репозиторием через GitHub-интеграцию и архивы

Этот протокол описывает, как ChatGPT работает с репозиторием, когда задача ведётся в чате, но результат должен стать частью Git-репозитория.

Он покрывает два режима:

1. **Direct commit mode** — ChatGPT пишет в GitHub через интеграцию and creates commits.
2. **Archive overlay mode** — ChatGPT получает snapshot репозитория or рабочей ветки, работает с файлами локально and возвращает архив-оверлей с изменениями.

Это не протокол Codex-задачи and not Codex worktree/session protocol. Для Codex используется `protocols/rules/codex-task-work-protocol.md`.

## Роль ChatGPT

ChatGPT используется для:

- смыслового обсуждения;
- архитектурных решений;
- проектирования протоколов, prompts, dossiers and reports;
- подготовки рабочих документов в `/work`;
- подготовки archive overlays для ручного применения or передачи Codex;
- точечных direct commits в `/project`, `/protocols`, `/site-spec` or `/work`, если пользователь явно просит `закоммить`;
- проверки результатов Codex and human-gate reasoning.

Тяжёлые изменения `/content`, массовый rewrite, site generation, большие diffs, повторяемые multi-pass workflows and task execution по умолчанию передаются Codex.

## Начало работы над ответом

Если ответ требует работы с текущей задачей в репозитории, ChatGPT должен начинать не с памяти текущего чата, а с чтения доступного repo context.

Перед содержательным ответом or записью ChatGPT должен:

1. Установить repository / branch / snapshot basis.
2. Прочитать `AGENTS.md`, если доступен.
3. Прочитать `project/repository-structure.md`, если доступен.
4. Если задача связана с ветками, прочитать `project/branching-and-task-model.md`.
5. Прочитать этот протокол.
6. Если задача вызывает skill, прочитать соответствующий файл из `protocols/skills/`.
7. Если задача относится к текущей ветке or `/work`, прочитать `work/discourse.md`.
8. Оценить сопутствующие документы в корне `/work` and прочитать нужные.
9. Если непонятно, какие документы нужны, прочитать все релевантные текстовые документы из корня `/work`, а не угадывать по именам.

`work/discourse.md` нельзя заменять кратким summary, commit messages, prompt-файлами or памятью chat-thread.

## Выбор режима результата

### Archive overlay mode — режим по умолчанию для многофайловой работы

По умолчанию для задач, которые создают or меняют несколько рабочих документов, ChatGPT работает в archive overlay mode.

Этот режим предпочтителен, если:

- создаётся много файлов;
- меняется `work/discourse.md`;
- нужно работать с длинными файлами;
- пользователь не хочет много раз нажимать UI approval;
- нужно подготовить результат для ручного commit;
- работа идёт через snapshot ветки;
- результат должен быть проверен перед commit.

Archive overlay mode явно включается фразами:

```text
результат в архив
без коммита
подготовь архив изменений
подготовь overlay
подготовь patch/import material
```

Если пользователь не просит прямо `закоммить`, ChatGPT должен считать archive overlay mode default.

### Direct commit mode — только по явной просьбе

Direct commit mode используется только когда пользователь явно пишет:

```text
закоммить в <branch-name-or-description>
```

Название ветки может быть неточным. Если оно не совпадает с точным именем ветки, ChatGPT должен попытаться найти подходящую ветку по названию or context. Если есть несколько правдоподобных веток, confidence низкий or target branch cannot be determined reliably, ChatGPT не должен коммитить and должен спросить.

## Archive overlay mode

### Snapshot input

Лучший input для содержательной работы через чат:

```text
git.zip / repo snapshot
```

В snapshot желательно включать:

```text
work/
project/
protocols/
content/**/*.md
site-spec/
AGENTS.md
```

Обычно не нужно включать тяжёлые бинарные assets:

```text
content/assets/**
site/**
node_modules/**
.git/**
```

Если задача касается изображений, viewer, site behavior or asset paths, assets нужно включить отдельно or дать assets-only snapshot.

Не переносить `content/assets` в корень только ради удобства чата. Это решает техническую проблему ценой смысловой путаницы and возможных поломок ссылок. Лучше использовать export/snapshot с exclude rules.

### Reading long files

Если файл доступен через snapshot, ChatGPT должен читать его как полный локальный файл.

Если файл доступен только через GitHub connector, длинные файлы читаются chunked-read режимом. Нельзя делать полную замену длинного файла, если он не был прочитан полностью and reliably.

Для длинного `work/discourse.md` предпочтительно:

- при наличии snapshot — вернуть полный обновлённый файл;
- без snapshot — вернуть append patch or ask for snapshot.

### Overlay output

Archive overlay должен иметь top-level folders that match repository paths.

Если меняется только текущая задача:

```text
work/
```

Если меняются постоянные проектные файлы:

```text
work/
protocols/
project/
content/
site-spec/
```

Archive overlay должен содержать только новые or изменённые файлы, unless user asks for full rebuilt snapshot.

### Baseline and cumulative archive rule

Базовая линия для archive overlay определяется только двумя событиями:

1. пользователь загрузил новый полный repo snapshot / `git.zip`;
2. пользователь явно сказал, что изменения применены, закоммичены или что новое состояние нужно считать базой.

Assistant-generated overlay, delta-zip, промежуточный архив результата или кэш-пакет не становятся новым baseline автоматически. ChatGPT не должен молча распаковывать предыдущий собственный overlay и считать его исходным состоянием следующей дельты.

Каждый archive overlay должен быть собран относительно текущего пользовательского baseline или явно названной commit/apply-точки. В итоговом сообщении и `work/APPLY_NOTES.md` нужно назвать эту базу.

Кумулятивность — это режим упаковки, а не перенос baseline. Если пользователь не дал новый full snapshot and не сказал, что уже сделал commit, и текущий архив должен заменить предыдущие результаты этой chat-work chain, он должен быть **кумулятивным относительно той же базовой линии**: включать все ранее принятые изменения, но вычисляться как итоговое состояние от пользовательского baseline, not as patch-on-patch поверх assistant-generated overlay.

Если пользователь просит узкую дельту по одной новой правке, ChatGPT может вернуть некумулятивный overlay только для этой правки, но должен явно сказать, что архив не включает прежние uncommitted overlays and applying it alone will not reproduce the whole current chain.

При новом full snapshot or explicit commit/apply point ChatGPT должен сменить base and начать новую chain.

### Full-file replacement

Для Markdown/protocol documents preferred mode is whole-file editing:

- прочитать полный файл;
- подготовить полный итоговый текст;
- положить полный файл в archive overlay or upload complete replacement in direct commit mode.

Не делать fragile line-only edits unless the file is small and fully visible.

### Required archive companion files

For non-trivial archive overlay include:

```text
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

`APPLY_NOTES.md` должен объяснять:

- исходный snapshot/base;
- какие файлы создать or заменить;
- какие документы были прочитаны;
- какие проверки выполнены;
- какие human gates остаются;
- как применить overlay.

`COMMIT_MESSAGE.txt` должен содержать suggested commit message / anchor.

`CHECKS.json` должен фиксировать machine-readable result state.

### Detailed chat report

После создания архива ChatGPT должен дать в чате не только ссылку, но и подробный отчёт:

- что изменено;
- почему изменено;
- какие файлы добавлены;
- какие файлы обновлены;
- какие решения зафиксированы;
- что делать дальше;
- что не делалось.

Пользователь читает отчёт в чате быстрее, чем открывает все файлы архива.

## Direct commit mode

В direct commit mode новые рабочие документы, drafts, audits, reports, intermediate plans and task-local notes создаются в репозитории, по умолчанию в `/work` целевой ветки.

Если файл меняется вне `/work`, это должно соответствовать задаче and user approval:

- `/project`;
- `/protocols`;
- `/site-spec`;
- `/content`.

Перед обновлением существующего файла в direct commit mode ChatGPT должен прочитать файл из нужной ветки and получить текущий `sha`. GitHub Contents API требует current blob SHA при обновлении; без этого можно перетереть чужую правку.

Стандартный режим для существенных документов:

```text
один изменяемый документ = один commit
```

Исключения допустимы для атомарных малых правок.

## Task-local reports and proposed decisions

Task-local reports, audits and proposed decisions по умолчанию создаются в `/work`:

```text
work/reports/...
work/decisions/...
work/dossiers/...
work/prompts/...
work/protocols/...
```

Если документ предлагает изменение approved architecture, source precedence, baseline restore rule or persistent project rule, ChatGPT должен сохранить recommendation/proposed decision in `/work` and stop for human gate.

После human approval persistent changes can be applied to:

```text
project/
protocols/
site-spec/
content/
```

## Protocol changes

Если в ходе chat-work появляется новое правило процесса, оно сначала может быть зафиксировано в `/work/reports` or `/work/protocols`.

Если правило становится общим для будущих задач, пользователь может попросить перенести его в `/protocols`. Тогда ChatGPT должен:

1. Проверить existing protocol files.
2. Выбрать минимальное место изменения.
3. Изменить persistent protocol file.
4. Обновить `work/discourse.md`, если это часть текущей рабочей ветки.
5. Добавить APPLY_NOTES / CHECKS if using archive mode.

## Обновление дискурса

Если работа изменила ход текущей задачи, ChatGPT должен обновить `work/discourse.md`:

- в direct commit mode — через commit;
- в archive overlay mode — включить полный обновлённый `work/discourse.md` в overlay, если snapshot был полным;
- если snapshot отсутствует and file is long — дать append patch or ask for snapshot.

Обновление дискурса выполняется по:

```text
protocols/rules/discourse-maintenance-rules.md
```

Для ChatGPT это особенно важно: смысловые выводы не должны оставаться только в ответе чата.

## Commit anchors

Каждый существенный commit or suggested commit message должен иметь anchor:

```text
<scope>: <action> <path> — <short-anchor>
```

Примеры:

```text
work: add stage 0.19 methodology protocol — protected-methodology-dossiers
protocols: update chat-github-repo-work-protocol.md — archive-overlay-default
work: apply approved ai-sdlc plan patch v4 — artifact-layer
```

В archive overlay mode ChatGPT указывает suggested anchor and writes it to `work/COMMIT_MESSAGE.txt`.

## Старые версии

Для сравнения со старой версией не создавать копии заранее. Использовать Git history: commit SHA + path.

Если пользователь ссылается на действие естественным языком, ChatGPT должен искать anchor in `work/discourse.md`, `work/COMMIT_MESSAGE.txt`, commit messages or reports. Если anchor неоднозначен, остановиться and ask.

## Прямая запись в main

Мелкие низкорисковые правки можно писать прямо в `main`, если пользователь явно разрешил. Крупные изменения, работа с `/work`, content architecture, source precedence, baseline restore rules, site behavior or merge logic идут через рабочую ветку or human gate.

## Human gate

ChatGPT должен остановиться и запросить подтверждение, если:

- правка в `main` не очевидно мелкая and low-risk;
- меняется source precedence;
- меняется approved plan / accepted ADR / persistent protocol;
- удаляется, сжимается or существенно переписывается большой документ;
- меняется baseline restore rule;
- правка затрагивает SPDD/Gas Town seeds;
- меняется protected methodology profile status;
- требуется merge в `main`;
- target branch for direct commit cannot be determined reliably;
- нужные документы не удаётся прочитать.

## Итог ChatGPT-ответа после direct commit

После direct commit ChatGPT сообщает:

1. Ветку.
2. Commit SHA.
3. Commit anchors.
4. Список изменённых файлов.
5. Какие документы были прочитаны.
6. Как обновлён `work/discourse.md`.
7. Какие вопросы остались открытыми.

## Итог ChatGPT-ответа после archive overlay

После archive overlay ChatGPT сообщает:

1. Ссылку на архив.
2. Что было base/snapshot.
3. Список новых/изменённых файлов.
4. Suggested commit anchor.
5. Какие документы были прочитаны.
6. Как обновлён `work/discourse.md`.
7. Что не делалось.
8. Какие вопросы/human gates остались.
9. Что делать дальше.

Если ни запись, ни архив не выполнялись, финальный ответ должен явно сказать, что изменений в репозитории нет and archive was not produced.
