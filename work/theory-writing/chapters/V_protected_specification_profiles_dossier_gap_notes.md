# Заметки по досье и gap-check для главы V

## SPEC_KIT_METHOD_DOSSIER

Использовать для проверки деталей official docs/repo, SDD-cycle, `constitution`, `specify`, `plan`, `tasks`, `analyze`, `implement`. Главный gap для главы — актуальность поведения Spec Kit и точная формулировка команд/артефактов. Если в основном тексте появятся claims о текущем продукте, их нужно сверить с официальной документацией или репозиторием, а не только с досье.

## KIRO_SPECS_DOSSIER

Использовать для проверки Feature/Bugfix Specs, Quick Plan, Analyze Requirements, hooks/MCP/Powers, supervised execution и состояния spec. Главный gap — продуктовые возможности Kiro могут быстро меняться. Нужны осторожные формулировки и, при необходимости, свежая проверка официальных документов. В главе нельзя опираться на досье так, будто оно гарантирует текущий UI.

## TDAD_COMPARATIVE_DOSSIER

Использовать для разведения двух линий TDAD: тесты как определение агента и тесты как регрессионный маршрут. Главный gap — не свести весь evidence к тестам. В V тесты важны как specification carrier; caveats по mutation testing, oracle quality и evidence threshold лучше оставить главе XI, если только они не нужны для короткой границы.

## CONSTITUTIONAL_SDD_DOSSIER

Использовать для constitution, traceability matrix, security/human checkpoints и compliance evidence. Главный gap — статус и степень принятия метода. Формулировать осторожно: Constitutional SDD показывает сильную рамку для ограничений и трассируемости, но не должен подаваться как зрелый отраслевой стандарт или доказанный массовый процесс.

## Общий gap по главе

Внутренних материалов достаточно для первого черновика. Внешняя проверка всё равно нужна для текущих claims по Spec Kit и Kiro, а также для статуса Constitutional SDD и первичных источников по TDAD. Глава не должна делать слишком много текущих продуктовых утверждений: чем конкретнее claim, тем выше требование к свежей ссылке.

## P04 update — проверка актуальности первичных источников

Spec Kit и Kiro нужно цитировать по официальной документации, а не только по Атласу: обе поверхности активны и могут меняться. Для Spec Kit особенно важно не устаревшее число интеграций/extensions, а подтверждённый workflow с quality gates. Для Kiro важно подтверждать текущие названия `requirements.md`, `design.md`, `tasks.md`, Feature Specs, Bugfix Specs, Quick Plan и Analyze Requirements.

TDAD нужно подавать как две линии, а не один устоявшийся метод. Внутренний материал это уже делает; P04 подтвердил, что разделение остаётся обязательным.

Constitutional SDD нужно подавать осторожно: это сильная исследовательско-демонстрационная линия, но не зрелый стандарт. Banking repo и Cisco Foundry дают полезные примеры constitution/specification as constraints, но не должны создавать ложное впечатление массовой практики.

## P12 — новые gap notes после интеграции

Spec Kit: добавлен Constitution Check, поэтому в финальной проверке нужно убедиться, что он не смешан с Constitutional SDD. В Spec Kit это проверка внутри workflow; в CSDD — сам подход правил выше локальной задачи.

Kiro: добавлена зависимость spec state от локального контекста проекта. На следующем проходе проверить, не уводит ли это слишком рано в главу VI.

Stories: Matt Pocock теперь используется как практический контрвес. Нужно сохранить его коротким и не превращать раздел 7 в пересказ story 12.

## P13 — после русской переписи

Проверить в финальном аудите: Spec Kit Constitution Check и Constitutional SDD должны остаться различёнными; Kiro-грань с главой VI не должна выглядеть как начало новой темы; Matt Pocock должен остаться коротким практическим предохранителем против чрезмерной методологии.

## P23 — final gap status

Spec Kit Constitution Check and CSDD remain distinct in the final text. Kiro context boundary is present but does not open chapter VI early. Matt Pocock remains a short practical counterweight. No unresolved dossier gap blocks readiness.
