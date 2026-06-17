# ADR-0016 — A16, старые статьи Атласа и пересмотр входа на сайт

Дата: 2026-06-17.  
Статус: принято как рабочее решение, кроме порядка сайта — там нужен отдельный навигационный пакет.

## Контекст

После решения ADR-0012–ADR-0015 Атлас стал равноправной технической частью корпуса, а не приложением к Теории. Карта A1–A15 уже закрывает большую часть технического пространства agentic development, но остаётся ещё один полезный слой: организационный контекст разработки.

Также нужно развести старые concept-first статьи Атласа и новую layer map. Старые статьи не должны быть выброшены, но они не обязаны занимать тот же уровень, что технические слои A1–A16.

Отдельный вопрос — порядок публичного сайта. Старый сайт фактически начинался с историй, но теперь корпус уже не сводится к историям. Истории остаются важным доказательным и практическим материалом, но порядок сайта должен проектироваться как читательский маршрут, а не как история возникновения материалов.

## Решение

1. Добавить в Level 1 Атласа новую статью:

```text
A16. Организационный контекст, software catalog и developer portal
```

Эта статья покрывает Backstage/Port-like software catalog and internal developer portal layer: сервисы, ownership, зависимости, environments, runbooks, scorecards, maturity/security/compliance metadata, self-service actions, workflow automations and agent-facing organizational context.

2. Старые статьи Атласа не удаляются. Они переводятся в нижние уровни карты:

- Level 2: концептуальные механизмы и методологические режимы — SPDD, Persistent Work Graph, ADR, Kiro Specs, Spec Kit, TDAD, Constitutional SDD, BMAD/GSD where useful.
- Level 3: плотные частные формы и case profiles — Gas Town/Beads, Kiro as product-specific integrated SDD IDE case, OpenHands/SWE-agent-style harnesses where useful.
- Level 4: вспомогательные досье и source maps.

3. Kiro article не бросать. Его следует рассматривать как полезный product/method profile, который раскрывает одну интегрированную форму: specs + steering + hooks + IDE workflow + MCP integrations. Он должен связываться с A1, A2, A4, A8, A11 and A14, но не заменять слой A8 целиком.

4. Порядок сайта не менять автоматически в этом overlay. Создать отдельную заметку для будущего navigation package: сайт, возможно, больше не должен начинаться с Историй. Новый вход должен показывать четыре равноправных части и помогать читателю быстро выбрать маршрут:

- понять общую модель — Теория / будущий `Жизненный цикл программного изменения`;
- понять технологии — Атлас;
- выбрать режим работы — Рабочие сценарии;
- диагностировать сбой — Каталог проблем и решений;
- посмотреть реальные случаи — Истории.

## Последствия

- `work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md` становится картой A1–A16.
- `work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md` должен синхронизироваться с A16 там, где главы говорят об organization/platform wrapper, ownership, environments, runbooks, services and platform governance.
- Старые Атласные статьи нельзя считать ошибкой только потому, что они не совпадают с новой Level 1 layer map. Их роль меняется: они становятся concept/profile articles и источниками для layer articles.
- Site navigation / homepage / section order требует отдельного решения после product framing review. До этого старый порядок не считать окончательным.
