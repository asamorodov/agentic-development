# B results integration and evaluation report

Дата: 2026-06-11.

## Что было импортировано

В рабочую файловую систему положены результаты трёх B-пакетов:

```text
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B1_source_usage.md
work/theory-writing/fragments/B1_story_anchor_map.md
work/theory-writing/fragments/B1_figure_candidates.md
work/theory-writing/fragments/B1_open_questions.md
work/theory-writing/fragments/B1_degradation_and_duplication_audit.md

work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B2_source_usage.md
work/theory-writing/fragments/B2_story_anchor_map.md
work/theory-writing/fragments/B2_figure_candidates.md
work/theory-writing/fragments/B2_open_questions.md
work/theory-writing/fragments/B2_degradation_and_duplication_audit.md

work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/B3_source_usage.md
work/theory-writing/fragments/B3_story_anchor_map.md
work/theory-writing/fragments/B3_figure_candidates.md
work/theory-writing/fragments/B3_open_questions.md
work/theory-writing/fragments/B3_degradation_and_duplication_audit.md
```

Служебные `MANIFEST.md`, `VERIFY.md` и `RESUME.md` из result-архивов не положены в корень репозитория. Они сохранены как импортный provenance-слой:

```text
work/theory-writing/reports/b-results-import/B1_MANIFEST.md
work/theory-writing/reports/b-results-import/B1_VERIFY.md
work/theory-writing/reports/b-results-import/B1_RESUME.md
work/theory-writing/reports/b-results-import/B2_MANIFEST.md
work/theory-writing/reports/b-results-import/B2_VERIFY.md
work/theory-writing/reports/b-results-import/B2_RESUME.md
work/theory-writing/reports/b-results-import/B3_MANIFEST.md
work/theory-writing/reports/b-results-import/B3_VERIFY.md
work/theory-writing/reports/b-results-import/B3_RESUME.md
```

## Общая оценка

Все три B-фрагмента выполняют свою рабочую функцию: они не пытаются заново написать A-фрагменты и не превращаются в последовательный каталог источников. B1 фиксирует вклад и границы SPDD, B2 формулирует PWG как отдельный вклад в теорию, B3 показывает, что Gas Town добавляет сверх PWG организационно-операционный слой.

Статус пакета в целом: `ready_with_known_debts`. Тексты можно использовать как вход для следующих C-мостов и композиционной сборки, но перед публикационной стадией нужен отдельный repair/style pass.

## B1 — SPDD contribution and limits

Оценка после повторного repair: рабочий фрагмент — примерно 8.3/10; публикационная готовность — примерно 7.5/10.

Что получилось хорошо:

- B1 удерживает правильную функцию: SPDD показан не как весь AI-driven SDLC и не как набор slash-команд, а как цикл поддержки спецификации.
- Центральная граница с PWG проведена корректно: SPDD удерживает намерение, Canvas, ревью, поведенческие проверки и синхронизацию промпта/кода, но не хранит очередь работы, владельцев, условия ожидания, передачу и восстановление.
- Фактура плотная и полезная: REASONS Canvas, `/spdd-story`, `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-api-test`, `/spdd-code-review`, `/spdd-prompt-update`, `/spdd-sync` используются не как список команд, а как элементы цикла спецификации.
- После первого repair-прохода текст получил умеренную H2-структуру: вклад SPDD, путь к Canvas, проверка/обновление спецификации, делегирование, граница SPDD, применимость и вклад в общую теорию.
- Единственная синтетическая фигура оправдана: она показывает нетривиальную границу SPDD/PWG и не заменяет готовую внешнюю картинку.

Что было исправлено:

- Устранена структурная плоскость: B1 больше не является длинной непрерывной колонкой.
- OpenSPDD-середина немного уплотнена без потери источниковых ссылок.
- Граница с B2/PWG вынесена в отдельный раздел `Где SPDD заканчивается`.
- `B1_figure_candidates.md` больше не говорит, что локальные SPDD-ассеты отсутствуют: в полном репозитории они есть, но не вставлены в B1 автоматически, чтобы не дублировать A3 и не перегружать фрагмент.
- Повторный repair вычистил переводной язык: `prompt` как обычное слово в прозе в основном заменён на `промпт` или `спецификация`, а искусственные формулы вроде `артефакт поставки`, `слой управляемого намерения` и `оракул правильного намерения` заменены прямыми русскими формулировками.
- Beads-контраст сокращён: B1 теперь только показывает предел SPDD, а не начинает выполнять работу B2.

Оставшиеся долги:

- Перед публикационной сборкой возможен точечный asset-pass: решить, нужен ли B1 один реальный SPDD asset, например REASONS Canvas, или достаточно текущей boundary-фигуры.
- При техническом атласе часть микродеталей OpenSPDD-команд можно вынести из основного текста.
- Нужен финальный языковой проход по `промпт`/`prompt`, `REASONS Canvas` и source-specific терминам OpenSPDD/Beads.

Readiness: `ready_with_known_debts`, но структурный и основной языковой blocker сняты.

## B2 — PWG contribution

Оценка после repair: рабочий фрагмент — примерно 8.4/10; публикационная готовность — примерно 7.6/10.

Что получилось хорошо:

- B2 выполняет свою главную задачу: PWG сформулирован как место, где работа становится долговечным, проверяемым и передаваемым состоянием, а не как ещё один task tracker.
- Подзаголовки работают: `Работа как долговечный объект`, `Готовность, контрольные условия и преждевременное закрытие`, `Источник как состояние работы`, `Передача и параллельность без распада смысла`, `Исполнение, восстановление и очистка` — это реальная структура, не декоративное дробление.
- Beads, Task Master, BMAD TEA, Anthropic multi-agent research, CodeCRDT/STORM, LangGraph and Git worktree используются как границы механизма, а не как большой обзор landscape.
- Сильная мысль сохранена: продолжение, передача, блокировка, проверка, параллельность, восстановление и очистка становятся предметом теории, а не ручной дисциплиной вокруг агента.
- Фигура `fig-b2-pwg-contribution-matrix` оставлена как единственная synthetic figure: она связывает типичные сбои длинной агентной работы с тем, что именно должен хранить PWG.

