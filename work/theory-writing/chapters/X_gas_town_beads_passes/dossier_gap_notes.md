# Dossier gap notes — Chapter X

## Closed / sufficiently covered

- Gas Town README / docs / design docs were reopened and checked in P04/P15.
- Beads current docs were checked for Dolt-backed architecture, `bd prime`, gates, coordination, routing, workflows and Codex integration.
- Polecat lifecycle/patrol was identified as a stronger source than `MAIL_PROTOCOL` for the central failure/recovery material.
- Scheduler and escalation were checked as current mechanism sources.
- Supporting story anchors now have direct external links in P13.

## Remaining gaps / cautions

1. `gt feed --problems` is now confirmed in Gas Town README through P15, but P13 text still says this was fixed by B3. Final integration should cite README directly in the paragraph about problem feed.
2. Figure paths in P13 use `../assets/...` as site-style paths. Before final repository integration, verify relative paths against the actual final chapter location.
3. `gt prime` is described through README/reference discovery. If final text expands this, add direct source link from README lines around runtime hooks / key commands.
4. `gt mail` remains lightly sourced through docs/reference/B3; no need to expand unless the final text makes it a central mechanism.
5. Beads limitations are included from Architecture docs. Do not add old JSON-backed statements unless explicitly framed as historical.

## Do not fill by speculation

- Do not infer exact internal Gas Town implementation beyond docs/repo statements.
- Do not claim Gas Town is mature, stable, widely adopted, or production-standard.
- Do not claim Beads solves all multi-writer or cross-repo problems; docs identify limits.
- Do not overstate supporting stories as direct implementations of Gas Town-like city layer.
