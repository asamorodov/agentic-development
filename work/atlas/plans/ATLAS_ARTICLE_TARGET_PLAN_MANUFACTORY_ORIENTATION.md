# Ориентация: manufactury target-group plans для статей концептуально-технического атласа

Статус: рабочая ориентация для текущего meta-package.  
Основание: `START.md`, `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`, `work/theory-writing/WORKING_DOCUMENTS_MAP.md`, `work/discourse.md`, `work/decisions/ADR-0011-concept-first-technical-atlas.md`, правила визуального слоя, языково-стилевые правила и протоколы package/target-group plans.  
Оговорка: файл `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md`, указанный в рабочем листе G01, в текущем repo snapshot не найден. Ориентация построена по остальным обязательным документам и по самому рабочему листу G01.

## 1. Назначение текущего meta-package

Текущий пакет не пишет статьи атласа и не собирает исполнительные article-writing packages. Его задача раньше по цепочке: создать и улучшить `target-group plans` для заранее известного набора статей концептуально-технического атласа.

Каждый такой план должен быть достаточно точным, чтобы позже по нему можно было собрать self-contained writing package для конкретной статьи. Это означает, что план должен заранее зафиксировать целевые файлы, точные read-only input paths, роль досье и первоисточников, визуальные правила, companion-файлы, порядок 25 проходов и финальную проверку.

Meta-package работает как плановая мануфактура: для каждой статьи он проходит цикл S01–S05, постепенно переходя от контракта статьи к готовому плану, затем проверяет этот план на buildability, полноту входов, отсутствие article-writing leakage и готовность к ручному просмотру.

## 2. Обязательные правила

Главное решение ADR-0011: технический атлас теперь является концептуально-техническим атласом. Статья атласа должна быть самостоятельной связной статьёй по конкретной концепции, методологии, механизму или инструментальной форме: SPDD, PWG / Beads, Gas Town / Beads, GSD, BMAD, TDAD, Spec Kit, Kiro, ADR и соседним узлам. Атлас не является узким приложением с командами и скриншотами, но и не должен превращаться во вторую общую теорию.

Для большой статьи атласа применяется `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`: базовая очередь — 25 рабочих проходов плюс отдельная финальная проверка. Очередь включает первичный черновик, article contract, dossier inventory, пять source-depth проходов, два свободных прохода добора материала, три visual asset passes, три concept reinforcement passes, три общих редакторских прохода, public/article structure pass, companion sync, два языковых и два стилевых прохода.

Для статьи атласа запрещены внутренние ограничения объёма. План не должен заранее сжимать будущую статью ради компактности. Объём будущей статьи определяется полнотой раскрытия концепции, источниковой фактурой, техническими деталями, изображениями, ограничениями и границами применения.

Все планы должны сохранять provenance. Внутренние досье являются quarry-материалом, но публичные ссылки в будущей статье должны вести на первоисточники, указанные или выводимые из досье. Если первоисточник не удаётся восстановить, план должен предусмотреть gap/source-pass, а не разрешать гладкую неподтверждённую прозу.

Визуальный слой проходит asset-classification gate до любой inline-вставки или переписывания. Возможные статусы: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate`, `editorial_visual_idea`. Локальный готовый asset вставляется в будущую статью как `<figure><img ...></figure>`; внешний реальный screenshot/source diagram/UI-image до asset-pass ставится как `external-real-candidate` placeholder и выносится в external image queue. Готовые изображения нельзя заменять текстовой схемой. Собственные схемы допустимы только при явной нетривиальной пользе.

Язык планов и будущих prompt-ов — русский технический текст. Английский допустим для имён инструментов, файлов, команд, устойчивых source terms и названий. Стиль должен быть рабочим и инженерным: без маркетингового тона, канцелярита, декоративных метафор и механических bullet-summary там, где нужно объяснение.

## 3. Запреты уровня meta-package

Meta-package не должен:

- писать сами статьи атласа;
- собирать article-writing packages;
- переносить фактуру из досье в будущие статьи как готовый опубликованный текст;
- создавать новые темы статей из внешнего поиска;
- расширять набор статей за пределы dossier-backed списка без отдельного решения пользователя;
- превращать article map или target-group plan в мини-атлас;
- подменять конкретные read-only paths формулами вроде «релевантные материалы»;
- полагаться на неявный репозиторий при будущей сборке self-contained package;
- использовать управляющий Python-скрипт, payload или служебные файлы текущего пакета как источник методологии.

План может описывать, какие внешние источники будущий writing package должен открыть или вывести из досье, но сам meta-package не должен проводить полноценный source-transfer в статью. Его работа — спроектировать очередь, входы и проверки так, чтобы будущий пакет сделал это правильно.

## 4. Self-contained future article packages

Для будущих article-writing packages действует правило self-contained по умолчанию. Это значит, что создаваемые target-group plans должны перечислять exact read-only input paths, которые затем будут упакованы вместе с пакетом.

В плане нельзя писать только «прочитать досье по теме», «использовать asset catalog» или «свериться с фрагментами теории». Нужно указывать конкретные пути, например:

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
work/theory-writing/fragments/A1_specification_layer.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
content/assets/theory-images/...
```

