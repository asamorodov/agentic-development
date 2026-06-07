# Finalize working branch for main

```text
Примени skill `protocols/skills/finalize-working-branch-for-main.md`.

Рабочая ветка: <branch>
Целевая ветка: main

Правила:
- временные материалы из /work не переносить в main;
- если из /work возникло устойчивое решение, правило или prompt, перенести его в /project или /protocols до merge;
- если есть конфликт, неожиданный diff, изменение source precedence, baseline restore rule, deep anchor seeds или риск потери content — остановиться и описать проблему;
- если diff чистый и проверки приемлемы — подготовить PR или merge по репозиторному протоколу.
```


Дополнительное условие: `main` не должен получить папку `/work`; если из `/work` возникли устойчивые документы, перенеси их в постоянные папки перед merge.
