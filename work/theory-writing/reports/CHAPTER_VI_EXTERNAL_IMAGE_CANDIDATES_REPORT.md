# Chapter VI external source image candidates — 2026-06-15

## Purpose

This report collects the external sources currently referenced by Chapter VI and reviews them for possible illustration candidates. The immediate goal is not to insert images into the chapter, but to identify which external materials could support a later asset pass.

The current Chapter VI file is:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

The scan covered the current inline external links in the chapter plus the explicit source lists in the recent Chapter VI patch reports:

```text
work/theory-writing/reports/CHAPTER_VI_ROUTES_AND_MCP_INTERFACE_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_HOOKS_SOURCE_EXPANSION_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_ROUTE_SELECTION_AND_NATURAL_RU_PASS_REPORT.md
```

## High-level conclusion

The best candidates are not ordinary decorative screenshots. The chapter is theoretical and technical, so the strongest assets should either be:

1. synthetic figures redrawn in a consistent local style from source-backed structures; or
2. carefully selected source screenshots/diagrams used as evidence of current practice.

The most useful asset set for Chapter VI would probably be:

1. a route-selection figure near `Маршруты действия`;
2. a skills/progressive-disclosure figure near `Skills`;
3. an MCP interface figure near `MCP-сервер`;
4. a hooks lifecycle / intervention figure near `Где инструкция становится вмешательством`;
5. a subagent/agent-team contrast figure near `Subagents`;
6. optionally, one field-practice screenshot/case box from Mark Erikson or Mae Capozzi.

The first, third and fourth are especially strong. The current synthetic `fig-vi-mcp-server-interface` can be kept, but it could be improved using the official MCP architecture and the MCP empirical paper’s high-level architecture figure.

## Strong candidates

### 1. Route-selection diagram: how the project chooses a working route

**Recommended form:** new synthetic figure.

**Likely placement:** after the expanded section `Маршруты действия: как проект выбирает способ работы`.

**Source basis:**

- LangChain multi-agent visual overview distinguishes `Subagents`, `Handoffs`, `Skills`, and `Router` patterns.
- The current Chapter VI adds a different but compatible project-facing route choice: skill / MCP / subagent / hook.
- Mae Capozzi’s hub-team article shows a practical coordinator that routes tasks through phases and specialists.

**Why it fits the chapter:**

This would give the expanded route-selection section its own visual support. It should not copy LangChain’s application-architecture taxonomy directly. Instead, it should translate that idea into the chapter’s vocabulary:

```text
повторяемая процедура  → skill
внешняя система / живые данные / API → MCP
широкая или независимая работа → subagent
точка обязательного вмешательства → hook
```

**Candidate local path:**

```text
content/assets/theory-images/chapter-vi-route-selection.svg
```

**Use note:** redraw locally. Do not use the LangChain diagrams as-is unless licensing and visual style are explicitly checked.

### 2. Skills as progressive disclosure

**Recommended form:** source-backed redraw or carefully adapted figure.

**Likely placement:** inside `Skills: повторяемые процедуры как часть проекта`, after the paragraph explaining that description quality affects whether the agent selects the right procedure.

**Source basis:**

- Anthropic’s Agent Skills article has several direct image candidates: `SKILL.md` anatomy, additional bundled files, progressive disclosure, skill trigger in the context window, and code execution through skills.
- The article’s text explicitly explains the metadata/body/additional-files loading sequence.
- Matt Pocock / AI Hero provides practice-oriented screenshots of real engineering skills: `grill-me`, PRD, issues, TDD, architecture improvement.

**Why it fits the chapter:**

Chapter VI treats skill not as a magic command, but as a repeatable procedure loaded at the right time. The most useful figure is therefore not a marketplace screenshot; it is a small three-level diagram:

```text
name + description loaded early
        ↓
SKILL.md loaded when selected
        ↓
references / scripts / examples loaded on demand
```

**Candidate local path:**

```text
content/assets/theory-images/chapter-vi-skill-progressive-disclosure.svg
```

