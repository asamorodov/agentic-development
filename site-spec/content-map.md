# Карта контента сайта

## Структура сайта

Сайт должен иметь такую структуру:

```text
Orientation
12 историй
  Введение к корпусу
  Как читать корпус историй
  12 отдельных историй
Теоретическая часть
Cross-Story Synthesis
Handbook
Fieldbook
```

Соответствие документов:

```text
Orientation → Orientation.md

12 историй:
  Введение к корпусу / Как читать корпус историй → Story_introduction.md
  сами истории → все файлы из /content/stories/ в указанном порядке 01–12

Теоретическая часть → Theoretical_synthesis.md
Cross-Story Synthesis → Cross_story_synthesis.md
Handbook → Handbook.md
Fieldbook → Fieldbook.md
```

Отдельный индекс историй не нужен: навигация слева уже выполняет эту функцию.

## Точный порядок историй

```text
  01_boris_tane_research_plan_implement_reconstruction_connected.md
  02_peter_steinberger_maximum_deep_dive_reconstruction_connected.md
  03_simon_willison_agentic_research_reconstruction_connected.md
  04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
  05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
  06_jesse_vincent_agentic_workflow_reconstruction_connected.md
  07_human_layer_agentic_harness_reconstruction_connected.md
  08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
  09_calvin_french_owen_maximum_deep_reconstruction_connected.md
  10_mark_erikson_maximum_deep_reconstruction_connected.md
  11_mae_capozzi_maximum_deep_reconstruction_connected.md
  12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
```

Порядок историй нельзя угадывать по времени изменения файлов. Если файл переименован, нужно обновить этот список и проверить ссылки из `Handbook.md`, `Cross_story_synthesis.md`, `Theoretical_synthesis.md` и `Fieldbook.md`.
