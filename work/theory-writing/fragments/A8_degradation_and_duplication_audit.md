# A8 degradation and duplication audit

## Цель прохода

Проверить, не превращает ли фрагмент технические сигналы в человеческое принятие. Основной риск A8 — authority laundering: агент или автоматический gate получает capability, а текст случайно описывает это как acceptance authority.

## Проверенные подмены

| Потенциальная подмена | Риск деградации | Исправление в фрагменте |
|---|---|---|
| `passing CI` → `accepted` | CI становится суррогатом product/security/architecture judgment. | CI описан как automated gate: он блокирует или допускает следующий шаг, но не владеет смыслом изменения. |
| `gate_satisfied` → `accepted` | Durable gate в PWG превращается в финальное принятие. | Добавлено различие между `gate_satisfied`/`blocked` и `accepted`; acceptance может быть автоматическим только при явной делегации и записанном owner. |
| `PR opened` → `task done` | Reviewable artifact принимается за завершённую работу. | PR описан как candidate/evidence package, который делает работу видимой и передаёт её владельцу review. |
| `agent_reported_done` → `verified` | Последняя строка модели становится доказательством. | Финальный абзац требует diff, tests, logs, ownership zones, open questions, gate и точный статус вместо общего `done`. |
| `policy compliant` → `approved` | Соблюдение правил участия подменяет содержательное принятие изменения. | Policy cluster и Homebrew/Zig оставлены как participation/eligibility boundaries, не approval. |
| `auto-merge queued` → `agent owns merge` | Repository automation читается как власть агента. | В `/babysit-pr` добавлена формулировка: auto-merge — configured process boundary, заданный владельцами репозитория. |
| `CODEOWNERS approved` → `architecture accepted` | Path ownership поглощает архитектурную власть. | CODEOWNERS оставлен lower-level owner-review gate; отдельные ADR/security/product gates сохраняются. |

## Дублирование

- Фрагмент по-прежнему пересекается с будущими узлами про пакет доказательств и human review, но теперь формулирует собственную функцию: разделить права действия и права принятия.
- Stripe/Jökull/Mike/Zig не пересказываются как истории. Каждый якорь работает на одну границу: PR-артефакт, сопровождение PR, локальное sandbox-действие, границу участия.
- Повтор «agent does not own acceptance» оставлен намеренно в ключевых местах, но технические примеры разведены по разным типам gates.

## Что не добавлялось

- На ранних редакционных проходах новые внешние источники не добавлялись.
- Не вводилась полная taxonomy governance policies.
- Не добавлялись отдельные Zig PR-инциденты: это усилило бы case retelling, но не authority laundering pass.


## Alignment pass: несущий фрагмент общей теории

- Основной текст переписан как один продолжающийся аргумент: право действия → автоматический gate → владение/принятие → модель состояния PWG.
- Story anchors сохранены, но не развёрнуты в пересказ: Stripe отвечает за артефакт для ревью, Jökull — за сопровождение PR, Mike/Homebrew — за локальную способность действовать и ответственность перед публикацией, Zig — за границу участия.
- Policy material сжат до функции: показать, что соблюдение правил участия не равно approval.
- Детальные схемы и таблицы вынесены в `A8_figure_candidates.md`; основной текст больше не выглядит как список будущих глав.
- Новые источники не добавлялись; ссылки сохранены там, где они поддерживают конкретные statements.


## Language protocol pass

- Убран лишний английский связующий слой в основном фрагменте: `capability grants` заменено на права на действие, `acceptance grants` — на права принятия, `evidence package` — на пакет доказательств, `reviewable artifact` — на артефакт для ревью.
- Сохранены точные технические имена, команды, статусы, имена файлов, названия источников и URL: CODEOWNERS, ADR, PR, CI, `bd gate`, `sv claude`, `codex review --base main`, `may_*` states.
- URL и anchors не русифицировались.
- Аргумент не менялся; правка была языковой.


## Second language protocol pass

- Исправлены остаточные гибриды: `owners` → владельцы там, где это не имя механизма; `ownership` → контур владения/правило владения; `policy` → политика; `reviewer` → ревьюер; `comments` → комментарии.
- Сохранены точные термины, где перевод стирал бы различие или ломал ссылку на источник: CODEOWNERS, code owner, ADR, PR, CI, gate, merge, auto-merge, prompt, `AI-assisted/generated`, команды и статусы.
- Уточнены места, где русификация могла стереть различие: `provenance` оставлен с пояснением как происхождение вклада; `disclosure` и `responsibility` пояснены как раскрытие использования инструмента и ответственность.


