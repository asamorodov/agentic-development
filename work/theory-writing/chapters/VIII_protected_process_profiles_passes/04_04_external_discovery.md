# 04 — Внешний поиск и source discovery для главы VIII

Статус: выполнено. Веб-доступ был доступен; поиск и чтение источников проводились 15 июня 2026 года.

Цель прохода — не собрать рынок инструментов и не расширить главу каталогом, а найти фактуру для механизма главы: как внешние практики превращают процесс в рабочий профиль, который удерживает фазу, роль, допустимый следующий ход, состояние проекта, проверку и восстановление.

## 1. Что именно искалось

Поиск был направлен на четыре группы материалов.

Первая группа — текущая документация Open GSD / GSD Core: фазовый цикл, структура `.planning/`, правила работы в свежих контекстах, роли агентов, проверка, автономный режим и восстановление состояния.

Вторая группа — текущая документация BMAD Method / BMM: workflow map, BMad-Help, Skills, Agents, Phase 4 implementation, `sprint-status.yaml`, `bmad-create-story`, `bmad-correct-course`, `bmad-investigate`, `project-context.md`, режимы Quick Flow / BMad Method / Enterprise.

Третья группа — первичные репозиторные источники: `SKILL.md`, README, changelog, release notes, issues, если они уточняют текущую механику лучше, чем обзорные страницы.

Четвёртая группа — current-practice материалы и обсуждения. Их задача не подтверждать основной тезис, а показать живые проблемы: устаревание документации, сбои установки, конфликты вокруг correct-course, желание связать BMAD с внешними work-management системами. Эти источники полезны только как вторичный материал; основой главы должны оставаться официальные документы и исходники.

## 2. Использованные внешние источники

### Open GSD / GSD Core

