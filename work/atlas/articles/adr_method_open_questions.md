# adr_method — open questions

Статус: P27 final synchronized.

## Текстовые блокеры

Текстовых блокеров для текущей версии статьи нет. Вопросы, которые раньше числились открытыми, закрыты в основном тексте:

- `origin: reconstructed` разведён со `status`; реконструированный ADR описан как гипотеза до ревью.
- Production-grade ADR gate покрыт через GitHub `Design Decision Gate` и общий порядок deterministic threshold → evidence → draft → human completion.
- Синхронизация полного ADR и короткой агентской проекции описана через index/command, skill, hook, resolver, compiler и PR/CI gate.
- Место LLM-reviewer ADR ограничено triage/draft/reconstruction; статус решения остаётся человеческим или организационным переходом.
- Tyree/Akerman/Y-statements не добавлялись, потому что статья уже держит reader question через Nygard/Fowler/MADR, `Confirmation`, replacement и agent-facing projection.
- Architecture fitness functions оставлены за пределами статьи: здесь они появляются только как часть `Confirmation`.

## Реальные оставшиеся долги

- Asset-долг: внешние изображения остаются placeholders. Нужны проверка прав, читаемости, crop, alt text, локализация и финальное решение, какие placeholders превращать в локальные `<img>`.
- Atlas-composition debt: когда будут известны постоянные URL соседних статей, можно добавить обратные ссылки на Spec Kit, TDAD, Persistent Work Graph и общую теорию. Это не блокирует текущую статью.
