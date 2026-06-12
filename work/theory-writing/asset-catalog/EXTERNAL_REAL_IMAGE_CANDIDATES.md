# External real image candidates from dossiers

This register is intentionally separate from local assets and from synthetic author diagrams. It records real images / source screenshots / source tables that are mentioned in dossiers but are not necessarily local files yet. Entries here must not be rewritten into textual diagrams by default. A later pass may download, screenshot, redraw or reject them, but only after checking source, rights, quality and target placement.

## Status values

- `external_real_candidate`: a real image/table/screenshot exists or probably exists in the source; no local file yet.
- `source_table_or_code_fragment`: a source table, code block, notebook fragment, workflow definition or CLI output might be screenshot-worthy, but can often be quoted or redrawn instead.
- `synthetic_redraw_preferred`: the dossier names a source diagram, but current best action is to redraw an original scheme from facts rather than reuse the source image.
- `local_asset_exists`: already recovered in `content/assets/**`.
- `rejected_for_now`: do not use until a stronger reason appears.

## High-priority external candidates

| ID | Source/dossier | Candidate | Status | Current action | Likely fragments |
| --- | --- | --- | --- | --- | --- |
| `ext-adr-nygard-minimal-adr` | `ADR_METHOD_DOSSIER.md` | Nygard article fragment around `Context / Decision / Status / Consequences` and supersession | `external_real_candidate` | rights-check before screenshot; synthetic ADR status diagram is safer for now | A2, A8, A9 |
| `ext-adr-madr-template-confirmation` | `ADR_METHOD_DOSSIER.md` | MADR template fields including `Decision Drivers`, `Decision Outcome`, `Confirmation` | `source_table_or_code_fragment` | prefer a cleaned source-linked excerpt/table; do not make it a decorative screenshot | A2, A9 |
| `ext-adr-aws-lifecycle` | `ADR_METHOD_DOSSIER.md` | AWS ADR process diagrams: create/accept, use in review, update ADR | `external_real_candidate` | rights-check; possible replacement for A8/A9 ADR lifecycle diagrams | A8, A9 |
| `ext-adr-pact-can-i-deploy` | `ADR_METHOD_DOSSIER.md` | Pact Broker `can-i-deploy` matrix/command output | `source_table_or_code_fragment` | use only when contract gate is central; otherwise keep synthetic oracle ladder | A2, A7, A9 |
| `ext-adr-argo-analysis-template` | `ADR_METHOD_DOSSIER.md` | Argo Rollouts `AnalysisTemplate` with metrics and failureLimit | `source_table_or_code_fragment` | candidate for release/repair evidence; no download yet | A9 |
| `ext-adr-sync-marketplace` | `ADR_METHOD_DOSSIER.md` | ADR Sync Marketplace status synchronization screenshot | `external_real_candidate` | rights-check; candidate for lifecycle synchronization surface | A9 |
| `ext-bmad-workflow-map` | `BMAD_METHOD_DOSSIER.md` | Official BMAD Workflow Map Diagram | `external_real_candidate` | inspect/download only after license/quality check; may also be redrawn | A5, future B/C |
| `ext-bmad-project-tree` | `BMAD_METHOD_DOSSIER.md` | Getting Started project tree and quick reference commands | `source_table_or_code_fragment` | redraw or quote; direct screenshot not necessary | A5, Fieldbook |
| `ext-csdd-ar5iv-fig1` | `CONSTITUTIONAL_SDD_DOSSIER.md` | ar5iv/PDF Figure 1: Constitution, spec layer, AI generation, implementation, compliance traceability | `external_real_candidate` | rights-check; possible replacement for CSDD hierarchy if readable | A3 |
| `ext-csdd-ar5iv-table1` | `CONSTITUTIONAL_SDD_DOSSIER.md` | ar5iv/PDF Table 1: compliance traceability matrix | `source_table_or_code_fragment` | better as local redrawn table with attribution | A3, A7 |
| `ext-csdd-ar5iv-fig2` | `CONSTITUTIONAL_SDD_DOSSIER.md` | ar5iv/PDF Figure 2: CWE coverage by implementation effort | `external_real_candidate` | only if metrics become important; otherwise leave pending | A3 |
| `ext-csdd-paper-fig4` | `CONSTITUTIONAL_SDD_DOSSIER.md` | `PAPER.md` Figure 4 three-phase CSDD pipeline | `external_real_candidate` | use cautiously; repo source is draft-like and rights unclear | A3 |
| `ext-csdd-maddevs-workflow` | `CONSTITUTIONAL_SDD_DOSSIER.md` | Mad Devs workflow illustration for constitution → spec → agent instructions → traceability → gates | `synthetic_redraw_preferred` | redraw from facts, do not copy graphic | A3, A8 |
| `ext-gastown-two-tier-beads-flow` | `GAS_TOWN_METHOD_DOSSIER.md` | Steve Yegge / Gas Town Figure 6: Two-Tier Beads Flow | `external_real_candidate` | high-priority candidate; rights/quality check before download | A4, A5, B3 |
| `ext-gastown-changelog-dashboard` | `GAS_TOWN_METHOD_DOSSIER.md` | Convoy Dashboard, two-level Beads architecture and ephemeral Polecat lifecycle screenshots | `external_real_candidate` | candidate for Gas Town deep anchor, not for all A fragments | A5, B3 |
| `ext-beads-ready-queue` | `GAS_TOWN_METHOD_DOSSIER.md` / `PWG_MECHANISM_DOSSIER.md` | Beads ready/blocked dependency queue diagrams or screenshots | `synthetic_redraw_preferred` | redraw compactly unless source diagram has special value | A4 |
| `ext-kiro-faster-smarter-specs` | `KIRO_SPECS_DOSSIER.md` | Kiro blog diagram for parallel task waves / faster specs | `external_real_candidate` | rights-check; otherwise redraw from text | A3, A6 |
| `ext-kiro-deep-spec-analysis` | `KIRO_SPECS_DOSSIER.md` | Deep Spec Analysis pipeline diagram | `external_real_candidate` | rights-check; may replace Kiro analysis synthetic scheme later | A3 |
| `ext-kiro-property-based-testing` | `KIRO_SPECS_DOSSIER.md` | Kiro property-based testing workflow diagram | `external_real_candidate` | rights-check; likely future evidence section | A3, A7 |
| `ext-pwg-github-subissues` | `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | GitHub sub-issues documentation screenshot | `external_real_candidate` | low priority baseline; synthetic comparison likely better | A4 |
| `ext-pwg-linear-blocked-flag` | `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Linear blocked/blocking issue relation screenshot/diagram | `external_real_candidate` | low priority baseline; synthetic comparison likely better | A4 |
| `ext-pwg-anthropic-multi-agent-process` | `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Anthropic multi-agent research process diagram | `external_real_candidate` | rights-check; may support parallel source work | A4, future B/C |
| `ext-pwg-mast-failure-distribution` | `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | MAST paper failure distribution/taxonomy figure | `external_real_candidate` | use only if multi-agent failure taxonomy becomes central | A4 |
| `ext-spec-kit-full-sdd-cycle` | `SPEC_KIT_METHOD_DOSSIER.md` | Spec Kit docs Mermaid/flowchart `Full SDD Cycle` | `external_real_candidate` | likely redraw own version; do not screenshot docs by default | A3 |
| `ext-spec-kit-repo-tree` | `SPEC_KIT_METHOD_DOSSIER.md` | GitHub repo tree with `integrations`, `templates`, `extensions`, `presets`, `workflows` | `source_table_or_code_fragment` | better redraw as integration topology | A3 |
| `ext-spec-kit-agents-paper` | `SPEC_KIT_METHOD_DOSSIER.md` | arXiv Spec Kit Agents context-binding figure | `external_real_candidate` | PDF inspection/rights check needed | A3, A6 |
| `ext-tdad-2603-08806-fig1` | `TDAD_COMPARATIVE_DOSSIER.md` | TDAD overview: TestSmith, PromptSmith, Compiled Agent, MutationSmith/spec evolution | `external_real_candidate` | rights-check; high-priority for A3 if TDAD remains detailed | A3, A7 |
| `ext-tdad-2603-08806-fig2` | `TDAD_COMPARATIVE_DOSSIER.md` | semantic mutation testing pipeline | `external_real_candidate` | use only if mutation score caveat is central | A3, A7 |
| `ext-tdad-2603-17973-fig1` | `TDAD_COMPARATIVE_DOSSIER.md` | agentic workflow with TDAD | `external_real_candidate` | rights-check; candidate for test-impact layer | A3, A7 |
| `ext-tdad-2603-17973-fig2` | `TDAD_COMPARATIVE_DOSSIER.md` | AST Parser → Graph Builder → Test Linker → Impact Analyzer → `test_map.txt` → AI Coding Agent | `external_real_candidate` | high-priority candidate for TDAD B if readable | A3, A7 |
| `ext-tdad-2603-17973-fig3` | `TDAD_COMPARATIVE_DOSSIER.md` | P2P test failures per approach | `external_real_candidate` | metrics-only; use only if benchmark comparison is discussed | A7 |
| `ext-tdflow-workflow-fig1` | `TDAD_COMPARATIVE_DOSSIER.md` | TDFlow workflow figure | `external_real_candidate` | adjacent pattern, not main TDAD illustration | A9/future repair |

