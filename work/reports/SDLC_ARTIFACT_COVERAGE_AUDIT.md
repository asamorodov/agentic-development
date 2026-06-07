# SDLC artifact coverage audit

Дата: 2026-06-07  
Режим: ChatGPT / локальный snapshot archive → archive handoff overlay  
Ветка-источник: `work/theory-ai-sdlc-rebuild`  
Статус: рабочий audit перед writing/rewrite глав. Главы не переписывались.

Этот audit отвечает на один вопрос: какие артефакты жизненного цикла программного изменения уже видны в утверждённом AI-driven SDLC плане, а какие пока существуют только как фон, как отдельные упоминания или вообще выпали из архитектуры.

Проверялись прежде всего:

- `work/approved-ai-sdlc-plan.md`;
- `work/theory-source-map-ai-driven-sdlc.md`;
- `work/discourse.md`;
- `work/old-site-headings.md`;
- `work/old-site-theoretical-synthesis-baseline.md`;
- `work/expanded-quarry-headings.md`;
- `work/specification-cluster-deep-plan.md`;
- `work/approved-decisions.md`;
- `work/anchor-case-baseline-restore-rule.md`;
- `work/source-depth-audit.md`;
- `work/anti-catalog-audit.md`;
- `work/case-dossier-protocol.md`;
- `work/open-questions.md`;
- `work/codex-first-task-prompt.md`;
- протоколы из `protocols/` и проектные документы из `project/`.

Внешние источники проверялись точечно, не как новый массовый source-search cycle. Цель была не расширить корпус, а проверить уже обнаруженные дырки: ADR / decision records, GSD, BMAD, OpenSpec / Agent Spec, Reversa and framework taxonomy.

Важно: audit не заменяет `approved-ai-sdlc-plan.md` и не меняет его напрямую. Если рекомендации принимаются, план нужно обновлять отдельным human-gated шагом.

## Общая диагностика

Текущий approved plan силён в четырёх зонах.

Первая — **intent/specification layer**. Здесь есть SPDD как отдельная глубокая часть, Spec Kit / Kiro / TDAD / Constitutional SDD как глубокие соседние режимы, и явный тезис, что prompt слишком слаб как единица управления.

Вторая — **session/evidence layer**. SWE-chat / Programming by Chat, benchmarks, tests, PR communication, review and evidence уже представлены.

Третья — **deep anchor cases**. SPDD и Gas Town защищены baseline restore rule.

Четвёртая — **governance/external boundary**. Open-source policy cluster, SASE and completion right уже есть.

Слабее представлены:

1. **Decision provenance.** ADR/RFC/design proposal пока не стали first-class SDLC artifacts.
2. **Operational release tail.** Release plan, migration plan, rollback plan, runbook, incident report, postmortem, deprecation/changelog/dependency policy пока слабее, чем intent/specification layer.
3. **Security/provenance as artifacts.** Threat model, security review, audit log, provenance record присутствуют как тема security/governance, но не полностью как набор рабочих артефактов lifecycle.
4. **Ownership artifacts.** CODEOWNERS / ownership map / escalation paths пока слабо оформлены как artifacts of completion right.
5. **Process framework layer.** GSD/BMAD/Reversa/OpenSpec-like материалы выявлены как отдельный класс и вынесены в parallel audit.

## Таблица покрытия SDLC artifacts

