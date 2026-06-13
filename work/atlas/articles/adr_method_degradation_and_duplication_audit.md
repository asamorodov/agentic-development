# adr_method — degradation and duplication audit

Статус: P01 initial audit.

## Проверка против деградации

- Статья не пересказывает досье подряд: основной порядок построен вокруг reader question, статуса решения, жизненного цикла, confirmation, операционной проекции, исследования AI/ADR, reconstruction, failures and boundaries.
- Наличие technical anchors: Nygard fields, `doc/arch/adr-NNN.md`, status values, adr-tools commands, AWS process, ArchUnit, CODEOWNERS, oasdiff/Pact/k6/SLO/Prometheus/Argo examples.
- Hard coverage matrix не создана; ledger фиксирует только реальные решения переноса.
- Внутренние досье и фрагменты не используются как публичные citations.

## Риски P01

- исследования AI/ADR пока дан обзорно; source-depth passes должны уточнить отдельные claims.
- Visual layer пока не выполнен; image candidates должны получить disposition.
- Операционная проекция ADR дана как модель; позже стоит усилить примерами из source-specific workflows.


## P02 — contract and boundaries

Reader question, tier, neighboring article boundaries and C5/A10 sync were clarified in the main article. ADR is now framed as a protected decision-profile article, not a template catalogue, generic governance overview, Spec Kit/TDAD/Constitutional SDD substitute, PWG substitute or A2/A8/A10 repeat.


## P03 — dossier inventory

Досье сверено без тотальной coverage matrix. Article-critical gaps closed: architectural diff after agent run, status/review finder, active-context/guardrails risk. Remaining source-depth and visual debts recorded in ledger/open questions.


## P05 — AI/ADR source-depth

Усилен слой исследования AI/ADR without literature-review drift: generation as draft, retrieval-aware generation, Context Matters active window, violation detection as triage, AgenticAKM as reconstruction pipeline, traceability as evidence-bound candidate links.


## P06 — confirmation source-depth

Усилен слой confirmation: добавлена шестиуровневая шкала, YAML-shaped technical anchors for structural/ownership/API/operations/rollout confirmation, уточнены CODEOWNERS details and boundary that checks are projections of ADR confirmation, not substitutes for the decision.


## P07 — lifecycle and failure modes

Усилены lifecycle boundaries through function: specification/Spec Kit/CSDD hold intent and constraints; TDAD/contracts expose behavioral errors; PWG holds durable work state/gates; ADR records decision status, origin, confirmation and replacement. Added failure modes: dead/stale record, unsupported belief, traceability without provenance, false executable-check visibility, improper action basis for agents.


## P08 — anti-summary source texture

Статья проверена против гладкого summary. Добавлены три concrete working examples: legacy dependency ADR with ArchUnit FreezingArchRule, public API compatibility ADR with oasdiff/Pact, reconstructed proposed ADR after agent run with evidence/confidence/review fields.


## P09 — free material expansion 1

Chosen shortage: practical agent-facing ADR surface. Added concrete source-backed forms: ADR index/slash command, Vercel `adr-skill` phase-0 scan/triggers, cADR architectural diff, Angular Architects short rules derived from ADR, Mneme ADR compiler/resolver, GitHub `gh-aw` Design Decision Gate. Remaining debt: P10 should check reader path and reduce overlap with existing operational-projection section if needed.

## P14 — standalone concept reinforcement

Усилен самостоятельный вход в статью: добавлен раздел о ADR как памяти архитектурного выбора и связке с подтверждением. Риск дублирования A2/A8 контролируется: статья использует различие specification / contract / ADR / PWG только для объяснения функции ADR, не превращаясь в главу общей теории. Дополнительный текст не добавляет новый терминологический слой и не расширяет статью в каталог инструментов проверки.

## P15 — mechanism, boundaries, typical mistakes

Добавлен механизм прохождения ADR через агентскую работу и переписан раздел типичных сбоев. Усилены четыре обязательные границы: мёртвая запись без lifecycle-связей, неподтверждённое убеждение без `Confirmation`, сгенерированная traceability без provenance/evidence, видимость исполнимой проверки без признания владельческого риска. Деградации в список лозунгов не произошло: каждый сбой связан с конкретным состоянием workflow и корректирующим действием.

