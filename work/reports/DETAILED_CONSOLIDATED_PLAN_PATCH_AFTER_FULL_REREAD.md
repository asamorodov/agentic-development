# Детализированный patch к плану после повторного перечитывания корпуса и Stage 0.5–0.9

Дата: 2026-06-07  
Режим: кумулятивный архив-оверлей.  
Статус: подробный проект изменения `work/approved-ai-sdlc-plan.md`. Сам approved plan этим файлом не меняется.

Этот документ заменяет прежний короткий consolidated patch как рабочий материал для принятия решения. Он не отменяет `work/reports/CONSOLIDATED_PLAN_PATCH_AFTER_STAGE_0_5_TO_0_9.md`, а раскрывает его подробнее после повторного перечитывания доступных материалов:

- старая теория из `content/Theoretical_synthesis.md`;
- последняя expanded/quarry-версия из `work/expanded-quarry-theoretical-synthesis.md`;
- `content/Cross_story_synthesis.md`;
- все 12 историй из `content/stories/`;
- `work/approved-ai-sdlc-plan.md`;
- `work/theory-source-map-ai-driven-sdlc.md`;
- отчёты Stage 0.5–0.9;
- правила языка, стиля и работы с англоязычными источниками из `protocols/rules/`.

Повторное чтение подтвердило главный вывод, но уточнило форму patch. Проблема уже не в нехватке источников. Проблема в том, как не превратить новую теорию в большое хранилище правильных артефактов. Поэтому patch должен добавлять не “ещё темы”, а более строгую внутреннюю механику: **изменение проходит через связанные артефакты и управляющие поверхности**.

## 1. Что именно стало яснее после перечитывания старой теории

Старая теория в `content/Theoretical_synthesis.md` сильна не полнотой современных источников, а композицией. В ней есть ясный исходный сдвиг:

```text
от удачного запроса → к рабочей среде вокруг модели
```

Её сильные узлы:

1. модель стала достаточно сильной, чтобы узкое место переместилось наружу;
2. агент — это петля действия и проверки, а не одноразовый ответ;
3. запрос перестаёт быть единицей управления;
4. контекст — это рабочее состояние, а не только окно;
5. спецификация, долговременный контекст и передача состояния — разные вещи;
6. SPDD раскрыт как мощный спецификационный контур;
7. обвязка, проверка, свидетельства и среда выполнения составляют самостоятельный слой;
8. Gas Town раскрыт как отдельная организационная модель;
9. человек остаётся владельцем того, что нельзя свести к датчику;
10. автономия — договор с окружением, а не свойство модели.

Именно эту композиционную силу нельзя потерять. Старый текст уже содержит будущий AI-driven SDLC в зародыше: там есть намерение, контекст, обвязка, среда, память задачи, проверка, ответственность, граница автономии and Handbook. Новая рамка не должна вытеснить это старое движение. Она должна переименовать и уточнить его через lifecycle программного изменения.

## 2. Что стало яснее после перечитывания expanded quarry

`work/expanded-quarry-theoretical-synthesis.md` богаче старой теории, но опаснее как форма. Он содержит множество полезных источников: реальные сессии, PR, рассогласования, SASE, open-source policy cluster, новые эмпирические исследования, спецификационные подходы, governance, benchmarks. Но его верхняя структура “карты течений” снова тянет текст к каталогу.

Quarry полезен для:

- фактов;
- источников;
- эмпирических предупреждений;
- формулировок о сессиях, PR and review;
- деталей по SASE/open-source governance;
- связок между evidence, ownership and completion right.

Quarry опасен для:

- верхней формы;
- равноправных source-name subsections;
- накопления medium cases без управляющей линии;
- повторного сжатия deep anchors;
- превращения Part XII в склад всех поздних предупреждений.

Поэтому patch должен явно сказать: новые артефакты из Stage 0.5–0.9 берутся не как “ещё разделы”, а как связующие звенья жизненного цикла.

## 3. Что стало яснее после перечитывания Cross-story synthesis и 12 историй

