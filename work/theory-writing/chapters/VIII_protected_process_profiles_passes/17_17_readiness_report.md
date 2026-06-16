# VIII — readiness report

Статус: глава готова как результат текущего пакета.

Основной файл:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
```

## Что объясняет глава

Глава VIII объясняет слой между долговечным состоянием работы и реальной средой исполнения. Главная мысль:

> PWG or durable work state показывает, где находится работа, но не выбирает следующий режим сам.

После главы VII у проекта может быть хороший work node: зависимости, блокеры, проверки, ревью, краткое восстановление контекста. Но следующая сессия всё равно может ошибиться, если войдёт в задачу не в том режиме: начнёт реализовывать там, где нужно исследовать старую систему, продолжит старый план там, где нужен `correct-course`, или начнёт чинить симптом там, где сначала нужен case file.

Сквозной пример `billing/API` показывает этот сбой на одном узле: одна и та же восстановленная работа может требовать story creation, execution, brownfield investigation, `correct-course`, verification or human checkpoint.

## Реально использованные источники

### Внутренние

- `C2_pwg_to_process_profiles.md` — центральное различение PWG/state and process profile.
- `A5_process_methodologies_synthesis.md` — GSD/BMAD как process methodologies.
- `B3_gas_town_beyond_pwg.md` — верхняя граница Gas Town/Beads.
- `gsd_open_gsd` atlas/dossier — GSD section.
- `bmad_method` atlas/dossier — BMAD section.
- `gas_town` atlas/dossier — boundary section.

### Внешние

- Open GSD docs: documentation home, Quickstart, The Phase Loop, Planning Artifacts, Specialist Agents.
- BMAD docs and repository sources: Workflow Map, Getting Started, Core Tools, `bmad-create-story` SKILL, `bmad-correct-course` SKILL, Established Projects FAQ, Project Context, Forensic Investigation.
- Jesse Vincent — Rules and Gates.
- HumanLayer — 12 Factor Agents.
- Matt Pocock skills repository.
- Beads documentation and Gas Town README.

В основном тексте сохранено 21 markdown-link, привязанных к месту использования фактуры.

## Что осознанно отклонено

- **Mae Capozzi and Shopify Roast** не включены в основной текст. Они были в исходном routing, но текущая глава уже показывает малые profiles через Jesse/HumanLayer/Matt. Возвращать их стоит только если нужен новый механизм, а не дополнительный пример.
- **BMAD Workflow Map diagram** не вставлен как изображение. Он слишком method-specific для общей теоретической главы и требует отдельной проверки прав/качества.
- **GSD atlas synthetic figures** не переиспользованы. Они объясняют GSD как метод, а не общий слой выбора режима.
- **HumanLayer and Gas Town local images** не вставлены. Они больше подходят главам IX–X.
- **Общие role-based agent workflow sources** не использованы, потому что официальные GSD/BMAD sources были точнее.

## Визуальные решения

Изображения не вставлены в основной markdown.

Созданы candidates:

1. `fig-viii-process-profile-interface` — основной synthetic candidate: work state/signal → profile selection → read set → allowed actions → required output → stop/reroute/gate → durable state update.
2. `fig-viii-billing-api-profile-routing` — вторичный synthetic candidate: один узел `billing/API` и разные правильные маршруты.

Остальные candidates отложены или отклонены в `VIII_protected_process_profiles_figure_candidates.md`.

## Companion files

Проверены и согласованы с основным текстом:

```text
work/theory-writing/chapters/VIII_protected_process_profiles_source_register.md
work/theory-writing/chapters/VIII_protected_process_profiles_fragment_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_atlas_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_dossier_gap_notes.md
work/theory-writing/chapters/VIII_protected_process_profiles_external_discovery_log.md
work/theory-writing/chapters/VIII_protected_process_profiles_story_anchors.md
work/theory-writing/chapters/VIII_protected_process_profiles_figure_candidates.md
work/theory-writing/chapters/VIII_protected_process_profiles_open_questions.md
work/theory-writing/chapters/VIII_protected_process_profiles_degradation_and_duplication_audit.md
```

## Regression note

- Центральная ось не потеряна: глава возвращается к вопросу «какой следующий ход имеет право быть следующим?».
- `billing/API` сохранён как synthetic cross-example and не представлен как реальный источник.
- GSD не превращён в самостоятельную статью.
- BMAD остаётся самым плотным разделом, но после P14 не захватывает главу: каждая деталь привязана к маршрутизации следующего режима.
- Gas Town/Beads оставлены как мост к главе X, а не раскрыты внутри главы VIII.
- Глава явно готовит главу IX: правильный профиль ещё не гарантирует безопасное действие без worktree/sandbox/permissions/tools/hooks/MCP access.
- В основном тексте не обнаружены служебные P11/P12/P13/P14 comments, TODO/FIXME or package instructions.

## Оставшиеся вопросы

1. Вставлять ли `fig-viii-process-profile-interface` в публикационную версию.
2. Проверить source-native terms в финальном стилевом слое, если chapter audience будет шире текущей инженерной аудитории.
3. Перед публикацией перепроверить актуальность BMAD/GSD docs, если будет временной разрыв.
4. Не расширять BMAD-раздел без удаления менее важной детали.
