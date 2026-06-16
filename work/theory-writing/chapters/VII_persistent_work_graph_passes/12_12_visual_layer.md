# P12 — визуальный слой главы VII

## Короткий вывод

Главе VII нужны не декоративные скриншоты инструментов, а несколько точных визуальных опор, которые помогают читателю увидеть различие между рассказом, задачей, графом состояния и средой выполнения. Основная иллюстрация уже есть: `content/assets/theory-images/beads-task-graph-memory.svg`. Её нужно сохранить как локально отрисованную, source-backed схему по Beads, а не заменять синтетическим текстовым блоком.

Новые реальные source images добавлять стоит осторожно. В главе есть источники с картинками вокруг HumanLayer, Mae, Codex и Gas Town, но большинство из них относятся к соседним главам: VI — context/interface, IX — execution/runtime, X — Gas Town, XI/XII — evidence/acceptance. Для VII лучше работают синтетические explanatory figures, потому что сама глава объясняет не UI конкретного инструмента, а слой состояния.

## Уже имеющийся локальный asset

### `fig-vii-beads-task-graph-memory`

- **Статус:** оставить.
- **Тип:** local asset / source-backed redraw.
- **Файл:** `content/assets/theory-images/beads-task-graph-memory.svg`.
- **Источник идеи:** Beads README / docs / graph issue tracker model.
- **Текущее место:** раздел «Что хранит Persistent Work Graph».
- **Функция в главе:** показать, что работа живёт как граф задач, зависимостей, claim-состояний и памяти, которую можно поднять через `bd prime`.
- **Почему не заменять:** это уже готовая локальная схема, специально отрисованная для теоретического сайта; она ближе к механизму главы, чем любой случайный screenshot Beads CLI.
- **Что улучшить в подписи:** сделать подпись менее общей и ближе к тезису главы:

```html
<figure class="image-asset" id="fig-vii-beads-task-graph-memory">
  <img src="../../../../content/assets/theory-images/beads-task-graph-memory.svg" alt="Схема Beads: граф задач, зависимости, закрепление работы и память агента." loading="lazy" data-repo-path="content/assets/theory-images/beads-task-graph-memory.svg" />
  <figcaption>Beads здесь важен не как продукт, а как наглядный пример формы PWG: задачи имеют зависимости, готовность, закрепление за агентом и компактное восстановление контекста через `bd prime`.</figcaption>
</figure>
```

## Figure candidates

### 1. `fig-vii-summary-vs-work-graph`

- **Статус:** рекомендовать.
- **Тип:** synthetic explanatory figure.
- **Предлагаемый файл:** можно не создавать отдельный asset; лучше вставить как HTML `<figure>` с таблицей, потому что содержание текстово-структурное.
- **Место:** после раздела «Почему хорошая сводка всё равно не спасает».
- **Зачем:** это главный визуальный мост главы. Читатель должен увидеть, что одна и та же ситуация как summary выглядит компактно, а как PWG раскрывает readiness, gates, claims, source state and forbidden actions.
- **Содержание:** две колонки: «Summary» и «PWG state».
- **Черновик HTML-блока:**

```html
<figure class="synthetic-figure" id="fig-vii-summary-vs-work-graph">
  <figcaption>Одна и та же работа как summary и как состояние графа. Summary пересказывает прошлое; PWG показывает, что можно делать, что заблокировано и что нельзя закрывать.</figcaption>
  <table>
    <thead>
      <tr><th>Summary</th><th>Persistent Work Graph</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>«Реализация почти готова, остались compatibility, CI и review»</td>
        <td>W-100 открыт; W-101–W-103 закрыты локально; W-104/W-105/W-106 блокируют closure; G-201/G-202/G-203 открыты.</td>
      </tr>
      <tr>
        <td>«Unit tests проходят»</td>
        <td>`ci/unit/18452` success on `feature@b12d44f`; не закрывает integration gate.</td>
      </tr>
      <tr>
        <td>«Нужно решить edge case»</td>
        <td>W-104 open; можно подготовить варианты; нельзя финализировать behavior до G-201.</td>
      </tr>
      <tr>
        <td>«Есть review comment»</td>
        <td>W-105 blocked by G-202; signal ещё не classified as fix/dismiss/escalate.</td>
      </tr>
      <tr>
        <td>«Следующей сессии продолжить»</td>
        <td>Agent A claim may be stale; recover branch/worktree before editing.</td>
      </tr>
    </tbody>
  </table>
</figure>
```

