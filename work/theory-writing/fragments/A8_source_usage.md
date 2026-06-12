# A8 source usage

## Источники, реально использованные в основном фрагменте

| Источник | Где использован | Какое утверждение поддерживает | Ограничение использования |
|---|---|---|---|
| GitHub Docs — About code owners: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | Абзац про CODEOWNERS | CODEOWNERS задаёт владельцев путей; owners automatically requested for review; branch protection может требовать code-owner approval; owners должны иметь write access; review берётся из CODEOWNERS на base branch; при обязательном owner review достаточно approval одного из указанных owners; CODEOWNERS рекомендуется защитить ownership-правилом. | Использован как governance-механика ownership и approval, не как полная модель архитектурной власти. |
| Michael Nygard — Documenting Architecture Decisions: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Абзац про ADR status | ADR содержит status; proposed/accepted/deprecated/superseded различают черновик и принятое архитектурное ограничение. | Использован только для статуса ADR; не пересказывается ADR-метод целиком. |
| AWS Prescriptive Guidance — ADR process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | Абзац про ADR review/adoption | Proposed ADR проходит review; team может оставить Proposed с action items, reject или approve; after approval owner adds timestamp/version/stakeholders and changes state to Accepted; accepted ADRs are used in code/architectural reviews, and code reviewers may ask authors to fix changes that violate ADRs. | Добавлен в source/depth pass как процессная опора для separation между draft/generated ADR и accepted architecture authority. |
| Stripe — Minions Part 1: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | Абзац про Stripe Minions | Агентный контур производит PR-кандидат: агент готовит ветку и проверки, а инженер открывает PR и запрашивает ревью; официальный текст связывает Minions с большим числом human-reviewed merged PR без человечески написанного кода. | Не использованы throughput numbers как доказательство исчезновения review; число упомянуто только чтобы показать, что даже в high-throughput режиме review остаётся отдельным контуром. |
| Stripe — Minions Part 2: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 | Абзац про Stripe Minions | Поддержка утверждения, что production-scale агентный контур всё равно выпускает PR для human review, а не получает самостоятельное право merge. | Использован как уточнение границы review/merge; подробные детали devbox/Toolshed не оставлены в основном тексте, потому что при этом проходе проверялась только центральная acceptance boundary. |
| Jökull Sólberg — Babysitting PRs: https://www.solberg.is/babysit-pr | Абзац про `/babysit-pr` | Цикл ожидания CI/Greptile, `codex review --base main`, triage Fix/Dismiss/Escalate, linter, commit/push, repeat до зелёного CI/no unresolved issues/max 3 iterations; Escalate = needs human judgment; разные review sources ловят разные типы проблем. | Использован как пример автоматизации PR-lifecycle; не утверждается, что агент получает право merge или что локальный Codex заменяет owner review. |
| Mike McQuaid — Sandboxed Agent Worktrees: https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/ | Абзацы про Sandvault/worktrees/review | Sandvault как альтернатива bypass/YOLO; macOS sandboxing + non-admin user; команды `sv claude`, `sv codex`, `sv shell`; git worktrees для параллельных branches; локальное review перед sharing, формы проверки и зависимость глубины от критичности/guardrails. | Использован как factual anchor для distinction между execution boundary и acceptance/publication boundary. |
| Sandvault repository: https://github.com/webcoyote/sandvault | Абзац про Sandvault | Дополнительная опора для факта о sandboxed local setup. | Не используется для broader governance claim. |
| Homebrew CONTRIBUTING: https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md | Абзац про Homebrew contribution policy | AI/LLM contribution требует disclosure в initial issue/PR с tool/model/etc.; author review всего generated content до запроса ревью; способность отвечать на review comments; один AI-assisted/generated PR одновременно для non-maintainers; close issue/PR if unable/unwilling. | Использован как policy boundary; не обобщён на все open-source проекты. |
| Zig Code of Conduct: https://ziglang.org/code-of-conduct/ | Абзац про Zig | Scope политики: ziglang organization на Codeberg, `#zig` IRC и Zig project development Zulip; strict no-LLM/no-AI policy запрещает LLM-generated code/prose, paraphrasing, editing, translation, brainstorming, bug finding и discussion of chatbot/LLM services в этих рабочих пространствах. | Использован как крайняя participation/governance boundary; scope не расширяется на всю внешнюю Zig community. |
| Loris Cro — Contributor Poker and AI: https://kristoff.it/blog/contributor-poker-and-ai/ | Абзац про Zig/contributor poker | Maintainer review может стоить дороже самостоятельной реализации; contributor poker — ставка на будущую ответственность участника; AI-generated contributions увеличивают review/reasoning cost через hallucinated drive-by PR, огромные first-time PR и surface-acceptable submissions, где follow-up reveals LLM regurgitation. | Использован как объяснение review-cost/participation boundary, не как единственный источник о Zig policy. |
| Linux kernel — Coding Assistance: https://docs.kernel.org/process/coding-assistants.html | Абзац про policy cluster | AI tools должны следовать стандартному kernel development process; AI agents не могут ставить `Signed-off-by`; человеческий submitter проверяет AI-generated code, добавляет собственный sign-off и берёт full responsibility. | Использован как policy boundary human responsibility / DCO, не как запрет AI-output в целом. |
| QEMU — Code Provenance: https://www.qemu.org/docs/master/devel/code-provenance.html | Абзац про policy cluster | QEMU требует сертификации provenance через DCO/Signed-off-by и в текущей политике decline contributions, которые believed to include or derive from AI generated content; исключения не снимают ответственности автора за весь patch. | Использован как жёсткая provenance/DCO boundary, а не как мягкая disclosure-policy. |
| LLVM — AI Tool Policy: https://llvm.org/docs/AIToolPolicy.html | Абзац про policy cluster | Contributors должны быть прозрачны и маркировать substantial tool-generated content; agents не должны действовать в digital spaces without human approval; unreviewed LLM output описан как extractive contribution, переносящий review cost на maintainers. | Использован как policy boundary transparency + human-in-the-loop + maintainer load. |
| tiangolo.com — Automated Code and AI: https://tiangolo.com/open-source/contributing/#automated-code-and-ai | Абзац про policy cluster | Инструменты, включая AI/LLM, допустимы, но contribution должен иметь meaningful human intervention, judgement, context; PR не стоит отправлять, если human effort автора меньше effort, нужного для review; repeated automated PR/comments могут привести к блокировке. | Заменяет старую FastAPI-ссылку, которая теперь ведёт на короткую страницу без нужного раздела; использован как maintainer-load anchor. |
| Beads CLI reference — bd gate: https://gastownhall.github.io/beads/cli-reference/gate | Абзац про Persistent Work Graph | Gate как async wait condition, который блокирует шаг workflow; типы human, timer, `gh:run`, `gh:pr`, bead; `gh:run`/`gh:pr` закрываются по успешному workflow run или merged PR. | Использован как практическая модель gate, не как единственная реализация PWG. |

