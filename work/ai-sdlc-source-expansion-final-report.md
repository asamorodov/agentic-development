# Final report — AI-driven SDLC source expansion

## Что сделано

Выполнены 3 честных шага поиска. Каждый шаг имеет отдельный search prompt и отдельный search results файл.

Обновлена карта первоисточников:

```text
updated/THEORY_SOURCE_MAP_AI_DRIVEN_SDLC_UPDATED_2026_06_05.md
```

## Главный результат

Рамка AI-driven / agentic SDLC теперь поддержана не только внутренней логикой наших документов, но и отдельным слоем первоисточников:

- DORA и Bain — для тезиса, что AI value требует системного/process/lifecycle redesign, а не просто coding acceleration.
- A-SDLC survey и SLR — для внешней исследовательской рамки и понятия maturity/verifiability by SDLC phase.
- OpenAI Codex, GitHub Copilot cloud agent, Google Jules, Claude Code docs — для platform/workflow primitives.
- GitHub Well-Architected, OpenSSF, Snyk — для governance/security/process-risk layer.
- Governing Technical Debt in Agentic AI Systems и maintenance papers — для lifecycle-tail: долг, сопровождение, stochastic tax.

## Что НЕ сделано

- Не утверждена новая структура теории.
- Не сделана новая версия `Theoretical_synthesis_rebuilt.md`.
- Не выполнен deep reading PDF `AI Codebase Maturity Model`; он оставлен кандидатом.
- Не добавлялись новости как несущие источники.

## Рекомендация

Следующий structural synthesis pass стоит делать уже с учётом нового раздела `0. Рамочные источники для AI-driven / Agentic SDLC`, но не копировать классическую SDLC-структуру. Более сильная линия:

```text
намерение → контекст → делегирование → исполнение → свидетельства → ревью → завершение → сопровождение/обучение среды
```