- **Риск:** таблица не должна стать слишком широкой. Для мобильной верстки лучше делать короткие строки или CSS-scroll для tables.

### 2. `fig-vii-work-item-state-contract`

- **Статус:** рекомендовать, если глава допускает вторую синтетическую схему.
- **Тип:** synthetic explanatory figure / compact state diagram.
- **Предлагаемый файл:** `content/assets/theory-images/pwg-work-item-state-contract.svg` или HTML table figure.
- **Место:** в разделе «Что хранит Persistent Work Graph», после объяснения work item and forbidden transitions.
- **Зачем:** показать, что PWG — не список полей, а контракт переходов состояния. Особенно полезно после P11-добавления про `ready`, `claimed`, `review`, `accepted`, `recovering`.
- **Содержание:** короткая линия состояний:

```text
found → ready → claimed → active → waiting_gate / review → accepted / rejected / recovering → cleaned
```

И рядом «запрещённые переходы»:

```text
claimed → accepted without gates/checks      forbidden
blocked → ready while blocker open           forbidden
other-agent claim → overwrite without handoff forbidden
read source → close source work              forbidden
```

- **Asset brief:**
  - background white;
  - one horizontal state lane;
  - red dashed arrows for forbidden shortcuts;
  - small callouts for `claim`, `gate`, `check basis`, `source state`, `cleanup`;
  - no product logos.
- **Причина не использовать реальное изображение:** этот механизм является авторской схемой главы, не UI источника.

### 3. `fig-vii-gates-as-durable-waits`

- **Статус:** optional / source-backed redraw.
- **Тип:** source-backed synthetic redraw по Beads `bd gate` + Temporal HITL.
- **Предлагаемый файл:** `content/assets/theory-images/pwg-gates-as-durable-waits.svg`.
- **Место:** раздел «Gate: ожидание как объект работы».
- **Зачем:** gate легко спутать с заметкой «ждём». Схема может показать, что gate блокирует work item, имеет resolver and resolution outcomes.
- **Содержание:** центральный work item W-100; три gate-узла:
  - human decision → resolved: fallback / strict / escalation;
  - `gh:run` / CI → success / failure / canceled / stale;
  - review / PR → accepted / changes requested / closed-not-merged.
- **Источник идеи:** Beads `bd gate` page; Temporal human-in-the-loop as runtime contrast.
- **Риск:** если вставить эту схему, раздел про gate может стать слишком Beads-heavy. Лучше делать её компактной.

### 4. `fig-vii-signal-triage`

- **Статус:** рекомендовать, особенно если в финальной главе остаётся Jökull/Mark/Mae.
- **Тип:** synthetic explanatory figure.
- **Предлагаемый файл:** HTML table figure; отдельный SVG не нужен.
- **Место:** раздел «Проверочный сигнал не является приказом».
- **Зачем:** визуально закрепить Fix / Dismiss / Escalate and graph-state mapping.
- **Содержание:**

```html
<figure class="synthetic-figure" id="fig-vii-signal-triage">
  <figcaption>Проверочный сигнал сначала классифицируется, и только потом меняет граф работы.</figcaption>
  <table>
    <thead><tr><th>Сигнал</th><th>Возможное состояние в PWG</th><th>Что нельзя делать автоматически</th></tr></thead>
    <tbody>
      <tr><td>CI failed</td><td>blocker / flaky signal / infrastructure issue / new work item</td><td>закрывать общий work item</td></tr>
      <tr><td>Reviewer comment</td><td>fix / dismiss / escalate / gate</td><td>чинить как приказ без triage</td></tr>
      <tr><td>Subagent report</td><td>accepted / stale / insufficient / superseded</td><td>переносить как timeless truth</td></tr>
      <tr><td>Trace or screenshot</td><td>source artifact attached to node</td><td>считать наблюдение полным acceptance</td></tr>
    </tbody>
  </table>
</figure>
```

