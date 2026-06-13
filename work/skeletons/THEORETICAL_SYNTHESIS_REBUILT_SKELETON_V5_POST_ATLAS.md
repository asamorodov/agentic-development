# Скелетон пересборки теоретического синтеза — v5 post-atlas

Статус: рабочий скелетон для написания глав после завершения concept-first Атласа.  
Основание: `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`, `00_spine_map`, готовые A/B/C-фрагменты, десять статей Атласа, досье, story corpus, последние решения по technical anchoring и стилю.

V4 остаётся историческим baseline. V5 не переписывает теорию с нуля. Его задача — перевести скелетон из предатласного режима в post-atlas режим: главы теперь пишутся не только по досье и старому skeleton, а по skeleton, A/B/C-фрагментам, Атласу, досье и внешнему source discovery там, где материал ещё недоразработан.

## Главная ось

Агентская разработка меняет не только способ писать код. Она меняет жизненный цикл программного изменения: от формулировки намерения и границ задачи до устойчивого состояния работы, проверки результата, принятия решения, восстановления после сбоев и передачи контекста между сессиями, людьми и агентами.

Единица анализа — не prompt и не diff, а изменение, которое должно пройти через проект и оставить после себя согласованное состояние: код, спецификации, решения, тесты, правила, рабочие графы, evidence и хвост сопровождения.

## Источниковый контракт для глав

Будущая глава не должна выбирать один главный источник на все случаи. У каждого слоя своя власть.

1. **`00_spine_map`, Skeleton V5 и CORE plan** задают композицию, термины и границы.
2. **A/B/C-фрагменты** дают существующий синтез. Их нужно читать как материал главы, а не как черновики, которые можно забыть.
3. **статьи Атласа** дают отполированный concept-first baseline по конкретным методам и механизмам.
4. **Досье** дают полный quarry: source details, failure modes, visual candidates, отложенные различения, материал, который был слишком подробен для Атласа.
5. **Внешние источники** работают не только как подтверждение и картинки. Для недоразработанных глав они дают содержание: новые термины, документы, диаграммы, исследования, контраргументы, практики и сравнительные рамки.
6. **Истории** используются как адресные практические якоря. Теория не пересказывает story corpus.

## Методологический контракт

### Глубокие опорные узлы

Три глубоких узла сохраняются:

- **SPDD** — спецификационный жизненный цикл: намерение, анализ, structured prompt, code generation, review, sync, prompt update, reverse reconstruction for legacy code.
- **Persistent Work Graph** — устойчивое состояние работы: объект работы, зависимости, ready/blocked, owner/claim, gate, evidence, prime/rehydration, source state, recovery.
- **Gas Town / Beads** — организационно-операционный жизненный цикл: роли как функции, двухслойные Beads, service agents, state vocabulary, backpressure и координацию работы многих агентов.

Эти узлы не должны превращаться в пересказ статей Атласа. В главе они используются для общей теории жизненного цикла изменения.

### Защищённые профили

Защищённые профили остаются обязательными, но не требуют одинаковой глубины в каждой главе:

- **Spec Kit** — переносимый specification toolkit и constitution-driven feature flow.
- **Kiro Specs** — продуктовая IDE-поверхность спецификаций, requirements/design/tasks, supervised execution.
- **Constitutional SDD** — constitution как спецификационный слой более высокого порядка, traceability matrix, security/human checkpoints.
- **TDAD** — два разных значения test-driven agentic work: agent definition и regression-oriented code-agent development.
- **GSD / Open GSD** — process-runtime profile: planning artifacts, phase state, routing, model/security policy, recovery.
- **BMAD** — role-based guided process: story, sprint status, checkpoint preview, correct-course, brownfield и ретроспективу.
- **ADR** — защищённый профиль памяти решений: proposed/accepted/rejected/superseded, confirmation, reconstructed ADR как candidate-запись, Design Decision Gate.

## Введение. Почему речь не о генерации кода

**Задача.** Ввести смену масштаба: от разговора про генерацию кода к жизненному циклу программного изменения.

