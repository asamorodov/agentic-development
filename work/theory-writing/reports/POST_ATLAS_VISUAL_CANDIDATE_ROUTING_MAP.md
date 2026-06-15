
# Post-Atlas visual candidate routing map

Статус: routing для будущего asset-pass. Изображения не скачивались и не вставлялись.  
Правило: ready local assets сохраняются как images; external real candidates требуют source/rights/quality/placement check; synthetic figures допустимы только там, где они реально проясняют аргумент.

| Глава | Политика | Кандидаты | Ограничение |
| --- | --- | --- | --- |
| INTRO | inline-use | `fig-00-post-atlas-lifecycle-axis` already exists as synthetic figure in 00; можно использовать или адаптировать. | Не добавлять декоративные AI coding screenshots. |
| I | inline-use / atlas-reference-only | local Boris lifecycle, OpenAI Codex evidence, Beads/PWG state images from A1 recovery. | Use only if argument needs carrier/lifecycle contrast. |
| II | chapter-queue | Simon Showboat image, Arvid/browser observation, Jökull PR/CI, Codex terminal logs, Armin harness. | Avoid story screenshot collage. |
| III | chapter-queue | ADR local SVGs, Fowler SPDD workflow/Canvas, CSDD traceability matrix candidates, Spec Kit cycle. | Do not overload with template screenshots. |
| IV | inline-use | Fowler/OpenSPDD local assets: REASONS Canvas, workflow, analysis/review, API test, code review, prompt-update/sync. | Use 1–3 strongest assets, not full SPDD gallery. |
| V | chapter-queue | Spec Kit/Kiro/CSDD/TDAD external candidates; some local Fowler SDD context asset. | Requires asset-pass; no synthetic replacement for real diagrams. |
| VI | chapter-queue | Fowler context/coding context, Anthropic context vs prompt, HumanLayer context firewall, Matt skills screenshots. | Keep focus on project as interface, not context-engineering overview. |
| VII | inline-use | beads-task-graph-memory.svg; PWG/Beads candidates; possible GitHub/Linear boundary visuals. | One central state figure is likely enough. |
| VIII | chapter-queue | BMAD workflow map, sprint-state synthetic figure, GSD process/runtime candidates, Jesse process images. | Avoid process framework brochure. |
| IX | chapter-queue | HumanLayer harness components, Mike worktrees/sandbox, OpenAI Codex dashboard/permissions/DevTools, Stripe Minions, Shopify Roast workflow. | Strong asset-pass needed; this chapter can easily become UI-tour. |
| X | inline-use | Gas Town local SVGs: pressure-to-mechanism stack, two-tier Beads flow, worker roles; external Gas Town candidates. | Use visuals to explain operation, not glossary. |
| XI | chapter-queue | Showboat/curl demo, Codex citations/evidence, Pact/can-i-deploy, TDAD figures, OpenAI DevTools validation. | Evidence visuals need exact claim and provenance. |
| XII | chapter-queue | Mike worktrees/maintainer boundary, ADR status/Design Decision Gate, policy screenshots only after source check. | No generic governance diagrams. |
| XIII | chapter-queue | Fowler continuous feedback, SPDD prompt-update/sync, BMAD correct-course, ADR lifecycle/sync, skills/rules update visuals. | Avoid maintenance checklist poster. |
| CONCLUSION | atlas-reference-only | Use earlier figures by reference; no new visual layer unless mode map is authored deliberately. | Do not create final mega-matrix without need. |
| APPENDIX | atlas-reference-only | Atlas articles keep their own image plans and queues. | No extra images. |

## Общие asset decisions

- Готовые локальные изображения из `content/assets/**` нельзя переписывать текстовыми схемами по умолчанию.
- External real candidates из `*_external_image_queue.md` и asset catalog остаются очередью до отдельного asset-pass.
- Для IX и XI нужен особенно строгий visual pass: там больше всего соблазн сделать UI-tour.
- Для IV, VII and X уже есть сильные локальные/синтетические опоры; эти главы не должны добирать картинки ради полноты.