| Artifact type | Lifecycle stage | Current coverage in approved design | Current coverage in source map / drafts | Depth | Risk if omitted | Recommended action |
|---|---|---|---|---|---|---|
| `prompt` | Intent entry / delegation | Сильно покрыт как слишком слабая единица управления в Part III; SPDD переносит prompt в delivery artifact | Старый baseline содержит “хороший запрос больше не является единицей управления”; expanded quarry много обсуждает prompt/spec | Deep | Текст может снова скатиться в prompt-centric картину | Оставить как отрицательную исходную точку Part III; не превращать prompt в главный artifact |
| `specification` | Intent / governance / executable plan | Очень сильно покрыта Parts IV–V: SPDD, Spec Kit, Kiro, TDAD, Constitutional SDD | Source map section 6; specification deep plan | Deep | Потеря центрального узла AI-driven SDLC | Сохранять specification zone как центральную; не сжимать соседние режимы |
| PRD / requirements | Intent clarification | Покрыто через Kiro `requirements.md`, Spec Kit `specify`, SPDD story shaping / analysis context | Old baseline SPDD headings; Kiro/Spec Kit sources | Medium-deep | Raw requirements могут смешаться со spec/plan/Canvas | В Part III явно различить raw requirement, PRD, spec, plan, Canvas |
| `plan.md` | Context / working state / delegation | Есть в local modes and project-as-interface, но не first-class artifact в approved plan | Old site mentions `research.md` and `plan.md`; HumanLayer/Boris Tane materials | Medium | План будет растворён между prompt and spec | В Part VI/VII выделить `plan.md` как externalized working state: lighter than spec, stronger than chat |
| ADR / decision record | Decision provenance / long-term memory | Почти отсутствует как first-class element | Old baseline упоминал ADR-like artifacts; external ADR sources confirm role | Medium-deep | Агент/читатель будет знать “что”, но потеряет “почему” и rejected alternatives | Добавить ADR layer: Part III artifact spectrum, Part VI project memory, Part XII decision debt; создать proposed ADR |
| RFC / design proposal | Pre-implementation decision / social review | Не выделен отдельно | SASE consultation/merge readiness, PR sources, old discussions imply proposal-like artifacts | Medium | Architecture/design discussion collapses into spec or PR | Добавить как sibling of ADR: design proposal/RFC as reviewable decision surface |
| Handoff | Context transfer / session continuity | Есть через Gas Town, Beads, long-lived task, Codex handoff | Old site and discourse strongly emphasize handoff/discourse | Medium | Long tasks and branch transitions lose continuity | Keep in Part VI and Gas Town; link to `work/discourse.md` as live process example |
| `research.md` | Discovery / context building | Implicit in local modes and project interface | Old site and stories mention Boris Tane / HumanLayer research-first | Medium | Research becomes hidden chat, not reusable evidence | Put in Part VI/VII as research artifact distinct from plan/spec |
| Task graph | Execution planning / durable task state | Strong in Gas Town / Beads, Kiro tasks, Spec Kit tasks | Old Gas Town headings; source map radical lines | Medium-deep | Multi-step agent work becomes session-bound checklist | Treat Beads/Gas Town as deep example; show lighter forms in Spec Kit/Kiro |
| Progress log | Execution trace / recovery | Weakly covered; session trace and evidence cover adjacent ground | SWE-chat trace, Gas Town continuation, work/discourse | Medium-short | Long-running work cannot be resumed or audited | Add under Part VI/VIII as progress/state trace; not separate deep case |
| Acceptance criteria | Intent-to-evidence bridge | Covered but implicit in SPDD, Kiro, Spec Kit, tests | Specification sources imply criteria | Medium | Tests/benchmarks may not validate intended behavior | Add explicitly in Part III/V/X as bridge from requirements to evidence |
| Test plan | Evidence planning | Part X covers tests/benchmarks; SPDD API tests; TDAD | Source map Part 8 | Medium | Tests treated as afterthought rather than planned evidence | Distinguish test plan from tests; connect to SPDD/Kiro/TDAD |
| Benchmark | Evidence / external evaluation | Strong in Part X | Source map section 8: UTBoost, SWE-Bench variants, benchmarks | Deep-medium | Benchmark validity treated superficially | Keep Part X; avoid making benchmark numbers substitute for lifecycle evidence |
| CI evidence | Evidence package / merge readiness | Present but not fully artifactized | PR/review sources, Codex/GitHub platform docs | Medium-high | Agent claims “done” without durable machine evidence | Add as explicit artifact in Part X: logs, CI status, test outputs, reproduction steps |
| PR description | Review interface / social artifact | Present in Part X/XI via PR communication | Source map section 9 | Medium-high | Human reviewer sees code but not agent work/context | Treat PR description as part of agent output, not decoration |
| Review comments | Review / feedback / repair | Present in Part X and old evidence sections | Source map PR/review; old baseline comments-as-signals | Medium-high | Agent treats comments as commands or ignores signal value | Keep as “signals, not commands”; connect to repair loops |
| Release plan | Deployment / completion tail | Undercovered; Part XII mentions tail but no artifact taxonomy | Bain/DORA imply bottlenecks; no strong dedicated source yet | Medium-short | SDLC ends at merge, repeating coding-centric bias | Add to Part XII as lifecycle-tail artifact; targeted source search only if needed |
| Migration plan | Change rollout / compatibility | Undercovered | Reversa and legacy modernization sources are relevant but not yet in source map deeply | Medium-short | Legacy/compatibility changes look like ordinary code changes | Add in Part XII; Reversa can be medium case for migration/spec extraction |
| Rollback plan | Recovery / operational risk | Undercovered | Security/ops sources imply but not central | Medium | Agentic speed increases irreversible change risk | Add to Part XII as high-risk artifact; not deep unless sources develop |
| Runbook | Operations / incident handling / agent behavior | Undercovered; TDAD Agent Definition includes runbook-like agents | Security and TDAD sources | Medium | Operational behavior not transferred to agents or humans | Add to Part XII and security/provenance cluster |
| Incident report | Learning environment / repair | Weak | DORA/system learning; no direct deep source in current map | Short-medium | Failures do not feed back into specs/tests/instructions | Mention in Part XII as lifecycle feedback artifact |
| Postmortem | Learning / process update | Weak | Adjacent to incident report | Short-medium | Same failures repeat without changing environment | Mention in Part XII; use as example of environment learning |
| Threat model | Security constraints before action | Part V Constitutional SDD and security sources cover adjacent ground | Source map section 10 includes MCP threat modeling | Medium-high | Security appears only after generation | Add explicit threat model artifact in Part V/VIII/XII; connect to Constitutional SDD and MCP |
| Security review | Review / governance | Covered as theme, not fully as artifact | Source map OpenSSF/Snyk/GitHub governance | Medium | Security remains vague warning | Add as artifact distinct from threat model and test evidence |
| Audit log | Evidence / governance / provenance | Part VIII/XI mention logs/evidence but not audit log as artifact | Platform docs / provenance sources | Medium | Actions cannot be attributed or reconstructed | Add audit log/provenance record as cross-cutting artifact |
| CODEOWNERS / ownership map | Completion right / review routing | Undercovered; Part XI has ownership but no artifact | Open-source policies and GitHub governance | Medium | “Right to complete” remains abstract, not encoded in project | Add to Part XI as concrete ownership artifact |
| Dependency policy | Maintenance / supply chain | Undercovered | Security/supply-chain sources imply | Short-medium | Agents may upgrade or add dependencies without policy | Add to Part XII/security as short artifact; targeted source if it becomes important |
| Deprecation policy | Lifecycle tail / compatibility | Undercovered | No strong current source | Short | Compatibility tail disappears | Mention briefly in Part XII; source-map only unless expanded |
| Changelog / release notes | User-facing memory / release communication | Undercovered | PR/release adjacent; no deep source | Short | Lifecycle loses external communication of change | Mention in Part XII as short artifact |
| Provenance record / agent action trace | Cross-cutting responsibility | Present indirectly in session trace, audit logs, PR, policies | Responsible agentic AI provenance source; Codex/GitHub logs | Medium-high | Cannot answer who/what produced a change and under what constraints | Add as explicit cross-cutting artifact; maybe Part I/VIII/XI |

