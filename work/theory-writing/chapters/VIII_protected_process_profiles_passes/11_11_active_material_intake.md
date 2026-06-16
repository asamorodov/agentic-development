# 11 — активный добор после первого черновика

Статус: выполнено. Это не отдельный набор заметок поверх черновика: по итогам добора изменён сам файл первого черновика `10_10_full_draft.md`. Основное вмешательство сделано в разделе BMAD, потому что именно там после перечитывания источников обнаружился недобор фактуры.

## Что было перечитано

Повторно просмотрены:

- `10_10_full_draft.md` — первый полный черновик главы;
- `04_04_external_discovery.md` — внешний discovery-лог;
- `07_07_source_family_deepening.md` — углубление семейства источников;
- `08_08_interface_and_current_practice.md` — интерфейсная модель профиля;
- [BMAD Workflow Map](https://docs.bmad-method.org/reference/workflow-map/) — особенно Phase 4, Quick Flow, Context Management and Project Context;
- [BMAD Established Projects FAQ](https://docs.bmad-method.org/explanation/established-projects-faq/) — работа с established projects, document-project, Quick Flow, вопрос следования старым conventions;
- [BMAD Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md) — что хранит `project-context.md`, кто его загружает и зачем он нужен в existing project;
- [BMAD Forensic Investigation](https://docs.bmad-method.org/explanation/forensic-investigation/) — отличие investigation от обычного debugging, evidence grading, stronghold first, hypothesis discipline, структура investigation file.

## Найденные тонкие места

### 1. Brownfield-часть была слишком общей

В первом черновике уже было сказано, что `project-context.md` нужен established projects, но это оставалось почти справочной фразой. Не хватало практического различия: established project — это не просто проект с кодом, а кодовая база, где странные решения, версии, testing patterns and conventions могут быть обязательными рабочими ограничениями. Без этого раздел мог прочитываться так, будто BMAD просто добавляет файл с правилами, а не меняет режим входа агента.

Исправление: раздел переписан так, чтобы показать brownfield как отдельный режим. Добавлены факты из Established Projects FAQ: document-project рекомендуется, если документации нет, она устарела или агентам нужен контекст по существующему коду; Quick Flow для established projects должен auto-detect stack, analyze patterns, detect conventions and ask for confirmation; если старый код не следует best practices, BMAD не должен автоматически модернизировать его, а спрашивает, следовать ли существующим соглашениям. Это усиливает главный тезис главы: восстановленная работа может требовать не исполнения, а сначала создания знания о старой системе.

### 2. `project-context.md` был описан как справочник, а не как ограничитель действия

В первом черновике `project-context.md` был упомянут как implementation guide. Но в логике главы важнее не то, что он «хранит сведения», а то, что он автоматически становится обязательным входом implementation workflows и сужает право агента применять generic best practices.

Исправление: добавлено, что `project-context.md` документирует technology stack and versions, critical implementation rules, code organization, testing patterns and project-specific constraints; что implementation workflows автоматически загружают его, если он существует; и что в existing project его можно генерировать, чтобы обнаружить established patterns and conventions. В тексте это связано с `billing/API`: старое странное поведение может быть внешним контрактом, а не мусором.

### 3. `bmad-investigate` был недоперенесён

В первом черновике investigation был сведен почти к release-note факту: forensic, evidence-graded case files. Этого недостаточно для главы VIII. Сам источник гораздо сильнее: он прямо отделяет investigation от fixing и объясняет, почему смешение evidence, reasoning and code change создаёт narrative lock-in and evidence amnesia.

Исправление: добавлен полноценный фрагмент о `bmad-investigate` как отдельном профиле. Перенесены ключевые элементы: skill не начинает чинить, а открывает case file; findings делятся на confirmed, deduced and hypothesized; investigation starts from a stronghold; hypotheses are never deleted; output goes to `{implementation_artifacts}/investigations/{slug}-investigation.md`; итоговый файл должен быть понятен инженеру, который не присутствовал при расследовании. Это напрямую связывает источник с тезисом главы: investigation and implementation reward different instincts, поэтому их нельзя незаметно смешивать в одной сессии.

### 4. Сквозной пример нужно было удержать внутри добора, а не только в общей таблице

`billing/API` присутствовал в черновике, но в BMAD brownfield/investigation-части он был слишком быстро свёрнут. Это создавало риск, что сквозной пример останется только в начале и в таблице, а не будет работать как проверка каждого профиля.

Исправление: в изменённый BMAD-фрагмент добавлен локальный пример: старый `invoice.status`, неудобное имя поля или странный error mapping могут оказаться частью совместимости; compatibility suite, падающий без ясной причины, должен запускать case file, а не автоматическую правку production code; результат investigation должен выбирать следующий профиль — dev-story, correct-course, уточнение story, human decision или расширение brownfield-модели.

## Что изменено в черновике

В `10_10_full_draft.md` заменён блок от фразы:

```text
BMAD также полезен в brownfield-проектах.
```

до фразы:

```text
У BMAD есть свои риски.
```

Новая версия делает три вещи:

1. превращает established/brownfield project из побочной темы в отдельный режим входа;
2. показывает `project-context.md` как рабочий ограничитель, а не как декоративную документацию;
3. отделяет investigation от debugging/fixing и связывает это различие с центральным сбоем главы.

## Текущий фрагмент после правки

```markdown
BMAD особенно полезен в brownfield-проектах, но не потому, что даёт агенту ещё один быстрый путь к реализации. Его ценность здесь противоположная: он заставляет агента признать, что существующая кодовая база уже имеет свои правила, паттерны, исторические решения и внешние контракты. Для established projects документация BMAD прямо рекомендует сначала документировать проект, особенно если документации нет, она устарела или агентам нужен контекст по существующему коду. Quick Flow тоже допускается для established projects, но он должен auto-detect existing stack, analyze code patterns, detect conventions and ask for confirmation; если старый код не следует best practices, BMAD не должен автоматически модернизировать его, а спрашивает, следовать ли существующим соглашениям или вводить новые стандарты с объяснением в spec. [BMAD Established Projects FAQ](https://docs.bmad-method.org/explanation/established-projects-faq/)

`project-context.md` в этой логике становится не справочником «о проекте», а ограничителем реализации. Документация описывает его как concise, LLM-optimized файл с тем, что агент должен знать, чтобы не применять generic best practices поверх живой кодовой базы: technology stack and versions, critical implementation rules, code organization, testing patterns, project-specific constraints. Важная техническая деталь: implementation workflows автоматически загружают `project-context.md`, если он существует; среди потребителей названы architecture, story creation, dev story, code review, quick dev, sprint planning, retrospective and correct-course. Для existing project файл можно создать через `bmad-generate-project-context`, чтобы обнаружить существующие patterns and conventions. [BMAD Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md)

В `billing/API` это означает: если старый API плохо документирован, нельзя начинать как greenfield и нельзя молча «улучшать» странные места. Сначала нужен профиль создания знаний о существующей системе: прочитать старый код, contract tests, SDK usage, logs, клиентскую документацию и production-примеры; отделить подтверждённое поведение от вывода и гипотез; понять, какие странности являются ошибками, а какие давно стали внешним контрактом. Старый `invoice.status`, неудобное имя поля или странный error mapping могут быть не мусором, а частью совместимости. Правильный профиль здесь не «реализуй новую модель», а «собери карту старого поведения и верни её как вход для story creation, correct-course или human checkpoint».

Отдельный режим — `bmad-investigate`. Его важно не смешивать ни с обычной реализацией, ни с brownfield-обзором. Страница Forensic Investigation формулирует это прямо: на вход можно дать crash log, stack trace или сообщение «раньше работало, теперь нет»; skill не начинает чинить, а открывает case file. Проблема обычного «just debug it» в том, что там смешиваются три разные операции: смотреть на факты, рассуждать о причине и менять код для проверки теории. Из этого возникают narrative lock-in and evidence amnesia: первая правдоподобная история начинает подчинять себе наблюдения, а уже проверенные тупики не сохраняются для следующего человека. [BMAD Forensic Investigation](https://docs.bmad-method.org/explanation/forensic-investigation/)

Поэтому `bmad-investigate` устроен как отдельная дисциплина: finding получает уровень уверенности; confirmed findings должны ссылаться на конкретные logs, code, dumps, path:line or timestamp; deductions отделяются от confirmed facts; hypotheses явно помечаются как неподтверждённые и содержат, что их подтвердит или опровергнет. Investigation starts from a stronghold — одного подтверждённого факта, к которому можно вернуться, если рассуждение ушло в сторону. Гипотезы не удаляются: их статус меняется на Open, Confirmed or Refuted, а resolution объясняет, чем они были закрыты. Итоговый файл лежит в `{implementation_artifacts}/investigations/{slug}-investigation.md` and separates confirmed findings, deductions, hypotheses, timeline, data gaps, conclusions, reproduction plan and backlog. [BMAD Forensic Investigation](https://docs.bmad-method.org/explanation/forensic-investigation/)

Для главы VIII здесь важен не брендированный workflow, а чистое различие профилей. Investigation and implementation reward different instincts: investigator должен быть медленнее, точнее и осторожнее, implementer — быстрее и увереннее в пределах уже выбранной story. Если compatibility suite для `billing/API` падает без ясной причины, профиль investigation должен вернуть case file: что реально наблюдается, какие выводы следуют из наблюдений, какие гипотезы остаются открытыми, каких данных не хватает, какой следующий профиль нужен. Он не должен сразу менять production code. Только после этого проект может выбрать: продолжать dev-story, запускать correct-course, уточнять story, просить человека о product decision или расширять brownfield-модель.
```

## Что пока оставлено следующему проходу

- В тексте всё ещё есть заметный английский слой: `current-practice`, `workflow`, `implementation`, `read set`, `execution`, `gate`, `story creation`, `correct-course`, `human checkpoint`. Часть терминов нужно оставить как source-native, но следующий языковой проход должен убрать английский клей там, где он не является точным названием.
- GSD-раздел после проверки выглядит достаточно наполненным для текущего уровня главы. Его не переписывал, чтобы не перегрузить chapter draft каталогом файлов.
- Малые профили Jesse/HumanLayer/Matt пока не расширял: они выполняют функцию связующего слоя между большими методиками и маленькими skills/gates. Расширение здесь может начать уводить главу в соседнюю тему execution harness.
- В следующем редакторском проходе нужно проверить, не стала ли BMAD-часть непропорционально тяжёлой относительно GSD и малых профилей. Если стала, лучше не удалять фактуру, а разнести её более плавно.