## Что усилено во втором проходе

- CODEOWNERS получил детали про write access, base branch, достаточность одного owner approval и защиту самого CODEOWNERS.
- `/babysit-pr` получил конкретику по `codex review --base main`, max 3 iterations, Escalate как human judgment и распределению ролей CI/Greptile/Codex.
- Stripe-параграф теперь явно связывает high-throughput PR production с остающимся человеческим review-контуром.
- Mike/Sandvault усилен различием между bypass/YOLO режимами и sandboxed non-admin execution, а также локальным review перед sharing.
- Homebrew policy дополнена всеми constraint-пунктами, которые нужны для maintainer review boundary.
- Zig/Contributor Poker усилены как participation boundary: добавлены scope политики, запрет на LLM-generated reasoning channels и объяснение review-cost failure mode.

## Внутренние документы, использованные только для навигации

- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` — определил место A8 в части XII и связь с evidence/PWG.
- `work/theory-writing/CORE_NODES_WRITING_PLAN.md` — подтвердил целевой тезис: агент получает право действовать, но не право самостоятельно считать изменение принятым.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` — задал правило: досье являются quarry, не финальными источниками.
- `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` — помог выбрать `/babysit-pr` как factual anchor и не превратить его в story retelling.
- `content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md` — помог выбрать Sandvault/worktrees, локальный review и Homebrew policy.
- `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` и `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md` — помогли отделить PR-generation от review authority.
- `work/dossiers/ADR_METHOD_DOSSIER.md` — помог найти первоисточники про ADR status и CODEOWNERS.
- `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` — помог найти первоисточник про `bd gate` и сформулировать состояния PWG.
- `work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md` — помог выбрать Zig Code of Conduct и Contributor Poker.
- `work/expanded-quarry-theoretical-synthesis.md` — использован только как указатель на policy cluster и формулировку distinction между operational agency и acceptance/merge governance.

## Что сознательно не использовано как доказательство