`content/Cross_story_synthesis.md` и истории дают очень важное ограничение: реальные разработчики не работают по одной большой методологии. Они выбирают режимы: research-first, plan-first, light conversational mode, browser/runtime loop, PR-sitting, sandbox/worktree isolation, skills/hooks, external memory, review package.

Истории сильны не тем, что каждая даёт новую “школу”, а тем, что они показывают повторяющиеся напряжения:

- план нужен не всегда, но когда нужен — он является местом решения, а не украшением;
- исследование иногда готовит реализацию, а иногда само является результатом;
- PR — не конец работы, а социально-техническая поверхность;
- песочница и рабочие деревья покупают автономию ограничением ущерба;
- skills/hooks/scripts чинят повторяемый сбой процесса;
- внешняя память защищает не только агента, но и человека;
- evidence package должен быть пригоден для следующего шага;
- человеческое внимание должно стоять в точках максимального рычага.

Это означает: patch не должен превращать теорию в “официальную методологию AI-driven SDLC”. Он должен дать карту выбора режима, но уже с уточнённой таксономией артефактов.

## 4. Центральная поправка к замыслу

Прежняя формула:

```text
AI-driven SDLC = жизненный цикл программного изменения.
```

Остаётся верной, но теперь её нужно уточнить:

```text
AI-driven SDLC = жизненный цикл программного изменения, проходящий через связанные артефакты, управляемые среды и права завершения.
```

