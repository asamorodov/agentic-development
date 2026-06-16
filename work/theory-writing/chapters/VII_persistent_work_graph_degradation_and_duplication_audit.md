# Degradation and duplication audit — Chapter VII

## Potential degradation

### English glue

P13 improved Russian flow but still contains dense English in technical areas. Final prose pass should reduce unnecessary glue:

- “It is tempting…” → Russian equivalent.
- “The lesson…” → Russian equivalent.
- “source artifact attached to node” in table may remain as field-like phrase but can be Russian in caption.
- “current-practice anchor” can be replaced by «практический якорь».

### Catalog risk

P13 was too sectioned. P14 repair plan merges:

- связи + готовность + claim;
- проверочные сигналы + subagent output;
- runtime boundary + current practice.

Final assembly should follow P14 structure.

### Beads overexposure

Beads appears many times. Each mention must answer one specific work-state question:

- image = graph memory;
- `bd ready/dep/blocked` = readiness;
- coordination = ownership;
- `bd gate` = wait conditions;
- `bd prime` = restoration;
- recovery/troubleshooting = graph hygiene.

Any Beads mention outside this should be removed or folded.

### Evidence chapter bleed

Avoid expanding проверочные основания into full evidence/oracle theory. VII only needs enough to say closure requires classified checking basis.

### Runtime chapter bleed

Avoid explaining Temporal/Restate/DBOS mechanics. Use them only as contrast: execution progress != work semantics.

## Duplication risk with neighboring chapters

| Neighbor | Risk | Current mitigation |
| --- | --- | --- |
| VI | skills/hooks/MCP/context interfaces | VII treats them as delivery mechanisms for PWG-derived context, not as topic. |
| VIII | process profiles/research-plan-implement | VII does not choose action method; only shows state. |
| IX | runtime/worktrees/permissions | VII boundary only; details deferred. |
| X | Gas Town organization | Only boundary mention. |
| XI/XII | evidence/acceptance/authority | Minimal checking-basis layer only. |
| XIII | cleanup/maintenance | Only graph-truth cleanup; full debt/cleanup later. |

## Missing material after audit

No major factual gap remains for VII. Main remaining work is editorial: integrate P14 structure into final chapter and polish language.
