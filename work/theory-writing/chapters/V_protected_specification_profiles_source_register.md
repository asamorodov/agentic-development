# Source register — глава V

Дата последнего содержательного решения: 2026-06-14.

Этот регистр фиксирует не просто список источников, а решение по каждому: какую работу он делает в главе V, где его можно цитировать, а где лучше остановиться.

## Основные внутренние источники

| Источник | Роль в главе | Решение |
| --- | --- | --- |
| `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md` | Главный внутренний синтез по specification layer: Spec Kit, Kiro, TDAD, CSDD как разные способы удерживать изменение. | Использовать как смысловой каркас, но не копировать формулы, если они звучат как рабочие ярлыки. |
| `work/theory-writing/fragments/C1_specification_to_pwg.md` | Граница между спецификацией и persistent work graph. | Использовать в финале главы: protected specification approach не равен рабочему графу и не хранит всю жизнь изменения. |
| `work/theory-writing/fragments/00_spine_map.md` | Общая ось книги: изменение проходит от намерения к устойчивому состоянию. | Использовать как композиционный контроль. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Размещение главы V между SPDD-главой и контекстной главой VI. | Использовать как границу, не как источник тезисов. |

## Атласные статьи и досье

| Источник | Что даёт | Решение |
| --- | --- | --- |
| `work/atlas/articles/spec_kit_method.md` + `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | Spec Kit как цепочка specification → plan → tasks → implementation; роли clarify/checklist/analyze/constitution. | Использовать, но текущие продуктовые claims сверять с официальной документацией. |
| `work/atlas/articles/kiro_specs.md` + `work/dossiers/KIRO_SPECS_DOSSIER.md` | Kiro Specs как продуктовая spec surface: requirements/design/tasks, Feature/Bugfix Specs, Quick Plan, Analyze Requirements. | Использовать как второй основной подход. Не переносить экскурсию по Kiro как среде. |
| `work/atlas/articles/tdad_comparative.md` + `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | Разведение двух TDAD-линий: agent definition через тесты и impact-analysis/regression route для code agents. | Использовать осторожно как test-as-spec approach. Evidence-claims оставить будущей главе. |
| `work/atlas/articles/constitutional_sdd.md` + `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | Constitution, traceability, security/human checkpoints, worked example. | Использовать как подход правил выше фичи. Статус метода формулировать осторожно. |

## Story anchors

| Источник | Роль | Решение |
| --- | --- | --- |
| `content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md` | Практический контрвес тяжёлой методологии: малые skills, PRD/user stories, repairable routines. | Использовать коротко в разделе о цене подхода. |
| `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` | PR/review/evidence boundary. | Упоминать только как границу, если глава начнёт заходить в ревью. |
| `content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md` | Platform/team context boundary. | Не использовать в основном сравнении; оставить для главы VI/IX. |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Harness/context/budget boundary. | Не использовать в подходах; можно упомянуть в финальной границе. |

## Внешние первичные источники: включить

| Источник | Что подтверждает | Как использовать в главе |
| --- | --- | --- |
| https://github.github.com/spec-kit/ | Spec Kit как toolkit for Spec-Driven Development; базовая цепочка `Spec → Plan → Tasks → Implement`. | Основной источник для позиционирования Spec Kit. |
| https://github.github.com/spec-kit/quickstart.html | Рекомендуемый lean/full workflow, включая `constitution`, `clarify`, `checklist`, `analyze`. | Использовать для объяснения, почему подход защищает переходы, а не только хранит `spec.md`. |
| https://github.github.com/spec-kit/reference/workflows.html | Workflow-гейты, orchestrated commands, pause/resume/status. | Использовать только если нужен один абзац о возобновляемом состоянии. |
| https://kiro.dev/docs/specs/ | Specs as structured artifacts; `requirements.md`/`bugfix.md`, `design.md`, `tasks.md`. | Основной источник для Kiro как spec surface. |
| https://kiro.dev/docs/specs/feature-specs/ | Feature Specs: requirements → design → implementation planning. | Использовать в Kiro-разделе. |
| https://kiro.dev/docs/specs/bugfix-specs/ | Bugfix Specs: root cause, fix design, regression prevention. | Использовать коротко, чтобы показать, что подход работает не только для новых фич. |
| https://kiro.dev/docs/specs/quick-plan/ | Quick Plan generates requirements/design/tasks in one pass. | Использовать как пример лёгкого режима и его цены. |
| https://kiro.dev/docs/specs/analyze-requirements/ | Проверка противоречий, неоднозначностей, конфликтующих constraints and assumptions. | Использовать для ранней остановки до design. |
| https://arxiv.org/abs/2603.08806 | Test-Driven AI Agent Definition: behavioral specs, visible/hidden tests, mutation, spec evolution. | Использовать как первую TDAD-линию: тест определяет ожидаемое поведение агента. |
| https://github.com/f-labs-io/tdad-paper-code | Reference implementation / SpecSuite-Core. | Использовать только для уточняющей детали, если нужно. |
| https://arxiv.org/abs/2603.17973 | Test-Driven Agentic Development: graph-based impact analysis, regression reduction. | Использовать как вторую TDAD-линию: тестовый маршрут для кодового агента. |
| https://github.com/pepealonso95/TDAD | Репозиторий impact-analysis линии. | Использовать только как практическую опору. |
| https://raw.githubusercontent.com/pepealonso95/tdad-skill/main/SKILL.md | Skill: locate impacted tests, run them, write regression test. | Использовать как компактный пример TDAD в рабочей инструкции агента. |
| https://arxiv.org/abs/2602.02584 | Constitutional Spec-Driven Development as proposed methodology. | Главный источник для CSDD, с осторожным статусом. |
| https://github.com/srinivasraom/banking-ms-by-constitution | Banking worked example. | Использовать только как демонстрацию. |
| https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md | Concrete security-first constitution. | Использовать для объяснения constitution как слоя правил, если нужен пример. |
| https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md | Compliance mapping from rules to implementation. | Использовать осторожно как пример trace/compliance mapping. |

## Внешние источники: optional / boundary only

| Источник | Решение |
| --- | --- |
| https://github.com/github/spec-kit | Не использовать количественные claims о релизах/stars/extensions, если они не нужны аргументу. Можно оставить для проверки текущего состояния проекта. |
| https://github.com/CiscoDevNet/foundry-security-spec | Optional adjacent source: specification/constitution as deliverable. Не называть CSDD. |
| https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md | Optional, только если нужен соседний пример `spec.md` + `constitution.md` без кода. |
| https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md | Optional, не вводить без необходимости. |
| https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md | Optional, не вводить без необходимости. |

## Отклонённые источники

| Источник / тип источника | Почему не использовать |
| --- | --- |
| Microsoft Developer Blog on Spec Kit | Вторичный источник; official docs лучше и точнее. |
| Private Spec Kit guides / SEO pages | Не добавляют осей сравнения, повышают риск продуктовой журналистики. |
| Kiro dev.to / Promptz guides | Официальная документация достаточно сильна. |
| ResearchGate mirror of CSDD | Зеркало arXiv, не добавляет содержания. |
| LinkedIn/YouTube summaries of CSDD | Недостаточно надёжные источники для теоретической главы. |
| TDAD TypeScript ports / GitHub topic pages | Может быть интересно для инструментального обзора, но не для аргумента главы V. |
| TDFlow paper | Возможный материал будущей главы о тестах/evidence, но не текущего подхода спецификации. |

## Итоговое правило переноса в основной текст

В главе V ссылка или источник вводится только там, где он усиливает сравнение подходов. Если факт не помогает ответить на вопрос «какую часть изменения этот подход делает устойчивой?», его лучше не переносить.

## P08 — фактическое использование в первом черновике

| Группа источников | Использование в черновике |
| --- | --- |
| Spec Kit official docs | Введены в разделе 3 для цепочки `Spec → Plan → Tasks → Implement` and full workflow. |
| Kiro official docs | Введены в разделе 4 для Specs, Feature/Bugfix Specs, Quick Plan and Analyze Requirements. |
| TDAD primary papers and skill | Введены в разделе 5 для двух TDAD-линий and test-as-specification approach. |
| Constitutional SDD paper and banking example | Введены в разделе 6 для constitution/approach above feature. |
| Cisco Foundry Security Spec | Введён одной граничной фразой как adjacent source, not CSDD. Проверить на следующем проходе, нужен ли он вообще. |
| Matt Pocock story | Введён коротко в разделе 7 как контрвес тяжёлой методологии. |

## P09 — русская перепись

В P09 источники не расширялись. Все внешние ссылки сохранены в местах первого переноса фактов. Текст переписан так, чтобы источники работали на сравнение подходов, а не на обзор инструментов.

Проверить в следующем проходе: нужна ли ссылка на Cisco Foundry в основном тексте или её лучше оставить только в source register как optional adjacent source.

## P14 — размещение внешних ссылок

В основном тексте ссылки поставлены рядом с соответствующими фактами. После P14 добавлена ссылка на Spec Kit workflows как источник для возобновляемого процесса со статусом и human checkpoints. Остальные внешние источники не расширялись.

## P15 — языковая проверка внешней вставки

Workflow source оставлен, но формулировка русифицирована и не подана как обзор функции инструмента.

## P16 — source-placement audit

Проверено: внешние источники стоят рядом с первым содержательным вводом факта/детали в основном тексте. Внутренние story anchors указаны локальными путями рядом с использованием. Новые источники без ссылки не обнаружены.

## P20 — visual decision

Внешние изображения не используются. Синтетическая матрица выбора подхода зафиксирована как optional future visual candidate, но не вставлена в основной текст, чтобы не вернуть главу к справочной/каталожной форме.

## P23 — final source status

Source register checked against the final chapter. No uncited external factual claims were found. External sources are used only where they support a approach or axis of comparison. Cisco Foundry remains peripheral and optional for later removal.
