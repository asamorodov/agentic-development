# Шаг 03. Результаты поиска — Хвост жизненного цикла: сопровождение, долг, security/governance

## Акцент

Искать источники, которые не дают рамке AI-driven SDLC стать оптимистическим “AI делает всё быстрее”: сопровождение AI-кода, agentic technical debt, stochastic tax, security before repo, controls inside workflows, OpenSSF/security guidance.

## Найденные источники и решение

### To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study

- URL: https://arxiv.org/abs/2605.06464
- Решение: `already_elevate`
- Пояснение: Уже есть в карте, но теперь должен быть поднят как lifecycle-tail source: не что агент сгенерировал, а что потом происходит с файлами и кто их поддерживает.

### Governing Technical Debt in Agentic AI Systems

- URL: https://arxiv.org/abs/2605.29129
- Решение: `include`
- Пояснение: Новый хороший концептуальный источник: agentic technical debt как debt prompts/memory/tool schemas/orchestration/control policies/observability; stochastic tax как операционная цена вероятностных агентов.

### Debt Behind the AI Boom

- URL: https://arxiv.org/abs/2603.28592
- Решение: `already_elevate`
- Пояснение: Уже есть в карте; оставить как эмпирический источник по AI-authored commits и долговому хвосту.

### OpenSSF Tech Talk Recap: Securing Agentic AI

- URL: https://openssf.org/blog/2026/04/08/openssf-tech-talk-recap-securing-agentic-ai/
- Решение: `include`
- Пояснение: Более конкретный OpenSSF источник, чем общий newsletter: Secure AI/ML-Driven Software Development course, AI/ML Security WG, SAFE-MCP.

### OpenSSF, Securing Agentic AI in Practice

- URL: https://openssf.org/blog/2026/03/13/securing-agentic-ai-in-practice-from-openssf-guidance-to-real-world-implementation/
- Решение: `include`
- Пояснение: Инфраструктурный/security источник для practical governance; полезен в security/source-chain разделе.

### Snyk, The New Security Risks of the Agentic Development Lifecycle

- URL: https://snyk.io/blog/agentic-development-lifecycle/
- Решение: `include_cautiously`
- Пояснение: Industry security framing: ADLC risk enters via what agents use/do/generate; useful as concrete security framing, but не academic и не независимый от vendor agenda.

### AI Codebase Maturity Model

- URL: https://arxiv.org/pdf/2604.09388
- Решение: `candidate_cautious`
- Пояснение: Интересная рамка “codebase readiness for agents”, но нужно отдельное чтение PDF и проверка качества; пока кандидат.

### TechRadar / other news on stability and outages

- URL: various
- Решение: `reject`
- Пояснение: Новости слишком вторичны/сенсационны для source map. Использовать только как pointer to primary reports, не как несущий источник.

## Итог шага


Шаг показал, что новая рамка обязана иметь сильный downstream/security хвост. Иначе AI-driven SDLC станет оптимистической историей о скорости генерации, а не теорией устойчивого изменения.
