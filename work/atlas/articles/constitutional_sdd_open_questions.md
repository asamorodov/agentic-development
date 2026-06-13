# constitutional_sdd — open questions

Статус: P26 guarded final style sync. Открытые вопросы сохранены; финальный стиль-проход не добавил source-depth или visual blockers.

## Source freshness and versioning

1. Проверить текущую страницу arXiv: есть ли версия позднее `v1` от 31 января 2026 года, изменились ли DOI/status/metadata.
2. Сверить ar5iv с PDF для таблиц, figure captions, threats to validity and future work.
3. Проверить текущий статус `banking-ms-by-constitution`: commits, issues, PRs, releases, license wording, branch names.
4. Проверить свежесть Spec Kit command/template sources: `/speckit.constitution`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, `.specify/memory/constitution.md`.
5. Проверить текущую версию Mad Devs guide and whether content/date changed.
6. Проверить DocGuard repository, PyPI release, license, GitHub Action behavior, write permissions, and community-extension listing.
7. Проверить current status, license, contributing/security docs, releases/issues/changelog для Foundry, если соседний раздел будет расширяться; CodeGuard не является текущим blocker для этой статьи.

## Method and evidence

1. Уточнить отношение между `15 principles`, `10 CWE vulnerabilities in scope` and broader raw reference Constitution.
2. Проверить, насколько `CONSTITUTION_COMPLIANCE.md` действительно auto-generated and by which tool.
3. Сверить exact line ranges and techniques in compliance matrix before final article.
4. Решить, как использовать 73% reduction: main text, cautious note, side box, or companion only.
5. Проверить client-side security coverage: JWT tokens in `localStorage`, CORS/origin rules, sensitive data in frontend logs, and whether compliance matrix covers these decisions.
6. Проверить whether task-level weakening is offset by `.claude/commands`, `CLAUDE.md`, or other context files.
7. Проверить whether `plan.md` Structure Decision vs Constitution Check is real drift, shorthand, or acceptable adaptation.
8. Проверить issue #697 and #40 statuses/comments before final use as public-feedback examples.

## Visual and rights

1. Download/rights/quality check ar5iv Figure 1 and Table 1.
2. Decide whether ar5iv Figure 2 belongs inline or only in source notes.
3. Check `PAPER.md` Figure 4 rights and canonicality against arXiv PDF.
4. Resolve README diagram rights; current source slice says `Private - All rights reserved`.
5. Decide whether to create original synthetic diagram of `constitution -> spec -> plan -> tasks -> code -> compliance matrix`.
6. Decide whether Foundry evidence gate deserves a small original figure in this article or should wait for a separate Foundry article.

## Article structure

1. Later passes should deepen technical anchoring without turning the article into a Spec Kit tutorial.
2. Keep Marri, Mad Devs, DocGuard and Foundry at different evidence levels.
3. Add more concrete snippets or tables only when they help answer the reader question.
4. Re-check language after translation/style passes: avoid slogans like “security by construction” unless tied to mechanism.

## P02 boundary follow-ups

1. Cross-check final article against future Spec Kit article so command/workflow detail remains local to CSDD enforcement, not a duplicate tutorial.
2. Cross-check final article against future SPDD article so structured prompt / REASONS details remain comparison material only.
3. Cross-check final article against ADR article if adding architecture-policy examples; keep ADR as decision memory and Constitution as higher policy constraint.
4. Cross-check final article against TDAD/A7 evidence material: make sure compliance matrix is never presented as sufficient evidence without tests/scanners/review/reproduction.
5. Cross-check final article against PWG material only if long-running compliance repair work becomes central; otherwise do not expand PWG in this article.
6. C5/A10 are already treated as read-only boundary context; only the concrete follow-ups above remain.

## P04 paper/repo separation follow-ups

1. Build a later source-depth checklist that distinguishes paper claims, repository artifacts and package-executable actions.
2. Verify whether `CONSTITUTION_COMPLIANCE.md` has a runnable generator; if not, keep it as report/evidence surface rather than automated gate.
3. When adding any future workflow instruction, cite a repository file or tool command, not the paper diagram alone.
4. When using any future metric from the paper, keep it in evaluation/caveat sections, not as a package acceptance criterion.

## P05 artifact-depth follow-ups

1. Verify exact fields and governance sections in the raw reference Constitution before finalizing the artifact table.
2. Check whether `spec.md` contains direct references to Constitution principles or only indirect security requirements.
3. Check whether `plan.md` has supporting downstream artifacts for its `Constitution Check` claims.
4. Check whether `tasks.md`, `CLAUDE.md` or `.claude/commands` carry principle-level constraints into agent execution.
5. Find whether the reference repo has explicit override/exception records; if not, keep override guidance as method requirement, not repo fact.
6. Decide whether the artifact table belongs in main article permanently or should become a condensed sidebar after style passes.

