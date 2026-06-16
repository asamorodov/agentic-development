# Source register — Chapter X Gas Town / Beads

## Назначение

Реестр отражает фактически использованные в `13_13_natural_russian_rewrite.md` источники и точечные доборы P14/P15. Это не список всех найденных материалов; сюда входят только источники, на которых держится текущий текст или ближайшая структурная правка.

## Основные внешние источники Gas Town / Beads

| Источник | Тип | Где использован в тексте | Статус |
|---|---|---|---|
| https://github.com/gastownhall/gastown | README / primary repo | Открытие: Gas Town as multi-agent orchestration / workspace manager; persistent work tracking; hooks; mailboxes/handoffs; Beads ledger. Дополнительно P15 подтвердил `gt feed --problems`, `gt sling`, `gt prime`, convoys, dashboard, watchdog, merge queue, scheduler. | Использован; прямую ссылку на README стоит добавить рядом с `gt feed --problems` при финальной интеграции P14. |
| https://gastownhall.github.io/beads/architecture | Beads docs | Dolt as sole storage backend / source of truth; version-controlled SQL; server mode; limitations. | Использован в Beads lower-layer and limitations sections. |
| https://gastownhall.github.io/beads/cli-reference/gate | Beads docs | `bd gate create`; human/timer/GitHub conditions; blocked issue not in `bd ready`. | Использован в Beads section and gate subsection. |
| https://gastownhall.github.io/beads/multi-agent/coordination | Beads docs | `bd pin`, `bd hook`, sequential handoff, fan-out/fan-in. | Использован in Beads section. |
| https://gastownhall.github.io/beads/cli-reference/prime | Beads docs | `bd prime` as AI-optimized context for sessions/hooks. | Использован in Beads lower layer. |
| https://gastownhall.github.io/beads/multi-agent/routing | Beads docs | routes, pattern matching, auto-routing, cross-repo dependencies, hydration. | Использован in Beads lower layer. |
| https://gastownhall.github.io/beads/integrations/codex | Beads docs | Codex SessionStart / PreCompact / PostCompact / UserPromptSubmit use of `bd prime`. | Использован in Beads/session context paragraph. |
| https://gastownhall.github.io/beads/workflows | Beads docs | formulas/TOML, molecules, gates, wisps general layer. | Использован in Beads workflows paragraph. |
| https://gastownhall.github.io/beads/workflows/molecules | Beads docs | molecule as persistent instance; steps map to issues; deps and hooks/pinning. | Использован in Beads workflows paragraph. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md | Gas Town design docs | Town-level vs rig-level beads; role taxonomy. | Использован in Gas Town section and figure `fig-x-two-tier-beads-flow`. |
| https://docs.gastownhall.ai/ | Public docs | Infrastructure roles; convoys; town/rig directory; common operational framing. | Использован in Gas Town roles/convoy paragraphs. |
| https://docs.gastownhall.ai/reference/ | Public reference | Commands / handoff / patrol loops / Beads as control plane. | Used indirectly through discovery; not heavily cited in P13. Candidate for final citation if command surface expands. |
| https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl | Role template | `gt sling <bead-id> <rig>` as dispatch: spawn polecat, hook work, start session. | Использован cautiously in Gas Town Mayor paragraph. |
| https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | Authorial article | “agent is not session”; roles; frontier/hands-on/expensive caveat; source-derived figures. | Использован in Gas Town and limitations. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/polecat-lifecycle-patrol.md | Design docs | `RECOVERED_BEAD`, `GUPP_VIOLATION`, `ORPHANED_WORK`, `MERGE_READY`, `MERGED`, `MERGE_FAILED`. | Использован in Gas Town/lifecycle and example. |
| https://github.com/gastownhall/gastown/blob/main/docs/glossary.md | Glossary | GUPP and hook rule. | Использован in stalled-claim subsection. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md | Design docs | Deferred dispatch, `scheduler.max_polecats`, capacity/backpressure, safety properties. | Использован in backpressure subsection. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/escalation.md | Design docs | Structured escalation; severity route; Deacon → Mayor → Overseer; stale detection. | Использован in escalation subsection. |

## Supporting story sources

| Источник | Тип | Где использован | Статус |
|---|---|---|---|
| https://www.solberg.is/babysit-pr | Public article | `/babysit-pr` as PR servicing loop. | Использован in supporting stories. |
| https://www.solberg.is/how-i-use-claude-code | Public article | Multiple working streams, issues, worktrees, context management, specialized agents. | Использован in supporting stories. |
| https://www.chatprd.ai/how-i-ai/stripes-ai-minions-ship-1300-prs-weekly-from-a-slack-emoji | Public case/article | Slack message / emoji reaction / Minion / PR. | Использован in supporting stories. |
| https://www.chatprd.ai/how-i-ai/workflows/how-to-automate-code-generation-from-a-slack-message-into-a-pull-request | Workflow page | Slack idea → emoji trigger → isolated cloud environment → agent loop → PR review. | Использован in supporting stories. |
| https://shopify.engineering/introducing-roast | Public engineering article | Roast as structured AI workflow framework. | Использован in supporting stories. |
| https://github.com/Shopify/roast/blob/main/README.md | Repo README | Ruby DSL: `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, named outputs/providers. | Использован in supporting stories. |
| https://maecapozzi.com/blog/ai-powered-toil-reduction-platform-engineering | Public article | Claude Code for platform toil; CI/test PRs; dependency reviews; instrumentation; cleanup/deletion work. | Использован in supporting stories. |

## Internal source files used

| File | Use |
|---|---|
| `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` | Main conceptual source: Gas Town beyond PWG, roles, B3 table, `gt feed --problems`, service agents, pressure mechanisms. |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Boundary with process profiles and gates/molecules as executable workflow instances. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Boundary with runtime/hooks/context return. |
| `work/atlas/articles/gas_town.md` | Concept-first Gas Town baseline; source links; figure candidates. |
| `work/atlas/articles/persistent_work_graph.md` | Boundary with PWG; durable work item concept. |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Detailed Gas Town mechanism source for roles/statuses. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Durable work state and comparison matrix. |
| `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` | Detailed Jökull PR servicing story and source provenance. |
| `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` | Detailed Stripe routing/devbox/platform source. |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | Roast workflow-as-code details. |
| `content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md` | Mae worktrees/traces/timeouts/platform toil supporting parallel. |
