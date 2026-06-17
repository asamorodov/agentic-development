# ADR-0017 — Многоязычная архитектура корпуса и будущий английский перевод

Дата: 2026-06-17.

## Статус

Принято как рабочее архитектурное решение для корпуса.

## Контекст

Корпус сейчас пишется и редактируется по-русски, потому что это быстрее и точнее для текущей разработки понятий, разрезов и структуры. При этом в будущем ожидается большая работа по английской версии: не машинный обратный перевод одной статьи, а перенос всего корпуса в английский язык.

Если не подготовиться заранее, английская версия начнёт жить как отдельное неконтролируемое переписывание: термины поплывут, названия частей будут переводиться случайно, якоря и ссылки разойдутся, а фактические материалы начнут переводиться с русского пересказа вместо возвращения к источникам.

## Решение

Вводится многоязычная архитектура корпуса.

Русский текст остаётся текущей рабочей и редакционной базой. Его не нужно делать искусственным ради будущего английского перевода. Но каждый крупный публичный материал должен постепенно становиться `translation-ready`: иметь стабильные идентификаторы, сохранённые источники, явные терминологические решения и переводческие заметки для мест, где русский текст использует локальную формулировку, культурный оттенок или неочевидный термин.

Главный принцип: английская версия должна переводить смысл, структуру и источниковую фактуру, а не механически калькировать русский текст. При переводе технических и источниковых мест нужно возвращаться к оригинальным английским терминам, названиям инструментов, документации и цитируемым источникам, а не переводить обратно русский пересказ.

## Практические правила

1. У каждой крупной части и статьи должен быть стабильный ID, не зависящий от языка публичного заголовка: например `atlas-a06-git-change-substrate`, `theory-xii-pr-acceptance`, `stories-humanlayer`.
2. Внутренние ссылки и карты должны по возможности опираться на ID/slug, а не только на локализованное название.
3. Для терминов уровня корпуса ведётся двуязычный реестр: русский публичный вариант, английский рабочий/публичный вариант, запретные кальки, область применения и примеры.
4. Технические собственные имена, названия продуктов, файлов, команд, API, протоколов и форматов не переводятся, если это не общепринято.
5. Английские источники не должны цитироваться через русский перевод. При подготовке английской версии нужно брать исходный английский source text / documentation wording и заново встраивать его в английский текст.
6. Русский текст не нужно заранее “англизировать”. Лучше сохранить естественный русский, но добавлять translation notes там, где будущий перевод может ошибиться.
7. Каждая статья, которая идёт к публичной стабилизации, должна проходить `translation-readiness check`.

## Названия частей корпуса

Рабочие пары названий фиксируются не как окончательный брендинг, а как текущие соответствия:

- `Теория` / возможное будущее публичное `Жизненный цикл программного изменения` → `Theory` / possible `Lifecycle of Software Change`.
- `Атлас` → `Atlas`.
- `Рабочие сценарии` → `Working Scenarios` or `Practical Scenarios`.
- `Практикум` → `Practicum`, only if the section becomes exercise-like or training-like.
- `Каталог проблем и решений` → `Problem and Solution Catalog`; if the diagnostic/failure framing is foregrounded, possible `Failure and Recovery Catalog`.
- `Истории` → `Stories` or `Developer Workflow Stories`.

These are working translation pairs, not final marketing names.

## Translation-readiness check

Before a major article/chapter is considered stable enough for later English transfer, check:

- Stable ID exists.
- Title has a working English equivalent.
- Key terms used in the article are listed in the bilingual term registry or local translation notes.
- Source links are present where source-derived claims are introduced.
- English-source claims preserve enough provenance to return to the original source during translation.
- Russian idioms, locally coined phrases and ambiguous terms have notes if literal translation would mislead.
- Figures, captions, tables and code blocks have language handling noted.
- Cross-links target stable IDs/slugs rather than fragile localized text.
- Any intentionally Russian-only wording is marked as such.

## Consequences

This prevents future English translation from becoming a second uncontrolled writing project. It also reduces the pressure to overload current Russian chapters with English terms. The Russian corpus can remain readable and natural, while the translation layer preserves the information needed to build a strong English version later.

This decision also affects future package design: theory, Atlas, Working Scenarios and Problem/Solution Catalog packages should include a small translation-readiness step when they stabilize public-facing material, without turning every draft pass into a full translation task.
