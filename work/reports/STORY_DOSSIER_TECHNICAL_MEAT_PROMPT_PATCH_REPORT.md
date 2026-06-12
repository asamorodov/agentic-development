# Story dossier prompt patch — technical episode meat

Изменён только нижний prompt:

```text
work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
```

Цель правки: слегка усилить требование к эпизодам. Теперь worker должен вытаскивать не только цепочку “что было → что сделали → как стало”, а техническое мясо эпизода: конкретную задачу, репозиторий/ветку/issue/PR, команды, файлы, конфиги, prompts, scripts, hooks, CI jobs, UI surfaces, policy texts, промежуточный результат, способ проверки и проверяемое before/after изменение.

TS-код, wrapper и управляющий prompt не менялись.
