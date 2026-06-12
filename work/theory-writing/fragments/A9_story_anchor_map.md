# A9 story anchor map

## Назначение карты

Эта карта фиксирует, какие истории и полевые эпизоды поддерживают A9. В основном фрагменте они не пересказываются: каждый эпизод используется как точный якорь для теоретического хода о ремонте жизненного цикла.

## Якоря

| История / эпизод | Теоретическая функция в A9 | Использованный первоисточник | Статус в основном тексте |
|---|---|---|---|
| Matt Pocock skills: PRD после реализации | Показывает, что forward-flow `grill-me → to-prd → to-issues → implement` оставляет открытый вопрос статуса PRD после завершения задач. | https://github.com/mattpocock/skills/issues/212 | Использовано как якорь устаревшей спецификации. |
| Matt Pocock skills: durable agent brief | Показывает, как спецификация для агента должна переживать изменение file paths и line numbers: поведение и критерии приёмки важнее текущего расположения строк. | https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/triage/AGENT-BRIEF.md | Использовано как якорь для переносимой спецификации. |
| Matt Pocock skills: triage state machine | Показывает, как support/user report становится состоянием issue, свидетельством воспроизведения, `needs-info` loop или долговечным agent brief. | https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md | Добавлено на source/depth pass как мост от пользовательского сигнала к следующей агентской работе. |
| Matt Pocock skills: handoff | Показывает, что handoff не должен создавать новую конкурирующую копию PRD/ADR/issues/diffs; он должен ссылаться на уже существующие артефакты. | https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md | Использовано как якорь для provenance и переноса состояния. |
| Matt Pocock skills: write-a-skill | Показывает skill как маленькую ремонтопригодную процедуру с описанием trigger, разделением reference-материалов и scripts. | https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/write-a-skill/SKILL.md | Использовано как якорь для rules/skills repair. |
| Claude Code memory/hooks boundary | Показывает, что memory/`CLAUDE.md` дают рекомендательный контекст, а hooks/settings/tests/gates подходят для принудительных проверок жизненного цикла. | https://code.claude.com/docs/en/memory; https://code.claude.com/docs/en/claude-directory; https://code.claude.com/docs/en/hooks; https://code.claude.com/docs/en/hooks-guide | Добавлено на source/depth pass как якорь для выбора repair target: memory, rule, skill, hook или gate. |
| Product Migration with Claude Code / Karthik Subramanian | Показывает два слоя: ошибка возвращается в систему как memory rule; migration tail держится на внешних oracle surfaces — read-only DB, reference implementation, live Swagger docs, per-ticket docs, CI/SonarQube gates and QA handoff claims. | https://dev.to/aws-builders/the-setup-is-the-strategy-how-i-orchestrated-a-product-migration-with-claude-code-b92 | Использовано как якорь learning loop и migration oracle, не как доказанный forensic case. |
| GSD phase loop / verify / ship | Показывает, что проверка и отправка имеют отдельные артефакты и gate-условия; PR собирает свидетельства и решения из planning artifacts. | https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md | Использовано как якорь релизного хвоста. |
| GSD issue-driven orchestration | Показывает фиксацию follow-up, human gates и явное взаимодействие с tracker после работы. | https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md | Использовано как якорь для follow-up work after merge. |
| BMAD project-context / established projects / retrospective | Показывает living context, очистку старых planning artifacts и перенос уроков/долга/готовности в следующий эпик. | https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/explanation/project-context.md; https://docs.bmad-method.org/how-to/established-projects/; https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-retrospective/SKILL.md | Использовано как якорь процессного cleanup и learning. |
| ADR lifecycle | Показывает строгую форму supersession, чтобы старое решение не оставалось действующим правилом. | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions; https://martinfowler.com/bliki/ArchitectureDecisionRecord.html; https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | Использовано как якорь ремонта памяти решений. |
| Vercel `adr-skill` | Показывает, как ADR становится agent-readable/agent-actionable артефактом: proactive triggers, implementation plan, verification criteria, code↔ADR links и post-acceptance lifecycle. | https://github.com/vercel/ai/blob/main/skills/adr-skill/SKILL.md | Добавлено на втором проходе как якорь устаревающих ADR/rules/skills. |
| PWG / Beads | Показывает, что состояние работы, dependencies, gates, prime и recovery/cleanup должны быть долговечными и запрашиваемыми; cleanup требует диагностики, backup/dry-run и осторожности вокруг auto-fix. | https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md; https://gastownhall.github.io/beads/cli-reference/gate; https://gastownhall.github.io/beads/cli-reference/prime; https://gastownhall.github.io/beads/recovery; https://gastownhall.github.io/beads/architecture | Использовано как якорь cleanup рабочего графа и evidence gates. |
| Claude Code worktrees | Показывает физический lifecycle tail параллельной работы: изолированные worktrees, правила cleanup, non-interactive leftovers и locked running worktrees. | https://code.claude.com/docs/en/worktrees | Добавлено на третьем проходе как якорь cleanup состояния исполнения. |
| Google SRE postmortem culture | Показывает, что incident feedback должен становиться прошедшими ревью задачами и записью в общий репозиторий инцидентов, а не оставаться неразобранным отчётом рядом с кодом. | https://sre.google/sre-book/postmortem-culture/ | Добавлено на втором проходе как якорь incident feedback. |
| Pact `can-i-deploy`, Argo Rollouts Analysis и Claude Code best practices | Показывают release/session evidence как проверяемую матрицу контрактов, progressive delivery metrics и runnable checks: тесты, build exit code, linter, fixture diff, screenshot evidence. | https://docs.pact.io/pact_broker/can_i_deploy; https://argo-rollouts.readthedocs.io/en/stable/features/analysis/; https://code.claude.com/docs/en/best-practices | Добавлено на втором/третьем проходе как якорь release feedback и oracle provenance. |

