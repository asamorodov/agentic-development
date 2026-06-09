import path from "node:path";
import { existsSync } from "node:fs";
import { mkdir, stat } from "node:fs/promises";

export function padPass(passNumber: number): string {
  return String(passNumber).padStart(2, "0");
}

export function safeDocName(docPath: string): string {
  const parsed = path.parse(docPath);
  const base = parsed.name || parsed.base || "document";

  return base
    .normalize("NFKD")
    .replace(/[^\p{L}\p{N}_-]+/gu, "_")
    .replace(/_+/g, "_")
    .replace(/^_+|_+$/g, "") || "document";
}

export function findRepoRootSync(startDir: string): string {
  let current = path.resolve(startDir);

  while (true) {
    if (existsSync(path.join(current, ".git"))) return current;
    if (existsSync(path.join(current, "project", "repository-structure.md")) && existsSync(path.join(current, "work"))) return current;

    const parent = path.dirname(current);
    if (parent === current) {
      throw new Error(`Cannot find repository root from ${startDir}. Pass --repo-root explicitly.`);
    }
    current = parent;
  }
}

export function resolveInsideRepo(repoRoot: string, userPath: string): string {
  const resolvedRoot = path.resolve(repoRoot);
  const resolvedPath = path.isAbsolute(userPath) ? path.resolve(userPath) : path.resolve(resolvedRoot, userPath);
  const relative = path.relative(resolvedRoot, resolvedPath);
  if (relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error(`Path is outside repo root: ${userPath}`);
  }
  return resolvedPath;
}

export function toRepoRelative(repoRoot: string, absolutePath: string): string {
  return path.relative(path.resolve(repoRoot), path.resolve(absolutePath)).replaceAll(path.sep, "/");
}

export function toPortableAbsolute(absolutePath: string): string {
  return path.resolve(absolutePath).replaceAll(path.sep, "/");
}

export async function ensureDir(dirPath: string): Promise<void> {
  await mkdir(dirPath, { recursive: true });
}

export async function exists(filePath: string): Promise<boolean> {
  try {
    await stat(filePath);
    return true;
  } catch {
    return false;
  }
}

export function passArtifactPaths(repoRoot: string, docPath: string, passNumber: number) {
  const safeName = safeDocName(docPath);
  const pass = padPass(passNumber);
  const dir = path.join(repoRoot, "passes", safeName);
  return {
    safeName,
    pass,
    dir,
    afterPass: path.join(dir, `${safeName}_after_pass_${pass}.md`),
    delta: path.join(dir, `${safeName}_delta_${pass}.md`),
    shouldStop: path.join(dir, `${safeName}_should_stop_${pass}.txt`)
  };
}