## P06 compliance/traceability follow-ups

1. Verify exact columns and examples in ar5iv Table 1 against the PDF before final publication.
2. Confirm whether `CONSTITUTION_COMPLIANCE.md` has a reproducible generator; if not, describe it as a report/matrix, not an automated enforcement gate.
3. Decide whether final article should require `SEC-*`/CWE annotations inside `tasks.md` or allow an equivalent recovered trace through context files and analysis tools.
4. Check whether PR-template, CI or review artifacts exist in the reference repo; if not, keep PR/review guidance sourced to Mad Devs rather than Marri.
5. Determine whether a future synthetic figure should show matrix pressure on `plan.md`, `tasks.md`, PR/review and amendment sync.

## P07 boundary follow-ups

1. Re-check the final CSDD article against the future Spec Kit article so the CSDD piece keeps only the command/workflow detail needed for constitutional enforcement.
2. Re-check the ADR boundary if future examples cite concrete authorization, persistence or observability decisions; ADR should remain decision memory, not policy layer.
3. Decide whether “security documentation becomes CSDD only when it changes action” should become a reusable atlas criterion for other security-method articles.
4. Verify whether any final public text should use the English phrase `policy layer` or translate it consistently as `слой политики` / `слой полномочий`.

## P08 limits/caveats follow-ups

1. Verify exact wording of Marri's limitations around vague principles, access control for Constitution artifacts and human review before final publication.
2. Decide how strongly to state that a matrix row requires test/scanner/review evidence when the original Marri Table 1 emphasizes file/line/technique.
3. Keep `CONSTITUTION_COMPLIANCE.md` automation as unresolved until a generator or reproduction path is confirmed.
4. Check whether final article should include a compact “false confidence checklist” or keep the full table.
5. Preserve the claim that responsibility remains human-owned; do not let later tool passes imply autonomous security assurance.

## P09 context-selection follow-ups

1. Verify the exact ar5iv/PDF wording around 78%, 96% and 91% compliance for full, relevant and hierarchical context selection.
3. Check whether the reference repo's `.claude/commands` or `CLAUDE.md` already implements a similar task-local selection pattern.
4. Define how a reviewer should approve omitted principles when only 3–5 are passed to the agent.

## P10 reader-path follow-ups

1. Verify the transfer-endpoint qualitative example against the arXiv PDF and decide whether to keep every numeric detail inline.
2. Check exact `spec.md` edge cases and `tasks.md` task IDs for the transfer/account flow before final publication.
3. Decide whether the walkthrough should remain in the main article or become a sidebar/example box.
4. If a visual pass happens, consider an original one-feature trace diagram instead of more external screenshots.

## P11 visual follow-ups

1. In final visual review, confirm that `fig-sdd-context-memory-and-specs` does not over-emphasize generic SDD relative to CSDD-specific source visuals.
2. Verify final site path rewriting for `../../../content/assets/theory-images/fowler-sdd-overview.png` if the atlas build expects `assets/...` URLs.
3. Keep real Marri/repo figures and Table 1 as higher-priority visual candidates for future asset-pass work.

## P12 external visual follow-ups

1. Download or screenshot Marri Figure 1 and Table 1 only after rights/readability/PDF checks.
2. Decide whether Table 1 should become a redrawn local table with attribution rather than an image capture.
3. Compare `PAPER.md` Figure 4 against the arXiv/PDF workflow before treating it as canonical.
4. Keep README diagrams on rights hold until license/permission is resolved.
5. If Mad Devs/DocGuard/Foundry visuals are needed, draw original synthetic diagrams from facts instead of copying source graphics.

## P13 synthetic visual follow-ups

1. Reconsider a diagram for the task-local package of constitutional constraints only after source figures are localized and the layout shows whether another explanatory visual is needed.
2. If the transfer walkthrough becomes central, consider an original one-feature trace diagram; do not create it merely for visual variety.
3. Keep synthetic diagrams subordinate to real Marri/repo figures and traceability table.

## P14 standalone-article follow-ups

1. In the style pass, decide whether the minimal vocabulary should remain as its own section or be folded into the opening reader question.
2. Ensure vocabulary uses consistent Russian equivalents for `policy layer`, `traceability`, `context files` and `compliance matrix` without making filenames/commands artificial.
3. Check that standalone explanations do not expand into a general theory recap.

## P15 mechanism/failure-mode follow-ups

