# GSD / Open GSD — open questions

Статус: Final verification / consolidated publication blockers.

Этот файл больше не хранит хронологический список долгов каждого прохода. Закрытые вопросы по P02–P22 удалены или сведены к текущим публикационным рискам ниже.

## Настоящие blockers перед публикацией

1. **Freshness / release channels.** Перед датированной публикацией нужно перепроверить текущие версии `gsd-core` и `gsd-pi`, release channels, tagged releases и различие между `main`, docs-site и опубликованными пакетами. Статья уже содержит caveat про tagged release и supply-chain trust; без свежего browse/release-pass нельзя утверждать точные версии.
2. **Lineage reference paths.** В статье сознательно использованы некоторые lineage/reference links (`artifact-types.md`, `verification-patterns.md`) как опора для механизма потребления артефактов и проверки. Перед финальной публикацией нужно либо подтвердить, что эти пути всё ещё являются правильной публичной ссылкой для текущего Open GSD, либо оставить их как lineage/source caveat в metadata.
3. **External real images.** Официальный rights-safe screenshot/diagram Open GSD не вставлен. Если финальная площадка требует реальные внешние изображения, нужен отдельный asset-pass: найти официальный источник, проверить права/качество, локализовать файл и вставить его рядом с соответствующим механизмом (`gsd-core`, `gsd-pi` или `gsd-browser`), а не в нижний редакционный backlog.
4. **Image path assembly.** Для локального Codex asset нужно сохранить `data-repo-path` и проверить, как site assembly переписывает относительный путь `../../../content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`.
5. **Language/style final polish.** P24–P26 выровняли тон, заголовки, переходы и основные калькированные обороты. Перед сдачей остаётся только publication-level copyedit при необходимости: проверить устойчивые source terms (`issue`, `workstream`, `seed`, `thread`, `hook`, `skill`, `profile`, `policy`) без изменения команд, config keys, source labels и имён продуктовых сущностей.
6. **Neighbor article links.** Когда в атласе появятся отдельные статьи про PWG, Spec Kit/Kiro/SPDD, BMAD, Gas Town, ADR или browser evidence, нужно добавить article-to-article links. Сейчас границы самодостаточны и не требуют раздувать основной текст.

## Вопросы, закрытые к P23

- Issue-driven orchestration перенесён в основной текст как входной слой и сквозной пример; это больше не отдельный долг P03/P09.
- Первый экран перестроен problem-first; старый долг о переносе failure section закрыт P22.
- Нижний пользовательский раздел `Внешние изображения для asset-pass` удалён; статус внешних изображений хранится только в companion-файлах.
- Визуальный слой признан достаточным для текущей статьи: четыре synthetic figures и один local image asset; дополнительные схемы остаются не blockers, а будущими editorial ideas.
- Общие `C5/A10 sync pending` не нужны: связь с C5/A10 сведена к конкретным theory links и будущим article-to-article links.

## Final verification note

Финальная проверка не обнаружила отсутствующих обязательных outputs. Текущие blockers остаются publication-level: свежесть release/docs, lineage paths, возможный внешний real-image pass, сборка относительного пути локального asset и будущие links на соседние статьи. Общего долга вида `relevant but untransferred` нет.