Финальная теория должна показывать не просто стадии:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → право завершения → сопровождение
```

а то, **какие артефакты переносят смысл между этими стадиями**.

Если этого не сделать, найденные новые материалы будут выглядеть как набор поздно добавленных “важных тем”: ADR, GSD, SBOM, секреты, observability, CODEOWNERS, traceability, contracts, runbooks. Если сделать, они станут не отдельными темами, а разными типами соединительной ткани жизненного цикла.

## 5. Пять классов артефактов вместо длинного списка

Чтобы не получить каталог, предлагается не перечислять 30 артефактов как равноправные, а сгруппировать их в пять классов.

### 5.1. Артефакты намерения и решения

Что сюда входит:

- prompt;
- requirements / PRD;
- specification;
- acceptance criteria;
- ADR / decision record;
- RFC / design proposal;
- API/data contract;
- traceability link.

Функция: удержать не только “что хотим”, но и почему, по каким альтернативам, с какими ограничениями and как это связано с кодом и проверкой.

Почему это нужно: старая теория уже говорила, что хороший запрос не является единицей управления. Stage 0.5–0.9 уточнили, что одной спецификации тоже мало: decision provenance and traceability are different functions.

### 5.2. Артефакты состояния задачи и проекта

Что сюда входит:

- `research.md`;
- `plan.md`;
- handoff;
- progress log;
- task graph;
- `AGENTS.md`;
- Cursor rules / Agent README;
- codebase readiness note;
- software catalog / ownership metadata.

Функция: сделать проект читаемым для агента и человека.

Почему это нужно: Cross-story synthesis постоянно возвращается к тому, что состояние задачи нельзя хранить только в чате. Истории Boris Tane, HumanLayer, Mark Erikson and Matt Pocock особенно поддерживают эту линию.

### 5.3. Артефакты среды исполнения и ограничений

Что сюда входит:

- dev container / reproducible environment;
- sandbox / permissions;
- worktree;
- tool/MCP boundary;
- policy-as-code;
- secret scanning;
- credential inventory;
- sensitive context boundary;
- agent workflow specification.

Функция: не просто дать агенту инструменты, а сделать его действие ограниченным, воспроизводимым and наблюдаемым.

Почему это нужно: старая теория уже говорила, что обвязка регулирует конкретное состояние кодовой базы. Stage 0.7–0.9 добавили более точные виды такой обвязки.

### 5.4. Артефакты свидетельства и проверки

Что сюда входит:

- test outputs;
- CI evidence;
- benchmark results;
- contract tests;
- traceability matrix;
- review comments;
- PR description;
- agent trace / tool-call log;
- policy check results;
- security review;
- SBOM/provenance evidence.

Функция: дать результату право двигаться дальше.

Почему это нужно: Part X не должен быть только “про тесты”. Он должен объяснять, что тип свидетельства зависит от типа изменения. Review, trace, contract and provenance are evidence too.

### 5.5. Артефакты завершения и хвоста lifecycle

Что сюда входит:

- CODEOWNERS;
- ownership map;
- review routing;
- escalation path;
- release plan;
- migration plan;
- rollback plan;
- runbook;
- incident report;
- postmortem;
- changelog/release notes;
- dependency policy;
- deprecation policy;
- context cleanup;
- stale ADR / decision debt.

Функция: показать, что AI-driven SDLC не заканчивается на merge.

Почему это нужно: Stage 0.5–0.9 показали, что главный риск Part XII — либо слабость, либо превращение в склад. Группировка через “хвост lifecycle” удерживает форму.

## 6. Подробный patch по частям

## Введение

### Что добавить

Введение должно сразу защитить от трёх неверных чтений:

1. “Это про prompt engineering”.
2. “Это обычный корпоративный SDLC с AI на каждой фазе”.
3. “Это про рост количества кода / PR / задач”.

Добавить тезис: AI-driven SDLC оценивается не по объёму агентского вывода, а по способности процесса сохранить намерение, проверить изменение, распределить ответственность and вернуть опыт в среду.

### Какие источники поддерживают

- DORA / Bain — AI усиливает существующую систему and bottlenecks.
- SPACE / DevEx — activity is not productivity.
- Human-AI review and supervisory engineering studies — больше generated activity может увеличить проверочную нагрузку.

### Как писать

Не превращать введение в обзор исследований. Дать рамку и сразу перейти к единице анализа.

## Часть I. Единица анализа: программное изменение, а не prompt

### Что добавить

Добавить “правило входа артефакта в теорию”:

```text
Артефакт важен для этой теории только если он переносит изменение через границу жизненного цикла.
```

Показать семь границ:

1. намерение → контекст;
2. контекст → делегирование;
3. делегирование → исполнение;
4. исполнение → свидетельства;
5. свидетельства → ревью;
6. ревью → право завершения;
7. завершение → сопровождение и обучение среды.

### Что не делать

Не давать полный список всех артефактов. Не начинать с таблицы. Таблица допустима позже в report/dossier, но основной текст должен быть аргументом.

## Часть II. Реальная агентская сессия

### Что добавить

Показать ограниченность session trace. Она видит:

- prompts;
- tool calls;
- corrections;
- pushback;
- generated code survival.

Но она плохо видит:

- ADR;
- ownership;
- release state;
- deployment/migration risk;
- SBOM;
- hidden contracts;
- stale context files.

### Зачем

Это создаёт естественный переход: реальная сессия показывает, почему lifecycle artifacts are needed. Не потому, что мы любим документацию, а потому что trace alone не удерживает всю инженерную работу.

## Часть III. Намерение: почему prompt слишком слаб как единица управления

### Что добавить подробно

Различить:

- prompt — локальная инструкция;
- requirements / PRD — исходное требование или продуктовая потребность;
- specification — целевое поведение and constraints;
- plan — путь исполнения;
- ADR — принятое решение and consequences;
- RFC/design proposal — пространство обсуждения до решения;
- contract — граница для других систем или данных;
- traceability link — связь между intent, implementation and evidence;
- acceptance criteria — мост между intent and evidence.

### Почему это важно

Сейчас Part III может стать слишком specification-heavy. После Stage 0.5–0.9 нужно показать, что specification — центральный, но не единственный артефакт intent layer. ADR and traceability carry different meaning.

### Что не делать

Не расписывать каждый artifact deeply здесь. Часть III должна дать различение, а deep treatment распределяется дальше.

## Часть IV. SPDD

### Что оставить

SPDD остаётся standalone deep anchor. Никаких сокращений, никакого переноса в Part III.

### Что уточнить

Показать SPDD как один полный вариант связанного артефактного контура:

```text
story shaping → analysis context → REASONS Canvas → generation → API tests → review → prompt update → sync → asset integrity
```

Важно: SPDD не просто “prompt как artifact”. Его сила в том, что он связывает намерение, генерацию, проверку and обновление intent artifact.

### Что не добавлять

Не добавлять в SPDD все новые artifact topics. SBOM, CODEOWNERS, feature flags, OPA etc. не должны размыть SPDD. Они появятся в других частях.

## Часть V. Соседние спецификационные режимы

### Что добавить

Показать, что Part V раскрывает разные формы спецификационного управления:

- Spec Kit — toolkit/ecosystem;
- Kiro — продуктовая поверхность спецификации внутри IDE;
- TDAD Agent Definition — поведение агента как тестируемый/собираемый артефакт;
- TDAD Agentic Development — code-test graph as agent skill;
- Constitutional SDD — security/governance constraints as specification.

### Как встроить новые Stage 0.7–0.9 материалы

- API/data contracts mention as neighboring boundary artifacts, not new deep method.
- Traceability mention as connection to evidence, not separate method.
- Policy-as-code connects to Constitutional SDD, but belongs later in execution/governance.

### Что не делать

Не добавлять GSD/BMAD сюда как “ещё два спецификационных режима”. Они принадлежат process/framework layer.

## Часть VI. Контекст и рабочее состояние: проект как интерфейс агента

### Что добавить подробно

Эта часть должна стать местом, где новые материалы особенно полезны:

1. `research.md` and `plan.md` as lightweight state artifacts.
2. Handoff and progress log as continuity artifacts.
3. ADR as project memory, not just architecture record.
4. Context files: `AGENTS.md`, Cursor rules, Agent READMEs.
5. Codebase readiness: tests, CI, metrics, instructions, observability.
6. Reproducible environment as condition for evidence.
7. Software catalog / ownership metadata as navigation surface.

### Главная мысль

Проект становится интерфейсом агента не потому, что в нём есть много документов. Он становится интерфейсом, когда агент может понять:

- где он действует;
- какие правила действуют;
- что уже решено;
- что можно запускать;
- кто владеет областью;
- как проверить изменение;
- как передать состояние дальше.

### Риск

Эта часть может распухнуть. Поэтому не делать deep sections for every artifact. GSD can be medium case; Agent README/AGENTS.md can be supporting evidence.

## Часть VII. Делегирование: выбор режима работы, а не выбор инструмента

### Что добавить

Добавить process/framework layer as medium section:

```text
Когда процесс становится устанавливаемым артефактом
```

Материалы:

- GSD / Open GSD — внешнее состояние, свежий контекст, малые планы, verify step.
- BMAD — роли, специализированные агенты, guided workflow.
- OpenSpec / AgentSPEX — workflow specification and portability.
- Reversa — recovery of operational specs from legacy.

### Как писать

Не “GSD, BMAD, OpenSpec, Reversa” как список. Написать через вопрос:

```text
Когда локальных документов и ручного выбора режима уже мало, процесс начинают устанавливать как повторяемую схему: роли, файлы состояния, workflow, проверки and handoff.
```

### Что не делать

Не превращать Part VII в новый каталог frameworks. Medium section only until dossiers justify more.

## Часть VIII. Исполнение: среда агента, harness, tools, permissions

### Что добавить

Исполнение должно описывать не только tool access, but control surface:

- sandbox;
- permissions;
- worktree;
- dev container / reproducible environment;
- MCP/tool boundary;
- secret scanning / credential inventory;
- policy-as-code;
- agent workflow specification;
- agent trace/tool-call log.

### Связь с источниками

- HumanLayer, Jesse Vincent, Mike McQuaid, Matt Pocock stories already support harness/skills/hooks/worktrees.
- Stage 0.7–0.9 add formal artifacts: policy-as-code, reproducible environment, agent trace, secrets boundary.

### Главная мысль

Среда исполнения должна не только дать агенту возможность действовать, но и ограничить, воспроизвести, записать and проверить его действие.

## Часть IX. Gas Town

### Что оставить

Gas Town остаётся standalone deep anchor and must start from old-site seed.

### Что уточнить

Stage 0.9 помогает лучше объяснить Gas Town: это не просто много агентов, а artifact graph / organizational platform.

- Beads — task memory and control layer.
- Mayor — visibility/control surface.
- Roles — organizational functions.
- GUPP/hooks/molecules/wisps — workflow continuity.
- Witness/Deacon/Refinery — service-agent maintenance.
- Cost — coordination and verification burden.

### Что не делать

Не добавлять unrelated Stage 0.5–0.9 artifacts into Gas Town just because they fit semantically. Gas Town should stay detailed but focused.

## Часть X. Свидетельства, тесты, ревью and benchmark validity

### Что добавить подробно

Part X should become “evidence package” theory.

Evidence package may include:

- unit/integration/API tests;
- contract tests;
- CI logs;
- benchmark results;
- traceability links;
- PR description;
- review comments;
- agent trace/tool-call log;
- policy check results;
- security review outputs;
- SBOM/provenance evidence;
- reproducible build evidence.

### Главная мысль

Тип свидетельства зависит от типа изменения. Нельзя требовать один и тот же proof package for UI tweak, migration, security-sensitive change, API contract change, refactor or agent workflow change.

### Связь с историями

Simon Willison, Arvid Kahl, Jökull Sólberg, Jesse Vincent and HumanLayer all support evidence as something produced by workflow, not by final summary.

## Часть XI. Завершение, governance и внешний контур

### Что добавить

Добавить concrete completion artifacts:

- CODEOWNERS;
- ownership map;
- review routing;
- escalation path;
- protected branch;
- required review;
- release authority;
- audit/provenance record.

### Главная формула

```text
право исполнять ≠ обязанность ревьюить ≠ право сливать ≠ право выпускать
```

### Связь с источниками

Open-source policy cluster remains the boundary anchor. GitHub/GitLab/Kubernetes ownership sources add concrete artifacts.

### Что не делать

Не растворять governance into generic “security and responsibility”. The key is completion right.

## Часть XII. Хвост lifecycle: сопровождение, долг и обучение среды

### Что добавить

Part XII needs controlled tail, not dumping ground.

Clusters:

1. Release and operational control:
   - release plan;
   - feature flags;
   - canary rollout;
   - migration plan;
   - rollback plan;
   - runbook.

2. Learning and repair:
   - incident report;
   - postmortem;
   - stale ADR;
   - context file cleanup;
   - prompt/context regression;
   - observability debt.

3. Supply-chain and security tail:
   - SBOM;
   - dependency/license inventory;
   - secret rotation;
   - credential follow-up;
   - provenance record.

4. Communication:
   - changelog;
   - release notes;
   - traceability to PR/issues/contracts.

### Главная мысль

Merge не завершает AI-driven SDLC. Завершение временно: изменение уходит в сопровождение, а сопровождение возвращает исправления в specs, tests, policies, context files, skills, hooks and gates.

### Что не делать

Не делать Part XII такой же большой, как SPDD/Gas Town. Она должна замыкать цикл, а не становиться эксплуатационным handbook.

## 7. Что именно должно измениться в approved plan

### Добавить в раздел 0

Новый пункт 0.9:

```text
0.9. Артефакты жизненного цикла становятся first-class objects

