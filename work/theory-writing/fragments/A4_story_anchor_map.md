# A4. Карта story anchors

Эта карта не предназначена для пересказа историй внутри A4. Её задача — сохранить, какие narrative anchors можно подключить позже, если раздел будет расширяться в главу о PWG, Gas Town или документной агентной работе.

| Якорь | Роль для A4 | Как использовать позже | Ограничение |
|---|---|---|---|
| Jökull / `/babysit-pr` | Показывает рабочий цикл, где PR сопровождается до проверяемого выхода: CI, review, Greptile/Codex feedback, Fix/Dismiss/Escalate, ограничение итераций. | Подключать как пример gate-driven loop: агент не «закончил», пока внешние проверки и решения не закрыты. | Не превращать в общий PWG: это PR-escort skill, а не весь механизм рабочего состояния. |
| Jökull / перенос знания в skill или `CLAUDE.md` | Показывает, что знание процедуры должно уходить из transient chat в durable рабочие носители. | Использовать для перехода от memory by conversation к memory by artifact/skill/work graph. | Не смешивать skill memory и PWG: skill хранит процедуру, PWG хранит состояние конкретной работы. |
| HumanLayer / research → plan → implement | Поддерживает тезис, что агентный harness должен различать исследование, план, реализацию, проверку, human intervention и control flow. | Использовать как bridge к gates и staged readiness. | Не цитировать как системный первоисточник без повторного открытия публичного материала. |
| HumanLayer / subagents as isolation/compression | Показывает, что subagents полезны как context isolation, но результат должен быть в проверяемом artifact. | Использовать рядом с Anthropic research system: subagent summary недостаточен без evidence package. | Не делать из subagent pattern замену PWG; он лишь производит материалы для графа. |
| Matt Pocock / `/to-prd`, `/to-issues`, `/handoff` | Хороший якорь для границы между intent artifacts, issues и handoff. | Подключать в section о том, почему issue is not contract и почему handoff должен быть stateful. | Не сводить PWG к PRD→issues pipeline. |
| Matt Pocock / PRD lifecycle gap | Показывает проблему: после закрытия issues не всегда ясно, кто синхронизирует PRD с фактическим состоянием. | Использовать как пример tail lifecycle и cleanup/update после выполнения. | Нужен первоисточник или явная внутренняя пометка перед публикацией. |
| Shopify Roast / executable workflow | Показывает, что workflow outputs, logs, session filenames and replayability должны быть частью проверки. | Использовать для figure о evidence and observability. | Не превращать в story overview; использовать только как короткий factual anchor. |
| Shopify Roast / generated documentation needs workflow checks | Поддерживает второй порядок: документация, созданная LLM, сама должна проходить workflow/readability checks. | Подключать к source audit и figure candidates for document-work gates. | Проверить источник перед финальной публикацией. |
| Gas Town / Beads inside town | Показывает иерархию: PWG как рабочий субстрат внутри более широкой агентной среды. | Использовать в boundary section только как верхний слой: публичный glossary подтверждает Town/Rig уровни и роли вроде Mayor, Deacon, Polecat, Refinery, Witness. | Не отождествлять Gas Town с PWG и не тащить весь cast ролей в A4. |
| GSD/BMAD process artifacts | Соседние формы долговечных process artifacts: state files, PRD/architecture/story/sprint status. | Использовать для сравнения в отдельном узле о process-state, если понадобится. | Не использовать как primary evidence для PWG без отдельного источникового прохода. |

## Проверка story anchors против core-object line

Истории не должны подменять объектную линию PWG. Для каждого будущего narrative insertion нужно заранее отметить, какой объект он поддерживает: work item, dependency, owner/claim, gate, readiness, evidence, handoff, prime, recovery или cleanup. Если история поддерживает только общее настроение «агенты нуждаются в процессе», она не должна входить в A4. Если история показывает конкретный переход — например, PR ждёт CI/review gate, handoff переносит state, generated docs требуют verification, PRD расходится с фактическим состоянием, — её можно использовать как короткий anchor при условии повторной проверки первоисточника.

## Boundary guard для историй

При добавлении story anchors в финальный текст нужно проверять, не сдвигают ли они фрагмент в соседний жанр. История про issue/PR должна поддерживать readiness, gate или evidence, а не превращать PWG в GitHub/Linear commentary. История про execution workflow должна поддерживать recovery или handoff, а не подменять PWG durable runtime. История про multi-agent coding должна показывать ownership/source/evidence boundary, а не сводиться к «несколько агентов работают быстрее». История про Gas Town допустима только как верхний слой организации, внутри которого PWG остаётся отдельным substrate.

## Failure-pressure guard

Истории можно добавлять только тогда, когда они усиливают конкретный failure pressure: ложное завершение, lost state, duplicated work, stale snapshot, wrong authority, незакрытый gate или unsynthesized source claim. История не должна становиться самостоятельным кейсом внутри A4. Её функция — коротко показать, какой сбой PWG делает видимым и управляемым.

## Source-depth note после прохода 0f1f024c5a

Beads Claude Code integration можно использовать как короткий технический anchor для prime, но не как отдельную историю. Его роль — показать, что prime должен быть регулярным, artifact, запускаемый hook’ами на границе старта сессии и уплотнения контекста, а не произвольным резюме агента. В narrative version это допустимо вставлять только рядом с различением prime, handoff and recovery.

## Стилевой guard после прохода a792e977b2

Во втором стилевом проходе A4 не использует истории как самостоятельные кейсы. Beads, GitHub/Linear, Task Master, durable execution, CodeCRDT/STORM и Anthropic остаются техническими anchors для границ механизма. Если позже добавлять Jökull, HumanLayer, Matt Pocock или Shopify Roast, они должны входить только как короткая проверка конкретного перехода: gate, evidence, handoff, source state, recovery или cleanup. История не должна заменять теоретический ход «обрыв сессии → продолжимое рабочее состояние → границы полномочий».

## Provenance note после прохода eec2b912df

Для Gas Town восстановлен публичный первоисточник — `gastown/docs/glossary.md`. В A4 он должен поддерживать только boundary-тезис: Gas Town расположен выше PWG как агентная среда с Town/Rig уровнями и ролями. Истории и внутренние реконструкции Gas Town не должны входить в A4 без отдельного первоисточника и отдельной композиционной причины.

## Остаточная починка после прохода 6e7b58388e

Дополнительных story anchors в A4 не вводилось. Сохранено решение: истории остаются картой будущих вставок, а текущий фрагмент держится на технических boundary anchors. Это оставлено без изменения, чтобы не превратить A4 в пересказ кейсов.

## Repair note 2026-06-11

A4 после repair всё ещё сознательно не вводит сюжетные story anchors в основной текст. Beads, Task Master, Anthropic, LangGraph/Temporal/DBOS/Restate, CodeCRDT/STORM и Gas Town остаются техническими boundary anchors. Истории Jökull/HumanLayer/Matt Pocock/Shopify Roast можно добавлять позже только как короткие проверки конкретных переходов PWG: gate, evidence, source state, передача работы, восстановление или cleanup.
