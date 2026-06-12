# A7 composition / visual / style repair report

Date: 2026-06-11

## Evaluation before repair

A7 already performed its central theoretical task: it distinguished **observation** as a signal that helps an agent continue work from **evidence** as a preserved, scoped and owner-accepted basis for a human decision. Its source base was strong: Arvid/browser checks, TDAD, ADR confirmation, Roast logs, Willison research/Showboat/Rodney/transcripts, Stripe verification loops and migration/parity examples all supported the central distinction.

Before repair, the working value was about **8/10**, while publication readiness was closer to **6.5/10**.

## Diagnosed problems

1. **Visual overload.** The main text had 13 inline figures. Several repeated the same status-chain argument or belonged to a technical atlas rather than the core A7 theory.
2. **Recovered-asset captions.** Real local images were captioned as “recovered source illustration / local file,” which exposed the assembly process instead of explaining the figure to the reader.
3. **English connective layer.** Many synthetic figures still used English labels such as `observation`, `verification oracle`, `provenance trace`, `handoff clue`, `evidence package`, `false completion`.
4. **Duplicate visual arguments.** `observation-status-ladder`, `observation-to-evidence-chain`, `working-traces-matrix`, `transcript-status` and `pwg-false-completion` all partially described the same transition from working trace to evidence.
5. **Boundary risk.** TDAD, ADR, Roast, Stripe and migration visuals risked turning A7 into a catalog of evidence mechanisms rather than a theoretical node about the status of signals.

## Applied changes

- Main A7 reduced from **13 figures** to **5 figures**.
- Kept as synthetic figures:
  - `fig-a7-observation-to-evidence-chain`
  - `fig-a7-evidence-type-by-promise`
  - `fig-a7-evidence-chain-pwg`
- Kept as real local assets:
  - `fig-a7-browser-observation-evidence`
  - `fig-a7-showboat-rodney-replay`
- Removed from inline and moved to `A7_figure_candidates.md` as merged/deferred:
  - `fig-a7-observation-status-ladder`
  - `fig-a7-working-traces-matrix`
  - `fig-a7-transcript-status`
  - `fig-a7-tdad-two-oracles`
  - `fig-a7-adr-confirmation-surface`
  - `fig-a7-roast-trace-not-truth`
  - `fig-a7-stripe-minion-evidence-loop`
  - `fig-a7-migration-parity-gate`
  - `fig-a7-pwg-false-completion`
- Rewrote captions for real image assets as public explanatory captions.
- Russianized remaining synthetic-figure connective prose where it was not an exact command, file name, field, status or source title.
- Replaced the weaker formula around “ложное завершение” with more direct Russian phrasing: преждевременное / неподтверждённое завершение.
- Preserved all source-specific facts and external citations.

## Evaluation after repair

- Working value: **~8.4/10**.
- Publication readiness: **~7.5/10**.
- Status: `ready_with_known_debts`.

A7 is now a clearer theoretical node and a better input for C3. Its remaining debts are late-stage: link/freshness check, final terminology decision for `replay`, and a possible final choice about whether both real image assets should remain in the main theory or whether one should move to the technical atlas/story layer.
