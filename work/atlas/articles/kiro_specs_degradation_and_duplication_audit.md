# kiro_specs — degradation and duplication audit

Статус: `P26_guarded_final_style_current`. Audit reflects the current article after P26 guarded final style pass and companion synchronization. It replaces the accumulated pass log with current checks, risks and closed regressions.

## Current degradation checks

| Check | Status | Notes |
| --- | --- | --- |
| Problem-first entry | Pass | First screen now starts with the weakness of a single prompt for complex change, then introduces Kiro Specs as working artifacts. |
| Standalone concept-first article | Pass | Mini-glossary and reader question make the article readable without prior C5/A10 reading. |
| Not a product feature catalogue | Pass with watch | UI/CLI/Web/MCP/enterprise details are kept when they explain specification-work, execution boundaries, evidence or governance. Continue watching dense CLI/Web/Governance sections. |
| Source provenance | Pass with source-depth debt | Public links point to primary Kiro/Fowler sources; freshness-sensitive claims remain in open questions. |
| Internal materials not cited publicly | Pass | C5/A10/dossiers are companion context only. Public article does not cite them. |
| Boundaries with Spec Kit/SPDD/TDAD/CSDD/ADR/PWG | Pass | Neighbor methods are used as negative boundaries, not as full comparison chapters. |
| Web/CLI overclaim prevention | Pass with freshness debt | Article avoids full parity claims; current Web/CLI status still needs source-depth verification. |
| Governance vs quality proof | Pass | Governance/monitoring table explicitly separates policy/observation from acceptance/evidence. |
| Hooks/status/monitoring vs evidence | Pass | Article states that hooks/status/logs are not evidence unless tied to requirement/design/task/diff/test/PBT review. |
| Visual layer consistency | Pass with asset debt | One local general SDD image, three synthetic mechanism figures and seven external-real placeholders match image plan/queue. |
| Synthetic figures non-decorative | Pass | Productized environment, lifecycle and context-layers figures explain mechanisms not easily held in prose. |
| Russian technical style | Pass | Language passes removed major hybrid/service phrasing. Product labels, URLs, paths and commands intentionally remain in original form. |
| Companion bureaucracy | Pass | P23 compacted source usage, ledger, image plan, queue, open questions, theory links and readiness into current-state files. |

## Current duplication / degradation risks

1. **CLI/Web/Governance density.** These sections contain many product details; later edits should keep only details that support specification-work and boundaries.
2. **Web/CLI freshness.** Product state can change; article must keep cautious wording until source-depth pass verifies current state.
3. **Task-status storage.** Article uses visible task status as execution surface but must not infer storage location.
4. **External visual placeholders.** They must not be mistaken for finished assets; rights/quality/freshness checks remain blockers.
5. **PBT overclaim.** PBT is evidence/feedback, not formal verification or automatic acceptance.
6. **Governance overclaim.** Enterprise policy and monitoring constrain/observe use but do not prove `requirements.md → design.md → tasks.md → diff → tests` correctness.

## Closed regressions by P23

- Public references to internal `досье`, `предыдущий черновик`, `редакторский недобор` are not present in the article body.
- Old service-style captions for external visual candidates are not present in inline figure captions.
- Duplicate standalone `## Проблема` section was removed after problem-first intro.
- Old Quick Plan heading references were synchronized to `Quick Plan: когда полный цикл был бы лишним`.
- Generic C5/A10 companion debt and old synthetic-figure review debt were removed from companion files.

## P23 sync note

No article facts or visual assets were added in P23. The pass repaired companion consistency: source usage now includes the local Fowler asset, image plan includes all current figures, open questions contain only concrete blockers, and ledger is compact rather than bureaucratic.
## P24 style-defect audit

Targeted defects fixed without total rewrite: heavy headings, `методологическая трассировка`, public `C5-логика`, `слой correctness`, `PBT-слой`, `магическая папка`, `рискованно убедительная`, `способ посадки процесса`, and several over-compressed `не X, а Y` style formulations. No source facts, image statuses or core structure changed.
## P25 selective natural rewrite audit

Selective rewrites completed without total restructuring. Fixed remaining style defects: `дисциплина становится интерфейсной`, `событийная автоматика`, meta phrases such as `в объяснении Kiro нужно...` / `безопаснее говорить так`, and several heavy theory/enterprise transitions. Source details, links, figure IDs and boundaries were preserved.

## P26 guarded final style audit

Final style pass completed. Remaining meta/service phrasing was reduced in the intro, scope, Feature Specs, Analyze Requirements, hooks, MCP, CLI/Web, theory and boundary sections. No source facts, URLs, figure IDs, image statuses, commands or product boundaries changed.
