# Figure asset catalog

This catalog is the working boundary between three different things that had been accidentally merged in earlier plans:

1. **Local ready assets** — files already stored under `content/assets/**`; they may be inserted as `<figure><img ...></figure>` when they support the surrounding argument.
2. **External real candidates** — real screenshots, diagrams, figures or tables mentioned in dossiers but not yet stored locally; they require source/rights/quality/placement checks before use.
3. **Synthetic figures** — authorial tables, state machines and diagrams created for this theory; they may be written inline as HTML/Markdown but must not pretend to be recovered source images.

## Files in this catalog

- `LOCAL_ASSET_INDEX.md` — complete local image list from `content/assets/theory-images` and `content/assets/story-images` in the current baseline+overlay state.
- `EXTERNAL_REAL_IMAGE_CANDIDATES.md` — high-priority real external candidates extracted from dossiers and not yet downloaded/localized.
- `../reports/A_FRAGMENTS_ASSET_RECOVERY_PASS.md` — decisions made during the A-fragment recovery pass.

## Rules for future fragment work

- Do not turn a ready image into a text diagram merely because a plan says “insert `<figure>`”.
- Do not turn every candidate into an image: if the figure is synthetic, keep it synthetic and label it that way.
- If the candidate is a real external image but not local, leave an explicit `external_real_candidate` / `asset-pass-required` entry rather than silently drawing a text surrogate.
- Inline placement means “place the chosen figure next to the argument it supports”, not “append all figures at the end”.
- A future site assembly pass may rewrite fragment-local paths such as `../../../content/assets/...` to the site-facing `assets/...` paths. The repo-relative truth is stored in `data-repo-path`.
