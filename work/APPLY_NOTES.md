# Apply notes — Russian language normalization prompt prep

Base snapshot used in this chat: `git(5).zip`.

This overlay prepares prompt files for a Codex-run language-only normalization pass over active dossiers and three new stories. It does not run the multi-pass workflow and does not edit target dossiers or stories.

## Files to add or replace

```text
work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md
work/prompts/RUN_RUSSIAN_LANGUAGE_NORMALIZATION.md
work/reports/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT_PREP.md
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

If you already applied accepted overlays after `git(5).zip`, this overlay should be applied on top of that working tree. It contains full-file replacements for the files above.

## What was read

```text
AGENTS.md
project/repository-structure.md
protocols/rules/chat-github-repo-work-protocol.md
protocols/rules/discourse-maintenance-rules.md
protocols/rules/russian-language.md
work/automation/README.md
work/automation/run-language-style-loop.cmd
work/automation/run-source-loop.cmd
work/automation/src/prompt-renderer.ts
work/automation/src/run-source-loop.ts
work/prompts/RUN_DOSSIERS_LANGUAGE_STYLE_NORMALIZATION.md
work/prompts/DOSSIER_LANGUAGE_STYLE_NORMALIZATION_PROMPT.md
work/discourse.md
```

## Human gate

Before running Codex, open `work/prompts/RUN_RUSSIAN_LANGUAGE_NORMALIZATION.md` and confirm that the target document list matches the current repository state.

## Checks performed here

```text
python -m json.tool work/checks.json
zip integrity check
text search: no internal informal short name in new prompt/report files
```

## Not performed here

The language normalization workflow itself was not run. No target dossier or story was language-normalized in this overlay.