**Что должно быть видно.** Код — важный, но не единственный результат. В агентской разработке особенно часто ломаются не строки, а переходы: намерение не стало спецификацией, спецификация не стала рабочим состоянием, рабочее состояние не получило evidence, evidence не дошло до человеческого принятия, после merge не обновились правила и память проекта.

**Главные входы.** `00_spine_map`, A1, A10, Cross-story synthesis, Атлас как завершённый baseline.

**Риск.** Не писать общее вступление про AI. Введение должно сразу показать, почему старая единица `prompt → code` слишком мала.

# I. Единица анализа: программное изменение, а не prompt

**Управляющий тезис.** Prompt — только вход в модель. Теория должна описывать изменение, которое проходит через намерение, решение, рабочее состояние, исполнение, свидетельства, принятие и сопровождение.

**Что раскрыть.**

- отличие prompt / task / diff / change;
- почему conversational coding работает только при малом радиусе и близкой проверке;
- когда внешний носитель становится необходимым;
- почему «модель поняла» не равно «проект сохранил смысл изменения».

**Atlas donors.** SPDD, Spec Kit, Kiro, BMAD.

**Dossier gap-check.** Сравнить, не потеряны ли в досье сильные различения про малый радиус, plan/research/implement, внешнюю память и story/state artifacts.

**External discovery.** Обычно не основной источник. Может понадобиться только для формального различения task/change/workflow, если глава станет слишком внутренней.

# II. Реальная агентская сессия: трасса, вмешательство, выживание результата

**Управляющий тезис.** Сессия — локальное исполнение, а не надёжная память изменения. Наблюдения, логи, transcript, browser state, PR-комментарии и ошибки консоли помогают управлять агентом, но сами не образуют устойчивое состояние.

**Что раскрыть.**

- trace как наблюдение;
- session как локальный контекст исполнения;
- человеческое вмешательство как steering и triage;
- что должно пережить сжатие контекста, handoff, обрыв и смену агента;
- why external work state becomes necessary.

**Внутренние входы.** A1, A6, A7, Cross-story synthesis, Simon Willison, Arvid Kahl, Jökull Sólberg, HumanLayer, Mark Erikson, Armin Ronacher.

**External source discovery.** Обязателен, если глава опирается на SWE-chat, Programming by Chat, How Coding Agents Fail, transcript analysis, таксономии agent traces или классификации сбоев coding agents. Эти источники должны давать содержание, а не только цитаты.

# III. Намерение, спецификация, контракт и архитектурное решение

**Управляющий тезис.** Specification, contract и ADR отвечают за разные вещи. Спецификация задаёт ожидаемое изменение и границы; contract фиксирует проверяемое ожидание; ADR хранит решение, статус, последствия и путь замены.

**Что раскрыть.**

- specification как рабочая поверхность для агента;
- contract как узкое проверяемое обещание;
- ADR как память решения;
- `Confirmation` как мост к evidence;
- Design Decision Gate как пример: LLM готовит черновик или сигнал, но завершение решения остаётся человеческим действием;
- generated/reconstructed ADR как candidate-запись до принятия.

**Atlas donors.** ADR, SPDD, Spec Kit, Constitutional SDD.

**Dossier gap-check.** MADR, AWS ADR lifecycle, AgenticAKM, Mneme, cADR, Vercel ADR skill и исследования generated ADRs.

**External discovery.** Нужен для claims об ADR-практике, architecture fitness / confirmation, CODEOWNERS / governance и AI-generated decision records, если они не покрыты Атласом достаточно хорошо.

# IV. SPDD как спецификационный жизненный цикл

**Управляющий тезис.** SPDD — не техника «лучше промптить», а способ сделать намерение видимым, проверяемым и синхронизируемым с кодом.

**Что раскрыть.**

- Fowler/Thoughtworks SPDD как концептуальную рамку;
- REASONS Canvas как структурированный носитель намерения;
- OpenSPDD как операционализацию через команды и шаблоны;
- три человеческих навыка: `Abstraction First`, `Alignment`, `Iterative Review`;
- billing example с числовыми anchors как показатель требуемого уровня evidence;
- `/spdd-reverse` как обратный вход для legacy-кода: candidate Canvas, а не исходное намерение;
- prompt update / sync как хвост жизненного цикла.

