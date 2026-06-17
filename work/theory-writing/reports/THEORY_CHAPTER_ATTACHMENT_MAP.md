# Карта приложений к главам Теории

Статус: живой рабочий документ для синхронизации Теории с Атласом, фрагментами и досье.  
Дата: 2026-06-17.  
Основание: Skeleton V6.3, `00_spine_map`, ADR-0012, ADR-0013, ADR-0014, новая карта Атласа `work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md`.

## Назначение

Этот документ отвечает на практический вопрос: что именно нужно прикладывать к каждой главе Теории, чтобы она была технически заземлена, но не превращалась в мини-Атлас.

`Прикладывать` здесь не значит механически вставлять разделы Атласа в главу. Это значит: chapter package должен заранее знать, какие статьи Атласа, фрагменты, досье, истории и внешние источники являются обязательными входами для данной главы, какие работают как gap-check, а какие нельзя разворачивать, чтобы не украсть материал соседней главы.

Документ должен синхронизироваться каждый раз, когда меняется карта Атласа A1–A19, принимается новый theory-ready fragment, меняется граница главы или добавляется новая сквозная рамка вроде Harness Engineering.

## Правило использования

Для каждой главы пакет должен пройти три вопроса:

```text
1. Какие технические слои Атласа заземляют тезис главы?
2. Какие фрагменты и старые A/B/C-синтезы должны быть прочитаны как доноры?
3. Где граница: что упомянуть в Теории, но оставить подробному Атласу, Рабочим сценариям или Каталогу проблем и решений?
```

Если текущий target-group plan противоречит этой карте, план нужно обновить перед новым запуском пакета.

## Условные обозначения

- `Atlas core` — слой Атласа, без которого глава рискует стать пустой методологией.
- `Atlas support` — слой, который нужен точечно.
- `Fragment core` — фрагмент, который должен реально войти в аргумент главы.
- `Gap-check` — материал для проверки потерь, не для полного пересказа.
- `Boundary` — что не раскрывать здесь.

## Карта глав

