# Открытые вопросы главы V

## 1. Насколько подробно раскрывать общий биллинговый пример?

Пример нужен как контрольный объект сравнения, но есть риск превратить главу в вымышленный кейс. Рабочее решение: держать пример компактным и возвращаться к нему только там, где подход иначе остался бы слишком абстрактным.

## 2. В каком порядке ставить TDAD и Constitutional SDD?

Есть две разумные композиции. Первая: Spec Kit → Kiro → TDAD → Constitutional SDD, от feature-flow к rules-above-feature. Вторая: Spec Kit → Kiro → Constitutional SDD → TDAD, чтобы сначала разобрать specification/rules, а потом evidence-like test carrier. Пока предпочтительнее первая: TDAD хорошо показывает, что спецификация может стать исполнимой, а CSDD завершает ряд слоем правил выше фичи.

## 3. Нужно ли включать численные результаты TDAD?

Числа из arXiv и репозиториев интересны, но основной тезис главы не о бенчмарках. Если включать, то очень коротко и только как иллюстрацию того, что targeted test context может снижать регрессии лучше, чем одна процедурная инструкция. Возможно, лучше оставить числа для главы XI.

## 4. Использовать ли Cisco Foundry Security Spec?

Пока только как optional source. Это не Constitutional SDD в узком смысле, но сильный соседний пример: specification/constitution как deliverable, invariants and guardrails. Если основной CSDD-раздел будет выглядеть слишком одиноким, можно добавить одну фразу как соседнюю тенденцию. Но нельзя смешивать Foundry с CSDD и нельзя делать из него центральный подход.

## 5. Как сохранить границу с главой VI?

Kiro и Spec Kit неизбежно говорят о context rules, skills, hooks, CLI, интеграциях и agent surfaces. Нужно в V сказать только то, что это соседние слои. Глава VI должна получить право подробно разбирать project context as agent interface.

## 6. Как не потерять критику тяжёлых подходов?

Нужно оставить явный раздел о цене подхода: защищённая спецификация полезна там, где ошибка дорогая, переходов много или работа должна пережить одну сессию. Для малых обратимых изменений тяжёлый подход может быть лишним, и здесь короткий якорь Matt Pocock помогает не продавать методологию ради методологии.

# P05 update

## Закрыто: нужен ли широкий внешний обзор?

Нет. Широкий внешний обзор не нужен. Глава может опираться на первичные источники и внутренний Атлас. Вторичные сравнения не добавляют существенного различения.

## Закрыто: нужно ли искать ещё CSDD adoption examples?

Нет для текущей главы. Поиск не дал достаточного основания писать о зрелой adoption-линии. Сохраняется осторожная формулировка: CSDD — proposed methodology and worked example.

## Остаётся открытым: включать ли Foundry

Остаётся optional. Foundry хорош как соседний пример specification/constitution as deliverable, но не обязателен. Решить на этапе черновика по месту: если раздел CSDD выглядит слишком узким, добавить одну осторожную фразу; если текст и так плотный, не включать.

## P17 — закрытие вопроса о человеческом решении

Добавлен отдельный раздел о том, где в каждом подходе стоит человек. Это закрывает прежний риск: глава могла говорить о review/остановках слишком общо. Теперь различены остановка до плана, принятие состояния фичи, решение о смысле теста и ответственность за исключение из правила.

## P23 — final status of open questions

- Billing example: resolved. It is compact but still anchors all approachs.
- TDAD/CSDD order: resolved as Spec Kit → Kiro → TDAD → CSDD.
- TDAD numbers: not included; deferred to verification/evidence chapter.
- Cisco Foundry: included only as peripheral adjacent source; can be removed in global edit if it feels like a tail.
- Boundary with VI: resolved through final section on documents vs continuation state.
- Critique of heavy approachs: handled through Matt Pocock and proportionality discussion.
