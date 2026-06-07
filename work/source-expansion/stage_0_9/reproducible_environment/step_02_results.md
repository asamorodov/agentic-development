# Search step 2 results — reproducible and hermetic builds

## Источники

- Reproducible Builds project / paper — исходный код and binary artifacts can be checked for correspondence; also hard and costly.
- Bazel hermeticity / sandboxing concepts — useful for build isolation and repeatability.
- Nix sources — reproducibility and dependency isolation, with important limitations and complexity.
- General hermetic build sources — connect environment, dependencies and artifact provenance.

## Оценка

This strengthens Stage 0.8 SBOM/provenance. Evidence package should include not only test output, but also whether the build was produced from a known environment and inputs.

## Влияние на план

Add reproducible/runnable environment and build reproducibility to Part VIII/XII as medium artifacts, not deep cases.
