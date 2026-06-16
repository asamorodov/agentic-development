# P17. Readiness report и регрессионная проверка главы IX

## 1. Текущий главный файл

Текущий основной вариант главы: `work/theory-writing/chapters/IX_execution_environment_runtime_rights_passes/16_16_final_revision.md`.

Рекомендация для сборки: использовать именно P16 как основной текст главы. P14 остаётся важным структурным предшественником, но P16 лучше: в нём снята служебная заметка P14, закрыт Quix provenance gap, сохранена структура и добавлена финальная редактура.

## 2. Что глава объясняет

Глава объясняет, что агентское поручение становится реальным инженерным действием только внутри конкретной среды исполнения. Эта среда задаёт:

- где агент читает и пишет: рабочая копия, worktree, sandboxed user, devbox, cloud environment;
- какие действия доступны технически: shell, files, browser/devtools, MCP/tools, network, local services, external APIs;
- какие действия находятся внутри текущего permission mode, а какие требуют approval;
- какие действия остаются невозможными или должны останавливаться;
- какие hooks, sensors, logs and local harness возвращают агенту пригодный feedback;
- как workflow runtime позволяет продолжить запуск, но не превращает его в осмысленное состояние работы;
- какой след исполнения остаётся после run и почему он ещё не является доказательством or acceptance.

Центральная мысль удержана: техническая возможность выполнить действие не равна допустимости, проверке и праву принять результат. Глава разводит `sandbox`, `permission`, `approval`, проверочный материал and authority.

Сквозной billing/UI example сохранён от начала до конца. Он работает как practical anchor: stale billing state after checkout, worktree diff, targeted tests, local browser, test-mode billing API, secrets/network boundary, external test objects, trace, PR and review.

## 3. Использованные источники

### Product/docs sources

- OpenAI Codex: sandboxing, agent approvals/security, permissions, auto-review, rules, MCP, worktrees.
- Claude Code: security, permission modes, Chrome extension, hooks.
- MCP specification: tools, authorization, security best practices.
- Kiro hooks.

Эти источники поддерживают technical boundary layer: sandbox, network, permission modes, command rules, hooks, browser surface, MCP/tool surface.

### Practice/story sources

- Arvid Kahl: allow/deny, browser loop, command bypass via script.
- Mike McQuaid / Sandvault: separate sandboxed user, worktrees, controlled transfer.
- HumanLayer: harness engineering, too many tools, progressive disclosure, skills/subagents.
- Armin Ronacher / Pi: local scripts/logs/browser/email stdout; code/CLI as useful tool surface.
- Shopify Roast: executable workflow, deterministic steps, bounded agent step, session resume/forking.
- Daniel Doubrovkine Roast walkthrough: ordinary runtime facts inside AI workflow.
- Quix / Klaus Kode: workflow engine around Claude Code, Quix Cloud sandbox, deterministic orchestration around bounded coding step.
- Stripe: integration benchmark, realistic test environments, deterministic graders, steering experiments.
- Homebrew CONTRIBUTING: contributor/review responsibility around AI-assisted PRs.

### Runtime sources

- LangGraph durable execution.
- Temporal workflows.
- Restate.
- DBOS workflows.

Они используются ограниченно: только для различения continuation/resume/history and work meaning. Глава не превращается в сравнение durable runtime frameworks.

## 4. Что осознанно отклонено или оставлено за рамкой

- Глава не стала обзором Codex, Claude Code, MCP, Kiro, Roast, Temporal, LangGraph or Sandvault.
- Stripe PR-volume / Minions headline metrics не использованы как аргумент. Сохранён structural point: platform agents shift pressure to environment, evidence, review and policy.
- GSD, BMAD and Gas Town не добавлены в текст ради полноты. Они относятся к соседним методологическим слоям и не нужны для собственной оси IX.
- Подробное сравнение Temporal/LangGraph/DBOS/Restate отклонено: достаточно общей границы durable run vs durable work state.
- Visual UI tour отклонён: P16 не вставляет dashboard screenshots or multiple product screenshots.
- Командные правила, MCP, browser, hooks and workflow runtime не описаны как самостоятельные каталоги. В P16 они подчинены главной линии: разные поверхности действия and different boundaries.

## 5. Визуальные решения

Текущий основной текст не содержит inline `<figure>`. Это осознанное решение, а не потеря материала. P12 зафиксировал visual candidates and asset briefs.

Лучшие кандидаты для будущего visual pass:

1. `fig-ix-runtime-rights-stack` — source-backed synthetic figure after introduction. Это лучший single figure: request → worktree/devbox/sandbox → permission/approval → shell/browser/MCP/network/secrets → hooks/logs/tests → trace → review/PWG.
2. `fig-ix-run-trace-to-work-state` — source-backed synthetic figure near section 7. Она показывает переход от execution trace к claim/evidence/gate/work state.
3. `fig-ix-codex-permission-prompt-boundary` — local image asset: `content/assets/theory-images/openai-codex-permission-prompt.webp`, if one real UI anchor is needed.
4. Optional: Codex DevTools validation, Fowler continuous feedback, HumanLayer too-many-MCP-tools. Эти candidates использовать только если соответствующие разделы требуют visual support.

Rejected/deferred visuals:

- Codex dashboard screenshots: too much UI-tour risk.
- Multiple Codex screenshots in one chapter: likely distract from theory.
- Sandvault `08-mike-*` screenshots: good candidates, but absent in current archive; require asset-pass/full snapshot.
- Shopify/Stripe story visuals: absent in current archive; better for atlas/story/evidence chapter.

## 6. Проверка согласованности main chapter and companion files

Согласовано:

- P16 follows P15 assembly note: use P16 as main after P14 structural repair.
- P15 listed Quix/Klaus Kode provenance gap; P16 repaired it by adding Quix blog and repository links.
- P15 warned against too many visuals; P16 keeps no inline figures.
- P15 noted possible duplication with C4/PWG; P16 keeps final bridge concise enough and does not expand PWG mechanics.
- P15 noted Homebrew may belong to XII; P16 keeps it only as a short authority/review example, not a governance detour.
- P15 noted GSD/BMAD/Gas Town absence; P16 does not force them into chapter body.

Remaining tension:

- P16 still contains many source-native English terms and some English clauses. This is partly deliberate because the chapter deals with product docs and source-native concepts, but a final style-only pass could rewrite several sentences more fully into Russian without losing terms.
- P16 is dense and long. This is acceptable under the no-hidden-limit workflow, but public assembly should ensure the chapter is not placed where a shorter overview is expected.

## 7. Regression note

### Structure regression

No major regression from P14. The final structure remains concept-first:

1. place of action;
2. sandbox/permission/approval/authority;
3. command/tool/browser surfaces;
4. feedback and local harness;
5. workflow runtime vs work meaning;
6. platform agents and review bottleneck;
7. execution trace vs checking material;
8. role in the theory.

This structure keeps chapter individuality. It no longer reads primarily as a list of tools.

### Source regression

No major source loss. P16 retains the main external source families and internal story anchors. It repairs the explicit Quix source gap.

Known future audit: final link verification for OpenAI Codex docs and Claude docs is still useful because these product docs can move, but P16 uses the current URL set discovered in earlier passes.

### Visual regression

No accidental visual degradation: real local assets were not replaced by synthetic text diagrams, and no external image candidate was smuggled into the chapter without asset-pass. Visual candidates remain in P12/P15.

### Neighbor-chapter regression

- Toward XI: P16 stops at “trace is not evidence/checking material”; it does not develop verification theory fully.
- Toward XII: P16 names authority, review and merge responsibility, but does not build governance chapter.
- Toward C4/PWG: P16 uses PWG-like mechanisms only as boundary and bridge.
- Toward A6: P16 uses execution-environment distinctions but has its own billing/UI run and boundary argument.

## 8. Remaining questions

1. Should a final style-only pass reduce remaining English clauses while preserving source-native terms?
2. Should the future public version include `fig-ix-runtime-rights-stack`? It would likely improve comprehension.
3. Should Homebrew policy stay in IX or be moved to XII? Current use is small and acceptable.
4. Should section 6 mention Stripe Minions primary pages directly, or is the benchmark/steering pair enough? Current choice is conservative and probably better.
5. Should section 7 use “доказательный материал” or “проверочный материал” consistently? P16 mostly uses “проверочный материал”; this is preferable.

## 9. Readiness verdict

Content readiness: high.

Structure readiness: high.

Source grounding: high, with routine final link audit recommended.

Visual readiness: deferred by design; not blocking.

Language readiness: good but not perfect. The chapter is readable and materially strong, but a pure Russian-style polish could still improve it by reducing English connective phrases that are not necessary source-native terms.

Final recommendation: package P16 as the main chapter result, P15 as companion/source register, P12 as visual plan, and P17 as readiness report. If there is time for one optional additional pass before publication, make it a style-only Russian polish over P16, not another structural rewrite.
