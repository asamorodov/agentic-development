# Chapter V — cleanup of self-commenting prose

## Scope

Edited `work/theory-writing/chapters/V_protected_specification_profiles.md` to remove places where the article commented on its own construction instead of continuing the argument.

The change did not alter the chapter's structure, sources, comparison object, or profile logic. It only rewrote self-referential and editorial-sounding phrases in the main text.

## Main removed pattern

The problematic pattern was not factual inaccuracy, but article-level self-commentary: phrases such as “for this chapter”, “so that the chapter does not become a catalog”, “the example is useful as a demonstration”, and “for the chapter this is not a function overview”.

These phrases make sense in a plan or editor note, but should not remain in the chapter itself.

## Representative changes

### Comparison setup

Before:

> Чтобы глава не распалась на каталог, дальше её держат три сквозные опоры: один и тот же годовой тариф, разные места человеческой остановки и одна граница на выходе — документы могут быть готовы, но продолжение работы ещё не восстановлено.

After:

> Дальше эти профили сравниваются на трёх общих опорах: один и тот же годовой тариф, разные места человеческой остановки и одна граница на выходе — документы могут быть готовы, но продолжение работы ещё не восстановлено.

### Spec Kit framing

Before:

> Для этой главы важно не количество команд и не интерфейс.

After:

> В этом профиле существенны не количество команд и не интерфейс.

### Spec Kit workflows

Before:

> Для главы это не обзор функции, а продолжение той же мысли: спецификация должна переживать не только один ответ агента, но и переход между шагами.

After:

> Рабочие цепочки важны по той же причине: документация описывает процесс, где команды, подсказки, скрипты и ручные остановки связываются в последовательность со статусом и возможностью продолжения. Спецификация должна переживать не только один ответ агента, но и переход между шагами.

### Kiro boundary

Before:

> В этой главе Kiro нужен только как пример того, как спецификация удерживает состояние задачи.

After:

> Здесь Kiro нужен как пример того, как спецификация удерживает состояние задачи; вопрос о том, как весь проектный контекст становится интерфейсом агента, относится к следующей главе.

### TDAD maturity caveat

Before:

> Для этой главы не нужно доказывать, что TDAD — единый зрелый метод.

After:

> Вопрос не в том, является ли TDAD единым зрелым методом. Для сравнения профилей важнее другое: тест может быть не только проверкой после реализации, но и носителем части спецификации.

### Constitutional SDD example

Before:

> Пример `banking-ms-by-constitution` полезен именно как демонстрация формы...

After:

> `banking-ms-by-constitution` хорошо показывает форму...

## Checks

Searched the main chapter for the following obvious self-commenting markers after the edit:

- `для этой главы`
- `в этой главе`
- `для главы`
- `чтобы глава`
- `глава не распалась`
- `пример полезен`
- `полезен именно`
- `обзор функций`
- `для основной линии`
- `именно здесь видно`
- `помогает увидеть`

None remained in the main text after the cleanup.
