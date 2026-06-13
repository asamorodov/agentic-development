# S02 note: `kiro_specs`

## Problems found

- Первичный S01-план был содержательным, но мог привести к обзору возможностей Kiro вместо самостоятельной статьи о Specs как форме AI-driven SDLC.
- Article contract недостаточно явно удерживал различие между product surface and lifecycle mechanism.
- Source-depth priorities needed stronger separation by product layers: Feature Specs, workflow variants, context/execution, verification/control, governance and caveats.
- Visual layer needed stronger emphasis because Kiro is partly a product/UI workflow.

## Decisions

- Preserve the full 25-pass queue.
- Frame Kiro Specs as product-integrated specification surface: requirements/design/tasks become visible and executable within IDE/Web/CLI context.
- Treat Spec Kit, SPDD, TDAD, ADR, PWG and BMAD as boundary checks rather than topics to re-explain.
- Make final gate block generic Kiro overview and UI/command inventory without lifecycle explanation.

## Changes made

- Rewrote `Article contract`.
- Rewrote `Почему очередь подходит статье` with the required judgment: whether the queue fits this article.
- Added `S02 integrated strengthening`.
- Strengthened final verification wording.

No atlas article was written and no article-writing package was built.
