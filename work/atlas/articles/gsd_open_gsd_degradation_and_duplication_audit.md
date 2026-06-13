# GSD / Open GSD — degradation and duplication audit

Статус: Final verification / degradation and duplication audit complete for current package.

## Проверка деградации статьи

| Риск | Наблюдение P01 | Статус |
|---|---|---|
| Статья стала пересказом досье | Структура построена вокруг reader question и центральной оси process-runtime profile; досье не пересказано по порядку | OK for P01 |
| Статья стала техническим справочником команд | Команды приведены как anchors механизма; подробные cheat sheets отложены в Fieldbook | OK for P01 |
| Статья стала мини-теорией | Раздел PWG ограничен boundary; C5/A10 не пересказаны целиком | OK for P01 |
| Недостаток фактуры закрыт общей прозой | Основные тезисы подкреплены командами, файлами, state surfaces, policies, gates, failure modes | OK for P01; нужен дальнейший source-depth проход |
| Визуальный слой подменил реальные изображения | Вставлены только synthetic figures; external real images не выдуманы и не скачаны | OK for P01 |
| Captions служебные | Captions объясняют смысл figure, не рассказывают историю asset-pass | OK |
| Source provenance | В статье используются primary/source links; internal dossier не цитируется как public source | OK for P01 |

## Controlled repetition audit

Повтор с общей теорией оправдан в трёх местах:

1. `process-runtime profile` — нужно для самостоятельного понимания GSD.
2. `GSD ещё не PWG` — центральная boundary статьи.
3. Свидетельства / acceptance / право завершения — нужно для связи GSD с SDLC decision map.

Повтор не разворачивает всю A10/C5 траекторию и не делает статью полной альтернативой общей теории.

## Style risks to repair later

- В P01 есть плотные технические абзацы; P17–P26 должны проверить тяжёлые цепочки и English glue.
- Термины `process-runtime profile`, `Persistent Work Graph`, `ToolsPolicy`, `context rot`, `checkpoint`, `workstream`, `runtime`, `headless` оставлены как source-specific или устойчивые technical labels; при языковом проходе нужно проверить, где рядом нужно русское объяснение.
- В статье много ссылок на source docs; structure pass может часть ссылок сгруппировать, не теряя provenance near facts.

## P02 contract audit

| Проверка | Итог P02 |
|---|---|
| Риск общего обзора | Снижен: добавлен явный контракт статьи и критерии успешного чтения |
| Риск продуктового учебника или справочника | Снижен: отрицательная граница запрещает уход в инвентарь команд и справочник конфигурации |
| Повтор теории | Контролируемый: PWG boundary повторяет только нужный критерий, не разворачивает всю PWG-теорию |
| Дубль BMAD | Снижен: BMAD упомянут через контраст artifact-first, без переноса деталей его рабочего процесса |
| Дубль Gas Town | Снижен: Gas Town упомянут как многоагентная операционная среда, без инвентаря ролей |
| Дубль Spec Kit/Kiro/SPDD | Снижен: specification family grouped as boundary, not explained as separate methods |
| Lifecycle control visibility | Усилен: contract names phase transition, context recovery, supervision/evidence, tool policy, git isolation and ceremony cost |


## P04 lifecycle-control audit

| Проверка | Итог P04 |
|---|---|
| Риск command catalog | Снижен: `User Guide` перенесён как lifecycle-control matrix, а не как полный список команд |
| Видимость stop/move/human-supervision | Усилена: добавлена таблица по маршрутизации, Discuss/UI, Plan, Execute, Verify/Ship и side channels |
| Риск дублирования существующего фазового раздела | Контролируемый: новый subsection даёт обзор переходов, а следующий раздел сохраняет подробный разбор `gsd-core` |
| Риск преждевременной gate taxonomy | Сдержан: точные gates/checkpoints оставлены как долг source-depth, P04 использует только уже поддержанные anchors |
| Визуальная перегрузка | Сдержана: новая схема не вставлена, возможный visual candidate отложен |


## P05 runtime-discipline audit

| Проверка | Итог P05 |
|---|---|
| Риск справочника команд | Сдержан: добавлена runtime-discipline table, а не inventory команд |
| Видимость configuration/architecture | Усилена: commands/config/architecture/tool policy/git/browser evidence сведены в один тезис |
| Риск дублирования `gsd-pi` section | Контролируемый: P05 subsection даёт cross-surface synthesis, а `gsd-pi` section сохраняет конкретную runtime mechanics |
| Риск visual duplication | Сдержан: новая figure не вставлена, возможный stack visual отложен до P13 |
| Source provenance | Сохранён: новые утверждения опираются на уже учтённые primary links, internal dossier не цитируется в статье |


