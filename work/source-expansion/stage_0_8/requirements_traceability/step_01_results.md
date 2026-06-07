# Search step 1 results — requirements traceability basics and matrix

## Selected sources

- Requirements traceability as ability to follow a requirement forward/backward through development, specification, deployment, use and refinement.
- Traceability matrix as table connecting high-level requirements to design, test plan, test cases and implementation artifacts.
- Requirements traceability literature notes toolchain integration as a major challenge.

## Evaluation

Traceability is a missing artifact category. It is not the same as specification, test plan or ADR. It links them.

## Impact on theory

Add `traceability link / traceability matrix` as a cross-cutting artifact:

```text
requirement → specification/design → implementation → test/evidence → release/use
```

Part III introduces it; Part X uses it for evidence; Part XII uses it for maintenance and change impact.
