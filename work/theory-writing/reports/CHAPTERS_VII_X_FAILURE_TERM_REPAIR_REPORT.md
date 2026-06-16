# Chapters VII–X — repair of the term `сбой`

Date: 2026-06-15

## Purpose

The user pointed out that `сбой` had become an overused working shortcut in the integrated chapters VII–X. In several contexts it sounded mechanical and unnatural in Russian, especially where the text meant a work problem, a wrong entry into work, an execution error, a process violation, or an unclear cause of a failed check.

This pass did not add new source material and did not change the structure of the chapters. It replaced the term contextually, preserving the argument of each chapter.

## Edited files

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/chapters/X_gas_town_beads.md
```

## Replacement principle

The pass did not use a single mechanical substitute. The chosen Russian phrase depends on the local meaning:

- `главный сбой` → `главная проблема`, when the chapter explains why a layer is needed;
- `интеграционный сбой` → `интеграционная проблема`, when the point is unresolved integration work;
- `инфраструктурный сбой` → `инфраструктурная причина падения`, when the text talks about a failed test/check;
- `сбой неправильного входа` → `проблема неправильного входа`, when the point is choosing the wrong mode of continuation;
- `после сбоя` → `после неудачной попытки`, when the point is runtime retry/continuation;
- `процессные сбои` → `нарушения рабочего процесса`, when the point is a coordination/process problem.

## Verification

A direct scan of the four chapter files after the edit found no remaining `сбо` root occurrences in the chapter text.

No links, figures, source references, or chapter structure were changed.
