# gas_town — open questions

Статус после Final: файл очищен от устаревших pass-to-pass долгов. Здесь остаются только реальные блокеры и проверочные вопросы текущей статьи.

## Publication blockers

1. **Два внешних placeholder-изображения.**
   - `fig-gastown-two-tier-beads-flow` и `fig-gastown-worker-roles` стоят в статье без локального `<img>`.
   - Нужно либо получить/проверить права/качество и добавить локальные файлы, либо заменить синтетическими схемами, либо удалить placeholder figures.

2. **Свежесть version-sensitive источников.**
   - Перед публикацией проверить актуальность формулировок по `Gas Town CHANGELOG`, `Gas Town Scheduler design`, `Beads Releases`, DoltHub sync workflow и troubleshooting/sandbox режимам.
   - Это не `source missing`, а freshness check: технические детали могут измениться.

3. **Hacker News ссылка.**
   - Сейчас HN используется только как слабый сигнал восприятия, не как источник фактов о Gas Town.
   - Финальное решение: оставить этот perception signal в статье или перенести в source notes, если публичная статья должна опираться только на первичные/официальные источники.

## Editorial watchpoints

1. **Плотность технических списков.**
   - Очередь/backpressure, decomposition и infrastructure sections содержат много статусов, команд и режимов.
   - Не сокращать их автоматически: они являются technical anchors. Но финальная вычитка может сгруппировать некоторые перечисления, если они мешают чтению.

2. **Contract/minimal frame после P22.**
   - Вход теперь начинается с проблемы и механизма, а не с таксономии.
   - Проверить в финальном проходе, нужно ли держать contract section и minimal frame двумя отдельными блоками или их можно слегка сжать без потери границы Beads/PWG/Gas Town.

3. **Визуальная близость `fig-gastown-architecture` и `fig-gastown-two-tier-beads-flow`.**
   - Они поддерживают разные тезисы: локальная архитектура рабочих областей и two-tier Beads state flow.
   - Если внешний source figure не будет добавлен, проверить, не достаточно ли локальной архитектурной схемы.

## Resolved questions

- H1 теперь называет Gas Town.
- Входная структура исправлена: проблема масштаба и pressure ladder идут до контракта Beads/PWG/Gas Town.
- Нижний раздел `Внешние изображения для asset-pass` восстановлен в финальной проверке, потому что package blueprint требует mirror для inline external-real candidates; подробная очередь остаётся в companion-файле.
- `fig-gastown-problems-view` больше не является external-real placeholder.
- Нет стандартного `C5/A10 sync pending`: соответствующие теоретические различения уже перенесены в публичные секции статьи.
