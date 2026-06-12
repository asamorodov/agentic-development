# План мануфактуры target-group plans для статей концептуально-технического атласа

Статус: рабочий план для будущего repo-bound meta-package, который создаёт и улучшает target-group plans для dossier-backed статей атласа.

Назначение: зафиксировать процесс, который **не пишет сами статьи атласа** и **не собирает executor packages для статей**, а последовательно создаёт планы этих статей: для каждой заранее известной dossier-backed статьи сначала пишет target-group plan, затем несколько раз улучшает именно этот план, фиксирует readiness и только потом переходит к следующей статье.

## 1. Среда выполнения

Этот meta-package должен запускаться на машине с уже развёрнутым репозиторием. Пользователь не должен отдельно подавать входные архивы, досье, source maps или assets.

Исполнитель обязан брать всё из файловой системы репозитория:

- `START.md`;
- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`;
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md`;
- `work/discourse.md`;
- `work/dossiers/*.md`;
- `work/dossier-passes/` and `work/methodology-passes/`;
- `work/theory-writing/fragments/`;
- `work/theory-writing/asset-catalog/`;
- `content/assets/`;
- relevant protocols and rules.

Если какой-то ожидаемый файл отсутствует, исполнитель не должен просить пользователя загрузить его вручную. Он должен зафиксировать отсутствие в readiness/status report и продолжить там, где это безопасно.

## 2. Уровень задачи

Этот план работает на уровне **создания планов**, а не написания статей.

Он должен создавать target-group plan, который позже будет использован для сборки отдельного article-writing package. Поэтому в рамках meta-package нельзя:

- писать саму статью атласа;
- добывать материал из досье как будто уже пишется статья;
- искать и вставлять изображения в статью;
- скачивать assets;
- создавать технический атлас или article map вместо плана;
- собирать executor package для статьи, если это прямо не запрошено отдельной задачей.

Но target-group plan, который создаётся этим процессом, обязан **заложить** все эти действия в будущий article-writing package: source-depth проходы, свободные доборные проходы, visual asset passes, внешние image candidates, companion sync, редакторские проходы, язык, стиль и финальную проверку.

Создаваемые target-group plans должны быть пригодны для сборки **независимых self-contained article-writing packages**. Это значит: все read-only inputs будущего пакета должны быть названы конкретными путями и упакованы вместе с ним при сборке. План не должен полагаться на расплывчатые формулы вроде `relevant files`, `related dossiers`, `asset catalog as needed` или на неоговорённый контекст развёрнутого репозитория. Если вход нужен будущей статье, он должен быть перечислен как read-only input / bundled input; если вход пока неизвестен, это readiness debt, а не скрытая зависимость.

## 3. Список статей: только dossier-backed set

Список статей не придумывается во время выполнения и не расширяется внешним поиском. В текущей версии атласа статьи строятся только по уже собранным досье. Досье — основной источник и основание существования статьи. Внешние источники могут быть разрешены внутри будущего article-writing plan как дополнение, проверка, уточнение и поиск изображений, но они не создают новую статью без отдельного решения пользователя.

Текущий known dossier-backed set:

