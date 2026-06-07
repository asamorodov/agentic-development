# Chat repository workflow protocol update

Дата: 2026-06-07  
Статус: persistent protocol update prepared in archive overlay.  
Scope: `protocols/` and current `work/` discourse/checks.

## Updated persistent protocol files

```text
protocols/rules/chat-github-repo-work-protocol.md
protocols/skills/chat-github-repo-work.md
protocols/rules/chat-codex-transfer-protocol.md
```

## What changed

### 1. Archive overlay mode is now explicit default

For multi-file work ChatGPT should produce an archive overlay unless the user explicitly asks for a direct commit.

### 2. Direct commit mode requires explicit wording

User phrase:

```text
закоммить в <branch-name-or-description>
```

If branch cannot be identified reliably, ChatGPT must ask instead of committing.

### 3. Snapshot-based work is preferred for long files

If user provides repo snapshot, ChatGPT should read long files locally and return full replacement files in the overlay.

### 4. Cumulative archive rule

Until the user provides a new full snapshot or says changes were committed, each new archive must include previous changes.

### 5. Overlay top-level folders

For task-local work: `work/`.

For persistent changes: include repository paths such as:

```text
work/
protocols/
project/
content/
site-spec/
```

### 6. Required companion files

Non-trivial archive overlays should include:

```text
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

### 7. Detailed chat report

ChatGPT must provide a substantial chat report after generating an archive, not just a link.

## Why this matters

This captures the workflow learned during Stage 0.5–0.19:

- GitHub connector can write, but direct write has approval friction.
- Long files are safer through local snapshots.
- Full `work/discourse.md` replacement is preferred when snapshot is available.
- Cumulative overlays prevent manual patch chaining.
- Codex can apply repo files after readiness check.
