# Persistent Work Graph plan repair and package report

## Изменения плана

План `persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` переписан из generic atlas-plan в более сильный PWG-specific target plan.

Сделано:

- убраны следы manufactury-history как самостоятельные секции (`S02/S03/S04`, stale sync debt);
- центральная ось переписана вокруг устойчивого состояния работы, а не `durable substrate` / `external work truth`;
- Beads задан как anchor и проверка механизма, а не product overview;
- явно разведены PWG, issue tracker, durable execution, Gas Town, CRDT/STORM/MAST;
- перенос на многопроходный document-process workflow сделан вторым доказательством понятия;
- P04–P08 переписаны как PWG-specific source-depth цепочка;
- visual-pass приоритизирует real assets и external candidates, synthetic figures ограничены нетривиальными механизмами/границами;
- C5/A10 sync-debt блок заменён на актуальный read-only context;
- добавлены PWG-specific failure modes и final blockers.

## Package

Собран self-contained article-writing package `persistent_work_graph_ATLAS_ARTICLE.zip`.

Проверки:

- `unzip -t` package: passed;
- smoke-test first runner transition: passed;
- smoke-test second runner transition after required-output stubs: passed.