| Article id | Рабочее название статьи | Основное досье | Предварительный тип |
|---|---|---|---|
| `spdd_method` | SPDD / OpenSPDD | `work/dossiers/SPDD_METHOD_DOSSIER.md` | core concept / method article |
| `spec_kit_method` | Spec Kit | `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | method / tool-form article |
| `kiro_specs` | Kiro Specs | `work/dossiers/KIRO_SPECS_DOSSIER.md` | tool/form article |
| `constitutional_sdd` | Constitutional SDD | `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | method article |
| `tdad_comparative` | TDAD | `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | method article |
| `adr_method` | ADR as method / decision memory | `work/dossiers/ADR_METHOD_DOSSIER.md` | method article |
| `gsd_open_gsd` | GSD / Open GSD | `work/dossiers/GSD_METHOD_DOSSIER.md` | method article |
| `bmad_method` | BMAD | `work/dossiers/BMAD_METHOD_DOSSIER.md` | method article |
| `persistent_work_graph` | Persistent Work Graph / Beads | `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | core concept article |
| `gas_town` | Gas Town | `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | core concept / organizational article |

Если в репозитории есть дополнительные досье, не входящие в этот список, исполнитель должен вынести их в `unplanned_dossiers` внутри отчёта, но не создавать для них article plan без явного решения пользователя.

## 4. Глобальные шаги meta-package

### G01 — ориентация в репозитории

Открыть `START.md`, этот документ, blueprint статей атласа, карту документов, discourse, правила визуального слоя, правила языка/стиля, правила repo overlay, правила target-group/package workflow.

Цель: работать из текущего репозитория, а не из памяти и не из внешнего списка.

### G02 — проверка known dossier-backed set

Проверить наличие всех dossier files из таблицы выше. Создать/обновить:

```text
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_LEDGER.md
```

В ledger зафиксировать:

- article id;
- dossier path;
- dossier exists / missing;
- предполагаемый output path target-group plan;
- preliminary status;
- known sync debts: `C5 sync pending`, `A10 sync pending`, если актуально.

Не добавлять новые article topics из внешнего поиска.

### G03 — подготовка выходных путей

Создать директории, если их нет:

```text
work/atlas/target-group-plans/
work/atlas/plans/
work/atlas/plans/reports/
```

Стандартный путь target-group plan:

```text
work/atlas/target-group-plans/<article_id>_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Стандартный путь per-article report:

```text
work/atlas/plans/reports/<article_id>_target_plan_manufacture_report.md
```

## 5. Цикл для одной статьи

Каждая статья проходит полный цикл до readiness stamp. Только после этого исполнитель переходит к следующей статье.

### S01 — создать первичный target-group plan статьи

Создать полный target-group plan для конкретной dossier-backed статьи.

Перед написанием plan-а исполнитель обязан сделать короткую ориентацию именно по этой статье: открыть основное досье, связанные фрагменты теории, asset catalog, relevant companion files и зафиксировать рабочее понимание темы. Это **не добыча материала для статьи** и **не написание статьи**; это подготовка к планированию, чтобы plan не стал механической копией blueprint. Article planning note не должен превращаться в конспект статьи или черновик atlas article.

S01 должен быть idempotent / rerun-safe:

- если target-group plan для статьи уже существует, не перезаписывать его слепо;
- сначала прочитать существующий plan и определить режим: `create_new`, `repair_existing`, `replace_because_invalid`;
- если plan заменяется, объяснить причину в per-article report / S01 note;
- не терять ручные правки пользователя, если они уже есть в plan-е; при сомнении предпочесть `repair_existing` и явно отметить debt.

В начале создаваемого target-group plan должен быть блок `Article contract`:

```text
Article contract
- reader question
- article tier
- primary dossier
- central claim / central explanation
- what this article explains itself
- neighboring articles and likely boundaries, where relevant
- required source-depth emphases
- required visual/asset emphases
- exact read-only inputs to bundle in future article package
- theory links
- known sync debts
```

План должен опираться на `ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` как сильный default, но не обязан механически иметь ровно 25 проходов. Количество проходов выбирается по сложности статьи и по тому, что будущая article-writing модель должна усилить, добавить или проверить.

Обязательные ограничения для initial plan:

- не вводить внутренний лимит объёма статьи;
- статья должна быть самостоятельной concept-first article;
- общие редакторские проходы обязательны;
- source-depth / free material expansion / visual assets / concept reinforcement / companion sync / language / style / final verification должны быть представлены в очереди, если нет сильного специального основания сузить статью до source note;
- локальные релевантные assets должны вставляться в будущую статью;
- внешние реальные image candidates должны быть разрешены и оформлены как asset-pass queue;
- собственные схемы допустимы редко и только при нетривиальной пользе;
- C5/A10 могут быть optional sync inputs, но не должны без причины блокировать создание article plan;
- все read-only inputs будущего article-writing package должны быть перечислены конкретными путями и позже упакованы с этим package; никаких placeholder-формул вроде `relevant dossier files` без точного списка.

S01 пишет сам plan file, а не report-only заметку.

### S02 — адресное усиление plan-а

Прочитать созданный target-group plan и выполнить все явные усиления, которые уже понятны из задачи статьи, blueprint и article contract.

S02 — не свободный проход и не написание статьи. Он должен адресно усилить plan как будущий инструмент получения хорошей статьи:

