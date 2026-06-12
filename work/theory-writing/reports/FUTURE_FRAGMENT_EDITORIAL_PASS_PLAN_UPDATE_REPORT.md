# Future fragment editorial pass plan update report

Дата: 2026-06-11.

## Причина

После серии ручных оценок и repair-проходов по A2, A4, A6, A7, A8, A9, B1, B2 и B3 стало видно, что многие дефекты должны ловиться не отдельными поздними правками, а внутри самих writing-пакетов. Пользовательская формула оказалась эффективнее старой очереди: «оцени текст, насколько он хорошо выполняет поставленную задачу; после формулирования проблем исправь их».

Главный вывод: проблема была не только в конкретных визуальных или языковых правилах, а в порядке проходов. Языковые и стилевые проходы приходили слишком рано или repair-проходы стояли слишком поздно, когда композиционные, визуальные, источниковые и companion-дефекты уже закреплялись.

## Что изменено

Обновлены общие правила:

```text
protocols/rules/fragment-defect-analysis-and-repair.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
START.md
```

В правилах теперь зафиксировано:

- для ещё не построенных writing-фрагментов после системного выравнивания и до языковых/стилевых проходов должны идти 2–3 общих редакторских прохода;
- эти проходы должны сохранять общность и не получать заранее специальную повестку вроде visual/source/style;
- каждый проход повторяет базовую формулу: оценить, насколько фрагмент выполняет поставленную задачу, сначала сформулировать проблемы, затем исправить их;
- первый проход обычно ловит крупные нарушения функции и композиции, второй перечитывает уже изменённый текст, третий нужен для сложных/несущих фрагментов и не должен переписывать текст ради активности;
- anti-meta, asset-classification, regression audit и readiness status остаются внутри этих общих проходов.

## Какие target-group plans обновлены

Обновлены только планы фрагментов, которые ещё не построены:

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
```

В каждом из этих планов старые поздние `repair-pass` sections после языковых/стилевых проходов заменены на три общих редакторских прохода сразу после системного выравнивания. После них идут два языковых и два стилевых прохода.

## Что сознательно не изменено

Планы уже построенных фрагментов A1–A9 и B1–B3 не переписывались под новую очередь. Их результаты уже существуют и ремонтировались отдельными cumulative repair overlays.

Executor-пакеты B1/B2/B3 не пересобирались: текущая операция меняет правила и будущие target-group plans, а не уже выполненные writing-пакеты.

## Проверка

- 7/7 ещё не построенных fragment target plans содержат три общих редакторских прохода.
- В этих планах общие редакторские проходы стоят после системного выравнивания и до языковых/стилевых проходов.
- В этих планах больше нет prompt-заголовков вида `repair-pass: ...` в конце очереди.
- Общие правила и template обновлены, чтобы будущие target-group plans не вернулись к старой форме «два repair-pass после стиля».
