# TDAD Comparative — open questions

Статус: P26 active open questions. Старые pass-specific долги очищены или свернуты; ниже оставлены только реальные blockers и watchpoints для текущей версии статьи.

## Source and provenance blockers

1. Проверить commit-level provenance для спорного mutation-result эпизода `ALWAYS_CREATE_TICKET` / `M_ALWAYS_TICKET` перед любым усилением числового вывода. Текущая статья уже использует его осторожно как source-conflict warning; без hash/JSON не превращать эпизод в стабильный результат.
2. Проверить raw artifacts для первой линии, если будущий проход захочет цитировать конкретные `spec_yaml`, generated tests, mutation intents, `total_cost_usd` или отдельные result JSON beyond current compact summary.
3. Проверить точное соответствие между runtime artifact, описанным во второй TDAD-статье, и опубликованным `tdad-skill`. Текущая статья различает paper-minimal skill и later practical packaging; это различие не ослаблять без проверки.
4. Если telemetry fields из `run_benchmark.py` станут центральным доказательством, открыть raw runner/eval artifacts and confirm field names, `EVAL_JSON_PATH` behavior and exact result provenance.

## Visual and asset-pass blockers

1. Локализовать inline external candidates before publication: `fig-tdad-definition-overview`, `fig-tdad-definition-mutation`, `fig-tdad-development-pipeline`, `fig-tdad-development-test-map`.
2. Проверить права, качество, crop and caption fidelity for each localized external figure. Inline placeholders must not remain as final publication assets.
3. Для `fig-tdad-development-test-map` найти действительно читаемый source screenshot / CLI trace. Если его нет, удалить inline slot and keep the code block.
4. Проверить права/licensing for local `fig-harness-types-verification-boundary`; local availability does not equal publication clearance.
5. Queue-only candidates (`fig-tdad-definition-repo-tree`, `fig-tdad-development-p2p-failures`, `fig-tdflow-reproduction-tests`) should become inline only if they materially improve reading after asset localization; avoid visual overload and leaderboard drift.

## Article structure watchpoints

1. Keep the opening problem-first. Future boundary or taxonomy edits must not move atlas-boundary material ahead of the reader question.
2. Keep TDFlow as contrast only, not a third TDAD line.
3. Check after final asset localization whether five inline figures are too many. If pruning is needed, demote the cross-source harness boundary visual before demoting TDAD-native source figures.
4. Later style pass may compress repetition across `Как читать показатели`, `Что считать свидетельством` and `Где человек решает`, but only if it preserves the distinction between metric, evidence and acceptance.
5. Keep the final article as concept-first comparison, not handbook/tutorial: commands and file paths are source-bound artifacts, not implementation instructions.

## Theory-link watchpoints

1. No generic theory-sync debt remains. C5/A10 back-links are already represented by concrete questions: carrier of intent, mode selection, evidence boundary and repair target.
2. If future theory references are added to the main body, they must explain what TDAD clarifies rather than becoming a neighboring-theory catalogue.

## P24 style watchpoint

P24 removed the active style defects found in the main text and visual notes. Future style passes should not flatten useful source-specific terms, but should keep watching for pseudo-terms if new material is added. No new open blocker was created by P24.

## P25 style watchpoint

Selective natural rewrite completed. No new open blocker. Future edits should preserve the more direct headings and avoid reintroducing model-like labels for section purposes.

## P26 style watchpoint

Guarded final style pass completed. No new open blocker. Remaining work is source/provenance and asset publication work, not article-style repair.
