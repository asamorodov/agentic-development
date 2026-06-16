# Figure candidates — Chapter X

## Included by default in P13

### `fig-x-pressure-mechanism-stack`

- Path: `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg`
- Type: synthetic explanatory figure.
- Use: after central work state / flow service distinction.
- Purpose: map pressure to mechanisms: durable object, lifecycle roles, queues/backpressure, recovery/prime, problem view/service agents.
- Status: included in P13. P14 recommends adding one sentence before it to explain it as a map of the chapter.

### `fig-x-two-tier-beads-flow`

- Path: `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg`
- Type: source-derived local asset based on “Welcome to Gas Town” Figure 6.
- Use: after town-level vs rig-level beads paragraph.
- Purpose: show Gas Town as two layers of work state/addressing, not a single task list.
- Status: included in P13.

## Deferred / optional

### `fig-x-gastown-basic-workflow`

- Path: `content/assets/theory-images/gastown-basic-workflow.svg`
- Decision: optional only if final example is hard to follow. P14 recommends not adding it by default.

### `fig-x-gastown-worker-roles`

- Path: `content/assets/atlas-images/gas-town/gastown-worker-roles.svg`
- Decision: defer; risk of turning chapter into roles glossary.

### `fig-x-beads-task-graph-memory`

- Path: `content/assets/theory-images/beads-task-graph-memory.svg`
- Decision: defer; likely duplicates Chapter VII/PWG.

### Mae/Honeycomb trace images

- Decision: reject/defer for X; supporting story only.

## Path caveat

P13 uses `../assets/...` in figure HTML. Verify final relative path before repository integration.
