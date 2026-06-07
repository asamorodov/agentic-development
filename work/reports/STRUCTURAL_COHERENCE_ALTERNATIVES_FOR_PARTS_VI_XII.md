# Structural coherence alternatives for Parts VI–XII

Дата: 2026-06-07  
Статус: рабочий сравнительный отчёт перед skeleton v4.  
Основание: пользователь подтвердил риск, что Parts VI–XII могут распухнуть и стать списком артефактов. Нужно проверить альтернативные структуры, прежде чем делать skeleton.

Этот документ не меняет `work/approved-ai-sdlc-plan.md`. Он проверяет три варианта композиции для Parts VI–XII and compares them with current v4 plan.

## Исходная проблема

После Part V документ получает очень много правильных, но потенциально разрозненных материалов:

- состояние проекта;
- context files;
- codebase readiness;
- GSD/BMAD;
- environments;
- policies;
- secrets;
- traces;
- architecture quality;
- test data;
- evidence package;
- ownership;
- lifecycle tail.

Если писать по каждому артефакту отдельную подглаву, текст снова станет каталогом. Поэтому структура должна строиться не по “какие артефакты есть”, а по “какое напряжение lifecycle эта часть разрешает”.

## Main baseline: v4 approved plan

Текущий v4 план:

```text
VI. Контекст и рабочее состояние: проект как интерфейс агента
VII. Делегирование: выбор режима работы, а не выбор инструмента
VIII. Исполнение: среда агента, harness, tools, permissions
IX. Deep case: Gas Town / Beads как организационно-операционный lifecycle
X. Свидетельства, тесты, ревью и качество доказательства
XI. Завершение, governance и внешний контур
XII. Хвост lifecycle: сопровождение, долг и обучение среды
```

Сильная сторона: сохраняет lifecycle sequence and all coverage.  
Слабость: внутренние subsection lists могут превратиться в artifact catalog.

## Honest pass 1: Conservative lifecycle rewrite

### Идея

Не менять верхний список частей. Вместо этого изменить внутреннюю композицию Parts VI–XII: каждая часть получает governing tension and narrative subsections.

### Структура

```text
VI. Как проект становится читаемым для агента
  1. Что агент должен знать, чтобы не действовать вслепую
  2. Где живёт состояние задачи
  3. Почему больше контекста не значит лучше
  4. Как кодовая база становится рабочей поверхностью
  5. Где контекст начинает устаревать

VII. Как выбрать форму делегирования
  1. Когда достаточно разговора
  2. Когда нужен research/plan
  3. Когда нужна спецификация
  4. Когда процесс становится устанавливаемым артефактом
  5. Когда агенту надо отказать

VIII. Как действие агента становится ограниченным и воспроизводимым
  1. Способность действовать
  2. Граница действия
  3. Воспроизводимость действия
  4. Исполняемые ограничения
  5. След действия

IX. Gas Town / Beads как организационно-операционный lifecycle
  сохранить как deep case

X. Что именно должно быть доказано
  1. Почему summary агента не является свидетельством
  2. Почему один evidence type не подходит всем изменениям
  3. Поведенческая правильность
  4. Граничная правильность
  5. Архитектурная сохранность
  6. Надёжность доказательства: данные, среда, oracle
  7. Социальная проверка
  8. Трасса выполнения

XI. Кто имеет право завершить изменение
  1. Агент может исполнить, но не владеть завершением
  2. Кто обязан смотреть
  3. Кто может принять
  4. Кто отвечает за выпуск
  5. Внешний контур
  6. Восстановимость завершения

XII. Как изменение возвращается в среду
  1. Release feedback
  2. Incident feedback
  3. Drift feedback
  4. Supply/security feedback
  5. User-facing memory
  6. Возврат в specs, tests, policies, context files
```

### Плюсы

- Минимальная перестройка approved plan.
- Сохраняет lifecycle order.
- Удерживает v4 coverage.
- Уменьшает риск каталога за счёт governing questions.
- Хорошо подходит для skeleton v4.

### Минусы

- Номера частей and boundaries остаются почти прежними; если Part VI or Part X всё равно перегрузить, структура сама не спасёт.
- Требует дисциплины writing: artifacts as support, not headings.

### Оценка

```text
Связность: 8.5/10
Риск каталога: средний, управляемый
Цена перестройки: низкая
Совместимость с approved plan: высокая
```

## Honest pass 2: Compressed flow after Part V

### Идея