## P16 — broader theory link without theory drift

Добавлена короткая связь с общей AI-driven SDLC рамкой. Риск дублирования общей теории контролируется: раздел не пересказывает Spec Kit, Constitutional SDD, TDAD или PWG, а только разводит их функции по вопросу source of truth. Усилена защита от деградации в governance-overview: акцент остаётся на ADR как памяти архитектурного решения, status-aware projection for agents, confirmation и явной замене решений.

## P19 — editorial arc check

Проблемы перед правкой:

- Главная дуга статьи была собрана по разделам, но в маршруте чтения не была проговорена как единый ход: `status` → rationale/alternatives/consequences → `Confirmation` → replacement → ограничения для агента.
- Минимальный YAML-контракт называл нужные поля, но не объяснял, какие из них отвечают за применимость во времени, какие — за причину решения, а какие ограничивают агентское действие.
- Финальная проверка перед внедрением называла статус, scope, `Confirmation` и агентскую проекцию, но явно не требовала сохранить обоснование, отвергнутые альтернативы и последствия.

Исправления:

- В раздел “Как читать эту статью” добавлена явная рабочая дуга статьи.
- После YAML-контракта добавлено объяснение ролей полей без превращения статьи в каталог шаблонов.
- Финальный checklist расширен с пяти до шести проверок: добавлена отдельная проверка rationale/alternatives/consequences и усилена связь статуса с replacement.

## P20 — post-P19 consequence check

Проблемы перед правкой:

- После P19 статья лучше удерживала дугу, но в YAML-контракте остался повреждённый ключ `альтернативами`; это ослабляло техническую опору минимального контракта.
- Усиление checklist и YAML-ролей могло слегка подтолкнуть раздел к восприятию ADR как обязательной формы для каждого PR.
- Главный вопрос статьи после ремонта сохранился, но финальному практическому контракту не хватало явного напоминания о пороге применения.

Исправления:

- Ключ контракта восстановлен как `alternatives`, и ссылка на него в объяснении полей приведена к тому же виду.
- После объяснения полей добавлен короткий ограничитель: ADR нужен при архитектурном пороге, а обычная локальная задача может оставаться в issue, спецификации, тесте или ревью.
- Новая правка не удаляет источниковую фактуру, не заменяет статью каталогом шаблонов и возвращает читателя к главному вопросу: когда ADR становится памятью решения и как агент должен безопасно работать с этой памятью.

## P21 — adversarial editorial reading

Проблемы перед правкой:

- Раздел с агентскими поверхностями мог читаться как последовательный набор ADR tools, хотя его функция — показать, как статус, область действия, `Confirmation` и замена переводятся в контекст агента.
- Граница со Spec Kit и Persistent Work Graph была объяснена, но adversarial reader мог всё ещё принять соседние артефакты за варианты одного governance-процесса.
- Риск деградации состоял не в потере источников, а в смещении фокуса: от “память решения” к “инструменты, проверки и рабочие процессы вокруг архитектуры”.

Исправления:

- В начало раздела “Как агент работает с ADR” добавлена проверка инструментальных форм по трём критериям: status/scope/replacement filtering, связь с `Confirmation`, человеческий переход статуса.
- В начало раздела о соседних артефактах добавлена adversarial boundary test: specification отвечает за намерение и шаги, PWG — за состояние работы, test/oracle — за обнаружение ошибки, ADR — за обоснование, статус, последствия и replacement.
- Статья не переписана под общую governance-теорию: поправки работают как границы чтения и не удаляют фактуру источников.

## P22 — public entry sequence

Проблемы перед правкой:

- Первый содержательный раздел после вступления был “Границы статьи”. Он слишком рано выводил читателя к внутренним границам атласа, C5/A10 и taxonomy вместо публичного смысла ADR.
- Структура входа могла создать впечатление, что статья начинается с защиты от соседних тем, а не с объяснения ADR как памяти архитектурного решения.

Исправления:

- Раздел “Границы статьи” перенесён ниже: после маршрута чтения и самостоятельного концептуального объяснения ADR.
- Первый экран теперь ведёт читателя от практической проблемы к маршруту и к функции ADR: статус, обоснование, подтверждение и замена.
- Boundary/taxonomy сохранены, но больше не перегружают вход.

