# Протокол переноса между ChatGPT и Codex

Этот протокол используется, когда результат обсуждения в ChatGPT нужно передать Codex, но ChatGPT не записывает изменения прямо в репозиторий.

Если ChatGPT имеет доступ на запись в GitHub-репозиторий и пользователь разрешил запись, предпочтительный путь — не создавать отдельный import packet, а обновить нужные файлы напрямую по `protocols/rules/chat-github-repo-work-protocol.md`.

## Когда применять

Используйте этот протокол, если:

- у ChatGPT нет write access к репозиторию;
- пользователь хочет сначала получить переносимый patch;
- обсуждение происходит в среде, которая не может коммитить в GitHub;
- нужно передать Codex результат внешнего разговора.

## Что переносить

Перенос должен быть не transcript and not summary, а применимый результат:

- фрагмент для добавления в `work/discourse.md`;
- список решений, которые нужно применить;
- файлы, которые нужно создать или обновить;
- human gates;
- точный Codex task prompt;
- открытые вопросы.

## Связь с дискурсом

Фрагмент для `work/discourse.md` должен соответствовать `protocols/rules/discourse-maintenance-rules.md`: однородный дискурс по поворотам разговора, без служебных status-блоков, с именами файлов внутри текста.

## Codex import

Codex, получив такой transfer packet, должен:

1. Прочитать `AGENTS.md`.
2. Прочитать `protocols/rules/codex-task-work-protocol.md`.
3. Прочитать `protocols/rules/discourse-maintenance-rules.md`.
4. Прочитать текущий `work/discourse.md` and relevant `/work` files.
5. Сопоставить transfer packet с текущим дискурсом and source precedence.
6. Если есть конфликт — остановиться и описать его.
7. Если конфликта нет — применить изменения к файлам репозитория.
8. Обновить `work/discourse.md` как часть результата.

## Что не делать

Не считать transfer packet новым source of truth после применения. После применения актуальное состояние должно быть в файлах репозитория, прежде всего в `work/discourse.md` and relevant project/protocol files.