## P06 continuation/recovery audit

| Проверка | Итог P06 |
|---|---|
| Риск приравнять durable markdown к PWG | Снижен: статья теперь явно говорит, что state files feed continuation but do not create graph semantics alone |
| Риск справочника artifact formats | Сдержан: `HANDOFF.json`, `.continue-here.md`, migration and diagnostics named only as mechanism anchors |
| Риск дублирования `gsd-pi` section | Контролируемый: P06 subsection synthesizes continuation/recovery boundary, while later `gsd-pi` section keeps runtime mechanics |
| Риск visual overload | Сдержан: новая figure не вставлена; visual candidate deferred |
| Source provenance | Сохранён: новые тезисы опираются на known primary links and companion ledger, not internal dossier citations |


## P07 runtime/state/verification audit

| Проверка | Итог P07 |
|---|---|
| Риск feature-list по `gsd-pi` | Снижен: добавлена lifecycle table rather than command inventory |
| Риск дублирования существующих paragraphs | Контролируемый: P07 subsection synthesizes lifecycle; later paragraphs preserve specific mechanisms |
| Риск слишком плотного `gsd-pi` section | Повышен умеренно; flagged for later compression/style pass |
| Риск смешать DB authority and markdown projections | Снижен: lifecycle table and existing P06 boundary reinforce source-of-truth distinction |
| Source provenance | Сохранён: P07 uses dossier-supported primary links only |


## P08 failure/anti-summary audit

| Проверка | Итог P08 |
|---|---|
| Риск рекламного резюме | Снижен: added anti-summary paragraph and failure limits |
| Риск tutorialization | Снижен: phase loop without control is explicitly rejected |
| Риск over-ceremony | Kept visible as first failure mode |
| Риск stale artifacts | Снижен: stale `PLAN.md` and consumer chain named explicitly |
| Риск PWG collapse | Снижен: no-full-graph-state boundary added |
| Риск overexpansion | Controlled: no new recipe, no full troubleshooting checklist, no full PWG theory |


## P09 free-expansion audit

| Проверка | Итог P09 |
|---|---|
| Did the pass add a real mechanism? | Yes: issue ingress and GitHub sync boundary |
| Risk of command catalog | Controlled: no full issue-driven command walkthrough |
| Risk of external-tool drift | Flagged: GitHub sync config needs freshness check before publication |
| Boundary clarity | Improved: tracker is mirror/channel, not internal runtime authority |
| Visual impact | No new image inserted; synthetic candidate deferred |


## P10 reader-path audit

| Проверка | Итог P10 |
|---|---|
| Coherence gap | Improved: added end-to-end issue-to-ship reader path |
| Risk of invented case | Controlled: explicitly synthetic/typical, no fake repo details |
| Risk of tutorialization | Controlled: example explains transition authority, not how-to commands |
| Duplication with artifact figure | Potential; flagged for visual/structure pass |
| Theory return | Strengthened through transition questions |


## P11 local visual asset audit

| Проверка | Итог P11 |
|---|---|
| Insert-or-explain for allowed local assets | Completed: one inserted, two explained as not inserted |
| Risk of source confusion | Controlled: caption explicitly states OpenAI Codex image is an analogy, not a GSD screenshot |
| Risk of decorative image | Controlled: dashboard image rejected; harness-feedback image rejected for this article |
| Visual/source provenance | Improved: image plan and source usage now record local asset decisions |
| Synthetic replacement risk | Avoided: no local ready asset was redrawn as a text surrogate |

## P12 external visual audit

| Проверка | Итог P12 |
|---|---|
| Dossier candidates disposition | Completed in image plan; candidates treated as synthetic/editorial unless already covered. |
| External-real placeholder discipline | Preserved: no inline placeholder inserted without a real standalone image candidate. |
| Screenshot substitution risk | Avoided: missing official screenshots were not replaced with synthetic text diagrams. |
| Local asset boundary | Preserved: P11 Codex image remains labeled as analogy, not GSD source screenshot. |
| Companion synchronization | Updated: source usage, transfer ledger, image plan, queue, open questions, theory links, audit and readiness reflect P12. |

## P13 synthetic visual audit

