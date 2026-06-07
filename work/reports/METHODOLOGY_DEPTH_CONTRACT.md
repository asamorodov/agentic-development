# Methodology depth contract

Дата: 2026-06-07  
Статус: **обязательный рабочий контракт перед writing**.  
Основание: пользователь утвердил решение защитить ключевые методологии от сжатого обзорного изложения.

## 1. Зачем нужен contract

После skeleton v4 стало ясно, что архитектура уже хорошо защищает SPDD and Gas Town как deep anchors. Но при этом остаётся другой риск: важные методологии могут быть “учтены” в плане, но фактически получить одну расплывчатую подглаву на несколько страниц.

Для текущей задачи это неприемлемо. Теоретическая часть работает не только как публикационный текст, но и как учебный материал для владельца проекта. Поэтому ключевые методологии должны быть раскрыты настолько, чтобы после чтения было понятно:

- какую проблему решает методология;
- как устроен её workflow;
- какие артефакты она создаёт;
- где она хранит контекст;
- где остаётся человеческое решение;
- как проверяется результат;
- где методология сильна;
- где она опасна, чрезмерна or слаба;
- чем она отличается от соседних подходов.

## 2. Две независимые оси

Начиная с этого решения, нельзя смешивать две оси:

```text
роль в архитектуре теории ≠ глубина изложения
```

### 2.1. Роль в архитектуре

- deep anchor;
- protected methodology profile;
- comparative support;
- short mention;
- source-map-only.

### 2.2. Глубина изложения

- full methodology profile;
- compact profile;
- short contrast;
- note only.

SPDD остаётся **deep anchor + full methodology profile**.  
Gas Town остаётся **deep anchor** as organizational/operational environment case.  
Spec Kit, Kiro, Constitutional SDD, TDAD, GSD and BMAD получают статус **protected methodology profile**.

## 3. Protected methodology profiles

Protected methodology profile — это не deep anchor, но protected depth. Такой материал нельзя сжать до обзорной подглавы.

Статус protected methodology profile получают:

```text
Spec Kit
Kiro Specs
Constitutional SDD
TDAD: Test-Driven AI Agent Definition
TDAD: Test-Driven Agentic Development
GSD / Open GSD
BMAD Method
```

### 3.1. Минимальная структура protected methodology profile

Для каждой методологии должны быть раскрыты:

1. Проблема, которую она решает.
2. Базовый workflow.
3. Артефакты, которые она создаёт.
4. Где живёт контекст.
5. Какие роли, участники or агенты предполагаются.
6. Где human gate / человеческое подтверждение.
7. Как проверяется результат.
8. Какой хвост lifecycle остаётся.
9. Где методология сильна.
10. Где она опасна, чрезмерна or слаба.
11. Чем она отличается от соседних подходов.
12. Что из неё полезно для нашей теории / Handbook / Fieldbook.

Если эти пункты не раскрыты хотя бы кратко, профиль считается незавершённым.

## 4. Обязательные comparative syntheses

Описание отдельных методологий необходимо, но недостаточно. Финальная теория должна содержать сравнительные синтезы, потому что именно они создают собственную ценность, а не просто пересказывают источники.

Обязательные comparative syntheses:

### 4.1. Specification methods comparative synthesis

Сравнить:

```text
SPDD
Spec Kit
Kiro
TDAD
Constitutional SDD
```

Главный вопрос:

```text
Каким способом намерение становится управляемым артефактом?
```

### 4.2. Process methods comparative synthesis

Сравнить:

```text
Spec Kit
GSD
BMAD
Reversa / OpenSpec / AgentSPEX
Gas Town
```

Главный вопрос:

```text
Когда процесс сам становится артефактом?
```

### 4.3. Evidence methods comparative synthesis

Сравнить:

```text
TDAD
contract tests
architecture fitness functions
test data / oracle independence
agent trace
```

Главный вопрос:

```text
Что именно считается доказательством для разных типов изменений?
```

### 4.4. Completion/governance comparative synthesis

Сравнить:

```text
SASE
open-source AI policy cluster
CODEOWNERS / ownership map
audit/provenance record
```

Главный вопрос:

```text
Почему способность агента действовать не равна праву завершить изменение?
```

## 5. Compression rules

Protected methodology profile нельзя:

- сводить к одному абзацу;
- описывать только через лозунг;
- раскрывать только через список команд;
- использовать как “ещё один пример” без workflow;
- упоминать без failure modes;
- ставить в один ряд с source-map-only материалами;
- переносить в Handbook до того, как теория дала conceptual reconstruction.

Сокращение возможно только после human gate and only if profile dossier shows what is intentionally moved out.

## 6. Dossier requirement

Перед writing защищённых методологических блоков нужно создать dossiers:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
```

Эти dossiers должны читать primary sources, not only prior summaries.

## 7. Relationship to deep anchors

SPDD and Gas Town are not demoted.

- SPDD stays Part IV and remains benchmark depth.
- Gas Town stays Part IX and remains organizational deep case.
- Protected methodology profiles enrich Parts V and VII.
- Comparative syntheses may become the most valuable parts of the text, but they do not replace deep anchors.

## 8. Skeleton implication

Skeleton v4 must be updated:

- Part V becomes a protected specification-methods block.
- Part VII becomes a protected process-methods block.
- Comparative sections become mandatory, not optional.
- The “one subsection / three pages / vague summary” outcome is explicitly forbidden.

## 9. Human gates

Human approval required before:

1. Demoting any protected methodology profile to short mention.
2. Removing any required profile element.
3. Merging GSD/BMAD into one shallow paragraph.
4. Treating Spec Kit/Kiro/Constitutional SDD/TDAD as mere contrasts to SPDD.
5. Starting writing Part V or Part VII without methodology dossiers.
