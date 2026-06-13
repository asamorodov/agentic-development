# SPDD target-plan second repair report

Дата: 2026-06-12.

Пользователь попросил сделать `spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` менее шаблонным, но пока не собирать article-writing package. Выполнен точечный repair только target-group plan и связанных служебных документов.

## Что было проблемой

- В начале плана оставалась история manufactury-run (`S01 создал...`, `S02/S03 работают...`), которая нужна отчётам, но не будущему исполнителю article-writing package.
- Центральная ось SPDD была верной, но ещё слишком похожей на общий blueprint: `structured prompt`, Canvas, OpenSPDD commands, визуальные проходы.
- Fowler SPDD и OpenSPDD были разведены недостаточно резко: OpenSPDD мог читаться как список команд, а не как операционализация поддержания Canvas.
- Failure modes были перечислены, но не поставлены как несущая ось статьи.
- P11–P13 дублировали общее правило про visual candidates; это делало план шумным.
- В конце оставались устаревшие sync/provenance notes.

## Что изменено

- Удалена секция истории правки плана из основного target-plan.
- Усилен article contract: SPDD представлен как способ превратить намерение изменения в сопровождаемый артефакт, а центральный риск — убедительный, но неверный или устаревший Canvas.
- Fowler SPDD и OpenSPDD разведены как концептуальная рамка и операционализация через команды, шаблоны, адаптерный слой, `prompt-update`, `sync` и optional checks.
- Failure modes стали article-critical: неверный Canvas, устаревший Canvas, локальный патч вместо обновления намерения, церемония дороже изменения, тесты подтверждают поведение, но не доказывают правильность исходного намерения.
- Source-depth P04–P08 переписаны SPDD-specific: анатомия REASONS Canvas, OpenSPDD как машина поддержания Canvas, API/code-review/prompt-update как разделение поведения, ревью и исправления намерения.
- Visual P11–P13 очищены от дублирующего boilerplate: P11 — local assets, P12 — external real candidates from dossier/source, P13 — rare synthetic figures. Общее правило disposition оставлено один раз в отдельной секции.
- C5/A10 теперь описаны как доступный read-only context; стандартный `sync pending` удалён из SPDD-плана.
- F01/Post-import notes удалены из target-plan как manufactury history.

## Что не сделано

- Article-writing package для SPDD не собирался.
- Текст статьи `work/atlas/articles/spdd_method.md` не создавался.
- Соседние target plans не переписывались содержательно.

## Статус

`spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` остаётся в статусе `ready_for_package_manufacture_after_manual_review`, но теперь меньше похож на общий blueprint и сильнее задаёт именно SPDD/OpenSPDD-статью.
