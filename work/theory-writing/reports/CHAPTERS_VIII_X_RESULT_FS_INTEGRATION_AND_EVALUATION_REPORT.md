# Chapters VIII–X result FS integration and evaluation

Date: 2026-06-15

## Scope

Integrated uploaded result packages into the current file-system working state:

- `CHAPTER_VIII_PROTECTED_PROCESS_PROFILES_NOSTAGE_RESULT.zip`
- `CHAPTER_IX_EXECUTION_ENVIRONMENT_RUNTIME_RIGHTS_RESULT.zip`
- `CHAPTER_X_GAS_TOWN_BEADS_RESULT.zip`

No Chapter VII result package was supplied in this turn, so Chapter VII was not integrated.

The integration copied the chapter result files and companion files under `work/theory-writing/chapters/` and stored the original result archives under `work/theory-writing/results/`.

## Integrated main chapter files

| Chapter | Main file | Size | Inline external links | Figures |
| --- | --- | ---: | ---: | ---: |
| VIII | `work/theory-writing/chapters/VIII_protected_process_profiles.md` | 31651 chars | 21 | 0 |
| IX | `work/theory-writing/chapters/IX_execution_environment_runtime_rights.md` | 42617 chars | 40 | 0 |
| X | `work/theory-writing/chapters/X_gas_town_beads.md` | 37265 chars | 30 | 2 |

## Evaluation summary

### Chapter VIII

Strong points:

- The chapter has the right individual axis: durable work state shows where the work is, but does not decide how the next session should act.
- The `billing/API` example works as a real routing example: the same work node may require story creation, execution, brownfield investigation, `correct-course`, verification or human checkpoint.
- GSD and BMAD are used functionally rather than as a catalogue. The chapter explains phase discipline, role/story handoff, `correct-course`, and small process rituals.
- The chapter keeps the upper boundary with Gas Town/Beads clear.

Concerns before accepting as canonical:

- The term `профиль` is still too dominant (`Защищённые процессные профили`, `процессный профиль`, `Нужный профиль`). This conflicts with the later terminology decision that `подход`, `способ работы`, `режим продолжения` or sometimes `методология` read more naturally here.
- There are several self-referential or plan-like phrases in the main prose, such as `Для главы VIII...`; they should be rewritten as subject-level statements.
- Visual layer is not integrated: the result leaves only figure candidates. This is acceptable as a text result, but weaker than the current visual-layer standard for chapters I–VI.
- Some English glue remains (`workflow`, `tool`, `brownfield`, etc.). Some of it may be source-specific, but the chapter needs a dedicated natural-Russian pass.

Overall: good conceptual result, but not yet canonical without terminology/natural-Russian cleanup and likely at least one visual figure.

### Chapter IX

Strong points:

- This is the most source-dense and technically concrete of the three results.
- The chapter has a clear individual axis: an agentic task becomes an engineering action only inside a concrete execution environment.
- The chapter successfully separates `sandbox`, `permission`, `approval`, runtime trace, verification material and authority.
- It uses current practice sources broadly and appropriately: Codex, Claude Code, MCP, Kiro, browser/devtools, Sandvault, Roast, Quix/Klaus Kode, Stripe, LangGraph/Temporal/Restate/DBOS.
- The cross-example is strong: `billing/UI` naturally moves from reading and local edits to tests, browser/devtools, API/tool boundaries, secrets/network and trace.

Concerns before accepting as canonical:

- The prose still contains too much English connective material, including full English phrases such as `Model can write code...`, `Missing middle is execution environment`, `blast radius`, `side effects must be logged`, `bounded, observable, recoverable and reviewable`. This needs a substantial Russian-language pass.
- Headings such as `Команда, tool и browser — разные поверхности действия` should be domesticated unless the English terms are intentionally preserved as exact technical names.
- No figures are integrated, although the chapter is visually well-suited to diagrams of execution boundary, action radius and approval loop.
- The chapter is strong but could become dense for the reader; after language cleanup it may need small structural breathing points rather than more content.

Overall: strong technical result and probably the most materially complete of the three, but it needs a serious natural-Russian pass before canonization.

### Chapter X

Strong points:

- The chapter has the clearest individual identity: many local agent actions do not automatically form a manageable project flow.
- Gas Town and Beads are used not as folklore but as a way to explain serviced work flow: claims, gates, queues, working spaces, recovery, backpressure, escalation and return to state.
- The `payment webhook` example is strong and carries the chapter well through dependent work items, stuck claims, unreturned results, gates, merge failures, backpressure and escalation.
- Two local atlas figures are integrated.
- Boundaries with VII, VIII, IX and XI are well maintained.

Concerns before accepting as canonical:

- Some Gas Town/Beads vocabulary remains heavy (`gate`, `backpressure`, `escalation`, `MERGE_FAILED`, `hook`) but much of it is source vocabulary. A light terminology pass should decide which terms stay as technical names and which get explained in Russian on first use.
- The chapter is close to canonical but may still benefit from a final naturalness pass to reduce source-vocabulary density.
- It deliberately does not become a full Gas Town reference. This is good, but if the chapter later needs more visual support, `gastown-basic-workflow.svg` remains a reasonable optional candidate.

Overall: strongest candidate for near-canonical integration among the three; likely needs only a light polishing pass unless a deeper comparison with the final chapter sequence reveals overlap.

## Cross-chapter evaluation

### Size and material intake

The chapters do not all converge to the same hidden size:

- VIII: 31651 chars
- IX: 42617 chars
- X: 37265 chars

This suggests the no-size-cap instruction was at least partially respected. However, VIII is substantially shorter and thinner than IX/X. That may be justified by the source set, but it should be reviewed after terminology cleanup: if GSD/BMAD and small process approaches still feel underdeveloped, an additional source/material pass is warranted.

### Individuality

- VIII: good, but the title and terminology still make it sound more abstract and less natural than the underlying argument.
- IX: strong technical identity, but language cleanup is required so the chapter does not read like partially translated source notes.
- X: strongest individual identity and best fit between plan and result.

### Visual layer

- VIII and IX still need visual integration if they are to match the current chapter standard.
- X already includes two figures and is adequate visually for the present pass.

### Source discipline

All three chapters include inline source links and companion source registers. Source discipline appears good at the integration level. A later audit should verify that the most load-bearing claims in VIII and IX are tied to the right sources, especially where source terms were paraphrased or mixed across tool ecosystems.

## Recommendation

Integrate the three results into the file system as working chapter results, but treat canonical acceptance asymmetrically:

- **Chapter X**: near-canonical after light language/terminology polish.
- **Chapter IX**: materially strong, requires substantial Russian-language cleanup and visual pass.
- **Chapter VIII**: conceptually correct, requires terminology rewrite away from `профиль`, removal of self-commentary, and likely visual pass; consider one additional material pass only if cleanup reveals thinness.

