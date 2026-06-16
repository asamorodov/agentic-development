# Visual assets and figures

Статус: обязательное правило для writing-pass, repair-pass, asset-pass и package-generation задач, где появляются `<figure>`, screenshots, diagrams, локальные изображения или figure candidates.

## Главная граница

Готовая иллюстрация не является сырьём для текстового пересказа.

Если материал уже существует как локальное изображение, screenshot, source diagram, график, таблица-изображение или другая внешняя визуальная форма, его нельзя по умолчанию переписывать, перерисовывать, «нормализовать» или заменять текстовой схемой. Такая замена допустима только после явного решения, что нужна новая авторская synthetic figure, а не сохранение исходного визуального ассета.

## Обязательная классификация

Перед любым действием с визуальным материалом сначала присвой ему один из статусов:

- `source_real_image` / `local_image_asset` — реальное изображение, screenshot, dashboard, trace, UI-снимок, source diagram, график или таблица, которые уже локализованы в репозитории и важны именно как наблюдаемая фактура источника;
- `external_real_image_candidate` — такая же реальная внешняя картинка, screenshot, source diagram, график или таблица, но ещё не локализованная, не проверенная или не готовая к вставке;
- `source_backed_redraw` — перерисованная схема по источнику или нескольким источникам: структура взята из внешнего материала, но переводится, упрощается, приводится к единому стилю или объединяется с близкими схемами;
- `source_backed_synthetic_figure` — авторская схема, основанная на источниках и тексте главы, но объясняющая собственный синтез главы, а не воспроизводящая один внешний рисунок;
- `synthetic_figure` — авторская схема, таблица или диаграмма, которую мы создаём сами для объяснения аргумента; этот статус допустим только после проверки, что схема действительно полезна, нетривиальна и не является декоративным пересказом прозы;
- `editorial_visual_idea` — идея будущей визуализации, которой пока нет ни как готового asset, ни как оформленной public figure.

`*_figure_candidates.md` — это реестр возможностей, статусов и решений. Он не означает, что каждый кандидат должен быть вставлен inline, и не означает, что каждый кандидат нужно превращать в текстовую схему.

## Правило выбора типа визуального материала

Решение зависит не от того, что проще вставить, а от функции изображения в объяснении главы.

1. Используй `source_real_image` / `local_image_asset`, если важна именно фактура источника: реальный UI, dashboard, trace, screenshot документации, конкретная диаграмма автора, таблица-изображение, видимый состав полей, кнопок, панелей или терминов.
2. Делай `source_backed_redraw`, если источник даёт сильную структуру, но её нужно перевести, упростить, привести к стилю книги, объединить с близкими источниками или сделать читаемой в нашем layout. В caption указывать source basis; redraw не должен притворяться оригинальным скриншотом.
3. Делай `source_backed_synthetic_figure` или `synthetic_figure`, если изображение объясняет собственный аргумент главы: lifecycle, границу ответственности, маршрут выбора, контур состояния, ошибку, переход или синтез нескольких материалов. В caption указывать, что это схема по материалам главы или по указанным источникам.
4. Отклоняй или откладывай кандидат, если он декоративен, дублирует соседний абзац, плохо читается, уводит в соседнюю тему, не имеет понятного происхождения или требует отдельного asset-pass.

Нельзя автоматически заменять реальные source images синтетическими схемами. Нельзя автоматически вставлять source images только потому, что они найдены. Сначала определить роль изображения, потом выбирать форму.

## Visual source discovery

Когда глава использует внешние источники, source-reading pass должен смотреть не только на текстовые аргументы, но и на визуальные элементы источников: diagrams, screenshots, UI examples, architecture diagrams, lifecycle diagrams, tables, API sketches and trace/dashboard fragments.

Для каждого сильного источника зафиксировать, есть ли визуальный кандидат и какое решение лучше: вставить готовый asset, поставить внешний кандидат в очередь, сделать source-backed redraw, сделать авторскую synthetic figure или отклонить.

## Нейтральные prompts для генерации схем

Если пакет или последующий asset-pass генерирует `source_backed_redraw`, `source_backed_synthetic_figure` или `synthetic_figure` через image-generation tool, формулировать задание нейтральным архитектурным языком. Это снижает риск ложного отказа генератора и не меняет смысл главы.

Предпочитать: `architecture diagram`, `lifecycle checkpoint`, `validation step`, `confirmation`, `review gate`, `controlled access`, `generic adapter`, `external data source`, `execution environment`, `state update`.

Осторожно использовать или переформулировать в prompts: `опасное действие`, `заблокировать`, `обойти`, `exploit`, `attack`, `shell access`, `external actions`, `production secret`, `вмешательство в опасные ходы`. Если глава действительно обсуждает безопасность, смысл не смягчать в тексте; но prompt для картинки можно формулировать как «действия, требующие проверки», «контрольная точка», «подтверждение», «ограничение радиуса действия».

