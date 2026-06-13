# ADR v4 patched article filesystem inclusion report

## Scope

Included the locally patched `adr_method` atlas article into the repository-style filesystem overlay. The patch was not a full article rewrite: it preserves the accepted ADR v4 article, adds the localized source-excerpt visual assets, and keeps the article in the current accepted atlas style/technical-anchoring regime.

This cumulative overlay also preserves the accepted patched article outputs for `spdd_method`, `persistent_work_graph`, and `gas_town`, so applying it after the earlier accepted plan/package work will not regress the anchor-article filesystem state.

## ADR files included

- `work/atlas/articles/adr_method.md`
- `work/atlas/articles/adr_method_source_usage.md`
- `work/atlas/articles/adr_method_source_transfer_ledger.md`
- `work/atlas/articles/adr_method_image_plan.md`
- `work/atlas/articles/adr_method_external_image_queue.md`
- `work/atlas/articles/adr_method_open_questions.md`
- `work/atlas/articles/adr_method_theory_links.md`
- `work/atlas/articles/adr_method_degradation_and_duplication_audit.md`
- `work/atlas/articles/adr_method_readiness_report.md`
- `work/atlas/articles/adr_method_final_readiness_status.md`
- `work/atlas/articles/adr_method_RESUME.md`
- `work/atlas/articles/adr_method_VERIFY.md`
- `work/atlas/articles/adr_method_MANIFEST.md`
- `work/atlas/articles/adr_method_patch_report.md`

## ADR local assets included

- `content/assets/atlas-images/adr/adr-nygard-minimal-record.svg`
- `content/assets/atlas-images/adr/adr-madr-template-confirmation.svg`
- `content/assets/atlas-images/adr/adr-aws-lifecycle-process.svg`
- `content/assets/atlas-images/adr/adr-design-decision-gate.svg`

## Validation

- all ADR `<img src=...>` references resolve inside the overlay;
- four ADR external candidates are now local `source_excerpt_asset` SVGs;
- remaining ADR external candidates stay in `adr_method_external_image_queue.md` for future asset-pass work;
- blueprint and target plans were not changed by this inclusion.
