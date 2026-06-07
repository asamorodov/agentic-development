# Ownership and completion artifacts note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: XI, X, XII.  
Глубина: medium.

## Роль

This note concretizes “completion right”. Operational agency is not completion authority.

## Источники

- SASE and collaborator/assistant sources.
- Open-source AI policy cluster.
- GitHub / GitLab CODEOWNERS.
- Kubernetes OWNERS / approvers/reviewers.
- Review assignment and code ownership empirical sources.
- GitHub governance for agents.

## Основная формула

```text
право исполнять ≠ обязанность ревьюить ≠ право сливать ≠ право выпускать
```

## Артефакты

- CODEOWNERS;
- ownership map;
- review routing;
- approvers/reviewers;
- protected branch;
- required review;
- escalation path;
- release authority;
- audit/provenance record;
- AI-generated contribution policy.

## Почему важно для агентов

Agent can produce code, PR, evidence and fixes. But it does not automatically gain authority to merge or release. In external/open-source context, even useful code can be unwanted review burden.

## Failure modes

1. Disclosure mistaken for permission.
2. AI-generated contribution adds review burden to maintainers.
3. Ownership unclear, so agent picks wrong reviewer or area.
4. Merge authority and release authority collapsed.
5. Human reviewer overloaded by generated output.
6. Audit/provenance missing.

## Где в theory

- Part XI is main home.
- Part X uses review comments and PR description as evidence.
- Part XII uses release authority and incident feedback.

## Что не сжимать

The distinction between action and completion. This is one of the central lines of the theory.
