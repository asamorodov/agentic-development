# Source register — Chapter VII Persistent Work Graph

## Назначение

Регистр отражает фактический текст главы после P13/P14: не все найденные источники, а те, которые реально питают главу.

## Внутренние источники

| Источник | Использование в главе | Статус переноса |
| --- | --- | --- |
| `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` | Главный тезис: summary / transcript / local done не являются состоянием работы; source state и cleanup должны жить в графе. | Перенесён в ось главы и early failure sections. |
| `work/theory-writing/fragments/B2_pwg_contribution.md` | Работа как долговечный объект: identity, boundary, dependencies, readiness, owner/claim, gates, acceptance basis, source state, recovery. | Перенесён в раздел «Что хранит PWG». |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Мост к VIII: process выбирает ход, PWG показывает состояние узла. | Перенесён в финал. |
| `work/theory-writing/fragments/C3_pwg_to_evidence.md` | Completion as state transition, проверочные основания должны пережить исполнителя. | Использован ограниченно, без разворота в evidence theory. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Runtime creates trace, but does not decide closure; durable execution != durable work. | Перенесён в boundary-section. |
| `work/atlas/articles/persistent_work_graph.md` | Основной концептуальный атлас: ready/claim/gate/prime/recovery/source state/cleanup. | Использован как каноническая опора. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Расширенная фактура: Beads, Task Master, durable runtime, source-state protocol. | Использован выборочно. |
| `work/atlas/articles/gas_town.md`, `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Только boundary: Gas Town шире PWG. | Не раскрывать глубже в VII. |

## Story anchors

| История | Конкретная функция в главе | Статус |
| --- | --- | --- |
| Jökull Sólberg | `/babysit-pr`, PR as work object, Fix/Dismiss/Escalate, CI/Greptile/Codex signals. | Главный anchor для section about signal triage. |
| HumanLayer | Research→plan→implement; wrong research discarded; subagents as bounded outputs; progressive disclosure. | Поддерживает «subagent output has state» and `prime`/context boundary. |
| Mark Erikson | `cachebro` / OpenCode source-state mismatch; DiffLoupe/read-only reviewer; Replay MCP observability. | Поддерживает source state and reviewer role. |
| Mae Capozzi | PRs/Linear/traces/spans/comments as checkable artifacts; human classification; Honeycomb telemetry. | Поддерживает artifact → classification → graph-state pattern. |

## Внешние источники, реально используемые

| Источник | Ссылка | Использование |
| --- | --- | --- |
| Beads documentation | https://gastownhall.github.io/beads/ | Главный current-practice anchor: dependency-aware execution, gates, agent-readable work graph. |
| Beads GitHub repository | https://github.com/gastownhall/beads | Product/repo anchor, not detailed review. |
| Beads core concepts | https://gastownhall.github.io/beads/core-concepts | Dependency types and issues as work items. |
| Beads `bd ready` | https://gastownhall.github.io/beads/cli-reference/ready | Readiness as computed state. |
| Beads `bd dep` | https://gastownhall.github.io/beads/cli-reference/dep | Dependency semantics; relation != blocker. |
| Beads `bd blocked` | https://gastownhall.github.io/beads/cli-reference/blocked | Negative/diagnostic side of readiness. |
| Beads `bd gate` | https://gastownhall.github.io/beads/cli-reference/gate | Gate as durable wait condition. |
| Beads `bd prime` | https://gastownhall.github.io/beads/cli-reference/prime | Restoration packet / session start context. |
| Beads Agent Coordination | https://gastownhall.github.io/beads/multi-agent/coordination | Pinning, hook, handoff, fan-out/fan-in, reservations/locks. |
| Beads Recovery Overview | https://gastownhall.github.io/beads/recovery | Graph infrastructure recovery; `bd status`, `bd doctor`, `bd blocked`. |
| Beads Architecture | https://gastownhall.github.io/beads/architecture | Dolt source of truth, auto-commits, sync/recovery/limits. |
| Beads Troubleshooting | https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md | Failure modes: empty ready queue, dependency misuse, repair/sync risks. |
| GitHub Issues | https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues | Baseline issue-tracker capabilities. |
| GitHub CLI changelog | https://github.blog/changelog/2026-06-10-github-cli-projects-issue-types-sub-issues-and-issue-dependencies/ | Agent-readable issue relationships via terminal/JSON. |
| Linear issue relations | https://linear.app/docs/issue-relations | Blocking/related/duplicate baseline. |
| Task Master task structure | https://docs.task-master.dev/capabilities/task-structure | Task graph baseline with dependencies/test strategy. |
| Task Master clusters | https://tryhamster.com/docs/taskmaster/capabilities/clusters | Execution topology and parallel task groups. |
| Jökull `/babysit-pr` | https://www.solberg.is/babysit-pr | PR signal triage and exit criteria. |
| Jökull Claude Code usage | https://www.solberg.is/how-i-use-claude-code | Skills / PR workflow context. |
| HumanLayer “Skill Issue” | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | Research as state; subagents/context firewall; harness discipline. |
| HumanLayer ACE FCA | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md | Progressive disclosure / right context at right time. |
| Anthropic multi-agent research system | https://www.anthropic.com/engineering/multi-agent-research-system | Subagent objective/output/tools/source boundaries. |
| Mark Erikson AI workflow setup | https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/ | Reviewer role, context tools, source-state examples. |
| `markerikson/opencode-config-example` | https://github.com/markerikson/opencode-config-example | Read-only reviewer, DiffLoupe, config examples. |
| `cachebro` | https://github.com/glommer/cachebro | Source-state mismatch example. |
| Mae Capozzi AI coding workflow | https://maecapozzi.com/blog/my-ai-coding-workflow | PR/Linear/Figma/workflow artifacts. |
| Mae dependency review | https://maecapozzi.com/blog/using-conductor-for-dependabot-reviews | Dependency-review artifact → human classification. |
| Mae telemetry article | https://maecapozzi.com/blog/ai-removes-observability-friction | Traces/spans/Honeycomb as operational signals. |
| Honeycomb Claude Code ROI | https://www.honeycomb.io/blog/measuring-claude-code-roi-adoption-honeycomb | Claude Code telemetry fields/events. |
| LangGraph persistence/interrupts | https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langgraph/interrupts | Runtime boundary. |
| Temporal HITL | https://docs.temporal.io/ai-cookbook/human-in-the-loop-python | Human approval as durable wait in runtime. |
| Pydantic AI durable execution | https://pydantic.dev/docs/ai/integrations/durable_execution/overview/ | Durable runtime family. |
| Pydantic AI Temporal/Restate + DBOS | https://pydantic.dev/docs/ai/integrations/durable_execution/temporal/ ; https://pydantic.dev/docs/ai/integrations/durable_execution/restate/ ; https://docs.dbos.dev/integrations/pydantic-ai | Concrete runtime boundary. |
| Git worktree | https://git-scm.com/docs/git-worktree | Worktree boundary. |
| Claude Code common workflows | https://docs.anthropic.com/en/docs/claude-code/common-workflows | Worktree workflow boundary. |
| OpenAI Codex worktrees | https://developers.openai.com/codex/app/worktrees | Codex worktree boundary. |

## Источники, найденные, но не раскрытые в основном тексте

| Источник | Причина неиспользования |
| --- | --- |
| DoltHub Gas Town posts | Слишком сильно ведут в главу X. |
| SKILL.nb / AEGIS / CodeCRDT / STORM | Полезны для соседних глав о gates, permissions, shared state, но перегружают VII. |
| Реальные HumanLayer/Mae/OpenAI изображения | Визуально ведут к context/runtime/evidence, а не к PWG. |