**Use note:** prefer a local redraw. If using Anthropic’s images directly, verify licensing and visual fit first.

### 3. MCP server as external interface

**Recommended form:** improve existing synthetic `fig-vi-mcp-server-interface`, or add one compact source-backed redraw.

**Likely placement:** inside `MCP-сервер: управляемый внешний интерфейс`, where the text explains host / client / server, JSON-RPC, lifecycle, transports and primitives.

**Source basis:**

- Official MCP architecture documentation: host creates one client per server; servers can be local over STDIO or remote over Streamable HTTP; MCP has a data layer and transport layer; the data layer uses JSON-RPC and contains lifecycle management plus primitives such as tools, resources, prompts and notifications.
- Official MCP architecture walkthrough shows `initialize`, capability negotiation, `notifications/initialized`, `tools/list`, `tools/call` and change notifications.
- The empirical MCP paper contains a high-level MCP client-server architecture figure and a motivating example showing MCP decoupling tools, prompts and resources from framework-specific interfaces.

**Why it fits the chapter:**

This is the most technical section of the chapter. A figure can make the key correction visible: MCP is not just “more context”; it is a protocol surface that separates read-oriented resources, user-facing prompt templates and model-invoked tools with possible side effects.

**Candidate local path:**

```text
content/assets/theory-images/chapter-vi-mcp-interface.svg
```

**Use note:** redraw locally. The official docs text is enough for a clean figure; the arXiv figures are useful as secondary confirmation but probably too paper-specific for direct insertion.

### 4. Hooks lifecycle / instruction-to-intervention diagram

**Recommended form:** source-backed redraw, possibly split into two smaller figures.

**Likely placement:** inside `Где инструкция становится вмешательством`.

**Source basis:**

- Claude Code Hooks reference exposes a direct hook lifecycle diagram candidate: lifecycle events across session, turns, tool calls, compacting, files and MCP tool execution.
- The same page has a hook-resolution diagram candidate for `PreToolUse`: event fires, matcher checks the tool, condition checks command shape, hook runs, deny blocks the tool call.
- Kiro hooks documentation provides a parallel conceptual split between trigger type and action; actions can be agent prompts or shell commands, and nonzero shell exits can block selected events.
- Gemini CLI hooks documentation frames hooks as lifecycle scripts that add context, validate actions and enforce policy.

**Why it fits the chapter:**

This is probably the best single external-image candidate in the current source set. It directly supports the chapter’s claim that hooks are not merely “another instruction”, but a place where the project can intervene during the agent’s lifecycle.

**Candidate local paths:**

```text
content/assets/theory-images/chapter-vi-hooks-lifecycle.svg
content/assets/theory-images/chapter-vi-hook-resolution.svg
```

**Use note:** the Claude diagrams are very strong but visually dense. A local redraw should simplify them around the chapter’s needs:

```text
SessionStart / UserPromptSubmit → PreToolUse → tool call → PostToolUse → Stop
```

and separately:

```text
event → matcher → hook → allow / deny / add context / require fix
```

### 5. Subagents versus agent teams / worker orchestration

**Recommended form:** use one source-backed redraw, not multiple screenshots.

**Likely placement:** inside `Subagents: разные исполнители для разных частей задачи`.

**Source basis:**

- Claude Code Agent Teams documentation has a direct diagram comparing subagents and agent teams: subagents report back to the main agent; teams coordinate through a shared task list and direct teammate communication.
- Anthropic’s multi-agent research article has two useful diagrams: orchestrator-worker architecture and the complete workflow from lead researcher to subagents to citation agent.
- LangChain’s visual overview shows subagents, handoffs, skills and router patterns.
- Cognition’s “Don’t Build Multi-Agents” provides useful anti-pattern diagrams and the important caution: share context and full traces, not just isolated messages.

**Why it fits the chapter:**

The chapter should not present subagents as a simple performance multiplier. The best figure would show the difference between:

```text
main session → focused subagent → result summary
```

and

```text
team of independent agents → shared task list / coordination overhead
```

