# A7 figure candidates

Этот файл является реестром решений по визуальному слою A7. После repair-pass 2026-06-11 основной фрагмент больше не содержит все кандидаты inline. В текст оставлены только фигуры, которые реально поддерживают несущую границу A7: наблюдение помогает агенту продолжать работу, свидетельство даёт человеку основание принять, отклонить или остановить изменение.

| Кандидат | Asset-класс | Источники фактуры | Решение | Причина |
| --- | --- | --- | --- | --- |
| `fig-a7-observation-to-evidence-chain` | `synthetic_figure` | Основной фрагмент A7; досье TDAD/ADR/PWG; Arvid; Willison; Roast; Stripe | **kept inline** | Главная схема фрагмента: показывает, что формат артефакта сам по себе не делает сигнал свидетельством. |
| `fig-a7-observation-status-ladder` | `synthetic_figure` | Основной фрагмент A7; Arvid; Willison transcripts; Roast logs; Stripe loop | **merged** into `fig-a7-observation-to-evidence-chain` | Дублировала ту же мысль через “лестницу статусов”. Содержательная линия сохранена в прозе и главной цепочке. |
| `fig-a7-working-traces-matrix` | `local_image_asset` candidate / deferred | `content/assets/theory-images/openai-codex-citations-evidence.webp` | **deferred to technical atlas / Codex evidence surface** | Это реальный локальный asset, но в A7 он слишком platform-specific и дублирует общую цепочку свидетельства. Не превращать в текстовую схему. |
| `fig-a7-evidence-type-by-promise` | `synthetic_figure` | Pact Docs; Thoughtworks architectural fitness function; Google SRE Workbook SLO/канареечная проверка; ADR/AWS ревью владельца | **kept inline** | Нетривиально разводит типы обещаний и типы свидетельств; предотвращает формулу “проверки прошли”. |
| `fig-a7-evidence-chain-pwg` | `synthetic_figure` | Основной фрагмент A7; PWG dossier; ADR/AWS/Vercel; Google SRE canary | **kept inline** | Связывает свидетельство с переходом состояния в PWG/ADR/review/rollout, то есть возвращает A7 в общую архитектуру теории. |
| `fig-a7-browser-observation-evidence` | `local_image_asset` | `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp`; Arvid Kahl; browser/DOM/console validation line | **kept inline as `<img>`** | Реальный локальный asset хорошо поддерживает отличие runtime-наблюдения от чтения файлов. Подпись переписана как публичная, без служебного asset-pass текста. |
| `fig-a7-tdad-two-oracles` | `synthetic_figure` / external-real alternatives pending | TDAD A HTML, TDAD B HTML, `tdad-skill`; possible TDAD paper figures in external catalog | **deferred to A3 / technical atlas** | A7 использует TDAD как пример качества проверочного критерия. Отдельная TDAD-схема перегружает A7 и дублирует A3. |
| `fig-a7-adr-confirmation-surface` | `synthetic_figure` | Nygard, MADR, AWS ADR process, Vercel `adr-skill` | **deferred to A2/A9 or technical atlas** | ADR-линия нужна в A7, но отдельная схема начинает выполнять работу A2/ADR-раздела. |
| `fig-a7-showboat-rodney-replay` | `local_image_asset` | `content/assets/story-images/03-simon-showboat-curl-demo.jpg`; Willison Showboat/Rodney | **kept inline as `<img>`** | Реальный локальный screenshot показывает демонстрационный документ как трассу происхождения. Подпись переписана как публичная. |
| `fig-a7-roast-trace-not-truth` | `synthetic_figure` | Shopify Engineering Roast, Doubrovkine Roast run, Shopify/roast PR #868 | **deferred** | Мысль сохранена в прозе: лог рабочего процесса помогает проверить форму работы, но не заменяет владельческое принятие результата. |
| `fig-a7-transcript-status` | `synthetic_figure` | Willison Showboat/Rodney, `claude-code-transcripts` | **merged** into prose and `fig-a7-observation-to-evidence-chain` | Таблица статуса стенограммы дублировала основную цепочку. |
| `fig-a7-stripe-minion-evidence-loop` | `synthetic_figure` | Stripe Minions Part 1/2, AI Engineer transcript, Stripe integration benchmark | **deferred** | Stripe остаётся важным кейсом в прозе; отдельная схема превращала A7 в каталог корпоративных проверочных циклов. |
| `fig-a7-migration-parity-gate` | `synthetic_figure` | Anthropic Code Modernization Playbook, TechChannel/Swimm, Augmented Code | **deferred** | Миграционная линия сохранена в тексте; отдельная схема лучше подходит для technical atlas или будущей главы о migration evidence. |
| `fig-a7-pwg-false-completion` | `synthetic_figure` | PWG dossier; Beads/Taskmaster as needed | **merged** into `fig-a7-evidence-chain-pwg` and final prose | Формула `completed` без пакета свидетельств сохранена как риск преждевременного завершения, без отдельной фигуры. |

## Текущий inline-набор

```text
fig-a7-observation-to-evidence-chain
fig-a7-evidence-type-by-promise
fig-a7-evidence-chain-pwg
fig-a7-browser-observation-evidence
fig-a7-showboat-rodney-replay
```

## Иллюстрационный принцип после repair-pass

A7 не должен становиться галереей проверок, логов, `replay`, SLO, TDAD, ADR и миграций. Основной текст оставляет только те фигуры, которые поддерживают одну из трёх функций:

1. различить наблюдение и свидетельство;
2. показать, что тип свидетельства выбирается по обещанию изменения;
3. связать свидетельство с переходом состояния работы.

Реальные локальные изображения не пересказываются текстом. Если они не нужны основному A7, они остаются в candidate/atlas слое как `local_image_asset`, а не превращаются в синтетический суррогат. Внешние TDAD/SRE/ADR/source diagrams не вставляются без отдельного asset-pass и проверки прав/качества.

## Asset-recovery note 2026-06-11

Для A7 уже существуют локальные source assets:

- `content/assets/theory-images/openai-codex-chrome-devtools-validation.webp` — оставлен inline;
- `content/assets/story-images/03-simon-showboat-curl-demo.jpg` — оставлен inline;
- `content/assets/theory-images/openai-codex-citations-evidence.webp` — отложен для technical atlas / Codex evidence surface, потому что в основном A7 дублирует более общую цепочку свидетельства.

Новые внешние изображения в этом repair-pass не скачивались.
