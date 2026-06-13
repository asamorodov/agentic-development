# adr_method — RESUME

## Where to resume

Open these files first:

1. `work/atlas/articles/adr_method.md`
2. `work/atlas/articles/adr_method_readiness_report.md`
3. `work/atlas/articles/adr_method_image_plan.md`
4. `work/atlas/articles/adr_method_external_image_queue.md`

## Current state

The article is text-complete for human review. It explains ADR as architectural memory for AI-driven SDLC and keeps the central mechanism explicit: status, reason, alternatives, consequences, `Confirmation`, replacement and safe agent use.

## Do next

The next meaningful pass is asset-pass, not another source-depth pass:

- decide which external-real placeholders become local images;
- check rights/terms, capture date, crop/readability and alt text;
- replace approved placeholders with `<figure><img ...></figure>` blocks;
- keep rejected/deferred candidates in the external queue with reasons.

## Do not do next

- Do not convert the article into a catalogue of ADR templates.
- Do not replace source screenshots/fragments with homemade diagrams where the primary visual source matters.
- Do not treat `proposed`, `reconstructed`, `rejected` or `superseded` ADRs as accepted instructions for an agent.
- Do not expand the article into a general governance overview; gates and owners are present only to explain status, confirmation and replacement.
- Do not use internal dossier fragments as public citations; use public primary sources in the article body.

## Known debts

- External images are placeholders only.
- Stable cross-links to neighboring atlas articles can be added later when final URLs/anchors exist.
