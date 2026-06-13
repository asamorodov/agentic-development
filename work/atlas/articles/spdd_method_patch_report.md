# SPDD v4 local patch report

## Scope

Patch zones only: no full article rewrite. Added: three human skills section, numeric billing evidence paragraph, fuller `/spdd-reverse` explanation, and three local source-excerpt SVG assets replacing previous external placeholders.

## Metrics

| Metric | Before v4 | Patched v4 | Full rollback | Hard |
|---|---:|---:|---:|---:|
| words | 7255 | 7614 | 9548 | 8131 |
| lines | 348 | 348 | 451 | 363 |
| headings | 23 | 21 | 27 | 24 |
| figures | 12 | 12 | 16 | 13 |
| external placeholders | 6 | 0 | 10 | 8 |
| local source-excerpt assets | 0 | 3 | 0 | 0 |
| inline code fragments | 265 | 301 | 429 | 292 |
| links | 51 | 59 | 84 | 81 |
| table lines | 14 | 19 | 21 | 15 |
| avg sentence length | 20.8 | 20.8 | 21.3 | 21.8 |
| /spdd-reverse mentions | 1 | 4 | 11 | 11 |
| billing numeric anchors | 0 | 8 | 0 | 8 |

## Degradation check

- Existing local Fowler/Thoughtworks assets remain present and all `<img>` paths resolve in the package.
- Three previous external placeholders are replaced by local `source_excerpt_asset` SVG files.
- Average sentence length stayed flat; the patch did not trigger a broad stylistic rewrite.
- The article gained focused technical anchors without returning to a coverage matrix or ledger-driven expansion.
- Main risk: the new skill section adds a concept-level H2. It is placed before workflow because it explains why Canvas and commands still require human engineering judgment.

## Assets added

- `content/assets/theory-images/openspdd-plan-vs-reasons-canvas.svg`
- `content/assets/theory-images/openspdd-code-review-report.svg`
- `content/assets/theory-images/openspdd-sync-bidirectional-flow.svg`

## User style edit application

Applied the user's edited text for the three inserted content zones: the human-skills section, the `/spdd-reverse` explanation, and the numeric billing paragraph. The edit was preserved as the target style, with only mechanical cleanup of markdown link artifacts and restored source citations for the billing details.

Style observation: the user edit improves naturalness mostly by removing secondary explanatory tails and choosing ordinary Russian transitions. This is better treated as a calibration note than as another strict rule: after a factual insertion, do not automatically add a final abstract sentence if the concrete example already carries the point.