| Глава | Функция | Atlas core | Fragment core | Gap-check / anchors | Boundary |
| --- | --- | --- | --- | --- | --- |
| INTRO | Ввести жизненный цикл программного изменения как рамку корпуса. | A1, A2, A8; точечно A6/A7. | `00_spine_map`, A1, A10. | Cross-story; Boris/Peter/Calvin/Mark. | Не объяснять технические слои и не писать обзор инструментов. |
| I | Зафиксировать, что через проект проходит изменение, а не prompt или diff. | A1, A6, A8; support A2. | A1, A10, `00_spine_map`. | SPDD/Spec Kit/Kiro/BMAD как короткие примеры носителей. | Не делать главу о Git или specs. |
| II | Показать, что сессия оставляет trace, но не удерживает долгоживущее состояние. | A2, A5, A1; support A6. | A6_execution_environment_distinctions, A7_observation_vs_evidence. | Simon/Arvid/Jökull/Armin; trace/browser/devtools candidates. | Достаточность проверок — XI; tracing platforms — A5. |
| III | Развести намерение, спецификацию, контракт и решение. | A8, A1; старые ADR/SPDD/Spec Kit/Kiro/CSDD nodes. | A2, A3, B1, C1. | ADR/SPDD/Spec Kit/CSDD dossiers. | Testing/confirmation и CODEOWNERS не разворачивать. |
| IV | Показать SPDD как спецификационный жизненный цикл. | `spdd_method.md`, A8. | B1, C1, `00_spine_map`. | SPDD dossier/source usage. | Не пересказывать всю статью Атласа. |
| V | Показать соседние защищённые спецификационные режимы. | A8, Spec Kit, Kiro, TDAD, CSDD. | A3, C1. | Method dossiers for Spec Kit/Kiro/TDAD/CSDD. | Не делать полную verification chapter. |
| VI | Показать проект как рабочую опору изменения. | A1, A8, A6; support A4. | A4, A6, C4. | Kiro/GSD/BMAD/PWG dossiers; context/interface stories. | Не превращать главу в A1. |
| VII | Объяснить durable work state: work item, relations, recovery. | PWG article, A8, A6; support A5. | B2, C2, C3, C4. | PWG dossier; Jökull/Mark/HumanLayer/Mae. | Не превращать PWG в orchestration framework. |
| VIII | Показать защищённые процессные профили. | A8, A3, GSD/Open GSD, BMAD; support A1/A4. | A5, B3, C2. | GSD/BMAD/Gas Town dossiers; Jesse/HumanLayer/Mae/Shopify/Matt. | Не делать Рабочие сценарии / Handbook. |
| IX | Развести среду действия, runtime, tools, permissions, sandbox и approval. | A2, A4, A6; support A3/A5. | A6, C4. | GSD/BMAD/PWG/Gas Town + Armin/Stripe/Shopify/HumanLayer. | Не писать security handbook; проверка — XI, завершение — XII. |
| X | Показать организационно-операционный слой параллельной агентской работы. | Gas Town article, A3, A8; support A6/A7. | B3, C2, C4. | Gas Town dossier; Jökull/Stripe/Shopify/Mae. | Качество результата — XI; не делать UI-tour. |
| XI | Связать обещание изменения с проверочным материалом и его границами. | A5, A7; support A6/A8. | A7_observation_vs_evidence, C3, ex-A3. | TDAD/ADR/CSDD evidence dossiers; Simon/Arvid/Jökull/HumanLayer/Mike/Shopify; external discovery. | Не принимать решение за XII; не писать technical Atlas A7 внутри Теории. |
| XII | Развести право действовать и право признать изменение завершённым. | A4, A7, A6; support A8. | A8_authority_to_act_vs_complete, A2, C3, ex-A3. | ADR/CSDD/policy dossiers; CODEOWNERS/provenance materials. | Не моральная глава; не повторять XI. |
| XIII | Показать, что merge не завершает lifecycle, если среда устарела. | A1, A6, A7, A8; support A5. | A9, C1–C4, ex-A3. | Relevant method dossiers; Matt/Jesse/HumanLayer/Mark/Shopify. | Не сводить к техдолгу или списку «обновить документы». |
| CONCLUSION | Свести Теорию к выбору минимально достаточной структуры. | Весь A1–A19 как reference layer, без пересказа. | A10, `00_spine_map`, routing maps. | SPDD, PWG, Gas Town, ADR как deep nodes. | Не превращать conclusion в Рабочие сценарии. |

## Развёрнутые примечания к ключевым стыкам



### Новые слои A9–A15

После расширения Атласа до A15 chapter packages должны использовать новые слои выборочно:

- **A9 / среды исполнения и песочницы**: особенно важен для IX, XI и XIII, где нужно показать среду действия, возможность проверки и восстановление после неудачного прогона.
- **A10 / извлечение контекста из кодовой базы**: важен для VI, VII и II, когда речь идёт о проекте как рабочей опоре, выборе нужного кода и границах того, что агент реально увидел. Shotgun должен проверяться как отдельный источник при подготовке A10 и связанных theory chapters.
- **A11 / issue-to-agent**: важен для X, XII и XIII, а также для будущих `Рабочих сценариев`, потому что показывает, как задача становится агентской рабочей единицей, а не свободным prompt.
- **A12 / долгая память проекта**: важен для II, VII и XIII. В Теории он должен использоваться как техническое заземление долговременного состояния и восстановления, но не как публичный вывод о Нoveia.
- **A13 / безопасность и supply chain**: важен для IX и XII, где обсуждаются действие, полномочие, проверка и право признать изменение завершённым.
- **A14 / Browser/GUI/app feedback**: важен для IX, XI и XIII, где нужно показать, что обратная связь может приходить не только из кода и тестов, но и из rendered app, screenshot, accessibility snapshot, devtools и визуального review.
- **A15 / model-provider layer**: использовать осторожно и только с датированными источниками. Он может заземлять II, IX и XI, но не должен превращать Теорию в обзор текущего рынка моделей.

