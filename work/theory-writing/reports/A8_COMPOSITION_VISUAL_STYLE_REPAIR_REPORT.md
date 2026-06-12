# A8 composition / visual / style repair report

Дата: 2026-06-11.

## Диагностика до ремонта

`A8_authority_to_act_vs_complete.md` хорошо выполнял базовую смысловую функцию: разводил право агента действовать и право признать изменение принятым. Фактура была сильной: CODEOWNERS, ADR status/process, CI/PR, Stripe Minions, `/babysit-pr`, Sandvault/worktrees, Homebrew/Zig/Linux/LLVM/FastAPI/QEMU policies и Beads `bd gate` работали на один общий тезис.

Проблемы были не в источниковой базе, а в старом композиционно-визуальном слое:

1. **Визуальный перегруз.** В основном A8 было 11 inline-фигур. Многие схемы были полезными рабочими заметками, но не обязательными для несущего теоретического фрагмента.
2. **Чрезмерная детализация governance-механизмов.** CODEOWNERS, ADR adoption, `/babysit-pr`, Homebrew и Zig получали отдельные фигуры, хотя в A8 они должны работать как factual anchors, а не превращать фрагмент в технический атлас.
3. **Служебная подпись к настоящему asset.** Подпись к `mike-superset-worktrees.png` рассказывала о recovery/local-file status вместо объяснения иллюстрации читателю.
4. **Английский и псевдотехнический слой.** В figure captions/labels оставались `authority laundering`, `right to act`, `human gate`, `evidence package`, `review-cost boundary` как обычный связующий язык.
5. **Риск дублирования A7/B2.** A8 начинал подробно разворачивать пакеты свидетельств и PWG-state machine вместо удержания собственной governance-функции.

## Принятое решение

Ремонт сделан как minimal sufficient repair, не как новая source-expansion. Новые внешние источники не добавлялись.

Inline-фигуры сокращены с 11 до 5:

| Figure id | Тип | Решение |
|---|---|---|
| `fig-a8-action-vs-acceptance-boundary` | synthetic | оставлена как центральная граница действия/принятия |
| `fig-a8-pr-as-candidate` | synthetic | оставлена как короткая схема PR-кандидата |
| `fig-a8-local-sandbox-action-boundary` | local image asset | оставлена как настоящий `<img>` с публичной подписью |
| `fig-a8-contribution-policy-boundaries` | synthetic | заменила прежние отдельные Homebrew/Zig/policy-схемы |
| `fig-a8-pwg-acceptance-state-machine` | synthetic | оставлена для финального перехода к PWG |

Сняты с inline и сохранены в `A8_figure_candidates.md`:

- `fig-a8-codeowners-gate`;
- `fig-a8-adr-adoption-vs-agent-draft`;
- `fig-a8-authority-laundering-antipatterns`;
- `fig-a8-babysit-pr-escalate-boundary`;
- `fig-a8-homebrew-maintainer-load-policy`;
- `fig-a8-contribution-boundary-spectrum`;
- `fig-a8-zig-participation-boundary`.

## Что изменилось в основном тексте

- Заголовок уточнён: «право признать изменение принятым» вместо более тяжёлой формулы «право считать изменение принятым».
- Центральный дефект описан человеческой формулировкой: технический сигнал начинает выглядеть как решение о принятии. Термин `authority laundering` убран из основного текста.
- Stripe и `/babysit-pr` объединены в одну композиционную линию: платформы и PR-автоматизация доводят работу до кандидата, а не принимают результат.
- Sandvault/worktrees блок сохранён, но локальная изоляция теперь прямо связана с ответственностью автора и Homebrew policy.
- Policy cluster сжат: разные политики показывают разные mechanisms — ответственность отправителя, раскрытие AI-использования, provenance, review load and participation boundary — но не превращаются в отдельную сравнительную taxonomy.
- PWG-блок оставлен как итог: `done` недостаточно; acceptance должен быть отдельным состоянием с владельцем и источником делегирования.

## Статус после ремонта

- Рабочая ценность: около 8.4/10.
- Публикационная готовность: около 7.5/10.
- Статус: `ready_with_known_debts`.

Оставшиеся долги:

1. Финально решить, какие model states остаются английскими (`ready_for_review`, `accepted`, `blocked_by_policy`) и где нужен русский читательский перевод.
2. При сборке technical atlas вернуть туда подробные схемы CODEOWNERS, ADR adoption, Homebrew checklist, Zig participation boundary и `/babysit-pr` loop, если они понадобятся.
3. Состыковать A8 с A7 и B2: A8 не должен снова объяснять все evidence mechanics; A7 отвечает за свидетельства, B2 — за PWG как долговечный рабочий субстрат.
