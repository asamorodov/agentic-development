# IX. Fragment usage

| Fragment | Использование | Решение |
|---|---|---|
| A6 execution environment distinctions | Стал базой для различения места действия, инструментальной поверхности, runtime and platform substrate. | В P14 материал переплавлен в главную ось, а не перенесён как список четырёх слоёв. |
| C4 execution runtime to PWG | Использован в разделе 5 and 7: runtime state does not equal work state; след запуска требует claim/gate/PWG. | Сохранить как финальный мост; не разворачивать C4 внутрь IX полностью. |
| 00 spine map | Поддерживает lifecycle framing: execution is middle layer between intent and evidence/acceptance. | Оставлен как фон; без прямой ссылки. |
| A6 degradation/duplication audit | Помог не сделать IX копией A6. | Структурная правка P14 уменьшила риск повтора A6. |
| C4 degradation/duplication audit | Помог удержать границу runtime vs work state. | Финальная часть P14 всё ещё близка к C4; нужна осторожность в будущей редакции. |
