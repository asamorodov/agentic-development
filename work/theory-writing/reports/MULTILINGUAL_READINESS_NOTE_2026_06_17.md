# Multilingual readiness note — 2026-06-17

## Why this note exists

The corpus will likely need a major English version later. The current work is Russian-first, but the repository should stop future translation from becoming a second uncontrolled rewrite.

The important distinction is this:

- Russian prose should remain natural and useful now.
- The repository should preserve enough metadata, terminology and provenance to make a later English version controlled.

## Accepted approach

Do not translate everything now. Do not maintain parallel Russian/English article versions during conceptual construction.

Instead, add a small multilingual layer:

1. stable article/chapter/story IDs;
2. working English titles for major objects;
3. bilingual term registry;
4. translation notes for ambiguous/local terms;
5. package-level translation-readiness check before public stabilization.

## Immediate files

- `work/decisions/ADR-0017-multilingual-corpus-architecture.md`
- `work/multilingual/MULTILINGUAL_CORPUS_PROTOCOL.md`
- `work/multilingual/BILINGUAL_TERM_REGISTRY.md`

## Practical effect on future packages

Atlas packages should add stable article IDs and working English titles. The detailed Atlas map already contains article labels; future updates should gradually add explicit IDs from the bilingual registry.

Theory packages should not become bilingual. They should add translation notes only where a stable concept/title/phrase would be hard to recover in English.

Story packages should preserve source-language provenance: if a story source is in English, later English output should not translate the Russian retelling back into English without checking the original source.

## Risk avoided

Without this layer, English translation would likely produce several failures:

- `Теория`, `Атлас`, `Рабочие сценарии`, `Каталог проблем и решений` would drift into inconsistent English names;
- source-derived technical terms would be translated twice;
- cross-links would break when titles change;
- Russian-only phrases would be over-literalized;
- public English pages would become new essays rather than controlled versions of the same corpus.

## Open decisions

- Final English branding is not decided.
- Site URL structure for multilingual output is not decided.
- Whether English output should be article-by-article translation or a later edited English edition is not decided.
- Whether stable IDs should live in frontmatter for all public pages is not decided, but likely yes.
