# Persistent Work Graph v4 patch report

Status: localized patch applied to PWG v4 article. No full article rebuild was performed.

## Patch scope

The patch applied the planned detail additions only to the existing v4 article:

- ready/blocked clarification in the dependency queue section;
- minimal gate-condition contract clarification;
- richer `bd prime` / compact recovery context explanation;
- `reopen_required` added to the source-state lifecycle;
- short provenance note for public source links.

No new external screenshots or synthetic figures were added. Existing local image assets were preserved.

## Style filter used

The inserted fragments were reviewed with the local patch style sequence:

1. language check for the new and adjacent paragraphs;
2. style defect audit for pseudo-terms, translation-like constructions, and mechanical over-explaining;
3. selective natural rewrite of only the inserted fragments;
4. guarded final technical style: keep the tone close to the article, do not remove technical anchors, and do not convert prose into protocol-like syntax.

## Degradation check

| Metric | Before patch | After patch |
|---|---:|---:|
| Characters | 61,635 | 63,298 |
| Words | 7,475 | 7,707 |
| Lines | 388 | 395 |
| Figures | 4 | 4 |
| Markdown links | 32 | 32 |
| Inline-code delimiter count | 372 | 384 |
| Average sentence length | 13.7 | 13.8 |

Assessment: no obvious degradation. The article became slightly denser in the intended PWG mechanics, while keeping the same section structure and visual set. The patch did not add large tables, did not change the H1/H2 structure, did not remove existing local assets, and did not reopen the hard coverage/ledger style.

## Image/path check

All local image references in `persistent_work_graph.md` still resolve inside the package:

- `content/assets/theory-images/beads-task-graph-memory.svg`
- `content/assets/theory-images/gastown-architecture.svg`
- `content/assets/theory-images/anthropic-multi-agent-process-diagram.webp`

No new external inline placeholders were introduced.
