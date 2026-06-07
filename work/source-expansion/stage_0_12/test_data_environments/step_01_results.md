# Search step 1 results — test data management basics

## Источники

- Test data management sources — TDM is the creation, preparation, control and distribution of data used for software testing; it supports repeatable data conditions, CI/DevOps and reliable test execution.
- Test data sources — test data covers positive/negative scenarios, edge cases, realistic user scenarios and regression checks.
- Synthetic data sources — synthetic data can mimic real-world data and help where privacy/access limitations block real data, but raises issues: bias, model collapse, accuracy/privacy tradeoff and verification.

## Оценка

Test data is not a minor implementation detail. It is an evidence artifact. Without controlled test data, test results are not stable and may not mean what they appear to mean.

## Влияние на план

Add to Part X evidence package:

```text
test data / fixtures / seeds / synthetic data / masked production-like data
```

Add to Part XII:

```text
test data drift / stale fixtures / privacy-sensitive test data cleanup
```
