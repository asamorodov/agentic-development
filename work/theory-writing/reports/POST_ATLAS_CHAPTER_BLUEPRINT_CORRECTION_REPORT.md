# Correction report — global routing vs per-chapter writing blueprint

Дата: 2026-06-13.

## Что исправлено

Предыдущий proposal `POST_ATLAS_CHAPTER_TARGET_PLAN_BLUEPRINT_PROPOSAL.md` смешивал два уровня:

1. общий corpus routing / preparation layer;
2. per-chapter writing package.

Из-за этого chapter blueprint стал слишком тяжёлым и заставлял каждую главу заново выполнять работу, которую можно сделать один раз для всех глав: Atlas routing, A/B/C fragment routing, dossier map, story map, visual map and external discovery profiles.

Теперь разделено два документа:

- `POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md` — подготовительный слой для всех будущих глав;
- `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` — blueprint для target plan одной главы, который использует уже готовые routing maps.

## Решение по общему слою

Общий слой нужен не внутри per-chapter blueprint, а для подготовки отдельных планов глав. Он должен быть выполнен отдельным target-group package / отдельным рабочим запуском, а не как обычная ad hoc задача в текущем чате, потому что его outputs станут базовыми входами для всех следующих chapter plans.

## Решение по discovery

External discovery больше не представлен как пустые обязательные P07–P08 для каждой главы. Вместо этого общий routing layer присваивает главе discovery profile:

- `D0` — no discovery;
- `D1` — provenance/restoration;
- `D2` — content discovery;
- `D3` — two-hop discovery.

Per-chapter plan добавляет discovery module только если профиль этого требует. Если discovery не нужен, в план не вставляются короткие подтверждающие проходы.

## Решение по языку и стилю

Per-chapter blueprint сохраняет принятый Atlas tail:

```text
language pass 1
language pass 2
general editorial repair 1–3
chapter entry / public structure / sequence pass
companion sync
style defect audit
selective natural rewrite
guarded final human technical style
final regression
```

Новые chapter-specific style rules не добавляются. Используются обычные принятые правила: `russian-language.md`, `language-style-rules.md`, `human-technical-style.md`.

## Статус

Это correction proposal. Планы глав ещё не создавались. Главы не писались. Следующий логичный шаг: создать `GLOBAL_CORPUS_ROUTING` target-group plan/package, выполнить его, затем использовать полученные routing maps для изготовления первого pilot chapter target plan.
