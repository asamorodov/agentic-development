
# Post-Atlas external source discovery map

Статус: профили внешнего поиска для будущих chapter packages.  
В этом package внешний поиск не выполнялся.

| Глава | Профиль | Почему | Seed terms / sources | Риск без discovery |
| --- | --- | --- | --- | --- |
| INTRO | D0 | Внутреннего корпуса достаточно; можно восстановить 1–2 источника только при финальной публикации. | нет массового поиска | Пустое вступление без technical anchors. |
| I | D1 | Нужно только при уточнении терминов task/change/workflow. | software change lifecycle, task vs change, programming by chat | Слишком внутренняя терминология. |
| II | D2 | Trace/session/failure материал может потребовать внешних источников как содержания. | SWE-chat; Programming by Chat; How Coding Agents Fail; agent trace analysis | Глава останется набором историй. |
| III | D2 | ADR/contract/architecture confirmation claims требуют первичных sources and broader practice. | Nygard ADR; Fowler ADR; MADR; architecture fitness functions; generated ADR research; CODEOWNERS | ADR станет частной методикой, а не decision-memory layer. |
| IV | D1 | SPDD в основном закрыт Атласом; нужно восстановить Fowler/Thoughtworks/OpenSPDD sources. | Fowler SPDD; OpenSPDD; REASONS Canvas | Потеря provenance and concrete examples. |
| V | D2 | Spec Kit/Kiro/CSDD/TDAD зависят от official docs, repos and changing product behavior. | Spec Kit docs/repo; Kiro docs/blog; CSDD paper/repo; TDAD arXiv papers | Профили станут устаревшим пересказом. |
| VI | D2 | Project context as interface требует sources around rules/skills/hooks/MCP/project memory. | Claude/Codex project rules; AGENTS.md; skills; MCP; context engineering; project memory | Глава сольётся с общим context talk. |
| VII | D1 | PWG mostly internal/Atlas; точечно восстановить Beads/PWG references and adjacent issue-state sources. | Beads; GitHub sub-issues; Linear blocked relations; Dolt; durable work state | Недостаточная проверка границ against trackers. |
| VIII | D2 | GSD/BMAD mostly Atlas, но соседние process profiles may need current docs. | GSD/Open GSD docs; BMAD docs; Reversa/OpenSpec/AgentSPEX if needed | Process profiles будут выглядеть закрытым списком. |
| IX | D3 | Execution/harness/runtime layer недособран внутренними sources and changes quickly. | LangGraph; Temporal; DBOS; Restate; HumanLayer; Sandvault; Codex/Claude docs; MCP/hooks/subagents | Глава станет tool list or stale runtime summary. |
| X | D1 | Gas Town source is mainly Yegge/Gas Town; нужно source restoration and image verification. | Gas Town/Beads original docs; Yegge material; local Gas Town assets | Термины будут оторваны от source-level meaning. |
| XI | D3 | Evidence types need outside material beyond Atlas. | contract testing; Pact/can-i-deploy; architecture fitness; rollout/SLO/error budgets; traces/replay; review evidence | Evidence сведётся к тестам и CI. |
| XII | D3 | Authority/governance requires current policies and maintainership practices. | CODEOWNERS; maintainer AI policies; open-source AI restrictions; enterprise sandbox/security policy; protected branches | Глава станет общим утверждением про людей без source anchors. |
| XIII | D2 | Lifecycle tail needs selected maintenance/security/supply-chain sources. | incident feedback; SBOM; dependency inventory; policy-as-code; prompt/context lifecycle; skills/rules updates | Хвост станет абстрактным post-merge reminder. |
| CONCLUSION | D0 | Новые sources не нужны; использовать уже собранные maps. | нет | Заключение раздутым внешним обзором. |
| APPENDIX | D0 | Reference layer по Атласу. | нет | Не применимо. |

## Правило для будущих package plans

- `D0`: не добавлять discovery-pass ради симметрии.
- `D1`: добавить короткий source-restoration module, если claim или image реально используется.
- `D2`: сделать bounded discovery по content gaps главы.
- `D3`: сделать discovery + unfolding: читать найденные sources, идти по важным ссылкам, diagrams, repos, authors and competing terms, затем принимать integration decision.

Если раскрытия источников находит новую крупную линию, она не входит в главу автоматически. Решение фиксируется как `integrate now`, `source register`, `future debt` или `separate appendix/Handbook/Fieldbook`.