## P23 — companion synchronization

Проблемы перед правкой:

- Companion-файлы сохраняли устаревшие статусы P01/P09/P12 и долги, которые уже закрыты в основном тексте.
- `source_transfer_ledger` начинал снова выглядеть как coverage-бюрократия, хотя должен фиксировать только реальные решения переноса.
- `open_questions` содержал вопросы, уже решённые разделами про `origin`, `proposed/reconstructed`, Design Decision Gate, projection/resolver и границы `Confirmation`.
- Image plan и external queue не были синхронизированы с фактическим набором figure id после редакторских проходов.

Исправления:

- `source_usage`, `source_transfer_ledger`, `open_questions`, `theory_links`, `image_plan` и `external_image_queue` переписаны как P23 synchronized companion-файлы.
- Удалены стандартные долги вида `C5/A10 sync pending`; оставлены только конкретные долги: asset rights/quality/localization и будущие atlas-composition links после появления стабильных URL.
- Ledger сокращён до решений о переносе фактуры в основной текст и запрета на превращение его в общую библиографию.

## P24 — style defect audit

Проблемы перед правкой:

- В нескольких местах слово “поверхность” стало псевдотермином и прятало простую мысль: где и как агент читает ADR.
- В тексте оставались кальки и тяжёлые формулы вроде “полный дамп”, “folder dump”, “архитектурное правосудие”, “магический запрос”.
- Заголовок `AI/ADR research` и ссылка на “ADR как рабочую поверхность агента” звучали менее естественно, чем остальная русская статья.

Исправления:

- Заголовок изменён на “Как агент работает с ADR”; рядом заменены “поверхность” и “ADR-поверхность” на формы чтения, рабочий способ или опору для проверки.
- Заголовок research-раздела изменён на “Исследования AI/ADR...”, а шкала AI/ADR частично русифицирована.
- Кальки и декоративные обороты заменены точечно; компактные технические термины `status`, `scope`, `Confirmation`, `gate`, `hook`, `resolver`, `skill` сохранены там, где они обозначают реальные поля или инструменты.

## P25 — selective natural rewrite

Проблемы перед правкой:

- В публичном тексте оставались следы внутренних проходов: “после P08”, “практический результат из досье”, “кандидаты, которые в P12...”.
- Несколько фраз звучали как служебная разметка статьи, а не как нормальное объяснение читателю: “граница для атласа”, “главный вывод для атласа”, “роль архитектурного органа”.
- В абзаце про Fowler оставалась английская вставка `supporting discussion`, хотя здесь не требовалась точная source label.

Исправления:

- Служебные ссылки на проходы и досье убраны из основной статьи без потери источниковой фактуры.
- Фразы заменены на естественные русские формулировки: практическая граница, практическая модель, орган принятия архитектурных решений.
- Technical anchors, команды, числа, статусы, источники и ограничения сохранены.

## P26 — guarded final human technical style pass

Проблемы перед правкой:

- Раздел границ сохранял внутренние формулы “защищённый профиль”, “глубокий якорь”, `A2/A8/A10`, `C5/A10`, которые мешали спокойному публичному чтению.
- “Технический якорь” и heading про ассеты звучали служебно.
- Нужно было сохранить конкретику источников, команд и статусов, не сгладив статью до общего рассуждения.

Исправления:

- Раздел переименован в “Границы статьи” и переписан человеческим техническим языком без потери роли ADR в атласе.
- Внутренние ссылки `A2/A8/A10` и `C5/A10` заменены на явную связь с общей теорией.
- “Технический якорь” заменён на “техническая опора”; финальный раздел изображений переименован в “Внешние изображения для asset-pass”.
- Источниковая фактура, команды, числа, статусы и границы статьи сохранены.

## P27 visual protocol correction

Финальная проверка вернула нижний раздел к требуемому названию “Внешние изображения для asset-pass” и добавила в `adr_method_image_plan.md` явный disposition для всех внешних candidates. Это исправление нужно для соответствия visual protocol; оно не меняет содержательную структуру статьи.

