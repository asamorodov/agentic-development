# A9 source usage

## Использованные первоисточники

| Источник | Как использован в `A9_lifecycle_repair.md` | Где в тексте |
|---|---|---|
| Michael Nygard, “Documenting Architecture Decisions” — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Семантика ADR lifecycle: `proposed`, `accepted`, `deprecated`, `superseded`; сохранение старого решения как исторически действовавшего. | Абзац про ADR как память решения во времени. |
| Martin Fowler, “Architecture Decision Record” — https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | Дисциплина не редактировать принятый ADR задним числом, а заменять новым superseding ADR. | Абзац про журнал того, как долго решение управляло работой. |
| AWS Prescriptive Guidance, ADR process — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | ADR как lifecycle-объект и связь ADR с code review: нарушение ведёт к исправлению кода или пересмотру решения. | Абзац про операционную проекцию ADR. |
| Vercel `adr-skill` — https://github.com/vercel/ai/blob/main/skills/adr-skill/SKILL.md | Добавлен на втором проходе для усиления stale ADR/rules/skills: agent-ready ADR, proactive triggers, code↔ADR linking, post-acceptance lifecycle и revisit triggers. | Абзац про агентские ADR-навыки и риск того, что stale ADR направит новые изменения по уже отменённому решению. |
| Matt Pocock skills issue #212 — https://github.com/mattpocock/skills/issues/212 | Открытый lifecycle-пробел после реализации PRD: исторический снимок, living spec или устаревший документ. | Абзац про хвост спецификации. |
| Matt Pocock skills, `triage/AGENT-BRIEF.md` — https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/triage/AGENT-BRIEF.md | Durable agent brief: поведение, интерфейсы, acceptance criteria; запрет опираться на line numbers и хрупкие file paths. | Абзац про переносимое состояние спецификации. |
| Matt Pocock skills, `triage/SKILL.md` — https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md | Добавлен на source/depth pass: issue state machine, `needs-info` loop, bug reproduction, `ready-for-agent` handoff и сохранение уже выясненного в triage notes. | Абзац про support/user signal как durable issue state and agent brief. |
| Matt Pocock skills, `handoff/SKILL.md` — https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md | Handoff как ссылочная передача состояния без дублирования PRD, plans, ADR, issues, commits и diffs. | Абзац про handoff и конкурирующие копии. |
| Matt Pocock skills, `write-a-skill/SKILL.md` — https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/write-a-skill/SKILL.md | Skill как маленькая ремонтопригодная процедура; scripts для детерминированных операций; review checklist для отсутствия time-sensitive информации. | Абзац про skills/rules как поверхность ремонта. |
| Claude Code memory — https://code.claude.com/docs/en/memory | Добавлен на source/depth pass: `CLAUDE.md` и auto memory дают контекст, но не принудительную конфигурацию; повторяющиеся correction лучше держать в кратких memory/rules; устаревшие или конфликтующие инструкции нужно периодически удалять; hard blocks должны уходить в hooks или settings. | Абзац про границу memory/rule/hook. |
| Claude Code `.claude` directory — https://code.claude.com/docs/en/claude-directory | Добавлен на source/depth pass: разные project/global файлы для context, permissions/hooks, skills, rules, settings и application data. | Абзац про выбор repair target по типу артефакта, а не “добавим в память”. |
| Claude Code hooks — https://code.claude.com/docs/en/hooks; https://code.claude.com/docs/en/hooks-guide | Добавлен на source/depth pass: hooks run at lifecycle points; `PreToolUse` can allow/deny/ask/defer before execution; `PostToolUse` cannot undo completed tool effects; hooks can tighten restrictions. | Абзац про enforceable lifecycle guardrails. |
| Karthik Subramanian, “The Setup Is the Strategy” — https://dev.to/aws-builders/the-setup-is-the-strategy-how-i-orchestrated-a-product-migration-with-claude-code-b92 | Product Migration anchor: 17 memory-файлов, feedback rules, Atlassian MCP truncation и repair rule; на третьем проходе дополнительно использован context funnel, read-only DB, reference implementation, live Swagger docs, per-ticket loop, `manage-mr`, CI/SonarQube gates and QA handoff claims как migration oracle/evidence pattern; статус источника ограничен авторским field report, а не независимой проверкой результата. | Абзацы про learning loop среды и migration oracle как repair evidence. |
| Beads Dependencies — https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md | Dependencies как механизм ready/blocked, влияющий на доступность работы для агента. | Абзац про Persistent Work Graph. |
| Beads `bd gate` — https://gastownhall.github.io/beads/cli-reference/gate | Gate-условия как долговечные асинхронные ожидания, блокирующие workflow step. | Абзац про Persistent Work Graph. |
| Beads `bd prime` — https://gastownhall.github.io/beads/cli-reference/prime | Compact AI-oriented prime для продолжения работы после сжатия или нового запуска. | Абзац про Persistent Work Graph. |
| Beads Recovery — https://gastownhall.github.io/beads/recovery | Добавлен на третьем проходе для work graph cleanup: diagnostic entry points `bd status`, `bd doctor`, `bd blocked` и runbook format. | Абзац про cleanup как диагностику, а не удаление. |
| Beads Architecture — https://gastownhall.github.io/beads/architecture | Добавлен на третьем проходе для recovery sequence и осторожность вокруг `bd doctor --fix`, backup и dry run. | Абзац про безопасный cleanup графа. |
| Claude Code worktrees — https://code.claude.com/docs/en/worktrees | Добавлен на третьем проходе для физического хвоста исполнения: worktree isolation, cleanup rules, non-interactive worktree removal и locked running worktrees. | Абзац про worktree/branch/temp-state cleanup как stale context. |
| GSD `COMMANDS.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md | Разделение verify/ship; PR body из planning artifacts, requirements, verification status и decisions. | Абзац про GSD как фазовый хвост. |
| GSD issue-driven orchestration — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md | Follow-up capture, human gates, отсутствие автоматической публикации/закрытия tracker без пользовательского действия. | Абзац про GSD follow-up loop. |
| BMAD `project-context.md` — https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md | `project-context.md` как живой документ, загружаемый несколькими workflow и обновляемый при изменении решений/patterns. | Абзац про BMAD контекст агента. |
| BMAD Established Projects — https://docs.bmad-method.org/how-to/established-projects/ | Очистка завершённых planning artifacts, чтобы старые документы не оставались ложным активным контекстом. | Абзац про BMAD cleanup. |
| BMAD `bmad-retrospective/SKILL.md` — https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md | Ретроспектива как перенос уроков, технического долга, замечаний ревью и пробелов готовности в следующий эпик. | Абзац про BMAD learning loop. |
| Google SRE, “Postmortem Culture: Learning from Failure” — https://sre.google/sre-book/postmortem-culture/ | Добавлен на втором проходе для incident feedback: postmortem как письменная запись, triggers, review и action items как system repair. | Абзац про инцидентный хвост после PR. |
| Pact Broker `can-i-deploy` — https://docs.pact.io/pact_broker/can_i_deploy | Добавлен на втором проходе для release feedback: contract verification matrix, коды завершения для решения deploy/no-deploy, deployment record после release. | Абзац про release feedback и contract matrix. |
| Argo Rollouts Analysis — https://argo-rollouts.readthedocs.io/en/stable/features/analysis/ | Добавлен на втором проходе для release feedback: `AnalysisTemplate`/`AnalysisRun`, success/failure conditions, inconclusive rollout pause. | Абзац про release feedback и canary/progressive delivery metrics. |
| Claude Code best practices — https://code.claude.com/docs/en/best-practices | Добавлен на третьем проходе как источник по oracle/evidence: tests, build exit code, linter, fixture diff и screenshots как проверки, которые агент может запустить. | Абзац про evidence package и oracle provenance. |

## Прочитанные внутренние материалы, не использованные как citation targets

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` — композиционная позиция A9 внутри Части XIII и связь с PWG/evidence/completion.
- `work/theory-writing/CORE_NODES_WRITING_PLAN.md` — главный тезис A9 и проверка качества: не превращать хвост в cleanup list.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` — правила использования рабочих документов и пакетной writing-логики.
- `work/dossiers/ADR_METHOD_DOSSIER.md` — навигация к Nygard, Fowler, AWS и ADR operational projection.
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` — навигация к Beads dependencies/gate/prime.
- `work/dossiers/GSD_METHOD_DOSSIER.md` — навигация к GSD verify/ship и issue-driven orchestration.
- `work/dossiers/BMAD_METHOD_DOSSIER.md` — навигация к project-context, established-project cleanup и retrospective.
- `content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md` — навигация к skills sources и issue #212.
- `work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md` — навигация к Subramanian migration source.
- Языковые и provenance-протоколы из `protocols/rules/` — использованы как правила стиля и ссылок.

