# Site entry point and reading order review note — 2026-06-17

## Problem

The site historically grew from Developer Workflow Stories and therefore tends to present stories early. After the corpus split into peer parts — Theory, Atlas, Working Scenarios and Problems/Solutions Catalog — the site may no longer be primarily a story site.

The order of pages matters less for cross-links than for first-contact retention: a reader should quickly find the part that matches their intent before leaving.

## Current hypothesis

The home/orientation layer should not force a single linear path. It should present several entrances:

- understand the conceptual model → Theory / future `Жизненный цикл программного изменения`;
- understand technologies → Atlas;
- choose a work mode → Рабочие сценарии;
- diagnose a failure → Каталог проблем и решений;
- read concrete evidence/cases → Истории.

## Stories

Stories remain important. They provide evidence, texture, and real developer practice. But they may be better positioned as a case corpus / evidence path rather than the default first section for every reader.

## What not to change yet

Do not rewrite site navigation in a small opportunistic edit. A separate navigation package should review:

1. homepage promise;
2. top-level section order;
3. reader personas and entry needs;
4. whether stories are evidence-first, intro-first or optional reading path;
5. cross-link strategy between Theory, Atlas, Working Scenarios, Problems/Solutions and Stories;
6. whether the old public file names (`Handbook`, `Fieldbook`) should be renamed in routes or only in visible titles.

## Working recommendation

Use a reader-oriented front door, not a chronology-of-work front door. Stories should stay prominent, but the first screen should probably advertise the whole corpus rather than imply that the site is only a story collection.


## Cross-story note: dark matter of software

The phrase `dark matter of software` should be routed primarily to Cross-story synthesis rather than to the Atlas layer map. It names a cross-story pattern: AI-assisted development may produce much more internal, personal, one-off, workflow-specific and invisible software than public product markets immediately reveal.

This is useful for the public entrypoint because it helps explain why the visible SaaS/product landscape may understate the real effect of agentic development. But it is not itself a technical layer. Atlas can point to the technologies that enable this pattern; Cross-story should explain the pattern across stories.