1. [Open GSD — documentation home](https://docs.opengsd.net/)

Использование: общий источник для формулировки Open GSD как не «ещё одного промпта», а рабочего цикла вокруг планов, чистых контекстов, проверки и состояния. В главе источник можно использовать осторожно, без рекламной рамки: он подтверждает, что метод позиционирует себя как операционный контур для агентской разработки, где важны планы, отдельные исполнительские контексты, проверка и история изменений.

2. [GSD Core — Quickstart](https://docs.opengsd.net/gsd-core/tutorials/quickstart)

Использование: главный источник для первого технического описания цикла: инициализация проекта, обсуждение, планирование, выполнение, проверка, отправка результата; создание `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, `config.json`, research-директории; требование явно утвердить roadmap; перенос значимого состояния в `.planning/` перед очисткой контекста. Это особенно важно для главы VIII, потому что здесь процесс становится не устным соглашением, а набором файлов, которые определяют продолжение работы.

3. [GSD Core — The Phase Loop](https://github.com/firescrawl/gsd-core/blob/main/docs/explanation/the-phase-loop.md)

Использование: основной источник для фазовой логики. Важны не сами названия фаз, а то, что цикл описан как последовательность защит от типичных сбоев: Discuss → UI design → Plan → Execute → Verify → Ship. В тексте главы это можно использовать для тезиса: процессный профиль не просто говорит «делай по шагам», а меняет право агента на следующий тип действия.

4. [GSD Core — Planning Artifacts](https://docs.opengsd.net/gsd-core/explanation/planning-artifacts)

Использование: самый важный источник для связки «процесс как артефакт». Здесь `.planning/` описан как корень состояния проекта, состоящий из Markdown/JSON-файлов, которые можно коммитить и читать после очистки контекста. Для главы особенно важны роли `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `CONTEXT.md`, `PLAN-*.md`, `SUMMARY-*.md`, `VERIFICATION-*.md`, `UAT-*.md`. Этот источник должен стать одной из главных опор раздела о том, что профиль процесса хранит не только инструкции, но и текущую позицию, решения, блокеры, требования, планы и доказательства проверки.

5. [GSD Core — Specialist Agents](https://docs.opengsd.net/gsd-core/explanation/specialist-agents)

Использование: источник для уточнения роли. GSD описывает специализированных агентов как свежие контексты с узкой задачей, входными артефактами, моделью и правами инструментов. Для главы VIII это полезно не как рассказ о multi-agent архитектуре, а как пример: профиль процесса выбирает не «умную личность», а рабочий режим с границами доступа, входами, выходами и проверкой.

6. [GSD Core — Context Management](https://docs.opengsd.net/gsd-core/explanation/context-management)

Использование: источник для центральной проблемы: контекст портится, если агент слишком долго несёт всё в одном разговоре; fresh-context subagents и `.planning/` должны переносить важное состояние между сессиями. В главе источник можно связать с главами VI–VII: контекст и рабочее состояние сами по себе ещё не выбирают процессный режим, но без них процессный режим не может честно продолжаться.

7. [GSD Core — Phase Lifecycle](https://docs.opengsd.net/gsd-core/reference/phase-lifecycle)

Использование: источник для командной механики `gsd-discuss-phase`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-phase`, `gsd-ship` и для результата каждой фазы. Он пригодится при написании конкретного фрагмента: профиль процесса создаёт не только общее состояние, но и ожидаемый выход каждой фазы.

8. [GSD Core — Autonomous Mode](https://docs.opengsd.net/gsd-core/reference/autonomous-mode)

Использование: вторичный источник для границы между интерактивным и автономным процессом. Важно для главы, потому что процессный профиль может менять степень участия человека: где нужен checkpoint, где можно auto-advance, где требуется review. Не следует превращать этот материал в отдельную тему автоматизации; он нужен как доказательство, что профиль процесса включает режим взаимодействия с человеком.

### BMAD Method / BMM

9. [BMAD Method — Workflow Map](https://docs.bmad-method.org/reference/workflow-map/)

Использование: главный текущий источник для BMAD. Он прямо описывает BMM как модуль для context engineering и planning: документы постепенно строятся в четырёх фазах, каждая фаза и workflow производят документы, которые затем информируют следующий шаг. Для главы особенно важны: Phase 3 Solutioning (`bmad-create-architecture`, `bmad-create-epics-and-stories`, `bmad-check-implementation-readiness`), Phase 4 Implementation (`bmad-sprint-planning`, `bmad-create-story`, `bmad-dev-story`, `bmad-code-review`, `bmad-correct-course`, `bmad-sprint-status`, `bmad-retrospective`, `bmad-investigate`), Quick Flow, и отдельный блок Context Management.

10. [BMAD Method — Getting Started](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/tutorials/getting-started.md)

Использование: источник для практической последовательности: выбор трека Quick Flow / BMad Method / Enterprise, свежий чат для каждого workflow, создание `sprint-status.yaml`, повторяющийся story cycle, автоматическое появление BMad-Help в конце workflow. Для главы это важный материал: BMAD не просто делит работу на роли, а постоянно возвращает пользователя к вопросу «что теперь делать?».

11. [BMAD Method — Skills](https://docs.bmad-method.org/reference/skills/)

Использование: источник для уточнения current mechanics. Skills генерируются установщиком из выбранных модулей и являются прямым способом загрузить агента, workflow или task. Это важно, чтобы глава не описывала BMAD только как набор «персон», а показывала его как систему входов в разные рабочие режимы. В главе нужно сказать аккуратно: skill — это не только prompt/persona, а точка запуска конкретного режима с ожидаемыми входами и выходами.

12. [BMAD Method — Agents](https://docs.bmad-method.org/reference/agents/)

Использование: источник для разведения «роли» и «личности». BMAD имеет named agents, но для главы важнее их процессная функция: Analyst, PM, Architect, Developer, UX Designer, Technical Writer запускают разные типы работ и разные workflow. Материал стоит использовать против ошибочного прочтения: процессные профили — это не театральное назначение персонажей, а распределение суждений по фазам жизненного цикла.

13. [BMAD Method — Core Tools](https://docs.bmad-method.org/reference/core-tools/)

Использование: источник для `bmad-help` и `bmad-spec`. `bmad-help` важен как интерфейс определения следующего шага: он смотрит на состояние проекта, уже созданные артефакты и доступные возможности. `bmad-spec` важен как короткое ядро намерения, которое можно передавать дальше. В главе нужно использовать это ограниченно: главный предмет главы — процессные профили, а не вся экосистема BMAD.

14. [BMAD Method — Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md)

Использование: источник для brownfield / established project логики и для того, как BMAD фиксирует правила проекта. `project-context.md` описан как implementation guide для AI agents: файл с технологиями, версиями, критическими правилами, паттернами и ограничениями, который загружается implementation workflows. Это важный мост к brownfield-навигации: профиль процесса должен учитывать не только фазу и story, но и существующие проектные соглашения.

15. [BMAD Method — `bmad-create-story` SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md)

Использование: первичный источник для story как контекстного контейнера. В файле workflow прямо описан как создание story file, который должен дать dev agent всё необходимое для реализации и предотвратить типичные ошибки: заново изобретённые решения, неверные библиотеки, неправильные пути, регрессии, игнорирование UX, расплывчатую реализацию, ложные заявления о завершении, потерю уже накопленного знания. Также важно, что workflow читает `sprint-status.yaml`, находит первую story в backlog, загружает planning artifacts и может использовать subagents / subprocesses для анализа.

16. [BMAD Method — `bmad-correct-course` SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md)

Использование: первичный источник для recovery / rerouting внутри процесса. Workflow загружает PRD, Epics, Architecture, UX, Spec и Document Project, требует clear change trigger, проходит checklist, формирует explicit edit proposals и в итоге Sprint Change Proposal. Для главы это, возможно, самый чистый пример «профиля процесса»: когда обнаружена проблема, агент не должен просто продолжать реализацию, а должен перейти в режим анализа влияния и согласованного изменения артефактов.

17. [BMAD Method — Changelog / Releases v6.7.0](https://github.com/bmad-code-org/BMAD-METHOD/releases)

Использование: источник для current-practice дельты. В релизных заметках v6.7.0 зафиксированы `bmad-investigate`, evidence-graded case files, `.decision-log` pattern, переработка PRD/Product Brief в intent-oriented skills. В основной главе этот источник можно использовать только точечно: он показывает, что BMAD движется от набора статичных workflow к более явным режимам намерения, расследования, фиксации решений и восстановления.

18. [BMAD Method — official update, May 2026](https://www.bmadcode.com/bmad-update-may-2026-web-bundles-prd-brief-platforms/)

Использование: вторичный официальный источник для текущего состояния v6.7–v6.8: `bmad-investigate`, `bmad-spec`, `.decision-log`, web bundles, hardening activation guardrails. Не стоит делать на нём основной тезис, но он полезен как подтверждение, что актуальная BMAD-ветка усиливает именно decision log, skills architecture и guards around activation.

## 3. Источники, использованные как вторичные признаки, но не как основная опора

1. GitHub issues по BMAD, связанные с `bmad-correct-course`, `bmad-create-story`, `sprint-status.yaml`, установкой agents/skills и подключением внешних work-management систем.

Использование: не переносить в основной текст как факты о методе, но держать в уме как реальные failure modes. Особенно полезны темы: correct-course может конфликтовать с immutability completed stories; story/epic синхронизация после course correction требует явного source-of-truth механизма; file-system-based skills для больших проектов могут требовать связи с Azure DevOps или другой системой; skill path mechanics могут ломаться на конкретных платформах. Это показывает, что процессный профиль сам нуждается в проверке и границах.

2. Search results и отдельные promotional / blog материалы о BMAD.

Использование: в основной текст не переносить. Они часто пересказывают официальную документацию хуже первоисточников и добавляют рекламный шум. Пригодны только для проверки, какие элементы current-practice сейчас считаются заметными: Skills Architecture, `.decision-log`, web bundles, subagent inclusion, workflow automation.

3. YouTube / community demos.

Использование: не использовать в текущей главе. Они могут дать хорошие иллюстрации UI или пользовательского опыта, но задача главы — теоретический механизм, а не практический туториал.

## 4. Отклонённые направления поиска

1. Общие материалы про agile, Scrum, XP, Kanban.

Причина отклонения: глава не о классическом управлении проектами и не должна становиться обзором процессных школ. Такие источники дали бы слишком широкий фон и размыли бы точный предмет: agentic process profiles as continuation machinery.

2. Сравнительные статьи «BMAD vs X» без первичных ссылок.

Причина отклонения: высокий риск рекламного пересказа, низкая плотность механики. Для этой главы нужны конкретные артефакты, workflow, входы, выходы и восстановительные ходы.

3. Материалы про «персоны» в prompt engineering без связи с артефактами процесса.

Причина отклонения: они ведут к ложной рамке. Глава должна показать, что роль в protected process profile — это не психологическая маска, а ограниченный рабочий режим с доступом к определённым источникам, ответственностью за конкретный выход и правом выполнять только определённый тип действия.

4. Исследовательские статьи, случайно совпадающие по аббревиатурам GSD / BMAD.

Причина отклонения: нерелевантны текущему корпусу главы.

## 5. Новые выводы для главы после внешнего добора

### 5.1. Open GSD надо описывать через «фазу + состояние + свежий контекст + evidence», а не только через `.planning/`

Локальный атлас уже правильно держит `.planning/` как центр GSD, но внешняя документация усиливает картину: GSD — это не просто durable state directory. Это связка фазового цикла, файлов состояния, свежих агентских контекстов, прав доступа, проверки и shipping ritual. Для главы VIII полезнее формула: профиль процесса задаёт, в какой фазе находится работа, какие файлы являются источником правды, какой агент имеет право действовать, что считается выходом фазы и какая evidence нужна для перехода дальше.

### 5.2. `STATE.md` и `CONTEXT.md` нужно развести точнее

Внешние документы GSD позволяют не смешивать рабочую позицию и решения. `STATE.md` держит текущую позицию, phase, планы, блокеры, recovery и метрики. `CONTEXT.md` / discussion artifacts держат decisions and rationale, которые потом читают planner, executor и verifier. Для главы это даёт хороший пример различия: рабочее состояние отвечает «где мы?», процессный профиль отвечает «в каком режиме можно продолжать?», а контекст решений отвечает «почему нельзя продолжить иначе, не потеряв смысл?».

### 5.3. BMAD сильнее, чем в локальном черновом образе, сдвинулся к интерфейсу «что делать дальше»

`bmad-help` в текущей документации описан не просто как справка, а как интерактивный guide, который смотрит на проект и рекомендует next step. Это важно для главы: protected process profile может быть не только статическим протоколом, но и интерфейсом выбора следующего режима. Однако это надо подать без рекламного усиления: ценность не в названии `bmad-help`, а в самом паттерне next-action routing на основании уже созданных артефактов.

### 5.4. Story file в BMAD — хороший пример контекстного контейнера, а correct-course — пример смены режима

`bmad-create-story` показывает, как процесс готовит агенту правильный вход: story file должен не просто скопировать epic, а собрать оптимизированный контекст реализации. `bmad-correct-course` показывает обратную ситуацию: при существенном изменении нельзя продолжать story execution; нужно загрузить широкий набор planning artifacts, пройти impact analysis и создать proposal. Это почти идеальная пара для главы: один профиль сужает контекст до реализации, другой расширяет его для пересборки курса.

### 5.5. `project-context.md` полезен как пример brownfield-ограничителя

В текущей документации BMAD `project-context.md` описан как файл, который хранит правила, паттерны, версии, соглашения и ограничения проекта и автоматически загружается implementation workflows. Это стоит включить в главу, но не разворачивать слишком широко: главная мысль — в established project профиль процесса должен не только знать, что нужно сделать, но и держать, как в этом проекте вообще можно делать изменения.

### 5.6. В главе нужно избегать ложного противопоставления GSD и BMAD

После внешнего чтения видно, что их лучше сравнивать по типу защищаемого сбоя, а не как конкурирующие frameworks. GSD лучше показывает recovery across sessions, clean execution contexts, phase evidence и git/verification rhythm. BMAD лучше показывает phased artifact transfer, role-specific workflow, story preparation, sprint status, course correction and investigation. В главе можно построить сравнение как разные профили защиты, а не как рейтинг методов.

### 5.7. Нужно сохранить границу с главой IX

В GSD много материала о permissions, model/security policy, specialist agents и execution contexts. В BMAD много материала о platform-specific skills and installation. Часть этого естественно тянет в главу IX об исполняющей среде. В VIII брать только то, что нужно для процессного режима: роль, входы, выходы, checkpoint, recovery, evidence, next-action routing. Детали sandbox, permissions, platform support и tool mechanics оставить для IX, если они не влияют на сам процессный профиль.

## 6. Source discovery log

| Источник | Статус | Как использовать |
|---|---:|---|
| Open GSD documentation home | used | Общая рамка GSD как operating loop; не цитировать рекламно. |
| GSD Core Quickstart | used | Фазовый цикл и создание `.planning/` артефактов. |
| GSD Core The Phase Loop | used | Логика фаз как защита от сбоев и разрешение следующего действия. |
| GSD Core Planning Artifacts | used | Главная фактура для process-as-artifact: PROJECT/REQUIREMENTS/STATE/CONTEXT/PLAN/SUMMARY/VERIFICATION/UAT. |
| GSD Core Specialist Agents | used | Свежие контексты, ограниченные роли, tool permissions; использовать только в рамках процессного профиля. |
| GSD Core Context Management | used | Контекстная гниль, fresh-context architecture, state transfer. |
| GSD Core Phase Lifecycle | used | Конкретные команды и выходы фаз; пригодится для примеров. |
| GSD Core Autonomous Mode | partial | Режим auto/manual/checkpoint; не делать отдельной темой. |
| BMAD Workflow Map | used | Основной источник по фазам, workflows, context management и Phase 4. |
| BMAD Getting Started | used | Практический порядок: tracks, fresh chats, sprint planning, story cycle, bmad-help. |
| BMAD Skills reference | used | Skills как входы в agent/workflow/task, а не только persona. |
| BMAD Agents reference | used | Роли как процессные функции; избегать persona-catalog. |
| BMAD Core Tools | used | `bmad-help`, `bmad-spec`; использовать точечно. |
| BMAD Project Context | used | Brownfield/established project restrictions and conventions. |
| BMAD `bmad-create-story` SKILL.md | used | Story file as implementation context container; reads sprint status and planning artifacts. |
| BMAD `bmad-correct-course` SKILL.md | used | Recovery/rerouting mode; impact analysis across planning artifacts. |
| BMAD releases/changelog v6.7.0 | partial | `bmad-investigate`, `.decision-log`, intent-based PRD; только как current delta. |
| BMAD official May 2026 update | partial | Подтверждение v6.7–v6.8 direction; не основной источник. |
| BMAD GitHub issues | partial / caution | Реальные failure modes; не использовать как факты о методе без оговорки. |
| Promotional blog posts / reposts | rejected | Слишком много пересказа и маркетинга, низкая плотность первичной механики. |
| Generic agile/process sources | rejected | Уводят главу в общий менеджмент, не в agentic process profiles. |
| YouTube demos | rejected for now | Возможны для иллюстраций, но не нужны для механизма главы. |

## 7. Открытые хвосты для следующих проходов

1. При написании основной главы стоит ещё раз открыть первичные `SKILL.md` для `bmad-investigate`, если раздел будет подробно говорить об investigation profile. Пока достаточно release/workflow-map уровня: investigation как forensic evidence-graded case file. Для глубокого описания нужен сам skill.

2. Если в главе появится фрагмент о established projects / brownfield, нужно проверить official Established Projects FAQ и не полагаться только на `project-context.md`.

3. Если в главе появится фрагмент о GSD autonomous mode, нужно не превращать его в тему полной автономии. Достаточно показать, что профиль процесса задаёт human checkpoint и режим advance.

4. Если глава захочет говорить о security/tool permissions, нужно либо оставить это для главы IX, либо очень явно объяснить, что в VIII это упоминается только как граница роли внутри process profile.

5. Нужно не забыть переносить ссылки в основной текст сразу при первом использовании внешнего материала, особенно при конкретных упоминаниях `.planning/`, `STATE.md`, `sprint-status.yaml`, `bmad-create-story`, `bmad-correct-course`, `bmad-help`, `project-context.md`.
