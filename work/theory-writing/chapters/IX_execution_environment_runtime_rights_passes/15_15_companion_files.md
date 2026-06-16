# P15. Сопутствующие файлы к главе IX

Статус: companion-сводка синхронизирована с реальным текстом `14_14_structure_and_individuality.md`, а не с ранним планом. Отдельные companion-файлы не создавались, потому что текущий рабочий лист требует один рабочий выход. Ниже собраны разделы, которые в полном репозитории могут быть разнесены на `source_register`, `fragment_usage`, `atlas_usage`, `dossier_gap_notes`, `external_discovery_log`, `story_anchors`, `figure_candidates`, `open_questions`, `degradation_and_duplication_audit`.

## 1. Source register

### Внутренние источники и рабочие материалы

| Источник | Как использован в главе IX | Статус |
|---|---|---|
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Задал позицию главы: execution environment, runtime rights, tools, permissions, continuation, след исполнения. | Использован как структурная рамка. |
| `work/theory-writing/fragments/00_spine_map.md` | Поддержал общую lifecycle-ось: изменение движется от намерения к проверке, принятию и устойчивому состоянию. | Использован как фон, без прямого пересказа. |
| `work/theory-writing/fragments/A6_execution_environment_distinctions.md` | Дал различение слоёв среды исполнения: место действия, инструменты/наблюдение, runtime/workflow, platform agent. | Сильно использован, но в P14 переписан в собственную ось главы. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Дал финальную границу: runtime state не равен work state; след запуска должен быть связан с claim/gate/PWG. | Сильно использован в финальных разделах. |
| `work/theory-writing/fragments/A6_figure_candidates.md` | Дал исходные решения по визуальному слою: Sandvault, HumanLayer, runtime/PWG. | Использован в P12; в P14 inline-фигуры не вставлялись. |
| `work/theory-writing/fragments/C4_figure_candidates.md` | Дал решения по trace→PWG and durable execution vs work graph. | Использован в P12 and final bridge. |
| `content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md` | Anchor для browser loop, allow/deny, запрет опасных команд and bypass-through-script failure. | Использован как story anchor. |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Anchor для harness engineering, tool surface pressure, skills/progressive disclosure, subagents/context firewall. | Использован как story anchor. |
| `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md` | Anchor для Sandvault, sandboxed user, worktrees, controlled transfer. | Использован как story anchor. |
| `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md` | Anchor для local harness: scripts, logs, browser, email stdout, code/CLI instead of everything-as-MCP. | Использован как story anchor. |
| `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` | Anchor для platform agents, Minions, realistic test environments and steering experiments. | Использован как story anchor. |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | Anchor для workflow runtime, Roast, Boba, cogs, session resume/forking. | Использован как story anchor. |
| `work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md` | Поддержал Ronacher/Pi фактуру. | Использован как secondary internal source. |
| `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md` | Поддержал Roast фактуру. | Использован как secondary internal source. |
| `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md` | Поддержал Stripe фактуру и осторожность с метриками. | Использован как secondary internal source. |

### Внешние источники, фактически вошедшие в P14

