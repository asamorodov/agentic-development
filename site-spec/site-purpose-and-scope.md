# Назначение и границы сайта

Мы создаём новый сайт из уже подготовленных Markdown-документов.

При полной пересборке сайт нужно строить из `/content` и `/site-spec`. Текущий `/site` не является источником содержательной истины: его можно использовать как текущий технический артефакт и ориентир по интерфейсу, но не как замену Markdown-документам.

Все содержательные изменения уже находятся в текущих `.md`. Не нужно заново писать главы, пересказывать документы, улучшать стиль, добавлять новые аналитические разделы или проводить содержательную редактуру. Задача — собрать сайт из актуальных Markdown-файлов, сохранить текст, сделать удобную навигацию, корректные якоря и рабочую структуру чтения.

Входная структура:

```text
/content/
  stories/
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

  Orientation.md
  Story_introduction.md
  Theoretical_synthesis.md
  Cross_story_synthesis.md
  Handbook.md
  Fieldbook.md
```

`Codex Working Reference` сейчас не входит в этот сайт. Это отдельный будущий справочный сайт / раздел, не надо смешивать его с этим корпусом.

## Цель

Нужно создать сайт для дальнейшей работы над материалом по агентской разработке.

Это не публичная полированная книга, а рабочий сайт для навигации, чтения, редактирования и дальнейшего развития корпуса. Главная ценность уже находится в документах. Задача сайта — аккуратно собрать их, сделать удобную навигацию, сохранить текст, сохранить и проверить перекрёстные ссылки, не потерять структуру и не исказить смысл.
