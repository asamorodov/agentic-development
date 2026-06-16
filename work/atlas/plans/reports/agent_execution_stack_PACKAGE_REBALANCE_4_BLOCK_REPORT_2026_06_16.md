# A2 package rebalance — 2026-06-16

The A2 package was rebuilt after the previous 50+ working-sheet blocks proved unreliable in execution.

The new package keeps one executor package, but uses four planned working blocks:

1. P01 + mini-dossiers 06, 09, 10 — 34 pass sheets.
2. mini-dossiers 05, 07, 08 — 35 pass sheets.
3. mini-dossiers 01, 02, 03, 04 — 37 pass sheets.
4. P13 through Final — 15 pass sheets.

The natural Russian rewrite passes were preserved. To reduce length, each mini-dossier lost one separate low-priority comparative local-angle sheet. The removed material is not forbidden: if it appears naturally in sources, it should be kept in the general collection, limitations, relationship map, or final synthesis.

The cached package is now:

```text
work/atlas/packages/agent_execution_stack_ATLAS_V2_ARTICLE.zip
```

Validation:

- `unzip -t` passed.
- Decoded runner queue shows 125 records.
- Stage pass counts: 34, 35, 37, 15.
- Stage stop count: 3.
