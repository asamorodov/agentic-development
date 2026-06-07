# Decision guide for consolidated patch

Дата: 2026-06-07  
Назначение: помочь пользователю принять решение по Stage 0.5–0.9 без чтения всех промежуточных файлов.

## Что нужно решить сейчас

Принять ли consolidated patch из:

```text
work/reports/CONSOLIDATED_PLAN_PATCH_AFTER_STAGE_0_5_TO_0_9.md
work/decisions/PROPOSED_ADR-0007-sdlc-artifact-and-framework-coverage.md
```

## Вариант A — принять patch полностью

Что это означает:

- обновить `work/approved-ai-sdlc-plan.md`;
- добавить artifact-selection rule;
- добавить ADR/RFC/decision provenance;
- добавить process/framework layer;
- добавить lifecycle-tail artifact cluster;
- добавить traceability/contracts/SBOM/secrets/observability/ownership artifacts;
- создать selected dossiers/notes;
- после этого переходить к skeleton/drafting.

Плюсы:

- меньше скрытых дыр перед writing;
- сильнее единый замысел;
- меньше риска нового каталога.

Минусы:

- ещё один подготовительный шаг;
- увеличивается сложность approved plan.

## Вариант B — принять patch частично

Рекомендуемый минимум:

1. Artifact-selection rule.
2. ADR/RFC/decision provenance.
3. GSD/BMAD as medium framework layer.
4. Lifecycle-tail cluster.
5. Traceability/contracts.
6. Observability/secrets/provenance.
7. Ownership artifacts.

Можно отложить:

- Backstage/software catalog;
- AgentSPEX/OpenSpec;
- policy-as-code;
- reproducible/attestable builds;
- ChainForge/promptware details;
- deep treatment of Reversa.

## Вариант C — отложить patch и начать drafting

Не рекомендуется. Вероятный риск: drafting начнётся по approved v3, затем придется перестраивать Part VI–XII.

## Рекомендуемое решение

Принять patch **частично, но не минимально**:

- внести в approved plan все artifact classes;
- не создавать новые top-level parts;
- не делать новые deep anchors;
- требовать dossiers/notes only for high-risk additions;
- после plan update остановить source expansion and move to skeleton.
