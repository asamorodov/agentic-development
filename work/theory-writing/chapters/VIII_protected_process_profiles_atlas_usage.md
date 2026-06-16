# VIII — atlas usage

Статус: заполнено по текущему тексту главы.

## GSD / Open GSD atlas

Использовано как методический anchor для длинной агентской работы:

- phase loop: Discuss → UI design when needed → Plan → Execute → Verify → Ship;
- `.planning/` as durable project state;
- `PROJECT.md`, `REQUIREMENTS.md`, `STATE.md`, `CONTEXT.md`, `PLAN-*.md`, `VERIFICATION-*.md`, `UAT-*.md`;
- fresh contexts and specialist agents;
- command/workflow routing in GSD User Guide, now integrated into the opening of the GSD section as the reason GSD is a route-selection mechanism rather than just a linear phase loop;
- `Verify` / `Ship` as a stopping and acceptance boundary, not a closing formula;
- `gsd-pi` as the point where process approach touches execution environment: `.gsd/`, SQLite state, auto mode, tool policy, git isolation, supervision and forced verification;
- GSD boundary with execution environment.

Не перенесены atlas synthetic figures. Причина: они объясняют GSD как отдельный метод, а глава VIII должна объяснять общий слой protected process profiles.

## BMAD atlas

Использовано как методический anchor для фазовой передачи контекста:

- Workflow Map and four-phase context building;
- `bmad-help` as route selection surface;
- `bmad-spec`, PRD, architecture, epics/stories;
- `bmad-sprint-planning`, `bmad-create-story`, `bmad-dev-story`, `bmad-code-review`, retrospective;
- `bmad-correct-course`;
- established project / brownfield workflow;
- `project-context.md`;
- `bmad-investigate`.

Часть BMAD-добора была перенесена в P11, затем структурно сжата в P14. Подробные source details сохранены в pass reports, но основной текст не должен расти дальше в BMAD-сторону.

## Gas Town / Beads atlas

Использовано только как верхняя граница:

- Beads: work objects, statuses, dependencies, gates, prime;
- Gas Town: broader operational environment with town/rig, workers, queues, handoffs, cleanup.

Не развёрнуто в подробный раздел, потому что глава VIII отвечает на вопрос «каким режимом продолжать один узел», а Gas Town относится к вопросу «как организовать много рабочих линий». Это мост к главе X.
