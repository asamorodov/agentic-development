# Stage 0.6 targeted source expansion

Дата: 2026-06-07  
Режим: локальный snapshot → archive handoff overlay  
Основание: Stage 0.5 audits выявили слабые зоны, которые требуют не массового source harvest, а gap-driven проверки.

Принцип: каждый тематический поиск выполнен в три повторных “честных” этапа с разными формулировками. Это нужно, чтобы не получить только один тип источников: например, только academic papers, только docs, только vendor posts or только уже известные названия.

Темы:

1. `decision_provenance/` — ADR, RFC, design rationale, decision records.
2. `agentic_frameworks/` — GSD, BMAD, Spec Kit, OpenSpec, Reversa, Spec Kitty and adjacent process frameworks.
3. `lifecycle_tail/` — release, rollback, migration, runbook, incident/postmortem, changelog, deprecation/dependency.
4. `security_provenance/` — threat model, security review, audit log, provenance, agent action trace, SLSA, MCP/tool boundary.
5. `ownership_completion_right/` — CODEOWNERS, ownership map, review routing, completion authority.

Общий вывод: Stage 0.5 рекомендации подтверждены. Новые источники не требуют смены master architecture, но требуют plan patch before drafting.