- уточнить `Article contract`, если он слишком общий;
- усилить reader question и центральное объяснение статьи;
- проверить направление: **подходит ли выбранная очередь проходов именно этой статье?**;
- адаптировать source-depth / free expansion / visual asset / concept reinforcement / final verification проходы к конкретной статье, а не оставить их копией blueprint;
- проверить, что plan ведёт к самостоятельной concept-first статье, а не к technical appendix, пересказу досье или повтору общей теории;
- проверить, что plan не потерял dossier-backed основание;
- уточнить границы с соседними статьями там, где это действительно помогает будущей статье, но не превращать boundary work в самоцель;
- проверить, что local assets, external image candidates and synthetic-figure rules встроены в plan с учётом темы статьи;
- проверить, что в plan-е нет скрытого лимита объёма, `keep concise`-логики или формулировок, провоцирующих конспект.

S02 обязан исправить найденные дефекты прямо в target-group plan и записать, что именно изменено.

### S03 — свободное редакторское усиление plan-а

Прочитать target-group plan после S02 как сильный редактор, без заранее заданной темы проверки.

Формула прохода:

> Оцени, приведёт ли этот plan к сильной самостоятельной статье атласа. Сначала сформулируй главные проблемы plan-а, затем исправь их.

S03 должен сохранить свободу модели. Он не обязан следовать заранее заданному чек-листу и должен сам определить, что мешает plan-у стать сильным: слабая постановка, слишком механическая очередь, недобор будущих проходов, плохая финальная проверка, лишняя бюрократия, слабая article-specific адаптация, опасное дублирование, плохая работа с визуальным слоем или что-то другое.

S03 обязан исправить найденные дефекты прямо в target-group plan и кратко зафиксировать изменения.

### S04 — integrated guardrail repair plan-а

Проверить, что target-group plan содержит все встроенные требования к будущему article-writing package, и **сразу исправить всё найденное**.

S04 объединяет в один проход то, что не стоит расписывать как отдельные длинные проверки для каждого plan-а:

- source-depth требования действительно заставят раскрыть досье, а не написать обзор;
- свободные доборные проходы не декоративны;
- external sources разрешены как supplement, особенно для картинок, но не создают новые article topics;
- local assets не могут быть проигнорированы из-за того, что тяжёлые файлы не переданы в package;
- external-real image candidates имеют inline placeholder и нижний раздел для asset-pass;
- synthetic figures ограничены usefulness/nontriviality gate;
- companion outputs заданы и синхронизируются;
- exact path grounding соблюдён: read-only inputs, target outputs, supporting outputs and asset/catalog files названы конкретными путями, без `relevant files` placeholders;
- package buildability проверяема: все входы будущего article-writing package перечислены для bundling; каждый prompt record сможет иметь required outputs; final verification проверяет реальные files; нет ссылок на будущие файлы, которые не создаются раньше в очереди; нет рассинхрона длинных/коротких имён companion-файлов;
- нет `keep concise`, лимитов объёма или формулировок, провоцирующих конспект;
- нет механического копирования blueprint без адаптации к этой статье.

Если S04 находит дефект, он не ограничивается записью в report. Он должен исправить сам target-group plan и затем кратко зафиксировать, что изменено.

### S05 — readiness stamp для plan-а

Поставить статус plan-у и перейти к следующей статье.

Возможные статусы:

```text
ready_for_package_manufacture
ready_for_package_manufacture_after_manual_review
ready_with_c5_sync_pending
ready_with_a10_sync_pending
ready_with_minor_debts
ready_with_boundary_debts
blocked_by_missing_dossier
blocked_by_unclear_article_goal_or_dossier_basis
deferred
```

`ready_for_package_manufacture_after_manual_review` означает: технически plan уже можно превратить в executor package, но перед этим человеку желательно утвердить article contract, tier, границы или спорный sync/debt. Это не blocker уровня missing dossier.

Неясные границы с соседними статьями сами по себе не должны блокировать plan, если цель статьи, reader question и dossier-backed основание заданы ясно. В таком случае boundary debt фиксируется как долг, а не как blocker. Блокер возникает только тогда, когда неясна сама статья: что она должна объяснить, на какое досье опирается или почему она имеет право на самостоятельную article package.

В per-article report зафиксировать:

