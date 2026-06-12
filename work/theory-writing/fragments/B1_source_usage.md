# B1: карта использования источников

## Основной принцип

В основном фрагменте использованы только внешне доступные первичные источники: статья Thoughtworks/Fowler о SPDD, статья Thoughtworks/Fowler о разных уровнях SDD, файлы репозитория OpenSPDD и документация Beads как внешний якорь для границы SPDD/PWG. Внутренние досье, структурный скелетон и план написания использованы только как композиционные входы и не поставлены как публичные ссылки.

## Использованные источники

| Источник | Что поддерживает | Где использован |
| --- | --- | --- |
| [Structured Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) | Тезис о prompt как первоклассном артефакте, который входит в поставку; хранение в системе контроля версий; REASONS Canvas; командный слой OpenSPDD; пример с биллингом; сильные и слабые зоны применимости SPDD. | Начальная постановка вклада SPDD; объяснение REASONS Canvas; короткий фактический якорь про биллинг; распределение API-проверок, ревью кода и модульных тестов; раздел о применимости и стоимости метода. |
| [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Различение spec-first, spec-anchored и spec-as-source; определение `spec` как структурированного, ориентированного на поведение артефакта для ИИ-агентов, работающих с кодом. | Абзац, где SPDD помещён ближе к spec-anchored практике, а не к spec-as-source. |
| [OpenSPDD repository](https://github.com/gszhangwei/open-spdd) | Наличие нескольких адаптеров и рабочих сред: Cursor, Claude Code, GitHub Copilot, OpenCode, Codex skills и другие среды. | Абзац о том, что SPDD нельзя сводить к конкретным командам со слэшем или одной IDE. |
| [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) | Контрольная рамка OpenSPDD: проблема не в недостаточной «умности» модели, а в необходимости явно задавать намерение и границы. | Использовано как фоновая проверка формулировок; в основной фрагмент отдельная ссылка не вынесена, чтобы не дублировать статью Thoughtworks и шаблоны. |
| [`/spdd-story` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md) | Разложение крупного бизнес-требования на истории, пригодные для независимой поставки; `Scope In`/`Scope Out`; критерии приёмки на языке бизнеса; INVEST-проверка; запрет преждевременного ухода в техническую реализацию. | Абзац о формировании истории перед анализом и Canvas. |
| [`/spdd-analysis` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md) | Целенаправленное исследование кодовой базы по понятиям, а не полное чтение репозитория; сохранение исходного требования; доменные понятия, стратегический подход, риски и пробелы как вход для REASONS Canvas. | Абзац о контексте анализа как мосте между бизнес-историей и спецификацией. |
| [`/spdd-reasons-canvas` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md) | Чтение `@files`/`@folders` без усечения; создание готового к реализации Canvas; запрет заполнителей/TODO до подтверждения. | Абзац о превращении входного контекста в спецификацию. |
| [`/spdd-generate` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md) | Генерация по утверждённому Canvas; следование Operations в порядке; соблюдение Norms/Safeguards; запрет самостоятельного расширения задачи. | Абзац о том, что SPDD задаёт жизненный цикл, а не просто prompt. |
| [`/spdd-api-test` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md) | Создание `scripts/test-api.sh`, `cURL`-проверок и читаемых человеком таблиц поведения. | Абзац о доказательствах поведения после генерации. |
| [`/spdd-code-review` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md) | Проверка кода против REASONS Canvas; поиск расхождения намерения, нарушений Safeguards, лишних изменений и неявных решений. | Абзац о ревью с учётом REASONS. |
| [`/spdd-prompt-update` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md) | Обновление prompt перед изменением поведения; минимальность правки; сохранение структуры. | Абзацы о синхронизации prompt и кода. |
| [`/spdd-sync` template](https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md) | Перенос деталей реализации обратно в prompt после допустимой правки; Prompt Sync Plan; живая документация. | Абзацы о временной связности спецификации и границе с состоянием процесса. |
| [Beads documentation](https://gastownhall.github.io/beads/) | Beads как трекер задач с хранилищем на Dolt для разработки под надзором ИИ-агентов; `bd ready` как машинно-видимая очередь готовых незаблокированных задач; общая рамка координации нескольких агентов. | Абзац-контраст после фигуры о границе SPDD/PWG. |
| [Beads dependencies](https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md) | Блокирующие и неблокирующие зависимости; исключение задач с открытыми блокерами из `bd ready`; `bd blocked` как просмотр блокеров. | Абзац о том, что SPDD не хранит долговечную очередь и состояние зависимостей. |
| [Beads molecules](https://github.com/gastownhall/beads/blob/main/docs/MOLECULES.md) | Многодневное выполнение через ready → claim → close; граф зависимостей как путь агента между сессиями; различение persistent `Mol` и ephemeral `Wisp`. | Короткое усиление границы передачи работы и долговечного графа работы после фигуры SPDD/PWG. |
| [Beads dependencies and gates](https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md#gates) | `Gates` как долговечные ожидания внешних условий: pull request, CI-запуск, таймер, upstream bead, human approval. | Абзац о контрольных точках и организационной среде за пределами SPDD. |
| [Beads Claude Code integration](https://gastownhall.github.io/beads/integrations/claude-code) | `bd prime` для восстановления контекста; команды `bd ready`, `bd update --claim`, `bd close`, `bd dolt push` в агентном рабочем процессе. | Абзац о передаче работы, владелец/исполнитель и восстановлении после сессии. |
| [Beads recovery](https://gastownhall.github.io/beads/recovery) | Процедуры восстановления: повреждение базы, конфликты синхронизации/merge, циклические зависимости, сбои `sync`; быстрые диагностики `bd status`, `bd doctor`, `bd blocked`. | Абзац о том, что восстановление процесса не принадлежит SPDD Canvas. |

## Источники, намеренно не использованные как публичные ссылки

| Материал | Решение | Причина |
| --- | --- | --- |
| `work/dossiers/SPDD_METHOD_DOSSIER.md` | Не цитируется в основном тексте. | Это внутреннее досье; оно помогло найти первоисточники и проверить композицию, но не является публичной ссылкой. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Не цитируется в основном тексте. | B1 должен только провести границу перед PWG. Подробная фактура persistent work graph должна уйти в соседний узел, чтобы B1 не стал мини-главой о PWG. |
| `work/old-site-theoretical-synthesis-baseline.md` | Не цитируется в основном тексте. | Использован как источник уже найденных сильных формулировок и ссылки на графические материалы; публичные факты перенесены через первичные ссылки. |
| `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md` | Не цитируется в основном тексте. | A3 уже существует и используется как композиционная опора: B1 не повторяет сравнительный обзор методов спецификации, а раскрывает SPDD как глубокий случай жизненного цикла спецификации. |
| Вторичные комментарии и производные публикации о SPDD/SDD | Не добавлялись. | Для первого черновика достаточно первичных источников; дополнительные мнения могут распылить аргумент. |

## Проверка происхождения материалов

- Утверждения о `/spdd-story`, `/spdd-analysis`, REASONS Canvas, командах OpenSPDD, `/spdd-api-test`, `/spdd-code-review`, `/spdd-prompt-update` и `/spdd-sync` привязаны к конкретным template-файлам.
- Утверждения о примере с биллингом, применимости, стоимости метода и prompt как артефакте, который входит в поставку привязаны к статье Thoughtworks/Fowler.
- Различение spec-first/spec-anchored/spec-as-source привязано к отдельной статье Thoughtworks/Fowler о SDD-инструментах; B1 не повторяет сравнительную матрицу A3.
- Утверждения о долговечной очереди, блокерах, `gates`, многодневном проходе `ready → claim → close`, владелец/исполнитель и восстановлении контекста привязаны к документации Beads, а не к внутреннему PWG-досье. В основном тексте Beads оставлен коротким пограничным контрастом, а не вторым предметом фрагмента.
- В основном тексте нет ссылок на внутренние планы, скелетон, досье или рабочие отчёты.

## Остаточная проверка

Остаточный проход починки не добавил новых источников. Основной фрагмент по-прежнему ссылается только на внешние первичные источники; внутренние досье, скелетон, планы и рабочие отчёты остаются композиционными входами, а не публичными ссылками.
