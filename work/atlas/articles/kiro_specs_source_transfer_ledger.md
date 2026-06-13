# kiro_specs — source transfer ledger

Статус: `P26_guarded_final_style_current`. Ledger фиксирует только решения переноса фактуры в основной текст и реальные deferrals. Он не является полной coverage-матрицей всех источников и не хранит длинный pass-by-pass журнал.

## Что сейчас перенесено в основной текст

| Перенесённая фактура / граница | Источниковая опора | Как работает в статье |
| --- | --- | --- |
| Kiro Specs как продуктовая спецификационная среда, а не просто набор Markdown-файлов | Kiro Specs/Feature Specs docs + C5 как read-only рамка | Центральный тезис вступления, positioning section, practical criterion. |
| `requirements.md → design.md → tasks.md → execution → Sync Files` | Feature Specs, Requirements-First, Design-First, Specs Best Practices, Kiro home task demo | Feature Specs lifecycle и synthetic figure `fig-kiro-feature-spec-lifecycle`. |
| Requirements-First / Design-First / Bugfix / Quick Plan как разные входы | Requirements-First, Design-First, Bugfix Specs, Quick Plan, faster-smarter blog | Раздел `Четыре входа...`: режим выбирается по типу неопределённости, а не по названию продукта. |
| Bugfix Spec с `bugfix.md` и unchanged behavior | Bugfix Specs docs | Дефект начинается с current/expected/reproduction/unchanged behavior и затем сходится к design/tasks. |
| Analyze Requirements как предкодовая проверка требований | Analyze Requirements docs, Deep Spec Analysis blog | Раздел показывает gaps/ambiguities/contradictions и границу: человек всё равно принимает доменное решение. |
| Задачи как единицы агентского исполнения | Specs docs, home demo, faster-smarter, run-all-tasks, best practices | `tasks.md` объяснён как очередь делегирования со статусами, dependency waves, Run all Tasks, diff/execution trace. |
| Hooks, Supervised/Autopilot, checkpoints как контроль исполнения | Hooks/types, Autopilot, Checkpoints docs | Контроль продолжается после утверждения задач, но hooks/status/checkpoint не равны acceptance. |
| `.kiro`, steering, `#spec`, Sync Files как контекст среды | Steering, chat/context, first-project, best practices | Контекст разделён на spec files, long-lived steering, chat provider and synchronization surfaces. |
| MCP и Powers как внешний контекст/инструменты | MCP docs, MCP configuration/usage, Powers docs | Access/permissions/elicitation описаны как граница действия агента, не как доказательство качества. |
| PBT как слой свидетельств вокруг spec | Correctness docs, IDE changelog 0.6 | PBT связывает EARS/requirements с executable properties и feedback loop, но не становится формальной гарантией. |
| CLI как соседняя поверхность с общей `.kiro`-конфигурацией | CLI blog, CLI steering/custom agents/headless/subagents/registry docs | CLI полезен для automation/headless/custom agents, но статья не утверждает полный IDE Feature Specs parity. |
| IDE subagents как соседние исполнители | Subagents docs | Вынесена важная граница: IDE subagents не имеют Specs access and Hooks do not trigger. |
| Web Preview как соседний автономный PR-cycle | Web docs/blog, autonomous mode, task creation, identity-center, Web MCP | Web описан cautiously: PR-cycle/roadmap рядом с Specs, не как уже доказанная IDE Specs equivalent. |
| Enterprise governance/monitoring как organizational control boundary | Governance/model/MCP/API/web-tools/monitoring/user-activity/prompt-logging docs | Политика и наблюдаемость отделены от evidence/acceptance. |
| Theory back-links | C5/A10/neighbor methods as read-only context | Раздел `Что Kiro даёт общей теории...` связывает статью с общей картой, не превращая её во вторую теорию. |
| Визуальный слой | Local Fowler asset; synthetic figures; official Kiro pages/blogs as external candidates | Один local/general SDD asset, три synthetic figures, семь external-real candidates. |

## Реальные deferrals после P23

| Deferral | Почему не перенесено в основной текст как утверждение |
| --- | --- |
| Свежая проверка текущего Kiro Web Specs status | Web/Specs roadmap is freshness-sensitive; статья намеренно не утверждает full Web Specs parity. |
| Свежая проверка CLI Feature Specs parity | CLI uses `.kiro` context and automation, but current article avoids claiming full IDE workflow until verified. |
| Точное хранение task status | Видимый UI status and execution surface used; storage in `tasks.md` vs IDE metadata remains unresolved. |
| PBT UI/defaults/current behavior | Article uses documented PBT mechanism, but current UI/default/optional behavior should be verified before publication. |
| Data protection vs prompt logging retention/policy | Governance/monitoring boundary is in article; detailed policy/retention implications need source pass. |
| MCP registry enforcement limits across enterprise/CLI | Article includes client-side and registry cautions; exact current behavior remains source-depth debt. |
| External-real image assets | Article keeps placeholders and bottom asset-pass block; no download/rights/quality/freshness check has been performed. |
| Handbook/Fieldbook checklists and admin procedures | Intentionally omitted to avoid turning concept article into a manual. |
| Full neighboring-method comparisons | Spec Kit/SPDD/TDAD/Constitutional SDD/ADR/PWG boundaries are included only as needed; full comparison belongs elsewhere. |

## P23 sync note

- Ledger has been compacted from accumulated pass notes into current transfer decisions.
- Stale `P01/P02 ready` statuses and generic C5/A10 companion debt are removed.
- C5/A10 remain valid read-only context; open issues are now concrete article blockers only.
## P24 style-audit transfer note

P24 did not transfer new external facts. It changed presentation only: several headings were made more natural, the public theory section no longer says `C5-логика`, `методологическая трассировка` was replaced with direct wording, and PBT/MCP/enterprise phrases were clarified without changing their source-backed meaning.
## P25 selective rewrite transfer note

P25 did not transfer or remove source facts. It clarified presentation in the scope, hooks, MCP, CLI, Web and theory sections: no new claim was added, and existing boundaries remain the same.

## P26 guarded final style transfer note

P26 did not transfer, remove or reorder source-backed facts. It changed presentation only: remaining heavy/meta formulations were rewritten while preserving the Kiro/Fowler source set, all boundaries and all deferrals.
