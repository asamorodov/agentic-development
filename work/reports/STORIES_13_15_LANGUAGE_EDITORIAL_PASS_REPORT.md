# Лёгкий редакторский проход по историям 13–15

Дата: 2026-06-10. Документы:

```text
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

Проход был ограниченным: не переписывать истории заново, не менять источники, не менять структуру и не превращать это в стилевую редактуру. Цель — убрать механические языковые хвосты после русификации.

## Armin Ronacher / Pi

Исправлены гибриды `prompt-файл`, `prompt-файлы`, `prompt-файлов` на `файл промпта`, `файлы промптов`, `файлов промптов`. Уточнены несколько фраз про gate-механизм и внешний вход, чтобы не оставлять буквальный `шлюз` там, где речь о contribution policy / issue-gate / pr-gate.

Оставлены без перевода:

- `issue-gate.yml`, `pr-gate.yml`, `APPROVED_CONTRIBUTORS`;
- имена URL, issue/PR labels, команды и code-like fragments;
- `Prompt injection` как устойчивый термин атаки.

## Stripe Minions

Исправлена формула про `входной шлюз`: в этой сцене Stripe автоматизирует не физический шлюз, а входную контрольную точку маршрутизации рабочего запроса.

Остальной текст не переписывался, потому что текущая история уже достаточно связная и главная проблема была не в стиле, а в точечной терминологии.

## Shopify Roast

Исправлены `промпт-файлы` и подпись/alt вокруг YAML/промпт-примеров. Сохранены `workflow.yml`, `workflow.output`, source titles вроде “Executing Structured A.I. Workflows with Shopify Roast”, потому что это точные имена файлов, API-полей или названия источников.

## Проверки

Markdown link targets и raw URLs в трёх историях сохранены без изменений относительно `git(8).zip`.
