# External discovery log — Chapter X

## Discovery status

Web discovery was available. Primary focus was Gas Town/Beads current docs and public source material. Broad market comparison was intentionally rejected to preserve the chapter’s mechanism focus.

## Used discovery sets

1. Gas Town repo and docs:
   - README / key commands / activity feed / problems view / watchdog / merge queue / scheduler.
   - Architecture design: town-level vs rig-level beads.
   - Polecat lifecycle patrol: GUPP/orphan/recovery/merge statuses.
   - Scheduler: capacity/backpressure/deferred dispatch.
   - Escalation: severity route, bead tracking, stale detection.
   - Glossary: GUPP/hook terms.
   - Public docs/reference: roles, convoys, command surface.

2. Beads docs:
   - Architecture: Dolt source of truth, limitations.
   - `bd prime`: AI-optimized context.
   - `bd gate`: blocking/ready behavior.
   - Multi-agent coordination: pin/hook/handoff/fan-out.
   - Routing: pattern routes/cross-repo deps.
   - Codex integration: lifecycle hooks.
   - Workflows/molecules: formula → persistent instance.

3. Supporting stories:
   - Jökull Sólberg public articles.
   - Stripe Minions / ChatPRD workflow pages.
   - Shopify Roast public article and repo README.
   - Mae Capozzi public article.

## Rejected / deferred

| Direction | Decision | Reason |
|---|---|---|
| General multi-agent frameworks/tools market | rejected | Would turn chapter into market overview and duplicate runtime/orchestration chapters. |
| HN/Reddit reaction threads | rejected | Useful for reception, weak for mechanism. |
| `workflows/wisps` direct page | partially blocked/deferred | General workflows page has sufficient wisp material; wisps are not central. |
| Full Gas Town role/template internals | deferred | Risk of turning chapter into reference. |
| Mae/Honeycomb trace images | deferred | Supporting parallel only; would pull visual center away from Gas Town/Beads. |
