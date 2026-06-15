
# Post-Atlas fragment-to-chapter routing map

Статус: классификация A/B/C-фрагментов для будущих chapter packages.  
Правило: фрагменты не переписывались. Они читаются как уже сделанный синтез, а не как автоматически устаревший слой.

| Фрагмент | Главы | Статус | Нельзя потерять | Style debt | Конфликт/граница с V5 |
| --- | --- | --- | --- | --- | --- |
| 00_spine_map.md | все главы | base/control text | lifecycle axis, source hierarchy, carrier table, boundaries theory/Atlas/Handbook/Fieldbook | Проверить термин `хвост сопровождения`: допустим как рабочее название, но в финальном тексте лучше заменить на `последующее сопровождение` или `repair/update layer` по-русски. | нет |
| A1_change_not_prompt.md | INTRO, I, II, CONCLUSION | base text | prompt/task/diff/change distinction; малый радиус; внешний носитель | Нужен языковой проход против английского клея вокруг prompt/change/mode. | Может спорить с V5, если строит главу вокруг prompt, а не lifecycle. |
| A2_specification_adr_contract.md | III, XI, XII | base text | specification vs contract vs ADR; Confirmation; decision authority | Проверить кальки вокруг contract/evidence/confirmation. | Нужно синхронизировать с ADR article and CSDD. |
| A3_specification_methodologies_synthesis.md | III, V | base text / partial salvage | protected spec profiles; comparison without catalog | Высокий риск таблицы методик; требуется anti-catalog pass. | V5 требует lifecycle question, а не comparison catalogue. |
| A4_persistent_work_graph_boundary.md | VI, VII, IX | distinction source | PWG boundary against transcript, issue tracker, runtime; gates and source-state line | Проверить термины graph/state/prime; оставить source-state line. | Может быть частично superseded by PWG Atlas, но distinctions сохранить. |
| A5_process_methodologies_synthesis.md | VIII, X, CONCLUSION | base text | process profile; GSD/BMAD/Gas Town boundaries; process overhead | Риск английского process-framework словаря. | V5 отделяет process profiles от Gas Town deep node; это нужно удержать. |
| A6_execution_environment_distinctions.md | VI, IX | distinction source | environment, tools, permissions, harness, project context as interface | Убрать английский клей around tools/runtime/context. | Может перетянуть VI into IX; разделить context interface and execution environment. |
| A7_observation_vs_evidence.md | II, XI | base text | observation vs evidence; browser/log/traces; evidence threshold | Проверить `trace`, `evidence`, `signal` translations locally. | XI needs stronger external sources; A7 alone insufficient. |
| A8_authority_to_act_vs_complete.md | XII, III, XI | base text | right to act vs right to complete; human gates; false completion | Снизить абстрактность вокруг authority/governance. | Связать с ADR/CODEOWNERS without making legal overview. |
| A9_lifecycle_repair.md | XIII, XI, CONCLUSION | base text | post-merge repair; stale specs/ADR/rules/skills/task graphs/source registers | Проверить `repair`, `tail`, `maintenance` как русские формулировки. | V5 делает XIII отдельной главой, не appendix. |
| A10_mode_selection_map.md | CONCLUSION, INTRO, I | base text | mode selection; minimal sufficient structure; over/under-structuring signals | Не превращать conclusion into decision matrix only. | A10 should summarize after chapters, not dictate structure too early. |
| B1_spdd_contribution_and_limits.md | IV, III, XI, XIII | base text | SPDD deep node; intent carrier, review/sync, limits | Проверить, что SPDD не описан как prompt craft. | Use Atlas baseline first, B1 as synthesis. |
| B2_pwg_contribution.md | VII, VI, IX, XIII | base text | PWG deep mechanism; durable work state and recovery | Нужен стиль проход, чтобы не перегрузить graph vocabulary. | Atlas уточняет Beads/PWG boundaries. |
| B3_gas_town_beyond_pwg.md | X, VIII, IX | base text | Gas Town as organization beyond PWG; roles/backpressure/recovery | Снизить словарный шум Gas Town. | V5 keeps Gas Town as deep node; avoid UI tour. |
| C1_specification_to_pwg.md | III, IV, V, VII, XIII | distinction source | how specification becomes work state; when specs need continuation state | Проверить переходы between spec/PWG. | Could duplicate III/VII boundary; use as bridge only. |
| C2_pwg_to_process_profiles.md | VII, VIII, X | distinction source | PWG vs process profiles vs Gas Town | Сохранить границы, убрать repetition. | Important to avoid BMAD/GSD/Gas Town merge. |
| C3_pwg_to_evidence.md | VII, XI, XII | distinction source | evidence as gate, source-state and acceptance boundary | Проверить evidence terms. | XI needs external evidence sources beyond C3. |
| C4_execution_runtime_to_pwg.md | VI, VII, IX, X | distinction source | runtime vs PWG; durable execution vs durable work state | Нужно особенно аккуратно с runtime/orchestration. | IX is discovery-heavy; C4 is not enough. |
| C5_theory_to_technical_atlas.md | APPENDIX, CONCLUSION, all chapter plans | boundary/control input | theory/atlas boundary; concept-first atlas; controlled repetition | Скорее служебный источник, не глава. | Partly superseded by completed Atlas, but boundary remains active. |

## Companion-файлы фрагментов

Для каждого основного фрагмента companion-файлы `*_source_usage.md`, `*_story_anchor_map.md`, `*_figure_candidates.md`, `*_open_questions.md`, `*_degradation_and_duplication_audit.md` читать только в релевантном chapter package. В общий routing layer они дают три решения:

- где нужны source/provenance checks;
- где есть visual candidates;
- где уже выявлены дефекты, которые нельзя повторять в главе.

## Решение по старой A/B/C-логике

Старая A/B/C-логика остаётся материалом, но не задаёт верхнюю композицию. Верхняя композиция теперь — Skeleton V5 and lifecycle-of-change axis. Поэтому будущий chapter package должен сначала определить section contract, затем выбрать нужные фрагменты, а не пытаться механически склеить A/B/C в новую главу.
