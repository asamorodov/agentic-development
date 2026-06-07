# Агентская разработка как проектирование рабочей среды
## 1. Зачем нужна отдельная теоретическая часть
# Часть I. От удачного запроса к рабочей среде
## 2. Модель стала достаточно сильной, чтобы проблема переместилась наружу
## 3. Агент как петля, а не одноразовый ответ
## 4. “Агент = модель + обвязка” — полезная, но неполная формула
## 5. Хороший запрос больше не является единицей управления процессом
## 6. Инструментальные поверхности: что интерфейс делает видимым и что прячет {#tool-surfaces}
# Часть II. Контекст и намерение
## 7. Контекст — не окно, а рабочее состояние {#6-kontekst-ne-okno-a-rabochee-sostoyanie}
## 8. Контекстные интерфейсы: кто решает, что загрузить {#7-kontekstnye-interfeysy-kto-reshaet-chto-zagruzit}
## 9. Кодовая база как контекстный интерфейс {#8-kodovaya-baza-kak-kontekstnyy-interfeys}
## 10. Долговременный контекст, спецификация и передача состояния — разные вещи {#9-dolgovremennyy-kontekst-spetsifikatsiya-i-peredacha-sostoyaniya-raznye-veschi}
## 11. Артефакт намерения: prompt как delivery artifact {#10-artefakt-namereniya-spdd-spetsifikatsiya-i-proverka-samoy-tseli}
## 12. Что SPDD добавляет к SDD и почему это не просто spec-first {#spdd-adds-to-sdd}
## 13. Шесть стадий SPDD: распределённое подтверждение намерения {#spdd-six-step-workflow}
## 14. Story shaping: сырое требование ещё не является входом для Canvas {#spdd-story-shaping}
## 15. Analysis context: strategic clarity до implementation detail {#spdd-analysis-context}
## 16. REASONS Canvas: intent, design, execution, governance {#spdd-reasons-canvas-intent-design-execution-governance}
## 17. Три core skills SPDD: Abstraction First, Alignment, Iterative Review {#spdd-three-core-skills}
## 18. Generate code: модель реализует locked intent, а не ищет решение заново {#spdd-generate-locked-intent}
## 19. Проверяемые свидетельства: API tests до глубокого code review {#spdd-validation-review-evidence}
## 20. Logic correction, prompt-update и sync: два направления обратной связи {#spdd-prompt-update-sync}
## 21. Unit tests: последний safety net, а не первый источник смысла {#spdd-unit-tests-after-stabilization}
## 22. Asset integrity: prompt version должен соответствовать code commit {#spdd-asset-integrity}
## 23. Где SPDD окупается: ROI, upfront cost и fit table {#spdd-fit-and-roi}
## 24. Hotfixes и production signal: governance можно отложить, но нельзя выбросить {#spdd-hotfix-production-signal}
## 25. Roadmap SPDD: от expert craft к organization-level asset system {#spdd-roadmap-decision-memory}
## 26. Сопротивление SPDD: variance, model drift, spec-as-source и предел человеческого суждения {#spdd-resistance-boundaries-and-spec-as-source}
# Часть III. Обвязка и проверка
## 27. Обвязка регулирует не “модель вообще”, а конкретное состояние кодовой базы {#11-obvyazka-reguliruet-ne-model-voobsche-a-konkretnoe-sostoyanie-kodovoy-bazy}
## 28. Направляющие и датчики {#12-napravlyayuschie-i-datchiki}
## 29. Качество надо держать левее {#13-kachestvo-nado-derzhat-levee}
## 30. Поддерживаемость, архитектура и поведение проверяются по-разному {#14-podderzhivaemost-arhitektura-i-povedenie-proveryayutsya-po-raznomu}
## 31. Пригодность проекта к обвязке {#15-prigodnost-proekta-k-obvyazke}
## 32. Среда сама подталкивает агента к правильному {#16-sreda-sama-podtalkivaet-agenta-k-pravilnomu}
## 33. Шаблоны и топологии: уменьшение разнообразия как способ контроля {#17-shablony-i-topologii-umenshenie-raznoobraziya-kak-sposob-kontrolya}
## 34. Навыки, хуки и подагенты {#18-navyki-huki-i-podagenty}
# Часть IV. Среда выполнения и память задачи
## 35. Агенту нужен не только чат, но и среда выполнения {#19-agentu-nuzhen-ne-tolko-chat-no-i-sreda-vypolneniya}
## 36. Поток работы как объект {#20-potok-raboty-kak-obekt}
## 37. Подтверждение как граница ответственности {#21-podtverzhdenie-kak-granitsa-otvetstvennosti}
## 38. Долгоживущая задача требует восстановления, а не только памяти {#22-dolgozhivuschaya-zadacha-trebuet-vosstanovleniya-a-ne-tolko-pamyati}
## 39. Большая часть сложности агентской системы находится не в модели {#23-bolshaya-chast-slozhnosti-agentskoy-sistemy-nahoditsya-ne-v-modeli}
## 40. Граф задач как внешняя память агента {#24-graf-zadach-kak-vneshnyaya-pamyat-agenta}
# Часть V. Gas Town как отдельный разбор агентской организации
## 41. Почему Gas Town заслуживает отдельного раздела {#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela}
## 42. Роли: не персонажи, а организационные функции {#26-roli-ne-personazhi-a-organizatsionnye-funktsii}
## 43. Mayor: видимость без чтения {#27-mayor-vidimost-bez-chteniya}
## 44. Агент — не сессия {#28-agent-ne-sessiya}
## 45. Beads как слой данных, слой управления и слой “почему” {#29-beads-kak-sloy-dannyh-sloy-upravleniya-i-sloy-pochemu}
## 46. GUPP, хуки, molecules и wisps: работа как цепочка устойчивых действий {#30-gupp-huki-molecules-i-wisps-rabota-kak-tsepochka-ustoychivyh-deystviy}
## 47. Refinery, Witness, Deacon: обслуживающие агенты {#31-refinery-witness-deacon-obsluzhivayuschie-agenty}
## 48. Цена Gas Town: пропускная способность против понимания {#32-tsena-gas-town-propusknaya-sposobnost-protiv-ponimaniya}
## 49. От Gas Town к платформенным примитивам {#33-ot-gas-town-k-platformennym-primitivam}
# Часть VI. Проверка и свидетельства
## 50. Агенту нельзя верить на слово, но и человека нельзя превращать в ручной линтер {#34-agentu-nelzya-verit-na-slovo-no-i-cheloveka-nelzya-prevraschat-v-ruchnoy-lint}
## 51. Надёжность вывода: почему уверенность агента не равна правоте {#output-reliability}
### Что доказывают зелёные тесты
### Как отличать найденный баг от бага, созданного тестом
### Надёжность вывода и внешний контекст
### Когда выводу можно доверять достаточно
## 52. Доказательство работы зависит от типа задачи {#35-dokazatelstvo-raboty-zavisit-ot-tipa-zadachi}
## 53. Поведенческая проверка остаётся слабым местом {#36-povedencheskaya-proverka-ostaetsya-slabym-mestom}
## 54. Логирование и наблюдаемость нельзя оставлять текстовой просьбе {#37-logirovanie-i-nablyudaemost-nelzya-ostavlyat-tekstovoy-prosbe}
## 55. Комментарии ревью — это сигналы, а не команды {#38-kommentarii-revyu-eto-signaly-a-ne-komandy}
## 56. Свидетельства должны быть пригодны для следующего шага {#39-svidetelstva-dolzhny-byt-prigodny-dlya-sleduyuschego-shaga}
## 57. Эмпирические предупреждения: скорость генерации не равна качеству {#40-empiricheskie-preduprezhdeniya-skorost-generatsii-ne-ravna-kachestvu}
# Часть VII. Ответственность, человек и границы автономии
## 58. `Human in the loop` слишком слабая формула {#41-human-in-the-loop-slishkom-slabaya-formula}
## 59. Человеческое внимание нужно ставить в точки максимального рычага {#42-chelovecheskoe-vnimanie-nuzhno-stavit-v-tochki-maksimalnogo-rychaga}
## 60. Человек остаётся владельцем того, что нельзя свести к датчику {#43-chelovek-ostaetsya-vladeltsem-togo-chto-nelzya-svesti-k-datchiku}
## 61. Агентский маховик: агент помогает улучшать среду, но не должен владеть ею {#44-agentskiy-mahovik-agent-pomogaet-uluchshat-sredu-no-ne-dolzhen-vladet-eyu}
## 62. Автономия — не свойство модели, а договор с окружением {#45-avtonomiya-ne-svoystvo-modeli-a-dogovor-s-okruzheniem}
## 63. Область действия и чрезмерная инициативность {#46-oblast-deystviya-i-chrezmernaya-initsiativnost}
## 64. Песочница, права и рабочие деревья решают разные задачи {#47-pesochnitsa-prava-i-rabochie-derevya-reshayut-raznye-zadachi}
## 65. MCP как расширение границы доверия {#48-mcp-kak-rasshirenie-granitsy-doveriya}
## 66. Риск не только технический {#49-risk-ne-tolko-tehnicheskiy}
# Часть VIII. Ближайший год и вывод для Handbook
## 67. Ближайший год будет не про исчезновение разработчика {#50-blizhayshiy-god-budet-ne-pro-ischeznovenie-razrabotchika}
## 68. Эмпирическая оговорка: агент ускоряет не любую систему {#ai-does-not-accelerate-every-system}
## 69. Что уже работает, что вероятно усилится, а что пока рано нормировать {#51-chto-uzhe-rabotaet-chto-veroyatno-usilitsya-a-chto-poka-rano-normirovat}
## 70. Практический Handbook должен стать картой выбора режима {#52-prakticheskiy-handbook-dolzhen-stat-kartoy-vybora-rezhima}
## 71. Итоговая рамка {#53-itogovaya-ramka}
## Карта источников {#54-karta-istochnikov}
### Основные теоретические источники
### Agent-first / agent-loop / context engineering
### Skills, subagents and agent system architecture
### Gas Town / Beads / многоагентная рабочая среда
### Безопасность, область действия и наблюдаемость
### Эмпирические предупреждения и организационный слой
