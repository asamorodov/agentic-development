
# Patch integration checklist after Stage 0.12

Дата: 2026-06-07  
Статус: checklist for applying detailed patch to `work/approved-ai-sdlc-plan.md`.

## Перед применением

- [ ] Пользователь подтвердил consolidated patch.
- [ ] Пользователь подтвердил Stage 0.12 addendum.
- [ ] Решено, что новые top-level parts не создаются.
- [ ] Решено, что новые deep anchors не создаются.
- [ ] Решено, что Part XII остаётся controlled tail.

## Внести в раздел 0 approved plan

- [ ] 0.9: SDLC artifacts are first-class objects.
- [ ] 0.10: Artifact selection rule.
- [ ] 0.11: Architecture quality and test data are named medium-high evidence/control layers.

## Внести в Part III

- [ ] Различить prompt, requirements, spec, plan, ADR, RFC, contract, traceability.
- [ ] Добавить quality attribute scenario and architecture constraint.
- [ ] Добавить test oracle assumption as evidence-related intent artifact.

## Внести в Part VI

- [ ] Codebase readiness.
- [ ] Context file quality/debt.
- [ ] Software catalog/ownership metadata.
- [ ] Project memory artifacts.

## Внести в Part VII

- [ ] Process/framework layer: GSD/BMAD/Reversa/OpenSpec candidates.
- [ ] Keep medium, not deep.

## Внести в Part VIII

- [ ] Reproducible/runnable environment.
- [ ] Policy-as-code.
- [ ] Secret/credential boundary.
- [ ] Agent workflow specification.
- [ ] Architecture fitness functions / architecture tests.
- [ ] Controlled test environments / service virtualization / test dependencies as code.

## Внести в Part X

- [ ] Evidence package taxonomy.
- [ ] Architecture quality and fitness functions.
- [ ] Test data, test environments and oracle independence.
- [ ] Contract tests and traceability.
- [ ] Agent traces and tool-call logs.

## Внести в Part XI

- [ ] Ownership artifacts.
- [ ] Completion rights distinctions.
- [ ] Audit/provenance record.

## Внести в Part XII

- [ ] Lifecycle tail artifacts.
- [ ] Architecture drift / stale fitness functions.
- [ ] Test data drift / stale fixtures / test environment drift.
- [ ] SBOM/dependency/license inventory.
- [ ] Secrets and credential follow-up.
- [ ] Context cleanup.
