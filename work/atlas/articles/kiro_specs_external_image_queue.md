# kiro_specs — external image queue

Статус: `P26_guarded_final_style_current`. Очередь содержит только те external-real candidates, которые реально стоят в текущей статье и зеркалированы в нижнем разделе `Внешние изображения для asset-pass`. Никакие изображения не скачивались; все элементы требуют отдельного asset-pass.

## Queue

### fig-kiro-quick-plan-candidate
- Источник: `https://kiro.dev/docs/specs/quick-plan/`; supporting source: `https://kiro.dev/blog/faster-smarter-specs/`
- Нужный ассет: официальный скриншот или диаграмма, где Quick Plan ведёт от идеи к `requirements.md`, `design.md`, `tasks.md` без отдельных approval-gates между фазами.
- Где используется: после раздела `Quick Plan: когда полный цикл был бы лишним`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/quick-plan-workflow.png`
- Статус: `external-real-candidate`; требуется загрузка, проверка прав, качества и свежести.

### fig-kiro-deep-spec-analysis-candidate
- Источник: `https://kiro.dev/blog/deep-spec-analysis/`
- Нужный ассет: диаграмма или скриншот процесса refinement → autoformalization → logical analysis → questions → updated `requirements.md`.
- Где используется: после раздела `Analyze Requirements: проверка требований до того, как они станут кодом`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/deep-spec-analysis-pipeline.png`
- Статус: `external-real-candidate`; требуется загрузка, проверка прав, качества и свежести.

### fig-kiro-task-status-ui-candidate
- Источник: `https://kiro.dev/`
- Нужный ассет: official homepage transcript/screenshot sequence with `Start task`, `Task in progress`, `Task completed`, `View changes`, `View execution`.
- Где используется: раздел `Задачи как единица агентского исполнения`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/task-status-ui.png`
- Статус: `external-real-candidate`; требуется загрузка, проверка прав, качества и свежести.

### fig-kiro-parallel-task-waves-candidate
- Источник: `https://kiro.dev/blog/faster-smarter-specs/`
- Нужный ассет: официальная диаграмма dependency waves / parallel task execution.
- Где используется: раздел `Задачи как единица агентского исполнения`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/parallel-task-waves.png`
- Статус: `external-real-candidate`; требуется загрузка, проверка прав, качества и свежести.

### fig-kiro-pbt-candidate
- Источник: `https://kiro.dev/docs/specs/correctness/`
- Нужный ассет: workflow or screenshots showing natural-language/EARS requirement → executable property → generated cases → failing scenario.
- Где используется: после раздела `Тестирование на основе свойств: как требования становятся проверяемыми свойствами`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/property-based-testing-workflow.png`
- Статус: `external-real-candidate`; требуется загрузка, проверка прав, качества и свежести.

### fig-kiro-subagents-boundary-candidate
- Источник: `https://kiro.dev/docs/chat/subagents/`
- Нужный ассет: официальный скриншот или диаграмма, которая подтверждает границу IDE subagents относительно Specs and Hooks.
- Где используется: после раздела `Subagents: соседние исполнители вне полного Specs-процесса`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/subagents-specs-boundary.png`
- Статус: `external-real-candidate`; сначала проверить, существует ли official real asset. Если нет, пометить `not_found_in_source` и отдельно решить вопрос synthetic fallback.

### fig-kiro-web-boundary-candidate
- Источник: `https://kiro.dev/docs/web/`; `https://kiro.dev/blog/introducing-kiro-web/`; supporting pages: `https://kiro.dev/docs/web/autonomous-mode/`, `https://kiro.dev/docs/web/using-the-agent/creating-tasks/`, `https://kiro.dev/docs/web/identity-center/`, `https://kiro.dev/docs/web/sandbox/mcp/`
- Нужный ассет: скриншот или схема, которая визуально разделяет Web Preview autonomous PR-cycle and IDE Specs workflow, с проверкой текущего статуса Web Specs.
- Где используется: после раздела `Web Preview: автономный PR-цикл рядом с будущими Web Specs`.
- Предлагаемый локальный путь: `content/assets/atlas-images/kiro/web-preview-vs-ide-specs.png`
- Статус: `external-real-candidate`; freshness check required before any final visual claim.

## P23 sync note

- Queue по составу совпадает с inline placeholders and bottom asset-pass block in `kiro_specs.md`.
- Старые pass notes удалены; реальные blockers остались в каждом элементе: загрузка, права, качество, свежесть, а для Subagents/Web — проверка наличия official visual.
## P24 queue note

No queue changes. Only article-section references were synchronized with the style-audit headings; all seven external-real candidates and blockers remain the same.
## P25 queue note

No queue changes. External-real candidates and asset-pass blockers remain unchanged.

## P26 queue note

No queue changes. External-real candidates, source URLs, proposed local paths and rights/quality/freshness blockers remain unchanged.