- **A16 / organizational context, software catalog and developer portal**: использовать там, где глава говорит об ownership, service boundaries, platform wrapper, environments, runbooks, organizational metadata, self-service actions or team/platform governance. Он может заземлять VI, IX, XII, XIII и Conclusion, но не должен превращать Теорию в обзор Backstage/Port-like portals.

Общее правило: если глава Теории нуждается в конкретной технологии, она упоминает слой и даёт минимально достаточную связку; полное техническое описание остаётся в соответствующей статье Атласа.



### Новые слои A17–A19

После второго coverage check Атлас расширяется до A19. Для Теории это не создаёт новых глав, но меняет техническое заземление нескольких уже существующих глав:

- **A17 / структурированная обратная связь от программы**: особенно важен для XI, IX and XIII. Он помогает не сводить проверочный материал только к тестам или CI: compiler/typechecker/LSP/debugger/static-analysis/runtime-log signals являются отдельным feedback/sensor layer.
- **A18 / автономное тестирование и QA-артефакты**: особенно важен для XI and XIII; точечно для III/VIII, когда речь идёт об acceptance criteria, воспроизводимости bugs, regression tests and tests generated by agents. Теория должна использовать этот слой как техническое заземление проверки, но не писать каталог testing tools.
- **A19 / release, deployment, production monitoring and incident/remediation agents**: особенно важен для XIII and Conclusion; support для XII. Он закрепляет, что merge не конец lifecycle: deployment, monitoring, incident response, rollback/remediation and learning-back loops продолжают изменение.

Граница: Теория может ссылаться на эти слои как на доказательство того, что feedback and post-merge loops are technically real, но полное сравнение инструментов, артефактов and gates остаётся Атласу.

### Ex-A3

`work/theory-writing/fragments/ex_a3_agent_run_to_accepted_change_theory_fragment.md` — донор для XI, XII и XIII. Его нельзя переносить как целую главу. Правильное использование:

- XI берёт различение trace/check/review material и границы доказательства;
- XII берёт ladder статусов: accepted / rejected / needs changes / superseded / unknown;
- XIII берёт хвост post-merge / revert / rollback / repair route.

### Git layer

A6 `Git, worktree и PR/MR` заземляет VI, IX, XI, XII и XIII. Но Теория не должна превращаться в учебник Git. В главе нужно использовать Git-объекты как носители статуса изменения: diff, branch, worktree, commit, PR/MR, review state, merge, revert.

### Atlas technical grounding

Каждый future chapter package должен создавать или обновлять свой `*_atlas_usage.md` из этой карты. В этом файле нужно явно указать:

```text
какие слои Атласа использованы
какие только упомянуты
какая техническая деталь оставлена Атласу
какая глава/раздел не должен забирать соседний материал
```

## Синхронизация

Эта карта должна обновляться при каждом из следующих событий:

1. меняется список A1–A19 или назначение статьи Атласа;
2. новая статья Атласа принята или отклонена;
3. появляется theory-ready fragment вроде ex-A3;
4. меняется target-group plan главы Теории;
5. пользователь принимает новое решение о публичных названиях частей корпуса.

Минимальный closeout после таких изменений:

```text
обновить ATLAS_V2_LAYER_ARTICLE_MAP.md
обновить THEORY_CHAPTER_ATTACHMENT_MAP.md
обновить WORKING_DOCUMENTS_MAP.md
обновить work/discourse.md
обновить APPLY_NOTES.md
```

Старые карты `POST_ATLAS_*` остаются полезными, но эта карта имеет приоритет для будущих пакетов после решений ADR-0012/0013/0014.


### Harness Engineering as a skeleton frame and retrofit patch rule

После ADR-0018 будущие chapter packages должны читать:

