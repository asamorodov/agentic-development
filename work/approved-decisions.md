# Approved decisions

## 1. Master title / frame

Approved working title:

> **Агентская разработка и AI-driven SDLC: как меняется жизненный цикл программного изменения**

The phrase AI-driven SDLC must be interpreted as lifecycle-of-change architecture, not as a banal corporate phase list.

## 2. New architecture replaces the “map of currents” top-level structure

The earlier “map of currents” idea remains valuable, but it is demoted from document architecture to analytical/source-map layer. It must not produce a flat catalogue of cases.

## 3. SPDD is a separate part

SPDD is no longer a deep block inside a general “intent” part. It is now a separate part because it is the strongest known methodology-level specification case in the corpus.

## 4. Specification zone is deep

The specification zone consists of:

- Part III — why prompt is too weak as a governance unit;
- Part IV — SPDD as specification lifecycle;
- Part V — Spec Kit, Kiro, TDAD, Constitutional SDD as neighboring deep specification regimes.

Spec Kit, Kiro, TDAD and Constitutional SDD should be treated deeply. They are not throwaway contrast cases.

## 5. Gas Town / Beads is a separate part

Gas Town must return to a full deep case status. The previous compression into one subsection is considered a structural degradation. Gas Town is the deep anchor for organizational/operational lifecycle: roles, Mayor, Beads, durable task state, hooks/GUPP/molecules/wisps, service agents, work identities and the cost of orchestration.

## 6. Baseline restoration rule for SPDD and Gas Town

For SPDD and Gas Town, start from the old site baseline sections unchanged. Then adapt and supplement them. Do not start from the latest expanded synthesis. Do not compress details.

## 7. Expanded theory is quarry, not authority

The latest expanded synthesis is useful for facts, links, source coverage and material. It is not authoritative as prose or structure.

## 8. Source search state

A targeted AI-SDLC source expansion was already done. No new mass source search is required now. Additional search should be targeted only at discovered gaps.

## 9. Codex role

Codex should not be allowed to “just rewrite the theory.” Its role is controlled workflow execution: inventory, dossiers, skeleton, draft rebuild, anti-catalog audit, source-depth repair and anti-degradation checks.

## 10. Human role

The human owner keeps architectural decisions and semantic gates. Human work should not be reduced to manually launching repeated passes or checking file counts.


## 11. Technical atlas is чтение от конкретной концепции

Технический атлас больше не трактуется как узкое приложение для технических деталей. Он становится концептуально-техническим слоем: самостоятельным набором статей с опорой на источники по конкретным концепциям и методологиям. Контролируемое повторение с теорией допустимо, если нужно для самостоятельного понимания статьи атласа. Теория остаётся поперечным SDLC-синтезом; атлас даёт путь чтения от конкретной концепции и не должен становиться ни копией общей теории, ни складом несвязанных деталей.

## 12. Единый корпус знаний и разные разрезы частей

Теория, Атлас, Handbook и Fieldbook работают на одном корпусе знаний по agentic development / AI-driven SDLC, но используют разные организующие разрезы. Теория строится по жизненному циклу изменения; Атлас — по техническим слоям и конкурирующим способам их построения; Handbook — по решениям, которые принимает практик; Fieldbook — по типовым сбоям, диагностике и восстановлению.

Это решение зафиксировано в `work/decisions/ADR-0012-shared-knowledge-genre-cuts.md`. Каждый будущий пакет должен явно указывать не только тему, но и жанр/разрез. Хороший текст, написанный в неверном разрезе, не считается принятым результатом для своей части.

## 13. Git/version-control слой — отдельная статья Атласа

Git и Git-совместимый workflow считаются практической базой современной агентской разработки: branches, worktrees, commits, diffs, patches, PR/MR, review state, merge/revert/rollback и связанные платформенные поверхности образуют основной change-substrate, на который опираются coding agents и review tooling. Это не означает, что другие VCS или Git-compatible слои невозможны, но Атлас и Handbook должны явно показывать, как они соотносятся с Git/PR/CI/review контуром.

В текущем корпусе Git покрыт как внутренний протокол проекта, но недостаточно покрыт как самостоятельный слой agentic development. Решение: сделать отдельную статью Атласа `Git, worktree и PR/MR как субстрат агентского изменения`, а не растворять этот слой внутри CI/review/acceptance tooling. Это зафиксировано в `work/decisions/ADR-0013-git-version-control-agentic-change-substrate.md` и `work/theory-writing/reports/VERSION_CONTROL_AGENTIC_DEVELOPMENT_COVERAGE_NOTE_2026_06_17.md`.


## 14. Атлас равноправен Теории; русские названия рабочих частей

Атлас считается самостоятельной крупной частью корпуса, а не приложением к Теории. Теория и Атлас работают с одной областью знаний, но в разных разрезах: Теория объясняет жизненный цикл изменения, Атлас строит техническую карту слоёв. Поэтому статья Атласа оценивается по собственному критерию technical payload, а не по тому, насколько хорошо она поддерживает теоретический аргумент.

Рабочие публичные названия нижних практических частей меняются в сторону русского языка: `Handbook` лучше называть `Рабочие сценарии` или, при необходимости, `Практикум`; `Fieldbook` лучше называть `Каталог проблем и решений` с уточнением про типовые сбои, диагностику и восстановление. Старые английские ярлыки и имена файлов пока могут сохраняться как техническая история, но новые карты и публичные планы должны использовать русские названия или давать пары.

Это зафиксировано в `work/decisions/ADR-0014-public-corpus-part-names-and-atlas-parity.md`.
