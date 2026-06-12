# A3 visual/style repair report

Дата: 2026-06-11.

## Повод

После обсуждения A3 пользователь принял основные долги фрагмента и отдельно указал на языковую проблему: выражения “хвост сопровождения” и “ложный авторитет” читаются как нечеловеческие псевдотехнические формулы. Их нужно было не только заменить в A3, но и добавить в стилевые правила как антипримеры.

## Изменения в стилевых правилах

Обновлены:

- `protocols/rules/human-technical-style.md`;
- `protocols/rules/fragment-defect-analysis-and-repair.md`.

Добавлены антипримеры:

- “хвост сопровождения”;
- “ложный авторитет”.

Предпочтительные формулировки:

- “последующая поддержка артефакта”;
- “порядок обновления артефакта”;
- “границы доверия к артефакту”;
- “артефакт выглядит убедительнее, чем заслуживает”;
- “пределы доказательной силы”.

## Изменения в A3

Обновлены:

- `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md`;
- `work/theory-writing/fragments/A3_figure_candidates.md`;
- `work/theory-writing/fragments/A3_open_questions.md`;
- `work/theory-writing/fragments/A3_degradation_and_duplication_audit.md`;
- `work/theory-writing/fragments/A3_source_usage.md`;
- `work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md`.

Основной A3 теперь содержит 5 inline-фигур вместо 15:

1. `fig-a3-specification-functions`;
2. `fig-a3-spdd-closed-loop`;
3. `fig-a3-spec-kit-plan-gate`;
4. `fig-a3-tdad-two-meanings`;
5. `fig-a3-artifact-trust-boundaries`.

Удалены из основного A3 или перенесены в candidate/status layer:

- `fig-a3-five-control-objects`;
- `fig-a3-five-axes-specification-layer`;
- `fig-a3-capability-vs-control`;
- `fig-a3-drift-taxonomy`;
- `fig-a3-spec-kit-toolkit-pipeline`;
- `fig-a3-kiro-ide-surface`;
- `fig-a3-context-routing`;
- `fig-a3-tests-two-jobs`;
- `fig-a3-csdd-hierarchy`;
- `fig-a3-specification-layer-staleness`;
- `fig-a3-false-artifact-authority`.

`fig-a3-false-artifact-authority` не просто удалён: его содержательная функция перенесена в новую фигуру `fig-a3-artifact-trust-boundaries`, где нет неудачной формулы “ложный авторитет”.

## B package consistency

Поскольку `B1_SPDD_CONTRIBUTION_AND_LIMITS.zip` содержит A3 как read-only input, после A3 repair был пересобран B1 package payload. B2 и B3 не содержат A3 как прямой read-only input, но их payload также обновлён в части общих read-only файлов: skeleton, style rule, fragment defect protocol и documents map.

Smoke-test после пересборки:

- `B1_SPDD_CONTRIBUTION_AND_LIMITS.zip`: `unzip -t`, first runner transition, second runner transition — OK.
- `B2_PWG_CONTRIBUTION.zip`: `unzip -t`, first runner transition, second runner transition — OK.
- `B3_GAS_TOWN_BEYOND_PWG.zip`: `unzip -t`, first runner transition, second runner transition — OK.

## Regression audit

- В основном A3 нет выражений “хвост сопровождения” и “ложный авторитет”.
- В основном A3 нет служебных подписей “Восстановленная source-иллюстрация” и “Локальный файл”.
- В основном A3 нет numbering вида `A3-10` в figcaption.
- Баланс `<figure>` / `</figure>`: 5 / 5.
- Количество `<img>`: 1.
- Единственный локальный image asset в A3 существует: `content/assets/theory-images/fowler-spdd-workflow.svg`.
- Готовые изображения не превращались в текстовые схемы.
- `fig-a3-drift-taxonomy` сохранён как local source asset candidate для B1, а не потерян.

## Readiness

Статус A3: `ready_with_known_debts`.

Фрагмент можно использовать как вход для следующих B/C-работ. Оставшиеся долги: link/freshness check перед публикацией, возможное сжатие процедурных деталей в technical atlas, отдельный asset-pass для внешних реальных image candidates, если они понадобятся в сайте.
