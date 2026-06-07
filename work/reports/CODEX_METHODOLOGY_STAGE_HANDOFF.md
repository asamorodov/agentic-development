# Codex methodology stage handoff

Дата: 2026-06-07  
Статус: рабочая записка для перехода Stage 0.19 в Codex.

## Что создано

Добавлены:

```text
work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md
work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md
work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md
```

## Как использовать

Сначала запустить в Codex:

```text
work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md
```

Если Codex вернёт `READY` or `READY_WITH_WARNINGS` без критических missing documents, затем запускать:

```text
work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md
```

## Почему readiness check нужен

Stage 0.19 сложный: Codex должен работать не с одной главой, а с большим корпусом решений, протоколов and source expansions. До запуска методологических dossiers нужно убедиться, что Codex:

- видит документы;
- понимает ход работы;
- понимает protected methodology profiles;
- понимает, что нельзя писать главы;
- понимает human gates;
- понимает языковые правила.

## Что будет считаться хорошим результатом Stage 0.19

- все pass files созданы;
- all protected methodology dossiers created;
- comparative synthesis reports created;
- anti-shallow audit passes;
- `work/discourse.md` updated;
- `work/CHECKS.json` updated;
- no final theory chapters written.
