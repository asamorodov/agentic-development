# S04 guardrail repair note: `persistent_work_graph`

## Audit results

- Read-only paths checked: 46.
- Missing article-specific read-only paths: 0.
- Required future outputs listed and referenced: 9 of 9.
- Unreferenced required outputs: 0.
- No internal length limit or compression instruction was found.
- The unavailable `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` remains a global provenance debt and is not treated as article-specific missing bundle input.

## Problems found

- The plan needed an explicit S04 integrated guardrail section for path grounding, output names, image candidate handling and final verification.
- PWG specifically needs a guardrail distinguishing source-backed facts from local project-design synthesis.
- The visual layer needed sharper classification: local asset, external-real-candidate or synthetic mechanism figure.

## Repairs made

- Updated plan status to S04-checked.
- Added `S04 integrated guardrails` section.
- Added path and output audit statements.
- Strengthened companion invariants around project-design synthesis and visual classification.
- Confirmed that the plan is adapted to PWG-specific level-separation risks rather than copied mechanically from the blueprint.

No article text was written and no article-writing package was built.
