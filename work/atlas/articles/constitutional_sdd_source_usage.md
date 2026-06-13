# constitutional_sdd — source usage

Статус: P26 guarded final style sync. Источники не добавлялись; правка затронула только тон, заголовки и отдельные публичные формулировки без изменения фактуры.

| Источник | Тип | Где использован | Что поддерживает | Ограничение |
|---|---|---|---|---|
| [Marri, arXiv:2602.02584](https://arxiv.org/abs/2602.02584) | Основная исследовательская статья | Ввод, постановка CSDD, метод, ограничения | CSDD как перенос требований безопасности в спецификационный слой | Перед публикацией нужна свежая сверка версии arXiv. |
| [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | Полный текст основной статьи | Constitution, workflow, matrix, metrics, caveats, figures | 15 principles, CSDD workflow, traceability table, qualitative examples, 73% claim with threats to validity | ar5iv используется как читаемая версия; при конфликте финально сверять с PDF. |
| [arXiv PDF](https://arxiv.org/pdf/2602.02584) | Канонический PDF основной статьи | Зафиксирован как источник для будущей сверки | Таблицы, threats to validity, будущая работа | В P01 не переоткрывался отдельно; точные формулировки следует сверить в позднем source-depth pass. |
| [banking-ms-by-constitution repository](https://github.com/srinivasraom/banking-ms-by-constitution) | Reference implementation | Context files, README details, license caveat, client-token blind spot | Структура референсного репозитория и поверхность реализации | README diagrams не вставлены из-за rights hold. |
| [.specify/memory/constitution.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md) | Reference Constitution | Разделы о Constitution, governance, lifecycle repair, human gates | Более широкий набор принципов, amendment process, quarterly reviews, CI/CD, testing and deployment gates | Нужно сверить отношение compact paper principles vs broader repo Constitution. |
| [spec.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/spec.md) | Feature spec | Раздел `spec.md`, `plan.md`, `tasks.md` | User stories, edge cases, FR-001...FR-022 | Использован как пример роли спецификации, не как полный аудит banking domain. |
| [plan.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/plan.md) | Implementation plan | Раздел о plan drift | Constitution Check, stack choices, possible mismatch with Structure Decision | Нужна поздняя сверка, является ли apparent drift реальным дефектом или допустимым сокращением. |
| [tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md) | Tasks | Раздел о task-level weakening | T001–T013 and lack of explicit SEC/CWE references | Использован как caution, не как утверждение о неверности реализации. |
| [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | Compliance report | Раздел о матрице соответствия | mappings, techniques, auto-generated claim | Инструмент генерации не установлен; статус automation remains open. |
| [CLAUDE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CLAUDE.md) | Agent context file | Раздел `Context files` | Agent-visible project memory, commands, template residue risk | Использован как example of context surface, not as source of truth over Constitution/spec/plan. |
| [PAPER.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md) | Repository paper draft | Workflow loop and image candidate | Three-phase workflow with feedback loop | Non-canonical against arXiv PDF; image needs rights/canonicality check. |
| [Spec Kit README](https://github.com/github/spec-kit) | Tool documentation | Spec Kit connection and commands | command names, `.specify/memory/constitution.md`, artifact chain | Freshness-sensitive; verify current commands later. |
| [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) | Methodological note | Spec-driven context | `spec -> plan -> tasks -> implement`, templates as LLM behavior constraints | Not a security-CSDD source; used for wider SDD mechanics. |
| [Spec Kit constitution command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/constitution.md) | Command template | Template drift and Sync Impact Report | dependent template review after Constitution changes | Freshness-sensitive. |
| [Spec Kit plan command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md) and [plan-template.md](https://raw.githubusercontent.com/github/spec-kit/main/templates/plan-template.md) | Command/template source | Plan gate mechanics | Constitution Check before/after design, downstream artifact creation | Freshness-sensitive. |
| [Spec Kit tasks command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/tasks.md) and [tasks-template.md](https://raw.githubusercontent.com/github/spec-kit/main/templates/tasks-template.md) | Command/template source | Task generation and task-level trace | ID/path/story/increment requirements and task chain | Freshness-sensitive. |
| [Spec Kit analyze command](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md) | Command source | Human gate before implementation | Read-only consistency analysis and CRITICAL conflicts with MUST principles | Freshness-sensitive. |
| [Spec Kit Issue #697](https://github.com/github/spec-kit/issues/697) | Public issue | Gate failure examples | missing downstream artifacts, optional CI despite Constitution requirement, reverse mapping problem | Public feedback, not official doctrine. |
| [Spec Kit Issue #40](https://github.com/github/spec-kit/issues/40) | Public issue | Unknown authorship / copied Constitution risk | user uncertainty over how to create Constitution | Public feedback, not official doctrine. |
| [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) | Practical guide | Threat-model-first, context files, PR-template, enforcement path, runtime caveat | operational details for `constitution.md` to compliance | Not replication of Marri metrics; kept separate. |
| [DocGuard repository](https://github.com/raccioly/docguard) | Community extension/tool | Guard/trace/diagnose examples | structured gate, reverse trace, CI-readable output, agent context generation | Not security scanner and not proof of CSDD; extension requires trust review. |
| [docguard-cli PyPI](https://pypi.org/project/docguard-cli/0.24.0/) | Package metadata | Companion ledger only | distribution surface for DocGuard | Not used for article claims beyond possible later freshness check. |
| [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html) | Official community catalog | Trust boundary of extensions | community extension warning and extension categories | Catalog entry is not an audit or endorsement. |
| [Cisco Foundry Security Spec](https://github.com/CiscoDevNet/foundry-security-spec), [Foundry README](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/README.md), [Foundry spec.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/spec.md), [Foundry constitution.md](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) | Neighbor source | Foundry section, priority rule, evidence gates, lifecycle repair | Constitution priority over spec/plan/tasks, `[NEEDS CLARIFICATION]`, principle->FR coverage, evidence over assertion | Neighbor example; not Marri replication. |
| Project CodeGuard | Deferred neighbor context, not cited in the public article | Not used as direct CSDD evidence after P23 sync | Could matter only if a future Foundry/neighbor article expands that branch | Do not track as a blocker for this article. |
| `C5_theory_to_technical_atlas.md` and `C5_concept_atlas_article_map.md` | Internal theory fragments | Article structure and theory-link direction | Concept-first article contract and Constitutional SDD registry role | Not cited in public article. |
| `A10_mode_selection_map.md` | Internal theory fragment | Theory-link framing | Evidence, authority, lifecycle repair, choosing sufficient external structure | Not cited in public article. |

## P02 boundary sources added

| Источник | Тип | Где использован | Что поддерживает | Ограничение |
|---|---|---|---|---|
| [Spec Kit documentation](https://github.github.com/spec-kit/) and [spec-driven.md](https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md) | Neighbor method/tool source | `О чём говорит эта статья и что остаётся рядом` | Spec Kit as repo workflow and artifact chain, not CSDD itself | Freshness-sensitive; avoid turning article into Spec Kit tutorial. |
| [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) and [OpenSPDD design philosophy](https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md) | Neighbor method source | Boundary with SPDD | SPDD as structured prompt/REASONS intent management | Used only for boundary, not as CSDD evidence. |
| [Kiro Specs](https://kiro.dev/docs/specs/) and [Feature Specs](https://kiro.dev/docs/specs/feature-specs/) | Neighbor product/method source | Boundary with Kiro | Kiro as product specification surface with requirements/design/tasks | Freshness-sensitive product surface. |
| [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | ADR primary source | Boundary with ADR | ADR as memory of architectural decision and consequences | Used only for contrast. |
| [Test-Driven Agentic Development](https://arxiv.org/html/2603.17973v2) | Neighbor evidence/test method source | Boundary with TDAD/evidence layer | Tests/test-impact as evidence-oriented control | Used only for contrast; not evidence for CSDD. |

## P03 source inventory note

P03 did not add new public article claims and did not open additional sources beyond the allowed dossier/article/companion inputs. It classified the existing dossier material into transferred material, deferred material, primary-source checks and technical-anchor gaps. The main article was left unchanged because no article-critical omission required immediate insertion.

Key inventory outcomes:

- Marri/ar5iv/PDF and reference repo remain the primary source-depth targets.
- `CONSTITUTION_COMPLIANCE.md` automation, task-level traceability, client-side security coverage and visual rights are the main technical gaps.
- Spec Kit, Mad Devs, DocGuard and Foundry remain supporting/neighbor sources with separate evidence levels.
- Full Foundry roles, DocGuard release metadata and Handbook checklists were deliberately deferred; Project CodeGuard is no longer a blocker for this article because it is not cited in the public text.

## P04 source-depth usage note

P04 added a source-depth distinction inside the article: Marri/ar5iv/PDF are used as the academic framing and evaluation layer, while the reference repository files are used as the executable or inspectable workflow layer. No new external sources were introduced; the pass reused existing primary links already present in the article/source usage.

The article now treats the following as repository workflow anchors: `.specify/memory/constitution.md`, `spec.md`, `plan.md`, `tasks.md`, `CLAUDE.md`, `CONSTITUTION_COMPLIANCE.md`, code and scripts. The article treats figures, paper metrics, Table 3 and the 73% claim as explanatory/evaluative material, not executable gates.

## P05 source-depth usage note

P05 expanded the article's concrete artifact map without adding new external sources. It reuses existing source classes:

- reference repository files for concrete surfaces (`.specify/memory/constitution.md`, `spec.md`, `plan.md`, `tasks.md`, `CLAUDE.md`, `CONSTITUTION_COMPLIANCE.md`);
- Spec Kit/Mad Devs/DocGuard context for generic context-file and gate surfaces;
- the main Marri/ar5iv source for why these artifacts matter.

The added table distinguishes artifact role, minimum content, state to verify and expected output. Claims that are not directly confirmed in the reference repo are phrased as expected CSDD surfaces, not as facts about the demo repository.

## P06 compliance-matrix / traceability usage

P06 did not add new external sources; it re-used already registered primary and neighbor sources to make matrix/traceability operational in the article.

| Источник | P06 use | Claim supported | Limitation |
|---|---|---|---|
| [ar5iv §5.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1) and [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | New section `Как матрица ограничивает работу до слияния` | Principle/CWE/file/line/technique mapping must constrain plan, tasks and review, not only summarize them | Exact line ranges and automation claim still need final primary-source verification. |
| [Spec Kit Issue #697](https://github.com/github/spec-kit/issues/697) | Same section | `PASS`/analysis can be weak if downstream artifacts or task-to-constitution mapping are absent | Public issue; not official Spec Kit doctrine. |
| [tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md) | Same section | Task-level traceability can weaken when `SEC-*`/CWE disappear from task text | Used as caution, not as proof that implementation is invalid. |
| [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) | Same section | PR-template and `traceability.md` keep matrix updates tied to change/review | Practical guide, not Marri metric replication. |
| [DocGuard README](https://github.com/raccioly/docguard) | Same section | Reverse trace is a useful tool requirement for checking code back to requirements/tasks/Constitution | Neighbor tooling example; not a security scanner. |
| [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) | Same section | Constitution changes should trigger `principle -> enforcing FRs` coverage and block on `GAP` in a neighboring Spec Kit-compatible process | Neighbor example; not Marri replication. |

## P07 boundary/source-depth usage — Spec Kit and security documentation

P07 added no new sources. It re-used registered sources to make the article's layer boundary more explicit.

| Источник | P07 use | Claim supported | Limitation |
|---|---|---|---|
| [Spec Kit spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md) | New section `Как CSDD ложится поверх спецификационного процесса` | General SDD workflow treats specification/plans as primary artifacts | Used only as workflow baseline, not as security-CSDD evidence. |
| [ar5iv §3.1–3.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | Same section | CSDD adds Constitution as higher security/governance layer over feature artifacts | Final PDF/ar5iv sync remains open. |
| [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) | Same section | Neighbor example of Constitution priority over downstream artifacts | Neighbor source; not Marri replication. |
| [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) | Same section | Security documentation becomes operational only when it reaches agent instructions, traceability, PR/CI/review gates | Practical guide, not empirical replication. |
| [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Same section | ADR records a decision and consequences; it does not replace policy/Constitution | Boundary source only. |

## P08 limits/caveats usage

P08 did not add new external sources. It re-used existing sources to make limits and false-confidence modes explicit.

| Источник | P08 use | Claim supported | Limitation |
|---|---|---|---|
| [ar5iv §6.1](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | New section `Где CSDD может дать ложную уверенность` | Vague principles are weaker; specific CWE/control and implementation patterns improve enforceability | Must be final-checked against PDF. |
| [Foundry Constitution](https://raw.githubusercontent.com/CiscoDevNet/foundry-security-spec/main/constitution.md) | Same section | `Evidence Over Assertion` as neighbor warning against matrix overconfidence | Neighbor source, not Marri replication. |
| [Mad Devs guide](https://maddevs.io/writeups/practical-security-layer-for-spec-driven-development/) | Same section | Security policy must connect to enforcement path, review or traceability | Practical guide, not empirical evidence. |
| [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | Same section | Compliance report is useful but automation remains open until generator/reproducibility are verified | Do not overclaim as proven automated gate. |
| [reference Constitution](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md) | Same section | Governance and amendment remain human-controlled responsibilities | Reference repo may be broader than compact paper model. |

## P09 free expansion — context selection / пакет конституционных ограничений

Editorial gap chosen: the article explained context files but did not show how the agent should receive a task-sized subset of Constitution. P09 added a task-local package of constitutional constraints to turn Marri's context-selection result into an operational artifact; the public article now uses the Russian term `пакет конституционных ограничений`.

| Источник | P09 use | Claim supported | Limitation |
|---|---|---|---|
| [ar5iv §6.2](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | Раздел `Что дать агенту из Constitution для одной задачи` | Full 15-principle context underperformed relevant 3–5 principle selection; context selection is an engineering step | Final PDF verification still needed. |
| Existing matrix examples from [ar5iv §5.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1) and [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | Same section | Required implementation pattern and evidence expectation fields | Examples are illustrative; exact line ranges remain a verification debt. |

## P10 free expansion — reader path through one feature

Editorial gap chosen: the article had many artifacts and caveats, but reader path through a single change was still too fragmented. P10 added a transfer-endpoint walkthrough to connect Constitution, spec, plan, tasks, context selection, matrix and repair loop.

| Источник | P10 use | Claim supported | Limitation |
|---|---|---|---|
| [ar5iv §5.2](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | New section `Сквозной пример...` | Transfer endpoint qualitative example: `Decimal`, positive amount, maximum, two decimals, no transfer to same account | Verify exact wording in PDF before publication. |
| [spec.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/spec.md) | Same section | User stories and edge cases as feature-spec surface | Used as workflow example, not full banking-domain audit. |
| [plan.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/plan.md) | Same section | Tech choices and Constitution Check as planning surface | Existing plan-drift caveat remains. |
| [tasks.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/specs/001-banking-crud/tasks.md) | Same section | Tasks for validation/auth/service/data/test work | Task-level `SEC-*` trace remains weak/open. |

## P11 local visual asset usage

| Asset/source | Type | Where used | What supports | Limitation |
|---|---|---|---|---|
| `content/assets/theory-images/fowler-sdd-overview.png` / [Martin Fowler, Exploring Generative AI](https://martinfowler.com/articles/exploring-gen-ai.html) | Local ready image asset | `Как CSDD ложится поверх спецификационного процесса` | Generic SDD context: agent works with project memory and specs | Used only as general SDD background; not evidence for CSDD, Marri metrics, Constitution, compliance matrix or security claims. |

## P12 external visual candidate pass

P12 normalized the inline external-real-candidate captions and confirmed the disposition of dossier-listed CSDD visual candidates. No external images were downloaded.

| Candidate/source | P12 decision | Article location | Limitation |
|---|---|---|---|
| ar5iv/PDF Figure 1 | Inline external-real-candidate retained with public caption | Introduction | Needs rights/download/quality/PDF check. |
| ar5iv/PDF Table 1 | Inline external-real-candidate retained with public caption | Compliance matrix section | Table may be better as a redrawn local table after rights/readability decision. |
| `PAPER.md` Figure 4 | Inline external-real-candidate retained with public caption | Workflow section | Non-canonical relative to arXiv/PDF; rights/canonicality check needed. |
| ar5iv/PDF Figure 2 | Queue only | Metrics/caveats area, not inline | Deferred so metrics do not dominate the concept article. |
| README diagrams from reference repo | Rights hold / queue only | Not inline | README license caveat prevents inline use before explicit rights decision. |
| Mad Devs / DocGuard / Foundry workflow ideas | Deferred as synthetic/editorial ideas, not external image queue additions | Not inline | Would need original diagrams; do not copy source graphics by default. |

## P13 synthetic visual pass

No synthetic figure was added in P13. The article already has one local SDD context image and three high-priority external-real CSDD candidates; adding a synthetic diagram now would either duplicate the prose tables or risk replacing source visuals. Candidate synthetic ideas were left deferred in the image plan.

## P14 standalone concept reinforcement

P14 added a minimal vocabulary section to make the article self-contained for a reader arriving directly at Constitutional SDD.

| Источник | P14 use | Claim supported | Limitation |
|---|---|---|---|
| [ar5iv §3.1–3.4](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | `Минимальный словарь этой статьи` | Constitution/spec/plan/tasks/matrix as CSDD artifact chain | Final PDF verification remains open. |
| [reference Constitution](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/.specify/memory/constitution.md) | Same section | Constitution as project policy artifact with governance/change process | Repo Constitution is broader than paper model. |
| [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | Same section | Matrix/traceability as link between principles and implementation evidence | Generator/reproducibility remains open. |
| C5 atlas fragments | Companion/theory framing only | Standalone concept-first article contract | Internal theory source, not cited in public text. |

## P15 concept reinforcement — mechanism, boundaries, embedded failure modes

P15 added no new source families. It re-used existing registered sources to remove the standalone `Типовые сбои` catalog and embed the same risks into the mechanism: Constitution definition, workflow transfers, `spec/plan/tasks`, matrix/evidence, context files, human gates and caveats.

| Источник | P15 use | Claim supported | Limitation |
|---|---|---|---|
| [Spec Kit Issue #40](https://github.com/github/spec-kit/issues/40) | Constitution section | Copied or unclear Constitution authorship is a practical risk; a template is not enough for CSDD authority | Public issue, not official doctrine. |
| [PAPER.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/PAPER.md) | Workflow section | Compliance failures can return to prompt/spec/plan/tasks, not only code | Repository paper is non-canonical until checked against arXiv/PDF. |
| [Spec Kit Issue #697](https://github.com/github/spec-kit/issues/697) | `spec/plan/tasks` and human gates | `PASS` text without downstream artifacts is a weak gate | Public issue, not official doctrine. |
| [CONSTITUTION_COMPLIANCE.md](https://raw.githubusercontent.com/srinivasraom/banking-ms-by-constitution/001-banking-crud/CONSTITUTION_COMPLIANCE.md) | Matrix/evidence caveat | Auto-generated compliance claim remains useful but open until reproducibility is verified | Do not present as proven automated enforcement. |
| [reference README](https://github.com/srinivasraom/banking-ms-by-constitution) | Matrix/evidence caveat | Client/runtime blind spots, including JWT in `localStorage`, require separate coverage review | Used only as a caution, not as a concluded vulnerability. |
| [ar5iv §6.1, §6.5](https://ar5iv.labs.arxiv.org/html/2602.02584v1) | Context files section | Specification/context files should be treated as security-critical artifacts | Final PDF verification remains open. |
| [Spec Kit Community Extensions](https://github.github.io/spec-kit/community/extensions.html) | Human gates section | Community extensions are independently maintained and not audited/supported/endorsed by maintainers | Freshness and exact wording should be rechecked. |

## P16 theory-link usage

P16 used internal theory fragments only for framing and semantic back-links. They are not cited in the public article as factual sources.

| Internal fragment | P16 use | Claim / question supported | Public article limitation |
|---|---|---|---|
| `00_spine_map.md` | Revised final theory section and `theory_links` | CSDD as one lifecycle case of preserving intent, evidence, responsibility and repair across a software change | Do not restate the whole spine inside the article. |
| `A3_specification_methodologies_synthesis.md` | `theory_links` and final section | CSDD belongs to specification layer by making Constitution the governable object above feature specs | Keep detailed methodology comparison out of main article. |
| `A5_process_methodologies_synthesis.md` | `theory_links` and final section | Working process vs process imitation: the rule must change the next allowed action | Keep process theory as backlink, not a new section. |
| `A7_observation_vs_evidence.md` | `theory_links` and final section | Matrix rows need evidence for human acceptance; trace alone is not enough | Do not turn CSDD into TDAD/evidence-layer article. |
| `A9_lifecycle_repair.md` | `theory_links` and final section | Constitution amendments trigger repair of downstream artifacts and context | Keep repair scoped to CSDD artifacts. |
| `C5_theory_to_technical_atlas.md` | `theory_links` | Technical atlas article should be standalone and source-specific, not a full theory rewrite | Preserve concept-first article contract. |
| `A10_mode_selection_map.md` | `theory_links` and final section | CSDD is a heavier mode chosen when durable policy, agent context, evidence and repair matter | Do not present as universal default. |


## P17 языковой проход 1

P17 не добавлял новых фактических источников. Использованы только языковые протоколы пакета и уже зарегистрированные источники. Фактура, ссылки и ограничения остались на прежних местах; изменён только пользовательский слой формулировок.

| Изменение | Источниковый эффект | Ограничение |
|---|---|---|
| `AI-assisted code generation`, `prompt`, `endpoint`, `runtime`, `traceability`, `evidence`, `compliance pass`, `audit table` и похожие англоязычные связки переведены в естественный русский текст. | Новых source claims нет; это редакционная нормализация переноса англоязычных источников. | Имена продуктов, файлов, команд, исходные source labels и точные статусы/принципы в кодовых фрагментах сохранены. |
| Старый гибридный packet-термин заменён в публичном тексте на `пакет конституционных ограничений`. | Термин теперь описывает механизм без лишнего англоязычного псевдотермина. | `Constitution` сохранён как имя артефакта CSDD. |
| Статусы внешних изображений и очередь визуального прохода русифицированы без изменения решений P11–P13. | Очередь изображений не изменилась. | Права, загрузка и проверка качества остаются долгами будущего asset-прохода. |

## P18 языковой проход 2

P18 не добавлял новых источников и не менял доказательную силу уже зарегистрированных источников. Правка касалась второго языкового прохода: заголовков, подписей, таблиц, нижней очереди изображений и link labels, где английская форма не была названием источника.

| Область | Что изменено | Источниковое ограничение |
|---|---|---|
| Публичные link labels | `reference Constitution`, `reference repository`, `reference README`, `Spec Kit documentation`, `analyze command` заменены на русские рабочие подписи. | URL, источник и поддерживаемые claims не менялись. |
| Inline prose | `Figure 1, Table 3` в объяснительном предложении переведено как рисунок/таблица, потому что это не служебный source field. | В нижней очереди источниковые labels `Figure 1`, `Table 1`, `Figure 4`, `Figure 2` сохранены как точные указатели на источник. |
| Технические термины | `diff`, `pull request`, `guard-инструмент` заменены на русские объяснения там, где точная английская форма не нужна. | `PR`, `CI`, имена команд, файлов, принципов и статусы вроде `external-real-candidate` сохранены как рабочие технические формы. |

## P19 редакторский проход 1

P19 не добавлял новых источников. Добавлены две редакторские связки на основе уже перенесённого материала: ранняя проверка «пройдите одно правило от Constitution до свидетельства» и отдельный раздел о случаях, когда CSDD оправдан. Эти тезисы синтезируют уже зарегистрированные источники и теоретические границы, а не вводят новую фактуру.

## P20 редакторский проход 2

P20 не добавлял новых источников. Правка уточнила уже существующие тезисы: заголовок матрицы больше не обещает, что намерение само «становится свидетельством»; публичный текст убрал след внутреннего черновика; финальная теория сокращена, чтобы не дублировать новый раздел о применимости CSDD.

## P21 редакторский проход 3

P21 не менял источники и фактические утверждения. Правка касалась навигации статьи: уточнены три заголовка, чтобы они звучали как самостоятельные рабочие разделы, а не как временные редакторские формулы.

## P22 structure / entry-sequence pass

P22 не добавлял источники. Правка изменила публичную структуру: Figure 1 перенесена после reader question и короткой проверки CSDD, чтобы первый экран оставался problem-first; подписи к Figure 1 и Figure 4 очищены от редакторской формулы `для этой статьи`; нижний раздел переименован в `Внешние изображения для asset-pass`.


## P23 companion sync

- Новые источники не добавлялись; файл приведён в соответствие с фактической публичной статьёй.
- CodeGuard оставлен только как отложенный соседний контекст и больше не числится blocker для текущей статьи, потому что публичный текст его не цитирует.
- Терминология `пакет конституционных ограничений`, визуальные места и source roles синхронизированы с P22/P23 структурой.

## P24 style-defect sync

- Новые источники не добавлялись, ссылки и доказательная база сохранены.
- Названия разделов синхронизированы с публичной статьёй: `Карта артефактов...` и `Как матрица ограничивает работу до слияния`.
- Стилевые правки убрали псевдотермины вроде «петля ремонта», «проверочная поверхность», «карта намерения/реализации/проверки» без изменения фактуры.

## P25 selective natural rewrite sync

- Новых источников, фактов и ссылок не добавлялось.
- Публичный текст точечно очищен от оставшихся искусственных формул: `карта полномочий`, `путь принудительного исполнения`, `трасса соответствия`, Fieldbook-англицизм в нижней очереди.
- Source usage остаётся прежним: правка изменила русский текст, а не доказательную базу.

## P26 guarded final style pass

P26 не добавлял новых источников и не менял доказательную силу уже зарегистрированных источников. Правка выровняла публичные заголовки и несколько формулировок вокруг приоритета Constitution, матрицы, контекстных файлов, Foundry и финальной связи с SDLC с ИИ.

| Область | Что изменено | Источниковое ограничение |
|---|---|---|
| Заголовки публичной статьи | Несколько технически точных, но тяжёлых заголовков заменены на более естественные русские формулировки. | Источники, claim coverage and article order unchanged. |
| Стиль вокруг приоритета Constitution | `полномочие`, `путь принудительного исполнения`, `трасса` и похожие тяжёлые обороты в публичном тексте заменены на приоритет, связь с проверкой и след соответствия. | Это языковая правка, не новая интерпретация источников. |
| Figure captions | Подписи Figure 1 и Figure 4 уточнены без изменения статуса изображений. | Все external-real-candidate debts preserved. |
