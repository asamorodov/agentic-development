# A8 open questions

1. **Знаменатель ревью Stripe.** В текущем фрагменте Stripe используется как пример PR-producing platform with human review. Не использованы публичные throughput/one-shot цифры как доказательство изменения review load, а детали devbox/Toolshed/rules оставлены за пределами основного текста до более точной первичной проверки. Для финальной сборки остаётся вопрос: есть ли первичный источник с разбивкой по типам PR, доле исправлений после review, review latency и reject/rollback rate.

2. **Auto-merge vs acceptance semantics в `/babysit-pr`.** Источник говорит о цикле до чистого состояния и примере, где auto-merge queued после второго прохода. Для A8 это трактуется как PR-lifecycle automation, но не как перенос human/product authority на агента. В финальной редакции стоит проверить, не нужна ли отдельная формулировка про заранее настроенные auto-merge rules.

3. **CODEOWNERS не покрывает архитектурную власть.** CODEOWNERS хорошо показывает path ownership, но architectural/product/security acceptance может пересекать несколько ownership-зон. В соседних фрагментах нужно не дать читателю решить, что owner approval полностью заменяет ADR/security/product gates.

4. **Policy cluster можно углубить отдельно.** Linux/LLVM/tiangolo-FastAPI/QEMU/Homebrew/Zig уже показывают общий инвариант, но не дают полной taxonomy. QEMU теперь должен оставаться жёсткой DCO/provenance boundary, а не мягким provenance-emphasis примером; FastAPI-ссылка должна вести на tiangolo.com Automated Code and AI. Если часть XII будет делать сравнительную матрицу policies, нужно отдельно разделить disclosure, provenance, authorship, maintainer load, AI-output ban, human-in-the-loop и enforcement.

5. **PWG state contract.** В A8 предложены состояния `patched`, `checks_passed`, `ready_for_review`, `waiting_for_code_owner`, `accepted`, `rejected`, `superseded`. В финальной теории нужно состыковать их с соседним узлом про evidence package: какие artifacts обязательны для перехода между состояниями, а какие являются необязательными notes.

6. **SASE / академическое описание ролей.** SASE и `Collaborator or Assistant?` оставлены за рамкой второго прохода. Их можно добавить, если нужен академический мост между Agent Execution Environment и human acceptance, но текущий фрагмент уже держится на инженерных governance mechanisms.


7. **Zig как крайняя точка, а не общий закон.** В A8 Zig теперь усилен через strict policy и Contributor Poker, но это крайний policy endpoint. Финальная редакция должна сохранить контраст с более мягкими policies, чтобы не создать ложное впечатление, будто open-source governance в целом сходится к no-AI ban.

8. **AI-generated reasoning vs AI-generated diff.** Contributor Poker полезен тем, что переносит разговор с «кто написал diff» на «кто отвечает за reasoning and follow-up». В соседних фрагментах стоит проверить, не нужна ли отдельная категория evidence для author understanding, потому что обычные tests/CI её не покрывают.


9. **ADR process variants.** Добавлен AWS ADR process как конкретный source-backed пример Proposed → review → Accepted и проверки code changes against accepted ADRs. В финальной версии нельзя превращать этот процесс в единственно правильный; нужно оставить его как pattern for acceptance boundary.


10. **Материал для технического атласа.** Подробные таблицы policy spectrum, authority-laundering anti-patterns и ADR state machine лучше держать в `A8_figure_candidates.md`/атласе. Основной фрагмент должен оставаться несущим аргументом, а не оглавлением всех governance mechanisms.

11. **Стыковка со скелетоном.** После выравнивания A8 держит функцию части XII: право действовать и право завершать принадлежат разным контурам. В финальной сборке нужно следить, чтобы соседние фрагменты про evidence и human review не повторяли тот же ход, а подхватывали его.

## После A8 composition/visual/style repair 2026-06-11

12. **Technical atlas candidates.** Детальные схемы CODEOWNERS, ADR adoption, Homebrew checklist, Zig participation boundary и `/babysit-pr` loop сняты с inline. Они остаются кандидатами для технического атласа или более прикладного governance-раздела, если такой слой будет собираться.

13. **Терминология статусов принятия.** В A8 оставлены точные статусы `ready_for_review`, `waiting_for_owner`, `blocked_by_policy`, `needs_human_judgment`, `accepted`, `rejected`, `superseded`. В финальной сборке нужно решить, какие из них остаются английскими как model states, а какие переводятся в русские читательские формулировки.