| Источник | URL | Использование в главе |
|---|---|---|
| OpenAI Codex sandboxing | `https://developers.openai.com/codex/concepts/sandboxing` | Разведение sandbox and approval policy; рабочая область, network, spawned commands. |
| OpenAI Codex Agent approvals & security | `https://developers.openai.com/codex/agent-approvals-security` | Default local network off, OS-enforced sandbox, security framing. |
| OpenAI Codex permissions | `https://developers.openai.com/codex/permissions` | Permission profiles, `:read-only`, `:workspace`, `:danger-full-access`; separate controls for app connectors, MCP, browser, cloud, approved escalations; network trust nuance. |
| OpenAI Codex Auto-review | `https://developers.openai.com/codex/concepts/sandboxing/auto-review` | Reviewer swap not permission grant; denial should not trigger workaround/circumvention. |
| OpenAI Codex rules | `https://developers.openai.com/codex/rules` | `prefix_rule`, allow/prompt/forbid, most restrictive wins, shell splitting. |
| OpenAI Codex MCP | `https://developers.openai.com/codex/mcp` | MCP as external tools/context surface; STDIO/HTTP, auth, server instructions. |
| OpenAI Codex worktrees | `https://developers.openai.com/codex/app/worktrees` | Multiple independent tasks in background worktrees, handoff. |
| Claude Code Security | `https://code.claude.com/docs/en/security` | Read-only default, explicit permissions, MCP trust caveat. |
| Claude Code permission modes | `https://code.claude.com/docs/en/permission-modes` | `acceptEdits`, `plan`, `auto`, `bypassPermissions`; review boundary. |
| Claude Code Chrome extension | `https://code.claude.com/docs/en/chrome` | Browser/devtools as observation and action surface; login-state risk. |
| Claude Code hooks | `https://code.claude.com/docs/en/hooks` | Hooks events and handler types: shell, HTTP, prompts, lifecycle. |
| Kiro hooks | `https://kiro.dev/docs/hooks/` | IDE hook pattern: events, predefined agent prompts or shell commands. |
| MCP tools specification | `https://modelcontextprotocol.io/specification/draft/server/tools` | Tools as model-controlled capabilities for external systems. |
| MCP Authorization specification | `https://modelcontextprotocol.io/specification/draft/basic/authorization` | Authorization/trust boundary. |
| MCP Security best practices | `https://modelcontextprotocol.io/specification/draft/basic/security_best_practices` | Confused deputy, security framing, trust concerns. |
| Arvid Kahl, “How to actually use Claude Code to build serious software” | `https://thebootstrappedfounder.com/how-to-actually-use-claude-code-to-build-serious-software/` | allow/deny, browser loop, command bypass story. |
| HumanLayer, “Skill Issue” | `https://www.humanlayer.dev/blog/skill-issue` | Harness engineering, tools, skills, subagents/context firewall. |
| HumanLayer, “Skill Issue: Harness Engineering for Coding Agents” | `https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents` | Tool overload, harness as agent environment. |
| Mike McQuaid, “Sandboxed Agent Worktrees” | `https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/` | Sandvault, sandboxed user, worktrees, controlled transfer. |
| Sandvault repository | `https://github.com/webcoyote/sandvault` | Commands and implementation anchor for Sandvault. |
| Fowler, “Harness engineering for coding agents” | `https://martinfowler.com/articles/harness-engineering.html` | guides/feedforward, sensors/feedback, LLM-oriented feedback. |
| Armin Ronacher, “Agentic Coding” | `https://lucumr.pocoo.org/2025/6/12/agentic-coding/` | Local harness, scripts/logs/browser/runtime details. |
| Armin Ronacher, “Code MCPs” | `https://lucumr.pocoo.org/2025/8/18/code-mcps/` | Code/CLI vs MCP; local tool surface. |
| Pi repository | `https://github.com/earendil-works/pi` | Minimal local harness anchor. |
| Shopify Engineering, “Introducing Roast” | `https://shopify.engineering/introducing-roast` | Roast, Boba, deterministic work + bounded agent + checks. |
| Shopify Roast repository | `https://github.com/Shopify/roast` | `cmd`, `ruby`, `chat`, `agent`, `map`, `repeat`, `call`, session resume/forking. |
| Daniel Doubrovkine, Roast walkthrough | `https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html` | Ordinary runtime facts: API key, model routing, workflow edits. |
| LangGraph durable execution | `https://langchain-ai.github.io/langgraph/concepts/durable_execution/` | Persistence, interrupts, HITL around tool calls. |
| Temporal documentation | `https://docs.temporal.io/workflows` | Durable workflows, event history, signals/timers/replay. |
| Restate documentation | `https://docs.restate.dev/` | Journaled steps/side effects and replay/skip completed work. |
| DBOS workflow tutorial | `https://docs.dbos.dev/python/tutorials/workflow-tutorial` | Workflow IDs, resuming from last completed step. |
| Stripe integration benchmark | `https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations` | Realistic environments, test Stripe API keys, deterministic graders. |
| Stripe steering experiments | `https://stripe.dev/blog/ai-steering-experiments` | “Don’t whisper”: put guidance on execution path. |
| Homebrew CONTRIBUTING | `https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md` | AI-assisted PR policy and contributor/review responsibility. |

