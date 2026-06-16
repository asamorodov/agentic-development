# 12 — визуальный слой главы VIII

Статус: выполнено. Глава прочитана как объяснительная структура, а не как место для декоративных картинок. Реальных source images, которые следовало бы немедленно вставить в главу, не найдено. Самые сильные визуальные кандидаты здесь — синтетические объяснительные схемы, потому что предмет главы не отдельный инструмент, а механизм выбора режима продолжения работы.

## Главный вывод

Визуальный слой главы должен объяснить одну вещь: **устойчивое рабочее состояние ещё не говорит, каким способом продолжать работу**. Поэтому лучший visual candidate — не скриншот интерфейса BMAD, GSD или Gas Town, а схема интерфейса между work state and profile selection.

Если в главу вставлять только одну фигуру, это должна быть схема:

```text
work state / signal
  → profile selection
  → role-specific read set
  → allowed action set
  → required output
  → gate / stop / reroute
  → durable state update
```

Она напрямую поддерживает центральный тезис главы и не привязана к одному источнику.

## Figure candidates

| Figure id | Тип | Disposition | Где ставить | Зачем нужна |
|---|---|---|---|---|
| `fig-viii-process-profile-interface` | synthetic explanatory figure | recommended primary | После раздела «Когда процесс становится артефактом» | Показывает профиль как интерфейс: состояние/сигнал → выбор режима → чтение → действие → выход → gate/reroute → обновление состояния. Это главная схема главы. |
| `fig-viii-billing-api-profile-routing` | synthetic explanatory figure | recommended secondary, если нужна вторая схема | После таблицы «Один рабочий узел, несколько правильных маршрутов» | Делает сквозной пример зрительно понятным: один PWG-узел `billing/API` может вести к story creation, brownfield investigation, correct-course, verification, human checkpoint or execution, а выход каждого маршрута возвращается в work state. |
| `fig-viii-bmad-investigation-boundary` | source-backed redraw / synthetic explanatory figure | defer | После rewritten BMAD investigation block, только если раздел останется тяжёлым после редакторского прохода | Может показать разницу investigation vs fixing: confirmed/deduced/hypothesized → case file → recommended next profile, без автоматической правки production code. Основание — BMAD Forensic Investigation. Пока лучше оставить прозой, чтобы не перегрузить BMAD-раздел. |
| `fig-viii-gsd-phase-artifact-profile` | source-backed redraw | defer | В GSD-разделе, если после структуры окажется, что GSD-переходы непонятны | Обобщает Discuss → Plan → Execute → Verify → Ship и `.planning/` artifacts. Но это уже подробно раскрыто в GSD atlas article; в теоретической главе отдельная GSD-схема может перетянуть внимание на один метод. |
| `fig-viii-bmad-workflow-map` | real source image / external-real-candidate | defer / maybe link, not inline now | В BMAD-разделе только при asset-pass и rights/quality проверке | Официальная Workflow Map полезна как source image, но она слишком BMAD-specific для центральной главы и уже учтена в BMAD atlas image plan как external-real-candidate. В главе VIII её лучше не вставлять без явной необходимости. |
| `fig-viii-small-profiles-as-gates` | synthetic explanatory figure | reject for now | Нет места в текущей версии | Можно было бы показать skills/gates/hooks как малые профили, но это близко к главам IX–X и рискует размножить визуальные сущности. |
| `fig-viii-gastown-boundary` | local real/synthetic asset reuse | reject/defer to chapter X | Не вставлять в главу VIII | `gastown-architecture.svg` and `gastown-basic-workflow.svg` важны для верхней границы, но они объясняют организационную среду, а не выбор режима одного узла. Лучше оставить Gas Town visuals для главы X. |

## Asset brief: `fig-viii-process-profile-interface`

Тип: synthetic explanatory figure.

Предлагаемый локальный файл: `content/assets/theory-images/protected-process-profile-interface.svg`.

Alt text:

```text
Схема protected process profile: рабочее состояние или сигнал проходят через выбор профиля, набор обязательного чтения, разрешённые действия, ожидаемый выход, gate/stop/reroute и возвращаются в долговечное состояние работы.
```

Caption:

```html
<figcaption>
  <strong>Защищённый процессный профиль как интерфейс продолжения.</strong>
  Долговечное состояние работы хранит, где находится задача, но следующий шаг выбирается отдельным профилем: что читать, что можно менять, какой выход оставить и когда остановиться или перенаправить работу.
</figcaption>
```

Содержание схемы:

```text
[Work state / signal]
  examples: PWG node, STATE.md, sprint-status.yaml, failed CI, review comment, change trigger
        ↓
[Profile selection]
  story creation | execution | review | correct-course | investigation | human checkpoint
        ↓
[Role-specific read set]
  requirements, plan, story, project-context, code/logs/tests, review criteria
        ↓
[Allowed action set]
  create story | patch code | write review | create Sprint Change Proposal | open case file | ask decision
        ↓
[Required output]
  story file | code+tests | PASS/FAIL/CONCERNS | proposal | investigation report | decision request
        ↓
[Gate / stop / reroute]
  pass | fail | blocked | needs human | reroute to another profile
        ↓
[Durable state update]
  updated node, blocker, decision, evidence, next profile recommendation
```