- Внутренние досье и story reconstructions не поставлены как ссылки в основном фрагменте.
- Спорные или презентационные метрики Stripe не использованы как аргумент о том, что человеческое ревью исчезло.
- Отдельные PR-инциденты Zig не включены, чтобы не превратить фрагмент в пересказ кейса или этическую вставку; вместо этого использован общий source-backed механизм review cost из Contributor Poker.
- `Collaborator or Assistant?` и SASE-пейперы оставлены за рамкой второго прохода: их можно добавить позже, если фрагменту понадобится более академическое различение execution roles и merge governance, но текущий ход мысли держится на policy/code-review anchors.


## Authority laundering pass

Новых внешних источников на этом проходе не добавлено. Изменения сделаны как редакционная проверка уже source-backed утверждений:

- CODEOWNERS оставлен как owner-review gate, а не как полная архитектурная acceptance authority.
- CI и automated gates описаны как условия движения по процессу (`gate_satisfied` / `blocked`), а не как самостоятельное принятие результата.
- `/babysit-pr` и auto-merge трактуются как configured process boundary, где условия заданы владельцами репозитория, а не как право агента объявить merge-worthiness.
- Policy compliance описан как eligibility/participation boundary, а не как approval.
- Agent report должен возвращать evidence and next gate, не `done`.


## Source/depth pass

Добавлен один новый внешний источник: AWS Prescriptive Guidance ADR process. Он усиливает уже существующий ADR-абзац процессной фактурой: Proposed/Accepted transition, owner/team review, action items, rejected state, use of accepted ADRs during code review.

Открыт, но не добавлен в основной текст: Martin Fowler, `Architecture Decision Record` (https://martinfowler.com/bliki/ArchitectureDecisionRecord.html). Причина: материал полезен для общей ADR background, но в текущем A8 он дублировал уже используемые Nygard/AWS функции и раздувал бы фрагмент.

Новые источники для Stripe metrics, SASE, GitHub auto-merge и отдельных Zig PR-инцидентов не добавлялись: каждый из них расширял бы контекст, но не усиливал бы текущую центральную границу capability/acceptance.

## Source/provenance verification pass

- Проверены публичные первоисточники, которые поддерживают конкретные факты: GitHub CODEOWNERS, Nygard ADR, AWS ADR process, Stripe Minions, Jökull `/babysit-pr`, Mike/Sandvault, Homebrew CONTRIBUTING, Zig Code of Conduct, Contributor Poker, Linux kernel, QEMU, LLVM, tiangolo/FastAPI contributing и Beads `bd gate`.
- Исправлена битая/устаревшая ссылка FastAPI: `https://fastapi.tiangolo.com/contributing/#automated-code-and-ai` больше не содержит нужного раздела; фактическим первоисточником для этого прохода стал `https://tiangolo.com/open-source/contributing/#automated-code-and-ai`.
- QEMU перестал описываться как мягкая provenance-policy: в текущем тексте он показан как жёсткая DCO/provenance boundary, где contributions believed to include or derive from AI-generated content отклоняются.
- Stripe-параграф сжат до проверяемой центральной функции: PR-кандидат и human review. Подробности devbox/Toolshed/rules оставлены вне основного текста, чтобы не опираться на пересказы вместо проверенного первичного текста.
- Ссылка Beads `bd gate` выровнена на рабочий первичный URL без trailing slash: `https://gastownhall.github.io/beads/cli-reference/gate`.

## Residual composition/style pass

- Новые источники на остаточном проходе не добавлялись. Правки касались композиции, точности формулировок и синхронизации служебных карт с уже проверенными источниками.
- Основной фрагмент не расширялся: Stripe, Jökull, Mike/Sandvault, Zig и policy cluster сохранены как якоря для различения действия, gate и принятия, а не как самостоятельные истории.
- В figure/open/audit файлах вычищены остатки старой мягкой шкалы policies и лишние английские подписи там, где они не являются именами команд, статусов или документов.

## Composition / visual / style repair 2026-06-11

Новые внешние источники не добавлялись. Все ссылки в основном A8 сохранены из предыдущей версии. Правка затрагивала композицию, визуальный слой и язык: 11 inline-фигур сокращены до 5, а детальные схемы CODEOWNERS/ADR/Homebrew/Zig/`/babysit-pr` перенесены из основного текста в `A8_figure_candidates.md` как deferred или technical-atlas material. Локальный asset `content/assets/theory-images/mike-superset-worktrees.png` сохранён inline; подпись стала публичной, без служебного recovery-текста.
