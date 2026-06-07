# Search step 2 results — agent skills and credential leakage

## Selected sources

- `Credential Leakage in LLM Agent Skills` — analyzes 17,022 skills, finds vulnerable skills, cross-modal leakage, debug logging/stdout as major vector, exploitable and persistent leaks.
- Reports about AI-related leaked secrets / MCP configuration risk — useful as caution, but vendor/news sources should be secondary.
- MCP/security materials from previous stages.

## Evaluation

This is directly relevant to agentic SDLC. Secrets risk is not just “don’t commit keys”; it includes agent skills, logs, stdout, prompt injection and local credentials.

## Impact on theory

Part VIII should discuss secrets as environment/tool-boundary artifact. Part XII should include credential rotation/inventory after incidents.