## Style pass 1

- Основной фрагмент переписан без изменения аргумента: уменьшена summary-интонация, убраны несколько бюрократических связок и мета-комментариев.
- Фактура и ссылки сохранены; кейсы не развёрнуты в пересказ.
- Различения `действие / gate / принятие` сохранены и местами сделаны жёстче.
- Новые источники не добавлялись.


## Style pass 2

- Основной фрагмент проверен как самостоятельный узел теории: переходы усилены между repository governance, ADR/CI, агентными платформами, локальной изоляцией, open-source participation boundary и PWG.
- Истории оставлены как якоря, а не как мини-досье; ограничения по каждой истории уточнены в `A8_story_anchor_map.md`.
- `A8_figure_candidates.md` приведён в порядок: исправлена нумерация, добавлена проверка, какие схемы поддержаны текстом и какие лучше держать в техническом атласе.
- Новые источники и новые факты не добавлялись.

## Source/provenance repair pass

- Исправлена источниковая опора FastAPI: старая ссылка на `fastapi.tiangolo.com/contributing/#automated-code-and-ai` больше не используется в A8; рабочая ссылка перенесена на `https://tiangolo.com/open-source/contributing/#automated-code-and-ai`.
- QEMU переклассифицирован: это не мягкая provenance-policy, а жёсткая DCO/provenance boundary, где contributions believed to include or derive from AI-generated content отклоняются.
- Stripe сжат до source-backed функции PR-кандидата и human review. Детали devbox/Toolshed/rules не вынесены в основной аргумент, чтобы не ссылаться на внутреннее досье или непроверенный пересказ вместо первичного текста.
- Ссылка Beads `bd gate` выровнена без trailing slash: `https://gastownhall.github.io/beads/cli-reference/gate`.
- В story map, figure candidates и open questions убрана формулировка, будто Linux/QEMU/LLVM/FastAPI образуют просто «мягкий» policy spectrum; теперь кластер описывает разные boundary-механизмы: DCO/provenance, disclosure, human responsibility, human-in-the-loop и maintainer load.

## Residual composition/style pass

- Основной фрагмент не переписывался заново: исправлены только остаточные шероховатости в переходах Stripe → Jökull → Sandvault → policy cluster → PWG.
- Убраны несколько слабых или разговорных формулировок: «неинтересно спорить», «хорошее право на действие», «спорное суждение остаётся gate». Они заменены на более точные композиционные фразы.
- В figure candidates русифицированы подписи, которые не являются командами, статусами или именами источников; технические labels оставлены там, где они работают как короткие элементы схемы.
- В open questions сохранены реальные нерешённые вопросы, но они меньше похожи на оглавление будущих глав.
- Новые источники не добавлялись; предыдущий source/provenance repair-pass оставлен источниковой основой.

## Composition / visual / style repair 2026-06-11

- Основной A8 прошёл повторный repair против текущих правил visual-assets-and-figures и fragment-defect-analysis-and-repair.
- Inline-фигуры сокращены с 11 до 5: оставлены только центральная граница действия/принятия, PR-кандидат, локальный Sandvault/worktrees asset, policy-boundary summary и PWG acceptance state machine.
- Детальные схемы CODEOWNERS, ADR adoption, `/babysit-pr`, Homebrew, Zig и authority-signal anti-patterns сняты с inline и перенесены в `A8_figure_candidates.md` как merged/deferred/technical-atlas material.
- Реальный локальный asset `content/assets/theory-images/mike-superset-worktrees.png` сохранён как `<img>`, но публичная подпись очищена от recovery-служебности и локального file-path narration.
- Термин `authority laundering` не используется в основном тексте: центральный дефект описан обычной русской формулировкой — технический сигнал начинает выглядеть как решение о принятии.
- Английские labels в оставшихся synthetic figures сокращены до точных статусов/команд (`may_*`, `PR`, `accepted`, `rejected`, `superseded`, `needs_changes`) там, где они работают как элементы модели, а не как английский связующий текст.
- A8 по-прежнему пересекается с A7/PWG/B2, но теперь держит собственную функцию: право действия, право принятия и статус принятия в рабочем графе.
