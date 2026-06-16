# 12 — Визуальный слой: figure candidates и asset briefs

## Чтение главы как объяснительной структуры

Глава держится на переходе от одиночного work state к обслуживаемому потоку многих работ. Поэтому картинки должны помогать не «показать Gas Town вообще», а удержать три различения:

1. почему давление масштаба порождает новые механизмы;
2. чем town-level organization отличается от rig-level work state;
3. как конкретная работа проходит через dispatch, hook, наблюдение, merge/recovery и возврат состояния.

Не нужно вставлять картинку только потому, что она найдена. Особенно опасны две формы перегруза: большой глоссарий ролей Gas Town и повторение Beads/PWG-диаграммы из предыдущей главы. Для X лучше 2–3 иллюстрации: одна главная объяснительная схема, одна source-derived схема по two-tier Beads/Gas Town, одна optional workflow-схема, если текст станет слишком абстрактным.

## figure_candidates

| ID | Тип | Путь / источник | Статус | Где ставить | Назначение | Решение |
|---|---|---|---|---|---|---|
| `fig-x-pressure-mechanism-stack` | local synthetic explanatory figure | `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg` | готовый локальный asset | после первого различения work state / flow service или перед разделом о Gas Town | Показывает: work растворена в чатах → нужен durable object; исполнителей много → роли lifecycle; работы больше capacity → queue/scheduler; сессии умирают → recovery/prime; шум скрывает сбои → problem view/service agents. | **Включить как главную схему главы.** Она лучше всего работает на центральный аргумент, а не на справочник Gas Town. |
| `fig-x-two-tier-beads-flow` | source-derived local asset | `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg` | готовый локальный asset, основан на Figure 6 / “Welcome to Gas Town” | в разделе «Gas Town как город вокруг рабочих объектов», рядом с town-level / rig-level distinction | Показывает, что Gas Town — не один список задач, а два слоя состояния и адресации: town-level orchestration и rig-level project work. | **Включить.** Эта схема удерживает главное отличие X от VII/PWG. |
| `fig-x-gastown-basic-workflow` | source-backed local redraw | `content/assets/theory-images/gastown-basic-workflow.svg` | готовый локальный asset, основан на Gas Town README basic workflow mermaid | возможно в сквозном примере, после первого dispatch | Показывает простую петлю: You → Mayor → Convoy → Agent → Hook → status/report/state. | **Условно включить**, если после интеграции P11 пример всё ещё звучит абстрактно. Не включать, если текст уже перегружен двумя Gas Town-схемами. |
| `fig-x-gastown-worker-roles` | source-derived local asset | `content/assets/atlas-images/gas-town/gastown-worker-roles.svg` | готовый локальный asset, основан на Figure 5 / “Welcome to Gas Town” | теоретически рядом с ролями Mayor/Polecat/Witness/Refinery/Deacon | Показывает роли как функции lifecycle: human decision, interface, long-lived coding, ephemeral workers, stuck-work recovery, merge pressure, service work. | **Deferred / optional.** Полезно, но рискует превратить главу в глоссарий ролей. Использовать только если тексту явно нужна визуальная развязка ролей. |
| `fig-x-gastown-architecture` | source-backed local redraw | `content/assets/theory-images/gastown-architecture.svg` | готовый локальный asset, based on Gas Town README architecture mermaid | рядом с Gas Town overview | Показывает Mayor, town workspace, rigs, crew, hooks, worker agents and git worktrees. | **Deferred.** Хорошо для Atlas/Reference, но для главы X менее точно, чем pressure-stack and two-tier flow. |
| `fig-x-beads-task-graph-memory` | local explanatory figure | `content/assets/theory-images/beads-task-graph-memory.svg` | готовый локальный asset | рядом с Beads/PWG lower layer | Показывает Beads как dependency-aware task graph memory, `bd ready`, `bd update --claim`, `bd dep add`, `bd prime`. | **Deferred / caution.** Может помочь Beads-разделу, но высокий риск дублировать главу VII. Включать только если редакторский проход покажет, что Beads непонятен без визуальной опоры. |
| `fig-x-gastown-mayor-hub` | local asset / likely source or UI-like illustration | `content/assets/theory-images/gastown-mayor-hub.webp` | готовый local asset | рядом с Mayor / human surface | Может показать Mayor as hub. | **Reject for now.** Слишком UI/role-specific; центральную структуру лучше держат SVG-схемы. |
| `fig-x-mae-trace-observability` | real/source image local asset | `content/assets/theory-images/mae-honeycomb-trace-observability.png` или `content/assets/story-images/11-mae-honeycomb-trace.png` | готовый local source image | supporting stories section, если Mae paragraph расширится | Показывает observability/traces as another form of flow visibility. | **Reject/defer.** Для X это supporting parallel, не основной аргумент. Если вставить, глава начнёт спорить сама с собой: Gas Town chapter suddenly shows Honeycomb trace. |

## Рекомендуемая вставка 1: главная схема давления и механизмов

### Asset brief

- **ID:** `fig-x-pressure-mechanism-stack`
- **Path:** `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg`
- **Type:** synthetic explanatory figure, already local
- **Placement:** после раздела `Work state и flow service`, перед подробным Beads/Gas Town разбором.
- **Purpose:** закрепить главную мысль главы: каждый механизм появляется как ответ на давление масштаба, а не ради терминологической игры.
- **Suggested caption:**

