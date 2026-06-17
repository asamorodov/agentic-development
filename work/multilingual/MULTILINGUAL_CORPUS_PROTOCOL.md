# Multilingual corpus protocol

Date: 2026-06-17.

This document defines how the corpus should prepare for a future English version while the current drafting and editing language remains Russian.

## 1. Core position

The current Russian corpus is not a disposable draft. It is the working canonical editorial surface for developing concepts, structure and prose. The future English corpus should be produced from this Russian surface plus the preserved source materials, terminology registry and translation notes.

Do not make Russian prose artificial in order to make it easy to translate. Instead, make the corpus structurally translatable:

- stable IDs;
- preserved source links;
- explicit terminology;
- local translation notes;
- predictable cross-linking;
- clear handling of names, slugs, figures and code.

## 2. Stable IDs and slugs

Every public article, chapter, story and major fragment should eventually have a stable ID that is independent of language. Examples:

```text
atlas-a06-git-change-substrate
atlas-a10-codebase-context-retrieval
theory-xii-pr-acceptance
stories-humanlayer
problems-ci-green-risk-not-covered
```

The title may change in Russian or English; the ID should not change unless the conceptual object itself is split or replaced.

Recommended rule: use stable IDs in maps, attachment files, package plans and cross-reference ledgers. Public localized titles can be resolved from metadata later.

## 3. Language roles

- Russian: current drafting/editing language and main development surface.
- English: future public translation/adaptation target.
- Source language: many primary materials are already English; claims derived from them should preserve enough provenance to return to source wording.

Do not translate English-source claims Russian → English mechanically. Use the Russian text to understand the role of the claim, then return to the source where exact terminology matters.

## 4. Terminology registry

Terms with corpus-level meaning must be recorded in `work/multilingual/BILINGUAL_TERM_REGISTRY.md` or a later structured equivalent.

Each term record should include:

```text
ID / concept
Russian public term
English working/public term
Do not translate as
Scope
Notes
Examples
```

This is separate from ordinary anti-calque cleanup in `protocols/rules/terminology-and-translation.md`. The anti-calque file helps Russian prose. The bilingual registry helps preserve conceptual equivalence across languages.

## 5. Article-level translation notes

For large public-facing articles, add a short `Translation notes` block in the working report or article metadata, not necessarily in the public page.

Use it for:

- terms that are locally coined;
- phrases that have no clean literal English equivalent;
- places where Russian title and English title should not be literal equivalents;
- source-language caveats;
- figures/tables/captions that will need localized text;
- intentional English terms left untranslated in Russian.

## 6. Figures, screenshots, code and UI strings

- Code comments remain English unless the user explicitly requests otherwise.
- Commands, file names, API names and protocol names are not translated.
- Screenshots with English UI can usually be reused in English output; Russian captions may need separate localized captions.
- Synthetic diagrams should avoid baking Russian prose into image assets if an English version is expected; prefer editable captions/labels or maintain source files.
- Tables should keep semantic column IDs where possible so headers can be localized later.

## 7. Cross-links

Do not make the English translation depend on Russian link text. Use stable IDs/slugs in maps and routing documents.

Preferred internal representation:

```text
id: atlas-a10-codebase-context-retrieval
ru_title: Индексация, поиск и извлечение контекста из кодовой базы
en_title: Codebase context retrieval, indexing and search
```

## 8. Package-level gate

When a package stabilizes an article/chapter for public use, add a small `translation-readiness` check:

```text
- stable ID present;
- English working title present;
- key terms checked against bilingual registry;
- source-derived terms preserve provenance;
- local translation notes added where needed;
- cross-links use stable IDs or have an obvious future mapping;
- no accidental Russian-only image/table text without note.
```

This is not a translation pass. It is a future-translation damage-control step.

## 9. What not to do now

- Do not maintain two full language versions during conceptual construction.
- Do not translate every draft as soon as it is written.
- Do not make Russian prose worse by preserving English syntax.
- Do not decide final English branding too early.
- Do not let the future English version erase source links or story/source provenance.

## 10. Minimum next implementation

For the next stabilization cycle:

1. Keep `work/multilingual/BILINGUAL_TERM_REGISTRY.md` updated for corpus-level terms.
2. Add stable IDs and working English titles to the Atlas article map.
3. Add stable IDs and working English titles to the Theory chapter attachment map when chapter packages are rebuilt.
4. Add translation-readiness as a small gate to future article/chapter package templates.
