# Отчёт: терминологический и анти-кальковый repair-pass

Дата: 2026-06-10. База: пользовательский baseline `git(8).zip`.

Проход выполнял ровно узкую задачу: убрать механические остатки русификации и выровнять самые заметные терминологические зоны в 10 активных досье и 3 новых историях. Это не source accumulation, не теоретическое расширение и не стилевой rewrite.

## Шаг 1. Очередь

Создан файл:

```text
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md
```

Он фиксирует решения по `SDLC с ИИ`, `ИИ-агент`, `промпт`, `файл промпта`, `модульные тесты`, `gate`, `workflow`, `source claim`, `citation audit`, `synthesis pass` и другим спорным зонам.

## Шаг 2. Repair-pass по 13 документам

Затронуты все документы области:

| Документ | Масштаб правки |
|---|---:|
| `work/dossiers/ADR_METHOD_DOSSIER.md` | 24 строки |
| `work/dossiers/BMAD_METHOD_DOSSIER.md` | 9 строк |
| `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | 4 строки |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | 16 строк |
| `work/dossiers/GSD_METHOD_DOSSIER.md` | 1 строка |
| `work/dossiers/KIRO_SPECS_DOSSIER.md` | 9 строк |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | 5 строк |
| `work/dossiers/SPDD_METHOD_DOSSIER.md` | 89 строк |
| `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | 4 строки |
| `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | 10 строк |
| `content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md` | 23 строки |
| `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` | 1 строка |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | 4 строки |

Основные типы правок:

- `AI-driven SDLC` → `SDLC с ИИ` в авторском тексте;
- `AI-агент` / `AI-система` → `ИИ-агент` / `ИИ-система`;
- `prompt-файл` и похожие гибриды → `файл промпта`, `файлы промптов`;
- `Unit tests` / `unit-тесты` в авторском тексте → `модульные тесты`;
- `источникный срез` → `срез источников`;
- `source claim`, `citation audit`, `synthesis pass`, `read snapshot` в PWG-зонах → русские технические формулы;
- явные кальки вида `шлюзs`, `Задачи-gate`, `ИИ-native graph`, `бизнес-prompt`, `трассируемость-risk`, `область-gate` исправлены.

## Шаг 3. Отдельный sanity-pass по SPDD

SPDD получил отдельную проверку, потому что ранее был помечен как документ с возможной ручной проверкой после encoding-glitch. В текущем проходе:

- явных mojibake/encoding-глюков в финальном тексте не найдено;
- раздел про `Unit tests` приведён к `Модульные тесты`;
- восстановлен локальный anchor `#spdd-unit-tests-after-stabilization`, чтобы ссылка снова указывала на существующий раздел корпуса;
- устранены грубые гибриды вокруг `prompt`, `API-test`, `source-pass`, `business-prompt` и figure IDs;
- проверено, что Markdown links и raw URL не изменились.

Подробный отчёт: `work/reports/SPDD_LANGUAGE_SANITY_PASS_REPORT.md`.

## Шаг 4. Лёгкий редакторский проход по историям 13–15

Истории не переписывались заново. Исправлены только механические языковые хвосты:

- Armin: `prompt-файлы` → `файлы промптов`, уточнены несколько форм про gate-механизм и внешний вход;
- Stripe: исправлена формула про входную контрольную точку;
- Shopify: `промпт-файлы` и alt/caption вокруг YAML/промпт-примеров приведены к нормальному русскому виду.

Подробный отчёт: `work/reports/STORIES_13_15_LANGUAGE_EDITORIAL_PASS_REPORT.md`.

## Проверки

Проверено скриптом:

```text
raw URLs: unchanged for all 13 docs
markdown link targets: unchanged except deliberate SPDD local-link repair
known bad patterns: removed
```

Остаточные английские слова остаются там, где это имена файлов, команд, исходных терминов, названия источников, GitHub-объекты, code-like context или устойчивые термины вроде `workflow-as-code`, `prompt-as-code`, `spec-as-source`, `issue`, `PR`, `MCP`.

## Остаточные риски

- Это не финальный стилевой проход. В досье всё ещё много рабочих меток и английских source titles, что нормально для quarry-материала.
- Некоторые термины вроде `gate`, `issue`, `workflow`, `prompt` сознательно не вычищались полностью, чтобы не потерять связь с источниками и артефактами.
- Перед публикацией теории нужен отдельный композиционный и стилевой pass, а не повторение этого repair-pass.