Новая теория должна отслеживать не только стадии AI-driven SDLC и кейсы, но и артефакты, которые переносят программное изменение между стадиями: намерение, контекст, решение, среду исполнения, свидетельства, право завершения и сопровождение. Артефакт получает место в основной теории только если он выполняет функцию в жизненном цикле изменения.
```

### Изменить план частей

Не менять список частей, но добавить notes into relevant parts:

- Part I — artifact selection rule.
- Part III — artifact distinctions.
- Part VI — project/interface readiness.
- Part VII — process/framework layer.
- Part VIII — execution control surface.
- Part X — evidence package.
- Part XI — completion artifacts.
- Part XII — lifecycle tail clusters.

## 8. Что должно остаться в source map only

Не выносить в основной текст как самостоятельные sections:

- Backstage;
- OPA / Kyverno / InSpec;
- ChainForge;
- Nix/Bazel/Reproducible Builds;
- AgentSPEX/Open Agent Specification;
- SBOM tool ecosystem details;
- Spec Kitty;
- most vendor/news sources;
- every individual empirical paper from Stage 0.5–0.9.

Они нужны как поддержка, но не как структура.

## 9. Минимальный набор dossiers before drafting

Если patch принят, не делать 20 одинаковых dossiers. Нужно 7–8 targeted files:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_AND_TRACEABILITY_NOTE.md
work/dossiers/EXECUTION_CONTROL_SURFACES_NOTE.md
work/dossiers/EVIDENCE_PACKAGE_TAXONOMY_NOTE.md
work/dossiers/LIFECYCLE_TAIL_ARTIFACTS_NOTE.md
work/dossiers/OWNERSHIP_AND_COMPLETION_ARTIFACTS_NOTE.md
```

