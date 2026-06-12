# C3 figure candidates

Статус: companion-файл к `C3_pwg_to_evidence.md`. Реестр фиксирует inline-решения, отложенные кандидаты, asset-pass notes, rights/status notes и причины отказа. Готовые внешние изображения не заменялись текстовыми схемами; для C3 оставлена одна `synthetic_figure`, потому что она объясняет нетривиальную структуру перехода от рабочего статуса к принятию `completed`.

| ID | Asset-статус | Источник / происхождение | Решение | Причина |
| --- | --- | --- | --- | --- |
| `fig-c3-completion-transition-guard` | `synthetic_figure` | Собственная схема по C3-аргументу, опирается на PWG/evidence/ADR/migration distinctions | Вставлена inline в основной текст. | Проходит usefulness/nontriviality gate: показывает, какие поля должны сопровождать переход в `completed`, явно разводит контрольное условие завершения, адрес прикрепления и пакет свидетельств, и не дублирует соседний абзац как декоративная таблица. |
| `fig-beads-ready-queue` | `editorial_visual_idea` | Beads Dependencies / `bd ready` / `bd blocked` | Перенесено в atlas/PWG-layer, не вставлено в C3. | Объясняет очередь готовой работы, но C3 фокусируется на доказанности завершения. Inline-вставка увела бы фрагмент в PWG-технический атлас; готового локального asset нет. |
| `fig-gates-as-durable-waits` | `editorial_visual_idea` | Beads `bd gate` + Temporal-style durable waits | Отложено. | Полезно для общего PWG-раздела, но связь gate/evidence уже встроена в основную inline-схему и короткий абзац. Отдельная фигура стала бы дублирующей. |
| `fig-tdad-test-map-evidence` | `external_real_image_candidate` | TDAD paper / tdad-skill `.tdad/test_map.txt` | Отложено в technical atlas или TDAD profile. | Поддерживает пример оракула, но C3 не должен становиться TDAD-обзором. Возможные фигуры из статьи не локализованы; права и качество не проверены. |
| `fig-adr-confirmation-ladder` | `editorial_visual_idea` | MADR `Confirmation`, CODEOWNERS, SLO, rollout | Не вставлено. | Близко к A2/ADR material. В C3 достаточно одного абзаца, иначе мост начнёт выполнять работу ADR-фрагмента. |
| `fig-migration-parity-gates` | `editorial_visual_idea` | Anthropic modernization, Winder, TechChannel, Augmented Code | Отложено в migration story / fieldbook. | Хороший полевой материал, но в C3 он был бы слишком большим и превратил мост в миграционный раздел. |
| `fig-source-state-to-evidence-package` | `editorial_visual_idea` | PWG dossier source-state flow + текущие companion files | Не вставлено. | Для документной работы важно, но уже покрыто текстом и companion-файлами. Лучше использовать позже в technical atlas для многопроходного документного процесса. |
| `fig-c3-observation-test-review-rollout-lanes` | `editorial_visual_idea` | Arvid Kahl, Roast, Stripe Minions, Argo Rollouts | Не вставлено. | Идея полезна как схема дорожек для итогового обзора, но сейчас вторая inline figure перегрузила бы мост и стала бы пересказом соседних абзацев. Оставить для позднего композиционный проход. |
| `fig-roast-final-output-artifact` | `external_real_image_candidate` | Daniel Doubrovkine Roast run / `.roast/sessions/.../final_output.txt` | Не локализовано. | Реальный saved artifact может быть полезен в A7/technical atlas, но права/качество не проверены; C3 использует источник как текстовое подтверждение. |
| `fig-stripe-clean-context-review-loop` | `editorial_visual_idea` | Stripe Minions + AI Engineer notes | Отложено. | Может показать рабочий агент → clean-context judge → diagnostics → PR/human review, но это уже диаграмма ревью за пределами моста C3. |
| `fig-argo-analysis-state-transition` | `editorial_visual_idea` | Argo Rollouts Analysis | Отложено. | Полезно для rollout chapter или evidence atlas; C3 использует rollout как один пример post-merge evidence, а не как самостоятельное объяснение progressive delivery. |
| `fig-sre-canary-evaluation` | `external_real_image_candidate` | Google SRE Workbook — Canarying Releases содержит реальные release/canary diagrams и metric figures. | Не вставлено. | Asset-classification pass: это не повод рисовать synthetic figure. Права/качество/потребность для C3 не проверены; текущий текст использует источник как operational claim, не как visual evidence. |
| `fig-pact-contract-scope` | `editorial_visual_idea` | Pact consumer contract scope | Не вставлено. | Слишком узко для C3. Pact добавлен как короткий API-оракул, а диаграмма превратила бы мост в contract-testing explainer. |
| A7 local image assets | `local_image_asset` | `openai-codex-chrome-devtools-validation.webp`, `03-simon-showboat-curl-demo.jpg` из A7 | Не вставлены в C3. | Это реальные локальные активы для различения observation/evidence в A7. В C3 они не являются центральным мостом к `completed`; повторная вставка создала бы дублирование и потерю композиционной границы. |

## Заметки asset-pass

- Второй стилевой проход нормализовал классификацию: каждый кандидат теперь имеет ровно один статус из asset policy — `synthetic_figure`, `local_image_asset`, `external_real_image_candidate` или `editorial_visual_idea`.
- `fig-c3-completion-transition-guard` не держится по инерции. Она остаётся нужна как transition-guard, но новых inline/local/external assets не требуется.
- Единственная inline-фигура остаётся достаточной; второй lane-summary, rollout diagram или contract scope diagram был бы дублирующим и сделал бы фрагмент похожим на визуальное оглавление.
- Предыдущий evidence-attachment pass изменил только существующую synthetic figure: добавлена строка `attachment_address`. Классификация не изменилась; usefulness/nontriviality gate пройден, потому что строка показывает, куда именно прикрепляется evidence внутри PWG.
- В C3 нет нового `local_image_asset`: разрешённые входы не содержали отдельного asset catalog, а выбранный ход лучше объясняется одной синтетической схемой.
- Внешние paper/product/customer diagrams из TDAD, Beads, ADR, Product Migration и Google SRE не локализованы, права не проверены, качество не проверено; они остаются кандидатами для atlas/fieldbook, а не inline-материалом C3.
- Ни один реальный внешний screenshot/source diagram не был перерисован как synthetic figure ради закрытия визуального требования; Google SRE figures явно классифицированы как реальные внешние image candidates, а не материал для текстовой схемы.

## Readiness note

`fig-c3-completion-transition-guard` готова как рабочая inline-фигура: она покрывает не только evidence package, но и границу gate/evidence плюс адрес прикрепления. Перед публикационной сборкой нужен общий visual pass: проверить, не дублирует ли она фигуры A7/A8, и решить, нужна ли более компактная подпись после сборки главы.
