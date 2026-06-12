# Stage 0.29 — SDK backend and subagents test prompt

Дата: 2026-06-08  
Статус: добавлен launch-prompt для проверки всей схемы SDK backend + native subagents.

## Что уже известно

- Nested `codex exec` внутри Codex-task не работает: `Access is denied` / `spawn EPERM`.
- SDK probe прошёл only with escalation:
  - без escalation: API request to `/v1/responses` disconnected;
  - с escalation: child SDK-thread created `SDK_PROBE.md`.

## Что нужно проверить теперь

Нужно проверить всю целевую цепочку:

```text
controller prompt
→ native subagent per debug document
→ TS-loop
→ --backend sdk
→ child SDK-thread per pass
→ DEBUG_SOURCE_ACCUMULATION_PROMPT
→ pass artifacts
→ should_stop после min_pass
```

## Добавленный prompt

```text
work/prompts/RUN_SDK_SUBAGENTS_TEST_PROMPT.md
```

Он запускает уже существующий:

```text
work/prompts/TEST_SOURCE_ACCUMULATION_CONTROLLER_PROMPT.md
```

но жёстко фиксирует условия:

- только debug documents;
- только `--backend sdk`;
- network/escalated access required;
- native subagents must be used if available;
- no fallback to nested CLI;
- no real dossiers.

## Discourse

`work/discourse.md` включён в delta as full replacement by user permission.
