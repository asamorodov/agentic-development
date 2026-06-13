# Post-Atlas Source Routing Map

Статус: рабочая карта источников для будущих глав.  
Назначение: показать, какие слои источников использовать при написании глав после Атласа.

## Общий порядок

```text
Skeleton V5 / 00 / CORE plan
→ A/B/C-фрагменты
→ Atlas articles
→ досье gap-check
→ external source discovery там, где он нужен
→ primary-source provenance
→ истории как практические якоря
```

## По частям

| Часть | Первичные внутренние входы | Atlas donors | Досье / gap-check | External discovery |
|---|---|---|---|---|
| Введение / I | 00, A1, A10, Cross-story | SPDD, Spec Kit, Kiro, BMAD | общие досье только если концепт становится слишком тонким | обычно нет |
| II. Сессия / трасса | A1, A6, A7, stories | PWG, GSD, BMAD | story dossiers, PWG/GSD/BMAD dossiers | SWE-chat, Programming by Chat, coding-agent failure/trace sources |
| III. Spec / contract / ADR | A2, A3, B1, C1 | ADR, SPDD, Spec Kit, CSDD | ADR, SPDD, Spec Kit, CSDD dossiers | ADR practice, architecture fitness, decision records, governance sources |
| IV. SPDD | B1, C1 | SPDD | SPDD dossier | только для недостающих деталей Fowler/OpenSPDD |
| V. Spec profiles | A3 | Spec Kit, Kiro, TDAD, CSDD | corresponding dossiers | official docs/repos for current behavior |
| VI. Context as interface | A6, C4 | Kiro, GSD, BMAD, Spec Kit, PWG | method dossiers | Codex/Claude/skills/hooks/MCP/project-rule docs |
| VII. PWG | A4, B2, C2, C3, C4 | PWG, Gas Town | PWG, Gas Town dossiers | обычно ограниченно; только для соседних механизмов |
| VIII. Process profiles | A5, B3, C2 | GSD, BMAD, Gas Town | GSD/BMAD/Gas Town dossiers | Reversa/OpenSpec/AgentSPEX только если нужны |
| IX. Execution | A6, C4, stories | PWG, Gas Town, GSD, BMAD | story/method dossiers | LangGraph, Temporal, DBOS, Restate, HumanLayer, Sandvault, Codex/Claude docs |
| X. Gas Town | B3, C2, C4 | Gas Town, PWG | Gas Town dossier | limited; source is mainly Yegge/Gas Town docs |
| XI. Evidence | A7, C3, A2 | SPDD, ADR, TDAD, CSDD, Kiro, GSD, BMAD | corresponding dossiers | contract testing, architecture fitness, rollout/SLO, replay/trace sources |
| XII. Completion / authority | A8, A2, C3 | ADR, CSDD, GSD, BMAD, PWG | ADR/CSDD/story dossiers | CODEOWNERS, maintainer policy, open-source AI policies, security/governance |
| XIII. Lifecycle tail | A9, C1–C4 | SPDD, ADR, CSDD, Spec Kit, Kiro, GSD, BMAD, PWG | all relevant dossiers | incident feedback, dependency inventory, SBOM, policy/rule/skill updates |
| Заключение | A10, все A/B/C | весь Атлас | все досье только как проверка | минимально |

## Usage rule

Chapter package не должен читать эту таблицу как coverage-бюрократию. Это routing map. Что именно нужно главе, решают `section contract`, `dossier gap map` и `content gap map`.
