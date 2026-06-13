# Open questions — Spec Kit article

Статус: P26 guarded final style. Этот файл хранит только актуальные блокеры и конкретные follow-ups для текущей статьи. Общий долг C5/A10 sync debt закрыт: C5 и A10 остаются read-only context, а статья уже отражает их через standalone contract и границу mode-selection.

## Publication / asset-pass blockers

1. Четыре external-real кандидата ещё требуют asset-pass: локализации, проверки прав, проверки качества и атрибуции до превращения в финальные локальные ассеты:
   - `fig-spec-kit-home-positioning` из главной страницы документации Spec Kit;
   - `fig-full-sdd-cycle` из справочника Workflows;
   - `fig-workflow-json-status` из справочника Workflows;
   - `fig-spec-kit-agents-context-hooks` из arXiv-статьи Spec Kit Agents, с требованиями атрибуции CC BY 4.0.
2. После локализации ассетов решить, должен ли нижний раздел `Внешние изображения для asset-pass` превратиться в production metadata или исчезнуть из публикуемой версии статьи.
3. Финальный layout должен проверить визуальную плотность: две synthetic figures, четыре external-real placeholders и один local contextual image могут быть уместны для большой concept-atlas статьи, но это нужно проверить в целевом рендере.
4. Таблица переходов состояния может потребовать layout-обработки на узких экранах; не превращать её в synthetic figure, если таблица не ломается в целевом рендере.

## Source / freshness follow-ups

1. Spec Kit чувствителен к версии. Если статья публикуется с утверждением “current as of”, нужен финальный freshness-pass по первичным docs/templates из `source_usage`.
2. Issue/PR-примеры (#975, PR #986, #1926, #1063) остаются только issue-level evidence. Их нельзя превращать в official roadmap или current-bug claims без свежей проверки источников.
3. Отложенные operational details — PowerShell variants, dry-run upgrade procedure, timeout environment variables, symlink handling, full integration registry — принадлежат source note или handbook, а не текущей concept article, если будущий pass явно не изменит scope.

## Editorial guardrails for package time

1. Сохранять problem-first вход: не возвращать contract/taxonomy блок выше раздела 1.
2. Держать `Как читать одну фичу Spec Kit` как маршрут ревью, а не полный tutorial walkthrough.
3. Держать раздел 17 как boundary prose, а не comparison table, если целевая публикация специально не попросит таблицу.
4. Держать раздел 18 как компактный return-to-theory bridge; не расширять его в параллельную теоретическую главу.
5. Сохранять точные имена файлов, команд, путей, source titles и integration terms; русские пояснения использовать только для обычной объяснительной прозы.

## P24 style-pass follow-up

No new factual, source, theory or visual blockers were opened by the style pass. Remaining blockers are still the asset-pass localization/rights/quality checks, the decision about the bottom asset-pass metadata section in the publishable version, final layout density, narrow-screen treatment for the state-transition table, and optional freshness check if the article is published with a “current as of” claim.

## P25 selective-rewrite follow-up

No new open questions were created. P25 did not change article scope, source set, image set or theory boundary; the same publication blockers from P23/P24 remain.

## P26 final-style follow-up

No new blocker opened. P26 was a guarded style pass; current open questions remain asset-pass localization/rights/quality, publishable handling of the bottom asset-pass metadata section, layout density, state-transition table rendering, and optional final source freshness if publishing with a date claim.
