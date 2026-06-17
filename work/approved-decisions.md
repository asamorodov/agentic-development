# Approved decisions

## 1. Master title / frame

Approved working title:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения**

The phrase AI-driven SDLC must be interpreted as lifecycle-of-change architecture, not as a banal corporate phase list.

## 2. New architecture replaces the “map of currents” top-level structure

The earlier “map of currents” idea remains valuable, but it is demoted from document architecture to analytical/source-map layer. It must not produce a flat catalogue of cases.

## 3. SPDD is a separate part

SPDD is no longer a deep block inside a general “intent” part. It is now a separate part because it is the strongest known methodology-level specification case in the corpus.

## 4. Specification zone is deep

The specification zone consists of:

- Part III — why prompt is too weak as a governance unit;
- Part IV — SPDD as specification lifecycle;
- Part V — Spec Kit, Kiro, TDAD, Constitutional SDD as neighboring deep specification regimes.

Spec Kit, Kiro, TDAD and Constitutional SDD should be treated deeply. They are not throwaway contrast cases.

## 5. Gas Town / Beads is a separate part

Gas Town must return to a full deep case status. The previous compression into one subsection is considered a structural degradation. Gas Town is the deep anchor for organizational/operational lifecycle: roles, Mayor, Beads, durable task state, hooks/GUPP/molecules/wisps, service agents, work identities and the cost of orchestration.

## 6. Baseline restoration rule for SPDD and Gas Town

For SPDD and Gas Town, start from the old site baseline sections unchanged. Then adapt and supplement them. Do not start from the latest expanded synthesis. Do not compress details.

## 7. Expanded theory is quarry, not authority

The latest expanded synthesis is useful for facts, links, source coverage and material. It is not authoritative as prose or structure.

## 8. Source search state

A targeted AI-SDLC source expansion was already done. No new mass source search is required now. Additional search should be targeted only at discovered gaps.

## 9. Codex role

Codex should not be allowed to “just rewrite the theory.” Its role is controlled workflow execution: inventory, dossiers, skeleton, draft rebuild, anti-catalog audit, source-depth repair and anti-degradation checks.

## 10. Human role

The human owner keeps architectural decisions and semantic gates. Human work should not be reduced to manually launching repeated passes or checking file counts.


## 11. Technical atlas is чтение от конкретной концепции

Технический атлас больше не трактуется как узкое приложение для технических деталей. Он становится концептуально-техническим слоем: самостоятельным набором статей с опорой на источники по конкретным концепциям и методологиям. Контролируемое повторение с теорией допустимо, если нужно для самостоятельного понимания статьи атласа. Теория остаётся поперечным SDLC-синтезом; атлас даёт путь чтения от конкретной концепции и не должен становиться ни копией общей теории, ни складом несвязанных деталей.

## 12. Единый корпус знаний и разные разрезы частей

Теория, Атлас, Handbook и Fieldbook работают на одном корпусе знаний по agentic development / AI-driven SDLC, но используют разные организующие разрезы. Теория строится по жизненному циклу изменения; Атлас — по техническим слоям и конкурирующим способам их построения; Handbook — по решениям, которые принимает практик; Fieldbook — по типовым сбоям, диагностике и восстановлению.

Это решение зафиксировано в `work/decisions/ADR-0012-shared-knowledge-genre-cuts.md`. Каждый будущий пакет должен явно указывать не только тему, но и жанр/разрез. Хороший текст, написанный в неверном разрезе, не считается принятым результатом для своей части.

## 13. Git/version-control слой — отдельная статья Атласа

Git и Git-совместимый workflow считаются практической базой современной агентской разработки: branches, worktrees, commits, diffs, patches, PR/MR, review state, merge/revert/rollback и связанные платформенные поверхности образуют основной change-substrate, на который опираются coding agents и review tooling. Это не означает, что другие VCS или Git-compatible слои невозможны, но Атлас и Handbook должны явно показывать, как они соотносятся с Git/PR/CI/review контуром.

В текущем корпусе Git покрыт как внутренний протокол проекта, но недостаточно покрыт как самостоятельный слой agentic development. Решение: сделать отдельную статью Атласа `Git, worktree и PR/MR как субстрат агентского изменения`, а не растворять этот слой внутри CI/review/acceptance tooling. Это зафиксировано в `work/decisions/ADR-0013-git-version-control-agentic-change-substrate.md` и `work/theory-writing/reports/VERSION_CONTROL_AGENTIC_DEVELOPMENT_COVERAGE_NOTE_2026_06_17.md`.


## 14. Атлас равноправен Теории; русские названия рабочих частей

Атлас считается самостоятельной крупной частью корпуса, а не приложением к Теории. Теория и Атлас работают с одной областью знаний, но в разных разрезах: Теория объясняет жизненный цикл изменения, Атлас строит техническую карту слоёв. Поэтому статья Атласа оценивается по собственному критерию technical payload, а не по тому, насколько хорошо она поддерживает теоретический аргумент.

Рабочие публичные названия нижних практических частей меняются в сторону русского языка: `Handbook` лучше называть `Рабочие сценарии` или, при необходимости, `Практикум`; `Fieldbook` лучше называть `Каталог проблем и решений` с уточнением про типовые сбои, диагностику и восстановление. Старые английские ярлыки и имена файлов пока могут сохраняться как техническая история, но новые карты и публичные планы должны использовать русские названия или давать пары.

Это зафиксировано в `work/decisions/ADR-0014-public-corpus-part-names-and-atlas-parity.md`.


## 15. Расширение Атласа до A15

