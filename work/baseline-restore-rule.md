# Baseline restore rule for SPDD and Gas Town

This is a hard process rule.

## Rule

For SPDD and Gas Town / Beads, rebuilding must begin from the old site baseline sections, not from the latest expanded synthesis.

## Required sequence

```text
old site baseline section
→ unchanged seed file
→ detail inventory
→ additive/adaptive rewrite
→ anti-degradation report
→ human gate if any detail is removed or compressed
```

## Required seed files

- `inputs/old_site_baseline/anchor_seed_SPDD_old_site_full.md`
- `inputs/old_site_baseline/anchor_seed_Gas_Town_old_site_full.md`

## What may be changed

Allowed:

- adapt transitions to the new AI-driven SDLC architecture;
- add newer source facts;
- add clearer lifecycle framing;
- split/rename internal headings if that improves structure;
- add links, source notes and diagrams;
- relocate repeated framing to avoid duplication.

Not allowed without human gate:

- compressing old detail;
- replacing old dense prose with a summary;
- losing named mechanisms or examples;
- removing internal structure;
- making SPDD/Gas Town just examples inside a general catalogue.

## Anti-degradation report must check

- old headings preserved or deliberately mapped;
- named mechanisms preserved;
- concrete workflow stages preserved;
- source facts preserved;
- no loss of explanation density;
- all removed material listed with reason and human gate marker.