После specification zone сократить количество частей, чтобы читатель видел меньше “станций” and stronger flow.

### Альтернативная структура

```text
VI. Проект как агентская рабочая поверхность
  объединяет context, project state, codebase readiness, context files, catalog

VII. Режим делегирования и установленный процесс
  объединяет modes, GSD/BMAD, research/plan/spec-first, refusal

VIII. Контролируемое исполнение
  tools, sandbox, worktrees, environment, policies, secrets, traces

IX. Gas Town / Beads
  deep organizational slice

X. Доказательство изменения
  evidence package, tests, contracts, architecture quality, test data, review, traces

XI. Право завершения
  governance, ownership, open-source boundary, release authority

XII. Возврат изменения в среду
  lifecycle tail, incidents, release, drift, SBOM, context cleanup
```

This is close to v4 but wording is more reader-facing and less artifact-facing.

### Плюсы

- Сильнее читательский поток.
- Headings become questions/claims, not categories.
- Part X becomes “proof of change” instead of “tests/review/benchmarks”.

### Минусы

- Почти то же количество частей, but title changes might require approved plan update.
- Still needs internal anti-catalog discipline.
- Less explicit “context vs delegation vs execution” if headings become too poetic.

### Оценка

```text
Связность: 8.2/10
Риск каталога: ниже baseline
Цена перестройки: средняя
Совместимость с approved plan: высокая-средняя
```

## Honest pass 3: Comparative deep-slice structure

### Идея

Удерживать Parts VI–XII через сравнительные пары/тройки cases, not through artifact clusters. This gives non-template chapters and avoids one-case-per-heading.

### Альтернативная структура

```text
VI. Как состояние работы становится внешним
  Boris Tane / HumanLayer / GSD as contrastive line

VII. Когда процесс становится артефактом
  GSD vs BMAD vs Spec Kit vs Reversa

VIII. Как автономия покупается средой
  Harness Engineering / Sandvault / Codex/Copilot/Claude/Jules

IX. Gas Town / Beads
  deep organizational slice, with contrast to GSD/BMAD

X. Почему доказательство шире тестов
  TDAD / benchmarks / architecture fitness / test data

XI. Кто завершает изменение
  SASE / open-source policies / CODEOWNERS

XII. Как хвост lifecycle учит среду
  incidents / SBOM / provenance / context cleanup
```

### Плюсы

- Самый нешаблонный вариант.
- Позволяет делать живые comparisons instead of artifact lists.
- GSD/BMAD can be evaluated properly without pretending they are SPDD-level.
- Good for reader interest.

### Минусы

- Самый высокий риск снова стать case catalog.
- Требует stronger dossiers before skeleton.
- Some source pairs may not be equally deep.
- Could pull attention away from lifecycle sequence.
- Might overpromote GSD/BMAD beyond available source depth.

### Оценка

```text
Связность: 7.5/10 if carefully written, 6/10 if not
Риск каталога: высокий
Цена перестройки: высокая
Совместимость с approved plan: средняя
```

## Comparison

| Criterion | Baseline v4 | Pass 1 Conservative | Pass 2 Compressed Flow | Pass 3 Comparative |
|---|---:|---:|---:|---:|
| Preserves approved plan | 10 | 10 | 8 | 6 |
| Reduces artifact-list risk | 5 | 8 | 8 | 7 |
| Keeps lifecycle movement | 8 | 9 | 8.5 | 7 |
| Reader clarity | 7 | 8.5 | 9 | 8 |
| Requires new dossiers | 6 | 6 | 6 | 8 |
| Risk of catalog relapse | High | Medium-low | Medium-low | Medium-high |
| Best use | Plan contract | Skeleton basis | Title refinement | Local comparative subchapters |

## Recommendation

Use **Pass 1** as the main basis for skeleton v4.

Borrow from **Pass 2** for stronger reader-facing titles, especially:

- Part X: `Доказательство изменения`;
- Part XII: `Возврат изменения в среду`.

Borrow from **Pass 3** only as local comparative subchapters, not as new top-level architecture.

Practical decision:

```text
Do not change approved top-level part list yet.
In skeleton, rewrite internal headings of VI–XII around tensions, not artifact classes.
Use comparative pairs/trios inside parts where they clarify the lifecycle problem.
```

## Anti-catalog rule for skeleton

For each subsection in VI–XII, ask:

```text
What lifecycle tension does this subsection resolve?
```

If the answer is just “this artifact exists”, move the material to dossier, source map, Handbook or Fieldbook.
