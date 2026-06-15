# POST_ATLAS_GLOBAL_CORPUS_ROUTING package build report

Дата: 2026-06-13.

Собран executor package:

```text
work/theory-writing/packages/POST_ATLAS_GLOBAL_CORPUS_ROUTING.zip
```

Режим: `repo-snapshot-bound`.

Пакет не содержит весь корпус источников. Он должен запускаться рядом с отдельно развёрнутым репозиторием:

```bash
python q8v4m.py --repo /path/to/repository/root
```

## Состав

- `START.md` — инструкция запуска.
- `q8v4m.py` — generic runner для последовательной выдачи рабочих листов.
- `z3k9p.dat` — opaque payload с 14 records: `G01`–`G13 + Final`.
- `TARGET_PLAN_SNAPSHOT.md` — снимок target-group plan.
- `PACKAGE_MANIFEST.json` — служебный manifest.

## Проверки

- package zip created: yes.
- package copied into repo cache: yes.
- mode explicitly repo-bound: yes.
- source corpus not bundled: yes.
- runner supports `--repo`: yes.
- first runner transition smoke-tested separately before final response: see assistant run log.

## Scope

Пакет создаёт общий routing layer для будущих chapter target plans. Он не пишет главы, не создаёт per-chapter plans, не переписывает Skeleton, Атлас, A/B/C-фрагменты and не запускает внешний поиск.