Editorial note: фигура должна быть простой, горизонтальной или вертикальной; без логотипов GSD/BMAD/Gas Town. Иначе она начнёт выглядеть как схема конкретного инструмента, а глава говорит о слое над инструментами.

## Asset brief: `fig-viii-billing-api-profile-routing`

Тип: synthetic explanatory figure.

Предлагаемый локальный файл: `content/assets/theory-images/billing-api-profile-routing.svg`.

Alt text:

```text
Схема одного рабочего узла billing/API, от которого расходятся разные правильные маршруты: story clarification, brownfield investigation, correct-course, verification, human checkpoint и execution; каждый маршрут возвращает свой выход в рабочее состояние.
```

Caption:

```html
<figcaption>
  <strong>Один узел работы, несколько правильных маршрутов.</strong>
  `billing/API` уже имеет рабочее состояние, но следующий ход зависит от сигнала: неполная story, неизвестное старое поведение, сломанный план, падающая проверка, продуктовый контракт или готовый scope требуют разных профилей.
</figcaption>
```

Содержание схемы:

```text
                  ┌─────────────────────────┐
                  │ PWG node: billing/API   │
                  │ deps, CI, review, block │
                  └────────────┬────────────┘
                               │
      ┌────────────────────────┼────────────────────────┐
      │                        │                        │
[story incomplete]      [unknown old API]       [plan contradicted]
      ↓                        ↓                        ↓
story creation         brownfield/investigation  correct-course
      ↓                        ↓                        ↓
story file + questions confirmed/deduced/hyp.    Sprint Change Proposal
      │                        │                        │
      └──────────────→ durable work state ←──────────────┘

[CI unclear] → investigation / verification → PASS/FAIL/CONCERNS
[product contract] → human checkpoint → decision / blocked state
[scope clear] → execution → code/tests/review-needed
```

Editorial note: эта схема полезна, если после следующего редакторского прохода таблица «Один рабочий узел, несколько правильных маршрутов» покажется слишком сухой. Если таблица уже достаточно читаема, фигуру можно не вставлять, чтобы не дублировать материал.

## Real source images and local assets

### Open GSD / GSD Core

Официальный GSD material в текущем корпусе лучше поддерживает source-backed redraw, а не real image insertion. В GSD atlas article уже были созданы synthetic figures для process/runtime profile and artifact consumption. Для главы VIII лучше не переносить их напрямую: они объясняют GSD как метод, а не общий слой protected process profiles.

Disposition: `defer`. Возможен source-backed redraw `fig-viii-gsd-phase-artifact-profile`, если после структурной проверки GSD-раздел окажется недостаточно ясным.

### BMAD Method

В BMAD atlas image plan уже зафиксирован официальный Workflow Map как `external-real-candidate`. Для главы VIII этот кандидат полезен только как source image for BMAD subsection. Но глава не является статьёй о BMAD, а Workflow Map визуально слишком привязывает теорию к одному методу.

Disposition: `defer`. Не вставлять без отдельного asset-pass, rights/quality проверки и решения, что BMAD-раздел действительно нуждается в source image.

### HumanLayer / story images

Локальные изображения HumanLayer (`context-firewall`, `sub-agents`, `backwards-harness`, `too-many-tools`) полезны для тем контекста, harness and subagents. В этой главе они были бы косвенными: они показывают execution/context architecture, но не сам выбор process profile.

Disposition: `reject for chapter VIII`, кроме возможной ссылки в будущей главе IX or X.

### Gas Town / Beads

`beads-task-graph-memory.svg`, `gastown-architecture.svg`, `gastown-basic-workflow.svg` and Gas Town atlas SVGs уже существуют локально и полезны для темы организационной среды. Но в главе VIII Gas Town — верхняя граница, а не центральный объект.

Disposition: `defer to chapter X`. Вставка здесь будет преждевременной и смешает «каким режимом продолжать один узел» с «как организовать много рабочих линий».

## Что не нужно делать

- Не вставлять BMAD Workflow Map только потому, что она является реальным source image. В этой главе source specificity может навредить общей теории.
- Не заменять реальные HumanLayer/Gas Town assets синтетикой: если эти темы понадобятся в будущих главах, лучше использовать уже сохранённые локальные изображения или source-derived SVGs.
- Не рисовать большой каталог профилей. Глава и так содержит таблицы; визуальный слой должен объяснять механизм, а не повторять список ролей.
- Не вставлять иллюстрацию, которая показывает «много агентов» вообще. Это уведёт главу к execution environment / orchestration.

## Рекомендация для следующей редакции

Вставить в финальную главу максимум две фигуры:

1. `fig-viii-process-profile-interface` — основной синтетический рисунок после объяснения process artifact;
2. `fig-viii-billing-api-profile-routing` — только если таблицу со сквозным примером решено разгрузить или визуально усилить.

Все остальные кандидаты оставить в очереди или перенести в соседние главы.
