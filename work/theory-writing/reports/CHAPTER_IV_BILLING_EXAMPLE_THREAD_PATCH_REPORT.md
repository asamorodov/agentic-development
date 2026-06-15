# CHAPTER IV — billing example thread patch report

## What changed

The billing example is now introduced inside the chapter, not only referenced through the external Fowler/Thoughtworks article.

The example now runs through the main SPDD work points:

- REASONS Canvas: requirements, entities, approach/structure, operations, norms and safeguards;
- `/spdd-generate`: implementation must follow the accepted billing policy, not invent adjacent business rules;
- `/spdd-api-test`: tests check concrete Canvas promises;
- `/spdd-code-review`: review checks architecture, placement and hidden decisions against Canvas;
- `/spdd-prompt-update`: used when the billing policy itself changes;
- `/spdd-sync`: used when the accepted implementation structure changed while behaviour stayed the same.

## Language cleanup

Removed or softened self-referential composition wording around the example and the figure. The chapter now speaks about the billing task itself, not about the usefulness of the example as a chapter device.

## Intent

The patch keeps the chapter from becoming a second SPDD Atlas article. The example is concrete enough for an engineer to understand how the mechanism works, but does not reproduce the full external billing case.
