# kiro_specs — open questions

Статус: `P26_guarded_final_style_current`. Этот файл хранит только настоящие blockers и freshness/source debts текущей статьи. Служебные долги прошлых проходов — общий долг по C5/A10, проверка первых synthetic figures и решение о problem-first opening — закрыты.

## Open for source-depth / freshness / asset-pass

1. **Текущий статус Kiro Web Specs.** Статья осторожно описывает Web Preview как autonomous PR-cycle рядом с roadmap переноса Specs в Web. Перед публикацией нужно проверить свежую документацию: есть ли уже полноценный Web workflow с `requirements.md`, `design.md`, `tasks.md`, approvals/checkpoints and execution semantics comparable to IDE Specs.
2. **CLI and Feature Specs parity.** Статья утверждает только shared `.kiro` context / steering / MCP / automation surfaces. Нужно проверить, появился ли официальный CLI workflow для создания, запуска и синхронизации Feature Specs с теми же approvals and Sync Files, что в IDE.
3. **Task status persistence.** Видимые статусы and home-page sequence are used as execution surface. Остаётся неизвестным, хранится ли task status directly in `tasks.md`, in IDE metadata, or derived state.
4. **Run all Tasks current documentation.** Статья опирается на blog/best-practices/faster-smarter material. Перед публикацией нужно проверить, есть ли отдельная актуальная docs page или changed constraints for package execution / mandatory tasks / failure behavior.
5. **PBT current UI/defaults.** Механизм Correctness/PBT перенесён как evidence loop, но нужно сверить current UI, optional/default behavior, and how properties are displayed/linked to requirements and tasks.
6. **Data protection, prompt logging and retention.** Governance/monitoring boundary is in the article, but detailed relation between data protection statements, prompt logging, S3/CloudTrail/CloudWatch retention and plan tier needs source-depth verification.
7. **Enterprise/CLI MCP registry limits.** Нужно подтвердить current interaction between managed registry, personal MCP servers, local overrides, version enforcement, client-side enforcement and admin-machine bypass risk.
8. **External image assets.** Для всех seven `external-real-candidate` entries нужно выполнить download/rights/quality/freshness checks. Для Subagents/Web additionally verify whether an official real visual exists; otherwise mark as not found and decide on synthetic fallback.

## Closed as article decisions by P23

- **C5/A10 synchronization.** C5 and A10 are read-only context and are already reflected in the article’s standalone concept-first frame and mode-selection criterion. No generic companion debt remains.
- **Problem-first opening.** P22 moved the practical problem into the first screen and removed the duplicate `Проблема` section.
- **Bottom asset-pass block.** It remains in the main `.md` as a clearly marked workflow block, not as reader-facing conclusion.
- **Synthetic figure usefulness after P11/P13.** Current synthetic figures are retained as mechanism explanations; no generic synthetic-figure review debt remains.
- **Public service-language cleanup.** Public mentions of internal `досье`, `черновик`, `редакторский недобор`, and service captions have been removed from the article body.
- **Spec Kit/SPDD/TDAD/Constitutional SDD/ADR/PWG boundaries.** Current article keeps these as boundaries rather than full comparisons.
## P24 open-question note

No new source or asset blockers were opened. Style-only fixes closed public wording defects; remaining questions are still Web/CLI freshness, task-status persistence, Run all Tasks docs, PBT current behavior, governance/logging details, MCP registry limits and external image asset checks.
## P25 open-question note

No new open questions. P25 only improved wording; Web/CLI freshness, task status, Run all Tasks, PBT, governance/logging, MCP registry and external-image checks remain the active blockers.

## P26 open-question note

No new open questions. P26 was style-only; Web/CLI freshness, task status, Run all Tasks, PBT, governance/logging, MCP registry and external-image checks remain the active blockers.
