# Source Bibliography

Дата обзора: 2026-06-16  
Назначение: рабочий список источников, использованных для practical agentic development field map. Это не полная библиография всего поля, а набор источников, достаточный для стратегического решения по теории, Атласу и dev-cycle.

## Early agent loop / tool use

1. **ReAct: Synergizing Reasoning and Acting in Language Models** — paper.  
   https://arxiv.org/abs/2210.03629  
   Early thought/action/tool-use loop.

2. **MRKL Systems: A modular, neuro-symbolic architecture** — paper.  
   https://arxiv.org/abs/2205.00445  
   External modules and routing.

3. **Toolformer: Language Models Can Teach Themselves to Use Tools** — paper.  
   https://arxiv.org/abs/2302.04761  
   Tool-use learning and API calls.

4. **Reflexion: Language Agents with Verbal Reinforcement Learning** — paper.  
   https://arxiv.org/abs/2303.11366  
   Verbal feedback as material for later attempts.

5. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** — paper.  
   https://arxiv.org/abs/2305.10601  
   Branching and deliberate search.

## Coding-agent products and surfaces

6. **OpenAI Codex CLI documentation** — official docs.  
   https://developers.openai.com/codex/cli/

7. **Introducing Codex** — OpenAI announcement.  
   https://openai.com/index/introducing-codex/

8. **Codex upgrades** — OpenAI announcement.  
   https://openai.com/index/codex-upgrades/

9. **Claude Code documentation** — official docs.  
   https://docs.anthropic.com/en/docs/claude-code/overview

10. **Claude Code hooks** — official docs.  
    https://docs.anthropic.com/en/docs/claude-code/hooks

11. **Claude Code skills** — official docs.  
    https://docs.anthropic.com/en/docs/claude-code/skills

12. **Claude Code subagents** — official docs.  
    https://docs.anthropic.com/en/docs/claude-code/sub-agents

13. **GitHub Copilot coding agent** — official docs.  
    https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent

14. **Assign issues to Copilot** — GitHub blog.  
    https://github.blog/ai-and-ml/github-copilot/assign-issues-to-copilot-from-github-com/

15. **GitHub repository custom instructions / AGENTS.md support** — official docs.  
    https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot

16. **Cursor documentation** — official docs.  
    https://docs.cursor.com/

17. **Cursor AI coding best practices** — Cursor blog/docs.  
    https://www.cursor.com/blog/ai-coding-best-practices

18. **Kiro documentation** — official docs.  
    https://kiro.dev/docs/

19. **Kiro steering** — official docs.  
    https://kiro.dev/docs/kiro/steering/

20. **Kiro specs** — official docs.  
    https://kiro.dev/docs/kiro/specs/

21. **Kiro hooks** — official docs.  
    https://kiro.dev/docs/kiro/hooks/

22. **Kiro powers** — official docs.  
    https://kiro.dev/docs/powers/

23. **Jules documentation** — official docs.  
    https://jules.google/docs/

24. **OpenHands** — open-source platform.  
    https://github.com/All-Hands-AI/OpenHands

25. **The OpenHands Software Agent SDK** — paper.  
    https://arxiv.org/abs/2511.03690

26. **Aider** — official site/docs.  
    https://aider.chat/

27. **Amp Manual** — official docs.  
    https://ampcode.com/manual

28. **Junie documentation** — JetBrains docs.  
    https://www.jetbrains.com/help/junie/get-started.html

29. **Replit Agent docs** — official docs.  
    https://docs.replit.com/replitai/agent

30. **Replit Agent 4 changelog** — official changelog.  
    https://replit.com/changelog/agent-4

## Repository configuration / Instructions-as-Code

31. **AGENTS.md** — open format site.  
    https://agents.md/  
    “README for agents”; useful as cross-agent repository instruction pattern.

32. **Configuring Agentic AI Coding Tools: An Exploratory Study** — paper.  
    https://arxiv.org/abs/2602.14690  
    Study of configuration mechanisms across Claude Code, GitHub Copilot, Cursor, Gemini and Codex; includes 2,926 repositories.

33. **Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests** — paper.  
    https://arxiv.org/abs/2606.13449  
    Shows that instruction files are not automatically beneficial and should be treated as software engineering artifacts.

## Runtime, orchestration, observability

34. **LangGraph overview** — official docs.  
    https://docs.langchain.com/oss/python/langgraph/overview

35. **LangSmith observability concepts** — official docs.  
    https://docs.langchain.com/langsmith/observability-concepts

36. **LangSmith agent evaluation** — official docs.  
    https://docs.langchain.com/langsmith/evaluate-agent

37. **OpenAI Agents SDK** — official docs.  
    https://openai.github.io/openai-agents-python/