Если для конкретной статьи нужен repo-snapshot-bound режим, это должно быть явным исключением, а не молчаливой зависимостью. В текущем направлении такие планы проектируются как self-contained.

## 5. Где брать досье, assets и правила

Досье и quarry-материал берутся из:

```text
work/dossiers/
work/dossier-passes/
work/methodology-passes/
work/theory-writing/fragments/
```

Основные dossier-backed концепции уже зафиксированы в карте документов: `SPDD_METHOD_DOSSIER.md`, `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`, `GAS_TOWN_METHOD_DOSSIER.md`, `ADR_METHOD_DOSSIER.md`, `SPEC_KIT_METHOD_DOSSIER.md`, `KIRO_SPECS_DOSSIER.md`, `TDAD_COMPARATIVE_DOSSIER.md`, `CONSTITUTIONAL_SDD_DOSSIER.md`, `GSD_METHOD_DOSSIER.md`, `BMAD_METHOD_DOSSIER.md`. Для некоторых статей нужны не только методологические досье, но и уже написанные A/B/C-фрагменты, потому что атлас должен показывать связь конкретной концепции с общей AI-driven SDLC рамкой.

Визуальные материалы и реестры берутся из:

```text
work/theory-writing/asset-catalog/
content/assets/
```

Правила для планов и будущих пакетов берутся из:

```text
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
```

Если план предполагает перенос фактуры или внешние ссылки, он должен также включать источниковые и preservation rules в prompt-блоки будущего package, даже если текущий G01-лист не требовал их чтения напрямую.

## 6. Почему список статей не расширяется внешним поиском

Внешний поиск разрешён будущим article-writing packages для проверки, насыщения первоисточников, уточнения команд/UI/версий и поиска реальных изображений. Но этот поиск не должен создавать новые статьи атласа сам по себе.

Список статей на этапе manufactury должен выводиться из уже принятого dossier-backed набора и из карты документов. Иначе meta-package начнёт смешивать две разные задачи: проектирование планов по утверждённому корпусу и исследовательское расширение корпуса. Это рискованно: появятся тонкие статьи без досье, нарушится приоритет глубоких опорных узлов, а article map станет списком интересных тем вместо управляемого маршрута чтения.

Новые внешние кандидаты можно фиксировать как `deferred / not enough material` или как open question для человеческого решения, но не включать их в основную очередь статей без явного разрешения.

## 7. Cycle per article: S01–S05

Для каждой статьи цикл должен работать одинаково по роли, но не механически по содержанию.

S01 формулирует article contract: рабочий `article_id`, article tier, reader question, границы статьи, опасные пересечения с соседними статьями, ожидаемые target outputs и первичный список exact read-only input paths.

S02 создаёт полный target-group plan по blueprint: обрабатываемые файлы, read-only inputs, внешние источники и готовую очередь prompt-ов. На этом шаге важно не написать статью, а спроектировать будущий package так, чтобы он мог написать её без догадок о контексте.

S03 выполняет первый repair плана: проверяет, подходит ли выбранная очередь именно этой статье, не пропущены ли обязательные source-depth, visual, concept reinforcement, general editorial, language/style and final checks, и нет ли внутренних ограничений объёма.

S04 выполняет buildability/self-contained audit: exact paths, наличие файлов, bundle-readiness, companion outputs, idempotency/rerun handling, emergency packaging, отсутствие placeholders вроде «релевантные файлы» и отсутствие зависимости от unstated repository context.

S05 выполняет финальную плановую проверку: план не должен писать статью, не должен расширять article set, должен сохранять границы с теорией и соседними статьями, должен фиксировать readiness status `ready_for_package_manufacture_after_manual_review` или понятный blocker.

После S05 можно переходить к следующей статье из dossier-backed очереди. Итог meta-package должен дать набор target-group plans, отчёт о готовности, карту статусов и список отложенных вопросов, но не статьи и не article-writing archives.
