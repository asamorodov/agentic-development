# A2 open questions

1. Какие поля reconstructed ADR должны стать обязательными в финальной теории: достаточно ли `origin`, `status`, `evidence`, `confidence`, `known_gaps`, `review_owner`, `confirmation_plan`, или нужно отдельно фиксировать `decision_scope` и `source_conflicts`?

2. Где должна жить operational projection: в `AGENTS.md`, локальном skill, rule file рядом с кодом, CI policy или generated context bundle? Ответ может зависеть от того, нужна ли проекция человеку, агенту или gate.

3. Какой минимальный review достаточен, чтобы перевести reconstructed/generated ADR из `proposed` в `accepted`: owner approval, lightweight architecture review, PR approval с явной меткой, отдельный ADR log update?

4. Как предотвратить автоматическое принятие ADR из-за заполненного шаблона: нужен ли policy rule “generated ADR cannot be accepted without explicit status-change commit”?

5. Должна ли `Confirmation` в ADR ссылаться только на существующие checks или может создавать новые обязательства для будущих checks? Это важно, чтобы не превратить ADR в unverifiable wish list.

6. Как синхронизировать `superseded` ADR и operational projections, чтобы агент не продолжал выполнять старое правило из кэша, memory file или скопированного контекста?

7. Какой минимум contract/oracle должен сопровождать разные типы спецификаций: feature spec, API spec, migration spec, refactoring spec? Нужна ли таблица “spec type → required oracle”.

8. Какие tests можно показывать агенту во время генерации, а какие должны оставаться hidden/evaluation-only, чтобы не получить test gaming?

9. Нужно ли считать `spdd-api-test` частью specification workflow или отдельным evidence/oracle layer в финальной терминологии?

10. Как описать частичный oracle, который покрывает только одну границу: Pact для известных consumers, `oasdiff` для published OpenAPI, smoke tests для главного маршрута, data parity для миграции?

11. Как включить проверку correctness of specification в lifecycle: отдельный review step до генерации, checklist в spec PR, acceptance examples от пользователя или интерактивное approve/reject тестов?

12. Где граница между informal specification, checkable specification и contract/oracle в финальной терминологии: contract — это только межсистемное обещание или любой checkable expectation?

## Материал, который лучше не раздувать внутри A2

- Точная schema reconstructed ADR и operational projection должна уйти в technical atlas ADR или fieldbook, а в A2 оставить только правило `origin ≠ status` и `projection ≠ full ADR`.
- Детали TDAD visible/hidden/mutation workflow полезнее раскрыть в будущем узле про evidence/oracle, а в A2 оставить только ограничение: tests can become optimization targets.
- Подробные Product Migration истории лучше использовать в migration/evidence разделе; в A2 нужны только два коротких якоря: negative oracle gap и positive setup/review discipline.

13. Как в финальной структуре назвать “зелёный результат проверки, который проверяет свою границу, но не объясняет архитектуру”: contract gate, evidence gate, oracle или проверяемое ожидание?

14. Повторный repair развёл термины в основном тексте: проверочный контракт — более узкое межсистемное или межверсионное обещание; оракул — более общий механизм проверки поведения, данных, миграций или скрытой оценки. Открытым остаётся только вопрос, насколько строго это различение нужно формализовать в глоссарии.

## After A2 repair: remaining questions

15. Закрыто повторным repair: основной A2 больше не использует “контракт/оракул” как неразобранную связку. В тексте используется “проверочный контракт или оракул” с объяснением различия; финальный глоссарий может только уточнить границу терминов.

16. Подтверждено повторным repair: отдельная карточка рабочей проекции ADR снята с inline и оставлена для technical atlas / fieldbook. В основном A2 достаточно правила `projection ≠ full ADR` и `projection does not change authority`.
