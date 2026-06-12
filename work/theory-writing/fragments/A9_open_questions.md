# A9 open questions

## 1. Сколько incident-management фактуры нужно в финальной главе

Во втором проходе A9 получил один сильный источник для incident feedback: Google SRE postmortem culture. Этого достаточно для структурного тезиса “incident → reviewed action items → repaired environment”, но не для отдельного обзора incident-management tooling. Если финальная глава захочет показать живую цепочку `incident report → PR → release → repaired rule/spec/ADR`, нужен отдельный публичный case with issue/PR/release/postmortem evidence. Без такого кейса лучше не расширять A9: иначе фрагмент уйдёт в обзор SRE вместо lifecycle repair.

## 2. Где провести границу между rule repair and rule accumulation

Фрагмент уже говорит, что repeating failure should become a rule/skill/hook/test/gate only when the trigger is precise. Открытый вопрос: нужна ли в финальном тексте отдельная политика удаления rules/skills, например expiry, owner, source event, last validated date or superseded-by field. Это может быть важнее добавления новых examples, потому что stale rules становятся главным failure mode после накопления memory files.

## 3. Нужен ли supply-chain / dependency inventory хвост

A9 упоминает dependency and release feedback, но не раскрывает SBOM, lockfile drift, dependency policy, package lifecycle scripts, vulnerability advisories or provenance updates. Эта тема может принадлежать соседнему фрагменту про evidence/completion или отдельному supply-chain tail. Если добавить её сюда, нужно удержать связь с “карта будущей работы”, а не превращать текст в security checklist.

## 4. Нужно ли добавлять отдельный release case study

Pact and Argo сейчас используются как tooling-level anchors: они показывают contract matrix, deployment record, canary metrics and inconclusive pause. Для повествовательной плотности можно добавить один public release case, где after-merge feedback изменил rule/spec/ADR. Но такой case должен иметь проверяемую цепочку, иначе он ослабит provenance discipline.

## 5. Какой рисунок выбрать

Primary candidate остаётся Figure 1, потому что она показывает петлю: merge → signals → freshness check → repair → next work. Figure 3 хороша как side matrix, но может сделать раздел слишком чек-листовым. Figure 4 useful if финальная глава хочет подчеркнуть routing сигналов: incident, release, spec drift and rule drift ремонтируют разные поверхности. Figure 5 полезна, если финальный текст будет сильнее опираться на product migration oracle.

## 6. Как не переутвердить Product Migration field report

Третий проход усилил Subramanian case как источник migration oracle patterns: read-only DB, reference implementation, live Swagger docs, per-ticket docs, CI/SonarQube gates, QA handoff. Но outcome metrics источника остаются author-reported. В финальном тексте нужно удержать статус: это field report about evidence design, not independent proof of migration success. Нельзя писать, что migration objectively proved zero defects without public PR/CI/review artifacts.

## 7. Нужно ли отделить work graph cleanup from workspace cleanup

В фрагмент добавлены Beads recovery/architecture and Claude Code worktrees. Это два разных хвоста: logical graph state and physical execution state. В финальной главе можно оставить их рядом как два слоя cleanup, но не стоит смешивать: graph cleanup answers “what work is still valid/blocked/evidenced?”, workspace cleanup answers “which branches/worktrees/temp configs still represent live work?”.

## 8. Нужна ли формальная модель oracle provenance

A9 уже называет oracle provenance: legacy behavior, reference implementation, schema comparison, contract matrix, fixture diff, canary metric, QA report. Открытый вопрос — нужна ли отдельная мини-таблица “oracle source / independence / scope / failure mode”. Это может связать A9 с будущей частью о test data, environment and oracle independence.


## 9. Как формально различать advisory memory and hard policy

Source/depth pass добавил Claude Code memory/hooks boundary: `CLAUDE.md`, rules and auto memory guide the agent, but hard blocking belongs in hooks, permissions, tests or external gates. В финальном тексте нужно не переутвердить memory as enforcement. Открытый вопрос — нужна ли в A9 короткая policy table: `memory/rule` for durable context, `skill` for repeatable procedure, `hook/test/gate` for enforceable lifecycle condition, `source event + owner + deletion path` for stale-rule control.

## 10. Нужно ли развернуть support/user signal отдельно от incident signal

Теперь support/user report прикреплён к Matt Pocock triage state machine, а incident feedback — к Google SRE postmortem. В финальной главе можно оставить их рядом как разные входы одного feedback router, но не стоит смешивать: support signal чаще требует triage state, reproduction and reporter loop; incident signal требует reviewed action items, priority and system repair.

## 11. Нужно ли разгрузить основной фрагмент от части ссылок

Композиционный проход сделал `A9_lifecycle_repair.md` более связным, но плотность источников остаётся высокой, потому что фрагмент покрывает ADR, spec, memory/rules/hooks, PWG, migration oracle, incident and release feedback. В финальной главе можно оставить все ссылки рядом с утверждениями, но технический атлас может принять на себя hook event schemas, Beads recovery details, release-tool comparison and oracle-provenance table.

## 12. Какой уровень детализации оставить для hooks and work graph cleanup

В основном тексте достаточно различить advisory memory, skill and enforceable hook/gate. Подробности Claude Code hook events and Beads recovery commands полезны для handbook/atlas, но могут снова превратить A9 в tooling catalogue. При финальной сборке нужно проверить, не лучше ли дать одну короткую таблицу выбора repair target, а детали перенести в атлас.


## Content repair pass status

Проверка как готовящегося теоретического фрагмента не потребовала новых внешних источников. Основной дефект был не в нехватке фактов, а в риске переутвердить Product Migration field report и в устаревших формулировках source/story/figure notes после стилевых проходов. Открытыми остаются те же вопросы финальной сборки: терминологический pass, распределение tool-specific деталей между теорией и technical atlas, выбор основной фигуры и возможный отдельный public case для incident/release chain.

## Residual repair pass status

Остаточный проход не открыл новых содержательных вопросов. Главные unresolved items остаются прежними: терминология source terms, распределение tool-specific деталей между основным текстом и atlas/sidebar, возможная отдельная цепочка incident/release case и supply/security tail. В основном фрагменте исправлены только локальные шероховатости переходов и точность Subramanian/Pact framing.

## Composition / visual / style repair status 2026-06-11

No new open questions were created. The main resolved defects were visual overload and service-style captions. Remaining open questions are narrower:

- whether ADR/release-specific source visuals should become technical-atlas figures after rights/quality check;
- whether a future public incident/release case should be added as a separate forensic anchor;
- how aggressively final terminology should translate source terms such as `skill`, `hook`, `gate`, `worktree`, `oracle`, `cutover` and `rollback`.
