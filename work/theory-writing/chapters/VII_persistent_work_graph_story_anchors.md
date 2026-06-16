# Story anchors — Chapter VII

## Jökull Sólberg

Use as main signal-triage anchor.

Facts to retain:

- `/babysit-pr` as Claude Code skill around PR lifecycle.
- Detect PR with `gh pr view`.
- Wait for CI and Greptile; run `codex review --base main`.
- Classify feedback as Fix / Dismiss / Escalate.
- Exit criteria: CI green, no untriaged issues, PR ready to merge.
- Max three iterations.
- Real example: CI green, Greptile observation dismissed, Codex found two semantic issues.

Graph interpretation:

- PR is work object with gates/signals.
- Review signal is not command.
- Untriaged issue prevents closure.

## HumanLayer

Use as research/subagent-state anchor.

Facts to retain:

- Research can be wrong and should sometimes be discarded.
- BAML positive example: corrected research improved plan/test strategy.
- Parquet/Hadoop negative example: shallow dependency research led to failed plan.
- Subagents as context firewall; outputs need typed return.
- Progressive disclosure supports right-sized restoration.

Graph interpretation:

- Research output can be accepted/rejected/stale/insufficient/superseded.
- Subagent summary is not durable work state until attached to graph.

## Mark Erikson

Use as source-state/reviewer-role anchor.

Facts to retain:

- `cachebro` / OpenCode mismatch: file read state known to MCP tool but not to edit-safety logic.
- DiffLoupe and read-only reviewer: analyze, do not edit; must fix / should fix / consider.
- Replay MCP/observability: screenshots/logs/recordings as source artifacts.
- `rtk grep` overcompression confused agent.

Graph interpretation:

- Source state must be shared across relevant layers.
- Review output must become graph state before edits.
- Compact restoration must preserve structure.

## Mae Capozzi

Use as artifact/human-classification anchor.

Facts to retain:

- Agent work produces PRs, Linear tickets, traces, spans, GitHub Action comments, dependency-review summaries.
- Human classifies diff/type errors/Honeycomb UI/review/dependency recommendations before merge.
- Honeycomb/Claude Code telemetry gives event/session/tool-action signals.
- Migration/backstop principles mostly deferred.

Graph interpretation:

- Artifact is inspectable but not acceptance.
- Trace can support source state, but trace != PWG.
