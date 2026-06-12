# C3 story anchor map

Статус: companion-файл к `C3_pwg_to_evidence.md`. Назначение — зафиксировать, какие истории и методологические эпизоды используются как фактические якоря моста, без пересказа историй. Три общих редакторских прохода уточнили границу: якоря должны поддерживать переход состояния, а не превращать C3 в каталог evidence surfaces.

| Якорь | Роль в C3 | Что НЕ делать |
| --- | --- | --- |
| PWG / Beads | Показывает, что граф работы уже умеет хранить устойчивую идентичность, зависимости, ready/blocked queue, контрольные условия и историю. C3 добавляет к этому вопрос доказанности `completed`. | Не сводить PWG к Beads и не раскрывать CLI/архитектуру Dolt как отдельный технический атлас. |
| Gate/evidence boundary | Beads gate и Temporal HITL помогают развести durable wait и доказательство результата: gate ждёт сигнал, evidence package объясняет, почему сигнал закрывает обещание. | Не превращать gate-resolution в acceptance; не делать отдельную подглаву про durable execution. |
| Механика прикрепления свидетельств | Все якоря C3 теперь читаются через адрес прикрепления: work item, claim/promise, gate, transition record и completion decision. | Не рассказывать заново A7; не описывать evidence как автономную папку логов рядом с графом. |
| Граница зелёного сигнала | Зелёные сигналы переводят статус пакета свидетельств, но не закрывают work item без authority: CI, review, rollout, saved run и browser pass остаются входами состояния. | Не принимать `passed` / `successful` / `approved-looking` за `completed`; не дублировать теорию observation/evidence из A7. |
| TDAD second line | Даёт пример оракула, привязанного к изменённой области: агенту нужны затронутые тесты через `.tdad/test_map.txt`, а не общая TDD-дисциплина. | Не писать обзор двух TDAD и не сравнивать все метрики/эксперименты. |
| Pact consumer contracts | API-якорь: contract evidence подходит для обещания совместимости запросов/ответов, но не закрывает functional/provider behavior или эксплуатационный риск. | Не превращать C3 в раздел о contract testing и не добавлять Pact workflow за пределами узкой точки про оракул. |
| ADR confirmation | Даёт пример, где доказанность решения шире теста: `Confirmation`, владельческое ревью, `CODEOWNERS`, совместимость, SLO или rollout-сигнал. | Не превращать C3 в подглаву об ADR; Nygard/Fowler/MADR подробно должны жить в A2/ADR-узле и атласе. |
| Anthropic modernization baseline | Называет типы evidence для миграции: tests/evals, domain experts, side-by-side execution, API wrappers, edge cases, parallel run, output comparison before cutover. | Не использовать как маркетинговое доказательство универсальной успешности Claude Code. |
| Winder.AI Kodit migration | Отрицательный якорь: локальные проверки, сборка и тесты прошли, но после видимого completion обнаружились semantic/API/search failures. | Не рассказывать всю историю миграции Python→Go; использовать только границу “local green ≠ parity evidence”. |
| TechChannel / Swimm COBOL critique | Жёсткая migration metric: покрытие бизнес-правил, повторяемость, пропущенные условия и семантика расчёта. | Не выдавать за нейтральный академический benchmark; источник полезен как критический technical warning. |
| Augmented Code RSpec→Minitest | Положительный чистый якорь: evidence package создаётся в ходе six-gate pipeline, а не после завершения как summary. | Не описывать все Rails/AASM детали; они нужны для fieldbook/atlas, а не для C3. |
| Karthik Subramanian product migration | Положительный полевой якорь: многоуровневый процесс с plan review, worktrees, MR loop, CI/review/QA handoff показывает роль acceptance owners. | Не использовать как воспроизводимое forensic-доказательство и не пересказывать customer-style outcome claims сверх нужного. |
| Arvid Kahl browser loop | Якорь наблюдения: screenshots/DOM/browser pass становятся свидетельством только после привязки к маршруту, действию пользователя, diff, повторному проходу и пределу проверки. | Не повторять A7 visual asset и не делать отдельную UI-testing подглаву. |
| Shopify Roast / external Roast run | Тестово-журнальный якорь: именованные шаги workflow, command output, Minitest seed/result и сохранённый `final_output.txt` показывают, как прогон становится прикрепляемым свидетельством. | Не утверждать, что saved output сам по себе доказывает продуктовую корректность. |
| Stripe Minions / integration benchmark | Якорь ревью: clean-context judge, diagnostics, CI/PR/human review и детерминированные evaluators отделяют review signal от final acceptance. | Не пересказывать enterprise platform story и adoption layer; использовать только границу review/evaluator. |
| Argo Rollouts analysis | Rollout-якорь: результат AnalysisRun может продолжить, прервать или поставить deployment на паузу, поэтому rollout evidence меняет состояние работы после merge. | Не превращать C3 в раздел progressive delivery; оставить как пример state-transition. |
| Google SRE canarying | Операционный якорь: canary evaluation решает, продолжать, ставить на паузу или откатывать rollout; поддерживает state flow accepted/rejected/blocked. | Не открывать широкую SRE/SLO-теорию здесь; оставить SLO/error-budget depth операционному evidence-разделу. |

## Свежая редакторская проверка

Второй общий проход не изменил набор якорей.
Третий общий проход не менял набор якорей: глубокого дефекта функции не найдено. Якоря остаются проверками разных переходов состояния, а не самостоятельными мини-историями.
Главная проверка: каждый якорь должен отвечать на вопрос, какой статус или решение он может изменить в PWG. По этой проверке TDAD/Pact/MADR/миграция/rollout остаются оправданными, а подробные истории остаются за пределами C3.

## Композиционная граница

C3 должен стоять после A7 и рядом с PWG-узлом. A7 различает наблюдение и свидетельство по адресату сигнала. C3 переносит это различение в состояние графа: свидетельство становится причиной перехода рабочего элемента, а не приложением к итоговому отчёту. Фрагмент не должен забирать работу A8 про право действовать/право завершать целиком; здесь нужен только тот минимум, без которого `completed` нельзя считать валидным состоянием.


## Второй стилевой проход

Проверка против досье-эффекта: истории остаются в C3 только как якоря переходов состояния. TDAD/Pact/MADR отвечают на вопрос выбора оракула; Winder/TechChannel/Anthropic/Augmented Code ограничивают миграционный oracle; Arvid/Roast/Stripe/Argo/Google SRE показывают, когда рабочий след, ревью или rollout-сигнал должен менять состояние графа.

Ограничение для следующих проходов: не расширять ни одну историю в самостоятельный кейс. Если потребуется больше деталей по миграции, UI-проверке, Roast, Stripe или rollout, переносить их в fieldbook/atlas; в C3 оставлять только ту часть, которая объясняет `waiting_for_evidence`, `review`, `accepted`, `rejected`, `blocked`, `rollout_paused` или `rollback_required`.