SPDD and Gas Town dossiers remain separate and governed by baseline restore rule.

## 10. Recommended decision

Принять patch, но с ограничителями:

1. Не добавлять новые top-level parts.
2. Не делать новых deep anchors.
3. Не раздувать Part XII.
4. Обновить approved plan before drafting.
5. Создать only selected dossiers/notes.
6. После этого перейти к skeleton and writing.

## 11. Следующий шаг после принятия

Если пользователь принимает этот patch, следующий архив должен содержать:

```text
work/approved-ai-sdlc-plan.md
work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md
work/discourse.md
work/reports/APPROVED_PLAN_PATCH_APPLIED.md
```

Если пользователь хочет правки, сначала уточнить scope.

## 12. Интеграция Stage 0.12: архитектурные качества и тестовая среда

Stage 0.12 проверил два оставшихся сильных кандидата на пропуск: **architecture quality / fitness functions** and **test data / test environments**. Оба подтвердились как настоящие patch items. Они не требуют новых верхнеуровневых частей, но должны быть явно внесены в approved plan как named medium-high subsections.

### 12.1. Почему architecture quality не сводится к ADR, spec или tests

Архитектурные качества занимают отдельное место:

- ADR фиксирует принятое архитектурное решение и его причины.
- Спецификация фиксирует желаемое поведение and constraints.
- Тесты проверяют наблюдаемое поведение.
- Quality attribute scenario формулирует качество, которое архитектура должна сохранять.
- Fitness function / architecture test делает часть этого качества проверяемой.
- Tradeoff analysis показывает, где качества конфликтуют.

