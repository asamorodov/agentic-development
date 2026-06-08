import { readFile } from "node:fs/promises";
import path from "node:path";
import { passArtifactPaths, toRepoRelative } from "./path-utils.js";

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
  const promptText = await readFile(promptAbs, "utf8");
  const artifacts = passArtifactPaths(input.repoRoot, input.docPath, input.passNumber);
  const docRel = toRepoRelative(input.repoRoot, path.resolve(input.repoRoot, input.docPath));
  const promptRel = toRepoRelative(input.repoRoot, promptAbs);
  const passDirRel = toRepoRelative(input.repoRoot, artifacts.dir);

  return `# Вход одного запуска

{имя документа}: ${docRel}
{номер прохода}: ${artifacts.pass}
{тема}: ${input.topic}
{используемый prompt}: ${promptRel}
{run_id}: ${input.runId}
{worker_id}: ${input.workerId}

# Обязательные артефакты этого прохода

Сохрани артефакты именно здесь:

\`\`\`text
${toRepoRelative(input.repoRoot, artifacts.afterPass)}
${toRepoRelative(input.repoRoot, artifacts.delta)}
${toRepoRelative(input.repoRoot, artifacts.shouldStop)}
\`\`\`

Каталог артефактов прохода:

\`\`\`text
${passDirRel}
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
