# adr_method — external image queue

Статус: local patch synchronized. Четыре основных candidates локализованы как `source_excerpt_asset` SVG; четыре candidates остаются inline external placeholders; остальные candidates оставлены только как future asset queue.

## Inline placeholders in article

| Figure id | Candidate id | Source | Placement / note |
| --- | --- | --- | --- |
| `fig-adr-nygard-minimal-record` | `ext-adr-nygard-minimal-adr` | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Минимальная ADR-запись и `superseded`. |
| `fig-adr-madr-template-confirmation` | `ext-adr-madr-template-confirmation` | https://adr.github.io/madr/ | Альтернативы, факторы решения и `Confirmation`. |
| `fig-adr-aws-lifecycle-process` | `ext-adr-aws-lifecycle` | https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | Lifecycle / review / update / supersession. |
| `fig-adr-pact-can-i-deploy` | `ext-adr-pact-can-i-deploy` | https://docs.pact.io/pact_broker/can_i_deploy | Ограниченное исполнимое подтверждение совместимости API. |
| `fig-adr-vercel-skill-phase0` | `ext-adr-vercel-adr-skill` | https://github.com/vercel/ai/blob/main/skills/adr-skill/SKILL.md | Agent-facing ADR process before drafting. |
| `fig-adr-mneme-compiler-constraints` | `ext-adr-mneme-compiler-constraints` | https://mnemehq.com/demo/adr-compiler/ | Status-aware resolver / compiled memory, not folder dump. |
| `fig-adr-design-decision-gate` | `ext-adr-github-design-decision-gate` | https://github.com/github/gh-aw/actions/runs/24966700524/agentic_workflow | Deterministic PR evidence before LLM draft and human completion. |
| `fig-adr-agenticakm-proposed-generated-adr` | `ext-adr-agenticakm-proposed-generated-adr` | https://github.com/sa4s-serc/AgenticAKM/tree/main/Generated_ADRs | Generated ADR with `Status: Proposed`. |

## Queue-only / deferred candidates

| Candidate id | Source | Reason / next action |
| --- | --- | --- |
| `ext-adr-fowler-supersession` | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | Useful lifecycle fragment; inline already covered by Nygard/AWS. |
| `ext-adr-llm-generation-2024` | https://arxiv.org/abs/2403.01709 | Research figure only if future article needs generation process visual. |
| `ext-adr-context-matters-2026` | https://arxiv.org/abs/2604.03826 | Context-selection figure/table; queue-only to avoid research-survey drift. |
| `ext-adr-template-comparison-desmet` | https://arxiv.org/abs/2604.27333 | Template comparison; queue-only because article is not template catalogue. |
| `ext-adr-agenticakm-taxonomy` | https://arxiv.org/abs/2602.04445 | AgenticAKM taxonomy; use only if reconstruction section expands. |
| `ext-adr-agenticakm-pipeline-code` | https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Code/AdrAgents.py | Pipeline/code fragment; generated `Status: Proposed` example is stronger inline anchor now. |
| `ext-adr-agenticakm-failed-summary-log` | https://raw.githubusercontent.com/sa4s-serc/AgenticAKM/main/Code/main.ipynb | Failure-mode evidence; requires notebook readability check. |
| `ext-adr-angular-boundaries` | https://www.angulararchitects.io/blog/verlaessliche-angular-architekturen-mit-ai-assisted-coding/ | Secondary example of operational projection; Vercel/Mneme/Gate already cover inline surface. |
| `ext-adr-wa-decision-finder` | https://github.com/wagov-dtt/architecture-decision-records/blob/main/decision-finder.md | Status/date/relevance check; text citation is enough unless status UI is needed. |
| `ext-adr-cadr-readme-generated-fields` | https://github.com/YotpoLtd/cADR/ | Diff-to-ADR capture candidate; future asset only after source/readability check. |
| `ext-adr-k6-thresholds` | https://grafana.com/docs/k6/latest/using-k6/thresholds/ | Operational confirmation candidate; text source is enough for current article. |
| `ext-adr-google-sre-slo` | https://sre.google/workbook/implementing-slos/ | SLO/error-budget source; likely better as text than screenshot. |
| `ext-adr-prometheus-alert-test` | https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/ | Alert rule testing candidate; future asset only if operations confirmation expands. |
| `ext-adr-argo-analysis-template` | https://argo-rollouts.readthedocs.io/en/stable/features/analysis/ | Progressive delivery confirmation; queue-only. |
| `ext-adr-claude-adr-command-index` | https://7tonshark.com/posts/claude-adr-pattern/ | ADR index/command visual; Vercel skill is stronger inline anchor. |
| `ext-adr-microsoft-retroactive-adr` | https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record | Brownfield/retroactive ADR; current text citation is enough. |
| `ext-adr-sig-status-no-standard` | https://www.softwareimprovementgroup.com/blog/using-architecture-decision-records-to-guide-your-architecture-choice/ | Status-set background; not needed inline. |
| `ext-adr-belle-reconstruction-abstract` | https://arxiv.org/abs/2112.01644 | Reconstruction research background; no inline visual needed. |
| `ext-adr-agents-md-eval` | https://arxiv.org/abs/2602.11988 | Active-context limit; likely text source only. |
| `ext-adr-guardrails-beat-guidance` | https://arxiv.org/abs/2604.11088 | Guardrails design; likely text source only. |
| `ext-adr-sync-marketplace` | https://github.com/marketplace/actions/adr-sync | Lifecycle synchronization screenshot candidate; rights and value not checked. |

## Asset-pass blockers

- Rights / license / terms for screenshots and source fragments.
- Readability after crop and localization.
- Alt text and caption quality.
- Stable local asset paths if placeholders become `<img>` tags.
