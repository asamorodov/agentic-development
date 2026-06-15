# Chapter I source register — unit of analysis

Статус: рабочий provenance-регистр для текущего черновика главы `I_unit_of_analysis.md`.

## Правило использования

Публичная глава не должна ссылаться на рабочие досье как на источники фактов. Досье, pass reports and routing maps используются как quarry / synthesis layer. Если в главе остаётся конкретный публичный факт о человеке, методе или инструменте, финальный citation layer должен вести к первичному источнику или опубликованной story/source-странице.

На момент P15 в основном тексте нет inline-ссылок. Поэтому этот регистр фиксирует, какие первичные источники должны поддерживать уже названные якоря, если в следующем проходе или при публикации будут добавлены ссылки.

## Истории и практические якоря, уже названные в главе

| Якорь | Где используется в главе | Первичный источник / источник для проверки | Статус |
|---|---|---|---|
| Boris Tane | `research.md`, `plan.md`, human annotations, запрет реализации до принятия плана | `https://boristane.com/blog/how-i-use-claude-code/` | Используется в тексте; ссылка пока не вставлена inline. |
| Peter Steinberger | малый радиус, короткий разговорный режим, быстрый просмотр `diff` и проверка | `https://steipete.me/posts/2025/just-talk-to-it` and related Steinberger workflow posts | Используется в тексте; требует точного выбора ссылки при citation pass. |
| Mark Erikson | дочерняя задача возвращает переносимое состояние, а не просто “done” | `https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/`; `https://github.com/markerikson/opencode-config-example` | Используется в тексте; source detail should be checked if quoted more specifically. |
| Calvin French-Owen | человеческое время проверки и принятия как bottleneck | `https://calv.info/agents-feb-2026`; adjacent Calvin posts in source dossier | Используется в тексте; точная ссылка зависит от финальной формулировки. |
| HumanLayer | harness / model-runtime-tools-context-skills-subagents-hooks-back-pressure | `https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents`; `https://martinfowler.com/articles/harness-engineering.html` | Используется в тексте; ссылка пока не вставлена inline. |

## Атласные методы, уже названные в главе

| Метод | Функция в главе | Первичные / опорные источники | Статус |
|---|---|---|---|
| SPDD / OpenSPDD | намерение, границы и запреты до кода; REASONS Canvas as carrier | `https://martinfowler.com/articles/structured-prompt-driven/`; `https://github.com/gszhangwei/open-spdd`; `https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md` | Используется как функциональный пример, без detailed mechanics. |
| Spec Kit | спецификация / план / задачи as repo-carried transition from behavior to implementation | `https://github.github.com/spec-kit/`; `https://github.com/github/spec-kit`; `https://github.github.com/spec-kit/reference/workflows.html` | Используется кратко; source pass needed before stronger claims. |
| Kiro | spec/design/tasks as IDE/product working surface | `https://kiro.dev/docs/specs/`; `https://kiro.dev/docs/specs/feature-specs/`; `https://kiro.dev/docs/specs/quick-plan/` | Используется кратко; details deliberately excluded. |
| BMAD Method | process state, planning artifacts, story context, status, review, correct-course | `https://docs.bmad-method.org/workflow-map-diagram.html`; `https://docs.bmad-method.org/how-to/install-bmad/`; `https://github.com/bmad-code-org/BMAD-METHOD/releases` | Используется кратко; no install/version details in chapter. |

## Внешняя калибровка из P05

Эти источники были восстановлены как возможная короткая external framing layer, но **не вставлены в текущий публичный черновик**. Их не нужно добавлять ради симметрии.

| Источник | Возможная функция | Статус |
|---|---|---|
| DORA 2025 State of AI-assisted Software Development | рамка: ИИ усиливает существующую организационную систему | Reserve only; not cited in current chapter. |
| Bain 2025 “From Pilots to Payoff: Generative AI in Software Development” | рамка: отдача от GenAI связана с lifecycle/process use, not coding-only acceleration | Reserve only; not cited in current chapter. |
| A-SDLC survey, arXiv `2604.26275` | academic/overview framing around agentic SDLC | Reserve only; not cited in current chapter. |
| SLR of agentic AI in SDLC, arXiv `2605.15245` | overview framing around verification / bounded action | Reserve only; not cited in current chapter. |

## Источники, намеренно не используемые сейчас

- Рабочие досье SPDD / Spec Kit / Kiro / BMAD as citation targets.
- A1/A10 pass reports as public provenance.
- Missing A1 image assets not present in this self-contained package.
- Broad literature review on prompt engineering, generic SDLC or AI coding productivity metrics.

