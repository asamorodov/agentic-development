
# Post-Atlas dossier-to-chapter gap map

Статус: досье классифицированы как gap-check, source restoration, visual/source queue or optional context.  
Правило: досье не являются public source для публикационных claims; будущая глава должна восстанавливать первоисточник.

| Досье | Mandatory gap-check | Optional | Что проверять | Ограничение |
| --- | --- | --- | --- | --- |
| SPDD_METHOD_DOSSIER.md | IV | III, XI, XIII | source restoration for Fowler/Thoughtworks/OpenSPDD; REASONS Canvas; review/sync/reverse | Do not restore command catalogue. |
| PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md | VII | VI, IX, X, XIII | Beads/PWG vocabulary; gates; prime; dependencies; source-state; failure modes | Do not make GitHub/Linear/Dolt a tool survey. |
| GAS_TOWN_METHOD_DOSSIER.md | X | VII, VIII, IX, XIII | Beads two-tier flow; roles; backpressure; service agents; recovery; local visual candidates | Do not import full Gas Town glossary into every chapter. |
| ADR_METHOD_DOSSIER.md | III, XII | XI, XIII | Nygard/Fowler/MADR/AWS ADR lifecycle; confirmation; cADR/AgenticAKM/Mneme as candidate ADR tooling | Public chapter should cite primary ADR sources, not dossier. |
| SPEC_KIT_METHOD_DOSSIER.md | V | III, VI, XI, XIII | official docs/repo; SDD cycle; constitution; specify/plan/tasks/analyze/implement | Use current official docs if product behavior matters. |
| KIRO_SPECS_DOSSIER.md | V, VI | II, IX, XI, XIII | Feature/Bugfix Specs; Quick Plan; Analyze Requirements; hooks/MCP/Powers; supervised execution | Avoid product tour. |
| CONSTITUTIONAL_SDD_DOSSIER.md | V | III, XI, XII, XIII | constitution; traceability matrix; security/human checkpoints; compliance evidence | Treat research/repo status carefully; don't overstate adoption. |
| TDAD_COMPARATIVE_DOSSIER.md | V, XI | III, XIII | two TDAD lines; executable tests as behavior spec vs regression route; mutation/testing evidence caveats | Do not collapse all evidence into tests. |
| GSD_METHOD_DOSSIER.md | VIII, IX | VI, XI, XIII | `.planning/`, `gsd-core`, `gsd-pi`, routing, model/security policy, recovery | Separate from BMAD and Gas Town. |
| BMAD_METHOD_DOSSIER.md | VIII | III, VI, IX, XI, XIII | PRD/architecture/story/sprint-status; checkpoint preview; correct-course; retrospective | Do not make personas the main theory object. |
| ARMIN_RONACHER_STORY_DOSSIER.md | II, VI, IX | XIII | minimal harness, logs, file memory, maintainer boundary | Use as story anchor, not full method dossier. |
| STRIPE_MINIONS_STORY_DOSSIER.md | IX, XII | VI, XI | internal developer platform, devbox, PR workflow, platform acceptance | Needs source restoration if used for claims. |
| SHOPIFY_ROAST_STORY_DOSSIER.md | IX, XI | VIII, XIII | executable workflow, replay, structured agent steps | Good runtime example, not whole workflow theory. |
| ZIG_NO_AI_POLICY_STORY_DOSSIER.md | XII | CONCLUSION | maintainer policy and external authority boundary | Use only if chapter discusses open-source AI contribution policies. |
| PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md | II, IX | I, XIII | migration trace, context and verification pressure | Optional until exact chapter contract names it. |
| QUIX_KLAUS_KODE_STORY_DOSSIER.md | II, VI | IX | agentic coding practice, context and local workflow | Optional; don't add for symmetry. |

## Общие решения

- Методологические досье читать обязательно только там, где глава опирается на соответствующий метод или где Atlas article мог сжать важное различение.
- Story dossiers читать как вспомогательный слой, когда публичной истории недостаточно для точного фактического якоря.
- Если досье содержит visual candidate, это не означает автоматическую вставку: кандидат идёт в visual routing and asset-pass.
- Если досье содержит устаревшие или исследовательские материалы, будущий package обязан отделить `source restoration` от `content discovery`.
