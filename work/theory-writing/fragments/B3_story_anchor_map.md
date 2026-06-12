# B3: карта сюжетных опор

| История / baseline | Где использована | Функция в B3 | Ограничение |
|---|---|---|---|
| `work/old-site-theoretical-synthesis-baseline.md` | Основной anti-degradation anchor для Gas Town. | Сохраняет старую сильную линию: Gas Town как организационная среда вокруг agentic development, где есть роли, Mayor, сервисные агенты, mail, hooks, merge queue, patrol, agent-not-session и цена оркестрации. | Не цитируется как внешний источник; фактические утверждения в B3 переведены на первичные ссылки. |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Не развёрнут в основном тексте; удержан как соседняя граница. | Показывает слой ниже: harness engineering делает отдельного агента пригодным через контекст, инструменты, hooks, проверки и правила. B3 использует только итоговую теоретическую связку: harness → PWG → Gas Town. | Не превращать B3 в пересказ HumanLayer; при расширении можно добавить одну связующую сноску к HumanLayer, но не в этот компактный фрагмент. |
| `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` | Непосредственная предшествующая опора. | Даёт уже установленную границу PWG: честное продолжение работы через долговечное состояние, зависимости, условия остановки, передачу, свидетельства и восстановление. B3 начинается там, где эта граница становится организационной средой. | Не повторять A4 и не расширять PWG так, чтобы он стал «всем Gas Town». |
| Gas Town primary-source cluster | Основные фактические якоря в B3. | README/Docs/Architecture/Welcome/Changelog/Beads docs показывают операционную петлю: роли, Mayor, Crew/Polecat, Beads/Dolt, `bd prime`, hooks, mail/передачу работы, workflows, merge queue, сервисных агентов, backpressure, escalation/seance/scheduler и цену. | Держать как несколько точных якорей, а не обзор источников. |

## Нарративная функция B3

B3 должен закрыть вопрос «зачем Gas Town нужен теории, если уже есть PWG». Ответ: PWG объясняет, как работа становится долговечной и продолжимой; Gas Town показывает, какие организационные функции появляются вокруг такой работы, когда исполнителей много, сессии расходуемы, а человек не может читать каждый поток. Поэтому B3 не рассказывает историю Gas Town хронологически. Он использует Gas Town как deep case организационно-операционного жизненного цикла.

## Фактические опоры, добавленные в repair-pass

В усиленном проходе B3 получил больше конкретики без превращения в обзор источников: `gt feed --problems` как поверхность видимости для человека; mail protocol как поверхность передачи работы; `bd pin`/`bd hook` как поддержка владения и передачи; MEOW/Molecule/Wisp как форма декомпозиции работы; Refinery/Witness/Deacon/Dogs как сервисные петли; цена оркестрации как деньги/токены, внимание и обслуживание.

## Второй repair-pass: граница PWG/Gas Town

Граница была сначала вынесена в отдельный блок, а затем в выравнивающем pass интегрирована во вступление, synthetic table и финальный тезис: bead/PWG-node остаётся носителем продолжимой работы, а Town/Rig, Mayor, queue, mail, hooks и сервисные агенты читаются как организационная оболочка. Это снижает риск свести Gas Town к Beads, не заставляя B3 дублировать A4.

## Source-pass: актуализация adjacent material

В source-pass раскрыты внешние источники, которые уже выводились из текста и inline-ссылок. Уточнены актуальные якоря: README теперь поддерживает scheduler и seance как механизмы ограничения пропускной способности и продолжения сессий; escalation design добавлен как управляемый путь blocker-а Agent → Deacon → Mayor → Overseer; polecat lifecycle patrol заменил старую mail-protocol ссылку и удерживает mail-based передачу вместе с recovery/patrol контекстом. Medium оставлен как источник по нарративу, ролям и цене; утверждения о storage для Beads перенесены на current Beads/Dolt sources, чтобы B3 не унаследовал устаревшую деталь из старой статьи.

## Второй style-pass: ограничение истории

История Steve Yegge / `Welcome to Gas Town` остаётся в B3 только как якорь для ролей, agent-not-session, GUPP/hook culture и цены frontier-системы. B3 не пересказывает статью и не строит хронологию Gas Town. Старый baseline используется как anti-degradation memory: он защищает плотность фактуры, но не диктует структуру публичного фрагмента.

## Repair-pass `dd3dc3e2`: story regression check

Повторная проверка не нашла пересказа истории в основном B3. `Welcome to Gas Town` используется как первичный narrative/cost/role anchor, а HumanLayer and old baseline остаются companion-level ориентирами. Новых story fragments в основной текст не добавлялось.

## Residual story note `35eab4eb`

Остаточный pass не добавлял новых историй и не расширял роль `Welcome to Gas Town`: статья остаётся ограниченным primary anchor for roles/cost, not a narrative spine.

## Repair-pass `b3_style_boundary_repair_2026_06_11`

Историческая функция B3 не изменилась: Gas Town остаётся deep case организационно-операционного жизненного цикла. Repair-pass не добавлял новые story anchors; он только подчистил язык основного текста и companion-файлов, чтобы роль Gas Town не читалась через машинные кальки вроде `рабочий субстрат` или через английский клей.
