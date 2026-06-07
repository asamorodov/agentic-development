# Plan patch recommendations after Stage 0.9

Дата: 2026-06-07  
Статус: дополняет Stage 0.5–0.8 recommendations; не меняет approved plan напрямую.

## Смысл Stage 0.9

Stage 0.9 нужен не для добавления ещё одной группы тем, а для защиты от распада на неоднородную коллекцию.

Главная рекомендация:

```text
Все новые артефакты проверять вопросом: какую функцию они выполняют в жизненном цикле программного изменения?
```

Если артефакт не переносит намерение, контекст, решение, проверку, право завершения or learning дальше по lifecycle, он не должен занимать место в основной теории.

## Patch items

### 1. Add artifact selection rule to Part I

Add:

```text
Артефакт попадает в основную теорию не потому, что он “важен в SDLC”, а потому что он переносит изменение через одну из границ lifecycle: от намерения к контексту, от контекста к исполнению, от исполнения к свидетельствам, от свидетельств к ревью, от ревью к праву завершения, от завершения к сопровождению и обучению среды.
```

### 2. Add platform/catalog/golden path to Part VI

Add:

```text
Проект как интерфейс агента может быть организован через внутреннюю платформу, каталог компонентов, владельцев, API, систем, среды выполнения and standard paths. Это не отдельная методология, а способ связать контекст, права, окружения и проверки.
```

### 3. Add reproducible/runnable environment to Part VIII

Add:

```text
Среда выполнения должна быть воспроизводимой настолько, чтобы агент мог не только читать код, но запускать проверки и оставлять свидетельства. Dev container, build configuration, dependency lock, reproducible/attestable build and test commands are evidence infrastructure.
```

### 4. Add policy-as-code cautiously

Add:

```text
Исполняемые политики связывают governance and environment. Они могут проверять часть ограничений автоматически, но сами становятся артефактами, которые нужно тестировать, ревьюить and сопровождать.
```

### 5. Add prompt/context lifecycle note

Add:

```text
Запросы, шаблоны запросов, context files and agent instructions должны иметь свой lifecycle: versioning, review, validation, regression checks and retirement. SPDD is the strongest full method here, but the general problem is broader.
```

### 6. Add artifact graph as hidden organizing model

Add:

```text
В финальном тексте не нужно вводить отдельную “часть про граф”. Но автор должен держать artifact graph as hidden model: требования, спецификации, ADR, контракты, тесты, трассы, PR, ownership and release artifacts связаны ссылками. Без этих связей список артефактов не даёт SDLC.
```

## Human gates

Human approval needed before:

- adding a new top-level platform/flow part;
- promoting policy-as-code, Backstage, platform engineering or workflow specification to deep case;
- expanding Part XII beyond a controlled tail;
- changing SPDD/Gas Town placement;
- modifying `work/approved-ai-sdlc-plan.md`.
