# Shopify Roast: когда агент становится шагом исполняемого рабочего процесса

В первых историях корпуса агент часто был главным действующим лицом: человек готовит исследование, запускает Codex или Claude Code, получает дифф, проверяет, чинит, повторяет. В истории Shopify Roast центр тяжести другой. Здесь важен не один умный агент и не корпоративная платформа разработки вокруг агентов, как у Stripe. Уникальный объект — **исполняемый рабочий процесс**, в котором агентский шаг занимает место рядом с shell-командой, Ruby-кодом, обычным LLM-запросом, обработкой коллекции, повторным циклом, возобновлением сессии и пользовательской проверкой.

Roast поэтому нельзя читать как ещё одну обёртку над Claude Code. Внутри Shopify он вырос из задач продуктивности разработчиков вроде нестабильных тестов, низкого покрытия и массовой работы с юнит-тестами; публично он стал Ruby-гемом и DSL для структурированных ИИ-рабочих процессов. Но сильная мысль истории не в названии категории. Сильная мысль в том, что Shopify пытается сделать ИИ-работу похожей на привычную инженерную автоматизацию: её можно положить в файл, вести в системе контроля версий, запустить из командной строки, разделить на шаги, заменить ИИ-шаг детерминированным кодом, повторить дорогой кусок через воспроизведение сессии и показать результат в читаемом виде.

## 1. Исходная развилка: агенту не добавляют свободу, а сужают сцену

Официальная статья Shopify Engineering начинает не с синтаксиса. Команда Augmented Engineering Developer Experience работала с задачами вроде нестабильных тестов и низкого покрытия. Идея была вполне практическая: использовать ИИ-агентов для анализа и оптимизации юнит-тестов в большом масштабе. Но первый вывод был отрицательным: когда агенту позволяют свободно ходить по миллионам строк кода, надёжность падает. Поэтому Roast появляется не как максимизация автономности, а как ответ на режим отказа свободного агента: сложную задачу нужно разрезать на дискретные шаги, а недетерминированную часть окружить обычным кодом и явным маршрутом. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)

В ранней публичной форме это выглядело как `workflow.yml` и набор файлов промптов. Автор рабочего процесса описывает шаги; Roast сам интерпретирует, что это за шаг: директория с `prompt.md`, shell-команда, встроенный промпт, вызов `CodingAgent`, пользовательский Ruby-класс или параллельная группа. Это уже даёт важную форму: промпт перестаёт быть единственным контейнером намерения. Намерение разложено между YAML/Ruby, файловой структурой, выводом команды, модельной конфигурацией и сессией.

<figure class="source-figure" id="fig-story-15-shopify-roast-structured-workflow-article">
  <img src="../assets/story-images/15-shopify-roast-structured-workflow-article.webp" alt="Скриншот статьи Shopify Engineering с рамкой структурированного рабочего процесса для Roast и ранними YAML/примерами промптов." loading="lazy" />
  <figcaption>Картинка нужна в начале истории, чтобы Roast сразу читался как структура рабочего процесса, а не как чатовый агент: ранняя публичная форма показывает шаги, файлы промптов, команды и агентские вызовы внутри одной исполняемой схемы. Источник: <a href="https://shopify.engineering/introducing-roast">Shopify Engineering: Introducing Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-roast-structured-workflow-article.webp</code>.</figcaption>
</figure>

Здесь появляется отличие от большинства историй корпуса. У Boris Tane центральна дисциплина “research → plan → implement”. У Matt Pocock — навыки и передача работы. У Armin Ronacher — минимальная изменяемая обвязка. У Shopify Roast объектом становится сама процедура: ИИ-шаг не обязан знать весь процесс, потому что процесс живёт вне модели.

## 2. Boba: внутренний кейс, где ИИ стоит после детерминированного сужения

Самый важный внутренний пример в статье — **Boba**, рабочий процесс для добавления Sorbet-аннотаций типов в тестовые Ruby-файлы Shopify. Источник не раскрывает полный внутренний файл рабочего процесса, дифф, количество обработанных файлов, повторы или статистику ошибок. Поэтому историю нельзя строить как полную реконструкцию всего Boba. Но раскрытой последовательности достаточно, чтобы понять рабочую форму.

Задача Boba начинается не с просьбы к модели “добавь типы”. Сначала выполняется механическая подготовка. Рабочий процесс убирает старую пометку `typed: false`, повышает строгость до `true`, запускает Sorbet autocorrect, а затем смотрит, какие ошибки типов остались. Только после этого в дело входит `CodingAgent`: он получает конкретный файл, остаточные ошибки Sorbet и инструкцию исправить проблему без изменения поведения тестов. После правок рабочий процесс прогоняет тесты и проверку типов. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)

Это важно именно как последовательность. Если дать весь набор тестов агенту сразу, он должен сам решить, где начинать, какие изменения безопасны, какие ошибки механические, а какие требуют рассуждения по коду. Boba переносит часть рассуждения в детерминированный предварительный проход. `sed`-подобная чистка и Sorbet autocorrect уменьшают пространство, где агенту вообще нужно думать. Агент получает не “сделай проект типизированным”, а остаточную зону после автоматического сужения.

<figure class="source-figure" id="fig-story-15-shopify-boba-coding-agent">
  <img src="../assets/story-images/15-shopify-boba-coding-agent.webp" alt="Скриншот раздела статьи Shopify о Boba: детерминированная очистка, Sorbet autocorrect и передача оставшихся ошибок в CodingAgent." loading="lazy" />
  <figcaption>Boba нужен как внутренняя опорная сцена истории: ИИ не заменяет весь процесс, а получает работу после детерминированной очистки и Sorbet autocorrect. Источник: <a href="https://shopify.engineering/introducing-roast">Shopify Engineering: Introducing Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-boba-coding-agent.webp</code>.</figcaption>
</figure>

Из этого кейса не следует, что Roast “автоматически типизирует Rails-монорепозиторий”. Такой вывод был бы сильнее источника. Следует другое: Shopify показывает схему смешанной автоматизации, где ИИ полезен не потому, что ему всё доверили, а потому что обычная автоматизация подготовила ему хорошо ограниченную задачу. В терминах корпуса это не чистое агентское кодирование, а **детерминированно-агентский сэндвич**: механика до агента, агентская работа внутри границ, проверка после агента.

