# Apply notes — Russian language normalization run

Base working tree: current `/work` state in the active branch.

This run applies only Russian-language normalization. It does not perform source accumulation, theory rewriting, style rewriting, dossier expansion or story reconstruction.

Changed / added control files:

```text
work/reports/RUSSIAN_LANGUAGE_NORMALIZATION_RUN_REPORT.md
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
```

Processed target documents:

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
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

Each target received at least five new language-normalization pass artifacts. The latest `should_stop` marker is `yes` for every target. `work/dossiers/GSD_METHOD_DOSSIER.md` required six passes.

Manual review note: `work/dossiers/SPDD_METHOD_DOSSIER.md` is marked for manual review because an intermediate pass reported repairing consequences of an encoding-glitch side effect. The quick final checks did not find obvious replacement markers, but the file deserves human inspection before using it as a stable source.

Infrastructure notes:

- some aggregate `status.json` files are absent because shell calls timed out after pass artifacts were written;
- SDK usage limits interrupted the run several times, and the work was resumed after successful SDK probe checks;
- stale worker processes were stopped only after required pass artifacts existed;
- the repeated PowerShell profile signature warning was nonfatal.
