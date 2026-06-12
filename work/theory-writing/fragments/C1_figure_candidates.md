# C1 figure candidates

Статус: companion-файл финальной упаковки `C1_specification_to_pwg.md`; визуальный набор после стилевых проходов не расширялся.

## Inline figures used

| Figure ID | Класс | Где стоит | Gate usefulness/nontriviality | Решение |
| --- | --- | --- | --- | --- |
| `fig-c1-specification-to-pwg-handoff` | `synthetic_figure` | После вводного хода о SPDD / Spec Kit / Kiro и до раздела “Что должно перейти из спецификации в состояние работы”. | Проясняет нетривиальную передачу: из области изменения, плана/задач, ADR/контракта, критериев приёмки, ожиданий по свидетельствам и состояние источника или визуального кандидата должны появиться разные элементы PWG. Таблица не повторяет соседний абзац, а держит границу между спецификационный слой и долговечное состояние работы. | Вставлена inline в основной текст. Седьмой проход уточнил одну строку под переход от артефакта к ответственности; первый общий repair-pass сгладил терминологию без изменения визуальный класс; второй общий repair-pass русифицировал первую строку и строку ADR/contract без изменения визуальный класс; третий общий repair-pass visual layer не менял; второй стилевой проход уточнил публичную подпись и заголовок третьей колонки без изменения класса. Новая figure не добавлялась. |

## External real image candidates / deferred