- какой режим использован в S01: `create_new`, `repair_existing` или `replace_because_invalid`;
- какие проблемы были найдены в S02–S04;
- что именно исправлено;
- какие долги остались;
- можно ли по этому plan собирать executor package;
- какие sync-pass нужны после C5/A10, если они ещё не готовы.

## 6. Финальные шаги после всех статей

### F01 — cross-plan consistency and anti-template repair

Прочитать все созданные target-group plans вместе и исправить несогласованности.

Проверить:

- все планы работают с dossier-backed article set;
- никто не добавил article topic без досье;
- правила объёма, источников, изображений, local assets, external images and synthetic figures согласованы;
- обязательные общие редакторские проходы присутствуют в каждом plan-е;
- границы соседних статей не конфликтуют там, где они действительно важны для ясности будущих статей;
- одинаковые companion roles называются одинаково;
- C5/A10 sync statuses не противоречат друг другу;
- планы не стали механическими копиями blueprint или друг друга: у каждого должен быть свой reader question, article-specific source-depth focus, visual/asset priority, final verification and central article logic.

Если найден конфликт или слишком шаблонный plan, F01 должен исправить соответствующие target-group plans, а не только записать проблему.

### F02 — final readiness matrix and report

Создать/обновить:

```text
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_READINESS_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLANS_MANUFACTORY_REPORT.md
```

В readiness matrix указать:

- article id;
- dossier path;
- target-group plan path;
- readiness status;
- package manufacture allowed / blocked;
- sync debts;
- asset/readiness caveats;
- priority suggestion.

Boundary matrix фиксирует:

- что статья объясняет сама;
- что оставляет соседним статьям;
- где допустим повтор;
- где повтор будет дублированием;
- какие semantic back-links ожидаются.

Final report должен объяснить, какие планы можно сразу превращать в executor packages, какие требуют sync после C5/A10, какие заблокированы и почему.

## 6.5. Минимальный quality bar для `ready_for_package_manufacture`

Plan нельзя пометить `ready_for_package_manufacture`, если:

- `Article contract` отсутствует или написан настолько общо, что не задаёт будущую статью;
- нет dossier-specific source-depth требований;
- visual/asset work описан общими словами и не учитывает локальные assets / external image candidates;
- read-only inputs будущего package не перечислены конкретными путями или не предназначены для bundling;
- нет свободных доборных проходов;
- нет обязательных общих редакторских проходов;
- есть внутренний лимит объёма, `keep concise` или аналогичная логика сокращения;
- final verification не проверяет конкретные риски этой статьи;
- plan выглядит как механическая копия blueprint без article-specific адаптации.

Неясные границы с соседними статьями не являются автоматическим blocker-ом, если цель статьи и её dossier-backed основание заданы ясно. Такой долг фиксируется как `ready_with_boundary_debts`, `ready_with_minor_debts` или `ready_for_package_manufacture_after_manual_review`. Блокировать нужно только тогда, когда неясна сама статья: её reader question, концептуальная цель или право на отдельную статью.

## 7. Финальная проверка meta-package

Финальная проверка должна подтвердить:

- все known dossier-backed articles обработаны;
- для каждой существующей dossier-backed статьи создан target-group plan или зафиксирован блокер;
- каждый plan прошёл S01–S05;
- S02 сделал адресные усиления, S03 сделал свободное редакторское усиление;
- S04 исправлял найденные дефекты, а не только отчётировал;
- каждый созданный plan содержит exact read-only input paths и пригоден для self-contained package bundling;
- не создано article topics без досье;
- не написаны сами статьи атласа;
- не собраны article executor packages, если это не было отдельно запрошено;
- readiness matrix, boundary matrix, ledger and final report созданы;
- START/discourse/WORKING_DOCUMENTS_MAP updated according to protocol;
- итоговый overlay / result package не содержит временных executor files в корне.

## 8. Принцип качества

Цель meta-package — не просто создать много target-group plans, а снизить будущую механическую доводку статей атласа. Хороший результат означает, что после запуска article-writing package пользователь должен в основном обсуждать смысл, интерпретацию, границы и акценты статьи, а не чинить базовые проблемы: недобор досье, игнор картинок, служебные captions, короткий обзор вместо большой статьи, неправильные companion files, отсутствие редакторских проходов или неясную reader question.