38. **OpenAI Agents SDK tracing** — official docs.  
    https://openai.github.io/openai-agents-python/tracing/

39. **Google Agent Development Kit** — official docs.  
    https://google.github.io/adk-docs/

40. **Google ADK announcement** — Google Developers Blog.  
    https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/

41. **Microsoft Agent Framework** — official docs.  
    https://learn.microsoft.com/en-us/agent-framework/

42. **AutoGen human-in-the-loop** — official docs.  
    https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/human-in-the-loop.html

43. **CrewAI docs** — official docs.  
    https://docs.crewai.com/

44. **CrewAI memory** — official docs.  
    https://docs.crewai.com/concepts/memory

45. **LlamaIndex Workflows** — official docs.  
    https://docs.llamaindex.ai/en/stable/understanding/workflows/

46. **ADK Arena** — paper.  
    https://arxiv.org/abs/2606.05548  
    Comparative evidence that framework choice can affect LLM-as-developer performance. Treat as recent evidence.

## Protocols, authorization, security

47. **Model Context Protocol Introduction** — official docs.  
    https://modelcontextprotocol.io/introduction

48. **MCP Authorization** — official spec/docs.  
    https://modelcontextprotocol.io/specification/draft/basic/authorization

49. **MCP Security Best Practices** — official spec/docs.  
    https://modelcontextprotocol.io/specification/draft/basic/security_best_practices

50. **A2A: A new era of agent interoperability** — Google Developers Blog.  
    https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

51. **A2A GitHub** — project repository.  
    https://github.com/a2aproject/A2A

52. **Interoperability Protocols for Agentic AI** — paper.  
    https://arxiv.org/abs/2605.04206

53. **Agent Identity Protocol** — paper.  
    https://arxiv.org/abs/2603.24775

54. **Authenticated Workflows / A Systems Approach to Protecting Agentic AI** — paper.  
    https://arxiv.org/abs/2602.10465

55. **MCP Safety Audit / tool poisoning** — paper.  
    https://arxiv.org/abs/2504.03767

56. **Breaking the Protocol** — paper.  
    https://arxiv.org/abs/2601.17549

57. **SMCP** — paper.  
    https://arxiv.org/abs/2602.01129

## Verification, benchmarks and state contracts

58. **Agentproof: Static Verification of Agent Workflow Graphs** — paper.  
    https://arxiv.org/abs/2603.20356

59. **Benchmarking LLM Agents on Enterprise API Tasks via Code Execution / Agent-Diff** — paper.  
    https://arxiv.org/html/2602.11224v1

60. **SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks** — paper.  
    https://arxiv.org/abs/2507.11059

61. **SWE-smith: Scaling Data for Software Engineering Agents** — paper.  
    https://arxiv.org/abs/2504.21798

62. **RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline** — paper.  
    https://arxiv.org/html/2508.01550v1

## Empirical coding-agent studies

63. **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** — paper.  
    https://arxiv.org/abs/2405.15793

64. **Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub** — paper.  
    https://arxiv.org/abs/2601.15195

65. **AIDev: Studying AI Coding Agents on GitHub** — paper/dataset.  
    https://arxiv.org/abs/2602.09185

66. **Agentic Refactoring: An Empirical Study of AI Coding Agents** — paper.  
    https://arxiv.org/abs/2511.04824

67. **How AI Coding Agents Modify Code: A Large-Scale Study of GitHub Pull Requests** — paper.  
    https://arxiv.org/abs/2601.17581

68. **How AI Coding Agents Communicate: A Study of Pull Request Description Characteristics and Human Review Responses** — paper.  
    https://arxiv.org/abs/2602.17084

69. **Who Writes the Docs in SE 3.0? Agent vs. Human Documentation Pull Requests** — paper.  
    https://arxiv.org/abs/2601.20171

70. **Agentic Much? Adoption of Coding Agents on GitHub** — paper.  
    https://arxiv.org/abs/2601.18341

71. **Understanding the Rejection of Fixes Generated by Agentic Pull Requests — Insights from the AIDev Dataset** — paper.  
    https://arxiv.org/abs/2606.13468

72. **Do Autonomous Agents Contribute Test Code? A Study of Tests in Agentic Pull Requests** — paper.  
    https://arxiv.org/abs/2601.03556

73. **Let’s Make Every Pull Request Meaningful: An Empirical Analysis of Developer and Agentic Pull Requests** — paper.  
    https://arxiv.org/abs/2601.18749

## Bibliography quality note

Some sources are very recent arXiv papers and should be treated as provisional evidence, not settled consensus. Product documentation is date-sensitive and should be rechecked before publication. The theory should use these sources for concrete examples and field signals, while keeping its conceptual frame independent of any single vendor.