**Atlas donor.** `spdd_method.md` — concept baseline. Детали отдельных команд остаются в Атласе, если не несут аргумент главы.

**Dossier gap-check.** Использовать досье только для восстановления недостающих концептуальных деталей, а не для повторного расширения каталога команд.

# V. Защищённые спецификационные профили

**Управляющий тезис.** Specification может стать управляемой поверхностью жизненного цикла разными способами. Глава должна сравнить, что именно каждый профиль делает устойчивым, а не перечислять все команды.

**Профили.**

- Spec Kit — feature lifecycle через specify/clarify/plan/tasks/analyze/implement и constitution.
- Kiro Specs — product-native spec state: Feature Specs, Bugfix Specs, Quick Plan, Analyze Requirements, design/tasks и supervised execution.
- TDAD — tests как agent definition vs tests как regression route для code-agent work.
- Constitutional SDD — constitution как спецификационный слой более высокого порядка, traceability matrix, security и human checkpoints.

**Что синтезировать.**

- что именно становится specification object;
- как это проходит ревью;
- как из этого выводятся tasks;
- где rules/constitution/policy ограничивают generation;
- какой failure mode предотвращает профиль;
- где профиль становится слишком тяжёлым.

**External discovery.** Нужен, когда профиль опирается на текущую документацию или быстро меняющиеся продуктовые возможности. Сначала использовать official docs и первичные repos.

# VI. Контекст и рабочее состояние: проект как интерфейс агента

**Управляющий тезис.** Context — это не просто tokens. В агентской работе проектные файлы, rules, specs, skills, state files и process artifacts становятся интерфейсом, через который агент понимает, что ему можно делать.

**Что раскрыть.**

- context file vs rule vs skill vs steering vs story vs state file vs work graph;
- project context как state-bearing surface;
- provenance of behavior: откуда взялось правило агента и кто может его менять;
- limits of stuffing more context into the prompt;
- bridge to PWG.

**Atlas donors.** Kiro, Spec Kit, GSD, BMAD, SPDD, PWG.

**External discovery.** Вероятно нужен: документация Codex/Claude по AGENTS.md, skills, hooks, MCP, subagents, project rules, steering и context management. Это content discovery, а не украшение ссылками.

# VII. Persistent Work Graph как устойчивый граф работы

**Управляющий тезис.** Работе нужно устойчивое состояние до исполнения, во время исполнения и после него. PWG хранит, что существует, что готово, что заблокировано, кто владеет работой, какие evidence нужны и как работу можно продолжить.

**Что включить.**

- почему сессии и markdown-заметки недостаточны;
- work item как долговечный объект;
- dependencies и ready queue;
- owner/claim/lock/pin;
- gate как долговечное ожидание с четырьмя полями: blocked transition, unblocker, evidence после снятия блокировки, fallback при сбое, тайм-ауте или ручном обходе;
- `bd ready` и `bd blocked` как конкретные anchors;
- `bd prime` как компактный restart context после сжатия контекста;
- source-state line: `found → opened → read → used_in_main_text / used_in_source_register / candidate_image_only / rejected_with_reason / reopen_required`;
- recovery и cleanup.

**Atlas donor.** `persistent_work_graph.md` is the concept baseline.

**Boundary.** PWG — не issue tracker, не execution runtime, не CRDT, не transcript и не project rules. Он может использовать эти носители, но хранит состояние продолжения работы.

# VIII. Защищённые процессные профили

**Управляющий тезис.** Некоторые методы не просто специфицируют feature; они оборачивают разработку в process profile, который говорит агентам и людям, какая сейчас роль, фаза, артефакт, checkpoint и recovery move.

**Профили.**

- GSD/Open GSD — process-runtime profile: `.planning/`, `gsd-core`, `gsd-pi`, routing, model/security policy, phase state, verification and recovery.
- BMAD — role-based guided process: story, `sprint-status.yaml`, checkpoint preview, `bmad-correct-course`, brownfield mode, retrospective/investigation.
- Лёгкие соседи — Reversa/OpenSpec/AgentSPEX — используются только если external discovery или Атлас показывают, что они действительно нужны.

**Что синтезировать.**