Атлас расширяется за пределы первого ядра A1–A8. В основную карту добавлены самостоятельные статьи: A9 `Воспроизводимые среды исполнения и песочницы`, A10 `Индексация, поиск и извлечение контекста из кодовой базы`, A11 `Issue-to-agent: задачи, очереди, assignment и progress surfaces`, A12 `Долгая память проекта и повторное использование опыта`, A13 `Безопасность агентской разработки и supply-chain controls`, A14 `Browser/GUI/app feedback surfaces`, A15 `Model/provider layer, routing, cost and inference constraints`.

A10 должен явно покрывать Shotgun / shotgun_code. A11 не является сквозным подразделом: это отдельная полезная статья о превращении task/issue в агентскую рабочую единицу. A12 пишется нейтрально как технический слой долгой памяти проекта, без преждевременной публичной привязки к Нoveia. A15 имеет fast-staleness статус: это полезная рабочая карта для текущих решений, но она требует более частого обновления и не должна быть рейтингом моделей.


## 16. A16 и маршрутизация старых статей Атласа

В Level 1 Атласа добавляется A16 `Организационный контекст, software catalog и developer portal`. Эта статья покрывает Backstage/Port-like слой: сервисы, ownership, dependencies, environments, runbooks, scorecards, self-service actions, workflow automations and agent-facing organizational context.

Старые concept-first статьи Атласа не удаляются. Они переводятся в нижние уровни карты: методологические узлы, продуктовые profiles, плотные частные формы и source/dossier nodes. Kiro article не бросать: его стоит расширять как integrated product/method profile про specs, steering, hooks, IDE workflow and MCP integrations, связанный с A1/A2/A4/A8/A11/A14.

Порядок публичного сайта больше не считать автоматически story-first. Истории остаются важным корпусом, но будущий site/navigation package должен проверить, не лучше ли начинать с reader-oriented entry point: Теория/Жизненный цикл, Атлас, Рабочие сценарии, Каталог проблем и решений, Истории.

## 17. Многоязычная архитектура корпуса

Корпус пишется по-русски как текущая рабочая и редакционная база, но заранее готовится к будущей английской версии. Русский текст не нужно делать искусственным ради будущего перевода; вместо этого вводится translation-readiness слой: стабильные ID для статей/глав/историй, рабочие английские названия, двуязычный терминологический реестр, сохранение source provenance, translation notes для неочевидных русских формулировок и небольшой gate перед публичной стабилизацией.

Английская версия должна переводить смысл, структуру и источниковую фактуру, а не механически калькировать русский текст. Claims из английских источников при переводе нужно сверять с оригинальными источниками, а не переводить обратно русский пересказ. Решение зафиксировано в `work/decisions/ADR-0017-multilingual-corpus-architecture.md`, `work/multilingual/MULTILINGUAL_CORPUS_PROTOCOL.md` и `work/multilingual/BILINGUAL_TERM_REGISTRY.md`.


## 18. Harness Engineering в скелетоне Теории

Harness Engineering принимается как сквозная рамка для Теории, но не как новая глава и не как замена внутренним понятиям проекта. Теория должна явно учитывать, что агентская разработка работает как `model + harness + environment`: модель действует через рабочую обвязку проекта — контекст, инструменты, filesystem, sandbox, browser/app feedback, orchestration, memory, task state, traces, evals, permissions, review gates and recovery loops.

Это решение помогает не объяснять все успехи и сбои качеством модели и одновременно не превращать Теорию в технический Атлас. Future chapter packages должны добавлять `harness-frame check` рядом с `atlas-technical-grounding check`. Решение зафиксировано в `work/decisions/ADR-0018-harness-engineering-in-theory-skeleton.md` и `work/theory-writing/reports/HARNESS_ENGINEERING_THEORY_SKELETON_NOTE_2026_06_17.md`.


## 19. Скелетон Атласа, A17–A19 и дополнительные статьи

Атлас уровня 1 расширен до A1–A19. Новые основные слои: A17 `Структурированная обратная связь от программы`, A18 `Автономное тестирование и QA-артефакты`, A19 `Release, deployment, production monitoring and incident/remediation agents`.

A19 считается частью ядра, а не кандидатом: A7 отвечает за engineering acceptance gates, а A19 — за выпуск, наблюдение в эксплуатации, incident/remediation и возвращение уроков в будущую работу.

Создан `work/atlas/ATLAS_V2_SKELETON.md`. Он описывает композицию Атласа и разводит статьи уровня 1 с дополнительными профилями, методами и кейсами. Kiro, SPDD, Persistent Work Graph, ADR, Spec Kit, TDAD, Constitutional SDD, BMAD/GSD/Open GSD, Gas Town/Beads и AgenticOps не удаляются; они ведутся как Level 2/3 articles и должны явно ссылаться на слои A1–A19, которые пересекают.

`Тёмная материя софта` относится прежде всего к Cross-story synthesis. Это паттерн про внутренний, личный, одноразовый или плохо видимый AI-assisted software, а не технический слой Атласа.

Решение зафиксировано в `work/decisions/ADR-0019-atlas-v2-skeleton-a17-a19-and-additional-articles.md`.


## 20. Корректность checkpoint-архивов и continuation packages

Для staged executor packages плановая остановка должна возвращать валидный `stage checkpoint archive`, а не просто архив файлов. Такой checkpoint обязан содержать уже сохранённое stop-state runner-а: текущая запись — stop-record, состояние остановки включено, следующий record после `continue` известен и существует.

`Continuation package` — отдельный тип архива. Он используется, когда следующую стадию нужно начать в новом чате обычным запуском runner-а. Такой пакет не должен требовать `continue` и не должен называться checkpoint.

Протоколы сборки обновлены: state сначала переводится в stop-state и сохраняется, только потом собирается checkpoint archive; после упаковки архив распаковывается во временную папку и проверяется. Решение зафиксировано в `work/decisions/ADR-0020-checkpoint-continuation-package-correctness.md`, `work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md` и `work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md`.