1. Re-check that final structure no longer has a separate failure catalog; limitations should remain embedded in Constitution, workflow, matrix, context and gate explanations.
2. Verify exact Marri wording for treating specification/context artifacts as security-critical and for prompt-injection/integrity risks.
3. Confirm whether `CONSTITUTION_COMPLIANCE.md` has a reproducible generator before any wording implies automated enforcement.
4. Review the `localStorage` JWT note as a client/runtime coverage question, not as a settled vulnerability claim.
5. Decide whether the phrase “what next action changed because of this rule?” should become a reusable atlas criterion for policy-layer methods.
6. Re-check Spec Kit issue #40/#697 and community-extension page before final publication because those are public-feedback/tooling-status sources rather than stable primary doctrine.

## P16 theory-link follow-ups

1. In the final structure pass, verify that the main article's theory section stays local and does not restate A3/A5/A7/A9/A10.
2. Check whether `theory_links` semantic back-links should be mirrored in an atlas registry/navigation file outside this article package.
3. Keep the mode-selection statement cautious: CSDD is justified for durable cross-feature security/policy constraints, not as a default for every feature.
4. Confirm that the evidence language stays compatible with the eventual TDAD/evidence article and does not claim matrix rows are sufficient without independent checks.


## P17 language-pass follow-ups

- Термин P09 для task-local subset of Constitution resolved for public text: use `пакет конституционных ограничений`; keep `Constitution` when naming the governing artifact.
- В следующем языковом проходе можно дополнительно решить, нужно ли переводить оставшиеся source labels `Figure 1`, `Table 1`, `reference Constitution` в link labels, но это не влияет на аргумент статьи.
- Проверить финальную типографику кавычек и падежи после следующего содержательного прохода.

## P18 — вопросы после языкового прохода

- После P18 новых фактических вопросов не появилось.
- Перед публикацией можно отдельно решить редакционный вопрос: оставлять ли `Figure/Table` в поле источника как точные указатели или дублировать русской формой в скобках. Сейчас сохранена точная форма источника.
- Остаётся долг будущего визуального прохода: загрузка, проверка прав и проверка качества для Marri Figure 1, Marri Table 1, `PAPER.md` Figure 4 и отложенных кандидатов, которые пока живут только в очереди.

## P19 — редакторские вопросы

- Проверить в финальном проходе, что раздел `Когда CSDD оправдан` не звучит как универсальная рекомендация внедрять CSDD в любом проекте.
- Убедиться, что ранняя проверка «правило от Constitution до свидетельства» не дублирует, а именно подготавливает последующие разделы о матрице, контексте и гейтах.

## P20 — редакторские вопросы

- В финальном проходе проверить, что новая формулировка раздела о матрице везде удерживает границу: трасса связывает намерение со свидетельством, но не заменяет само свидетельство.
- Проверить, не осталось ли в публичном тексте внутренних следов черновика или названий проходов.

## P21 — редакторские вопросы

- В финальной проверке пройти оглавление целиком: заголовки должны образовывать путь от вопроса читателя к применимости, ограничениям и сопровождению после слияния.
- Проверить, что ссылки companion-файлов на разделы статьи не расходятся с новыми названиями.

## P22 — вопросы структуры входа

- В финальной сборке проверить, как выглядит первый экран после переноса Figure 1: читатель должен увидеть проблему и reader question до визуального placeholder.
- Проверить, что нижний раздел `Внешние изображения для asset-pass` не попадёт в пользовательскую публикацию, если публикационная система ожидает хранить asset-pass queue только в companion-файле.


## P23 companion sync

- Удалён решённый терминологический долг вокруг старого packet-термина; текущий публичный термин — `пакет конституционных ограничений`.
- C5/A10 больше не записаны как общий sync debt: в списке оставлены только конкретные boundary follow-ups.
- CodeGuard не является blocker для этой статьи; проверка нужна только если будущий отдельный Foundry/neighbor article расширит эту ветку.

## P24 style-defect sync

- Новые открытые вопросы не добавлялись.
- Закрыты только стилевые дефекты публичного текста: тяжёлые псевдотермины, кальки и несколько механических противопоставлений.
- Реальные blockers остаются прежними: source freshness, PDF/ar5iv verification, generator provenance, visual rights/readability, client/runtime and traceability checks.

## P25 selective rewrite sync

- Новые открытые вопросы не добавлялись.
- P25 не менял источники, изображения, границы или технические долги; исправлены только реальные языковые дефекты, оставшиеся после P24.

## P26 guarded final style sync

No new open question was introduced. Existing debts remain: freshness/PDF verification, generator provenance, visual rights/readability, client/runtime coverage and traceability checks.
