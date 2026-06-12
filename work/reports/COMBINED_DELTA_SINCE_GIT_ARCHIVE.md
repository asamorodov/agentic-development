# Общая дельта с момента последнего базового архива

База сравнения: `git.zip` из `/mnt/data/git.zip`.

Этот пакет собирает в одну дельту все актуальные изменения, подготовленные после загрузки базового архива: обновлённые методологические досье, новые anchor-досье SPDD/Gas Town, mechanism dossier Persistent Work Graph, prompt-only режим языко-стилевого прохода и prompt-only режим сбора досье для 6 новых историй.

## Проверка

- Modified count: 7
- Added count: 15
- Removed count: 0

## Изменённые файлы

- `work/automation/README.md`
- `work/dossiers/BMAD_METHOD_DOSSIER.md`
- `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md`
- `work/dossiers/GSD_METHOD_DOSSIER.md`
- `work/dossiers/KIRO_SPECS_DOSSIER.md`
- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`
- `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`

## Новые файлы

- `DELETE_PATHS_COMBINED_DELTA.txt`
- `work/automation/run-language-style-loop.cmd`
- `work/automation/run-story-dossier-loop.cmd`
- `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md`
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`
- `work/dossiers/SPDD_METHOD_DOSSIER.md`
- `work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md`
- `work/prompts/RUN_DOSSIERS_LANGUAGE_STYLE_NORMALIZATION.md`
- `work/prompts/RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION.md`
- `work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md`
- `work/reports/COMBINED_DELTA_SINCE_GIT_ARCHIVE.md`
- `work/reports/LANGUAGE_STYLE_PROMPT_ONLY_PATCH_REPORT.md`
- `work/reports/LANGUAGE_STYLE_PROMPT_ONLY_PATCH_VALIDATION.md`
- `work/reports/STORY_DOSSIER_LOOP_PATCH_REPORT.md`
- `work/reports/STORY_DOSSIER_LOOP_PATCH_VALIDATION.md`

## Удаления

Прямых удалений относительно `git.zip` в архиве нет. Если ранее применялись промежуточные экспериментальные дельты, см. `DELETE_PATHS_COMBINED_DELTA.txt`.

## Состав по смыслу

- `work/dossiers/*` — 6 обновлённых методологических досье плюс финальные SPDD/Gas Town и Persistent Work Graph.
- `work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md` и `RUN_DOSSIERS_LANGUAGE_STYLE_NORMALIZATION.md` — режим языко-стилевой нормализации 10–20 проходов.
- `work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md` и `RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION.md` — режим сбора досье для 6 новых историй 10–20 проходов.
- `work/automation/run-language-style-loop.cmd` и `run-story-dossier-loop.cmd` — простые wrappers поверх обычной `run-source-loop.cmd`, без изменения TS-ядра.
- `work/automation/README.md` — объединённое описание обоих новых prompt-only режимов.

## Cleanup для промежуточных ошибочных дельт

Если в рабочее дерево уже применялись промежуточные экспериментальные дельты, вручную удалить пути из `DELETE_PATHS_COMBINED_DELTA.txt`. При применении этой общей дельты напрямую к `git.zip` удалять нечего.