### Источники, использованные в discovery, но не вошедшие явно в P14

| Источник / семейство | Статус | Причина |
|---|---|---|
| OpenAI Codex dashboard / terminal logs / citations UI assets | Использованы только для P12 visual layer. | P14 не вставлял inline-фигуры. |
| Stripe Minions Part 1 / Part 2 / Sessions 2026 | Использованы как фон story anchor. | P14 предпочёл Stripe integration benchmark and steering experiments; Minions PR-counts deliberately not foregrounded. |
| Quix / Klaus Kode primary source | Использован по discovery summary, но без прямой ссылки в P14. | Нужен source audit: если Quix paragraph останется, лучше добавить точный первоисточник или вынести пример в companion/open question. |
| GSD / BMAD / Gas Town atlas | Использованы только как границы соседних глав, не как фактура P14. | Не добавлять их в chapter body без необходимости, чтобы IX не потеряла собственную ось. |

## 2. Fragment usage

| Fragment | Использование | Решение |
|---|---|---|
| A6 execution environment distinctions | Стал базой для различения места действия, инструментальной поверхности, runtime and platform substrate. | В P14 материал переплавлен в главную ось, а не перенесён как список четырёх слоёв. |
| C4 execution runtime to PWG | Использован в разделе 5 and 7: runtime state does not equal work state; след запуска требует claim/gate/PWG. | Сохранить как финальный мост; не разворачивать C4 внутрь IX полностью. |
| 00 spine map | Поддерживает lifecycle framing: execution is middle layer between intent and evidence/acceptance. | Оставлен как фон; без прямой ссылки. |
| A6 degradation/duplication audit | Помог не сделать IX копией A6. | Структурная правка P14 уменьшила риск повтора A6. |
| C4 degradation/duplication audit | Помог удержать границу runtime vs work state. | Финальная часть P14 всё ещё близка к C4; нужна осторожность в будущей редакции. |

## 3. Atlas usage

| Atlas / article | Использование в P14 | Комментарий |
|---|---|---|
| Persistent Work Graph | Явно появляется в финальной границе: run log must be attached to claim/work item/gate/state. | Использовано как мост, не как отдельная тема. Это правильно для IX. |
| GSD / Open GSD | Не используется в тексте P14. | Не добавлять ради полноты; chapter IX does not need GSD mechanics. |
| BMAD | Не используется в тексте P14. | Не добавлять, чтобы глава не превращалась в process-framework overview. |
| Gas Town | Не используется в тексте P14. | Нет прямой необходимости. |
| Roast as atlas-like mechanism | Используется фактически как workflow runtime story/source, а не как atlas article. | Если позже появится Roast atlas article, можно заменить часть source exposition ссылкой/мостом, но не нужно ослаблять текущую фактуру. |

## 4. Story anchors

| Anchor | Роль в главе | Где в P14 |
|---|---|---|
| Arvid Kahl | Бытовая практика allow/deny, browser loop, bypass-through-script failure; показывает, что command rules need semantic boundary. | Section 3. |
| HumanLayer | Tool/harness surface: too many tools, skills, progressive disclosure, subagents/context firewall. | Section 3. |
| Mike McQuaid / Sandvault | Sandbox/worktree boundary: separate user, controlled transfer, worktree isolation. | Section 1 and 2. |
| Armin Ronacher / Pi | Local harness: scripts, logs, browser, email stdout; code/CLI can be better than MCP. | Section 4. |
| Shopify Roast | Executable workflow: deterministic steps + bounded agent + checks; cogs, session resume/forking. | Section 5. |
| Quix / Klaus Kode | Deterministic orchestration around bounded Claude Code step; prompt/MCP catalog brittleness. | Section 5, but needs direct source audit. |
| Stripe Minions / Stripe benchmark | Platform substrate, realistic test environments, deterministic graders, payment-domain example. | Section 6. |
| Homebrew policy | Review/authority around AI-assisted PRs. | Section 6. |

## 5. Figure candidates

Статус P14: inline `<figure>` not inserted. This is deliberate: the structure pass focused on the chapter’s axis and avoided turning the piece into a UI tour.