## Already local real/source candidates used by the recovery pass

| Fragment | Figure id | Local asset | Action |
| --- | --- | --- | --- |
| A1 | `fig-a1-change-lifecycle-overview` | `content/assets/story-images/01-boris-agentic-lifecycle.svg` | replaced empty candidate block with local story/source lifecycle image |
| A1 | `fig-a1-evidence-and-authority` | `content/assets/theory-images/openai-codex-citations-evidence.webp` | replaced empty candidate block with local source evidence UI screenshot |
| A1 | `fig-a1-session-trace-vs-durable-state` | `content/assets/theory-images/beads-task-graph-memory.svg` | replaced empty candidate block with local Beads/PWG state image |
| A3 | `fig-a3-spdd-closed-loop` | `content/assets/theory-images/fowler-spdd-workflow.svg` | replaced synthetic ASCII with local source image |
| A3 | `fig-a3-drift-taxonomy` | `content/assets/theory-images/fowler-spdd-code-review.svg` | deferred to B1/SPDD-focused section after A3 visual repair; do not use as text surrogate |
| A4 | `fig-a4-pwg-minimal-node` | `content/assets/theory-images/beads-task-graph-memory.svg` | replaced empty candidate caption with local Beads/PWG scheme |
| A5 | `fig-a5-method-pwg-organization-stack` | `content/assets/theory-images/gastown-architecture.svg` | inserted Gas Town architecture as real anchor for organizational layer |
| A6 | `fig-a6-humanlayer-harness-components` | `content/assets/story-images/07-humanlayer-harness-components.png` | replaced synthetic harness components block |
| A6 | `fig-a6-sandvault-separate-user-worktrees` | `content/assets/story-images/08-mike-sv-claude.png` | replaced synthetic Sandvault block |
| A6 | `fig-a6-mcp-context-cost-vs-deterministic-code` | `content/assets/theory-images/humanlayer-too-many-mcp-tools.png` | replaced synthetic MCP context cost block |
| A7 | `fig-a7-browser-observation-evidence` | `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` | kept inline as local image asset after A7 repair; public caption, no service recovery text |
| A7 | `fig-a7-showboat-rodney-replay` | `content/assets/story-images/03-simon-showboat-curl-demo.jpg` | kept inline as local image asset after A7 repair; supports demonstration/provenance boundary |
| A7 | `fig-a7-working-traces-matrix` | `content/assets/theory-images/openai-codex-citations-evidence.webp` | local asset exists but deferred to technical atlas / Codex evidence surface; do not turn into text surrogate |
| A8 | `fig-a8-local-sandbox-action-boundary` | `content/assets/theory-images/mike-superset-worktrees.png` | kept inline after A8 repair as local sandbox/worktree boundary image; public caption, no recovery service text |
| A9 | `fig-a9-post-merge-repair-loop` | `content/assets/theory-images/fowler-harness-continuous-feedback.png` | kept inline after A9 repair as local continuous-feedback image asset; public caption, no recovery service text |

## Not downloaded in this pass

No new external images were downloaded in this pass. The reason is deliberate: many external candidates need rights-check, quality check or a decision whether a redrawn scheme is better than a screenshot. The pass recovered already-local assets and built a queue for future `download/rights/quality` work.