```html
<figure class="source-figure" id="fig-x-pressure-mechanism-stack">
  <img src="../assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg" alt="Схема: давления многопоточной агентской работы и механизмы Gas Town-like среды: durable work state, роли жизненного цикла, queues, recovery, problem view." loading="lazy" />
  <figcaption>Масштабирование агентской работы требует не только большего числа исполнителей, а набора обслуживающих механизмов: устойчивого рабочего объекта, ролей жизненного цикла, очередей, recovery, problem view и человеческого решения. Схема синтетическая, собрана по материалам Gas Town/Beads и локального атласа.</figcaption>
</figure>
```

### Notes

Путь `../assets/...` нужно проверить относительно будущего расположения финальной главы. В pass-файле путь может быть другим; для сайта обычно главы смотрят на `../assets/...`, но перед финальной интеграцией лучше сверить с соседними главами.

## Рекомендуемая вставка 2: two-tier Beads/Gas Town flow

### Asset brief

- **ID:** `fig-x-two-tier-beads-flow`
- **Path:** `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg`
- **Type:** source-derived local asset, based on “Welcome to Gas Town” Figure 6 description.
- **Placement:** в разделе `Gas Town как город вокруг рабочих объектов`, сразу после абзаца о town-level и rig-level beads.
- **Purpose:** помочь читателю увидеть, что Gas Town — не просто один task tracker; есть слой организации town и слой работы rig.
- **Suggested caption:**

```html
<figure class="source-figure" id="fig-x-two-tier-beads-flow">
  <img src="../assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg" alt="Схема two-tier Beads flow: town-level orchestration and rig-level project work with routing prefixes and project ids." loading="lazy" />
  <figcaption>Двухуровневая форма Beads/Gas Town: town-level слой держит координацию, Mayor и маршрутизацию, а rig-level слой — локальную проектную работу, implementation tasks и merge/review. Локальный source-derived asset по материалам Steve Yegge, “Welcome to Gas Town”.</figcaption>
</figure>
```

## Условная вставка 3: basic workflow

### Asset brief

- **ID:** `fig-x-gastown-basic-workflow`
- **Path:** `content/assets/theory-images/gastown-basic-workflow.svg`
- **Type:** source-backed local redraw based on Gas Town README workflow mermaid.
- **Placement:** рядом со сквозным примером после первого dispatch, если нужен визуальный якорь.
- **Purpose:** показать простую петлю You → Mayor → Convoy → Agent → Hook → status/report/state.
- **Decision:** включать только если после следующей интеграции глава кажется слишком абстрактной. Если уже включены pressure-stack и two-tier flow, третья Gas Town-схема может перегрузить текст.
- **Suggested caption if included:**

```html
<figure class="source-figure" id="fig-x-gastown-basic-workflow">
  <img src="../assets/theory-images/gastown-basic-workflow.svg" alt="Базовая петля Gas Town: пользователь задаёт работу, Mayor координирует, Convoy диспетчеризует, Agent исполняет, Hook возвращает состояние." loading="lazy" />
  <figcaption>Базовая петля Gas Town-like работы: задача проходит через Mayor и Convoy к исполнителю, а hook возвращает завершение и состояние в общий контур. Локальная перерисовка по Gas Town README.</figcaption>
</figure>
```

## Отклонённые / отложенные иллюстрации

### `gastown-worker-roles.svg`

Хорошая карта ролей, но для главы X есть риск неправильной оптики. Если поставить её в середине текста, читатель начнёт запоминать Mayor/Polecat/Witness/Refinery/Deacon как глоссарий. Глава должна вести не через персонажей, а через сбой потока. Этот asset лучше оставить для Atlas/Reference или использовать только если редакторский проход покажет, что роли стали непонятны.

### `gastown-architecture.svg`

Полезно для общего представления Gas Town, но pressure-stack и two-tier flow точнее работают на аргумент главы. Architecture diagram может дублировать two-tier flow и basic workflow.

### `beads-task-graph-memory.svg`

Сильная картинка для Beads/PWG, но вероятно относится к главе VII. В X её можно использовать только при явной необходимости объяснить нижний слой Beads читателю, который пропустил предыдущую главу. Иначе она утянет X назад к persistent work graph.

### Mae / Honeycomb trace images

Реальные/source images важны для истории Mae, но в X Mae — supporting parallel. Вставка Honeycomb trace может создать ложный центр тяжести: глава внезапно станет про observability, а не про Beads/Gas Town/flow service. Отложить.

## Итоговое решение для следующего draft pass

1. Встроить **две** иллюстрации по умолчанию:
   - `fig-x-pressure-mechanism-stack`;
   - `fig-x-two-tier-beads-flow`.
2. Не вставлять `gastown-basic-workflow.svg` автоматически; оставить как optional.
3. Не заменять existing source-derived/local assets синтетикой. Они уже готовы и лучше согласованы с текущим корпусом.
4. Перед финальной интеграцией проверить относительные пути изображений по фактическому расположению итоговой главы.
5. Подписи писать не как «на рисунке показано», а как мини-тезис главы: почему эта схема нужна для понимания потока.
