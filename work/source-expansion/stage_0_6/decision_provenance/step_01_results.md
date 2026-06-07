# Search step 1 results — decision provenance / ADR basics

## Selected sources

- `ADR GitHub organization / adr.github.io` — practical hub for ADR usage and templates. Role: baseline practical reference.
- `joelparkerhenderson/architecture-decision-record` — large ADR examples/templates repository. Role: template/reference collection, not theory.
- Michael Nygard-style ADR template — context/decision/status/consequences as compact structure. Role: useful minimal artifact shape.
- RFC model / IETF RFC process — useful as contrast: proposal/discussion/publication/history, not identical to ADR.

## Evaluation

This search confirms that ADR is not a specification. It records a decision and its rationale/consequences. RFC/design proposal is usually pre-decision or discussion-oriented; ADR is accepted-decision memory.

## Impact on theory

Add distinction:

```text
specification says what should be true;
plan says how we intend to proceed;
RFC/design proposal opens a decision surface;
ADR records why a decision was accepted and what consequences were taken.
```
