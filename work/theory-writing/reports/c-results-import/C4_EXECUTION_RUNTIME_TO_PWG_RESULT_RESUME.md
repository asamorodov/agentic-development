# RESUME — C4_EXECUTION_RUNTIME_TO_PWG

Статус: completed  
Готовность: `ready_with_known_debts`

## Что собрано

- Написан и проверен основной фрагмент `C4_execution_runtime_to_pwg.md`.
- Фрагмент удерживает границу между состоянием запуска и состоянием работы: `run_id`, thread, worktree, devbox, браузер, песочница, checkpoint, лог, diff и PR не считаются достаточным рабочим состоянием без work item, владельца, gate, dependency, evidence package, handoff и cleanup.
- Durable execution отделён от durable work: восстановление процесса не равно восстановлению пригодного продолжения работы.
- Roast, Stripe Minions, Mike McQuaid / Sandvault / Homebrew, LangGraph, Temporal, DBOS, Restate, Beads и Git/worktree-механики используются как точечные якоря, а не как пересказ историй.
- В основной текст вставлены две собственные схемы `synthetic_figure`; реальные screenshots/source diagrams оставлены в реестре кандидатов и не подменены текстовыми суррогатами.
- Companion-файлы по source usage, story anchors, figures, open questions и repair audit включены в архив.

## Известные долги

- Перед публикационной сборкой нужно проверить пересечения с A6, A4, C3 и A9, чтобы C4 не стал повторной мини-главой о runtime или полным определением PWG.
- Часть плотной runtime-фактуры может быть вынесена в технический атлас, если глава окажется перегруженной.
- Реальные визуальные материалы Stripe / Shopify / Mike требуют отдельного asset-pass: локализация файлов, проверка качества, прав и точного места использования.
- Детали Claude Code / Codex worktrees не стоит расширять без отдельного source-pass.