- process profile vs specification;
- process profile vs PWG;
- process profile vs Gas Town;
- когда процесс становится артефактом;
- когда process overhead превышает риск.

# IX. Исполнение: среда агента, harness, tools, permissions

**Управляющий тезис.** Действие агента ограничено средой, инструментами и правами. Runtime может исполнять и наблюдать, но он не хранит автоматически смысл работы и authority принятия.

**Четыре слоя.**

1. граница исполнения: sandbox, worktree, devbox, permissions, protected user;
2. поверхность инструментов и наблюдения: browser, logs, DOM, database, CLI, test harness;
3. workflow runtime / durable execution: replay, возобновление, timers, orchestration;
4. platform agent / internal developer platform: devbox, PR integration, policy, organizational control.

**Внутренние доноры.** A6, C4, PWG, Gas Town, GSD, BMAD, story corpus.

**External discovery.** Обязателен. Вероятные источники: LangGraph, Temporal, DBOS, Restate, HumanLayer, Sandvault, Codex/Claude docs, MCP/hook/subagent docs, platform-agent case studies. Глава не должна стать списком инструментов. Её настоящий вопрос: что делает действие агента ограниченным, воспроизводимым, наблюдаемым, возобновляемым и подотчётным.

# X. Gas Town / Beads как организационно-операционный жизненный цикл

**Управляющий тезис.** Gas Town показывает, что происходит, когда многим агентам нужны организация, backpressure, maintenance loops и handoff. Это PWG плюс операционная культура, а не просто граф задач.

**Что включить.**

- роли как функции жизненного цикла, а не забавные имена;
- two-tier Beads: town-level coordination vs rig-level execution;
- словарь проблемных состояний: `Working`, `Stalled`, `Zombie`, `GUPP Violation`, `FIX_NEEDED`, `MERGE_FAILED`, `ORPHANED_WORK`;
- service agents: Witness, Refinery, Deacon/Dogs;
- mail, patrols, queues и словарь статусов как control surfaces;
- граница: не превращать главу в экскурсию по UI Gas Town.

**Atlas donor.** `gas_town.md` с patched visual assets — concept baseline.

# XI. Свидетельства, тесты, ревью и качество доказательства

**Управляющий тезис.** Решающим становится не вопрос, произвёл ли агент output, а вопрос, каких evidence достаточно, чтобы человек или организация приняли изменение.

**Организовать раздел по типам обещаний, а не по типам инструментов.**

- behavior evidence;
- boundary/contract evidence;
- architectural confirmation;
- security/governance traceability;
- runtime/rollout evidence;
- human/maintainer acceptance.

**Atlas donors.** SPDD (`/spdd-api-test`, `/spdd-code-review`), ADR (`Confirmation`, Pact/can-i-deploy, OAS diff, SLO/rollout), TDAD, Constitutional SDD, Kiro, GSD, BMAD.

**External discovery.** Нужен для contract testing, architecture fitness functions, rollout/SLO/error-budget, replay/trace sources и исследований review/verification.

# XII. Завершение, управление ответственностью и внешний контур

**Управляющий тезис.** Право действовать и право завершать — разные вещи. Агент может выполнять шаги, но принятие результата остаётся у человека, команды, maintainer policy или governance layer.

**Что включить.**

- right to act vs right to complete;
- ADR status и decision authority;
- CODEOWNERS и maintainer policies;
- open-source AI contribution policies;
- platform-agent PR completion и human gates;
- false completion и evidence laundering.

**External discovery.** Нужен для open-source AI policies, CODEOWNERS, maintainer trust cost, security/sandbox policies и enterprise acceptance gates.

# XIII. Хвост жизненного цикла: сопровождение, долг и обучение среды

**Управляющий тезис.** Merge закрывает путь кода, но не обязательно жизненный цикл. Если окружающие артефакты остаются устаревшими, следующий агент начинает из ложного состояния проекта.

**Что включить.**

- SPDD `prompt-update` / `sync`;
- ADR supersession и устаревание operational projection;
- constitution/spec update после incident/regulatory changes;
- Spec Kit / Kiro tasks и specs после implementation;
- GSD/BMAD state cleanup, retrospective и correct-course;
- PWG cleanup: stale deps, obsolete gates, orphaned claims;
- skills/rules/hooks/AGENTS updates.