### Recommended inline candidates for a later visual/asset pass

| Candidate id | Тип | Priority | Placement | Решение |
|---|---|---:|---|---|
| `fig-ix-runtime-rights-stack` | `source_backed_synthetic_figure` | 1 | After introduction or before section 1 | Best single figure. Shows request → environment/worktree/devbox → sandbox/permissions/approval → shell/browser/MCP/network/secrets → hooks/logs/tests → trace → review/PWG. |
| `fig-ix-run-trace-to-work-state` | `source_backed_synthetic_figure` | 2 | Section 7 | Bridge from execution trace to claim/evidence/gate/work state. Should avoid duplicating C4 too much. |
| `fig-ix-codex-permission-prompt-boundary` | `local_image_asset` | 3 | Section 2 | Path: `content/assets/theory-images/openai-codex-permission-prompt.webp`. Use only if chapter needs one real UI anchor. |
| `fig-ix-tool-surface-ladder` | `synthetic_figure` | 4 | Section 3 | Shows read-only docs → private read → test side effect → durable mutation → authority/deployment. |
| `fig-ix-codex-browser-devtools-validation` | `local_image_asset` | Optional | Section 3 | Path: `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`. Use only if browser/devtools becomes central. |
| `fig-ix-fowler-continuous-feedback-hooks` | `local_image_asset` | Optional | Section 4 | Path: `content/assets/theory-images/fowler-harness-continuous-feedback.png`. Use only if hooks/sensors section needs visual support. |
| `fig-ix-humanlayer-too-many-mcp-tools` | `local_image_asset` | Optional | Section 3 | Path: `content/assets/theory-images/humanlayer-too-many-mcp-tools.png`. Use only instead of, not alongside, the synthetic tool ladder. |

### External or missing visual candidates

| Candidate | Status | Note |
|---|---|---|
| Sandvault `08-mike-*` screenshots | Mentioned in manifest, absent in current archive. | Strong candidate for sandbox/worktree boundary, but cannot be inserted without asset-pass/full snapshot. |
| Shopify Roast workflow images | Absent in current archive. | Defer to Roast atlas or dedicated asset pass. |
| Stripe Minions/devbox/benchmark images | Absent in current archive. | Defer to Stripe story/atlas/evidence chapter. |
| Codex dashboard/general UI screenshots | Local assets available, but rejected for main IX. | Risk of UI-tour; permission prompt or DevTools image is more precise. |

## 6. Dossier gap notes

| Gap | Severity | Suggested repair |
|---|---:|---|
| Quix/Klaus Kode paragraph in P14 lacks direct source link. | Medium | Either add exact primary/source link in a future citation pass or remove/soften Quix paragraph. Current text derives from discovery summary, not chapter-visible source. |
| Some OpenAI Codex URL formats changed during discovery. | Medium | P14 uses current URL set from P08/P11; final citation pass should still verify all Codex links. |
| Visual layer not integrated inline. | Low/Medium | P12 gives decisions; later visual pass can add 2–3 figures. Not a correctness gap, but final chapter may benefit from one conceptual figure. |
| Stripe Minions metrics deliberately not used. | Not a problem | Keep this choice; exact PR counts are context-sensitive and could distract from structural claim. |
| GSD/BMAD/Gas Town absent from chapter body. | Not a problem | They are neighboring framework material, not necessary for IX. |
| Language still contains source-native English. | Medium | P13/P14 reduced protocol language, but final style pass should decide which terms remain source-native and which should be translated. |
| P14 contains a pass-level structural note before the public chapter. | Low | Final assembly should strip the P14 meta note and use the chapter text after the `---` separator. |

## 7. External discovery log

- External discovery was performed in earlier passes and updated during P08/P11. P15 did not run new web search; it synchronized companion notes against the current chapter text.
- Current OpenAI Codex docs replaced older URL guesses. Relevant current pages are: agent approvals/security, sandboxing, permissions, rules, hooks, MCP, worktrees, auto-review.
- Claude Code docs used: security, permission modes, Chrome extension, hooks.
- MCP docs used: tools specification, authorization, security best practices.
- External/current-practice sources used: Arvid Kahl, HumanLayer, Mike McQuaid/Sandvault, Fowler, Ronacher/Pi, Shopify Roast, Doubrovkine, Stripe integration benchmark, Stripe steering, Homebrew policy.
- Durable runtime sources used: LangGraph, Temporal, Restate, DBOS. They are used only to establish the continuation/resume/history distinction, not to compare frameworks.
- Open gap: Quix/Klaus Kode needs a direct link check if retained.

