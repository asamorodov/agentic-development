# Shopify Roast: когда агент становится шагом исполняемого workflow

В первых историях корпуса агент часто был главным действующим лицом: человек готовит research, запускает Codex или Claude Code, получает diff, проверяет, чинит, повторяет. В истории Shopify Roast центр тяжести другой. Здесь важен не один умный агент и не корпоративная dev-platform вокруг агентов, как у Stripe. Уникальный объект — **исполняемый workflow**, в котором агентский шаг занимает место рядом с shell-командой, Ruby-кодом, обычным LLM-запросом, обработкой коллекции, повторным циклом, session resume и пользовательской проверкой.

Roast поэтому нельзя читать как ещё один “Claude Code wrapper”. Внутри Shopify он вырос из задач developer productivity вроде flaky tests, низкого покрытия и массовой работы с unit tests; публично он стал Ruby gem и DSL для structured AI workflows. Но сильная мысль истории не в названии категории. Сильная мысль в том, что Shopify пытается сделать AI-работу похожей на привычную инженерную автоматизацию: её можно положить в файл, version-control, запустить из командной строки, разделить на шаги, заменить AI-шаг deterministic-кодом, повторить дорогой кусок через session replay и показать результат в читаемом виде.

## 1. Исходная развилка: агенту не добавляют свободу, а сужают сцену

Официальная статья Shopify Engineering начинает не с синтаксиса. Команда Augmented Engineering Developer Experience работала с задачами вроде flaky tests и низкого coverage. Идея была вполне практическая: использовать AI agents для анализа и оптимизации unit tests в большом масштабе. Но первый вывод был отрицательным: когда агенту позволяют свободно ходить по миллионам строк кода, надёжность падает. Поэтому Roast появляется не как максимизация autonomy, а как ответ на failure mode свободного агента: сложную задачу нужно разрезать на дискретные шаги, а недетерминированную часть окружить обычным кодом и явным маршрутом. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)

В ранней публичной форме это выглядело как `workflow.yml` и набор prompt-файлов. Автор workflow описывает шаги; Roast сам интерпретирует, что это за шаг: директория с `prompt.md`, shell-команда, inline prompt, `CodingAgent`-вызов, пользовательский Ruby-класс или параллельная группа. Это уже даёт важную форму: prompt перестаёт быть единственным контейнером намерения. Намерение разложено между YAML/Ruby, файловой структурой, command output, модельной конфигурацией и сессией.

<figure class="source-figure" id="fig-story-15-shopify-roast-structured-workflow-article">
  <img src="../assets/story-images/15-shopify-roast-structured-workflow-article.webp" alt="Скриншот Shopify Engineering article showing Roast structured workflow framing and early YAML/prompt examples." loading="lazy" />
  <figcaption>Картинка нужна в начале истории, чтобы Roast сразу читался как workflow-структура, а не как чатовый агент: ранняя публичная форма показывает шаги, prompts, commands and agent calls внутри одной исполняемой схемы. Источник: <a href="https://shopify.engineering/introducing-roast">Shopify Engineering: Introducing Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-roast-structured-workflow-article.webp</code>.</figcaption>
</figure>

Здесь появляется отличие от большинства историй корпуса. У Boris Tane центральна дисциплина “research → plan → implement”. У Matt Pocock — skills and handoff. У Armin Ronacher — минимальный изменяемый harness. У Shopify Roast объектом становится сама процедура: AI-шаг не обязан знать весь процесс, потому что процесс живёт вне модели.

## 2. Boba: внутренний кейс, где AI стоит после детерминированного сужения

Самый важный внутренний пример в статье — **Boba**, workflow для добавления Sorbet type annotations в Ruby test files Shopify. Источник не раскрывает полный внутренний workflow-файл, diff, количество обработанных файлов, retries или статистику ошибок. Поэтому историю нельзя строить как forensic reconstruction всего Boba. Но раскрытой последовательности достаточно, чтобы понять рабочую форму.

Задача Boba начинается не с просьбы к модели “добавь типы”. Сначала выполняется механическая подготовка. Workflow убирает старую пометку `typed: false`, повышает strictness до `true`, запускает Sorbet autocorrect, а затем смотрит, какие type errors остались. Только после этого в дело входит `CodingAgent`: он получает конкретный файл, остаточные Sorbet errors и инструкцию исправить проблему без изменения поведения тестов. После правок workflow прогоняет тесты и typecheck. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)

Это важно именно как последовательность. Если дать весь test suite агенту сразу, он должен сам решить, где начинать, какие изменения безопасны, какие errors mechanical, а какие требуют code reasoning. Boba переносит часть reasoning в deterministic pre-pass. `sed`-подобная чистка и Sorbet autocorrect уменьшают пространство, где агенту вообще нужно думать. Агент получает не “сделай проект typed”, а остаточную зону после автоматического сужения.

<figure class="source-figure" id="fig-story-15-shopify-boba-coding-agent">
  <img src="../assets/story-images/15-shopify-boba-coding-agent.webp" alt="Скриншот Shopify article section describing Boba: deterministic cleanup, Sorbet autocorrect, remaining errors handed to CodingAgent." loading="lazy" />
  <figcaption>Boba нужен как внутренний anchor истории: AI не заменяет весь процесс, а получает работу после deterministic cleanup and Sorbet autocorrect. Источник: <a href="https://shopify.engineering/introducing-roast">Shopify Engineering: Introducing Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-boba-coding-agent.webp</code>.</figcaption>
</figure>

Из этого кейса не следует, что Roast “автоматически типизирует Rails-монорепозиторий”. Такой вывод был бы сильнее источника. Следует другое: Shopify показывает pattern смешанной автоматизации, где AI полезен не потому, что ему всё доверили, а потому что обычная автоматизация подготовила ему хорошо ограниченную задачу. В терминах корпуса это не pure agentic coding, а **deterministic/agentic sandwich**: механика до агента, агентская работа внутри границ, проверка после агента.

В той же статье есть ещё несколько внутренних use cases, но они раскрыты значительно слабее, поэтому их нужно держать как directional evidence, не forensic cases. Test quality at scale описан как анализ тысяч test files and automatic identification/fixing of common antipatterns. SRE use case — периодическое scanning of internal Slack channels for early indicators of emerging issues, with alerts to appropriate teams. Competitive intelligence workflow собирает news/market analysis, migration patterns, brand switching data and trends from customer-conversation/CRM-like sources into reports. “Chesterton’s Fence” workflow researches commit history, related PRs and reasons why puzzling code exists, чтобы developer не удалил seemingly unnecessary but actually critical lines. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)


Интересная поздняя формула в статье — мысль о временном AI approximation. Автор workflow может поставить AI-step туда, где deterministic automation ещё не ясна; по мере понимания problem space этот шаг можно заменить обычным кодом. Это не надо читать как оправдание sloppy agents. Наоборот, это объясняет эволюционную функцию Roast: AI может быть provisional cog in a workflow, а не permanent oracle. Тогда workflow становится местом обучения системы: сначала модель помогает пройти неизвестный участок, потом этот участок постепенно hardens into code.