Для MCP, hooks, permissions, sandbox и внешних сервисов по возможности использовать generic labels вместо брендов и логотипов: `репозиторий`, `документация`, `сервис задач`, `наблюдаемость`, `файловое хранилище`. Если генерация отказывается, повторить по одной иллюстрации за раз и убрать лишние формулировки про управление внешними действиями, оставив техническую структуру.

## Ограничение на собственные схемы

Собственные синтетические схемы — исключительный инструмент, а не способ закрыть пункт «добавить figure». Создавай `synthetic_figure` только если она одновременно:

- проясняет нетривиальную связь, развилку, процесс, границу ответственности, lifecycle-переход или сравнительную структуру, которую трудно удержать в прозе;
- добавляет самостоятельную объяснительную ценность, а не повторяет соседний абзац в виде банальной таблицы или декоративного блока;
- не подменяет готовый local/external image asset и не маскирует отсутствие asset-pass;
- заслуживает сохранения как часть читательского материала, а не как рабочая заметка редактора.

Если схема не проходит этот gate, оставь идею в `*_figure_candidates.md` со статусом `editorial_visual_idea`, `deferred` или `rejected`; не вставляй её в основной текст ради количества визуальных блоков.

## Что можно вставлять inline

Inline в основной фрагмент можно вставлять только готовые публичные визуальные элементы:

1. `local_image_asset` / `source_real_image`, если путь проверен и материал можно использовать: `<figure class="image-asset" id="..."><img src="..." alt="..." /><figcaption>...</figcaption></figure>`.
2. `source_backed_redraw`, если он уже создан как локальный asset или оформленная публичная схема с понятным source basis.
3. `source_backed_synthetic_figure` / `synthetic_figure`, если она прошла usefulness/nontriviality gate и уже оформлена как публичная схема/таблица/диаграмма без служебного мета-текста.

`external_real_image_candidate` без asset-pass, rights-check, download/localization и quality-check остаётся в companion-файле и/или общем asset catalog. Его нельзя подменять synthetic figure только ради того, чтобы закрыть пункт «вставить `<figure>` в текст».

## Repair-pass

Repair-pass должен убирать из публичного текста служебный мета-текст: `Тип`, `Идея`, `Зачем нужен`, `Статус`, `лучше поставить`, `если редактор`, `repair-note`, `executor-note`, asset-pass notes и другие следы рабочего процесса.

Но cleanup не должен деградировать изображение. Если служебная заметка относится к настоящему изображению, она должна стать asset-reference/status note в companion-файле или нормальной `<figure><img ...></figure>` после asset-pass. Если служебная заметка относится к synthetic figure, её можно переписать как публичную подпись, таблицу или схему только при условии, что сама схема проходит usefulness/nontriviality gate; иначе идею нужно оставить в companion-файле или удалить из основного текста.

## Каталог

Если в workflow уже есть общий каталог, синхронизируй решения с:

```text
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
```

Каталог должен хранить не только уже скачанные файлы, но и внешние реальные изображения-кандидаты из досье, пока они не прошли asset-pass.

## Специальное правило для статей концептуально-технического атласа

Для обычных теоретических фрагментов визуальный слой должен быть строгим и экономным. Для больших статей концептуально-технического атласа правило другое: релевантные изображения являются нормальной частью самостоятельного concept-first объяснения.

Если локальный asset уже есть в репозитории и релевантен статье, его следует вставить в текст как `<figure><img ...></figure>`, даже если тяжёлый файл не передан в текущий package context. Если в первоисточнике есть реальное внешнее изображение, screenshot, source diagram, UI-снимок или architecture diagram, но оно ещё не локализовано, его нужно поставить как inline `external-real-candidate` placeholder и добавить в нижний раздел `Внешние изображения для asset-pass` / external image queue.

Это правило не отменяет запрет на деградацию изображений: внешнюю или локальную картинку нельзя пересказывать текстовой схемой. Собственная synthetic figure остаётся допустимой только при явной нетривиальной пользе и не может заменять готовый или внешний реальный asset.

## Dossier image-candidate sections

For concept-atlas article packages, the primary dossier's image-candidate section is a required visual source. Search headings such as `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates`, or equivalent wording before doing broad external image search.

Every dossier-listed real image candidate must receive an explicit disposition in the article image plan: inserted inline, queued only, deferred, rejected, superseded by local asset, or not found in source. If the candidate is needed for the article, place an inline `<figure data-asset-status="external-real-candidate">` at the relevant point in the article and mirror it in the bottom `Внешние изображения для asset-pass` section and the external image queue.

Existing local assets follow insert-or-explain: insert relevant assets as real `<figure><img ...></figure>` blocks or explicitly explain rejection in the image plan. Never replace a ready local asset or external source image with a synthetic text diagram by default.
