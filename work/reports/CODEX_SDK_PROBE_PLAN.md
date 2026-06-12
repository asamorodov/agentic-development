# Codex SDK probe plan

Дата: 2026-06-08  
Статус: подготовлен тест обхода `nested codex exec` через Codex SDK.

## Почему это добавлено

Тест `Codex controller → TS loop → codex exec` завершился `FAIL`: `codex --version` дал `Access is denied`, настоящий nested запуск упал на `spawn EPERM`, pass artifacts не были созданы.

Это означает, что CLI-вложение из текущей Codex-среды нельзя считать рабочим путём.

Следующая гипотеза:

```text
Codex controller
→ TS probe
→ @openai/codex-sdk
→ new Codex thread
→ debug file
```

Если она проходит, automation loop можно перевести на SDK backend for nested execution.

## Добавленные файлы

```text
work/prompts/CODEX_SDK_PROBE_PROMPT.md
work/automation/src/sdk-probe.ts
```

`work/automation/package.json` получил script:

```text
npm run sdk-probe
```

## Что проверяет probe

- импортируется ли `@openai/codex-sdk`;
- можно ли создать Codex object;
- можно ли открыть thread;
- можно ли выполнить prompt;
- может ли дочерний SDK-thread записать `work/automation/debug/SDK_PROBE.md`;
- где возникают ошибки: package, auth, sandbox, approval, filesystem, runtime.

## Что не проверяется

- реальные методологические досье;
- source accumulation protocol;
- 10–20 pass loop;
- subagents;
- `codex exec`.

Это именно точечный backend probe.
