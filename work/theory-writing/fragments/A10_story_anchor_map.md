# A10 story anchor map

Статус: companion-файл к `A10_mode_selection_map.md` после второго стилевого прохода S02. Он фиксирует, какие story anchors использованы как фактические якоря, какую функцию они выполняют в аргументе и как они соотносятся с опорой на A/B/C-узлы, чтобы истории не подменяли теорию.

| История / anchor | Где в A10 | Функция якоря |
|---|---|---|
| [Peter Steinberger — короткие запросы вместо ceremony](#story-02-peter-steinberger--9-just-talk-to-it-korotkie-zaprosy-vmesto-ceremony) | Введение; раздел “Разговор и план”. | Показывает, что лёгкий разговорный режим может быть экспертной формой при малом радиусе, близкой проверке и сильной ментальной модели человека. |
| [Boris Tane — plan.md как отдельный документ](#story-01-boris-tane--4-stadiya-planirovaniya-plan-kak-otdelnyy-markdown-dokument) | Введение; раздел “Разговор и план”. | Показывает критерий перехода от conversation к plan: раннее предположение агента должно стать видимым до дорогой реализации. |
| [HumanLayer — research-plan-implement](#story-07-humanlayer--3-research-plan-implement-kontur-sohraneniya-smysla) | Раздел “Разговор и план”. | Поддерживает различение стадий исследования, плана и реализации как разных контекстов и точек обратной связи. |
| [Simon Willison — вопросы о коде можно решать кодом](#story-03-simon-willison--1-ishodnyy-printsip-voprosy-o-kode-chasto-mozhno-reshat-kodom) | Разделы “Разговор и план”, “Свидетельства и завершение”. | Показывает режим исследования как самостоятельного проверочного артефакта, а не как подготовки к правке основного проекта. |
| [Mark Erikson — dev-plans и внешняя рабочая память](#story-10-mark-erikson--11-dev-plans-vneshnyaya-rabochaya-pamyat-otdelennaya-ot-repozitoriya-koda) | Введение; разделы про PWG и последующий ремонт. | Показывает, что внешняя память защищает ментальную модель человека, а не только способность агента продолжить работу. |
| [Jesse Vincent — план как переносимый носитель контекста](#story-06-jesse-vincent--5-plan-kak-perenosimyy-nositel-konteksta) | Раздел про спецификацию, ADR и PWG. | Показывает промежуточный случай: plan начинает работать как handoff между сессиями, но ещё не равен полноценному PWG. |
| [Calvin French-Owen — Codex web и длинный поводок](#story-09-calvin-french-owen--4-codex-web-asinhronnyy-agent-dlinnyy-povodok-i-proveryaemye-sledy) | Раздел про PWG; раздел про завершение. | Показывает, что фоновая работа требует восстанавливаемого состояния утром: что сделано, что проверено, где нужен выбор. |
| [Matt Pocock — skills as small process repair](#story-12-matt-pocock-skills--1-pochemu-eto-ne-odin-bolshoy-protsess) | Раздел “Процесс и среда”; раздел “Последующий ремонт”. | Показывает критерий перехода к процессу: повторяемый сбой получает малую внешнюю форму, которую можно читать, чинить и удалять. |
| [Jesse Vincent — Superpowers and gates](#story-06-jesse-vincent--11-superpowers-ruchnye-priemy-stanovyatsya-dostupnymi-agentu) | Раздел “Процесс и среда”. | Показывает более тяжёлую траекторию формализации и её риск: процесс сам начинает требовать чистки. |
| [Mae Capozzi — platform-level agentic work](#story-11-mae-capozzi--1-tsentralnaya-liniya-agent-uskoryaet-rabotu-tolko-posle-poyavleniya-platformenn) | Разделы “Процесс и среда”, “Свидетельства и завершение”, “Последующий ремонт”. | Показывает командный уровень: агентская работа становится вопросом CI, наблюдаемости, design system, трассировок, проверок и принятия инструментов. |
| [Mike McQuaid — Sandvault, sandbox-exec, worktrees](#story-08-mike-mcquaid--5-sandvault-otdelnyy-polzovatel-macos-plyus-sandbox-exec) | Введение; раздел “Процесс и среда”. | Показывает критерий controlled environment: автономия покупается ограничением ущерба, а не просьбой к модели быть аккуратной. |
| [Arvid Kahl — browser loop, allow/deny](#story-04-arvid-kahl--9-brauzernyy-tsikl-kod-brauzer-svidetelstvo-pravka-proverka) | Разделы “Процесс и среда”, “Свидетельства и завершение”. | Показывает, что интерфейсные и продуктовые задачи требуют канала наблюдения за поведением, а не только чтения файлов. |
| [Jökull Sólberg — /babysit-pr](#story-05-jokull-solberg--6-babysit-pr-pr-kak-obekt-kotoryy-agent-vedet-do-proveryaemogo-vyhoda) | Раздел “Свидетельства и завершение”. | Показывает PR как самостоятельный объект сопровождения: CI, автоматическое ревью, исправления, повторные прогоны и состояние готовности. |
| [Jökull Sólberg — Fix / Dismiss / Escalate](#story-05-jokull-solberg--7-fix-dismiss-escalate-zaschita-ot-mehanicheskogo-poslushaniya) | Раздел “Свидетельства и завершение”. | Поддерживает различение review signals and commands: замечание требует классификации, а не механического исполнения. |
| [Mike McQuaid — PR как социальная нагрузка](#story-08-mike-mcquaid--20-pr-podgotovlennye-s-ii-kak-sotsialnaya-nagruzka-na-meynteynerov) | Раздел “Свидетельства и завершение”. | Показывает границу completion/authority: внешний PR остаётся ответственностью человека, который его приносит. |
| [Mae Capozzi — дешёвый запуск задач как командная нагрузка](#story-11-mae-capozzi--2-ishodnoe-davlenie-zapusk-zadach-stal-slishkom-deshevym) | Раздел “Свидетельства и завершение”. | Показывает, что рост агентского потока увеличивает нагрузку на ревью, CI, зависимости и платформенную инфраструктуру. |

## Проверка против задачи A10

- Истории использованы как точные якоря для критериев выбора режима, а не как последовательный пересказ.
- В основном тексте сохранены разные ответы на разные риски: conversation, plan, research, specification, ADR, PWG, process, environment, evidence, completion, repair.
- Ни одна история не объявлена нормой для всех задач.


## Связь story anchors с A/B/C-опорой

Этот раздел добавлен во втором проходе и дополнен в третьем, чтобы показать: story anchors дают фактуру, но не заменяют несущие теоретические узлы. A10 использует истории как проверочные примеры для уже заданных различений.

| Опорное различение | Story anchors в A10 | Какой риск закрывают |
|---|---|---|
| A1: изменение шире `prompt` | Boris Tane, Peter Steinberger, Mark Erikson, Calvin French-Owen | Показывают, что один и тот же агентский труд может требовать разговора, плана, внешней памяти или фона в зависимости от радиуса и состояния задачи. |
| A2–A3 / B1: спецификация, контракт, ADR и пределы spec-first | Boris Tane, HumanLayer, Jesse Vincent | Поддерживают мысль, что план и спецификация полезны как поверхности ревью, но сами по себе не хранят весь жизненный цикл работы. |
| A4 / B2 / C1 / C4: PWG как долговечное состояние работы | Mark Erikson, Jesse Vincent, Calvin French-Owen | Показывают handoff, восстановление контекста и длинную работу, где одиночный markdown-файл или след исполнения недостаточны. |
| A5 / C2: процесс после повторяемого сбоя | Matt Pocock, Jesse Vincent, Mae Capozzi, HumanLayer | Показывают разные носители повторяемого repair: маленький навык, более тяжёлый экзоскелет, платформенная проверка или изменение обвязки. |
| A6: среда исполнения и радиус ущерба | Mike McQuaid, Arvid Kahl | Поддерживают границу: документ управляет смыслом, но права, данные, команды, браузер и среда исполнения требуют отдельного контура. |
| A7 / C3: наблюдение vs свидетельство | Simon Willison, Arvid Kahl, Jökull Sólberg | Показывают, что тест, браузерный сценарий, CI, benchmark или петля ревью становится свидетельством только когда связаны с обещанием изменения. |
| A8: право действовать vs право завершать | Mike McQuaid, Jökull Sólberg, Mae Capozzi | Показывают, что PR, CI и автоматическое ревью не отменяют владельца принятия и социальную ответственность человека. |
| A9: последующий ремонт | Matt Pocock, Mae Capozzi, Mark Erikson | Показывают, что повторяемые сбои должны возвращаться в навыки, платформу, детерминированные инструменты или очистку устаревшего контекста. |
| B3: организационная среда сверх PWG | Mae Capozzi, Calvin French-Owen, Mike McQuaid | Поддерживают тезис, что при росте потока задач узким местом становится не только граф работы, но и ревью-пропускная способность, CI, права, культура и платформенный слой. |


## Edge cases, проверенные в edge/source-pass

| Edge case | Story / policy anchors | Как используется в A10 |
|---|---|---|
| Small reversible tasks | Peter Steinberger; Arvid Kahl | Разговорный режим допустим, когда правка мала, результат виден в `diff`, браузере или тесте, а откат дешевле предварительного документа. |
| Migration / dependency / platform task | Mae Capozzi; Calvin French-Owen | Первый проход может быть исследованием или планом, но продолжение требует совместимости, dry run, CI, владельца данных и плана отката. |
| Architecture decision | Boris Tane; Matt Pocock; A2/A3 plan | Малый `diff` не отменяет ADR, если решение станет будущим архитектурным ограничением или частью доменного языка. |
| Platform agents | Mae Capozzi; HumanLayer; Calvin French-Owen | Когда агент действует через CI, Figma, трассировки, MCP или внутреннюю платформу, карта должна выбирать права, наблюдаемость и человеческий контрольный барьер, а не только документ. |
| Policy-bound contributions | Mike McQuaid; Zig no-AI policy; Linux Foundation; EFF; OpenInfra | Contribution boundary относится к completion/authority: внешняя политика и ответственность человека могут ограничить даже технически возможную агентскую работу; условно-разрешающие политики добавляют права, лицензии, disclosure и повышенную ответственность ревью. |

## External policy anchors used

| Источник | Почему это не обычный story anchor | Где использован |
|---|---|---|
| Zig Code of Conduct, `Strict No LLM / No AI Policy` — https://ziglang.org/code-of-conduct/ | Это публичная политика проекта, а не история из corpus; она нужна как крайний случай policy-bound contribution. | Новый edge-case абзац в основном тексте; source ledger; open questions. |
| Mike McQuaid, Open Source Initiative maintainer profile — https://opensource.org/maintainers/mikemcquaid | Это внешний текст, на который ссылался `Cross_story_synthesis.md`; открыт как первоисточник для утверждения о проверке AI-output самим участником. | Новый edge-case абзац в основном тексте; source ledger; open questions. |
| Linux Foundation guidance regarding use of generative AI tools — https://www.linuxfoundation.org/legal/generative-ai | Это не story anchor, а правовая/policy рамка: она показывает условно-разрешающий режим AI-generated content через права, лицензии и проектные правила. | Уточнение policy-bound edge case; source ledger; open questions. |
| EFF policy on LLM-assisted contributions — https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects | Это policy anchor с промежуточной позицией: LLM assistance не запрещается целиком, но ответственность за понимание кода и human-authored docs/comments остаётся у участника. | Уточнение policy-bound edge case; source ledger; open questions. |
| OpenInfra Foundation policy for AI-generated content — https://openinfra.org/legal/ai-policy/ | Это policy anchor, где режим вклада задаётся через human-in-the-loop, disclosure labels, Signed-Off-By и повышенное ревью. | Уточнение policy-bound edge case; source ledger; open questions. |

## P06 criteria-strengthening note

- Story anchors не расширялись и не пересказывались заново: целевой проход усилил не фактуру историй, а признаки выбора режима, уже выведенные из story anchors и A/B/C-опор.
- Новые критерии после таблицы сохраняют прежние anchors: small reversible tasks поддерживают conversation, plan-first истории поддерживают research/plan, long-running/context stories поддерживают PWG, platform/sandbox/PR stories поддерживают environment/evidence/completion.

## P07 transition-strengthening note

- Переходы между режимами усилены без новых story anchors. Существующие истории используются как проверки: Steinberger-режим остаётся примером неусложнения, Boris/HumanLayer — перехода к plan/research, Mark/Jesse/Calvin — перехода к долговечному состоянию, Matt/Jesse/Mae — перехода от локальной коррекции к process/platform, McQuaid/Arvid/Jökull — перехода к environment/evidence/completion.
- Новая формула “цена опоздавшей структуры выше цены её ведения” не добавляет фактуру, а связывает уже использованные anchors в критерий перехода.

## P08 practical-applicability note

- Практическое правило выбора режима не добавляет новых story anchors. Оно связывает уже использованные истории в операционную последовательность: начать с лёгкого достаточного режима, поднять структуру при неизвестном фронте, долговечном обязательстве или опасных правах/передаче, и понизить режим, когда исследование доказало локальность и обратимость.

## P09 general editor pass note

- Story anchors не расширялись. Основное изменение — более явная ссылка на Simon Willison в evidence-разделе и разделение edge-case абзаца, чтобы policy-bound contribution не смешивался с другими граничными случаями.
- Функция story anchors сохранена: они остаются проверками критериев выбора режима, а не повторным пересказом корпуса историй.

## P10 general editor pass note

- Новых story anchors не добавлено. Повторная оценка не выявила потери фактуры: изменения P10 касались только двух формулировок в общем аргументе, а не story-specific материала.

## P11 general editor pass note

- Третий общий редакторский проход не добавил и не удалил story anchors. Проверка подтвердила, что основной фрагмент использует истории как граничные проверки выбора режима, а не как повторный story synthesis.

## S02 style pass note

- Второй стилевой проход не добавил story anchors и не расширил роль существующих историй. Основной фрагмент читается как теоретическая карта выбора режима: истории остаются граничными проверками, а не самостоятельным досье.
- Ограничение для будущей сборки: если anchors будут заменяться на внутриглавные ссылки, нужно сохранить их функцию проверки границы, а не превращать их в новый пересказ story corpus.

## Проверка после edge/source-pass

- Story anchors остались точечными: они поддерживают критерии выбора режима, но не превращаются в повторный пересказ историй.
- В A10 добавлена явная граница: карта не вводит новый метод, а сжимает A/B/C-различения в практический режим выбора.
- Истории не используются для утверждений о SPDD, PWG или Gas Town сверх того, что разрешённый план уже задаёт как функцию соответствующих узлов.
- Полная сверка с фактическими текстами A/B/C-фрагментов остаётся открытым долгом, потому что эти файлы не были разрешёнными входами текущего листа.
- Пять edge cases добавлены как проверка карты на границах: small reversible task, migration, architecture decision, platform agent, policy-bound contribution; последний теперь опирается не только на строгий запрет и maintainer etiquette, но и на условно-разрешающие policy anchors.
