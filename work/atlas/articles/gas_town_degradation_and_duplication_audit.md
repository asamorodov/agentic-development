# gas_town — degradation and duplication audit

Статус после Final: аудит синхронизирован с текущей статьёй. Старые pass-specific долги удалены; ниже оставлены только актуальные риски деградации и готовности.

## Контрольный вопрос статьи

Текущий H1: `Gas Town: какие организационные механизмы нужны, когда агентная работа выходит за пределы одного чата, одного рабочего дерева и ручного наблюдения?`

Статья должна отвечать именно на этот вопрос. Gas Town рассматривается как организационная среда вокруг долговечного рабочего состояния, а не как продуктовый tutorial, role glossary, generic multi-agent hype или самостоятельная теория PWG.

## Current structure check

| Article area | Current role | Audit status |
|---|---|---|
| Вступление + «Почему одного чата становится мало» | даёт практическую проблему масштаба до таксономии | После P22 вход стал публично читаемым. |
| «Линия давления» + synthetic figure | показывает pressure → mechanism sequence | Сохранять; не превращать в список возможностей. |
| Contract/minimal frame | разводит Beads, PWG и Gas Town | Полезно после P22, но можно слегка сжать в финальном стиле, если вход кажется длинным. |
| Beads lower layer | даёт технический substrate | Не расширять в Beads manual. |
| Town/rig, roles, delivery, decomposition | объясняет организационную механику Gas Town | Риск role glossary контролируется functional/cost framing. |
| Queue/backpressure/observability/recovery/service work/infrastructure | главные technical anchors | Плотно, но фактура нужна; группировать только без source loss. |
| Failure modes / unresolved gaps | удерживает критическую границу | Полезно: не даёт статье стать рекламой Gas Town. |
| Small-process transfer / theory links | показывает переносимые функции и связь с атласом | После P21/P22 больше не зависит от internal `A10` label. |

## Актуальные риски деградации

| Risk | Current status | What to do |
|---|---|---|
| Beads/PWG duplicate | Низкий/средний: Beads секции технически плотные, но связаны с Gas Town. | Не добавлять новые Beads commands unless they support fleet organization. |
| Role glossary | Низкий: роли объяснены через lifecycle functions and costs. | Не добавлять новые роли ради полноты; если Worker Roles image перегружает текст, заменить synthetic map. |
| Generic multi-agent hype | Низкий: вступление и failure modes подчёркивают цену, хаос и человеческое узкое место. | Сохранять критические границы. |
| Implementation checklist | Низкий после P21: small-process transfer привязан к сбоям. | Не превращать финальный раздел в план внедрения. |
| Ledger-summary in article body | Решено P20: asset queue removed. | Держать companion metadata вне основного текста. |
| Source freshness | Средний: CHANGELOG/scheduler/releases/workflow details version-sensitive. | Проверить перед публикацией. |
| Visual readiness | Высокий: два inline external placeholders без локальных файлов. | Asset/rights/render pass required. |
| List density | Средний: commands/statuses make sections dense. | Финальная группировка допустима только без потери technical anchors. |

## Source loss check after P23 / still valid after Final

- Не удалены load-bearing источники из статьи.
- Не удалены technical anchors: `bd ready`, `claim`, `dep`, `prime`, gates, Formula/Molecule/Wisp, `gt sling`, mail statuses, scheduler/backpressure, Dashboard/telemetry, troubleshooting/debug/sandbox/sync risks, operation-log gap.
- Удалённые/сжатые companion histories не являются source loss: они были workflow logs, а не статья.

## Image audit after P23 / updated by Final