Что было исправлено:

- Убраны слабые формулы и технический клей: `рабочий субстрат`, `ложное завершение`, `gate-условия`, несколько формул с “хвостом”, `cleanup-tail`, `evidence package` и лишний `handoff` в обычной русской прозе.
- Заголовок и раздел готовности переписаны через `контрольные условия` и `преждевременное закрытие`; точное имя команды `bd gate` сохранено только там, где оно нужно для источниковой точности.
- Caption синтетической figure переписан как публичная формулировка: не “субстрат”, а “единая форма состояния работы”.
- Раздел про источники очищен от внутреннего workflow-оттенка: источник описан как состояние работы и источник будущих долгов, а не как “источниковый хвост”.
- Финал переписан без “рабочего хвоста”: PWG делает очистку незакрытой работы предметом теории.
- Companion-файлы синхронизированы; ошибочная автоматическая замена URL Beads Recovery исправлена обратно на `/recovery`.
- Добавлен отчёт `B2_LANGUAGE_BOUNDARY_REPAIR_REPORT.md`.

Оставшиеся долги:

- Перед публикационной сборкой можно решить, нужно ли оставлять единственную synthetic figure или заменить часть её функции прозой.
- Внешняя диаграмма Anthropic остаётся `external_real_image_candidate`; без отдельного asset-pass её нельзя вставлять в основной текст.
- C3 и C4 не должны считать закрытыми протокол свидетельств и архитектуру исполнения: B2 даёт формулу вклада PWG, а не полный технический протокол.

Readiness: `ready_with_known_debts`, но основной языковой/style blocker снят; B2 годится как вход для C1–C4.

## B3 — Gas Town beyond PWG

Оценка после repair: рабочий фрагмент — примерно 8.2/10; публикационная готовность — примерно 7.5/10.

Что получилось хорошо:

- B3 ясно удерживает свою функцию: Gas Town не переопределяет PWG, а показывает организацию вокруг долговечной работы.
- Хорошо проведено различение: PWG даёт долговечность работы; Gas Town добавляет долговечность организации вокруг работы.
- Роли Mayor/Crew/Polecat/Witness/Refinery/Deacon/Dogs раскрыты не как lore и не как список имён, а как контуры ответственности.
- Сильная часть — цена метода: деньги, токены, внимание, merge/review bottleneck, обслуживание очередей, heartbeat, sync, stale/zombie states и cleanup. Это защищает текст от рекламного чтения Gas Town.
- Фигура `fig-b3-gas-town-organizational-loop` полезна: она объясняет, что Gas Town добавляет к PWG по жизненному циклу, а не просто перечисляет компоненты. После repair таблица русифицирована и больше не выглядит как внутренний рабочий лист.

Что было исправлено:

- Во вступлении и таблице вычищен лишний английский клей: `gates`, `evidence`, `handoff`, `recovery`, `graph theater` заменены на русские рабочие формулировки там, где это не имена команд/статусов.
- Псевдотехнические кальки вроде `контрольная плоскость` и `рабочий субстрат` заменены на `управленческий слой`, `слой рабочего состояния`, `долговечная единица работы`.
- `B3_figure_candidates.md` исправлен: локальные Gas Town assets больше не считаются отсутствующими; они классифицированы как `local_image_asset`, но не вставлены автоматически из-за риска дублирования A5 и ухода в technical atlas.
- Companion-файлы B3 синхронизированы с новым состоянием; добавлен отчёт `B3_STYLE_BOUNDARY_REPAIR_REPORT.md`.

Оставшиеся долги:

- Нужен publication-time freshness check: Gas Town/Beads быстро меняются, а B3 опирается на README, Changelog, design docs and docs site.
- Визуальный слой перед публикацией требует composition/asset-pass: решить, нужен ли B3 собственный Gas Town image asset, если A5 уже использует `gastown-architecture.svg`.
- Командный уровень Gas Town (`gt`, `bd`, scheduler/seance/escalation details) стоит вынести в technical atlas, если основной текст при финальной сборке окажется слишком плотным.

Readiness: `ready_with_known_debts`, но языковой/style blocker снят.

## Последствия для следующего шага

После импорта B1/B2/B3 карта готовности меняется:

- `B1_spdd_contribution_and_limits.md`, `B2_pwg_contribution.md`, `B3_gas_town_beyond_pwg.md` теперь существуют как рабочие фрагменты.
- `B2_pwg_contribution.md` больше не является отсутствующей зависимостью для C1–C4.
- C1–C4 можно собирать как writing-пакеты, если пользователь хочет идти дальше по мостам.
- C5 всё ещё преждевременен: для него нужны не только B1–B3, но и `00_spine_map.md`, `A10_mode_selection_map.md` и C1–C4.

## Необходимые repair-направления перед публикационной сборкой

1. B1: структурный repair выполнен; перед публикацией остаются точечный asset-pass и финальная языковая чистка.
2. B2/B3: отдельный языковой проход против английского клея и неудачных псевдотехнических формул.
3. Все B: проверить visual asset candidates, но не превращать реальные изображения в текстовые схемы.
4. B3: выполнить freshness check по быстро меняющимся Gas Town/Beads sources.
5. Все B: при composition-pass проверить дублирование с A3/A4/A5 и будущими C-мостами.
