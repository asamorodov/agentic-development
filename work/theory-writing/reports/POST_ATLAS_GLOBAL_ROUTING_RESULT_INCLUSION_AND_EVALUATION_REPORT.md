# Post-Atlas global routing result — inclusion and evaluation

Статус: результат включён в файловую систему как рабочий routing layer для будущего изготовления планов глав.

## Что включено

Из `POST_ATLAS_GLOBAL_CORPUS_ROUTING_RESULT.zip` включены:

```text
work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md
work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md
work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md
work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_OPEN_QUESTIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_READINESS_REPORT.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_VERIFY.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_RESUME.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_PACKAGE_MANIFEST.md
```

Сырой result-архив также сохранён для трассируемости:

```text
work/theory-writing/results/POST_ATLAS_GLOBAL_CORPUS_ROUTING_RESULT.zip
```

## Общая оценка

Результат полезен и его можно принимать как текущий слой маршрутизации корпуса. Он выполняет именно ту функцию, ради которой создавался общий package: не пишет главы, не запускает внешний поиск, не выбирает окончательные формулировки, а раскладывает корпус по будущим главам.

Главный практический выход:

```text
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
```

Эта матрица должна стать первым входом для будущего изготовления планов глав. Она не заменяет Skeleton V5, `00_spine_map` или per-chapter blueprint, но снимает необходимость заново инвентаризировать весь корпус для каждой главы.

## Что получилось хорошо

- Все будущие главы имеют entry: `INTRO`, I–XIII, `CONCLUSION`, `APPENDIX`.
- Все 10 статей Атласа маршрутизированы.
- A/B/C-фрагменты классифицированы как базовый синтез, источники различений или служебные контрольные входы.
- Досье поставлены на место gap-check/source-restoration, а не превращены в основной черновик глав.
- Истории маршрутизированы разреженно: как фактические якоря, а не как материал для пересказа всего story corpus.
- External discovery профили назначены без искусственного поиска для всех глав: `D0`, `D1`, `D2`, `D3`.
- Visual candidates отделены от текста глав и оставлены для будущего asset-pass.

## Что не является проблемой

Во время uploaded run в использованном snapshot были недоступны два blueprint-файла:

```text
work/theory-writing/reports/POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
```

В текущем cumulative filesystem state эти файлы уже существуют. Это не требует повторного запуска общего routing package. Достаточно использовать result maps вместе с актуальным `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md`.

## Watchpoints перед изготовлением планов глав

1. **VI / VII boundary.** `Контекст и рабочее состояние` и `Persistent Work Graph` близки. При изготовлении планов нужно решить, остаётся ли VI самостоятельной мостовой главой или часть материала переносится в VII/IX.
2. **V / VIII catalog risk.** Главы о защищённых спецификационных и процессных профилях легко превращаются в каталог методов. Нужен сильный section contract.
3. **IX scope risk.** Глава про execution/harness/runtime требует D3-discovery, но не должна стать обзором LangGraph/Temporal/DBOS/Restate/Codex/Claude.
4. **XI evidence scope.** Глава о свидетельствах требует внешних источников, но evidence нельзя сводить к тестам или CI.
5. **XII governance boundary.** Глава должна говорить о праве действия и праве завершения в lifecycle программного изменения, а не уходить в общую политику или юридический обзор.
6. **Visual asset pass.** Внешние визуальные кандидаты не проверялись. Это отдельный будущий проход, не блокер для изготовления текстовых планов.

## Нужно ли что-то поправить

Содержательно — нет, полный повтор общего package не нужен.

Нужны только две малые правки/осторожности перед следующим этапом:

1. При создании планов глав считать `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` актуальным blueprint, несмотря на то что uploaded run не видел этот файл.
2. Перед массовым изготовлением планов глав желательно сделать короткий локальный language/style cleanup самих routing maps. В них остался служебный англо-русский слой; он приемлем для рабочего routing layer, но не должен мигрировать в будущие публичные или near-public документы.

## Рекомендация

Принять результат как baseline для следующего шага. Следующий рабочий шаг — изготовить первый per-chapter target plan по матрице входов. Лучшие кандидаты:

- глава III — specification / contract / ADR;
- глава VII — Persistent Work Graph;
- глава IX — execution / harness / runtime;
- глава XI — evidence / review / proof quality.