| Проверка | Итог P13 |
|---|---|
| Rare/nontrivial gate | Applied: no new synthetic figure passed the usefulness threshold. |
| Duplication risk | Reduced: issue-to-ship, runtime-stack and failure-matrix visuals deferred. |
| External image substitution risk | Avoided: P13 did not turn unfound external candidates into author diagrams. |
| Public-text cleanliness | Main article keeps the existing figures and updates only the asset-pass status section. |

## P14 standalone concept audit

| Проверка | Итог P14 |
|---|---|
| Standalone readability | Improved: article now gives a local five-part frame before deep technical sections. |
| Theory duplication risk | Controlled: no broad A/B/C theory path copied; repeated terms are immediately grounded in GSD. |
| Reference-catalogue risk | Reduced: the new frame evaluates commands/files by function rather than listing them. |
| Source provenance | Preserved: public article cites Open GSD primary links, not internal C5 fragments or dossier pass history. |
| Visual impact | No new figure; no queue change. |

## P15 mechanism/failure audit

| Проверка | Итог P15 |
|---|---|
| Phase workflow tutorial risk | Reduced: added negative test that phases require input/consumer/stop condition. |
| Persistent-file illusion | Reduced: files without consumers/freshness checks are explicitly called archive, not usable state. |
| Hidden supervision | Strengthened: autonomous continuation requires visible stop/pause/recover/takeover boundaries. |
| Weak verification | Strengthened through existence/substance/wiring/behavior distinction. |
| Pseudo-PWG risk | Strengthened: graph-like artifacts are insufficient without explicit graph state. |
| Ceremony exceeds task risk | Strengthened: quick/fast/no-GSD path named as correct reduction. |
| Catalogue risk | Controlled: no separate error catalogue added; limits embedded near mechanism. |

## P16 theory-link audit

| Проверка | Итог P16 |
|---|---|
| Generic “see also” risk | Avoided: backlinks name the question each theory fragment answers. |
| Main-text theory bloat | Avoided: article text unchanged because P14/P15 already carry local theory. |
| Standalone article | Preserved: no requirement to read A3/A5/A7/A9/A10 before understanding GSD. |
| Boundary precision | Improved through companion links to specification, process, evidence, repair and mode-selection questions. |
| Visual impact | No image changes. |


## P17 language audit

| Проверка | Итог P17 |
|---|---|
| Русский режим основного текста | Улучшен: случайная английская связка заменена русскими формами. |
| Повреждение технических имён | Не выявлено после проверки: команды, URL, `workflow.*`, `/gsd-workflow`, пути и ключи сохранены. |
| Риск потери фактов | Низкий: проход не менял источник, аргумент или структуру статьи. |
| Риск чрезмерного перевода | Контролируется: точные source labels оставлены там, где они нужны для проверки источника. |
| Следующий языковой долг | Остаются отдельные устойчивые термины (`issue`, `workstream`, `seed`, `thread`, `hook`, `skill`, `audit trace`) для второго прохода. |

## P18 language audit

| Проверка | Итог P18 |
|---|---|
| Заголовки | Улучшены: часть калькированных и pass-facing форм заменена человеческими заголовками. |
| Captions | Улучшены: подписи объясняют рабочую функцию изображений без декоративности. |
| Tables | Улучшены: отдельные source labels получили русское пояснение, а таблица `gsd-pi` стала яснее. |
| Bottom asset section | Улучшен: убрана ссылка на P12 из основного пользовательского текста. |
| Сохранение содержания | Сохранено: факты, источники, границы и изображение не менялись. |

## P19 editorial audit

| Проверка | Итог P19 |
|---|---|
| Standalone concept-first финал | Улучшен: статья больше не заканчивается служебным asset-pass разделом. |
| Потеря визуальной информации | Избежана: все решения по изображениям сохранены в image companions. |
| Дублирование P12/P18 в основном тексте | Устранено: пользовательская статья не содержит pass-history. |
| Фактическая целостность | Сохранена: источники, аргумент, схемы и локальное изображение не менялись. |
| Readiness | Улучшена: основной текст готовнее к публикационной вычитке. |

## P20 editorial audit

| Проверка | Итог P20 |
|---|---|
| Вступительный meta-layer | Уменьшен: `Контракт статьи` заменён на `Что важно удержать`. |
| Standalone concept-first entry | Улучшен: читатель получает рабочую модель, а не редакционный бриф. |
| Сохранение фактуры | Сохранено: технические детали и источники не менялись. |
| Дублирование с мини-рамкой | Контролируется: первый раздел даёт задачу чтения, мини-рамка ниже даёт локальные различения. |
| Visual impact | Нет изменений. |

