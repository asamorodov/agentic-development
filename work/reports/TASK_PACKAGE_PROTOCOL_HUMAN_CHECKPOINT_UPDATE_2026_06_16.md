# Task package protocol update — human clarification checkpoints

Date: 2026-06-16

## What changed

The task package protocols now distinguish ordinary technical stage stops from checkpoints that ask for human clarification.

The update is intentionally general. It does not mention Atlas articles, mini-dossiers, or any other private shape of the current packages.

## New rule

If a target-group plan explicitly defines a checkpoint, a stop for a human decision, or a question to the user, the package builder preserves that stop by default. The builder may remove or flatten such a stop only when the package-building request explicitly says so. Any such override must be recorded in the build report.

If neither the target-group plan nor the package-building request asks for a staged package, the package is built as before. The builder must not add human questions merely because they might be useful.

## Checkpoint output

A checkpoint that asks for human clarification must be saved as a file and also summarized in the chat. The chat output should include only the useful working content: what was done, the main uncertainty, one question, and the default decision if the user does not answer the question.

If the user answers the question, the executor treats the answer as an instruction for this checkpoint, records its understanding, applies any immediate narrow change that follows from the answer, and then continues the runner. If the user sends only a continuation-like message or an answer that does not address the question, the executor continues according to the default decision recorded in the checkpoint.

## Files changed

- `work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md`
- `work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md`

## Files not changed

No target-group plans, chapter text, Atlas articles, or executor packages were changed by this update.