## 8. Open questions

1. Should the public final chapter keep the Quix/Klaus Kode paragraph? It is conceptually useful, but needs direct source provenance or a softer formulation.
2. How many English source-native terms should remain in the Russian text? Current P14 deliberately keeps `sandbox`, `permission`, `approval`, `workflow runtime`, `worktree`, `MCP`, `browser/devtools`, `hook`, `sensor`, `tool`, `authority`, `review`, `run trace`. A style pass should avoid both over-translation and English glue.
3. Should `authority` be translated consistently as “право принять изменение”, “полномочие принять результат”, or left as `authority` when naming the conceptual boundary? P14 mostly explains it in Russian, but the heading still uses English terms.
4. Should the chapter include the synthetic `runtime-rights-stack` figure inline? It is probably the best visual addition, but not required for P14.
5. Should browser/devtools section include the real Codex DevTools validation screenshot, or would that shift the chapter toward UI tour? P12 recommends conditional insertion only.
6. Does final bridge to PWG duplicate C4 too strongly? P14 keeps it as bridge, but a later pass should check C4 itself to avoid repeated wording.
7. Should Homebrew policy stay in chapter IX or move to governance/authority chapter XII? It supports authority/review boundary well, but it is slightly downstream from execution environment.
8. Should a concise table of boundary distinctions be added? Possible risk: makes chapter feel like Handbook rather than theory. Prefer a figure if adding any visual structure.

## 9. Degradation and duplication audit

### Деградации, исправленные в P14

- P13 had many adjacent mechanism headings; P14 collapsed them into larger conceptual sections, reducing catalogue feel.
- Worktrees moved from isolated tool section into “place of action”; this better matches chapter axis.
- Command rules, MCP/tools and browser were grouped as action surfaces; this made them examples of boundary crossing rather than independent product topics.
- Hooks and local harness were grouped as feedback/safe-path machinery; this reduced tool-by-tool enumeration.
- Workflow runtime and durable execution now explicitly point to the boundary “run continuation ≠ work meaning”.
- Platform agents section now more clearly says: platform accelerates candidate production, not acceptance.

### Remaining risks

- P14 is still long and fact-heavy. This is acceptable for the user’s no-limit workflow, but final pass should remove any source catalogue residue.
- Some paragraphs still contain English clauses (`This pattern...`, `At scale...`, etc.). A final natural-Russian pass should rewrite them unless they are intentionally source-native.
- The source density is high in sections 2–6. Final pass should ensure links support claims without making prose feel like a bibliography.
- The Quix paragraph remains under-sourced in the visible chapter text.
- If figures are added later, they must not duplicate the prose or replace ready local/external images. P12 classification should govern that pass.

### Duplication with neighboring materials

| Neighbor | Risk | Current status |
|---|---|---|
| A6 execution environment fragment | High if IX becomes four-layer taxonomy again. | P14 reduced this risk by making billing/UI and boundary transitions the center. |
| C4 runtime to PWG | Medium/high in final section. | P14 uses C4 as bridge only, but wording should be compared before final assembly. |
| Chapter XI evidence/verification | Medium. | IX says trace is not evidence; XI should develop evidence/verification proper. Avoid adding too much testing theory to IX. |
| Chapter XII authority/governance | Medium. | IX needs authority boundary; XII should own governance, acceptance, policy, roles. Homebrew example may be movable. |
| Technical atlas / Handbook | Medium. | Command rules/MCP/hooks details can slide into reference mode. P14 keeps them as examples, but final pass should watch for procedural over-detail. |

## 10. Assembly note

For final assembly, prefer the chapter text inside `14_14_structure_and_individuality.md` after the `---` separator as the current best full version. Apply future style/citation/visual fixes against that version, not against P10/P13, unless a later pass explicitly chooses otherwise.
