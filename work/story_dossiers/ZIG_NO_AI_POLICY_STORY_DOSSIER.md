# Zig no-AI policy

## Черновое назначение

Документ создан режимом fresh для накопления материала из первоисточников. Это досье для будущей истории, а не методологическая заметка: здесь важны факты, спорные углы, ограничения, конкретные PR, социальный контракт проекта и то, как запрет на LLM-вклады работает как часть сопровождения языка Zig.

Тема может оказаться контр-историей для корпуса AI-assisted / agentic development. Здесь не нужно искать агентскую практику любой ценой. Более честный угол: крупный open-source проект явно ограничивает AI-вклады, потому что для него ценность вклада связана с ответственностью человека, последующим сопровождением, обучением участника и сохранением дефицитного времени ревью.

## Рабочая карта истории

### Возможные углы

1. Запрет как защита ревью-бюджета. В 2025 финансовом отчёте Zig Software Foundation видно, что спрос на внимание растёт быстрее способности команды закрывать issues и PR: среднее время закрытия issues за последний месяц перед отчётом было больше года, а среднее время закрытия pull requests за последний месяц выросло до двух месяцев [Zig 2025 Financial Report](https://ziglang.org/news/2025-financials/). На этом фоне LLM-вклады воспринимаются не как бесплатная помощь, а как дополнительный шум, который отнимает время у обычных contributors.

2. Запрет как часть социального контракта. Loris Cro объясняет это через `contributor poker`: проект инвестирует время ревью не только в конкретный первый PR, но и в человека, который может стать более сильным и надёжным участником позже [Loris Cro, Contributor Poker and Zig's AI Ban](https://kristoff.it/blog/contributor-poker-and-ai/). Если автор не понимает собственный патч и подменяет обсуждение ответами LLM, ставка на такого участника для Zig выглядит плохой.

3. Запрет как инженерная политика качества. В PR #24983 ревьюер `mlugg` закрыл вклад после поверхностной проверки: указал на compile errors, не подключённый и бессмысленный test file, возможные stack UAF, необъяснённую замену `@memmove` на `@memcpy`, а также на случайное пингование нескольких core contributors [ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983). Это не абстрактная позиция против AI, а конкретный пример работы, которую пришлось разбирать людям.

4. Запрет как конфликт с платформенной средой GitHub. В посте о миграции на Codeberg Andrew Kelley связывает нарушения no-LLM policy с тем, что GitHub продвигает Copilot прямо в рабочем интерфейсе issues, и одновременно описывает проблемы с GitHub Actions, vendor lock-in и снижением качества GitHub как инфраструктуры [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/). История запрета здесь переплетается с историей ухода с GitHub, но не сводится к ней.

5. Запрет как более жёсткая версия общей open-source реакции. Luanti в 2026 открыл обсуждение AI-assisted contributions и перечислил разные модели: Fedora и LLVM допускают с раскрытием, Krita и Widelands ближе к отказу, NetBSD сильно ограничивает, Linux kernel допускает при ответственности человека [Luanti issue #17088](https://github.com/luanti-org/luanti/issues/17088). Zig в этой карте интересен тем, что запрещает не только код, но и prose, paraphrasing, editing, translation, brainstorming, bug finding и разговоры об использовании LLM в рабочих пространствах проекта [Zig Code of Conduct](https://ziglang.org/code-of-conduct/).

6. Запрет как ранняя реакция на изменение интерфейса GitHub. GitHub 19 мая 2025 года вывел в публичный предварительный режим создание issues через Copilot: пользователь мог описать проблему естественным языком, загрузить скриншот, попросить Copilot заполнить форму issue и подготовить несколько черновиков issues сразу [GitHub Changelog, Creating issues with Copilot](https://github.blog/changelog/2025-05-19-creating-issues-with-copilot-on-github-com-is-in-public-preview/). Через четыре дня в `ziglang/zig` появился commit `d238078ae8`, который добавил в `.github/ISSUE_TEMPLATE/config.yml` contact link `Copilot and Other LLMs` с предупреждением не использовать GitHub Copilot или другие LLM для написания issue [zig commit d238078ae8, mirror](https://git.medv.io/zig/commit/d238078ae87f1beb565d42caee01ebd6a7a00d43.html). Это делает платформенный слой не фоном, а частью хронологии policy.

7. Запрет как правило core-проекта, которое не тождественно всей Zig-экосистеме. Ziggit FAQ запрещает AI-ответы на вопросы, непроверенный AI-generated code и просьбы чинить AI-generated code, но явно разрешает AI для механического перевода [Ziggit FAQ, AI Policy](https://ziggit.dev/faq). В апреле-мае 2026 модераторы Ziggit отдельно обсуждали, что форум не будет пространством нулевой терпимости для LLM / agents: демонстрационные проекты с AI допускаются при `llm` tag, а “slop / vibe-coded projects” должны отклоняться модераторами [Ziggit, AI/LLM Policy Updates](https://ziggit.dev/t/ai-llm-policy-updates/15497). Это важный контрфакт против простой формулы “Zig community bans AI everywhere”.

8. Запрет как правило, которое после миграции применяется уже на Codeberg. Ziggit thread от 27 мая 2026 года фиксирует жалобу пользователя `hrgdavor`: его комментарии в Codeberg issue `ziglang/zig#32119` были удалены, а сам он связывает блокировку с тем, что в комментарии признал использование LLM при разборе ошибки и предложении улучшить диагностическое сообщение [Ziggit, Blocked without warning or explanation](https://ziggit.dev/t/blocked-without-warning-or-explanation-for-comment-on-https-codeberg-org-ziglang-zig-issues-32119/15741). Это слабее, чем первичный Codeberg moderation log, потому что удалённые комментарии читаются через пересказ участника, но эпизод показывает практическое трение вокруг запрета на LLM brainstorming и обсуждение LLM usage.

9. Запрет как часть управления каноническим пространством, а не всей децентрализованной community. Официальный сайт Zig говорит, что community decentralized, нет универсального статуса “official / unofficial”, а у каждого gathering place свои moderators and rules; main development сейчас находится на Codeberg, и contributors там expected to follow Zig’s Code of Conduct [Zig home page](https://ziglang.org/). Сам Code of Conduct ограничивает своё действие `ziglang` organization on Codeberg, `#zig` IRC и Zig project development Zulip chat, а не всеми местами, где обсуждают Zig [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это помогает не превращать историю в утверждение “весь Zig запрещает всё AI”.

10. Запрет как спор не только о качестве PR, но и о распознавании LLM-паттернов. В обсуждении на Lobsters Andrew Kelley отвечает на возражение “вы не можете знать, кто использует LLM”: он признаёт, что 100% случаев поймать нельзя, но утверждает, что человеческие ошибки и LLM hallucinations имеют разные заметные паттерны, а позже уточняет, что после многих часов ревью видит признаки даже без явных ошибок; при этом он говорит, что хотел бы invitation-tree модель доверия и что текущая роль enforcement стала токсичной [Lobsters, Contributor Poker and Zig's AI Ban](https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban). Это добавляет к истории неформальную сторону policy: запрет держится не на forensic proof по каждому PR, а на накопленном ревьюерском опыте и желании снизить необходимость быть “полицией”.

11. Запрет как downstream boundary, а не только входной фильтр PR. Bun в апреле 2026 показал AI-assisted изменения в своём Zig fork, которые ускорили compilation, но публично не планировал upstream из-за строгого запрета Zig на LLM-authored contributions [Simon Willison, 30th April 2026 archive](https://simonwillison.net/2026/Apr/30/). В Ziggit обсуждении `mlugg` отдельно объяснил, что параллельный semantic analysis давно желателен, но требует языковых изменений для детерминизма; иначе история легко превращается в слишком простой конфликт “AI сделал ускорение, Zig отказался” [Ziggit, Bun’s Zig fork got 4x faster compilation times](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183).

### Что мешает слишком простой рамке

- Запрет не выглядит только юридической реакцией на provenance. В текущем Code of Conduct нет развёрнутой юридической аргументации; акцент больше на рабочих пространствах, техническом фокусе, нежелательном контенте и поведении [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Для сравнения, NetBSD часто описывается через риск “tainted code”, но это пока фоновый источник, а не раскрытая ветка для Zig.

- Запрет не означает, что Zig отказывается от open-source contributions. В старой странице `Contributing`, отредактированной Andrew Kelley 11 июля 2025 года, рядом с no-LLM policy находится подробная инструкция, как начинать проекты на Zig, искать contributor-friendly issues, собирать Zig из исходников и запускать релевантные тесты [Zig wiki, Contributing, revision 61aff1c](https://github.com/ziglang/zig/wiki/Contributing/61aff1ce9b3ebd8c38c0f5a18db00c06f0fa4022). Политика не закрывает вход; она задаёт цену входа в виде собственного понимания и тестирования.

- Запрет не обязательно исчерпывается качеством отдельного PR. Loris Cro пишет, что в раннем Zig можно было инвестировать почти в каждого нового contributor, а теперь входящих PR больше, чем энергии у core contributors [Loris Cro, Contributor Poker and Zig's AI Ban](https://kristoff.it/blog/contributor-poker-and-ai/). Поэтому даже “выглядящий нормально” LLM-assisted вклад несёт риск: follow-up обсуждение может быстро показать, что автор не держит модель изменений в голове.

- Миграция с GitHub даёт яркий сюжет, но может затмить саму policy. В посте о миграции основные причины связаны с Actions, CI backlog, невозможностью вмешаться в scheduling и донорской зависимостью от GitHub Sponsors; no-LLM violations появляются как бонусный ожидаемый эффект ухода [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/). В будущей истории важно не перепутать причину миграции с причиной запрета.

- Внешняя пресса быстро превращает policy в заголовок “Zig bans AI code”. JetBrains blog от 5 июня 2026 года ведёт к полному интервью с Andrew Kelley и прямо говорит, что там обсуждается отношение проекта к AI-generated contributions [JetBrains Blog, Why Zig Isn’t 1.0 (Yet)](https://blog.jetbrains.com/blog/2026/06/05/why-zig-isn-t-1-0-yet/). Business Insider / Yahoo пересказывает это как историю про “invariably garbage”, “negative value”, около 200 open pull requests и простоту blanket ban [Yahoo / Business Insider, Zig president says AI coding contributions are 'invariably garbage'](https://tech.yahoo.com/ai/claude/articles/zig-president-says-ai-coding-171749742.html). Это полезный слой реакции, но не замена первичному видео или transcript.

## Контекст проекта

Zig развивает язык и toolchain с большой долей собственного кода и инфраструктуры. В 2024 расходы ZSF составили $520,748.91, из них значительная часть пошла на contractors и единственного employee, Andrew Kelley; total income за 2024 указан как $670,672.59 [Zig 2025 Financial Report](https://ziglang.org/news/2025-financials/). Этот финансовый масштаб важен: политика вклада появляется не в корпорации с большим штатом triage, а в проекте, где внимание core team и оплаченных contributors является главным ограничением.

В том же отчёте описан рост пользовательской активности: всё больше людей добавляет Zig в свои stacks, открывает issues, отправляет PR, задаёт вопросы и ship-ит software, зависящее от Zig [Zig 2025 Financial Report](https://ziglang.org/news/2025-financials/). Таблица времени закрытия показывает ухудшение: issues в среднем закрывались за 7 месяцев all time, за 11 месяцев за past year и больше чем за год за past month; pull requests закрывались за 16 дней all time, 30 дней за past year и 2 месяца за past month [Zig 2025 Financial Report](https://ziglang.org/news/2025-financials/). Это даёт материальный фон для фразы “LLM PR как нагрузка”, а не просто культурная неприязнь.


### Дополнительный эпизод: policy применима не только к коду, но и к reasoning в обсуждении

Ziggit thread вокруг “Contributor Poker” даёт важное уточнение к официальному запрету. Loris Cro формулирует проблему через ограниченный review budget: если у проекта не хватает ресурсов смотреть каждый PR, нет смысла тратить дополнительные усилия на восстановление reasoning за LLM-generated PR, когда ждёт очередь non-LLM contributions [Ziggit](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232). В обсуждении появляется жёсткая practical rule: если проект подозревает, что contributor использует LLM for generating code or arguing about the problem, PR can be closed and contributor banned; при этом зрелый инженер, который использовал LLM exploratory и не приносит output как authority, описан как более сложный случай [Ziggit](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232).

Simon Willison’s note добавляет внешний contrast: Bun, написанный на Zig and acquired by Anthropic in December 2025, uses AI assistance heavily; Bun fork reportedly got a 4x compile-time improvement, but Bun did not plan to upstream it because Zig has a strict LLM-authored contributions ban, while later Zig contributor details show there were independent architecture/determinism concerns around parallel semantic analysis and codegen units [Simon Willison](https://simonwillison.net/2026/Apr/30/zig-anti-ai/). Поэтому будущая история не должна сводиться к лозунгу “Zig отказывается от полезных AI patches”. Точная сцена сложнее: downstream может двигаться быстрее в fork, а upstream оценивает не только происхождение, но и maintainability, determinism and review cost.

## Ход событий и эволюция правила

Раздел переписан как последовательность policy episodes. Здесь важно не просто “Zig bans AI”, а какие именно рабочие сцены сделали такой запрет рациональным для проекта: generated issues, PR review cost, contributor poker, hidden LLM reasoning, Code of Conduct and migration context.

### Эпизод 1. GitHub Copilot issue-creation and first rule surface: generated reasoning enters the tracker

В 2025 GitHub публично вводит Copilot issue-creation flows. Zig создаёт wiki page “Writing Issues with Copilot and Other LLMs”; позднее содержание переносится в Code of Conduct. The archived wiki page now mainly says the content moved to `ziglang.org/code-of-conduct`, with Andrew Kelley editing it on Nov 23, 2025. This small provenance detail matters: the rule moved from an ad hoc wiki instruction to the project’s broader social contract ([GitHub Copilot issue creation changelog](https://github.blog/changelog/2025-05-19-creating-issues-with-copilot-on-github-com-is-in-public-preview/), [Zig wiki page](https://github.com/ziglang/zig/wiki/Writing-Issues-with-Copilot-and-Other-LLMs), [Zig Code of Conduct](https://ziglang.org/code-of-conduct/)).

The problem was not only AI-generated patches. Issues and comments can also contain generated reasoning. If a user asks an LLM to produce a bug report or argument, the reviewer must now verify not just reproduction steps or code, but whether the author understands the claim, can answer follow-up questions and can own the consequences. That is why later Zig discussion clarifies that the policy can apply to reasoning in tracker discussion, not just final code diffs ([Ziggit: contributor poker and AI ban](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232), [Ziggit: Ziggit and LLMs](https://ziggit.dev/t/ziggit-and-large-language-models/15068)).

### Эпизод 2. July–November 2025: rule moves from contribution guidance into Code of Conduct and governance context

By July 2025 the no-LLM rule appears in contribution guidance; by November it is in Code of Conduct. Around the same period Zig’s migration from GitHub to Codeberg gives the policy a wider governance frame. The important change is not just location of the text. When the rule enters Code of Conduct, it becomes part of acceptable participation, not a maintainer preference hidden in a wiki. The project is saying: if you participate in Zig’s technical spaces, do not outsource your contribution or reasoning to LLMs in a way that shifts verification burden onto maintainers ([Zig Code of Conduct](https://ziglang.org/code-of-conduct/), [Zig migration news](https://ziglang.org/news/migrating-from-github-to-codeberg/)).

The rule should still be stated narrowly. It does not prove that no AI-assisted work can ever be useful elsewhere. It says Zig’s maintainers do not want to spend scarce reviewer time on contributions whose author may not personally understand and own the reasoning. This distinction matters because the policy is about review economics and contributor development as much as code quality.

### Эпизод 3. PR #24983: small working scene of policy and technical judgement

PR `#24983`, “Add ALPN (Application Layer Protocol Negotiation) support to TLS Client”, is the clearest small scene. A contributor opens a TLS-client feature PR. A core/member comment says Zig has a strict no LLM/AI policy, and that after giving the PR benefit of the doubt, a quick look suggested both the comment and code looked like LLM-generated material. The PR is closed ([ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983)).

This case is useful precisely because it is not just “AI detected → close”. Simon Willison later reports nuance from a core contributor: the rejected patch had issues independent of the LLM policy, including language-level implications around parallel semantic analysis. So the scene shows policy and ordinary technical judgement intersecting. The reviewer is not merely checking syntax. They have to decide whether the contributor understands TLS ALPN, Zig internals, semantic analysis implications and future maintenance. If generated reasoning obscures that, the PR consumes reviewer time without building a trusted contributor relationship ([Simon Willison](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)).

### Эпизод 4. Contributor poker: review is investment in a person, not cleanup after output

Loris Cro’s “Contributor Poker and Zig’s AI Ban” gives the clearest rationale. In successful open-source projects, maintainers eventually receive more PRs than they can process. A narrow ROI calculation would say “accept only nearly perfect PRs.” Zig instead tries to help contributors improve because contribution is an iterated game: maintainers invest effort in a person, and later that person may become trusted, prolific and responsible for the code they changed. Cro calls this “contributor poker”: you play the person, not just the cards; you bet on the contributor, not just the first PR ([Contributor Poker](https://kristoff.it/blog/contributor-poker-and-ai/)).

AI-generated submissions break that calculus. A contributor who submits generated code may not know the codebase or problem space, may not be trusted to have thought through the changes, and may not be able to support the code after merge. Cro lists concrete failure modes: worthless drive-by PRs full of hallucinations that do not compile or pass CI; extremely large first-time PRs around 10k lines; PRs that look acceptable on the surface but where follow-up discussion reveals the author is secretly consulting an LLM and repeating its wrong answers. The cost is not only merge risk; it consumes the scarce reviewer budget that could have been spent onboarding a real future contributor ([Contributor Poker](https://kristoff.it/blog/contributor-poker-and-ai/)).

### Эпизод 5. Hidden LLM use in reasoning: the policy reaches comments, not only diffs

Ziggit discussions after the policy make clear that detection is not the central point. Some people object that maintainers cannot reliably know whether a contributor used an LLM. Cro’s answer is that this misses the contributor poker frame. The project is not running a detector as a formal proof system. It is making a rational triage decision: if a contribution shows signs that the author is not personally reasoning through the problem, it is a bad bet compared with other contributors who bring their own understanding and can participate in follow-up discussion ([Ziggit discussion](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232), [Contributor Poker](https://kristoff.it/blog/contributor-poker-and-ai/)).

This is why reasoning in comments matters. A generated-looking explanation can be as costly as generated code, because it forces maintainers to debug the conversation itself. The reviewer has to separate actual understanding from plausible text. In a language implementation project, that is especially expensive: the right answer often depends on long-term invariants, compiler architecture, subtle language semantics and maintenance responsibility after merge.

### Эпизод 6. Additional exhibits: hallucinated PRs, 10k-line first PRs, migration comments and downstream contrast

The dossier contains several external exhibits. Simon Willison’s post records the policy and public reaction. HN, Lobsters and Business Insider add reaction layers, but should be treated as weaker evidence. Ziggit threads discuss AI/LLM policy updates, Codeberg comments and contributor experiences. A useful contrast is downstream/upstream: a downstream project can experiment with AI-assisted code in a fork, but upstream Zig has to own the language and toolchain. That means the same patch can have different acceptability depending on where responsibility lives ([Simon Willison](https://simonwillison.net/2026/Apr/30/zig-anti-ai/), [Ziggit policy updates](https://ziggit.dev/t/ai-llm-policy-updates/15497), [Bun/Zig fork discussion](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183)).

Another important exhibit is the migration away from GitHub. The no-AI policy is not the only reason for migration, but the move to Codeberg changes the governance surface: issue tracker, comments, PR flow and social contract are no longer only GitHub defaults. The story should not overstate this as “Zig left GitHub because of AI”, but the timing and governance context matter: Zig is actively redesigning how contributions reach maintainers ([Zig migration news](https://ziglang.org/news/migrating-from-github-to-codeberg/)).

### Эпизод 7. After policy: what the rule preserves and what it risks

The policy preserves reviewer time, contributor formation and after-merge responsibility. It also risks false positives, discouraging legitimate tool-assisted contributors, and producing social friction around accusations. This is why the story should be written as a counter-story, not as a universal commandment. Zig is a project with language/toolchain stakes, limited maintainer time and a strong contributor-development model. In that context, AI-generated drive-by work is not a productivity gift. It is an input-quality and reviewer-economics problem.

### Эпизод 8. Code of Conduct wording matters because it moves the rule from taste to participation contract

The Code of Conduct placement gives the policy a specific social force. The dossier should not leave this at “Zig banned AI”. The rule becomes part of how Zig defines acceptable participation in project spaces: the issue is not merely whether a diff compiles, but whether the participant is doing the reasoning they present to maintainers. That is why LLM-written issue text, LLM-written comments and LLM-written PR explanations are in scope. A generated answer in a tracker discussion can consume the same scarce reviewer capacity as generated code, because maintainers now have to debug whether the author understands the issue at all ([Zig Code of Conduct](https://ziglang.org/code-of-conduct/), [Ziggit discussion](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232)).

This also clarifies the Codeberg migration context. The migration should not be turned into a causal claim that “Zig left GitHub because of AI”. But it belongs in the same governance story: Zig is deliberately shaping contribution surfaces, issue tracking and social norms rather than accepting GitHub’s default AI-augmented inflow. In that environment, a no-LLM rule is not a technical linter; it is part of boundary-setting for a contributor community that depends on long-term trust and after-merge responsibility ([Zig migration news](https://ziglang.org/news/migrating-from-github-to-codeberg/)).

## Практика в действии

Zig policy требует от участника не только авторства текста или кода, но и способности вести follow-up. У Cro это выражено через ожидание, что contributor understands the codebase and problem space, thought through changes, and remains responsible after merge; если после merge обнаруживаются проблемы, ценность имеет обсуждение с человеком, который получил insight в problem space [Loris Cro, Contributor Poker and Zig's AI Ban](https://kristoff.it/blog/contributor-poker-and-ai/). В русском пересказе это можно сформулировать так: Zig покупает ревью не ради одного diff, а ради будущего человека в проекте.

PR #24983 показывает отрицательный кейс. Вклад выглядел как быстро собранный feature request под реальную потребность HTTP/2 / gRPC, но ревьюер нашёл признаки, что автор не прошёл даже базовую проверку. Особенно важна связка “test file exists” и “test file bogus”: наличие теста как артефакта само по себе ничего не значит, если тест не подключён, не компилируется или проверяет бессмысленное поведение [ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983). Для истории это лучше, чем общий тезис “AI PRs плохие”: есть конкретный набор дефектов.

Старые инструкции `Contributing` дают положительный контрпример ожидаемой практики: contributor собирает Zig из source, выбирает подходящую команду проверки, понимает ограничения тестов на non-native targets, знает, где применимы QEMU, Wine или wasmtime, и при работе с `translate-c` добавляет test case в нужный каталог [Zig wiki, Contributing, revision 61aff1c](https://github.com/ziglang/zig/wiki/Contributing/61aff1ce9b3ebd8c38c0f5a18db00c06f0fa4022). Именно такая плотная локальная ответственность плохо заменяется сгенерированным “похожим на PR” текстом.

PR #25974 даёт другой тип enforcement: исходно он выглядит как обычный маленький bugfix в DWARF handling, затем reviewer просит объяснить связь с integer underflow, третий участник указывает на AI-generated происхождение и недостаток reasoning, после чего Andrew Kelley закрывает PR ссылкой на policy [ziglang/zig PR #25974](https://github.com/ziglang/zig/pull/25974). Это отличает Zig от policy-моделей, где AI-assisted contribution может быть допустимым при раскрытии инструмента и принятии ответственности человеком [ziglang/zig PR #25974](https://github.com/ziglang/zig/pull/25974); [Luanti issue #17088](https://github.com/luanti-org/luanti/issues/17088). Для истории здесь важно не оценивать, был ли конкретный diff хорошим: проект не хочет тратить ревью на восстановление reasoning за патчем, если происхождение уже связано с LLM.

PR `www.ziglang.org#502` расширяет поле policy за пределы compiler code. Вклад касался package management documentation, но reviewer нашёл устаревшие версии, obsolete manifest/API details и generic best practices; затем автор признал Claude / Gemini review и нехватку собственного знания technical specifics, после чего Andrew Kelley закрыл PR ссылкой на policy [ziglang/www.ziglang.org PR #502](https://github.com/ziglang/www.ziglang.org/pull/502). Это полезная деталь для будущей живой сцены: “AI policy” проявляется не только в кодовых PR, а в рутинной охране документации от уверенно изложенной, но устаревшей фактуры.

Bun fork показывает положительный на вид, но всё равно не upstream-сценарий. В отличие от rejected PR, там нет публичного Zig review, где maintainer обязан разбирать чужой AI-assisted diff. Ценность эпизода в другом: downstream-проект может получить локальное ускорение и оставить его у себя, но для Zig upstream остаются вопросы детерминизма semantic analysis, долговременного сопровождения и происхождения вклада [Simon Willison, 30th April 2026 archive](https://simonwillison.net/2026/Apr/30/); [Ziggit, Bun’s Zig fork got 4x faster compilation times](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183). Это помогает не сводить policy к “плохие AI PR”: даже потенциально полезный downstream result не автоматически становится хорошим upstream contribution.

Текущий официальный сайт Zig добавляет инфраструктурную рамку после миграции: ссылка `Source` ведёт на Codeberg, main development описан как Codeberg repository plus issue tracker and proposals, а GitHub repository page уже показывает `Moved to Codeberg` и предупреждение `This repository is not mirrored` [Zig home page](https://ziglang.org/); [GitHub ziglang/zig repository](https://github.com/ziglang/zig). Это важно для будущего эпизода после ноября 2025: enforcement больше нельзя описывать только как GitHub moderation, потому что каноническое рабочее пространство переехало.

В июне 2026 появился ещё один слой публичного объяснения через JetBrains. Blog post `Why Zig Isn’t 1.0 (Yet)` не даёт transcript no-AI фрагмента, но подтверждает контекст: это разговор JetBrains с Andrew Kelley, полное видео опубликовано по `jb.gg/andrew-kelley-zig-interview`, и в нём среди тем названо отношение проекта к AI-generated contributions [JetBrains Blog, Why Zig Isn’t 1.0 (Yet)](https://blog.jetbrains.com/blog/2026/06/05/why-zig-isn-t-1-0-yet/). Пересказ Business Insider / Yahoo даёт более конкретные тезисы интервью: Kelley связывает AI PR с отрицательной ценностью из-за времени ревью, называет нехватку core review узким местом и упоминает около 200 open pull requests на момент записи; там же blanket ban объясняется как правило, которое не заставляет reviewers оценивать “хороший” и “плохой” AI PR по одному [Yahoo / Business Insider, Zig president says AI coding contributions are 'invariably garbage'](https://tech.yahoo.com/ai/claude/articles/zig-president-says-ai-coding-171749742.html). Это стоит держать как вторичный источник до тех пор, пока не будет раскрыт полный transcript или первичный фрагмент видео; прямое открытие Yahoo в проходе 05 отдало 429, фактура проверялась по раскрытому поисковому результату и должна быть перепроверена по Business Insider / YouTube перед финальным текстом.

## Артефакты и детали, которые нельзя потерять

- Текущий Code of Conduct применим не ко всем Zig-сообществам, а только к указанным пространствам: `ziglang` organization on Codeberg, `#zig` IRC на Libera.chat и Zig project development Zulip chat [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это важная граница: проект допускает децентрализованные community spaces с другими правилами.

- В `.github/ISSUE_TEMPLATE/config.yml` commit `d238078ae8` одновременно отключает blank issues и добавляет contact link `Copilot and Other LLMs`; это техническое обходное решение против конкретного GitHub UI, а не только текстовая просьба в документации [zig commit d238078ae8, mirror](https://git.medv.io/zig/commit/d238078ae87f1beb565d42caee01ebd6a7a00d43.html).

- В Code of Conduct рядом с no-LLM policy находится запрет на “drive-by” language proposals: желающий изменить язык должен убедить core team member подать и champion-ить proposal [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это не AI-specific правило, но оно поддерживает тот же social contract: проект не хочет принимать поверхностные предложения без человека, который берёт на себя сопровождение.

- Enforcement в Code of Conduct поручен Andrew Kelley и Loris Cro, оба оплачиваются Zig Software Foundation; moderation входит в их работу [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это показывает, что policy не просто декларация на wiki.

- В миграции на Codeberg новая canonical ветка задана как `https://codeberg.org/ziglang/zig.git`, GitHub repo сделан read-only, старые issues не переносятся массово, Codeberg numbering стартует с 30000 [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/). Эти детали помогут показать, что отказ от GitHub был практической инфраструктурной операцией.

- В финансовом отчёте GitHub Sponsors дал $170,656.04 из total income $670,672.59 за 2024; Zig просит donors переходить на Every.org, а GitHub Sponsors описывает как liability несмотря на его историческую важность [Zig 2025 Financial Report](https://ziglang.org/news/2025-financials/); [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/). Это создаёт трение: уйти с GitHub легче идеологически, чем финансово.

- В PR #24983 после закрытия есть cross-reference на Luanti discussion `luanti-org/luanti#17088` [ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983). Это маленькая, но полезная деталь: Zig policy используется другими open-source проектами как reference point в собственных дебатах.

- В Ziggit policy есть отдельная граница для AI-использования в проектах: демонстрационный AI project допускается с явным `llm` tag, но AI-generated posts и просьбы чинить AI-generated code запрещаются [Ziggit FAQ, AI Policy](https://ziggit.dev/faq); [Ziggit, AI/LLM Policy Updates](https://ziggit.dev/t/ai-llm-policy-updates/15497). Это нельзя смешивать с официальным Code of Conduct Zig core spaces.

- Ziggit discussion вокруг post-migration Codeberg case `#32119` показывает пользовательскую цену strict policy: участник `hrgdavor` воспринимает удаление комментариев и блокировку как неожиданное наказание за учебное использование LLM, а другие участники отвечают ссылкой на буквальные запреты CoC [Ziggit, Blocked without warning or explanation](https://ziggit.dev/t/blocked-without-warning-or-explanation-for-comment-on-https-codeberg-org-ziglang-zig-issues-32119/15741); [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это не отменяет policy, но даёт сцену трения после миграции.

## Ограничения и неудобные детали

- Старый открытый вопрос о `issues/25642` и `issues/25579` оказался ложным следом первого прохода: реальные exhibit links из миграционного поста — `ziglang/zig#25974`, `ziglang/zig#24983` и `ziglang/www.ziglang.org#502` [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/). В досье нужно оставить эту коррекцию, чтобы будущие проходы не строили поиск вокруг неверных номеров.

- Проход 02 неверно описал два exhibit cases: PR #25974 был `Fix integer underflow in Unit.resizeHeader()` от `joelreymont`, а не `promoteVectorIndex` от `Overclocked-llama`; PR `www.ziglang.org#502` был package management guide, а не `.well-known/ai.txt` / AI scraper guidance [ziglang/zig PR #25974](https://github.com/ziglang/zig/pull/25974); [ziglang/www.ziglang.org PR #502](https://github.com/ziglang/www.ziglang.org/pull/502). Эти исправления нужно сохранить как anti-degradation marker, чтобы будущие проходы не вернули старую ошибку.

- JetBrains video `Zig 2026: No-AI Policy, $670K Foundation, Left GitHub & Why Zig Isn’t 1.0 - Andrew Kelley Explains` найден через Podwise / Crow Watch; Crow Watch показывает YouTube id `iqddnwKF8HQ`, но полный первичный просмотр или transcript в этом проходе не раскрыты. Его можно держать как кандидат на источник, но не использовать для точных утверждений об Andrew Kelley сверх того, что уже подтверждают официальные Zig posts и документы.

- Слово “AI” в этой истории неоднородно. В источниках Zig policy фактически направлена на LLM / chatbot content и contributions. Не нужно расширять её до любого automated tooling, static analysis, compiler diagnostics или обычных локальных инструментов без подтверждения.

- Политика запрещает даже translation через LLM, но одновременно говорит, что English encouraged but not required и что другие участники могут использовать свои translation tools, чтобы интерпретировать чужие слова [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Это тонкое место: автору сообщения нельзя использовать LLM для подготовки текста, но читатель может пользоваться своими инструментами интерпретации. В будущей истории нужно объяснить это аккуратно, без карикатуры.

- Code of Conduct сам ограничивает область действия: `ziglang` organization on Codeberg, `#zig` IRC и Zig project development Zulip chat [Zig Code of Conduct](https://ziglang.org/code-of-conduct/). Если будущий текст будет говорить “Zig bans AI”, нужно рядом пояснить, что речь о contribution/development spaces проекта, а не о запрете пользователям Zig писать AI-приложения или обсуждать LLM в других сообществах.

- Внешние реакции часто превращают позицию Zig в культурный лозунг “anti-AI”. У Cro формулировка осторожнее: theoretical valid contributor with LLMs possible, but irrational to bet on LLM users given observed risk and pool of non-LLM contributors [Loris Cro, Contributor Poker and Zig's AI Ban](https://kristoff.it/blog/contributor-poker-and-ai/). Эта оговорка важна, потому что история иначе станет слишком гладкой.

- В обсуждении Cro появляется отдельный reputational аргумент: даже rigorously accepted LLM-assisted contributions могут оставить у пользователей ощущение, что Zig стал `slop` / `vibecoded project`, а такой branding hit трудно откатить [Ziggit, Contributor Poker and Zig's AI Ban, page 2](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232?page=2). Это не главный официальный мотив, но сильная неудобная деталь о том, почему “просто разрешить trusted contributors” не выглядит для проекта дешёвым компромиссом.

- GitHub commit `d238078ae8` прочитан через зеркало `git.medv.io`, потому что обычная GitHub commit page не раскрылась в текущем web fetch. Это, вероятно, точное отображение Git object с hash, author, diff и commit message, но для позднего финального текста лучше дополнительно проверить официальный GitHub URL или локальный clone истории.

- Не каждый конфликт вокруг AI-сгенерированных изменений равен вопросу “можно ли upstream-ить AI code”. В обсуждении Bun’s Zig fork на Ziggit `mlugg` прямо сдвигает разговор с происхождения патча на технические причины: параллельный semantic analysis давно планировался, но безопасная реализация требует языковых изменений, иначе возможна недетерминированность компиляции; отдельное разбиение LLVM output на несколько модулей он считает не главным направлением работы Zig [Ziggit, Bun’s Zig fork got 4x faster compilation times](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183). Это мешает удобной истории “AI предложил ускорение, Zig отверг из-за policy”: у core-разработчика были самостоятельные инженерные возражения.

- Lobsters discussion добавляет слабое место policy, которое нельзя сгладить: у проекта нет публичного измерения ложных срабатываний и пропусков при распознавании LLM-вкладов. Kelley и Cro отвечают через ревьюерский опыт, предупреждение заранее и желание trust model вроде invitation tree, но это не формальная процедура доказательства [Lobsters, Contributor Poker and Zig's AI Ban](https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban). Для будущей истории это хорошая граница: strict policy может быть рациональна для Zig и всё равно оставаться грубым инструментом.

## Детали, восстановленные после сверки с последней загруженной версией

- The first operational policy layer should keep the GitHub issue-template detail: commit `d238078ae8` / `Block GitHub Copilot Issue Morpher` changed `.github/ISSUE_TEMPLATE/config.yml`, setting `blank_issues_enabled` from `true` to `false` and adding `contact_links` to `Writing Issues with Copilot and Other LLMs`, which later moved into Code of Conduct language ([Zig repository](https://github.com/ziglang/zig); [Code of Conduct](https://ziglang.org/code-of-conduct)).
- PR `#24983` should remain a technical scene, not only policy evidence: it proposed ALPN support in TLS Client through `alpn_protocols` in `Client.Options`, `negotiated_alpn` in `Client`, encoding in `ClientHello`, parsing in `ServerHello`, tests and HTTP/2 / gRPC motivation; review references included concrete locations such as `Client.zig:295` ([ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983)).
- The baseline also preserved adjacent exhibits that should not disappear: issues/PRs `#25579`, `#25642`, `www.ziglang.org#502`, comments by `jimkring`, `linusg`, `mrjbq7`, `lalinsky`, `wbrian`, `videbar`, `frank`, `Ryan Liptak`, and migration/version examples like `0.11.0` → `0.14.1`, `Client`, `ClientHello`, `ServerHello`, `.rc`, `anyerror!u64`, `available_len = 0` ([Zig GitHub](https://github.com/ziglang/zig); [ziglang/www.ziglang.org](https://github.com/ziglang/www.ziglang.org)).
- The technical test/build commands are important because they show the kind of burden a serious contribution enters: `stage3/bin/zig build -p stage4 -Denable-llvm -Dno-lib`, `stage4/bin/zig build test -Denable-llvm`, `zig build test-std -Dskip-release -Dskip-non-native`, `zig test lib/std/std.zig --zig-lib-dir lib`, `--test-filter`, and related commands should remain connected to policy and review-budget discussion rather than being lost as low-level detail ([Zig contribution docs](https://github.com/ziglang/zig/blob/master/CONTRIBUTING.md)).
- The reputational layer from Ziggit should remain: Cro’s concern was not only broken code, but a future where even accepted LLM-assisted contributions may brand the project as `slop` or `vibecoded`, while responsible AI users can choose not to use AI for this project. This preserves the difference between “no AI anywhere” and “this project refuses AI-sourced participation cost” ([Ziggit discussion](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232)).

## Источники

### Первичные / официальные

- [Zig Code of Conduct](https://ziglang.org/code-of-conduct/) — текущий официальный текст strict no LLM / no AI policy. Подтверждает scope, конкретные запреты, связь с рабочими пространствами проекта, enforcement и соседние правила про proposals.

- [Zig home page](https://ziglang.org/) — текущая главная страница Zig. Подтверждает децентрализованность community, отсутствие универсального “official / unofficial” для всех gathering places, текущий main development на Codeberg и ожидание follow Zig Code of Conduct для contributors.

- [Migrating from GitHub to Codeberg](https://ziglang.org/news/migrating-from-github-to-codeberg/) — официальный пост Andrew Kelley от 26 ноября 2025 года. Подтверждает миграцию на Codeberg, read-only GitHub, новую canonical origin, numbering strategy для issues, GitHub Actions / CI complaints, GitHub Sponsors risk и связь Copilot UI с нарушениями no-LLM policy.

- [Zig 2025 Financial Report and Fundraiser](https://ziglang.org/news/2025-financials/) — официальный финансовый отчёт от 2 сентября 2025 года. Нужен для масштаба проекта, бюджета, расходов, incoming demand, времени закрытия issues / PR и зависимости от GitHub Sponsors.

- [Zig wiki, Contributing, revision 61aff1c](https://github.com/ziglang/zig/wiki/Contributing/61aff1ce9b3ebd8c38c0f5a18db00c06f0fa4022) — historical GitHub wiki revision, edited Andrew Kelley 11 июля 2025. Подтверждает раннюю форму no-LLM policy и технический стандарт вкладов через build / test commands.

- [Writing Issues with Copilot and Other LLMs](https://github.com/ziglang/zig/wiki/Writing-Issues-with-Copilot-and-Other-LLMs) — GitHub wiki page, edited Andrew Kelley 23 ноября 2025. Сейчас сообщает, что content moved to Code of Conduct; важна как след миграции policy из wiki в официальный CoC.

- [zig commit d238078ae8, `Block GitHub Copilot Issue Morpher`](https://git.medv.io/zig/commit/d238078ae87f1beb565d42caee01ebd6a7a00d43.html) — зеркало Git commit от 23 мая 2025 года. Подтверждает изменение `.github/ISSUE_TEMPLATE/config.yml`: отключение blank issues и contact link на `Writing Issues with Copilot and Other LLMs`. Статус: первичный git object, но прочитан через зеркало; официальный GitHub commit URL стоит перепроверить в позднем проходе.

- [ziglang/zig PR #25974](https://github.com/ziglang/zig/pull/25974) — `Exhibit A` из поста о миграции. PR `Fix integer underflow in Unit.resizeHeader()` от `joelreymont`; в обсуждении внешний participant указывает на AI-generated происхождение и недостаток reasoning, затем Andrew Kelley закрывает PR ссылкой на strict no-LLM / no-AI policy. Нужен как пример, где маленький bugfix превращается в enforcement case.

- [ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983) — конкретный rejected PR, на который ссылается пост о миграции. Подтверждает тип дефектов, реакцию reviewers и то, как policy применялась в обсуждении.

- [ziglang/www.ziglang.org PR #502](https://github.com/ziglang/www.ziglang.org/pull/502) — `Exhibit C` из поста о миграции. PR `Package Management Guide (doc)`: reviewer указывает на устаревшие версии, manifest/API details и generic best practices; автор признаёт Claude / Gemini review и недостаток собственного знания Zig; Andrew Kelley закрывает PR ссылкой на policy. Полезен как документальный, а не compiler-code case.

### Первичные / близкие к проекту

- [Loris Cro, Contributor Poker and Zig's AI Ban](https://kristoff.it/blog/contributor-poker-and-ai/) — объяснение от Loris Cro, работающего в Zig Software Foundation. Это не официальный policy text, но очень важный источник мотивации: review budget, repeated interactions, contributor poker, examples of valuable contributors, growing pains и опыт LLM PRs.

- [Ziggit FAQ, AI Policy](https://ziggit.dev/faq) — правила community forum Ziggit. Это не официальный Code of Conduct core-проекта, но важный источник для разграничения: AI-generated posts и помощь с AI-generated code запрещены, механический перевод допускается.

- [Ziggit, Ziggit and Large Language Models](https://ziggit.dev/t/ziggit-and-large-language-models/15068) — обсуждение policy forum от апреля 2026 года. Нужен для понимания community moderation, раскрытия использования LLM и отличия демонстрационных AI projects от AI-generated ответов.

- [Ziggit, AI/LLM Policy Updates](https://ziggit.dev/t/ai-llm-policy-updates/15497) — follow-up от 13 мая 2026 года. Подтверждает `llm` tag для демонстрационных проектов, исключение для механического перевода и нежелательность slop / vibe-coded projects.

- [Ziggit, Bun’s Zig fork got 4x faster compilation times](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183) — внешняя дискуссия вокруг AI-generated изменений в fork. Важна как контрфакт: `mlugg` обсуждает техническую пригодность изменений отдельно от их происхождения.

- [Ziggit, Contributor Poker and Zig's AI Ban](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232) — обсуждение поста Loris Cro на Ziggit. Важно как источник уточнений Cro по практическому enforcement: подозрение на LLM-generated code или reasoning ведёт к закрытию PR / ban, а самый безопасный путь для contributors — не использовать LLM при участии в Zig.

- [Ziggit, Contributor Poker and Zig's AI Ban, page 2](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232?page=2) — продолжение обсуждения. Добавляет важные уточнения Cro: responsible AI users can choose not to use AI for a specific project, invite/vouch systems не снимают проблему приоритета non-LLM PR, reputational risk вокруг `vibecoded project`, и текущее понимание, что policy applies to core developers too.

- [Ziggit, Blocked without warning or explanation for comment on `https://codeberg.org/ziglang/zig/issues/32119`](https://ziggit.dev/t/blocked-without-warning-or-explanation-for-comment-on-https-codeberg-org-ziglang-zig-issues-32119/15741) — post-migration self-report и обсуждение после удаления Codeberg comments. Это не первичный moderation log, но полезный источник о том, как strict policy воспринимается участником и как community ссылается на Code of Conduct.

- [Lobsters, Contributor Poker and Zig's AI Ban](https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban) — публичное обсуждение поста Cro. Важен не как официальный policy text, а как источник возражений и ответов: `mtlynch` формулирует проблему ground truth / good LLM-assisted contributors, Cro объясняет предупредительную функцию policy, Andrew Kelley пишет о распознавании паттернов LLM-вкладов, неидеальности detection и желании invitation-tree trust model.

### Вторичные / реакции / фон

- [Luanti issue #17088, Discussion: Policy for AI-assisted contributions](https://github.com/luanti-org/luanti/issues/17088) — не источник о Zig policy как факте, но полезен как след внешнего обсуждения: PR #24983 упоминается как reference, а Luanti сравнивает разные модели AI contribution policy.

- [GitHub Changelog, Creating issues with Copilot on github.com is in public preview](https://github.blog/changelog/2025-05-19-creating-issues-with-copilot-on-github-com-is-in-public-preview/) — первичный источник GitHub о запуске функции, которая снижала трение при создании issues через Copilot. Это источник о платформенном контексте, а не о мотивах Zig.

- [GitHub ziglang/zig repository](https://github.com/ziglang/zig) — текущая GitHub page старого репозитория. Подтверждает публичный статус `Moved to Codeberg` и фразу `This repository is not mirrored`; полезно для визуального эпизода миграции, но не заменяет официальный пост о миграции.

- [Simon Willison, 30th April 2026 archive](https://simonwillison.net/2026/Apr/30/) — вторичный источник о том, как история Zig policy вышла в более широкий разговор об AI-assisted programming. Полезен как указатель на Bun fork / no upstream comment, пост Cro и комментарий Andrew Kelley на Lobsters; факты о Zig policy подтверждать первичными источниками. В проходе 06 использован только как внешний указатель на downstream-эпизод Bun и публичное восприятие policy, а не как замена Zig/Ziggit источникам.

- [JetBrains Blog, Why Zig Isn’t 1.0 (Yet)](https://blog.jetbrains.com/blog/2026/06/05/why-zig-isn-t-1-0-yet/) — официальный JetBrains blog post к интервью с Andrew Kelley. Подтверждает существование полного видео и то, что среди тем разговора есть отношение проекта к AI-generated contributions; не даёт transcript no-AI фрагмента.

- [Yahoo / Business Insider, Zig president says AI coding contributions are 'invariably garbage'](https://tech.yahoo.com/ai/claude/articles/zig-president-says-ai-coding-171749742.html) — вторичный пересказ Business Insider от 29 мая 2026 года с фрагментами из JetBrains podcast: negative review value, около 200 open PR, mentorship, drive-by contributors и простота blanket ban. В проходе 05 прямое открытие Yahoo вернуло 429, но поисковая выдача раскрыла полный релевантный фрагмент; использовать осторожно до раскрытия первичного видео / transcript.

- [QEMU Code Provenance documentation](https://www.qemu.org/docs/master/devel/code-provenance.html) — фоновый источник для сравнения open-source provenance policies. В текущем досье почти не раскрыт; не использовать для выводов о Zig.

### Непрочитанные / требуют проверки

- JetBrains / YouTube video `Zig 2026: No-AI Policy, $670K Foundation, Left GitHub & Why Zig Isn’t 1.0 - Andrew Kelley Explains`, YouTube id `iqddnwKF8HQ` — подтверждён через `jb.gg/andrew-kelley-zig-interview`, но полный первичный transcript / таймкоды no-AI фрагмента в проходе 05 не раскрыты. Не использовать для точных утверждений сверх JetBrains blog и вторичного пересказа Business Insider / Yahoo.

- NetBSD / Gentoo / Linux kernel AI contribution policies — найдены как внешний фон через Luanti discussion и поисковые результаты. Их нужно раскрывать только если будущая история будет сравнивать Zig с другими policy families.

- Официальная GitHub commit page для `d238078ae87f1beb565d42caee01ebd6a7a00d43` — желательно перепроверить, потому что текущий проход прочитал commit через mirror.

### Источники, заново раскрытые для переработки эпизодов

- [Loris Cro, “Contributor Poker and Zig's AI Ban”](https://kristoff.it/blog/contributor-poker-and-ai/) — основной первичный источник по contributor poker, перегрузке ревью, after-merge responsibility, hallucinated PRs, 10k-line first-time PRs and hidden LLM use in follow-up discussions.
- [ziglang/zig PR #24983](https://github.com/ziglang/zig/pull/24983) — конкретный exhibit case: maintainer comment about strict no LLM/AI policy, suspicion of LLM-generated comment/code and PR closure.
- [Zig wiki page “Writing Issues with Copilot and Other LLMs”](https://github.com/ziglang/zig/wiki/Writing-Issues-with-Copilot-and-Other-LLMs) — historical source showing the old wiki page moved into Code of Conduct.
- [Simon Willison, “The Zig project's rationale for their firm anti-AI contribution policy”](https://simonwillison.net/2026/Apr/30/zig-anti-ai/) — secondary interpretation and useful framing, including caution that a concrete rejected patch had technical concerns independent of the LLM issue.

## Поисковые формулировки

- `Zig project no AI generated contributions policy`
- `site:github.com/ziglang/zig AI generated pull requests policy`
- `Zig AI generated code contributions not accepted`
- `Andrew Kelley Zig AI generated code policy`
- `site:ziglang.org/news/ zig moving from github AI policy`
- `Zig moving from GitHub AI policy Codeberg Andrew Kelley`
- `site:ziglang.org/news "GitHub" "AI" "Zig"`
- `site:ziglang.org/devlog "GitHub" "AI" "Zig"`
- `"Block GitHub Copilot Issue Morpher" Zig`
- `"d238078ae87f1beb565d42caee01ebd6a7a00d43" Zig`
- `"Creating issues with Copilot" "public preview" GitHub May 2025`
- `"promoteVectorIndex" "Claude Code" "ziglang/zig"` — старый ложный след прохода 02; не использовать как подтверждённый exhibit без новой проверки.
- `"Fix integer underflow in Unit.resizeHeader" "ziglang/zig" "AI-generated"`
- `"ziglang/zig" "#25974" "strict no-llm"`
- `"ziglang/www.ziglang.org" "ai.txt" "AI-generated"` — старый ложный след прохода 02; не смешивать с PR #502 без новой проверки.
- `"Package Management Guide" "jimkring" "No LLM / AI Policy"`
- `"codeberg.org/ziglang/zig/issues/32119" LLM`
- `"Blocked without warning or explanation" "ziglang/zig/issues/32119"`
- `"AI/LLM Policy Updates" Ziggit`
- `site:ziggit.dev "Large Language Models" "Ziggit"`
- `site:ziggit.dev "Bun" "Zig fork" "compilation times" "mlugg"`
- `"Bun" "Zig fork" "4x faster compilation times" "LLM-authored"`
- `"We do not currently plan to upstream this" "Zig has a strict ban"`
- `"parallel semantic analysis" "determinism" "Zig" "mlugg"`
- `site:ziggit.dev "vibecoded project" "Zig" "kristoff"`
- `site:ziggit.dev "Does the current code-of-conduct" "core Zig developers"`
- `"This repository is not mirrored" "ziglang/zig" "Moved to Codeberg"`
- `JetBrains Andrew Kelley Zig no AI policy transcript`
- `Andrew Kelley Zig no-AI policy contributor poker`
- `"contributor poker" "Zig" "Andrew Kelley"`
- `"invariably garbage" "contributor poker" Zig`
- `site:youtube.com JetBrains Andrew Kelley Zig 2026 No-AI Policy`
- `"Zig 2026: No-AI Policy" YouTube JetBrains Andrew Kelley`
- `"Contributor Poker and Zig's AI Ban" Lobsters andrewrk`
- `"digital smell" "agentic coding" "andrewrk"`
- `"I hate being the cops" "andrewrk" "LLM"`
- `"Why Zig Isn't 1.0 (Yet)" JetBrains Andrew Kelley AI-generated contributions`
- `"Zig president says AI coding contributions are invariably garbage" Business Insider`
- `"People are sending us contributions that have no value whatsoever" "Zig"`
- `QEMU AI generated contributions policy`
- `NetBSD AI generated code policy`
- `OBS Studio AI generated contributions human written policy`
- `Luanti policy AI-assisted contributions Zig no AI`


### Дополнительные раскрытые источники текущего прохода

- [Ziggit, “Contributor Poker and Zig’s AI Ban”](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232) — primary/community source: review budget, LLM PR reasoning cost, suspected LLM use, distinction between mature exploration and bringing LLM output as authority.
- [Simon Willison, “The Zig project’s rationale...”](https://simonwillison.net/2026/Apr/30/zig-anti-ai/) — внешний источник: strict policy excerpt, Bun/Anthropic context, 4x compile-time fork improvement, no-upstream statement and later Zig contributor caveat.

### Дополнительные раскрытые источники pass 3

- [Loris Cro, “Contributor Poker and Zig’s AI Ban”](https://kristoff.it/blog/contributor-poker-and-ai/) — основной explanatory source: review capacity, investment in contributors, after-merge responsibility, why AI contributions damage the repeated game.
- [Hacker News discussion](https://news.ycombinator.com/item?id=47957294) — external reaction/source of concrete negative examples: hallucinated PRs, non-compiling code, huge first-time PRs, LLM use surfacing in follow-up discussion. Использовать осторожно; это не official Zig policy.
- [Business Insider, “Zig president says AI coding contributions are ‘invariably garbage’...”](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5) — secondary press source around JetBrains interview: Andrew Kelley’s public framing, review bottleneck, about 200 open PRs, no-exceptions enforcement. Проверить transcript/таймкоды перед прямыми цитатами.
- [Lobsters thread](https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban) — community discussion with useful framing of LLM PRs as one-shot game vs iterated contributor relationship. Не использовать как primary factual source.

## Кандидаты на иллюстрации

- Источник: [Loris Cro post](https://kristoff.it/blog/contributor-poker-and-ai/). Что искать: section headings `Growing pains`, `Banning AI contributions`, and paragraphs around after-merge responsibility. Зачем: показать policy как maintainer-economics argument. Статус: high; лучше пересказать, чем делать длинный screenshot.
- Источник: [Business Insider article](https://www.businessinsider.com/zig-programming-language-ai-rules-2026-5). Что искать: headline/card and quote area around review bottleneck/open PRs. Зачем: показать, что internal policy стала mainstream media event. Статус: low/medium; источник вторичный, права проверить.
- Источник: [HN discussion](https://news.ycombinator.com/item?id=47957294). Что искать: short fragment with concrete negative examples. Зачем: показать external controversy. Статус: low; использовать аккуратно, без длинных цитат.

- Zig Code of Conduct, раздел `Strict No LLM / No AI Policy`: скриншот или текстовый фрагмент страницы. Нужен для показа того, насколько широко сформулирован запрет: code, prose, editing, translation, brainstorming, bug finding, discussion of chatbot use. Статус: кандидат; права на скриншот проверить перед публикацией.

- PR #24983 discussion around `mlugg` comment and closure. Нужен как визуальный артефакт конкретного ревью: compile errors, bogus tests, stack UAF, `@memmove` -> `@memcpy`, random pings. Статус: кандидат; лучше использовать как ссылку и короткое описание, скриншот только после проверки прав / допустимости.

- Git commit / diff `d238078ae8` для `.github/ISSUE_TEMPLATE/config.yml`. Нужен как маленький технический артефакт: policy была превращена в изменение issue template сразу после запуска GitHub Copilot issue creation. Статус: кандидат; лучше перепроверить официальный GitHub commit page.

- GitHub Changelog screenshot / page fragment for `Creating issues with Copilot on github.com is in public preview`. Нужен для показа платформенного интерфейса, против которого Zig сделал обходное решение. Статус: кандидат; использовать осторожно, источник GitHub.

- PR #25974 discussion: маленький bugfix `Fix integer underflow in Unit.resizeHeader()`, вопрос `jacobly0` о reasoning, комментарий `s-lambert` про AI-generated происхождение и закрытие Andrew Kelley со ссылкой на policy. Нужен как короткая сцена, где maintainers не продолжают восстанавливать reasoning за AI-linked patch. Статус: кандидат; скриншот только после проверки прав.

- `www.ziglang.org` PR #502 discussion around Package Management Guide. Нужен как пример policy на документации: obsolete Zig versions, manifest/API details, old-style hash, `zig-cache no longer exists`, признание Claude / Gemini review и закрытие Andrew Kelley. Статус: кандидат.

- Zig 2025 Financial Report charts: 2024 GitHub Issues Per Month, closing time tables, donations / cash charts. Нужны для фона review pressure и бюджетных ограничений. Статус: кандидат; источник официальный, но права на воспроизведение проверить.

- Migrating from GitHub to Codeberg page, especially migration plan and issue numbering from 30000. Нужен для инфраструктурного поворота и связи policy с платформой. Статус: кандидат.

- Codeberg repository page `https://codeberg.org/ziglang/zig`. Нужен как визуальный знак, что canonical repo реально переехал. Статус: кандидат; в текущем проходе не раскрыт глубоко.

- Ziggit `AI Policy` FAQ / `llm` tag pages. Нужны для различения official Zig core policy и более гибкой moderation форума. Статус: кандидат; лучше не смешивать с официальным Zig Code of Conduct.

- Ziggit `AI/LLM Policy Updates` fragment around correction `Ziggit still is by humans and for humans` and `AI options and plugins are turned off`. Нужен как визуальная сцена, где форум разграничивает свою policy и authority ZSF / Andrew Kelley. Статус: кандидат; использовать как community artifact, не как official Zig policy.

- GitHub `ziglang/zig` repository page after migration: `Moved to Codeberg`, `This repository is not mirrored`, visible GitHub chrome with Copilot products in global navigation. Нужен как визуальный контраст между старой платформой и новой canonical source. Статус: кандидат; скриншот только после проверки прав / допустимости.

- Ziggit thread `Blocked without warning or explanation...` как скриншот пользовательского self-report после Codeberg issue `#32119`: удалённый комментарий, признание LLM help, ссылки участников на CoC, реакция про отмену donation. Нужен для сцены social friction; статус: слабый кандидат, потому что первичный Codeberg comment удалён.

- Ziggit thread `Bun's Zig fork got 4x faster compilation times`: фрагмент с разбором `mlugg` про parallel semantic analysis, детерминизм и codegen units. Нужен как визуальный counter-exhibit: downstream AI-assisted ускорение существует, но core maintainer обсуждает не лозунг, а конкретные ограничения compiler architecture. Статус: кандидат; права на скриншот проверить.

- Simon Willison archive fragment about Zig anti-AI / Bun fork: компактный внешний сигнал, что policy стала заметна за пределами Zig community. Статус: слабый кандидат; лучше использовать как secondary context, не как основной визуальный артефакт.

- Lobsters discussion fragment around `andrewrk` comments: спор о detectability, неидеальности распознавания, желании invitation tree и фраза про то, что текущая enforcement role стала токсичной. Нужен как визуальная сцена публичного спора о policy, а не только официального текста. Статус: кандидат; лучше цитировать коротко и ссылаться на thread, права на скриншот проверить.

- JetBrains blog / YouTube interview page: карточка `Why Zig Isn’t 1.0 (Yet)` и full interview link `jb.gg/andrew-kelley-zig-interview`. Может быть полезна, если история использует интервью как позднее публичное объяснение позиции Andrew Kelley. Статус: не использовать для точных цитат без transcript / таймкодов; thumbnail / кадры требуют проверки прав.


- Источник: [Ziggit Contributor Poker thread](https://ziggit.dev/t/contributor-poker-and-zigs-ai-ban/15232). Что искать: fragment around review-budget explanation and “closed/banned” practical rule. Зачем: показать, что policy в community discussion работает через review capacity and reasoning burden, not abstract culture war. Статус: high; лучше использовать короткий текстовый фрагмент/пересказ.
- Источник: [Simon Willison archive fragment](https://simonwillison.net/2026/Apr/30/zig-anti-ai/). Что искать: compact section linking Zig policy and Bun fork. Зачем: показать downstream/upstream contrast. Статус: medium.

### Дополнительные кандидаты после переработки эпизодов

- Скриншот PR #24983 с maintainer comment about strict no LLM/AI policy — high: конкретный exhibit case.
- Скриншот Code of Conduct / moved wiki reference — medium/high: показывает institutionalization of policy.
- Схема contributor poker: first PR → review investment → later contributor value vs one-shot LLM PR — high, лучше сделать локально.
- Скриншот/цитатный блок из Loris Cro article с “you play the person, not the cards” — medium: полезен, но нужно аккуратно с цитированием.

## Открытые вопросы

- Можно ли подтвердить commit `d238078ae87f1beb565d42caee01ebd6a7a00d43` через официальный GitHub URL или локальную историю, чтобы не опираться на зеркало в поздней версии истории?

- Когда именно policy перешла из `Contributing` / `Writing Issues with Copilot and Other LLMs` в Code of Conduct? Сейчас есть две точки: 11 июля 2025 в `Contributing` и 23 ноября 2025 move notice. Нужна commit / page history Code of Conduct, если будущей истории важна точная эволюция.

- Что Andrew Kelley говорит в JetBrains video о no-AI policy своими словами и на каких таймкодах? Пока есть JetBrains blog, редирект `jb.gg/andrew-kelley-zig-interview` на YouTube id `iqddnwKF8HQ` и вторичный пересказ Business Insider / Yahoo, но нет раскрытого primary transcript.

- Есть ли публичные Codeberg issues после миграции, где policy уже применялась в новом forge и сохранился первичный moderation trace? Сейчас есть Ziggit self-report вокруг `codeberg.org/ziglang/zig/issues/32119`, но удалённые комментарии и сама модерация не раскрыты как первичный source.

- Как проект различает запрещённый LLM brainstorming и допустимые локальные инструменты, компиляторные diagnostics, static analysis, обычный поиск и перевод на стороне читателя? В Code of Conduct граница задана, но практические кейсы могут быть сложнее.

- Как no-AI policy влияет на downstream projects вроде Bun, Ghostty, TigerBeetle или Uber, если они используют Zig, но имеют собственные policies? Для Bun теперь есть один раскрытый эпизод: AI-assisted изменения остались в fork и не планировались к upstream, а `mlugg` отдельно указал на проблемы детерминизма parallel semantic analysis [Simon Willison, 30th April 2026 archive](https://simonwillison.net/2026/Apr/30/); [Ziggit, Bun’s Zig fork got 4x faster compilation times](https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183). Для остальных downstream-проектов фактуры пока нет.

- Нужно ли будущей истории включать reputational/branding argument Cro про `vibecoded project`, или оставить его как фон? Он яркий, но может увести текст от ревью-бюджета и конкретных PR в культурную полемику.

- Как аккуратно описать “мы можем распознать LLM-паттерны”, не превращая это в необоснованный детектор? Lobsters даёт сильный материал от Andrew Kelley, но также показывает возражение про отсутствие эталона и риск ложных срабатываний / скрытых хороших LLM users.

## Синтез

Zig no-AI policy is the strongest counter-story in the new set. It does not argue that AI tools are useless. It argues that in a high-pressure open-source compiler project, the value of a contribution is not separable from the contributor’s understanding, follow-up responsibility and ability to grow into a trusted participant.

The policy is grounded in concrete maintainer economics: hallucinated PRs, non-compiling code, giant first-time patches, generated reasoning in discussions and the difficulty of distinguishing author understanding from LLM fluency. “Contributor poker” gives the story its core: maintainers are not only reviewing cards; they are betting on people. This makes Zig a necessary limit case for the corpus. AI-assisted work may be useful downstream or in private ownership, but upstream review has a social and maintenance budget that generated contributions can burn rather than save.
