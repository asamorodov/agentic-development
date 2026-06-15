# Chapter II and III target plans — creation report

Статус: планы созданы, главы и executor packages не запускались.

## Что создано

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
```

## Принципы

Планы не копируют механически план главы I. Они используют тот же общий формат per-chapter planning, но отражают собственные риски глав.

Глава II получает профиль `D2`: внутренние истории сильны, но без внешних источников глава рискует стать набором story anchors. В план добавлен bounded discovery по session trace, observation, intervention and agent failure / transcript analysis.

Глава III тоже получает профиль `D2`: Атлас и A2/A3/B1/C1 дают основу, но для публичной главы нужны первичные источники и внешняя калибровка вокруг ADR, Confirmation, architecture fitness, generated ADR and authority boundary.

## Что не делалось

- главы не писались;
- пакеты не собирались;
- внешний поиск не запускался;
- Skeleton, routing maps, global blueprint and package protocols не менялись.

## Проверка

- оба плана содержат target files, read-only inputs, очередь проходов and readiness criteria;
- оба плана включают обычный языко-стилевой хвост;
- оба плана имеют discovery module because routing profile is `D2`;
- планы не используют старый заголовок `Вопрос читателя` and route that decision into entry/sequence pass;
- prompts written in Russian except source-native terms, file paths and exact method names.
