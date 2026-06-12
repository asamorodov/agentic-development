# Story dossier loop patch report

Статус: добавлен prompt-only режим накопления досье для шести кандидатных историй.

## Добавлено

```text
work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
work/prompts/RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION.md
work/automation/run-story-dossier-loop.cmd
work/reports/STORY_DOSSIER_LOOP_PATCH_REPORT.md
work/reports/STORY_DOSSIER_LOOP_PATCH_VALIDATION.md
```

Также обновлён:

```text
work/automation/README.md
```

## Что не менялось

TS-ядро многопроходного документного процесса не изменялось:

```text
work/automation/src/run-source-loop.ts
work/automation/src/args.ts
work/automation/src/prompt-renderer.ts
```

Новый режим задаётся только wrapper-ом and prompt-ами.

## Целевые истории

```text
Shopify Roast
Product Migration with Claude Code
Quix / Klaus Kode
Armin Ronacher
Zig no-AI policy
Stripe Minions
```

Целевой каталог:

```text
work/story_dossiers/
```

## Параметры

```text
min_pass = 10
max_pass = 20
mode = fresh
fresh_action = stub
backend = sdk
```

## Назначение нижнего prompt-а

Prompt ориентирован на историю, а не на методологию. Он ищет контекст, повороты, артефакты, трение, изменение взгляда, угловатую фактуру, источники and кандидатов на иллюстрации. Он запрещает автоматическую раскладку по theory / Handbook / Fieldbook.

## Follow-up correction: anti-anchoring

Нижний prompt исправлен: ранние проходы теперь не должны заранее фиксировать главный смысл истории. Worker должен держать несколько конкурирующих углов, проверять их источниками, сохранять контрфакты и не писать готовую историю до поздних проходов. Это снижает риск, что досье станет подтверждением первой удобной рамки.
