# Apply notes — terminology and anti-calque repair pass

Base snapshot: user-uploaded `git(8).zip`.

This overlay contains a targeted terminology and anti-calque repair pass for the same 13 documents that were processed by the Russian language normalization run. It is **not** a new source accumulation pass, not a stylistic rewrite, and not a theoretical restructuring.

## Files to replace

Dossiers:

```text
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
```

Stories:

```text
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

Reports and task files:

```text
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_PASS_REPORT.md
work/reports/SPDD_LANGUAGE_SANITY_PASS_REPORT.md
work/reports/STORIES_13_15_LANGUAGE_EDITORIAL_PASS_REPORT.md
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

## What changed

- Mechanical hybrids such as `prompt-файл`, `источникный срез`, `ИИ-native graph`, `бизнес-prompt`, `Задачи-gate`, `трассируемость-risk`, `область-gate` were repaired.
- In ordinary Russian prose, `AI-driven SDLC` was normalized to `SDLC с ИИ`, and `AI-агент` / `AI-система` were normalized to `ИИ-агент` / `ИИ-система`.
- SPDD received a separate sanity pass: visible `Unit tests` / `unit-тесты` text was normalized to `модульные тесты`, and previously calqued local link targets were restored to the actual story filename and corpus anchors.
- Three new stories received a small editorial repair pass only for mechanical language artifacts.

## Checks performed

```text
python -m json.tool work/checks.json
Markdown link target comparison against git(8).zip for all 13 documents
Raw URL comparison against git(8).zip for all 13 documents
Known-bad-pattern scan after repair
unzip -t final overlay archive
```

Raw URLs remain unchanged. Markdown link targets are unchanged except for deliberate SPDD local-link repair: Jesse Vincent story path, `#spdd-six-step-workflow`, and `#spdd-unit-tests-after-stabilization`.

## Human gates

- This pass deliberately does not replace a future stylistic pass.
- The terminology queue should be reviewed before it becomes a permanent protocol.
- Dossiers remain quarry/source material, not final public theory prose.
