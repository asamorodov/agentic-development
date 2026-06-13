# gas_town — external image queue after patch-pass

Статус после локального patch-pass: прежние inline external-real candidates решены как локальные `source_excerpt_asset` SVG. В статье больше нет пустых external placeholders.

## Resolved source-derived assets

| Figure id | Source signal | Local file | Current status |
|---|---|---|---|
| `fig-gastown-two-tier-beads-flow` | Steve Yegge, `Welcome to Gas Town`, Figure 6: `Two-Tier Beads Flow` | `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg` | local `source_excerpt_asset`; inline in article |
| `fig-gastown-worker-roles` | Steve Yegge, `Welcome to Gas Town`, Figure 5: `Gas Town’s Worker Roles` | `content/assets/atlas-images/gas-town/gastown-worker-roles.svg` | local `source_excerpt_asset`; inline in article |

## Deferred / queue-only source candidates

Эти кандидаты не стоят в статье и не являются blockers. Возвращаться к ним стоит только при отдельном визуальном проходе:

| Candidate | Source signal | Why queue-only |
|---|---|---|
| `fig-gastown-convoy-cli` | `Welcome to Gas Town`, Convoy CLI figure | Delivery loop уже поддержан локальной basic workflow figure; ещё одна картинка уведёт в UI-тур. |
| `fig-gastown-patrols` | `Welcome to Gas Town`, Patrols figure | Service agents объяснены прозой; отдельная картинка повысит плотность без нового тезиса. |
| `fig-gastown-formulas-cooking` | `Welcome to Gas Town`, Formulas/Cooking figure | Риск увести статью в MEOW/Formulas glossary. |
| `fig-gastown-ndi` | `Welcome to Gas Town`, NDI figure | Recovery/NDI не центральный визуальный тезис текущей версии. |
| `fig-gastown-gupp` | `Welcome to Gas Town`, GUPP figure | GUPP объяснён как принцип исполнения, не требует отдельной картинки. |
| `fig-gastown-meow-decomposition` | `Welcome to Gas Town`, MEOW figure | Декомпозиция достаточно поддержана текстом; фигура нужна только при явном comprehension gap. |
| `fig-gastown-plugins`, `fig-gastown-tmux-status`, `fig-gastown-tmux-list-sessions` | source article / UI surface | Сейчас отвели бы внимание от организационного состояния к терминальному/UI-туру. |

## Publication note

Локальные SVG являются редакционными source-derived diagrams, а не копиями Medium-изображений. Если позже потребуется именно оригинальный рисунок, нужен отдельный rights/quality pass.
