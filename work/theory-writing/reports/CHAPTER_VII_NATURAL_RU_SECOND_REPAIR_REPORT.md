# Chapter VII natural-Russian second repair report

Date: 2026-06-15

## Scope

Rewrote `work/theory-writing/chapters/VII_persistent_work_graph.md` with a stronger natural-Russian pass after user feedback that the previous version still sounded unnatural in bulk, not just in isolated phrases.

The pass did not add new source material and did not change the chapter argument, section order, links, figures or core examples.

## Main repairs

- Removed the failed `стенограмма` wording and applied `conceptual-translation-glossary.md`: the chapter now uses `переписка`, `полная переписка` or direct description where the function is a raw chat/session record.
- Replaced awkward phrases around `завершение изменения` with more natural Russian about when the work can be closed or considered ready.
- Rewrote the boundary paragraph that previously used `решает соседнюю, но другую задачу`; the chapter now says that durable execution is useful, but answers a different question.
- Reworked multiple artificial noun phrases and English connective fragments around summary/transcript, gates, source state, restoration packet, worktrees and durable execution.
- Preserved source-specific terms where they are actual mechanism names or exact labels: `PWG`, `done`, `claim`, `gate`, `source state`, `restoration packet`, `Beads`, command names, status labels and source-side categories.

## Checks

Performed grep checks for known bad markers:

- `стенограмма` / `стенограмм*`
- `завершение изменения`
- `решает соседнюю`
- `соседн*` in the previous bad construction
- `способ действия`
- `сбой`
- `профайл`, `профиль`, `profile`

No matching bad markers remain in the main Chapter VII text, except allowed source-specific or HTML/file identifiers where applicable.

## Status

Ready as the current working text after natural-Russian repair. It still uses some English source-side terms where those terms are actual names, command outputs, labels or technical mechanisms, not ordinary connective prose.