Для AI-driven SDLC это важно потому, что агент может внести локально корректный diff, который постепенно разрушает архитектурную форму: нарушает слойность, вводит нежелательную зависимость, создаёт цикл, ухудшает модифицируемость, обходит boundary, вредит deployability or violates an architectural decision. Обычные unit tests могут при этом оставаться зелёными.

### 12.2. Что добавить в классы артефактов

В класс “Артефакты намерения и решения” добавить:

```text
quality attribute scenario
architecture constraint
tradeoff / risk record
```

В класс “Артефакты среды исполнения и ограничений” добавить:

```text
architecture fitness function
architecture test
layer/dependency/cycle rule
```

В класс “Артефакты свидетельства и проверки” добавить:

```text
architecture fitness result
architecture test output
tradeoff review result
```

В класс “Артефакты завершения и хвоста lifecycle” добавить:

```text
architecture drift
stale fitness function
architecture-test maintenance
```

### 12.3. Куда встроить architecture quality в структуру

В **Part III** добавить короткое различение: quality attribute scenario and architecture constraint are not ordinary requirements and not ADR. They express durable qualities the architecture must preserve.

В **Part VIII** добавить architecture fitness functions and architecture tests as executable constraints in the agent environment.

В **Part X** добавить named subsection:

```text
Архитектурные качества как проверяемые ограничения
```