## Ограничения карты

- Истории Mark Erikson, Armin Ronacher, Simon Willison и другие кандидаты lifecycle-tail не включены в первый черновик A9. Их можно добавить в source/depth pass, если фрагменту понадобится больше фактуры о review capacity, harness repair или evidence quality.
- Reddit Product Migration thread не использован, потому что текущему фрагменту хватило более проверяемого primary anchor Subramanian для learning loop. Reddit case может понадобиться отдельному migration-tail pass.
- A9 пока не раскрывает SBOM/dependency inventory/supply-chain хвост; это оставлено для будущего фрагмента или расширения Части XIII.
- Новый source/depth pass уточнил Claude Code memory/hooks boundary, но это не означает, что `CLAUDE.md` можно трактовать как hard policy; hard blocking должен жить в hooks/settings/tests/gates.
- Incident/release feedback теперь раскрыт через Google SRE, Pact, Argo и Claude Code best practices, но без отдельного case study реального production outage; при необходимости это можно усилить отдельным публичным incident chain.
- Migration oracle раскрыт через авторский field report Subramanian; его outcome claims не нужно переписывать как независимые факты без PR/CI/review artifacts.


## Second style pass constraints

После второго стилевого прохода истории оставлены как якоря, а не как самостоятельные сюжеты. В основном фрагменте Subramanian используется только для двух рабочих форм: feedback memory как repair rule и migration oracle как evidence surface. Его outcome claims не расширяются до независимого доказательства успешной миграции.

Matt Pocock skills удерживаются как якорь передачи состояния: PRD status, agent brief, handoff и triage. Их не нужно разворачивать в историю о всём репозитории skills; для A9 важен только переход от пользовательского или сигнала реализации к будущей агентской работе.

Google SRE, Pact, Argo, GSD, BMAD, Beads и Claude Code worktrees оставлены как механизмы замыкания цикла. Они не должны превращать A9 в обзор incident management, release engineering, task tracking или workspace cleanup.


## Content repair note

Проверка как готовящегося теоретического фрагмента подтвердила прежнее ограничение: истории не должны расширяться в самостоятельные кейсы. Особенно это касается Product Migration: основной текст может брать из него схему memory repair и migration oracle, но не должен доказывать outcome claims автора без внешних PR/CI/review/release artifacts.

Новых story anchors не добавлено. Mark Erikson, Armin Ronacher, Simon Willison, supply-chain хвост и отдельный production outage case остаются кандидатами для будущих pass, только если появится чёткая композиционная потребность.

## Composition / visual / style repair 2026-06-11

Story anchors unchanged. Repair did not add new stories and did not promote any side case into a new narrative. Product Migration remains a field-report anchor for evidence design and migration oracle surfaces; Matt Pocock skills remain an anchor for durable handoff/triage state; Armin/Simon/HumanLayer-related references remain secondary context, not a new A9 story expansion.

The main text now uses fewer figures and less service narration, so story anchors should continue to point to functions in the repair loop rather than to image placement decisions.