- **Источник фактуры:** Jökull `/babysit-pr`, Mark read-only reviewer / DiffLoupe, Mae artifact → human classification.
- **Преимущество:** поддерживает важнейшую мысль главы без дополнительного внешнего изображения.

### 5. `fig-vii-source-state-flow`

- **Статус:** optional, скорее для документного процесса / later evidence chapter.
- **Тип:** synthetic explanatory figure.
- **Предлагаемый файл:** возможно `content/assets/theory-images/pwg-source-state-flow.svg`.
- **Место:** раздел «Source state: выводы стареют».
- **Содержание:**

```text
found → opened → read → attached to claim → used with link / rejected / stale / needs reopen
```

- **Зачем:** в главе много говорится про source state; читателю полезна короткая шкала.
- **Риск:** если вставить вместе с summary-vs-graph and signal-triage, визуальный слой станет перегруженным. Лучше сохранить как asset brief для будущего, а в этой главе использовать текст и billing/API snapshot.

### 6. `fig-vii-restoration-packet`

- **Статус:** optional / maybe replace by code block.
- **Тип:** synthetic explanatory figure or structured code block.
- **Место:** раздел «Prime: восстановление рабочей формы».
- **Зачем:** показать, что restoration packet is not summary.
- **Рекомендация:** отдельную картинку не делать; текущий structured text block уже работает лучше, потому что показывает конкретную форму packet. Визуальная картинка добавит меньше, чем точный пример.

### 7. `fig-vii-runtime-vs-pwg-boundary`

- **Статус:** defer to chapter IX unless final chapter needs boundary rescue.
- **Тип:** synthetic explanatory figure.
- **Содержание:** два слоя:
  - Runtime: checkpoint, replay, interrupt, durable timer, tool step.
  - PWG: readiness, claim, gate, source state, acceptance basis, recovery.
- **Зачем:** хорошо объясняет boundary, но это уже ведёт в главу IX.
- **Решение:** не вставлять в VII по умолчанию. Оставить как possible chapter IX figure.

## Real/source image candidates from existing assets

### `humanlayer-intentional-compaction.png`

- **Статус:** defer / do not use by default.
- **Тип:** local real/source image.
- **Потенциальное место:** Prime / restoration packet.
- **Почему не вставлять сейчас:** изображение про context compaction и управляемое восстановление; это ближе к главе VI. В VII оно может усилить тему восстановления, но сдвинет акцент с рабочего графа на контекстный интерфейс.

### `humanlayer-context-firewall.png`

- **Статус:** defer to VI/VIII.
- **Тип:** local real/source image.
- **Потенциальное место:** subagents section.
- **Почему не вставлять:** в VII subagents нужны только как источник typed output. Картинка про context firewall начнёт объяснять архитектуру subagents и уведёт главу к orchestration/process profile.

### `mae-honeycomb-trace-observability.png`

- **Статус:** optional but likely defer to IX/XI.
- **Тип:** local real/source image.
- **Потенциальное место:** Source state / observability artifacts.
- **Плюс:** показывает trace as checkable artifact.
- **Минус:** визуально это будет Honeycomb/observability story, а не PWG. В текущей главе достаточно сказать, что traces can become source artifacts attached to work items.

### `openai-codex-citations-evidence.webp`

- **Статус:** reject for VII / defer to evidence chapters.
- **Почему:** цитирование и проверочные основания важны, но глава VII не должна становиться главой про evidence/authority. Этот asset лучше для XI/XII.

### `gastown-architecture.svg`, `gastown-basic-workflow.svg`, `gastown-mayor-hub.webp`