## P21 editorial audit

| Проверка | Итог P21 |
|---|---|
| Теоретический жаргон во входе | Уменьшен: `местные различения` заменены на `рабочие опоры`. |
| Standalone readability | Улучшена: читателю не нужно знать внутренний язык атласа. |
| Риск потери концептов | Низкий: пять понятий сохранены и привязаны к GSD-поверхностям. |
| Visual impact | Нет изменений. |

## P22 structure audit

| Проверка | Итог P22 |
|---|---|
| First-screen problem-first entry | Улучшена: раздел о том, что ломается без внешнего процесса, теперь стоит сразу после вводного объекта статьи. |
| Taxonomy-first risk | Снижен: различие `gsd-core` / `gsd-pi` / `gsd-browser` остаётся во вступлении, но за ним сразу следует конкретная проблема. |
| Handbook/tutorial drift | Не усилен: команды и файлы не расширялись; изменён только порядок уже существующих объяснений. |
| Visual balance | Не изменился: четыре synthetic figures и один local image asset остаются на своих местах. |
| Service captions / asset-pass notes | Не выявлены в основном тексте; нижний asset backlog остаётся вне публичной статьи. |

## P23 companion-sync audit

| Проверка | Итог P23 |
|---|---|
| Устаревшие долги | Очищены из `open_questions`: вместо pass-history оставлены текущие publication blockers. |
| Source usage alignment | Соответствует статье; главный риск теперь freshness/release verification, а не пропущенный перенос фактуры. |
| Ledger bloat | Снижен: отложенный материал переописан как реальные границы статьи и публикационные проверки. |
| Image companions | Согласованы с основным текстом: четыре synthetic figures, один local image asset, внешних inline candidates нет. |
| C5/A10 pending | Не оставлено как общий долг; theory links содержат конкретные semantic links и будущие article-link задачи. |

## P24 style-defect audit

| Проверка | Итог P24 |
|---|---|
| Псевдотермины / кальки | Исправлены реальные дефекты: `публичная поверхность`, `анти-резюме`, `процессная машина`, `исполняемая дисциплина`, `coverage решений`. |
| Неестественные заголовки | Смягчены три заголовка: negative-test, phase-permission and command-surface sections now read more naturally in Russian. |
| Content preservation | Сохранено: факты, источники, figures, source labels, команды и config keys не переписаны. |
| Over-editing risk | Контролируется: компактные технические фразы оставлены, где они понятны и не прячут смысл. |
| Theory term bridge | `Ремонт жизненного цикла` в читательском блоке заменён на `Обновление после поставки`; semantic link сохранён в companion theory note. |

## P25 selective rewrite audit

| Проверка | Итог P25 |
|---|---|
| Selective rewrite | Выполнен точечно: исправлены оставшиеся кальки и тяжёлые обороты, без переписывания сильных технических абзацев. |
| Content preservation | Сохранено: структура, источники, команды, paths, config keys, figures and claims unchanged. |
| Russian naturalness | Улучшены boundary paragraphs, command-routing section, runtime policy section, `gsd-pi` lifecycle table and final failure-mode wording. |
| Summary drift | Не усилился: конкретика команд, файлов, режимов и ограничений сохранена. |

## P26 guarded final style audit

| Проверка | Итог P26 |
|---|---|
| Human technical tone | Улучшен: финальные правки выровняли вступление, переходы, runtime-profile paragraph, `gsd-pi` details and PWG boundary wording. |
| Preservation of specificity | Сохранено: команды, числа, ограничения, source labels, paths, config keys and figures unchanged. |
| English handling | Улучшено: обычные слова вроде shell pipeline / pytest markers переведены; source-specific labels kept or code-styled. |
| Pseudo-term regression | Не выявлен: P24/P25 corrections not reverted. |
| Over-smoothing risk | Контролируется: техническая конкретика и таблицы сохранены. |

## Final verification audit

Финальная проверка подтвердила: основной текст не превратился в краткий overview, source companions не заменяют статью, captions публичные, локальный asset имеет читательскую подпись без служебных пометок, synthetic figures не подменяют выбранные real images, а C5/A10 sync представлен через конкретные semantic links and debts. Найденная стилeвая регрессия `ремонт жизненного цикла` исправлена в основном тексте без потери технических anchors.
