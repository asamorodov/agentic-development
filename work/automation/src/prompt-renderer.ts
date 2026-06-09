import { readFile } from "node:fs/promises";
import path from "node:path";
import { passArtifactPaths, toPortableAbsolute, toRepoRelative } from "./path-utils.js";

export interface PromptInput {
  repoRoot: string;
  promptPath: string;
  docPath: string;
  topic: string;
  passNumber: number;
  runId: string;
  workerId: string;
}

export async function renderPassPrompt(input: PromptInput): Promise<string> {
  const promptAbs = path.resolve(input.repoRoot, input.promptPath);
  const docAbs = path.resolve(input.repoRoot, input.docPath);
  const promptText = await readFile(promptAbs, "utf8");
  const artifacts = passArtifactPaths(input.repoRoot, input.docPath, input.passNumber);
  const docRel = toRepoRelative(input.repoRoot, docAbs);
  const promptRel = toRepoRelative(input.repoRoot, promptAbs);
  const passDirRel = toRepoRelative(input.repoRoot, artifacts.dir);

  return `# Вход одного запуска

{корень репозитория}: ${toPortableAbsolute(input.repoRoot)}
{имя документа}: ${docRel}
{абсолютный путь документа}: ${toPortableAbsolute(docAbs)}
{номер прохода}: ${artifacts.pass}
{тема}: ${input.topic}
{используемый prompt}: ${promptRel}
{run_id}: ${input.runId}
{worker_id}: ${input.workerId}

# Критический контракт путей

Все относительные пути в этом prompt отсчитываются от корня репозитория:

\`\`\`text
${toPortableAbsolute(input.repoRoot)}
\`\`\`

Не отсчитывай пути от \`work/automation\` or текущего каталога процесса.

Если создаёшь or изменяешь файлы, используй repo-relative path exactly as written or the absolute path shown below. Do not create duplicated paths such as \`work/automation/work/automation/...\` or \`work/automation/passes/...\`.

# Обязательные артефакты этого прохода

Сохрани артефакты именно здесь, внутри корня репозитория:

\`\`\`text
${toRepoRelative(input.repoRoot, artifacts.afterPass)}
${toRepoRelative(input.repoRoot, artifacts.delta)}
${toRepoRelative(input.repoRoot, artifacts.shouldStop)}
\`\`\`

Абсолютные пути тех же артефактов:

\`\`\`text
${toPortableAbsolute(artifacts.afterPass)}
${toPortableAbsolute(artifacts.delta)}
${toPortableAbsolute(artifacts.shouldStop)}
\`\`\`

Каталог артефактов прохода:

\`\`\`text
${passDirRel}
${toPortableAbsolute(artifacts.dir)}
\`\`\`

# Границы записи

Работай только с документом \`${docRel}\`, его pass-артефактами и временными файлами/заметками, если они прямо нужны для этого документа.

Не редактируй:

\`\`\`text
work/discourse.md
work/CHECKS.json
work/APPLY_NOTES.md
общие отчёты
общие source maps
документы других тем
\`\`\`

Если основной prompt требует общий отчёт, не создавай его в этом worker-запуске. Вместо этого запиши короткую заметку в delta текущего прохода.

# Основной prompt

${promptText}
`;
}
