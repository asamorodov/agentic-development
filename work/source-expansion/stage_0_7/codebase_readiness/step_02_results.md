# Search step 2 results — codebase readiness / persistent context files

## Selected sources

- `An Empirical Study of Developer-Provided Context for AI Coding Assistants in Open-Source Projects` — analyzes 401 repositories with Cursor rules; identifies high-level themes such as conventions, guidelines, project information, LLM directives and examples.
- `Agent READMEs: An Empirical Study of Context Files for Agentic Coding` — analyzes 2,303 agent context files from 1,925 repositories; shows these files evolve like configuration code and often contain build/run commands, implementation details and architecture, while non-functional requirements like security/performance are rare.
- `Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?` — warns that context files can reduce task success and increase inference cost when they contain unnecessary requirements; agents tend to respect them, but more context is not always better.

## Evaluation

This is a strong corrective to naïve “just add AGENTS.md” thinking. Context files are SDLC artifacts, but they are not automatically good. They can become configuration debt or misleading governance.

## Impact on theory

Part VI should treat context files as living configuration artifacts with quality requirements, not as generic documentation.