## 3. Внешний запуск раннего YAML: grading `resources_test.rb` как исполняемый эпизод

Хороший противовес внутреннему Boba — внешний запуск Daniel Doubrovkine. Это не идеальная demo-страница, а реальный ручной заход раннего Roast, где видны установка, модельная конфигурация, command line, лог выполнения, отчёт и даже отличие качества между моделями. Он показывает Roast не как обещание, а как tool run.

Сначала Doubrovkine проверяет OpenAI key обычным API-запросом, затем клонирует `Shopify/roast`, потому что хочет использовать пример workflow из репозитория. Проверка ключа не спрятана за Roast: он показывает обычный `curl` к `https://api.openai.com/v1/chat/completions` с `model: gpt-4.1-mini` и простым сообщением `What is 1+1?`, а успешный ответ должен быть `chat.completion`. Только после этого он переходит к Roast. Его цель — прогнать test-grading workflow над собственным тестом Roast `test/roast/resources_test.rb`. [Doubrovkine, “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

В исходной конфигурации grading workflow разные шаги использовали разные модели: coverage analysis — `gpt-4.1-mini`, recommendations — `o3`. У автора free tier не даёт удобно пользоваться более дорогими моделями, поэтому он меняет workflow. Это не “настроил модель где-то в интерфейсе”, а правка исполняемого файла: добавляется token from `OPENAI_API_KEY`, появляется общий `model: gpt-4.1-mini`, а локальные overrides у `analyze_coverage`, `generate_grades` и `generate_recommendations` убираются.

```diff
 name: Grading current test changes
+
+api_token: $(echo $OPENAI_API_KEY)
+model: gpt-4.1-mini
+
 tools:
   - Roast::Tools::Grep
   - Roast::Tools::ReadFile
@@
 analyze_coverage:
-  model: gpt-4.1-mini
   auto_loop: false
   json: true
 
 generate_grades:
-  model: o3
   json: true
 
 generate_recommendations:
-  model: o3
   auto_loop: false
   json: true
```

Это не мелкая setup-деталь. Она показывает, что model choice находится в workflow, а не растворён в глобальном “используй лучший LLM”. Один и тот же процесс можно сделать дешевле, слабее, быстрее или доступнее, меняя configuration. В результате внешний пользователь не просто “запускает AI”; он редактирует исполняемый план.

<figure class="source-figure" id="fig-story-15-shopify-dblock-model-config-diff">
  <img src="../assets/story-images/15-shopify-dblock-model-config-diff.webp" alt="Скриншот diff из поста Doubrovkine: workflow.yml получает OPENAI_API_KEY, global gpt-4.1-mini and removed o3 overrides." loading="lazy" />
  <figcaption>Этот diff полезен как первая concrete scene: пользователь не переписывает prompt, а меняет model/API configuration in workflow. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-model-config-diff.webp</code>.</figcaption>
</figure>

Затем он запускает короткую команду:

```bash
./exe/roast execute examples/grading/workflow.yml test/roast/resources_test.rb
```

Лог идёт не как чатовая стенка текста, а как выполнение workflow. Roast сообщает workflow path, target file, запускает `read_dependencies`, ищет `resources.rb`, читает `lib/roast/resources.rb`, запускает `run_coverage`, требует Ruby step file, печатает Minitest seed и результат: 13 runs, 16 assertions, без failures/errors/skips. После этого выполняются AI/analysis steps: `analyze_coverage`, `verify_test_helpers`, `verify_mocks_and_stubs`, grep по `def`, `generate_grades`, Ruby step `calculate_final_grade`, Ruby step `format_result`, затем `generate_recommendations`. Выход сохраняется в `.roast/sessions/.../final_output.txt`. [Doubrovkine](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

<figure class="source-figure" id="fig-story-15-shopify-dblock-workflow-log">
  <img src="../assets/story-images/15-shopify-dblock-workflow-log.webp" alt="Скриншот execution log from Doubrovkine: read_dependencies, run_coverage, Minitest run, grading steps and final_output path." loading="lazy" />
  <figcaption>Лог нужен как доказательство формы: Roast выглядит как исполняемый pipeline with named steps, Ruby files, tests and saved session output, а не как один LLM response. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-workflow-log.webp</code>.</figcaption>
</figure>

Отчёт получает score 80/100, letter grade B. Он разбит на rubric categories: line coverage 9/10, method coverage 10/10, branch coverage 6/10, test helper usage 10/10, mocks/stubs 10/10, readability 8/10, maintainability 8/10, effectiveness 7/10. Это важно не как оценка качества `resources_test.rb`, а как артефакт workflow: deterministic coverage/test steps and LLM-generated rubric sit in one output. В конце Doubrovkine сравнивает результат с более дорогой моделью: общий grade становится C, static coverage остаётся тем же, но test effectiveness падает с 7 до 6, потому что модель обнаруживает edge cases around command targets and glob patterns. [Doubrovkine](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

<figure class="source-figure" id="fig-story-15-shopify-dblock-grade-report">
  <img src="../assets/story-images/15-shopify-dblock-grade-report.webp" alt="Скриншот final TEST GRADE REPORT with score 80/100, letter grade B and rubric categories." loading="lazy" />
  <figcaption>Отчёт нужен не как красивый output, а как пример hybrid result: тестовый прогон, coverage signals and LLM rubric are assembled into one workflow artifact. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-grade-report.webp</code>.</figcaption>
</figure>

Системный вывод из этого эпизода простой: Roast делает AI-оценку менее похожей на консультацию и больше похожей на build artifact. Есть command, target file, named steps, Ruby step files, Minitest, model configuration, saved session and final report. Это не доказывает, что grading всегда правильный; зато показывает, куда помещается неопределённость модели: внутрь исполняемого процесса.

## 4. Старая YAML-поверхность: agent step как особая строка в workflow

RubyDoc snapshot сохраняет старую документационную форму Roast. В ней workflow определяется через YAML, prompt directories and step configuration. Это важно сохранить, потому что история Roast — не стабильный API с первого дня, а быстрая смена публичной формы. В старом README пользователь сначала создавал `workflow.yml`, рядом складывал prompt files вроде `step_name/prompt.md`, а запускал всё как обычную команду: `roast execute workflow.yml target_file.rb` или targetless `roast execute workflow.yml`. Если path неполный, Roast мог искать `project_root/roast/workflow_name/workflow.yml`. [RubyDoc snapshot](https://rubydoc.info/github/Shopify/roast)

Минимальный YAML-мир был не “prompt list”, а маленький orchestration language. Стандартный шаг ссылался на directory with `prompt.md`; custom Ruby step жил в `workflow/analyze_code.rb`, должен был иметь class `AnalyzeCode`, initializer с workflow-context and `call`, а результат попадал в `workflow.output`. Команда вставлялась прямо в `steps` через `$()`: например `rubocop: $(bundle exec rubocop -A)`. Если `exit_on_error: false`, неуспешная команда не валит workflow сразу, а её output получает exit status, который можно использовать дальше.

```yaml
steps:
  - analyze_code
  - rubocop: $(bundle exec rubocop -A)

lint_check:
  exit_on_error: false
```

В старой модели уже были conditional branches and loops. `if`/`unless` мог смотреть Ruby expression, shell command, previous step output or literal value. `each` мог итерироваться по Ruby expression, command output или step reference; `repeat` имел `until` and `max_iterations`; `case` ветвился по значению вроде detected language. Это даёт важное историческое уточнение: до Ruby DSL Roast уже пытался сделать AI workflow полноценным control-flow object, но выражал это через YAML, interpolation and conventions. [RubyDoc snapshot](https://rubydoc.info/github/Shopify/roast)

```yaml
steps:
  - process_files:
      each: "{{Dir.glob('**/*.rb')}}"
      as: current_file
      steps:
        - analyze_file
        - Generate a report for {{current_file}}
  - improve_code:
      repeat:
        until: "{{output['test_pass'] == true}}"
        max_iterations: 5
        steps:
          - run_tests
          - fix_issues
```

Особенно важен agent step. В старой модели префикс `^` отправляет prompt directly to `CodingAgent`, powered by Claude Code, bypassing обычный LLM translation layer. Это мог быть file-based prompt вроде `^fix_linting_errors`, inline instruction вроде `^Review the code and identify any performance issues`, или normal LLM step рядом с ним. У agent step есть context controls: `continue: true` продолжает предыдущую Claude Code session, а `resume: step_name` возобновляет конкретную прошлую session. RubyDoc прямо предупреждает: session IDs доступны только если CodingAgent настроен на JSON output, включая `--output-format stream-json`; если custom command не выдаёт JSON, resume не сработает. [RubyDoc snapshot](https://rubydoc.info/github/Shopify/roast)

```yaml
steps:
  - ^analyze_codebase
  - ^implement_feature
  - ^polish_implementation

analyze_codebase:
  continue: false

implement_feature:
  continue: true

polish_implementation:
  resume: analyze_codebase
```

<figure class="source-figure" id="fig-story-15-shopify-rubydoc-yaml-agent-step">
  <img src="../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp" alt="Скриншот RubyDoc old Roast README section showing YAML steps, agent step prefix and session continuation/resume options." loading="lazy" />
  <figcaption>Эта иллюстрация нужна для исторического слоя: до Ruby DSL Roast уже различал normal LLM step and direct CodingAgent step, включая continuation/resume semantics. Источник: <a href="https://rubydoc.info/github/Shopify/roast">RubyDoc snapshot</a>. Локальный файл: <code>../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp</code>.</figcaption>
</figure>

На этом уровне уже видна философия: агентский вызов — не произвольное “поговорить с Claude Code”, а type of step. Его можно поставить после `rubocop`, перед summary, внутри repeat-loop, после file search, alongside custom Ruby. В старой версии это ещё YAML convention; в новой версии та же мысль переезжает в Ruby DSL.

## 5. Переход к Ruby DSL: Roast сам переписывает свою публичную форму

В начале 2026 года публичная форма меняется резко. Release `v0.5.2` прямо объявляет, что это последний planned release before `v1.0`: legacy functionality будет убрана, новая DSL станет official, а дальнейшая работа v0.x уйдёт в `develop-v0`. Затем `v1.0.0` объявляет complete overhaul around a new Ruby DSL. Вместо YAML workflows становятся pure Ruby; cogs `chat`, `cmd`, `agent`, `ruby`, `map`, `repeat` can be chained; outputs доступны by name; scopes reusable through `call`; collections parallelized with `map`; agent cog gives local filesystem access through Claude Code. [GitHub releases](https://github.com/Shopify/roast/releases)

Сам release note показывает не только slogan, но и маленький executable specimen. Toy `review.rb` сначала вызывает `chat(:plan)`, чтобы получить три пункта для code review; затем `cmd(:files)` исполняет `git diff --name-only HEAD~1`; потом `agent(:review)` получает оба результата — file list from command and focus list from chat — and produces the review. Это почти compressed Roast in one screen: ordinary shell, ordinary chat and local coding agent находятся в одном Ruby `execute` block. [GitHub releases](https://github.com/Shopify/roast/releases)

```ruby
execute do
  chat(:plan) { "List 3 things to check in a code review." }
  cmd(:files) { "git diff --name-only HEAD~1" }
  agent(:review) do
    <<~PROMPT
      Review these files: #{cmd!(:files).out}
      Focus on: #{chat!(:plan).response}
    PROMPT
  end
end
```

Это не только release-note. PR chain показывает переходную работу. `#519` — 1.0 preview. `#521` — попытка `init` for DSL examples. `#524` — new README for 1.0. Даже если не читать весь diff, публичная история видна: framework, который сам продаёт structured workflows, быстро перестраивает собственный user-facing API. [PR #519](https://github.com/Shopify/roast/pull/519), [PR #521](https://github.com/Shopify/roast/pull/521), [PR #524](https://github.com/Shopify/roast/pull/524)

<figure class="source-figure" id="fig-story-15-shopify-release-v1-dsl">
  <img src="../assets/story-images/15-shopify-release-v1-dsl.webp" alt="Скриншот Roast v1.0.0 release notes announcing the new Ruby DSL and cogs." loading="lazy" />
  <figcaption>Release screen нужен, чтобы переход YAML → Ruby DSL был виден как публичный breaking turn, а не как незаметная правка README. Источник: <a href="https://github.com/Shopify/roast/releases">Shopify/roast releases</a>. Локальный файл: <code>../assets/story-images/15-shopify-release-v1-dsl.webp</code>.</figcaption>
</figure>

Текущий README уже начинается с Ruby DSL. Минимальный example `analyze_codebase.rb` не говорит “ask AI to review code”. Он задаёт three-step workflow: `cmd(:recent_changes)` берёт changed files from `git diff --name-only HEAD~5..HEAD`; `agent(:review)` превращает command output в prompt, где нужно проверить recently changed files for security, performance and maintainability; `chat(:summary)` берёт `agent!(:review).response` and summarizes it for non-technical stakeholders. Запуск — `bin/roast execute analyze_codebase.rb`. [README](https://github.com/Shopify/roast/blob/main/README.md)

```ruby
execute do
  cmd(:recent_changes) { "git diff --name-only HEAD~5..HEAD" }

  agent(:review) do
    files = cmd!(:recent_changes).lines
    <<~PROMPT
      Review these recently changed files for potential issues:
      #{files.join("\n")}

      Focus on security, performance, and maintainability.
    PROMPT
  end

  chat(:summary) do
    "Summarize this for non-technical stakeholders:

#{agent!(:review).response}"
  end
end
```

<figure class="source-figure" id="fig-story-15-shopify-readme-quick-example">
  <img src="../assets/story-images/15-shopify-readme-quick-example.webp" alt="Скриншот current Roast README quick example: cmd(:recent_changes), agent(:review), chat(:summary)." loading="lazy" />
  <figcaption>README example — хороший короткий снимок новой формы: shell command creates input, coding agent works on code, chat transforms result for another audience. Источник: <a href="https://github.com/Shopify/roast/blob/main/README.md">Shopify/roast README</a>. Локальный файл: <code>../assets/story-images/15-shopify-readme-quick-example.webp</code>.</figcaption>
</figure>

Системный смысл перехода не в том, что Ruby красивее YAML. Ruby DSL делает workflow ближе к обычному code artifact: можно писать blocks, scopes, config, reusable calls, collection processing, custom Ruby logic. AI перестаёт быть внешним “assistant” и становится одним из cogs внутри языка автоматизации.

Package-level детали подтверждают тот же поворот. `roast-ai.gemspec` публикует gem as `roast-ai`, связывает version with `Roast::VERSION`, requires Ruby `>= 3.3.0` and declares ordinary Ruby dependencies: `activesupport`, `async`, `rainbow`, `ruby_llm`, `type_toolkit`, `zeitwerk`. CLI surface в `lib/roast/cli.rb` остаётся узкой: `execute`, `version`, `help`; unknown command can be resolved as workflow path; `execute` builds `WorkflowParams` from targets and args, changes into `ROAST_WORKING_DIRECTORY` or current directory, then loads `Roast::Workflow.from_file`. [gemspec](https://github.com/Shopify/roast/blob/main/roast-ai.gemspec), [CLI source](https://github.com/Shopify/roast/blob/main/lib/roast/cli.rb)


Этот слой не даёт большой драматической сцены, но делает историю системной. Обещание Roast держится и на скучных границах package/CLI: исполняемый файл, targets, working directory, workflow args, dependencies, version, help. Agentic workflow becomes software.

## 6. Tutorial `code_review.rb`: security review как цепочка agent → chat → chat → ruby

Самый наглядный текущий example — `tutorial/02_chaining_cogs/code_review.rb`. Это toy workflow, но он полезен именно потому, что мал и полный. В config он разводит два слоя: `agent` uses Claude provider/model, `chat` uses OpenAI provider/model. Поэтому даже в tutorial review не является одним LLM call: file-aware security analysis делает local agent, а downstream summaries делает обычный chat cog. [code_review.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb)

Первый step — `agent(:review_security)`. Prompt asks for a security-focused code review of files changed by the latest commit. Важно, что задача уже frame-ится как review artifact: for each issue, explain what the vulnerability is, why it is dangerous and how to fix it.

```ruby
agent(:review_security) do
  <<~PROMPT
    You are a security-focused code reviewer. Analyze the files changed by the latest commit in this project
    and identify security vulnerabilities.

    For each issue found, explain:
    1. What the vulnerability is
    2. Why it's dangerous
    3. How to fix it
  PROMPT
end
```

Затем workflow не отдаёт этот ответ человеку напрямую. Второй step `chat(:prioritize)` takes `agent!(:review_security).text` and asks another model to create a prioritized action list ranked Critical/High/Medium/Low, formatted as `- **[Severity]** Issue: Brief description`. Третий step `chat(:summarize_for_executive)` uses `agent!(:review_security).response` again, but changes audience: 2–3 sentence executive summary for a non-technical stakeholder, focused on business impact and urgency.

```ruby
chat(:prioritize) do
  review = agent!(:review_security).text
  <<~PROMPT
    Review this security analysis and create a prioritized action list.
    Rank issues by severity (Critical, High, Medium, Low).

    Security Review:
    #{review}
  PROMPT
end

chat(:summarize_for_executive) do
  review = agent!(:review_security).response
  <<~PROMPT
    Create a 2-3 sentence executive summary of this security review
    for a non-technical stakeholder:
    #{review}
  PROMPT
end
```

Четвёртый step уже не LLM. `ruby(:display_report)` печатает three sections — `EXECUTIVE SUMMARY`, `PRIORITIZED ACTION ITEMS`, `DETAILED FINDINGS` — and returns structured metadata: timestamp, sections array and total length of agent response. Пятый Ruby step `check_report` checks whether `total_length > 0` and prints success/warning. Это не “AI wrote a report”. Это pipeline: agent produces detailed evidence, chat rewrites it twice for different audiences, Ruby turns it into a report artifact and checks that artifact is non-empty. [code_review.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb)

<figure class="source-figure" id="fig-story-15-shopify-code-review-tutorial">
  <img src="../assets/story-images/15-shopify-code-review-tutorial.webp" alt="Скриншот tutorial code_review.rb showing agent security review, chat prioritization, executive summary and Ruby report output." loading="lazy" />
  <figcaption>Эта картинка должна показать не весь файл, а саму форму chain: agent производит detailed code review, chat меняет representation twice, Ruby превращает responses в report artifact. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb">tutorial/02_chaining_cogs/code_review.rb</a>. Локальный файл: <code>../assets/story-images/15-shopify-code-review-tutorial.webp</code>.</figcaption>
</figure>

Эта сцена раскрывает, что Roast понимает под “chain”. Агентская работа не заканчивается на answer. Один и тот же agent output становится input для двух последующих LLM transformations and one Ruby report step. При этом config может назначить разным cogs разные providers/models. Если workflow author считает, что code review лучше делать через local coding agent, а summary через cheaper/faster chat model, это выражается в workflow code, not in operator memory.

## 7. Session resumption: контекст можно форкнуть, а не только продолжить

`session_resumption.rb` показывает более тонкую механику: Roast treats LLM conversation state as a value that can be assigned. Сначала config задаёт defaults: chat uses `gpt-4o-mini`, hides display and shows stats; named `chat(:recall_code)` switches to `gpt-4.1-nano`; default agent uses `haiku`; named `agent(:followup_question)` uses `sonnet`. То есть session control and model routing already live in the same file. [session_resumption.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb)

Первый `chat(:introduce_topic)` tells the model: “The secret code word is: thunderbolt.” Then `chat(:recall_code)` assigns `my.session = chat!(:introduce_topic).session` and asks what the code word was. Next `chat(:update_code)` resumes from the recall session and changes the word to `mermaid`. After that `chat(:resume_from_beginning)` deliberately resumes from the earlier `introduce_topic` session and asks “What is the current secret code word?” The file comment explains the key behavior: every time you resume from a previous session, a new session is forked; you can resume from that point again without later context being present. [session_resumption.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb)

```ruby
chat(:recall_code) do |my|
  my.session = chat!(:introduce_topic).session
  my.prompt = "What was the secret code word I told you?"
end

chat(:update_code) do |my|
  my.session = chat!(:recall_code).session
  my.prompt = "The new code word is 'mermaid'"
end

chat(:resume_from_beginning) do |my|
  my.session = chat!(:introduce_topic).session
  my.prompt = "What is the current secret code word?"
end
```

<figure class="source-figure" id="fig-story-15-shopify-session-resumption">
  <img src="../assets/story-images/15-shopify-session-resumption.webp" alt="Скриншот session_resumption.rb showing chat session assignment, recall, update and resume from an earlier point." loading="lazy" />
  <figcaption>Session resumption нужна как отдельная иллюстрация: workflow управляет ветвями LLM context explicitly, а не просто продолжает один линейный чат до исчерпания окна. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb">session_resumption.rb</a>. Локальный файл: <code>../assets/story-images/15-shopify-session-resumption.webp</code>.</figcaption>
</figure>

В конце тот же pattern показан для agent cog. Сначала `agent(:analyze_file)` asks the agent to list a few files in current directory. Then `agent(:followup_question)` resumes `agent!(:analyze_file).session` and asks the agent to pick one file and explain what it is. Это маленький example, но он показывает важную сторону Roast: session не просто побочный log. Она становится workflow data. Её можно передать, fork, resume and compose.

Для корпуса это важно как контраст к обычным long-running agent chats. В Roast автор procedure decides which context continues and which context branches. Это ближе к versioned computation graph, чем к разговору.

## 8. Обработка коллекций: от одного prompt к batch workflow

В `tutorial/07_processing_collections` Roast показывает, как один named scope применить к коллекции. Базовый example defines `execute(:process_item)` with `chat(:analyze)` and then calls `map(run: :process_item)` over `['item1', 'item2', 'item3']`. Results can be gathered through `collect`, transformed with access to original item and index, or reduced into aggregate. [tutorial chapter 7](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md)

```ruby
execute(:process_item) do
  chat(:analyze) do |_, item|
    "Analyze this item: #{item}"
  end
end

execute do
  map(run: :process_item) { ["item1", "item2", "item3"] }
end
```

Следующий слой — не “получили три ответа”, а работа с выходами. Tutorial показывает `collect(map!(:process_items))`, затем форму с доступом к `output`, original `item` и `index`, и отдельно сбор session objects из каждой итерации. Для aggregate case есть `reduce(map!(:calculate_scores), 0)`, где block возвращает новый accumulator, а пример с hash explicitly skips item if output text includes `failure`.

```ruby
results = collect(map!(:process_items)) do |output, item, index|
  { original_item: item, result_text: output.text, index: }
end

sessions = collect(map!(:process_items)) do
  chat!(:analyze).session
end

results = reduce(map!(:process_items), {}) do |hash, output, item, index|
  hash.merge(item => output) unless output.text.include?("failure")
end
```

Параллельный example делает это более конкретно. Config declares three map modes: `map(:serial) { no_parallel! }`, `map(:limited_parallel) { parallel(2) }`, `map(:unlimited_parallel) { parallel! }`. Named scope `execute(:generate_fact)` asks chat to generate a one-sentence fact about a topic and label it as `Fact #{index}:`. Main workflow then processes topics `Ruby`, `Python`, `JavaScript`, `Go`, `Rust` three ways: serially, with two concurrent iterations, and all at once. It collects `chat!(:fact).response.strip` and prints results. Even for parallel runs, tutorial notes that results return in original order regardless of completion order. [parallel_map.rb](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/parallel_map.rb)

```ruby
config do
  map(:limited_parallel) do
    parallel(2)
  end
  map(:unlimited_parallel) do
    parallel!
  end
end

execute(:generate_fact) do
  chat(:fact) do |_, topic, index|
    "Generate a brief, interesting fact (one sentence) about: #{topic}
Label it as "Fact #{index}:""
  end
end
```

<figure class="source-figure" id="fig-story-15-shopify-map-collections">
  <img src="../assets/story-images/15-shopify-map-collections.webp" alt="Скриншот tutorial chapter 7 showing map cog, collect, reduce and parallel execution." loading="lazy" />
  <figcaption>Эта фигура нужна, потому что она переводит Roast из “workflow over one file” в batch-processing surface: named scope, collection, ordered results and parallel execution. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections">tutorial/07_processing_collections</a>. Локальный файл: <code>../assets/story-images/15-shopify-map-collections.webp</code>.</figcaption>
</figure>

Это место соединяет публичный DSL с внутренней мотивацией Shopify. Если команда хочет “grade tests at scale” or process many files, one-off prompt insufficient. Нужно выразить batch boundary: what is one item, how results are collected, how concurrency controlled, how order preserved. Roast не решает автоматически correctness of each LLM result; зато даёт форму, где массовая AI-работа становится batch job, а не хаосом prompts.

## 9. `repeat`: итерация как контролируемый цикл, а не “попроси модель ещё раз”

Ещё один важный cog — `repeat`. В tutorial chapter 8 он описан как named scope that runs repeatedly until workflow calls `break!` or reaches maximum iterations. Each iteration receives previous value and index; `outputs` determines what flows into next iteration and always runs even if `break!` or `next!` was called earlier. [tutorial chapter 8](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md)

Basic repeat example makes this concrete. Scope `execute(:refine_text)` has `chat(:improve)` that asks the model to make text “more concise and clear”, keep same meaning, use fewer words, and return only improved text. Then Ruby prints the current iteration and response, calls `break! if index >= 3`, and `outputs { chat!(:improve).text }`, so the next iteration receives the improved version from the previous iteration. Main workflow starts with a verbose sentence about regular physical exercise, calls `repeat(:refinement, run: :refine_text) { initial_text }`, prints the final result and then collects all intermediate versions from `repeat!(:refinement).results`. [basic_repeat.rb](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/basic_repeat.rb)

```ruby
execute(:refine_text) do
  chat(:improve) do |_, text|
    <<~PROMPT
      Improve this text by making it more concise and clear.
      Keep the same meaning but use fewer words.
      Text: #{text}
      Return only the improved text, nothing else.
    PROMPT
  end

  ruby do |_, _, index|
    break! if index >= 3
  end

  outputs { chat!(:improve).text }
end
```

<figure class="source-figure" id="fig-story-15-shopify-repeat-cog">
  <img src="../assets/story-images/15-shopify-repeat-cog.webp" alt="Скриншот tutorial chapter 8 showing repeat cog, break!, next! and outputs block." loading="lazy" />
  <figcaption>`repeat` нужен для связи с Boba and agent repair loops: повторение становится cog-level control flow, а не неформальной просьбой к модели “try again”. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows">tutorial/08_iterative_workflows</a>. Локальный файл: <code>../assets/story-images/15-shopify-repeat-cog.webp</code>.</figcaption>
</figure>

Эта механика особенно важна для агентских задач, где first pass often fails. В обычном чате retry — это новая реплика. В Roast retry can be a workflow construct: a scope transforms value, Ruby checks condition, `break!` terminates, `outputs` carries forward state, and all intermediate outputs remain available for inspection. Это не гарантирует, что модель исправит ошибку; but it makes retry visible, bounded and testable.

## 10. Когда workflow становится программой: провайдеры, модели и session state

После `cmd`, `agent`, `chat`, `map` and `repeat` основная механика Roast уже видна. Дальше история легко может расползтись в список GitHub-заметок: provider docs, deprecated models, session filenames, logging, architecture docs. Но системно это не “мелкие хвосты после главного”. Это один следующий слой: если AI-workflow становится исполняемой программой, его нужно обслуживать как программу. У него появляются конфигурация провайдеров, жизненный цикл моделей, файловое состояние, читаемый вывод, события логирования and generated docs. Эти темы стоит держать вместе, иначе конец истории превращается в каталог PRs.

Provider story показывает первый такой boundary. Текущий README сначала говорит, что `chat` can use OpenAI, Anthropic, Perplexity and Gemini, but also includes a provider section saying current `chat` cog supports OpenAI provider. Repository source `lib/roast/cogs/chat/config.rb` currently lists OpenAI provider in `PROVIDERS`; `agent/config.rb` lists agent providers `:claude` and `:pi`, with Claude as default. Это неровность текущего open-source state, и её нельзя сглаживать. [README](https://github.com/Shopify/roast/blob/main/README.md), [chat config](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/chat/config.rb), [agent config](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/agent/config.rb)

PR `#888` показывает, как эта неровность попадает в maintenance работу. Автор PR clarifies that provider settings are selected in workflow `config` blocks; documents current chat provider setup through `OPENAI_API_KEY`, optional `OPENAI_API_BASE` and `provider :openai`; documents agent providers `:claude` and `:pi`; and explicitly notes that there is no CLI flag or environment variable for changing default provider globally. Verification is minimal and honest: `git diff --check`; `bundle exec rake` could not run because Ruby/Bundler was not installed in the workspace. The author says it was implemented with Codex assistance, with final diff reviewed against provider configuration source. [PR #888](https://github.com/Shopify/roast/pull/888)

<figure class="source-figure" id="fig-story-15-shopify-provider-pr-888">
  <img src="../assets/story-images/15-shopify-provider-pr-888.webp" alt="Скриншот PR #888 summary and verification: provider setup docs, no global CLI/env switch, Codex assistance, diff checked against config source." loading="lazy" />
  <figcaption>PR #888 важен как maintenance micro-case: provider choice is not a marketing bullet, it becomes docs/code alignment work, with Codex assistance and explicit verification limits. Источник: <a href="https://github.com/Shopify/roast/pull/888">Shopify/roast PR #888</a>. Локальный файл: <code>../assets/story-images/15-shopify-provider-pr-888.webp</code>.</figcaption>
</figure>

Issue `#875` даёт соседний аспект того же слоя. Some docs and tutorial workflows used deprecated models such as `claude-3-5-haiku-20241022`. The issue asks to replace deprecated models with newer ones and suggests a way to periodically do model “cleaning” — explicitly calling it a perfect use case for a Roast workflow. [Issue #875](https://github.com/Shopify/roast/issues/875)


Вместе `#888` and `#875` дают не две случайные проблемы документации, а один вывод: model/provider choice становится dependency surface. Deprecated model names are not just stale docs; they can break tutorial execution, confuse provider setup and make examples lie. Roast eventually needs workflows not only for app code, but also for keeping AI workflow examples themselves current.

Вторая boundary — state. PR `#468`, “Avoiding session file names that are too long”, выглядит боковым, но хорошо показывает, что human-readable workflow text eventually becomes filesystem state. Входная задача была не про модель и не про prompt quality: PR ссылался на issue `#267` и пытался защитить session filenames from path-length problems. Сначала решение шло через helper around safe filenames. Review остановил это как слишком общий ответ: либо helper должен быть generic enough for any file path, либо logic нужно moved into `file_state_repository` and made specific to session paths. Juniper поддержал второй вариант: general filename safety important, but too many ways filenames might be generated; purpose-specific logic is easier until several similar cases justify a generic utility. Автор force-push-ит новую версию и пишет, что logic moved into `lib/roast/workflow/file_state_repository.rb`, а file suffix стал optional argument defaulting to `.json`. После ещё нескольких review questions PR was approved, but then closed later when that functionality was removed from 1.0. [PR #468](https://github.com/Shopify/roast/pull/468)

Почему это важно для agent workflows? Проблема не в красивом имени файла. Step names, prompts and sessions cross into filesystem-backed state. When workflow uses long natural-language step names, those names can become session path components. Agentic instructions are no longer ephemeral text; they become filenames, state repositories, logs, resume handles. That creates ordinary software constraints: path length, sanitization, helper boundaries, review of where generic utility should live. И ещё один вывод: даже полезный fix can be correct for one generation of the workflow surface and removed after API reset. That is part of workflow-as-software, not an exception to it.

<figure class="source-figure" id="fig-story-15-shopify-pr-468-session-filenames">
  <img src="../assets/story-images/15-shopify-pr-468-session-filenames.webp" alt="Скриншот PR #468 review around session file names and file_state_repository." loading="lazy" />
  <figcaption>PR #468 показывает обратную сторону workflow-as-code: human-readable agent instructions eventually touch filesystem state, so UX text becomes storage engineering. Источник: <a href="https://github.com/Shopify/roast/pull/468">Shopify/roast PR #468</a>. Локальный файл: <code>../assets/story-images/15-shopify-pr-468-session-filenames.webp</code>.</figcaption>
</figure>

Эта сцена удерживает историю от слишком чистой теории. Если agent workflow записывается, replayed and resumed, naming becomes infrastructure. The workflow author’s nice English phrase is also an identifier.

## 11. Свидетельства выполнения: вывод workflow должен быть читаемым материалом проверки

Третий boundary — evidence. В structured AI workflow недостаточно “получить ответ модели”. Prompt, response, token stats, tool output, command output and logs становятся материалом человеческого review. Если этот материал плохо отформатирован, workflow превращается в blur: формально шаги выполнены, но человек не может быстро понять, что именно произошло.

После `1.1.0` публичный tracker shows this family of issues directly. Discussion `#896` frames the problem as potential approaches to better prompt and response formatting. Issue `#882` asks to clarify env variables and supported providers. This is not polishing after the “real” AI work. In structured AI workflows, output formatting is part of reviewability. [Issue #896](https://github.com/Shopify/roast/issues/896), [Issue #882](https://github.com/Shopify/roast/issues/882)


PR `#893` даёт очень земную проблему: multi-line output читается плохо, если prefix есть только на первой строке. PR explicitly says the goal is to make workflow output easier to read and understand which lines belong to which action. It includes old/new terminal and log output screenshots. A reviewer note explains why continuation lines use dots instead of whitespace: whitespace prefix could look like rendering glitch or dropped line, and future `.strip` elsewhere could collapse it silently. [PR #893](https://github.com/Shopify/roast/pull/893)

После этого PR stack moves from display patch to event representation. In the same Graphite-managed stack, `#898` adds a block type event, `#899` uses block events in Claude, `#900` in chat cogs, `#901` in Pi agent cogs, `#902` for LLM stats, and `#903` tags log messages with originating stream. `#903` states the concrete refactor: log messages get a `type` attribute so `LogFormatter#colourize` is more robust; because messages can now be either strings or `Roast::Log::Message`, `CustomLogging` normalizes with `.to_s`. [PR #893](https://github.com/Shopify/roast/pull/893), [PR #898](https://github.com/Shopify/roast/pull/898), [PR #899](https://github.com/Shopify/roast/pull/899), [PR #900](https://github.com/Shopify/roast/pull/900), [PR #902](https://github.com/Shopify/roast/pull/902), [PR #903](https://github.com/Shopify/roast/pull/903)


<figure class="source-figure" id="fig-story-15-shopify-log-prefix-pr-893">
  <img src="../assets/story-images/15-shopify-log-prefix-pr-893.webp" alt="Скриншот PR #893 old/new terminal and log output for repeated log prefix on multi-line output." loading="lazy" />
  <figcaption>PR #893 стоит показать отдельно от #903: здесь виден исходный human-readability defect, где multi-line output трудно привязать к action. Источник: <a href="https://github.com/Shopify/roast/pull/893">Shopify/roast PR #893</a>. Локальный файл: <code>../assets/story-images/15-shopify-log-prefix-pr-893.webp</code>.</figcaption>
</figure>

<figure class="source-figure" id="fig-story-15-shopify-log-message-pr-903">
  <img src="../assets/story-images/15-shopify-log-message-pr-903.webp" alt="Скриншот PR #903 describing Roast::Log::Message type attribute and LogFormatter robustness." loading="lazy" />
  <figcaption>PR #903 нужен как concrete maintenance scene: prompt/response output becomes typed log/event infrastructure, because humans need robust display of agent evidence. Источник: <a href="https://github.com/Shopify/roast/pull/903">Shopify/roast PR #903</a>. Локальный файл: <code>../assets/story-images/15-shopify-log-message-pr-903.webp</code>.</figcaption>
</figure>

Эта линия важна для системности всей истории. Roast переводит AI work into files and workflows, но затем сам должен обеспечить наблюдаемость этих workflows. A hidden or unreadable agent response cannot be reviewed well. Token stats, prompts, responses, agent sessions and command output need formatting semantics. Otherwise workflow-as-code produces workflow-as-blur.

## 12. Workflow второго порядка: AI-generated документация тоже требует проверки

Четвёртый late-stage boundary — документация. PR `#868` остаётся черновым. Он предлагает detailed architecture documentation, generated by LLM. Автор прямо пишет, что прогнал несколько automated validation passes, но не полностью уверен, что всё корректно. Эта оговорка важнее самого факта генерации документации: architecture docs здесь становятся AI-produced artifact, который ещё нуждается в проверке, а не готовым источником истины. [PR #868](https://github.com/Shopify/roast/pull/868)

PR `#892` связан с ним как черновой workflow для validation/update internal architecture documentation. Связка `#868`, `#892` и работы над internal comments documentation показывает не “сгенерировали docs и положили в репозиторий”, а следующий уровень самой логики Roast: если документация создаётся AI-шагом, вокруг неё тоже нужен workflow проверки и обновления. [PR #892](https://github.com/Shopify/roast/pull/892)

<figure class="source-figure" id="fig-story-15-shopify-architecture-docs-pr-868">
  <img src="../assets/story-images/15-shopify-architecture-docs-pr-868.webp" alt="Скриншот draft PR #868: LLM-generated architecture documentation and caution about correctness." loading="lazy" />
  <figcaption>PR #868 полезен как boundary case: generated architecture docs are valuable, but even maintainer says automated validation has not made correctness certain. Источник: <a href="https://github.com/Shopify/roast/pull/868">Shopify/roast PR #868</a>. Локальный файл: <code>../assets/story-images/15-shopify-architecture-docs-pr-868.webp</code>.</figcaption>
</figure>


Эти PRs не должны занимать больше места, чем основные workflow examples. Но они добавляют важную позднюю ноту: structured AI workflows порождают second-order workflows. Сначала AI помогает писать код; потом AI генерирует docs for agents/new contributors; потом нужен workflow to validate those docs. История закольцовывается не случайно: workflow становится способом производить и проверять следующие workflow-артефакты.

## 13. Что эта история добавляет к корпусу

Shopify Roast добавляет в корпус форму, которую нельзя заменить ни Stripe, ни Armin, ни HumanLayer. Stripe показывает enterprise platform substrate: agents inherit devboxes, analyzers, blueprints and internal tools. Armin shows a small mutable harness controlled by one toolsmith. HumanLayer shows harness and back-pressure around production workflows. Shopify показывает **workflow-as-code for AI steps**: a Ruby DSL where AI calls, coding agents, shell commands, Ruby logic, sessions, maps, repeats and output formatting are one executable object.

Главный переносимый урок не “надо взять Roast”. Главный урок — не давать агенту владеть всей процедурой. Если у задачи есть детерминированная подготовка, поставь её до агента. Если output модели должен попасть к другой аудитории, оформи эту трансформацию как отдельный шаг. Если session нужно разветвить, задай это явно. Если batch идёт по многим файлам, вырази collection semantics. Если важен retry, положи repeat/break/outputs в workflow. Если провайдеры отличаются, сделай model choice частью config. Если output служит evidence, format it as evidence. Если documentation produced by AI, give it a validation workflow instead of treating it as authority.

Эта история также меняет отношение к “prompt engineering”. В Roast prompt остаётся важным, но prompt уже не весь артефакт. Главный артефакт — файл, который можно review, run, change, version and decompose. Именно поэтому Roast нужен в основном корпусе: он даёт практическую форму перехода от ad hoc prompting к executable agentic procedure.

## 14. Ограничения источников и открытые края

База источников неровная. Shopify Engineering article is primary for public launch, Boba, early YAML form, CodingAgent, built-in tools and internal use cases, but it does not reveal internal workflow files, metrics, PRs, diff, cost or error rates. Doubrovkine post is strong for a real external run of old YAML grading workflow, but it is one user’s local execution and not proof of large-scale internal impact.

GitHub README, tutorials, config files, releases, issues and PRs сильны для публичной механики framework. Они показывают actual DSL surfaces, example workflows, provider configuration, session resumption, collection processing, release transitions and maintenance friction. Они не доказывают, что каждый pattern deployed at Shopify at scale. Некоторые источники заведомо draft/incomplete: `#868` and `#892` нужно читать как open/draft evidence, not finished architecture-doc pipeline.

Главный открытый край: Boba — самый важный internal case, но публичный материал даёт только форму, а не full run. Внешний grading example даёт full run, но не внутреннюю production-проблему Shopify. Поэтому история держится на двух дополняющих слоях: internal motivation and Boba pattern from Shopify; public executable mechanics from repo/tutorials/blog/PRs.

## 15. Карта источников

- [Shopify Engineering — “Introducing Roast: Structured AI workflows made easy”](https://shopify.engineering/introducing-roast) — primary source for launch framing, Augmented Engineering DX motivation, Boba, early YAML/prompt structure, CodingAgent, built-in tools, shared context, session replay, internal use cases and human-in-the-loop position.
- [Daniel Doubrovkine — “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html) — primary/field source for external old-YAML grading run: OpenAI setup, workflow.yml edits, command, execution log, Minitest run, final report and model comparison.
- [RubyDoc snapshot for Shopify/roast](https://rubydoc.info/github/Shopify/roast) — source for legacy YAML surface: step types, command execution, agent-step prefix, session continuation/resume, shell script/input steps and old `roast execute workflow.yml` model.
- [Shopify/roast README](https://github.com/Shopify/roast/blob/main/README.md) — source for current Ruby DSL: `execute do`, `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call`, installation, provider configuration and tutorial map.
- [`roast-ai.gemspec`](https://github.com/Shopify/roast/blob/main/roast-ai.gemspec) and [`lib/roast/cli.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cli.rb) — source for gem name, Ruby requirement, dependencies, CLI commands, workflow path resolution and target/argument handling.
- [Shopify/roast releases](https://github.com/Shopify/roast/releases) — source for `v0.5.2` legacy deprecation warning, `v1.0.0` Ruby DSL transition, `v1.0.1`/`v1.0.2` log/session refinements and `1.1.0` agent/provider/session changes.
- [PR #519](https://github.com/Shopify/roast/pull/519), [PR #521](https://github.com/Shopify/roast/pull/521), [PR #524](https://github.com/Shopify/roast/pull/524) — transition markers for 1.0 preview, DSL init and new README.
- [`tutorial/02_chaining_cogs/code_review.rb`](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb) — source for concrete agent → chat → chat → ruby security-review workflow.
- [`tutorial/02_chaining_cogs/session_resumption.rb`](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb) — source for chat and agent session resumption, context fork and session assignment.
- [`tutorial/07_processing_collections`](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md) — source for `map`, `collect`, `reduce`, ordered results, specific iteration access and parallel execution.
- [`tutorial/08_iterative_workflows`](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md) — source for `repeat`, `break!`, `next!`, `outputs`, max iterations and iterative value passing.
- [`lib/roast/cogs/chat/config.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/chat/config.rb) and [`lib/roast/cogs/agent/config.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/agent/config.rb) — source for current provider/config details in code.
- [PR #888](https://github.com/Shopify/roast/pull/888) — provider documentation maintenance case: workflow config selection, no global CLI/env switch, agent providers, Codex assistance, verification limits.
- [Issue #875](https://github.com/Shopify/roast/issues/875) and [Issue #882](https://github.com/Shopify/roast/issues/882) — open-source friction around deprecated models and provider/env docs.
- [PR #468](https://github.com/Shopify/roast/pull/468) — session filename/path-length maintenance case and review around where state-path logic belongs.
- [Issue #896](https://github.com/Shopify/roast/issues/896), [PR #893](https://github.com/Shopify/roast/pull/893), [PR #898](https://github.com/Shopify/roast/pull/898), [PR #899](https://github.com/Shopify/roast/pull/899), [PR #900](https://github.com/Shopify/roast/pull/900), [PR #902](https://github.com/Shopify/roast/pull/902), [PR #903](https://github.com/Shopify/roast/pull/903) — prompt/response formatting, repeated log prefix, block event representation, LLM stats and typed log message maintenance line.
- [PR #868](https://github.com/Shopify/roast/pull/868) and [PR #892](https://github.com/Shopify/roast/pull/892) — draft architecture-docs line: LLM-generated architecture docs and workflow to validate/update them.

## Временный список ассетов для скачивания

- `../assets/story-images/15-shopify-roast-structured-workflow-article.webp` — source URL: `https://shopify.engineering/introducing-roast`. Нужен как opening figure for structured AI workflow / early YAML-поверхность. Статус: не скачано.
- `../assets/story-images/15-shopify-boba-coding-agent.webp` — source URL: `https://shopify.engineering/introducing-roast`. Нужен для internal Boba scene: deterministic cleanup → Sorbet autocorrect → CodingAgent → tests/typecheck. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-model-config-diff.webp` — source URL: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для workflow.yml model/API-token adaptation. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-workflow-log.webp` — source URL: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для execution log with named steps, Ruby files, Minitest and final output path. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-grade-report.webp` — source URL: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для final grade report and rubric categories. Статус: не скачано.
- `../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp` — source URL: `https://rubydoc.info/github/Shopify/roast`. Нужен для legacy YAML agent-step prefix and session continuation/resume semantics. Статус: не скачано.
- `../assets/story-images/15-shopify-release-v1-dsl.webp` — source URL: `https://github.com/Shopify/roast/releases`. Нужен для `v1.0.0` Ruby DSL transition. Статус: не скачано.
- `../assets/story-images/15-shopify-readme-quick-example.webp` — source URL: `https://github.com/Shopify/roast/blob/main/README.md`. Нужен для current README sequence `cmd` → `agent` → `chat`. Статус: не скачано.
- `../assets/story-images/15-shopify-code-review-tutorial.webp` — source URL: `https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb`. Нужен для agent → chat → chat → ruby report. Статус: не скачано.
- `../assets/story-images/15-shopify-session-resumption.webp` — source URL: `https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb`. Нужен для session assignment and context fork. Статус: не скачано.
- `../assets/story-images/15-shopify-map-collections.webp` — source URL: `https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md`. Нужен для `map`, `collect`, `reduce`, parallel and ordered results. Статус: не скачано.
- `../assets/story-images/15-shopify-repeat-cog.webp` — source URL: `https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md`. Нужен для `repeat`, `break!`, `next!`, `outputs`. Статус: не скачано.
- `../assets/story-images/15-shopify-provider-pr-888.webp` — source URL: `https://github.com/Shopify/roast/pull/888`. Нужен для provider configuration docs maintenance, Codex assistance and verification limits. Статус: не скачано.
- `../assets/story-images/15-shopify-pr-468-session-filenames.webp` — source URL: `https://github.com/Shopify/roast/pull/468`. Нужен для session filenames/path-length state case. Статус: не скачано.
- `../assets/story-images/15-shopify-log-prefix-pr-893.webp` — source URL: `https://github.com/Shopify/roast/pull/893`. Нужен для old/new terminal and log output вокруг multi-line prefix problem. Статус: не скачано.
- `../assets/story-images/15-shopify-log-message-pr-903.webp` — source URL: `https://github.com/Shopify/roast/pull/903`. Нужен для typed log messages / LogFormatter robustness. Статус: не скачано.
- `../assets/story-images/15-shopify-architecture-docs-pr-868.webp` — source URL: `https://github.com/Shopify/roast/pull/868`. Нужен для LLM-generated docs as draft evidence. Статус: не скачано.
