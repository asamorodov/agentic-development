# adr_method — image plan

Статус: local patch synchronized. В статье сейчас четыре локальных `source_excerpt_asset` SVG, четыре оставшихся external-real placeholders и одна синтетическая схема.

## Local assets — решение P11/P27

Локальный asset scan пакета выявил `content/assets/theory-images/fowler-sdd-overview.png` и служебный `content/assets/theory-images/MANIFEST.md`. Изображение `fowler-sdd-overview.png` относится к SDD/specification surface, а не к ADR status/replacement/confirmation, поэтому не вставлено. `MANIFEST.md` перечисляет broader theory assets для соседних материалов; они не являются ADR-specific локальными figure candidates для этой статьи и в текущем package не используются как source images. Итого: релевантных ADR-specific local assets для вставки нет; реальный visual layer ADR оставлен как external-real candidate queue.

## Inline placeholders, фактически присутствующие в статье

| Figure id | Тип | Источник / candidate | Placement | Asset-долг |
| --- | --- | --- | --- | --- |
| `fig-adr-nygard-minimal-record` | local_source_excerpt_asset | Nygard article fragment around `Context / Decision / Status / Consequences` and `superseded` | `Что именно записывает ADR` | Проверить права, crop и читаемость фрагмента. |
| `fig-adr-madr-template-confirmation` | local_source_excerpt_asset | MADR template fields around `Decision Drivers`, `Decision Outcome`, `Confirmation`, `Pros and Cons` | `Что именно записывает ADR` | Проверить права и выбрать фрагмент, который не превращает статью в template catalogue. |
| `fig-adr-aws-lifecycle-process` | local_source_excerpt_asset | AWS ADR process/update/review diagrams | `Жизненный цикл: создать, принять, заменить` | Проверить права AWS docs, качество диаграмм и один ли нужен crop или несколько. |
| `fig-adr-pact-can-i-deploy` | external-real-candidate | Pact Broker `can-i-deploy` output or matrix | ``Confirmation`: не один тест...` | Проверить, что скриншот показывает ограниченную совместимость, а не “доказательство всего ADR”. |
| `fig-adr-vercel-skill-phase0` | external-real-candidate | Vercel `adr-skill` around philosophy and `Phase 0: Scan the Codebase` | `Как агент работает с ADR` | Проверить права GitHub fragment и читаемость. |
| `fig-adr-mneme-compiler-constraints` | external-real-candidate | Mneme ADR compiler pipeline and constraints | `Как агент работает с ADR` | Проверить source status и качество фрагмента; важно показать status-aware resolver, не general governance. |
| `fig-adr-design-decision-gate` | local_source_excerpt_asset | GitHub `gh-aw` Design Decision Gate workflow artifacts/trigger/draft | `Как агент работает с ADR` | Проверить стабильность workflow URL и читаемость PR/CI evidence. |
| `fig-adr-agenticakm-proposed-generated-adr` | external-real-candidate | AgenticAKM generated ADR with `Status: Proposed` | `исследования AI/ADR...` / `Три рабочих примера` | Проверить, что фрагмент ясно показывает proposed boundary. |
| `fig-adr-neighbor-artifact-boundaries` | synthetic_figure | Собственная схема статьи | `ADR в жизненном цикле соседних артефактов` | Не заменяет real-source screenshots; оставить как карту границы specification / ADR / contract / PWG. |


## Disposition всех внешних candidates