| Candidate ID | Класс | Источник | Возможная роль | Asset-pass / rights / status notes | Решение |
| --- | --- | --- | --- | --- | --- |
| `fig-c1-kiro-task-status-screen` | `external_real_image_candidate` | [Kiro Specs](https://kiro.dev/docs/specs/) | Показать интерфейсный task execution/status layer: `tasks.md`, real-time status updates, in-progress/completed state, waves. | Source-depth pass подтвердил, что это реальное внешнее изображение/страничная диаграмма (`Image: Task execution in Kiro specs` / loading image), не synthetic material. Нужны screenshot/download/localization, rights-check и quality-check. Текст C1 использует факт статуса, но не вставляет картинку без asset-pass. | Deferred. |
| `fig-c1-kiro-run-all-waves` | `external_real_image_candidate` или `synthetic_figure` | [Run all tasks](https://kiro.dev/blog/run-all-tasks/), [Kiro Specs](https://kiro.dev/docs/specs/) и [Specs just got faster](https://kiro.dev/blog/faster-smarter-specs/) | Показать волны параллельного исполнения из `tasks.md`, где clear spec не отвечает на вопросы: какая волна безопасна, какой сбой локален, кто владеет зависшим узлом, какой diff требует ревью, какое evidence привязано к задаче. | Source-depth pass нашёл реальные внешние image candidates (`Task list Run all tasks`, task execution image) и уже существующее текстовое описание wave 1/wave 2/wave N. Официальные изображения требуют rights-check; synthetic replacement не вставлен, потому что был бы подменой внешнего изображения и уводил бы C1 в Kiro mechanics. | Deferred to atlas / C4. |
| `fig-c1-speckit-workflow-state` | `synthetic_figure` | [Spec Kit Workflows](https://github.github.com/spec-kit/reference/workflows.html) | Показать `state.json`, `inputs.json`, `log.jsonl` рядом с PWG-полями владением, состоянием источников, свидетельствами и восстановлением. | Полезно для технического атласа, но в C1 может смешать состояние запуска команды и состояние работы, хотя сам текст именно разводит эти уровни. | Rejected for main text; possible atlas material. |
| `fig-c1-clear-spec-unresolved-handoff` | `synthetic_figure` | Комбинация источников C1: Spec Kit Workflows, Kiro Run all/Best Practices, Beads coordination. | Показать типовую ситуацию второго прохода: спецификация утверждена, задачи запущены, часть завершилась/упала/ждёт ревью, а PWG собирает статусы `blocked_by_test`, `waiting_human`, `handoff_ready`, `evidence_attached`. | Нетривиальная, но близка к текстовому сценарию раздела “Промежуточный сбой”; добавление inline перегрузило бы короткий мостовой фрагмент. | Deferred; лучший кандидат, если редактор попросит вторую схему. |
| `fig-c1-readiness-gate-recovery-ladder` | `synthetic_figure` | Spec Kit Workflows/checklist/analyze, Kiro Best Practices, SPDD sync, Beads gate/prime/recovery. | Показать три обязательства PWG после старта: readiness как вычислимое право начать/продолжить, gate как долговечное ожидание, recovery как короткий вход из state. | Может быть полезно для atlas или C2, но в C1 начало бы конкурировать с уже вставленной handoff-схемой и добавленным текстовым абзацем. | Deferred; не вставлять без редакторского запроса на второй visual. |
| `fig-c1-spdd-reasons-canvas-to-pwg-node` | `synthetic_figure` | [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) и OpenSPDD templates | Показать, какие поля Canvas переходят в PWG-node. | Почти дублирует inline figure и рискует превратить C1 в SPDD-подраздел. | Rejected as duplicate. |
| `fig-c1-beads-ready-gate-prime` | `synthetic_figure` или `local_image_asset` after asset-pass | Beads Dependencies, `bd ready`, `bd blocked`, `bd gate`, `bd prime` | Показать ready/blocked → gate → prime/recovery как часть PWG. | Source-depth pass открыл `bd ready`/`bd blocked`, но это CLI-reference material, не готовый локальный image asset. A4 уже использует Beads asset and synthetic figures. Повторение Beads в C1 ухудшит границу с A4. | Deferred to A4/technical atlas; not inline in C1. |
| `fig-c1-source-state-transfer` | `synthetic_figure` | PWG source-state notes + visual-assets rule | Показать state of source/image candidate after specification starts. | Схема полезна, но уже покрыта одной строкой inline figure. Полная state-machine лучше подходит A4 или source/provenance atlas. | Deferred. |

## Local image assets

Локальные image assets для C1 не вставлялись. Разрешённый рабочий лист не включал общий asset catalog или локальные ассеты C1; готовый Beads SVG уже используется в A4 и не должен повторяться в мостовом фрагменте без новой роли.

## Седьмой адресный visual check

Visual layer не расширялся. Уже существующая `synthetic_figure` прошла usefulness/nontriviality gate ранее; в этом проходе уточнена только строка про acceptance criteria/ожиданий по свидетельствам, чтобы она соответствовала усиленной механике перехода. Внешние image candidates по-прежнему deferred до asset-pass.

## Восьмой адресный visual check

Visual layer не изменялся. Boundary-разведение спецификационный слой/PWG-layer выполнено прозой; новая схема не нужна и была бы повтором существующей synthetic-figure.

## Первый общий repair-pass visual regression

Visual layer не расширялся. Существующая synthetic-figure сохранена, потому что по-прежнему объясняет нетривиальный переход спецификационный слой → состояние работы; исправлена только терминологическая строка, чтобы не выглядеть рабочей заметкой или калькой.

## Второй общий repair-pass visual regression

Visual layer не расширялся. Повторная оценка подтвердила, что единственная inline `synthetic_figure` остаётся полезной: она удерживает mapping спецификационный слой → dangerous gap → PWG state. Исправлены только публичные формулировки внутри таблицы: `Scope`, `evidence`, `resolver` заменены русскими эквивалентами там, где они не были точными именами источника. External image candidates по-прежнему deferred до asset-pass.

## Третий общий repair-pass visual regression

Visual layer не изменялся. Проверка не выявила инерционной или декоративной фигуры: единственная inline-схема по-прежнему поддерживает главный переход и не подменяет внешний image asset. Дополнительные Kiro/Spec Kit/Beads изображения остаются external real image candidates или deferred ideas до отдельного asset-pass.

## Второй стилевой проход visual check

Inline-схема сохранена как `synthetic_figure`: она по-прежнему проходит usefulness/nontriviality gate и не выглядит декоративным пересказом. Изменены только публичные формулировки подписи и заголовка третьей колонки, чтобы схема читалась как часть аргумента, а не как рабочий registry. Новые кандидаты не вставлялись; external real image candidates остаются deferred до asset-pass.

## Registry notes

- Внешние изображения и source diagrams не заменялись текстовыми схемами.
- Единственная inline-схема классифицирована как `synthetic_figure` и прошла usefulness/nontriviality gate.
- Второй проход добавил кандидат `fig-c1-clear-spec-unresolved-handoff`, а третий — `fig-c1-readiness-gate-recovery-ladder`; оба оставлены deferred, потому что текст уже удерживает ситуации, где clear spec не решает continuation/ownership/handoff/readiness/recovery.
- Все внешние визуальные кандидаты оставлены в этом registry до asset-pass: rights/status notes, возможная роль и причина отказа/переноса записаны рядом.
- Пятый source-depth pass подтвердил Kiro images как external real image candidates, а не повод создавать текстовую схему. Локальных готовых C1 image assets в разрешённых входах нет.

## Readiness

`ready_with_known_debts` — визуальный слой достаточен после третьего общего repair-pass. Перед публикационной сборкой нужен asset-pass только если редактор решит, что C1 должен содержать реальный интерфейсный скриншот Kiro, Spec Kit workflow-state material или вторую synthetic-схему про unresolved handoff/readiness/gates/recovery.

## Финальная проверка упаковки

Единственная inline-фигура сохранена как `synthetic_figure` и проходит usefulness/nontriviality gate. Внешние реальные изображения остаются `external_real_image_candidate`/deferred и не заменены текстовыми суррогатами.