В той же статье есть ещё несколько внутренних сценариев использования, но они раскрыты значительно слабее, поэтому их нужно держать как направленное свидетельство, а не как подробные кейсы для реконструкции. Сценарий качества тестов в масштабе описан как анализ тысяч тестовых файлов и автоматическое выявление/исправление распространённых антипаттернов. SRE-сценарий — периодическое сканирование внутренних Slack-каналов в поиске ранних признаков возникающих проблем с отправкой предупреждений соответствующим командам. Рабочий процесс конкурентной разведки собирает новости и рыночный анализ, миграционные паттерны, данные о смене брендов и тренды из источников вроде клиентских разговоров/CRM в отчёты. Рабочий процесс “Chesterton’s Fence” исследует историю коммитов, связанные PR и причины существования непонятного кода, чтобы разработчик не удалил на вид лишние, но на самом деле критические строки. [Shopify Engineering: Introducing Roast](https://shopify.engineering/introducing-roast)


Интересная поздняя формула в статье — мысль о временной ИИ-аппроксимации. Автор рабочего процесса может поставить ИИ-шаг туда, где детерминированная автоматизация ещё не ясна; по мере понимания пространства проблемы этот шаг можно заменить обычным кодом. Это не надо читать как оправдание небрежных агентов. Наоборот, это объясняет эволюционную функцию Roast: ИИ может быть временным cog-шагом внутри рабочего процесса, а не постоянным оракулом. Тогда рабочий процесс становится местом обучения системы: сначала модель помогает пройти неизвестный участок, потом этот участок постепенно застывает в коде.

## 3. Внешний запуск раннего YAML: оценивание `resources_test.rb` как исполняемый эпизод

Хороший противовес внутреннему Boba — внешний запуск Daniel Doubrovkine. Это не идеальная демонстрационная страница, а реальный ручной заход раннего Roast, где видны установка, модельная конфигурация, командная строка, лог выполнения, отчёт и даже отличие качества между моделями. Он показывает Roast не как обещание, а как запуск инструмента.

Сначала Doubrovkine проверяет ключ OpenAI обычным API-запросом, затем клонирует `Shopify/roast`, потому что хочет использовать пример рабочего процесса из репозитория. Проверка ключа не спрятана за Roast: он показывает обычный `curl` к `https://api.openai.com/v1/chat/completions` с `model: gpt-4.1-mini` и простым сообщением `What is 1+1?`, а успешный ответ должен быть `chat.completion`. Только после этого он переходит к Roast. Его цель — прогнать рабочий процесс оценки тестов над собственным тестом Roast `test/roast/resources_test.rb`. [Doubrovkine, “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

В исходной конфигурации рабочего процесса оценки разные шаги использовали разные модели: анализ покрытия — `gpt-4.1-mini`, рекомендации — `o3`. У автора бесплатный тариф не даёт удобно пользоваться более дорогими моделями, поэтому он меняет рабочий процесс. Это не “настроил модель где-то в интерфейсе”, а правка исполняемого файла: добавляется токен из `OPENAI_API_KEY`, появляется общий `model: gpt-4.1-mini`, а локальные переопределения у `analyze_coverage`, `generate_grades` и `generate_recommendations` убираются.

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

Это не мелкая деталь настройки. Она показывает, что выбор модели находится в рабочем процессе, а не растворён в глобальном “используй лучший LLM”. Один и тот же процесс можно сделать дешевле, слабее, быстрее или доступнее, меняя конфигурацию. В результате внешний пользователь не просто “запускает ИИ”; он редактирует исполняемый план.

<figure class="source-figure" id="fig-story-15-shopify-dblock-model-config-diff">
  <img src="../assets/story-images/15-shopify-dblock-model-config-diff.webp" alt="Скриншот диффа из поста Doubrovkine: workflow.yml получает OPENAI_API_KEY, общий gpt-4.1-mini и удалённые переопределения o3." loading="lazy" />
  <figcaption>Этот дифф полезен как первая конкретная сцена: пользователь не переписывает промпт, а меняет конфигурацию модели/API внутри рабочего процесса. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-model-config-diff.webp</code>.</figcaption>
</figure>

Затем он запускает короткую команду:

```bash
./exe/roast execute examples/grading/workflow.yml test/roast/resources_test.rb
```

Лог идёт не как чатовая стенка текста, а как выполнение рабочего процесса. Roast сообщает путь рабочего процесса, целевой файл, запускает `read_dependencies`, ищет `resources.rb`, читает `lib/roast/resources.rb`, запускает `run_coverage`, требует файл Ruby-шага, печатает Minitest seed и результат: 13 runs, 16 assertions, без failures/errors/skips. После этого выполняются ИИ/аналитические шаги: `analyze_coverage`, `verify_test_helpers`, `verify_mocks_and_stubs`, grep по `def`, `generate_grades`, Ruby-шаг `calculate_final_grade`, Ruby-шаг `format_result`, затем `generate_recommendations`. Выход сохраняется в `.roast/sessions/.../final_output.txt`. [Doubrovkine](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

<figure class="source-figure" id="fig-story-15-shopify-dblock-workflow-log">
  <img src="../assets/story-images/15-shopify-dblock-workflow-log.webp" alt="Скриншот лога выполнения у Doubrovkine: read_dependencies, run_coverage, прогон Minitest, шаги оценки и путь final_output." loading="lazy" />
  <figcaption>Лог нужен как доказательство формы: Roast выглядит как исполняемый конвейер с именованными шагами, Ruby-файлами, тестами и сохранённым выводом сессии, а не как один ответ LLM. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-workflow-log.webp</code>.</figcaption>
</figure>

Отчёт получает счёт 80/100 и буквенную оценку B. Он разбит на категории рубрики: покрытие строк 9/10, покрытие методов 10/10, покрытие ветвлений 6/10, использование test helper 10/10, mocks/stubs 10/10, читаемость 8/10, поддерживаемость 8/10, эффективность 7/10. Это важно не как оценка качества `resources_test.rb`, а как артефакт рабочего процесса: детерминированные шаги покрытия/тестов и сгенерированная LLM рубрика собраны в одном выводе. В конце Doubrovkine сравнивает результат с более дорогой моделью: общая оценка становится C, статическое покрытие остаётся тем же, но эффективность тестов падает с 7 до 6, потому что модель обнаруживает пограничные случаи с целями команд и glob-паттернами. [Doubrovkine](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html)

<figure class="source-figure" id="fig-story-15-shopify-dblock-grade-report">
  <img src="../assets/story-images/15-shopify-dblock-grade-report.webp" alt="Скриншот final TEST GRADE REPORT со счётом 80/100, буквенной оценкой B и категориями рубрики." loading="lazy" />
  <figcaption>Отчёт нужен не как красивый вывод, а как пример гибридного результата: тестовый прогон, сигналы покрытия и LLM-рубрика собраны в один артефакт рабочего процесса. Источник: <a href="https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html">Doubrovkine, Executing Structured A.I. Workflows with Shopify Roast</a>. Локальный файл: <code>../assets/story-images/15-shopify-dblock-grade-report.webp</code>.</figcaption>
</figure>

Системный вывод из этого эпизода простой: Roast делает ИИ-оценку менее похожей на консультацию и больше похожей на артефакт сборки. Есть команда, целевой файл, именованные шаги, файлы Ruby-шагов, Minitest, модельная конфигурация, сохранённая сессия и итоговый отчёт. Это не доказывает, что оценивание всегда правильное; зато показывает, куда помещается неопределённость модели: внутрь исполняемого процесса.

## 4. Старая YAML-поверхность: агентский шаг как особая строка в рабочем процессе

Снимок RubyDoc сохраняет старую документационную форму Roast. В ней рабочий процесс определяется через YAML, директории промптов и конфигурацию шагов. Это важно сохранить, потому что история Roast — не стабильный API с первого дня, а быстрая смена публичной формы. В старом README пользователь сначала создавал `workflow.yml`, рядом складывал файлы промптов вроде `step_name/prompt.md`, а запускал всё как обычную команду: `roast execute workflow.yml target_file.rb` или `roast execute workflow.yml` без target. Если путь неполный, Roast мог искать `project_root/roast/workflow_name/workflow.yml`. [RubyDoc snapshot](https://rubydoc.info/github/Shopify/roast)

Минимальный YAML-мир был не “списком промптов”, а маленьким языком оркестрации. Стандартный шаг ссылался на директорию с `prompt.md`; пользовательский Ruby-шаг жил в `workflow/analyze_code.rb`, должен был иметь класс `AnalyzeCode`, инициализатор с контекстом рабочего процесса и `call`, а результат попадал в `workflow.output`. Команда вставлялась прямо в `steps` через `$()`: например `rubocop: $(bundle exec rubocop -A)`. Если `exit_on_error: false`, неуспешная команда не валит рабочий процесс сразу, а её вывод получает код выхода, который можно использовать дальше.

```yaml
steps:
  - analyze_code
  - rubocop: $(bundle exec rubocop -A)

lint_check:
  exit_on_error: false
```

В старой модели уже были условные ветвления и циклы. `if`/`unless` мог смотреть Ruby-выражение, shell-команду, вывод предыдущего шага или буквальное значение. `each` мог итерироваться по Ruby-выражению, выводу команды или ссылке на шаг; `repeat` имел `until` и `max_iterations`; `case` ветвился по значению вроде обнаруженного языка. Это даёт важное историческое уточнение: до Ruby DSL Roast уже пытался сделать ИИ-рабочий процесс полноценным объектом управления потоком, но выражал это через YAML, интерполяцию и соглашения.

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

Особенно важен агентский шаг. В старой модели префикс `^` отправляет промпт напрямую в `CodingAgent`, работающий через Claude Code, обходя обычный слой перевода в LLM. Это мог быть промпт из файла вроде `^fix_linting_errors`, встроенная инструкция вроде `^Review the code and identify any performance issues` или обычный LLM-шаг рядом с ним. У агентского шага есть средства управления контекстом: `continue: true` продолжает предыдущую сессию Claude Code, а `resume: step_name` возобновляет конкретную прошлую сессию. RubyDoc прямо предупреждает: идентификаторы сессий доступны только если CodingAgent настроен на JSON-вывод, включая `--output-format stream-json`; если пользовательская команда не выдаёт JSON, resume не сработает. [RubyDoc snapshot](https://rubydoc.info/github/Shopify/roast)

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
  <img src="../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp" alt="Скриншот старого раздела Roast README в RubyDoc: YAML-шаги, префикс агентского шага и параметры продолжения/возобновления сессии." loading="lazy" />
  <figcaption>Эта иллюстрация нужна для исторического слоя: до Ruby DSL Roast уже различал обычный LLM-шаг и прямой шаг CodingAgent, включая семантику продолжения/возобновления сессии. Источник: <a href="https://rubydoc.info/github/Shopify/roast">RubyDoc snapshot</a>. Локальный файл: <code>../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp</code>.</figcaption>
</figure>

На этом уровне уже видна философия: агентский вызов — не произвольное “поговорить с Claude Code”, а тип шага. Его можно поставить после `rubocop`, перед сводкой, внутри repeat-цикла, после поиска файлов, рядом с пользовательским Ruby. В старой версии это ещё YAML-соглашение; в новой версии та же мысль переезжает в Ruby DSL.

## 5. Переход к Ruby DSL: Roast сам переписывает свою публичную форму

В начале 2026 года публичная форма меняется резко. Релиз `v0.5.2` прямо объявляет, что это последний запланированный релиз перед `v1.0`: устаревшая функциональность будет убрана, новая DSL станет официальной, а дальнейшая работа v0.x уйдёт в `develop-v0`. Затем `v1.0.0` объявляет полную переработку вокруг новой Ruby DSL. Вместо YAML рабочие процессы становятся чистым Ruby; cogs `chat`, `cmd`, `agent`, `ruby`, `map`, `repeat` можно связывать в цепочки; outputs доступны по имени; scopes переиспользуются через `call`; коллекции распараллеливаются через `map`; agent cog даёт доступ к локальной файловой системе через Claude Code. [GitHub releases](https://github.com/Shopify/roast/releases)

Само примечание к релизу показывает не только лозунг, но и маленький исполняемый образец. Игрушечный `review.rb` сначала вызывает `chat(:plan)`, чтобы получить три пункта для проверки кода; затем `cmd(:files)` исполняет `git diff --name-only HEAD~1`; потом `agent(:review)` получает оба результата — список файлов из команды и список фокусов из chat — и создаёт ревью. Это почти сжатый Roast на одном экране: обычная shell-команда, обычный chat-шаг и локальный coding agent находятся в одном Ruby-блоке `execute`. [GitHub releases](https://github.com/Shopify/roast/releases)

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

Это не только примечание к релизу. Цепочка PR показывает переходную работу. `#519` — предварительная версия 1.0. `#521` — попытка `init` для примеров DSL. `#524` — новый README для 1.0. Даже если не читать весь дифф, публичная история видна: фреймворк, который сам продвигает структурированные рабочие процессы, быстро перестраивает собственный пользовательский API. [PR #519](https://github.com/Shopify/roast/pull/519), [PR #521](https://github.com/Shopify/roast/pull/521), [PR #524](https://github.com/Shopify/roast/pull/524)

<figure class="source-figure" id="fig-story-15-shopify-release-v1-dsl">
  <img src="../assets/story-images/15-shopify-release-v1-dsl.webp" alt="Скриншот примечаний к релизу Roast v1.0.0 с объявлением новой Ruby DSL и cogs." loading="lazy" />
  <figcaption>Экран релиза нужен, чтобы переход YAML → Ruby DSL был виден как публичный поворот с нарушением совместимости, а не как незаметная правка README. Источник: <a href="https://github.com/Shopify/roast/releases">Shopify/roast releases</a>. Локальный файл: <code>../assets/story-images/15-shopify-release-v1-dsl.webp</code>.</figcaption>
</figure>

Текущий README уже начинается с Ruby DSL. Минимальный пример `analyze_codebase.rb` не говорит “попроси ИИ проверить код”. Он задаёт рабочий процесс из трёх шагов: `cmd(:recent_changes)` берёт изменённые файлы из `git diff --name-only HEAD~5..HEAD`; `agent(:review)` превращает вывод команды в промпт, где нужно проверить недавно изменённые файлы на безопасность, производительность и поддерживаемость; `chat(:summary)` берёт `agent!(:review).response` и кратко пересказывает его для нетехнических заинтересованных лиц. Запуск — `bin/roast execute analyze_codebase.rb`. [README](https://github.com/Shopify/roast/blob/main/README.md)

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
  <img src="../assets/story-images/15-shopify-readme-quick-example.webp" alt="Скриншот текущего quick example из Roast README: cmd(:recent_changes), agent(:review), chat(:summary)." loading="lazy" />
  <figcaption>Пример README — хороший короткий снимок новой формы: shell-команда создаёт входные данные, coding agent работает с кодом, chat преобразует результат для другой аудитории. Источник: <a href="https://github.com/Shopify/roast/blob/main/README.md">Shopify/roast README</a>. Локальный файл: <code>../assets/story-images/15-shopify-readme-quick-example.webp</code>.</figcaption>
</figure>

Системный смысл перехода не в том, что Ruby красивее YAML. Ruby DSL делает рабочий процесс ближе к обычному кодовому артефакту: можно писать блоки, scope-блоки, конфигурацию, переиспользуемые вызовы, обработку коллекций, пользовательскую Ruby-логику. ИИ перестаёт быть внешним “помощником” и становится одним из cogs внутри языка автоматизации.

Детали уровня пакета подтверждают тот же поворот. `roast-ai.gemspec` публикует gem как `roast-ai`, связывает версию с `Roast::VERSION`, требует Ruby `>= 3.3.0` и объявляет обычные Ruby-зависимости: `activesupport`, `async`, `rainbow`, `ruby_llm`, `type_toolkit`, `zeitwerk`. CLI-поверхность в `lib/roast/cli.rb` остаётся узкой: `execute`, `version`, `help`; неизвестная команда может быть разрешена как путь к рабочему процессу; `execute` строит `WorkflowParams` из targets и args, переходит в `ROAST_WORKING_DIRECTORY` или текущую директорию, затем загружает `Roast::Workflow.from_file`. [gemspec](https://github.com/Shopify/roast/blob/main/roast-ai.gemspec), [CLI source](https://github.com/Shopify/roast/blob/main/lib/roast/cli.rb)


Этот слой не даёт большой драматической сцены, но делает историю системной. Обещание Roast держится и на скучных границах пакета/CLI: исполняемый файл, targets, рабочая директория, аргументы рабочего процесса, зависимости, версия, help. Агентский рабочий процесс становится программным обеспечением.

## 6. Учебный пример `code_review.rb`: проверка безопасности как цепочка agent → chat → chat → ruby

Самый наглядный текущий пример — `tutorial/02_chaining_cogs/code_review.rb`. Это игрушечный рабочий процесс, но он полезен именно потому, что мал и полный. В блоке `config` он разводит два слоя: `agent` использует provider/model Claude, `chat` использует provider/model OpenAI. Поэтому даже в учебном примере проверка не является одним LLM-вызовом: анализ безопасности с доступом к файлам делает локальный агент, а последующие сводки делает обычный chat cog. [code_review.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb)

Первый шаг — `agent(:review_security)`. Промпт просит сделать проверку кода с фокусом на безопасность файлов, изменённых последним коммитом. Важно, что задача уже оформляется как артефакт проверки: для каждой проблемы нужно объяснить, что это за уязвимость, почему она опасна и как её исправить.

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

Затем рабочий процесс не отдаёт этот ответ человеку напрямую. Второй шаг `chat(:prioritize)` берёт `agent!(:review_security).text` и просит другую модель создать приоритизированный список действий с ранжированием Critical/High/Medium/Low, в формате `- **[Severity]** Issue: Brief description`. Третий шаг `chat(:summarize_for_executive)` снова использует `agent!(:review_security).response`, но меняет аудиторию: 2–3 предложения резюме для нетехнического заинтересованного лица, с фокусом на бизнес-влияние и срочность.

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

Четвёртый шаг уже не LLM. `ruby(:display_report)` печатает три раздела — `EXECUTIVE SUMMARY`, `PRIORITIZED ACTION ITEMS`, `DETAILED FINDINGS` — и возвращает структурированные метаданные: timestamp, массив sections и общую длину ответа агента. Пятый Ruby-шаг `check_report` проверяет, что `total_length > 0`, и печатает success/warning. Это не “ИИ написал отчёт”. Это конвейер: агент производит подробные свидетельства, chat дважды переписывает их для разных аудиторий, Ruby превращает ответы в отчётный артефакт и проверяет, что этот артефакт непустой. [code_review.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb)

<figure class="source-figure" id="fig-story-15-shopify-code-review-tutorial">
  <img src="../assets/story-images/15-shopify-code-review-tutorial.webp" alt="Скриншот tutorial code_review.rb с agent-проверкой безопасности, chat-приоритизацией, резюме для руководителя и выводом Ruby-отчёта." loading="lazy" />
  <figcaption>Эта картинка должна показать не весь файл, а саму форму цепочки: agent производит подробную проверку кода, chat дважды меняет представление, Ruby превращает ответы в отчётный артефакт. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb">tutorial/02_chaining_cogs/code_review.rb</a>. Локальный файл: <code>../assets/story-images/15-shopify-code-review-tutorial.webp</code>.</figcaption>
</figure>

Эта сцена раскрывает, что Roast понимает под “цепочкой”. Агентская работа не заканчивается на ответе. Один и тот же вывод агента становится входом для двух последующих LLM-трансформаций и одного Ruby-шага отчёта. При этом `config` может назначить разным cogs разные провайдеры/модели. Если автор рабочего процесса считает, что проверку кода лучше делать через локального coding agent, а сводку через более дешёвую или быструю chat-модель, это выражается в коде рабочего процесса, а не в памяти оператора.

## 7. Возобновление сессии: контекст можно ответвить, а не только продолжить

`session_resumption.rb` показывает более тонкую механику: Roast обращается с состоянием LLM-разговора как со значением, которое можно присвоить. Сначала `config` задаёт `defaults`: chat использует `gpt-4o-mini`, скрывает `display` и показывает `stats`; именованный `chat(:recall_code)` переключается на `gpt-4.1-nano`; агент по умолчанию использует `haiku`; именованный `agent(:followup_question)` использует `sonnet`. То есть управление сессиями и маршрутизация моделей уже живут в одном файле. [session_resumption.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb)

Первый `chat(:introduce_topic)` говорит модели: “The secret code word is: thunderbolt.” Затем `chat(:recall_code)` присваивает `my.session = chat!(:introduce_topic).session` и спрашивает, каким было кодовое слово. Потом `chat(:update_code)` возобновляется из recall-сессии и меняет слово на `mermaid`. После этого `chat(:resume_from_beginning)` намеренно возобновляется из более ранней сессии `introduce_topic` и спрашивает “What is the current secret code word?” Комментарий в файле объясняет ключевое поведение: каждый раз, когда рабочий процесс возобновляется из предыдущей сессии, создаётся ответвление новой сессии; из этой точки можно возобновиться снова, без последующего контекста. [session_resumption.rb](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb)

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
  <img src="../assets/story-images/15-shopify-session-resumption.webp" alt="Скриншот session_resumption.rb с присваиванием chat session, recall, update и resume from an earlier point." loading="lazy" />
  <figcaption>Возобновление сессии нужно как отдельная иллюстрация: рабочий процесс явно управляет ветвями LLM-контекста, а не просто продолжает один линейный чат до исчерпания окна. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb">session_resumption.rb</a>. Локальный файл: <code>../assets/story-images/15-shopify-session-resumption.webp</code>.</figcaption>
</figure>

В конце та же схема показана для agent cog. Сначала `agent(:analyze_file)` просит агента перечислить несколько файлов в текущей директории. Потом `agent(:followup_question)` возобновляет `agent!(:analyze_file).session` и просит агента выбрать один файл и объяснить, что это такое. Это маленький пример, но он показывает важную сторону Roast: сессия не просто побочный лог. Она становится данными рабочего процесса. Её можно передать, ответвить, возобновить и скомпоновать.

Для корпуса это важно как контраст к обычным долгим агентским чатам. В Roast автор процедуры решает, какой контекст продолжается, а какой контекст ветвится. Это ближе к версионированному графу вычислений, чем к разговору.

## 8. Обработка коллекций: от одного промпта к пакетному рабочему процессу

В `tutorial/07_processing_collections` Roast показывает, как один именованный scope применить к коллекции. Базовый пример определяет `execute(:process_item)` с `chat(:analyze)`, а затем вызывает `map(run: :process_item)` над `['item1', 'item2', 'item3']`. Результаты можно собрать через `collect`, преобразовать с доступом к исходному элементу и индексу или свернуть в агрегат. [tutorial chapter 7](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md)

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

Следующий слой — не “получили три ответа”, а работа с выходами. Учебная глава показывает `collect(map!(:process_items))`, затем форму с доступом к `output`, исходному `item` и `index`, и отдельно сбор объектов сессий из каждой итерации. Для случая агрегации есть `reduce(map!(:calculate_scores), 0)`, где блок возвращает новый аккумулятор, а пример с hash явно пропускает элемент, если output text содержит `failure`.

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

Параллельный пример делает это более конкретно. Блок `config` объявляет три режима map: `map(:serial) { no_parallel! }`, `map(:limited_parallel) { parallel(2) }`, `map(:unlimited_parallel) { parallel! }`. Именованный scope `execute(:generate_fact)` просит chat сгенерировать факт из одного предложения о теме и пометить его как `Fact #{index}:`. Затем основной рабочий процесс обрабатывает темы `Ruby`, `Python`, `JavaScript`, `Go`, `Rust` тремя способами: последовательно, с двумя одновременными итерациями и всеми сразу. Он собирает `chat!(:fact).response.strip` и печатает результаты. Даже для параллельных запусков учебный материал отмечает, что результаты возвращаются в исходном порядке независимо от порядка завершения. [parallel_map.rb](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/parallel_map.rb)

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
  <img src="../assets/story-images/15-shopify-map-collections.webp" alt="Скриншот главы 7 учебных материалов с map cog, collect, reduce и параллельным выполнением." loading="lazy" />
  <figcaption>Эта фигура нужна, потому что она переводит Roast из “рабочего процесса над одним файлом” в поверхность пакетной обработки: named scope, коллекция, упорядоченные результаты и параллельное выполнение. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections">tutorial/07_processing_collections</a>. Локальный файл: <code>../assets/story-images/15-shopify-map-collections.webp</code>.</figcaption>
</figure>

Это место соединяет публичный DSL с внутренней мотивацией Shopify. Если команда хочет “оценивать тесты в масштабе” или обрабатывать много файлов, разового промпта недостаточно. Нужно выразить границу пакетной обработки: что считается одним элементом, как собираются результаты, как управляется параллелизм и как сохраняется порядок. Roast не решает автоматически корректность каждого LLM-результата; зато даёт форму, где массовая ИИ-работа становится пакетной задачей, а не хаосом промптов.

## 9. `repeat`: итерация как контролируемый цикл, а не “попроси модель ещё раз”

Ещё один важный cog — `repeat`. В главе 8 учебных материалов он описан как именованный scope, который повторно запускается, пока рабочий процесс не вызовет `break!` или не достигнет максимального числа итераций. Каждая итерация получает предыдущее значение и index; `outputs` определяет, что переходит в следующую итерацию, и всегда выполняется, даже если раньше был вызван `break!` или `next!`. [tutorial chapter 8](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md)

Базовый пример `repeat` делает это конкретным. Scope `execute(:refine_text)` содержит `chat(:improve)`, который просит модель сделать текст “more concise and clear”, сохранить тот же смысл, использовать меньше слов и вернуть только улучшенный текст. Затем Ruby печатает текущую итерацию и ответ, вызывает `break! if index >= 3`, а `outputs { chat!(:improve).text }` передаёт в следующую итерацию улучшенную версию из предыдущей итерации. Основной рабочий процесс начинает с многословного предложения о регулярных физических упражнениях, вызывает `repeat(:refinement, run: :refine_text) { initial_text }`, печатает итоговый результат, а затем собирает все промежуточные версии из `repeat!(:refinement).results`. [basic_repeat.rb](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/basic_repeat.rb)

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
  <img src="../assets/story-images/15-shopify-repeat-cog.webp" alt="Скриншот главы 8 учебных материалов с repeat cog, break!, next! и блоком outputs." loading="lazy" />
  <figcaption>`repeat` нужен для связи с Boba и циклами агентского исправления: повторение становится управлением потоком на уровне cog, а не неформальной просьбой к модели “попробуй ещё раз”. Источник: <a href="https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows">tutorial/08_iterative_workflows</a>. Локальный файл: <code>../assets/story-images/15-shopify-repeat-cog.webp</code>.</figcaption>
</figure>

Эта механика особенно важна для агентских задач, где первый проход часто не срабатывает. В обычном чате повторная попытка — это новая реплика. В Roast повторная попытка может быть конструкцией рабочего процесса: scope преобразует значение, Ruby проверяет условие, `break!` завершает цикл, `outputs` переносит состояние дальше, а все промежуточные outputs остаются доступными для проверки. Это не гарантирует, что модель исправит ошибку; зато делает повторную попытку видимой, ограниченной и проверяемой.

## 10. Когда рабочий процесс становится программой: провайдеры, модели и состояние сессии

После `cmd`, `agent`, `chat`, `map` и `repeat` основная механика Roast уже видна. Дальше история легко может расползтись в список GitHub-заметок: документация провайдеров, устаревшие модели, имена файлов сессий, логирование, архитектурная документация. Но системно это не “мелкие хвосты после главного”. Это один следующий слой: если ИИ-рабочий процесс становится исполняемой программой, его нужно обслуживать как программу. У него появляются конфигурация провайдеров, жизненный цикл моделей, файловое состояние, читаемый вывод, события логирования и сгенерированная документация. Эти темы стоит держать вместе, иначе конец истории превращается в каталог PR.

История с провайдерами показывает первую такую границу. Текущий README сначала говорит, что `chat` может использовать OpenAI, Anthropic, Perplexity и Gemini, но также содержит раздел `provider`, где сказано, что текущий `chat` cog поддерживает провайдера OpenAI. Исходный код репозитория `lib/roast/cogs/chat/config.rb` сейчас перечисляет провайдера OpenAI в `PROVIDERS`; `agent/config.rb` перечисляет провайдеров `agent` `:claude` и `:pi`, с Claude по умолчанию. Это неровность текущего состояния открытого проекта, и её нельзя сглаживать. [README](https://github.com/Shopify/roast/blob/main/README.md), [chat config](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/chat/config.rb), [agent config](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/agent/config.rb)

PR `#888` показывает, как эта неровность попадает в работу сопровождения. Автор PR уточняет, что настройки провайдера выбираются в блоках рабочего процесса `config`; документирует текущую настройку провайдера chat через `OPENAI_API_KEY`, опциональный `OPENAI_API_BASE` и `provider :openai`; документирует провайдеров `agent` `:claude` и `:pi`; и явно отмечает, что нет CLI-флага или переменной окружения для глобального изменения провайдера по умолчанию. Проверка минимальна и честна: `git diff --check`; `bundle exec rake` не удалось запустить, потому что Ruby/Bundler не был установлен в рабочем окружении. Автор говорит, что реализация была сделана с помощью Codex, а финальный дифф сверялся с исходником конфигурации провайдеров. [PR #888](https://github.com/Shopify/roast/pull/888)

<figure class="source-figure" id="fig-story-15-shopify-provider-pr-888">
  <img src="../assets/story-images/15-shopify-provider-pr-888.webp" alt="Скриншот PR #888: разделы summary и verification, документация настройки провайдера, отсутствие глобального переключателя CLI/env, помощь Codex и сверка диффа с исходной конфигурацией." loading="lazy" />
  <figcaption>PR #888 важен как микрокейс сопровождения: выбор провайдера — не маркетинговый пункт, а работа по согласованию документации и кода, с помощью Codex и явными пределами проверки. Источник: <a href="https://github.com/Shopify/roast/pull/888">Shopify/roast PR #888</a>. Локальный файл: <code>../assets/story-images/15-shopify-provider-pr-888.webp</code>.</figcaption>
</figure>

Issue `#875` даёт соседний аспект того же слоя. Некоторые документы и учебные рабочие процессы использовали устаревшие модели вроде `claude-3-5-haiku-20241022`. Issue просит заменить устаревшие модели более новыми и предлагает способ периодически делать “очистку” моделей — прямо называя это удачным сценарием использования для рабочего процесса Roast. [Issue #875](https://github.com/Shopify/roast/issues/875)


Вместе `#888` и `#875` дают не две случайные проблемы документации, а один вывод: выбор модели/провайдера становится поверхностью зависимостей. Устаревшие имена моделей — это не просто залежавшаяся документация; они могут ломать выполнение учебных материалов, путать настройку провайдера и делать примеры вводящими в заблуждение. Roast со временем нужны рабочие процессы не только для кода приложений, но и для поддержания самих примеров ИИ-рабочих процессов в актуальном состоянии.

Вторая граница — состояние. PR `#468`, “Avoiding session file names that are too long”, выглядит боковым, но хорошо показывает, что человекочитаемый текст рабочего процесса со временем становится состоянием файловой системы. Входная задача была не про модель и не про качество промпта: PR ссылался на issue `#267` и пытался защитить session filenames от проблем длины пути. Сначала решение шло через helper вокруг безопасных имён файлов. Ревью остановило это как слишком общий ответ: либо helper должен быть достаточно общим для любого пути к файлу, либо логику нужно перенести в `file_state_repository` и сделать специфичной для путей сессий. Juniper поддержал второй вариант: общая безопасность имён файлов важна, но способов породить имена файлов слишком много; специализированная логика проще, пока несколько похожих случаев не оправдают универсальную утилиту. Автор делает force-push новой версии и пишет, что логика перенесена в `lib/roast/workflow/file_state_repository.rb`, а суффикс файла стал необязательным аргументом со значением `.json` по умолчанию. После ещё нескольких вопросов на ревью PR был одобрен, но позже закрыт, когда эта функциональность была удалена из 1.0. [PR #468](https://github.com/Shopify/roast/pull/468)

Почему это важно для агентских рабочих процессов? Проблема не в красивом имени файла. Имена шагов, промпт и сессии переходят в состояние, поддержанное файловой системой. Когда рабочий процесс использует длинные естественно-языковые имена шагов, эти имена могут стать компонентами пути сессии. Агентские инструкции уже не эфемерный текст; они становятся именами файлов, репозиториями состояния, логами, resume-handles. Это создаёт обычные программные ограничения: длина пути, очистка имён, границы helper, ревью того, где должна жить универсальная утилита. И ещё один вывод: даже полезное исправление может быть корректным для одного поколения поверхности рабочего процесса и удалённым после API-сброса. Это часть рабочего процесса как программного обеспечения, а не исключение из него.

<figure class="source-figure" id="fig-story-15-shopify-pr-468-session-filenames">
  <img src="../assets/story-images/15-shopify-pr-468-session-filenames.webp" alt="Скриншот PR #468 review вокруг session file names и file_state_repository." loading="lazy" />
  <figcaption>PR #468 показывает обратную сторону рабочего процесса как кода: человекочитаемые агентские инструкции со временем касаются состояния файловой системы, поэтому UX-текст становится инженерией хранения. Источник: <a href="https://github.com/Shopify/roast/pull/468">Shopify/roast PR #468</a>. Локальный файл: <code>../assets/story-images/15-shopify-pr-468-session-filenames.webp</code>.</figcaption>
</figure>

Эта сцена удерживает историю от слишком чистой теории. Если агентский рабочий процесс записывается, воспроизводится и возобновляется, именование становится инфраструктурой. Красивая английская фраза автора рабочего процесса одновременно является идентификатором.

## 11. Свидетельства выполнения: вывод рабочего процесса должен быть читаемым материалом проверки

Третья граница — свидетельства выполнения. В структурированном ИИ-рабочем процессе недостаточно “получить ответ модели”. Промпт, response, статистика токенов, вывод инструментов, вывод команд и логи становятся материалом человеческой проверки. Если этот материал плохо отформатирован, рабочий процесс превращается в размытый процесс: формально шаги выполнены, но человек не может быстро понять, что именно произошло.

После `1.1.0` публичный трекер показывает эту группу проблем напрямую. Discussion `#896` формулирует проблему как возможные подходы к лучшему форматированию `prompt` и `response`. Issue `#882` просит уточнить переменные окружения и поддерживаемых провайдеров. Это не полировка после “настоящей” ИИ-работы. В структурированных ИИ-рабочих процессах форматирование вывода — часть проверяемости. [Issue #896](https://github.com/Shopify/roast/issues/896), [Issue #882](https://github.com/Shopify/roast/issues/882)


PR `#893` даёт очень земную проблему: многострочный вывод читается плохо, если префикс есть только на первой строке. PR явно говорит, что цель — сделать вывод рабочего процесса более читаемым и помочь понимать, какие строки к какому действию относятся. Он включает скриншоты старого/нового вывода терминала и логов. Примечание ревьюера объясняет, почему строки продолжения используют точки вместо пробелов: префикс из пробелов мог бы выглядеть как сбой отрисовки или потерянная строка, а будущий `.strip` где-нибудь ещё мог бы незаметно схлопнуть его. [PR #893](https://github.com/Shopify/roast/pull/893)

После этого PR-стек переходит от правки отображения к представлению событий. В том же стеке, управляемом Graphite, `#898` добавляет событие типа `block`, `#899` использует `block events` в Claude, `#900` — в chat cogs, `#901` — в Pi agent cogs, `#902` — для статистики LLM, а `#903` помечает исходный поток сообщений лога. `#903` формулирует конкретный рефакторинг: сообщения лога получают атрибут `type`, чтобы `LogFormatter#colourize` был устойчивее; поскольку сообщения теперь могут быть либо строками, либо `Roast::Log::Message`, `CustomLogging` нормализует их через `.to_s`. [PR #893](https://github.com/Shopify/roast/pull/893), [PR #898](https://github.com/Shopify/roast/pull/898), [PR #899](https://github.com/Shopify/roast/pull/899), [PR #900](https://github.com/Shopify/roast/pull/900), [PR #902](https://github.com/Shopify/roast/pull/902), [PR #903](https://github.com/Shopify/roast/pull/903)


<figure class="source-figure" id="fig-story-15-shopify-log-prefix-pr-893">
  <img src="../assets/story-images/15-shopify-log-prefix-pr-893.webp" alt="Скриншот PR #893 старого/нового вывода терминала и логов для повторяющегося префикса лога в многострочном выводе." loading="lazy" />
  <figcaption>PR #893 стоит показать отдельно от #903: здесь виден исходный дефект читаемости, где многострочный вывод трудно привязать к действию. Источник: <a href="https://github.com/Shopify/roast/pull/893">Shopify/roast PR #893</a>. Локальный файл: <code>../assets/story-images/15-shopify-log-prefix-pr-893.webp</code>.</figcaption>
</figure>

<figure class="source-figure" id="fig-story-15-shopify-log-message-pr-903">
  <img src="../assets/story-images/15-shopify-log-message-pr-903.webp" alt="Скриншот PR #903 с описанием атрибута type у Roast::Log::Message и устойчивости LogFormatter." loading="lazy" />
  <figcaption>PR #903 нужен как конкретная сцена сопровождения: вывод `prompt`/`response` становится типизированной инфраструктурой логов/событий, потому что людям нужен устойчивый показ агентских свидетельств. Источник: <a href="https://github.com/Shopify/roast/pull/903">Shopify/roast PR #903</a>. Локальный файл: <code>../assets/story-images/15-shopify-log-message-pr-903.webp</code>.</figcaption>
</figure>

Эта линия важна для системности всей истории. Roast переводит ИИ-работу в файлы и рабочие процессы, но затем сам должен обеспечить наблюдаемость этих рабочих процессов. Скрытый или нечитаемый ответ агента нельзя хорошо проверить. Статистика токенов, промпты, ответы, agent sessions и вывод команд требуют семантики форматирования. Иначе рабочий процесс как код порождает размытый рабочий процесс.

## 12. Рабочий процесс второго порядка: ИИ-сгенерированная документация тоже требует проверки

Четвёртая поздняя граница — документация. PR `#868` остаётся черновым. Он предлагает подробную архитектурную документацию, сгенерированную LLM. Автор прямо пишет, что прогнал несколько автоматических проходов проверки, но не полностью уверен, что всё корректно. Эта оговорка важнее самого факта генерации документации: архитектурная документация здесь становится ИИ-артефактом, который ещё нуждается в проверке, а не готовым источником истины. [PR #868](https://github.com/Shopify/roast/pull/868)

PR `#892` связан с ним как черновой рабочий процесс для проверки/обновления внутренней архитектурной документации. Связка `#868`, `#892` и работы над документацией внутренних комментариев показывает не “сгенерировали документацию и положили в репозиторий”, а следующий уровень самой логики Roast: если документация создаётся ИИ-шагом, вокруг неё тоже нужен рабочий процесс проверки и обновления. [PR #892](https://github.com/Shopify/roast/pull/892)

<figure class="source-figure" id="fig-story-15-shopify-architecture-docs-pr-868">
  <img src="../assets/story-images/15-shopify-architecture-docs-pr-868.webp" alt="Скриншот чернового PR #868: LLM-сгенерированная архитектурная документация и оговорка о корректности." loading="lazy" />
  <figcaption>PR #868 полезен как граничный кейс: сгенерированные архитектурные документы ценны, но даже сопровождающий говорит, что автоматическая проверка не сделала корректность гарантированной. Источник: <a href="https://github.com/Shopify/roast/pull/868">Shopify/roast PR #868</a>. Локальный файл: <code>../assets/story-images/15-shopify-architecture-docs-pr-868.webp</code>.</figcaption>
</figure>


Эти PR не должны занимать больше места, чем основные примеры рабочих процессов. Но они добавляют важную позднюю ноту: структурированные ИИ-рабочие процессы порождают рабочие процессы второго порядка. Сначала ИИ помогает писать код; потом ИИ генерирует документацию для агентов/новых участников; потом нужен рабочий процесс для проверки этой документации. История закольцовывается не случайно: рабочий процесс становится способом производить и проверять следующие артефакты рабочего процесса.

## 13. Что эта история добавляет к корпусу

Shopify Roast добавляет в корпус форму, которую нельзя заменить ни Stripe, ни Armin, ни HumanLayer. Stripe показывает платформенную основу корпоративного уровня: агенты наследуют devboxes, анализаторы, blueprints и внутренние инструменты. Armin показывает маленькую изменяемую обвязку под контролем одного toolsmith. HumanLayer показывает обвязку и back-pressure вокруг производственного рабочего процесса. Shopify показывает **рабочий процесс как код для ИИ-шагов**: Ruby DSL, где ИИ-вызовы, coding agent-вызовы, shell-команды, Ruby-логика, сессии, `map`, `repeat` и форматирование вывода становятся одним исполняемым объектом.

Главный переносимый урок не “надо взять Roast”. Главный урок — не давать агенту владеть всей процедурой. Если у задачи есть детерминированная подготовка, поставь её до агента. Если вывод модели должен попасть к другой аудитории, оформи эту трансформацию как отдельный шаг. Если сессию нужно разветвить, задай это явно. Если пакетная обработка идёт по многим файлам, вырази семантику коллекции. Если важна повторная попытка, положи `repeat`/`break!`/`outputs` в рабочий процесс. Если провайдеры отличаются, сделай выбор модели частью конфигурации. Если вывод служит свидетельством, отформатируй его как свидетельство. Если документация создана ИИ, дай ей рабочий процесс проверки вместо того, чтобы считать её авторитетным источником.

Эта история также меняет отношение к проектированию промптов. В Roast промпт остаётся важным, но промпт уже не весь артефакт. Главный артефакт — файл, который можно проверить, запустить, изменить, версионировать и разложить на части. Именно поэтому Roast нужен в основном корпусе: он даёт практическую форму перехода от ситуативного промптинга к исполняемой агентской процедуре.

## 14. Ограничения источников и открытые края

База источников неровная. Статья Shopify Engineering — основной источник для публичного запуска, Boba, ранней YAML-формы, CodingAgent, встроенных инструментов и внутренних сценариев использования, но она не раскрывает внутренние файлы рабочих процессов, метрики, PR, дифф, стоимость или частоту ошибок. Пост Doubrovkine силён как реальный внешний запуск старого YAML-рабочего процесса оценки, но это локальное выполнение одного пользователя, а не доказательство крупномасштабного внутреннего эффекта.

GitHub README, учебные материалы, конфигурационные файлы, релизы, issues и PR сильны для публичной механики фреймворка. Они показывают реальные поверхности DSL, примерные рабочие процессы, конфигурацию провайдеров, возобновление сессий, обработку коллекций, переходы релизов и трение сопровождения. Они не доказывают, что каждый паттерн развёрнут в Shopify в масштабе. Некоторые источники заведомо черновые/неполные: `#868` и `#892` нужно читать как открытое/черновое свидетельство, а не как законченный конвейер архитектурной документации.

Главный открытый край: Boba — самый важный внутренний кейс, но публичный материал даёт только форму, а не полный запуск. Внешний пример оценки даёт полный запуск, но не внутреннюю производственную проблему Shopify. Поэтому история держится на двух дополняющих слоях: внутренняя мотивация и Boba-паттерн от Shopify; публичная исполняемая механика из репозитория, учебных материалов, блога и PR.

## 15. Карта источников

- [Shopify Engineering — “Introducing Roast: Structured AI workflows made easy”](https://shopify.engineering/introducing-roast) — основной источник для рамки запуска, мотивации Augmented Engineering DX, Boba, ранней YAML/промпт-структуры, CodingAgent, встроенных инструментов, общего контекста, воспроизведения сессии, внутренних сценариев использования и позиции с человеком в контуре.
- [Daniel Doubrovkine — “Executing Structured A.I. Workflows with Shopify Roast”](https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html) — основной/полевой источник для внешнего запуска старого YAML-оценивания: настройки OpenAI, правки `workflow.yml`, команды, лога выполнения, прогона Minitest, итогового отчёта и сравнения моделей.
- [RubyDoc snapshot for Shopify/roast](https://rubydoc.info/github/Shopify/roast) — источник по старой YAML-поверхности: типам шагов, выполнению команд, префиксу агентского шага, продолжению/возобновлению сессии, шагам shell script/input и старой модели `roast execute workflow.yml`.
- [Shopify/roast README](https://github.com/Shopify/roast/blob/main/README.md) — источник по текущей Ruby DSL: `execute do`, `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call`, установке, конфигурации провайдера и карте учебных материалов.
- [`roast-ai.gemspec`](https://github.com/Shopify/roast/blob/main/roast-ai.gemspec) и [`lib/roast/cli.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cli.rb) — источники по имени gem, требованию Ruby, зависимостям, CLI-командам, разрешению пути рабочего процесса и обработке target/argument.
- [Shopify/roast releases](https://github.com/Shopify/roast/releases) — источник по предупреждению об устаревании legacy-функциональности в `v0.5.2`, переходу `v1.0.0` к Ruby DSL, уточнениям log/session в `v1.0.1`/`v1.0.2` и изменениям agent/provider/session в `1.1.0`.
- [PR #519](https://github.com/Shopify/roast/pull/519), [PR #521](https://github.com/Shopify/roast/pull/521), [PR #524](https://github.com/Shopify/roast/pull/524) — маркеры перехода: предварительная версия 1.0, DSL init и новый README.
- [`tutorial/02_chaining_cogs/code_review.rb`](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb) — источник по конкретному рабочему процессу проверки безопасности: agent → chat → chat → ruby.
- [`tutorial/02_chaining_cogs/session_resumption.rb`](https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb) — источник по возобновлению chat- и agent-сессий, ветвлению контекста и присваиванию сессий.
- [`tutorial/07_processing_collections`](https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md) — источник по `map`, `collect`, `reduce`, упорядоченным результатам, доступу к конкретной итерации и параллельному выполнению.
- [`tutorial/08_iterative_workflows`](https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md) — источник по `repeat`, `break!`, `next!`, `outputs`, максимальному числу итераций и передаче значения между итерациями.
- [`lib/roast/cogs/chat/config.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/chat/config.rb) и [`lib/roast/cogs/agent/config.rb`](https://github.com/Shopify/roast/blob/main/lib/roast/cogs/agent/config.rb) — источники по текущим деталям `provider`/`config` в коде.
- [PR #888](https://github.com/Shopify/roast/pull/888) — кейс сопровождения документации провайдеров: выбор `config` рабочего процесса, отсутствие глобального переключателя CLI/env, провайдеры `agent`, помощь Codex, пределы проверки.
- [Issue #875](https://github.com/Shopify/roast/issues/875) и [Issue #882](https://github.com/Shopify/roast/issues/882) — трение вокруг открытого проекта из-за устаревших моделей и документации `provider`/`env`.
- [PR #468](https://github.com/Shopify/roast/pull/468) — кейс сопровождения имён файлов сессий/длины пути и ревью о том, где должна жить логика state-path.
- [Issue #896](https://github.com/Shopify/roast/issues/896), [PR #893](https://github.com/Shopify/roast/pull/893), [PR #898](https://github.com/Shopify/roast/pull/898), [PR #899](https://github.com/Shopify/roast/pull/899), [PR #900](https://github.com/Shopify/roast/pull/900), [PR #902](https://github.com/Shopify/roast/pull/902), [PR #903](https://github.com/Shopify/roast/pull/903) — форматирование `prompt`/`response`, повторяющийся префикс лога, представление `block`-событий, статистика LLM и линия сопровождения типизированных сообщений лога.
- [PR #868](https://github.com/Shopify/roast/pull/868) и [PR #892](https://github.com/Shopify/roast/pull/892) — черновая линия архитектурной документации: LLM-сгенерированная архитектурная документация и рабочий процесс для её проверки/обновления.

## Временный список ассетов для скачивания

- `../assets/story-images/15-shopify-roast-structured-workflow-article.webp` — URL источника: `https://shopify.engineering/introducing-roast`. Нужен как стартовая иллюстрация для структурированного ИИ-рабочего процесса / ранней YAML-поверхности. Статус: не скачано.
- `../assets/story-images/15-shopify-boba-coding-agent.webp` — URL источника: `https://shopify.engineering/introducing-roast`. Нужен для внутренней сцены Boba: детерминированная очистка → Sorbet autocorrect → CodingAgent → тесты/проверка типов. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-model-config-diff.webp` — URL источника: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для адаптации модели/API-токена в `workflow.yml`. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-workflow-log.webp` — URL источника: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для лога выполнения с именованными шагами, Ruby-файлами, Minitest и путём итогового вывода. Статус: не скачано.
- `../assets/story-images/15-shopify-dblock-grade-report.webp` — URL источника: `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html`. Нужен для итогового отчёта об оценке и категорий рубрики. Статус: не скачано.
- `../assets/story-images/15-shopify-rubydoc-yaml-agent-step.webp` — URL источника: `https://rubydoc.info/github/Shopify/roast`. Нужен для устаревшего префикса YAML agent-step и семантики продолжения/возобновления сессии. Статус: не скачано.
- `../assets/story-images/15-shopify-release-v1-dsl.webp` — URL источника: `https://github.com/Shopify/roast/releases`. Нужен для перехода `v1.0.0` к Ruby DSL. Статус: не скачано.
- `../assets/story-images/15-shopify-readme-quick-example.webp` — URL источника: `https://github.com/Shopify/roast/blob/main/README.md`. Нужен для текущей последовательности README `cmd` → `agent` → `chat`. Статус: не скачано.
- `../assets/story-images/15-shopify-code-review-tutorial.webp` — URL источника: `https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/code_review.rb`. Нужен для agent → chat → chat → Ruby-отчёта. Статус: не скачано.
- `../assets/story-images/15-shopify-session-resumption.webp` — URL источника: `https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb`. Нужен для присваивания сессии и ветвления контекста. Статус: не скачано.
- `../assets/story-images/15-shopify-map-collections.webp` — URL источника: `https://github.com/Shopify/roast/blob/main/tutorial/07_processing_collections/README.md`. Нужен для `map`, `collect`, `reduce`, параллельных и упорядоченных результатов. Статус: не скачано.
- `../assets/story-images/15-shopify-repeat-cog.webp` — URL источника: `https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md`. Нужен для `repeat`, `break!`, `next!`, `outputs`. Статус: не скачано.
- `../assets/story-images/15-shopify-provider-pr-888.webp` — URL источника: `https://github.com/Shopify/roast/pull/888`. Нужен для сопровождения документации конфигурации провайдера, помощи Codex и пределов проверки. Статус: не скачано.
- `../assets/story-images/15-shopify-pr-468-session-filenames.webp` — URL источника: `https://github.com/Shopify/roast/pull/468`. Нужен для кейса состояния с именами файлов сессий/длиной пути. Статус: не скачано.
- `../assets/story-images/15-shopify-log-prefix-pr-893.webp` — URL источника: `https://github.com/Shopify/roast/pull/893`. Нужен для старого/нового вывода терминала и логов вокруг проблемы многострочного префикса. Статус: не скачано.
- `../assets/story-images/15-shopify-log-message-pr-903.webp` — URL источника: `https://github.com/Shopify/roast/pull/903`. Нужен для типизированных сообщений лога / устойчивости LogFormatter. Статус: не скачано.
- `../assets/story-images/15-shopify-architecture-docs-pr-868.webp` — URL источника: `https://github.com/Shopify/roast/pull/868`. Нужен для LLM-сгенерированной документации как чернового свидетельства. Статус: не скачано.
