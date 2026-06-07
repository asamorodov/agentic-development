# Агентская разработка как карта текущих течений
## Часть I. Как читать карту течений
### Зачем нужна отдельная теоретическая часть
### Что эта карта должна дать читателю {#what-the-map-should-give-reader}
### Источник в карте — это тип сигнала, а не украшение ссылкой {#source-as-signal-type}
### Что считать течением, а что считать примером {#what-counts-as-current}
### Отрицательная граница тоже является материалом карты {#negative-boundary-as-map-material}
### Течение, контур и режим — разные уровни карты
### Как пользоваться уровнями карты без лишней иерархии {#theory-map-levels-without-overhead}
### Модель стала достаточно сильной, чтобы проблема переместилась наружу
### Почему новый материал должен быть плотным, а не просто “современным” {#new-material-density-principle}
### Эмпирическая оговорка: агент ускоряет не любую систему {#ai-does-not-accelerate-every-system}
### Как читать эмпирические исследования без ложной уверенности {#how-to-read-empirical-studies-without-false-certainty}
### Эмпирический источник надо читать через его поверхность наблюдения {#empirical-source-observation-surface}
### Что не должно попасть в карту как самостоятельная часть {#what-should-not-become-separate-part}
### Что уже работает, что вероятно усилится, а что пока рано нормировать {#51-chto-uzhe-rabotaet-chto-veroyatno-usilitsya-a-chto-poka-rano-normirovat}
## Часть II. Реальные сессии, PR и изменение работы разработчика
### Агентская сессия как последовательность действий
### Что видно в полной трассе агентской сессии {#full-agent-session-trace}
### Трасса сессии — это пакет свидетельств, а не стенограмма чата {#session-trace-as-evidence-package}
### Выживание кода как отдельный фильтр {#code-survival-as-filter}
### Pushback как наблюдаемый сигнал качества взаимодействия {#pushback-as-observable-signal}
### Ограничение SWE-chat: сессия видна, но не вся инженерная работа {#swe-chat-limitations}
### Постепенная спецификация и короткие коррекции
### Progressive specification не отменяет план, но объясняет, когда план появляется {#progressive-specification-and-plan}
### Постепенная спецификация должна оставлять состояние, иначе она снова становится шумом {#progressive-specification-must-leave-state}
### Делегирование диагностики, понимания и проверки {#delegating-diagnosis-comprehension-validation}
### Контекстная инъекция и переговоры об автономии {#context-injection-and-autonomy-negotiation}
### Постепенная спецификация как нормальная форма работы {#progressive-specification-as-normal-form}
### Рассогласование видно по вмешательствам разработчика
### Семь форм рассогласования и почему они не сводятся к “модель ошиблась” {#seven-misalignment-forms}
### Рассогласование как цена несовпадения рабочей модели агента и проекта {#misalignment-as-model-project-mismatch}
### Effort cost и trust cost как реальные расходы процесса {#effort-and-trust-costs}
### Inaccurate self-reporting как отдельный сбой {#inaccurate-self-reporting-as-failure}
### Рассогласование должно возвращаться в рабочую систему {#misalignment-must-feed-back-into-system}
### Агентский PR как отдельная поверхность
### PR сообщает не только код, но и форму работы агента {#pr-communicates-agent-work}
### PR lifecycle как место, где агентская работа становится социальной {#pr-lifecycle-social-surface}
### Описание PR как часть результата агента {#pr-description-as-agent-result}
### Описание PR тоже должно проверяться, потому что оно становится интерфейсом ревью {#pr-description-must-be-verified}
### Результат агента может закончиться до merge, но не исчезнуть {#agent-output-before-merge}
### Почему часть агентского результата не становится кодом проекта
### Полезный результат сессии не всегда является кодом, но это надо фиксировать {#useful-session-output-not-always-code}
### Изменение работы разработчика: от создания к направлению и проверке
### Надзорная инженерная работа имеет собственную стоимость {#supervisory-engineering-cost}
## Часть III. Контуры владения, акторы и право завершения
### Агент как участник процесса, но не владелец результата
### Актор не равен исполнителю команды {#actor-not-command-executor}
### Роль агента надо описывать через артефакты, иначе акторность становится риторикой {#agent-role-through-artifacts}
### Двусторонние артефакты вместо неформального чата
### Почему SASE важен именно как карта ролей и артефактов {#why-sase-matters-as-role-artifact-map}
### BriefingScript, LoopScript и MentorScript как разные типы общения {#briefing-loop-mentor-scripts}
### Consultation Request Pack: агент должен уметь спрашивать, а не только исполнять {#consultation-request-pack}
### Merge-Readiness Pack: готовность должна доказываться, а не декларироваться {#merge-readiness-pack}
### Пакеты запроса и пакеты готовности как новая форма инженерной коммуникации {#consultation-and-readiness-packs}
### Три контура владения
### Три контура отличаются не масштабом, а устройством ответственности {#three-contours-responsibility}
### Локальный контур: человек может держать больше неявного состояния {#local-contour-implicit-state}
### Платформенный контур: свобода агента покупается инфраструктурой {#platform-contour-buys-autonomy-with-infrastructure}
### Платформенная автономия покупается инфраструктурой, а не верой в модель {#platform-autonomy-as-infrastructure-product}
### Внешний контур: входящий поток может быть полезным кодом и всё равно вредной нагрузкой {#external-contour-review-burden}
### Кто платит за проверку {#who-pays-for-verification}
### Раскрытие использования AI не переносит право завершения {#disclosure-does-not-transfer-completion-right}
### Право завершения как отдельный объект проектирования {#completion-right-as-design-object}
### Право завершения
### Операционная инициативность и право слияния расходятся {#operational-agency-vs-merge-governance}
### Опыт участника проекта меняет проверку агентского результата {#core-peripheral-agent-use}
### `Human in the loop` слишком слабая формула {#41-human-in-the-loop-slishkom-slabaya-formula}
### Человеческое внимание нужно ставить в точки максимального рычага {#42-chelovecheskoe-vnimanie-nuzhno-stavit-v-tochki-maksimalnogo-rychaga}
### Человек остаётся владельцем того, что нельзя свести к датчику {#43-chelovek-ostaetsya-vladeltsem-togo-chto-nelzya-svesti-k-datchiku}
### Подтверждение как граница ответственности {#21-podtverzhdenie-kak-granitsa-otvetstvennosti}
### Автономия — не свойство модели, а договор с окружением {#45-avtonomiya-ne-svoystvo-modeli-a-dogovor-s-okruzheniem}
### Область действия и чрезмерная инициативность {#46-oblast-deystviya-i-chrezmernaya-initsiativnost}
## Часть IV. Локальная палитра режимов работы
### Локальный режим выбирается по задаче, а не по вкусу к инструменту
### Лёгкий разговорный режим: контроль остаётся внутри человека
### Работа в незнакомом участке: сначала карта, потом изменение
### План до кода: когда первая неверная карта дорого стоит
### Исследование кодом: агент производит проверяемый артефакт
### Браузерный цикл: когда файлового чтения недостаточно
### Проверка до исправления: багфикс начинается с сигнала сбоя
### PR-сопровождение: локальная работа продолжается после `push`
### Внешняя память задачи: защита не только агента, но и человека
### Песочница, права и рабочие деревья решают разные задачи {#47-pesochnitsa-prava-i-rabochie-derevya-reshayut-raznye-zadachi}
### Навыки, хуки и скрипты: ремонтировать повторяемый сбой, а не украшать процесс
### Простые инструменты и код против тяжёлой инструментальной поверхности
### Подготовка до запуска агента: когда контекст надо собрать заранее
### Как выбирать локальный режим
### Последняя граница локальной палитры
## Часть V. Спецификации, SPDD и артефакты намерения
### Хороший запрос больше не является единицей управления процессом
### Долговременный контекст, спецификация и передача состояния — разные вещи {#9-dolgovremennyy-kontekst-spetsifikatsiya-i-peredacha-sostoyaniya-raznye-veschi}
### Почему спецификационный слой выделяется отдельно {#spec-layer-why-separate}
### Семейство спецификационных режимов: spec-first, spec-anchored и spec-as-source {#spec-family-spec-first-anchored-source}
### Спецификация, план, конституция и передача состояния — разные артефакты {#spec-plan-constitution-handoff}
### Артефакт намерения: prompt как delivery artifact {#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli}
### Что SPDD добавляет к SDD и почему это не просто spec-first {#spdd-adds-to-sdd}
### OpenSPDD: когда метод получает командный слой {#openspdd-command-layer}
### Spec Kit: конституция, требования, план, задачи и реализация {#spec-kit-constitution-spec-plan-tasks}
### Kiro: `requirements.md`, `design.md`, `tasks.md` и режимы применения {#kiro-requirements-design-tasks}
### Constitutional SDD: когда ограничения безопасности становятся частью спецификации {#constitutional-sdd-security-constraints}
### TDAD: поведение агента как проверяемый артефакт {#tdad-agent-behavior-as-artifact}
### Шесть стадий SPDD: распределённое подтверждение намерения {#spdd-six-step-workflow}
### Story shaping: сырое требование ещё не является входом для Canvas {#spdd-story-shaping}
### Analysis context: strategic clarity до implementation detail {#spdd-analysis-context}
### REASONS Canvas: intent, design, execution, governance {#spdd-reasons-canvas-intent-design-execution-governance}
### Три core skills SPDD: Abstraction First, Alignment, Iterative Review {#spdd-three-core-skills}
### Generate code: модель реализует locked intent, а не ищет решение заново {#spdd-generate-locked-intent}
### Проверяемые свидетельства: API tests до глубокого code review {#spdd-validation-review-evidence}
### Logic correction, prompt-update и sync: два направления обратной связи {#spdd-prompt-update-sync}
### Unit tests: последний safety net, а не первый источник смысла {#spdd-unit-tests-after-stabilization}
### Asset integrity: prompt version должен соответствовать code commit {#spdd-asset-integrity}
### Где SPDD окупается: ROI, upfront cost и fit table {#spdd-fit-and-roi}
### Hotfixes и production signal: governance можно отложить, но нельзя выбросить {#spdd-hotfix-production-signal}
### Roadmap SPDD: от expert craft к organization-level asset system {#spdd-roadmap-decision-memory}
### Сопротивление SPDD: variance, model drift, spec-as-source и предел человеческого суждения {#spdd-resistance-boundaries-and-spec-as-source}
### Mise en Place: подготовка контекста до запуска агентов {#mise-en-place-preparation-before-agents}
### Structured workflow вместо свободной спецификации: Roast и граница SPDD {#structured-workflow-vs-specification}
### Как выбирать спецификационный режим {#choosing-specification-mode}
### Как спецификационная линия проявляется в корпусе историй {#specification-line-in-stories}
### Где спецификационный подход может мешать {#specification-approach-can-hurt}
## Часть VI. Среда агента: интерфейс, обвязка, контекст и инструменты
### Агент как петля, а не одноразовый ответ
### Agent-computer interface: интерфейс как часть качества агента {#agent-computer-interface}
### Гранулярность действия: интерфейс должен помогать маленьким обратимым шагам {#aci-action-granularity}
### Ошибка должна возвращаться как рабочий сигнал, а не как длинный шум {#aci-error-signal}
### “Агент = модель + обвязка” — полезная, но неполная формула {#4-agent-model-obvyazka-poleznaya-no-nepolnaya-formula}
### Обвязка как среда выполнения: обязанности, а не набор украшений {#harness-runtime-substrate}
### Одиннадцать обязанностей обвязки: что именно должно быть спроектировано {#harness-eleven-responsibilities}
### Уровни зрелости обвязки: от финального patch к проверяемому эпизоду {#harness-levels-episode-package}
### Инструментальные поверхности: что интерфейс делает видимым и что прячет {#tool-surfaces}
### Claude Code как пример: маленькая петля и большая система вокруг неё {#claude-code-design-space}
### Claude Code показывает, что CLI-агент уже является системой, а не одной командой {#claude-code-cli-as-system}
### Права, песочница и подтверждения: разные элементы одной границы {#permissions-sandbox-approvals-boundary}
### Контекст — не окно, а рабочее состояние {#6-kontekst-ne-okno-a-rabochee-sostoyanie}
### Операции над контекстом: записать, выбрать, сжать, изолировать {#context-operations-write-select-compress-isolate}
### Коллапс контекста и эволюционирующие инструкции {#context-collapse-evolving-playbooks}
### Контекстная инженерия в coding-agent: где живёт знание проекта {#coding-agent-context-engineering}
### Постоянный контекст должен быть оглавлением, а не складом инструкций {#persistent-context-as-index}
### Конфигурационный долг: правила тоже устаревают {#configuration-debt}
### Контекстные интерфейсы: кто решает, что загрузить {#7-kontekstnye-interfeysy-kto-reshaet-chto-zagruzit}
### Конфигурация агентских инструментов: что уже стало обычной практикой {#agentic-tool-configuration}
### Восемь механизмов конфигурации: context files уже победили, но это только начало {#eight-configuration-mechanisms}
### Кодовая база как контекстный интерфейс {#8-kodovaya-baza-kak-kontekstnyy-interfeys}
### Проект как обучающая среда для агента {#project-as-agent-learning-environment}
### Обвязка регулирует не “модель вообще”, а конкретное состояние кодовой базы {#11-obvyazka-reguliruet-ne-model-voobsche-a-konkretnoe-sostoyanie-kodovoy-bazy}
### Направляющие и датчики {#12-napravlyayuschie-i-datchiki}
### Качество надо держать левее {#13-kachestvo-nado-derzhat-levee}
### Поддерживаемость, архитектура и поведение проверяются по-разному {#14-podderzhivaemost-arhitektura-i-povedenie-proveryayutsya-po-raznomu}
### Пригодность проекта к обвязке {#15-prigodnost-proekta-k-obvyazke}
### Среда сама подталкивает агента к правильному {#16-sreda-sama-podtalkivaet-agenta-k-pravilnomu}
### Шаблоны и топологии: уменьшение разнообразия как способ контроля {#17-shablony-i-topologii-umenshenie-raznoobraziya-kak-sposob-kontrolya}
### Навыки как процедурные артефакты с жизненным циклом {#skills-lifecycle-procedural-artifacts}
### Progressive disclosure: skill должен открываться по необходимости {#skills-progressive-disclosure}
### Жизненный цикл навыка: представить, получить, выбрать, изменить {#skills-lifecycle}
### Навыки, хуки и подагенты {#18-navyki-huki-i-podagenty}
### Агенту нужен не только чат, но и среда выполнения {#19-agentu-nuzhen-ne-tolko-chat-no-i-sreda-vypolneniya}
### Поток работы как объект {#20-potok-raboty-kak-obekt}
### Долгоживущая задача требует восстановления, а не только памяти {#22-dolgozhivuschaya-zadacha-trebuet-vosstanovleniya-a-ne-tolko-pamyati}
### Большая часть сложности агентской системы находится не в модели {#23-bolshaya-chast-slozhnosti-agentskoy-sistemy-nahoditsya-ne-v-modeli}
### Наблюдаемость: след агентской работы должен быть инженерным артефактом {#agent-observability-episode-package}
### Пакет эпизода: что надо сохранить после работы агента {#episode-package-contents}
### Наблюдаемость контекста: нужно видеть не только tool calls {#context-observability}
### Самоизменяющаяся обвязка: проверяемые изменения вместо стихийного самоулучшения {#observability-driven-harness-evolution}
### Агентский маховик: агент помогает улучшать среду, но не должен владеть ею {#44-agentskiy-mahovik-agent-pomogaet-uluchshat-sredu-no-ne-dolzhen-vladet-eyu}
### MCP как расширение границы доверия {#48-mcp-kak-rasshirenie-granitsy-doveriya}
### Code execution with MCP: иногда инструмент лучше представить как код, а не как список tool definitions {#code-execution-with-mcp}
### Три границы доверия в MCP: клиент, сервер, downstream-система {#mcp-trust-boundaries}
## Часть VII. Организационные и многоагентные рабочие системы
### Почему организационный режим нельзя выводить из локальной сессии
### Spotify Honk: фоновый PR-поток внутри уже существующей платформы
### Stripe Minions: промышленный one-shot PR-поток и вопрос о публичной фактуре
### Shopify Roast: структура рабочего процесса вместо свободного roaming agent
### Quix / Klaus Kode: детерминированная оболочка вокруг агента
### Armin Ronacher: простой код как противоядие от тяжёлой инструментальной поверхности
### Task graph и внешняя память: когда рабочего процесса уже недостаточно
### Граф задач как внешняя память агента {#24-graf-zadach-kak-vneshnyaya-pamyat-agenta}
### Gas Town: многоагентная организация с ролями, но не без трения
### Anthropic parallel Claudes: дорогой край автономного параллелизма
### Multi-agent research system: когда параллельность действительно естественна
### Cognition и спор вокруг multi-agent architectures
### MetaMorph и file-lock-параллелизм как переносимый минимальный паттерн
### Как выбирать между платформой, рабочим процессом, графом задач и multi-agent режимом
### Нужно ли делить эту часть на две
### Вывод для будущего dev-process
### Редакторская проверка после структурного насыщения
## Часть VIII. Проверка, ревью, бенчмарки и долгосрочное качество
### Агенту нельзя верить на слово, но и человека нельзя превращать в ручной линтер {#34-agentu-nelzya-verit-na-slovo-no-i-cheloveka-nelzya-prevraschat-v-ruchnoy-lint}
### Надёжность вывода: почему уверенность агента не равна правоте {#output-reliability}
#### Developer pushback как источник знания о сбое
#### Что доказывают зелёные тесты
#### Как отличать найденный баг от бага, созданного тестом
#### Надёжность вывода и внешний контекст
#### Когда выводу можно доверять достаточно
### Доказательство работы зависит от типа задачи {#35-dokazatelstvo-raboty-zavisit-ot-tipa-zadachi}
### Benchmark evidence тоже имеет область применимости {#benchmark-evidence-scope}
### Поведенческая проверка остаётся слабым местом {#36-povedencheskaya-proverka-ostaetsya-slabym-mestom}
### Логирование и наблюдаемость нельзя оставлять текстовой просьбе {#37-logirovanie-i-nablyudaemost-nelzya-ostavlyat-tekstovoy-prosbe}
### Наблюдаемость агента отличается от наблюдаемости продукта {#agent-observability-not-product-observability}
### Комментарии ревью — это сигналы, а не команды {#38-kommentarii-revyu-eto-signaly-a-ne-komandy}
#### PR — это коммуникационный артефакт, а не упаковка diff
### Свидетельства должны быть пригодны для следующего шага {#39-svidetelstva-dolzhny-byt-prigodny-dlya-sleduyuschego-shaga}
#### Evidence package не должен быть гладким summary
#### Intent debt и verification debt
### Эмпирические предупреждения: скорость генерации не равна качеству {#40-empiricheskie-preduprezhdeniya-skorost-generatsii-ne-ravna-kachestvu}
### Практический вывод: проверка должна менять среду {#part-viii-practical-conclusion}
## Часть IX. Внешняя граница: open source, происхождение вклада, безопасность и право отказа
### Жёсткая линия: происхождение важнее потенциальной пользы
### LLVM: ревью-время, обучение и “extractive contribution”
### Linux Kernel и Ghostty: человек остаётся сертифицирующим субъектом
### Governance бывает неловким: Gentoo и Debian
### Право закрыть автоматизированный вклад: scikit-learn, FastAPI и GNOME Shell Extensions
### Foundation-level policies: disclosure без снятия ответственности
### Security reports: когда шум похож на полезный сигнал
### Эмпирический слой: не вся активность становится полезным вкладом
### Когда кейс должен остаться в главе, а когда уйти в карту источников
### Вывод для карты течений
## Заключение. Что из карты должно перейти в практику
### Как пользоваться картой без превращения её в методологию
### Что реальные сессии добавляют к общей картине
### SPDD задаёт эталон глубины, но не единственную норму
### Что уже стало рабочей реальностью
### Агент может действовать, но не должен владеть завершением
### Проверка и внешний контур задают предел расширения
### Что пока не стоит нормировать
### Локальные режимы остаются нужными, но требуют явных условий
### Практический вывод для Handbook {#52-prakticheskiy-handbook-dolzhen-stat-kartoy-vybora-rezhima}
### Статус новых источник-кейсов
### Итоговая рамка {#53-itogovaya-ramka}
## Карта источников {#54-karta-istochnikov}
### Новые источник-кейсы Итерации 3
#### Spotify Honk
#### Anthropic parallel Claudes
#### Open-source AI policy cluster
### Основные теоретические источники
### Agent-first / agent-loop / context engineering
### Skills, subagents and agent system architecture
### Gas Town / Beads / многоагентная рабочая среда
### Безопасность, область действия и наблюдаемость
### Эмпирические предупреждения и организационный слой