## Findings by lifecycle step

### Intent

Intent is the strongest layer. Prompt, specification, PRD/requirements and acceptance criteria are already well supported, but ADR/RFC need to be added as decision-provenance artifacts. The key distinction should become:

```text
prompt ≠ plan ≠ specification ≠ ADR ≠ RFC/design proposal ≠ handoff
```

The document already says prompt is too weak. It now needs to say more clearly that different intent artifacts preserve different things: desired outcome, plan of attack, governing constraint, decision rationale, rejected alternatives, state transfer.

### Context / working state

`research.md`, `plan.md`, handoff, progress log and task graph are partly visible through stories and Gas Town, but they need cleaner taxonomy. They do not need a new top-level part; they should strengthen Part VI “project as agent interface” and Part VII “delegation mode”.

### Execution / evidence

Benchmarks, tests, review and PR communication are covered, but CI evidence, audit log and provenance record need more explicit artifact treatment. Generated code is not enough; the lifecycle needs an evidence package.

### Completion / governance

Open-source policies and completion right are strong, but ownership artifacts like CODEOWNERS, review ownership and escalation map are not yet concrete enough. Without them, “right to completion” risks staying a concept rather than a project interface.

### Lifecycle tail

This is the weakest structural area after ADR/frameworks. Release plan, rollback plan, migration plan, runbook, incident report, postmortem, dependency/deprecation policy and changelog should not all become deep cases, but Part XII needs a visible artifact cluster. Otherwise AI-driven SDLC will still effectively end at merge/review.

## Recommended additions before drafting

1. Add a short artifact taxonomy to Part I or Part III.
2. Add ADR / decision record as medium-deep cross-cutting artifact.
3. Add RFC/design proposal as a sibling to ADR, not as a spec.
4. Add release/ops tail artifact cluster to Part XII.
5. Add threat model / security review / audit log / provenance record as explicit artifacts in Parts V, VIII, XI, XII.
6. Add CODEOWNERS / ownership map to Part XI.
7. Update approved plan after human approval; do not patch it silently.