- **Статус:** reject for VII / defer to X.
- **Почему:** глава VII специально не должна расширяться до Gas Town. Эти изображения перетянут внимание к организации агентов, Mayor, rigs and workflows.

## Рекомендуемая визуальная конфигурация главы VII

Минимальный вариант:

1. `fig-vii-beads-task-graph-memory` — оставить в разделе «Что хранит Persistent Work Graph».
2. `fig-vii-summary-vs-work-graph` — добавить как HTML table figure после раздела о summary.
3. `fig-vii-signal-triage` — добавить как HTML table figure в разделе о проверочных сигналах.

Расширенный вариант, если глава после финальной сборки остаётся тяжёлой для восприятия:

4. `fig-vii-work-item-state-contract` — добавить как SVG или table figure после объяснения state transitions.
5. `fig-vii-gates-as-durable-waits` — добавить как компактный source-backed redraw in gate section.

Что не добавлять по умолчанию:

- реальные HumanLayer screenshots, потому что они уводят в context engineering;
- Mae/Honeycomb screenshot, если в главе нет отдельного подблока про trace state;
- Gas Town images;
- OpenAI/Codex evidence screenshots.

## Asset briefs for possible new local figures

### Brief A — `pwg-work-item-state-contract.svg`

- **Purpose:** показать PWG как контракт переходов, а не task list.
- **Placement:** after “Что хранит Persistent Work Graph”.
- **Visual elements:** horizontal lifecycle lane; small nodes; red forbidden shortcuts.
- **Nodes:** `found`, `ready`, `claimed`, `active`, `waiting_gate`, `review`, `accepted/rejected`, `recovering`, `cleaned`.
- **Callouts:** `claim`, `gate`, `source state`, `check basis`, `cleanup`.
- **Caption:** «PWG полезен только тогда, когда состояние узла меняет следующий допустимый шаг: что можно брать, что ждёт gate, что требует проверочных оснований и что можно только восстанавливать.»
- **Source status:** synthetic explanatory figure based on the chapter’s conceptual model and Beads-inspired vocabulary; no copied source image.

### Brief B — `pwg-gates-as-durable-waits.svg`

- **Purpose:** показать gate as durable wait condition with resolution outcomes.
- **Placement:** Gate section.
- **Visual elements:** central W-100; three gate boxes; arrows to outcomes.
- **Gate boxes:** `human`, `ci/run`, `review/pr`.
- **Outcomes:** pass/approve, fail/create work, cancel/stale, escalate.
- **Caption:** «Gate — не просьба “подождать”, а состояние ожидания, которое блокирует work item и после разрешения меняет граф: закрывает блокер, создаёт новую работу или требует escalation.»
- **Source status:** source-backed redraw; fact base from Beads `bd gate` and runtime contrast from Temporal HITL.

### Brief C — `pwg-source-state-flow.svg`

- **Purpose:** показать, что источник — не URL, а состояние переноса.
- **Placement:** Source state section, if needed.
- **Visual elements:** pipeline with states and branch outcomes.
- **States:** `found`, `opened`, `read`, `attached`, `used`, `rejected`, `stale`, `needs_reopen`.
- **Caption:** «Source state нужен, чтобы следующая сессия не принимала найденную ссылку, старый CI run или subagent report за актуальное основание закрытия.»
- **Source status:** synthetic explanatory figure; do not use real images.

## Итоговое решение для следующего прохода

В финальную сборку главы нужно внести как минимум два визуальных решения:

1. сохранить и немного переподписать существующий `beads-task-graph-memory.svg`;
2. добавить `fig-vii-summary-vs-work-graph` as table figure.

`fig-vii-signal-triage` strongly recommended, потому что он удерживает Jökull/Mark/Mae не как каталог практик, а как один механизм: signal → triage → graph state.

Новые source screenshots не добавлять без отдельной причины. В этой главе они скорее ухудшат фокус: читатель начнёт смотреть на UI инструментов, хотя ему нужно понять рабочий слой состояния.
