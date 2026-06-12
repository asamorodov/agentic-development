# Очередь терминологического и анти-калькового repair-pass

Основание: после общего языкового цикла в `git(8).zip` документы уже читаются по-русски, но в них остались хвосты механической русификации, гибридные формы и неодинаковый перевод повторяющихся терминов. Этот файл фиксирует, что именно правилось в узком repair-pass. Это не source accumulation и не стилевой rewrite.

## Область прохода

Обрабатывались 13 документов:

```text
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

## Терминологические решения

| Зона | Решение |
|---|---|
| `AI-driven SDLC` | В обычном русском объяснительном тексте использовать `SDLC с ИИ`. Английскую форму оставлять только в названиях источников или там, где она нужна как цитируемая формула. |
| `AI-agent`, `AI-система` | В русском авторском тексте использовать `ИИ-агент`, `ИИ-система`. |
| `prompt` | В обычном тексте использовать `промпт`. Пути, имена файлов вроде `prompt.md`, названия команд и устойчивые source terms не переводить. |
| `prompt-файл` | Исправлять на `файл промпта` / `файлы промптов`, чтобы не оставлять грубую гибридную форму. |
| `unit tests` | В обычном тексте использовать `модульные тесты`. URL-anchors не менять. |
| `source-pass`, `chat source-pass` | Использовать `проход по источникам` / `срез источников из чат-прохода`. |
| `source claim`, `citation audit`, `synthesis pass` | Для PWG использовать `заявка на источник`, `аудит цитирования`, `синтезирующий проход`. Английские имена оставлять только в source titles или code-like context. |
| `gate` | Не переводить механически как `шлюз` там, где речь о проверочной точке процесса. Использовать `контрольная точка`, `gate-механизм` или оставить `gate`, если это имя команды/объекта источника. `шлюз` сохранять для API/network gateway. |
| `workflow` | Не делать массовую замену. В обычном тексте уже чаще используется `рабочий процесс`; английскую форму сохранять в названиях источников, файлах `workflow.yml`, GitHub Actions workflows и устойчивых формулировках вроде `workflow-as-code`. |
| `review` | Не заменять механически. `ревью` допустимо как русский технический термин. Явные кальки вроде `review path` исправлять. |
| `issue` | Сохранять как GitHub-термин, если речь именно об issue. Не подменять все вхождения на `задача`, чтобы не потерять связь с источниками. |
| `baseline` | В обычном теоретическом тексте предпочитать `базовый снимок`; в именах файлов и рабочих status/report-файлах можно оставлять `baseline`. |
| `deep case`, `deep anchor` | В будущей теории использовать `глубокий опорный случай` / `глубокий опорный узел`. В этом repair-pass массовая замена не делалась, потому что в текущих документах такие формы чаще появляются как рабочие метки. |

## Анти-кальковая очередь

В проходе искались и исправлялись явные поломки:

```text
шлюзs
тестs
Задачи-gate
ИИ-native graph
бизнес-prompt
трассируемость-risk
область-gate
источникный срез
prompt-файл / prompt-файлы / prompt-файлов
Unit tests в обычном тексте
source state / source claim / citation audit / synthesis pass в обычном русском тексте
```

Отдельно проверялись грубые формы, обнаруженные при оценке Pro-результата:

```text
open источник
ревью path
ревью debt
рабочий процессs
набор файл запросаов
```

В текущем `git(8).zip` часть этих форм уже отсутствовала; очередь всё равно сохранена как контрольный список для будущих языковых проходов.

## Что не делалось

- Не переписывались досье заново.
- Не менялись источники и внешние ссылки.
- Не проводился новый поиск источников.
- Не делался полноценный стилевой проход.
- Не переводились имена файлов, команд, API, URL, source titles и code-like fragments.


## Дополнительная проверка ссылочных целей

Отдельно проверялись Markdown link destinations, которые могли быть испорчены предыдущей русификацией. В SPDD-досье восстановлены calqued targets для истории Jesse Vincent и anchors `#spdd-six-step-workflow`, `#spdd-unit-tests-after-stabilization`. Это не изменение внешних источников, а repair уже существующих локальных ссылок на реальные файлы и anchors корпуса.