A caution note from Cognition can be attached in text or in the caption: parallelization without shared context and trace discipline easily produces incompatible partial results.

**Candidate local path:**

```text
content/assets/theory-images/chapter-vi-subagents-vs-agent-teams.svg
```

**Use note:** redraw locally. Do not overload the chapter with several competing multi-agent architecture diagrams.

### 6. Current practice screenshot: orchestrator / phase workflow / handoff

**Recommended form:** optional case-box or small screenshot, not a central theoretical figure.

**Likely placement:** near the early Mark Erikson paragraph or in a later case-style insert if the chapter gets case boxes.

**Source basis:**

- Mark Erikson’s article includes screenshots of a parent orchestrator session and child subtask sessions.
- Mae Capozzi’s article includes a `Hub Team Workflow Session` screenshot and describes six phases: Planning, Git Setup, Implementation, Testing, Review and PR Creation.
- Kiro Specs has screenshots for task execution and creating a specification.
- Spec Kit has CLI/bootstrap screenshots, but those are more useful for chapters about specification-driven workflows than for Chapter VI.

**Why it fits the chapter:**

This would provide evidence that the chapter’s mechanisms are not purely abstract. However, it is less clean than the protocol diagrams: screenshots are visually busy, tied to individual setups, and may age faster.

**Candidate local paths:**

```text
content/assets/theory-images/chapter-vi-erikson-orchestrator-screenshot.png
content/assets/theory-images/chapter-vi-mae-hub-team-workflow-screenshot.png
```

**Use note:** only use if the next visual pass wants a “field practice” insert. Otherwise cite the sources in text and keep the figure synthetic.

## Secondary candidates

### MCP security / governance figures

The MCP security and governance research papers contain several possible figures:

- high-level MCP architecture and motivating framework-fragmentation example;
- tool poisoning conceptual example;
- vulnerability distribution by server type;
- SKILL.md registry attack lifecycle;
- selection-manipulation and governance-evasion heatmaps;
- MCP proxy / architectural enforcement paper advertises one figure in its abstract metadata;
- VIPER-MCP likely has auditing and exploit-trace figures, though the abstract page was enough to confirm the topic and figure count was not inspected here.

**Use note:** these are valuable, but probably not for Chapter VI’s current main line. They belong more naturally in a later security / governance / threat-model chapter or in a caveat box near MCP/hooks. If used in Chapter VI, the best candidate is the simple MCP client-server architecture / tool-poisoning conceptual figure, not empirical result charts.

### Kiro Specs / task execution

Kiro Specs has a direct `Task execution in Kiro specs` image and describes real-time task status, dependency waves and parallel execution. This could support the idea that project state can become an interface, but it is not as central as MCP/hooks/skills/subagents.

**Use note:** optional; probably better for a later chapter about work graph / task state.

### AGENTS.md / rules layer

AGENTS.md and Codex AGENTS.md sources are strong text sources but weak image sources. A small synthetic figure could show rule precedence:

```text
global instructions → repository AGENTS.md → directory AGENTS.md → user prompt
```

This would support `Правила: что считается устойчивым`, but the chapter already has a broad project-interface figure, and adding too many foundational figures may overload the opening.

## Sources with no useful direct illustration candidate

The following sources are useful as textual or code evidence, but did not produce strong direct visual candidates for Chapter VI:

- most OpenAI Codex documentation pages used in the chapter;
- raw GitHub files in `markerikson/opencode-config-example`;
- raw `mattpocock/skills` `SKILL.md` files;
- BMAD context pages;
- GSD Core README, except as a conceptual five-step loop;
- Stripe Minions posts as fetched by the web reader, where no direct image candidates were exposed;
- Figma, Notion, GitHub MCP, Chrome DevTools MCP, Playwright MCP, Context7 and Sentry MCP pages: useful as examples of MCP server surfaces, but not ideal as central visuals for this chapter.

## Recommended next visual pass

A later visual pass should not try to use every candidate. The best chapter-level image set is probably:

1. keep and possibly refine `fig-vi-project-interface-layers`;
2. add `chapter-vi-route-selection.svg`;
3. add `chapter-vi-skill-progressive-disclosure.svg`;
4. replace or refine `fig-vi-mcp-server-interface` as `chapter-vi-mcp-interface.svg`;
5. add `chapter-vi-hooks-lifecycle.svg`;
6. add at most one subagents figure, preferably `chapter-vi-subagents-vs-agent-teams.svg`.

This would give Chapter VI a coherent visual spine without turning it into a gallery of product screenshots.

## Full external URL inventory from the current chapter

- https://agents.md/
- https://arxiv.org/abs/2506.13538
- https://arxiv.org/abs/2508.14925
- https://arxiv.org/abs/2602.08004
- https://arxiv.org/abs/2604.04323
- https://arxiv.org/abs/2605.11418
- https://arxiv.org/abs/2605.18414
- https://arxiv.org/abs/2605.21392
- https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/sub-agents
- https://cognition.ai/blog/dont-build-multi-agents
- https://developers.figma.com/docs/figma-mcp-server/
- https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/
- https://developers.notion.com/guides/mcp/overview
- https://developers.openai.com/codex/cli/slash-commands
- https://developers.openai.com/codex/concepts/customization
- https://developers.openai.com/codex/concepts/subagents
- https://developers.openai.com/codex/config-advanced
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/hooks
- https://developers.openai.com/codex/learn/best-practices
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/subagents
- https://developers.openai.com/codex/use-cases/frontend-designs
- https://developers.openai.com/codex/use-cases/reusable-codex-skills
- https://docs.bmad-method.org/how-to/project-context/
- https://docs.bmad-method.org/tutorials/getting-started/
- https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server
- https://docs.langchain.com/oss/python/langchain/multi-agent
- https://docs.langchain.com/oss/python/langchain/multi-agent/subagents
- https://docs.stripe.com/mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/ComposioHQ/awesome-claude-skills
- https://github.com/anthropics/skills
- https://github.com/getsentry/sentry-mcp
- https://github.com/github/github-mcp-server
- https://github.com/github/spec-kit
- https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/writing-hooks.md
- https://github.com/markerikson/opencode-config-example
- https://github.com/markerikson/opencode-config-example/blob/main/config/AGENTS.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/agent/orchestrator.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/agent/reviewer.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/command/context.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/command/progress.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/command/subtask-complete.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/command/subtask-resume.md
- https://github.com/markerikson/opencode-config-example/blob/main/config/scripts/devplans.ts
- https://github.com/mattpocock/skills
- https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnose/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md
- https://github.com/mcp
- https://github.com/microsoft/playwright-mcp
- https://github.com/modelcontextprotocol/servers
- https://github.com/open-gsd/gsd-core
- https://github.com/openai/skills
- https://github.com/upstash/context7
- https://hamy.xyz/blog/2026-02_code-reviews-claude-subagents
- https://kiro.dev/docs/hooks/
- https://kiro.dev/docs/hooks/actions/
- https://kiro.dev/docs/hooks/examples/
- https://kiro.dev/docs/hooks/types/
- https://kiro.dev/docs/powers/
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/steering/
- https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- https://lucumr.pocoo.org/2025/8/18/code-mcps/
- https://maecapozzi.com/blog/building-a-multi-agent-orchestrator
- https://mcpservers.org/agent-skills
- https://modelcontextprotocol.io/docs/learn/architecture
- https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- https://modelcontextprotocol.io/specification/2025-11-25
- https://modelcontextprotocol.io/specification/2025-11-25/basic
- https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle
- https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- https://modelcontextprotocol.io/specification/2025-11-25/server/prompts
- https://modelcontextprotocol.io/specification/2025-11-25/server/resources
- https://modelcontextprotocol.io/specification/2025-11-25/server/tools
- https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
- https://www.aihero.dev/5-agent-skills-i-use-every-day
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://www.anthropic.com/engineering/multi-agent-research-system
