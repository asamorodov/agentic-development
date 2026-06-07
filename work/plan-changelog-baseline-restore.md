# Changelog: baseline restore rule for SPDD and Gas Town

Дата: 2026-06-05

## Что зафиксировано

Добавлено жёсткое правило: при работе с SPDD и Gas Town нужно сначала брать соответствующие разделы **целиком из старого сайта / документа baseline**, а не из последнего синтеза.

## Почему

Последний expanded/synthesis-документ используется как quarry, но не как форма. В нём Gas Town уже был сжат, а SPDD находится под риском такого же ужима. Старый сайт сохраняет лучшие вычитанные версии этих deep anchor cases.

## Что меняется в процессе

Перед написанием SPDD и Gas Town частей добавляется baseline restoration stage:

1. extract from old site baseline;
2. unchanged seed;
3. structure/detail inventory;
4. adaptation plan;
5. additive rewrite;
6. anti-degradation check;
7. human gate.

## Что не меняется

- AI-driven SDLC остаётся master architecture.
- SPDD остаётся отдельной Part IV.
- Spec Kit/Kiro/TDAD/Constitutional SDD остаются глубокой Part V.
- Gas Town остаётся отдельной deep part.
- Expanded theory остаётся source quarry.