## Сознательно не использовано

- Внутренние досье, планы и отчёты не поставлены как ссылки в основном теоретическом тексте.
- Reddit Product Migration thread, Winder.AI, Augmented Code, TechChannel/Swimm и другие migration sources не использованы в основном тексте, чтобы не превращать A9 в обзор migration cases.
- Более широкий incident-management обзор не раскрывался; для A9 использован только Google SRE postmortem culture как источник для структурного тезиса об action items и review.
- Release-engineering источники за пределами Pact/Argo и Claude Code best practices не добавлялись, чтобы фрагмент не превратился в обзор deployment tooling.

## Feedback-loop pass mapping

Новых внешних источников на feedback-loop pass не добавлялось. Правки в `A9_lifecycle_repair.md` переиспользуют уже открытые первоисточники и связывают repair targets с feedback signals:

| Feedback signal | Repair target в тексте | Источники, которые уже открыты и использованы |
|---|---|---|
| Review / implementation drift | PRD/spec status, ADR supersession, operational projection | Matt Pocock issue #212; Nygard/Fowler/AWS; Vercel `adr-skill` |
| Failed agent execution / repeated correction | Rule, skill, hook, test, memory rule с trigger и deletion path | `write-a-skill`; Claude Code memory/hooks; Subramanian Product Migration; Claude Code best practices |
| Runtime / rollout / release evidence | Contract matrix, canary metric, deploy record, confirmation criteria | Pact `can-i-deploy`; Argo Rollouts Analysis; Claude Code best practices |
| Incident / support signal | Reviewed action items, triage state, reproduction evidence, runbook, alert, ADR/rule/work item repair | Google SRE postmortem culture; Matt Pocock `triage/SKILL.md` |
| Migration discovery | Migration oracle, compatibility layer, cutover plan, worktree/branch state | Subramanian Product Migration; Claude Code worktrees; Beads Recovery/Architecture |
| Work graph drift | Claims, dependencies, gates, blocked/ready state, evidence attachment | Beads Dependencies, `bd gate`, `bd prime`, Beads Recovery, Beads Architecture |

