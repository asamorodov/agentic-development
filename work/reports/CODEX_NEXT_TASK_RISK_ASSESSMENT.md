# Codex next task risk assessment

Дата: 2026-06-08  
Следующая предполагаемая задача: `work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md`

## Вердикт

Stage 0.19 можно запускать после этой readiness check, но только как dossier/pass task. Писать главы, менять `work/approved-ai-sdlc-plan.md`, менять skeleton или демотировать методологии нельзя.

## Риски перед Stage 0.19

1. **Риск глубины источников.** Stage 0.19 требует primary / official sources для protected methodology profiles. Existing internal notes и source-expansion materials помогают сориентироваться, но не заменяют настоящий source inventory. Если локальных материалов недостаточно, Codex должен остановиться и запросить human decision или одобренный доступ к источникам.

2. **Риск поверхностного профиля.** GSD, BMAD, Spec Kit, Kiro, TDAD и Constitutional SDD могут выглядеть “covered”, если каждый получит аккуратное summary. Этого явно недостаточно. Каждый dossier должен восстановить workflow, artifacts, gates, validation, lifecycle tail и failure modes.

3. **Смешение архитектурной роли и глубины.** GSD/BMAD являются protected profiles, но не текущими deep anchors. Promotion to deep anchor или demotion to short mention требует human gate.

4. **Риск сжатия SPDD/Gas Town через сравнения.** Comparative sections могут случайно превратить SPDD или Gas Town в примеры внутри process spectrum. Stage 0.19 должен ссылаться на них аккуратно и сохранять их deep-anchor status.

5. **Риск каталогизации.** Methodology dossiers могут стать списками команд, ролей или артефактов. Обязательный anti-shallow audit должен проверять, служит ли каждый артефакт функции lifecycle.

6. **Языковой риск.** Многие названия источников и методологий английские, но объяснительный текст должен оставаться русским. Stage 0.19 должен избегать English-heavy report prose.

7. **Риск расширения области.** Stage 0.19 легко может превратиться в broad source search, skeleton redesign или chapter drafting. Это stop conditions без явного одобрения.

8. **Риск регистра имени `CHECKS`.** Prompt называет `work/CHECKS.json`; существующий файл в этом worktree называется `work/checks.json`. В Windows workspace это один путь, но в будущей case-sensitive среде регистр стоит нормализовать отдельным осознанным решением.

## Рекомендуемая следующая задача

Запустить `work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md` после принятия этой readiness check человеком.

## Обязательное поведение во время Stage 0.19

- Прочитать Stage 0.19 prompt и `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md`.
- Создать pass folders и pass files for Spec Kit, Kiro, Constitutional SDD, TDAD, GSD и BMAD.
- Создать final dossiers только после шести проходов.
- Создать comparative synthesis reports.
- Обновить `work/discourse.md` и `work/checks.json`.
- Остановиться для human decision, если source depth слабый или задача требует изменения approved architecture.

## Оставшиеся human gates

- Одобрение broad new source search или стратегии network/source access.
- Demotion любого protected methodology profile.
- Promotion GSD/BMAD или adjacent methods to deep anchors.
- Writing Part V или Part VII before dossiers exist.
- Изменение `work/approved-ai-sdlc-plan.md`.
- Изменение `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`.
- Compressing SPDD или Gas Town against baseline restore rule.
