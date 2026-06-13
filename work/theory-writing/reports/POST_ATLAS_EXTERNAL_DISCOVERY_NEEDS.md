# Post-Atlas External Discovery Needs

Статус: preliminary map for heavy chapter packages.  
Назначение: выделить главы, где внешние источники нужны как содержательный слой, а не только как проверка ссылок или поиск картинок.

## Принцип

Внешний source discovery запускается не для полноты ради полноты. Он нужен там, где будущая глава не может быть достаточно сильной только на skeleton / A-B-C / Atlas / dossiers. Контур:

```text
content gap map
→ external source discovery
→ source unfolding
→ integration decision
→ provenance/style integration
```

`source unfolding` означает, что найденный источник нужно не только открыть, но и посмотреть его ссылки, авторов, термины, диаграммы, репозитории, связанные документы и конкурирующие рамки. Иногда именно второй шаг найдёт настоящий источник для главы.

## High priority

### Часть IX. Исполнение: среда агента, harness, tools, permissions

Внутренний материал даёт направление, но глава легко станет списком инструментов. Нужны внешние источники для содержания:

- durable execution / workflow runtimes: Temporal, DBOS, Restate;
- agent orchestration: LangGraph и связанные документы;
- harness/tool boundary: HumanLayer, Sandvault, Codex/Claude docs;
- permissions, worktrees, sandboxing, MCP/hooks/subagents.

Вопрос главы: что делает действие агента ограниченным, наблюдаемым, возобновляемым и подотчётным.

### Часть XI. Evidence / review / proof quality

Нужно добрать источники по видам evidence:

- contract testing и `can-i-deploy`;
- architecture fitness / confirmation;
- rollout/SLO/error budget signals;
- trace/replay sources;
- review evidence и человеческое принятие.

Вопрос главы: какие обещания требуют каких свидетельств.

### Часть XII. Completion / authority / external governance

Нужно внешнее содержание по authority:

- CODEOWNERS и модели владения;
- maintainer policies around AI contributions;
- open-source AI-use restrictions;
- enterprise policy/sandbox acceptance;
- цена доверия и граница ответственности.

Вопрос главы: кто может разрешить действие и кто может признать изменение завершённым.

### Часть XIII. Lifecycle tail

Вероятно нужны источники по repair/maintenance after merge:

- incident feedback loops;
- dependency и supply-chain inventory;
- SBOM / security update practices;
- policy/rules/skills update practices;
- documentation/spec drift.

Вопрос главы: что должно измениться после принятия результата, чтобы следующая работа не стартовала из ложного состояния.

## Medium priority

### Часть II. Session / trace / intervention

Возможные источники: SWE-chat, Programming by Chat, How Coding Agents Fail, transcript/trace research. Нужны только если глава будет делать классификацию traces/failures, а не только мост к PWG.

### Часть VI. Context as interface

Возможные источники: Codex/Claude project rules, skills, hooks, subagents, MCP, документация Kiro/BMAD/GSD. Нужны, если глава станет содержательной главой о project context as interface, а не коротким переходом.

### Часть III. Specification / ADR / contract

Возможные источники: ADR practice, MADR/AWS/Nygard, architecture fitness functions, generated ADR research. Многие уже покрыты Атласом, но для более широкой теории может понадобиться раскрытие.

## Low priority / mostly internal

SPDD, PWG, Gas Town и главы по protected methodology profiles уже имеют сильный материал Атласа и досье. External discovery там нужен точечно: для проверки свежести official docs, восстановления первичных источников или точных visual assets.

## Guardrail

External discovery не должен молча расширять scope главы. Если source unfolding находит крупную новую линию, package должен её классифицировать:

- integrate now;
- только source register;
- future debt;
- separate appendix/Handbook/Fieldbook material.