## Source/depth pass additions

Новые источники этого прохода добавлены только рядом с уже написанной логикой A9:

| Новый источник | Какой пробел закрыт |
|---|---|
| Matt Pocock `triage/SKILL.md` | Связал support/user report с issue state machine, reproduction evidence и durable agent brief. |
| Claude Code memory | Уточнил, что `CLAUDE.md`/auto memory дают контекст, а не enforcement; stale/conflicting rules нужно удалять. |
| Claude Code `.claude` directory | Дал карту выбора между context, permissions/hooks, skills, rules и settings. |
| Claude Code hooks + hooks guide | Отделил enforceable lifecycle guardrail от advisory memory: `PreToolUse` before execution, `PostToolUse` after execution, hook limitations. |


## Content repair pass

Проверка текущего фрагмента не нашла внутренних досье, планов или отчётов в качестве ссылок в `A9_lifecycle_repair.md`: все citation targets ведут на публичные первоисточники или официальную документацию. Внутренние документы остаются только навигацией и композиционным контролем.

По итогам проверки ослаблено единственное потенциально слишком сильное утверждение о Subramanian Product Migration: источник оставлен как авторский field report и как схема evidence/oracle surfaces, а не как независимое доказательство результата миграции. Новые внешние источники не добавлялись, потому что обнаруженные дефекты исправлялись уточнением уже поддержанных утверждений.

## Residual repair pass

Остаточный проход новых источников не добавлял. Проверка нашла не source gap, а несколько устаревших или сухих описаний после предыдущих редакций: Subramanian остаётся field report; Vercel `adr-skill` поддерживает риск stale ADR как отменённого решения; Pact поддерживает коды завершения для решения deploy/no-deploy; BMAD retrospective описана через уроки, технический долг, замечания ревью и пробелы готовности. В основном тексте ссылок на внутренние досье нет.

## Composition / visual / style repair 2026-06-11

Новые источники не добавлялись. Ремонт A9 был редакторским: сохранены публичные первоисточники и точные source-specific claims, но основной текст очищен от служебных подписей к asset, дублирующих router/matrix figures and awkward lifecycle-tail phrasing.

Source usage boundaries after repair:

- Fowler/Thoughtworks continuous-feedback image remains the only inline local image asset; it supports the general feedback-loop/harness-repair frame.
- Nygard/Fowler/AWS/Vercel remain the ADR lifecycle anchors.
- Matt Pocock `AGENT-BRIEF.md`, `/handoff` and `triage` remain anchors for durable state transfer, not a full skills overview.
- Claude Code memory / `.claude` directory / hooks remain anchors for advisory-context vs enforceable-control boundary.
- Subramanian Product Migration remains a field report for migration evidence/oracle surfaces, not proof of universal migration success.
- Beads and Claude Code worktrees remain anchors for logical work-state cleanup and physical execution-state cleanup.
- GSD/BMAD, Google SRE, Pact, Argo and Claude Code best practices remain representative anchors for process, incident, release and verification feedback.

Removed inline figures did not remove source claims; their ideas are now carried by prose or deferred to technical atlas.