**External discovery.** Нужен, если глава расширяется до incident feedback, supply-chain/dependency inventory, SBOM, practices обновления policy/rules или platform memory maintenance.

# Заключение. Не карта кейсов, а карта выбора режима

**Управляющий тезис.** Финальная рамка не должна ранжировать методы по «продвинутости». Она должна помогать выбрать минимальную внешнюю структуру, которая при данном риске сохраняет intent, state, evidence, authority и repair.

**Что включить.**

- when chat/diff is enough;
- когда specification должна стать артефактом;
- when work needs PWG;
- when process profile is necessary;
- when Gas Town-like organization becomes useful;
- when ADR/constitution/evidence gates are mandatory;
- сигналы недостаточной структуры и избыточного процесса.

**Inputs.** A10, статьи Атласа, all A/B/C fragments.

# Приложение. Post-atlas concept-first Atlas

Атлас достаточно завершён, чтобы служить baseline для написания теории. В нём десять canonical articles:

1. `spdd_method.md`
2. `persistent_work_graph.md`
3. `gas_town.md`
4. `adr_method.md`
5. `spec_kit_method.md`
6. `kiro_specs.md`
7. `constitutional_sdd.md`
8. `tdad_comparative.md`
9. `gsd_open_gsd.md`
10. `bmad_method.md`

Внешним ассетам всё ещё нужен общий asset-pass. Это не блокирует написание глав, если глава не зависит от конкретного визуального утверждения.

Use rule:

```text
Read the relevant Atlas article before writing a chapter section that uses that concept.
После этого использовать досье для gap-check, а не как первую поверхность черновика.
Use external sources for content discovery when internal material is thin.
```

# Heavy chapter package model

Chapter packages должны быть тяжёлыми. Они синтезируют несколько готовых артефактов и иногда требуют нового внешнего исследования. Стартовая форма package:

```text
P01 — read discourse, map, Skeleton V5, 00, CORE plan
P02 — section contract: что глава должна доказать и чем не должна стать
P03 — existing-fragment inventory: A/B/C и связанные фрагменты
P04 — atlas donor map: primary, secondary и control atlas articles
P05 — dossier gap map: what important material exists outside Atlas/fragments
P06 — content gap map: где главе не хватает содержания даже после внутренних источников
P07 — external source discovery pass, если есть gaps
P08 — source unfolding pass: прочитать найденные источники и пройти по важным ссылкам, diagrams и repos
P09 — integration decision: what enters chapter, what stays in source register, what is future debt
P10 — first synthesis draft
P11 — anti-catalog pass: пересобрать вокруг аргумента главы, а не вокруг списка методов
P12 — cross-article consistency pass against Atlas и 00
P13 — source/provenance pass
P14 — chapter repair: structure, transitions, boundaries with neighbor chapters
P15 — language pass 1
P16 — language pass 2
P17 — style defect audit
P18 — selective natural rewrite
P19 — guarded final human technical style
P20 — regression check: no loss of critical distinctions, technical anchors, source obligations
Final — package chapter, companion files, source register, open questions, discourse/map updates
```

Глава с тяжёлым external discovery может потребовать больше source-проходов. Глава, почти закрытая Атласом и A/B/C-фрагментами, может потребовать меньше. Процесс регулируется явным section contract, а не скрытой компрессией.

# Anti-degradation checks

Before accepting a chapter, check:

- Does it serve the lifecycle-of-change axis?
- Does it avoid becoming an Atlas table of contents?
- Does it use existing A/B/C fragments rather than ignore them?
- Использует ли она Атлас как concept baseline, не копируя каждую статью?
- Does it use dossiers for gap-check without restoring coverage bureaucracy?
- Запускает ли она external discovery там, где содержание главы действительно тонкое?
- Сохраняет ли она SPDD, PWG и Gas Town как deep anchors?
- Сохраняет ли она ADR как профиль decision-memory / authority?
- Does it preserve natural Russian style?
- Does it name future debts instead of hiding them behind smooth synthesis?
