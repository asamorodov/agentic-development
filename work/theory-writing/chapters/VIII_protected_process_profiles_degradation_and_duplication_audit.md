# VIII — degradation and duplication audit

Статус: заполнено по текущему тексту главы.

## Риски деградации

| Риск | Статус | Комментарий |
|---|---|---|
| Процесс превращается в бюрократию | controlled | Раздел «Когда процесс становится артефактом» прямо задаёт критерий: результат процесса должен менять следующий допустимый ход. |
| PWG и process profile смешиваются | controlled | Глава несколько раз разводит work state and mode selection. |
| BMAD захватывает главу | watchpoint | После P14 раздел сжат, но остаётся самым длинным. Больше не расширять без замены. |
| GSD превращается в отдельную статью | controlled | GSD используется только как профиль длинной работы; детали `gsd-pi` and broader architecture не развёрнуты. |
| Gas Town / Beads уводят в главу X | controlled | Раздел оставлен коротким и явно описан как верхняя граница. |
| Английский связующий язык возвращается | watchpoint | P13 убрал большую часть английского клея, но source-native terms остаются. Требуется финальный стиль-проход. |
| `billing/API` начинает выглядеть как реальный case | controlled | В story anchors отмечено: это synthetic explanatory example. |
| Investigation vocabulary завышает силу материалов | watchpoint | В BMAD Forensic контексте `investigation` оправдан. В остальных местах лучше не расширять это слово. |

## Дублирование с соседними главами

| Соседняя глава / материал | Потенциальное дублирование | Решение |
|---|---|---|
| Глава VII / PWG | Work state, durable node, dependencies, blockers. | В VIII это только вход: состояние не выбирает режим. |
| Глава IX | Permissions, sandbox, worktree, hooks, MCP access. | В VIII это только мост: профиль выбирает режим, IX показывает реальное исполнение и права. |
| Глава X / Gas Town | Multi-agent operation, queues, workers, orchestration. | В VIII это верхняя граница, не подробное раскрытие. |
| GSD atlas article | `.planning/`, phase loop, specialist agents. | В VIII оставлены только элементы, нужные для process profile argument. |
| BMAD atlas article | Full BMAD method details. | В VIII BMAD сжат до routing functions: help, story, correct-course, brownfield, investigation. |
| Story articles | Jesse/HumanLayer/Matt details. | В VIII взяты только те эпизоды, которые показывают маленькие process profiles. |

## Итог

Глава не дублирует соседние главы механически. Её собственный вклад: показать слой выбора следующего режима между долговечным состоянием работы и средой исполнения.
