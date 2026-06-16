# IX. Figure candidates

Статус P14: inline `<figure>` not inserted. This is deliberate: the structure pass focused on the chapter’s axis and avoided turning the piece into a UI tour.

### Recommended inline candidates for a later visual/asset pass

| Candidate id | Тип | Priority | Placement | Решение |
|---|---|---:|---|---|
| `fig-ix-runtime-rights-stack` | `source_backed_synthetic_figure` | 1 | After introduction or before section 1 | Best single figure. Shows request → environment/worktree/devbox → sandbox/permissions/approval → shell/browser/MCP/network/secrets → hooks/logs/tests → trace → review/PWG. |
| `fig-ix-run-trace-to-work-state` | `source_backed_synthetic_figure` | 2 | Section 7 | Bridge from execution trace to claim/evidence/gate/work state. Should avoid duplicating C4 too much. |
| `fig-ix-codex-permission-prompt-boundary` | `local_image_asset` | 3 | Section 2 | Path: `content/assets/theory-images/openai-codex-permission-prompt.webp`. Use only if chapter needs one real UI anchor. |
| `fig-ix-tool-surface-ladder` | `synthetic_figure` | 4 | Section 3 | Shows read-only docs → private read → test side effect → durable mutation → authority/deployment. |
| `fig-ix-codex-browser-devtools-validation` | `local_image_asset` | Optional | Section 3 | Path: `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`. Use only if browser/devtools becomes central. |
| `fig-ix-fowler-continuous-feedback-hooks` | `local_image_asset` | Optional | Section 4 | Path: `content/assets/theory-images/fowler-harness-continuous-feedback.png`. Use only if hooks/sensors section needs visual support. |
| `fig-ix-humanlayer-too-many-mcp-tools` | `local_image_asset` | Optional | Section 3 | Path: `content/assets/theory-images/humanlayer-too-many-mcp-tools.png`. Use only instead of, not alongside, the synthetic tool ladder. |

### External or missing visual candidates

| Candidate | Status | Note |
|---|---|---|
| Sandvault `08-mike-*` screenshots | Mentioned in manifest, absent in current archive. | Strong candidate for sandbox/worktree boundary, but cannot be inserted without asset-pass/full snapshot. |
| Shopify Roast workflow images | Absent in current archive. | Defer to Roast atlas or dedicated asset pass. |
| Stripe Minions/devbox/benchmark images | Absent in current archive. | Defer to Stripe story/atlas/evidence chapter. |
| Codex dashboard/general UI screenshots | Local assets available, but rejected for main IX. | Risk of UI-tour; permission prompt or DevTools image is more precise. |