| Candidate id | Disposition | Где зафиксирован / причина |
| --- | --- | --- |
| `ext-adr-nygard-minimal-adr` | `inserted_inline_external_placeholder` | `fig-adr-nygard-minimal-record`; mirrored in bottom section and external queue. |
| `ext-adr-madr-template-confirmation` | `inserted_inline_external_placeholder` | `fig-adr-madr-template-confirmation`; mirrored in bottom section and external queue. |
| `ext-adr-aws-lifecycle` | `inserted_inline_external_placeholder` | `fig-adr-aws-lifecycle-process`; mirrored in bottom section and external queue. |
| `ext-adr-pact-can-i-deploy` | `inserted_inline_external_placeholder` | `fig-adr-pact-can-i-deploy`; mirrored in bottom section and external queue. |
| `ext-adr-vercel-adr-skill` | `inserted_inline_external_placeholder` | `fig-adr-vercel-skill-phase0`; mirrored in bottom section and external queue. |
| `ext-adr-mneme-compiler-constraints` | `inserted_inline_external_placeholder` | `fig-adr-mneme-compiler-constraints`; mirrored in bottom section and external queue. |
| `ext-adr-github-design-decision-gate` | `inserted_inline_external_placeholder` | `fig-adr-design-decision-gate`; mirrored in bottom section and external queue. |
| `ext-adr-agenticakm-proposed-generated-adr` | `inserted_inline_external_placeholder` | `fig-adr-agenticakm-proposed-generated-adr`; mirrored in bottom section and external queue. |
| `ext-adr-fowler-supersession` | `external_queue_only` | Extra lifecycle fragment; inline already covered by Nygard/AWS. |
| `ext-adr-llm-generation-2024` | `external_queue_only` | Research figure only if future article expands LLM generation process. |
| `ext-adr-context-matters-2026` | `external_queue_only` | Context selection figure/table; not inline to avoid research-survey drift. |
| `ext-adr-template-comparison-desmet` | `external_queue_only` | Template comparison; not inline because article is not template catalogue. |
| `ext-adr-agenticakm-taxonomy` | `external_queue_only` | Useful only if reconstruction section expands. |
| `ext-adr-agenticakm-pipeline-code` | `external_queue_only` | Pipeline/code fragment; generated proposed example is stronger inline anchor. |
| `ext-adr-agenticakm-failed-summary-log` | `external_queue_only` | Failure-mode evidence; requires notebook readability check. |
| `ext-adr-angular-boundaries` | `external_queue_only` | Secondary operational-projection example; inline surface already covered. |
| `ext-adr-wa-decision-finder` | `external_queue_only` | Status/date/relevance check; text citation is enough unless status UI is needed. |
| `ext-adr-cadr-readme-generated-fields` | `external_queue_only` | Diff-to-ADR capture candidate; future asset after readability check. |
| `ext-adr-k6-thresholds` | `external_queue_only` | Operational confirmation candidate; text source sufficient now. |
| `ext-adr-google-sre-slo` | `external_queue_only` | SLO/error-budget source; better as text unless operations section expands. |
| `ext-adr-prometheus-alert-test` | `external_queue_only` | Alert rule testing candidate; future asset only if operations confirmation expands. |
| `ext-adr-argo-analysis-template` | `external_queue_only` | Progressive delivery confirmation; queue-only. |
| `ext-adr-claude-adr-command-index` | `external_queue_only` | ADR index/command visual; Vercel skill is stronger inline anchor. |
| `ext-adr-microsoft-retroactive-adr` | `external_queue_only` | Brownfield/retroactive ADR; current text citation is enough. |
| `ext-adr-sig-status-no-standard` | `external_queue_only` | Status-set background; not needed inline. |
| `ext-adr-belle-reconstruction-abstract` | `external_queue_only` | Reconstruction research background; no inline visual needed. |
| `ext-adr-agents-md-eval` | `external_queue_only` | Active-context limit; likely text source only. |
| `ext-adr-guardrails-beat-guidance` | `external_queue_only` | Guardrails design; likely text source only. |
| `ext-adr-sync-marketplace` | `external_queue_only` | Lifecycle synchronization screenshot candidate; rights and value not checked. |

## Queue-only candidates

Queue-only candidates сохранены в `adr_method_external_image_queue.md`. Они не являются блокером текста. Их нельзя вставлять как decoration: каждый будущий asset должен поддерживать конкретное место статьи и не раздувать tool list, research survey или каталог шаблонов.

## Asset-pass requirements

- Проверить права/условия использования каждого screenshot/source fragment.
- Сохранить source URL, дату capture, alt text, caption и связь с placement.
- Не заменять внешние реальные source fragments авторскими схемами, если именно внешний первоисточник нужен как доказательная визуальная опора.
- Не локализовать изображение, пока не ясно, что оно улучшает статью сильнее, чем уже вставленная текстовая ссылка.
