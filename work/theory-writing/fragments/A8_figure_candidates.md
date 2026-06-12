# A8 figure candidates

Статус после composition/visual/style repair 2026-06-11: основной фрагмент A8 держит 5 inline-фигур. Остальные кандидаты сохранены здесь как deferred / merged / technical-atlas material. Это не список обязательных вставок: каждая будущая фигура должна пройти asset-classification gate и usefulness/nontriviality gate.

## Inline в основном фрагменте

| Figure id | Тип | Решение | Зачем оставлена inline |
|---|---|---|---|
| `fig-a8-action-vs-acceptance-boundary` | `synthetic_figure` | keep inline | Центральное различение A8: разрешение на действие не равно праву признать изменение принятым. |
| `fig-a8-pr-as-candidate` | `synthetic_figure` | keep inline | Показывает PR как проверяемый кандидат, а не завершение работы. |
| `fig-a8-local-sandbox-action-boundary` | `local_image_asset` | keep inline as `<img>` | Реальная локальная иллюстрация к sandbox/worktree boundary; подпись очищена от служебного recovery-текста. |
| `fig-a8-contribution-policy-boundaries` | `synthetic_figure` | keep inline | Сводит разные open-source policy mechanisms без ложной линейной шкалы permissiveness. |
| `fig-a8-pwg-acceptance-state-machine` | `synthetic_figure` | keep inline | Нужна для финального перехода к PWG: принятие как отдельное состояние, а не переименование технического сигнала. |

## Снято с inline / объединено

| Старый figure id | Решение | Причина |
|---|---|---|
| `fig-a8-codeowners-gate` | merged into prose | CODEOWNERS важен как factual anchor, но отдельная схема была слишком технической для основного фрагмента и уводила в governance atlas. |
| `fig-a8-adr-adoption-vs-agent-draft` | merged into prose / possible atlas | ADR adoption описан в тексте через Nygard/AWS; отдельная state-flow схема может пригодиться в technical atlas или A9, но в A8 перегружает визуальный слой. |
| `fig-a8-authority-laundering-antipatterns` | merged into opening thesis / rejected as main figure | Таблица была полезной рабочей диагностикой, но в основном тексте выглядела как новая taxonomy. Центральный смысл теперь передан в начале и в PWG-state figure. |
| `fig-a8-babysit-pr-escalate-boundary` | merged into prose | `/babysit-pr` остаётся сильным якорем, но отдельная схема PR babysitting дублирует объяснение Fix/Dismiss/Escalate. |
| `fig-a8-homebrew-maintainer-load-policy` | merged into policy cluster | Homebrew-пункты сохранены в тексте; отдельная policy checklist была слишком локальной для A8. |
| `fig-a8-contribution-boundary-spectrum` | replaced by `fig-a8-contribution-policy-boundaries` | Старый вариант выглядел как шкала. Новый вариант показывает разные policy mechanisms без подмены их линейным спектром. |
| `fig-a8-zig-participation-boundary` | merged into policy cluster | Zig остаётся строгой точкой сравнения, но отдельная схема слишком раздувала open-source блок. |

## Asset-recovery status

- `content/assets/theory-images/mike-superset-worktrees.png` оставлен inline как локальный asset.
- CODEOWNERS, ADR status, `/babysit-pr`, Homebrew/Zig policy и PWG acceptance остаются синтетическими/текстовыми решениями; готового локального source image, который надо было бы восстановить вместо схемы, для них сейчас не используется.
- Внешние реальные кандидаты по ADR (`ext-adr-nygard-minimal-adr`, `ext-adr-aws-lifecycle`) остаются в asset catalog и требуют отдельного rights/quality/placement pass перед любой заменой текста на screenshot/source diagram.

## Проверка поддержки текстом

Текущий набор inline-фигур покрывает только несущие различения A8. Детальные схемы CODEOWNERS, ADR adoption, `/babysit-pr`, Homebrew и Zig лучше держать для technical atlas или локальных вставок в более прикладных разделах. Основной A8 должен оставаться governance-узлом: кто может действовать, кто принимает, какие свидетельства нужны между этими контурами и как это хранится в PWG.
