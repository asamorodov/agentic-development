# Решение и следующий рабочий план

Дата: 2026-06-05

## 1. Рекомендуемое решение

Перейти на новую архитектуру:

```text
Агентская разработка и AI-driven SDLC:
как меняется жизненный цикл программного изменения
```

Но использовать её не как корпоративную SDLC-фазовую схему, а как lifecycle программного изменения:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение / обучение среды
```

Предыдущий structural synthesis plan не отменяется. Он становится процессным контрактом:

```text
AI-driven SDLC — верхняя структура.
Structural synthesis — правила качества и защиты от каталога.
```

## 2. Почему это лучше

1. Новая рамка даёт сквозную линию, которой не хватало expanded-версии.
2. Она органично включает новые AI-SDLC источники: DORA, Bain, A-SDLC survey, SLR, Codex, Copilot cloud agent, GitHub governance, OpenSSF, technical debt sources.
3. Она переводит кейсы из статуса “интересные примеры” в статус “вертикальные срезы lifecycle”.
4. Она лучше связывает теорию с Handbook/Fieldbook: Handbook становится картой выбора режима программного изменения.
5. Она позволяет сохранить старую композиционную дисциплину, если явно оставить structural synthesis guardrails.

## 3. Что нельзя делать дальше

- Не продолжать honest-pass cycles по expanded-версии как основному документу.
- Не пытаться “встроить” AI-driven SDLC в текущую expanded-структуру косметически.
- Не делать новый массовый поиск источников до skeleton/part-project.
- Не раскрывать все кейсы одинаково.
- Не превращать AI-driven SDLC в “AI in requirements / AI in coding / AI in testing”.

## 4. Что сделать первым

### 4.1. Создать skeleton-документ

Файл:

```text
current/Theoretical_synthesis_rebuilt.md
```

Содержит только:

- название;
- краткий preface;
- структуру частей;
- управляющий тезис каждой части;
- функцию каждой части;
- anchors/contrasts/move-drop placeholders;
- ссылки на будущие dossiers.

### 4.2. Создать dossiers

Минимальный набор:

```text
cases/AI_SDLC_FRAME_DOSSIER.md
cases/SWE_CHAT_PROGRAMMING_BY_CHAT_DOSSIER.md
cases/SPDD_DOSSIER.md
cases/GAS_TOWN_DOSSIER.md
cases/POLICY_GOVERNANCE_DOSSIER.md
```

Особенно важно: Gas Town dossier должен восстановить старую фактуру и новую DoltHub/Gas Town фактуру до уровня, достаточного для отдельной части.

### 4.3. Первый writing batch

Я бы не начинал сразу с частей I–III. Лучше:

```text
Введение + Части I–II
```

Функция batch:

- проверить голос новой рамки;
- убедиться, что она не стала whitepaper;
- поставить empirical ground через SWE-chat/Programming by Chat;
- не перегрузить старт SPDD.

После этого делать:

```text
Часть III + SPDD deep block
```

а затем:

```text
Части IV–VI
Часть VII / Gas Town
Части VIII–X + заключение
```

## 5. Codex/process implication

В Codex это не должно запускаться как “rewrite whole theory”. Первый Codex-task должен быть process/scaffold:

1. создать skeleton;
2. разложить source map;
3. создать dossiers placeholders;
4. создать checks;
5. создать decision ledger;
6. не переписывать основной текст без отдельного gate.

## 6. Human gates

Обязательные решения за пользователем:

1. Утверждение AI-driven SDLC как master architecture.
2. Утверждение места SPDD: Part III deep block vs separate Part IIIA.
3. Утверждение Gas Town как отдельной Части VII.
4. Утверждение первого writing batch: Introduction + Parts I–II или Introduction + Parts I–III.
5. Утверждение того, какие medium cases не попадут в основной текст.

## 7. Короткая формула

```text
Не ремонтировать expanded-досье.
Собрать новый clean synthesis.
Новая форма — lifecycle программного изменения.
Старая дисциплина — часть как мысль, кейсы подчинены тезису.
Deep anchors — SPDD и Gas Town.
Empirical ground — SWE-chat / Programming by Chat.
Boundary — policy/governance cluster.
Outcome — Handbook как карта выбора режима.
```
