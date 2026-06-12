# Codex understanding summary

Дата: 2026-06-08  
Задача: `work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md`

Текущая работа больше не является продолжением старой попытки механически расширить теоретическую часть про агентскую разработку. В старой версии был сильный композиционный ход: от удачного запроса к рабочей среде вокруг модели. В expanded-версии накопилось больше источников, артефактов и кейсов, но сама форма начала деградировать: источники и кейсы стали становиться единицами композиции. Поэтому проект перешёл к рамке AI-driven SDLC: объектом анализа стало не отдельное использование модели, а жизненный цикл программного изменения.

Эта рамка описывает движение через намерение, контекст, делегирование, исполнение, свидетельства, ревью, право завершения и сопровождение. Она не равна обычной корпоративной схеме SDLC с добавленным AI на каждой фазе. Важнее другое: как намерение становится проверяемым артефактом, как агент получает ограниченную рабочую среду, как результат получает свидетельства, кто имеет право принять изменение и как опыт возвращается в спецификации, тесты, политики, инструкции, skills и контекстные файлы.

Expanded theory теперь является quarry, а не main draft. Это означает, что из неё можно брать фактуру, источники, удачные связи и уже найденные наблюдения, но нельзя возвращать её каталожную структуру как форму будущего документа. Старый сайт и старая теория остаются композиционным baseline: не потому, что они полнее по источникам, а потому что лучше удерживают движение мысли.

SPDD и Gas Town защищены как deep anchors. SPDD показывает intent/specification lifecycle: prompt становится first-class delivery artifact, связанным с REASONS Canvas, OpenSPDD, генерацией, тестами, review, обновлением prompt и sync. Gas Town / Beads показывает organizational/operational lifecycle: роли, Mayor, Beads, durable task state, hooks, service agents, session continuation и cost of orchestration. Оба кейса уже пострадали или могли пострадать от сжатия, поэтому для них действует baseline restore rule: сначала old-site seed целиком, затем адаптация и дополнение, затем anti-degradation check. Нельзя начинать с compressed expanded-версии и нельзя снижать детализацию без human gate.

Protected methodology profile решает другой риск. Не каждая методология должна стать deep anchor уровня SPDD или Gas Town, но важные методологии нельзя сжимать до поверхностного обзора. Spec Kit, Kiro Specs, Constitutional SDD, два TDAD, GSD / Open GSD и BMAD Method должны быть раскрыты через проблему, workflow, артефакты, место контекста, роли, human gates, проверку, lifecycle tail, сильные стороны, failure modes, сравнение с соседями и разделение theory vs Handbook/Fieldbook. Это нужно, чтобы избежать провала “mentioned but not understood”.

GSD и BMAD поэтому не являются shallow mentions. Они не promoted to deep anchors now, потому что их архитектурная роль отличается от SPDD и Gas Town. Но они защищены от расплывчатого пересказа. В Part VII они должны объяснять, когда процесс сам становится артефактом: GSD как lightweight context/process loop, BMAD как role-based guided process, Spec Kit как specification toolkit, Gas Town как full organizational environment.

Parts VI-XII нельзя превращать в artifact catalog. ADR-0007 добавил много важных классов артефактов: decision records, context files, contracts, execution constraints, evidence packages, ownership, completion, lifecycle tail, architecture fitness, test data и другие. Но артефакт попадает в теорию только если он помогает перейти границу lifecycle. Поэтому skeleton v4.1 формулирует внутренние подглавы Parts VI-XII как жизненные напряжения, а не как перечень документов или инструментов.

Stage 0.19 должен создать protected methodology dossiers, а не финальные главы. Для каждой методологии нужны шесть видимых проходов: source inventory, workflow reconstruction, artifact and gate map, missing detail pass, comparative pass, anti-shallow audit. Только после этого создаются финальные dossiers и comparative synthesis reports. Если source depth окажется слабым, если потребуется demotion, promotion to deep anchor, изменение approved plan или broad source search, Codex должен остановиться и запросить human decision.

Языковое правило жёсткое: рабочие объяснения и отчёты должны быть по-русски. Английские названия допустимы для точных имён инструментов, файлов, source titles и устойчивых терминов, но английский не должен становиться клеем обычного объяснения.

По итогам readiness check я считаю, что Codex готов запускать Stage 0.19 с предупреждениями. Предупреждения не блокируют старт: все core-документы видны. Но Stage 0.19 должен строго проверять достаточность primary/official sources для каждой методологии и не выдавать prior summaries за полноценный source inventory.