Эта подглава должна покрыть:

- quality attribute scenarios;
- tradeoffs and sensitivity points;
- architecture fitness functions;
- architecture tests;
- layer/dependency/cycle rules;
- limits of automated checks;
- human architectural judgment.

В **Part XII** добавить architecture drift, stale fitness functions and fitness-function maintenance.

### 12.4. Почему test data / test environments не являются мелкой тестовой деталью

Evidence package weakens if it does not say:

- какие данные использовались;
- как они были подготовлены;
- откуда взяты fixtures/seeds;
- насколько окружение похоже на нужный execution context;
- какие зависимости были реальными, виртуализированными or контейнеризованными;
- кто создал oracle;
- не сгенерировала ли модель одновременно код, тесты, данные and interpretation.

В AI-driven SDLC есть особый риск:

```text
агент генерирует код →
агент генерирует тесты →
агент генерирует тестовые данные →
агент интерпретирует результат
```

Если источник тестов, данных and oracle too tightly coupled to the same model assumptions, evidence может выглядеть сильным and still fail to prove the intended behavior.

### 12.5. Что добавить в классы артефактов

В класс “Артефакты намерения и решения” добавить:

```text
test oracle assumption
data representativeness requirement
```

В класс “Артефакты среды исполнения и ограничений” добавить:

```text
controlled test environment
test dependencies as code
service virtualization
environment identity
```

В класс “Артефакты свидетельства и проверки” добавить:

```text
test data source
fixture / seed state
synthetic data note
masked production-like data note
oracle provenance
independent validation of generated tests
```

В класс “Артефакты завершения и хвоста lifecycle” добавить:

```text
test data drift
stale fixtures
test environment drift
test data privacy cleanup
```

### 12.6. Куда встроить test data / test environments в структуру

В **Part VIII** добавить controlled test environment, service virtualization and test dependencies as code as parts of execution environment.

В **Part X** добавить named subsection:

```text
Тестовые данные, тестовая среда и независимость оракула
```

Эта подглава должна покрыть:

- test data management;
- fixtures, seeds and generated data;
- masked production-like data;
- synthetic data and its verification;
- service virtualization;
- Testcontainers-style dependencies as code;
- generated tests and generated test data;
- oracle independence;
- environment identity in evidence package.

В **Part XII** добавить test data drift, stale fixtures, test environment drift and test data privacy cleanup.

### 12.7. Как это меняет минимальный набор dossiers/notes

Минимальный набор после Stage 0.12 становится таким:

```text
work/dossiers/ADR_DECISION_PROVENANCE_DOSSIER.md
work/dossiers/GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md
work/dossiers/CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md
work/dossiers/API_DATA_CONTRACTS_AND_TRACEABILITY_NOTE.md
work/dossiers/EXECUTION_CONTROL_SURFACES_NOTE.md
work/dossiers/ARCHITECTURE_QUALITY_AND_FITNESS_FUNCTIONS_NOTE.md
work/dossiers/TEST_DATA_ENVIRONMENTS_AND_ORACLES_NOTE.md
work/dossiers/EVIDENCE_PACKAGE_TAXONOMY_NOTE.md
work/dossiers/LIFECYCLE_TAIL_ARTIFACTS_NOTE.md
work/dossiers/OWNERSHIP_AND_COMPLETION_ARTIFACTS_NOTE.md
```

SPDD and Gas Town dossiers остаются отдельными and governed by baseline restore rule.

### 12.8. Human gate после Stage 0.12

Перед обновлением `work/approved-ai-sdlc-plan.md` пользователь должен отдельно подтвердить, что два блока принимаются как named medium-high subsections:

1. `Архитектурные качества как проверяемые ограничения`.
2. `Тестовые данные, тестовая среда и независимость оракула`.

По умолчанию они не становятся новыми top-level parts and not deep anchors.
