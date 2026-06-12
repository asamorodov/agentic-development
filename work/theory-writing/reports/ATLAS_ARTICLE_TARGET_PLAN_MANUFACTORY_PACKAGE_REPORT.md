# Atlas article target-plan manufactury package report

Дата: 2026-06-12

Уточнён `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` и пересобран executor-пакет:

```text
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
```

Изменения:

- Создаваемые target-group plans должны быть пригодны для независимых self-contained article-writing packages: все read-only inputs будущего пакета перечисляются конкретными путями и должны быть упакованы с package при сборке.
- S01 стал idempotent/rerun-safe: existing plan is read before create/repair/replace; manual edits should not be blindly overwritten.
- S01 requires mini dossier-orientation but explicitly forbids article-writing leakage.
- S02 keeps targeted strengthening and includes only the high-level direction: “Подходит ли выбранная очередь проходов именно этой статье?” without turning it into a long checklist.
- S04 now checks exact path grounding and package-buildability and must repair found defects.
- S05 includes `ready_for_package_manufacture_after_manual_review`.
- Boundary uncertainty does not block a plan when article goal and dossier-backed basis are clear.
- No new role-distribution F01 audit was added.

Пакет пересобран после этих изменений. Records: 56.

Проверки:

- package zip contains only `START.md`, `q8v4m.py`, `z3k9p.dat`;
- runner generic/opaque;
- smoke-test first transition passed;
- smoke-test second transition passed after required fake output;
- package expects execution in deployed repository root;
- package does not bundle dossiers/assets/source files because it is itself the manufactury package; generated article plans will require future article packages to bundle their inputs.