```text
work/theory-writing/reports/HARNESS_ENGINEERING_THEORY_SKELETON_NOTE_2026_06_17.md
```

Harness Engineering не добавляет новую главу и не меняет основной lifecycle-разрез Теории. Он вводит сквозную рамку: модель действует не сама по себе, а через рабочую обвязку — проектный контекст, инструменты, filesystem, sandbox, browser/app feedback, orchestration, memory, task state, traces, evals, permissions, review gates and recovery loops.

Все ретроспективные патчи к уже написанным главам должны фиксироваться здесь, в `THEORY_CHAPTER_ATTACHMENT_MAP.md`, а не в отдельных параллельных patch maps. Причина простая: Atlas layers, ex-A3, старые фрагменты, Harness Engineering and future source attachments должны согласовываться в одной карте, иначе chapter packages начнут получать несколько несовместимых маршрутизаторов.

#### Минимальный harness-retrofit для уже написанных глав I–X

Ретрофит должен быть небольшим. Его задача — не переписать главы, а проверить, не объясняют ли они успех/сбой агентской разработки только качеством модели там, где реальная причина лежит в рабочей обвязке: контексте, инструментах, среде, правах, проверках, памяти, состоянии задачи or acceptance gates.

Перед правкой любой уже написанной главы package должен показать короткий patch list и остановиться на human checkpoint:

```text
1. Где глава сейчас может выглядеть так, будто всё зависит только от модели?
2. Какие элементы рабочей обвязки реально участвуют в её аргументе?
3. Какие 1–3 точечные правки нужны в тексте?
4. Какие companion-файлы нужно обновить: atlas_usage, source_register, readiness_report, open_questions?
5. Какие технические детали должны остаться Атласу?
```

Ориентиры по уже написанным главам:

- **I**: уточнить, что единица анализа — программное изменение внутри проектной системы, а не prompt, run, diff or model output.
- **II**: показать, что trace возникает из взаимодействия модели с tools, terminal, files, tests, browser/app feedback and environment state, а не только из диалога.
- **III**: представить specification/ADR/contract как feedforward-слой обвязки: они заранее задают задачу, ограничения, основание решения and completion boundary.
- **IV**: показать SPDD как пример проектирования рабочей петли вокруг спецификации, не заменяя SPDD термином Harness Engineering.
- **V**: уточнить, что protected specification profile задаёт режим работы агента: context, checks, rights, radius of action and gates.
- **VI**: сделать явным, что repository, rules, docs, specs, ADR, AGENTS/CLAUDE/Kiro steering, skills, hooks, MCP and subagents образуют рабочую обвязку, через которую агент понимает проект.
- **VII**: показать PWG как durable state layer внутри более широкой обвязки, не растворяя его в общей memory-теме.
- **VIII**: показать process profile как выбор формы обвязки под риск и задачу, не превращая главу в `Рабочие сценарии`.
- **IX**: особенно явно сказать, что tools, MCP, filesystem, sandbox, browser, approvals and permissions are runtime substrate, not accessories.
- **X**: показать Gas Town as organizational scaling of harness: roles, queues, backpressure, recovery, local histories, beaded work units and responsibility boundaries, не превращая главу в A16.

Для ещё не написанных XI–XIII это не retrofit, а обычное условие написания:

- **XI**: verification material как feedback/sensor layer: traces, tests, diagnostics, static analysis, browser feedback, evals.
- **XII**: acceptance как social-technical gate: harness can produce evidence/routes, but does not itself grant completion.
- **XIII**: post-merge monitoring, rollback, cleanup, memory/rules update как feedback into future harness.

Граница: Теория использует Harness Engineering как рамку, но не перечисляет весь набор компонентов. Подробная техническая декомпозиция остаётся в Атласе. Ретрофит не должен массово вставлять английский термин `Harness Engineering` в русский текст и не должен ухудшать уже удачные главы ради новой рамки.