| Figure id | Current status | Risk |
|---|---|---|
| `fig-gastown-pressure-to-mechanism-stack` | local synthetic SVG | Check render only. |
| `fig-beads-task-graph-memory` | local SVG | Keep caption boundary: lower memory, not full Gas Town. |
| `fig-gastown-architecture` | local SVG | May overlap visually with external Two-Tier Beads Flow. |
| `fig-gastown-two-tier-beads-flow` | external placeholder | Publication blocker until asset/rights/quality resolved. |
| `fig-gastown-worker-roles` | external placeholder | Publication blocker; can over-reinforce role glossary if visually busy. |
| `fig-gastown-basic-workflow` | local SVG | Ready if path renders. |
| `fig-gastown-mayor-hub` | local WebP | Ready if path renders and asset rights are acceptable. |

## Readiness status after P23 / superseded by Final status

Editorial readiness: close, but not final. The article now has a public H1, corrected entry sequence, no executor asset queue in the body, strong technical support and explicit boundaries.

Publication readiness: not ready until the two external image placeholders are resolved and version-sensitive source details receive a final freshness check.

## P24 style audit

Стилевой проход не переписывал статью целиком и не удалял фактуру. Исправлены только реальные дефекты формы:

- `организационная механика` во вступлении заменена на более прямое `организационное устройство`;
- формулы про `насыщение` и `цепь насыщений` заменены на обычное объяснение, что следующий механизм появляется там, где предыдущего уже не хватает;
- заголовок decomposition section теперь говорит о снятии неявности из поручения, а не держит лишнее противопоставление `не больше промптов, а меньше неявности`;
- фраза про роли как `театр` заменена на прямое объяснение: роли перестают помогать, когда становятся только названиями;
- `газтауновская механика` заменена на `механика Gas Town`;
- несколько абстрактных формул вроде `карта будущих примитивов` заменены на обычные рабочие формулировки.

Source loss не обнаружен: правки не меняют источники, роли, изображения, тезисы или фактические утверждения. Compact technical phrases, которые звучат нормально и несут точный смысл (`контрольный барьер`, `обратное давление`, `рабочий объект`, `граф работы`), оставлены без механического разворачивания.

## P25 selective natural rewrite

P25 исправил оставшиеся точечные дефекты публичного звучания без переписывания статьи:

- внутреннее слово `досье` удалено из основного текста;
- `флотская работа` заменена на нормальное `работа флота`;
- формулы `для статьи важно` в технических местах заменены на прямое объяснение рабочей границы;
- диагностический абзац про `BD_DEBUG*` переписан без псевдотермина `организационное слепое пятно`;
- caption Two-Tier Beads Flow теперь говорит о слоях состояния, а не о менее естественных `плоскостях состояния`.

Факты, команды, source labels, изображения и границы не изменились.

## P26 guarded final style pass

P26 сделал финальную точечную вычитку формы без изменения фактуры:

- смягчены самоссылки вида `в этой статье` там, где они звучали как служебный каркас, а не публичное объяснение;
- оставшийся публичный маркер `досье` заменён на нейтральное `материалы`;
- декоративная метафора `маленький участок города` заменена на прямую формулировку про одну или две переносимые функции;
- несколько противопоставлений и формул переписаны более естественно, без потери команд, ролей, источников, ограничений и статусов.

Факты, изображения, источники, роли и границы статьи не менялись. Публикационные блокеры остаются прежними: external image placeholders and freshness checks.

## Final package-readiness audit

Final check restored the required bottom mirror section `Внешние изображения для asset-pass` for the two inline external-real candidates, while keeping detailed asset work in `gas_town_external_image_queue.md`. This is a packaging/readiness requirement, not a new source claim.

Package-level checks: required article and companion files exist and are non-empty; source usage and transfer ledger are populated; local image paths exist for all `<img>` figures; two external-real figures remain placeholders by design; synthetic figure count stays limited to one nontrivial pressure-to-mechanism diagram; controlled repetition with theory remains justified by the final reverse-link table.

Article risk status: not a role glossary, not a Beads/PWG duplicate, not generic multi-agent hype, not implementation plan, and not a pile of technical details without concept. Publication blockers remain external image rights/localization and freshness checks for version-sensitive sources.
