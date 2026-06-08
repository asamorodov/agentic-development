# Первая проверка готовности Codex перед Stage 0.19

Используйте этот prompt как первую задачу Codex перед запуском Stage 0.19.

## Задача

Проверить, что Codex может работать с этим репозиторием, видит документы текущей рабочей ветки и понимает workflow перестройки теории перед созданием protected methodology dossiers.

Это только проверка готовности и понимания.

Codex не должен:

- писать теоретические главы;
- создавать methodology dossiers;
- запускать Stage 0.19;
- менять `work/approved-ai-sdlc-plan.md`;
- менять `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`;
- менять `/content`.

## Что прочитать по порядку

```text
AGENTS.md
project/repository-structure.md
project/source-precedence.md
project/branching-and-task-model.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/theory-rebuild-rules.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
work/discourse.md
work/approved-ai-sdlc-plan.md
work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md
work/decisions/ADR-0008-protected-methodology-profiles.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/reports/SKELETON_V4_QUALITY_AUDIT.md
work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md
```

Затем осмотреть:

```text
work/dossiers/
work/reports/
work/source-expansion/
work/prompts/
```

## Что создать

```text
work/reports/CODEX_READINESS_CHECK.md
work/reports/CODEX_DOCUMENT_VISIBILITY_INVENTORY.md
work/reports/CODEX_UNDERSTANDING_SUMMARY.md
work/reports/CODEX_NEXT_TASK_RISK_ASSESSMENT.md
work/CHECKS.json
work/discourse.md
```

Если в текущей среде уже существует `work/checks.json`, обновить его как рабочий checks-файл ветки и явно отметить вопрос регистра имени `CHECKS` в отчёте.

## Что проверить

### 1. Видимость репозитория и документов

Подтвердить, что Codex видит:

- `work/`;
- `work/discourse.md`;
- `work/approved-ai-sdlc-plan.md`;
- ADR-0007 и ADR-0008;
- methodology depth contract;
- skeleton v4.1;
- selected dossiers;
- source-expansion materials;
- оба prompt-файла для readiness check и Stage 0.19.

### 2. Текущее состояние работы

Объяснить по-русски:

- почему проект перешёл от старой теории к AI-driven SDLC;
- почему expanded theory является quarry, а не main draft;
- почему SPDD и Gas Town являются protected deep anchors;
- что означает protected methodology profile;
- почему GSD/BMAD не являются shallow mentions;
- почему Parts VI-XII нельзя превращать в artifact catalog;
- что Stage 0.19 должен сделать и чего он не должен делать.

### 3. Откуда брать интернет-источники для Stage 0.19

Подтвердить понимание source strategy:

- `work/source-expansion/`, `work/dossiers/`, `work/reports/` и `work/theory-source-map-ai-driven-sdlc.md` используются как навигация, карта уже найденных направлений и список кандидатов, но не заменяют чтение первоисточников.
- Для фактических утверждений в methodology dossiers приоритет имеют раскрытые и прочитанные внешние первоисточники: official docs, official repositories, official blog posts, specifications, papers, documentation pages, changelogs и project pages.
- Для research claims использовать papers / research sources, но отделять их от official / primary sources.
- Интернет-источник считается использованным только после того, как Codex открыл сам источник, прочитал релевантные разделы и, если нужно, связанные страницы или files.
- Source snippets, search results, прежние summaries и internal notes не являются достаточным основанием для dossier claim.
- Ссылки на внешние источники нужно ставить рядом с конкретными фактами в dossier, а не только в конце документа.
- Поиск внутри уже утверждённых методологий Stage 0.19 разрешён автоматически. Расширение задачи на новые methodology families или new deep anchors требует human gate.

Если текущая среда не даёт открыть внешние источники или проверить primary/official sources, readiness status должен быть `READY_WITH_WARNINGS` или `NOT_READY` с явным объяснением.

### 4. Автоматический цикл работы над каждым dossier

Подтвердить понимание, что работа над каждым protected methodology dossier в Stage 0.19 — это не один проход и не шесть статичных pass-файлов, а автоматический повторяемый цикл.

Один цикл состоит из трёх этапов:

1. **Раскрытие источников.** Найти, открыть, загрузить или прочитать источники; перечитать их вместе со связанными частями: linked docs, repository files, examples, papers, specification pages, changelog fragments или source references.
2. **Перенос деталей в dossier.** Перенести детали в нужном объёме в черновик dossier, писать по-русски, сразу ставить ссылки на внешние источники рядом с утверждениями, соблюдать language/style/source protocols. На этом же этапе расставить кандидаты на включение внешних изображений: URL, краткое описание того, что находится по ссылке, и объяснение, почему изображение может быть полезно для будущего текста. Сами image assets не скачивать и не включать: это отдельный будущий проход.
3. **Обнаружение новых источников.** В прочитанных материалах найти новые source candidates, linked docs, references, repositories, papers или related pages и перенести их в source document / source register для этой методологии.

Этот цикл повторяется для каждого dossier:

- не меньше 10 раз;
- не больше 20 раз;
- автоматически, без ручного подтверждения человека между повторами;
- после 10-го цикла можно остановиться только если новые существенные детали и новые значимые источники перестали появляться в серьёзном количестве;
- если к 20-му циклу существенные новые детали или источники всё ещё появляются, нужно остановиться, зафиксировать residual source queue и запросить human decision.

Только после этих циклов можно переходить к финальной части Stage 0.19: final dossiers, comparative synthesis reports, quality audit, checks и discourse update.

Visual candidates должны оставаться только кандидатами. Они не являются разрешением включать external assets в итоговый документ.

### 5. Соблюдение протоколов

Подтвердить, что Codex понимает:

- обязательность русского языка;
- правила работы с англоязычными источниками;
- baseline restore rule для SPDD и Gas Town;
- запрет писать главы на readiness check и Stage 0.19;
- запрет менять approved plan без human gate;
- запрет демотировать protected methodology profiles;
- human gates для source access, broad search, architecture changes и deep-anchor changes.

### 6. Готовность к сложной задаче

Указать, готов ли Codex запускать Stage 0.19.

Если не готов, объяснить почему:

- отсутствуют core documents;
- нет доступа к внешним источникам;
- непонятен source cycle;
- конфликтуют протоколы;
- неясен human gate.

## Обязательные детали выходных файлов

`work/reports/CODEX_READINESS_CHECK.md` должен включать:

```text
status: READY / READY_WITH_WARNINGS / NOT_READY
documents_read:
missing_documents:
understanding_summary:
internet_source_strategy:
dossier_cycle_understanding:
risks:
recommended_next_task:
human_gates:
```

`work/reports/CODEX_DOCUMENT_VISIBILITY_INVENTORY.md` должен перечислить обязательные файлы и указать, найдены ли они.

`work/reports/CODEX_UNDERSTANDING_SUMMARY.md` должен быть связным рассказом о текущем workflow, а не checklist.

`work/reports/CODEX_NEXT_TASK_RISK_ASSESSMENT.md` должен назвать риски перед Stage 0.19, включая риски источников, автоматических циклов, ссылок, языка, visual candidates и human gates.

## Stop condition

Если отсутствует любой required core document, не переходить к Stage 0.19.

Создать readiness reports, зафиксировать missing documents и запросить human decision.


## Дополнительно проверь новые файлы

Убедись, что видишь и понимаешь:

```text
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
```

Объясни, что общий протокол применим к разным документам, а prompt только уточняет его для методологических досье.
